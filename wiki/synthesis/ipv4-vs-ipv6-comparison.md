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
  - "Comparativa IPv4 e IPv6"
---

# Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6

Matriz comparativa de características técnicas entre el protocolo IPv4 tradicional y la siguiente generación IPv6.

---

## 🏛️ Matriz de Características Técnicas

| Parámetro | IPv4 (RFC 791) | IPv6 (RFC 8200) |
|-----------|----------------|-----------------|
| **Tamaño de Dirección** | **32 bits (4 octetos)** | **128 bits (16 octetos)** |
| **Número Total de Direcciones** | $2^{32} \approx 4.29 \times 10^9$ | $2^{128} \approx 3.4 \times 10^{38}$ |
| **Notación Textual** | Decimal con puntos: `192.168.1.254` | Hexadecimal con dos puntos: `2001:db8::1` |
| **Tamaño Cabecera Base** | **20 a 60 bytes** (variable) | **40 bytes FIJOS** (procesamiento óptimo por hardware) |
| **Checksum en Cabecera** | Sí (debe recalcularse en cada router) | **No** (se delega la detección de errores a L2 y L4) |
| **Fragmentación** | Realizada por routers intermedios y emisor | **Exclusivamente por el host emisor** (PMTUD) |
| **Transmisión de Difusión** | **Broadcast** (`255.255.255.255`) | **Inexistente** (sustituido por Multicast optimizado) |
| **Tipos de Direccionamiento** | Unicast, Multicast, Broadcast | Unicast, Multicast, **Anycast** |
| **Mecanismo de Autoconfiguración** | Manual o mediante servidor DHCP | Manual, DHCPv6 o **SLAAC sin estado** (RFC 4862) |
| **Resolución de Direcciones (L2)** | Protocolo **ARP** (Broadcast) | **ICMPv6 Neighbor Discovery (NDP)** (Multicast) |
| **Seguridad (IPsec)** | Opcional | **Nativo y obligatorio por especificación** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
