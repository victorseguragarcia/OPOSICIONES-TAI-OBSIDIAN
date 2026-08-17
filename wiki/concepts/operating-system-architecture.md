---
title: "Arquitectura de Sistemas Operativos y Software de Base"
type: "concept"
tags:
  - operating-systems
  - os-architecture
  - kernel
  - firmware
  - sysadmin
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de Sistemas Operativos"
  - "OS Architecture"
---

# Arquitectura de Sistemas Operativos y Software de Base

La **arquitectura del sistema operativo** define la organización estructural, las capas de abstracción y los mecanismos de comunicación entre el hardware, el núcleo (kernel), los controladores de dispositivos y el software de aplicación.

---

## 🏛️ Modelos de Arquitectura de Kernel

1. **Kernel Monolítico Puro**: Todos los componentes del sistema operativo (planificador, gestión de memoria, sistemas de archivos, drivers de dispositivos y red) se ejecutan en un único espacio de direcciones con el máximo nivel de privilegio (**Ring 0**). Alta velocidad por llamadas a funciones directas, pero menor robustez ante fallos de controladores.
2. **Kernel Monolítico Modular (Linux)**: Mantiene el alto rendimiento monolítico pero permite cargar y descargar controladores dinámicamente en caliente (*Loadable Kernel Modules - LKM*).
3. **Microkernel (Mach, MINIX, QNX)**: Reduce el núcleo a las funciones estrictamente mínimas: comunicación entre procesos (IPC), gestión básica de memoria y planificación. Los servicios como sistemas de archivos y drivers corren en espacio de usuario (**Ring 3**). Máxima tolerancia a fallos y seguridad a costa de una pequeña penalización de rendimiento por cambios de contexto e IPC.
4. **Kernel Híbrido (Windows NT, macOS XNU)**: Combina la velocidad del monolito con la estructura modular del microkernel.

---

## 🧩 Firmware de Arranque: BIOS vs UEFI

| Característica | BIOS Tradicional (Legacy) | UEFI (Unified Extensible Firmware Interface) |
|----------------|---------------------------|----------------------------------------------|
| **Lenguaje de Programación** | Ensamblador | **Lenguaje C** |
| **Modo de Operación CPU** | 16 bits en modo real | **32 bits o 64 bits** en modo protegido |
| **Tabla de Particiones** | **MBR** (máx 2 TB, 4 particiones primarias) | **GPT** (hasta 128 particiones, soporte >2 TB) |
| **Seguridad en el Arranque** | Sin validación de firmas | **Secure Boot** (firmas digitales obligatorias) |
| **Soporte de Red Pre-SO** | Limitado | Nativo (PXE, diagnósticos, IPv4/IPv6) |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tipo de Kernel Linux | **Monolítico Modular** |
| Anillos de Privilegio x86 | **Ring 0** (Kernel) y **Ring 3** (Usuario) |
| Límite Direccionamiento MBR | **2 Terabytes** |
| Especificación UEFI | Escrita en **C**, sucesor de BIOS, soporte Secure Boot |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
