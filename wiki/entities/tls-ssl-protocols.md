---
title: "Protocolos Criptográficos TLS y SSL"
type: "entity"
tags:
  - tls
  - ssl
  - cryptography
  - https
  - security
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TLS"
  - "SSL"
  - "TLS 1.3"
  - "HTTPS Encryption"
---

# Protocolos Criptográficos TLS y SSL

**Transport Layer Security (TLS)** es el estándar criptográfico sucesor de SSL que provee confidencialidad, integridad y autenticación sobre canales de comunicación en redes IP.

## Principios Criptográficos
- **Criptografía Asimétrica (Clave Pública)**: RSA o Curvas Elípticas (ECDHE) para el intercambio seguro de claves y autenticación mediante certificados digitales X.509.
- **Criptografía Simétrica**: Cifrado masivo de datos mediante AES-GCM o ChaCha20-Poly1305.
- **Integridad**: Funciones hash seguras (SHA-256 / SHA-384).

## Avances en TLS 1.3 (RFC 8446)
- Reducción del apretón de manos (*Handshake*) a 1 solo RTT (y soporte de 0-RTT para reconexiones).
- Eliminación de algoritmos obsoletos e inseguros (DES, 3DES, RC4, MD5, SHA-1, suites CBC).
- Cifrado obligatorio de la mayoría de mensajes del handshake.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Perímetro: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]]
- Correo: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]

