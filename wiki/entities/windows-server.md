---
title: "Windows Server y Administración de Dominios"
type: "entity"
tags:
  - windows
  - windows-server
  - active-directory
  - operating-systems
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Windows Server"
  - "Administración Windows"
---

# Windows Server y Administración de Dominios

**Windows Server** es la línea de sistemas operativos empresariales de Microsoft diseñada para la provisión de servicios centralizados de red, almacenamiento, identidad y virtualización.

---

## 🏛️ Roles y Servicios Principales

- **Active Directory Domain Services (AD DS)**:
  - Servicio de directorio LDAP/Kerberos centralizado para la autenticación y autorización en redes empresariales.
  - Almacena identidades de usuarios, grupos, equipos y políticas en la base de datos `NTDS.dit`.
- **Servicios de Infraestructura de Red**:
  - **DNS Server**: Rol integrado de resolución de nombres con zonas integradas en Active Directory replicadas de forma segura.
  - **DHCP Server**: Asignación automática de IPs con soporte de *Failover DHCP* en modo activo-activo o activo-pasivo.
  - **WSUS (Windows Server Update Services)**: Servidor de distribución y aprobación de parches en intranet.
- **Seguridad y Control de Acceso**:
  - **GPO (Group Policy Objects)**: Administración masiva de configuraciones y directivas de seguridad para usuarios y equipos.
  - **BitLocker**: Cifrado completo de volúmenes de disco mediante chips TPM.
  - **AppLocker / Windows Defender Application Control**: Listas blancas de ejecutables y scripts autorizados.
- **Almacenamiento y Virtualización**:
  - **Hyper-V**: Hipervisor de Tipo 1 (Bare-metal) integrado en Windows Server.
  - **Storage Spaces Direct (S2D)**: Almacenamiento definido por software para clústeres hiperconvergentes.
  - **DFS (Distributed File System)**: Espacio de nombres unificado (DFS-N) y replicación de carpetas (DFS-R).

---

## 🎯 Datos Clave para Oposiciones TAI

| Rol / Herramienta | Función / Comando |
|-------------------|-------------------|
| Editor de Directivas | `gpedit.msc` (Local) / `gpmc.msc` (Consola de Dominio) |
| Actualizar Directivas | `gpupdate /force` |
| Ver Informe Directivas | `gpresult /r` o `rsop.msc` |
| Visor de Eventos | `eventvwr.msc` |
| Administrador de Discos | `diskmgmt.msc` / comando `diskpart` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
