---
title: "Test de Autoevaluación: Bloque 3 - Tema 04 (POO, Patrones de Diseño GoF y UML 2.x)"
type: "test"
target: "wiki/sources/bloque3-tema04.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-3
  - poo
  - gof
  - patrones-diseno
  - uml
sources:
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 04: POO, Patrones de Diseño GoF y Diagramas UML 2.x

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. ¿A qué categoría de patrones GoF pertenece el patrón 'Singleton', que garantiza que una clase tenga una única instancia en toda la aplicación?
- [ ] a) Estructural.
- [ ] b) Creacional.
- [ ] c) De Comportamiento.
- [ ] d) Arquitectónico.

### 2. ¿Qué patrón de diseño GoF define una dependencia 1 a N entre objetos, de forma que cuando el objeto principal cambia de estado, todos sus dependientes son notificados y actualizados automáticamente?
- [ ] a) Strategy.
- [ ] b) Observer.
- [ ] c) Decorator.
- [ ] d) Facade.

### 3. El patrón 'Decorator' se utiliza principalmente para:
- [ ] a) Convertir la interfaz de una clase en otra interfaz esperada por el cliente.
- [ ] b) Añadir responsabilidades y funcionalidades a un objeto de manera dinámica y flexible sin recurrir a la herencia múltiple.
- [ ] c) Proporcionar una interfaz unificada y simplificada a un conjunto de interfaces de un subsistema.
- [ ] d) Encapsular una petición como un objeto.

### 4. En un Diagrama de Clases UML 2.x, ¿cómo se representa una relación de COMPOSICIÓN (agregación fuerte con ciclo de vida coincidente)?
- [ ] a) Línea con rombo hueco en el extremo del todo.
- [ ] b) Línea con rombo relleno (negro) en el extremo del todo.
- [ ] c) Línea discontinua con flecha abierta.
- [ ] d) Línea continua con triángulo hueco.

### 5. ¿Cuál de los siguientes diagramas de UML 2.x es un diagrama de COMPORTAMIENTO o DINÁMICO?
- [ ] a) Diagrama de Clases.
- [ ] b) Diagrama de Secuencia.
- [ ] c) Diagrama de Despliegue.
- [ ] d) Diagrama de Componentes.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: Singleton, Factory Method, Abstract Factory, Builder y Prototype son patrones Creacionales.
> - **Pregunta 2 (b)**: Observer (Sujeto/Observador) gestiona eventos y suscripciones 1:N.
> - **Pregunta 3 (b)**: Decorator es un patrón estructural para envolver objetos y agregar funcionalidad en tiempo de ejecución.
> - **Pregunta 4 (b)**: Composición = Rombo relleno (negro). Agregación débil = Rombo hueco (blanco).
> - **Pregunta 5 (b)**: Diagrama de Secuencia es de interacción/comportamiento; Clases, Componentes y Despliegue son estructurales.
