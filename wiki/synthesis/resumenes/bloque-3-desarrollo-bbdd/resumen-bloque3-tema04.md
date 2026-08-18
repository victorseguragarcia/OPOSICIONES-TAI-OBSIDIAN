---
title: "Resumen Exhaustivo Tema 04 (Bloque 3): Arquitectura de Software y Plataformas Empresariales (Java EE, .NET)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-04
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema04.md]]"
  - "[[wiki/sources/bloque3-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|Tema 05 ➡️]]

# 🔴 Resumen Exhaustivo Tema 04 (Bloque 3): Arquitectura de Software y Plataformas Empresariales (Java EE, .NET)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 04**
> Patrones de arquitectura (Monolito, Modelo en Capas, MVC, Microservicios, SOA, Arquitectura Hexagonal/Ports & Adapters), plataforma Java EE / Jakarta EE (EJB, JPA, Servlets, JSP, CDI, JAX-RS), plataforma .NET (.NET Core, ASP.NET Core, Entity Framework Core) y servidores de aplicaciones.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Patrones Arquitectónicos de Software
- **Arquitectura en Capas (N-Tier)**: Capa de Presentación (UI), Capa de Lógica de Negocio (Servicios) y Capa de Acceso a Datos (Persistencia / DAO).
- **Patrón MVC (Model-View-Controller)**:
  - *Modelo*: Encapsula el estado de la aplicación, datos y reglas de negocio.
  - *Vista*: Renderiza la interfaz de usuario y presenta los datos del modelo.
  - *Controlador*: Recibe las peticiones del usuario, invoca los servicios del modelo y selecciona la vista de respuesta.
- **Monolito vs Microservicios**:
  - *Monolito*: Todo el sistema se compila y despliega como un único artefacto ejecutable (`.war`, `.ear`, binario).
  - *Microservicios*: Descomposición en servicios independientes, desacoplados, autónomos y desplegables de forma independiente, comunicados mediante APIs REST, gRPC o colas de mensajería (RabbitMQ, Kafka).
- **Arquitectura Hexagonal (Ports and Adapters)**: Aisla la lógica de negocio central de las dependencias externas (bases de datos, frameworks, UI) mediante Puertos (interfaces) y Adaptadores.

### 2. Plataforma Java EE / Jakarta EE
- **Especificaciones Clave**:
  - *Servlets*: Componentes Java del lado del servidor que procesan peticiones HTTP (`HttpServlet`, métodos `doGet`, `doPost`).
  - *JSP (JavaServer Pages)*: Páginas HTML combinadas con código Java compiladas internamente como Servlets.
  - *EJB (Enterprise JavaBeans)*: Componentes de negocio gestionados por el contenedor (Session Beans: *Stateless*, *Stateful*, *Singleton*; Message-Driven Beans - MDB para mensajería asíncrona JMS).
  - *JPA (Java Persistence API / Jakarta Persistence)*: Estándar ORM de persistencia de datos (implementaciones: Hibernate, EclipseLink). Utiliza consultas JPQL y `EntityManager`.
  - *JAX-RS*: Especificación para servicios REST (`@Path`, `@GET`, `@POST`, `@Produces`).
- **Servidores de Aplicaciones Web**: Tomcat / Jetty (contenedores de servlets puros) vs WildFly / Payara / WebLogic / WebSphere (servidores Java EE completos).

### 3. Plataforma Microsoft .NET (.NET Core / Modern .NET)
- **Componentes Fundamentales**:
  - *CLR (Common Language Runtime)*: Motor de ejecución que gestiona la memoria (Garbage Collector), hilos y seguridad.
  - *CIL / MSIL (Common Intermediate Language)*: Código intermedio generado por los compiladores (C#, F#, VB.NET) que el compilador JIT (*Just-In-Time*) convierte a código máquina nativo.
  - *ASP.NET Core*: Framework web multiplataforma de alto rendimiento para APIs REST y aplicaciones web.
  - *Entity Framework Core (EF Core)*: Framework ORM para .NET (soporta enfoques *Code-First* y *Database-First*).

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 04 (Bloque 3)**
> 1. **Tomcat vs WildFly**: Apache Tomcat es un **contenedor de Servlets/JSP** (no es un servidor Java EE completo; no soporta EJBs de forma nativa sin extensiones como TomEE).
> 2. **Tipos de Session Beans en EJB**: Son 3 (**Stateless** sin estado, **Stateful** mantiene estado entre peticiones del mismo cliente, **Singleton** una única instancia global).
> 3. **Código Intermedio en .NET**: Los compiladores de C# no generan código máquina directo, sino **CIL/MSIL** que es interpretado y compilado por el **CLR via JIT**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Tipos Session Beans**: **3S** $\rightarrow$ **S**tateless, **S**tateful, **S**ingleton.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema04|Fuente Oficial del Tema 04]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema04|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema04-poo-patrones-uml|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|Tema 05 ➡️]]
