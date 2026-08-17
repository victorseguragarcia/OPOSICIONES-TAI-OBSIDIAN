---
title: "Guía del Documento y Expediente Electrónico, Metadatos Mínimos (NTI) y Archivo Único"
type: "synthesis"
tags:
  - synthesis
  - expediente-electronico
  - documento-electronico
  - nti
  - eni
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema08.md"
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Documento y Expediente Electrónico"
  - "Expediente Electrónico NTI"
---

# 🔴 Guía del Documento y Expediente Electrónico, Metadatos Mínimos (NTI) y Archivo Único

Estructura técnica normalizada del documento administrativo electrónico, índice foliado, metadatos mínimos obligatorios y archivo electrónico bajo la **Ley 39/2015**, **Ley 40/2015** y las **Normas Técnicas de Interoperabilidad (NTIs)**.

---

## 📄 1. Estructura del Documento Electrónico (Ley 39/2015 Art. 26 y NTI)

Todo documento administrativo electrónico debe contener:
1. **Contenido**: Información digital (texto, imagen, datos estructurados XML).
2. **Firma Electrónica**: Firma de la autoridad u órgano emisor (mediante certificado cualificado, sello electrónico o CSV).
3. **Metadatos Mínimos Obligatorios**:
   - `Identificador`: Código unívoco del documento.
   - `Órgano Emisor`: Código DIR3 de la unidad productora.
   - `Fecha de Captura`: Fecha y hora de generación.
   - `Origen`: Ciudadano o Administración.
   - `Estado de Elaboración`: Original, Copia auténtica con cambio de formato, Copia auténtica sin cambio de formato, Copia simple.
   - `Tipo Documental`: Clasificación según tabla NTI (Acta, Resolución, Notificación, etc.).

---

## 📁 2. Estructura del Expediente Administrativo Electrónico (Ley 39/2015 Art. 70 y NTI)

El expediente electrónico es el conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolución administrativa:

```
                              EXPEDIENTE ELECTRÓNICO
                                        │
      ┌─────────────────────────────────┼─────────────────────────────────┐
      ▼                                 ▼                                 ▼
1. Documentos Electrónicos    2. Índice Electrónico Foliado     3. Metadatos del Expediente
  • Conjunto de documentos      • Índice firmado por el órgano    • Identificador
    con sus metadatos y firma     garantizando la integridad      • Órgano (DIR3)
                                • Huella digital (Hash SHA-256)   • Fecha de apertura
                                • Foliado electrónico numerado    • Estado (Abierto/Cerrado)
```

---

## 📦 3. Archivo Electrónico Único (Ley 39/2015 Art. 46 y Ley 40/2015 Art. 17)

- Cada Administración Pública debe mantener un **Archivo Electrónico Único** para almacenar todos los documentos electrónicos correspondientes a procedimientos finalizados.
- **Formatos a Largo Plazo**: Uso de formatos abiertos y duraderos según NTI de Catálogo de Estándares (**PDF/A-1a, PDF/A-1b, PDF/A-2**, XML, PNG/JPEG para imágenes, TIFF).
- **Preservación Digital**: Plataforma **ARCHIVE** de la AGE (basada en el estándar internacional OAIS ISO 14721).

---

## 🔗 Referencias Cruzadas
- Concepto: [[wiki/concepts/documento-y-expediente-electronico-nti|Documento y Expediente Electrónico NTI]]
- Entidad: [[wiki/entities/esquema-nacional-interoperabilidad-eni|Esquema Nacional de Interoperabilidad (ENI)]]
