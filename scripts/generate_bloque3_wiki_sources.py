# -*- coding: utf-8 -*-
r"""
Script generador de las notas fuente estructuradas para wiki/sources/ del Bloque 3 (TAI).
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

WIKI_SOURCES_B3 = {
    "wiki/sources/bloque3-tema01.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 01: Ciclo de Vida del Software, Metodologías Ágiles y MÉTRICA Versión 3"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema01
  - ciclo-de-vida
  - metrica-v3
  - scrum
  - kanban
  - xp
sources:
  - "raw/sources/bloque3-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Ciclo de Vida y Métrica v3"
  - "bloque3-tema01"
---

# Resumen Fuente: Bloque 3 - Tema 01: Ciclo de Vida del Software, Metodologías Ágiles y MÉTRICA Versión 3

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema01.md|bloque3-tema01.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la ingeniería de procesos del software: los modelos clásicos de ciclo de vida (Cascada, Modelo en V con su simetría desarrollo-pruebas, Prototipado y Espiral de Boehm con análisis de riesgos), el marco de metodologías ágiles (**Scrum** con roles PO/SM/Devs, eventos Sprint/Daily/Review/Retro y artefactos Backlog/Incremento; **Kanban** con límites WIP; y **XP** con TDD y *Pair Programming*), y la metodología oficial de las AAPP españolas: **MÉTRICA Versión 3 (MÉTRICA v3)** con sus procesos estructurados y orientados a objetos (**PSI**, **EVS**, **ASI**, **DSI**, **CSI**, **IAS**) e interfaces de soporte (Gestión de Proyectos, Seguridad, Calidad y Configuración).

---

## 🎯 Datos Clave para Oposiciones TAI

| Metodología / Proceso | Función / Especificación de Examen |
|-----------------------|------------------------------------|
| **Modelo en Espiral (Boehm)** | Ciclo iterativo guiado por el **análisis y gestión de riesgos** |
| **Scrum Roles** | **Product Owner (PO)** (negocio/backlog), **Scrum Master (SM)** (facilitador) y **Developers** |
| **Métrica v3 - PSI** | **Planificación de Sistemas de Información** (marco estratégico global) |
| **Métrica v3 - EVS** | **Estudio de Viabilidad del Sistema** (alternativas técnica, económica y legal) |
| **Métrica v3 - ASI** | **Análisis del Sistema de Información** (requisitos lógicos y casos de uso) |
| **Métrica v3 - DSI** | **Diseño del Sistema de Información** (arquitectura física, BD, interfaces y plan de pruebas) |
| **Métrica v3 - CSI** | **Construcción del Sistema de Información** (codificación, pruebas unitarias e integración) |
| **Métrica v3 - IAS** | **Implantación y Aceptación del Sistema** (puesta en producción y aceptación final) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/metrica-v3-methodology|Metodología MÉTRICA Versión 3]]
- Entidad: [[wiki/entities/scrum-and-agile-frameworks|Metodologías Ágiles: Scrum, Kanban y XP]]
- Concepto: [[wiki/concepts/software-lifecycle-models|Modelos del Ciclo de Vida del Software]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
- Síntesis: [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía de Procesos y Artefactos de MÉTRICA v3]]
""",

    "wiki/sources/bloque3-tema02.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 02: Análisis y Diseño OO, UML 2.x y Patrones de Diseño GoF"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema02
  - uml
  - patrones-diseno
  - gof
  - solid
  - poo
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen UML y Patrones GoF"
  - "bloque3-tema02"
---

# Resumen Fuente: Bloque 3 - Tema 02: Análisis y Diseño OO, UML 2.x y Patrones de Diseño GoF

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema02.md|bloque3-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el diseño orientado a objetos: los pilares de la POO (abstracción, encapsulamiento, herencia y polimorfismo con ligadura dinámica) y los **principios SOLID**, el estándar de modelado **UML 2.x** con su doble división entre diagramas estructurales (clases con relaciones de asociación, agregación $\diamondsuit$, composición $\blacklozenge$, generalización $\vartriangle$; componentes, despliegue, paquetes) y diagramas de comportamiento (casos de uso con `<<include>>` y `<<extend>>`, secuencia con líneas de vida, actividades, máquinas de estados), y el catálogo completo de los 23 patrones de diseño **Gang of Four (GoF)** clasificados en Creacionales, Estructurales y de Comportamiento.

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Diagrama UML | Categoría / Definición de Examen |
|-----------------------|----------------------------------|
| **Singleton** | Creacional: Garantiza una **única instancia** con punto de acceso global |
| **Factory Method / Abstract Factory** | Creacional: Creación de objetos o familias de objetos mediante interfaces polimórficas |
| **Adapter** | Estructural: **Convierte la interfaz** de una clase en otra esperada por el cliente |
| **Composite** | Estructural: Jerarquías parte-todo (árboles) tratando a hojas y compuestos uniformemente |
| **Decorator** | Estructural: Añade responsabilidades dinámicamente sin modificar la clase original |
| **Facade** | Estructural: Interfaz simplificada y de alto nivel a un subsistema complejo |
| **Observer** | Comportamiento: Dependencia 1 a N donde el cambio de estado del sujeto notifica a observadores |
| **Strategy** | Comportamiento: Encapsula una familia de algoritmos haciéndolos intercambiables en ejecución |
| **UML `<<include>>` vs `<<extend>>`** | `<<include>>`: Ejecución **obligatoria** \| `<<extend>>`: Ejecución **opcional / condicional** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/uml-diagrams-and-modeling|Diagramas UML 2.x y Modelado]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones de Diseño GoF (Gang of Four)]]
- Síntesis: [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones de Diseño GoF]]
""",

    "wiki/sources/bloque3-tema03.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 03: Lenguajes, Plataforma Java/JVM y Git"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema03
  - java
  - jvm
  - git
  - control-versiones
  - spring
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes, Java y Git"
  - "bloque3-tema03"
---

# Resumen Fuente: Bloque 3 - Tema 03: Lenguajes, Plataforma Java/JVM y Git

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema03.md|bloque3-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza los lenguajes de programación y herramientas de desarrollo: los paradigmas (imperativo, POO, funcional y declarativo), la arquitectura de la **Plataforma Java / JVM** (*WORA*, Bytecode `.class`, compilador JIT, gestión de memoria Stack vs Heap con Young/Old Generation y Metaspace, y recolector de basura Garbage Collector), el ecosistema empresarial con **Spring Boot** (Inversión de Control e Inyección de Dependencias) y JPA/Hibernate, y el sistema de control de versiones distribuido **Git** (las tres zonas: Working Tree, Staging Area y Repositorio Local; comandos esenciales, diferencias entre `git merge` y `git rebase`, y el modelo de ramas GitFlow).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Comando | Especificación Técnica |
|--------------------|------------------------|
| **Java Bytecode** | Código intermedio ejecutable por la **JVM** (`.class` generado por `javac`) |
| **Java Heap vs Stack** | **Heap**: Objetos e instancias gestionados por GC \| **Stack**: Variables locales y llamadas |
| **Spring IoC / DI** | Inversión de Control delegando la creación y enlace de objetos al contenedor Spring |
| **Git: Staging Area (Index)** | Zona intermedia donde se preparan los cambios con `git add` antes del commit |
| **`git rebase` vs `git merge`** | `rebase`: Reescribe la base creando un historial lineal \| `merge`: Crea un commit de unión |
| **`git cherry-pick`** | Aplica un commit específico de otra rama sobre la rama actual |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/java-platform-and-jvm|Plataforma Java, JVM y Ecosistema Spring]]
- Entidad: [[wiki/entities/git-version-control-system|Sistema de Control de Versiones Git]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
""",

    "wiki/sources/bloque3-tema04.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 04: Arquitecturas Web, Servicios SOAP, RESTful y Microservicios"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema04
  - arquitecturas-web
  - rest
  - soap
  - microservicios
  - apis
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitecturas Web, REST y SOAP"
  - "bloque3-tema04"
---

# Resumen Fuente: Bloque 3 - Tema 04: Arquitecturas Web, Servicios SOAP, RESTful y Microservicios

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema04.md|bloque3-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema examina las arquitecturas distribuidas modernas: el modelo multicapa (*N-Tier*: Presentación, Lógica de Negocio y Persistencia), la comparativa técnica entre servicios web **SOAP** (basado en XML, con Envelope/Header/Body/Fault, descriptores WSDL, UDDI y seguridad WS-Security) y servicios **REST / RESTful** (basado en HTTP, sin estado *Stateless*, con recursos identificados por URIs, representaciones JSON, verbos GET/POST/PUT/PATCH/DELETE y madurez Richardson/HATEOAS), y las arquitecturas de **microservicios** con patrones API Gateway, Service Discovery, Circuit Breaker y mensajería asíncrona con brokers como RabbitMQ y Apache Kafka.

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Criterio | SOAP | REST |
|-----------------------|------|------|
| **Naturaleza** | Protocolo formal W3C | Estilo arquitectónico (Roy Fielding) |
| **Formato de Mensaje** | **Exclusivamente XML** | **JSON** (predominante), XML, texto |
| **Descripción de Servicio** | **WSDL** (Web Services Description Language) | OpenAPI / Swagger |
| **Estado de Sesión** | Puede mantener estado | Estrictamente **Sin Estado (Stateless)** |
| **Seguridad Estándar** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Verbos HTTP** | Habitualmente solo POST con payload XML | **GET, POST, PUT, PATCH, DELETE** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios Web RESTful y SOAP]]
- Concepto: [[wiki/concepts/multitier-and-microservices-architectures|Arquitecturas Multicapa y Microservicios]]
- Síntesis: [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
""",

    "wiki/sources/bloque3-tema05.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema05
  - pruebas-software
  - caja-blanca
  - caja-negra
  - mccabe
  - cicd
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Calidad, Pruebas y CI/CD"
  - "bloque3-tema05"
---

# Resumen Fuente: Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema05.md|bloque3-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el aseguramiento de la calidad del software: la jerarquía de niveles de pruebas (Unitarias, Integración, Sistema, Aceptación Alpha/Beta y Regresión), las técnicas de diseño de casos de prueba de **Caja Blanca** (coberturas y la métrica de **Complejidad Ciclomática de McCabe** $V(G) = E - N + 2P$ para caminos básicos independientes) frente a **Caja Negra** (particiones de equivalencia y análisis de valores límite), y los pipelines de integración y despliegue continuo (**CI/CD** con Jenkins, GitLab CI, GitHub Actions) integrados con análisis estático de código mediante **SonarQube** para evaluar deuda técnica y *Quality Gates*.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Métrica | Fórmula / Definición de Examen |
|--------------------|--------------------------------|
| **Complejidad Ciclomática ($V(G)$)** | **$V(G) = E - N + 2P$** ($E$ aristas, $N$ nodos, $P$ componentes conexos) |
| **Fórmula Alternativa McCabe** | **$V(G) = \text{Nodos Predicado} + 1$** |
| **Pruebas de Caja Blanca** | Analizan la **estructura interna y código fuente** (sentencias, ramas, caminos) |
| **Pruebas de Caja Negra** | Basadas en **especificación externa** (clases de equivalencia, valores límite) |
| **Pruebas de Regresión** | Verifican que los cambios nuevos no hayan roto funcionalidades previas |
| **CI vs CD** | **CI**: Integración y tests automáticos \| **CD**: Despliegue automático a producción |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Pruebas de Caja Blanca, Caja Negra y Métrica de McCabe]]
- Concepto: [[wiki/concepts/ci-cd-pipelines-and-devops|Pipelines CI/CD, DevOps y Calidad de Código]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software y QA]]
""",

    "wiki/sources/bloque3-tema06.md": """---
title: "Resumen Fuente: Bloque 3 - Tema 06: Accesibilidad Web, WCAG 2.1/2.2, EN 301 549 y RD 1112/2018"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema06
  - accesibilidad-web
  - wcag
  - pour
  - rd-1112-2018
  - en-301-549
sources:
  - "raw/sources/bloque3-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Accesibilidad Web y WCAG"
  - "bloque3-tema06"
---

# Resumen Fuente: Bloque 3 - Tema 06: Accesibilidad Web, WCAG 2.1/2.2, EN 301 549 y RD 1112/2018

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema06.md|bloque3-tema06.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la accesibilidad y usabilidad web en el sector público: las pautas internacionales **WCAG 2.1 / 2.2** del W3C/WAI estructuradas en los **4 Principios POUR** (**Perceptible**, **Operable**, **Comprensible** y **Robusto**) con sus niveles de conformidad **A**, **AA** y **AAA**, la norma europea **EN 301 549** de compras públicas TIC, y la transposición obligatoria en España mediante el **Real Decreto 1112/2018**, que impone el cumplimiento del **Nivel AA** a todos los sitios web y aplicaciones móviles de las Administraciones Públicas, junto a la obligación de publicar una Declaración de Accesibilidad y designar una Unidad Responsable de Accesibilidad (URA).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento / Norma | Exigencia Legal / Técnica |
|------------------|---------------------------|
| **4 Principios WCAG (POUR)** | **Perceptible**, **Operable**, **Comprensible** y **Robusto** |
| **Nivel Exigido en AAPP** | **Nivel AA** (mediante norma europea **EN 301 549**) |
| **Ratio de Contraste Nivel AA** | Mínimo **4.5:1** para texto normal y **3:1** para texto grande |
| **Norma Nacional de Accesibilidad** | **Real Decreto 1112/2018**, de 7 de septiembre |
| **Obligaciones del RD 1112/2018** | **Declaración de Accesibilidad**, mecanismo de comunicación/quejas y **URA** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018|Accesibilidad Web: WCAG, EN 301 549 y RD 1112/2018]]
- Síntesis: [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR y Accesibilidad Pública]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
"""
}

print("[*] Escribiendo 6 notas fuente de Desarrollo de Sistemas en wiki/sources/bloque3-tema*.md...")
for path, content in WIKI_SOURCES_B3.items():
    write_file(path, content)

print("[*] 6 fuentes de wiki del Bloque 3 generadas exitosamente.")
