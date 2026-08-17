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

Los protocolos **TCP** y **UDP** operan en la **Capa de Transporte (Nivel 4)** de la pila TCP/IP para proporcionar comunicación lógica proceso-a-proceso mediante el uso de puertos (16 bits: 0 a 65535).

---

## 🏛️ Comparativa: TCP vs UDP

| Característica | TCP (RFC 793 / 9293) | UDP (RFC 768) |
|----------------|----------------------|---------------|
| **Orientación a Conexión** | Sí (Handshake previo obligatorio) | No (Envío directo sin conexión) |
| **Fiabilidad / Entrega** | Fiable (Garantiza entrega y orden vía ACKs) | No fiable (*Best-Effort*, sin retransmisión) |
| **Control de Flujo** | Sí (Ventana Deslizante / *Sliding Window*) | No |
| **Control de Congestión** | Sí (Algoritmos Slow Start, Congestion Avoidance) | No |
| **Tamaño Cabecera** | **20 a 60 bytes** | **8 bytes FIJOS** |
| **Sobrecarga (Overhead)** | Alta | Mínima |
| **Casos de Uso Típicos** | Web (HTTP/1-2), Correo (SMTP), SSH, FTP, BGP | DNS, DHCP, VoIP (RTP), Streaming, HTTP/3 (QUIC) |

---

## 🧩 Protocolo TCP: Conexión y Flags

- **Three-Way Handshake (Establecimiento)**:
  1. Cliente $ightarrow$ Servidor: `SYN` (Seq = $x$)
  2. Servidor $ightarrow$ Cliente: `SYN-ACK` (Seq = $y$, Ack = $x + 1$)
  3. Cliente $ightarrow$ Servidor: `ACK` (Seq = $x + 1$, Ack = $y + 1$)
- **Flags de Cabecera TCP**:
  - `SYN` (Sincronización), `ACK` (Confirmación), `FIN` (Cierre ordenado), `RST` (Reinicio inmediato), `PSH` (Envío inmediato a la aplicación), `URG` (Puntero urgente).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Cabecera TCP / UDP | **20 bytes mínimo** / **8 bytes fijos** |
| Rango de Puertos Bien Conocidos | **0 a 1023** |
| Rango de Puertos Registrados | **1024 a 49151** |
| Rango de Puertos Dinámicos / Efímeros | **49152 a 65535** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
