---
title: "Resumen Exhaustivo Tema 02 (Bloque 3): Lenguajes de Programación y Paradigmas (POO, SOLID, Patrones GoF)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-02
  - desarrollo
  - bbdd
  - ingenieria-software
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema02.md]]"
  - "[[wiki/sources/bloque3-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema03|Tema 03 ➡️]]

# 🔴 Resumen Exhaustivo Tema 02 (Bloque 3): Lenguajes de Programación y Paradigmas (POO, SOLID, Patrones GoF)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 02**
> Paradigmas de programación (Imperativo, Declarativo, Funcional, Orientado a Objetos), pilares de POO (Abstracción, Encapsulamiento, Herencia, Polimorfismo), principios SOLID de diseño de software y catálogo de patrones de diseño GoF (Creacionales, Estructurales y de Comportamiento).

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Paradigmas de Programación y Pilares de POO
- **Clasificación de Paradigmas**:
  - *Imperativo/Estructurado*: Secuencia de instrucciones que modifican el estado (C, Pascal).
  - *Declarativo*: Especifica qué resultado se desea sin detallar el flujo de control (SQL, Prolog).
  - *Funcional*: Funciones puras de primer orden, inmutabilidad de datos y sin efectos secundarios (Haskell, Scala, Lisp, Erlang).
  - *Orientado a Objetos (POO)*: Modelado basado en clases, objetos y paso de mensajes (Java, C++, C#, Python).
- **Los 4 Pilares Fundamentales de la POO**:
  1. **Abstracción**: Oculta los detalles complejos mostrando solo las características esenciales mediante interfaces y clases abstractas.
  2. **Encapsulamiento**: Agrupación de datos y métodos con restricción de acceso directo mediante modificadores (`private`, `protected`, `public`, `default/package`).
  3. **Herencia**: Mecanismo que permite a una clase hija heredar atributos y comportamientos de una clase padre, promoviendo la reutilización de código (simple en Java/C#, múltiple en C++/Python).
  4. **Polimorfismo**: Capacidad de objetos de diferentes clases de responder al mismo mensaje de formas distintas:
     - *Estático (Sobrecarga / Overloading)*: Mismo nombre de método con distinta firma (número o tipo de parámetros) resuelto en tiempo de compilación.
     - *Dinámico (Sobreescritura / Overriding)*: Reimplementación de un método heredado con la misma firma resuelto en tiempo de ejecución (*late binding* / despacho dinámico).

### 2. Principios SOLID de Diseño Orientado a Objetos

| Principio SOLID | Nombre Completo en Español | Definición y Regla de Oro |
|:---|:---|:---|
| **S** | **Single Responsibility Principle (SRP)** | **Principio de Responsabilidad Única**: Una clase debe tener una única razón para cambiar (un solo propósito o responsabilidad funcional). |
| **O** | **Open/Closed Principle (OCP)** | **Principio de Abierto/Cerrado**: Las entidades de software (clases, módulos, funciones) deben estar **abiertas para su extensión, pero cerradas para su modificación** (utilizando abstracciones e interfaces). |
| **L** | **Liskov Substitution Principle (LSP)** | **Principio de Sustitución de Liskov**: Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el correcto funcionamiento del programa. |
| **I** | **Interface Segregation Principle (ISP)** | **Principio de Segregación de Interfaces**: Los clientes no deben verse forzados a depender de interfaces que no utilizan (preferir muchas interfaces específicas y pequeñas a una sola interfaz sobrecargada). |
| **D** | **Dependency Inversion Principle (DIP)** | **Principio de Inversión de Dependencias**: Los módulos de alto nivel no deben depender de los de bajo nivel; ambos deben depender de abstracciones. Las abstracciones no deben depender de los detalles (inyección de dependencias - IoC). |

### 3. Catálogo de Patrones de Diseño GoF (Gang of Four)

| Categoría GoF | Patrón de Diseño | Propósito y Estructura Clave |
|:---|:---|:---|
| **Creacionales** (Instanciación de objetos) | **Singleton** | Garantiza que una clase tenga **una única instancia** en todo el sistema y proporciona un punto de acceso global a ella. |
| | **Factory Method** | Define una interfaz para crear un objeto, pero delega en las subclases la decisión de qué clase exacta instanciar. |
| | **Abstract Factory** | Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. |
| | **Builder** | Separa la construcción de un objeto complejo de su representación, permitiendo crear diferentes configuraciones paso a paso. |
| | **Prototype** | Crea nuevos objetos clonando una instancia existente (*shallow/deep copy*). |
| **Estructurales** (Composición de clases y objetos) | **Adapter** | Convierte la interfaz de una clase en otra interfaz que el cliente espera, permitiendo colaborar a clases incompatibles. |
| | **Decorator** | Añade responsabilidades y comportamientos a un objeto dinámicamente sin modificar la clase base (alternativa flexible a la herencia). |
| | **Facade (Fachada)** | Proporciona una interfaz simplificada y unificada de alto nivel a un subsistema complejo de clases. |
| | **Proxy** | Proporciona un objeto sustituto o intermediario que controla el acceso a otro objeto (remoto, virtual/perezoso, de seguridad). |
| | **Composite** | Compone objetos en estructuras de árbol para representar jerarquías parte-todo (trata a objetos individuales y compuestos uniformemente). |
| **Comportamiento** (Interacción y algoritmos) | **Observer** | Define una dependencia 1 a N entre objetos, de modo que cuando uno cambia de estado, **todos sus observadores son notificados y actualizados automáticamente** (arquitecturas Publish/Subscribe, eventos GUI). |
| | **Strategy** | Define una familia de algoritmos, encapsula cada uno y los hace intercambiables en tiempo de ejecución. |
| | **Command** | Encapsula una petición como un objeto, permitiendo parametrizar clientes, encolar operaciones y soportar deshacer (*undo*). |
| | **Iterator** | Proporciona un modo de acceder secuencialmente a los elementos de una colección sin exponer su representación interna. |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 02 (Bloque 3)**
> 1. **Sobrecarga (Overloading) vs Sobreescritura (Overriding)**: La *Sobrecarga* cambia los parámetros y se resuelve en compilación; la *Sobreescritura* mantiene firma exacta y se resuelve en tiempo de ejecución.
> 2. **Clasificación de Patrones GoF**: *Singleton, Factory, Builder* son **Creacionales**; *Adapter, Decorator, Facade, Proxy* son **Estructurales**; *Observer, Strategy, Command* son de **Comportamiento**.
> 3. **Principio de Liskov (LSP)**: Se viola frecuentemente al heredar cuando una subclase lanza excepciones no previstas o anula métodos del padre cambiando su contrato.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **SOLID**: **S**ingle, **O**pen, **L**iskov, **I**nterface, **D**ependency.
> - **Patrones Creacionales**: **S-F-A-B-P** $\rightarrow$ **S**ingleton, **F**actory Method, **A**bstract Factory, **B**uilder, **P**rototype.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema02|Fuente Oficial del Tema 02]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema02|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema02-lenguajes-compiladores|Test Tema 02]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema03|Tema 03 ➡️]]
