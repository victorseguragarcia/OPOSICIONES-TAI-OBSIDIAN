---
title: "Protocolos de Enrutamiento Dinámico: OSPF y BGP"
type: "entity"
tags:
  - routing
  - ospf
  - bgp
  - networking
  - internet
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "OSPF"
  - "BGP"
  - "Dynamic Routing"
---

# Protocolos de Enrutamiento Dinámico: OSPF y BGP

Protocolos encargados de calcular las mejores rutas en topologías de red complejas mediante intercambio de información entre routers.

## OSPF (Open Shortest Path First)
- **Tipo**: IGP (Interior Gateway Protocol) de estado de enlace (*Link-State*).
- **Algoritmo**: Algoritmo de Dijkstra (SPF - Shortest Path First) con métrica de coste inversamente proporcional al ancho de banda.
- **Topología**: Organización jerárquica en Áreas centradas en el Área Troncal (Área 0 / Backbone Area).

## BGP (Border Gateway Protocol)
- **Tipo**: EGP (Exterior Gateway Protocol) de vector de caminos (*Path-Vector*).
- **Función**: Es el protocolo que interconecta los **Sistemas Autónomos (AS)** en el núcleo de Internet. Utiliza TCP puerto 179.
- **Toma de Decisiones**: Basada en atributos y políticas de enrutamiento (AS-Path, Local Preference, MED, Weight).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Arquitectura: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]

