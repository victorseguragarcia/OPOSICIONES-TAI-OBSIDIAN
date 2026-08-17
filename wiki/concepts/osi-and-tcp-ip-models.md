---
title: "Modelos Arquitectónicos ISO-OSI y TCP-IP"
type: "concept"
tags:
  - osi-model
  - tcp-ip
  - networking-models
  - encapsulation
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelo OSI"
  - "Modelo TCP-IP"
  - "Capas de Red"
---

# Modelos Arquitectónicos ISO-OSI y TCP-IP

Estructuras de referencia estratificadas para la estandarización de las comunicaciones entre sistemas heterogéneos.

## Comparativa de Capas
| Capa OSI (7 Niveles) | Capa TCP/IP (4 Niveles) | PDU (Protocol Data Unit) | Protocolos Representativos |
| :--- | :--- | :--- | :--- |
| **7. Aplicación** | **Aplicación** | Datos | HTTP, DNS, SMTP, SSH, FTP |
| **6. Presentación** | **Aplicación** | Datos | TLS/SSL, ASCII, JPEG, JSON |
| **5. Sesión** | **Aplicación** | Datos | RPC, NetBIOS, Sockets |
| **4. Transporte** | **Transporte** | Segmento (TCP) / Datagrama (UDP) | [[wiki/entities/tcp-and-udp\|TCP, UDP]] |
| **3. Red** | **Internet** | Paquete / Datagrama IP | [[wiki/entities/ipv4-and-ipv6\|IPv4, IPv6]], ICMP, [[wiki/entities/bgp-and-ospf\|OSPF, BGP]] |
| **2. Enlace de Datos**| **Acceso a Red** | Trama (*Frame*) | [[wiki/entities/ethernet-and-ieee-standards\|Ethernet (802.3)]], Wi-Fi (802.11), PPP |
| **1. Física** | **Acceso a Red** | Bits | Cables UTP, Fibra Óptica, Radio |

## Concepto de Encapsulación
A medida que los datos descienden por las capas del emisor, cada nivel añade su propia cabecera (*Header*) y pie (*Trailer*), convirtiéndose en la PDU del nivel inferior.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Síntesis: [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa Detallada OSI vs TCP-IP]]
- Protocolos IP: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]

