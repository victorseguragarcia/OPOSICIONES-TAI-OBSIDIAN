---
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
