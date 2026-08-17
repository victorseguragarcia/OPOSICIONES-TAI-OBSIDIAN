---
title: "Guía Comparativa y Práctica de Active Directory y LDAP"
type: "synthesis"
tags:
  - synthesis
  - active-directory
  - ldap
  - identity
  - windows-server
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía AD y LDAP"
  - "Active Directory & LDAP Guide"
---

# Guía Comparativa y Práctica de Active Directory y LDAP

Estudio exhaustivo de los servicios de directorio empresariales, el estándar LDAPv3 y la arquitectura de Active Directory Domain Services (AD DS).

---

## 🏛️ Comparativa: LDAP Abierto vs Active Directory

| Aspecto | Servidor LDAP Abierto (OpenLDAP) | Active Directory Domain Services (AD DS) |
|---------|-----------------------------------|------------------------------------------|
| **Proveedor / Licencia** | Código abierto (OpenLDAP License) | Propietario de Microsoft (Windows Server) |
| **Protocolo de Directorio** | LDAPv3 estricto (RFC 4511) | LDAPv3 + Extensiones propietarias de Microsoft |
| **Autenticación Primaria** | Simple Bind / SASL | **Kerberos v5** nativo integrado |
| **Gestión de Políticas** | No integrada (requiere herramientas externas) | **GPO (Group Policy Objects)** integradas |
| **Resolución de Nombres** | Independiente | Estrechamente acoplado con **DNS dinámico** |
| **Replicación** | Syncrepl (Maestro-Esclavo / Multimaestro) | Replicación Multimaestro de particiones de directorio |

---

## 🎯 Datos Clave para Oposiciones TAI

- **Puertos**: LDAP (**389**), LDAPS (**636**), Kerberos (**88**), GC (**3268**), GC-SSL (**3269**).
- **Esquema de Nombres Distinguidos (DN)**: `CN=Nombre,OU=Unidad,DC=dominio,DC=com`.
- **Estructura AD**: Dominios $ightarrow$ Árboles $ightarrow$ Bosques.
- **Roles FSMO**: 5 roles (2 de bosque: Schema Master, Domain Naming Master; 3 de dominio: PDC Emulator, RID Master, Infrastructure Master).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
