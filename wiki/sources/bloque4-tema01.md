---
title: "Resumen Fuente: Bloque 4 - Tema 01: Administración del Sistema Operativo y Software de Base"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema01
  - sistemas-operativos
  - active-directory
  - ldap
  - bash
  - powershell
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Administración del Sistema Operativo y Software de Base"
  - "bloque4-tema01"
---

# Resumen Fuente: Bloque 4 - Tema 01: Administración del Sistema Operativo y Software de Base

Resumen estructurado y puntos clave procesados desde la fuente original [[raw/sources/bloque4-tema01.md|bloque4-tema01.md]].

---

## 📖 Resumen Ejecutivo

Este tema abarca la administración integral del sistema operativo y el software de base en infraestructuras corporativas. Cubre la clasificación del software (sistemas vs. aplicación), firmware (BIOS vs. UEFI con Secure Boot), evolución de los sistemas operativos (monolíticos, jerárquicos, microkernels), servicios de directorio distribuidos (X.500, LDAPv3, eDirectory de Novell, Active Directory Domain Services de Microsoft), funciones del administrador de sistemas, gestión de actualizaciones masivas (WSUS, unattended-upgrades), herramientas de línea de comandos de diagnóstico de red y scripting avanzado con Bash y PowerShell, auditoría mediante logs, y tendencias de gestión móvil (BYOD, MDM).

---

## 🧩 Estructura y Desglose Temático

### 1. Software de Base y Firmware
- **Firmware de arranque**:
  - **BIOS** (Basic Input/Output System): Firmware en ROM/Flash que ejecuta el POST (Power-On Self-Test) y arranca el gestor de arranque en modo de 16 bits.
  - **UEFI** (Unified Extensible Firmware Interface): Especificación moderna escrita en C. Soporta tablas de particiones GPT (>2 TB), arranque seguro (**Secure Boot** con firmas criptográficas), diagnóstico avanzado y gestión de red previa al SO (PXE, Wake-on-LAN).
- **Funciones del Sistema Operativo**:
  - Gestor de recursos: CPU (CFS, prioridades `nice`), Memoria (paginación, swap, MMU), E/S (drivers, DMA, interrupciones) y Almacenamiento (VFS, inodos).
  - Estructura monolítica vs. modular/microkernel.

### 2. Servicios de Directorio y Gestión de Identidades
Un servicio de directorio almacena información sobre identidades y recursos con optimización para **altas tasas de lectura** y búsquedas jerárquicas mediante esquemas extensibles.

#### 2.1 Serie ITU-T X.500 y Protocolo LDAP
- **X.500**: Conjunto de estándares ITU-T/ISO de la capa de aplicación para directorios distribuidos. Diseñado para soportar el sistema de mensajería X.400. Incluye DAP (Directory Access Protocol) y la especificación **X.509** para certificados digitales.
- **LDAP (Lightweight Directory Access Protocol)**:
  - Definido en **RFC 4511** (hoja de ruta en RFC 4510), versión actual **LDAPv3**.
  - Puertos estándar: **389 TCP/UDP** (LDAP en texto plano / StartTLS) y **636 TCP** (LDAPS sobre SSL/TLS).
  - Utiliza sintaxis **ASN.1** y codificación **BER** (Basic Encoding Rules).
  - Formato de nombres distinguidos (DN): `CN=Juan Perez,OU=Informatica,DC=tai,DC=gob,DC=es`.
  - Operaciones: `Bind`, `Search`, `Compare`, `Add`, `Delete`, `Modify`, `ModifyDN`, `Abandon`, `StartTLS`, `Unbind`.

#### 2.2 eDirectory de Novell (NetIQ)
- Base de datos jerárquica y orientada a objetos (anteriormente NDS).
- Soporta replicación multimaestro, herencia dinámica de derechos y el servicio **NMAS** (Novell Modular Authentication Service) para autenticación multifactor y federada.

#### 2.3 Active Directory Domain Services (AD DS)
- Introducido en Windows 2000 Server; formalizado como AD DS en Windows Server 2008 hasta versiones actuales (2016, 2019, 2022).
- **Jerarquía lógica**:
  - **Dominio**: Límite de seguridad y replicación que comparte base de datos NTDS y directivas.
  - **Árbol**: Conjunto de dominios que comparten un espacio de nombres DNS contiguo.
  - **Bosque (Forest)**: Límite de seguridad máximo de AD. Comparte un único Catálogo Global y Esquema común.
- **Componentes críticos**:
  - `NTDS.dit`: Base de datos de AD basada en el motor ESE (Extensible Storage Engine).
  - `SYSVOL`: Recurso compartido replicado vía DFS-R que almacena scripts de inicio y GPOs.
  - **Kerberos v5**: Protocolo primario de autenticación mediante tickets (TGT, TGS).
  - **Catálogo Global (GC)**: Puerto TCP 3268 (3269 SSL), contiene réplica parcial de solo lectura de todos los objetos del bosque.
- **Relaciones de Confianza (Trusts)**:
  - Transitivas / No transitivas.
  - De acceso directo (Shortcut), de Bosque (Forest Trust), Externas (External) y de Dominio.
- **Directivas de Grupo (GPOs)**:
  - Orden de procesamiento: **LSDOU** (Local → Sitio → Dominio → Unidad Organizativa).
  - Herramientas: `gpedit.msc`, `gpmc.msc`, `gpupdate /force`, `gpresult /r`, `rsop.msc`.

### 3. Tareas Críticas del Administrador de Sistemas
- **Copias de seguridad**: Políticas 3-2-1, esquemas GFS (Grandfather-Father-Son), archive bit para Full/Incremental/Diferencial.
- **Despliegue y actualización centralizada**:
  - **WSUS** (Windows Server Update Services): Aprobación selectiva de parches mediante GPOs en intranet.
  - **Linux**: `apt update && apt upgrade`, paquete `unattended-upgrades` configurado en `/etc/apt/apt.conf.d/50unattended-upgrades`.
- **Monitorización y diagnóstico**:
  - Windows: Visor de eventos (`eventvwr.msc`), Monitor de rendimiento (`perfmon.msc`), Administrador de tareas.
  - Linux: `/var/log/syslog`, `/var/log/auth.log`, `journalctl -u servicio`, `logrotate`.

### 4. Herramientas de Consola y Diagnóstico de Red
- **Comandos de Windows**:
  - `ipconfig /all`, `/release`, `/renew`, `/flushdns`, `/displaydns`.
  - `ping` (ICMP echo), `tracert` (ICMP Time Exceeded con TTL incremental, max 30 saltos).
  - `arp -a` (tabla ARP caché), `route print / add / delete`.
  - `netstat -ano` (conexiones TCP/UDP activas, puertos escuchando, PID).
  - `nbtstat` (NetBIOS sobre TCP/IP), `nslookup` (consultas DNS interactivas y no interactivas).
  - `netsh`: Configuración integral de interfaces (`interface ip set address ...`), firewall y perfiles WLAN (`wlan show networks mode=bssid`).
  - `net user`: Gestión de usuarios y contraseñas locales por CLI.
- **Netcat (`nc`)**: La "navaja suiza" de redes creada por Hobbit en 1996. Permite abrir sockets TCP/UDP, transferir archivos, banner grabbing y port scanning.
- **Bash (Bourne-Again Shell)**:
  - Desarrollado por Brian Fox en 1988 para el proyecto GNU (primera beta 0.99 el 8 de junio de 1989).
  - Variables especiales: `$0` (script), `$1..$n` (argumentos), `$#` (recuento), `$@` y `$*` (todos los argumentos), `$?` (código de retorno), `$$` (PID).
  - Vulnerabilidad histórica **Shellshock** (CVE-2014-6271, descubierta por Stéphane Chazelas en 2014) en la exportación de funciones mediante variables de entorno.
- **PowerShell**:
  - Creado por Microsoft en noviembre de 2006 (Windows XP SP2 / Server 2003). Código abierto desde 2016 (MIT, PowerShell 7.x multiplataforma sobre .NET Core).
  - Basado en **objetos .NET** transmitidos a través del pipeline `|` (no cadenas de texto plano).
  - Estructura Verbo-Sustantivo (`Get-Process`, `Set-ExecutionPolicy`, `Invoke-Command`).
  - Políticas de ejecución: `Restricted`, `AllSigned`, `RemoteSigned`, `Unrestricted`, `Bypass`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Protocolo | Valor / Estándar |
|-----------------------|------------------|
| Puerto LDAP estándar | **389 TCP/UDP** |
| Puerto LDAPS (seguro) | **636 TCP** |
| Puerto Catálogo Global AD | **3268 TCP** (3269 LDAPS) |
| Puerto Kerberos AD | **88 TCP/UDP** |
| Estándar LDAPv3 | **RFC 4511** (RFC 4510) |
| Estándar Certificados Digitales | **X.509** (de la serie ITU-T X.500) |
| Longitud del GUID en AD | **128 bits** |
| Orden aplicación GPOs | **LSDOU** (Local, Sitio, Dominio, OU) |
| Lanzamiento original Bash | **8 de junio de 1989** (Brian Fox / GNU) |
| Vulnerabilidad Shellshock | **CVE-2014-6271** (Septiembre 2014) |
| Lanzamiento PowerShell | **Noviembre 2006** (Open Source en 2016) |
| Netcat autor original | **Hobbit** (1996) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/linux-kernel|Linux Kernel y Software de Base]]
- [[wiki/entities/windows-server|Windows Server y Administración de Dominios]]
- [[wiki/entities/active-directory|Active Directory Domain Services]]
- [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
- [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
- [[wiki/entities/powershell|PowerShell y Cmdlets]]
- [[wiki/entities/dns-protocol|Protocolo DNS]]
- [[wiki/entities/dhcp-protocol|Protocolo DHCP]]

### Conceptos Teóricos:
- [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
- [[wiki/concepts/process-and-memory-management|Gestión de Procesos y Memoria]]
- [[wiki/concepts/directory-services-and-identity|Servicios de Directorio y Gestión de Identidades]]

### Síntesis de Estudio:
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
- [[wiki/synthesis/active-directory-and-ldap-guide|Guía Comparativa y Práctica de Active Directory y LDAP]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
