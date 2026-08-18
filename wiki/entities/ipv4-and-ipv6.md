---
title: "Protocolos de Red: IPv4 e IPv6"
type: "entity"
tags:
  - ipv4
  - ipv6
  - networking
  - ip-protocols
  - addressing
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPv4"
  - "IPv6"
  - "Internet Protocol"
---

# Protocolos de Red: IPv4 e IPv6

El **Protocolo de Internet (IP)** es el protocolo fundamental de la capa de red (Nivel 3) responsable del direccionamiento lógico, enrutamiento y fragmentación de paquetes en la arquitectura de Internet.

---

## 🏛️ Comparativa Técnica Fundamental: IPv4 vs IPv6

| Característica | IPv4 (RFC 791) | IPv6 (RFC 8200) |
|----------------|----------------|-----------------|
| **Longitud de Dirección** | **32 bits (4 bytes)** | **128 bits (16 bytes)** |
| **Espacio de Direcciones** | $\approx 4.29 \times 10^9$ ($2^{32}$) | $\approx 3.4 \times 10^{38}$ ($2^{128}$) |
| **Notación** | Decimal con puntos (`192.168.1.1`) | Hexadecimal con dos puntos (`2001:db8::1`) |
| **Tamaño Cabecera Base** | **20 a 60 bytes** (variable) | **40 bytes FIJOS** |
| **Checksum en Cabecera** | Sí (recalculado en cada salto) | **No** (eliminado para mayor velocidad) |
| **Fragmentación** | Realizada por el emisor y routers | **Solo por el host emisor** (PMTUD) |
| **Tipos de Comunicación** | Unicast, Multicast, **Broadcast** | Unicast, Multicast, **Anycast** (**Sin Broadcast**) |
| **Configuración de IP** | Manual o DHCP | Manual, DHCPv6 o **SLAAC** (RFC 4862) |
| **IPsec** | Opcional (añadido a posteriori) | **Nativo e integrado** en la especificación |

---

## 🧩 Ámbitos y Rangos Especiales

### Rangos IPv4 Notables
- `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`: Direcciones Privadas (RFC 1918).
- `127.0.0.0/8`: Bucle local (*Loopback*).
- `169.254.0.0/16`: APIPA (RFC 3927).
- `224.0.0.0/4`: Clase D (Multicast).

### Rangos IPv6 Notables
- `fe80::/10`: **Enlace Local (Link-Local)** (no enrutable fuera de la subred local).
- `2000::/3`: **Global Unicast (GUA)** (públicas y enrutables en Internet).
- `fc00::/7`: **Unique Local (ULA)** (privadas, típicamente `fd00::/8`).
- `ff00::/8`: **Multicast** (`ff02::1` todos los nodos, `ff02::2` todos los routers).
- `::1/128`: Loopback local.
- `::/128`: Dirección no especificada.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Cabecera IPv4 / IPv6 | **20-60 bytes** / **40 bytes fijos** |
| Longitud Dirección IPv4 / IPv6 | **32 bits** / **128 bits** |
| Prefijo Link-Local IPv6 | `fe80::/10` |
| Prefijo Global Unicast IPv6 | `2000::/3` |
| Campo Equivalente a TTL en IPv6 | **Hop Limit** (8 bits) |
| Campo Protocolo en IPv6 | **Next Header** (8 bits) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos ISO-OSI y TCP-IP]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
