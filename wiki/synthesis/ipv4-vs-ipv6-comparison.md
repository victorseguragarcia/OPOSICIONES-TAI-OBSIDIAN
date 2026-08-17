---
title: "Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - ipv4
  - ipv6
  - networking
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPv4 vs IPv6"
  - "Comparativa IP"
---

# Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6

Matriz comparativa de características técnicas entre el protocolo IPv4 tradicional y la siguiente generación IPv6.

## Matriz Técnica

| Característica | [[wiki/entities/ipv4-and-ipv6\|IPv4]] | [[wiki/entities/ipv4-and-ipv6\|IPv6]] |
| :--- | :--- | :--- |
| **Longitud de Dirección** | 32 bits (4 bytes) | 128 bits (16 bytes) |
| **Espacio de Direcciones** | $\sim 4.29 \times 10^9$ | $\sim 3.4 \times 10^{38}$ |
| **Formato de Notación** | Decimal con puntos (ej: `192.168.1.1`) | Hexadecimal con dos puntos (ej: `2001:db8::1`) |
| **Tamaño Cabecera Base** | Variable (20 a 60 bytes con opciones) | Fijo (40 bytes), opciones en cabeceras de extensión |
| **Checksum en Cabecera** | Sí (recalculado en cada salto de router) | No (eliminado para acelerar el reenvío) |
| **Fragmentación** | Realizada por el host origen y routers intermedios | Realizada **únicamente por el host emisor** |
| **Difusión (Broadcast)** | Soportado extensivamente mediante direcciones broadcast | **No existe broadcast**, reemplazado por Multicast |
| **Configuración Automática**| DHCPv4 o manual | SLAAC (Stateless Address Autoconfiguration) o DHCPv6 |

## Mecanismos de Transición
- **Dual-Stack**: Las interfaces de red operan pilas IPv4 e IPv6 simultáneamente.
- **Túneles (Tunneling)**: Encapsulación de paquetes IPv6 dentro de datagramas IPv4 (6to4, Teredo, ISATAP).
- **Traducción**: NAT64 / DNS64 para permitir a clientes IPv6 conectarse a servidores solo IPv4.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]

