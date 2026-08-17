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
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DNS"
  - "Domain Name System"
---

# Protocolo DNS (Domain Name System)

El **Domain Name System (DNS)** es una base de datos jerárquica y distribuida definida en **RFC 1034** y **RFC 1035** que traduce nombres de dominio legibles para humanos (FQDN) en direcciones IP numéricas.

---

## 🏛️ Operación y Puertos

- **Puerto Estándar**: **53 TCP y UDP**.
  - **UDP 53**: Consultas estándar de resolución (límite tradicional de 512 bytes, ampliable mediante **EDNS0** - RFC 6891).
  - **TCP 53**: Transferencias de zona completas (**AXFR**) o incrementales (**IXFR**) entre servidores primarios y secundarios, y respuestas que superan los 512 bytes sin EDNS0.
- **Tipos de Servidores**:
  - **Servidores Raíz (`.`)**: 13 direcciones IP lógicas (`a.root-servers.net` a `m.root-servers.net`) operadas por distintas entidades mediante Anycast.
  - **Servidores TLD**: Gestionan dominios de nivel superior (`.es`, `.com`, `.gob.es`).
  - **Servidores Autoritativos**: Poseen los registros definitivos de una zona.
  - **Servidores Recursivos / Resolvers**: Resuelven consultas iterando en la jerarquía y almacenan resultados en caché según el **TTL** (*Time to Live*).

---

## 🧩 Tipos de Registros DNS Críticos

| Registro | Tipo | Función |
|----------|------|---------|
| `A` | Host IPv4 | Asocia un FQDN a una dirección IPv4 de 32 bits |
| `AAAA` | Host IPv6 | Asocia un FQDN a una dirección IPv6 de 128 bits |
| `CNAME` | Canonical Name | Alias de un nombre a otro FQDN |
| `MX` | Mail Exchanger | Servidor de correo del dominio con prioridad numérica |
| `NS` | Name Server | Servidor autoritativo para la zona |
| `PTR` | Pointer | Resolución inversa (IP a FQDN) en zonas `in-addr.arpa` o `ip6.arpa` |
| `SOA` | Start of Authority | Metadatos de la zona: Servidor primario, email del admin, Serial, Refresh, Retry, Expire, TTL mínimo |
| `TXT` | Text Record | Texto arbitrario (usado por SPF, DKIM, DMARC) |
| `SRV` | Service Record | Localización de servicios (puerto, protocolo, peso, prioridad) en Active Directory |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto DNS | **53 TCP/UDP** |
| Servidores Raíz Lógicos | **13** (`A` a `M`) |
| RFCs Fundacionales | **RFC 1034** y **RFC 1035** |
| Seguridad DNS | **DNSSEC** (RFC 4033-4035) mediante firmas digitales RRSIG/DNSKEY |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/dhcp-protocol|Protocolo DHCP]]
