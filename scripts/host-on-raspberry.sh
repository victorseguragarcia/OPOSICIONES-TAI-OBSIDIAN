#!/usr/bin/env bash
# ==============================================================================
# SCRIPT MAESTRO DE HOSTING OBSIDIAN EN RASPBERRY PI 4 (AUTO-APERTURA DIRECTA)
# ==============================================================================

set -e

echo "======================================================================"
echo "🍓 CONFIGURANDO SERVIDOR MAESTRO DE OBSIDIAN EN RASPBERRY PI"
echo "======================================================================"

DEPLOY_DIR="$HOME/obsidian-tai-server"
mkdir -p "$DEPLOY_DIR/config/.config/obsidian"
cd "$DEPLOY_DIR"

# 1. Clonar o actualizar la bóveda de GitHub
if [ -d "vault/.git" ]; then
    echo "[1/4] Actualizando bóveda desde GitHub..."
    cd vault
    git fetch origin main
    git reset --hard origin/main
    cd ..
else
    echo "[1/4] Clonando repositorio oficial de GitHub..."
    rm -rf vault
    git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git vault
fi

# 2. Configurar auto-apertura directa de la bóveda (sin necesidad de buscar carpetas)
echo "[2/4] Preconfigurando apertura automática de la Bóveda TAI..."
VAULT_HASH=$(echo -n "/vaults/OPOSICIONES-TAI" | md5sum | awk '{print $1}')
cat << EOF > "$DEPLOY_DIR/config/.config/obsidian/obsidian.json"
{
  "vaults": {
    "${VAULT_HASH}": {
      "path": "/vaults/OPOSICIONES-TAI",
      "ts": $(date +%s%3N),
      "open": true
    }
  }
}
EOF

# 3. Archivo docker-compose.yml
echo "[3/4] Configurando Docker Compose..."
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

# 4. Script de actualización automática en Cron
cat << 'EOF' > update-vault.sh
#!/usr/bin/env bash
DEPLOY_DIR="$HOME/obsidian-tai-server"
if [ -d "$DEPLOY_DIR/vault/.git" ]; then
    cd "$DEPLOY_DIR/vault"
    git fetch origin main > /dev/null 2>&1
    LOCAL_HASH=$(git rev-parse HEAD)
    REMOTE_HASH=$(git rev-parse origin/main)

    if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sincronizando cambios de GitHub..."
        git reset --hard origin/main
    fi
fi
EOF
chmod +x update-vault.sh

CRON_JOB="*/5 * * * * $DEPLOY_DIR/update-vault.sh >> $DEPLOY_DIR/sync.log 2>&1"
(crontab -l 2>/dev/null | grep -v "obsidian-tai-server/update-vault.sh" ; echo "$CRON_JOB") | crontab -

# 5. Reiniciar contenedor
echo "[4/4] Reiniciando contenedor de Obsidian..."
if docker compose version &> /dev/null; then
    docker compose down 2>/dev/null || true
    docker compose up -d
else
    docker-compose down 2>/dev/null || true
    docker-compose up -d
fi

LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "127.0.0.1")
TAILSCALE_IP=$(tailscale ip -4 2>/dev/null || echo "")

echo ""
echo "======================================================================"
echo "🎉 ¡CONFIGURACIÓN COMPLETADA!"
echo "======================================================================"
echo "La Bóveda TAI ahora se abre AUTOMÁTICAMENTE al entrar a la web."
echo ""
echo "👉 Entra a: https://${LOCAL_IP}:3001"
if [ -n "$TAILSCALE_IP" ]; then
echo "👉 O con Tailscale: https://${TAILSCALE_IP}:3001"
fi
echo "======================================================================"
