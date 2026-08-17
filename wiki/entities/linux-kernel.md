---
title: "Linux Kernel y Software de Base"
type: "entity"
tags:
  - linux
  - kernel
  - operating-systems
  - software-base
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Núcleo Linux"
  - "Linux OS"
---

# Linux Kernel y Software de Base

El **Linux Kernel** es un núcleo monolítico modular que gestiona recursos de hardware, memoria virtual, planificación de procesos y controladores de dispositivos en sistemas tipo UNIX.

## Componentes Clave
- **Gestión de Procesos**: Planificador CFS (Completely Fair Scheduler), estados de proceso (R, S, D, Z, T), llamadas `fork()`, `exec()`, `wait()`.
- **Memoria Virtual**: Paginación bajo demanda, swap, TLB y asignador Buddy System.
- **Sistemas de Archivos**: VFS (Virtual File System) soportando ext4, XFS, Btrfs y ZFS.
- **Gestión de Servicios**: Init tradicional vs. `systemd` (unidades `.service`, `.target`, `systemctl`, `journalctl`).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
- Scripting: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]

