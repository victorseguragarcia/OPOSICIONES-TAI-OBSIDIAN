---
title: "Guía de Códigos de Estado, Métodos y Cabeceras HTTP para TAI"
type: "synthesis"
tags:
  - synthesis
  - http
  - web
  - status-codes
  - headers
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Códigos de Estado HTTP"
  - "HTTP Status Codes Guide"
---

# Guía de Códigos de Estado, Métodos y Cabeceras HTTP para TAI

Compendio exhaustivo de métodos, clases de códigos de respuesta y cabeceras del protocolo HTTP (RFC 9110 / 9112).

---

## 🏛️ Métodos HTTP (Verbos)

- **Idempotencia**: Un método es idempotente si ejecutarlo múltiples veces con los mismos parámetros produce el mismo estado en el servidor.
- **Seguridad**: Un método es seguro si no altera el estado del recurso en el servidor (solo lectura).

| Método | Función | ¿Seguro? | ¿Idempotente? |
|--------|---------|----------|---------------|
| `GET` | Recuperar una representación del recurso especificado | **Sí** | **Sí** |
| `HEAD` | Idéntico a GET pero el servidor devuelve **solo las cabeceras** (sin cuerpo) | **Sí** | **Sí** |
| `POST` | Enviar datos para ser procesados por el recurso (creación subordinada) | No | **No** |
| `PUT` | Reemplazar completamente el recurso destino con la carga útil enviada | No | **Sí** |
| `DELETE` | Eliminar el recurso especificado | No | **Sí** |
| `PATCH` | Aplicar modificaciones parciales al recurso | No | No (puede serlo según implementación) |
| `OPTIONS`| Describir las opciones de comunicación permitidas por el servidor (CORS) | **Sí** | **Sí** |
| `TRACE` | Eco de la petición para diagnóstico (prohibido por seguridad XST) | **Sí** | **Sí** |
| `CONNECT`| Establecer un túnel bidireccional TCP a través de un proxy (usado en HTTPS) | No | No |

---

## 🔢 Códigos de Estado HTTP por Clases

### 1xx: Informativos (Petición recibida, proceso en curso)
- `100 Continue`: El cliente puede continuar enviando el cuerpo de la petición.
- `101 Switching Protocols`: El servidor acepta cambiar de protocolo (ej. actualización a WebSocket).
- `103 Early Hints`: Retorna cabeceras anticipadas mientras el servidor procesa la respuesta.

### 2xx: Éxito (Petición recibida, entendida y aceptada con éxito)
- `200 OK`: Petición exitosa estándar.
- `201 Created`: Petición completada y nuevo recurso creado (común tras `POST`/`PUT`).
- `202 Accepted`: Petición aceptada para procesamiento, pero no completada aún (asíncrona).
- `204 No Content`: Petición exitosa pero el servidor no devuelve cuerpo (común tras `DELETE`).
- `206 Partial Content`: El servidor entrega solo una parte del recurso solicitada por cabecera `Range`.

### 3xx: Redirección (Acción adicional requerida para completar la petición)
- `301 Moved Permanently`: El recurso ha sido movido permanentemente a una nueva URI.
- `302 Found`: Redirección temporal tradicional (los navegadores solían cambiar `POST` a `GET`).
- `304 Not Modified`: El recurso no ha cambiado desde la fecha indicada en `If-Modified-Since` (usa caché).
- `307 Temporary Redirect`: Redirección temporal que **garantiza que el método HTTP no cambiará**.
- `308 Permanent Redirect`: Redirección permanente que **garantiza que el método HTTP no cambiará**.

### 4xx: Errores del Cliente (Sintaxis errónea o petición no autorizada)
- `400 Bad Request`: Sintaxis de la petición inválida o corrupta.
- `401 Unauthorized`: Autenticación requerida (falta cabecera `Authorization` válida).
- `403 Forbidden`: El servidor entiende la petición pero **se niega a autorizarla** (permisos denegados).
- `404 Not Found`: El recurso solicitado no se encuentra en el servidor.
- `405 Method Not Allowed`: El método HTTP utilizado no está permitido para este recurso.
- `408 Request Timeout`: El servidor agotó el tiempo de espera de la petición del cliente.
- `409 Conflict`: Conflicto en el estado actual del recurso (ej. colisión de edición).
- `410 Gone`: El recurso ya no está disponible y no se conoce dirección de reenvío (permanente).
- `413 Payload Too Large`: La petición enviada supera el límite de tamaño fijado por el servidor.
- `415 Unsupported Media Type`: El formato del contenido no es soportado (`Content-Type`).
- `429 Too Many Requests`: El cliente ha superado el límite de peticiones (*Rate Limiting*).

### 5xx: Errores del Servidor (El servidor falló al intentar procesar una petición válida)
- `500 Internal Server Error`: Error genérico no controlado en el servidor.
- `501 Not Implemented`: El servidor no soporta la funcionalidad requerida para procesar la petición.
- `502 Bad Gateway`: El servidor, actuando como proxy/gateway, recibió una respuesta inválida del backend.
- `503 Service Unavailable`: Servidor sobrecargado o en mantenimiento temporal.
- `504 Gateway Timeout`: El proxy/gateway no recibió respuesta a tiempo del servidor upstream.
- `505 HTTP Version Not Supported`: La versión de HTTP de la petición no está soportada.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Código / Definición |
|----------|---------------------|
| Petición Exitosa Sin Cuerpo | **`204 No Content`** |
| Caché No Modificada | **`304 Not Modified`** |
| Redirección Permanente Estricta | **`308 Permanent Redirect`** |
| Error Autenticación vs Permisos | **`401 Unauthorized`** (quién eres) vs **`403 Forbidden`** (no tienes permiso) |
| Error Gateway Caído / Timeout | **`502 Bad Gateway`** / **`504 Gateway Timeout`** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
