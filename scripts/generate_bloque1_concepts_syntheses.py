# -*- coding: utf-8 -*-
"""
Script generador de Conceptos y Síntesis del Bloque 1 para TAI Oposiciones.
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
# CONCEPTOS BLOQUE 1 (8 Conceptos)
# ==============================================================================

BLOQUE1_CONCEPTS = {
    "wiki/concepts/derechos-fundamentales-y-libertades-publicas.md": """---
title: "Derechos Fundamentales, Garantías Constitucionales y Recurso de Amparo"
type: "concept"
tags:
  - derechos-fundamentales
  - garantias
  - recurso-amparo
  - constitucion
sources:
  - "raw/sources/bloque1-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Derechos Fundamentales"
  - "Garantías Constitucionales"
---

# Derechos Fundamentales, Garantías Constitucionales y Recurso de Amparo

El Título I de la Constitución Española articula el régimen de derechos y deberes y su sistema de garantías escalonadas según el Artículo 53 CE.

---

## 🏛️ Sistema de Garantías Constitucionales (Art. 53 CE)

```
                            Sistema de Garantías del Título I
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
  Nivel Máximo                        Nivel Medio                         Nivel Básico
(Art. 14, 15-29 y 30.2)            (Sección 2ª, Art. 30-38)           (Capítulo III, Art. 39-52)
• Reserva Ley Orgánica (15-29)     • Reserva Ley Ordinaria             • Principios informadores
• Tutela preferente y sumaria      • Recurso Inconstitucionalidad      • Solo alegables según leyes
• Recurso de Amparo ante TC        • (Sin Amparo)                       que los desarrollen
```

---

## 🎯 Datos Clave para Oposiciones TAI

| Nivel de Protección | Derechos Incluidos | Garantías Específicas |
|---------------------|--------------------|-----------------------|
| **Máximo** | **Art. 14, Sección 1ª (Art. 15-29) y Art. 30.2** | Ley Orgánica (15-29), Procedimiento Preferente y Sumario, **Recurso de Amparo ante el TC** |
| **Medio** | **Sección 2ª (Art. 30 a 38)** | Ley Ordinaria (respetando contenido esencial) y Recurso de Inconstitucionalidad |
| **Básico** | **Capítulo III (Art. 39 a 52)** | Principios rectores; no cabe amparo ni vinculan directamente sin desarrollo legislativo |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema01|Resumen Bloque 1 - Tema 01]]
- Entidad: [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]]
""",

    "wiki/concepts/fuentes-derecho-comunitario.md": """---
title: "Fuentes del Derecho Comunitario y Principios de Primacía y Efecto Directo"
type: "concept"
tags:
  - derecho-comunitario
  - fuentes-derecho
  - union-europea
  - primacia
sources:
  - "raw/sources/bloque1-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Fuentes del Derecho de la UE"
  - "Derecho Comunitario"
---

# Fuentes del Derecho Comunitario y Principios de Primacía y Efecto Directo

El ordenamiento jurídico de la Unión Europea es un sistema autónomo e integrado en el derecho interno de los Estados miembros.

---

## 🏛️ Jerarquía de Fuentes de la Unión Europea

1. **Derecho Originario (Primario)**: Tratados constitutivos (TUE, TFUE, Tratados de Adhesión) y la Carta de los Derechos Fundamentales.
2. **Derecho Derivado (Secundario - Art. 288 TFUE)**:
   - **Reglamento**: Alcance general, obligatorio en todos sus elementos y **directamente aplicable** sin transposición nacional.
   - **Directiva**: Obliga al Estado en cuanto al **resultado que deba conseguirse**, requiriendo **transposición en norma nacional** dentro de un plazo límite.
   - **Decisión**: Obligatoria en todos sus elementos para sus destinatarios específicos.
   - **Recomendaciones y Dictámenes**: Actos no vinculantes.

---

## 🧩 Principios de Articulación con el Derecho Nacional

- **Principio de Primacía**: Establecido por la jurisprudencia del TJUE (**Sentencia Costa c. ENEL, 1964**). Las normas de la UE prevalecen sobre cualquier norma nacional contraria.
- **Principio de Efecto Directo**: Establecido por la **Sentencia Van Gend en Loos (1963)**. Los particulares pueden invocar directamente derechos comunitarios ante tribunales nacionales.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema04|Resumen Bloque 1 - Tema 04]]
- Entidad: [[wiki/entities/instituciones-union-europea|Instituciones de la Unión Europea]]
- Síntesis: [[wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia|Guía de Instituciones Europeas]]
""",

    "wiki/concepts/situaciones-administrativas-funcionarios.md": """---
title: "Situaciones Administrativas de los Funcionarios de Carrera"
type: "concept"
tags:
  - situaciones-administrativas
  - trebep
  - funcionarios
  - excedencias
sources:
  - "raw/sources/bloque1-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Situaciones Administrativas"
  - "Excedencias y Servicios Especiales"
---

# Situaciones Administrativas de los Funcionarios de Carrera

El TREBEP (Artículos 85 a 92) regula las diferentes situaciones administrativas en las que pueden hallarse los funcionarios de carrera.

---

## 🏛️ Cuadro Comparativo de Situaciones Administrativas

| Situación Administrativa | Requisitos Previos | Devengo Retribuciones | Cómputo a Efectos de Trienios y Carrera | Reserva de Puesto de Trabajo |
|--------------------------|--------------------|-----------------------|-----------------------------------------|------------------------------|
| **Servicio Activo** | Nombramiento en puesto | **Sí** (íntegras) | **Sí** | Puesto propio |
| **Servicios Especiales** (Cargos electos, Ministros, etc.) | Nombramiento en cargo tasado | Retribuciones del cargo desempeñado | **Sí** | **Sí** (en la misma localidad) |
| **Servicio en otras AAPP** | Concurso, libre designación o transferencia | En la Administración de destino | Según normas de la Administración receptora | Según normativa aplicable |
| **Excedencia por Interés Particular** | **Mínimo 5 años** de servicio previo | **No** | **No** | **No** (duración mínima **2 años**) |
| **Excedencia por Agrupación Familiar** | Cónyuge en otra localidad con puesto definitivo | **No** | **No** | **No** |
| **Excedencia Cuidado Familiares** | Hijo o familiar hasta 2º grado dependiente | **No** | **Sí** (máximo **3 años**) | **Sí durante 2 años** (3º año en misma localidad y nivel) |
| **Excedencia Violencia de Género** | Acreditación de víctima | **Sí durante los primeros 6 meses** | **Sí** | **Sí** |
| **Suspensión Firme** | Sanción disciplinaria o condena | **No** | **No** | Pérdida de puesto si excede de **6 meses** (máx **6 años**) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema05|Resumen Bloque 1 - Tema 05]]
- Entidad: [[wiki/entities/trebep-empleado-publico|TREBEP]]
- Síntesis: [[wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia|Guía del TREBEP]]
""",

    "wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos.md": """---
title: "Eficacia, Validez, Nulidad y Anulabilidad de los Actos Administrativos"
type: "concept"
tags:
  - actos-administrativos
  - nulidad
  - anulabilidad
  - lpacap
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Actos Nulos y Anulables"
  - "Invalidez de los Actos Administrativos"
---

# Eficacia, Validez, Nulidad y Anulabilidad de los Actos Administrativos

La teoría de la invalidez de los actos administrativos se articula en los Artículos 47 a 52 de la Ley 39/2015 (LPACAP).

---

## 🏛️ Nulidad de Pleno Derecho vs Anulabilidad

| Criterio | Nulidad de Pleno Derecho (Art. 47 LPACAP) | Anulabilidad (Art. 48 LPACAP) |
|----------|-------------------------------------------|-------------------------------|
| **Gravedad del Vicio** | Máxima gravedad (vicios tasados por ley) | Cualquier otra infracción del ordenamiento o desviación de poder |
| **Efectos en el Tiempo** | *Ex tunc* (desde el origen, el acto nunca existió) | *Ex nunc* (desde que se declara la anulación) |
| **Subsanación / Convalidación** | **Insubsanable** (no puede convalidarse) | **Convalidable** subsanando los vicios (Art. 52) |
| **Prescripción de la Acción** | **Imprescriptible** (revisión de oficio en cualquier momento) | Prescribe a los **4 años** (revisión de lesividad) |
| **Supuestos Tasados** | Lesión DDFF amparables, incompetencia manifiesta material/territorial, contenido imposible, delito, omisión total de procedimiento, adquisición ilícita de derechos | Defectos de forma determinantes de indefensión, actuaciones extemporáneas cuando el plazo sea esencial |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Entidad: [[wiki/entities/ley-39-2015-lpacap|Ley 39/2015 LPACAP]]
- Síntesis: [[wiki/synthesis/actos-nulos-vs-anulables-guia|Guía de Actos Nulos vs Anulables]]
""",

    "wiki/concepts/recursos-administrativos-y-plazos.md": """---
title: "Recursos Administrativos en Vía Administrativa y Régimen de Plazos"
type: "concept"
tags:
  - recursos-administrativos
  - alzada
  - reposicion
  - lpacap
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Recursos Administrativos"
  - "Alzada y Reposición"
---

# Recursos Administrativos en Vía Administrativa y Régimen de Plazos

Los recursos administrativos permiten impugnar actos y decisiones administrativas antes de acudir a la jurisdicción contencioso-administrativa (Título V de la Ley 39/2015).

---

## 🏛️ Matriz Comparativa de Recursos Administrativos

| Recurso | Actos Impugnables | Ante Quién se Interpone | Quién Resuelve | Plazo Interposición | Plazo de Resolución | Silencio Administrativo |
|---------|-------------------|-------------------------|----------------|---------------------|---------------------|-------------------------|
| **Alzada** (Art. 121-122) | Actos que **NO ponen fin a la vía administrativa** | Órgano que dictó el acto o el superior | **Superior Jerárquico** | **1 mes** (expreso) / En cualquier momento (silencio) | **3 meses** | **Desestimatorio** (salvo alzada impropia que es estimatorio) |
| **Potestativo de Reposición** (Art. 123-124) | Actos que **SÍ ponen fin a la vía administrativa** | Mismo órgano que dictó el acto | **Mismo Órgano** | **1 mes** (expreso) / En cualquier momento (silencio) | **1 mes** | **Desestimatorio** |
| **Extraordinario de Revisión** (Art. 125-126) | Actos **firmes en vía administrativa** (4 causas tasadas) | Órgano competente | **Mismo Órgano** | **3 meses** (causas 2, 3, 4) / **4 años** (error de hecho) | **3 meses** | **Desestimatorio** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Síntesis: [[wiki/synthesis/recursos-administrativos-comparativa-guia|Guía Comparativa de Recursos Administrativos]]
""",

    "wiki/concepts/computo-de-plazos-administrativos.md": """---
title: "Cómputo de Plazos Administrativos (Ley 39/2015)"
type: "concept"
tags:
  - computo-plazos
  - dias-habiles
  - lpacap
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cómputo de Plazos"
  - "Días Hábiles LPACAP"
---

# Cómputo de Plazos Administrativos (Ley 39/2015)

El Artículo 30 de la Ley 39/2015 unificó el régimen de plazos en el procedimiento administrativo común.

---

## 🏛️ Reglas Generales de Cómputo

1. **Días Hábiles (Regla General por Defecto)**:
   - Se **excluyen del cómputo los sábados, los domingos y los declarados festivos**.
   - Se cuentan siempre a partir del **día siguiente** al de la notificación o publicación.
2. **Días Naturales**: Solo cuando una Ley o el Derecho de la UE lo exprese expresamente.
3. **Plazos por Meses o Años**:
   - Se computan **de fecha a fecha** a partir del día siguiente al de la notificación.
   - Si en el mes de vencimiento no hubiera día equivalente (ej. notificación el 31 de enero en plazo de 1 mes), el plazo expira el **último día del mes** (28 o 29 de febrero).
   - Si el último día es inhábil, se prorroga al primer día hábil siguiente.
4. **Plazos por Horas**: Todas las horas hábiles de días hábiles, de minuto en minuto a partir de la hora de notificación.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Síntesis: [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Cheatsheet de Plazos LPACAP]]
""",

    "wiki/concepts/responsabilidad-patrimonial-administracion.md": """---
title: "Responsabilidad Patrimonial de las Administraciones Públicas"
type: "concept"
tags:
  - responsabilidad-patrimonial
  - indemnizacion
  - ley-40-2015
  - lrjsp
sources:
  - "raw/sources/bloque1-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Responsabilidad Patrimonial"
  - "Indemnizaciones AAPP"
---

# Responsabilidad Patrimonial de las Administraciones Públicas

El sistema de responsabilidad patrimonial directa y objetiva de las AAPP se fundamenta en el Artículo 106.2 CE y los Artículos 32 a 37 de la Ley 40/2015 (LRJSP).

---

## 🏛️ Requisitos y Procedimiento

- **Principio**: Derecho de los particulares a ser indemnizados de toda lesión en bienes o derechos consecuencia del funcionamiento normal o anormal de los servicios públicos, salvo **fuerza mayor**.
- **Requisitos**: Daño real, efectivo, evaluable económicamente e individualizado, con **nexo causal** directo entre la acción administrativa y la lesión.
- **Plazo de Prescripción (Art. 67 Ley 39/2015)**: El derecho a reclamar prescribe al **1 año** de producido el hecho lesivo o de la curación/determinación del alcance de las secuelas.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema08|Resumen Bloque 1 - Tema 08]]
- Entidad: [[wiki/entities/ley-40-2015-lrjsp|Ley 40/2015 LRJSP]]
""",

    "wiki/concepts/derechos-digitales-y-arco-pol.md": """---
title: "Derechos Ciudadanos ARCO-POL y Derechos Digitales (RGPD / LOPDGDD)"
type: "concept"
tags:
  - proteccion-datos
  - arco-pol
  - derechos-digitales
  - rgpd
  - lopdgdd
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Derechos ARCO-POL"
  - "Garantía de Derechos Digitales"
---

# Derechos Ciudadanos ARCO-POL y Derechos Digitales (RGPD / LOPDGDD)

Catálogo de derechos de los titulares de datos personales bajo el RGPD y el Título X de la LOPDGDD (Ley Orgánica 3/2018).

---

## 🏛️ Catálogo de Derechos ARCO-POL

1. **Acceso (Art. 15 RGPD)**: Confirmación de tratamiento y copia gratuita de los datos.
2. **Rectificación (Art. 16 RGPD)**: Corrección de datos inexactos o incompletos.
3. **Supresión ("Derecho al Olvido" - Art. 17 RGPD)**: Borrado de datos innecesarios o tras retirar el consentimiento.
4. **Limitación (Art. 18 RGPD)**: Bloqueo cautelar de tratamiento mientras se resuelven controversias.
5. **Portabilidad (Art. 20 RGPD)**: Recepción de datos en formato estructurado de lectura mecánica (JSON/CSV).
6. **Oposición (Art. 21 RGPD)**: Oponerse al tratamiento por motivos de situación particular.
7. **No sujeción a decisiones automatizadas / perfilado (Art. 22 RGPD)**.
- **Plazo General de Respuesta**: **1 mes** desde la solicitud.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Bloque 1 - Tema 09]]
- Entidad: [[wiki/entities/rgpd-y-lopdgdd|RGPD y LOPDGDD]]
- Síntesis: [[wiki/synthesis/rgpd-lopdgdd-derechos-y-sanciones-guia|Guía RGPD y LOPDGDD]]
"""
}

print("[*] Escribiendo 8 conceptos jurídicos del Bloque 1...")
for path, content in BLOQUE1_CONCEPTS.items():
    write_file(path, content)

# ==============================================================================
# SÍNTESIS BLOQUE 1 (8 Fichas)
# ==============================================================================

BLOQUE1_SYNTHESES = {
    "wiki/synthesis/bloque1-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 1: Administración Pública y Normativa (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-1
  - oposiciones
  - tai
sources:
  - "raw/sources/bloque1-tema01.md"
  - "raw/sources/bloque1-tema02.md"
  - "raw/sources/bloque1-tema03.md"
  - "raw/sources/bloque1-tema04.md"
  - "raw/sources/bloque1-tema05.md"
  - "raw/sources/bloque1-tema06.md"
  - "raw/sources/bloque1-tema07.md"
  - "raw/sources/bloque1-tema08.md"
  - "raw/sources/bloque1-tema09.md"
  - "raw/sources/bloque1-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 1"
  - "Bloque 1 TAI Master Guide"
---

# Guía Maestra de Bloque 1: Administración Pública y Normativa (TAI)

Mapa integral de conocimientos del **Bloque 1** para las oposiciones de Técnicos Auxiliares de Informática de la AGE.

---

## 🗺️ Mapa Temático del Bloque 1

| Tema | Materia Oficial | Resumen Fuente | Entidades Clave | Conceptos Clave |
|------|-----------------|----------------|-----------------|-----------------|
| **Tema 01** | La Constitución Española de 1978 | [[wiki/sources/bloque1-tema01\|Resumen Tema 01]] | [[wiki/entities/constitucion-espanola-1978\|Constitución Española]], [[wiki/entities/cortes-generales\|Cortes Generales]] | [[wiki/concepts/derechos-fundamentales-y-libertades-publicas\|Derechos Fundamentales y Garantías]] |
| **Tema 02** | El Gobierno y la AGE | [[wiki/sources/bloque1-tema02\|Resumen Tema 02]] | [[wiki/entities/gobierno-y-age\|El Gobierno y la AGE]], [[wiki/entities/ley-40-2015-lrjsp\|Ley 40/2015]] | Órganos Superiores vs Directivos |
| **Tema 03** | Organización Territorial y CCAA | [[wiki/sources/bloque1-tema03\|Resumen Tema 03]] | [[wiki/entities/comunidades-autonomas-y-ee-ll\|CCAA y Entidades Locales]] | Competencias Art. 148/149, Art. 155 |
| **Tema 04** | La Unión Europea y Derecho Comunitario | [[wiki/sources/bloque1-tema04\|Resumen Tema 04]] | [[wiki/entities/instituciones-union-europea\|Instituciones UE]] | [[wiki/concepts/fuentes-derecho-comunitario\|Fuentes del Derecho Comunitario]] |
| **Tema 05** | El Empleado Público y el TREBEP | [[wiki/sources/bloque1-tema05\|Resumen Tema 05]] | [[wiki/entities/trebep-empleado-publico\|TREBEP]] | [[wiki/concepts/situaciones-administrativas-funcionarios\|Situaciones Administrativas]] |
| **Tema 06** | Igualdad y Violencia de Género | [[wiki/sources/bloque1-tema06\|Resumen Tema 06]] | [[wiki/entities/ley-igualdad-y-violencia-genero\|Leyes LO 3/2007 y LO 1/2004]] | Planes de Igualdad (50+ trab.), JVM |
| **Tema 07** | Procedimiento Administrativo (LPACAP) | [[wiki/sources/bloque1-tema07\|Resumen Tema 07]] | [[wiki/entities/ley-39-2015-lpacap\|Ley 39/2015 LPACAP]] | [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos\|Actos Nulos y Anulables]], [[wiki/concepts/recursos-administrativos-y-plazos\|Recursos]], [[wiki/concepts/computo-de-plazos-administrativos\|Cómputo Plazos]] |
| **Tema 08** | Régimen Jurídico del Sector Público (LRJSP) | [[wiki/sources/bloque1-tema08\|Resumen Tema 08]] | [[wiki/entities/ley-40-2015-lrjsp\|Ley 40/2015 LRJSP]] | [[wiki/concepts/responsabilidad-patrimonial-administracion\|Responsabilidad Patrimonial]], Sede Electrónica |
| **Tema 09** | Protección de Datos (RGPD y LOPDGDD) | [[wiki/sources/bloque1-tema09\|Resumen Tema 09]] | [[wiki/entities/rgpd-y-lopdgdd\|RGPD y LOPDGDD]], [[wiki/entities/aepd-agencia-proteccion-datos\|AEPD]] | [[wiki/concepts/derechos-digitales-y-arco-pol\|Derechos ARCO-POL]], DPD |
| **Tema 10** | Transparencia y Buen Gobierno | [[wiki/sources/bloque1-tema10\|Resumen Tema 10]] | [[wiki/entities/ley-19-2013-transparencia\|Ley 19/2013 Transparencia]] | Publicidad Activa, Consejo Transparencia |

---

## 📚 Síntesis Monográficas de Examen
- [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Cheatsheet de Plazos del Procedimiento Administrativo]]
- [[wiki/synthesis/recursos-administrativos-comparativa-guia|Guía Comparativa de Recursos Administrativos]]
- [[wiki/synthesis/actos-nulos-vs-anulables-guia|Guía de Actos Nulos vs Anulables]]
- [[wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet|Cheatsheet de Artículos Clave de la Constitución]]
- [[wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia|Guía del TREBEP: Situaciones y Régimen Disciplinario]]
- [[wiki/synthesis/rgpd-lopdgdd-derechos-y-sanciones-guia|Guía del RGPD y LOPDGDD]]
- [[wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia|Guía de Instituciones Europeas]]
""",

    "wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet.md": """---
title: "Cheatsheet de Plazos del Procedimiento Administrativo (Ley 39/2015 y Ley 40/2015)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - plazos
  - lpacap
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema07.md"
  - "raw/sources/bloque1-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet de Plazos LPACAP"
  - "Plazos Procedimiento Administrativo"
---

# Cheatsheet de Plazos del Procedimiento Administrativo (Ley 39/2015 y Ley 40/2015)

Tabla maestra de memorización de plazos procedimentales para las oposiciones TAI.

---

## ⏱️ Tabla Maestra de Plazos del Procedimiento

| Trámite / Actuación | Plazo Legal | Base Legal |
|---------------------|-------------|------------|
| **Días Hábiles Administrativos** | Excluyen **sábados, domingos y festivos** | Art. 30.2 Ley 39/2015 |
| **Subsanación y Mejora de Solicitud** | **10 días hábiles** (ampliable 5 días más) | Art. 68.1 Ley 39/2015 |
| **Práctica de Notificaciones Electrónicas** | Se entiende rechazada a los **10 días naturales** sin acceder | Art. 43.2 Ley 39/2015 |
| **Periodo de Prueba** | **10 a 30 días hábiles** | Art. 77.2 Ley 39/2015 |
| **Emisión de Informes** | **10 días hábiles** (por defecto) | Art. 80.2 Ley 39/2015 |
| **Trámite de Audiencia** | **10 a 15 días hábiles** | Art. 82.2 Ley 39/2015 |
| **Plazo Máximo Resolución General** | **3 meses** (si norma no fija plazo; máx legal 6 meses) | Art. 21.3 Ley 39/2015 |
| **Caducidad por Inactividad del Interesado** | **3 meses** de paralización tras advertencia | Art. 95.1 Ley 39/2015 |
| **Interposición Recurso de Alzada** | **1 mes** (acto expreso) | Art. 122.1 Ley 39/2015 |
| **Resolución Recurso de Alzada** | **3 meses** (Silencio Desestimatorio) | Art. 122.2 Ley 39/2015 |
| **Interposición Recurso de Reposición** | **1 mes** (acto expreso) | Art. 124.1 Ley 39/2015 |
| **Resolución Recurso de Reposición** | **1 mes** (Silencio Desestimatorio) | Art. 124.2 Ley 39/2015 |
| **Prescripción Responsabilidad Patrimonial** | **1 año** desde el hecho lesivo o secuelas | Art. 67 Ley 39/2015 |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Concepto: [[wiki/concepts/computo-de-plazos-administrativos|Cómputo de Plazos]]
""",

    "wiki/synthesis/recursos-administrativos-comparativa-guia.md": """---
title: "Guía Comparativa de Recursos Administrativos: Alzada, Reposición y Revisión"
type: "synthesis"
tags:
  - synthesis
  - recursos-administrativos
  - alzada
  - reposicion
  - lpacap
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Recursos Administrativos"
  - "Guía de Recursos LPACAP"
---

# Guía Comparativa de Recursos Administrativos: Alzada, Reposición y Revisión

Matriz exhaustiva de recursos en vía administrativa bajo los Artículos 112 a 126 de la Ley 39/2015.

---

## 🏛️ Matriz Comparativa

| Parámetro | Recurso de Alzada | Recurso Potestativo de Reposición | Recurso Extraordinario de Revisión |
|-----------|-------------------|-----------------------------------|-----------------------------------|
| **Tipo de Recurso** | **Ordinario y Preceptivo** para agotar vía | **Ordinario y Potestativo** (o ir a lo Contencioso) | **Extraordinario** (tasado) |
| **Fin de Vía Administrativa** | Actos que **NO ponen fin** a la vía | Actos que **SÍ ponen fin** a la vía | Actos **firmes** en vía administrativa |
| **Órgano ante el que se Interpone** | El que dictó el acto o el superior jerárquico | El **mismo órgano** que dictó el acto | El **mismo órgano** competente |
| **Órgano que Resuelve** | **Superior jerárquico** | El **mismo órgano** que lo dictó | El **mismo órgano** |
| **Plazo Interposición (Expreso)** | **1 mes** | **1 mes** | **4 años** (error de hecho) / **3 meses** (demás causas) |
| **Plazo para Resolver y Notificar** | **3 meses** | **1 mes** | **3 meses** |
| **Efecto del Silencio Administrativo** | **Desestimatorio** (negativo)* | **Desestimatorio** (negativo) | **Desestimatorio** (negativo) |

> *\*Excepción de Silencio Positivo en Alzada*: Cuando el recurso de alzada se haya interpuesto contra la desestimación por silencio administrativo de una solicitud previa, el transcurso de 3 meses sin resolución del recurso de alzada opera con **silencio estimatorio (positivo)**, siempre que no afecte al dominio público, medio ambiente o facultades sustantivas (Art. 24.1 tercer párrafo).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Concepto: [[wiki/concepts/recursos-administrativos-y-plazos|Recursos Administrativos]]
""",

    "wiki/synthesis/actos-nulos-vs-anulables-guia.md": """---
title: "Guía de Invalidez: Actos Nulos de Pleno Derecho vs Actos Anulables"
type: "synthesis"
tags:
  - synthesis
  - actos-nulos
  - actos-anulables
  - lpacap
  - ley-39-2015
sources:
  - "raw/sources/bloque1-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Actos Nulos vs Anulables"
  - "Guía de Invalidez LPACAP"
---

# Guía de Invalidez: Actos Nulos de Pleno Derecho vs Actos Anulables

Esquema de contraste entre las causas y consecuencias jurídicas de la nulidad radical y la anulabilidad en la Ley 39/2015.

---

## 🏛️ Comparativa Esencial

```
                            Invalidez del Acto Administrativo
                                            │
        ┌───────────────────────────────────┴───────────────────────────────────┐
        ▼                                                                       ▼
  Actos Nulos de Pleno Derecho (Art. 47)                           Actos Anulables (Art. 48)
  • Vicios tasados expresamente por Ley                           • Regla general: cualquier infracción
  • Insubsanable (no cabe convalidación)                          • Convalidable subsanando el vicio
  • Imprescriptible (Revisión de oficio en cualquier momento)     • Declaración de lesividad en 4 años
  • Efectos Ex Tunc (desde el origen)                             • Efectos Ex Nunc (desde la anulación)
```

### Causas Tasadas de Nulidad de Pleno Derecho (Art. 47.1 LPACAP)
1. Lesionen derechos y libertades susceptibles de amparo constitucional (**Art. 14 a 29 y 30.2 CE**).
2. Dictados por órgano **manifiestamente incompetente** por razón de la materia o del territorio.
3. Tengan un **contenido imposible**.
4. Sean **constitutivos de infracción penal** o se dicten como consecuencia de ésta.
5. Dictados **prescindiendo total y absolutamente del procedimiento legalmente establecido** o de las normas de formación de voluntad de órganos colegiados.
6. Actos contrarios por los que se **adquieran facultades o derechos careciendo de los requisitos esenciales**.
7. Cualquier otro establecido expresamente en disposición con rango de Ley.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema07|Resumen Bloque 1 - Tema 07]]
- Concepto: [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos|Actos Nulos y Anulables]]
""",

    "wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet.md": """---
title: "Cheatsheet de Artículos Clave de la Constitución Española para TAI"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - constitucion
  - articulos-clave
  - tai
sources:
  - "raw/sources/bloque1-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Artículos Clave Constitución"
  - "Constitución Española Cheatsheet"
---

# Cheatsheet de Artículos Clave de la Constitución Española para TAI

Tabla de los artículos y mayorías constitucionales más frecuentes en exámenes de oposiciones.

---

## 📋 Artículos Clave y Contenido

| Artículo CE | Materia Regulada | Puntos Memorísticos Críticos |
|-------------|------------------|------------------------------|
| **Art. 1** | Estado de Derecho y Soberanía | Valores: **Libertad, Justicia, Igualdad, Pluralismo**; Monarquía parlamentaria |
| **Art. 9.3** | Principios Jurídicos | Legalidad, jerarquía, publicidad, **irretroactividad sancionadora desfavorable**, seguridad jurídica |
| **Art. 14** | Igualdad ante la Ley | No discriminación por nacimiento, raza, sexo, religión u opinión |
| **Art. 17** | Libertad y Seguridad | Detención preventiva máxima de **72 horas**; procedimiento de *Habeas Corpus* |
| **Art. 24** | Tutela Judicial Efectiva | Derecho a juez ordinario, defensa letrada, a no declarar contra sí mismo y presunción de inocencia |
| **Art. 53** | Sistema de Garantías | **53.2**: Recurso de amparo ante el TC para Art. 14, 15-29 y 30.2 |
| **Art. 56** | La Corona | El Rey es el Jefe del Estado; persona **inviolable y no sujeta a responsabilidad** |
| **Art. 64** | Refrendo de Actos del Rey | Refrendados por Presidente del Gobierno, Ministros o Presidente del Congreso (Art. 99) |
| **Art. 68** | Congreso de los Diputados | **350 Diputados** (LOREG), mandato de 4 años, sistema proporcional (D'Hondt) |
| **Art. 81** | Leyes Orgánicas | Desarrollo DDFF (15-29), Estatutos, LOREG. Exige **Mayoría Absoluta del Congreso** |
| **Art. 86** | Decretos-Leyes | Urgente necesidad. Sometidos a votación en **30 días** ante el Congreso |
| **Art. 99** | Investidura del Presidente | 1ª votación: **Mayoría Absoluta**; 2ª votación (48h): **Mayoría Simple**; límite **2 meses** |
| **Art. 113**| Moción de Censura | Propuesta por **1/10 Diputados (35)**; votación tras **5 días**; exige **Mayoría Absoluta** |
| **Art. 155**| Coerción Estatal CCAA | Requiere aprobación por **Mayoría Absoluta del Senado** |
| **Art. 159**| Tribunal Constitucional | **12 miembros por 9 años** (4 Congreso, 4 Senado, 2 Gobierno, 2 CGPJ) |
| **Art. 167**| Reforma Ordinaria | **3/5 de cada Cámara** (referéndum si pide 10% en 15 días) |
| **Art. 168**| Reforma Agravada | **2/3 de cada Cámara** + Disolución + Ratificación 2/3 + **Referéndum preceptivo** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema01|Resumen Bloque 1 - Tema 01]]
- Entidad: [[wiki/entities/constitucion-espanola-1978|Constitución Española]]
""",

    "wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia.md": """---
title: "Guía del TREBEP: Situaciones Administrativas y Régimen Disciplinario"
type: "synthesis"
tags:
  - synthesis
  - trebep
  - situaciones-administrativas
  - regimen-disciplinario
  - faltas-sanciones
sources:
  - "raw/sources/bloque1-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía TREBEP"
  - "Régimen Disciplinario TREBEP"
---

# Guía del TREBEP: Situaciones Administrativas y Régimen Disciplinario

Compendio de situaciones administrativas, excedencias, faltas disciplinarias y prescripciones según el RD Legislativo 5/2015.

---

## ⏱️ Prescripción de Faltas y Sanciones (Art. 97 TREBEP)

| Gravedad | Prescripción de la FALTA (desde que se comete) | Prescripción de la SANCIÓN (desde que es firme) |
|----------|------------------------------------------------|-------------------------------------------------|
| **Muy Grave** | **3 años** | **3 años** |
| **Grave** | **2 años** | **2 años** |
| **Leve** | **6 meses** | **1 año** |

---

## 📋 Resumen de Excedencias

- **Interés Particular**: Mínimo 5 años previos; duración mínima continuada de 2 años (no computa).
- **Agrupación Familiar**: Cónyuge en otra localidad con puesto definitivo (no computa).
- **Cuidado de Hijos / Familiares**: Máx 3 años (**computa para trienios y carrera**; reserva de puesto 2 años).
- **Violencia de Género**: Sin tiempo mínimo (primeros 6 meses con retribución íntegra y reserva de puesto).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema05|Resumen Bloque 1 - Tema 05]]
- Entidad: [[wiki/entities/trebep-empleado-publico|TREBEP]]
""",

    "wiki/synthesis/rgpd-lopdgdd-derechos-y-sanciones-guia.md": """---
title: "Guía del RGPD y LOPDGDD: Principios, Derechos ARCO-POL y Régimen Sancionador"
type: "synthesis"
tags:
  - synthesis
  - rgpd
  - lopdgdd
  - proteccion-datos
  - arco-pol
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Protección de Datos"
  - "RGPD y LOPDGDD Guía"
---

# Guía del RGPD y LOPDGDD: Principios, Derechos ARCO-POL y Régimen Sancionador

Manual de protección de datos personales bajo el RGPD (UE 2016/679) y la LOPDGDD (LO 3/2018).

---

## 🏛️ Resumen de Principios y DPD

- **7 Principios**: Licitud/lealtad/transparencia, limitación de finalidad, minimización de datos, exactitud, limitación de plazo de conservación, integridad/confidencialidad y responsabilidad proactiva (*Accountability*).
- **DPD en AAPP**: Obligatorio en todo el sector público; comunicación a la AEPD en **10 días**.
- **Plazo de Respuesta Derechos ARCO-POL**: **1 mes** desde la recepción.
- **Régimen Sancionador en AAPP (Art. 77 LOPDGDD)**: Sanción económica sustituida por **apercibimiento** e incoación de expediente disciplinario.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema09|Resumen Bloque 1 - Tema 09]]
- Entidad: [[wiki/entities/rgpd-y-lopdgdd|RGPD y LOPDGDD]]
- Entidad: [[wiki/entities/aepd-agencia-proteccion-datos|AEPD]]
""",

    "wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia.md": """---
title: "Guía de Instituciones de la Unión Europea: Composición, Sedes y Votación"
type: "synthesis"
tags:
  - synthesis
  - union-europea
  - instituciones-ue
  - sedes-ue
sources:
  - "raw/sources/bloque1-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Instituciones Europeas"
  - "Instituciones UE Guía"
---

# Guía de Instituciones de la Unión Europea: Composición, Sedes y Votación

Guía de referencia rápida sobre los órganos de la Unión Europea tras el Tratado de Lisboa.

---

## 🏛️ Cuadro de Sedes y Mayorías

| Institución | Sede Principal | Mandato | Sistema de Votación |
|-------------|----------------|---------|---------------------|
| **Parlamento Europeo** | Estrasburgo (Plenos) / Bruselas (Comisiones) | 5 años | Mayoría de votos emitidos |
| **Consejo Europeo** | Bruselas | Presidente (2,5 años) | Consenso |
| **El Consejo (UE)** | Bruselas | Presidencia semestral | **Mayoría Cualificada: 55% Estados (mín 15) y 65% población** |
| **Comisión Europea** | Bruselas | 5 años (27 Comisarios) | Mayoría de los miembros |
| **TJUE** | Luxemburgo | Jueces (6 años) | Mayoría |
| **BCE** | Fráncfort | Presidente (8 años no renovable) | Mayoría |
| **Tribunal de Cuentas** | Luxemburgo | 6 años | Mayoría |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque1-tema04|Resumen Bloque 1 - Tema 04]]
- Entidad: [[wiki/entities/instituciones-union-europea|Instituciones de la Unión Europea]]
"""
}

print("[*] Escribiendo 8 síntesis del Bloque 1...")
for path, content in BLOQUE1_SYNTHESES.items():
    write_file(path, content)

print("[*] Síntesis del Bloque 1 creadas exitosamente.")
