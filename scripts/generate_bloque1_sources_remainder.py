# -*- coding: utf-8 -*-
"""
Script generador integral de todas las notas del Bloque 1 (TAI):
- Sources 03 al 10
- 12 Entities
- 8 Concepts
- 8 Syntheses
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

# ==============================================================================
# WIKI SOURCES (Temas 03 al 10)
# ==============================================================================

WIKI_SOURCES_REMAINDER = {
    "wiki/sources/bloque1-tema03.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 03: Organización Territorial del Estado y Entidades Locales"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema03
  - comunidades-autonomas
  - administracion-local
  - estatutos-autonomia
sources:
  - "raw/sources/bloque1-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Organización Territorial y Entidades Locales"
  - "bloque1-tema03"
---

# Resumen Fuente: Bloque 1 - Tema 03: Organización Territorial del Estado y Entidades Locales

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema03.md|bloque1-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema abarca la estructura territorial del Estado según el Título VIII de la Constitución Española de 1978: los principios de unidad, autonomía, solidaridad (Fondo de Compensación Interterritorial) e igualdad; las vías de acceso a la autonomía (vía ordinaria del art. 143 y vía especial del art. 151), la naturaleza de los Estatutos de Autonomía aprobados por Ley Orgánica, la distribución competencial (art. 148 y 149 CE) con sus cláusulas de cierre (residual, prevalencia y supletoriedad), las formas de control e intervención estatal (Art. 155 CE aprobado por mayoría absoluta del Senado), y el régimen de la Administración Local (Municipios, Provincias e Islas según la Ley 7/1985 LRBRL).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro Constitucional | Especificación |
|--------------------------|----------------|
| Principio de Solidaridad | **Fondo de Compensación Interterritorial** (Art. 158.2 CE) |
| Aprobación Estatuto de Autonomía | **Ley Orgánica** (Art. 81 y 147 CE) |
| Competencias Exclusivas del Estado | **Artículo 149.1 CE** (32 materias) |
| Cláusulas de Cierre | **Residual** (CCAA o Estado), **Prevalencia** y **Supletoriedad** (Art. 149.3) |
| Mecanismo Coerción Estatal (Art. 155) | Aprobado por **Mayoría Absoluta del Senado** |
| Elementos del Municipio | **Territorio**, **Población (Padrón)** y **Organización (Ayuntamiento)** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/comunidades-autonomas-y-ee-ll|Comunidades Autónomas y Entidades Locales]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
""",

    "wiki/sources/bloque1-tema04.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 04: La Unión Europea, Instituciones y Derecho Comunitario"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema04
  - union-europea
  - parlamento-europeo
  - comision-europea
  - tjue
sources:
  - "raw/sources/bloque1-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen La Unión Europea y Derecho Comunitario"
  - "bloque1-tema04"
---

# Resumen Fuente: Bloque 1 - Tema 04: La Unión Europea, Instituciones y Derecho Comunitario

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema04.md|bloque1-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en la arquitectura política y jurídica de la Unión Europea: la evolución de los Tratados constitutivos hasta el **Tratado de Lisboa de 2007** (en vigor el 1 de diciembre de 2009 con personalidad jurídica única, TUE, TFUE y Carta de Derechos Fundamentales vinculante); la composición y funciones de las instituciones clave (Parlamento Europeo elegido cada 5 años, Consejo Europeo, Consejo de la UE con Mayoría Cualificada del 55%/65%, Comisión Europea como guardiana de los tratados y TJUE en Luxemburgo); y el sistema de fuentes comunitarias (Reglamentos directamente aplicables vs Directivas con transposición) y principios de **Primacía** y **Efecto Directo**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Institución / Norma | Característica Clave |
|---------------------|----------------------|
| Entrada en vigor Tratado de Lisboa | **1 de diciembre de 2009** |
| Mandato Parlamento Europeo | **5 años** (Sufragio universal directo) |
| Mayoría Cualificada en el Consejo | **55% de Estados miembros (mínimo 15)** que representen al **65% de la población** |
| Reglamento Comunitario | Alcance general, obligatorio y **directamente aplicable** sin transposición |
| Directiva Comunitaria | Obliga en el resultado (**requiere transposición nacional** en plazo) |
| Principio de Primacía | **Sentencia Costa c. ENEL (1964)** |
| Principio de Efecto Directo | **Sentencia Van Gend en Loos (1963)** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/instituciones-union-europea|Instituciones de la Unión Europea]]
- Concepto: [[wiki/concepts/fuentes-derecho-comunitario|Fuentes del Derecho Comunitario y Principios de Aplicación]]
- Síntesis: [[wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia|Guía de Instituciones Europeas, Composición y Sedes]]
""",

    "wiki/sources/bloque1-tema05.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 05: El Personal Funcionario al Servicio de las AAPP (TREBEP)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema05
  - trebep
  - empleado-publico
  - situaciones-administrativas
  - regimen-disciplinario
sources:
  - "raw/sources/bloque1-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen El Empleado Público y el TREBEP"
  - "bloque1-tema05"
---

# Resumen Fuente: Bloque 1 - Tema 05: El Personal Funcionario al Servicio de las AAPP (TREBEP)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema05.md|bloque1-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda el régimen estatutario del empleo público en España regulado por el **Real Decreto Legislativo 5/2015 (TREBEP)**: clasificación del personal (funcionarios de carrera e interinos, personal laboral y eventual), grupos de clasificación profesional (Subgrupos A1, A2, Grupo B, Subgrupos C1, C2), derechos y código de conducta (principios éticos y de conducta), situaciones administrativas (servicio activo, servicios especiales, excedencias voluntarias e involuntarias, suspensión de funciones) y el régimen disciplinario con la tipificación y plazos de prescripción de faltas y sanciones.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro TREBEP | Valor Legal |
|------------------|-------------|
| Texto Legal Vigente | **Real Decreto Legislativo 5/2015**, de 30 de octubre |
| Titulación Subgrupo A1 / A2 | **Título Universitario de Grado** |
| Titulación Subgrupo C1 / C2 | **Bachiller/FP Grado Medio** (C1) / **Graduado en ESO** (C2) |
| Excedencia por Interés Particular | Requiere **5 años** de servicio previo; duración mínima **2 años** (no computa) |
| Excedencia Cuidado Familiares | Máximo **3 años** (computa para trienios, carrera y reserva puesto 2 años) |
| Prescripción Faltas | **Muy graves: 3 años** \| **Graves: 2 años** \| **Leves: 6 meses** |
| Prescripción Sanciones | **Muy graves: 3 años** \| **Graves: 2 años** \| **Leves: 1 año** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/trebep-empleado-publico|TREBEP y Clases de Empleados Públicos]]
- Concepto: [[wiki/concepts/situaciones-administrativas-funcionarios|Situaciones Administrativas de los Funcionarios de Carrera]]
- Síntesis: [[wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia|Guía del TREBEP: Situaciones y Régimen Disciplinario]]
""",

    "wiki/sources/bloque1-tema06.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 06: Políticas de Igualdad y Violencia de Género"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema06
  - igualdad
  - violencia-genero
  - lo-3-2007
  - lo-1-2004
sources:
  - "raw/sources/bloque1-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Políticas de Igualdad y Violencia de Género"
  - "bloque1-tema06"
---

# Resumen Fuente: Bloque 1 - Tema 06: Políticas de Igualdad y Violencia de Género

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema06.md|bloque1-tema06.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza las políticas públicas de igualdad de género y lucha contra la violencia sobre la mujer: la **Ley Orgánica 3/2007 para la igualdad efectiva de mujeres y hombres** (conceptos de discriminación directa e indirecta, acoso sexual y por razón de sexo, acciones positivas, transversalidad *mainstreaming*, presencia equilibrada 40/60% y obligatoriedad de planes de igualdad en empresas de 50 o más trabajadores); y la **Ley Orgánica 1/2004 de Medidas de Protección Integral contra la Violencia de Género** (definición, derechos laborales y asistenciales de las víctimas, y Juzgados de Violencia sobre la Mujer).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Norma | Especificación |
|------------------|----------------|
| Ley Orgánica de Igualdad | **Ley Orgánica 3/2007**, de 22 de marzo |
| Ley de Violencia de Género | **Ley Orgánica 1/2004**, de 28 de diciembre |
| Obligación Planes de Igualdad | Empresas de **50 o más personas trabajadoras** |
| Presencia Equilibrada | Ningún sexo con porcentaje inferior al **40%** ni superior al **60%** |
| Ámbito Violencia de Género | Ejercida por quienes sean o hayan sido **cónyuges o relaciones de afectividad similares, aun sin convivencia** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ley-igualdad-y-violencia-genero|Leyes de Igualdad (LO 3/2007) y Violencia de Género (LO 1/2004)]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
""",

    "wiki/sources/bloque1-tema07.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 07: El Procedimiento Administrativo Común (Ley 39/2015 LPACAP)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema07
  - lpacap
  - ley-39-2015
  - actos-administrativos
  - recursos-administrativos
  - plazos
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Procedimiento Administrativo Común LPACAP"
  - "bloque1-tema07"
---

# Resumen Fuente: Bloque 1 - Tema 07: El Procedimiento Administrativo Común (Ley 39/2015 LPACAP)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema07.md|bloque1-tema07.md]].

---

## 📖 Resumen Ejecutivo

Este tema constituye el pilar procedimental de las Administraciones Públicas: la **Ley 39/2015 (LPACAP)**. Detalla los sujetos obligados a la relación electrónica (personas jurídicas, profesionales colegiados y empleados públicos), el régimen de cómputo de plazos (días hábiles excluyendo sábados, domingos y festivos; cómputo de fecha a fecha en meses), la teoría de la invalidez de los actos administrativos distinguiendo los **casos tasados de nulidad de pleno derecho (Art. 47)** de la **anulabilidad (Art. 48)** y su convalidación, las fases del procedimiento (iniciación, ordenación, instrucción con audiencia de 10-15 días y finalización) y el régimen de recursos administrativos (**Alzada, Reposición y Revisión**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento LPACAP | Regla / Plazo |
|-----------------|---------------|
| Días Hábiles Administrativos | **Excluyen sábados, domingos y festivos** |
| Plazo Recurso de Alzada | Interposición: **1 mes** (expreso) \| Resolución: **3 meses** (Silencio Desestimatorio) |
| Plazo Recurso de Reposición | Interposición: **1 mes** (expreso) \| Resolución: **1 mes** (Silencio Desestimatorio) |
| Plazo Trámite de Audiencia | **10 a 15 días hábiles** |
| Plazo de Caducidad por Paralización | **3 meses** por causa imputable al interesado |
| Obligados a Relación Electrónica | Personas jurídicas, entidades sin personalidad, colegiados y **empleados públicos** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ley-39-2015-lpacap|Ley 39/2015 LPACAP]]
- Concepto: [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos|Eficacia, Validez, Nulidad y Anulabilidad de Actos]]
- Concepto: [[wiki/concepts/recursos-administrativos-y-plazos|Recursos Administrativos y Régimen de Plazos]]
- Concepto: [[wiki/concepts/computo-de-plazos-administrativos|Cómputo de Plazos Administrativos]]
- Síntesis: [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Cheatsheet de Plazos del Procedimiento Administrativo]]
- Síntesis: [[wiki/synthesis/recursos-administrativos-comparativa-guia|Guía Comparativa de Recursos Administrativos]]
- Síntesis: [[wiki/synthesis/actos-nulos-vs-anulables-guia|Guía de Actos Nulos vs Anulables]]
""",

    "wiki/sources/bloque1-tema08.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 08: Régimen Jurídico del Sector Público (Ley 40/2015 LRJSP)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema08
  - lrjsp
  - ley-40-2015
  - organos-colegiados
  - responsabilidad-patrimonial
  - administracion-electronica
sources:
  - "raw/sources/bloque1-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Régimen Jurídico del Sector Público LRJSP"
  - "bloque1-tema08"
---

# Resumen Fuente: Bloque 1 - Tema 08: Régimen Jurídico del Sector Público (Ley 40/2015 LRJSP)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema08.md|bloque1-tema08.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en la organización y funcionamiento interno del sector público según la **Ley 40/2015 (LRJSP)**: principios generales (eficacia, jerarquía, descentralización, desconcentración, cooperación), la administración electrónica institucional (sedes electrónicas, portales de internet, Punto de Acceso General Electrónico PAGe, actuaciones administrativas automatizadas, certificados y sellos electrónicos, ENI y ENS), el régimen de funcionamiento de los órganos colegiados (convocatorias, quórum, abstención obligatoria de funcionarios, actas) y la **responsabilidad patrimonial de las Administraciones Públicas** (requisitos del daño efectivo, nexo causal y prescripción anual).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro LRJSP | Especificación Legal |
|-----------------|----------------------|
| Sede Electrónica (Art. 38) | Dirección electrónica bajo titularidad de una Administración con certificado de sede |
| Actuación Administrativa Automatizada | Acto realizado íntegramente por medios electrónicos sin intervención humana directa (Sello/CSV) |
| Órganos Colegiados Quórum | Presencia del Presidente, Secretario y al menos **la mitad de los miembros** |
| Prescripción Responsabilidad Patrimonial | **1 año** desde el hecho lesivo o determinación de secuelas (Art. 67 Ley 39/2015) |
| Marcos Estatales de Seguridad e Interoperabilidad | **ENS (Esquema Nacional de Seguridad)** y **ENI (Esquema Nacional de Interoperabilidad)** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ley-40-2015-lrjsp|Ley 40/2015 LRJSP]]
- Concepto: [[wiki/concepts/responsabilidad-patrimonial-administracion|Responsabilidad Patrimonial de las Administraciones Públicas]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
""",

    "wiki/sources/bloque1-tema09.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 09: Protección de Datos Personales (RGPD y LOPDGDD)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema09
  - rgpd
  - lopdgdd
  - proteccion-datos
  - aepd
  - derechos-arco-pol
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Protección de Datos RGPD y LOPDGDD"
  - "bloque1-tema09"
---

# Resumen Fuente: Bloque 1 - Tema 09: Protección de Datos Personales (RGPD y LOPDGDD)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema09.md|bloque1-tema09.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la normativa europea y nacional de protección de datos: el **Reglamento (UE) 2016/679 (RGPD)** y la **Ley Orgánica 3/2018 (LOPDGDD)**. Se analizan los principios del tratamiento (licitud, lealtad, transparencia, limitación de la finalidad, minimización de datos, exactitud, limitación de conservación, integridad/confidencialidad y responsabilidad proactiva o *accountability*), las 6 bases jurídicas de legitimación, el catálogo de derechos ciudadanos (**ARCO-POL**: Acceso, Rectificación, Supresión/Olvido, Limitación, Portabilidad, Oposición y no sumisión a decisiones automatizadas/perfiles), la figura del **Delegado de Protección de Datos (DPD/DPO)** obligatorio en el sector público, y las potestades de la **Agencia Española de Protección de Datos (AEPD)**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Legal |
|-----------|----------------------|
| Aplicación RGPD | **25 de mayo de 2018** (Reglamento UE 2016/679) |
| Ley Española de Adaptación | **Ley Orgánica 3/2018**, de 5 de diciembre (LOPDGDD) |
| Plazo General de Respuesta Derechos ARCO-POL | **1 mes** desde la recepción de la solicitud (prorrogable 2 meses más) |
| DPD en el Sector Público | **Obligatorio por Ley** para todas las autoridades y organismos públicos |
| Comunicación DPD a la AEPD | En el plazo de **10 días** desde su designación |
| Sanción a AAPP por Infracción de Datos | **Apercibimiento formal** (sin multa económica en AAPP españolas, Art. 77 LOPDGDD) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/rgpd-y-lopdgdd|RGPD y LOPDGDD]]
- Entidad: [[wiki/entities/aepd-agencia-proteccion-datos|Agencia Española de Protección de Datos (AEPD)]]
- Concepto: [[wiki/concepts/derechos-digitales-y-arco-pol|Derechos Ciudadanos ARCO-POL y Derechos Digitales]]
- Síntesis: [[wiki/synthesis/rgpd-lopdgdd-derechos-y-sanciones-guia|Guía del RGPD y LOPDGDD: Principios, Derechos y DPD]]
""",

    "wiki/sources/bloque1-tema10.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 10: Transparencia y Acceso a la Información Pública (Ley 19/2013)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema10
  - transparencia
  - buen-gobierno
  - ley-19-2013
  - consejo-transparencia
sources:
  - "raw/sources/bloque1-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Transparencia y Buen Gobierno"
  - "bloque1-tema10"
---

# Resumen Fuente: Bloque 1 - Tema 10: Transparencia y Acceso a la Información Pública (Ley 19/2013)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema10.md|bloque1-tema10.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza la **Ley 19/2013 de Transparencia, Acceso a la Información Pública y Buen Gobierno**: el doble pilar de la transparencia formado por la **Publicidad Activa** (obligación de publicar de oficio información institucional, jurídica y económico-presupuestaria en el Portal de la Transparencia) y el **Derecho de Acceso a la Información Pública** (solicitud universal sin necesidad de motivar, límites tasados, plazo de resolución de 1 mes con silencio negativo/desestimatorio), la reclamación potestativa ante el **Consejo de Transparencia y Buen Gobierno (CTBG)** y los principios de buen gobierno.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro Ley 19/2013 | Especificación |
|-----------------------|----------------|
| Norma de Transparencia | **Ley 19/2013**, de 9 de diciembre |
| Motivación de Solicitud de Acceso | **No requerida** (el solicitante no necesita justificar su interés) |
| Plazo de Resolución de Acceso | **1 mes** (prorrogable otro mes en casos complejos) |
| Silencio Administrativo en Acceso | **DESESTIMATORIO** (Silencio negativo) |
| Plazo Reclamación ante el Consejo de Transparencia | **1 mes** desde la notificación o silencio |
| Plazo Resolución Reclamación Consejo | **3 meses** (Silencio desestimatorio) |
| Mandato Presidente Consejo Transparencia | **5 años no renovable** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ley-19-2013-transparencia|Ley 19/2013 de Transparencia y Buen Gobierno]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
"""
}

print("[*] Escribiendo fuentes wiki/sources/bloque1-tema03 a tema10...")
for path, content in WIKI_SOURCES_REMAINDER.items():
    write_file(path, content)

print("[*] Fuentes completadas.")
