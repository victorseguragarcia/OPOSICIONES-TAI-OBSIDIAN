---
title: "Test Tema 08: Arquitectura de Internet, Protocolos Web y Servidores de Correo"
type: "test"
target: "wiki/sources/bloque4-tema08-internet-web-correo.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 08: Arquitectura de Internet, Protocolos Web y Servidores de Correo

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 08: Arquitectura de Internet, Protocolos Web y Servidores de Correo",
  "questions": [
    {
      "question": "¿Cuál es la principal mejora técnica introducida por el protocolo HTTP/2 (RFC 7540) frente a HTTP/1.1?",
      "options": [
        "Utiliza formato de texto plano y descarta el cifrado TLS.",
        "Formato binario, multiplexación de múltiples peticiones/respuestas sobre una única conexión TCP y compresión de cabeceras HPACK.",
        "Elimina el uso de puertos TCP pasando a utilizar UDP exclusivamente.",
        "No requiere servidor DNS."
      ],
      "answer": "b",
      "explanation": "HTTP/2 es binario, multiplexado (elimina bloqueo de cabeza de línea HTTP) y comprime cabeceras con HPACK."
    },
    {
      "question": "¿En qué puertos TCP estándar operan respectivamente los protocolos de correo IMAPS (IMAP seguro con TLS implícito) y POP3S (POP3 seguro con TLS implícito)?",
      "options": [
        "IMAPS: 993 \\| POP3S: 995",
        "IMAPS: 143 \\| POP3S: 110",
        "IMAPS: 587 \\| POP3S: 465",
        "IMAPS: 25 \\| POP3S: 80"
      ],
      "answer": "a",
      "explanation": "IMAPS usa puerto 993; POP3S usa puerto 995. (Sus versiones sin cifrar son IMAP 143 y POP3 110)."
    },
    {
      "question": "¿Qué mecanismo de seguridad en correo electrónico permite al dominio remitente publicar en el DNS qué direcciones IP están autorizadas a enviar correos en su nombre?",
      "options": [
        "SPF (Sender Policy Framework - Registro TXT).",
        "DKIM (DomainKeys Identified Mail).",
        "DMARC.",
        "STARTTLS."
      ],
      "answer": "a",
      "explanation": "SPF (registro DNS TXT) lista las IPs autorizadas para enviar correo del dominio para prevenir spoofing."
    },
    {
      "question": "¿Qué código de estado HTTP devuelve un servidor web cuando un cliente solicita un recurso para el cual no dispone de permisos suficientes incluso estando autenticado?",
      "options": [
        "401 Unauthorized.",
        "403 Forbidden.",
        "404 Not Found.",
        "405 Method Not Allowed."
      ],
      "answer": "b",
      "explanation": "403 Forbidden indica que el servidor entiende la petición pero se niega a autorizar el acceso; 401 indica falta de autenticación válida."
    },
    {
      "question": "¿Qué protocolo de transporte y cifrado utiliza HTTP/3 para resolver el bloqueo de cabeza de línea a nivel de transporte y acelerar el *handshake* a 0-RTT?",
      "options": [
        "TCP con TLS 1.2.",
        "QUIC sobre UDP con TLS 1.3 integrado.",
        "SCTP sobre IP.",
        "IPSec ESP."
      ],
      "answer": "b",
      "explanation": "HTTP/3 opera sobre QUIC (Quick UDP Internet Connections) con TLS 1.3 nativo, eliminando el bloqueo de cabeza de línea de TCP."
    }
  ]
}
```
