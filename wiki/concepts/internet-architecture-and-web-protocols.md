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
  - "Web Protocols"
---

# Arquitectura de Internet y Protocolos Web (HTTP/1-3)

La infraestructura de Internet opera mediante una jerarquía global descentralizada de proveedores de servicios interconectados a través de puntos neutros y protocolos de aplicación web.

---

## 🏛️ Jerarquía de Tráfico Global en Internet

- **Tier 1 (Troncales Globales)**: Operadores con redes de fibra transoceánicas que no pagan por tránsito (*Settlement-Free Peering*).
- **IXP (Internet Exchange Points)**: Conmutadores de alta capacidad donde ISPs y CDNs intercambian tráfico localmente (ej. ESpanix en España).
- **CDNs (Content Delivery Networks)**: Redes distribuidas geográficamente que cachean contenido estático y dinámico cerca de los usuarios finales (Cloudflare, Akamai).

---

## 🧩 Evolución de los Protocolos Web HTTP

- **HTTP/1.1**: Conexiones persistentes (`Keep-Alive`) pero limitado por bloqueo en cabeza de línea (*Head-of-Line Blocking*) a nivel de aplicación.
- **HTTP/2**: Formato binario con multiplexación de múltiples flujos sobre una sola conexión TCP y compresión **HPACK**.
- **HTTP/3**: Elimina el transporte TCP sustituyéndolo por **QUIC (RFC 9000)** sobre **UDP** (puerto 443), eliminando el bloqueo en cabeza de línea de transporte, integrando **TLS 1.3** nativo (0-RTT/1-RTT) y permitiendo migración transparente de conexión por *Connection ID*.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo | Transporte | Puerto | Compresión Cabeceras |
|-----------|------------|--------|----------------------|
| HTTP/1.1 | TCP | 80 / 443 (TLS) | Ninguna |
| HTTP/2 | TCP | 443 (TLS) | **HPACK** |
| HTTP/3 | **QUIC (UDP)** | **443 UDP** | **QPACK** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
- Entidad: [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]
