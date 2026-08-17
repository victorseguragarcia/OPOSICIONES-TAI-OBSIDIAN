# -*- coding: utf-8 -*-
r"""
Script generador de las 4 Guías Maestras de Síntesis del Temario TAI con enlaces exactos:
- wiki/synthesis/bloque1-tai-oposiciones-master-guide.md
- wiki/synthesis/bloque2-tai-oposiciones-master-guide.md
- wiki/synthesis/bloque3-tai-oposiciones-master-guide.md
- wiki/synthesis/bloque4-tai-oposiciones-master-guide.md
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

BLOQUES_SYNTHESIS = {
    # =========================================================================
    # BLOQUE 1 MASTER SYNTHESIS
    # =========================================================================
    "wiki/synthesis/bloque1-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 1: Organización del Estado, Administración Pública y Marco Digital (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-1
  - oposiciones
  - tai
  - constitucion
  - lpacap
  - lrjsp
  - trebep
  - administracion-digital
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

# 🔴 Guía Maestra de Bloque 1: Organización del Estado, Administración Pública y Marco Digital (TAI)

Compendio estructurado de estudio para el **Bloque 1**, integrando el Derecho Constitucional, Administrativo, Función Pública y el Marco de Administración Electrónica de la AGE.

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 1 (10 Temas)

| Tema | Materia Oficial | Fuente Resumida | Entidades Principales | Guías y Cheatsheets Clave |
|:---|:---|:---|:---|:---|
| **Tema 01** | La Constitución Española de 1978 | [[wiki/sources/bloque1-tema01|Resumen Tema 01]] | [[wiki/entities/constitucion-espanola-1978|CE 1978]], [[wiki/entities/cortes-generales|Cortes Generales]] | [[wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet|Cheatsheet Constitución]] |
| **Tema 02** | El Gobierno y la AGE | [[wiki/sources/bloque1-tema02|Resumen Tema 02]] | [[wiki/entities/gobierno-y-age|Gobierno y AGE]] | Órganos Superiores vs Directivos |
| **Tema 03** | Organización Territorial y CCAA | [[wiki/sources/bloque1-tema03|Resumen Tema 03]] | [[wiki/entities/comunidades-autonomas-y-ee-ll|CCAA y EE.LL.]] | Competencias Arts. 148 / 149 CE |
| **Tema 04** | La Unión Europea y Derecho Comunitario | [[wiki/sources/bloque1-tema04|Resumen Tema 04]] | [[wiki/entities/instituciones-union-europea|Instituciones UE]] | [[wiki/synthesis/instituciones-europeas-composicion-y-sedes-guia|Guía Instituciones UE]] |
| **Tema 05** | El Empleado Público y el TREBEP | [[wiki/sources/bloque1-tema05|Resumen Tema 05]] | [[wiki/entities/trebep-empleado-publico|TREBEP (RDL 5/2015)]] | [[wiki/synthesis/trebep-situaciones-y-regimen-disciplinario-guia|Guía TREBEP Situaciones]] |
| **Tema 06** | Igualdad y Violencia de Género | [[wiki/sources/bloque1-tema06|Resumen Tema 06]] | [[wiki/entities/ley-igualdad-y-violencia-genero|LO 3/2007 y LO 1/2004]] | Planes de Igualdad (50+ trab.) |
| **Tema 07** | Procedimiento Administrativo (LPACAP) | [[wiki/sources/bloque1-tema07|Resumen Tema 07]] | [[wiki/entities/ley-39-2015-lpacap|Ley 39/2015 LPACAP]] | [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Cheatsheet Plazos]], [[wiki/synthesis/recursos-administrativos-comparativa-guia|Recursos]] |
| **Tema 08** | Régimen Jurídico del Sector Público (LRJSP) | [[wiki/sources/bloque1-tema08|Resumen Tema 08]] | [[wiki/entities/ley-40-2015-lrjsp|Ley 40/2015 LRJSP]] | [[wiki/synthesis/gestion-documento-y-expediente-electronico-eni-guia|Expediente NTI]], [[wiki/synthesis/servicios-comunes-age-administracion-electronica-cheatsheet|Servicios Comunes]] |
| **Tema 09** | Protección de Datos (RGPD y LOPDGDD) | [[wiki/sources/bloque1-tema09|Resumen Tema 09]] | [[wiki/entities/rgpd-y-lopdgdd|RGPD / LOPDGDD]], [[wiki/entities/aepd-agencia-proteccion-datos|AEPD]] | [[wiki/synthesis/derechos-digitales-titulo-x-lopdgdd-cheatsheet|Derechos Digitales (Título X)]] |
| **Tema 10** | Transparencia y Acceso a la Información | [[wiki/sources/bloque1-tema10|Resumen Tema 10]] | [[wiki/entities/ley-19-2013-transparencia|Ley 19/2013 Transparencia]] | Consejo de Transparencia (CTBG) |

---

## 🟣 2. Síntesis de los Conceptos de Máxima Pregunta en Examen

### A. Procedimiento Administrativo Común (Ley 39/2015)
- **Actos Nulos de Pleno Derecho (Art. 47)**: Tasados expresamente (lesión de DDFF, incompetencia manifiesta por razón de materia/territorio, contenido imposible, delito, omisión total del procedimiento legal). *Efectos ex tunc, no subsanables, imprescriptibles*.
- **Actos Anulables (Art. 48)**: Cualquier otra infracción del ordenamiento jurídico (incluida la desviación de poder). *Subsanables y convalidables*.
- **Recursos Administrativos**:
  - **Alzada**: Contra actos que *no ponen fin a la vía administrativa* ante el superior jerárquico. Plazo de interposición: **1 mes** (expreso) / cualquier momento (silencio). Resolución: **3 meses**.
  - **Reposición (Potestativo)**: Contra actos que *ponen fin a la vía administrativa* ante el mismo órgano. Plazo: **1 mes**. Resolución: **1 mes**.
  - **Extraordinario de Revisión**: Por causas tasadas (error de hecho, documentos sobrevenidos, prevaricación/falsedad penal firme). Plazo: **4 años** (error de hecho) o **3 meses** (demás causas).

> [!mnemo] 🧠 Mnemotecnia de Silencio Administrativo en Alzada
> Si un recurso de alzada se interpone contra la desestimación por silencio de una solicitud, si la Administración no resuelve en 3 meses, el silencio es **POSITIVO** (doble silencio positivo), salvo excepciones materiales del art. 24.1.

---

### B. Empleo Público (TREBEP - RDL 5/2015)
- **Situaciones Administrativas**:
  - *Servicio Activo*.
  - *Servicios Especiales*: Puestos políticos, altos cargos, jueces TC/CGPJ (reserva de plaza, cómputo de trienios y carrera).
  - *Servicio en otras Administraciones Públicas*: Por transferencia o procesos de provisión.
  - *Excedencia*: Por interés particular (mínimo 2 años de servicio previo, sin reserva de puesto ni cobro), por cuidado de familiares (máx 3 años, reserva 2 años), por violencia de género o terrorismo.
  - *Suspensión de Funciones*: Firme (máx 6 años) o provisional (máx 6 meses).
- **Régimen Disciplinario**:
  - Faltas Muy Graves: Prescriben a los **3 años** (sanciones a los 3 años).
  - Faltas Graves: Prescriben a los **2 años** (sanciones a los 2 años).
  - Faltas Leves: Prescriben a los **6 meses** (sanciones al año).

---

### C. Marco Digital de la AGE (Leyes 39/2015, 40/2015, eIDAS y LOPDGDD)
- **Red SARA**: Red privada interadministrativa conectada a **sTESTA / EuroDomain**.
- **Servicios Comunes**: **SIR** (asientos registrales SICRES 3.0), **GEISER/ORVE** (aplicaciones de registro), **Cl@ve** (PIN/Permanente), **Cl@ve Firma** (HSM en la nube), **Autofirm@** (cliente local), **FACe** (factura electrónica Facturae 3.2.x), **INSIDE** (expediente electrónico NTI) y **ARCHIVE** (preservación OAIS).
- **Título X LOPDGDD**: Consentimiento redes sociales a los **14 años** (Art. 83), **Desconexión digital laboral** (Art. 88), videovigilancia laboral sin zonas íntimas (Art. 89) y **Testamento digital** (Art. 96).

---

## 🔵 3. Batería de Autoevaluación del Bloque 1
- [[wiki/tests/temas/test-bloque1-tema01-constitucion|Test Tema 01: La Constitución Española de 1978]]
- [[wiki/tests/bloques/index-tests-bloques|Simulacros Globales de Bloque 1]]
""",

    # =========================================================================
    # BLOQUE 2 MASTER SYNTHESIS
    # =========================================================================
    "wiki/synthesis/bloque2-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 2: Tecnología Básica, Hardware, Algoritmos, SO y SGBD (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-2
  - oposiciones
  - tai
  - hardware
  - sistemas-operativos
  - sgbd
  - nosql
  - algoritmos
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
  - "raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md"
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 2"
  - "Bloque 2 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 2: Tecnología Básica, Hardware, Algoritmos, SO y SGBD (TAI)

Compendio estructurado de estudio para el **Bloque 2**, cubriendo representación de datos, hardware de procesador y buses, estructuras de datos y algoritmos, gestión interna de sistemas operativos y bases de datos relacionales y NoSQL.

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 2 (5 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis |
|:---|:---|:---|:---|:---|
| **Tema 01** | Informática Básica y Representación | [[wiki/sources/bloque2-tema01|Resumen Tema 01]] | [[wiki/entities/cpu-architecture-von-neumann|Von Neumann / Harvard]], [[wiki/entities/ieee-754-floating-point|IEEE 754]] | [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet C2 y Coma Flotante]] |
| **Tema 02** | Periféricos, Puertos y Conectividad | [[wiki/sources/bloque2-tema02|Resumen Tema 02]] | [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|USB, PCIe, NVMe, Thunderbolt]] | [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet Puertos y Buses]] |
| **Tema 03** | Estructuras de Datos, Algoritmos y Ficheros | [[wiki/sources/bloque2-tema03|Resumen Tema 03]] | [[wiki/entities/data-structures-trees-and-graphs|Árboles AVL, B-Trees]], [[wiki/entities/sorting-and-searching-algorithms|Algoritmos]] | [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz Algoritmos Big-O]] |
| **Tema 04** | Sistemas Operativos: Procesos y Memoria | [[wiki/sources/bloque2-tema04|Resumen Tema 04]] | [[wiki/entities/operating-systems-architecture-and-scheduling|Planificación CPU]], [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual]] | [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet CPU / Deadlocks]], [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Paginación]] |
| **Tema 05** | SGBD Relacionales, NoSQL y Teorema CAP | [[wiki/sources/bloque2-tema05|Resumen Tema 05]] | [[wiki/entities/nosql-databases-and-cap-theorem|NoSQL y CAP]], [[wiki/entities/relational-databases-rdbms|RDBMS]] | [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía NoSQL y Teorema CAP]] |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Representación Numérica y Buses
- **Complemento a 2 ($n$ bits)**: Rango $[-2^{n-1}, +2^{n-1}-1]$. Para 8 bits: **$-128$ a $+127$**. El cero es único (`00000000`).
- **IEEE 754 Coma Flotante**:
  - Simple (32 bits): Signo (1), Exponente (8, sesgo **127**), Mantisa (23).
  - Doble (64 bits): Signo (1), Exponente (11, sesgo **1023**), Mantisa (52).
- **Puertos de E/S**:
  - **USB 2.0**: 480 Mbps | **USB 3.0 (3.1 Gen 1)**: 5 Gbps | **USB 3.1 Gen 2**: 10 Gbps | **USB4 / Thunderbolt 4**: **40 Gbps**.
  - **NVMe**: Protocolo sobre PCIe que soporta hasta **64.000 colas con 64.000 comandos** cada una en paralelo (frente a 1 cola de 32 comandos en AHCI/SATA).

---

### B. Algoritmos de Ordenación y Complejidad
| Algoritmo | Caso Medio | Peor Caso | Espacio | Estable | Estrategia |
|:---|:---:|:---:|:---:|:---:|:---|
| **Quicksort** | $O(n \log n)$ | $O(n^2)$ (pivote extremo) | $O(\log n)$ | NO | Divide y Vencerás (Partición) |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **SÍ** | Divide y Vencerás (Mezcla) |
| **Heapsort** | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | NO | Árbol Montículo |
| **Búsqueda Binaria** | $O(\log n)$ | $O(\log n)$ | $O(1)$ | - | Divide y Vencerás (requiere array ordenado) |

---

### C. Sistemas Operativos (Procesos, Memoria y Deadlocks)
- **Planificación CPU**: FCFS (efecto convoy), SJF/SRTF (óptimo en tiempo de espera), Round Robin (quantum $q$).
- **Deadlocks**: 4 condiciones de Coffman (*Exclusión mutua, Retención y espera, No apropiación, Espera circular*). Evasión: **Algoritmo del Banquero de Dijkstra**.
- **Memoria Virtual**: Páginas ($4\text{ KB}$) $\rightarrow$ Marcos de página (*Frames*). TLB (*Translation Lookaside Buffer*).
  - Reemplazo de páginas: **FIFO** (sufre la **Anomalía de Belady**), **LRU** (*Least Recently Used*), Reloj / Segunda oportunidad.

---

### D. NoSQL y Teorema CAP de Brewer
- **Teorema CAP**: Ante una partición de red ($P$), los sistemas deben elegir entre **Consistencia (CP)** o **Disponibilidad (AP)**.
- **Familias NoSQL**:
  - *Clave-Valor*: **Redis** (en memoria RAM, CP/AP).
  - *Documentales*: **MongoDB** (almacenamiento en **BSON**, CP).
  - *Columnas Anchas*: **Apache Cassandra** (alta disponibilidad, AP con modelo BASE).
  - *Grafos*: **Neo4j** (nodos y relaciones, CA).

---

## 🔵 3. Recursos de Evaluación del Bloque 2
- [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Algoritmos Big-O]]
- [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
- [[wiki/tests/bloques/index-tests-bloques|Simulacros Globales de Bloque 2]]
""",

    # =========================================================================
    # BLOQUE 3 MASTER SYNTHESIS
    # =========================================================================
    "wiki/synthesis/bloque3-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 3: Desarrollo de Sistemas, Metodologías, BBDD y Software (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-3
  - oposiciones
  - tai
  - metrica-v3
  - uml
  - patrones-diseno
  - normalizacion
  - java
  - dotnet
  - web
  - qa
  - git
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
  - "raw/sources/bloque3-tema07-front-html5-css-js.md"
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 3"
  - "Bloque 3 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 3: Desarrollo de Sistemas, Metodologías, BBDD y Software (TAI)

Compendio estructurado de estudio para el **Bloque 3**, abarcando el ciclo de vida del software, bases de datos relacionales, POO, patrones GoF, plataformas Java/.NET, arquitecturas web y testing.

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 3 (9 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis y Supuestos |
|:---|:---|:---|:---|:---|
| **Tema 01** | Modelado de Datos y Normalización | [[wiki/sources/bloque3-tema01|Resumen Tema 01]] | [[wiki/entities/relational-database-modeling-and-normalization|Modelado E/R y Formas Normales]] | [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet Normalización]], [[wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd|Supuesto Normalización]] |
| **Tema 02** | Lenguajes, Compiladores y Chomsky | [[wiki/sources/bloque3-tema02|Resumen Tema 02]] | [[wiki/entities/programming-languages-and-compilers|Compiladores y Chomsky]] | [[wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion|Supuesto Código Java/PHP]] |
| **Tema 03** | SQL ANSI, DDL, DML y Procedimientos | [[wiki/sources/bloque3-tema03|Resumen Tema 03]] | [[wiki/entities/sql-ansi-and-stored-procedures|SQL ANSI y Transacciones]] | [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet SQL]] |
| **Tema 04** | POO, Patrones GoF y Diagramas UML | [[wiki/sources/bloque3-tema04|Resumen Tema 04]] | [[wiki/entities/gof-design-patterns|Patrones GoF]], [[wiki/entities/uml-diagrams-and-modeling|UML 2.x]] | [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet Patrones GoF]] |
| **Tema 05** | Plataformas Java EE y Microsoft .NET | [[wiki/sources/bloque3-tema05|Resumen Tema 05]] | [[wiki/entities/java-platform-and-jvm|Java / JVM]], [[wiki/entities/dotnet-framework-and-clr|CLR / .NET]] | [[wiki/synthesis/java-ee-vs-dotnet-comparison-guide|Comparativa Java vs .NET]] |
| **Tema 06** | Arquitecturas Web, REST y SOAP | [[wiki/sources/bloque3-tema06|Resumen Tema 06]] | [[wiki/entities/rest-and-soap-web-services|REST y SOAP]] | [[wiki/synthesis/rest-vs-soap-comparison-guide|Comparativa REST vs SOAP]] |
| **Tema 07** | Tecnologías Front: HTML5, CSS y JS | [[wiki/sources/bloque3-tema07|Resumen Tema 07]] | [[wiki/entities/web-technologies-html5-css-javascript|HTML5, CSS3, ES6+]] | Semántica Web y DOM |
| **Tema 08** | Accesibilidad WCAG y RD 1112/2018 | [[wiki/sources/bloque3-tema08|Resumen Tema 08]] | [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018|WCAG 2.1 y RD 1112/2018]] | [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet POUR y Plazos]] |
| **Tema 09** | Metodologías, QA y Control de Versiones | [[wiki/sources/bloque3-tema09|Resumen Tema 09]] | [[wiki/entities/metrica-v3-methodology|MÉTRICA v3]], [[wiki/entities/git-version-control-system|Git]] | [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía MÉTRICA v3]], [[wiki/synthesis/software-testing-and-qa-guide|Guía Testing McCabe]] |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Normalización Relacional (1FN a 5FN y BCNF)
- **1FN**: Valores atómicos, sin grupos repetitivos.
- **2FN**: 1FN + Todo atributo no primo tiene **dependencia funcional completa** de toda la clave (elimina dependencias parciales en claves compuestas).
- **3FN**: 2FN + Ningún atributo no primo depende transitivamente de la clave ($X \rightarrow Y \rightarrow Z$).
- **BCNF (Boyce-Codd)**: Para toda dependencia funcional $X \rightarrow A$, $X$ debe ser superclave.
- **4FN**: Elimina dependencias multivaluadas independientes ($X \twoheadrightarrow Y$).
- **5FN**: Elimina dependencias de reunión (*join dependencies*).

---

### B. Patrones de Diseño GoF (Gang of Four)
- **Creacionales**: *Singleton* (instancia única), *Factory Method*, *Abstract Factory*, *Builder*, *Prototype*.
- **Estructurales**: *Adapter* (convierte interfaces), *Decorator* (añade responsabilidades dinámicamente), *Facade* (interfaz simplificada), *Composite* (estructura de árbol), *Proxy*.
- **Comportamiento**: *Observer* (suscripción 1:N), *Strategy* (familia de algoritmos intercambiables), *Command*, *Iterator*, *State*, *Template Method*.

---

### C. Metodología MÉTRICA Versión 3
- **Procesos Principales**:
  1. **PSI**: Planificación de Sistemas de Información (marco estratégico global).
  2. **EVS**: Estudio de Viabilidad del Sistema.
  3. **ASI**: Análisis del Sistema de Información (especificación de requisitos funcionales y casos de uso).
  4. **DSI**: Diseño del Sistema de Información (arquitectura técnica, modelo físico de datos).
  5. **CSI**: Construcción del Sistema de Información (codificación, pruebas unitarias y de integración).
  6. **IAS**: Implantación y Aceptación del Sistema (puesta en producción y paso a mantenimiento).
  7. **CAL / MNT**: Mantenimiento del Sistema de Información (correctivo, adaptativo, perfectivo, evolutivo).

---

### D. Testing y Métrica de Complejidad de McCabe
- **Complejidad Ciclomática**: Cantidad de caminos linealmente independientes en un grafo de control de flujo:
  $$V(G) = E - N + 2P = D + 1$$
  - $E$: Número de aristas (*Edges*).
  - $N$: Número de nodos (*Nodes*).
  - $P$: Componentes conexos (habitualmente $P=1$).
  - $D$: Número de nodos predicado (puntos de decisión condicional `if`, `while`).

---

## 🔵 3. Batería de Supuestos Prácticos de Examen (Bloque 3)
- [**Supuesto Práctico: Normalización de BBDD y SQL DDL**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md)
- [**Supuesto Práctico: Trazas de Código Java y PHP**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion.md)
- [**Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai.md)
""",

    # =========================================================================
    # BLOQUE 4 MASTER SYNTHESIS
    # =========================================================================
    "wiki/synthesis/bloque4-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 4: Sistemas, Comunicaciones, Redes y Seguridad (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-4
  - oposiciones
  - tai
  - redes
  - tcp-ip
  - windows-server
  - linux
  - virtualizacion
  - ens
  - seguridad
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema03.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema06.md"
  - "raw/sources/bloque4-tema07.md"
  - "raw/sources/bloque4-tema08.md"
  - "raw/sources/bloque4-tema09.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 4"
  - "Bloque 4 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 4: Sistemas, Comunicaciones, Redes y Seguridad (TAI)

Compendio estructurado de estudio para el **Bloque 4**, integrando modelos de red ISO/OSI y TCP/IP, subnetting IPv4/IPv6, protocolos de transporte y aplicación, administración avanzada de Windows Server y Linux, virtualización y Esquema Nacional de Seguridad (ENS).

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 4 (10 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis y Cheatsheets |
|:---|:---|:---|:---|:---|
| **Tema 01** | Conceptos de SO y Arquitectura | [[wiki/sources/bloque4-tema01|Resumen Tema 01]] | [[wiki/entities/docker-and-containers|Docker y Contenedores]] | [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa VMs vs Contenedores]] |
| **Tema 02** | Administración de Windows Server | [[wiki/sources/bloque4-tema02|Resumen Tema 02]] | [[wiki/entities/windows-server|Windows Server]], [[wiki/entities/active-directory|Active Directory]] | [[wiki/synthesis/windows-server-administration-guide|Guía Maestra Windows Server]], [[wiki/synthesis/active-directory-and-ldap-guide|LDAP / Kerberos]] |
| **Tema 03** | Administración de Sistemas Linux | [[wiki/sources/bloque4-tema03|Resumen Tema 03]] | [[wiki/entities/linux-kernel|Linux Kernel]], [[wiki/entities/bash-and-shell-scripting|Bash Scripting]] | [[wiki/synthesis/sysadmin-commands-windows-and-linux-cheatsheet|Cheatsheet Comandos Sysadmin]] |
| **Tema 04** | Redes LAN, DHCP y DNS | [[wiki/sources/bloque4-tema04|Resumen Tema 04]] | [[wiki/entities/dns-protocol|DNS]], [[wiki/entities/dhcp-protocol|DHCP]] | [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet Puertos de Red]] |
| **Tema 05** | Almacenamiento, CPD, RAID y Backup | [[wiki/sources/bloque4-tema05|Resumen Tema 05]] | [[wiki/entities/raid-storage|Sistemas RAID]] | [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía TIER, RAID y DRP]] |
| **Tema 06** | Medios de Transmisión y Cableado | [[wiki/sources/bloque4-tema06|Resumen Tema 06]] | [[wiki/entities/optical-fiber-and-gpon|Fibra Óptica y GPON]] | [[wiki/synthesis/network-cabling-and-fiber-optics-guide|Guía Cableado y Fibras]] |
| **Tema 07** | Modelo OSI, TCP/IP e IPv4/IPv6 | [[wiki/sources/bloque4-tema07|Resumen Tema 07]] | [[wiki/entities/tcp-and-udp|TCP y UDP]], [[wiki/entities/ipv4-and-ipv6|IPv4 e IPv6]] | [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa OSI vs TCP/IP]], [[wiki/synthesis/subnetting-and-ipv4-ipv6-addressing-guide|Subnetting VLSM]] |
| **Tema 08** | Internet, Protocolos Web y Correo | [[wiki/sources/bloque4-tema08|Resumen Tema 08]] | [[wiki/entities/http-protocol|Protocolo HTTP]], [[wiki/entities/smtp-imap-pop3|SMTP, IMAP, POP3]] | [[wiki/synthesis/http-status-codes-and-headers-guide|Guía Códigos HTTP]], [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Email]] |
| **Tema 09** | Seguridad, Criptografía y ENS | [[wiki/sources/bloque4-tema09|Resumen Tema 09]] | [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]], [[wiki/entities/tls-ssl-protocols|TLS / SSL]] | [[wiki/synthesis/ens-rd-311-2022-and-ccn-stic-guide|Guía Exhaustiva ENS]], [[wiki/synthesis/cryptography-algorithms-comparison|Criptografía]] |
| **Tema 10** | Topologías LAN, IEEE 802 y Switching | [[wiki/sources/bloque4-tema10|Resumen Tema 10]] | [[wiki/entities/ethernet-and-ieee-standards|Estándares IEEE Ethernet]] | CSMA/CD vs CSMA/CA, Spanning Tree (STP) |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Modelo OSI vs Pila TCP/IP y Protocolos Clave
- **OSI (7 Capas)**: *Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación*.
- **TCP/IP (4 Capas)**: *Acceso a Red, Internet, Transporte, Aplicación*.
- **Puertos Esenciales**:
  - **DNS**: 53 (UDP consultas, TCP transferencias de zona).
  - **DHCP**: 67 (Servidor), 68 (Cliente).
  - **HTTP**: 80 | **HTTPS / TLS**: 443 | **HTTP/3**: 443 (sobre protocolo **QUIC / UDP**).
  - **SSH**: 22 | **Telnet**: 23 | **FTP**: 20 (Datos) y 21 (Control).
  - **SMTP**: 25 / 587 | **IMAP**: 143 / 993 (SSL) | **POP3**: 110 / 995 (SSL).
  - **LDAP**: 389 / 636 (LDAPS) | **Kerberos**: 88.

---

### B. Subnetting IPv4 y Direccionamiento IPv6
- **Subnetting IPv4**:
  - `/24`: $256$ IPs ($254$ hosts) | Máscara `255.255.255.0`
  - `/25`: $128$ IPs ($126$ hosts) | Máscara `255.255.255.128`
  - `/26`: $64$ IPs ($62$ hosts) | Máscara `255.255.255.192`
  - `/27`: $32$ IPs ($30$ hosts) | Máscara `255.255.255.224`
  - `/28`: $16$ IPs ($14$ hosts) | Máscara `255.255.255.240`
  - `/29`: $8$ IPs ($6$ hosts) | Máscara `255.255.255.248`
  - `/30`: $4$ IPs ($2$ hosts - enlaces punto a punto) | Máscara `255.255.255.252`
- **IPv6**: 128 bits expresados en 8 grupos hexadecimales de 16 bits. Sin broadcast (sustituido por *Multicast* y *Anycast*). Autoconfiguración SLAAC mediante EUI-64 (invierte el 7º bit del OUI MAC e inserta `FF:FE`).

---

### C. Esquema Nacional de Seguridad (ENS - RD 311/2022)
- **7 Principios Básicos**: Seguridad integral, gestión de riesgos, prevención/reacción/recuperación, líneas de defensa, reevaluación periódica, función diferenciada de seguridad y vigilancia continua.
- **5 Dimensiones de Seguridad**: **Disponibilidad (D), Autenticidad (A), Integridad (I), Confidencialidad (C) y Trazabilidad (T)**.
- **3 Categorías de Seguridad**: **Básica, Media y Alta** (determinadas por el impacto mayor de las dimensiones).

---

## 🔵 3. Batería de Autoevaluación del Bloque 4
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet Completo de Puertos y Protocolos]]
- [[wiki/synthesis/subnetting-and-ipv4-ipv6-addressing-guide|Guía Práctica de Subnetting VLSM]]
- [[wiki/tests/bloques/index-tests-bloques|Simulacros Globales de Bloque 4]]
"""
}

print("[*] Escribiendo las 4 Guías Maestras de Síntesis de los Bloques 1, 2, 3 y 4 con enlaces verificados...")
for path, content in BLOQUES_SYNTHESIS.items():
    write_file(path, content)

print("[*] Generación completada exitosamente.")
