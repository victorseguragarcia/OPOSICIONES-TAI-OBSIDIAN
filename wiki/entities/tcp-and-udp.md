---
title: "Protocolos de Transporte: TCP y UDP"
type: "entity"
tags:
  - tcp
  - udp
  - transport-layer
  - networking
  - protocols
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TCP"
  - "UDP"
  - "Capa de Transporte"
---

# Protocolos de Transporte: TCP y UDP

Protocolos fundamentales de la capa de transporte que gestionan la comunicación extremo a extremo entre procesos.

## TCP (Transmission Control Protocol)
- **Orientado a conexión**: Establecimiento mediante *Three-Way Handshake* (SYN ➔ SYN-ACK ➔ ACK) y cierre (FIN ➔ ACK).
- **Garantías**: Entrega ordenada, control de flujo por ventana deslizante (*Sliding Window*), control de congestión (Tahoe, Reno, CUBIC) y retransmisión por temporizador de ACK (ARQ).

## UDP (User Datagram Protocol)
- **No orientado a conexión**: Cabecera ultra-ligera de 8 bytes (Source Port, Dest Port, Length, Checksum).
- **Uso**: Aplicaciones en tiempo real sensibles al retardo y streaming (DNS, DHCP, VoIP, HTTP/3 QUIC).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Modelos: [[wiki/concepts/osi-and-tcp-ip-models|Modelos OSI y TCP-IP]]
- Web: [[wiki/entities/bgp-and-ospf|Protocolos OSPF y BGP]]

