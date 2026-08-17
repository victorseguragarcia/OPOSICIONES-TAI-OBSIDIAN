---
title: "Protocolo DHCP (Dynamic Host Configuration Protocol)"
type: "entity"
tags:
  - dhcp
  - networking
  - protocols
  - lan
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DHCP"
  - "Dynamic Host Configuration Protocol"
---

# Protocolo DHCP (Dynamic Host Configuration Protocol)

**DHCP** (RFC 2131) es un protocolo cliente-servidor de la capa de aplicación que automatiza la asignación dinámica de parámetros de configuración IP (dirección IP, máscara de subred, puerta de enlace, servidores DNS).

---

## 🏛️ Puertos y Proceso de Concesión DORA

- **Puertos Estándar**:
  - **IPv4**: Servidor escucha en **67 UDP**; Cliente escucha en **68 UDP**.
  - **DHCPv6**: Servidor escucha en **547 UDP**; Cliente escucha en **546 UDP**.
- **Fases de la Concesión DORA**:
  1. **Discover (DHCPDISCOVER)**: El cliente envía broadcast (`255.255.255.255`, puerto 67) solicitando IP.
  2. **Offer (DHCPOFFER)**: El servidor responde ofreciendo una IP disponible con parámetros de red.
  3. **Request (DHCPREQUEST)**: El cliente solicita formalmente la IP ofrecida mediante broadcast.
  4. **Acknowledge (DHCPACK)**: El servidor confirma la concesión (*Lease*) y registra la asignación.
- **Tiempos de Renovación**:
  - **T1 (50% del tiempo de concesión)**: Intento de renovación unicast con el servidor emisor original.
  - **T2 (87.5% del tiempo de concesión)**: Si T1 no responde, reenvío en broadcast a cualquier servidor DHCP.
  - **Expiración (100%)**: La IP se libera si no se ha podido renovar.
- **DHCP Relay Agent (RFC 3046 / Opción 82)**: Permite a los routers reenviar las solicitudes broadcast locales hacia un servidor DHCP ubicado en otra subred.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puertos DHCPv4 | **67 UDP (Server)** / **68 UDP (Client)** |
| Puertos DHCPv6 | **547 UDP (Server)** / **546 UDP (Client)** |
| Secuencia de Concesión | **DORA** (Discover, Offer, Request, Acknowledge) |
| Renovación T1 / T2 | **50% (Unicast)** / **87.5% (Broadcast)** |
| IP Autoconfigurada si falla | **APIPA** (`169.254.0.0/16`) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Entidad: [[wiki/entities/dns-protocol|Protocolo DNS]]
- Concepto: [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
