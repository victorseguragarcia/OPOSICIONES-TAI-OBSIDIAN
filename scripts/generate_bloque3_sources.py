# -*- coding: utf-8 -*-
r"""
Script generador del temario oficial y notas fuente del Bloque 3 (TAI Oposiciones - Desarrollo de Sistemas).
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
# 1. RAW SOURCES BLOQUE 3 (Temas 01 al 06)
# ==============================================================================

RAW_SOURCES_B3 = {
    "raw/sources/bloque3-tema01.md": """---
title: "Bloque 3 - Tema 01: Ciclo de Vida del Software, Metodologías Ágiles y MÉTRICA Versión 3"
type: "raw-source"
topic: "ciclo-de-vida-metrica3"
date: "2026-08-17"
---

# Bloque 3 - Tema 01: Modelos de Ciclo de Vida, Metodologías de Desarrollo (Tradicionales y Ágiles) y MÉTRICA Versión 3

## 1. Modelos del Ciclo de Vida del Software
- **Modelo en Cascada Clásico (Royce, 1970)**: Secuencial y rígido. Fases: Análisis de requisitos $\\rightarrow$ Diseño $\\rightarrow$ Implementación $\\rightarrow$ Pruebas $\\rightarrow$ Despliegue y Mantenimiento. No permite retroceso fácil; los errores de requisitos se detectan muy tarde.
- **Modelo en V (Verificación y Validación)**: Establece una correspondencia directa y simétrica entre cada fase de desarrollo y su correspondiente fase de pruebas (Requisitos $\\leftrightarrow$ Pruebas de Aceptación, Diseño General $\\leftrightarrow$ Pruebas de Sistema, Diseño Detallado $\\leftrightarrow$ Pruebas de Integración, Codificación $\\leftrightarrow$ Pruebas Unitarias).
- **Modelo Prototipado**: Construcción rápida de maquetas y prototipos interactivos para clarificar requisitos ambiguos con el usuario.
- **Modelo en Espiral (Boehm, 1986)**: Ciclo iterativo guiado por el **análisis y gestión de riesgos**. Cuatro cuadrantes por ciclo: 1. Fijar objetivos y alternativas $\\rightarrow$ 2. Análisis y evaluación de riesgos $\\rightarrow$ 3. Desarrollo y verificación del producto $\\rightarrow$ 4. Planificación de la siguiente iteración.

## 2. Metodologías Ágiles
Basadas en el **Manifiesto Ágil (2001)**: Valora a los individuos y sus interacciones sobre los procesos y herramientas; software funcionando sobre documentación exhaustiva; colaboración con el cliente sobre negociación contractual; y respuesta al cambio sobre seguimiento de un plan.
- **Scrum**:
  - **Roles**: **Product Owner (PO)** (representa al negocio y prioriza el Product Backlog), **Scrum Master (SM)** (líder servicial que elimina impedimentos y vela por el marco Scrum) y **Developers / Equipo de Desarrollo** (autoorganizado y multifuncional).
  - **Artefactos**: **Product Backlog** (lista priorizada de requisitos/historias de usuario), **Sprint Backlog** (tareas seleccionadas para el Sprint) e **Incremento** (software potencialmente desplegable que cumple la *Definition of Done* - DoD).
  - **Eventos**: **Sprint** (contenedor de 1 a 4 semanas), **Sprint Planning** (planificación del trabajo), **Daily Scrum** (reunión diaria de sincronización de 15 minutos), **Sprint Review** (demostración del incremento al PO y *stakeholders*) y **Sprint Retrospective** (mejora continua del equipo).
- **Kanban**: Sistema visual de gestión de flujo de trabajo basado en tableros. Principios: visualización del flujo, **límite del trabajo en curso (WIP - Work In Progress)** y optimización del *Lead Time* y *Cycle Time*.
- **eXtreme Programming (XP - Kent Beck)**: Enfatiza la excelencia técnica. Prácticas: Programación en Parejas (*Pair Programming*), Desarrollo Guiado por Pruebas (**TDD - Test-Driven Development**), Integración Continua, Refactorización constante, Propiedad colectiva del código y entregas pequeñas (*small releases*).

## 3. Metodología MÉTRICA Versión 3 (MÉTRICA v3)
Metodología oficial de desarrollo de sistemas de información del Ministerio de Administraciones Públicas (MAP / actual Ministerio de Transformación Digital y Función Pública) para las Administraciones Públicas españolas. Abarca tanto el enfoque Estructurado como el Orientado a Objetos.

### Estructura de Procesos de MÉTRICA v3:
1. **Planificación de Sistemas de Información (PSI)**:
   - Objetivo: Definir el marco estratégico y la arquitectura global de sistemas de información que dé soporte a los objetivos de la organización.
   - Actividades: Iniciación del PSI, Definición de requisitos, Estudio de sistemas de información actuales, Diseño de la arquitectura de información, Selección de la arquitectura tecnológica y Plan de proyectos.
2. **Estudio de Viabilidad del Sistema (EVS)**:
   - Objetivo: Analizar las necesidades del negocio para proponer alternativas de solución técnica y organizativa, evaluando su viabilidad económica, técnica, legal y operativa.
   - Actividades: Establecimiento del alcance del sistema, Estudio de la situación actual, Definición de requisitos del sistema, Estudio de alternativas de solución, Valoración de alternativas y Selección de la solución.
3. **Análisis del Sistema de Información (ASI)**:
   - Objetivo: Obtener la especificación detallada del sistema (modelo lógico de datos y procesos o modelo de clases y casos de uso).
   - Actividades: Definición del sistema, Establecimiento de requisitos, Identificación de subsistemas, Análisis de casos de uso / procesos y Elaboración del modelo de datos / clases.
4. **Diseño del Sistema de Información (DSI)**:
   - Objetivo: Diseñar la arquitectura física del sistema, módulos, interfaces de usuario y esquemas de base de datos relacional u OO.
   - Actividades: Definición de la arquitectura tecnológica, Diseño de la arquitectura de soporte, Diseño de casos de uso / módulos, Diseño de la base de datos, Diseño de interfaces de usuario y Plan de pruebas.
5. **Construcción del Sistema de Información (CSI)**:
   - Objetivo: Codificación de componentes, generación del esquema físico de BD, ejecución de pruebas unitarias, pruebas de integración y pruebas del sistema, y elaboración de manuales (usuario y explotación).
6. **Implantación y Aceptación del Sistema (IAS)**:
   - Objetivo: Puesta en producción del sistema, migración y carga inicial de datos, formación de usuarios y pruebas de aceptación final por parte del cliente.

### Procesos de Soporte / Interfaces de MÉTRICA v3:
- **Gestión de Proyectos (GP)**.
- **Seguridad (SEG)** (alineada con Magerit y el Esquema Nacional de Seguridad).
- **Garantía de Calidad (GC)** (aseguramiento de la calidad de procesos y productos).
- **Gestión de la Configuración (GCF)**.
""",

    "raw/sources/bloque3-tema02.md": """---
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
""",

    "raw/sources/bloque3-tema03.md": """---
title: "Bloque 3 - Tema 03: Lenguajes de Programación, Plataforma Java y Control de Versiones con Git"
type: "raw-source"
topic: "lenguajes-java-git"
date: "2026-08-17"
---

# Bloque 3 - Tema 03: Lenguajes de Programación, Paradigmas, Plataforma Java / JVM y Control de Versiones Distribuido con Git

## 1. Paradigmas y Lenguajes de Programación
- **Imperativo / Estructurado**: Basado en secuencias de órdenes, instrucciones de control de flujo y estados mutables (C, Pascal).
- **Orientado a Objetos (POO)**: Basado en objetos que encapsulan estado y comportamiento (Java, C++, C#, Python).
- **Funcional**: Basado en funciones matemáticas puras sin efectos secundarios ni mutabilidad de variables (Haskell, Lisp, Scala, funciones Lambda en Java/Python).
- **Declarativo / Lógico**: Se describe el resultado deseado sin detallar el flujo de control paso a paso (SQL, Prolog).

## 2. La Plataforma Java y la Máquina Virtual (JVM)
- **Filosofía**: *"Write Once, Run Anywhere"* (WORA). El código fuente (`.java`) es compilado por `javac` a código intermedio multiplataforma denominado **Bytecode** (`.class`), ejecutado por la **JVM (Java Virtual Machine)**.
- **Componentes**:
  - **JDK (Java Development Kit)**: Herramientas de compilación, depuración y librerías para desarrolladores.
  - **JRE (Java Runtime Environment)**: Entorno mínimo para ejecutar aplicaciones Java (contiene la JVM y librerías estándar).
  - **JIT (Just-In-Time Compiler)**: Compila partes frecuentes de bytecode a código máquina nativo en tiempo de ejecución para máximo rendimiento.
- **Gestión de Memoria y Recolector de Basura (Garbage Collector - GC)**:
  - **Stack (Pila)**: Almacena referencias a objetos, llamadas a métodos y variables primitivas locales. Rápida y de gestión automática por ámbito.
  - **Heap (Montículo)**: Almacena todos los objetos e instancias creadas con `new`. Gestionado por el GC.
    - *Young Generation*: Eden y Survivor Spaces (S0/S1). Objetos nuevos; se limpian mediante *Minor GC*.
    - *Old Generation (Tenured)*: Objetos que han sobrevivido a varios ciclos de recolección; se limpian mediante *Major GC / Full GC*.
    - *Metaspace (desde Java 8)*: Memoria nativa para metadatos de clases (reemplazó al antiguo *PermGen*).
- **Tipos de Datos en Java**: Primitivos (byte, short, int, long, float, double, boolean, char) y por Referencia (Objetos, Arrays, Interfaces).
- **Frameworks Empresariales**: **Spring Framework** e **Inversión de Control (IoC) / Inyección de Dependencias (DI)**; **Spring Boot** para microservicios y APIs REST; **JPA (Java Persistence API) / Hibernate** para mapeo objeto-relacional (ORM).

## 3. Control de Versiones Distribuido con Git
Git es un sistema de control de versiones distribuido (DVCS) creado por Linus Torvalds en 2005. Cada desarrollador tiene un clon completo del repositorio local con todo el historial.
- **Las Tres Zonas de Git**:
  1. **Working Directory (Directorio de Trabajo)**: Archivos locales que se están editando.
  2. **Staging Area / Index (Área de Preparación)**: Zona intermedia donde se seleccionan los cambios antes de confirmar (`git add`).
  3. **Local Repository (Repositorio Local / `.git`)**: Base de datos de objetos y commits confirmados (`git commit`).
  - *Remote Repository*: Servidor remoto compartido (GitHub, GitLab, Bitbucket) sincronizado mediante `git push` y `git fetch/pull`.
- **Comandos Esenciales de Git**:
  - `git init`: Inicializa un nuevo repositorio local.
  - `git clone <url>`: Clona un repositorio remoto.
  - `git status` y `git diff`: Muestra el estado del árbol de trabajo y las diferencias.
  - `git add <archivo>` o `git add .`: Añade archivos al área de Staging.
  - `git commit -m "mensaje"`: Registra una instantánea de los cambios en el historial local.
  - `git branch <nombre>` / `git checkout -b <nombre>` / `git switch -c <nombre>`: Gestión de ramas.
  - `git merge <rama>`: Fusiona una rama en la rama actual creando un commit de merge (o *fast-forward*).
  - `git rebase <rama>`: Reescribe la base de la rama actual situándola sobre el extremo de otra rama, creando un historial lineal y limpio.
  - `git cherry-pick <commit-hash>`: Aplica un commit específico de otra rama en la rama actual.
  - `git stash` / `git stash pop`: Guarda temporalmente cambios sin confirmar en una pila auxiliar.
  - `git reset` (soft, mixed, hard) y `git revert` (crea un nuevo commit que deshace los cambios sin alterar el historial).
- **Modelo de Ramas GitFlow**:
  - `main` / `master` (código en producción).
  - `develop` (integración de desarrollo).
  - `feature/*` (nuevas características).
  - `release/*` (preparación de versiones).
  - `hotfix/*` (parches urgentes sobre producción).
""",

    "raw/sources/bloque3-tema04.md": """---
title: "Bloque 3 - Tema 04: Arquitecturas Web Multicapa, Servicios SOAP, RESTful y Microservicios"
type: "raw-source"
topic: "arquitecturas-web-servicios"
date: "2026-08-17"
---

# Bloque 3 - Tema 04: Arquitecturas de Aplicaciones Web Multicapa, Servicios Web SOAP, APIs RESTful y Microservicios

## 1. Arquitecturas Multicapa (N-Tier)
Separación lógica de responsabilidades en capas desacopladas e independientes:
1. **Capa de Presentación (Front-end / Tier 1)**: Interfaz de usuario interactiva ejecutada en el navegador web (HTML5, CSS3, JavaScript/TypeScript, frameworks SPA como Angular, React o Vue).
2. **Capa de Lógica de Negocio / Aplicación (Tier 2)**: Procesamiento central, reglas de validación y flujos de negocio (Java Spring Boot, Node.js, .NET Core, Python Django/FastAPI).
3. **Capa de Acceso a Datos / Persistencia (Tier 3)**: Almacenamiento y persistencia en Sistemas Gestores de Bases de Datos Relacionales (RDBMS: PostgreSQL, Oracle, MySQL, SQL Server) o NoSQL (MongoDB, Redis, Cassandra).

## 2. Servicios Web: SOAP vs REST

### 1. SOAP (Simple Object Access Protocol)
- Protocolo formal estandarizado por el W3C basado en mensajería **XML**.
- **Estructura del Mensaje SOAP**:
  - `Envelope`: Elemento raíz obligatorio que identifica el documento XML como un mensaje SOAP.
  - `Header`: Elemento opcional que contiene metadatos de autenticación, transacciones y enrutamiento.
  - `Body`: Elemento obligatorio que contiene la carga útil (*payload*) y la llamada a la función o datos de respuesta.
  - `Fault`: Sub-elemento del Body que describe errores y excepciones ocurridas durante el procesamiento.
- **Tecnologías Asociadas**:
  - **WSDL (Web Services Description Language)**: Documento XML formal que describe la interfaz del servicio, tipos de datos, operaciones disponibles, puertos y protocolos de transporte.
  - **UDDI (Universal Description, Discovery and Integration)**: Registro y catálogo de servicios web.
  - **WS-Security**: Estándar de seguridad a nivel de mensaje que soporta firma y cifrado XML.

### 2. REST (Representational State Transfer - Roy Fielding, 2000)
- Estilo arquitectónico basado en la infraestructura estándar de la web (**HTTP/HTTPS**) y orientado a **Recursos** identificados mediante **URIs** uniformes.
- **Principios y Restricciones REST**:
  1. **Cliente-Servidor**: Separación estricta de la interfaz de usuario de la persistencia de datos.
  2. **Sin Estado (Stateless)**: Cada petición del cliente debe contener toda la información necesaria para ser procesada; el servidor no almacena contexto de sesión del cliente entre peticiones.
  3. **Capacidad de Caché (Cacheable)**: Las respuestas deben definirse explícitamente como almacenables o no en caché mediante cabeceras HTTP (`Cache-Control`, `ETag`).
  4. **Sistema en Capas**: La arquitectura puede interponer proxies, balanceadores y pasarelas de forma transparente.
  5. **Interfaz Uniforme**: Identificación de recursos por URIs, manipulación mediante representaciones (**JSON** / XML), mensajes auto-descriptivos y **HATEOAS** (*Hypermedia As The Engine Of Application State*).
- **Verbos HTTP y Semántica**:
  - `GET`: Recupera un recurso (Seguro e Idempotente).
  - `POST`: Crea un nuevo recurso subordinado (No seguro, No idempotente).
  - `PUT`: Reemplaza completamente un recurso existente (Idempotente).
  - `PATCH`: Modificación parcial de un recurso (No necesariamente idempotente).
  - `DELETE`: Elimina un recurso (Idempotente).

## 3. Arquitecturas de Microservicios y Mensajería
- **Monolito vs Microservicios**: Los microservicios dividen una aplicación en un conjunto de servicios independientes, desplegables de forma autónoma, con su propia base de datos (*Database per Service*) y comunicados mediante APIs HTTP ligeras o colas de mensajería.
- **Patrones de Microservicios**:
  - **API Gateway**: Punto de entrada único que enruta peticiones, autentica clientes, balancea carga y agrega respuestas.
  - **Service Discovery**: Registro centralizado (Eureka, Consul) para localización dinámica de instancias de microservicios.
  - **Circuit Breaker (Cortocircuitos)**: Previene fallos en cascada cortando temporalmente llamadas a servicios caídos.
- **Mensajería Asíncrona (Brokers)**:
  - **RabbitMQ**: Broker AMQP con colas y enrutamiento por *exchanges*.
  - **Apache Kafka**: Plataforma distribuida de *streaming* de eventos de alto rendimiento basada en logs de eventos particionados y persistentes.
""",

    "raw/sources/bloque3-tema05.md": """---
title: "Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD"
type: "raw-source"
topic: "calidad-pruebas-cicd"
date: "2026-08-17"
---

# Bloque 3 - Tema 05: Calidad del Software, Niveles y Tipos de Pruebas (Caja Blanca / Negra), Complejidad de McCabe e Integración Continua (CI/CD)

## 1. Niveles y Tipos de Pruebas de Software
- **Niveles de Pruebas**:
  1. **Pruebas Unitarias**: Verifican el funcionamiento aislado de componentes individuales (métodos, clases). Automatizadas con frameworks como JUnit o NUnit.
  2. **Pruebas de Integración**: Verifican la interacción correcta y el intercambio de datos entre múltiples módulos o con servicios externos y bases de datos.
  3. **Pruebas de Sistema**: Evalúan el sistema completo e integrado respecto a los requisitos funcionales y no funcionales especificados.
  4. **Pruebas de Aceptación**: Realizadas por el usuario final o cliente (*Alpha testing* en entorno de desarrollo, *Beta testing* en entorno real) para validar que el software cumple las expectativas de negocio.
- **Otros Tipos de Pruebas**:
  - **Pruebas de Regresión**: Verifican que los cambios recientes o correcciones de bugs no hayan introducido nuevos errores en funcionalidades existentes.
  - **Pruebas No Funcionales**: Rendimiento, Carga, Estrés, Seguridad y Accesibilidad.

## 2. Técnicas de Diseño de Casos de Prueba

### 1. Pruebas de Caja Blanca (Estructurales)
Basadas en el conocimiento de la estructura interna y el código fuente del programa.
- **Criterios de Cobertura**:
  - *Cobertura de Sentencias / Instrucciones*: Garantiza que cada línea de código se ejecute al menos una vez.
  - *Cobertura de Decisiones / Ramas*: Garantiza que cada rama condicional (True y False) se evalúe al menos una vez.
  - *Cobertura de Condiciones*: Garantiza que cada condición booleana individual tome ambos valores.
  - *Cobertura de Caminos*: Garantiza que se ejecuten todos los caminos independientes posibles.
- **Complejidad Ciclomática de McCabe ($V(G)$)**:
  - Métrica de la ingeniería del software que mide la complejidad lógica de un programa y determina el **número mínimo de casos de prueba necesarios para garantizar la cobertura de todos los caminos básicos independientes**:
  $$V(G) = E - N + 2P$$
  Donde:
  - $E$ = Número de aristas (*Edges*) del grafo de flujo de control.
  - $N$ = Número de nodos (*Nodes*) del grafo.
  - $P$ = Número de componentes conexos ($P=1$ para un único programa/método).
  - *Fórmula Alternativa*: $V(G) = \text{Número de Nodos Predicado (Decisiones)} + 1$.
  - *Fórmula por Regiones*: $V(G) = \text{Número de Regiones del Grafo Plano}$.

### 2. Pruebas de Caja Negra (Funcionales)
Basadas en la especificación de requisitos sin conocer el código interno.
- **Particiones o Clases de Equivalencia**: Divide el dominio de entrada en subconjuntos de datos equivalentes (válidos e inválidos), seleccionando un caso representativo de cada clase.
- **Análisis de Valores Límite (BVA - Boundary Value Analysis)**: Se diseñan casos de prueba en los bordes extremos de las particiones (valor mínimo, justo por debajo del mínimo, justo por encima, valor máximo, justo por encima del máximo). Los errores suelen concentrarse en los límites de los rangos.
- **Tablas de Decisión** y **Pruebas de Transición de Estados**.

## 3. Integración y Despliegue Continuo (CI/CD) y Análisis Estático
- **Integración Continua (CI)**: Práctica de fusionar los cambios de código frecuentemente en una rama compartida, ejecutando automáticamente la compilación y la batería de pruebas unitarias/integración en cada commit.
- **Entrega Continua (Continuous Delivery)**: Automatiza el empaquetado del software para que cualquier versión probada esté lista para ser desplegada en producción con un clic manual.
- **Despliegue Continuo (Continuous Deployment)**: Automatiza el paso a producción de forma completamente desatendida tras superar con éxito todas las pruebas del pipeline.
- **Herramientas**: Jenkins, GitLab CI, GitHub Actions, Azure DevOps, ArgoCD.
- **Análisis Estático de Código (SonarQube)**: Inspección automatizada del código fuente sin ejecutarlo para detectar bugs, vulnerabilidades de seguridad (*Security Hotspots*), olores de código (*Code Smells*), duplicidades y calcular la **Deuda Técnica** (*Technical Debt*) frente a **Quality Gates**.
""",

    "raw/sources/bloque3-tema06.md": """---
title: "Bloque 3 - Tema 06: Accesibilidad Web, WCAG 2.1/2.2, EN 301 549 y RD 1112/2018"
type: "raw-source"
topic: "accesibilidad-wcag-rd1112"
date: "2026-08-17"
---

# Bloque 3 - Tema 06: Accesibilidad Web y Usabilidad, Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018

## 1. Concepto de Accesibilidad Web y W3C / WAI
La accesibilidad web implica que personas con discapacidad puedan percibir, entender, navegar e interactuar con la web, aportando al mismo tiempo contenidos. Desarrollada por la iniciativa **WAI (Web Accessibility Initiative)** del consorcio **W3C**.

## 2. Pautas de Accesibilidad para el Contenido Web (WCAG 2.1 / 2.2)
Las pautas WCAG se estructuran en **4 Principios Fundamentales (Acrónimo POUR)**:
1. **Perceptible**: La información y los componentes de la interfaz de usuario deben presentarse a los usuarios de modo que puedan percibirlos.
   - *Alternativas textuales* para contenido no textual (imágenes con atributo `alt`).
   - *Subtítulos y audiodescripción* para contenido multimedia temporal.
   - *Adaptable*: Contenido estructurado semánticamente (etiquetas HTML5 `header`, `nav`, `main`, `footer`, encabezados `h1-h6`).
   - *Distinguible*: Contraste de color adecuado (mínimo ratio **4.5:1** para texto normal y **3:1** para texto grande en nivel AA), tamaño de texto ajustable sin pérdida de contenido, y no usar el color como único medio visual.
2. **Operable**: Los componentes de la interfaz de usuario y la navegación deben ser manejables.
   - *Accesible por teclado*: Toda la funcionalidad disponible mediante teclado sin trampas de foco.
   - *Tiempo suficiente*: Permitir al usuario ajustar o desactivar límites de tiempo.
   - *Ataques y convulsiones*: No diseñar contenido que parpadee más de 3 veces por segundo.
   - *Navegable*: Enlaces con propósito claro, orden de foco lógico, mecanismos para saltar bloques repetitivos (*skip links*) y múltiples vías para localizar páginas.
   - *Modalidades de entrada*: Soporte para gestos táctiles simples sin movimientos complejos.
3. **Comprensible**: La información y el manejo de la interfaz de usuario deben ser comprensibles.
   - *Legible*: Declaración del idioma principal de la página (`<html lang="es">`).
   - *Predecible*: Las páginas operan de forma predecible sin cambios de contexto automáticos al recibir el foco.
   - *Ayuda a la entrada de datos*: Identificación y descripción clara de errores en formularios, sugerencias de corrección y confirmación previa en envíos legales o financieros.
4. **Robusto**: El contenido debe ser suficientemente robusto para ser interpretado de forma fiable por una amplia variedad de aplicaciones de usuario, incluidas las tecnologías de asistencia (lectores de pantalla como NVDA o JAWS).
   - Marcado HTML válido, elementos con etiquetas de inicio y fin correctas y soporte de atributos **WAI-ARIA** (`role`, `aria-label`, `aria-expanded`).

### Niveles de Conformidad WCAG:
- **Nivel A**: Requisitos mínimos básicos indispensables.
- **Nivel AA**: Nivel estándar exigido internacional y legalmente para administraciones públicas y sitios corporativos.
- **Nivel AAA**: Máximo nivel de accesibilidad especializada.

## 3. Marco Normativo de Accesibilidad en el Sector Público
- **Estándar Europeo EN 301 549**: Norma europea sobre requisitos de accesibilidad adecuados para la contratación pública de productos y servicios TIC en Europa (adopta los criterios de WCAG 2.1 nivel AA).
- **Real Decreto 1112/2018, de 7 de septiembre**: Sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles del sector público (transposición de la Directiva UE 2016/2102).
  - **Ámbito de Aplicación**: Toda la Administración Pública española (AGE, CCAA, Entidades Locales), organismos públicos, universidades públicas y empresas que gestionen servicios públicos.
  - **Nivel de Exigencia**: Obliga al cumplimiento del **Nivel AA de las WCAG** (mediante la norma EN 301 549).
  - **Obligaciones Principales**:
    - Publicar una **Declaración de Accesibilidad** periódicamente actualizada en cada sitio web y app móvil.
    - Establecer un **Mecanismo de Comunicación** para que los ciudadanos puedan presentar sugerencias, quejas y reclamaciones sobre accesibilidad.
    - Designar una **Unidad Responsable de Accesibilidad (URA)** encargada de garantizar el cumplimiento y remitir informes periódicos de seguimiento al Ministerio.
    - Revisiones periódicas de accesibilidad obligatorias (autoevaluaciones y auditorías externas).
"""
}

print("[*] Escribiendo 6 fuentes brutas de Desarrollo de Sistemas en raw/sources/bloque3-tema*.md...")
for path, content in RAW_SOURCES_B3.items():
    write_file(path, content)

print("[*] 6 fuentes brutas del Bloque 3 generadas exitosamente.")
