---
title: "Protocolo DHCP (Dynamic Host Configuration Protocol)"
type: "entity"
tags:
  - dhcp
  - networking
  - protocols
  - lan
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DHCP"
  - "Dynamic Host Configuration Protocol"
---

# Protocolo DHCP (Dynamic Host Configuration Protocol)

**DHCP** es un protocolo cliente-servidor (UDP puertos 67 y 68) que automatiza la asignación dinámica de parámetros de red a dispositivos en una LAN.

## Proceso de Asignación DORA
1. **Discover** (Cliente ➔ Broadcast `255.255.255.255`): El cliente solicita configuración IP.
2. **Offer** (Servidor ➔ Unicast/Broadcast): El servidor ofrece una IP con tiempo de concesión (*lease time*).
3. **Request** (Cliente ➔ Broadcast): El cliente acepta formalmente la oferta elegida.
4. **Acknowledge** (Servidor ➔ Unicast/Broadcast): Confirmación final con máscara, puerta de enlace y servidores DNS.

## Parámetros Clave
- **Lease Time**: Tiempo de validez del alquiler IP antes de renovación (T1 al 50%, T2 al 87.5%).
- **DHCP Relay Agent**: Reenvía peticiones DHCP entre subredes a través de routers (Opción 82).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Nombres: [[wiki/entities/dns-protocol|Protocolo DNS]]
- Conmutación: [[wiki/concepts/routing-and-switching-mechanisms|Enrutamiento y Conmutación]]

