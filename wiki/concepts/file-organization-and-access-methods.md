---
title: "Organización de Ficheros y Métodos de Acceso"
type: "concept"
tags:
  - ficheros
  - organizacion-ficheros
  - acceso-secuencial
  - acceso-directo
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Organización de Ficheros"
  - "Métodos de Acceso"
---

# Organización de Ficheros y Métodos de Acceso

Estructuración lógica de los datos sobre soportes de almacenamiento no volátil.

---

## 🏛️ Clasificación de Organizaciones

1. **Secuencial**: Registros contiguos en orden físico. Muy rápida para procesar el 100% de registros en lotes; lenta para búsquedas individuales.
2. **Directa / Relativa (Hash)**: Ubicación calculada mediante función de dispersión sobre la clave. Acceso en $O(1)$.
3. **Indexada / Secuencial-Indexada (ISAM)**: Área secuencial más tabla de índices auxiliar. Soporta tanto acceso secuencial ordenado como acceso directo por clave.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos]]
