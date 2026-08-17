# -*- coding: utf-8 -*-
r"""
Script para adaptar y enriquecer toda la base de conocimiento del Bloque 3
en base a los 9 PDFs extraídos (UD012107 a UD012116).
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
# WIKI SOURCES BLOQUE 3 (9 Temas oficiales de los PDFs)
# ==============================================================================

WIKI_SOURCES_B3_ADAPTED = {
    "wiki/sources/bloque3-tema01.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo E/R y Normalización"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema01
  - modelado-datos
  - modelo-er
  - normalizacion
  - formas-normales
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Modelado de Datos y Normalización"
  - "bloque3-tema01"
---

# Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo Entidad-Relación y Normalización

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema01-modelado-datos-bbdd.md|bloque3-tema01-modelado-datos-bbdd.md]] (90 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en las fases de diseño de bases de datos (Conceptual, Lógico y Físico): el **Modelo Entidad-Relación (E/R de Peter Chen)** (entidades fuertes y débiles, atributos simples/compuestos/multivaluados/derivados, relaciones 1:1, 1:N, M:N, cardinalidades mínimas y máximas), las reglas de transformación del modelo conceptual al **Modelo Lógico Relacional de Codd** (tablas, tuplas, atributos, dominios, claves primarias PK y foráneas FK, integridad de entidad e integridad referencial), y la **Teoría de la Normalización** (Dependencias Funcionales, 1FN, 2FN, 3FN, Forma Normal de Boyce-Codd BCNF, 4FN con dependencias multivaluadas y 5FN con dependencias de unión).

---

## 🎯 Datos Clave para Oposiciones TAI

| Fase / Regla | Concepto / Fórmula de Examen |
|--------------|------------------------------|
| **Fases de Diseño BBDD** | 1. **Conceptual** (Modelo E/R) $\rightarrow$ 2. **Lógico** (Relacional) $\rightarrow$ 3. **Físico** (Tablas, índices y archivos) |
| **Primera Forma Normal (1FN)** | Todos los atributos son **atómicos** (valores indivisibles, sin grupos repetitivos) |
| **Segunda Forma Normal (2FN)** | Está en 1FN y todo atributo no clave tiene **dependencia funcional completa** de la PK (sin dependencias parciales) |
| **Tercera Forma Normal (3FN)** | Está en 2FN y **no existen dependencias transitivas** entre atributos no clave ($X \rightarrow Y \rightarrow Z$) |
| **Forma Normal de Boyce-Codd (BCNF)** | Para toda dependencia funcional $X \rightarrow Y$, $X$ es **superclave / clave candidata** |
| **Integridad Referencial** | Toda clave foránea (FK) debe coincidir con un valor de clave primaria (PK) existente o ser nula |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado de Datos Relacional y Normalización]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias Funcionales]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]
""",

    "wiki/sources/bloque3-tema02.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas y Compiladores"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema02
  - lenguajes-programacion
  - compiladores
  - interpretes
  - gramaticas
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes de Programación y Compiladores"
  - "bloque3-tema02"
---

# Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas y Compiladores

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema02-lenguajes-programacion.md|bloque3-tema02-lenguajes-programacion.md]] (114 páginas).

---

## 📖 Resumen Ejecutivo

Este tema analiza los fundamentos de los lenguajes de programación: la evolución de generaciones (1GL máquina, 2GL ensamblador, 3GL alto nivel, 4GL declarativos SQL, 5GL IA/lógica), los paradigmas de programación (imperativo, estructurado, orientado a objetos, funcional y lógico), la teoría de traductores (diferencias entre **Compiladores** e **Intérpretes**) y las fases formales del proceso de compilación: **Análisis Léxico** (tokens con autómatas finitos), **Análisis Sintáctico** (árboles de derivación con gramáticas libres de contexto), **Análisis Semántico** (comprobación de tipos con tabla de símbolos), **Generación de Código Intermedio**, **Optimización de Código** y **Generación de Código Máquina Objeto**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Fase del Compilador | Tarea Principal |
|---------------------|-----------------|
| **Análisis Léxico (Scanner)** | Lee caracteres y genera **Tokens** (elimina espacios y comentarios) |
| **Análisis Sintáctico (Parser)** | Verifica la gramática y construye el **Árbol de Sintaxis Abstracta (AST)** |
| **Análisis Semántico** | Comprueba la coherencia lógica, concordancia de tipos y tabla de símbolos |
| **Generación de Código Intermedio** | Genera código independiente de la máquina (ej. código de 3 direcciones, Bytecode) |
| **Compilador vs Intérprete** | Compilador: Traduce todo el programa a ejecutable binario \| Intérprete: Traduce y ejecuta línea a línea |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/programming-languages-and-compilers|Lenguajes de Programación, Paradigmas y Compiladores]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
""",

    "wiki/sources/bloque3-tema03.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 03 (UD012110): Lenguajes de Interrogación SQL, Stored Procedures y Triggers"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema03
  - sql
  - ddl
  - dml
  - stored-procedures
  - triggers
  - transacciones
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen SQL, Stored Procedures y Triggers"
  - "bloque3-tema03"
---

# Resumen Fuente: Bloque 3 - Tema 03 (UD012110): Lenguajes de Interrogación SQL, Stored Procedures y Triggers

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md|bloque3-tema03-sql-interrogacion-bbdd.md]] (140 páginas).

---

## 📖 Resumen Ejecutivo

Este tema aborda el estándar **ANSI SQL** para sistemas relacionales: sublenguajes **DDL** (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`), **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), **DCL** (`GRANT`, `REVOKE`) y **TCL** (`COMMIT`, `ROLLBACK`, `SAVEPOINT`), consultas avanzadas con agregación (`GROUP BY`, `HAVING`), tipos de combinaciones (**INNER JOIN**, **LEFT/RIGHT/FULL OUTER JOIN**, **CROSS JOIN**, **NATURAL JOIN**), subconsultas correlacionadas, objetos de programación en servidor: **Procedimientos Almacenados (Stored Procedures)**, **Funciones de Usuario (UDF)** y **Disparadores (Triggers `BEFORE`/`AFTER`/`INSTEAD OF`)**, y las propiedades transaccionales **ACID** y niveles de aislamiento SQL.

---

## 🎯 Datos Clave para Oposiciones TAI

| Objeto / Comando SQL | Función / Definición |
|----------------------|----------------------|
| **`WHERE` vs `HAVING`** | `WHERE`: Filtra filas antes de agrupar \| `HAVING`: Filtra grupos tras el `GROUP BY` |
| **`TRUNCATE` vs `DELETE`** | `TRUNCATE`: DDL rápido, reinicia identidad, sin WHERE \| `DELETE`: DML fila a fila con rollback |
| **Triggers (Disparadores)** | Procedimientos automáticos ejecutados ante eventos DML (`INSERT`, `UPDATE`, `DELETE`) |
| **Propiedades ACID** | **Atomicidad** (todo o nada), **Consistencia**, **Aislamiento** y **Durabilidad** |
| **Niveles de Aislamiento** | *Read Uncommitted*, *Read Committed*, *Repeatable Read*, *Serializable* |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/sql-ansi-and-stored-procedures|Estándar ANSI SQL, Procedimientos Almacenados y Triggers]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]
""",

    "wiki/sources/bloque3-tema04.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 04 (UD012111): POO, Patrones de Diseño GoF y UML"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema04
  - poo
  - solid
  - patrones-gof
  - uml
sources:
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen POO, Patrones GoF y UML"
  - "bloque3-tema04"
---

# Resumen Fuente: Bloque 3 - Tema 04 (UD012111): POO, Patrones de Diseño GoF y UML

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema04-poo-patrones-uml.md|bloque3-tema04-poo-patrones-uml.md]] (68 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el diseño orientado a objetos: los pilares de la POO (abstracción, encapsulamiento, herencia y polimorfismo con ligadura dinámica), los principios **SOLID**, el lenguaje de modelado **UML 2.x** distinguiendo diagramas estructurales (clases, objetos, componentes, despliegue, paquetes) y de comportamiento (casos de uso con `<<include>>` obligatoria y `<<extend>>` opcional, secuencia, actividades, estados), y el catálogo de **23 Patrones de Diseño GoF** clasificados en Creacionales (Singleton, Factory Method, Abstract Factory, Builder, Prototype), Estructurales (Adapter, Composite, Decorator, Facade, Proxy, Bridge, Flyweight) y de Comportamiento (Observer, Strategy, Command, Template Method, Iterator, State).

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Diagrama UML | Categoría / Definición de Examen |
|-----------------------|----------------------------------|
| **Singleton** | Creacional: Garantiza una **única instancia** con punto de acceso global |
| **Factory Method** | Creacional: Delega la instanciación de objetos en las subclases |
| **Adapter** | Estructural: **Convierte la interfaz** de una clase en otra esperada por el cliente |
| **Decorator** | Estructural: **Añade responsabilidades dinámicamente** sin modificar la clase |
| **Observer** | Comportamiento: Dependencia 1 a N donde el cambio de estado del sujeto notifica a observadores |
| **Strategy** | Comportamiento: Encapsula una familia de algoritmos haciéndolos intercambiables |
| **UML `<<include>>` vs `<<extend>>`** | `<<include>>`: Ejecución **obligatoria** \| `<<extend>>`: Ejecución **opcional / condicional** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/uml-diagrams-and-modeling|Diagramas UML 2.x y Modelado]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones de Diseño GoF (Gang of Four)]]
- Síntesis: [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones de Diseño GoF]]
""",

    "wiki/sources/bloque3-tema05.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 05 (UD012112): Componentes, Java EE / Jakarta EE y Plataforma .NET"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema05
  - componentes
  - java-ee
  - jakarta-ee
  - dotnet
  - clr
sources:
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Componentes, Java EE y .NET"
  - "bloque3-tema05"
---

# Resumen Fuente: Bloque 3 - Tema 05 (UD012112): Desarrollo Basado en Componentes, Java EE / Jakarta EE y Plataforma .NET

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema05-componentes-javaee-dotnet.md|bloque3-tema05-componentes-javaee-dotnet.md]] (132 páginas).

---

## 📖 Resumen Ejecutivo

Este tema examina el Desarrollo Basado en Componentes (CBD) y las dos grandes plataformas empresariales:
1. **Plataforma Java EE / Jakarta EE**: Arquitectura de contenedores (Web Container, EJB Container), componentes (Servlets, JSP, EJB Session Stateless/Stateful, Message-Driven Beans MDB), APIs empresariales (JPA/Hibernate, JTA transacciones, JMS mensajería, JAX-RS REST, JAX-WS SOAP) y servidores de aplicaciones (WildFly/JBoss, GlassFish, WebLogic, Tomcat/Jetty).
2. **Plataforma Microsoft .NET**: Arquitectura de ejecución **CLR (Common Language Runtime)**, código intermedio **MSIL / CIL**, compilación JIT, biblioteca de clases base (BCL), lenguajes (C#, VB.NET, F#), **ASP.NET Core**, ADO.NET y Entity Framework (ORM).

---

## 🎯 Datos Clave para Oposiciones TAI

| Plataforma / Componente | Función Técnica |
|-------------------------|-----------------|
| **EJB (Enterprise Java Beans)** | Componentes de lógica de negocio del lado servidor (Session Beans, MDB para JMS) |
| **JPA (Java Persistence API)** | Estándar de mapeo objeto-relacional (ORM) en Java |
| **CLR (Common Language Runtime)** | Motor de ejecución virtual de la plataforma .NET (equivalente a la JVM) |
| **MSIL / CIL** | Código intermedio en .NET compilado a binario por el JIT |
| **Entity Framework** | Framework ORM oficial de Microsoft para .NET |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/java-platform-and-jvm|Plataforma Java, JVM y Ecosistema Spring]]
- Entidad: [[wiki/entities/dotnet-framework-and-clr|Plataforma .NET y Entorno CLR]]
- Síntesis: [[wiki/synthesis/java-ee-vs-dotnet-comparison-guide|Guía Comparativa Java EE / Jakarta EE vs Plataforma .NET]]
""",

    "wiki/sources/bloque3-tema06.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 06 (UD012113): Arquitecturas Multicapa, Servicios SOAP y RESTful"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema06
  - arquitecturas-sistemas
  - multicapa
  - soap
  - rest
  - apis
sources:
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitecturas Multicapa y Servicios Web"
  - "bloque3-tema06"
---

# Resumen Fuente: Bloque 3 - Tema 06 (UD012113): Arquitecturas Multicapa, Servicios SOAP y RESTful

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema06-arquitecturas-servicios-web.md|bloque3-tema06-arquitecturas-servicios-web.md]] (88 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en las arquitecturas de sistemas distribuidos: modelos Cliente/Servidor (2 capas, 3 capas, N capas, cliente ligero vs cliente pesado), tecnologías de interoperabilidad y servicios web: el estándar **SOAP** (protocolo XML con Envelope, Header, Body, Fault, descriptores **WSDL**, registros **UDDI** y seguridad **WS-Security**) frente al estilo arquitectónico **REST / RESTful** (orientado a recursos, URIs, representaciones JSON, sin estado *Stateless*, métodos HTTP `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, modelo de madurez de Richardson y HATEOAS).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Criterio | SOAP | REST |
|-----------------------|------|------|
| **Formato de Carga Útil** | **Exclusivamente XML** | **JSON** (predominante), XML, texto |
| **Contrato Formal** | **WSDL** (XML) | OpenAPI / Swagger |
| **Estado de Sesión** | Puede mantener estado | Estrictamente **Sin Estado (Stateless)** |
| **Seguridad** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Verbos HTTP** | Habitualmente solo POST con payload XML | **GET, POST, PUT, PATCH, DELETE** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios Web RESTful y SOAP]]
- Concepto: [[wiki/concepts/multitier-and-microservices-architectures|Arquitecturas Multicapa y Microservicios]]
- Síntesis: [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
""",

    "wiki/sources/bloque3-tema07.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 07 (UD012114): Aplicaciones y Desarrollo Web: HTML5, DOM, CSS y JavaScript"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema07
  - desarrollo-web
  - html5
  - dom
  - css3
  - javascript
sources:
  - "raw/sources/bloque3-tema07-desarrollo-web-frontend.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Desarrollo Web Frontend"
  - "bloque3-tema07"
---

# Resumen Fuente: Bloque 3 - Tema 07 (UD012114): Aplicaciones y Desarrollo Web: HTML5, DOM, CSS y JavaScript

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema07-desarrollo-web-frontend.md|bloque3-tema07-desarrollo-web-frontend.md]] (206 páginas).

---

## 📖 Resumen Ejecutivo

Este tema abarca las tecnologías fundamentales del desarrollo web: los lenguajes de marcado y estándares web (**SGML**, **XML**, **HTML5** con elementos semánticos `header`, `nav`, `main`, `article`, `section`, `footer`, Web Storage `localStorage`/`sessionStorage`), el **DOM (Document Object Model)** y **Shadow DOM** (encapsulamiento en Web Components), hojas de estilo en cascada **CSS3** (box model, selectores, Flexbox, CSS Grid, media queries para *Responsive Web Design*), y **JavaScript** en el lado cliente (tipos, funciones, eventos, manipulación del DOM, AJAX con `fetch`/`XMLHttpRequest`, promesas y async/await), complementado con tecnologías de servidor como Servlets y JSP.

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología Web | Definición Técnica |
|----------------|--------------------|
| **HTML5 Web Storage** | `localStorage` (persistente sin caducidad) vs `sessionStorage` (válido solo durante la sesión de pestaña) |
| **DOM vs Shadow DOM** | **DOM**: Árbol jerárquico de nodos accesible globalmente \| **Shadow DOM**: Árbol DOM encapsulado y aislado |
| **CSS Flexbox vs Grid** | **Flexbox**: Diseño unidimensional (fila o columna) \| **Grid**: Diseño bidimensional (filas y columnas) |
| **AJAX** | Comunicación asíncrona cliente-servidor en segundo plano mediante `fetch()` o `XMLHttpRequest` sin recargar la página |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/web-technologies-html5-css-javascript|Tecnologías Web: HTML5, DOM, CSS3 y JavaScript]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
""",

    "wiki/sources/bloque3-tema08.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 08 (UD012115): Accesibilidad Web, Usabilidad y Seguridad en Puesto de Usuario"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema08
  - accesibilidad-web
  - wcag
  - usabilidad
  - seguridad-usuario
sources:
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Accesibilidad, Usabilidad y Seguridad"
  - "bloque3-tema08"
---

# Resumen Fuente: Bloque 3 - Tema 08 (UD012115): Accesibilidad Web, Usabilidad y Seguridad en Puesto de Usuario

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md|bloque3-tema08-accesibilidad-usabilidad-seguridad.md]] (106 páginas).

---

## 📖 Resumen Ejecutivo

Este tema integra la interacción persona-ordenador y la protección del puesto cliente: las pautas de accesibilidad **WCAG 2.1/2.2** (los 4 principios **POUR**: Perceptible, Operable, Comprensible, Robusto; niveles A, AA, AAA), la norma **EN 301 549** y el **Real Decreto 1112/2018** (nivel AA obligatorio en AAPP, Declaración de Accesibilidad y URA), los principios de **Usabilidad** (norma ISO 9241, heurísticas de Jakob Nielsen), y las medidas de **Seguridad en el Puesto de Usuario Final** (confidencialidad, integridad, disponibilidad, protección contra malware, ransomware, phishing, autenticación multifactor MFA y políticas de contraseñas).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Norma | Exigencia Técnica / Legal |
|------------------|---------------------------|
| **4 Principios WCAG (POUR)** | **Perceptible**, **Operable**, **Comprensible** y **Robusto** |
| **Nivel Exigido en AAPP** | **Nivel AA** (mediante norma europea **EN 301 549** y **RD 1112/2018**) |
| **Ratio de Contraste Nivel AA** | Mínimo **4.5:1** para texto normal y **3:1** para texto grande |
| **Obligaciones del RD 1112/2018** | **Declaración de Accesibilidad**, canal de quejas/reclamaciones y **URA** |
| **Heurísticas de Usabilidad** | Jakob Nielsen (visibilidad del estado del sistema, coherencia, prevención de errores) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018|Accesibilidad Web: WCAG, EN 301 549 y RD 1112/2018]]
- Síntesis: [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR y Accesibilidad Pública]]
""",

    "wiki/sources/bloque3-tema09.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 09 (UD012116): Repositorios, Metodologías, Pruebas y Git"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema09
  - metrica-v3
  - scrum
  - testing
  - git
  - cicd
sources:
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Metodologías, Pruebas y Git"
  - "bloque3-tema09"
---

# Resumen Fuente: Bloque 3 - Tema 09 (UD012116): Repositorios, Metodologías, Pruebas y Git

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema09-metodologias-pruebas-git.md|bloque3-tema09-metodologias-pruebas-git.md]] (124 páginas).

---

## 📖 Resumen Ejecutivo

Este tema engloba la ingeniería de desarrollo colaborativo: los modelos de ciclo de vida (**MÉTRICA v3** con sus procesos PSI, EVS, ASI, DSI, CSI, IAS y marcos ágiles **Scrum**, **Kanban** y **XP**), las técnicas y niveles de **Pruebas de Software** (Unitarias, Integración, Sistema, Aceptación, Regresión; Caja Blanca con la métrica de **Complejidad Ciclomática de McCabe** $V(G) = E - N + 2P$ y Caja Negra con particiones y valores límite), y los sistemas de control de versiones y plataformas colaborativas (**Git** con sus tres zonas, ramas, merge/rebase, GitFlow y pipelines **CI/CD** con Jenkins y SonarQube).

---

## 🎯 Datos Clave para Oposiciones TAI

| Proceso / Herramienta | Función / Fórmula |
|-----------------------|-------------------|
| **Métrica v3 Procesos** | **PSI**, **EVS**, **ASI**, **DSI**, **CSI**, **IAS** |
| **Complejidad de McCabe** | **$V(G) = E - N + 2P = \text{Nodos Predicado} + 1$** |
| **Zonas de Git** | **Working Directory** $\rightarrow$ `git add` $\rightarrow$ **Staging Area (Index)** $\rightarrow$ `git commit` $\rightarrow$ **Local Repo** |
| **`git rebase` vs `merge`** | `rebase`: Historial lineal sin commit de merge \| `merge`: Conserva historial con commit de unión |
| **SonarQube** | Análisis estático de código para calidad, cobertura, olores de código y *Quality Gates* |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/metrica-v3-methodology|Metodología MÉTRICA Versión 3]]
- Entidad: [[wiki/entities/git-version-control-system|Sistema de Control de Versiones Git]]
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Pruebas de Caja Blanca, Caja Negra y McCabe]]
- Síntesis: [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía de Procesos y Artefactos de MÉTRICA v3]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software y QA]]
"""
}

print("[*] Escribiendo 9 notas fuente de Bloque 3 adaptadas...")
for path, content in WIKI_SOURCES_B3_ADAPTED.items():
    write_file(path, content)

# ==============================================================================
# ENTIDADES NUEVAS/ADAPTADAS DEL BLOQUE 3 (10 Entidades)
# ==============================================================================

BLOQUE3_ENTITIES_ADAPTED = {
    "wiki/entities/relational-database-modeling-and-normalization.md": """---
title: "Modelado de Datos Relacional, Modelo E/R y Formas Normales"
type: "entity"
tags:
  - modelado-datos
  - bases-datos
  - modelo-er
  - normalizacion
  - sql
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelado Relacional"
  - "Modelo Entidad-Relación"
  - "Normalización"
---

# Modelado de Datos Relacional, Modelo E/R y Formas Normales

Metodología de diseño conceptual, lógico y físico de bases de datos relacionales basada en el modelo Entidad-Relación de Chen y las reglas de normalización de Codd.

---

## 🏛️ Fases de Diseño y Formas Normales

1. **1FN (Primera Forma Normal)**: Todos los valores de los atributos son **atómicos** e indivisibles (sin campos multivaluados ni arrays).
2. **2FN (Segunda Forma Normal)**: Cumple 1FN y todos los atributos no clave dependen funcionalmente de **toda la clave primaria** (sin dependencias parciales de partes de una PK compuesta).
3. **3FN (Tercera Forma Normal)**: Cumple 2FN y **no existen dependencias funcionales transitivas** entre atributos no clave ($X \rightarrow Y \rightarrow Z$).
4. **BCNF (Forma Normal de Boyce-Codd)**: Para cada dependencia funcional $X \rightarrow Y$, $X$ debe ser **superclave / clave candidata**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
""",

    "wiki/entities/programming-languages-and-compilers.md": """---
title: "Lenguajes de Programación, Paradigmas y Compiladores"
type: "entity"
tags:
  - lenguajes-programacion
  - compiladores
  - interpretes
  - gramaticas
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Lenguajes de Programación"
  - "Compiladores e Intérpretes"
---

# Lenguajes de Programación, Paradigmas y Compiladores

Fundamentos teóricos de los lenguajes informáticos, paradigmas de desarrollo y fases del proceso de traducción de código fuente a código máquina.

---

## 🏛️ Fases de la Compilación

```
Código Fuente ──> [ Análisis Léxico (Tokens) ]
                        │
                  [ Análisis Sintáctico (AST) ]
                        │
                  [ Análisis Semántico (Tipos) ]
                        │
                  [ Código Intermedio ]
                        │
                  [ Optimización de Código ]
                        │
                        ▼
                  Código Máquina Objeto (.exe / .o)
```

- **Compilador vs Intérprete**: Compilador traduce el código completo a binario independiente antes de la ejecución; el Intérprete traduce y ejecuta instrucción a instrucción en tiempo real.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
""",

    "wiki/entities/sql-ansi-and-stored-procedures.md": """---
title: "Estándar ANSI SQL, Procedimientos Almacenados y Triggers"
type: "entity"
tags:
  - sql
  - ddl
  - dml
  - stored-procedures
  - triggers
  - transacciones
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ANSI SQL"
  - "Stored Procedures y Triggers"
  - "Lenguaje SQL"
---

# Estándar ANSI SQL, Procedimientos Almacenados y Triggers

Lenguaje estándar para la definición, manipulación y control de datos en Sistemas Gestores de Bases de Datos Relacionales (RDBMS).

---

## 🏛️ Sublenguajes y Objetos de Base de Datos

- **DDL (Data Definition Language)**: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
- **DML (Data Manipulation Language)**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL (Data Control Language)**: `GRANT`, `REVOKE`.
- **TCL (Transaction Control Language)**: `COMMIT`, `ROLLBACK`, `SAVEPOINT`.
- **Objetos Programables**:
  - **Stored Procedures**: Procedimientos compilados y guardados en el motor de BD.
  - **Triggers**: Disparadores automáticos ante eventos `INSERT`, `UPDATE` o `DELETE` (`BEFORE`, `AFTER`, `INSTEAD OF`).
  - **Vistas (Views)**: Tablas virtuales basadas en consultas predefinidas.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
""",

    "wiki/entities/dotnet-framework-and-clr.md": """---
title: "Plataforma Microsoft .NET y Entorno de Ejecución CLR"
type: "entity"
tags:
  - dotnet
  - clr
  - csharp
  - aspnet
  - msil
sources:
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - ".NET"
  - "Plataforma .NET"
  - "CLR"
---

# Plataforma Microsoft .NET y Entorno de Ejecución CLR

Marco de desarrollo empresarial de Microsoft basado en el motor de ejecución virtual **Common Language Runtime (CLR)** y el lenguaje intermedio **MSIL / CIL**.

---

## 🏛️ Arquitectura de la Plataforma .NET

- **CLR (Common Language Runtime)**: Motor de ejecución que gestiona la memoria (Garbage Collection), hilos de ejecución y seguridad de tipos (equivalente a la JVM en Java).
- **CIL / MSIL (Common Intermediate Language)**: Código intermedio independiente del hardware generado por los compiladores de C#, VB.NET o F#.
- **JIT Compiler**: Compila el código MSIL a código binario nativo en tiempo de ejecución.
- **ASP.NET Core**: Framework modular de alto rendimiento para desarrollo de aplicaciones web y APIs REST multiplataforma.
- **Entity Framework Core**: Framework ORM para mapeo objeto-relacional en .NET.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Entidad: [[wiki/entities/java-platform-and-jvm|Java y JVM]]
- Síntesis: [[wiki/synthesis/java-ee-vs-dotnet-comparison-guide|Guía Comparativa Java EE vs .NET]]
""",

    "wiki/entities/web-technologies-html5-css-javascript.md": """---
title: "Tecnologías Web Frontend: HTML5, DOM, CSS3 y JavaScript"
type: "entity"
tags:
  - frontend
  - html5
  - dom
  - css3
  - javascript
sources:
  - "raw/sources/bloque3-tema07-desarrollo-web-frontend.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "HTML5, CSS y JavaScript"
  - "Desarrollo Web Frontend"
---

# Tecnologías Web Frontend: HTML5, DOM, CSS3 y JavaScript

Estándares del W3C y ECMA para el desarrollo de interfaces interactivas y aplicaciones enriquecidas en el navegador web.

---

## 🏛️ Componentes Fundamentales

- **HTML5**: Estructura semántica (`header`, `nav`, `main`, `footer`), Web Storage (`localStorage` vs `sessionStorage`), soporte multimedia nativo.
- **DOM y Shadow DOM**: Modelo de objetos del documento estructurado en árbol; Shadow DOM permite el aislamiento y encapsulamiento de estilos en Web Components.
- **CSS3**: Maquetación con **Flexbox** (unidimensional) y **CSS Grid** (bidimensional), media queries para *Responsive Web Design*.
- **JavaScript (ES6+)**: Lenguaje interpretado orientado a eventos, promesas, `async/await`, AJAX (`fetch()`).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema07|Resumen Bloque 3 - Tema 07]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
"""
}

print("[*] Escribiendo entidades adaptadas del Bloque 3...")
for path, content in BLOQUE3_ENTITIES_ADAPTED.items():
    write_file(path, content)

# ==============================================================================
# CONCEPTOS ADICIONALES DEL BLOQUE 3 (2 Conceptos)
# ==============================================================================

BLOQUE3_CONCEPTS_ADAPTED = {
    "wiki/concepts/normalization-and-normal-forms.md": """---
title: "Formas Normales, Dependencias Funcionales y Descomposición Relacional"
type: "concept"
tags:
  - normalizacion
  - formas-normales
  - dependencias-funcionales
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Formas Normales"
  - "Teoría de la Normalización"
---

# Formas Normales, Dependencias Funcionales y Descomposición Relacional

El proceso de normalización organiza los atributos y relaciones de una base de datos relacional para **evitar la redundancia de datos, anomalías de inserción/borrado/modificación y garantizar la integridad referencial**.

---

## 🏛️ Jerarquía de Formas Normales

$$\text{1FN} \subset \text{2FN} \subset \text{3FN} \subset \text{BCNF} \subset \text{4FN} \subset \text{5FN}$$

- **1FN**: Atributos con valores atómicos indivisibles.
- **2FN**: 1FN + sin dependencias parciales de claves primarias compuestas.
- **3FN**: 2FN + sin dependencias transitivas entre atributos no clave.
- **BCNF**: Todo determinante en una dependencia funcional es clave candidata.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado Relacional]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
"""
}

print("[*] Escribiendo conceptos adaptados del Bloque 3...")
for path, content in BLOQUE3_CONCEPTS_ADAPTED.items():
    write_file(path, content)

# ==============================================================================
# SÍNTESIS ADICIONALES DEL BLOQUE 3 (2 Síntesis)
# ==============================================================================

BLOQUE3_SYNTHESES_ADAPTED = {
    "wiki/synthesis/database-normalization-and-sql-cheatsheet.md": """---
title: "Cheatsheet de Normalización de Bases de Datos y Estándar ANSI SQL"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - normalizacion
  - sql
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet SQL y Normalización"
  - "Normalización y SQL Guía"
---

# Cheatsheet de Normalización de Bases de Datos y Estándar ANSI SQL

Tabla de referencia rápida sobre reglas de normalización y comandos SQL para exámenes TAI.

---

## 📋 1. Reglas de Normalización

| Forma Normal | Requisito Principal | Error que Elimina |
|--------------|---------------------|-------------------|
| **1FN** | Atributos **atómicos**, sin grupos repetitivos | Tablas anidadas y listas en campos |
| **2FN** | 1FN + **Dependencia funcional completa** de la PK | Redundancia por atributos que dependen de parte de una PK compuesta |
| **3FN** | 2FN + **Sin dependencias transitivas** ($X \rightarrow Y \rightarrow Z$) | Redundancia por dependencias entre campos no clave |
| **BCNF** | Para todo $X \rightarrow Y$, $X$ es **superclave** | Dependencias anómalas en tablas con múltiples claves candidatas compuestas solapadas |

---

## 💻 2. Tabla de Tipos de JOINs en SQL

- **INNER JOIN**: Devuelve solo las filas que tienen coincidencia en ambas tablas.
- **LEFT OUTER JOIN**: Devuelve todas las filas de la tabla izquierda y las coincidentes de la derecha (NULL si no hay coincidencia).
- **RIGHT OUTER JOIN**: Devuelve todas las filas de la tabla derecha y las coincidentes de la izquierda.
- **FULL OUTER JOIN**: Devuelve todas las filas cuando hay coincidencia en cualquiera de las dos tablas.
- **CROSS JOIN**: Producto cartesiano de ambas tablas ($N \times M$ filas).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Entidad: [[wiki/entities/sql-ansi-and-stored-procedures|ANSI SQL]]
""",

    "wiki/synthesis/java-ee-vs-dotnet-comparison-guide.md": """---
title: "Guía Comparativa: Plataforma Java EE / Jakarta EE vs Plataforma .NET"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - java-ee
  - jakarta-ee
  - dotnet
  - clr
  - jvm
sources:
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Java EE vs .NET"
  - "Java vs .NET Guía"
---

# Guía Comparativa: Plataforma Java EE / Jakarta EE vs Plataforma .NET

Contraste arquitectónico entre los dos mayores ecosistemas de desarrollo empresarial de software.

---

## 🏛️ Matriz Técnica Comparativa

| Criterio | Java EE / Jakarta EE | Plataforma .NET |
|----------|----------------------|-----------------|
| **Empresa / Origen** | Sun Microsystems / Oracle / Eclipse Foundation | Microsoft |
| **Máquina Virtual** | **JVM (Java Virtual Machine)** | **CLR (Common Language Runtime)** |
| **Código Intermedio** | **Bytecode** (`.class`) | **MSIL / CIL** (Common Intermediate Language) |
| **Lenguaje Principal** | Java | C# (también F#, VB.NET) |
| **Componentes Web** | Servlets, JSP, JSF | ASP.NET Core MVC / Razor |
| **Componentes de Negocio** | **EJB (Enterprise Java Beans)** | Clases / Servicios .NET con DI |
| **ORM Estándar** | **JPA (Hibernate, EclipseLink)** | **Entity Framework Core** |
| **Mensajería Asíncrona** | **JMS (Java Message Service)** | Azure Service Bus / RabbitMQ .NET |
| **Servidores / Hosts** | Tomcat, WildFly, GlassFish, WebLogic | Kestrel, IIS |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Entidad: [[wiki/entities/java-platform-and-jvm|Plataforma Java]]
- Entidad: [[wiki/entities/dotnet-framework-and-clr|Plataforma .NET]]
"""
}

print("[*] Escribiendo síntesis adicionales del Bloque 3...")
for path, content in BLOQUE3_SYNTHESES_ADAPTED.items():
    write_file(path, content)

print("[*] Adaptación completa del Bloque 3 finalizada.")
