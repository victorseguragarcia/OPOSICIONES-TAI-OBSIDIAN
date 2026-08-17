---
title: "Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC"
type: "synthesis"
tags:
  - synthesis
  - email
  - smtp
  - pop3
  - imap
  - dkim
  - spf
  - dmarc
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Protocolos de Correo"
  - "Email Protocols Guide"
---

# Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC

Manual de referencia sobre la arquitectura de correo electrónico corporativo, flujo entre agentes y mecanismos criptográficos contra el phishing y spoofing.

---

## 🏛️ Flujo de Mensajería y Agentes

```
[ Emisor ]
    │ (MUA)
    ▼  [Puerto 587 TCP / STARTTLS]
[ MTA Origen ] (Postfix / Sendmail)
    │  Consulta DNS (Registros MX del dominio destino)
    ▼  [Puerto 25 TCP]
[ MTA Destino ] ──► [ MDA / Mail Store ] (Dovecot)
                          │
                          ▼  [Puerto 993 TCP (IMAPS) / 995 TCP (POP3S)]
                     [ Destinatario (MUA) ]
```

---

## 🧩 Seguridad y Autenticación del Remitente

1. **SPF (Sender Policy Framework - RFC 7208)**: Publica en DNS `TXT` las IPs autorizadas a enviar correos del dominio.
2. **DKIM (DomainKeys Identified Mail - RFC 6376)**: Añade firma criptográfica asimétrica en la cabecera validable con la clave pública en DNS `TXT`.
3. **DMARC (RFC 7489)**: Establece la política de alineación y rechazo (`p=none`, `p=quarantine`, `p=reject`) ante fallos de SPF/DKIM.

---

## 🎯 Datos Clave para Oposiciones TAI

- **Puertos**: SMTP Relay (**25**), Submission (**587**), SMTPS (**465**), POP3/POP3S (**110 / 995**), IMAP/IMAPS (**143 / 993**).
- **Formato Mensaje**: Cabeceras + Línea en blanco + Cuerpo + Finalización con `<CRLF>.<CRLF>`.
- **Extensiones MIME**: RFC 2045-2049 para contenido no ASCII y ficheros binarios.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
