#!/usr/bin/env bash
# ==============================================================================
# SCRIPT MAESTRO DE HOSTING OBSIDIAN EN RASPBERRY PI 4
# Bóveda: Oposiciones Técnicos Auxiliares de Informática (TAI - AGE)
# ==============================================================================

set -e

echo "======================================================================"
echo "🍓 CONFIGURANDO SERVIDOR MAESTRO DE OBSIDIAN EN RASPBERRY PI"
echo "======================================================================"

# 1. Instalar utilidades del sistema
echo "[1/6] Verificando dependencias base (git, curl, cron, jq)..."
sudo apt-get update -qq
sudo apt-get install -y -qq git curl cron jq

# 2. Instalar Docker y Docker Compose si no existen
if ! command -v docker &> /dev/null; then
    echo "[2/6] Instalando Docker Engine..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker "$USER"
    rm -f get-docker.sh
else
    echo "[2/6] Docker ya está instalado."
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "[*] Instalando Docker Compose plugin..."
    sudo apt-get install -y -qq docker-compose-plugin || sudo apt-get install -y -qq docker-compose
fi

# 3. Instalar y configurar Tailscale para acceso remoto privado
if ! command -v tailscale &> /dev/null; then
    echo "[3/6] Instalando Tailscale para acceso remoto 4G/5G..."
    curl -fsSL https://tailscale.com/install.sh | sh
fi

# 4. Crear directorio del servidor y clonar/actualizar la bóveda
echo "[4/6] Descargando y sincronizando la Bóveda de Oposiciones TAI..."
DEPLOY_DIR="$HOME/obsidian-tai-server"
mkdir -p "$DEPLOY_DIR/config"
cd "$DEPLOY_DIR"

if [ -d "vault/.git" ]; then
    echo "[*] Actualizando bóveda existente a la última versión de GitHub..."
    cd vault
    git fetch origin main
    git reset --hard origin/main
    cd ..
else
    echo "[*] Clonando repositorio oficial desde GitHub..."
    rm -rf vault
    git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git vault
fi

# 5. Generar archivo docker-compose.yml optimizado para Raspberry Pi ARM64
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
    volumes:
      - ./config:/config
      - ./vault:/vaults/OPOSICIONES-TAI
    ports:
      - 3000:3000
      - 3001:3001
    shm_size: "1gb"
    restart: unless-stopped
EOF

# 6. Crear script de auto-actualización periódica (cada 5 minutos)
cat << 'EOF' > update-vault.sh
#!/usr/bin/env bash
DEPLOY_DIR="$HOME/obsidian-tai-server"
if [ -d "$DEPLOY_DIR/vault/.git" ]; then
    cd "$DEPLOY_DIR/vault"
    git fetch origin main > /dev/null 2>&1
    LOCAL_HASH=$(git rev-parse HEAD)
    REMOTE_HASH=$(git rev-parse origin/main)

    if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Nuevos tests y notas detectados en GitHub. Sincronizando..."
        git reset --hard origin/main
        cp docker-compose.yml "$DEPLOY_DIR/docker-compose.yml" 2>/dev/null || true
    fi
fi
EOF
chmod +x update-vault.sh

# Configurar Cron para auto-actualización
echo "[5/6] Configurando sincronización automática con GitHub..."
CRON_JOB="*/5 * * * * $DEPLOY_DIR/update-vault.sh >> $DEPLOY_DIR/sync.log 2>&1"
(crontab -l 2>/dev/null | grep -v "obsidian-tai-server/update-vault.sh" ; echo "$CRON_JOB") | crontab -

# 7. Levantar el contenedor Docker
echo "[6/6] Iniciando contenedor de Obsidian Server..."
if docker compose version &> /dev/null; then
    docker compose down 2>/dev/null || true
    docker compose up -d
else
    docker-compose down 2>/dev/null || true
    docker-compose up -d
fi

# 8. Obtener IPs de acceso
LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "192.168.1.226")
TAILSCALE_IP=$(tailscale ip -4 2>/dev/null || echo "")

echo ""
echo "======================================================================"
echo "🎉 ¡SERVIDOR OBSIDIAN DESPLEGADO CON ÉXITO EN TU RASPBERRY PI!"
echo "======================================================================"
echo ""
echo "🌐 1. ACCESO EN TU RED LOCAL (WiFi de casa):"
echo "   👉 http://${LOCAL_IP}:3000"
echo ""
if [ -n "$TAILSCALE_IP" ]; then
echo "🛡️ 2. ACCESO REMOTO SEGURO DESDE FUERA DE CASA (4G/5G con Tailscale):"
echo "   👉 http://${TAILSCALE_IP}:3000"
else
echo "🛡️ 2. ACCESO REMOTO DESDE CUALQUIER LUGAR (Tailscale):"
echo "   Para activar el acceso remoto privado, ejecuta:"
echo "   👉 sudo tailscale up"
fi
echo ""
echo "📌 PRIMERA VEZ AL ABRIR EL NAVEGADOR:"
echo "   1. Haz clic en 'Open folder as vault'"
echo "   2. Selecciona la carpeta: /vaults/OPOSICIONES-TAI"
echo ""
echo "🔄 AUTO-ACTUALIZACIÓN: ACTIVADA (revisa GitHub cada 5 minutos automáticamente)."
echo "⚡ Para forzar actualización manual: bash ~/obsidian-tai-server/update-vault.sh"
echo "======================================================================"
