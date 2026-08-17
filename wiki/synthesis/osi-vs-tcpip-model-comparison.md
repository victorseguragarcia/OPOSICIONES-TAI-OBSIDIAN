---
title: "Comparativa: Modelo de Referencia ISO-OSI vs Pila de Protocolos TCP-IP"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - osi
  - tcp-ip
  - networking
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "OSI vs TCP/IP"
  - "Comparativa OSI y TCP/IP"
---

# Comparativa: Modelo de Referencia ISO-OSI vs Pila de Protocolos TCP-IP

Matriz de contraste técnico y conceptual entre los dos modelos fundamentales de redes de ordenadores.

---

## 🏛️ Matriz Comparativa Estructural

| Criterio | Modelo de Referencia ISO-OSI | Pila de Protocolos TCP/IP |
|----------|------------------------------|---------------------------|
| **Origen / Organismo** | Desarrollado por ISO e ITU-T (estándar formal teórico) | Desarrollado por DARPA y formalizado por IETF (estándar práctico) |
| **Número de Capas** | **7 Capas** estrictamente definidas | **4 Capas** (o 5 en modelo híbrido didáctico) |
| **Filosofía de Diseño** | Define claramente **Servicios, Interfaces y Protocolos** antes de su implementación | Los protocolos surgieron primero; el modelo describió la arquitectura existente |
| **Capa de Transporte** | Soporta servicios orientados a conexión y no orientados | Soporta ambos (**TCP** orientado a conexión, **UDP** no orientado) |
| **Capa de Red** | Soporta servicios con conexión (X.25) y sin conexión (CLNS) | **Solo sin conexión (Protocolo IP / Datagramas)** |
| **Sesión y Presentación** | Capas independientes dedicadas (5 y 6) | Integradas directamente en la **Capa de Aplicación** |
| **Adopción en el Mundo Real** | Éxito teórico conceptual; escasa adopción comercial directa | **El estándar de facto absoluto de Internet y redes modernas** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Entidad: [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
