---
title: "Protocolo SNMP (Simple Network Management Protocol)"
type: "entity"
tags:
  - snmp
  - monitoring
  - network-management
  - protocols
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SNMP"
  - "Simple Network Management Protocol"
---

# Protocolo SNMP (Simple Network Management Protocol)

**SNMP** es un protocolo de la capa de aplicación de la pila TCP/IP diseñado para la monitorización, gestión y administración de dispositivos de red (routers, switches, servidores, impresoras).

---

## 🏛️ Arquitectura y Puertos

- **Componentes**:
  - **NMS (Network Management Station)**: Estación de administración que ejecuta el software de monitorización.
  - **Agente SNMP**: Proceso que corre en el dispositivo gestionado y mantiene la información de estado.
  - **MIB (Management Information Base)**: Base de datos jerárquica y estructurada de objetos gestionables representados mediante identificadores **OID** (Object Identifiers en formato ASN.1).
- **Puertos Estándar**:
  - **161 UDP**: Consultas y modificaciones estándar (`GetRequest`, `SetRequest`, `GetNextRequest`, `GetBulkRequest`).
  - **162 UDP**: Notificaciones asíncronas no solicitadas enviadas por los agentes (**SNMP Traps** e `InformRequest`).

---

## 🧩 Evolución de Versiones

- **SNMPv1 (RFC 1157)**: Autenticación básica en texto plano mediante cadenas de comunidad (*Community Strings*: `public` / `private`). Inseguro.
- **SNMPv2c (RFC 1901)**: Añade la operación eficiente `GetBulkRequest` y tipos de datos de 64 bits (contadores de tráfico de interfaces gigabit), pero mantiene autenticación débil por comunidad.
- **SNMPv3 (RFC 3411-3418)**: Introduce el marco de seguridad completo **USM** (User-Based Security Model) con:
  - **Autenticación**: HMAC-MD5, HMAC-SHA (SHA-1, SHA-256, SHA-512).
  - **Confidencialidad (Cifrado)**: DES, 3DES, **AES** (AES-128, AES-192, AES-256).
  - Niveles de seguridad: `noAuthNoPriv`, `authNoPriv`, `authPriv`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto Consultas SNMP | **161 UDP** |
| Puerto SNMP Traps | **162 UDP** |
| Versión Segura con Cifrado | **SNMPv3** (Modelo USM con HMAC y AES) |
| Estructura de Datos | **MIB** (identificada por OIDs) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Entidad: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
