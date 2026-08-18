---
title: "Resumen Exhaustivo Tema 01 (Bloque 4): Administración de Sistemas Operativos Servidor (Linux SysAdmin, Windows Server)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-01
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema01.md]]"
  - "[[wiki/sources/bloque4-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Portada Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|Tema 02 ➡️]]

# 🔴 Resumen Exhaustivo Tema 01 (Bloque 4): Administración de Sistemas Operativos Servidor (Linux SysAdmin, Windows Server)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 01**
> Administración de Linux (Debian, RHEL), init vs systemd (systemctl, journalctl), gestión de volúmenes LVM (PV, VG, LV), permisos especiales (SUID, SGID, Sticky bit, ACLs), umask, administración de Windows Server, Server Manager, PowerShell y automatización.

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Administración de Servidores Linux (Debian, Ubuntu, RHEL, Rocky)
- **Gestor de Sistema e Inicialización: `systemd`**:
  - Reemplazó a SysVinit (`/etc/init.d`) ofreciendo paralelización en el arranque y gestión por sockets.
  - `systemctl`:
    - `systemctl start | stop | restart | reload | status <servicio>`
    - `systemctl enable | disable <servicio>` (activa o desactiva arranque automático al inicio).
    - `systemctl mask <servicio>` (enlaza a `/dev/null` impidiendo que sea iniciado incluso manualmente).
  - `journalctl`: Visor centralizado de logs binarios de systemd (`journalctl -u nginx -f` seguimiento en tiempo real, `journalctl -p err` solo errores).
- **Gestión Lógica de Almacenamiento: LVM (Logical Volume Manager)**:
  - Arquitectura en 3 capas:
    1. **PV (Physical Volume)**: Discos duros o particiones físicas inicializadas (`pvcreate /dev/sdb1`, `pvs`, `pvdisplay`).
    2. **VG (Volume Group)**: Agrupación de PVs en un pool común de almacenamiento (`vgcreate vg_datos /dev/sdb1 /dev/sdc1`, `vgextend`, `vgs`).
    3. **LV (Logical Volume)**: Volúmenes lógicos creados a partir del VG sobre los que se crea el sistema de ficheros (`lvcreate -L 50G -n lv_web vg_datos`, `lvextend -r -L +20G /dev/vg_datos/lv_web`).
- **Permisos UNIX/Linux y Bits Especiales**:
  - `chmod u+s /archivo` (SUID - `4755`): Ejecuta con privilegios del propietario.
  - `chmod g+s /directorio` (SGID - `2775`): Los archivos nuevos heredan el grupo del directorio.
  - `chmod +t /tmp` (Sticky Bit - `1777`): Solo el propietario puede borrar sus propios archivos en la carpeta compartida.

### 2. Administración de Windows Server y PowerShell
- **Ediciones de Windows Server**: Standard, Datacenter (máquinas virtuales ilimitadas con Hyper-V), Essentials.
- **Modos de Instalación**: Server Core (sin interfaz gráfica, menor superficie de ataque, menor consumo de RAM) vs Desktop Experience (con GUI completa).
- **PowerShell y Cmdlets Esenciales**:
  - Estructura estándar: `Verbo-Sustantivo` (ej. `Get-Service`, `Start-Process`, `Set-ExecutionPolicy`).
  - *Políticas de Ejecución*: `Restricted` (por defecto en cliente), `AllSigned`, `RemoteSigned` (estándar en servidores: scripts locales sin firmar, remotos firmados), `Unrestricted`, `Bypass`.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 01 (Bloque 4)**
> 1. **Jerarquía LVM**: El orden exacto de creación es **PV $\rightarrow$ VG $\rightarrow$ LV** (nunca se crea un LV directamente sobre un disco físico).
> 2. **systemctl mask**: Es la única forma de impedir que un servicio sea iniciado por dependencias de otros servicios.
> 3. **Sticky bit (1000)**: En directorios como `/tmp` permite que todos escriban, pero **solo el dueño del archivo puede borrarlo**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Capas LVM**: **P - V - L** $\rightarrow$ **P**hysical Volume $\rightarrow$ **V**olume Group $\rightarrow$ **L**ogical Volume.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema01|Fuente Oficial del Tema 01]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema01|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema01-conceptos-so-virtualizacion|Test Tema 01]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Portada Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|Tema 02 ➡️]]
