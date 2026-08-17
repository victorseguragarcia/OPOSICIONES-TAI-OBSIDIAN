---
title: "Bloque 3 - Tema 02: Análisis y Diseño Orientado a Objetos, UML 2.x y Patrones de Diseño GoF"
type: "raw-source"
topic: "poo-uml-patrones"
date: "2026-08-17"
---

# Bloque 3 - Tema 02: Análisis y Diseño Orientado a Objetos, Lenguaje Unificado de Modelado (UML 2.x) y Patrones de Diseño (GoF)

## 1. Principios del Paradigma Orientado a Objetos (POO)
- **Abstracción**: Identificación de las características esenciales de un objeto prescindiendo de los detalles no relevantes.
- **Encapsulamiento**: Ocultación del estado interno de un objeto protegiendo sus atributos mediante métodos de acceso públicos (*getters/setters*). Modificadores de acceso: `public` (+), `private` (-), `protected` (#) y `package/default` (~).
- **Herencia**: Mecanismo que permite a una clase hija (*subclase*) heredar atributos y métodos de una clase padre (*superclase*). Relación "es-un" (*is-a*).
- **Polimorfismo**: Capacidad de objetos de diferentes clases de responder a un mismo mensaje de forma diferente. Sobrecarga (*Overloading*, polimorfismo estático en tiempo de compilación) vs Sobrescritura (*Overriding*, polimorfismo dinámico en tiempo de ejecución con ligadura tardía).
- **Principios SOLID (Robert C. Martin)**:
  - **S - Single Responsibility Principle**: Una clase debe tener una única razón para cambiar.
  - **O - Open/Closed Principle**: Abierto para la extensión, cerrado para la modificación.
  - **L - Liskov Substitution Principle**: Las subclases deben poder sustituir a sus clases base sin alterar el comportamiento.
  - **I - Interface Segregation Principle**: Múltiples interfaces específicas son mejores que una interfaz genérica.
  - **D - Dependency Inversion Principle**: Depender de abstracciones, no de implementaciones concretas.

## 2. Lenguaje Unificado de Modelado (UML 2.x)
Estándar de la OMG (Object Management Group) para visualización y especificación de software.
- **Diagramas Estructurales (Estáticos)**:
  1. **Diagrama de Clases**: Muestra clases, atributos, operaciones y relaciones (Asociación, Agregación rombo blanco, Composición rombo negro, Generalización/Herencia triángulo hueco, Dependencia flecha discontinua).
  2. **Diagrama de Objetos**: Muestra instancias concretas de clases y valores de atributos en un instante temporal.
  3. **Diagrama de Componentes**: Muestra la organización y dependencias entre módulos de software y librerías ejecutables.
  4. **Diagrama de Despliegue**: Muestra la arquitectura física del hardware (nodos, servidores, dispositivos) y los artefactos de software instalados en ellos.
  5. **Diagrama de Paquetes**: Agrupación lógica de elementos en espacios de nombres.
  6. **Diagrama de Estructura Compuesta**: Estructura interna de una clase o clasificador.
- **Diagramas de Comportamiento (Dinámicos)**:
  1. **Diagrama de Casos de Uso**: Actores, casos de uso y relaciones (`<<include>>` obligatoria/precondición, `<<extend>>` opcional/punto de extensión, y generalización).
  2. **Diagrama de Secuencia**: Representa la interacción e intercambio de mensajes ordenados cronológicamente a lo largo de líneas de vida (*lifelines*).
  3. **Diagrama de Actividades**: Flujo de control y datos paso a paso con bifurcaciones, uniones y barras de sincronización (*fork/join*).
  4. **Diagrama de Máquina de Estados**: Estados de un objeto a lo largo de su ciclo de vida y transiciones disparadas por eventos.
  5. **Diagrama de Comunicación (antiguo Colaboración)**: Muestra interacciones entre objetos enfatizando los enlaces estructurales.
  6. **Diagrama Global de Interacción** y **Diagrama de Tiempos**.

## 3. Patrones de Diseño (GoF - Gang of Four)
Soluciones reutilizables a problemas comunes de diseño de software (Gamma, Helm, Johnson, Vlissides, 1994).
- **1. Patrones Creacionales (Mecanismos de creación de objetos)**:
  - **Singleton**: Garantiza que una clase tenga una única instancia en toda la aplicación y proporciona un punto de acceso global a ella.
  - **Factory Method**: Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase concreta instanciar.
  - **Abstract Factory**: Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
  - **Builder**: Separa la construcción de un objeto complejo de su representación, permitiendo que el mismo proceso cree representaciones distintas.
  - **Prototype**: Crea nuevos objetos clonando una instancia existente.
- **2. Patrones Estructurales (Composición de clases y objetos)**:
  - **Adapter**: Convierte la interfaz de una clase en otra interfaz que el cliente espera, permitiendo trabajar juntas a clases incompatibles.
  - **Bridge**: Desacopla una abstracción de su implementación para que ambas puedan variar independientemente.
  - **Composite**: Compone objetos en estructuras de árbol para representar jerarquías parte-todo (trata a objetos individuales y compuestos uniformemente).
  - **Decorator**: Añade responsabilidades adicionales a un objeto dinámicamente sin modificar la clase original.
  - **Facade**: Proporciona una interfaz simplificada y de alto nivel a un subsistema complejo de clases.
  - **Proxy**: Proporciona un objeto intermediario o sustituto para controlar el acceso a otro objeto (seguridad, caché, carga remota *lazy loading*).
  - **Flyweight**: Comparte eficientemente grandes cantidades de objetos de granularidad fina mediante estados intrínsecos compartidos.
- **3. Patrones de Comportamiento (Interacción y asignación de responsabilidades)**:
  - **Observer**: Define una dependencia uno-a-muchos entre objetos, de forma que cuando el sujeto cambia de estado, todos sus observadores son notificados automáticamente.
  - **Strategy**: Define una familia de algoritmos, encapsula cada uno y los hace intercambiables en tiempo de ejecución.
  - **Command**: Encapsula una petición como un objeto, permitiendo parametrizar clientes, poner peticiones en cola y soportar operaciones deshacer (*undo*).
  - **Iterator**: Proporciona un modo de acceder secuencialmente a los elementos de un objeto agregado sin exponer su estructura interna.
  - **State**: Permite a un objeto alterar su comportamiento cuando cambia su estado interno.
  - **Template Method**: Define el esqueleto de un algoritmo en una operación, difiriendo algunos pasos a las subclases.
  - **Chain of Responsibility, Mediator, Memento, Visitor, Interpreter**.
