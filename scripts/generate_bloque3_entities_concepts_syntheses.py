# -*- coding: utf-8 -*-
r"""
Script generador de Entidades, Conceptos y Síntesis del Bloque 3 (Desarrollo de Sistemas) para TAI.
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
# ENTIDADES BLOQUE 3 (8 Entidades)
# ==============================================================================

BLOQUE3_ENTITIES = {
    "wiki/entities/metrica-v3-methodology.md": """---
title: "Metodología MÉTRICA Versión 3 (MÉTRICA v3)"
type: "entity"
tags:
  - metrica-v3
  - ingenieria-software
  - administracion-publica
  - metodologias
sources:
  - "raw/sources/bloque3-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "MÉTRICA v3"
  - "Métrica Versión 3"
  - "Metodología Métrica"
---

# Metodología MÉTRICA Versión 3 (MÉTRICA v3)

**MÉTRICA Versión 3** es la metodología de referencia oficial para la planificación, desarrollo y mantenimiento de sistemas de información en las Administraciones Públicas españolas (Ministerio de Administraciones Públicas / Ministerio de Transformación Digital y Función Pública).

---

## 🏛️ Procesos Principales de MÉTRICA v3

```
                              Estructura de Procesos MÉTRICA v3
                                              │
      ┌───────────────────────────────────────┴───────────────────────────────────────┐
      ▼                                                                               ▼
Proceso de Planificación                                                     Procesos de Desarrollo
        │                                                                               │
     [ PSI ] Planificación SI                                     ┌─────────────────────┼─────────────────────┐
                                                                  ▼                     ▼                     ▼
                                                               [ EVS ]               [ DSI ]               [ IAS ]
                                                              Estudio de            Diseño SI            Implantación
                                                              Viabilidad                │                y Aceptación
                                                                  │                  [ CSI ]                  ▲
                                                                  ▼                Construcción               │
                                                               [ ASI ] ────────────── SI ─────────────────────┘
                                                              Análisis SI
```

---

## 🎯 Datos Clave para Oposiciones TAI

| Proceso | Denominación Completa | Producto Principal Entregable |
|---------|-----------------------|------------------------------|
| **PSI** | Planificación de Sistemas de Información | Plan de Proyectos y Arquitectura de Información |
| **EVS** | Estudio de Viabilidad del Sistema | Propuesta de Solución y Estudio de Alternativas |
| **ASI** | Análisis del Sistema de Información | Catálogo de Requisitos y Modelo Lógico de Datos/Procesos o Clases |
| **DSI** | Diseño del Sistema de Información | Arquitectura Física, Esquema de BD y Plan de Pruebas |
| **CSI** | Construcción del Sistema de Información | Código fuente ejecutable, componentes y manuales |
| **IAS** | Implantación y Aceptación del Sistema | Sistema en producción y Acta de Aceptación |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Síntesis: [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía de Procesos y Artefactos de MÉTRICA v3]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
""",

    "wiki/entities/scrum-and-agile-frameworks.md": """---
title: "Metodologías Ágiles: Scrum, Kanban y eXtreme Programming (XP)"
type: "entity"
tags:
  - agile
  - scrum
  - kanban
  - xp
  - metodologias
sources:
  - "raw/sources/bloque3-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Scrum"
  - "Metodologías Ágiles"
  - "Kanban"
---

# Metodologías Ágiles: Scrum, Kanban y eXtreme Programming (XP)

Marcos de trabajo iterativos e incrementales fundamentados en el **Manifiesto Ágil (2001)** para la entrega continua de valor.

---

## 🏛️ Componentes del Marco Scrum

- **Roles Scrum**:
  - **Product Owner (PO)**: Maximiza el valor del producto y gestiona el *Product Backlog*.
  - **Scrum Master (SM)**: Líder que promueve Scrum y elimina obstáculos del equipo.
  - **Developers**: Profesionales que crean el incremento utilizable en cada Sprint.
- **Eventos Scrum**: Sprint (1-4 semanas), Sprint Planning, Daily Scrum (15 min), Sprint Review y Sprint Retrospective.
- **Artefactos Scrum**: Product Backlog, Sprint Backlog e Incremento (conforme a la *Definition of Done* - DoD).

---

## 🎯 Datos Clave para Oposiciones TAI

| Metodología | Característica Distintiva |
|-------------|---------------------------|
| **Scrum** | Timeboxing estricto (Sprints), 3 roles, 5 eventos y 3 artefactos |
| **Kanban** | Flujo continuo visual, limitación del **WIP (Work In Progress)** |
| **XP (eXtreme Programming)** | **TDD**, *Pair Programming*, refactorización y propiedad colectiva |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Concepto: [[wiki/concepts/software-lifecycle-models|Modelos de Ciclo de Vida]]
""",

    "wiki/entities/uml-diagrams-and-modeling.md": """---
title: "Diagramas UML 2.x y Lenguaje de Modelado"
type: "entity"
tags:
  - uml
  - modelado
  - poo
  - diagramas
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "UML"
  - "Diagramas UML"
---

# Diagramas UML 2.x y Lenguaje de Modelado

Estándar de la OMG (Object Management Group) para la especificación, visualización y documentación de artefactos de software orientado a objetos.

---

## 🏛️ Clasificación de Diagramas en UML 2.x

1. **Diagramas Estructurales (Estáticos)**:
   - **Diagrama de Clases**: Clases, interfaces, relaciones de asociación, agregación ($\diamondsuit$), composición ($\blacklozenge$) y generalización/herencia ($\vartriangle$).
   - **Diagrama de Componentes**: Módulos ejecutables y dependencias.
   - **Diagrama de Despliegue**: Asignación de artefactos de software sobre nodos físicos de hardware.
   - **Diagrama de Objetos**, **Paquetes** y **Estructura Compuesta**.
2. **Diagramas de Comportamiento (Dinámicos)**:
   - **Diagrama de Casos de Uso**: Actores y casos de uso con relaciones `<<include>>` (obligatoria) y `<<extend>>` (opcional con condición).
   - **Diagrama de Secuencia**: Interacción temporal entre objetos mediante líneas de vida.
   - **Diagrama de Actividades**: Flujos de trabajo con bifurcaciones y barras *fork/join*.
   - **Diagrama de Máquina de Estados**: Estados y transiciones disparadas por eventos.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones GoF]]
""",

    "wiki/entities/gof-design-patterns.md": """---
title: "Patrones de Diseño GoF (Gang of Four)"
type: "entity"
tags:
  - patrones-diseno
  - gof
  - poo
  - arquitectura-software
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Patrones GoF"
  - "Design Patterns"
---

# Patrones de Diseño GoF (Gang of Four)

Catálogo de 23 patrones de diseño clásicos de Gamma, Helm, Johnson y Vlissides (1994) para resolver problemas recurrentes de arquitectura de software.

---

## 🏛️ Clasificación de los 23 Patrones GoF

| Categoría | Propósito Principal | Patrones Incluidos |
|-----------|---------------------|-------------------|
| **Creacionales** | Abstraen el proceso de instanciación | **Singleton**, **Factory Method**, **Abstract Factory**, **Builder**, **Prototype** |
| **Estructurales** | Composición de clases y objetos | **Adapter**, **Bridge**, **Composite**, **Decorator**, **Facade**, **Proxy**, **Flyweight** |
| **Comportamiento** | Algoritmos y asignación de responsabilidades | **Observer**, **Strategy**, **Command**, **Iterator**, **State**, **Template Method**, Chain of Resp., Mediator, Memento, Visitor, Interpreter |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Síntesis: [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones GoF]]
""",

    "wiki/entities/java-platform-and-jvm.md": """---
title: "Plataforma Java, JVM y Ecosistema Spring"
type: "entity"
tags:
  - java
  - jvm
  - spring
  - bytecode
  - garbage-collector
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Java"
  - "JVM"
  - "Spring Boot"
---

# Plataforma Java, JVM y Ecosistema Spring

Plataforma de desarrollo empresarial orientada a objetos basada en el paradigma *"Write Once, Run Anywhere"* mediante la compilación de código fuente a **Bytecode** ejecutado por la **JVM**.

---

## 🏛️ Arquitectura de Memoria de la JVM

- **Stack (Pila)**: Hilos de ejecución, variables primitivas locales y referencias a objetos.
- **Heap (Montículo)**: Almacén de objetos gestionado por el **Garbage Collector (GC)**.
  - *Young Generation*: Eden + Survivor Spaces (S0/S1). Limpiado por *Minor GC*.
  - *Old Generation (Tenured)*: Objetos de larga vida. Limpiado por *Major/Full GC*.
  - *Metaspace (Java 8+)*: Metadatos de clases en memoria nativa del sistema operativo.
- **Ecosistema**: **Spring Boot** con Inversión de Control (IoC) e Inyección de Dependencias (DI).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Entidad: [[wiki/entities/git-version-control-system|Git]]
""",

    "wiki/entities/git-version-control-system.md": """---
title: "Sistema de Control de Versiones Distribuido Git"
type: "entity"
tags:
  - git
  - control-versiones
  - devops
  - repositorios
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Git"
  - "Control de Versiones"
---

# Sistema de Control de Versiones Distribuido Git

Sistema de control de versiones descentralizado creado por Linus Torvalds que registra instantáneas (*snapshots*) completas del árbol de archivos.

---

## 🏛️ Zonas de Trabajo y Comandos

```
      Working Directory ──────[ git add ]──────> Staging Area (Index)
             │                                         │
      [ git checkout ]                          [ git commit ]
             │                                         │
             ▼                                         ▼
      Archivos Modificados                     Local Repository (.git)
                                                       │
                                                [ git push / pull ]
                                                       │
                                                       ▼
                                                Remote Repository
```

- **`git merge` vs `git rebase`**: `merge` preserva el historial creando un commit de unión; `rebase` reescribe los commits linealmente sobre la rama destino.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Concepto: [[wiki/concepts/ci-cd-pipelines-and-devops|Pipelines CI/CD]]
""",

    "wiki/entities/rest-and-soap-web-services.md": """---
title: "Servicios Web: APIs RESTful y Protocolo SOAP"
type: "entity"
tags:
  - web-services
  - rest
  - soap
  - apis
  - http
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "REST y SOAP"
  - "Servicios Web"
  - "APIs RESTful"
---

# Servicios Web: APIs RESTful y Protocolo SOAP

Mecanismos estándares para la interoperabilidad e intercambio de datos entre aplicaciones en red.

---

## 🏛️ Contraste SOAP vs REST

- **SOAP**: Protocolo formal del W3C basado estrictamente en **XML**. Mensajes con estructura `Envelope`, `Header`, `Body` y `Fault`. Descriptores formales **WSDL** y seguridad **WS-Security**.
- **REST**: Estilo arquitectónico basado en **HTTP**. Recursos identificados por **URIs**, comunicación sin estado (**Stateless**), representaciones **JSON** y verbos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema04|Resumen Bloque 3 - Tema 04]]
- Síntesis: [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
""",

    "wiki/entities/web-accessibility-wcag-and-rd-1112-2018.md": """---
title: "Accesibilidad Web: WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018"
type: "entity"
tags:
  - accesibilidad-web
  - wcag
  - pour
  - rd-1112-2018
  - administracion-publica
sources:
  - "raw/sources/bloque3-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Accesibilidad Web"
  - "WCAG"
  - "RD 1112/2018"
---

# Accesibilidad Web: WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018

Marco normativo y técnico para garantizar el acceso universal a los sitios web y aplicaciones móviles del sector público para personas con discapacidad.

---

## 🏛️ Principios POUR y Nivel Legal

- **4 Principios WCAG**: **Perceptible**, **Operable**, **Comprensible** y **Robusto** (POUR).
- **Exigencia Legal**: **Nivel AA** obligatorio en todas las AAPP españolas bajo el **Real Decreto 1112/2018** y la norma europea **EN 301 549**.
- **Obligaciones del RD 1112/2018**: Declaración de accesibilidad, canal de quejas/reclamaciones y designación de una **Unidad Responsable de Accesibilidad (URA)**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema06|Resumen Bloque 3 - Tema 06]]
- Síntesis: [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR]]
"""
}

print("[*] Escribiendo 8 entidades del Bloque 3...")
for path, content in BLOQUE3_ENTITIES.items():
    write_file(path, content)

# ==============================================================================
# CONCEPTOS BLOQUE 3 (4 Conceptos)
# ==============================================================================

BLOQUE3_CONCEPTS = {
    "wiki/concepts/software-lifecycle-models.md": """---
title: "Modelos del Ciclo de Vida del Software"
type: "concept"
tags:
  - ciclo-de-vida
  - cascada
  - espiral
  - modelo-en-v
  - prototipado
sources:
  - "raw/sources/bloque3-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ciclo de Vida del Software"
  - "Modelos de Ciclo de Vida"
---

# Modelos del Ciclo de Vida del Software

Marcos conceptuales que describen las fases y transiciones desde la concepción de un software hasta su retirada.

---

## 🏛️ Modelos Clásicos

1. **Cascada**: Secuencial lineal. Sencillo pero rígido; no tolera cambios de requisitos.
2. **Modelo en V**: Establece correspondencia directa y simétrica entre fases de diseño y niveles de pruebas.
3. **Espiral (Boehm)**: Iterativo y guiado por la **evaluación continua de riesgos**.
4. **Prototipado**: Reducción de incertidumbre de requisitos mediante maquetas interactivas.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/metrica-v3-methodology|MÉTRICA v3]]
""",

    "wiki/concepts/white-box-and-black-box-testing.md": """---
title: "Pruebas de Caja Blanca, Caja Negra y Complejidad Ciclomática de McCabe"
type: "concept"
tags:
  - testing
  - caja-blanca
  - caja-negra
  - mccabe
  - qa
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Caja Blanca y Caja Negra"
  - "Complejidad de McCabe"
---

# Pruebas de Caja Blanca, Caja Negra y Complejidad Ciclomática de McCabe

Estrategias fundamentales de diseño de casos de prueba en ingeniería de software.

---

## 🏛️ Comparativa y Fórmulas

- **Caja Blanca (Estructural)**: Analiza el código interno.
  - **Fórmula de McCabe**: $$V(G) = E - N + 2P = \text{Nodos Predicado} + 1$$
  - Determina el número de caminos independientes básicos para cobertura total.
- **Caja Negra (Funcional)**: Basada en especificación.
  - **Técnicas**: Particiones de equivalencia (clases válidas/inválidas) y análisis de valores límite (BVA).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software]]
""",

    "wiki/concepts/ci-cd-pipelines-and-devops.md": """---
title: "Pipelines CI/CD, DevOps y Calidad de Código"
type: "concept"
tags:
  - cicd
  - devops
  - integracion-continua
  - sonarqube
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "CI/CD"
  - "Integración y Despliegue Continuo"
---

# Pipelines CI/CD, DevOps y Calidad de Código

Automatización del ciclo de entrega de software desde el commit del desarrollador hasta producción.

---

## 🏛️ Fases del Pipeline CI/CD

1. **Integración Continua (CI)**: Compilación y ejecución automática de pruebas unitarias/integración tras cada commit.
2. **Entrega Continua (Continuous Delivery)**: Empaquetado de artefactos listos para despliegue manual en producción.
3. **Despliegue Continuo (Continuous Deployment)**: Paso a producción 100% automatizado tras superar todos los tests.
4. **Análisis Estático (SonarQube)**: Inspección de código, cálculo de deuda técnica y verificación de *Quality Gates*.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Entidad: [[wiki/entities/git-version-control-system|Git]]
""",

    "wiki/concepts/multitier-and-microservices-architectures.md": """---
title: "Arquitecturas Multicapa y Microservicios"
type: "concept"
tags:
  - arquitectura-software
  - microservicios
  - multicapa
  - api-gateway
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitecturas Multicapa"
  - "Microservicios"
---

# Arquitecturas Multicapa y Microservicios

Evolución arquitectónica desde aplicaciones monolíticas multicapa hacia servicios independientes distribuidos.

---

## 🏛️ Modelos Arquitectónicos

- **Arquitectura Multicapa (3-Tier)**: Separación en Capa de Presentación, Lógica de Negocio y Persistencia/BD.
- **Arquitectura de Microservicios**: Servicios autónomos desacoplados con su propia base de datos, coordinados mediante **API Gateway**, *Service Discovery* y mensajería asíncrona (RabbitMQ/Kafka).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema04|Resumen Bloque 3 - Tema 04]]
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios REST y SOAP]]
"""
}

print("[*] Escribiendo 4 conceptos de Desarrollo de Sistemas...")
for path, content in BLOQUE3_CONCEPTS.items():
    write_file(path, content)

# ==============================================================================
# SÍNTESIS BLOQUE 3 (6 Fichas)
# ==============================================================================

BLOQUE3_SYNTHESES = {
    "wiki/synthesis/bloque3-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-3
  - oposiciones
  - tai
sources:
  - "raw/sources/bloque3-tema01.md"
  - "raw/sources/bloque3-tema02.md"
  - "raw/sources/bloque3-tema03.md"
  - "raw/sources/bloque3-tema04.md"
  - "raw/sources/bloque3-tema05.md"
  - "raw/sources/bloque3-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 3"
  - "Bloque 3 TAI Master Guide"
---

# Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)

Mapa integral de conocimientos del **Bloque 3 (Desarrollo de Sistemas)** para las oposiciones TAI de la AGE.

---

## 🗺️ Mapa Temático del Bloque 3

| Tema | Materia Oficial | Resumen Fuente | Entidades Clave | Conceptos Clave |
|------|-----------------|----------------|-----------------|-----------------|
| **Tema 01** | Ciclo de Vida, Scrum y MÉTRICA v3 | [[wiki/sources/bloque3-tema01\|Resumen Tema 01]] | [[wiki/entities/metrica-v3-methodology\|MÉTRICA v3]], [[wiki/entities/scrum-and-agile-frameworks\|Scrum y Ágil]] | [[wiki/concepts/software-lifecycle-models\|Ciclo de Vida]] |
| **Tema 02** | Análisis OO, UML 2.x y Patrones GoF | [[wiki/sources/bloque3-tema02\|Resumen Tema 02]] | [[wiki/entities/uml-diagrams-and-modeling\|Diagramas UML]], [[wiki/entities/gof-design-patterns\|Patrones GoF]] | Principios SOLID |
| **Tema 03** | Lenguajes, Java/JVM y Git | [[wiki/sources/bloque3-tema03\|Resumen Tema 03]] | [[wiki/entities/java-platform-and-jvm\|Java y JVM]], [[wiki/entities/git-version-control-system\|Git]] | Stack vs Heap, GitFlow |
| **Tema 04** | Arquitecturas Web, REST y SOAP | [[wiki/sources/bloque3-tema04\|Resumen Tema 04]] | [[wiki/entities/rest-and-soap-web-services\|REST y SOAP]] | [[wiki/concepts/multitier-and-microservices-architectures\|Multicapa y Microservicios]] |
| **Tema 05** | Calidad, Pruebas y CI/CD | [[wiki/sources/bloque3-tema05\|Resumen Tema 05]] | Jenkins, SonarQube | [[wiki/concepts/white-box-and-black-box-testing\|Caja Blanca/Negra y McCabe]], [[wiki/concepts/ci-cd-pipelines-and-devops\|CI/CD]] |
| **Tema 06** | Accesibilidad Web (WCAG y RD 1112/2018) | [[wiki/sources/bloque3-tema06\|Resumen Tema 06]] | [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018\|Accesibilidad WCAG y RD 1112]] | Principios POUR, Nivel AA |

---

## 📚 Síntesis Monográficas de Examen
- [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía de Procesos y Artefactos de MÉTRICA v3]]
- [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones de Diseño GoF]]
- [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
- [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software y QA]]
- [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR y Accesibilidad Pública]]
""",

    "wiki/synthesis/metrica-v3-processes-and-artifacts-guide.md": """---
title: "Guía de Procesos, Actividades y Artefactos de MÉTRICA Versión 3"
type: "synthesis"
tags:
  - synthesis
  - metrica-v3
  - ingenieria-software
  - administracion-publica
sources:
  - "raw/sources/bloque3-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía MÉTRICA v3"
  - "Procesos MÉTRICA v3"
---

# Guía de Procesos, Actividades y Artefactos de MÉTRICA Versión 3

Tabla integral de referencia de la metodología oficial de desarrollo del software en las Administraciones Públicas.

---

## 🏛️ Matriz de Procesos y Entregables

| Proceso | Objetivo Principal | Actividades Clave | Productos Entregables Principales |
|---------|--------------------|-------------------|-----------------------------------|
| **PSI** (Planificación) | Marco estratégico global de SI | Definición de arquitectura tecnológica y plan de proyectos | Plan de Proyectos, Modelo de Información |
| **EVS** (Estudio Viabilidad) | Análisis coste/beneficio y viabilidad | Estudio situación actual y alternativas | Propuesta de Solución Seleccionada |
| **ASI** (Análisis) | Requisitos detallados del sistema | Casos de uso, modelo de datos y procesos | Catálogo de Requisitos, Modelo Lógico de Datos |
| **DSI** (Diseño) | Especificación de arquitectura física | Diseño de BD, módulos, interfaces y plan de pruebas | Modelo Físico de BD, Plan de Pruebas |
| **CSI** (Construcción) | Codificación y pruebas de componentes | Pruebas unitarias, integración y sistema | Componentes ejecutables, Manuales de Usuario |
| **IAS** (Implantación) | Puesta en explotación y entrega | Migración de datos, formación y pruebas de aceptación | Sistema en Producción, Acta de Aceptación |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/metrica-v3-methodology|MÉTRICA v3]]
""",

    "wiki/synthesis/gof-design-patterns-cheatsheet.md": """---
title: "Cheatsheet de Patrones de Diseño GoF (Gang of Four)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - gof
  - patrones-diseno
  - poo
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet Patrones GoF"
  - "Patrones de Diseño Tabla"
---

# Cheatsheet de Patrones de Diseño GoF (Gang of Four)

Clasificación de los 23 patrones clásicos con su propósito de diseño.

---

## 🏛️ Tabla Maestra de Patrones GoF

| Patrón | Tipo | Intención / Propósito de Diseño |
|--------|------|---------------------------------|
| **Singleton** | Creacional | Garantiza una **única instancia** de una clase con acceso global |
| **Factory Method** | Creacional | Delega la instanciación de objetos en las subclases |
| **Abstract Factory**| Creacional | Crea **familias de objetos** relacionados sin especificar clases concretas |
| **Builder** | Creacional | Construye objetos complejos paso a paso separando construcción y representación |
| **Prototype** | Creacional | Crea objetos clonando instancias existentes |
| **Adapter** | Estructural | **Adapta interfaces incompatibles** para que puedan colaborar |
| **Composite** | Estructural | Estructuras en árbol para representar jerarquías parte-todo |
| **Decorator** | Estructural | **Añade responsabilidades dinámicamente** sin modificar la clase |
| **Facade** | Estructural | Proporciona una **interfaz simplificada** a un subsistema complejo |
| **Proxy** | Estructural | Objeto intermediario que controla el acceso a otro objeto |
| **Observer** | Comportamiento| Notificación automática 1 a N ante cambios de estado |
| **Strategy** | Comportamiento| Encapsula una familia de algoritmos haciéndolos intercambiables |
| **Command** | Comportamiento| Encapsula una petición como un objeto para colas y operaciones undo |
| **Template Method** | Comportamiento| Define el esqueleto de un algoritmo difiriendo pasos a subclases |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones GoF]]
""",

    "wiki/synthesis/rest-vs-soap-comparison-guide.md": """---
title: "Guía Comparativa de Servicios Web: REST vs SOAP"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - rest
  - soap
  - apis
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa REST vs SOAP"
  - "REST vs SOAP Guía"
---

# Guía Comparativa de Servicios Web: REST vs SOAP

Matriz de contraste técnico entre servicios web tradicionales SOAP y APIs RESTful.

---

## 🏛️ Matriz Técnica Comparativa

| Criterio | SOAP | REST |
|----------|------|------|
| **Tipo** | Protocolo formal W3C | Estilo arquitectónico (Roy Fielding) |
| **Formato de Carga Útil** | **Exclusivamente XML** | **JSON** (predominante), XML, YAML, HTML |
| **Contrato Formal** | **WSDL** (XML) | OpenAPI / Swagger |
| **Transporte** | HTTP, SMTP, TCP, JMS | Exclusivamente sobre **HTTP / HTTPS** |
| **Manejo de Estado** | Opcionalmente con estado (*Stateful*) | Estrictamente **Sin Estado (*Stateless*)** |
| **Seguridad** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Rendimiento y Sobrecarga** | Pesado (envoltorios XML grandes) | Ligero y optimizado para web y móviles |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema04|Resumen Bloque 3 - Tema 04]]
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios REST y SOAP]]
""",

    "wiki/synthesis/software-testing-and-qa-guide.md": """---
title: "Guía de Pruebas de Software, Métricas de Cobertura y McCabe"
type: "synthesis"
tags:
  - synthesis
  - testing
  - caja-blanca
  - mccabe
  - qa
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Testing"
  - "Pruebas de Software QA"
---

# Guía de Pruebas de Software, Métricas de Cobertura y McCabe

Manual de diseño de casos de prueba y niveles de verificación para oposiciones TAI.

---

## 🔢 1. Cálculo de la Complejidad Ciclomática de McCabe ($V(G)$)

Fórmula fundamental para determinar el número de casos de prueba de caminos independientes:
$$V(G) = E - N + 2P$$
- $E$: Aristas (*Edges*).
- $N$: Nodos (*Nodes*).
- $P$: Componentes conexos ($P=1$ para un único programa).
- **Regla Inmediata**: $V(G) = \text{Nodos de Decisión (if/while/for)} + 1$.

---

## 📋 2. Jerarquía de Pruebas de Software

1. **Unitarias**: Módulos/métodos aislados.
2. **Integración**: Interfaces y comunicación entre módulos.
3. **Sistema**: Requisitos funcionales y no funcionales globales.
4. **Aceptación**: Validación final del usuario de negocio (*Alpha/Beta*).
5. **Regresión**: Comprobación tras modificaciones o corrección de bugs.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Caja Blanca y Caja Negra]]
""",

    "wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet.md": """---
title: "Cheatsheet de Principios POUR y Accesibilidad Web en el Sector Público (RD 1112/2018)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - accesibilidad-web
  - wcag
  - pour
  - rd-1112-2018
sources:
  - "raw/sources/bloque3-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet POUR"
  - "Accesibilidad RD 1112/2018"
---

# Cheatsheet de Principios POUR y Accesibilidad Web en el Sector Público (RD 1112/2018)

Resumen de los 4 principios WCAG y requisitos legales obligatorios para las Administraciones Públicas.

---

## 👁️ Los 4 Principios POUR de las WCAG

| Principio | Significado | Criterios Clave Nivel AA |
|-----------|-------------|--------------------------|
| **P - Perceptible** | La información debe presentarse para que los usuarios puedan percibirla | Texto alternativo (`alt`), contraste mínimo **4.5:1** (3:1 texto grande), subtítulos |
| **O - Operable** | Los componentes y navegación deben ser manejables | **Accesibilidad por teclado completa**, sin trampas de foco, tiempo suficiente |
| **U - Comprensible** | La información y operación deben ser claras | Idioma de la página declarado (`lang="es"`), formularios con ayuda y detección de errores |
| **R - Robusto** | Compatible con tecnologías de asistencia actuales y futuras | Marcado HTML estándar válido, uso de atributos **WAI-ARIA** |

---

## 🏛️ Exigencias del Real Decreto 1112/2018 para AAPP

- **Nivel Exigido**: **Nivel AA** (norma europea EN 301 549).
- **Declaración de Accesibilidad**: Obligatoria y actualizada en cada web/app pública.
- **Unidad Responsable de Accesibilidad (URA)**: Designación obligatoria en cada organismo público.
- **Mecanismo de Comunicación**: Canal para consultas, sugerencias y reclamaciones ciudadanas.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema06|Resumen Bloque 3 - Tema 06]]
- Entidad: [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018|Accesibilidad Web]]
"""
}

print("[*] Escribiendo 6 síntesis del Bloque 3...")
for path, content in BLOQUE3_SYNTHESES.items():
    write_file(path, content)

print("[*] Generación del Bloque 3 completada exitosamente.")
