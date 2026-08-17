---
title: "Active Directory Domain Services (AD DS)"
type: "entity"
tags:
  - active-directory
  - ad-ds
  - ldap
  - kerberos
  - windows-server
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Active Directory"
  - "AD DS"
  - "Directorio Activo"
---

# Active Directory Domain Services (AD DS)

**Active Directory Domain Services (AD DS)** es el servicio de directorio distribuido y jerárquico desarrollado por Microsoft para la gestión centralizada de identidades, autenticación, autorización y recursos de red en sistemas operativos Windows Server.

---

## 🏛️ Estructura Lógica y Física

### 1. Jerarquía Lógica
- **Objetos**: Instancias de clases definidas en el Esquema (usuarios, grupos, equipos, impresoras, carpetas compartidas).
- **Unidades Organizativas (OUs)**: Contenedores lógicos dentro de un dominio para agrupar objetos y delegar administración y aplicar GPOs.
- **Dominio**: Límite administrativo y de seguridad fundamental. Comparte una base de datos `NTDS.dit` y directivas de seguridad.
- **Árbol de Dominios**: Conjunto de uno o más dominios que comparten un espacio de nombres DNS contiguo (ej. `tai.gob.es` y `madrid.tai.gob.es`).
- **Bosque (Forest)**: Estructura jerárquica superior. Conjunto de uno o más árboles que comparten un **Catálogo Global**, un **Esquema único** y una **Configuración común**. Representa el límite de seguridad definitivo.

### 2. Estructura Física
- **Controlador de Dominio (DC)**: Servidor que ejecuta AD DS, almacena la base de datos `NTDS.dit` y autentica peticiones.
- **Sitios (Sites)**: Subredes IP interconectadas por enlaces LAN de alta velocidad. Optimiza el tráfico de replicación entre DCs y la localización del DC más cercano por parte de los clientes.
- **Catálogo Global (GC)**: Controlador de dominio que almacena una réplica completa de su propio dominio y una **réplica parcial de solo lectura** de los atributos más consultados de todos los objetos del bosque. Permite búsquedas globales y resolución de UPNs en todo el bosque.
- **Roles FSMO (Flexible Single Master Operations)**:
  - A nivel de Bosque (1 por bosque): Maestro de Esquema (*Schema Master*) y Maestro de Nombres de Dominio (*Domain Naming Master*).
  - A nivel de Dominio (1 por dominio): Emulador PDC (*PDC Emulator* - sincronización horaria NTP y contraseñas), Maestro RID (*RID Master* - asigna bloques de IDs únicos) y Maestro de Infraestructura (*Infrastructure Master*).

### 3. Protocolos y Puertos de Comunicación
- **Kerberos v5**: Puerto **88 TCP/UDP** (autenticación primaria mediante tickets TGT/TGS).
- **LDAP**: Puerto **389 TCP/UDP** (consultas de directorio).
- **LDAPS**: Puerto **636 TCP** (LDAP sobre SSL/TLS).
- **Catálogo Global**: Puerto **3268 TCP** (LDAP GC) y **3269 TCP** (LDAPS GC).
- **DNS**: Puerto **53 TCP/UDP** (localización de DCs mediante registros `SRV`).
- **SMB**: Puerto **445 TCP** (acceso a carpetas compartidas y SYSVOL).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Técnica |
|----------|------------------------|
| Base de Datos de AD | `NTDS.dit` (Motor ESE / Jet Blue) |
| Protocolo de Autenticación | **Kerberos v5** (RFC 4120) en puerto **88 TCP/UDP** |
| Puertos Catálogo Global | **3268 TCP** (Plano) / **3269 TCP** (SSL) |
| Puertos LDAP / LDAPS | **389 TCP/UDP** / **636 TCP** |
| Identificador Único Objeto | **GUID de 128 bits** (inmutable) y **SID** (de seguridad) |
| Formato UPN | `usuario@dominio.com` |
| Orden de Aplicación GPO | **LSDOU**: Local → Sitio → Dominio → OU |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Comparativa y Práctica de Active Directory y LDAP]]
