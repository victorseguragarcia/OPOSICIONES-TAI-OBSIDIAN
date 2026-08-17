---
title: "Documento Administrativo Electrónico, Expediente y Metadatos Mínimos (NTI)"
type: "concept"
tags:
  - documento-electronico
  - expediente-electronico
  - nti
  - eni
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema08.md"
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Documento y Expediente Electrónico NTI"
  - "Estructura del Expediente Electrónico"
---

# Documento Administrativo Electrónico, Expediente y Metadatos Mínimos (NTI)

Especificaciones técnicas y funcionales que garantizan la autenticidad, integridad, trazabilidad y foliado de los documentos y expedientes públicos.

---

## 🏛️ Componentes y Metadatos Obligatorios

```
+-------------------------------------------------------------+
|               DOCUMENTO ELECTRÓNICO (NTI)                   |
|                                                             |
| 1. CONTENIDO DIGITAL (Texto, XML, Imagen)                   |
| 2. FIRMA ELECTRÓNICA (XAdES, PAdES, CAdES, CSV)            |
| 3. METADATOS MÍNIMOS OBLIGATORIOS:                          |
|    • Identificador (Código único)                           |
|    • Órgano (Código DIR3)                                   |
|    • Fecha de Captura                                       |
|    • Origen (Ciudadano / Administración)                    |
|    • Estado de Elaboración (Original, Copia Auténtica)      |
|    • Tipo Documental                                        |
+-------------------------------------------------------------+
```

- **Foliado Electrónico**: Numeración consecutiva de los documentos de un expediente garantizada mediante la firma electrónica del **Índice Electrónico**.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/esquema-nacional-interoperabilidad-eni|Esquema Nacional de Interoperabilidad]]
- Síntesis: [[wiki/synthesis/gestion-documento-y-expediente-electronico-eni-guia|Guía del Documento y Expediente Electrónico]]
