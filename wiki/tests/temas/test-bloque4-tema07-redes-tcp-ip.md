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

# 🔴 Test de Autoevaluación: Bloque 4 - Tema 07 (Redes TCP/IP y Subnetting)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 4 - Tema 07 (Redes TCP/IP y Subnetting)",
  "questions": [
    {
      "question": "¿En qué capa del modelo OSI opera el protocolo ICMP (Internet Control Message Protocol)?",
      "options": [
        "Capa 2 (Enlace de datos).",
        "Capa 3 (Red).",
        "Capa 4 (Transporte).",
        "Capa 7 (Aplicación)."
      ],
      "answer": "b",
      "explanation": "ICMP opera en Capa 3 (Red) del modelo OSI encapsulado directamente en datagramas IP (número de protocolo 1 en IPv4, 58 en IPv6)."
    },
    {
      "question": "Dada la dirección IPv4 `192.168.10.65/26`, ¿cuál es la dirección de red y la dirección de broadcast de la subred a la que pertenece?",
      "options": [
        "Red: `192.168.10.0` | Broadcast: `192.168.10.63`",
        "Red: `192.168.10.64` | Broadcast: `192.168.10.127`",
        "Red: `192.168.10.64` | Broadcast: `192.168.10.255`",
        "Red: `192.168.10.32` | Broadcast: `192.168.10.95`"
      ],
      "answer": "b",
      "explanation": "Con `/26`, el salto de subred es $256 - 192 = 64$. Subredes: `0-63`, `64-127`. La IP `192.168.10.65` cae en la red `192.168.10.64` con broadcast `192.168.10.127`."
    },
    {
      "question": "¿Cuántos hosts útiles (*utilizables*) permite asignar una subred con máscara `/29`?",
      "options": [
        "8 hosts.",
        "6 hosts.",
        "14 hosts.",
        "30 hosts."
      ],
      "answer": "b",
      "explanation": "`/29` reserva 3 bits de host ($2^3 = 8$). Restando red y broadcast: $8 - 2 = 6$ hosts útiles."
    },
    {
      "question": "¿Cuál de los siguientes campos NO está presente en la cabecera básica de un paquete IPv6?",
      "options": [
        "Traffic Class (Clase de tráfico).",
        "Flow Label (Etiqueta de flujo).",
        "Checksum (Suma de verificación de cabecera).",
        "Hop Limit (Límite de saltos)."
      ],
      "answer": "c",
      "explanation": "En IPv6 se eliminó el campo **Checksum** de la cabecera para acelerar el procesamiento de enrutadores, delegando la integridad en capas de enlace y transporte."
    },
    {
      "question": "En el protocolo TCP, ¿cuál es la secuencia exacta de flags en el saludo de tres vías (*Three-Way Handshake*) para el establecimiento de conexión?",
      "options": [
        "`SYN` $",
        "`SYN` $",
        "`FIN` $",
        "`RST` $"
      ],
      "answer": "b",
      "explanation": "El Three-Way Handshake es cliente envía `SYN`, servidor responde `SYN-ACK`, cliente confirma con `ACK`."
    },
    {
      "question": "¿Qué mecanismo utiliza IPv6 para autoconfigurar automáticamente la dirección de enlace local (*Link-Local*) a partir de la dirección MAC física de la tarjeta de red?",
      "options": [
        "DHCPv6 Stateful.",
        "Proceso EUI-64 (invirtiendo el bit U/L e insertando `FF:FE`).",
        "NAT64 / DNS64.",
        "ARP Request / Reply."
      ],
      "answer": "b",
      "explanation": "Formato EUI-64 divide la MAC de 48 bits en dos mitades de 24 bits, inserta `FF:FE` en medio (convirtiéndola en 64 bits) e invierte el 7º bit del primer byte (bit Universal/Local)."
    },
    {
      "question": "¿Cuál es el tamaño fijo de la cabecera base de un paquete IPv6 sin cabeceras de extensión?",
      "options": [
        "20 bytes.",
        "32 bytes.",
        "40 bytes.",
        "64 bytes."
      ],
      "answer": "c",
      "explanation": "La cabecera base de IPv6 tiene una longitud fija de **40 bytes** (320 bits), lo que permite procesamiento por hardware en routers."
    },
    {
      "question": "En la capa de transporte, ¿cuál es la principal diferencia entre TCP y UDP?",
      "options": [
        "TCP es no orientado a conexión y no garantiza entrega; UDP es orientado a conexión con control de flujo.",
        "TCP es orientado a conexión con control de congestión y retransmisión; UDP es no orientado a conexión con mínima sobrecarga de cabecera (8 bytes).",
        "TCP solo funciona sobre IPv4 y UDP solo sobre IPv6.",
        "TCP no usa puertos y UDP sí."
      ],
      "answer": "b",
      "explanation": "TCP ofrece fiabilidad y control de flujo con cabecera de 20-60 bytes; UDP ofrece baja latencia con cabecera fija de 8 bytes sin acuses ni retransmisiones."
    },
    {
      "question": "¿Cuál de los siguientes rangos de direcciones IPv4 corresponde a Direcciones Privadas según la RFC 1918?",
      "options": [
        "`127.0.0.0/8`",
        "`169.254.0.0/16`",
        "`172.16.0.0/12` (hasta `172.31.255.255`)",
        "`224.0.0.0/4`"
      ],
      "answer": "c",
      "explanation": "RFC 1918 define `10.0.0.0/8`, `172.16.0.0/12` (`172.16.0.0` - `172.31.255.255`) y `192.168.0.0/16`. `127.0.0.0/8` es loopback y `169.254.0.0/16` es APIPA."
    },
    {
      "question": "En una red Ethernet conmutada, ¿qué protocolo previene la formación de bucles de capa 2 (*Bridging Loops*) desactivando enlaces redundantes?",
      "options": [
        "BGP (Border Gateway Protocol).",
        "STP (Spanning Tree Protocol - IEEE 802.1D).",
        "OSPF (Open Shortest Path First).",
        "RIPv2 (Routing Information Protocol)."
      ],
      "answer": "b",
      "explanation": "Spanning Tree Protocol (IEEE 802.1D / 802.1w RSTP) calcula un árbol libre de bucles en redes de capa 2 mediante el envío de tramas BPDU."
    }
  ]
}
```
