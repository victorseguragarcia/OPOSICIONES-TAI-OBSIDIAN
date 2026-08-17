---
title: "Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III (20 Preguntas)"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-3
  - examen-tai
  - oposiciones
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Simulacro Examen Bloque 3"
  - "Supuesto Oficial TAI Bloque III"
---

# 🔴 Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III

Simulacro de 20 preguntas reales con plantilla oficial argumentada cubriendo Desarrollo de Sistemas, Bases de Datos, Accesibilidad, UML, Git y Métrica v3.

---

## 📝 Bloque de Preguntas de Examen

### Pregunta 1: Métrica v3 y Estudio de Viabilidad
En MÉTRICA Versión 3, ¿en qué proceso se define la arquitectura de información y el plan global de proyectos de una organización?
> [!question]- ❓ Ver Solución
> **Respuesta**: **PSI (Planificación de Sistemas de Información)**.
> *Justificación*: EVS analiza la viabilidad de un sistema individual, mientras que PSI establece el marco estratégico global.

---

### Pregunta 2: Diagramas UML de Interacción
En un diagrama de casos de uso UML 2.x, ¿qué relación indica que el caso de uso base incorpora obligatoriamente el comportamiento de otro caso de uso?
> [!question]- ❓ Ver Solución
> **Respuesta**: **`<<include>>`** (mientras que `<<extend>>` es opcional y depende de una condición de extensión).

---

### Pregunta 3: Patrones de Diseño GoF
¿Qué patrón de diseño estructural permite añadir funcionalidades a un objeto dinámicamente en tiempo de ejecución sin alterar la clase original ni utilizar herencia estática?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Decorator (Envoltorio)**.

---

### Pregunta 4: Transacciones ACID
En el estándar ANSI SQL, ¿qué nivel de aislamiento previene las *Lecturas Sucias* y las *Lecturas No Repetibles*, pero no garantiza la prevención de *Lecturas Fantasma*?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Repeatable Read**.

---

### Pregunta 5: Accesibilidad Web Pública (RD 1112/2018)
Según el Real Decreto 1112/2018, ¿cuál es el plazo máximo para responder a una reclamación sobre accesibilidad presentada por un ciudadano ante la URA?
> [!question]- ❓ Ver Solución
> **Respuesta**: **20 días hábiles**.

---

### Pregunta 6: Git y Reescribir Historial
¿Qué comando de Git aplica un commit específico de una rama diferente sobre la rama actualmente activa?
> [!question]- ❓ Ver Solución
> **Respuesta**: **`git cherry-pick <commit-hash>`**.

---

### Pregunta 7: Métricas de Calidad de McCabe
Si un programa posee un grafo de flujo de control con 14 aristas ($E$), 10 nodos ($N$) y 1 componente conexo ($P$), ¿cuál es su complejidad ciclomática $V(G)$?
> [!question]- ❓ Ver Solución
> **Respuesta**: **$V(G) = E - N + 2P = 14 - 10 + 2(1) = 6$**.

---

### Pregunta 8: Arquitectura RESTful
En el modelo de madurez de Richardson para APIs REST, ¿qué nivel introduce el uso de hipermedios y enlaces dinámicos (HATEOAS)?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Nivel 3 (Hypermedia Controls / HATEOAS)**.

---

## 🎯 Plantilla Resumen de Respuestas
| Nº | Materia | Respuesta Clave |
|---|---|---|
| **1** | Métrica v3 | **PSI** |
| **2** | UML | **`<<include>>`** |
| **3** | Patrones GoF | **Decorator** |
| **4** | SQL ACID | **Repeatable Read** |
| **5** | RD 1112/2018 | **20 días hábiles** |
| **6** | Git | **`git cherry-pick`** |
| **7** | McCabe | **$V(G) = 6$** |
| **8** | REST | **Nivel 3 (HATEOAS)** |

---

## 🔗 Referencias Cruzadas
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
