---
title: "Test Tema 06: Arquitecturas Multicapa, Servicios Web SOAP y RESTful"
type: "test"
target: "wiki/sources/bloque3-tema06-arquitecturas-web-servicios.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 06: Arquitecturas Multicapa, Servicios Web SOAP y RESTful

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 06: Arquitecturas Multicapa, Servicios Web SOAP y RESTful",
  "questions": [
    {
      "question": "En el protocolo SOAP (Simple Object Access Protocol), ¿qué elemento XML es OBLIGATORIO dentro del elemento raíz <soap:Envelope>?",
      "options": [
        "<soap:Header>",
        "<soap:Body>",
        "<soap:Fault>",
        "<soap:Attachment>"
      ],
      "answer": "b",
      "explanation": "El elemento <soap:Body> es obligatorio en todo mensaje SOAP; <soap:Header> es opcional y <soap:Fault> solo va dentro del Body en caso de error."
    },
    {
      "question": "¿Cuál de las siguientes propiedades describe el principio de 'Idempotencia' en los métodos HTTP de una API RESTful?",
      "options": [
        "El método no produce efectos secundarios en el servidor (solo lectura).",
        "Ejecutar la petición múltiples veces de forma consecutiva produce exactamente el mismo resultado y estado en el servidor que ejecutarla una sola vez.",
        "El método siempre requiere autenticación OAuth 2.0.",
        "La respuesta debe almacenarse obligatoriamente en caché."
      ],
      "answer": "b",
      "explanation": "Un método es idempotente (GET, PUT, DELETE, HEAD) si múltiples ejecuciones idénticas dejan el servidor en el mismo estado."
    },
    {
      "question": "En una API RESTful bien diseñada, ¿cuál es el método HTTP semánticamente correcto para actualizar PARCIALMENTE un recurso existente?",
      "options": [
        "PUT",
        "POST",
        "PATCH",
        "OPTIONS"
      ],
      "answer": "c",
      "explanation": "PATCH aplica modificaciones parciales a un recurso; PUT reemplaza el recurso completo."
    },
    {
      "question": "¿Qué estándar de seguridad para servicios web SOAP define la inclusión de tokens de seguridad (ej. SAML, UsernameToken) y firma/cifrado XML en el encabezado del mensaje?",
      "options": [
        "WS-Security (WSS).",
        "WS-ReliableMessaging.",
        "WS-Addressing.",
        "JSON Web Token (JWT)."
      ],
      "answer": "a",
      "explanation": "WS-Security (OASIS) proporciona integridad, confidencialidad y autenticación en mensajes SOAP mediante XML Encryption y XML Signature."
    },
    {
      "question": "En el modelo de madurez de Richardson para APIs REST, ¿qué nivel representa el uso de 'HATEOAS' (Hypermedia as the Engine of Application State)?",
      "options": [
        "Nivel 0 (El pantano de POX).",
        "Nivel 1 (Recursos URI).",
        "Nivel 2 (Verbos HTTP).",
        "Nivel 3 (Controles Hipermedia / HATEOAS)."
      ],
      "answer": "d",
      "explanation": "El Nivel 3 (máxima madurez REST) incorpora hipermedios (enlaces HATEOAS) en las respuestas para guiar la navegación del cliente."
    }
  ]
}
```
