---
title: "Protocolo SNMP (Simple Network Management Protocol)"
type: "entity"
tags:
  - snmp
  - monitoring
  - networking
  - protocols
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SNMP"
  - "Network Management"
---

# Protocolo SNMP (Simple Network Management Protocol)

**SNMP** es el estándar de la capa de aplicación (UDP puertos 161 y 162) para la monitorización y administración remota de dispositivos de red.

## Arquitectura SNMP
- **NMS (Network Management Station)**: Estación central de monitorización.
- **Agente SNMP**: Proceso ejecutándose en el dispositivo administrado.
- **MIB (Management Information Base)**: Base de datos estructurada en árbol jerárquico de variables y métricas.
- **OID (Object Identifier)**: Identificador numérico único de cada variable en la MIB.

## Versiones de SNMP
- **SNMPv1 / SNMPv2c**: Autenticación simple mediante cadenas de comunidad en texto plano (Community Strings `public`/`private`). Inseguro.
- **SNMPv3**: Incorpora seguridad criptográfica con autenticación (HMAC-MD5/SHA) y cifrado de privacidad (DES, AES), además de control de acceso basado en usuarios (USM y VACM).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Monitorización CPD: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]

