---
title: "Protocolos de Correo Electrónico: SMTP, IMAP y POP3"
type: "entity"
tags:
  - email
  - smtp
  - imap
  - pop3
  - protocols
  - networking
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SMTP"
  - "IMAP"
  - "POP3"
  - "Servidores de Correo"
---

# Protocolos de Correo Electrónico: SMTP, IMAP y POP3

La arquitectura de correo electrónico estándar define agentes especializados (MUA, MTA, MDA) comunicados mediante protocolos de aplicación específicos.

## Protocolos de Transporte y Acceso
| Protocolo | Puerto Estándar | Puerto Seguro (TLS) | Función |
| :--- | :--- | :--- | :--- |
| **SMTP** (Simple Mail Transfer Protocol) | 25 / 587 | 465 (SMTPS) | Envío y retransmisión entre servidores (MTA a MTA). |
| **IMAP4** (Internet Message Access Protocol) | 143 | 993 (IMAPS) | Consulta y sincronización bidireccional en servidor. |
| **POP3** (Post Office Protocol) | 110 | 995 (POP3S) | Descarga local de mensajes desde el servidor. |

## Seguridad y Mecanismos Antispam
- **SPF (Sender Policy Framework)**: Registro DNS TXT que declara IPs autorizadas para enviar correos desde un dominio.
- **DKIM (DomainKeys Identified Mail)**: Firma criptográfica en cabeceras validada con clave pública en DNS.
- **DMARC**: Política que define la acción a tomar si SPF o DKIM fallan (none, quarantine, reject).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Seguridad Criptográfica: [[wiki/entities/tls-ssl-protocols|Protocolos TLS y SSL]]

