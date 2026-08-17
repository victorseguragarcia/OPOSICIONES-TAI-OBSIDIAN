# -*- coding: utf-8 -*-
r"""
Script generador de la sección monográfica especializada:
'Informática Pública, Administración Electrónica y Marco Digital de la AGE' (Bloque 1 TAI).
Basado en los PDFs oficiales de raw/bloque 1 (UD012190 a UD012193).
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

NOTES = {
    # =========================================================================
    # GUÍAS DE SÍNTESIS
    # =========================================================================
    "wiki/synthesis/bloque1-informatica-y-administracion-digital-master-guide.md": """---
title: "Guía Maestra de Informática, Administración Electrónica y Marco Digital de la AGE (Bloque 1)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-1
  - administracion-electronica
  - informatica-publica
  - eidas
  - red-sara
  - eni
sources:
  - "raw/sources/bloque1-tema08.md"
  - "raw/sources/bloque1-tema09.md"
  - "raw/sources/bloque1-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Informática Bloque 1"
  - "Administración Electrónica AGE Master Guide"
---

# 🔴 Guía Maestra de Informática, Administración Electrónica y Marco Digital de la AGE (Bloque 1)

Compendio integral de toda la normativa TIC, infraestructuras, plataformas comunes, firma electrónica y gobierno digital exigidos en el **Bloque 1** para el Cuerpo TAI.

---

## 🗺️ Mapa de la Informática en el Bloque 1

```
                        MARCO DIGITAL DE LA ADMINISTRACIÓN PÚBLICA (BLOQUE 1)
                                                  │
       ┌──────────────────────────┬───────────────┴───────────────┬──────────────────────────┐
       ▼                          ▼                               ▼                          ▼
1. IDENTIDAD Y FIRMA     2. PROCEDIMIENTO DIGITAL      3. SERVICIOS COMUNES AGE    4. SEGURIDAD Y DATOS
 • eIDAS (Regl. 910/2014) • Ley 39/2015 (LPACAP)        • Red SARA (Testa/EuroDomain)• RGPD (Regl. 2016/679)
 • Ley 6/2020 (LSEC)      • Ley 40/2015 (LRJSP)         • Cl@ve (Identificación)    • LOPDGDD 3/2018 (Título X)
 • Tipos de Firma         • Documento/Expediente Elect. • SIR / GEISER / ORVE       • ENS (RD 311/2022)
 • DNIe (3.0 / 4.0)       • ENI (RD 4/2010) + NTIs      • Notific@, FACe, INSIDE    • AEPD / DPD / EIPD
```

---

## 📋 1. Los 5 Pilares TIC del Bloque 1

| Pilar TIC | Normativa Principal | Conceptos y Plataformas Esenciales |
|-----------|---------------------|-----------------------------------|
| **Identidad y Firma** | **Reglamento (UE) 910/2014 (eIDAS)** y **Ley 6/2020** | Firma Simple, Avanzada y Cualificada; Certificados cualificados, DNIe, Sellos de tiempo |
| **Procedimiento Electrónico** | **Ley 39/2015** (Arts. 13-14, 16, 26-28, 40-44) | Registro Electrónico General, Notificaciones Telemáticas, Archivo Electrónico Único |
| **Interoperabilidad y Normas Técnicas** | **Esquema Nacional de Interoperabilidad (ENI - RD 4/2010)** | Dimensiones Técnica, Semántica y Organizativa; Normas Técnicas de Interoperabilidad (NTIs) |
| **Infraestructuras y Servicios Comunes** | **Ley 40/2015** (Arts. 155-158) y Declaración de Servicios Compartidos | **Red SARA**, **Cl@ve**, **SIR**, **GEISER**, **FACe**, **INSIDE**, **ARCHIVE**, **PAGe**, **SIA** |
| **Privacidad y Derechos Digitales** | **RGPD** y **LOPDGDD 3/2018** (Título X: Arts. 79-97) | Desconexión digital, intimidad laboral (dispositivos/videovigilancia/geolocalización), testamento digital |

---

## 📚 Síntesis Específicas de la Sección
- [[wiki/synthesis/servicios-comunes-age-administracion-electronica-cheatsheet|Cheatsheet de Servicios Comunes e Infraestructuras Digitales de la AGE]]
- [[wiki/synthesis/firma-electronica-eidas-ley6-2020-dnie-guia|Guía de Identidad Digital, Reglamento eIDAS, Ley 6/2020 y DNIe]]
- [[wiki/synthesis/gestion-documento-y-expediente-electronico-eni-guia|Guía del Documento y Expediente Electrónico, Metadatos NTI y Archivo Único]]
- [[wiki/synthesis/derechos-digitales-titulo-x-lopdgdd-cheatsheet|Cheatsheet de Derechos Digitales (Título X LOPDGDD)]]

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema08|Resumen Ley 39/2015 LPACAP]]
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Ley 40/2015 LRJSP]]
- Fuente: [[wiki/sources/bloque1-tema10|Resumen RGPD y LOPDGDD]]
""",

    "wiki/synthesis/servicios-comunes-age-administracion-electronica-cheatsheet.md": """---
title: "Cheatsheet de Servicios Comunes, Plataformas e Infraestructuras Digitales de la AGE"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-1
  - administracion-electronica
  - red-sara
  - clave
  - face
  - geiser
  - inside
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Servicios Comunes AGE Cheatsheet"
  - "Catálogo Servicios Digitales AGE"
---

# 🔴 Cheatsheet de Servicios Comunes, Plataformas e Infraestructuras Digitales de la AGE

Tabla de memorización de las plataformas tecnológicas del Catálogo de Servicios de Administración Digital de la Secretaría General de Administración Digital (SGAD).

---

## 🏛️ Matriz Maestra de Servicios Comunes de la AGE

| Servicio / Plataforma | Nombre Completo / Acrónimo | Función Técnica Principal |
|-----------------------|----------------------------|---------------------------|
| **Red SARA** | **S**istema de **A**plicaciones y **R**edes para las **A**dministraciones | Red privada de alta velocidad y seguridad que interconecta todos los Ministerios, CCAA, EE.LL. y la Unión Europea (mediante sTESTA / EuroDomain). |
| **Cl@ve** | Plataforma de Identidad Digital | Sistema unificado de autenticación ciudadana: Cl@ve PIN (código temporal por SMS/App) y Cl@ve Permanente (usuario/contraseña + OTP). |
| **Cl@ve Firma** | Firma Centralizada en la Nube | Firma electrónica avanzada con certificados cualificados almacenados en servidores seguros (HSM) de la AGE. |
| **Autofirm@** | Cliente de Firma Local | Aplicación de escritorio desarrollada por el Ministerio para realizar firmas electrónicas avanzadas en navegadores web (sin applets Java). |
| **@Firma (VALIDe)** | Plataforma de Validación de Firma | Servicio horizontal de validación de certificados y firmas electrónicas multi-PKI y sede de validación para ciudadanos (**VALIDe**). |
| **SIR** | **S**istema de **I**nterconexión de **R**egistros | Plataforma troncal que permite el intercambio electrónico seguro de asientos registrales entre todas las Administraciones (conforme a norma SICRES 3.0). |
| **GEISER** | Gestión Integrada de Servicios de Registro | Solución integral en la nube para oficinas de registro de la AGE conectada a SIR. |
| **ORVE** | Oficina de Registro Virtual | Aplicación web para digitalizar y enviar documentos desde oficinas de registro de entidades locales hacia cualquier administración a través de SIR. |
| **Notific@** | Plataforma de Notificaciones | Plataforma centralizada para emisión y gestión de notificaciones telemáticas y papel (conecta con la **Dirección Electrónica Habilitada única - DEHú**). |
| **FACe** | Punto General de Entrada de Facturas Electrónicas | Ventanilla única estatal para la remisión de facturas electrónicas (**Facturae 3.2.x**) a cualquier organismo público. |
| **INSIDE** | Infraestructura y Servicios de Documentos Electrónicos | Sistema para la gestión, foliado y remisión de expedientes electrónicos entre administraciones y con la Administración de Justicia. |
| **ARCHIVE** | Archivo Electrónico Único | Solución modular para la conservación y preservación a largo plazo de documentos y expedientes electrónicos (conforme al modelo OAIS). |
| **PAGe** | Punto de Acceso General electrónico | Portal ciudadano estatal (`administracion.gob.es`) con sede electrónica, buscador de trámites y acceso a **Mi Carpeta Ciudadana**. |
| **SIA** | **S**istema de **I**nformación **A**dministrativa | Inventario oficial y normalizado de todos los procedimientos administrativos de la AGE y otras AAPP. |
| **PID (SCSP)** | Plataforma de Intermediación de Datos | Servicio para evitar que el ciudadano aporte certificados en papel (consulta telemática de títulos, padrón, IRPF, TGSS mediante protocolo SCSP). |

---

## ⚠️ Trampas Típicas en Test sobre Servicios Comunes
- **SIR vs GEISER/ORVE**: **SIR** es la *red de intercambio/interconexión*, mientras que **GEISER** y **ORVE** son las *aplicaciones cliente de registro* que se conectan a SIR.
- **INSIDE vs ARCHIVE**: **INSIDE** gestiona el expediente durante su *tramitación activa e intercambio*; **ARCHIVE** gestiona la *custodia y preservación a largo plazo*.
- **FACe**: Exige el uso del formato estándar **Facturae** (XML firmado con XAdES).

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/servicios-comunes-administracion-electronica|Servicios Comunes de Administración Electrónica]]
- Guía: [[wiki/synthesis/bloque1-informatica-y-administracion-digital-master-guide|Guía Maestra Informática Bloque 1]]
""",

    "wiki/synthesis/firma-electronica-eidas-ley6-2020-dnie-guia.md": """---
title: "Guía de Identidad Digital, Reglamento eIDAS, Ley 6/2020 y DNI Electrónico (DNIe)"
type: "synthesis"
tags:
  - synthesis
  - firma-electronica
  - eidas
  - ley-6-2020
  - dnie
  - criptografia
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Firma Electrónica y eIDAS"
  - "eIDAS y Ley 6/2020 Guía"
---

# 🔴 Guía de Identidad Digital, Reglamento eIDAS, Ley 6/2020 y DNI Electrónico (DNIe)

Estudio técnico-jurídico del **Reglamento (UE) 910/2014 (eIDAS)**, la **Ley 6/2020** de servicios electrónicos de confianza y el **DNI Electrónico**.

---

## 🏛️ 1. Tipos de Firma Electrónica según el Reglamento eIDAS

```
                                  JERARQUÍA DE FIRMAS ELECTRÓNICAS
                                                 │
          ┌──────────────────────────────────────┼──────────────────────────────────────┐
          ▼                                      ▼                                      ▼
1. FIRMA SIMPLE                        2. FIRMA AVANZADA                      3. FIRMA CUALIFICADA
• Datos en formato electrónico         • Vinculada al firmante de             • Creada mediante un Dispositivo
  asociados a otros datos para           manera única.                          Cualificado de Creación de Firma
  identificar al firmante.             • Permite identificar al firmante.       (QSCD / tarjeta criptográfica).
• Ejemplo: PIN, usuario/password,      • Creada con datos de creación bajo    • Basada en un Certificado Cualificado.
  casilla acepto condiciones.            control exclusivo del firmante.      • **EQUIVALENCIA PLENA A LA FIRMA**
                                       • Detecta cualquier cambio posterior.    **MANUSCRITA EN TODA LA UE**.
```

---

## 📜 2. Novedades de la Ley 6/2020 (LSEC) frente a la derogada Ley 59/2003

- **Derogación**: La Ley 6/2020, de 11 de noviembre, deroga expresamente la Ley 59/2003 de Firma Electrónica para adaptarse al Reglamento eIDAS.
- **Servicios de Confianza Regulados**:
  1. Creación, verificación y validación de firmas y sellos electrónicos.
  2. Creación, verificación y validación de sellos de tiempo electrónicos.
  3. Servicios de entrega electrónica certificada.
  4. Certificados para autenticación de sitios web (SSL/TLS).
  5. Conservación de firmas y sellos electrónicos.
- **Supervisión**: Corresponde al Ministerio para la Transformación Digital y de la Función Pública.

---

## 🪪 3. El DNI Electrónico (DNIe 3.0 / DNI 4.0)

- **Chip Criptográfico**: Almacena dos pares de claves y sus respectivos certificados X.509 v3 expedidos por la Dirección General de la Policía (DGP):
  1. **Certificado de Autenticación**: Garantiza la identidad electrónica del ciudadano ante sistemas telemáticos.
  2. **Certificado de Firma**: Permite la firma cualificada de documentos electrónicos con validez legal manuscrita.
- **Evolución del DNIe**:
  - **DNIe 1.0/2.0**: Contacto físico mediante chip inteligente (*Smart Card* con lector de tarjetas).
  - **DNIe 3.0**: Incorpora tecnología inalámbrica **NFC (Near Field Communication)** según norma ISO/IEC 14443.
  - **DNI 4.0 (DNI Europeo)**: Conforme al Reglamento (UE) 2019/1157, preparado para integración en el futuro *European Digital Identity Wallet*.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/firma-electronica-y-reglamento-eidas|Firma Electrónica y eIDAS]]
- Entidad: [[wiki/entities/dnie-dni-electronico|DNI Electrónico]]
""",

    "wiki/synthesis/gestion-documento-y-expediente-electronico-eni-guia.md": """---
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
""",

    "wiki/synthesis/derechos-digitales-titulo-x-lopdgdd-cheatsheet.md": """---
title: "Cheatsheet de Derechos Digitales: Título X de la LOPDGDD (Artículos 79 al 97)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - derechos-digitales
  - lopdgdd
  - rgpd
  - privacidad
sources:
  - "raw/sources/bloque1-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Derechos Digitales Título X Cheatsheet"
  - "Garantía de los Derechos Digitales"
---

# 🔴 Cheatsheet de Derechos Digitales: Título X de la LOPDGDD (Artículos 79 al 97)

Tabla de repaso de la **Ley Orgánica 3/2018 (LOPDGDD)**, pionera en Europa en incorporar un título específico dedicado a la garantía de los derechos digitales de la ciudadanía.

---

## 📱 Matriz de los Derechos Digitales (Artículos 79 a 97)

| Artículo | Derecho Digital Reconocido | Contenido Clave de Examen |
|----------|----------------------------|---------------------------|
| **Art. 79** | **Neutralidad de la Red** | Acceso a internet sin discriminación técnica ni tarifaria por tipo de tráfico o contenido. |
| **Art. 80** | **Acceso Universal a Internet** | Acceso universal, asequible y de calidad en todo el territorio. |
| **Art. 81** | **Seguridad Digital** | Derecho a la seguridad en las comunicaciones electrónicas de los usuarios. |
| **Art. 82** | **Educación Digital** | Formación en competencias digitales en el sistema educativo y universidad. |
| **Art. 83** | **Protección de Menores en Internet** | Uso seguro y responsable; consentimiento para redes sociales fijado a partir de los **14 años** en España. |
| **Art. 84** | **Rectificación en Internet** | Rectificación de información falsa o inexacta en medios de comunicación digitales y redes sociales. |
| **Art. 85** | **Actualización de Noticias Digitales** | Derecho a que los medios digitales añadan un aviso de actualización en noticias con desenlace posterior favorable al afectado. |
| **Art. 86** | **Olvido en Buscadores de Internet** | Supresión de resultados en motores de búsqueda cuando los datos sean obsoletos, inexactos o no pertinentes. |
| **Art. 87** | **Intimidad y Dispositivos en el Trabajo** | Criterios claros de uso de dispositivos de empresa; prohibido uso extralaboral sin autorización expresa. |
| **Art. 88** | **Desconexión Digital en el Ámbito Laboral** | Derecho del trabajador a no responder llamadas, emails o mensajes fuera de su horario laboral para garantizar su descanso. |
| **Art. 89** | **Intimidad frente a Videovigilancia Laboral** | Permitida para control laboral previo aviso expreso; **estrictamente prohibida en vestuarios, comedores y zonas de descanso**. |
| **Art. 90** | **Intimidad frente a Geolocalización Laboral** | Uso de GPS en el trabajo permitido solo si es necesario, informando previamente al empleado de su existencia. |
| **Art. 96** | **Testamento Digital** | Acceso, supresión o gestión de los contenidos digitales de personas fallecidas por sus herederos legítimos salvo prohibición expresa. |

---

## ⚠️ Preguntas Típicas de Examen sobre Derechos Digitales
- **Edad de consentimiento para redes sociales en España**: **14 años** (Art. 7 LOPDGDD y Art. 83).
- **Cámaras en el trabajo**: Se debe informar a los trabajadores con el distintivo amarillo/blanco y aviso previo. Prohibido audio y zonas de descanso.
- **Desconexión digital**: Obligación de la empresa de elaborar una política interna de desconexión previa consulta con los representantes sindicales.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema10|Resumen RGPD y LOPDGDD]]
- Entidad: [[wiki/entities/rgpd-y-lopdgdd|RGPD y LOPDGDD]]
"""
}

print("[*] Escribiendo 5 guías maestras y cheatsheets de la sección de Informática del Bloque 1...")
for path, content in NOTES.items():
    write_file(path, content)

print("[*] Sección de Informática del Bloque 1 creada exitosamente.")
