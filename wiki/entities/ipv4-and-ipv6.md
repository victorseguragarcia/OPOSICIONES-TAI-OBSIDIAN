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
  - "Protocolo IP"
---

# Protocolos de Red: IPv4 e IPv6

El **Protocolo de Internet (IP)** es el protocolo principal de la capa de red del modelo TCP/IP encargado del direccionamiento no orientado a conexión y del enrutamiento de datagramas.

## IPv4 vs. IPv6
- **IPv4**: Direcciones de 32 bits (4 octetos decimales con punto), espacio de 4.300 millones de direcciones. Fragmentación realizada por routers y host emisor.
- **IPv6**: Direcciones de 128 bits (8 grupos hexadecimales), espacio prácticamente inagotable ($3.4 \times 10^{38}$). Cabecera simplificada de tamaño fijo (40 bytes), fragmentación delegada exclusivamente al host emisor mediante cabeceras de extensión.

## Tipos de Direcciones IPv6
- **Unicast**: Global Unicast (`2000::/3`), Link-Local (`fe80::/10`), Unique Local (`fc00::/7`).
- **Multicast** (`ff00::/8`): Reemplaza a las difusiones broadcast de IPv4.
- **Anycast**: Identificador para un conjunto de interfaces donde el paquete se entrega a la más cercana.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Comparativa: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Detallada IPv4 vs IPv6]]
- Capas: [[wiki/concepts/osi-and-tcp-ip-models|Modelos OSI y TCP-IP]]

