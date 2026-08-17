#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue y Auto-Actualización de Obsidian Server en Raspberry Pi
# Bóveda: Oposiciones Técnicos Auxiliares de Informática (TAI)
# ==============================================================================

set -e

echo "======================================================================"
echo "🚀 INICIANDO INSTALACIÓN, DESPLIEGUE Y AUTO-ACTUALIZACIÓN"
echo "======================================================================"

# 1. Instalar dependencias básicas, Docker y Docker Compose si no existen
if ! command -v git &> /dev/null || ! command -v curl &> /dev/null; then
    echo "[*] Instalando utilidades base (git, curl, cron)..."
    sudo apt-get update && sudo apt-get install -y git curl cron
fi

if ! command -v docker &> /dev/null; then
    echo "[*] Instalando Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker "$USER"
    rm -f get-docker.sh
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "[*] Instalando Docker Compose..."
    sudo apt-get update && sudo apt-get install -y docker-compose-plugin || sudo apt-get install -y docker-compose
fi

# 2. Crear directorio del servidor y clonar/actualizar la bóveda
DEPLOY_DIR="$HOME/obsidian-tai-server"
mkdir -p "$DEPLOY_DIR"
cd "$DEPLOY_DIR"

if [ -d "vault/.git" ]; then
    echo "[*] Actualizando repositorio existente..."
    cd vault
    git fetch origin main
    git reset --hard origin/main
    cd ..
else
    echo "[*] Clonando repositorio de Oposiciones TAI desde GitHub..."
    rm -rf vault
    git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git vault
fi

# 3. Copiar archivo docker-compose.yml
cp vault/docker-compose.yml ./docker-compose.yml

# 4. Crear script de actualización manual y automática (update.sh)
cat << 'EOF' > update.sh
#!/usr/bin/env bash
# Script de actualización automática de la bóveda TAI
DEPLOY_DIR="$HOME/obsidian-tai-server"
if [ -d "$DEPLOY_DIR/vault/.git" ]; then
    cd "$DEPLOY_DIR/vault"
    # Comprobar si hay cambios remotos en GitHub
    git fetch origin main > /dev/null 2>&1
    LOCAL_HASH=$(git rev-parse HEAD)
    REMOTE_HASH=$(git rev-parse origin/main)

    if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Detectados nuevos cambios en GitHub. Actualizando bóveda..."
        git reset --hard origin/main
        cp docker-compose.yml "$DEPLOY_DIR/docker-compose.yml" 2>/dev/null || true
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Bóveda actualizada a commit: $(git rev-parse --short HEAD)"
    fi
fi
EOF
chmod +x update.sh

# 5. Configurar tarea Cron para Auto-Actualización periódica (cada 5 minutos)
echo "[*] Configurando auto-actualización periódica con GitHub (cada 5 minutos)..."
CRON_CMD="$DEPLOY_DIR/update.sh >> $DEPLOY_DIR/auto-update.log 2>&1"
(crontab -l 2>/dev/null | grep -v "obsidian-tai-server/update.sh" ; echo "*/5 * * * * $CRON_CMD") | crontab -

# 6. Levantar el contenedor Docker
echo "[*] Levantando contenedor Docker de Obsidian..."
if docker compose version &> /dev/null; then
    docker compose down 2>/dev/null || true
    docker compose up -d
else
    docker-compose down 2>/dev/null || true
    docker-compose up -d
fi

# 7. Detectar direcciones IP (Local y Tailscale)
LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "127.0.0.1")
TAILSCALE_IP=$(tailscale ip -4 2>/dev/null || echo "")

echo "======================================================================"
echo "✅ SERVIDOR OBSIDIAN DESPLEGADO Y AUTO-SINCRONIZADO"
echo "======================================================================"
echo "🔄 Auto-Actualización: ACTIVADA (revisa GitHub cada 5 minutos automáticamente)"
echo ""
echo "🌐 1. Acceso en tu RED LOCAL (WiFi de casa):"
echo "   👉 http://${LOCAL_IP}:3000   (HTTP)"
echo "   👉 https://${LOCAL_IP}:3001  (HTTPS)"
echo ""
if [ -n "$TAILSCALE_IP" ]; then
echo "🛡️ 2. Acceso REMOTO SEGURO desde cualquier lugar (Tailscale 4G/5G):"
echo "   👉 http://${TAILSCALE_IP}:3000"
echo ""
else
echo "🛡️ 2. Acceso Remoto desde fuera de casa:"
echo "   Para acceder por 4G/5G, instala Tailscale: sudo tailscale up"
echo ""
fi
echo "📌 Primera vez al abrir en el navegador:"
echo "   1. Selecciona 'Open folder as vault'"
echo "   2. Elige la carpeta: /vaults/OPOSICIONES-TAI"
echo ""
echo "⚡ Para forzar una actualización manual en cualquier momento:"
echo "   bash ~/obsidian-tai-server/update.sh"
echo "======================================================================"
