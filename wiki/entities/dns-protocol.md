---
title: "Protocolo DNS (Domain Name System)"
type: "entity"
tags:
  - dns
  - networking
  - protocols
  - infrastructure
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DNS"
  - "Domain Name System"
  - "Servidores DNS"
---

# Protocolo DNS (Domain Name System)

El **Domain Name System (DNS)** es una base de datos jerárquica y distribuida que traduce nombres de dominio legibles para humanos en direcciones IP binarias.

## Jerarquía y Tipos de Servidores
- **Root Servers**: 13 servidores raíz nombrados de la A a la M.
- **TLD Servers**: Gestionan dominios de nivel superior (`.es`, `.com`, `.gob.es`).
- **Servidores Autoritativos**: Contienen los registros oficiales de una zona.
- **Servidores Recursivos (Resolvers)**: Realizan la búsqueda iterativa en nombre del cliente.

## Tipos de Registros DNS Críticos
- `A` (IPv4) / `AAAA` (IPv6): Mapeo nombre a dirección IP.
- `CNAME`: Alias canónico hacia otro nombre de dominio.
- `MX`: Servidores de intercambio de correo con prioridad.
- `PTR`: Registro de resolución inversa (IP a nombre).
- `NS`: Servidor autoritativo de la zona.
- `TXT`: Registros de texto (usados por SPF, DKIM, verificación de dominio).

## Seguridad DNS
- **DNSSEC**: Firma digital de registros DNS para evitar envenenamiento de caché (DNS Cache Poisoning / Spoofing).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Correo: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
- Direccionamiento: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]

