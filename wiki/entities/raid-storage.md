---
title: "Sistemas de Almacenamiento RAID, DAS, NAS y SAN"
type: "entity"
tags:
  - raid
  - storage
  - das
  - nas
  - san
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RAID"
  - "Storage Architectures"
---

# Sistemas de Almacenamiento RAID, DAS, NAS y SAN

Las tecnologías de almacenamiento masivo redundante proporcionan tolerancia a fallos, alta disponibilidad y alto rendimiento en infraestructuras corporativas.

---

## 🏛️ Niveles RAID (Redundant Array of Independent Disks)

| Nivel RAID | Nombre | Mínimo Discos | Tolerancia a Fallos | Capacidad Útil | Rendimiento |
|------------|--------|---------------|---------------------|----------------|-------------|
| **RAID 0** | Striping (Bandas) | 2 | **0 discos** (sin redundancia) | $N \times S$ (100%) | Máxima velocidad lectura/escritura |
| **RAID 1** | Mirroring (Espejo) | 2 | **1 disco** | $1 \times S$ (50%) | Buena lectura, escritura estándar |
| **RAID 5** | Paridad Distribuida | 3 | **1 disco** | $(N - 1) \times S$ | Buena lectura, penalización en escritura |
| **RAID 6** | Doble Paridad Distribuida | 4 | **2 discos simultáneos** | $(N - 2) \times S$ | Alta lectura, mayor penalización escritura |
| **RAID 10 (1+0)** | Espejo de Bandas | 4 | **1 disco por sub-array** (hasta 2) | $(N / 2) \times S$ (50%) | Excelente lectura y escritura |

---

## 🧩 Comparativa Arquitectónica: DAS vs NAS vs SAN

| Característica | DAS (Direct Attached) | NAS (Network Attached) | SAN (Storage Area Network) |
|----------------|-----------------------|------------------------|----------------------------|
| **Nivel de Acceso** | Bloque local | **Ficheros** (*File-level*) | **Bloques** (*Block-level*) |
| **Medio / Red** | Bus local (SATA/SAS/NVMe) | LAN compartida (TCP/IP) | Red dedicada de alta velocidad |
| **Protocolos** | SCSI, SATA, SAS | **NFS, SMB/CIFS** | **Fibre Channel (FC), iSCSI, FCoE** |
| **Escalabilidad** | Muy limitada | Media | Muy alta |
| **Rendimiento** | Alto | Limitado por LAN | Ultrarrápido |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Mínimo discos RAID 5 / RAID 6 | **3 discos** / **4 discos** |
| Tolerancia fallos RAID 5 / 6 | **1 disco** / **2 discos simultáneos** |
| Puerto estándar iSCSI | **3260 TCP** |
| Protocolos NAS típicos | **NFS** (Linux/UNIX) y **SMB/CIFS** (Windows) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Concepto: [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación]]
