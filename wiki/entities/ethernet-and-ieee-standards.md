---
title: "Estándares Ethernet y Familia IEEE 802.3"
type: "entity"
tags:
  - ethernet
  - ieee-802-3
  - lan
  - networking
  - cables
sources:
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ethernet"
  - "IEEE 802.3"
  - "Fast Ethernet"
  - "Gigabit Ethernet"
---

# Estándares Ethernet y Familia IEEE 802.3

**Ethernet** es la tecnología dominante de red de área local cableada estandarizada en el grupo IEEE 802.3.

## Trama Ethernet II (802.3)
- **Preámbulo y SFD**: 8 bytes de sincronización.
- **Dirección MAC Destino / Origen**: 6 bytes cada una (OUI + serial fabricante).
- **EtherType / Longitud**: 2 bytes (ej: `0x0800` IPv4, `0x86DD` IPv6, `0x8100` VLAN 802.1Q).
- **Carga Útil (Payload)**: 46 a 1500 bytes (MTU estándar).
- **FCS (Frame Check Sequence)**: 4 bytes de verificación CRC-32.

## Método de Acceso CSMA/CD
- *Carrier Sense Multiple Access with Collision Detection*: Escuchar el medio antes de transmitir, detectar colisiones y aplicar retroceso exponencial aleatorio (*Exponential Backoff*). Obsoleto en redes conmutadas Full-Duplex modernas.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Métodos de Acceso]]

