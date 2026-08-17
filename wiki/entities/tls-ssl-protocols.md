---
title: "Protocolos TLS/SSL y Criptografía Web"
type: "entity"
tags:
  - tls
  - ssl
  - https
  - cryptography
  - security
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TLS"
  - "SSL"
  - "Transport Layer Security"
---

# Protocolos TLS/SSL y Criptografía Web

**TLS (Transport Layer Security)** es el protocolo criptográfico estándar que proporciona comunicaciones seguras a través de Internet, garantizando **confidencialidad**, **integridad** y **autenticación**.

---

## 🏛️ Evolución de Versiones y Seguridad

- **SSL 2.0 / 3.0**: Diseñados por Netscape (1995/1996). Vulnerables (POODLE) y completamente obsoletos.
- **TLS 1.0 / 1.1**: Deprecados por IETF en RFC 8996 (2021).
- **TLS 1.2 (RFC 5246)**: Estándar ampliamente desplegado con negociación en 2 viajes de ida y vuelta (2-RTT).
- **TLS 1.3 (RFC 8446 - 2018)**:
  - **Reducción de Latencia**: Negociación en **1-RTT** (primera conexión) y **0-RTT** (*Early Data* para reanudaciones).
  - **Depuración Criptográfica**: Eliminación total de suites débiles (DES, 3DES, RC4, MD5, SHA-1, suites CBC vulnerables a BEAST/Lucky13).
  - **PFS Obligatorio**: Obliga el uso de intercambio de claves Diffie-Hellman efímero (**ECDHE** / DHE), eliminando el intercambio estático con RSA.
  - Cifrado del certificado del servidor durante el handshake.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Especificación Técnica |
|---------|------------------------|
| Versión Actual Recomendada | **TLS 1.3 (RFC 8446)** |
| Latencia Handshake TLS 1.3 | **1-RTT** (0-RTT en reanudación) |
| Requisito PFS | **ECDHE** (Curvas elípticas efímeras) |
| Puerto HTTPS Estándar | **443 TCP** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
- Concepto: [[wiki/concepts/cryptography-and-digital-signatures|Criptografía Simétrica, Asimétrica y Firma Digital]]
