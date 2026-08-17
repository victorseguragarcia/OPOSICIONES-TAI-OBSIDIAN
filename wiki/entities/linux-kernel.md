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

El **Linux Kernel** es un núcleo monolítico modular de código abierto tipo UNIX creado originalmente por Linus Torvalds en 1991. Gestiona los recursos del hardware, la memoria virtual, los procesos, los controladores de dispositivos y el sistema de archivos del sistema operativo.

---

## 🏛️ Arquitectura y Subsistemas Principales

- **Arquitectura Monolítica Modular**: Aunque todos los servicios principales del sistema operativo se ejecutan en el espacio del núcleo (**Kernel Space / Ring 0**), el kernel puede cargar y descargar dinámicamente **módulos de kernel** (`.ko`) en tiempo de ejecución mediante `insmod`, `rmmod`, `modprobe` y `lsmod`.
- **Gestión y Planificación de Procesos**:
  - Planificador por defecto: **CFS (Completely Fair Scheduler)** basado en árboles rojo-negro (*Red-Black Trees*).
  - Llamadas al sistema de control de procesos: `fork()` (creación de proceso hijo duplicando el espacio de memoria mediante *Copy-On-Write*), `execve()` (reemplazo de imagen de proceso), `wait()` / `waitpid()` (sincronización con procesos hijos) y `exit()` (terminación).
  - Estados de proceso: `R` (Running/Runnable), `S` (Interruptible Sleep), `D` (Uninterruptible Sleep / I/O), `Z` (Zombie: finalizado sin recogida por el padre), `T` (Stopped).
- **Gestión de Memoria Virtual**:
  - Espacio de direcciones virtual dividido en Espacio de Usuario (Ring 3) y Espacio de Núcleo (Ring 0).
  - Asignación de memoria física mediante el algoritmo **Buddy System** y el asignador de objetos **SLAB / SLUB**.
  - Paginación bajo demanda con soporte de páginas estándar (4 KB) y páginas gigantes (*HugePages* de 2 MB / 1 GB).
  - Algoritmo de reemplazo de páginas (LRU - Least Recently Used) y área de intercambio (*Swap* / `swappiness`).
- **Sistema Virtual de Ficheros (VFS)**:
  - Capa de abstracción que unifica el acceso a diferentes sistemas de archivos (ext4, XFS, Btrfs, ZFS, NFS, procfs, sysfs).
  - Estructuras VFS: `superblock` (metadatos del sistema de archivos), `inode` (metadatos del archivo y punteros a bloques), `dentry` (asociación de nombres de archivo a inodos en caché) y `file` (estado de archivo abierto por un proceso).
- **Control de Acceso y Permisos POSIX**:
  - Permisos tradicionales: Lectura (`r`=4), Escritura (`w`=2), Ejecución (`x`=1) para Propietario (u), Grupo (g) y Otros (o).
  - Bits especiales: **SUID** (4000: ejecuta con privilegios del dueño), **SGID** (2000: herencia de grupo), **Sticky Bit** (1000: solo el dueño puede borrar ficheros en el directorio, ej. `/tmp`).
  - Listas de Control de Acceso extendidas: `getfacl` y `setfacl`.
- **Sistema de Inicialización y Servicios (systemd)**:
  - Sucesor de SysVinit y Upstart. Reemplaza el PID 1 tradicional.
  - Unidades de systemd: `.service` (servicios), `.target` (estados/niveles de ejecución, ej. `multi-user.target`, `graphical.target`), `.socket` (activación por socket), `.timer` (temporizadores programados tipo cron).
  - Comandos: `systemctl {start|stop|restart|status|enable|disable}`, `journalctl -u servicio -f`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Valor Técnico / Comando |
|---------|-------------------------|
| Tipo de Núcleo | **Monolítico Modular** |
| Planificador de CPU | **CFS (Completely Fair Scheduler)** |
| Tamaño de Página Estándar | **4 KB** |
| Permiso SUID / SGID / Sticky | `4000` (SUID), `2000` (SGID), `1000` (Sticky Bit) |
| Gestor de Servicios Moderno | **systemd** (PID 1) |
| Herramientas de Módulos | `lsmod`, `modprobe`, `insmod`, `rmmod` |
| Consulta de Logs systemd | `journalctl -xe` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
- Concepto: [[wiki/concepts/process-and-memory-management|Gestión de Procesos y Memoria]]
- Scripting: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
