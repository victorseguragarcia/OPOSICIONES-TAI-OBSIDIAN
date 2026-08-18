---
title: "Resumen Exhaustivo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-04
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema04.md]]"
  - "[[wiki/sources/bloque4-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]

# 🔴 Resumen Exhaustivo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 04**
> Estándar de clasificación TIER I a TIER IV de Uptime Institute (disponibilidad, redundancia y tiempo de inactividad anual), arquitecturas de almacenamiento DAS, NAS (NFS, SMB/CIFS) vs SAN (Fibre Channel, iSCSI), y niveles de RAID (0, 1, 5 con paridad distribuida, 6 con doble paridad, 10, 50).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Clasificación TIER de CPDs (Uptime Institute)

| Nivel TIER | Disponibilidad Anual | Tiempo Máximo de Inactividad al Año | Nivel de Redundancia de Componentes | Vías de Distribución Eléctrica y Clima | Mantenimiento Concurrente |
|:---|:---:|:---:|:---:|:---:|:---:|
| **TIER I (Básico)** | **99,671%** | **28,8 horas / año** | $N$ (Sin redundancia) | 1 única vía de distribución | ❌ NO (Exige parada total) |
| **TIER II (Redundante)** | **99,741%** | **22,0 horas / año** | $N+1$ (Componentes redundantes) | 1 única vía de distribución | ❌ NO (Exige paradas programadas) |
| **TIER III (Mantenible Concurrente)** | **99,982%** | **1,6 horas / año (95 min)** | $N+1$ | **Múltiples vías (1 activa + 1 pasiva)** | **SÍ (Sin interrumpir servicio)** |
| **TIER IV (Tolerante a Fallos)** | **99,995%** | **26,3 minutos / año** | **$2(N+1)$ o $2N+1$** | **Múltiples vías activas simultáneas** | **SÍ (Tolerancia total a fallos)** |

### 2. Arquitecturas de Almacenamiento en Red: DAS, NAS y SAN
- **DAS (Direct Attached Storage)**: Almacenamiento conectado directamente al bus del servidor (SATA, SAS, PCIe). No compartido por red.
- **NAS (Network Attached Storage)**: Servidor de almacenamiento dedicado conectado a la red LAN compartiendo datos a **nivel de fichero (File-level)** mediante protocolos de red:
  - **NFS (Network File System)**: Protocolo estándar en entornos UNIX/Linux (puerto 2049 TCP/UDP).
  - **SMB / CIFS (Server Message Block)**: Protocolo estándar en Windows (puerto 445 TCP).
- **SAN (Storage Area Network)**: Red dedicada de alta velocidad que conecta servidores a cabinas de discos compartiendo almacenamiento a **nivel de bloque (Block-level)** (el sistema operativo ve el LUN como un disco local en crudo):
  - **Fibre Channel (FC)**: Red dedicada sobre fibra óptica mediante conmutadores FC y tarjetas HBA (Host Bus Adapter). Velocidades: 8, 16, 32, 64 Gbps.
  - **iSCSI**: Encapsula comandos SCSI sobre paquetes TCP/IP estándar (puerto **3260 TCP**), utilizando switches Ethernet estándar de 10/25/100 GbE.

### 3. Niveles de RAID (Redundant Array of Independent Disks)

| Nivel RAID | Denominación y Técnica | Discos Mínimos | Capacidad Útil Total ($N$ discos de tamaño $C$) | Tolerancia a Fallos de Disco | Rendimiento Lectura / Escritura |
|:---|:---|:---:|:---:|:---:|:---|
| **RAID 0** | Striping (Bandeado / Fraccionamiento) | **2** | **$N \times C$** (100% capacidad) | **0 discos** (1 fallo = pérdida total) | Muy Alto / Muy Alto |
| **RAID 1** | Mirroring (Espejo) | **2** | **$C$** (50% de 2 discos) | **1 disco** (en array de 2) | Alto / Medio |
| **RAID 5** | Striping con **Paridad Distribuida** | **3** | **$(N - 1) \times C$** | **1 disco** | Muy Alto / Medio (penalización por cálculo de paridad) |
| **RAID 6** | Striping con **Doble Paridad Distribuida** | **4** | **$(N - 2) \times C$** | **2 discos simultáneos** | Muy Alto / Lento en escritura |
| **RAID 10 (1+0)** | Espejo de franjas (Mirroring + Striping) | **4** (pares) | **$(N / 2) \times C$** (50%) | Hasta 1 disco por sub-espejo | Muy Alto / Muy Alto |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 04 (Bloque 4)**
> 1. **Discos Mínimos en RAID**: RAID 0 (2 discos), RAID 1 (2 discos), **RAID 5 (3 discos)**, **RAID 6 (4 discos)**, RAID 10 (4 discos).
> 2. **NAS vs SAN**: NAS opera a **nivel de Fichero** (NFS, SMB); SAN opera a **nivel de Bloque** (iSCSI, Fibre Channel).
> 3. **TIER III**: Es el nivel que introduce el **Mantenimiento Concurrente** (permite reparar cualquier componente sin cortar el servicio).

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Capacidades RAID**: **RAID 5 $= N-1$ discos** / **RAID 6 $= N-2$ discos** / **RAID 1 y 10 $= 50\%$ capacidad**.
> - **Nivel Almacenamiento**: **NAS $=$ Archivo** / **SAN $=$ Bloque**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema04|Fuente Oficial del Tema 04]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema04|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema04-redes-lan-dhcp-dns|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]
