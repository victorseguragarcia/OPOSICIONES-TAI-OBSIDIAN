---
title: "Topologías LAN y Métodos de Control de Acceso al Medio (MAC)"
type: "concept"
tags:
  - lan-topologies
  - mac
  - csma-cd
  - csma-ca
  - ethernet
sources:
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Topologías LAN"
  - "Métodos de Acceso MAC"
---

# Topologías LAN y Métodos de Control de Acceso al Medio (MAC)

Organización geométrica de nodos y protocolos de compartición de canales de difusión en redes de área local.

## Topologías de Red
- **Estrella**: Todos los nodos se conectan a un dispositivo central (switch/concentrador). Tolera fallos en cables individuales.
- **Árbol (Jerárquica)**: Estructura de niveles (Acceso, Distribución, Núcleo) estándar en redes corporativas.
- **Malla Completa / Parcial**: Múltiples rutas redundantes entre nodos. Utilizada en centros de datos y backbones de telecomunicaciones.

## Métodos de Acceso al Medio
- **CSMA/CD (Acceso Múltiple por Detección de Portadora con Detección de Colisiones)**: Utilizado en redes cableadas Ethernet compartidas.
- **CSMA/CA (con Prevención de Colisiones)**: Utilizado en redes inalámbricas Wi-Fi (802.11) mediante tramas RTS/CTS (*Request to Send / Clear to Send*).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Estándar: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet e IEEE 802.3]]

