# -*- coding: utf-8 -*-
r"""
Script generador de las Entidades y Conceptos de la sección de Informática del Bloque 1.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

ENTITIES_CONCEPTS = {
    "wiki/entities/servicios-comunes-administracion-electronica.md": """---
title: "Servicios Comunes, Plataformas y Red SARA de la AGE"
type: "entity"
tags:
  - servicios-comunes
  - red-sara
  - clave
  - face
  - geiser
  - inside
  - administracion-electronica
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Servicios Comunes AGE"
  - "Red SARA y Plataformas SGAD"
---

# Servicios Comunes, Plataformas y Red SARA de la AGE

Conjunto de infraestructuras, plataformas tecnológicas y aplicaciones horizontales desarrolladas por la Secretaría General de Administración Digital (SGAD) para prestar servicios compartidos a todas las Administraciones Públicas españolas.

---

## 🏛️ Principales Plataformas del Catálogo

- **Red SARA**: Red troncal de comunicaciones segura de las AAPP interconectada con la red europea **sTESTA / EuroDomain**.
- **Cl@ve**: Plataforma común de identificación, autenticación y firma electrónica para los servicios públicos.
- **SIR**: Sistema de Interconexión de Registros (norma SICRES 3.0).
- **FACe**: Punto General de Entrada de Facturas Electrónicas de la AGE.
- **INSIDE y ARCHIVE**: Gestión integral de documentos y expedientes electrónicos y su archivo a largo plazo conforme al modelo OAIS.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Ley 40/2015 LRJSP]]
- Síntesis: [[wiki/synthesis/servicios-comunes-age-administracion-electronica-cheatsheet|Cheatsheet de Servicios Comunes AGE]]
- Síntesis: [[wiki/synthesis/bloque1-informatica-y-administracion-digital-master-guide|Guía Maestra Informática Bloque 1]]
""",

    "wiki/entities/firma-electronica-y-reglamento-eidas.md": """---
title: "Firma Electrónica, Servicios de Confianza y Reglamento eIDAS (UE 910/2014)"
type: "entity"
tags:
  - firma-electronica
  - eidas
  - ley-6-2020
  - seguridad
  - certificados
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Firma Electrónica y eIDAS"
  - "Reglamento eIDAS"
  - "Ley 6/2020 LSEC"
---

# Firma Electrónica, Servicios de Confianza y Reglamento eIDAS (UE 910/2014)

Marco legal europeo y nacional que regula la identificación electrónica y los servicios de confianza para las transacciones electrónicas en el mercado interior.

---

## 🏛️ Clasificación de Firmas Electrónicas

1. **Firma Electrónica Simple**: Datos en formato electrónico anejos a otros datos electrónicos o asociados de manera lógica con ellos que utiliza el firmante para firmar.
2. **Firma Electrónica Avanzada**:
   - Está vinculada al firmante de manera única.
   - Permite la identificación del firmante.
   - Creada con datos de creación bajo control exclusivo del firmante.
   - Vinculada con los datos de forma que cualquier cambio ulterior sea detectable.
3. **Firma Electrónica Cualificada**:
   - Firma avanzada creada mediante un **Dispositivo Cualificado de Creación de Firma (QSCD)**.
   - Basada en un **Certificado Cualificado de Firma Electrónica**.
   - Posee **equivalencia jurídica plena a la firma manuscrita** en toda la Unión Europea.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Ley 40/2015 LRJSP]]
- Síntesis: [[wiki/synthesis/firma-electronica-eidas-ley6-2020-dnie-guia|Guía de Firma Electrónica y eIDAS]]
""",

    "wiki/entities/dnie-dni-electronico.md": """---
title: "DNI Electrónico (DNIe 3.0 / DNI 4.0)"
type: "entity"
tags:
  - dnie
  - identidad-digital
  - certificados
  - nfc
  - criptografia
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DNIe"
  - "DNI Electrónico"
---

# DNI Electrónico (DNIe 3.0 / DNI 4.0)

Documento físico y digital emitido por la Dirección General de la Policía (DGP) que acredita presencial y telemáticamente la identidad y nacionalidad española.

---

## 🏛️ Arquitectura Técnica y Certificados

- **Chip Criptográfico Seguro**: Tarjeta inteligente con microprocesador criptográfico.
- **Certificados Incorporados (X.509 v3)**:
  1. **Certificado de Autenticación**: Autenticación segura y control de acceso.
  2. **Certificado de Firma Electrónica**: Firma cualificada con equivalencia legal manuscrita.
- **Generaciones**:
  - **DNIe 3.0**: Incorpora interfaz dual (contactos y antena inalámbrica **NFC ISO/IEC 14443**).
  - **DNI 4.0**: Adaptado al Reglamento (UE) 2019/1157 para su interoperabilidad y uso en monederos digitales europeos.

---

## 🔗 Referencias Cruzadas
- Síntesis: [[wiki/synthesis/firma-electronica-eidas-ley6-2020-dnie-guia|Guía de Firma Electrónica y DNIe]]
""",

    "wiki/entities/esquema-nacional-interoperabilidad-eni.md": """---
title: "Esquema Nacional de Interoperabilidad (ENI - Real Decreto 4/2010)"
type: "entity"
tags:
  - eni
  - interoperabilidad
  - nti
  - administracion-electronica
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ENI"
  - "Esquema Nacional de Interoperabilidad"
---

# Esquema Nacional de Interoperabilidad (ENI - Real Decreto 4/2010)

Conjunto de criterios y recomendaciones que deben seguir las Administraciones Públicas para permitir el intercambio de información y la prestación conjunta de servicios digitales.

---

## 🏛️ Dimensiones de la Interoperabilidad

1. **Interoperabilidad Técnica**: Infraestructuras y protocolos de comunicación (redes, interfaces de red, formatos de codificación).
2. **Interoperabilidad Semántica**: Significado preciso de los datos intercambiados para que sea interpretado unívocamente por cualquier sistema.
3. **Interoperabilidad Organizativa**: Procesos de negocio, objetivos y acuerdos de colaboración entre organismos administrativos.

---

## 📜 Normas Técnicas de Interoperabilidad (NTIs)
- NTI de Catálogo de Estándares.
- NTI de Documento Electrónico.
- NTI de Digitalización de Documentos.
- NTI de Expediente Electrónico.
- NTI de Política de Firma y Sello Electrónicos.
- NTI de Procedimiento de Copiado Auténtico y Conversión.
- NTI de Modelo de Datos para el Intercambio de Asientos Registrales (SICRES).
- NTI de Reutilización de Recursos de Información.

---

## 🔗 Referencias Cruzadas
- Concepto: [[wiki/concepts/documento-y-expediente-electronico-nti|Documento y Expediente Electrónico NTI]]
- Síntesis: [[wiki/synthesis/gestion-documento-y-expediente-electronico-eni-guia|Guía del Documento y Expediente Electrónico]]
""",

    "wiki/concepts/documento-y-expediente-electronico-nti.md": """---
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
"""
}

print("[*] Escribiendo 5 entidades y conceptos de la sección de Informática del Bloque 1...")
for path, content in ENTITIES_CONCEPTS.items():
    write_file(path, content)

print("[*] Entidades y conceptos de Informática del Bloque 1 creados exitosamente.")
