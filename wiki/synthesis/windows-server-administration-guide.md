---
title: "Guía Maestra de Administración de Windows Server para Oposiciones TAI"
type: "synthesis"
tags:
  - synthesis
  - windows-server
  - active-directory
  - hyper-v
  - gpo
  - wsus
  - tai
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Windows Server TAI"
  - "Windows Server Administration Guide"
---

# Guía Maestra de Administración de Windows Server para Oposiciones TAI

Manual integral de preparación sobre arquitectura, servicios de directorio, administración de directivas, almacenamiento, virtualización y herramientas de línea de comandos en **Windows Server** según el programa del Bloque 4.

---

## 🏛️ 1. Arquitectura de Dominio y Servicios de Directorio (AD DS)

### Estructura Jerárquica Lógica
1. **Bosque (Forest)**: Límite de seguridad máximo. Comparte un único Catálogo Global (`GC`), Esquema y Configuración.
2. **Árbol de Dominios**: Uno o más dominios con espacio de nombres DNS contiguo.
3. **Dominio**: Límite administrativo y de replicación de políticas y cuentas.
4. **Unidad Organizativa (OU)**: Contenedor para delegación administrativa y vinculación de **GPOs**.

### Ficheros y Recursos Clave de AD DS
- **`NTDS.dit`**: Base de datos relacional de AD basada en el motor ESE (*Extensible Storage Engine* o Jet Blue). Por defecto ubicada en `%SystemRoot%\NTDS\ntds.dit`.
- **`SYSVOL`**: Carpeta compartida (`\\dominio\SYSVOL`) que almacena las plantillas de directivas de grupo (`GPT`) y scripts de inicio/cierre de sesión. Replicada entre todos los DCs mediante **DFS-R** (anteriormente FRS).
- **Catálogo Global (Global Catalog / GC)**: DC que almacena una réplica parcial de solo lectura de todos los objetos del bosque (puertos **3268 TCP** y **3269 LDAPS**).

---

## 📋 2. Directivas de Grupo (GPOs): Ciclo de Vida y Orden de Aplicación

### Orden de Procesamiento: Regla LSDOU
Las directivas de grupo se procesan de forma acumulativa y secuencial. Las directivas procesadas más tarde sobrescriben las anteriores en caso de conflicto:
1. **L - Local**: Directiva de grupo local del equipo (`gpedit.msc`).
2. **S - Sitio (Site)**: Directivas vinculadas al sitio físico de Active Directory.
3. **D - Dominio**: Directivas vinculadas a nivel de todo el dominio.
4. **OU - Unidad Organizativa**: Directivas vinculadas a las OUs (evaluadas desde la OU padre hacia las OUs hijas anidadas).

### Mecanismos de Excepción en GPOs
- **Herencia Bloqueada (*Block Inheritance*)**: Impide que una OU hija herede las GPOs de los niveles superiores.
- **Directiva Forzada (*Enforced / No Override*)**: Tiene prioridad absoluta; se aplica obligatoriamente incluso si un nivel inferior bloquea la herencia.
- **Filtrado de Seguridad**: Restringe la aplicación de la GPO mediante listas ACL (permiso de *Lectura* y *Aplicar directiva de grupo* a usuarios/grupos específicos).
- **Filtrado WMI**: Aplica la GPO solo si el equipo cumple una consulta WMI (ej. solo equipos con Windows 11 o portátiles con batería).

---

## ⚙️ 3. Roles de Infraestructura de Red en Windows Server

| Servicio | Rol en Windows Server | Características Notables | Puertos |
|----------|-----------------------|--------------------------|---------|
| **DNS Server** | `DNS` | Zonas integradas en AD, DNS dinámico seguro, registros SRV | **53 TCP/UDP** |
| **DHCP Server** | `DHCP` | Failover DHCP (Load Balance / Hot Standby), Opciones DHCP | **67 UDP / 68 UDP** |
| **Actualizaciones** | `WSUS` | Descarga centralizada y aprobación por grupos de equipos | **8530 HTTP / 8531 HTTPS** |
| **Escritorio Remoto** | `RDS` | RemoteApp, RD Gateway, RD Connection Broker, RD Web | **3389 TCP/UDP** |
| **Servidor Web** | `Web-Server (IIS)` | Módulos desacoplados, Application Pools independientes | **80 TCP / 443 TCP** |
| **Gestión Remota** | `WinRM` | Administración remota mediante PowerShell remoting | **5985 HTTP / 5986 HTTPS** |

---

## 💾 4. Almacenamiento y Virtualización en Windows Server

### Hyper-V (Hipervisor Tipo 1)
- Hipervisor nativo integrado en el kernel.
- **Tipos de Conmutadores Virtuales (vSwitches)**:
  - **Externo**: Conecta las VMs con la red física externa a través de la tarjeta de red física del host.
  - **Interno**: Permite la comunicación entre VMs y con el sistema operativo host (sin salida a la red física exterior).
  - **Privado**: Permite exclusivamente la comunicación entre VMs que residen en el mismo host físico (el host no tiene acceso a esta red virtual).
- **Migración en Caliente (Live Migration)**: Mueve la memoria y el estado de la VM por la red sin corte de servicio hacia otro nodo del clúster de conmutación por error (*Failover Cluster*).

### DFS y Sistemas de Archivos
- **DFS-N**: Espacio de nombres único (`\\empresa.local\datos`).
- **DFS-R**: Replicación delta eficiente con compresión diferencial remota.
- **Sistemas de Ficheros**:
  - **NTFS**: Soporta ACLs, compresión, cifrado EFS, cuotas de disco y transacciones.
  - **ReFS (Resilient File System)**: Diseñado para máxima resiliencia contra corrupción de metadatos, clonación rápida de bloques para VMs Hyper-V y volúmenes masivos con Storage Spaces Direct.

---

## 🛠️ 5. Tabla Maestra de Comandos y Consolas de Administración

| Tarea Administrativa | Consola Gráfica (MMC) | Comando de Consola (CMD) | Cmdlet de PowerShell |
|----------------------|-----------------------|--------------------------|----------------------|
| **Gestión de Usuarios AD** | `dsa.msc` | `net user <usr> /domain` | `Get-ADUser`, `New-ADUser` |
| **Directivas de Grupo** | `gpmc.msc` / `gpedit.msc` | `gpresult /r` | `Get-GPO`, `New-GPO` |
| **Forzar Directivas** | N/A | `gpupdate /force` | `Invoke-GPUpdate` |
| **Visor de Eventos** | `eventvwr.msc` | `wevtutil` | `Get-WinEvent`, `Get-EventLog` |
| **Administración Discos** | `diskmgmt.msc` | `diskpart` | `Get-Disk`, `Get-Volume` |
| **Monitor de Recursos** | `resmon.exe` / `perfmon.msc` | `typeperf` | `Get-Counter` |
| **Configuración de Red** | `ncpa.cpl` | `netsh interface ip ...` | `Get-NetIPAddress`, `Set-NetIPAddress` |
| **Diagnóstico de Red** | N/A | `ipconfig /all`, `tracert` | `Test-NetConnection -Port 443` |
| **Servicios del Sistema** | `services.msc` | `sc query`, `net start` | `Get-Service`, `Start-Service` |

---

## 🎯 Datos Clave para Oposiciones TAI

| Pregunta Típica de Examen | Respuesta Correcta |
|---------------------------|--------------------|
| ¿Cuál es el orden de aplicación de las directivas de grupo en Active Directory? | **LSDOU (Local $\rightarrow$ Sitio $\rightarrow$ Dominio $\rightarrow$ Unidad Organizativa)** |
| ¿Qué puerto utiliza el servicio de Catálogo Global en Active Directory sobre LDAP seguro? | **Puerto 3269 TCP (3268 en texto plano)** |
| ¿Qué protocolo de replicación utiliza SYSVOL en Windows Server modernos? | **DFS-R (Distributed File System Replication)** |
| ¿Qué tipo de hipervisor es Microsoft Hyper-V? | **Hipervisor de Tipo 1 (Bare-Metal / Nativo)** |
| ¿Qué comando de consola muestra el informe RSoP de directivas aplicadas? | **`gpresult /r`** o la consola **`rsop.msc`** |
| ¿Cuáles son los puertos estándar de PowerShell Remoting (WinRM)? | **5985 TCP (HTTP)** y **5986 TCP (HTTPS)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Active Directory y LDAP]]
- Síntesis: [[wiki/synthesis/sysadmin-commands-windows-and-linux-cheatsheet|Cheatsheet de Comandos Sysadmin]]
