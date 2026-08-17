---
title: "Sistemas de Archivos: FAT32, NTFS, ext4 y XFS"
type: "entity"
tags:
  - sistemas-archivos
  - fat32
  - ntfs
  - ext4
  - xfs
  - inodos
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Sistemas de Archivos"
  - "NTFS y ext4"
---

# Sistemas de Archivos: FAT32, NTFS, ext4 y XFS

Arquitectura y características técnicas de los sistemas de archivos más utilizados en Windows y GNU/Linux.

---

## 🏛️ Comparativa de Límites y Características

| Sistema | Tamaño Máx Archivo | Tamaño Máx Volumen | Journaling | Estructura Central |
|---------|-------------------|-------------------|------------|--------------------|
| **FAT32** | **4 GB ($2^{32}-1$)** | **2 TB** | No | File Allocation Table |
| **NTFS** | **16 TB** a 8 PB | **8 PB** | **Sí (`$LogFile`)** | **MFT (Master File Table)** |
| **ext4** | **16 TB** | **1 Exabyte** | **Sí** | **Inodos + Extents** |
| **XFS** | **8 Exabytes** | **8 Exabytes** | **Sí** | **Allocation Groups (AG)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización de Ficheros]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
