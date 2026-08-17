---
title: "Resumen Fuente: Bloque 2 - Tema 05: Ficheros, Organización y Sistemas de Archivos: FAT32, NTFS, ext4, XFS"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema05
  - ficheros
  - sistemas-archivos
  - fat32
  - ntfs
  - ext4
  - xfs
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Ficheros y Sistemas de Archivos"
  - "bloque2-tema05"
---

# Resumen Fuente: Bloque 2 - Tema 05: Ficheros, Organización y Sistemas de Archivos: FAT32, NTFS, ext4, XFS

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema05.md|bloque2-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza los fundamentos del almacenamiento a nivel de sistema operativo: la estructura lógica de ficheros (registros lógicos, bloques físicos y factor de bloqueo), las organizaciones de ficheros (**secuencial**, **directa/relativa por hash** e **indexada/ISAM**) y sus modos de acceso (secuencial, directo y dinámico), y la arquitectura y límites de los principales sistemas de archivos modernos: **FAT32** (límite estricto de 4 GB por archivo), **NTFS** (basado en la tabla MFT, con soporte de journaling `$LogFile`, permisos ACL, cifrado EFS, cuotas y VSS), **ext4** (basado en inodos con extensiones *extents*, asignación retardada y journaling de 3 modos) y **XFS** (diseñado para escalabilidad masiva con Grupos de Asignación paralelos y volúmenes de hasta 8 Exabytes).

---

## 🎯 Datos Clave para Oposiciones TAI

| Sistema de Archivos | Tamaño Máximo de Archivo | Tamaño Máximo de Volumen | Journaling | Estructura Principal |
|---------------------|--------------------------|--------------------------|------------|----------------------|
| **FAT32** | **4 GB ($2^{32}-1$ bytes)** | **2 TB** | **No** | File Allocation Table (28 bits) |
| **NTFS** | **16 TB** a 8 PB | **8 PB** | **Sí (`$LogFile`)** | **MFT (Master File Table)** |
| **ext4** | **16 TB** | **1 Exabyte (EB)** | **Sí** | **Inodos + Extents** |
| **XFS** | **8 Exabytes (EB)** | **8 Exabytes (EB)** | **Sí** | **Allocation Groups (AG)** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos: FAT32, NTFS, ext4 y XFS]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización de Ficheros y Métodos de Acceso]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
