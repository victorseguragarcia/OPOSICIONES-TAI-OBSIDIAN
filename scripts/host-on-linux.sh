#!/usr/bin/env bash
# ==============================================================================
# SCRIPT UNIVERSAL DE DESPLIEGUE OBSIDIAN SERVER EN LINUX (Cualquier Distro)
# Compatible con: Ubuntu, Debian, Raspberry Pi OS, Fedora, RHEL, Arch, openSUSE
# Arquitecturas soportadas: x86_64 / amd64, aarch64 / arm64, armv7l
# ==============================================================================

set -e

echo "======================================================================"
echo "🐧 INSTALADOR UNIVERSAL DE OBSIDIAN SERVER EN LINUX"
echo "   Bóveda: Oposiciones Técnicos Auxiliares de Informática (TAI - AGE)"
echo "======================================================================"

# 1. Detectar gestor de paquetes e instalar dependencias básicas
echo "[1/5] Detectando distribución Linux e instalando herramientas base..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update -qq
    sudo apt-get install -y -qq git curl cron jq ca-certificates
elif command -v dnf &> /dev/null; then
    sudo dnf install -y git curl cronie jq ca-certificates
    sudo systemctl enable --now crond 2>/dev/null || true
elif command -v pacman &> /dev/null; then
    sudo pacman -Sy --noconfirm git curl cronie jq ca-certificates
    sudo systemctl enable --now cronie 2>/dev/null || true
elif command -v zypper &> /dev/null; then
    sudo zypper install -y git curl cron jq ca-certificates
fi

# 2. Instalar Docker y Docker Compose si no están presentes
echo "[2/5] Verificando Docker Engine..."
if ! command -v docker &> /dev/null; then
    echo "[*] Instalando Docker mediante instalador oficial universal..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker "$USER" 2>/dev/null || true
    rm -f get-docker.sh
fi

# 3. Descargar/Actualizar la bóveda desde GitHub
echo "[3/5] Sincronizando Bóveda oficial de Oposiciones TAI..."
DEPLOY_DIR="$HOME/obsidian-tai-server"
mkdir -p "$DEPLOY_DIR/config/.config/obsidian"
cd "$DEPLOY_DIR"

if [ -d "vault/.git" ]; then
    echo "[*] Actualizando repositorio existente a la última versión..."
    cd vault
    git fetch origin main
    git reset --hard origin/main
    cd ..
else
    echo "[*] Clonando repositorio desde GitHub..."
    rm -rf vault
    git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git vault
fi

# 4. Preconfigurar apertura automática de la Bóveda en Obsidian
echo "[4/5] Preconfigurando apertura automática de la Bóveda..."
VAULT_HASH=$(echo -n "/vaults/OPOSICIONES-TAI" | md5sum | awk '{print $1}')
cat << EOF > "$DEPLOY_DIR/config/.config/obsidian/obsidian.json"
{
  "vaults": {
    "${VAULT_HASH}": {
      "path": "/vaults/OPOSICIONES-TAI",
      "ts": $(date +%s%3N 2>/dev/null || date +%s000),
      "open": true
    }
  }
}
EOF

# 5. Generar archivo docker-compose.yml
cat << 'EOF' > docker-compose.yml
version: "3.8"

services:
  obsidian-remote:
    image: lscr.io/linuxserver/obsidian:latest
    container_name: obsidian-tai-server
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Madrid
      - TITLE=Boveda Oposiciones TAI (AGE)
      - CUSTOM_PORT=3000
      - CUSTOM_HTTPS_PORT=3001
    volumes:
      - ./config:/config
      - ./vault:/vaults/OPOSICIONES-TAI
    ports:
      - 3000:3000
      - 3001:3001
    shm_size: "1gb"
    restart: unless-stopped
EOF

# 6. Configurar script de actualización periódica (Cron)
cat << 'EOF' > update-vault.sh
#!/usr/bin/env bash
DEPLOY_DIR="$HOME/obsidian-tai-server"
if [ -d "$DEPLOY_DIR/vault/.git" ]; then
    cd "$DEPLOY_DIR/vault"
    git fetch origin main > /dev/null 2>&1
    LOCAL_HASH=$(git rev-parse HEAD)
    REMOTE_HASH=$(git rev-parse origin/main)

    if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sincronizando nuevos cambios desde GitHub..."
        git reset --hard origin/main
    fi
fi
EOF
chmod +x update-vault.sh

CRON_JOB="*/5 * * * * $DEPLOY_DIR/update-vault.sh >> $DEPLOY_DIR/sync.log 2>&1"
(crontab -l 2>/dev/null | grep -v "obsidian-tai-server/update-vault.sh" ; echo "$CRON_JOB") | crontab - 2>/dev/null || true

# 7. Levantar contenedor Docker
echo "[5/5] Levantando contenedor de Obsidian..."
if docker compose version &> /dev/null; then
    docker compose down 2>/dev/null || true
    docker compose up -d
elif command -v docker-compose &> /dev/null; then
    docker-compose down 2>/dev/null || true
    docker-compose up -d
else
    docker run -d \
      --name obsidian-tai-server \
      --restart unless-stopped \
      -e PUID=1000 \
      -e PGID=1000 \
      -e TZ=Europe/Madrid \
      -e TITLE="Boveda Oposiciones TAI (AGE)" \
      -e CUSTOM_PORT=3000 \
      -e CUSTOM_HTTPS_PORT=3001 \
      -p 3000:3000 \
      -p 3001:3001 \
      --shm-size="1gb" \
      -v "$DEPLOY_DIR/config:/config" \
      -v "$DEPLOY_DIR/vault:/vaults/OPOSICIONES-TAI" \
      lscr.io/linuxserver/obsidian:latest
fi

# 8. Obtener IPs de acceso
LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || ip -4 route get 1.1.1.1 2>/dev/null | awk '{print $7}' || echo "127.0.0.1")
TAILSCALE_IP=$(tailscale ip -4 2>/dev/null || echo "")

echo ""
echo "======================================================================"
echo "🎉 ¡SERVIDOR OBSIDIAN DESPLEGADO CON ÉXITO EN LINUX!"
echo "======================================================================"
echo "La Bóveda TAI se abrirá AUTOMÁTICAMENTE al entrar en el navegador."
echo ""
echo "🌐 1. ACCESO EN RED LOCAL:"
echo "   👉 https://${LOCAL_IP}:3001"
echo ""
if [ -n "$TAILSCALE_IP" ]; then
echo "🛡️ 2. ACCESO REMOTO SEGURO (Tailscale 4G/5G):"
echo "   👉 https://${TAILSCALE_IP}:3001"
else
echo "🛡️ 2. ACCESO REMOTO DESDE FUERA DE CASA:"
echo "   Si usas Tailscale, activa el túnel con: sudo tailscale up"
fi
echo ""
echo "🔄 Auto-Sincronización: ACTIVADA (revisa GitHub cada 5 minutos)."
echo "⚡ Para forzar actualización manual: bash ~/obsidian-tai-server/update-vault.sh"
echo "======================================================================"
