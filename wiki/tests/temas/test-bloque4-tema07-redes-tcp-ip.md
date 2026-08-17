---
title: "Test de Autoevaluación: Bloque 4 - Tema 07 (Redes TCP/IP y Subnetting)"
type: "test"
target: "wiki/sources/bloque4-tema07.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-4
  - redes
  - tcp-ip
  - osi
  - subnetting
  - ipv4
  - ipv6
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 07: Modelo OSI, Pila TCP/IP y Direccionamiento IPv4/IPv6

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---

## ❓ Preguntas

### 1. ¿En qué capa del modelo OSI opera el protocolo ICMP (Internet Control Message Protocol)?
- [ ] a) Capa 2 (Enlace de datos).
- [ ] b) Capa 3 (Red).
- [ ] c) Capa 4 (Transporte).
- [ ] d) Capa 7 (Aplicación).

### 2. Dada la dirección IPv4 `192.168.10.65/26`, ¿cuál es la dirección de red y la dirección de broadcast de la subred a la que pertenece?
- [ ] a) Red: `192.168.10.0` | Broadcast: `192.168.10.63`
- [ ] b) Red: `192.168.10.64` | Broadcast: `192.168.10.127`
- [ ] c) Red: `192.168.10.64` | Broadcast: `192.168.10.255`
- [ ] d) Red: `192.168.10.32` | Broadcast: `192.168.10.95`

### 3. ¿Cuántos hosts útiles (*utilizables*) permite asignar una subred con máscara `/29`?
- [ ] a) 8 hosts.
- [ ] b) 6 hosts.
- [ ] c) 14 hosts.
- [ ] d) 30 hosts.

### 4. ¿Cuál de los siguientes campos NO está presente en la cabecera básica de un paquete IPv6?
- [ ] a) Traffic Class (Clase de tráfico).
- [ ] b) Flow Label (Etiqueta de flujo).
- [ ] c) Checksum (Suma de verificación de cabecera).
- [ ] d) Hop Limit (Límite de saltos).

### 5. En el protocolo TCP, ¿cuál es la secuencia exacta de flags en el saludo de tres vías (*Three-Way Handshake*) para el establecimiento de conexión?
- [ ] a) `SYN` $ightarrow$ `ACK` $ightarrow$ `SYN-ACK`
- [ ] b) `SYN` $ightarrow$ `SYN-ACK` $ightarrow$ `ACK`
- [ ] c) `FIN` $ightarrow$ `ACK` $ightarrow$ `FIN-ACK`
- [ ] d) `RST` $ightarrow$ `SYN` $ightarrow$ `ACK`

### 6. ¿Qué mecanismo utiliza IPv6 para autoconfigurar automáticamente la dirección de enlace local (*Link-Local*) a partir de la dirección MAC física de la tarjeta de red?
- [ ] a) DHCPv6 Stateful.
- [ ] b) Proceso EUI-64 (invirtiendo el bit U/L e insertando `FF:FE`).
- [ ] c) NAT64 / DNS64.
- [ ] d) ARP Request / Reply.

### 7. ¿Cuál es el tamaño fijo de la cabecera base de un paquete IPv6 sin cabeceras de extensión?
- [ ] a) 20 bytes.
- [ ] b) 32 bytes.
- [ ] c) 40 bytes.
- [ ] d) 64 bytes.

### 8. En la capa de transporte, ¿cuál es la principal diferencia entre TCP y UDP?
- [ ] a) TCP es no orientado a conexión y no garantiza entrega; UDP es orientado a conexión con control de flujo.
- [ ] b) TCP es orientado a conexión con control de congestión y retransmisión; UDP es no orientado a conexión con mínima sobrecarga de cabecera (8 bytes).
- [ ] c) TCP solo funciona sobre IPv4 y UDP solo sobre IPv6.
- [ ] d) TCP no usa puertos y UDP sí.

### 9. ¿Cuál de los siguientes rangos de direcciones IPv4 corresponde a Direcciones Privadas según la RFC 1918?
- [ ] a) `127.0.0.0/8`
- [ ] b) `169.254.0.0/16`
- [ ] c) `172.16.0.0/12` (hasta `172.31.255.255`)
- [ ] d) `224.0.0.0/4`

### 10. En una red Ethernet conmutada, ¿qué protocolo previene la formación de bucles de capa 2 (*Bridging Loops*) desactivando enlaces redundantes?
- [ ] a) BGP (Border Gateway Protocol).
- [ ] b) STP (Spanning Tree Protocol - IEEE 802.1D).
- [ ] c) OSPF (Open Shortest Path First).
- [ ] d) RIPv2 (Routing Information Protocol).

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **c** | 5. **b** | 6. **b** | 7. **c** | 8. **b** | 9. **c** | 10. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: ICMP opera en Capa 3 (Red) del modelo OSI encapsulado directamente en datagramas IP (número de protocolo 1 en IPv4, 58 en IPv6).
> - **Pregunta 2 (b)**: Con `/26`, el salto de subred es $256 - 192 = 64$. Subredes: `0-63`, `64-127`. La IP `192.168.10.65` cae en la red `192.168.10.64` con broadcast `192.168.10.127`.
> - **Pregunta 3 (b)**: `/29` reserva 3 bits de host ($2^3 = 8$). Restando red y broadcast: $8 - 2 = 6$ hosts útiles.
> - **Pregunta 4 (c)**: En IPv6 se eliminó el campo **Checksum** de la cabecera para acelerar el procesamiento de enrutadores, delegando la integridad en capas de enlace y transporte.
> - **Pregunta 5 (b)**: El Three-Way Handshake es cliente envía `SYN`, servidor responde `SYN-ACK`, cliente confirma con `ACK`.
> - **Pregunta 6 (b)**: Formato EUI-64 divide la MAC de 48 bits en dos mitades de 24 bits, inserta `FF:FE` en medio (convirtiéndola en 64 bits) e invierte el 7º bit del primer byte (bit Universal/Local).
> - **Pregunta 7 (c)**: La cabecera base de IPv6 tiene una longitud fija de **40 bytes** (320 bits), lo que permite procesamiento por hardware en routers.
> - **Pregunta 8 (b)**: TCP ofrece fiabilidad y control de flujo con cabecera de 20-60 bytes; UDP ofrece baja latencia con cabecera fija de 8 bytes sin acuses ni retransmisiones.
> - **Pregunta 9 (c)**: RFC 1918 define `10.0.0.0/8`, `172.16.0.0/12` (`172.16.0.0` - `172.31.255.255`) y `192.168.0.0/16`. `127.0.0.0/8` es loopback y `169.254.0.0/16` es APIPA.
> - **Pregunta 10 (b)**: Spanning Tree Protocol (IEEE 802.1D / 802.1w RSTP) calcula un árbol libre de bucles en redes de capa 2 mediante el envío de tramas BPDU.
