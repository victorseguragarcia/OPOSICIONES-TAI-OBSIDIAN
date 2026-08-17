---
title: "Cortafuegos, Redes Privadas Virtuales (VPN) e IPsec"
type: "entity"
tags:
  - firewalls
  - vpn
  - ipsec
  - network-security
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Firewalls"
  - "VPN"
  - "IPsec"
---

# Cortafuegos, Redes Privadas Virtuales (VPN) e IPsec

Los **cortafuegos** y las **VPNs** constituyen las tecnologías fundamentales de protección perimetral e interconexión segura de redes sobre infraestructuras públicas.

---

## 🏛️ Protocolos IPsec (IP Security - RFC 4301)

Operan en la **Capa de Red (Nivel 3)** y constan de dos protocolos de seguridad y un protocolo de gestión de claves:

1. **AH (Authentication Header - RFC 4302, Protocolo IP 51)**:
   - Proporciona autenticación de origen e integridad sin cifrado (**NO aporta confidencialidad**).
   - Incompatible con NAT (el reemplazo de IPs por NAT rompe el hash de integridad de la cabecera IP).
2. **ESP (Encapsulating Security Payload - RFC 4303, Protocolo IP 50)**:
   - Proporciona **confidencialidad (cifrado)**, autenticación e integridad.
   - Compatible con NAT mediante **NAT-Traversal (NAT-T)** encapsulando en **UDP puerto 4500**.
3. **IKE (Internet Key Exchange - IKEv2 RFC 7296)**:
   - Negocia las Asociaciones de Seguridad (SA) y claves criptográficas sobre el puerto **500 UDP**.

### Modos de Operación de IPsec
- **Modo Transporte**: Protege solo la carga útil (*payload*); la cabecera IP original queda visible. Empleado en comunicaciones host-a-host directas.
- **Modo Túnel**: Encapsula el paquete IP original completo dentro de un nuevo paquete IP con una nueva cabecera externa. Empleado en VPNs Site-to-Site y Remote Access.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo / Función | Valor Técnico |
|---------------------|---------------|
| Protocolo IP AH | **Protocolo 51** (Solo autenticación/integridad) |
| Protocolo IP ESP | **Protocolo 50** (Cifrado + autenticación) |
| Puertos IKE / NAT-Traversal | **500 UDP** (IKE) / **4500 UDP** (NAT-T) |
| Puerto OpenVPN Estándar | **1194 UDP/TCP** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
- Síntesis: [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
