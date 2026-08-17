---
title: "Cortafuegos y Redes Privadas Virtuales (VPN)"
type: "entity"
tags:
  - firewalls
  - vpn
  - ipsec
  - wireguard
  - security
  - network-security
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Firewalls"
  - "VPN"
  - "IPsec"
  - "Seguridad Perimetral"
---

# Cortafuegos y Redes Privadas Virtuales (VPN)

Tecnologías centrales para el aislamiento perimetral y la interconexión cifrada de sedes y usuarios remotos.

## Tipologías de Cortafuegos
1. **Filtrado de Paquetes Stateless**: Inspección básica de IPs, puertos y flags TCP en Capa 3/4.
2. **Stateful Inspection**: Mantiene una tabla de estado de conexiones para autorizar respuestas legítimas.
3. **Next-Generation Firewalls (NGFW)**: Inspección profunda de paquetes (DPI) en Capa 7, control de aplicaciones y prevención de amenazas integrada.
4. **WAF (Web Application Firewall)**: Protección especializada contra ataques web (OWASP Top 10: SQLi, XSS, CSRF).

## Tecnologías VPN
- **IPsec**: Protocolo en Capa 3 con modos Transporte y Túnel. Protocolos AH (autenticación e integridad) y ESP (cifrado y autenticación).
- **SSL/TLS VPN** (OpenVPN): Opera en Capa de Transporte/Aplicación.
- **WireGuard**: Protocolo VPN moderno, simple y de alto rendimiento en el kernel Linux.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Normativa: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

