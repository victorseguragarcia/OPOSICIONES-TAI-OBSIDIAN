---
title: "Mecanismos de Conmutación (Switching) y Enrutamiento LAN"
type: "concept"
tags:
  - switching
  - routing
  - vlan
  - stp
  - lan
  - networking
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Switching"
  - "Conmutación LAN"
  - "VLAN y STP"
---

# Mecanismos de Conmutación (Switching) y Enrutamiento LAN

Tecnologías de reenvío de tramas en Capa 2 y paquetes en Capa 3 en redes de área local.

## Conmutación en Capa 2
- **Tabla CAM (Content Addressable Memory)**: Asocia direcciones MAC con puertos físicos mediante aprendizaje dinámico (*MAC Learning*).
- **VLANs (IEEE 802.1Q)**: Segmentación lógica de dominios de broadcast. Inserción de cabecera de 4 bytes con VLAN ID (1-4094).
- **STP / RSTP (IEEE 802.1D / 802.1w)**: Algoritmo de árbol de expansión que bloquea enlaces redundantes para evitar tormentas de broadcast causadas por bucles.

## Enrutamiento Inter-VLAN
- **Router-on-a-Stick**: Un router conectado al switch mediante un único enlace troncal con subinterfaces lógicas 802.1Q.
- **Switches Multicapa (Capa 3)**: Reenvío a velocidad de cable mediante interfaces virtuales de switch (SVI) y hardware ASIC especializado.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Protocolos LAN: [[wiki/entities/dhcp-protocol|Protocolo DHCP]] y [[wiki/entities/dns-protocol|Protocolo DNS]]

