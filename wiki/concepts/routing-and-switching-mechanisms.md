---
title: "Mecanismos de Conmutación (Switching) y Enrutamiento LAN"
type: "concept"
tags:
  - switching
  - routing
  - vlan
  - stp
  - lan
sources:
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Conmutación y Enrutamiento"
  - "Switching and Routing"
---

# Mecanismos de Conmutación (Switching) y Enrutamiento LAN

Los switches y routers constituyen los dispositivos activos fundamentales para el control de tráfico y segmentación en redes locales y corporativas.

---

## 🏛️ Conmutación de Nivel 2 y Protocolos STP

- **Tabla de Direcciones MAC (CAM Table)**: Los switches aprenden dinámicamente las direcciones MAC de origen de las tramas entrantes asociándolas a sus puertos físicos con un temporizador de envejecimiento (*Aging Time* de 300 s).
- **Protocolo Spanning Tree (STP - IEEE 802.1D)**:
  - Previene bucles de capa 2 y tormentas de broadcast en topologías redundantes bloqueando puertos lógicamente.
  - Elección del **Bridge Raíz (Root Bridge)**: Switch con el menor valor de **Bridge ID (BID)** (prioridad + MAC).
  - Estados de puerto STP: *Bloqueo (Blocking)* $\rightarrow$ *Escucha (Listening)* $\rightarrow$ *Aprendizaje (Learning)* $\rightarrow$ *Reenvío (Forwarding)*.
- **Rapid Spanning Tree Protocol (RSTP - IEEE 802.1w)**: Reduce el tiempo de convergencia de 30-50 segundos a unos pocos milisegundos mediante negociación de propuestas y acuerdos.

---

## 🧩 Segmentación con VLANs y Enrutamiento Inter-VLAN

- **VLANs (Virtual Local Area Networks - IEEE 802.1Q)**:
  - Dividen un switch físico en múltiples dominios de difusión lógicos aislados.
  - Etiqueta 802.1Q de **4 bytes**: Contiene el TPID (`0x8100`) y el **VLAN ID (12 bits: 1 a 4094)**.
  - Puertos de Acceso (*Access Ports* - sin etiquetar) vs. Puertos Troncales (*Trunk Ports* - etiquetados).
- **Enrutamiento Inter-VLAN**:
  - **Router-on-a-Stick**: Un único router conectado por un enlace troncal al switch mediante subinterfaces con encapsulación 802.1Q.
  - **Switch de Capa 3 (Multilayer Switch)**: Enrutamiento por hardware a velocidad de cable mediante interfaces virtuales de switch (**SVI**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar STP Clásico / RSTP | **IEEE 802.1D** / **IEEE 802.1w** |
| Tamaño Tag VLAN 802.1Q | **4 bytes** (VLAN ID de **12 bits**) |
| Rango de VLAN IDs | **1 a 4094** |
| Criterio Elección Root Bridge | **Menor Bridge ID (Prioridad + MAC)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Acceso al Medio]]
