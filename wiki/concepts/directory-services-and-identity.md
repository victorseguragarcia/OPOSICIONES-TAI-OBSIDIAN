---
title: "Servicios de Directorio y Gestión de Identidades"
type: "concept"
tags:
  - directory-services
  - identity
  - ldap
  - active-directory
  - sso
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Servicios de Directorio"
  - "Directory Services"
---

# Servicios de Directorio y Gestión de Identidades

Un **servicio de directorio** es un sistema de software especializado que almacena, organiza y proporciona acceso seguro y jerárquico a información sobre usuarios, grupos, equipos y recursos de red en una organización.

---

## 🏛️ Características y Diferencias frente a RDBMS

| Característica | Servicio de Directorio (LDAP / AD) | Base de Datos Relacional (RDBMS) |
|----------------|-------------------------------------|----------------------------------|
| **Perfil de Carga** | **Altamente optimizado para LECTURAS** ($>90\%$) | Equilibrado entre Lecturas y Escrituras masivas |
| **Estructura de Datos** | **Jerárquica en Árbol (DIT)** | Tablas bidimensionales normalizadas |
| **Esquema** | Extensible mediante clases de objetos y atributos | Esquema estricto de tablas y claves |
| **Protocolo de Acceso** | **LDAPv3 (RFC 4511)** / Kerberos | SQL (DDL, DML) vía ODBC/JDBC |
| **Replicación** | Multimaestro o maestro-esclavo optimizada para WAN | Replicación transaccional síncrona/asíncrona |

---

## 🧩 Protocolos y Autenticación Centralizada

- **X.500 / LDAPv3**: Estándares de consulta y esquema de nombrado mediante nombres distinguidos (**DN**).
- **Kerberos v5 (RFC 4120)**: Protocolo de autenticación basado en un Centro de Distribución de Claves (**KDC**) que emite tickets de concesión de tickets (**TGT**) y tickets de servicio (**TGS**), evitando el envío de contraseñas por la red.
- **Single Sign-On (SSO)**: Permite al usuario autenticarse una sola vez y acceder a múltiples sistemas autorizados (mediante Kerberos, SAML 2.0, OpenID Connect / OAuth 2.0).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Técnica |
|----------|------------------------|
| Puerto LDAP / LDAPS | **389 TCP/UDP** / **636 TCP** |
| Puerto Kerberos KDC | **88 TCP/UDP** |
| Estándar de Certificados | **X.509** |
| Formato de Exportación | **LDIF** (RFC 2849) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Active Directory y LDAP]]
