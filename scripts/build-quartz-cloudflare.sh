#!/usr/bin/env bash
# ==============================================================================
# Script de Compilación de Quartz 4 para Cloudflare Pages
# ==============================================================================

set -e

echo "======================================================================"
echo "🚀 INICIANDO COMPILACIÓN DE QUARTZ 4 EN CLOUDFLARE PAGES"
echo "======================================================================"

# 1. Clonar el motor oficial de Quartz en un directorio temporal
rm -rf .quartz-engine public
git clone --depth 1 https://github.com/jackyzha0/quartz.git .quartz-engine

# 2. Copiar todo el contenido de la bóveda a .quartz-engine/content
mkdir -p .quartz-engine/content
cp -r wiki .quartz-engine/content/
cp index.md .quartz-engine/content/index.md 2>/dev/null || true
cp Dashboard.md .quartz-engine/content/Dashboard.md 2>/dev/null || true
cp README.md .quartz-engine/content/README.md 2>/dev/null || true

if [ -d "raw/assets" ]; then
  mkdir -p .quartz-engine/content/raw/assets
  cp -r raw/assets/* .quartz-engine/content/raw/assets/ 2>/dev/null || true
fi

if [ -f "quartz.config.ts" ]; then
  cp quartz.config.ts .quartz-engine/quartz.config.ts
fi

# 3. Instalar dependencias y compilar Quartz
cd .quartz-engine
npm ci
npx quartz build

# 4. Mover la carpeta de salida 'public' a la raíz
cd ..
cp -r .quartz-engine/public ./public
rm -rf .quartz-engine

echo "======================================================================"
echo "✅ COMPILACIÓN DE QUARTZ FINALIZADA CON ÉXITO"
echo "======================================================================"
