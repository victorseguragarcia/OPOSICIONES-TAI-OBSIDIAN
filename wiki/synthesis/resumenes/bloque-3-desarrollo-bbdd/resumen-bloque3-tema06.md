---
title: "Resumen Exhaustivo Tema 06 (Bloque 3): Servicios Web y Arquitecturas Orientadas a Servicios (SOAP vs REST)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-06
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema06.md]]"
  - "[[wiki/sources/bloque3-tema06]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|⬅️ Tema 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|Tema 07 ➡️]]

# 🔴 Resumen Exhaustivo Tema 06 (Bloque 3): Servicios Web y Arquitecturas Orientadas a Servicios (SOAP vs REST)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 06**
> Conceptos de SOA, servicios web SOAP (WSDL, XML, SOAP Envelope/Header/Body, WS-Security) vs servicios RESTful (JSON, principios de Fielding, stateless, métodos HTTP GET/POST/PUT/PATCH/DELETE, códigos de estado HTTP), OpenAPI/Swagger, GraphQL y gRPC.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Arquitectura Orientada a Servicios (SOA) y Servicios Web
- **Principios SOA**: Acoplamiento débil (*loose coupling*), contratos estandarizados, reutilización, abstracción, componibilidad y descubribilidad mediante registros.
- **Servicios Web Basados en SOAP (Simple Object Access Protocol)**:
  - Protocolo formal basado exclusivamente en **XML** respaldado por el consorcio W3C.
  - *Estructura del Mensaje SOAP*:
    - `<soap:Envelope>`: Elemento raíz obligatorio que identifica el documento XML como mensaje SOAP.
    - `<soap:Header>`: Elemento opcional con metadatos (autenticación, transacciones, enrutamiento).
    - `<soap:Body>`: Elemento obligatorio con la carga útil (datos y llamadas a métodos) y el elemento `<soap:Fault>` para control de errores.
  - *WSDL (Web Services Description Language)*: Documento XML que describe el contrato formal del servicio (tipos de datos, operaciones/mensajes y endpoints).
  - *UDDI (Universal Description, Discovery, and Integration)*: Directorio/registro de publicación y búsqueda de servicios web.
  - *Estándares WS-**: WS-Security (cifrado y firma XML), WS-ReliableMessaging, WS-Addressing.

### 2. Servicios Web RESTful (Representational State Transfer)

| Criterio de Comparación | Servicios Web SOAP | Servicios Web REST (RESTful) |
|:---|:---|:---|
| **Naturaleza** | **Protocolo formal estricto** (W3C). | **Estilo arquitectónico** (Roy Fielding, 2000). |
| **Formato de Mensajes** | **Exclusivamente XML**. | Múltiples formatos: **JSON (dominante)**, XML, YAML, texto plano. |
| **Protocolo de Transporte** | Independiente (HTTP, HTTPS, SMTP, JMS, TCP). | Estrechamente ligado a **HTTP / HTTPS**. |
| **Definición de Contrato** | Formal mediante archivo **WSDL**. | Opcional/descriptivo mediante **OpenAPI / Swagger**. |
| **Manejo de Estado** | Puede ser con o sin estado. | Estrictamente **Stateless (Sin estado)** en el servidor. |
| **Seguridad** | WS-Security a nivel de mensaje y transporte. | HTTPS (TLS) a nivel de transporte, OAuth 2.0 y JWT a nivel de aplicación. |

- **Semántica de los Métodos HTTP en REST**:

| Verbo HTTP | Operación CRUD | ¿Es Seguro? *(No modifica estado)* | ¿Es Idempotente? *(Múltiples llamadas producen el mismo efecto)* |
|:---|:---:|:---:|:---:|
| **GET** | Read (Consultar recursos) | **SÍ** | **SÍ** |
| **POST** | Create (Crear nuevo recurso) | ❌ NO | ❌ **NO (Crea múltiples registros)** |
| **PUT** | Update / Replace (Reemplazar recurso completo) | ❌ NO | **SÍ** |
| **PATCH** | Partial Update (Modificar parcialmente un recurso) | ❌ NO | ❌ NO (habitualmente no idempotente) |
| **DELETE** | Delete (Eliminar recurso) | ❌ NO | **SÍ** |

- **Códigos de Estado HTTP Fundamentales de Examen**:
  - `200 OK`: Éxito en la petición.
  - `201 Created`: Recurso creado exitosamente (respuesta a `POST`).
  - `204 No Content`: Éxito pero sin cuerpo de respuesta (común en `DELETE`).
  - `400 Bad Request`: Petición mal formada o error de sintaxis en el cliente.
  - `401 Unauthorized`: Falta de autenticación (credenciales no enviadas o inválidas).
  - `403 Forbidden`: Autenticado pero sin permisos para acceder al recurso.
  - `404 Not Found`: Recurso no encontrado.
  - `500 Internal Server Error`: Error no controlado en el servidor.
  - `503 Service Unavailable`: Servidor sobrecargado o en mantenimiento temporal.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 06 (Bloque 3)**
> 1. **Idempotencia de Métodos HTTP**: `GET, PUT y DELETE` son **Idempotentes**; `POST` **NO es idempotente**.
> 2. **Código 401 vs 403**: `401 Unauthorized` significa *no autenticado* (quién eres); `403 Forbidden` significa *autenticado pero sin autorización/permisos* (no puedes pasar).
> 3. **Estructura SOAP**: El elemento `<soap:Fault>` va **DENTRO del `<soap:Body>`**, no como hijo directo de Envelope.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Métodos Idempotentes**: **G-P-D** $\rightarrow$ **G**ET, **P**UT, **D**ELETE.
> - **Estructura SOAP**: **E-H-B-F** $\rightarrow$ **E**nvelope $\rightarrow$ **H**eader $\rightarrow$ **B**ody $\rightarrow$ **F**ault.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema06|Fuente Oficial del Tema 06]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema06|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema06-arquitecturas-web-servicios|Test Tema 06]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|⬅️ Tema 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|Tema 07 ➡️]]
