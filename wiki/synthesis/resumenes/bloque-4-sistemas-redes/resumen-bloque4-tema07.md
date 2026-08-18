---
title: "Resumen Exhaustivo Tema 07 (Bloque 4): Protocolo IP, Subnetting IPv4/IPv6, ICMP, DHCP y DNS"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-07
  - sistemas
  - redes
  - seguridad
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema07.md]]"
  - "[[wiki/sources/bloque4-tema07]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|⬅️ Tema 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|Tema 08 ➡️]]

# 🔴 Resumen Exhaustivo Tema 07 (Bloque 4): Protocolo IP, Subnetting IPv4/IPv6, ICMP, DHCP y DNS

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 07**
> Arquitectura de red TCP/IP, cabecera IPv4 vs IPv6, direccionamiento IPv4 (Clases A/B/C/D/E, IPs privadas RFC 1918, VLSM, CIDR), direccionamiento IPv6 (formato 128 bits, prefijos, Unicast, Anycast, Multicast, SLAAC), protocolo ICMP, DHCP (proceso DORA, puertos 67/68) y DNS (jerarquía, tipos de registros A, AAAA, CNAME, MX, PTR, SOA).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Protocolo IPv4, Clases y Subnetting (VLSM / CIDR)
- **Cabecera IPv4 (RFC 791)**: Longitud mínima de **20 bytes** (hasta 60 con opciones). Campos: Versión (4 bits), IHL (4 bits), TTL (Time-To-Live, decrece en cada salto de router), Protocolo (6 TCP, 17 UDP, 1 ICMP), Checksum, IP Origen (32 bits), IP Destino (32 bits).
- **Clases Históricas de Direcciones IPv4**:
  - *Clase A*: `0.0.0.0` a `127.255.255.255` (máscara `/8` - $255.0.0.0$).
  - *Clase B*: `128.0.0.0` a `191.255.255.255` (máscara `/16` - $255.255.0.0$).
  - *Clase C*: `192.0.0.0` a `223.255.255.255` (máscara `/24` - $255.255.255.0$).
  - *Clase D*: `224.0.0.0` a `239.255.255.255` (Multicast).
  - *Clase E*: `240.0.0.0` a `255.255.255.255` (Reservada / Investigación).
- **Rangos de Direcciones IP Privadas (RFC 1918 - No Enrutables en Internet)**:
  - **Clase A**: `10.0.0.0` a `10.255.255.255` (`10.0.0.0/8`).
  - **Clase B**: `172.16.0.0` a `172.31.255.255` (`172.16.0.0/12` - 16 bloques contiguos).
  - **Clase C**: `192.168.0.0` a `192.168.255.255` (`192.168.0.0/16` - 256 bloques clase C).
- **Fórmulas de Subnetting**:
  - Número de subredes posibles con $s$ bits prestados: $2^s$.
  - Número de hosts útiles por subred con $h$ bits de host: **$2^h - 2$** (se resta la dirección de red y la de broadcast).

### 2. Protocolo IPv6 (RFC 8200)
- **Características**: Direcciones de **128 bits** representadas en 8 bloques hexadecimales de 16 bits (`2001:0db8:85a3:0000:0000:8a2e:0370:7334`).
  - Cabecera fija simplificada de **40 bytes**. El campo TTL pasa a llamarse **Hop Limit**; desaparece el checksum de cabecera.
  - ❌ **NO existe el concepto de Broadcast en IPv6** (reemplazado por Multicast eficiente).
- **Tipos de Direcciones IPv6**:
  - **Unicast Global**: `2000::/3` (enrutable públicamente en Internet).
  - **Link-Local (Enlace Local)**: `fe80::/10` (autogenerada para comunicación dentro del mismo segmento local).
  - **Unique Local (Privadas)**: `fc00::/7` (equivalente a RFC 1918).
  - **Loopback**: `::1/128` (equivalente al `127.0.0.1` de IPv4).
  - **Multicast**: `ff00::/8`.
  - **Anycast**: Asignada a múltiples interfaces; el paquete se entrega al nodo más cercano.
- **Autoconfiguración SLAAC**: Autoconfiguración sin estado mediante mensajes ICMPv6 Router Solicitation / Router Advertisement.

### 3. Protocolos Auxiliares de Red: DHCP y DNS
- **DHCP (Dynamic Host Configuration Protocol - RFC 2131)**:
  - **Proceso DORA**:
    1. **D**iscover: El cliente envía broadcast solicitando IP (`0.0.0.0:68` $\rightarrow$ `255.255.255.255:67`).
    2. **O**ffer: El servidor DHCP ofrece una configuración IP.
    3. **R**equest: El cliente solicita formalmente la IP ofrecida.
    4. **A**cknowledge: El servidor confirma la concesión (*Lease*).
  - Puertos: **UDP 67 (Servidor)** y **UDP 68 (Cliente)**.
- **DNS (Domain Name System - RFC 1035)**:
  - Puerto: **53 TCP/UDP** (UDP para consultas ordinarias de resolución; TCP para transferencias de zona AXFR/IXFR o respuestas mayores a 512 bytes / DNSSEC).
  - *Tipos de Registros DNS Críticos*:
    - **A**: Mapea nombre a dirección IPv4.
    - **AAAA**: Mapea nombre a dirección IPv6.
    - **CNAME**: Alias canónico que apunta a otro nombre de dominio.
    - **MX**: Servidor de correo entrante para el dominio (incluye prioridad).
    - **PTR**: Resolución inversa (IP $\rightarrow$ Nombre) en `in-addr.arpa`.
    - **NS**: Servidor de nombres autoritativo para la zona.
    - **SOA (Start of Authority)**: Información de autoridad sobre la zona (número de serie, timers de refresco y TTL).
    - **TXT**: Texto arbitrario (usado en SPF, DKIM y DMARC para seguridad de correo).

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 07 (Bloque 4)**
> 1. **Broadcast en IPv6**: En IPv6 **NO existe la dirección de Broadcast** (se usa Multicast).
> 2. **Rango de IPs Privadas Clase B**: Es `172.16.0.0/12` (abarca desde `172.16.0.0` hasta **`172.31.255.255`**; la IP `172.32.1.1` ya es pública).
> 3. **Puertos DHCP**: Servidor escucha en **UDP 67** y el Cliente en **UDP 68**.
> 4. **DNS sobre TCP**: DNS usa TCP para **transferencias de zona (Zone Transfers)** y paquetes mayores a 512 bytes.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Proceso DHCP**: **D - O - R - A** $\rightarrow$ **D**iscover, **O**ffer, **R**equest, **A**cknowledge.
> - **Registros DNS**: **A $=$ IPv4 / AAAA $=$ IPv6 / PTR $=$ Reverso / MX $=$ Mail**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema07|Fuente Oficial del Tema 07]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema07|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema07-redes-tcp-ip|Test Tema 07]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|⬅️ Tema 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|Tema 08 ➡️]]
