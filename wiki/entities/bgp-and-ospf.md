---
title: "Protocolos de Enrutamiento Dinámico: OSPF y BGP"
type: "entity"
tags:
  - routing
  - ospf
  - bgp
  - networking
  - protocols
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "OSPF"
  - "BGP"
  - "Protocolos de Enrutamiento"
---

# Protocolos de Enrutamiento Dinámico: OSPF y BGP

El enrutamiento dinámico permite a los routers intercambiar información de topología de red para calcular automáticamente las mejores rutas hacia cada destino.

---

## 🏛️ Comparativa: OSPF vs BGP

| Característica | OSPF (RFC 2328) | BGPv4 (RFC 4271) |
|----------------|-----------------|------------------|
| **Tipo de Protocolo** | **IGP** (Interior Gateway Protocol) | **EGP** (Exterior Gateway Protocol) |
| **Algoritmo** | **Estado de Enlace** (*Link-State* - Dijkstra SPF) | **Vector de Caminos** (*Path-Vector*) |
| **Ámbito** | Dentro de un único Sistema Autónomo (AS) | Interconexión entre distintos Sistemas Autónomos |
| **Protocolo de Transporte** | Encapsulado directo en **IP (Protocolo 89)** | Sesión sobre **TCP (Puerto 179)** |
| **Métrica Principal** | **Coste** ($\text{Coste} = \text{Ancho de Banda de Referencia} / \text{Ancho de Banda del Enlace}$) | Atributos de ruta (**AS-PATH**, Local Preference, MED, Weight) |
| **Estructura Jerárquica** | Jerarquía de Áreas (Área `0` / *Backbone Area*) | Sistemas Autónomos identificados por números **ASN** |
| **Convergencia** | Ultrarrápida | Diseñado para estabilidad y políticas de tráfico global |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto / Protocolo OSPF | **Protocolo IP 89** (Multicast `224.0.0.5` y `224.0.0.6`) |
| Puerto / Protocolo BGP | **Puerto 179 TCP** |
| Algoritmo OSPF | **Dijkstra** (SPF - Shortest Path First) |
| Área Backbone OSPF | **Área 0** (`0.0.0.0`) |
| Prevención Bucles BGP | Atributo **AS-PATH** (descarta rutas que contengan su propio ASN) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Concepto: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
