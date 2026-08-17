---
title: "Resumen Fuente: Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema07
  - modelo-osi
  - tcp-ip
  - ipv4
  - ipv6
  - subnetting
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Modelo ISO-OSI, TCP-IP, IPv4 e IPv6"
  - "bloque4-tema07"
---

# Resumen Fuente: Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema07.md|bloque4-tema07.md]].

---

## 📖 Resumen Ejecutivo

Este tema constituye el núcleo teórico de redes de comunicaciones en las oposiciones TAI. Realiza un estudio comparativo exhaustivo entre el **Modelo de Referencia OSI de 7 capas** (ISO/IEC 7498-1) y la **Pila de Protocolos TCP/IP de 4 capas** (RFC 1122), analizando las Unidades de Datos de Protocolo (PDU) y primitivas de servicio. Se detalla el direccionamiento IPv4 (clases tradicionales A/B/C/D/E, subnetting, VLSM, CIDR RFC 1519, cabecera de 20-60 bytes), el direccionamiento IPv6 (formato de 128 bits, ámbitos Link-Local, Unique Local y Global Unicast, autoconfiguración SLAAC con EUI-64 modificado, cabecera fija simplificada de 40 bytes y cabeceras de extensión), los protocolos de transporte TCP y UDP, y los Registros Regionales de Internet (RIRs como RIPE NCC).

---

## 🧩 Estructura y Desglose Temático

### 1. Modelo de Referencia ISO/OSI (7 Capas)
- **Concepto**: Modelo arquitectónico estándar desarrollado por ISO para la interconexión de sistemas heterogéneos.
- **Desglose de Capas y PDUs**:

| Nº | Capa OSI | PDU | Funciones Principales | Protocolos / Dispositivos |
|---|----------|-----|----------------------|---------------------------|
| **7** | **Aplicación** | Datos | Interfaz de servicios de red con las aplicaciones de usuario | HTTP, DNS, SMTP, SNMP, FTP, SSH |
| **6** | **Presentación** | Datos | Formateo, sintaxis, compresión y cifrado de datos | ASN.1, MIME, TLS/SSL, ASCII, JPEG |
| **5** | **Sesión** | Datos | Establecimiento, mantenimiento y sincronización de sesiones (puntos de control) | NetBIOS, RPC, PPTP, SCP |
| **4** | **Transporte** | Segmento | Comunicación extremo a extremo, control de flujo, multiplexación por puertos | TCP (orientado a conexión), UDP (no orientado) |
| **3** | **Red** | Paquete | Direccionamiento lógico global, enrutamiento y selección de ruta | IPv4, IPv6, ICMP, IPsec, OSPF, BGP / Routers |
| **2** | **Enlace de Datos** | Trama (*Frame*) | Direccionamiento físico (MAC), control de acceso al medio (MAC/LLC), detección de errores (CRC) | Ethernet (802.3), Wi-Fi (802.11), PPP, STP / Switches, Bridges |
| **1** | **Física** | Bit | Transmisión binaria no estructurada sobre el medio físico, voltajes, conectores | Cables UTP, Fibra, Hubs, Repetidores |

- **Primitivas de Comunicación OSI**: `Petición (Request)`, `Indicación (Indication)`, `Respuesta (Response)`, `Confirmación (Confirm)`.

### 2. Protocolo IPv4 (Internet Protocol Version 4)
- Definido en **RFC 791**. Direcciones de **32 bits (4 bytes)** en notación decimal con puntos (`192.168.1.1`).
- **Clases Históricas de Red**:
  - **Clase A**: `0.0.0.0` a `127.255.255.255` (Primer bit `0`, máscara `/8`, 126 redes, 16.7 millones de hosts).
  - **Clase B**: `128.0.0.0` a `191.255.255.255` (Primeros bits `10`, máscara `/16`, 16.384 redes, 65.534 hosts).
  - **Clase C**: `192.0.0.0` a `223.255.255.255` (Primeros bits `110`, máscara `/24`, 2 millones de redes, 254 hosts).
  - **Clase D**: `224.0.0.0` a `239.255.255.255` (Primeros bits `1110`, reservada para **Multicast**).
  - **Clase E**: `240.0.0.0` a `255.255.255.255` (Primeros bits `1111`, reservada para experimentación/investigación).
- **Rangos Privados (RFC 1918)**:
  - `10.0.0.0/8` (`10.0.0.0` - `10.255.255.255`)
  - `172.16.0.0/12` (`172.16.0.0` - `172.31.255.255`)
  - `192.168.0.0/16` (`192.168.0.0` - `192.255.255.255`)
- **Direcciones Especiales**:
  - `127.0.0.0/8`: Bucle local (*Loopback* - `127.0.0.1`).
  - `169.254.0.0/16`: Direcciones APIPA (Auto-IP si DHCP falla, RFC 3927).
  - `0.0.0.0/0`: Ruta por defecto / Red actual.
  - Dirección de Red (todos los bits de host a 0) y Dirección de Broadcast (todos los bits de host a 1).
- **Subnetting y CIDR (RFC 1519)**: Enrutamiento interdominio sin clases con máscaras de longitud variable (**VLSM**).
- **Cabecera IPv4**: Tamaño mínimo **20 bytes** (máximo 60 con opciones). Campos: Versión (4 bits), IHL (4 bits), Tipo de Servicio/DSCP (8 bits), Longitud Total (16 bits), Identificador (16 bits), Flags (3 bits: Reserved, DF-Don't Fragment, MF-More Fragments), Desplazamiento de Fragmento (13 bits), **TTL** (8 bits), **Protocolo** (8 bits: `1` ICMP, `6` TCP, `17` UDP, `89` OSPF), Checksum de Cabecera (16 bits), IP Origen (32 bits), IP Destino (32 bits).

### 3. Protocolo IPv6 (Internet Protocol Version 6)
- Definido en **RFC 8200** (estándar de Internet). Direcciones de **128 bits (16 bytes)** en notación hexadecimal separada por dos puntos (`2001:0db8:85a3::8a2e:0370:7334`).
- **Reglas de Abreviatura**: Omisión de ceros a la izquierda en bloques; sustitución de una secuencia contigua de bloques de ceros por `::` (una sola vez por dirección).
- **Ámbitos de Direcciones IPv6**:
  - **Enlace Local (Link-Local)**: `fe80::/10` (no enrutable fuera del enlace local; autoconfigurada obligatoria en cada interfaz activa).
  - **Global Unicast (GUA)**: `2000::/3` (públicas y enrutables globalmente en Internet).
  - **Unique Local (ULA)**: `fc00::/7` (equivalente a RFC 1918 privado; típicamente `fd00::/8`).
  - **Multicast**: `ff00::/8` (ej. `ff02::1` todos los nodos, `ff02::2` todos los routers).
  - **Loopback**: `::1/128`.
  - **No especificada**: `::/128`.
- **Autoconfiguración Sin Estado (SLAAC - RFC 4862)**:
  - El host envía peticiones *Router Solicitation* (RS) y recibe *Router Advertisement* (RA) con el prefijo de red `/64`.
  - **EUI-64 Modificado**: Genera el ID de interfaz de 64 bits a partir de la MAC de 48 bits: inserta `FF:FE` en el centro y conmuta el 7º bit del primer byte (bit Universal/Local).
  - **DAD (Duplicate Address Detection)**: Verifica con ICMPv6 Neighbor Solicitation que la dirección no esté duplicada en la red.
- **Cabecera IPv6 Simplificada**:
  - Tamaño fijo de **40 bytes** (procesamiento por hardware ultrarrápido).
  - Sin checksum de cabecera (delegado a capas 2 y 4), sin fragmentación en routers (solo el host emisor fragmenta mediante *Path MTU Discovery*).
  - Campos: Versión (4 bits), Traffic Class (8 bits), Flow Label (20 bits), Payload Length (16 bits), **Next Header** (8 bits), **Hop Limit** (8 bits, equivale a TTL), IP Origen (128 bits), IP Destino (128 bits).
  - **Cabeceras de Extensión**: Encadenadas mediante el campo *Next Header* (Hop-by-Hop, Routing, Fragment, ESP, AH, Destination Options).

### 4. Modelo TCP/IP y Protocolos de Transporte
- **Pila TCP/IP de 4 Capas (RFC 1122)**:
  1. Aplicación (combina capas 5, 6 y 7 de OSI).
  2. Transporte (TCP, UDP).
  3. Internet (IPv4, IPv6, ICMP, IGMP).
  4. Acceso a la Red (combina capas 1 y 2 de OSI: Ethernet, Wi-Fi, PPP).
- **TCP (Transmission Control Protocol - RFC 793 / 9293)**:
  - Conexión fiable orientada a conexión, control de flujo por ventana deslizante (*sliding window*), control de congestión (Tahoe, Reno, CUBIC), retransmisión de segmentos perdidos (ARQ con ACK acumulativo).
  - Establecimiento de conexión: **Three-Way Handshake** (`SYN` → `SYN-ACK` → `ACK`).
  - Cierre de conexión: **Four-Way Handshake** (`FIN` → `ACK` → `FIN` → `ACK`).
  - Cabecera: Mínimo **20 bytes** (máximo 60 con opciones). Flags: `URG`, `ACK`, `PSH`, `RST`, `SYN`, `FIN`.
- **UDP (User Datagram Protocol - RFC 768)**:
  - No orientado a conexión, no fiable, sin control de flujo ni retransmisión, mínimo overhead.
  - Cabecera fija de **8 bytes**: Puerto Origen (16 bits), Puerto Destino (16 bits), Longitud (16 bits), Checksum (16 bits).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Protocolo | Especificación Técnica |
|-----------------------|------------------------|
| Capas Modelo OSI | **7 capas** (Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación) |
| Capas Modelo TCP/IP | **4 capas** (Acceso a Red, Internet, Transporte, Aplicación) |
| Tamaño Cabecera IPv4 | **20 bytes mínimo** (hasta 60 bytes con opciones) |
| Tamaño Cabecera IPv6 | **40 bytes FIJOS** (sin checksum, usa cabeceras de extensión) |
| Tamaño Cabecera TCP | **20 bytes mínimo** (hasta 60 bytes con opciones) |
| Tamaño Cabecera UDP | **8 bytes FIJOS** |
| Rango APIPA IPv4 | `169.254.0.0/16` |
| Rango Loopback IPv4 / IPv6 | `127.0.0.0/8` / `::1/128` |
| Prefijo Link-Local IPv6 | `fe80::/10` |
| Prefijo Global Unicast IPv6 | `2000::/3` |
| Prefijo Multicast IPv6 | `ff00::/8` |
| Generación EUI-64 | Inserta `FFFE` en el medio de la MAC e invierte el **bit 7 (U/L)** |
| RIR para Europa | **RIPE NCC** (Réseaux IP Européens Network Coordination Centre) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Capa de Enlace]]
- [[wiki/entities/bgp-and-ospf|Protocolos de Enrutamiento: OSPF y BGP]]

### Conceptos Teóricos:
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]

### Síntesis de Estudio:
- [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI frente a TCP-IP]]
- [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
