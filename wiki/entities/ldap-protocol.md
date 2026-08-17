---
title: "Protocolo LDAP y Estándar X.500"
type: "entity"
tags:
  - ldap
  - x500
  - directory-services
  - protocols
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "LDAP"
  - "X.500"
  - "Lightweight Directory Access Protocol"
---

# Protocolo LDAP y Estándar X.500

El protocolo **LDAP (Lightweight Directory Access Protocol)** es un estándar abierto de la capa de aplicación diseñado para consultar y modificar servicios de información de directorio distribuidos sobre redes IP.

---

## 🏛️ Historia y Estándares

- **Origen en ITU-T X.500**: La serie X.500 de la ITU-T (desarrollada junto con ISO) definió un modelo integral de directorio distribuido para soportar la mensajería X.400. Sin embargo, su protocolo de acceso nativo (**DAP**) era excesivamente pesado al requerir la pila completa OSI.
- **Nacimiento de LDAP ("X.500 Lite")**: Creado por la Universidad de Michigan y estandarizado por el IETF para operar directamente sobre la pila **TCP/IP**.
- **Versión Actual**: **LDAPv3** formalizado en **RFC 4511** (hoja de ruta en **RFC 4510**).
- **Puertos Estándar**:
  - **389 TCP/UDP**: LDAP estándar en texto plano (soporta actualización a conexión segura mediante la operación `StartTLS`).
  - **636 TCP**: LDAPS legado (LDAP encapsulado directamente en un túnel SSL/TLS).

---

## 🧩 Modelo de Información y Sintaxis

- **Estructura Jerárquica DIT (Directory Information Tree)**:
  - Los datos se organizan en forma de árbol jerárquico.
  - Cada entrada del directorio posee un nombre unívoco llamado **DN (Distinguished Name)**.
  - El DN se compone de una secuencia de **RDNs (Relative Distinguished Names)** separados por comas:
    - `CN`: Common Name (ej. `CN=Carlos Sanchez`)
    - `OU`: Organizational Unit (ej. `OU=Desarrollo`)
    - `DC`: Domain Component (ej. `DC=tai,DC=gob,DC=es`)
    - `O`: Organization (ej. `O=Ministerio`)
    - `C`: Country (ej. `C=ES`)
- **Esquema de Directorio**:
  - **ObjectClasses**: Definen qué tipos de objetos pueden existir y qué atributos son obligatorios (`MUST`) u opcionales (`MAY`). Tipos: estructurales, auxiliares y abstractas (`top`).
  - **Sintaxis y Reglas de Coincidencia**: Codificado en **ASN.1** y transmitido usando **BER** (Basic Encoding Rules).

---

## 🎯 Operaciones del Protocolo LDAPv3

| Operación | Descripción |
|-----------|-------------|
| `Bind` | Autentica al cliente ante el servidor LDAP (anónima, simple o SASL) |
| `Search` | Busca y recupera entradas en base a un filtro de búsqueda (ej. `(&(objectClass=user)(mail=*@gob.es))`) |
| `Compare` | Verifica si una entrada posee un valor de atributo específico |
| `Add` / `Delete` | Añade o elimina una entrada del DIT |
| `Modify` | Modifica atributos de una entrada existente (añadir, reemplazar, borrar valores) |
| `ModifyDN` | Renombra o mueve una entrada en el árbol jerárquico |
| `StartTLS` | Negocia cifrado TLS sobre la conexión existente en el puerto 389 |
| `Abandon` | Cancela una operación asíncrona enviada previamente |
| `Unbind` | Cierra la sesión y la conexión TCP con el servidor |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| RFC LDAPv3 | **RFC 4511** (Sintaxis RFC 4512) |
| Puerto LDAP / LDAPS | **389 TCP/UDP** / **636 TCP** |
| Lenguaje de Descripción | **ASN.1** (Abstract Syntax Notation One) |
| Codificación en Red | **BER** (Basic Encoding Rules) |
| Formato de Intercambio de Datos | **LDIF** (LDAP Data Interchange Format - RFC 2849) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Concepto: [[wiki/concepts/directory-services-and-identity|Servicios de Directorio y Gestión de Identidades]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Comparativa y Práctica de Active Directory y LDAP]]
