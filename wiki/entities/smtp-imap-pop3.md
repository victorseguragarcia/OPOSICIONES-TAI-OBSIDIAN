---
title: "Protocolos de Correo Electrónico: SMTP, IMAP y POP3"
type: "entity"
tags:
  - email
  - smtp
  - imap
  - pop3
  - protocols
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Protocolos de Correo"
  - "SMTP/POP3/IMAP"
---

# Protocolos de Correo Electrónico: SMTP, IMAP y POP3

Los protocolos de correo electrónico estructuran el transporte, entrega y sincronización de mensajes en redes IP.

---

## 🏛️ Comparativa Exhaustiva de Protocolos

| Protocolo | Función Principal | Puerto Plano | Puerto Seguro (SSL/TLS) | RFC Principal | Modelo Operativo |
|-----------|-------------------|--------------|-------------------------|---------------|------------------|
| **SMTP (Relay)** | Transferencia entre Servidores MTA | **25 TCP** | 25 con STARTTLS | RFC 5321 | *Push* (Envío) |
| **SMTP (Submission)** | Envío Cliente MUA a Servidor | **587 TCP** | 587 con STARTTLS | RFC 6409 | *Push* con Autenticación |
| **SMTPS (Legado)** | Envío directo sobre SSL | N/A | **465 TCP** | RFC 8314 | *Push* cifrado directo |
| **POP3** | Descarga de buzón al cliente | **110 TCP** | **995 TCP** (POP3S) | RFC 1939 | *Pull* (Descarga y borra) |
| **IMAP4** | Sincronización de carpetas en servidor | **143 TCP** | **993 TCP** (IMAPS) | RFC 3501 | *Sync* bidireccional |

---

## 🧩 Seguridad y Reputación de Dominio

1. **SPF (Sender Policy Framework - RFC 7208)**: Registro DNS `TXT` que autoriza qué IPs pueden enviar correos del dominio (ej. `v=spf1 ip4:192.0.2.1 include:_spf.google.com -all`).
2. **DKIM (DomainKeys Identified Mail - RFC 6376)**: Firma digital asimétrica en la cabecera `DKIM-Signature`; la clave pública se publica en DNS `TXT`.
3. **DMARC (RFC 7489)**: Política de alineación de SPF y DKIM con directivas: `p=none` (solo monitorizar), `p=quarantine` (a spam) o `p=reject` (rechazo total).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Valor Técnico |
|----------|---------------|
| Puerto SMTP Relay / Submission | **25 TCP** / **587 TCP** |
| Puertos Seguros IMAPS / POP3S | **993 TCP** / **995 TCP** |
| Finalización Cuerpo SMTP | Línea con un solo punto `<CRLF>.<CRLF>` |
| Códigos de Éxito / Error SMTP | `250 OK`, `354 Start mail input`, `550 User not found` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Síntesis: [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC]]
