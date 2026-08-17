---
title: "Arquitectura de Sistemas Operativos y Software de Base"
type: "concept"
tags:
  - operating-systems
  - kernel
  - os-architecture
  - concepts
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura del SO"
  - "Operating System Architecture"
---

# Arquitectura de Sistemas Operativos y Software de Base

El Sistema Operativo es la capa de software intermediaria entre el hardware físico y los programas de usuario, garantizando abstracción y asignación equitativa de recursos.

## Niveles Arquitectónicos
1. **Espacio del Kernel (Kernel Space)**: Ejecución en modo privilegiado (Ring 0), acceso directo a registros, memoria física e interrupciones.
2. **Espacio de Usuario (User Space)**: Aplicaciones ejecutándose en modo no privilegiado (Ring 3).
3. **Llamadas al Sistema (System Calls)**: Interfaz controlada que permite a las aplicaciones solicitar servicios al kernel (`read`, `write`, `fork`, `execve`).

## Tipos de Núcleo
- **Monolítico** (Linux): Todos los servicios del SO (gestión de memoria, red, IPC, drivers) residen en el mismo espacio de memoria privilegiado.
- **Microkernel** (Mach, QNX): Solo las funciones esenciales residen en el kernel; servidores en espacio de usuario se comunican mediante IPC.
- **Híbrido** (Windows NT, macOS XNU): Estructura monolítica con componentes modulares organizados por capas.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel y Software de Base]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]

