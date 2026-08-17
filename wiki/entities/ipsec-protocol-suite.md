---
title: "Suite de Protocolos IPsec (IP Security)"
type: "entity"
tags:
  - ipsec
  - vpn
  - network-security
  - ah
  - esp
  - ike
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPsec"
  - "IP Security"
  - "AH y ESP"
---

# Suite de Protocolos IPsec (IP Security)

**IPsec (IP Security)** es un conjunto de protocolos y estándares de seguridad definidos por el IETF (RFC 4301) que operan en la **Capa de Red (Nivel 3 del modelo OSI)** para proporcionar confidencialidad, autenticidad de origen, integridad de datos y protección contra reenvíos (*Anti-Replay*) para paquetes IP.

---

## 🏛️ Protocolos de Seguridad Principales

### 1. AH (Authentication Header - RFC 4302)
- **Número de Protocolo IP**: **51**.
- **Servicios**: Proporciona **integridad de datos**, **autenticación de origen** y protección contra reenvíos.
- **Limitación Crítica**: **NO proporciona confidencialidad (NO cifra los datos)**.
- **Incompatibilidad con NAT**: AH calcula el hash de integridad sobre casi toda la cabecera IP original (incluyendo las direcciones IP de origen y destino). Al atravesar un router NAT, la modificación de la IP invalida el checksum de AH, descartando el paquete.

### 2. ESP (Encapsulating Security Payload - RFC 4303)
- **Número de Protocolo IP**: **50**.
- **Servicios**: Proporciona **confidencialidad (cifrado)** mediante algoritmos como AES-CBC o AES-GCM, además de integridad y autenticación opcional.
- **Compatibilidad con NAT (NAT-Traversal / NAT-T - RFC 3948)**:
  - Encapsula los paquetes ESP dentro de datagramas **UDP en el puerto 4500**, permitiendo atravesar routers NAT sin que la traducción de puertos rompa la sesión.

---

## 🧩 Modos de Operación: Transporte vs Túnel

| Característica | Modo Transporte | Modo Túnel |
|----------------|-----------------|------------|
| **Protección** | Solo la **carga útil (payload)** / datos de Capa 4 | **El paquete IP original COMPLETO** (cabecera original + datos) |
| **Cabecera IP** | Mantiene la cabecera IP original visible | Añade una **NUEVA cabecera IP externa** que oculta el origen/destino real |
| **Uso Principal** | Comunicación directa **Host-to-Host** | Conexiones **Site-to-Site (LAN-to-LAN)** y **Remote Access VPN** |
| **Sobrecarga** | Menor tamaño de cabecera | Mayor sobrecarga por la doble cabecera IP |

---

## 🔑 Protocolo IKE (Internet Key Exchange)

- **IKEv1 (RFC 2409) vs IKEv2 (RFC 7296)**: Opera sobre **UDP puerto 500**.
- **Fase 1 (IKE SA)**: Autentica a los pares (mediante certificados X.509 o claves precompartidas PSK) y establece un canal seguro cifrado bidireccional.
- **Fase 2 (IPsec SA / Quick Mode)**: Negocia las Asociaciones de Seguridad (SAs) unidireccionales de AH o ESP para el tráfico de datos real.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Protocolo IP AH | **51** (Solo autenticación e integridad) |
| Protocolo IP ESP | **50** (Cifrado + autenticación) |
| Puerto Negociación IKE | **500 UDP** |
| Puerto NAT-Traversal (NAT-T) | **4500 UDP** |
| RFC Arquitectura IPsec | **RFC 4301** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/firewalls-and-vpn|Cortafuegos y VPN]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
