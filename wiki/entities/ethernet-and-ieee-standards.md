---
title: "Estándares Ethernet y Familia IEEE 802"
type: "entity"
tags:
  - ethernet
  - ieee-802-3
  - ieee-802
  - lan
  - mac
sources:
  - "raw/sources/bloque4-tema06.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ethernet"
  - "IEEE 802.3"
  - "IEEE 802"
---

# Estándares Ethernet y Familia IEEE 802

La familia de estándares **IEEE 802** define las especificaciones de redes de área local (LAN) y metropolitana (MAN) en las capas física y de enlace de datos.

---

## 🏛️ Subcomités Clave de IEEE 802

- **IEEE 802.1**: Arquitectura general, gestión y puenteo (*Bridging*):
  - **802.1D**: Spanning Tree Protocol (STP).
  - **802.1w**: Rapid Spanning Tree Protocol (RSTP).
  - **802.1Q**: Etiquetado de VLANs (4 bytes añadidos, VLAN ID de 12 bits = 4094 VLANs).
  - **802.1X**: Control de acceso a la red basado en puertos (EAP/RADIUS).
- **IEEE 802.2**: Control de Enlace Lógico (LLC).
- **IEEE 802.3**: Redes Ethernet cableadas con CSMA/CD.
- **IEEE 802.11**: Redes inalámbricas WLAN (Wi-Fi).
- **IEEE 802.15**: Redes WPAN (Bluetooth 802.15.1, Zigbee 802.15.4).

---

## 🧩 Evolución de Estándares Ethernet (IEEE 802.3)

| Estándar | Nombre Comercial | Velocidad | Medio de Transmisión | Distancia Máxima |
|----------|------------------|-----------|----------------------|------------------|
| **10BASE-T** | Ethernet | 10 Mbps | Par trenzado Cat 3/5 | 100 m |
| **100BASE-TX** | Fast Ethernet | 100 Mbps | Par trenzado Cat 5 (2 pares) | 100 m |
| **1000BASE-T** | Gigabit Ethernet (802.3ab) | 1 Gbps | Par trenzado Cat 5e/6 (4 pares) | 100 m |
| **1000BASE-SX** | Gigabit Ethernet (802.3z) | 1 Gbps | Fibra Multimodo (850 nm) | 220 - 550 m |
| **1000BASE-LX** | Gigabit Ethernet (802.3z) | 1 Gbps | Fibra Monomodo (1310 nm) | 5 - 10 km |
| **10GBASE-T** | 10 Gigabit Ethernet (802.3an) | 10 Gbps | Par trenzado Cat 6A | 100 m |
| **10GBASE-SR** | 10 Gigabit Ethernet (802.3ae) | 10 Gbps | Fibra Multimodo (850 nm) | 300 m (OM3) |
| **10GBASE-LR** | 10 Gigabit Ethernet (802.3ae) | 10 Gbps | Fibra Monomodo (1310 nm) | 10 km |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Tamaño Trama Ethernet II | **64 bytes mínimo** / **1518 bytes máximo** (1522 bytes con 802.1Q) |
| MTU Estándar | **1500 bytes** |
| Protocolo Acceso Compartido | **CSMA/CD** (IEEE 802.3) |
| Longitud Dirección MAC | **48 bits (6 bytes)** |
| Tag VLAN IEEE 802.1Q | **4 bytes** (VLAN ID de 12 bits: 1 a 4094) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
