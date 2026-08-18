#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue en Raspberry Pi / Servidores Linux
# Redirige al script universal 'host-on-linux.sh'
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/host-on-linux.sh" ]; then
    bash "$SCRIPT_DIR/host-on-linux.sh" "$@"
else
    curl -sSL https://raw.githubusercontent.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN/main/scripts/host-on-linux.sh | bash
fi
