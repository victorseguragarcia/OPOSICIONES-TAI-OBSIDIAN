#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue Automático de Obsidian Server en Raspberry Pi (Docker)
# Bóveda: Oposiciones Técnicos Auxiliares de Informática (TAI)
# ==============================================================================

set -e

echo "======================================================================"
echo "🚀 INICIANDO INSTALACIÓN Y DESPLIEGUE EN RASPBERRY PI"
echo "======================================================================"

# 1. Actualizar repositorios e instalar Docker y Docker Compose si no existen
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
    git pull origin main
    cd ..
else
    echo "[*] Clonando repositorio de Oposiciones TAI..."
    rm -rf vault
    git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git vault
fi

# 3. Descargar o copiar docker-compose.yml
cp vault/docker-compose.yml ./docker-compose.yml

# 4. Levantar el contenedor Docker
echo "[*] Levantando contenedor Docker de Obsidian..."
if docker compose version &> /dev/null; then
    docker compose down || true
    docker compose up -d
else
    docker-compose down || true
    docker-compose up -d
fi

# 5. Obtener IP local
LOCAL_IP=$(hostname -I | awk '{print $1}')

echo "======================================================================"
echo "✅ SERVIDOR OBSIDIAN DESPLEGADO EXITOSAMENTE"
echo "======================================================================"
echo "🌐 Accede desde cualquier navegador web en tu red local:"
echo "   👉 http://${LOCAL_IP}:3000   (HTTP)"
echo "   👉 https://${LOCAL_IP}:3001  (HTTPS)"
echo ""
echo "📌 Primera vez al abrir en el navegador:"
echo "   1. Selecciona 'Open folder as vault'"
echo "   2. Elige la carpeta: /vaults/OPOSICIONES-TAI"
echo "======================================================================"
