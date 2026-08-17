---
title: "Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3"
type: "entity"
tags:
  - http
  - http2
  - http3
  - quic
  - web
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "HTTP"
  - "HTTP/2"
  - "HTTP/3"
  - "QUIC"
---

# Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3

El **Hypertext Transfer Protocol (HTTP)** es el protocolo cliente-servidor de la capa de aplicación sobre el que se fundamenta la World Wide Web.

---

## 🏛️ Evolución Arquitectónica de HTTP

| Característica | HTTP/1.1 (RFC 9112) | HTTP/2 (RFC 9113) | HTTP/3 (RFC 9114) |
|----------------|---------------------|-------------------|-------------------|
| **Capa de Transporte** | **TCP** (Puerto 80/443) | **TCP** (Puerto 443 con TLS) | **QUIC sobre UDP** (Puerto 443) |
| **Formato de Mensaje** | Texto plano | **Binario** (Frames y Streams) | **Binario** (Frames y Streams) |
| **Multiplexación** | No (Pipelining limitado con HoL blocking) | **Sí** (Múltiples streams sobre 1 TCP) | **Sí nativa** (Streams independientes sin HoL) |
| **Compresión Cabeceras** | No | **HPACK** (RFC 7541) | **QPACK** (RFC 9204) |
| **Seguridad / Cifrado** | Opcional (HTTPS / TLS) | Prácticamente obligatorio (TLS 1.2+) | **Integrado por diseño (TLS 1.3 nativo)** |
| **Migración Conexión** | No (ligado a IP/Puerto TCP) | No | **Sí** (mediante *Connection ID*) |
| **Latencia Handshake** | 2-3 RTT (TCP + TLS) | 2-3 RTT | **0-RTT o 1-RTT** |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puerto HTTP / HTTPS | **80 TCP** / **443 TCP** |
| Puerto HTTP/3 | **443 UDP** |
| Transporte HTTP/3 | **QUIC (RFC 9000)** sobre UDP |
| Algoritmos de Compresión Cabeceras | **HPACK** (HTTP/2) y **QPACK** (HTTP/3) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]
- Concepto: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
