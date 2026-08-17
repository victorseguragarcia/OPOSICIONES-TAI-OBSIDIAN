# -*- coding: utf-8 -*-
"""
Script generador de Entidades, Conceptos y Síntesis de Estudio del Bloque 1 para TAI.
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
# ENTIDADES BLOQUE 1 (12 Fichas)
# ==============================================================================

BLOQUE1_ENTITIES = {
    "wiki/entities/constitucion-espanola-1978.md": """---
title: "Constitución Española de 1978"
type: "entity"
tags:
  - constitucion
  - derecho-constitucional
  - estado-de-derecho
  - corona
  - cortes-generales
sources:
  - "raw/sources/bloque1-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Constitución Española"
  - "CE 1978"
  - "Carta Magna"
---

# Constitución Española de 1978

La **Constitución Española de 1978** es la norma jurídica suprema y fundamental del ordenamiento jurídico del Reino de España, aprobada por las Cortes Generales el 31 de octubre de 1978, ratificada en referéndum el 6 de diciembre de 1978 y en vigor desde su publicación en el BOE el **29 de diciembre de 1978**.

---

## 🏛️ Estructura y Títulos

- **169 Artículos**, 1 Preámbulo, 1 Título Preliminar, 10 Títulos numerados, 4 Disposiciones Adicionales, 9 Disposiciones Transitorias, 1 Disposición Derogatoria y 1 Disposición Final.
- **Valores Superiores (Art. 1.1)**: Libertad, Justicia, Igualdad y Pluralismo político.
- **Forma Política (Art. 1.3)**: Monarquía parlamentaria.
- **Principios Jurídicos (Art. 9.3)**: Legalidad, jerarquía normativa, publicidad, irretroactividad de disposiciones sancionadoras desfavorables, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad de los poderes públicos.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto Constitucional | Especificación |
|------------------------|----------------|
| Fecha de Publicación y Entrada en Vigor | **29 de diciembre de 1978** |
| Mayoría Ley Orgánica (Art. 81) | **Mayoría Absoluta del Congreso** en votación final de conjunto |
| Composición Tribunal Constitucional | **12 miembros** nombrados por el Rey por **9 años** (renovación de 4 cada 3 años) |
| Reforma Ordinaria vs Agravada | Art. 167 (**3/5 Cámaras**) vs Art. 168 (**2/3 Cámaras + Disolución + Referéndum obligatorio**) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema01|Resumen Bloque 1 - Tema 01]]
- Entidad: [[wiki/entities/cortes-generales|Cortes Generales]]
- Concepto: [[wiki/concepts/derechos-fundamentales-y-libertades-publicas|Derechos Fundamentales y Garantías]]
- Síntesis: [[wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet|Cheatsheet de Artículos Clave de la CE]]
""",

    "wiki/entities/cortes-generales.md": """---
title: "Cortes Generales: Congreso de los Diputados y Senado"
type: "entity"
tags:
  - cortes-generales
  - congreso
  - senado
  - poder-legislativo
sources:
  - "raw/sources/bloque1-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cortes Generales"
  - "Congreso de los Diputados"
  - "Senado"
---

# Cortes Generales: Congreso de los Diputados y Senado

Las **Cortes Generales** representan al pueblo español y ejercen el Poder Legislativo del Estado, aprueban sus Presupuestos Generales y controlan la acción del Gobierno mediante un sistema de **bicameralismo imperfecto**.

---

## 🏛️ Composición y Cámaras

- **Congreso de los Diputados (Cámara Baja - Art. 68 CE)**:
  - Entre 300 y 400 diputados (fijado en **350 por la LOREG**).
  - Circunscripción electoral provincial (Ceuta y Melilla eligen 1 diputado cada una).
  - Sistema de elección proporcional mediante la **regla D'Hondt**. Mandato de 4 años.
- **Senado (Cámara Alta / Representación Territorial - Art. 69 CE)**:
  - **Senadores Provinciales**: 4 por provincia peninsular; 3 por isla mayor; 1 por isla menor; 2 por Ceuta y 2 por Melilla.
  - **Senadores Autonómicos**: Designados por las Asambleas Legislativas autonómicas: **1 fijo por Comunidad Autónoma + 1 adicional por cada millón de habitantes**. Mandato de 4 años.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Legal |
|-----------|-------------|
| Número de Diputados en el Congreso | **350 Diputados** (LOREG) |
| Periodos Ordinarios de Sesiones | **Septiembre a Diciembre** (1º) y **Febrero a Junio** (2º) |
| Convalidación Real Decreto-Ley | **30 días naturales** ante el Congreso (Art. 86 CE) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema01|Resumen Bloque 1 - Tema 01]]
- Entidad: [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]]
""",

    "wiki/entities/gobierno-y-age.md": """---
title: "El Gobierno y la Administración General del Estado (AGE)"
type: "entity"
tags:
  - gobierno
  - age
  - consejo-ministros
  - poder-ejecutivo
sources:
  - "raw/sources/bloque1-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "El Gobierno"
  - "AGE"
  - "Administración General del Estado"
---

# El Gobierno y la Administración General del Estado (AGE)

El **Gobierno** dirige la política interior y exterior, la administración civil y militar y la defensa del Estado, ejerciendo la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes (Ley 50/1997 y Ley 40/2015).

---

## 🏛️ Clasificación de Órganos en la AGE (Art. 55 Ley 40/2015)

1. **Órganos Superiores** (Fijan planes de actuación):
   - **Ministros** (Jefes de departamento).
   - **Secretarios de Estado** (Dirección sectorial).
   - *Nombramiento*: Libre designación política (no se exige ser funcionario).
2. **Órganos Directivos** (Ejecución y gestión):
   - **Subsecretarios** y **Secretarios Generales Técnicos**: Nombramiento obligatorio entre **funcionarios del Subgrupo A1**.
   - **Directores Generales**: Nombramiento entre **funcionarios del Subgrupo A1** (salvo excepciones motivadas en el RD de estructura).
   - **Subdirectores Generales**: Nombramiento obligatorio entre **funcionarios del Subgrupo A1** (sin excepciones).
   - **Delegados del Gobierno en las CCAA** (Rango Subsecretario) y **Subdelegados del Gobierno en las provincias** (Rango Subdirector General, obligatoriamente **funcionario A1**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Cargo / Órgano | Rango Administrativo / Requisito |
|----------------|----------------------------------|
| Delegado del Gobierno | Rango de **Subsecretario** (libre nombramiento por RD) |
| Subdelegado del Gobierno | Rango de **Subdirector General** (**Funcionario A1 obligatorio**) |
| Órgano Preparatorio Consejo Ministros | **Comisión General de Secretarios de Estado y Subsecretarios** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema02|Resumen Bloque 1 - Tema 02]]
- Entidad: [[wiki/entities/ley-40-2015-lrjsp|Ley 40/2015 LRJSP]]
""",

    "wiki/entities/comunidades-autonomas-y-ee-ll.md": """---
title: "Comunidades Autónomas y Entidades Locales"
type: "entity"
tags:
  - comunidades-autonomas
  - administracion-local
  - estatutos-autonomia
  - ayuntamientos
sources:
  - "raw/sources/bloque1-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comunidades Autónomas"
  - "Entidades Locales"
---

# Comunidades Autónomas y Entidades Locales

La organización territorial del Estado se fundamenta en el Título VIII de la Constitución Española y la Ley 7/1985 (LRBRL), articulando el Estado en **Municipios**, **Provincias** y **Comunidades Autónomas**.

---

## 🏛️ Conceptos y Distribución de Competencias

- **Estatutos de Autonomía**: Aprobados mediante **Ley Orgánica**.
- **Competencias**: Art. 148 CE (asumibles por CCAA) y Art. 149.1 CE (exclusivas del Estado en 32 materias).
- **Cláusulas de Cierre (Art. 149.3 CE)**: Residual, Prevalencia del derecho estatal y Supletoriedad.
- **Coerción Estatal (Art. 155 CE)**: Aprobada por **mayoría absoluta del Senado**.
- **Entidades Locales Básicas**:
  - **Municipio**: Territorio, Población (Padrón) y Ayuntamiento (Alcalde y Concejales).
  - **Provincia**: Entidad local determinada por la agrupación de municipios y gobernada por la **Diputación Provincial**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Legal |
|----------|----------------------|
| Mecanismo Art. 155 CE | Requiere requerimiento previo al Presidente de la CA y aprobación por **Mayoría Absoluta del Senado** |
| Fondo de Nivelación Territorial | **Fondo de Compensación Interterritorial** (Art. 158.2 CE) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema03|Resumen Bloque 1 - Tema 03]]
- Entidad: [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]]
""",

    "wiki/entities/instituciones-union-europea.md": """---
title: "Instituciones de la Unión Europea"
type: "entity"
tags:
  - union-europea
  - parlamento-europeo
  - comision-europea
  - consejo-ue
  - tjue
sources:
  - "raw/sources/bloque1-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Instituciones UE"
  - "Unión Europea"
---

# Instituciones de la Unión Europea

Las instituciones de la Unión Europea ejercen las competencias delegadas por los Estados miembros en el marco del **Tratado de la Unión Europea (TUE)** y el **Tratado de Funcionamiento de la Unión Europea (TFUE)** tras el Tratado de Lisboa (2009).

---

## 🏛️ Cuadro Institucional de la UE

| Institución | Representa a | Sede Oficial | Mandato / Composición | Función Principal |
|-------------|--------------|--------------|-----------------------|-------------------|
| **Parlamento Europeo** | **Ciudadanos de la UE** | Estrasburgo | 5 años (máx 750 + Presidente) | Colegislador, control político y presupuestario |
| **Consejo Europeo** | Jefes de Estado/Gobierno | Bruselas | Presidente (2,5 años) | Define orientaciones políticas (**NO legisla**) |
| **El Consejo (de la UE)** | **Gobiernos de los Estados** | Bruselas | Nivel ministerial (Presidencia semestral) | Colegislador (Mayoría Cualificada 55%/65%) |
| **Comisión Europea** | **Interés General de la UE** | Bruselas | 5 años (1 Comisario por Estado) | Iniciativa legislativa ("Guardiana de Tratados") |
| **TJUE** | El Derecho y los Tratados | Luxemburgo | Tribunal de Justicia + Tribunal General | Interpretación uniforme y control de legalidad |
| **BCE** | Estabilidad del Euro | Fráncfort | Comité Ejecutivo + Consejo de Gobierno | Política monetaria de la zona euro |
| **Tribunal de Cuentas** | Finanzas de la Unión | Luxemburgo | 1 miembro por Estado (6 años) | Fiscalización de ingresos y gastos de la UE |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Regla Técnica |
|-----------|---------------|
| Mayoría Cualificada Consejo UE | **55% de Estados miembros (mínimo 15)** que sumen al menos el **65% de la población** |
| Fuentes Vinculantes | **Reglamentos** (directamente aplicables), **Directivas** (requieren transposición) y **Decisiones** |
| Fuentes No Vinculantes | **Recomendaciones** y **Dictámenes** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema04|Resumen Bloque 1 - Tema 04]]
- Concepto: [[wiki/concepts/fuentes-derecho-comunitario|Fuentes del Derecho Comunitario]]
- Síntesis: [[wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia|Guía de Instituciones Europeas]]
""",

    "wiki/entities/trebep-empleado-publico.md": """---
title: "TREBEP: Estatuto Básico del Empleado Público (RD Legislativo 5/2015)"
type: "entity"
tags:
  - trebep
  - empleado-publico
  - funcionarios
  - situaciones-administrativas
  - regimen-disciplinario
sources:
  - "raw/sources/bloque1-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TREBEP"
  - "Estatuto Básico del Empleado Público"
  - "EBEP"
---

# TREBEP: Estatuto Básico del Empleado Público (RD Legislativo 5/2015)

El **Texto Refundido de la Ley del Estatuto Básico del Empleado Público (TREBEP)**, aprobado por **Real Decreto Legislativo 5/2015, de 30 de octubre**, regula las bases del régimen estatutario de los funcionarios públicos y las normas aplicables al personal laboral al servicio de todas las Administraciones Públicas españolas.

---

## 🏛️ Clasificación del Personal y Grupos de Titulación

- **Personal Funcionario de Carrera (Art. 9)**: Ejercicio exclusivo de potestades públicas y salvaguardia de intereses generales.
- **Personal Funcionario Interino (Art. 10)**: Por razones justificadas de necesidad y urgencia (vacantes máx 3 años).
- **Personal Laboral (Art. 11)** y **Personal Eventual (Art. 12)** (confianza y asesoramiento especial).
- **Grupos de Clasificación (Art. 76)**:
  - **Subgrupo A1**: Grado Universitario / Licenciado / Doctor.
  - **Subgrupo A2**: Grado Universitario / Diplomado.
  - **Grupo B**: Técnico Superior (FP Superior).
  - **Subgrupo C1**: Bachiller o FP Grado Medio.
  - **Subgrupo C2**: Graduado en ESO.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro TREBEP | Especificación Legal |
|------------------|----------------------|
| Prescripción de Faltas | **Muy graves: 3 años** \| **Graves: 2 años** \| **Leves: 6 meses** |
| Prescripción de Sanciones | **Muy graves: 3 años** \| **Graves: 2 años** \| **Leves: 1 año** |
| Sanción de Separación del Servicio | Exclusiva para **faltas muy graves** de funcionarios de carrera |
| Duración Máxima Suspensión Firme | **6 años** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema05|Resumen Bloque 1 - Tema 05]]
- Concepto: [[wiki/concepts/situaciones-administrativas-funcionarios|Situaciones Administrativas de los Funcionarios]]
- Síntesis: [[wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia|Guía del TREBEP]]
""",

    "wiki/entities/ley-igualdad-y-violencia-genero.md": """---
title: "Leyes de Igualdad (LO 3/2007) y Violencia de Género (LO 1/2004)"
type: "entity"
tags:
  - igualdad
  - violencia-genero
  - lo-3-2007
  - lo-1-2004
sources:
  - "raw/sources/bloque1-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ley de Igualdad"
  - "Ley de Violencia de Género"
---

# Leyes de Igualdad (LO 3/2007) y Violencia de Género (LO 1/2004)

Marco legal orgánico para garantizar la efectividad de la igualdad de género y la protección integral de las víctimas de violencia machista en España.

---

## 🏛️ Aspectos Fundamentales

- **LO 3/2007 (Igualdad)**:
  - Conceptos de discriminación directa, discriminación indirecta, acoso sexual y por razón de sexo.
  - **Planes de Igualdad obligatorios**: Para empresas con **50 o más trabajadores**.
  - **Presencia Equilibrada**: 40% a 60% en órganos de selección y directivos.
  - Principio transversal de igualdad (*Mainstreaming*).
- **LO 1/2004 (Violencia de Género)**:
  - Violencia ejercida por cónyuges o exparejas con relación análoga de afectividad, aun sin convivencia.
  - Creación de los **Juzgados de Violencia sobre la Mujer (JVM)** con competencias mixtas penal-civil.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema06|Resumen Bloque 1 - Tema 06]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
""",

    "wiki/entities/ley-39-2015-lpacap.md": """---
title: "Ley 39/2015 del Procedimiento Administrativo Común (LPACAP)"
type: "entity"
tags:
  - lpacap
  - ley-39-2015
  - procedimiento-administrativo
  - recursos-administrativos
  - plazos
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ley 39/2015"
  - "LPACAP"
  - "Procedimiento Administrativo Común"
---

# Ley 39/2015 del Procedimiento Administrativo Común (LPACAP)

La **Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (LPACAP)** regula los requisitos de validez y eficacia de los actos administrativos, el procedimiento administrativo común y el régimen de recursos.

---

## 🏛️ Estructura y Capítulos Principales

- **133 Artículos**, Título Preliminar y 6 Títulos.
- **Relación Electrónica Obligatoria (Art. 14.2)**: Personas jurídicas, entidades sin personalidad, profesionales colegiados y **empleados públicos**.
- **Cómputo de Plazos (Art. 30)**: Días hábiles (excluyendo sábados, domingos y festivos) y meses de fecha a fecha.
- **Actos Nulos de Pleno Derecho (Art. 47)** vs **Actos Anulables (Art. 48)**.
- **Recursos Administrativos**: Alzada (Art. 121), Reposición (Art. 123) y Extraordinario de Revisión (Art. 125).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Regla / Plazo |
|-----------|---------------|
| Plazo Recurso de Alzada | Interposición: **1 mes** \| Resolución: **3 meses** |
| Plazo Recurso de Reposición | Interposición: **1 mes** \| Resolución: **1 mes** |
| Trámite de Audiencia | **10 a 15 días hábiles** |
| Caducidad Procedimiento por Paralización | **3 meses** por causa imputable al interesado |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Concepto: [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos|Actos Nulos y Anulables]]
- Concepto: [[wiki/concepts/recursos-administrativos-y-plazos|Recursos Administrativos]]
- Síntesis: [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Cheatsheet de Plazos LPACAP]]
""",

    "wiki/entities/ley-40-2015-lrjsp.md": """---
title: "Ley 40/2015 de Régimen Jurídico del Sector Público (LRJSP)"
type: "entity"
tags:
  - lrjsp
  - ley-40-2015
  - sector-publico
  - organos-colegiados
  - responsabilidad-patrimonial
sources:
  - "raw/sources/bloque1-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ley 40/2015"
  - "LRJSP"
  - "Régimen Jurídico del Sector Público"
---

# Ley 40/2015 de Régimen Jurídico del Sector Público (LRJSP)

La **Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (LRJSP)** regula las bases del régimen jurídico de las Administraciones Públicas, los principios del sistema de responsabilidad patrimonial y la organización de la AGE.

---

## 🏛️ Contenido Clave

- **Principios de Actuación (Art. 3)**: Eficacia, jerarquía, descentralización, desconcentración, coordinación, cooperación y personalidad jurídica única de cada Administración.
- **Administración Electrónica**: Sede Electrónica (Art. 38), Portal de Internet (Art. 39), Punto de Acceso General Electrónico PAGe (Art. 40), Actuación Administrativa Automatizada (Art. 41 con Sello/CSV), ENI (Art. 45) y ENS (Art. 46).
- **Órganos Colegiados (Art. 15-24)**: Convocatoria con 2 días de antelación, quórum de constitución (Presidente, Secretario y mitad de miembros).
- **Responsabilidad Patrimonial (Art. 32-37)**: Daño efectivo, evaluable e individualizado con nexo causal (prescripción de 1 año).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema08|Resumen Bloque 1 - Tema 08]]
- Entidad: [[wiki/entities/gobierno-y-age|El Gobierno y la AGE]]
- Concepto: [[wiki/concepts/responsabilidad-patrimonial-administracion|Responsabilidad Patrimonial]]
""",

    "wiki/entities/rgpd-y-lopdgdd.md": """---
title: "RGPD (UE 2016/679) y LOPDGDD (Ley Orgánica 3/2018)"
type: "entity"
tags:
  - rgpd
  - lopdgdd
  - proteccion-datos
  - arco-pol
  - derechos-digitales
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RGPD"
  - "LOPDGDD"
  - "Normativa de Protección de Datos"
---

# RGPD (UE 2016/679) y LOPDGDD (Ley Orgánica 3/2018)

El marco normativo conjunto formado por el **Reglamento General de Protección de Datos (UE 2016/679)** y la **Ley Orgánica 3/2018 (LOPDGDD)** garantiza el derecho fundamental a la protección de datos y regula los derechos digitales en España.

---

## 🏛️ Principios y Derechos

- **Principios del Tratamiento (Art. 5 RGPD)**: Licitud, lealtad, transparencia, limitación de la finalidad, minimización de datos, exactitud, limitación de conservación, integridad/confidencialidad y responsabilidad proactiva (*Accountability*).
- **Derechos ARCO-POL**: Acceso, Rectificación, Supresión (Olvido), Limitación, Portabilidad, Oposición y decisiones no automatizadas (plazo de respuesta general de **1 mes**).
- **Delegado de Protección de Datos (DPD / DPO)**: Obligatorio en todo el sector público; comunicación a la AEPD en **10 días**.
- **Garantía de Derechos Digitales (Título X LOPDGDD)**: Desconexión digital en el trabajo, intimidad en uso de dispositivos, educación digital y testamento digital.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Legal |
|-----------|-------------|
| Aplicación RGPD | **25 de mayo de 2018** |
| Plazo de Respuesta Derechos | **1 mes** (prorrogable 2 meses más) |
| Sanción a AAPP por Datos | **Apercibimiento formal** (sin multa económica en AAPP, Art. 77 LOPDGDD) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Bloque 1 - Tema 09]]
- Entidad: [[wiki/entities/aepd-agencia-proteccion-datos|AEPD]]
- Concepto: [[wiki/concepts/derechos-digitales-y-arco-pol|Derechos ARCO-POL y Derechos Digitales]]
- Síntesis: [[wiki/synthesis/rgpd-lopdgdd-derechos-y-sanciones-guia|Guía RGPD y LOPDGDD]]
""",

    "wiki/entities/aepd-agencia-proteccion-datos.md": """---
title: "Agencia Española de Protección de Datos (AEPD)"
type: "entity"
tags:
  - aepd
  - proteccion-datos
  - autoridad-independiente
  - privacidad
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "AEPD"
  - "Agencia de Protección de Datos"
---

# Agencia Española de Protección de Datos (AEPD)

La **Agencia Española de Protección de Datos (AEPD)** es la autoridad administrativa independiente de ámbito estatal encargada de velar por el cumplimiento de la legislación de protección de datos personales.

---

## 🏛️ Funciones y Potestades

- **Naturaleza**: Autoridad administrativa independiente con personalidad jurídica propia y plena independencia de los poderes públicos.
- **Potestades**: Investigación, emisión de circulares vinculantes, dictamen preceptivo de proyectos normativos y potestad sancionadora.
- **Canal Prioritario**: Mecanismo de urgencia para solicitar la retirada inmediata de contenidos sensibles difundidos en Internet sin consentimiento (violencia, abusos).
- **Presidencia de la AEPD**: Nombrado por Real Decreto a propuesta del Gobierno para un mandato de **5 años**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Bloque 1 - Tema 09]]
- Entidad: [[wiki/entities/rgpd-y-lopdgdd|RGPD y LOPDGDD]]
""",

    "wiki/entities/ley-19-2013-transparencia.md": """---
title: "Ley 19/2013 de Transparencia, Acceso a la Información y Buen Gobierno"
type: "entity"
tags:
  - transparencia
  - buen-gobierno
  - ley-19-2013
  - consejo-transparencia
sources:
  - "raw/sources/bloque1-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ley 19/2013"
  - "Ley de Transparencia"
  - "Transparencia y Buen Gobierno"
---

# Ley 19/2013 de Transparencia, Acceso a la Información y Buen Gobierno

La **Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno** articula los mecanismos de rendición de cuentas de las Administraciones Públicas mediante la publicidad activa y el derecho de acceso a la información.

---

## 🏛️ Contenido Clave

- **Publicidad Activa**: Publicación de oficio en el **Portal de la Transparencia** de información institucional, normativa y económico-presupuestaria.
- **Derecho de Acceso a la Información**:
  - No requiere motivación de la solicitud.
  - Plazo de resolución: **1 mes** (prorrogable 1 mes más).
  - Silencio administrativo: **DESESTIMATORIO** (Silencio negativo).
- **Reclamación ante el Consejo de Transparencia y Buen Gobierno (CTBG)**:
  - Reclamación potestativa previa a la vía judicial (plazo de interposición de **1 mes**, plazo de resolución de **3 meses** con silencio negativo).

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Especificación Legal |
|---------|----------------------|
| Silencio en Derecho de Acceso | **DESESTIMATORIO (Negativo)** |
| Plazo de Resolución de Acceso | **1 mes** |
| Mandato Presidente Consejo Transparencia | **5 años no renovable** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema10|Resumen Bloque 1 - Tema 10]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
"""
}

print("[*] Escribiendo 12 entidades del Bloque 1...")
for path, content in BLOQUE1_ENTITIES.items():
    write_file(path, content)

print("[*] Entidades del Bloque 1 creadas exitosamente.")
