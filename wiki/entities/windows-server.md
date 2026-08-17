---
title: "Windows Server: Arquitectura, Roles, Servicios y Administración de Dominios"
type: "entity"
tags:
  - windows
  - windows-server
  - active-directory
  - hyper-v
  - wsus
  - gpo
  - powershell
  - sysadmin
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Windows Server"
  - "Administración Windows Server"
  - "Roles y Servicios Windows Server"
---

# Windows Server: Arquitectura, Roles, Servicios y Administración de Dominios

**Windows Server** es la plataforma de sistemas operativos de servidor de Microsoft diseñada para la gestión empresarial de identidades, almacenamiento definido por software, virtualización de hipervisor nativo, infraestructura de red y servicios de aplicaciones corporativas.

---

## 🏛️ Evolución de Versiones y Opciones de Instalación

### 1. Evolución Histórica de Versiones
- **Windows NT 4.0 Server (1996)**: Modelo de dominios clásico NT (PDC/BDC) y arquitectura de seguridad SAM.
- **Windows 2000 Server (2000)**: Introducción revolucionaria de **Active Directory**, DNS dinámico y Kerberos v5.
- **Windows Server 2003 / 2003 R2**: Consolidación de AD, volumen shadow copy (VSS) y roles modulares.
- **Windows Server 2008 / 2008 R2**: Introducción de **Hyper-V**, instalación **Server Core**, **PowerShell**, y renombrado a **AD DS**.
- **Windows Server 2012 / 2012 R2**: Storage Spaces, IPAM (IP Address Management), Hyper-V réplica.
- **Windows Server 2016 / 2019 / 2022**: Contenedores Windows nativos, Storage Spaces Direct (S2D), clústeres hiperconvergentes (HCI), soporte TLS 1.3 nativo, DNS sobre HTTPS (DoH) y Secured-core Server.

### 2. Opciones de Instalación y Ediciones
- **Opciones de Instalación**:
  - **Server Core (Recomendada)**: Instalación sin interfaz gráfica de usuario (GUI). Administrada exclusivamente mediante **PowerShell**, **Windows Admin Center** o **RSAT** (Remote Server Administration Tools). Reduce drásticamente la superficie de ataque, el consumo de memoria RAM y la necesidad de reinicios por parches.
  - **Servidor con Experiencia de Escritorio (Desktop Experience)**: Instalación completa con GUI y consolas gráficas MMC tradicionales.
- **Ediciones Principales**:
  - **Datacenter**: Para entornos altamente virtualizados y centros de datos en la nube (máquinas virtuales y contenedores Hyper-V **ilimitados**, Storage Spaces Direct, redes definidas por software SDN).
  - **Standard**: Para entornos físicos o de baja densidad de virtualización (permite ejecutar **hasta 2 entornos de sistema operativo / VMs** con la misma licencia de núcleos).
  - **Essentials**: Para pequeñas empresas de hasta 25 usuarios y 50 dispositivos (sin necesidad de CALs).

---

## 🧩 Roles de Servidor Fundamentales (Server Roles)

```
                            Roles Principales en Windows Server
                                             │
      ┌────────────────────┬─────────────────┼─────────────────┬──────────────────┐
      ▼                    ▼                 ▼                 ▼                  ▼
    AD DS             Hyper-V           Infraestructura   Almacenamiento     Acceso / Web
(Identidades      (Hipervisor Tipo 1    (DNS, DHCP,       (S2D, DFS-N/R,    (RDS / Terminal,
 y Políticas GPO)  y Virtualización)     WSUS, IPAM)       iSCSI Target)     IIS, WinRM)
```

### 1. Active Directory Domain Services (AD DS)
- Base de datos distribuida y jerárquica (`NTDS.dit`) que gestiona usuarios, grupos, equipos y políticas en dominios, árboles y bosques.
- **Autenticación Kerberos v5** (puerto **88 TCP/UDP**), directorio **LDAP/LDAPS** (puertos **389 / 636**), y **Catálogo Global** (puertos **3268 / 3269**).
- **Directivas de Grupo (GPO)**: Aplicadas en orden estricto **LSDOU** (Local $\rightarrow$ Sitio $\rightarrow$ Dominio $\rightarrow$ Unidad Organizativa).

### 2. Hyper-V (Virtualización de Servidores)
- Hipervisor de **Tipo 1 (Bare-Metal)** que se ejecuta directamente sobre el hardware.
- Características avanzadas de clúster:
  - **Live Migration**: Migración en caliente de máquinas virtuales entre hosts sin tiempo de inactividad.
  - **Hyper-V Replica**: Replicación asíncrona de VMs a través de WAN hacia un sitio de contingencia.
  - **Dynamic Memory**: Asignación elástica y recuperación de memoria RAM en tiempo real.
  - **Formatos de Disco Virtual**: **VHD** (máximo 2 TB) y **VHDX** (hasta 64 TB, con protección contra corrupción por cortes eléctricos).

### 3. Servicios de Infraestructura de Red
- **DNS Server**: Soporta **Zonas integradas en Active Directory** (almacenadas en la partición de directorio y replicadas de forma segura y multimaestro), actualizaciones dinámicas seguras y registros `SRV` de localización de controladores de dominio.
- **DHCP Server**: Soporta **Failover DHCP** en modo activo-activo (reparto de carga) o activo-pasivo (conmutación por error), exclusiones, reservas ligadas a dirección MAC y opciones DHCP (Opción 3 Gateway, Opción 6 DNS, Opción 15 Dominio).
- **WSUS (Windows Server Update Services)**: Servidor local de descarga, filtrado, aprobación y distribución de actualizaciones de Microsoft para los puestos y servidores de la red interna, configurado en los clientes mediante directivas de grupo GPO (`gpedit.msc`).

### 4. Almacenamiento y Servicios de Archivos
- **DFS (Distributed File System)**:
  - **DFS-N (Namespaces)**: Agrupa carpetas compartidas ubicadas en diferentes servidores bajo una única estructura jerárquica virtual transparente (ej. `\\dominio\publico`).
  - **DFS-R (Replication)**: Motor de replicación multimaestro diferencial mediante el algoritmo RDC (*Remote Differential Compression*). Reemplazó al antiguo servicio FRS para la replicación del recurso `SYSVOL`.
- **Storage Spaces Direct (S2D)**: Agrupa discos locales SATA, SAS y NVMe de varios servidores para crear un pool de almacenamiento compartido hiperconvergente de alta disponibilidad sin necesidad de cabinas SAN dedicadas.
- **VSS (Volume Shadow Copy Service)**: Infraestructura para crear instantáneas (*Snapshots*) consistentes de volúmenes en caliente mientras las aplicaciones y bases de datos siguen abiertas.

### 5. Servicios de Acceso Remoto y Aplicaciones
- **RDS (Remote Desktop Services / Terminal Services)**: Permite a múltiples usuarios conectarse simultáneamente a escritorios virtuales o aplicaciones remotas (**RemoteApp**) sobre el protocolo **RDP (puerto 3389 TCP/UDP)**.
- **IIS (Internet Information Services)**: Servidor web modular corporativo de Microsoft para alojar sitios web HTTP/HTTPS, aplicaciones ASP.NET y servicios REST.

---

## 🛠️ Herramientas y Consolas de Administración de Windows Server

| Herramienta / Consola | Comando de Ejecución | Función Administrativa |
|-----------------------|----------------------|------------------------|
| **Administrador del Servidor** | `ServerManager.exe` | Consola central de aprovisionamiento de roles y características |
| **Usuarios y Equipos de AD** | `dsa.msc` | Gestión de cuentas de usuario, grupos y unidades organizativas |
| **Administración de Directivas de Grupo** | `gpmc.msc` | Creación, vinculación y edición de objetos GPO en el dominio |
| **Editor de Directivas Locales** | `gpedit.msc` | Configuración de directivas en la máquina local |
| **Actualización de Directivas** | `gpupdate /force` | Fuerza la reaplicación inmediata de las GPOs sin esperar al intervalo |
| **Informe de Directivas Aplicadas** | `gpresult /r` o `rsop.msc` | Muestra el Conjunto Resultante de Directivas (RSoP) del usuario/equipo |
| **Administrador de Hyper-V** | `virtmgmt.msc` | Creación y administración de máquinas virtuales y switches virtuales |
| **Administrador de Discos** | `diskmgmt.msc` / `diskpart` | Particionado de discos MBR/GPT y formateo NTFS/ReFS |
| **Visor de Eventos** | `eventvwr.msc` | Consulta de registros de eventos (Application, Security, System) |
| **Monitor de Rendimiento** | `perfmon.msc` | Análisis de contadores de CPU, memoria, disco y red en tiempo real |
| **Configuración del Sistema** | `msconfig.exe` | Ajustes de arranque y servicios de diagnóstico |
| **Configuración de Red por CLI** | `netsh` | Configuración de interfaces IP, firewall y perfiles WLAN |

---

## 💻 Cmdlets de PowerShell Esenciales para Windows Server

```powershell
# Instalación de Roles y Características
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
Install-WindowsFeature -Name Web-Server -IncludeAllSubFeature

# Gestión de Active Directory
New-ADUser -Name "Juan Perez" -SamAccountName "jperez" -AccountPassword (ConvertTo-SecureString "Pass123!" -AsPlainText -Force) -Enabled $true
Get-ADUser -Filter * -Properties * | Select-Object Name, SamAccountName, LastLogonDate
Get-ADDomainController -Filter * | Select-Object Name, IPv4Address, OperatingSystem

# Gestión de Red e Interfaces
Get-NetIPAddress | Where-Object { $_.InterfaceAlias -eq "Ethernet" }
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.10 -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses ("192.168.1.10", "192.168.1.11")

# Ejecución Remota de Comandos (WinRM)
Invoke-Command -ComputerName "SRV-DC01", "SRV-WEB01" -ScriptBlock { Get-Service -Name W32Time }
```

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Servicio | Especificación Técnica |
|---------------------|------------------------|
| Base de Datos de AD DS | **`NTDS.dit`** (Motor Jet Blue / ESE) |
| Recurso Replicado de GPOs | **`SYSVOL`** (Replicado mediante DFS-R) |
| Orden de Evaluación de Directivas | **LSDOU** (Local, Sitio, Dominio, Unidad Organizativa) |
| Puerto RDP (Escritorio Remoto) | **3389 TCP/UDP** |
| Puertos WinRM (PowerShell Remoto) | **5985 HTTP** / **5986 HTTPS** |
| Protocolo Autenticación Dominio | **Kerberos v5** (Puerto **88 TCP/UDP**) |
| Tipo de Hipervisor Hyper-V | **Tipo 1 (Bare-Metal)** |
| Formato de Disco Virtual Moderno | **VHDX** (hasta 64 TB) |
| Licencias Windows Server Core | Basadas en **núcleos físicos de CPU (mínimo 16 núcleos por servidor)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services (AD DS)]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Comparativa de Active Directory y LDAP]]
- Síntesis: [[wiki/synthesis/sysadmin-commands-windows-and-linux-cheatsheet|Cheatsheet de Comandos Sysadmin]]
