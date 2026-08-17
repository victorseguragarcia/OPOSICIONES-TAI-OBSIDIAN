# -*- coding: utf-8 -*-
"""
Script generador del temario oficial y notas fuente del Bloque 1 (TAI Oposiciones).
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
# 1. RAW SOURCES BLOQUE 1 (Temas 01 al 10)
# ==============================================================================

RAW_SOURCES = {
    "raw/sources/bloque1-tema01.md": """---
title: "Bloque 1 - Tema 01: La Constitución Española de 1978"
type: "raw-source"
topic: "constitucion-espanola"
date: "2026-08-17"
---

# Bloque 1 - Tema 01: La Constitución Española de 1978: Estructura, Derechos Fundamentales, la Corona, las Cortes Generales y el Tribunal Constitucional

## 1. Estructura y Principios Generales de la Constitución Española
Aprobada por las Cortes Generales el 31 de octubre de 1978, ratificada en referéndum por el pueblo español el 6 de diciembre de 1978, sancionada y promulgada por el Rey Don Juan Carlos I el 27 de diciembre de 1978 y publicada en el BOE y entrada en vigor el 29 de diciembre de 1978.
Consta de 1 Preámbulo (sin fuerza jurídica vinculante), 169 Artículos distribuidos en 1 Título Preliminar y 10 Títulos numerados, 4 Disposiciones Adicionales, 9 Disposiciones Transitorias, 1 Disposición Derogatoria y 1 Disposición Final.

### Estructura Sistemática:
- Título Preliminar: Artículos 1 al 9. Define a España como un Estado social y democrático de Derecho que propugna como valores superiores de su ordenamiento jurídico la libertad, la justicia, la igualdad y el pluralismo político (Art. 1.1). La soberanía nacional reside en el pueblo español (Art. 1.2). La forma política del Estado es la Monarquía parlamentaria (Art. 1.3). El castellano es la lengua oficial del Estado (Art. 3). La capital es la villa de Madrid (Art. 5). Principios de legalidad, jerarquía normativa, publicidad de las normas, irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad de los poderes públicos (Art. 9.3).
- Título I: De los derechos y deberes fundamentales (Art. 10 a 55).
- Título II: De la Corona (Art. 56 a 65).
- Título III: De las Cortes Generales (Art. 66 a 96).
- Título IV: Del Gobierno y de la Administración (Art. 97 a 107).
- Título V: De las relaciones entre el Gobierno y las Cortes Generales (Art. 108 a 116).
- Título VI: Del Poder Judicial (Art. 117 a 127).
- Título VII: Economía y Hacienda (Art. 128 a 136).
- Título VIII: De la Organización Territorial del Estado (Art. 137 a 158).
- Título IX: Del Tribunal Constitucional (Art. 159 a 165).
- Título X: De la Reforma Constitucional (Art. 166 a 169).

## 2. Derechos y Deberes Fundamentales y su Sistema de Garantías
El Título I se divide en:
- Artículo 10: La dignidad de la persona, los derechos inviolables que le son inherentes, el libre desarrollo de la personalidad. Interpretación conforme a la Declaración Universal de Derechos Humanos.
- Capítulo I: De los españoles y los extranjeros (Art. 11 a 13). Mayoría de edad a los 18 años (Art. 12).
- Capítulo II: Derechos y libertades (Art. 14 a 38):
  - Artículo 14: Principio de igualdad ante la ley sin discriminación por nacimiento, raza, sexo, religión, opinión.
  - Sección 1ª (Derechos Fundamentales y Libertades Públicas, Art. 15 a 29): Derecho a la vida y a la integridad física y moral, abolición de la pena de muerte (Art. 15); libertad ideológica y religiosa (Art. 16); libertad personal y seguridad, detención preventiva máx 72 horas, habeas corpus (Art. 17); honor, intimidad y propia imagen, inviolabilidad del domicilio, secreto de las comunicaciones (Art. 18); libertad de residencia y circulación (Art. 19); libertad de expresión y producción (Art. 20); derecho de reunión pacífica sin armas (Art. 21); derecho de asociación (Art. 22); derecho de participación y acceso a cargos públicos (Art. 23); tutela judicial efectiva sin indefensión (Art. 24); principio de legalidad penal (Art. 25); prohibición de tribunales de honor (Art. 26); libertad de enseñanza y derecho a la educación (Art. 27); libertad de sindicación y derecho a la huelga (Art. 28); derecho de petición (Art. 29).
  - Sección 2ª (De los derechos y deberes de los ciudadanos, Art. 30 a 38): Objeción de conciencia (Art. 30); sostenimiento de los gastos públicos mediante sistema tributario justo (Art. 31); derecho al matrimonio (Art. 32); derecho a la propiedad privada y a la herencia (Art. 33); derecho de fundación (Art. 34); deber de trabajar y derecho al trabajo (Art. 35); colegios profesionales (Art. 36); negociación colectiva laboral (Art. 37); libertad de empresa (Art. 38).
- Capítulo III: De los principios rectores de la política social y económica (Art. 39 a 52): Protección a la familia, seguridad social (Art. 41), salud (Art. 43), medio ambiente (Art. 45), vivienda digna (Art. 47).
- Capítulo IV: De las garantías de las libertades y derechos fundamentales (Art. 53 y 54):
  - Sistema de Protección de Tres Niveles (Art. 53):
    - Nivel Máximo (Art. 14 y Sección 1ª, Art. 15-29 + Art. 30 objeción): Vinculan a todos los poderes públicos, reserva de **Ley Orgánica** (para 15-29), tutela judicial ordinaria por procedimiento preferente y sumario, y **Recurso de Amparo ante el Tribunal Constitucional** (Art. 53.2).
    - Nivel Medio (Sección 2ª, Art. 30-38): Vinculan a los poderes públicos, reserva de ley ordinaria (respetando su contenido esencial), recurso de inconstitucionalidad. No cabe recurso de amparo.
    - Nivel Básico (Capítulo III, Art. 39-52): Principios informadores de la legislación, práctica judicial y actuación pública. Solo pueden ser alegados ante la jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen.
  - El Defensor del Pueblo (Art. 54): Alto comisionado de las Cortes Generales designado por éstas para la defensa de los derechos del Título I. Regulado por LO 3/1981. Elegido por mayoría de 3/5 del Congreso y del Senado para un mandato de 5 años.
- Capítulo V: De la suspensión de los derechos y libertades (Art. 55): Estados de alarma, excepción y sitio (Art. 116).

## 3. La Corona (Título II, Art. 56 a 65)
- El Rey es el Jefe del Estado, símbolo de su unidad y permanencia, arbitra y modera el funcionamiento regular de las instituciones (Art. 56.1). Su persona es inviolable y no está sujeta a responsabilidad; sus actos estarán siempre **refrendados** por el Presidente del Gobierno y, en su caso, por los Ministros competentes, o por el Presidente del Congreso (propuesta y nombramiento del Presidente del Gobierno y disolución de Cortes del art. 99). Carecen de validez sin dicho refrendo (salvo nombramiento de miembros civiles y militares de su Casa, Art. 65.2).
- Sucesión en la Corona (Art. 57): Hereditaria en los sucesores de S.M. Don Juan Carlos I de Borbón. Orden de primogenitura y representación: línea anterior a las posteriores; en la misma línea, grado más próximo al más remoto; en el mismo grado, el varón a la mujer; y en el mismo sexo, la persona de más edad a la de menos. Las abdicaciones y renuncias se resolverán por Ley Orgánica.
- Regencia (Art. 59) y Tutela del Rey menor (Art. 60).

## 4. Las Cortes Generales (Título III, Art. 66 a 96)
- Representan al pueblo español y están formadas por el **Congreso de los Diputados** y el **Senado** (bicameralismo imperfecto). Ejercen la potestad legislativa del Estado, aprueban sus Presupuestos y controlan la acción del Gobierno.
- **Congreso de los Diputados (Art. 68)**: Entre 300 y 400 Diputados (fijado en 350 por la LOREG). Circunscripción electoral es la provincia (Ceuta y Melilla representadas por 1 Diputado cada una). Elección por sufragio universal, libre, igual, directo y secreto mediante sistema proporcional (regla D'Hondt). Mandato de 4 años.
- **Senado (Art. 69)**: Cámara de representación territorial. Mandato de 4 años.
  - Senadores provinciales: 4 por cada provincia peninsular; en islas mayores (Gran Canaria, Mallorca, Tenerife) 3 cada una; en islas menores (Ibiza-Formentera, Menorca, Fuerteventura, Gomera, Hierro, Lanzarote, La Palma) 1 cada una; Ceuta y Melilla eligen 2 cada una.
  - Senadores autonómicos: 1 por Comunidad Autónoma y 1 más por cada millón de habitantes de su territorio, designados por las Asambleas Legislativas autonómicas.
- Periodos ordinarios de sesiones (Art. 73): Dos periodos al año: primero de septiembre a diciembre, segundo de febrero a junio.
- Tipos de Leyes:
  - **Leyes Orgánicas (Art. 81)**: Relativas al desarrollo de los derechos fundamentales y libertades públicas (Art. 15-29), las que aprueben los Estatutos de Autonomía y el régimen electoral general y las demás previstas en la Constitución. Aprobación, modificación o derogación exige **mayoría absoluta del Congreso** en una votación final sobre el conjunto del proyecto.
  - **Leyes Ordinarias**: Aprobadas por mayoría simple.
  - **Decretos Legislativos (Art. 82-85)**: Delegación de las Cortes al Gobierno (Textos Articulados mediante Ley de Bases o Textos Refundidos mediante Ley Ordinaria).
  - **Decretos-Leyes (Art. 86)**: Dictados por el Gobierno en casos de extraordinaria y urgente necesidad. Disposiciones legislativas provisionales que no pueden afectar al ordenamiento de las instituciones básicas del Estado, a los derechos, deberes y libertades del Título I, al régimen de las CCAA ni al Derecho electoral general. Deben ser sometidos a debate y votación de totalidad al Congreso en el plazo de **30 días** siguientes a su promulgación para su convalidación o derogación.

## 5. El Tribunal Constitucional (Título IX, Art. 159 a 165)
- Intérprete supremo de la Constitución, independiente de los demás órganos constitucionales y sometido solo a la Constitución y a su Ley Orgánica (LOTC 2/1979).
- **Composición (Art. 159)**: **12 miembros** nombrados por el Rey por un periodo de **9 años** y renovados por terceras partes (4 miembros) cada **3 años**:
  - 4 a propuesta del Congreso de los Diputados (mayoría de 3/5).
  - 4 a propuesta del Senado (mayoría de 3/5).
  - 2 a propuesta del Gobierno.
  - 2 a propuesta del Consejo General del Poder Judicial (CGPJ).
- **Competencias (Art. 161)**:
  - **Recurso de Inconstitucionalidad**: Contra leyes y disposiciones normativas con fuerza de ley. Legitimados: Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores, órganos colegiados ejecutivos y Asambleas de las CCAA.
  - **Cuestión de Inconstitucionalidad**: Promovida por jueces y tribunales de oficio o a instancia de parte cuando una norma con rango de ley aplicable al caso de cuya validez dependa el fallo pueda ser contraria a la Constitución.
  - **Recurso de Amparo**: Por violación de los derechos y libertades de los Artículos 14 a 29 y 30.2. Legitimados: toda persona natural o jurídica que invoque un interés legítimo, el Defensor del Pueblo y el Ministerio Fiscal.
  - **Conflictos de Competencia**: Entre el Estado y las CCAA o de éstas entre sí.
  - **Conflictos entre órganos constitucionales del Estado** (Gobierno, Congreso, Senado, CGPJ).

## 6. Reforma Constitucional (Título X, Art. 166 a 169)
- **Procedimiento Ordinario (Art. 167)**:
  - Proyectos de reforma aprobados por mayoría de **3/5 de cada Cámara**. Si no hay acuerdo, comisión paritaria Congreso-Senado. Si el texto no es aprobado, el Congreso puede aprobarlo por mayoría de **2/3** siempre que el Senado haya obtenido la mayoría absoluta.
  - Sometimiento a referéndum facultativo si lo solicita una **décima parte (10%)** de los miembros de cualquiera de las Cámaras en los 15 días siguientes a su aprobación.
- **Procedimiento Agravado / Extraordinario (Art. 168)**:
  - Exigido para la revisión total de la Constitución o parcial que afecte al **Título Preliminar**, al **Capítulo II, Sección 1ª del Título I (Art. 15-29)** o al **Título II (La Corona)**.
  - Aprobación del principio por **mayoría de 2/3 de cada Cámara** $\rightarrow$ Disolución inmediata de las Cortes $\rightarrow$ Nuevas Cortes ratifican la decisión y estudian el nuevo texto constitucional (aprobado por mayoría de 2/3 de ambas Cámaras) $\rightarrow$ **Referéndum preceptivo y vinculante obligatoriamente**.
""",

    "raw/sources/bloque1-tema02.md": """---
title: "Bloque 1 - Tema 02: El Gobierno y la Administración General del Estado"
type: "raw-source"
topic: "gobierno-y-age"
date: "2026-08-17"
---

# Bloque 1 - Tema 02: El Gobierno y la Administración General del Estado

## 1. El Gobierno: Composición, Nombramiento y Cese (Ley 50/1997, de 27 de noviembre, del Gobierno)
- **Composición (Art. 98 CE y Art. 1 Ley 50/1997)**: El Gobierno se compone del **Presidente**, del o de los **Vicepresidentes** (opcionales), de los **Ministros** y de los demás miembros que establezca la ley.
- **Órganos Colegiados del Gobierno**:
  - **Consejo de Ministros**: Formado por el Presidente, Vicepresidentes y Ministros. Sus deliberaciones son **secretas** (Art. 5.3 Ley 50/1997). Actúa como órgano colegiado superior que aprueba proyectos de ley, Reales Decretos-Leyes, Reales Decretos Legislativos, reglamentos, tratados internacionales y nombramientos de altos cargos.
  - **Comisiones Delegadas del Gobierno**: Creadas, modificadas y suprimidas por Real Decreto del Consejo de Ministros a propuesta del Presidente. Coordinan la acción de varios Ministerios en materias conjuntas.
- **Órganos de Apoyo y Colaboración del Gobierno**:
  - **Comisión General de Secretarios de Estado y Subsecretarios**: Presidida por el Vicepresidente que determine el Presidente del Gobierno (o Ministro de la Presidencia). Prepara las sesiones del Consejo de Ministros examinando todos los asuntos que vayan a ser sometidos a su deliberación. Ningún asunto puede someterse al Consejo de Ministros sin haber sido examinado previamente por esta Comisión (salvo urgencia declarada por el Presidente).
  - **Secretariado del Gobierno**: Órgano de apoyo técnico y administrativo al Consejo de Ministros, a las Comisiones Delegadas y a la Comisión General de Secretarios de Estado y Subsecretarios. Gestiona la publicación en el BOE. Integrado en el Ministerio de la Presidencia.
  - **Gabinetes**: Órganos de apoyo político y técnico del Presidente, Vicepresidentes, Ministros y Secretarios de Estado. Personal eventual de confianza y asesoramiento especial.

## 2. Nombramiento y Cese del Presidente del Gobierno
- **Investidura Ordinaria (Art. 99 CE)**: Tras cada renovación del Congreso y en los demás supuestos constitucionales en que así proceda (dimisión, fallecimiento, pérdida de confianza):
  1. El Rey, previa consulta con los representantes designados por los grupos políticos con representación parlamentaria, y a través del Presidente del Congreso, propone un candidato a la Presidencia del Gobierno.
  2. El candidato expone ante el Congreso de los Diputados el programa político del Gobierno que pretenda formar y solicita la confianza de la Cámara.
  3. Primera votación: Requiere **mayoría absoluta** de los miembros del Congreso (176 votos).
  4. Si no se alcanza, segunda votación 48 horas después: Requiere **mayoría simple** (más votos a favor que en contra).
  5. Si transcurrido el plazo de **2 meses** a partir de la primera votación de investidura ningún candidato obtiene la confianza, el Rey disolverá ambas Cámaras y convocará nuevas elecciones con el refrendo del Presidente del Congreso.
- **Cuestión de Confianza (Art. 112 y 114.1 CE)**: El Presidente del Gobierno, previa deliberación del Consejo de Ministros, puede plantear ante el Congreso la cuestión de confianza sobre su programa o una declaración de política general. La confianza se entiende otorgada cuando vote a favor la **mayoría simple** de los Diputados. Si no la obtiene, el Gobierno presenta su dimisión al Rey y se inicia el procedimiento del art. 99.
- **Moción de Censura (Art. 113 y 114.2 CE)**:
  - Exige responsabilidad política al Gobierno de forma constructiva (debe incluir un candidato a la Presidencia del Gobierno).
  - Propuesta por al menos la **décima parte de los Diputados (35 Diputados)**.
  - Periodo de enfriamiento: No puede ser votada hasta transcurridos **5 días** desde su presentación; en los 2 primeros días pueden presentarse mociones alternativas.
  - Aprobación exige **mayoría absoluta del Congreso de los Diputados**. Si se aprueba, el Gobierno presenta su dimisión al Rey y el candidato incluido en la moción se entiende investido de la confianza de la Cámara.

## 3. La Administración General del Estado (Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público)
La Administración General del Estado (AGE) actúa bajo la dirección del Gobierno para la gestión de los intereses generales. Su estructura se divide en:
1. **Servicios Centrales** (Ministerios y órganos directivos centrales).
2. **Servicios Territoriales** (Delegaciones del Gobierno, Subdelegaciones y Direcciones Insulares).
3. **Administración General del Estado en el Exterior** (Misiones diplomáticas permanentes, representaciones permanentes, delegaciones y oficinas consulares).

### Clasificación de Órganos en la AGE (Art. 55 Ley 40/2015)
- **Órganos Superiores**:
  - **Ministros**: Jefes superiores del departamento y miembros del Gobierno.
  - **Secretarios de Estado**: Responsables directos de la ejecución de la acción del Gobierno en un sector de actividad específico.
  - *Nombramiento*: Libre designación política (RD del Consejo de Ministros). No se exige condición de funcionario.
- **Órganos Directivos**:
  - **Subsecretarios** y **Secretarios Generales**: Rango de Subsecretario. Ostentan la representación ordinaria del Ministerio y jefatura superior del personal. Nombramiento por Real Decreto del Consejo de Ministros entre **funcionarios de carrera del Subgrupo A1** (salvo excepciones justificadas para Secretarios Generales).
  - **Secretarios Generales Técnicos** y **Directores Generales**: Rango de Director General. Nombramiento por RD del Consejo de Ministros entre **funcionarios del Subgrupo A1** (salvo excepciones por Real Decreto motivado para Directores Generales).
  - **Subdirectores Generales**: Responsables directos de la ejecución de proyectos y gestión ordinaria. Nombramiento por el Ministro o Secretario de Estado entre **funcionarios de carrera del Subgrupo A1** (sin excepciones).
  - En la organización territorial: **Delegados del Gobierno** (Rango de Subsecretario, nombrados libremente por RD sin exigir funcionario) y **Subdelegados del Gobierno en las provincias** (Rango de Subdirector General, nombrados por el Delegado del Gobierno obligatoriamente entre **funcionarios del Subgrupo A1**).
""",

    "raw/sources/bloque1-tema03.md": """---
title: "Bloque 1 - Tema 03: Organización Territorial del Estado y Entidades Locales"
type: "raw-source"
topic: "organizacion-territorial"
date: "2026-08-17"
---

# Bloque 1 - Tema 03: Organización Territorial del Estado, Comunidades Autónomas y Administración Local

## 1. Principios Constitucionales de la Organización Territorial (Título VIII CE)
- **Artículo 137 CE**: El Estado se organiza territorialmente en **Municipios**, en **Provincias** y en las **Comunidades Autónomas** que se constituyan. Todas estas entidades gozan de autonomía para la gestión de sus respectivos intereses.
- **Principios Rectores**:
  - **Unidad**: La Constitución se fundamenta en la indisoluble unidad de la Nación española (Art. 2).
  - **Autonomía**: Garantizada para nacionalidades y regiones, provincias y municipios (Art. 2 y 137). Autonomía política para las CCAA y administrativa para las Entidades Locales.
  - **Solidaridad**: El Estado garantiza la realización efectiva del principio de solidaridad interterritorial (Art. 138.1), velando por el equilibrio económico adecuado mediante el **Fondo de Compensación Interterritorial** (Art. 158.2).
  - **Igualdad**: Todos los españoles tienen los mismos derechos y obligaciones en cualquier parte del territorio del Estado (Art. 139.1). Ninguna autoridad podrá adoptar medidas que obstaculicen la libertad de circulación y establecimiento de personas y libre circulación de bienes (Art. 139.2).

## 2. Las Comunidades Autónomas: Vías de Acceso y Competencias
- **Vías de Acceso a la Autonomía**:
  - **Vía Ordinaria o Lenta (Art. 143 CE)**: Provincias limítrofes con características históricas, culturales y económicas comunes. Iniciativa por las Diputaciones Provinciales y las 2/3 partes de los municipios cuya población represente al menos la mayoría del censo electoral de cada provincia. Tras 5 años podían ampliar competencias al marco del art. 149.
  - **Vía Especial o Rápida (Art. 151 CE)**: Andalucía y nacionalidades históricas con plebiscito en el pasado (Disposición Transitoria 2ª: Cataluña, País Vasco, Galicia). Iniciativa por Diputaciones y 3/4 partes de los municipios de cada provincia que representen la mayoría del censo, y ratificación en referéndum por mayoría absoluta de electores de cada provincia. Asumían el máximo competencial inmediatamente.
- **Estatutos de Autonomía (Art. 147 CE)**: Norma institucional básica de cada Comunidad Autónoma, que el Estado reconoce y ampara como parte integrante de su ordenamiento jurídico. Aprobados mediante **Ley Orgánica**.
- **Distribución de Competencias (Art. 148 y 149 CE)**:
  - **Artículo 148**: Materias que pueden ser asumidas por las CCAA (ordenación del territorio, urbanismo, vivienda, obras públicas de interés autonómico, agricultura, ferias, fomento de la cultura y lengua propia).
  - **Artículo 149.1**: Competencias exclusivas del Estado (32 materias: nacionalidad, relaciones internacionales, defensa y Fuerzas Armadas, administración de justicia, legislación mercantil, penal, procesal y laboral, régimen aduanero, sistema monetario, bases y coordinación de la sanidad, seguridad pública, telecomunicaciones).
  - **Cláusulas de Cierre (Art. 149.3 CE)**:
    - *Cláusula Residual*: Las materias no atribuidas expresamente al Estado pueden ser asumidas por las CCAA en sus Estatutos. Las no asumidas corresponderán al Estado.
    - *Cláusula de Prevalencia*: Las normas estatales prevalecerán en caso de conflicto sobre las autonómicas en todo lo que no esté atribuido a la exclusiva competencia de éstas.
    - *Cláusula de Supletoriedad*: El derecho estatal será, en todo caso, supletorio del derecho de las Comunidades Autónomas.
- **Control sobre los órganos de las CCAA (Art. 153 CE)**:
  - Por el Tribunal Constitucional (constitucionalidad de normas con fuerza de ley).
  - Por el Gobierno, previo dictamen del Consejo de Estado (ejercicio de funciones delegadas del art. 150.2).
  - Por la Jurisdicción Contencioso-Administrativa (administración autónoma y normas reglamentarias).
  - Por el Tribunal de Cuentas (gestión económica y presupuestaria).
- **Artículo 155 CE (Coerción Estatal)**: Si una Comunidad Autónoma no cumpliere las obligaciones impuestas por la Constitución o las leyes, o actuare de forma que atente gravemente al interés general de España, el Gobierno, previo requerimiento al Presidente de la CA y, en el caso de no ser atendido, con la aprobación por **mayoría absoluta del Senado**, podrá adoptar las medidas necesarias para obligar a aquélla al cumplimiento forzoso o para la protección del interés general.

## 3. La Administración Local (Ley 7/1985, Reguladora de las Bases del Régimen Local - LRBRL)
- **El Municipio (Art. 140 CE y Art. 11 LRBRL)**: Entidad local básica de la organización territorial del Estado. Personalidad jurídica plena. Elementos: **Territorio (Término municipal)**, **Población (Padrón municipal)** y **Organización**.
  - Órgano de gobierno: El **Ayuntamiento**, integrado por el **Alcalde** y los **Concejales**. Concejales elegidos por los vecinos mediante sufragio universal proporcional (D'Hondt). El Alcalde es elegido por los Concejales (o directamente por los vecinos en municipios de Concejo Abierto).
- **La Provincia (Art. 141 CE)**: Entidad local con personalidad jurídica propia, determinada por la agrupación de municipios y división territorial para el cumplimiento de las actividades del Estado. Gobierno y administración encomendados a las **Diputaciones Provinciales** (u otras corporaciones representativas: Cabildos en Canarias, Consejos Insulares en Baleares).
""",

    "raw/sources/bloque1-tema04.md": """---
title: "Bloque 1 - Tema 04: La Unión Europea, Instituciones y Derecho Comunitario"
type: "raw-source"
topic: "union-europea"
date: "2026-08-17"
---

# Bloque 1 - Tema 04: La Unión Europea: Tratados, Instituciones y Fuentes del Derecho Comunitario

## 1. Evolución Histórica y Tratados de la Unión Europea
- **Tratados Constitutivos Originarios**:
  - Tratado de París (1951): Comunidad Europea del Carbón y del Acero (CECA).
  - Tratados de Roma (1957): Comunidad Económica Europea (CEE) y Comunidad Europea de la Energía Atómica (EURATOM).
- **Tratados de Modificación y Reforma**:
  - Acta Única Europea (1986): Mercado interior único y libre circulación de mercancías, personas, servicios y capitales.
  - **Tratado de Maastricht / Tratado de la Unión Europea (1992)**: Creación de la Unión Europea basada en 3 pilares, ciudadanía europea y unión económica y monetaria (Euro).
  - Tratado de Ámsterdam (1997) y Tratado de Niza (2001).
  - **Tratado de Lisboa (firmado en 2007, en vigor el 1 de diciembre de 2009)**: Elimina la estructura de pilares dotando a la UE de personalidad jurídica única. Modifica el TUE y transforma el TCE en el **TFUE (Tratado de Funcionamiento de la Unión Europea)**. Incorpora con valor jurídico vinculante la **Carta de los Derechos Fundamentales de la Unión Europea**. Creación del Presidente del Consejo Europeo y del Alto Representante para Asuntos Exteriores y Política de Seguridad.

## 2. Instituciones de la Unión Europea (Art. 13 TUE)
1. **Parlamento Europeo**:
   - Representa a los **ciudadanos de la Unión**. Elegido por sufragio universal directo cada **5 años**.
   - Sede oficial: Estrasburgo (plenos mensuales); trabajos de comisiones en Bruselas; Secretaría General en Luxemburgo.
   - Composición: Máximo 750 diputados más el Presidente (705 tras el Brexit, ampliado a 720). Ningún Estado tiene menos de 6 ni más de 96 escaños.
   - Funciones: Colegislador junto con el Consejo (Procedimiento Legislativo Ordinario), aprueba el presupuesto de la UE y ejerce control político sobre la Comisión (moción de censura).
2. **Consejo Europeo**:
   - Define las **orientaciones y prioridades políticas generales** de la UE. **NO ejerce funciones legislativas**.
   - Composición: Jefes de Estado o de Gobierno de los Estados miembros, su Presidente (elegido por 2,5 años renovable una vez) y el Presidente de la Comisión. Participa en los trabajos el Alto Representante.
   - Decisiones por consenso (salvo excepciones en los Tratados). Sede: Bruselas.
3. **El Consejo (Consejo de la Unión Europea / Consejo de Ministros)**:
   - Representa a los **Gobiernos de los Estados miembros**.
   - Composición: Un representante de cada Estado miembro a nivel ministerial, facultado para comprometer al Gobierno. Presidencia rotatoria semestral por ternas de países (salvo el Consejo de Asuntos Exteriores, presidido por el Alto Representante).
   - Votación por **Mayoría Cualificada (Doble Mayoría de Lisboa)**: Requiere al menos el **55% de los Estados miembros (mínimo 15 de 27)** que representen al menos el **65% de la población total de la UE**. Minoría de bloqueo: al menos 4 Estados que representen más del 35% de la población.
4. **Comisión Europea**:
   - Defiende el **interés general de la Unión** ("Guardiana de los Tratados"). Órgano ejecutivo y con monopolio de la iniciativa legislativa.
   - Composición: Un Colegio de Comisarios (1 por Estado miembro, actualmente 27) designados por 5 años por su competencia e independencia. Sede: Bruselas.
5. **Tribunal de Justicia de la Unión Europea (TJUE)**:
   - Garantiza el respeto del Derecho en la interpretación y aplicación de los Tratados. Sede: Luxemburgo.
   - Estructura: **Tribunal de Justicia** (1 juez por Estado miembro + 11 abogados generales) y **Tribunal General** (2 jueces por Estado miembro).
   - Procedimientos: Cuestión Prejudicial (planteada por jueces nacionales sobre interpretación de normas de la UE), Recurso por Incumplimiento (contra Estados), Recurso de Anulación (contra actos de instituciones).
6. **Banco Central Europeo (BCE)**: Sede en Fráncfort. Política monetaria de la zona euro.
7. **Tribunal de Cuentas**: Sede en Luxemburgo. Control de las finanzas y ejecución presupuestaria.

## 3. Fuentes del Derecho de la Unión Europea
- **Derecho Originario o Primario**: Tratados constitutivos (TUE, TFUE, Tratados de adhesión) y la Carta de Derechos Fundamentales. Rango supremo.
- **Derecho Derivado o Secundario (Art. 288 TFUE)**:
  - **Actos Obligatorios / Vinculantes**:
    - **Reglamento**: Alcance general, obligatorio en todos sus elementos y **directamente aplicable** en cada Estado miembro desde su publicación en el DOUE (sin transposición).
    - **Directiva**: Obliga al Estado miembro destinatario en cuanto al **resultado que deba conseguirse**, dejando a las autoridades nacionales la elección de la forma y los medios (**requiere transposición nacional** en un plazo fijado).
    - **Decisión**: Obligatoria en todos sus elementos para todos sus destinatarios si los designa específicamente.
  - **Actos No Vinculantes**:
    - **Recomendaciones**: Sugieren una conducta a seguir.
    - **Dictámenes**: Expresan un juicio o valoración de una institución.
- **Principios de Articulación con el Derecho Interno**:
  - **Principio de Primacía (Sentencia Costa c. ENEL, 1964)**: El Derecho de la UE prevalece sobre cualquier norma nacional contradictoria, incluso de rango constitucional.
  - **Efecto Directo (Sentencia Van Gend en Loos, 1963)**: Los particulares pueden invocar directamente normas claras, precisas e incondicionales de la UE ante los tribunales nacionales.
""",

    "raw/sources/bloque1-tema05.md": """---
title: "Bloque 1 - Tema 05: El Personal Funcionario al Servicio de las Administraciones Públicas (TREBEP)"
type: "raw-source"
topic: "trebep-empleado-publico"
date: "2026-08-17"
---

# Bloque 1 - Tema 05: El Personal al Servicio de las Administraciones Públicas: TREBEP (RD Legislativo 5/2015)

## 1. Clases de Personal al Servicio de las Administraciones Públicas (Art. 8 a 13 TREBEP)
- **Funcionarios de Carrera (Art. 9)**: Quienes, en virtud de nombramiento legal, están vinculados a una Administración Pública por una relación estatutaria regulada por el Derecho Administrativo para el desempeño de servicios profesionales retribuidos de carácter permanente. En todo caso, el ejercicio de las funciones que impliquen la participación directa o indirecta en el ejercicio de las potestades públicas o en la salvaguardia de los intereses generales del Estado corresponden exclusivamente a los funcionarios públicos.
- **Funcionarios Interinos (Art. 10)**: Nombrados por razones expresamente justificadas de necesidad y urgencia para plazas vacantes (máximo 3 años), sustitución transitoria de titulares, ejecución de programas temporales (máx 3 años ampliable 12 meses) o exceso/acumulación de tareas (máx 9 meses en 18 meses).
- **Personal Laboral (Art. 11)**: En virtud de contrato de trabajo formalizado por escrito en cualquiera de las modalidades previstas en la legislación laboral (Fijo, Por tiempo indefinido o Temporal).
- **Personal Eventual (Art. 12)**: Nombramiento libre y cese libre para funciones expresamente calificadas como de **confianza o asesoramiento especial**. No constituye mérito para el acceso a la función pública.
- **Personal Directivo Profesional (Art. 13)**: Desarrolla funciones directivas profesionales sujetas a evaluación de resultados.

### Grupos de Clasificación Profesional de Funcionarios (Art. 76 y Disp. Transitoria 3ª):
- **Grupo A**: Dividido en dos subgrupos:
  - **Subgrupo A1**: Título universitario de Grado (Doctor, Licenciado, Grado). Funciones directivas, de gestión, inspección y control.
  - **Subgrupo A2**: Título universitario de Grado (Diplomado, Grado). Funciones de gestión y ejecución.
- **Grupo B**: Título de Técnico Superior (Formación Profesional de Grado Superior).
- **Grupo C**: Dividido en dos subgrupos:
  - **Subgrupo C1**: Título de Bachiller o Técnico (FP Grado Medio).
  - **Subgrupo C2**: Título de Graduado en ESO.
- Otras agrupaciones profesionales sin requisito de titulación (antiguo Grupo E).

## 2. Derechos y Deberes de los Empleados Públicos
- **Derechos Individuales (Art. 14)**: Inamovilidad en la condición de funcionario de carrera, carrera profesional y promoción interna, retribuciones justas, formación continua, vacaciones, permisos y licencias, jubilación.
- **Derechos de Ejercicio Colectivo (Art. 15)**: Libertad sindical, huelga, negociación colectiva, reunión.
- **Código de Conducta (Art. 52 a 54)**:
  - *Principios Éticos (Art. 53)*: Lealtad a la Constitución, neutralidad política, eficacia, confidencialidad, no aceptación de regalos que superen usos habituales, dedicación al servicio público.
  - *Principios de Conducta (Art. 54)*: Trato respetuoso, diligencia, austeridad en el uso de recursos públicos, obediencia a instrucciones legítimas de superiores (salvo orden manifiestamente ilegal, en cuyo caso se pondrá por escrito a conocimiento del superior).

## 3. Situaciones Administrativas de los Funcionarios de Carrera (Art. 85 a 92)
1. **Servicio Activo (Art. 86)**: Desempeño de puesto de trabajo propio de su cuerpo/escala. Gozan de todos los derechos y deberes.
2. **Servicios Especiales (Art. 87)**: Nombramiento como miembros del Gobierno, Ministros, Secretarios de Estado, Diputados, Senadores, miembros del TC, CGPJ, puestos en organismos internacionales o gabinete de Ministros. **Computa tiempo a efectos de trienios, carrera y derechos pasivos**. Reserva de plaza en la misma localidad y retribuciones del puesto desempeñado.
3. **Servicio en otras Administraciones Públicas (Art. 88)**: Transferencias autonómicas o provisión de puestos por concurso/libre designación en otra Administración.
4. **Excedencias (Art. 89)**:
   - *Por interés particular*: Exige haber prestado servicios efectivos durante un mínimo de **5 años** inmediatamente anteriores. Duración mínima continuada de **2 años**. No devenga retribuciones ni computa para trienios ni carrera.
   - *Por agrupación familiar*: Cónyuge reside en otra localidad por haber obtenido puesto definitivo en cualquier Administración. Sin requisito de tiempo previo. No devenga retribuciones ni computa.
   - *Por cuidado de familiares*: Cuidado de cada hijo (máximo **3 años** desde nacimiento/adopción) o familiar hasta 2º grado por consanguinidad/afinidad que no pueda valerse por sí mismo (máximo **3 años**). **Computa a efectos de trienios, carrera y derechos pasivos**. Reserva del puesto de trabajo durante los primeros **2 años** (el 3º año reserva de puesto en la misma localidad y de igual nivel).
   - *Por razón de violencia de género / terrorismo*: Sin tiempo mínimo. Primeros **6 meses** con reserva del puesto y derecho a percibir retribuciones íntegras.
5. **Suspensión de Funciones (Art. 90)**:
   - *Provisional*: Durante tramitación de proceso penal o disciplinario. Máximo **6 meses** (salvo paralización imputable al funcionario). Percibe retribuciones básicas (sueldo y trienios).
   - *Firme*: Por condena penal o sanción disciplinaria. No puede exceder de **6 años**. Pérdida del puesto de trabajo si excede de 6 meses.

## 4. Régimen Disciplinario (Art. 93 a 98)
- **Faltas Muy Graves (Art. 95)**: Prescriben a los **3 años**. Entre ellas:
  - Incumplimiento del deber de fidelidad a la Constitución en el ejercicio de la función pública.
  - Discriminación por razón de sexo, raza, religión, discapacidad, orientación sexual.
  - Abandono del servicio o no asunción de tareas encomendadas.
  - Adopción de acuerdos manifiestamente ilegales que causen perjuicio grave.
  - Publicación o utilización indebida de secretos oficiales o información reservada.
  - Notoria falta de rendimiento continuada.
  - Acoso laboral, sexual y por razón de sexo.
- **Faltas Graves**: Prescriben a los **2 años**.
- **Faltas Leves**: Prescriben a los **6 meses**.
- **Sanciones Disciplinarias (Art. 96)**: Separación del servicio (solo para muy graves, priva de la condición de funcionario), despido disciplinario (personal laboral), suspensión firme de funciones (máximo 6 años), traslado forzoso con o sin cambio de localidad, demérito, apercibimiento.
- **Prescripción de las Sanciones**: Sanciones muy graves prescriben a los **3 años**, graves a los **2 años**, leves al **1 año**.
""",

    "raw/sources/bloque1-tema06.md": """---
title: "Bloque 1 - Tema 06: Políticas de Igualdad y Violencia de Género"
type: "raw-source"
topic: "igualdad-genero"
date: "2026-08-17"
---

# Bloque 1 - Tema 06: Políticas de Igualdad de Género (LO 3/2007) y Contra la Violencia de Género (LO 1/2004)

## 1. Ley Orgánica 3/2007, de 22 de marzo, para la igualdad efectiva de mujeres y hombres
- **Objeto (Art. 1)**: Hacer efectivo el derecho de igualdad de trato y de oportunidades entre mujeres y hombres, en particular mediante la eliminación de la discriminación de la mujer en cualesquiera de los ámbitos de la vida.
- **Conceptos Clave**:
  - **Discriminación Directa por Razón de Sexo (Art. 6.1)**: Situación en que se encuentra una persona que haya sido, sea o pudiera ser tratada de manera menos favorable que otra en situación comparable por razón de su sexo.
  - **Discriminación Indirecta (Art. 6.2)**: Situación en que una disposición, criterio o práctica aparentemente neutros pone a personas de un sexo en desventaja particular con respecto a personas del otro, salvo que dicha disposición, criterio o práctica puedan justificarse objetivamente con una finalidad legítima.
  - **Acoso Sexual (Art. 7.1)**: Cualquier comportamiento, verbal o físico, de naturaleza sexual que tenga el propósito o produzca el efecto de atentar contra la dignidad de una persona, en particular cuando se crea un entorno intimidatorio, degradante u ofensivo.
  - **Acoso por Razón de Sexo (Art. 7.2)**: Cualquier comportamiento realizado en función del sexo de una persona con el propósito o el efecto de atentar contra su dignidad.
  - **Acciones Positivas (Art. 11)**: Medidas específicas a favor de las mujeres para corregir situaciones patentes de desigualdad de hecho respecto de los hombres.
- **Transversalidad del Principio de Igualdad (Mainstreaming - Art. 15)**: Principio informador que debe presidir con carácter transversal la actuación de todos los poderes públicos.
- **Planes de Igualdad en las Empresas (Art. 45 y 46)**: Conjunto ordenado de medidas evaluables adoptadas tras realizar un diagnóstico de situación. Obligatorios para empresas de **50 o más trabajadores**.
- **Presencia Equilibrada (Disposición Adicional 1ª)**: Presencia de mujeres y hombres de forma que ningún sexo supere el 60% ni sea inferior al 40%.

## 2. Ley Orgánica 1/2004, de 28 de diciembre, de Medidas de Protección Integral contra la Violencia de Género
- **Concepto de Violencia de Género (Art. 1)**: La violencia que, como manifestación de la discriminación, la situación de desigualdad y las relaciones de poder de los hombres sobre las mujeres, se ejerce sobre éstas por parte de quienes sean o hayan sido sus **cónyuges o de quienes estén o hayan estado ligados a ellas por relaciones similares de afectividad, aun sin convivencia**.
- **Derechos de las Víctimas**:
  - Derecho a la información, asistencia jurídica gratuita inmediata y atención psicológica integral.
  - Derechos laborales: Reducción o reordenación del tiempo de trabajo, movilidad geográfica forzosa con reserva de puesto, suspensión del contrato de trabajo y extinción voluntaria con derecho a desempleo.
- **Juzgados de Violencia sobre la Mujer (JVM)**: Órganos judiciales especializados dentro del orden jurisdiccional penal con competencias mixtas (penal y civil en procesos de familia vinculados).
""",

    "raw/sources/bloque1-tema07.md": """---
title: "Bloque 1 - Tema 07: El Procedimiento Administrativo Común (Ley 39/2015 LPACAP)"
type: "raw-source"
topic: "ley-39-2015-lpacap"
date: "2026-08-17"
---

# Bloque 1 - Tema 07: El Procedimiento Administrativo Común de las Administraciones Públicas (Ley 39/2015 LPACAP)

## 1. Estructura y Ámbito de Aplicación de la Ley 39/2015, de 1 de octubre
Consta de 133 artículos estructurados en 1 Título Preliminar y 6 Títulos numerados, 5 Disposiciones Adicionales, 5 Disposiciones Transitorias, 1 Disposición Derogatoria y 7 Disposiciones Finales.
- Título Preliminar: Disposiciones generales (ámbito de aplicación y principios).
- Título I: De los interesados en el procedimiento (capacidad de obrar, representación, identificación y firma electrónica).
- Título II: De la actividad de las Administraciones Públicas (normas de emisión de documentos, registros, archivo y cómputo de plazos).
- Título III: De los actos administrativos (requisitos, eficacia, nulidad y anulabilidad).
- Título IV: De las disposiciones sobre el procedimiento administrativo común (iniciación, ordenación, instrucción y finalización).
- Título V: De la revisión de los actos en vía administrativa (revisión de oficio y recursos administrativos).
- Título VI: De la iniciativa legislativa y potestad normativa.

## 2. Los Interesados y la Relación Electrónica con la Administración
- **Sujetos Obligados a Relacionarse Electrónicamente (Art. 14.2)**:
  - Personas jurídicas.
  - Entidades sin personalidad jurídica.
  - Quienes ejerzan una actividad profesional que requiera colegiación obligatoria.
  - Quienes representen a un interesado obligado.
  - **Los empleados de las Administraciones Públicas** para los trámites realizados por razón de su condición de empleado público.
- **Identificación y Firma Electrónica (Art. 9 y 10)**: Firma obligatoria para formular solicitudes, presentar declaraciones responsables, interponer recursos, desistir y renunciar.

## 3. Cómputo de Plazos Administrativos (Art. 30)
- **Cómputo en Horas**: Salvo que por Ley o en el Derecho de la UE se fije otro cómputo, las horas son **hábiles** (todas las del día que formen parte de un día hábil). Se cuentan de hora en hora y de minuto en minuto desde la hora y minuto en que tenga lugar la notificación.
- **Cómputo en Días**: Salvo que por Ley o en Derecho UE se exprese que son naturales, los días son **HÁBILES**, entendiéndose que se **excluyen del cómputo los sábados, los domingos y los declarados festivos**. Se cuentan a partir del **día siguiente** a aquel en que tenga lugar la notificación o publicación.
- **Cómputo en Meses o Años**: Se computan **de fecha a fecha** a partir del día siguiente a la notificación. Si en el mes de vencimiento no hubiera día equivalente, el plazo expira el último día del mes. Si el último día es inhábil, se prorroga al primer día hábil siguiente.

## 4. Eficacia, Nulidad y Anulabilidad de los Actos Administrativos
- **Eficacia (Art. 39)**: Los actos se presumen válidos y producen efectos desde la fecha en que se dicten, salvo que en ellos se disponga otra cosa o su eficacia esté demorada por notificación, publicación o aprobación superior.
- **Actos Nulos de Pleno Derecho (Art. 47.1)** - *Vicio Insubsanable, Imprescriptible, Efectos Ex Tunc (desde el origen)*:
  a) Lesionen derechos y libertades susceptibles de amparo constitucional (Art. 14 a 29 CE).
  b) Dictados por órgano manifiestamente incompetente por razón de la materia o del territorio.
  c) Contenido imposible.
  d) Constitutivos de infracción penal o dictados como consecuencia de ésta.
  e) Dictados prescindiendo total y absolutamente del procedimiento legalmente establecido o de las normas de formación de la voluntad de órganos colegiados.
  f) Actos expresos o presuntos contrarios al ordenamiento jurídico por los que se adquieran facultades o derechos cuando se carezca de los requisitos esenciales.
  g) Cualquier otro establecido expresamente en una disposición con rango de Ley.
- **Actos Anulables (Art. 48)** - *Vicio Subsanable, Convalidable (Art. 52), Prescriptible (4 años)*:
  - Son anulables los actos de la Administración que incurran en cualquier infracción del ordenamiento jurídico, incluso la desviación de poder.
  - El defecto de forma solo determinará la anulabilidad cuando el acto carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados.
  - La realización de actuaciones fuera del tiempo establecido solo implicará la anulabilidad cuando así lo imponga la naturaleza del término o plazo.

## 5. Fases del Procedimiento Administrativo Común
1. **Iniciación (Art. 54 a 69)**: De oficio (por propia iniciativa, orden superior, petición razonada o denuncia) o a solicitud del interesado.
2. **Ordenación (Art. 70 a 74)**: Principio de celeridad, impulso de oficio, tramitación en orden riguroso de incoación.
3. **Instrucción (Art. 75 a 83)**: Alegaciones, prueba (periodo de 10 a 30 días), informes (preceptivos/facultativos, vinculantes/no vinculantes, plazo 10 días), **trámite de audiencia** (plazo de **10 a 15 días** para alegar antes de la propuesta de resolución; se puede prescindir si no figuran en el procedimiento ni se tienen en cuenta otros hechos que los alegados por el interesado).
4. **Finalización (Art. 84 a 95)**: Resolución expresa, desistimiento, renuncia, caducidad (paralización por causa imputable al interesado durante 3 meses) o terminación convencional.

## 6. Recursos Administrativos (Título V, Art. 112 a 126)
Ponen fin a la vía administrativa (Art. 114): Resoluciones de recursos de alzada, resoluciones de órganos administrativos que carezcan de superior jerárquico (salvo ley en contrario), acuerdos y pactos de terminación convencional.

| Recurso | Actos Contra los que Procede | Órgano ante el que se Interpone | Órgano que Resuelve | Plazo de Interposición | Plazo Máximo para Resolver y Notificar | Efecto del Silencio Administrativo |
|---------|------------------------------|---------------------------------|---------------------|------------------------|----------------------------------------|------------------------------------|
| **Recurso de Alzada** (Art. 121-122) | Actos que **NO ponen fin a la vía administrativa** y actos de trámite cualificados | Ante el órgano que dictó el acto o ante el superior jerárquico | **Superior jerárquico** | **1 mes** (acto expreso) / En cualquier momento desde el día siguiente al silencio | **3 meses** | **Desestimatorio** (salvo en la "alzada impropia" contra la desestimación por silencio de una solicitud previa, donde el silencio es ESTIMATORIO) |
| **Recurso Potestativo de Reposición** (Art. 123-124) | Actos que **SÍ ponen fin a la vía administrativa** | Ante el **mismo órgano que dictó el acto** | El **mismo órgano** que lo dictó | **1 mes** (acto expreso) / En cualquier momento desde el día siguiente al silencio | **1 mes** | **Desestimatorio** (permite acudir a la vía Contencioso-Administrativa) |
| **Recurso Extraordinario de Revisión** (Art. 125-126) | Actos **firmes en vía administrativa** cuando concurran 4 causas tasadas (error de hecho documental, documentos decisivos recobrados, documentos/testimonios falsos, sentencia por prevaricación/cohecho) | Ante el órgano competente que dictó el acto | El **mismo órgano** | **3 meses** (causas 2, 3 y 4) / **4 años** (causa 1: error de hecho) | **3 meses** | **Desestimatorio** |
""",

    "raw/sources/bloque1-tema08.md": """---
title: "Bloque 1 - Tema 08: Régimen Jurídico del Sector Público (Ley 40/2015 LRJSP)"
type: "raw-source"
topic: "ley-40-2015-lrjsp"
date: "2026-08-17"
---

# Bloque 1 - Tema 08: Régimen Jurídico del Sector Público (Ley 40/2015 LRJSP)

## 1. Estructura y Principios Generales de la Ley 40/2015, de 1 de octubre
Consta de 158 artículos estructurados en 1 Título Preliminar y 3 Títulos numerados, 22 Disposiciones Adicionales, 4 Disposiciones Transitorias, 1 Disposición Derogatoria y 18 Disposiciones Finales.
- **Principios Generales de Actuación (Art. 3)**: Eficacia, jerarquía, descentralización, desconcentración, coordinación, cooperación y colaboración, transparencia, servicio efectivo a los ciudadanos, simplicidad y racionalidad organizativa, buena fe y confianza legítima.
- **Principio de Personalidad Jurídica (Art. 3.4)**: Cada una de las Administraciones Públicas actúa para el cumplimiento de sus fines con personalidad jurídica única.

## 2. Funcionamiento Electrónico del Sector Público (Art. 38 a 46)
- **Sede Electrónica (Art. 38)**: Dirección electrónica disponible para los ciudadanos a través de redes de telecomunicaciones cuya titularidad corresponde a una Administración Pública. Garantiza identificación, integridad y confidencialidad mediante certificados electrónicos de sede.
- **Portal de Internet (Art. 39)**: Punto de acceso electrónico que permite el acceso a información y sedes electrónicas.
- **Punto de Acceso General Electrónico (PAGe - Art. 40)**: Facilita el acceso a los servicios, trámites e información de la AGE.
- **Actuación Administrativa Automatizada (Art. 41)**: Cualquier acto o actuación realizada íntegramente a través de medios electrónicos por una Administración en el marco de un procedimiento, sin intervención directa de una persona física. Requiere definición previa de órganos competentes y sistemas de firma (Sello electrónico de órgano o Código Seguro de Verificación - CSV).
- **Esquema Nacional de Interoperabilidad (ENI - Art. 45)** y **Esquema Nacional de Seguridad (ENS - Art. 46)**: Marcos de obligado cumplimiento para garantizar la interoperabilidad técnica, semántica y organizativa, y la seguridad integral de los sistemas y datos.

## 3. Órganos Colegiados (Art. 15 a 24)
- Formados por 3 o más miembros.
- **Régimen de Funcionamiento**:
  - Convocatoria: Remitida por el Secretario con antelación mínima de 2 días salvo urgencia, incluyendo el Orden del Día.
  - Quórum para válidamente constituirse: Presencia del Presidente y Secretario (o sustitutos) y de al menos la mitad de los miembros.
  - Votaciones: Mayoría simple. El Presidente ostenta voto de calidad en caso de empate. Los miembros no pueden abstenerse en las votaciones si ostentan la condición de autoridades o personal al servicio de las AAPP por razón de su cargo.
  - **Acta de la Sesión**: Redactada por el Secretario, aprobada en la misma o en la siguiente sesión.

## 4. La Responsabilidad Patrimonial de las Administraciones Públicas (Art. 32 a 37)
- **Principio General (Art. 32.1 y Art. 106.2 CE)**: Los particulares tendrán derecho a ser indemnizados por las Administraciones Públicas de toda lesión que sufran en cualquiera de sus bienes y derechos, salvo en los casos de fuerza mayor, siempre que la lesión sea consecuencia del funcionamiento normal o anormal de los servicios públicos.
- **Requisitos de la Responsabilidad**:
  1. Daño efectivo, evaluable económicamente e individualizado con relación a una persona o grupo de personas.
  2. El daño no debe ser deber jurídico del particular de soportarlo de acuerdo con la Ley.
  3. Relación de causalidad directa e inmediata entre el funcionamiento del servicio público y la lesión.
- **Plazo de Prescripción del Derecho a Reclamar (Art. 67 Ley 39/2015)**: **1 año** desde que se produjo el hecho lesivo o desde la curación o determinación del alcance de las secuelas (en daños físicos/psíquicos).
- **Responsabilidad Concurrente de varias AAPP**: Solidaria cuando derive de fórmulas conjuntas de actuación.
""",

    "raw/sources/bloque1-tema09.md": """---
title: "Bloque 1 - Tema 09: Protección de Datos Personales (RGPD y LOPDGDD)"
type: "raw-source"
topic: "proteccion-datos"
date: "2026-08-17"
---

# Bloque 1 - Tema 09: Protección de Datos Personales: RGPD (UE 2016/679) y LOPDGDD (Ley Orgánica 3/2018)

## 1. Marco Normativo de Protección de Datos
- **Reglamento (UE) 2016/679 (RGPD / GDPR)**: Aplicable directamente en toda la Unión Europea desde el **25 de mayo de 2018**.
- **Ley Orgánica 3/2018, de 5 de diciembre (LOPDGDD)**: De Protección de Datos Personales y garantía de los derechos digitales. Adapta el ordenamiento español al RGPD e introduce el Título X dedicado a los Derechos Digitales.

## 2. Principios Fundamentales del Tratamiento de Datos (Art. 5 RGPD)
1. **Licitud, lealtad y transparencia**: Tratado de forma lícita, leal y transparente en relación con el interesado.
2. **Limitación de la finalidad**: Recogidos con fines determinados, explícitos y legítimos, y no tratados ulteriormente de manera incompatible.
3. **Minimización de datos**: Adecuados, pertinentes y limitados a lo necesario en relación con los fines (**"data minimization"**).
4. **Exactitud**: Exactos y actualizados; supresión o rectificación inmediata de datos inexactos.
5. **Limitación del plazo de conservación**: Mantenidos durante no más tiempo del necesario para los fines del tratamiento.
6. **Integridad y confidencialidad**: Tratados garantizando una seguridad adecuada contra el tratamiento no autorizado o ilícito y contra su pérdida, destrucción o daño accidental mediante medidas técnicas u organizativas.
7. **Responsabilidad proactiva (*Accountability*)**: El responsable del tratamiento será responsable del cumplimiento y capaz de demostrarlo.

## 3. Bases de Legitimación del Tratamiento (Art. 6 RGPD)
- Consentimiento explícito del interesado.
- Ejecución de un contrato.
- Cumplimiento de una obligación legal aplicable al responsable.
- Protección de intereses vitales del interesado o de otra persona.
- Cumplimiento de una misión realizada en **interés público o en el ejercicio de poderes públicos**.
- Satisfacción de intereses legítimos del responsable o de un tercero (salvo cuando prevalezcan los derechos fundamentales del interesado, especialmente niños). *Nota*: Las autoridades públicas NO pueden acogerse al interés legítimo en el ejercicio de sus funciones.

## 4. Derechos de los Ciudadanos (Derechos ARCO-POL)
- **Acceso (Art. 15 RGPD)**: Conocer si se tratan sus datos y obtener copia gratuita.
- **Rectificación (Art. 16 RGPD)**: Modificación de datos inexactos o incompletos.
- **Supresión ("Derecho al Olvido" - Art. 17 RGPD)**: Eliminación de datos cuando ya no sean necesarios o se retire el consentimiento.
- **Limitación del Tratamiento (Art. 18 RGPD)**: Marcar los datos para suspender su tratamiento mientras se verifica su exactitud o licitud.
- **Portabilidad (Art. 20 RGPD)**: Recibir los datos en formato estructurado, de uso común y lectura mecánica interoperable (ej. JSON, XML, CSV).
- **Oposición (Art. 21 RGPD)**: Oponerse al tratamiento por motivos relacionados con su situación particular.
- **Decisiones individuales automatizadas (Art. 22 RGPD)**: Derecho a no ser objeto de una decisión basada únicamente en el tratamiento automatizado, incluida la elaboración de perfiles (*profiling*).
- **Plazo de Respuesta**: El responsable debe responder en el plazo máximo de **1 mes** a partir de la recepción de la solicitud (prorrogable 2 meses más en casos complejos).

## 5. El Delegado de Protección de Datos (DPD / DPO - Art. 37 RGPD y Art. 34 LOPDGDD)
- **Designación Obligatoria**:
  - Cuando el tratamiento lo realice una **autoridad u organismo público** (salvo tribunales en ejercicio de función judicial).
  - Cuando las actividades principales requieran observación habitual y sistemática de interesados a gran escala.
  - Cuando las actividades consistan en el tratamiento a gran escala de categorías especiales de datos.
- **Posición y Funciones**: Nombrado por sus cualidades profesionales y conocimientos especializados. Debe comunicarse su designación a la AEPD en **10 días**. Actúa con total independencia y no puede recibir instrucciones sobre el ejercicio de sus funciones.

## 6. La Agencia Española de Protección de Datos (AEPD)
- Autoridad administrativa independiente de ámbito estatal con personalidad jurídica propia y plena independencia.
- Potestades de investigación, correctivas (apercibimientos, órdenes de cumplimiento) y sancionadoras.
- Sanciones económicas: Hasta 10 o 20 millones de euros (o del 2% al 4% del volumen de negocio anual global para empresas). *En el sector público*, la sanción económica es sustituida por un **apercibimiento** formal y propuesta de iniciación de expediente disciplinario a los responsables (Art. 77 LOPDGDD).
""",

    "raw/sources/bloque1-tema10.md": """---
title: "Bloque 1 - Tema 10: Transparencia, Acceso a la Información Pública y Buen Gobierno"
type: "raw-source"
topic: "transparencia"
date: "2026-08-17"
---

# Bloque 1 - Tema 10: Transparencia y Acceso a la Información Pública: Ley 19/2013

## 1. La Ley 19/2013, de 9 de diciembre, de Transparencia, Acceso a la Información Pública y Buen Gobierno
Tiene por objeto ampliar y reforzar la transparencia de la actividad pública, regular y garantizar el derecho de acceso a la información relativa a aquella y establecer las obligaciones de buen gobierno que deben cumplir los responsables públicos.
Estructurada en 3 Títulos:
- Título I: Transparencia de la actividad pública (Publicidad activa y Derecho de acceso).
- Título II: Buen gobierno (Principios éticos, de conducta y régimen sancionador de altos cargos).
- Título III: Consejo de Transparencia y Buen Gobierno.

## 2. Publicidad Activa (Título I, Capítulo II)
- Los sujetos obligados deben publicar de forma periódica, actualizada, comprensible y en formatos reutilizables la información relevante para garantizar la transparencia:
  - **Información Institucional y Organizativa (Art. 6)**: Estructura, organigramas, funciones, normativa.
  - **Información de Relevancia Jurídica (Art. 7)**: Directrices, instrucciones, proyectos de ley y reglamentos.
  - **Información Económica, Presupuestaria y Estadística (Art. 8)**: Contratos, convenios, subvenciones, presupuestos anuales, cuentas anuales, retribuciones de altos cargos, declaraciones de bienes e incompatibilidades.
- **Portal de la Transparencia**: Plataforma oficial centralizada de la AGE para facilitar el acceso a la publicidad activa.

## 3. Derecho de Acceso a la Información Pública (Capítulo III)
- Todas las personas tienen derecho a acceder a la información pública, entendida como los contenidos o documentos, cualquiera que sea su formato o soporte, que obren en poder de los sujetos obligados y que hayan sido elaborados o adquiridos en el ejercicio de sus funciones.
- **Límites al Derecho de Acceso (Art. 14)**:
  - Seguridad nacional, defensa, relaciones exteriores, seguridad pública, prevención e investigación de delitos, funciones administrativas de vigilancia y control, secreto comercial y propiedad intelectual, protección del medio ambiente.
  - Aplicación justificada, proporcionada y caso por caso mediante el *test del daño* y el *test del interés público*.
- **Procedimiento de Acceso (Art. 17 a 22)**:
  - Solicitud por cualquier medio que permita tener constancia. No requiere motivar la solicitud.
  - Plazo máximo para resolver y notificar: **1 mes** desde la recepción de la solicitud por el órgano competente (prorrogable otro mes en casos de volumen o complejidad).
  - Silencio Administrativo: Si transcurre el plazo sin resolución expresa, la solicitud se entenderá **DESESTIMADA**.
- **Reclamación ante el Consejo de Transparencia (Art. 23 y 24)**:
  - Reclamación previa y potestativa a la vía judicial contencioso-administrativa.
  - Plazo de interposición: **1 mes** desde la notificación del acto o desde el día siguiente a la producción del silencio.
  - Plazo para resolver la reclamación: **3 meses** (el silencio es desestimatorio).

## 4. El Consejo de Transparencia y Buen Gobierno (CTBG)
- Organismo público independiente adscrito a efectos organizativos al Ministerio de Transformación Digital y Función Pública.
- Vela por el cumplimiento de las obligaciones de publicidad activa y resuelve las reclamaciones frente a denegaciones del derecho de acceso a la información pública.
- Presidido por el Presidente del Consejo de Transparencia, nombrado por Real Decreto para un mandato de **5 años no renovable**.
"""
}

print("[*] Escribiendo 10 fuentes brutas oficiales en raw/sources/bloque1-tema*.md...")
for path, content in RAW_SOURCES.items():
    write_file(path, content)

print("[*] 10 fuentes brutas del Bloque 1 generadas con éxito.")
