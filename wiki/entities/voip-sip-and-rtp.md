---
title: "Telefonía IP (VoIP): Protocolos SIP, SDP, RTP y RTCP"
type: "entity"
tags:
  - voip
  - sip
  - rtp
  - sdp
  - protocols
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "VoIP"
  - "SIP y RTP"
  - "Telefonía sobre IP"
---

# Telefonía IP (VoIP): Protocolos SIP, SDP, RTP y RTCP

La telefonía sobre IP (**VoIP**) integra la transmisión digitalizada de voz y vídeo en tiempo real a través de redes conmutadas por paquetes basadas en el protocolo IP.

---

## 🏛️ Arquitectura y Protocolos de VoIP

```
[ Teléfono VoIP A ]                                            [ Teléfono VoIP B ]
        │                                                               │
        │ ── 1. Señalización SIP (Puerto 5060 TCP/UDP) ───────────────► │
        │    (Negociación de códecs con SDP en el cuerpo SIP)           │
        │                                                               │
        │ ◄── 2. Flujo de Audio/Vídeo en Tiempo Real (RTP sobre UDP) ──► │
        │ ◄── 3. Control de Calidad y Jitter (RTCP sobre UDP) ─────────► │
```

---

## 🧩 Desglose de Protocolos

### 1. SIP (Session Initiation Protocol - RFC 3261)
- Protocolo de señalización textual de la capa de aplicación similar a HTTP.
- **Puertos**: **5060 TCP/UDP** (texto plano) y **5061 TCP** (SIPS con cifrado TLS).
- **Métodos Principales**:
  - `INVITE`: Inicia el establecimiento de una sesión o llamada.
  - `ACK`: Confirma la recepción de la respuesta final al INVITE.
  - `BYE`: Termina una sesión activa.
  - `CANCEL`: Cancela una petición pendiente antes de ser respondida.
  - `REGISTER`: Registra la ubicación del usuario ante el servidor *Registrar*.
  - `OPTIONS`: Consulta las capacidades de un servidor o cliente.

### 2. SDP (Session Description Protocol - RFC 4566)
- Formato de texto que describe los parámetros de la sesión multimedia transportado dentro del cuerpo del mensaje SIP: direcciones IP de los medios, puertos UDP asignados y códecs soportados.

### 3. RTP y RTCP (RFC 3550)
- **RTP (Real-time Transport Protocol)**: Transporta los paquetes de medios sobre **UDP** usando puertos dinámicos pares (1024 a 65535). Incluye marcas de tiempo (*Timestamps*) y números de secuencia para reconstruir el flujo de audio en orden y medir el *jitter*.
- **RTCP (RTP Control Protocol)**: Supervisa la calidad del servicio transmitiendo estadísticas de pérdida de paquetes, retardo y jitter sobre el puerto impar inmediatamente superior ($RTP + 1$).
- **SRTP (Secure RTP - RFC 3711)**: Versión segura con cifrado AES y autenticación HMAC-SHA1.

---

## 🎵 Códecs de Voz Principales

| Códec | Estándar ITU-T | Tasa de Bits | Algoritmo / Calidad | Ancho de Banda con Cabeceras |
|-------|----------------|--------------|---------------------|------------------------------|
| **G.711** | ITU-T G.711 | **64 kbps** | PCM ($\mu$-law en EEUU/Japón, A-law en Europa) | $\sim 87.2 	ext{ kbps}$ |
| **G.729** | ITU-T G.729 | **8 kbps** | CS-ACELP (alta compresión) | $\sim 31.2 	ext{ kbps}$ |
| **G.722** | ITU-T G.722 | **64 kbps** | SB-ADPCM (Voz HD / Wideband 7 kHz) | $\sim 87.2 	ext{ kbps}$ |
| **Opus** | IETF RFC 6716 | **6 a 510 kbps** | Dinámico / Adaptativo (estándar WebRTC) | Variable |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto SIP / SIPS | **5060 TCP/UDP** / **5061 TLS** |
| Transporte de Medios | **RTP sobre UDP** (puertos pares) |
| Control de Calidad | **RTCP sobre UDP** (puertos impares) |
| Códec Telefónico Estándar Europa | **G.711 A-law (64 kbps)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
