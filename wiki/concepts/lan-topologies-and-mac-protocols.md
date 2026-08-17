---
title: "Topologías LAN y Protocolos de Acceso al Medio (MAC)"
type: "concept"
tags:
  - lan
  - topologies
  - csma-cd
  - csma-ca
  - ieee-802
sources:
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Topologías LAN y Control de Acceso"
  - "MAC Protocols"
---

# Topologías LAN y Protocolos de Acceso al Medio (MAC)

Las redes de área local organizan sus nodos mediante disposiciones geométricas (topologías físicas y lógicas) y gestionan la contienda sobre medios compartidos mediante protocolos de control de acceso al medio (**MAC**).

---

## 🏛️ Topologías de Red Principales

- **Bus**: Todos los nodos comparten un mismo canal físico lineal con terminadores en los extremos. Punto único de fallo en el cable troncal.
- **Estrella**: Todos los nodos se conectan a un conmutador central. Es la topología física dominante en las redes Ethernet modernas.
- **Anillo (Ring)**: Circuito cerrado donde cada nodo reenvía al siguiente (Token Ring, FDDI con doble anillo).
- **Malla Completa**: Cada nodo se conecta con todos los demás. Requiere $N(N-1)/2$ enlaces. Máxima tolerancia a fallos.

---

## 🧩 Protocolos de Contienda: CSMA/CD frente a CSMA/CA

| Parámetro | CSMA/CD (IEEE 802.3 - Ethernet Cableado) | CSMA/CA (IEEE 802.11 - Wi-Fi Inalámbrico) |
|-----------|------------------------------------------|-------------------------------------------|
| **Principio** | Detección de Colisiones (*Collision Detection*) | Prevención de Colisiones (*Collision Avoidance*) |
| **Mecanismo** | Escucha mientras transmite; si detecta colisión envía señal *Jam* y ejecuta Backoff | Escucha antes de hablar; utiliza IFS (DIFS/SIFS) y reservas virtuales **RTS/CTS** |
| **Motivo** | Los cables permiten detectar variaciones anómalas de voltaje durante la transmisión | En radio, la potencia de transmisión del propio nodo ensordece su receptor |
| **Backoff** | **Retroceso Exponencial Binario (BEB)** tras colisión | Ventana de contienda aleatoria antes de transmitir |
| **Límite Intentos** | **16 intentos máximos** (descarte de trama) | Límite de retransmisiones de tramas |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Mínimo Trama Ethernet | **64 bytes (512 bits / Slot Time)** |
| Tamaño Máximo Trama Ethernet | **1518 bytes** (1522 bytes con 802.1Q) |
| Enlaces Malla Completa | $N(N-1)/2$ |
| Algoritmo de Espera Ethernet | **Binary Exponential Backoff** (hasta intento 10) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
