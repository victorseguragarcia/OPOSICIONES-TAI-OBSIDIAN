---
title: "Matriz Comparativa de Sistemas de Archivos: FAT32, NTFS, ext4 y XFS"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - file-systems
  - fat32
  - ntfs
  - ext4
  - xfs
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Sistemas de Archivos"
  - "FAT32 vs NTFS vs ext4"
---

# Matriz Comparativa de Sistemas de Archivos: FAT32, NTFS, ext4 y XFS

Contraste técnico de capacidades, seguridad y tolerancia a fallos entre sistemas de archivos.

---

## 🏛️ Matriz Técnica Comparativa

| Característica | FAT32 | NTFS | ext4 | XFS |
|----------------|-------|------|------|-----|
| **Sistema Operativo Principal** | Multiplataforma | Windows Server / 11 | GNU/Linux | Linux (RHEL/CentOS) |
| **Tamaño Máximo de Archivo** | **4 GB ($2^{32}-1$)** | **16 TB** (hasta 8 PB) | **16 TB** | **8 Exabytes (EB)** |
| **Tamaño Máximo de Volumen** | **2 TB** | **8 PB** | **1 Exabyte (EB)** | **8 Exabytes (EB)** |
| **Registro por Diario (Journaling)**| **No** | **Sí (`$LogFile`)** | **Sí (3 modos)** | **Sí** |
| **Estructura Interna de Metadatos** | Tabla FAT (28 bits) | **MFT (Master File Table)**| **Inodos + Extents** | **Allocation Groups** |
| **Permisos de Seguridad** | No | ACLs (DACL / SACL) | Permisos POSIX + ACLs | Permisos POSIX + ACLs |
| **Cifrado y Compresión Nativos** | No | **Sí (EFS / LZNT1)** | Opcional | No nativo |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos]]
