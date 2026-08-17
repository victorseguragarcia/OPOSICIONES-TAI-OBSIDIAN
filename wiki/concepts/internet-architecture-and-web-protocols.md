---
title: "Arquitectura de Internet y Protocolos Web (HTTP/1-3)"
type: "concept"
tags:
  - internet
  - web
  - http
  - http2
  - http3
  - quic
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de Internet"
  - "Protocolos Web"
  - "HTTP Evolution"
---

# Arquitectura de Internet y Protocolos Web (HTTP/1-3)

Evolución de la topología interconectada global y los protocolos de entrega de aplicaciones web.

## Topología de Internet
- **ISP Tier 1**: Operadores de tránsito global interconectados libremente entre sí mediante acuerdos de *Peering*.
- **Puntos Neutros (IXP - Internet Exchange Points)**: Infraestructuras físicas donde múltiples ISPs y CDNs intercambian tráfico localmente.

## Evolución de HTTP
- **HTTP/1.1**: Protocolo de texto plano, cabeceras redundantes, bloqueo en cabeza de línea a nivel de aplicación (*Head-of-Line Blocking*).
- **HTTP/2**: Enmarcado binario, multiplexación completa de peticiones sobre una única conexión TCP, compresión de cabeceras HPACK, Server Push.
- **HTTP/3**: Reemplaza TCP por **QUIC** (basado en UDP) con TLS 1.3 integrado, eliminando el bloqueo en cabeza de línea a nivel de transporte ante pérdida de paquetes.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Seguridad Web: [[wiki/entities/tls-ssl-protocols|Protocolos Criptográficos TLS y SSL]]
- Enrutamiento: [[wiki/entities/bgp-and-ospf|Protocolos OSPF y BGP]]

