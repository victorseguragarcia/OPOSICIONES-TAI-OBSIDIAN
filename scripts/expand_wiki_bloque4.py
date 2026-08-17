# -*- coding: utf-8 -*-
"""
Script de expansión exhaustiva de la wiki del Bloque 4 para TAI Oposiciones.
Genera fichas y resúmenes de alta densidad técnica (100-250 líneas por archivo)
basados en los 10 temas del Bloque 4.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

print("[*] Generando fuentes ampliadas en wiki/sources/...")

# ==============================================================================
# WIKI SOURCES (Temas 01 al 10)
# ==============================================================================

# Tema 01 ya fue escrito manualmente, pero lo incluimos completo y pulido
TEMA01_MD = """---
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
"""

TEMA02_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 02: Administración de Bases de Datos, Virtualización y Cloud"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema02
  - bases-datos
  - dba
  - backup
  - raid
  - virtualizacion
  - cloud-computing
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Bases de Datos, Virtualización y Cloud"
  - "bloque4-tema02"
---

# Resumen Fuente: Bloque 4 - Tema 02: Administración de Bases de Datos, Virtualización y Cloud

Resumen exhaustivo y estructurado procesado desde la fuente original [[raw/sources/bloque4-tema02.md|bloque4-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda tres pilares fundamentales de las TIC en la administración pública: la administración de bases de datos relacionales y no relacionales bajo el modelo ANSI/SPARC y las 12 reglas de Codd; las políticas y técnicas de backup, almacenamiento redundante (RAID, DAS, NAS, SAN) y métricas de continuidad (RTO/RPO); la arquitectura de virtualización de servidores (anillos de protección x86, hipervisores Tipo 1 vs Tipo 2, vMotion, DRS, paravirtualización); y los modelos de servicio (IaaS, PaaS, SaaS, FaaS) e implementación de la computación en la nube (Cloud Computing).

---

## 🧩 Estructura y Desglose Temático

### 1. Fundamentos y Administración de Bases de Datos
- **Definición de Base de Datos (Flory, 1982)**: Colección exhaustiva y no redundante de datos estructurados, independientes de la aplicación física, accesibles en tiempo real por usuarios concurrentes.
- **Objetivos de un SGBD**: Independencia lógica y física de datos, integridad semántica, atomicidad transaccional, control de concurrencia y seguridad.
- **Arquitectura ANSI/X3/SPARC (3 niveles de abstracción)**:
  - **Nivel Externo (Vistas)**: Percepción de datos según el perfil de usuario/aplicación.
  - **Nivel Conceptual**: Estructura global de datos y relaciones (modelo Entidad/Relación o Relacional), independiente del almacenamiento físico.
  - **Nivel Interno / Físico**: Representación física de los datos en disco, estructuras de indexación (árboles B/B+), punteros y asignación de bloques.
- **Las 12 Reglas de E. F. Codd (Modelo Relacional)**:
  - Regla 0 (Fundacional), Regla 1 (Información en tablas), Regla 2 (Acceso garantizado por PK/Columna), Regla 3 (Tratamiento sistemático de NULL), Regla 4 (Catálogo dinámico relacional en línea), Regla 5 (Sublenguaje comprensivo: DDL, DML, DCL, TCL), Regla 6 (Actualización de vistas), Regla 7 (Inserción/actualización/borrado de alto nivel sobre conjuntos), Reglas 8 y 9 (Independencia física y lógica), Regla 10 (Independencia de integridad), Regla 11 (Independencia de distribución), Regla 12 (No subversión de reglas relacionales).
- **El Administrador de Bases de Datos (DBA)**:
  - Rol técnico responsable de la instalación, afinamiento (*tuning*), optimización de consultas (`EXPLAIN PLAN`), indexación, seguridad, replicación y planes de respaldo/recuperación.

### 2. Políticas de Backup, Almacenamiento y Continuidad
- **Métricas de Continuidad de Negocio**:
  - **RPO (Recovery Point Objective)**: Cantidad máxima tolerable de datos perdidos medida en tiempo.
  - **RTO (Recovery Time Objective)**: Tiempo máximo admisible para restaurar los servicios tras un desastre.
- **Tipos de Copia de Seguridad**:
  - **Completa (Full)**: Copia todos los archivos; borra el *archive bit*.
  - **Incremental**: Copia solo lo modificado desde el último backup (full o incremental); borra el *archive bit*. Recuperación más lenta (requiere full + todas las incrementales).
  - **Diferencial**: Copia todo lo modificado desde el último backup Full; NO borra el *archive bit*. Recuperación rápida (solo requiere full + última diferencial).
- **Estrategias de Respaldo**:
  - **Regla 3-2-1**: 3 copias de los datos, en 2 medios diferentes, con 1 copia fuera de la sede (*off-site* o nube). Evolución **3-2-1-1-0** (+1 copia inmutable/air-gapped y 0 errores de verificación).
  - **Esquema GFS (Grandfather-Father-Son)**: Rotación jerárquica de cintas/soportes (Hijo: diario, Padre: semanal, Abuelo: mensual/anual).
  - **Snapshots**: Capturas instantáneas de punteros a bloques (*Copy-on-Write* o *Redirect-on-Write*). No sustituyen al backup físico independiente.
- **Sistemas de Almacenamiento Masivo**:
  - **DAS** (Direct Attached Storage): Discos conectados directamente al bus del host (SATA, SAS, NVMe).
  - **NAS** (Network Attached Storage): Servidor de ficheros a nivel de archivo conectado a LAN (NFS, SMB/CIFS).
  - **SAN** (Storage Area Network): Red dedicada de alta velocidad a nivel de bloque (Fibre Channel, iSCSI, FCoE).
- **Matrices RAID**:
  - **RAID 0** (Striping): Alto rendimiento, 0 tolerancia a fallos.
  - **RAID 1** (Mirroring): Duplicación exacta, 50% de eficiencia de capacidad.
  - **RAID 5** (Striping con paridad distribuida): Mínimo 3 discos, tolera fallo de 1 disco. Capacidad: `(N-1) * S`.
  - **RAID 6** (Doble paridad distribuida): Mínimo 4 discos, tolera fallo de 2 discos simultáneos. Capacidad: `(N-2) * S`.
  - **RAID 10 (1+0)**: Espejo de bandas, alto rendimiento y alta tolerancia a fallos.

### 3. Virtualización de Sistemas
- **Mecanismos de Protección de CPU**:
  - Arquitectura x86: Anillos de privilegio (*Rings 0 a 3*). Anillo 0 para Kernel/Supervisor; Anillo 3 para espacio de usuario.
  - Virtualización clásica: Problema de las 17 instrucciones x86 sensibles no privilegiadas (Popek-Goldberg).
- **Clasificación de Hipervisores (VMM)**:
  - **Tipo 1 (Bare-Metal)**: Se ejecuta directamente sobre el hardware físico (VMware ESXi, Microsoft Hyper-V, KVM, Xen). Máximo rendimiento y seguridad empresarial.
  - **Tipo 2 (Hosted)**: Se ejecuta como aplicación sobre un SO anfitrión (VirtualBox, VMware Workstation).
- **Técnicas de Virtualización**:
  - **Virtualización Completa**: Traducción binaria o asistencia por hardware (**Intel VT-x / AMD-V**, EPT/NPT para MMU).
  - **Paravirtualización**: El SO invitado se modifica mediante *hypercalls* para interactuar directamente con el hipervisor (Xen).
  - **Virtualización a Nivel de SO (Contenedores)**: Comparte el mismo kernel mediante namespaces y cgroups.
- **Funcionalidades Avanzadas de Clúster Virtual**:
  - **Live Migration (vMotion / Live Migration)**: Migración de máquinas virtuales en caliente sin corte de servicio.
  - **DRS (Distributed Resource Scheduler)**: Balanceo dinámico automático de carga de CPU y memoria entre hosts.
  - **HA (High Availability)**: Reinicio automático de VMs en otros hosts del clúster si un nodo físico falla.
  - **DPM (Distributed Power Management)**: Apagado y encendido dinámico de servidores según la demanda de carga.
  - **HCI (Infraestructura Hiperconvergente)**: Convergencia de cómputo, red y almacenamiento definido por software (vSAN, Nutanix).

### 4. Computación en la Nube (Cloud Computing)
- **Modelos de Servicio (NIST SP 800-145)**:
  - **IaaS** (Infraestructura como Servicio): VMs, almacenamiento, redes virtuales (AWS EC2, Azure VMs).
  - **PaaS** (Plataforma como Servicio): Entorno de ejecución y middleware administrado (AWS Elastic Beanstalk, Heroku).
  - **SaaS** (Software como Servicio): Aplicaciones listas para el usuario final (Microsoft 365, Google Workspace).
  - **FaaS / Serverless**: Ejecución de código basada en eventos sin gestión de servidores (AWS Lambda, Azure Functions).
- **Modelos de Despliegue**: Nube Pública, Nube Privada, Nube Híbrida y Nube Comunitaria.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Tecnología | Especificación Clave |
|-----------------------|----------------------|
| ANSI/X3/SPARC | 3 niveles: Externo (Vistas), Conceptual (Lógico global), Interno (Físico) |
| Reglas de Codd | 13 reglas (Regla 0 a Regla 12) para SGBD Relacionales |
| Mínimo discos RAID 5 | **3 discos** (tolera 1 fallo, capacidad `N-1`) |
| Mínimo discos RAID 6 | **4 discos** (tolera 2 fallos, capacidad `N-2`) |
| Mínimo discos RAID 10 | **4 discos** (espejo de bandas) |
| Protocolos SAN | **Fibre Channel (FC)**, **iSCSI** (puerto TCP 3260), **FCoE** |
| Virtualización CPU x86 | Extensiones **Intel VT-x** y **AMD-V** |
| Anillos CPU x86 | Ring 0 (Kernel/Supervisor), Ring 3 (Usuario) |
| Estrategia Backup | **3-2-1** (3 copias, 2 medios, 1 externa) |
| Archive Bit | Activo = modificado; Respaldo Full e Incremental lo borran; Diferencial NO lo borra |
| Modelos Cloud NIST | **IaaS, PaaS, SaaS** (Modelos de servicio); Pública, Privada, Híbrida, Comunitaria (Despliegue) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
- [[wiki/entities/nosql-databases|Bases de Datos NoSQL]]
- [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- [[wiki/entities/kubernetes|Kubernetes]]
- [[wiki/entities/raid-storage|Sistemas de Almacenamiento RAID, NAS y SAN]]

### Conceptos Teóricos:
- [[wiki/concepts/database-normalization-and-acid|Normalización de Bases de Datos y Propiedades ACID]]
- [[wiki/concepts/virtualization-and-cloud-computing|Virtualización, Hipervisores y Computación Cloud]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación ante Desastres]]

### Síntesis de Estudio:
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
- [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema01.md", TEMA01_MD)
write_file("wiki/sources/bloque4-tema02.md", TEMA02_MD)

# Continuamos con Tema 03 al 10 en bloques de código limpios
TEMA03_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 03: Servidores de Correo, Contenedores y Microservicios"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema03
  - email-protocols
  - smtp
  - pop3
  - imap
  - microservicios
  - docker
  - kubernetes
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Servidores de Correo, Contenedores y Microservicios"
  - "bloque4-tema03"
---

# Resumen Fuente: Bloque 4 - Tema 03: Servidores de Correo, Contenedores y Microservicios

Resumen estructurado y puntos clave procesados desde la fuente original [[raw/sources/bloque4-tema03.md|bloque4-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema cubre la arquitectura de mensajería electrónica corporativa y la administración moderna de aplicaciones mediante contenedores y microservicios. Se detalla el funcionamiento de los agentes de correo (MUA, MTA, MDA, MS), el diálogo de comandos y códigos de estado de SMTP (RFC 5321), POP3 (RFC 1939), IMAP4 (RFC 3501), las extensiones MIME y S/MIME, y los mecanismos de autenticación y reputación de correo (SPF, DKIM, DMARC, RFC 2142). En la segunda parte, se analiza la arquitectura de microservicios frente al monolito, la contenedorización con Docker (namespaces, cgroups, imágenes OCI, Dockerfile) y la orquestación distribuida con Kubernetes (Pods, Deployments, Services, Ingress, arquitectura Master/Worker).

---

## 🧩 Estructura y Desglose Temático

### 1. Arquitectura y Protocolos de Correo Electrónico
- **Agentes del Ecosistema de Correo**:
  - **MUA (Mail User Agent)**: Cliente de correo del usuario (Thunderbird, Outlook, Webmail).
  - **MTA (Mail Transfer Agent)**: Servidor que enruta y transfiere correos entre dominios mediante SMTP (Postfix, Sendmail, Exim, Exchange).
  - **MDA (Mail Delivery Agent)**: Deposita el correo en el buzón local del destinatario (Dovecot, Procmail).
  - **MS (Mail Store)**: Almacén de buzones en formatos `mbox` (un solo fichero por buzón) o `Maildir` (un fichero por mensaje).
- **El Rol de DNS en el Correo**:
  - Registros **MX (Mail Exchanger)**: Indican los servidores MTA de un dominio con valor de prioridad (menor número = mayor prioridad).
  - Registros **A / AAAA**: Resuelven las FQDN de los MTAs a direcciones IP.
  - Registro **PTR**: Resolución inversa utilizada por los MTAs receptores para verificar la legitimidad de la IP del remitente.

#### 1.1 Protocolo SMTP (Simple Mail Transfer Protocol)
- Definido originalmente en RFC 821, actualizado en **RFC 5321** (ESMTP).
- Puertos estándar:
  - **25 TCP**: Transferencia entre MTAs (relay servidor-servidor).
  - **587 TCP**: Envío (*Submission*) cliente-a-servidor con autenticación (RFC 6409, `STARTTLS`).
  - **465 TCP**: SMTPS legado (SMTP encapsulado en SSL/TLS directo).
- **Comandos Principales SMTP**:
  - `HELO` / `EHLO` (identificación del cliente, EHLO habilita ESMTP).
  - `MAIL FROM:<origen>` (inicia transacción y define remitente del envelope).
  - `RCPT TO:<destino>` (especifica destinatario; puede repetirse).
  - `DATA` (inicia cuerpo del mensaje; finaliza con `<CRLF>.<CRLF>`).
  - `RSET` (cancela transacción actual), `NOOP` (no-operación), `QUIT` (cierra sesión), `VRFY` (verifica usuario), `STARTTLS` (negocia cifrado TLS).
- **Códigos de Respuesta SMTP**:
  - `2xx`: Éxito definitivo (ej. `220` Servicio listo, `250` Acción completada OK).
  - `3xx`: Éxito intermedio (ej. `354` Envíe datos de correo finalizando con `.`).
  - `4xx`: Fallo temporal (el cliente debe reintentar más tarde; ej. `421` Servicio no disponible).
  - `5xx`: Fallo permanente (rechazo definitivo; ej. `550` Buzón no encontrado).

#### 1.2 Protocolos de Recuperación: POP3 e IMAP4
- **POP3 (Post Office Protocol v3 - RFC 1939)**:
  - Puertos: **110 TCP** (plano) y **995 TCP** (POP3S con SSL/TLS).
  - Modelo *descarga y borra*: Descarga mensajes al cliente local y los elimina del servidor (o los deja temporalmente según configuración).
  - Estados: *Autorización* (`USER`, `PASS`, `APOP`), *Transacción* (`STAT`, `LIST`, `RETR`, `DELE`, `NOOP`, `RSET`), *Actualización* (`QUIT`).
- **IMAP4 (Internet Message Access Protocol v4 - RFC 3501)**:
  - Puertos: **143 TCP** (plano / STARTTLS) y **993 TCP** (IMAPS con SSL/TLS).
  - Modelo *sincronización bidireccional*: Los mensajes y carpetas residen permanentemente en el servidor.
  - Soporta descarga parcial (cabeceras antes del cuerpo/adjuntos), flags de estado (`\Seen`, `\Draft`, `\Deleted`) y múltiples clientes simultáneos.
- **Extensiones y Formatos**:
  - **MIME (Multipurpose Internet Mail Extensions - RFC 2045-2049)**: Permite adjuntos binarios (imágenes, PDFs) codificados en Base64, caracteres no ASCII y texto multipart/HTML.
  - **S/MIME**: Cifrado y firma digital de mensajes mediante certificados X.509.

#### 1.3 Seguridad y Reputación de Correo
- **SPF (Sender Policy Framework - RFC 7208)**: Registro DNS `TXT` que especifica qué IPs están autorizadas a enviar correo en nombre de un dominio.
- **DKIM (DomainKeys Identified Mail - RFC 6376)**: Firma criptográfica asimétrica añadida a la cabecera; el receptor valida la firma usando la clave pública publicada en DNS `TXT`.
- **DMARC (RFC 7489)**: Política unificada basada en SPF y DKIM que indica al receptor qué hacer ante correos no alineados (`none`, `quarantine`, `reject`) y genera reportes.
- **RFC 2142**: Nombres de buzón estándar obligatorios (`postmaster@`, `abuse@`, `webmaster@`, `hostmaster@`).

### 2. Arquitectura de Microservicios
- **Monolito vs. Microservicios**:
  - Monolito: Base de código única, despliegue todo-o-nada, acoplamiento alto, dificultad para escalar componentes individuales.
  - Microservicios: Servicios autónomos, desacoplados, desplegables independientemente, comunicados mediante APIs REST/gRPC o colas de mensajes (Kafka, RabbitMQ).
- **Patrones de Microservicios**: API Gateway, Service Mesh (Istio), Circuit Breaker (Netflix Hystrix), Service Discovery (Consul, Eureka).

### 3. Docker y Contenedores
- **Fundamentos del Kernel de Linux**:
  - **Namespaces**: Aislamiento de recursos (`pid`, `net`, `ipc`, `mnt`, `uts`, `user`).
  - **Control Groups (cgroups)**: Límite y monitorización de consumo de hardware (CPU, memoria, I/O, red).
  - **Union File Systems (Overlay2)**: Sistema de capas de solo lectura apiladas con una capa superior de lectura/escritura efímera.
- **Ecosistema Docker**:
  - Docker Engine (demonio `dockerd`), Docker CLI, Dockerfile (`FROM`, `RUN`, `COPY`, `CMD`, `ENTRYPOINT`, `EXPOSE`, `VOLUME`).
  - Registro de imágenes (Docker Hub, Harbor).
  - Estándar OCI (Open Container Initiative): `runc` y `containerd`.

### 4. Kubernetes (K8s) y Orquestación
- Plataforma de orquestación de contenedores desarrollada originalmente por Google.
- **Arquitectura del Clúster**:
  - **Control Plane (Master)**: `kube-apiserver` (punto central de API), `etcd` (almacén clave-valor distribuido), `kube-scheduler` (asigna pods a nodos), `kube-controller-manager` (controladores de estado deseado).
  - **Nodos Worker**: `kubelet` (agente de nodo que comunica con el runtime de contenedores), `kube-proxy` (gestión de reglas iptables/IPVS de red), Container Runtime (`containerd`, `CRI-O`).
- **Objetos Principales de Kubernetes**:
  - **Pod**: Unidad mínima de despliegue (uno o más contenedores estrechamente acoplados que comparten red y almacenamiento).
  - **Deployment / ReplicaSet**: Gestión declarativa de réplicas, actualizaciones progresivas (*rolling updates*) y rollbacks.
  - **Service**: Abstracción de red que expone un conjunto de pods bajo una IP/DNS estable (`ClusterIP`, `NodePort`, `LoadBalancer`).
  - **Ingress**: Enrutamiento HTTP/HTTPS perimetral hacia servicios internos con balanceo y terminación SSL.
  - **ConfigMaps y Secrets**: Inyección desacoplada de configuraciones y credenciales sensibles.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo / Herramienta | Puertos y Especificaciones |
|-------------------------|---------------------------|
| SMTP Transfer (Relay) | **25 TCP** (RFC 5321) |
| SMTP Submission | **587 TCP** (RFC 6409 con STARTTLS) |
| SMTPS (Legado SSL) | **465 TCP** |
| POP3 / POP3S | **110 TCP** / **995 TCP** (RFC 1939) |
| IMAP4 / IMAPS | **143 TCP** / **993 TCP** (RFC 3501) |
| Seguridad Anti-Spoofing | **SPF** (TXT), **DKIM** (Firma clave pública en TXT), **DMARC** (Alineación) |
| Buzones RFC 2142 | `postmaster@`, `abuse@`, `hostmaster@`, `webmaster@` |
| Primitivas Kernel Docker | **Namespaces** (aislamiento) + **cgroups** (límites de recursos) |
| Almacén Estado K8s | **etcd** (base de datos clave-valor distribuida en Raft, puertos 2379/2380) |
| Unidad Mínima K8s | **Pod** (comparte espacio de red `localhost` y volúmenes) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
- [[wiki/entities/docker-and-containers|Docker y Motores de Contenedores]]
- [[wiki/entities/kubernetes|Kubernetes y Orquestación de Contenedores]]
- [[wiki/entities/dns-protocol|Protocolo DNS y Registros MX]]

### Conceptos Teóricos:
- [[wiki/concepts/microservices-and-middleware|Microservicios, APIs y Middleware]]
- [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Computación Cloud]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC]]
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
"""

write_file("wiki/sources/bloque4-tema03.md", TEMA03_MD)

TEMA04_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 04: Administración de Redes de Área Local"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema04
  - redes-lan
  - vlan
  - dhcp
  - dns
  - stp
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Administración de Redes de Área Local"
  - "bloque4-tema04"
---

# Resumen Fuente: Bloque 4 - Tema 04: Administración de Redes de Área Local

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema04.md|bloque4-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el diseño, administración, segmentación y servicios fundamentales de las redes de área local (LAN). Se analizan los esquemas de arquitectura de red perimetral (esquemas simples, con DMZ o zona neutra, múltiples zonas internas y DMZs compuestas), conceptos de Intranet y Extranet, direccionamiento MAC e IP (herramientas `ipconfig`, `ifconfig`, `ip`), servicios de infraestructura crítica (DHCP y el ciclo DORA, DNS y resolución recursiva/iterativa), administración de usuarios y grupos en sistemas cliente y servidor (Windows y Linux), y gestión de almacenamiento de discos y periféricos compartidos.

---

## 🧩 Estructura y Desglose Temático

### 1. Esquemas de Arquitectura de Red y DMZ
- **Concepto de DMZ (Zona Desmilitarizada / Zona Neutra)**: Subred intermedia ubicada entre la red no confiable (Internet) y la red corporativa interna protegida.
- **Topologías Perimetrales**:
  - **Esquema Básico**: Router con cortafuegos conectando red interna con Internet.
  - **Esquema con DMZ y un solo cortafuegos (Three-Pronged / Cortafuegos de 3 patas)**: Una interfaz para Internet, otra para la DMZ (servidores web, correo externo, DNS público) y otra para la LAN interna.
  - **Esquema con DMZ entre dos cortafuegos (Back-to-Back)**: Máxima seguridad; cortafuegos perimetral externo y cortafuegos interno (idealmente de fabricantes distintos para evitar vulnerabilidades comunes).
  - **Esquemas con múltiples DMZs**: Separación de DMZ pública (servicios web) y DMZ de aplicaciones/datos intermedias.
- **Intranets y Extranets**:
  - **Intranet**: Red privada basada en protocolos de Internet (HTTP, TCP/IP) accesible exclusivamente por los miembros de la organización.
  - **Extranet**: Extensión controlada de la intranet accesible a usuarios externos autorizados (proveedores, socios, clientes) mediante túneles VPN o TLS.

### 2. Direccionamiento y Configuración de Red
- **Dirección MAC (Media Access Control)**:
  - Identificador físico de 48 bits (6 bytes) en la capa de enlace (Nivel 2).
  - Primeros 24 bits: **OUI** (Organizationally Unique Identifier) asignado por el IEEE.
  - Últimos 24 bits: Asignados por el fabricante (NIC).
- **Herramientas de Configuración y Diagnóstico**:
  - **Windows**: `ipconfig /all`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
  - **Linux clásico**: `ifconfig` (paquete `net-tools`, en desuso).
  - **Linux moderno**: Comando `ip` (paquete `iproute2`): `ip addr show`, `ip link set dev eth0 up`, `ip route show`.

### 3. Servicios de Infraestructura Básica

#### 3.1 Protocolo DHCP (Dynamic Host Configuration Protocol)
- Definido en **RFC 2131** (IPv4) y **RFC 8415** (DHCPv6).
- Puertos estándar: **67 UDP** (Servidor) y **68 UDP** (Cliente). En DHCPv6: **546 UDP** (Cliente) y **547 UDP** (Servidor).
- **Proceso de Concesión DORA**:
  1. **Discover**: Cliente envía broadcast (`255.255.255.255`, puerto 67) buscando servidores DHCP.
  2. **Offer**: Servidor responde con unicast/broadcast ofreciendo IP, máscara, gateway, DNS y tiempo de concesión (*lease time*).
  3. **Request**: Cliente solicita formalmente la IP ofrecida.
  4. **Acknowledge (ACK)**: Servidor confirma la concesión y el cliente activa la configuración.
- **Tiempos de Renovación**:
  - **T1 (0.5 * Lease Time)**: Cliente intenta renovar con el mismo servidor vía Unicast (`DHCPREQUEST`).
  - **T2 (0.875 * Lease Time)**: Si no hay respuesta, cliente envía Broadcast a cualquier servidor DHCP disponible.
- **DHCP Relay Agent (RFC 3046 / Opción 82)**: Permite a routers reenviar peticiones DHCP broadcast de clientes de subredes locales a un servidor DHCP centralizado en otra subred.

#### 3.2 Protocolo DNS (Domain Name System)
- Definido en **RFC 1034** y **RFC 1035**.
- Puerto estándar: **53 TCP y UDP** (UDP para consultas estándar de hasta 512 bytes / EDNS0; TCP para transferencias de zona AXFR/IXFR y respuestas mayores a 512 bytes).
- **Espacio de Nombres Jerárquico**:
  - Nodo raíz (`.` gestionado por los 13 servidores raíz lógicos `a.root-servers.net` a `m.root-servers.net`).
  - **TLD (Top-Level Domain)**: gTLD (`.com`, `.org`, `.gob`), ccTLD (`.es`, `.fr`).
  - Dominios de segundo nivel y subdominios.
- **Tipos de Registros DNS Críticos**:
  - `A` (IPv4, 32 bits), `AAAA` (IPv6, 128 bits), `CNAME` (Alias canónico).
  - `MX` (Mail Exchanger con prioridad), `NS` (Servidor de nombres autoritativo).
  - `PTR` (Puntero de resolución inversa bajo `in-addr.arpa` o `ip6.arpa`).
  - `SOA` (Start of Authority: número de serie, refresh, retry, expire, TTL mínimo).
  - `TXT` (Texto arbitrario, usado por SPF, DKIM, DMARC), `SRV` (Localización de servicios en AD).
- **Consultas**: Recursivas (el servidor DNS resuelve hasta el final y devuelve el resultado) vs. Iterativas (el servidor devuelve la mejor referencia que conoce).

### 4. Gestión de Dispositivos y Almacenamiento en Clientes/Servidores
- **Windows**: Consola de Administración de discos (`diskmgmt.msc`), comando `diskpart`. Tablas MBR (máx 2 TB, 4 particiones primarias) vs. GPT (hasta 128 particiones, soporte >2 TB con UEFI).
- **Linux**: Herramientas `fdisk`, `gdisk` (para GPT), `parted`, `mkfs.ext4`, `mkfs.xfs`, montaje en `/etc/fstab`, y gestión de volúmenes lógicos con **LVM** (PV: Physical Volumes, VG: Volume Groups, LV: Logical Volumes).

---

## 🎯 Datos Clave para Oposiciones TAI

| Servicio / Parámetro | Valor Técnico |
|----------------------|---------------|
| Puertos DHCPv4 | **67 UDP** (Server), **68 UDP** (Client) |
| Puertos DHCPv6 | **547 UDP** (Server), **546 UDP** (Client) |
| Fases DHCP | **DORA** (Discover, Offer, Request, Acknowledge) |
| Tiempos renovación DHCP | **T1 = 50%** del lease time (unicast); **T2 = 87.5%** (broadcast) |
| Puerto DNS | **53 TCP/UDP** |
| Longitud Dirección MAC | **48 bits (6 bytes)**; 24 bits OUI + 24 bits NIC |
| Servidores Raíz DNS | **13 nombres lógicos** (`A` hasta `M`), operados con Anycast |
| Límite MBR vs GPT | MBR máx **2 TB** y 4 particiones primarias; GPT sin límite práctico (requiere UEFI) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/dhcp-protocol|Protocolo DHCP y Concesiones DORA]]
- [[wiki/entities/dns-protocol|Protocolo DNS y Resolución de Nombres]]
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Direcciones MAC]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, DMZ y Redes Privadas Virtuales]]

### Conceptos Teóricos:
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema04.md", TEMA04_MD)

TEMA05_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 05: Seguridad, Criptografía, CPDs y Gestión de Incidencias"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema05
  - seguridad-informatica
  - criptografia
  - cpd
  - tia-942
  - itil
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Seguridad, Criptografía, CPDs y Gestión de Incidencias"
  - "bloque4-tema05"
---

# Resumen Fuente: Bloque 4 - Tema 05: Seguridad, Criptografía, CPDs y Gestión de Incidencias

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema05.md|bloque4-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda con profundidad cuatro grandes áreas de la seguridad física y lógica: los conceptos fundamentales de seguridad (dimensiones CIDAN, análisis de riesgos, amenazas, vulnerabilidades y taxonomía de ciberataques); los algoritmos criptográficos (simétricos, asimétricos, funciones hash, firma digital, formatos XAdES/PAdES/CAdES y certificados digitales X.509); el diseño y acondicionamiento físico de Centros de Proceso de Datos bajo la norma **ANSI/TIA-942** y la clasificación **TIER I a IV**; y los sistemas de gestión de incidencias y gobierno de servicios TI según el marco **ITIL** (Service Desk, ciclo de vida de incidencias, SLA).

---

## 🧩 Estructura y Desglose Temático

### 1. Seguridad de la Información: Principios y Amenazas
- **Dimensiones de la Seguridad (CIDAN / ENS)**:
  - **Confidencialidad**: Acceso exclusivo a personas autorizadas.
  - **Integridad**: Garantía de que la información no ha sido alterada indebidamente.
  - **Disponibilidad**: Acceso y utilización de los sistemas cuando se requiera.
  - **Autenticidad**: Garantía de la identidad del emisor/origen.
  - **Trazabilidad (No Repudio)**: Registro auditable de las acciones realizadas sin posibilidad de negar su autoría.
- **Taxonomía de Amenazas y Ciberataques**:
  - Ataques de Malware: Virus, Gusanos, Troyanos, Ransomware, Spyware, Rootkits, Botnets.
  - Ataques de Red: Man-in-the-Middle (MitM), Spoofing (IP, ARP, DNS), DoS/DDoS (SYN Flood, Amplificación DNS/NTP, Smurf), Inyecciones SQL (SQLi), Cross-Site Scripting (XSS).
  - Ataques de Canal Lateral (Side-Channel): Análisis de consumo energético, radiación electromagnética (TEMPEST) y tiempos de ejecución.
  - Ingeniería Social: Phishing, Spear Phishing, Vishing, Smishing, Baiting.
- **Auditorías de Seguridad**: Test de intrusión (*Penetration Testing*: Caja Negra, Caja Gris, Caja Blanca) y Análisis Forense Digital (cadena de custodia, adquisición de evidencias volátiles en RAM antes que almacenamiento persistente).

### 2. Criptografía y Firma Digital
- **Criptografía Simétrica (Clave Secreta)**:
  - Misma clave para cifrar y descifrar. Muy rápida, ideal para grandes volúmenes de datos.
  - Algoritmos de bloque: **AES** (Rijndael, bloques de 128 bits, claves de 128/192/256 bits), **DES** (56 bits, obsoleto), **3DES** (112/168 bits), **Blowfish**, **Twofish**, **IDEA**, **RC4** (flujo, obsoleto).
- **Criptografía Asimétrica (Clave Pública / Privada)**:
  - Clave pública para cifrar/verificar; clave privada para descifrar/firmar.
  - Basada en problemas matemáticos difíciles (factorización de números primos grandes, logaritmo discreto, curvas elípticas).
  - Algoritmos: **RSA** (longitudes típicas 2048, 4096 bits), **Diffie-Hellman** (intercambio de claves), **DSA**, **ECDSA / Ed25519** (Criptografía de Curva Elíptica).
- **Criptografía Híbrida**: Combina la velocidad del cifrado simétrico (para el payload con una clave de sesión efímera) con la seguridad del asimétrico (para cifrar la clave de sesión). Empleado en TLS, PGP y SSH.
- **Funciones Hash (Resumen Unidireccional)**:
  - Propiedades: Unidireccionalidad (imposible obtener el mensaje original del hash), resistencia a colisiones (dos mensajes distintos no producen el mismo hash) y efecto avalancha.
  - Algoritmos: **MD5** (128 bits, roto), **SHA-1** (160 bits, deprecado), **SHA-2** (SHA-256, SHA-512), **SHA-3** (Keccak).
- **Firma Digital y Certificados X.509**:
  - Proceso: `Hash(Mensaje)` cifrado con la `Clave Privada del Emisor`. El receptor descifra con la `Clave Pública del Emisor` y compara con su propio cálculo del hash.
  - Formatos de Firma Electrónica Avanzada:
    - **CAdES** (CMS Advanced Electronic Signatures): Para ficheros binarios genéricos.
    - **XAdES** (XML Advanced Electronic Signatures): Para documentos basados en XML.
    - **PAdES** (PDF Advanced Electronic Signatures): Integrada nativamente en ficheros PDF (ISO 32000-1).
  - **Jerarquía de Certificados**: Autoridad de Certificación Raíz (CA), CA Subordinadas, Autoridad de Registro (RA), Listas de Revocación de Certificados (**CRL**) y protocolo de consulta en tiempo real **OCSP** (RFC 6960, puerto 80 HTTP).

### 3. Infraestructura Física de CPDs: Estándar ANSI/TIA-942
El estándar **ANSI/TIA-942** (*Telecommunications Infrastructure Standard for Data Centers*) define los requisitos de arquitectura, climatización, suministro eléctrico y telecomunicaciones organizados en **4 niveles TIER**:

| Nivel TIER | Nombre / Tipo | Disponibilidad | Redundancia | Tiempo Inactividad Anual | Vías de Distribución |
|------------|---------------|----------------|-------------|--------------------------|---------------------|
| **TIER I** | Básico | 99.671% | N (Sin redundancia) | 28.8 horas/año | 1 vía única (sin tolerancia a fallos) |
| **TIER II** | Componentes Redundantes | 99.741% | N+1 (Componentes redundantes) | 22.0 horas/año | 1 vía única |
| **TIER III** | Mantenimiento Concurrente | 99.982% | N+1 (Mantenible sin parar) | 1.6 horas/año | 1 activa + 1 pasiva (2 vías) |
| **TIER IV** | Tolerante a Fallos | 99.995% | 2(N+1) o 2N+1 | 26.3 minutos/año | 2 vías activas simultáneas |

- **Condiciones Ambientales en CPD (ASHRAE TC 9.9)**:
  - Temperatura recomendada: **18 °C a 27 °C**.
  - Humedad relativa: **40% a 60%** (prevenir condensación y descargas electrostáticas ESD).
  - Diseño de pasillos: **Pasillo frío / Pasillo caliente** (*Hot/Cold Aisle containment*).
  - Sistemas de extinción de incendios: Gases limpios no conductores que no dañan componentes electrónicos (Novec 1230, FM-200, Inergen) sustituyendo al gas Halón (prohibido).
  - Suministro eléctrico: SAIs (*UPS* Online de doble conversión), grupos electrógenos diésel y doble acometida desde subestaciones eléctricas independientes (TIER IV).

### 4. Gestión de Servicios e Incidencias (ITIL)
- **ITIL (Information Technology Infrastructure Library)**: Marco de buenas prácticas para la Gestión de Servicios TI (ITSM).
- **Service Desk (Centro de Servicios)**: Único punto de contacto (SPOC) entre los usuarios y el departamento de TI.
  - Diferencia: *Help Desk* (soporte técnico reactivo de primer nivel) vs. *Service Desk* (enfoque global integrado en la estrategia del negocio).
- **Ciclo de Vida de una Incidencia**:
  1. Identificación y Registro (Ticket).
  2. Clasificación y Categorización.
  3. Priorización (Impacto x Urgencia).
  4. Diagnóstico Inicial.
  5. Escalamiento (Funcional a Nivel 2/3 o Jerárquico).
  6. Investigación y Diagnóstico.
  7. Resolución y Recuperación.
  8. Cierre de la Incidencia y Encuesta de Satisfacción.
- **SLA (Service Level Agreement)**: Acuerdo de nivel de servicio que define los tiempos máximos comprometidos de respuesta y resolución.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Estándar | Especificación Técnica |
|----------------------|------------------------|
| Estándar de CPDs | **ANSI/TIA-942** |
| Disponibilidad TIER I | **99.671%** (28.8 h caída/año, N) |
| Disponibilidad TIER II | **99.741%** (22.0 h caída/año, N+1) |
| Disponibilidad TIER III | **99.982%** (1.6 h caída/año, Mantenimiento concurrente) |
| Disponibilidad TIER IV | **99.995%** (26.3 min caída/año, Tolerante a fallos 2N+1) |
| AES Tamaños de Clave | **128, 192 y 256 bits** (bloques fijos de 128 bits) |
| SHA-2 Tamaños Hash | **SHA-224, SHA-256, SHA-384, SHA-512** |
| Formatos Firma Avanzada | **CAdES** (binario), **XAdES** (XML), **PAdES** (PDF) |
| Protocolo Estado Certificado | **OCSP** (RFC 6960, puerto 80 HTTP) vs **CRL** |
| SPOC en ITIL | **Service Desk** (Single Point of Contact) |
| Prioridad de Incidencia | `Prioridad = Impacto * Urgencia` |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL y Criptografía Híbrida]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, VPN y Defensa Perimetral]]
- [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
- [[wiki/entities/ccn-cert-and-ens|CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad]]

### Conceptos Teóricos:
- [[wiki/concepts/cryptography-and-digital-signatures|Criptografía Simétrica, Asimétrica y Firma Digital]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Niveles TIER]]
- [[wiki/concepts/incident-management-and-itil|Gestión de Incidencias y Marco ITIL]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital]]
- [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
- [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
"""

write_file("wiki/sources/bloque4-tema05.md", TEMA05_MD)

TEMA06_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 06: Medios de Transmisión, Modulación y Comunicaciones Inalámbricas"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema06
  - medios-transmision
  - fibra-optica
  - par-trenzado
  - cableado-estructurado
  - wifi
  - 5g
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Medios de Transmisión, Modulación y Comunicaciones Inalámbricas"
  - "bloque4-tema06"
---

# Resumen Fuente: Bloque 4 - Tema 06: Medios de Transmisión, Modulación y Comunicaciones Inalámbricas

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema06.md|bloque4-tema06.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en los fundamentos de la capa física de comunicaciones: modos de transmisión de datos (Simplex, Half-Duplex, Full-Duplex; Unicast, Multicast, Broadcast, Anycast; síncrona, asíncrona, isócrona), técnicas de multiplexación (FDM, TDM, WDM, DWDM) y modulación analógica/digital (ASK, FSK, PSK, QAM). Analiza detalladamente los medios guiados (par trenzado UTP/FTP/STP y categorías Cat 5e a Cat 8, cable coaxial, fibra óptica monomodo/multimodo y tecnologías FTTH/GPON), sistemas de cableado estructurado según norma ISO/IEC 11801 y TIA/EIA-568, y medios no guiados inalámbricos (estándares Wi-Fi IEEE 802.11a/b/g/n/ac/ax/be y generaciones móviles desde 1G hasta 5G NR).

---

## 🧩 Estructura y Desglose Temático

### 1. Modos de Comunicación y Transmisión
- **Según el Sentido del Flujo**:
  - **Simplex**: Transmisión unidireccional estricta (ej. radiodifusión, televisión comercial).
  - **Semi-Dúplex (Half-Duplex)**: Bidireccional no simultáneo; ambos transmiten pero no al mismo tiempo (ej. Walkie-talkie, CSMA/CD en Ethernet con hubs).
  - **Dúplex Completo (Full-Duplex)**: Bidireccional simultáneo en ambos sentidos (ej. telefonía, Ethernet con conmutadores).
- **Según el Destino**:
  - **Unicast**: Envío de un emisor a un único receptor específico.
  - **Broadcast**: Envío de un emisor a todos los hosts del dominio de difusión (`255.255.255.255`). Inexistente en IPv6 (reemplazado por multicast).
  - **Multicast**: Envío a un grupo suscrito de receptores (IPv4 Clase D `224.0.0.0/4`; IPv6 `ff00::/8`).
  - **Anycast**: Envío al nodo más cercano (según métrica de enrutamiento) de un grupo que comparte la misma dirección IP.
- **Sincronismo de Bits**:
  - **Asíncrona**: Cada carácter lleva bits de inicio (*start bit*) y parada (*stop bit*); relojes emisor/receptor no sincronizados permanentemente.
  - **Síncrona**: Trama continua delimitada por flags; emisor y receptor sincronizados con reloj común o recuperado de la señal.
  - **Isócrona**: Garantía de retardo máximo y tasa constante, esencial para audio/vídeo en tiempo real.

### 2. Multiplexación y Modulación
- **Técnicas de Multiplexación**:
  - **FDM (Frequency Division Multiplexing)**: División del espectro en canales de distinta frecuencia portadora (radio, ADSL).
  - **TDM (Time Division Multiplexing)**: Asignación de ranuras de tiempo (*time slots*) rotativas (telefonía digital PCM, E1/T1). Puede ser síncrona o estadística.
  - **WDM / DWDM (Wavelength Division Multiplexing)**: Multiplexación por longitud de onda en fibra óptica. DWDM (*Dense WDM*) permite cientos de canales ópticos en una sola fibra.
- **Técnicas de Modulación**:
  - Digital sobre portadora analógica: **ASK** (Amplitud), **FSK** (Frecuencia), **PSK** (Fase: BPSK, QPSK), **QAM** (Amplitud en Cuadratura: 16-QAM, 64-QAM, 256-QAM, 1024-QAM, combinando fase y amplitud).

### 3. Medios Guiados de Transmisión

#### 3.1 Par Trenzado de Cobre
- El trenzado reduce interferencias electromagnéticas externas y diafonía (*crosstalk*).
- **Blindajes (ISO/IEC 11801)**:
  - **U/UTP**: Sin apantallar (el más común y económico).
  - **F/UTP**: Pantalla global de papel de aluminio sobre todos los pares.
  - **S/FTP**: Pantalla de malla metálica global + cada par blindado con papel de aluminio (máximo blindaje).
- **Categorías de Cable de Cobre**:
  - **Cat 5e**: Ancho de banda **100 MHz**, soporta Gigabit Ethernet (**1000BASE-T** hasta 100 m).
  - **Cat 6**: Ancho de banda **250 MHz**, soporta 1000BASE-T (100 m) y 10GBASE-T (hasta 55 m).
  - **Cat 6A**: Ancho de banda **500 MHz**, soporta **10GBASE-T** a **100 m**.
  - **Cat 7 / 7A**: Ancho de banda **600 / 1000 MHz** (conectores GG45/TERA).
  - **Cat 8 (8.1 / 8.2)**: Ancho de banda **2000 MHz (2 GHz)**, soporta **25GBASE-T** y **40GBASE-T** (hasta 30 m).
- **Conexiones**: Conector **RJ-45** (8P8C) según esquemas **T568A** y **T568B**.

#### 3.2 Fibra Óptica
- Transmisión de pulsos de luz mediante reflexión interna total en núcleo de sílice/vidrio rodeado de cubierta (*cladding*). Inmune a interferencias electromagnéticas (EMI) y sin radiación de señal.
- **Tipos de Fibra**:
  - **Monomodo (SMF - Single Mode Fiber)**: Núcleo muy pequeño (~9 µm), un solo rayo de luz viaja sin dispersión modal. Fuente: Láser (longitudes de onda **1310 nm** y **1550 nm**). Gran alcance (>10-40 km).
  - **Multimodo (MMF - Multi Mode Fiber)**: Núcleo más grueso (**50 µm** o **62.5 µm**), múltiples modos de propagación sufren dispersión modal. Fuente: LED o VCSEL (longitudes de onda **850 nm** y **1300 nm**). Alcance típico hasta 300-550 m (OM1, OM2, OM3, OM4, OM5).
- **Conectores Ópticos**: SC (*Subscriber Connector*), LC (*Lucent Connector* - estándar en switches SFP), ST (*Straight Tip*), FC (*Ferrule Connector*), MPO/MTP.
- **Topologías FTTx y GPON**:
  - **FTTH (Fiber to the Home)**: Fibra directa hasta la ONT del abonado.
  - **GPON (Gigabit Passive Optical Network - ITU-T G.984)**: Red óptica pasiva punto a multipunto mediante divisores ópticos (*splitters* pasivos sin alimentación). Velocidades: **2.488 Gbps bajada / 1.244 Gbps subida**.
  - **XG-PON / XGS-PON**: GPON de 10 Gbps simétricos.

#### 3.3 Sistema de Cableado Estructurado (SCE)
- Normas: **ISO/IEC 11801**, **ANSI/TIA/EIA-568**.
- Elementos:
  - **Cableado Horizontal**: Desde rosetas de puesto (área de trabajo) hasta el distribuidor de planta (máx **90 m** de cable horizontal fijo + **10 m** de latiguillos = **100 m canal total**).
  - **Cableado Troncal / Backbone (Vertical)**: Interconecta distribuidores de planta con el distribuidor de edificio o de campus (típicamente fibra óptica).
  - Cuarto de telecomunicaciones (*Racks*, paneles de parcheo).

### 4. Comunicaciones Inalámbricas y Móviles
- **Familia Wi-Fi (IEEE 802.11)**:
  - **802.11b** (1999): 2.4 GHz, hasta 11 Mbps (DSSS).
  - **802.11a** (1999): 5 GHz, hasta 54 Mbps (OFDM).
  - **802.11g** (2003): 2.4 GHz, hasta 54 Mbps (OFDM).
  - **802.11n (Wi-Fi 4)** (2009): 2.4 / 5 GHz, hasta 600 Mbps (MIMO).
  - **802.11ac (Wi-Fi 5)** (2013): 5 GHz exclusivo, hasta 6.9 Gbps (MU-MIMO, canales de 80/160 MHz, 256-QAM).
  - **802.11ax (Wi-Fi 6 / 6E)** (2019/2021): 2.4, 5 y **6 GHz** (Wi-Fi 6E), hasta 9.6 Gbps (**OFDMA**, 1024-QAM, Target Wake Time).
  - **802.11be (Wi-Fi 7)**: Hasta 46 Gbps, canales de 320 MHz, 4096-QAM, MLO (Multi-Link Operation).
- **Seguridad Wi-Fi**: WEP (roto), WPA (TKIP), WPA2 (AES-CCMP), **WPA3** (SAE - *Simultaneous Authentication of Equals*, cifrado de 192 bits en modo Enterprise).
- **Evolución de Telefonía Móvil (3GPP)**:
  - **1G**: Analógica (AMPS, TACS).
  - **2G**: Digital GSM (900/1800 MHz, TDMA, SMS). Evolución GPRS (2.5G) y EDGE (2.75G).
  - **3G**: UMTS (WCDMA, hasta 2 Mbps). Evolución HSPA / HSPA+ (hasta 42 Mbps).
  - **4G**: **LTE / LTE-Advanced** (Todo IP, OFDM, MIMO, hasta 1 Gbps).
  - **5G NR (New Radio)**: Bandas sub-6 GHz y onda milimétrica (mmWave). Modos **NSA** (*Non-Standalone*, sobre núcleo 4G EPC) y **SA** (*Standalone*, sobre núcleo nativo 5G Core). Características: eMBB (banda ancha mejorada), URLLC (ultra baja latencia <1 ms), mMTC (comunicaciones masivas máquina a máquina / IoT).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Parámetro | Especificación Técnica |
|------------------------|------------------------|
| Longitud máxima canal horizontal UTP | **100 metros** (90 m fijo + 10 m latiguillos) |
| Cat 5e / Cat 6 / Cat 6A anchos de banda | **100 MHz / 250 MHz / 500 MHz** |
| Velocidad 10GBASE-T sobre Cat 6A | **10 Gbps hasta 100 metros** |
| Longitudes de onda Fibra Monomodo | **1310 nm y 1550 nm** (Láser, núcleo ~9 µm) |
| Longitudes de onda Fibra Multimodo | **850 nm y 1300 nm** (LED/VCSEL, núcleo 50/62.5 µm) |
| Velocidades GPON (ITU-T G.984) | **2.488 Gbps Downstream / 1.244 Gbps Upstream** |
| Estándar Wi-Fi 6 | **IEEE 802.11ax** (OFDMA, 2.4/5/6 GHz, 1024-QAM) |
| Protocolo autenticación WPA3 | **SAE** (Simultaneous Authentication of Equals) |
| Pilares 5G NR | **eMBB** (Banda ancha), **URLLC** (Baja latencia), **mMTC** (IoT masivo) |
| Estándar Cableado Estructurado | **ISO/IEC 11801** y **ANSI/TIA/EIA-568** |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- [[wiki/entities/wi-fi-and-mobile-standards|Estándares Wi-Fi y Tecnologías Móviles]]

### Conceptos Teóricos:
- [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Cableado]]

### Síntesis de Estudio:
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
"""

write_file("wiki/sources/bloque4-tema06.md", TEMA06_MD)

TEMA07_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema07
  - modelo-osi
  - tcp-ip
  - ipv4
  - ipv6
  - subnetting
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Modelo ISO-OSI, TCP-IP, IPv4 e IPv6"
  - "bloque4-tema07"
---

# Resumen Fuente: Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema07.md|bloque4-tema07.md]].

---

## 📖 Resumen Ejecutivo

Este tema constituye el núcleo teórico de redes de comunicaciones en las oposiciones TAI. Realiza un estudio comparativo exhaustivo entre el **Modelo de Referencia OSI de 7 capas** (ISO/IEC 7498-1) y la **Pila de Protocolos TCP/IP de 4 capas** (RFC 1122), analizando las Unidades de Datos de Protocolo (PDU) y primitivas de servicio. Se detalla el direccionamiento IPv4 (clases tradicionales A/B/C/D/E, subnetting, VLSM, CIDR RFC 1519, cabecera de 20-60 bytes), el direccionamiento IPv6 (formato de 128 bits, ámbitos Link-Local, Unique Local y Global Unicast, autoconfiguración SLAAC con EUI-64 modificado, cabecera fija simplificada de 40 bytes y cabeceras de extensión), los protocolos de transporte TCP y UDP, y los Registros Regionales de Internet (RIRs como RIPE NCC).

---

## 🧩 Estructura y Desglose Temático

### 1. Modelo de Referencia ISO/OSI (7 Capas)
- **Concepto**: Modelo arquitectónico estándar desarrollado por ISO para la interconexión de sistemas heterogéneos.
- **Desglose de Capas y PDUs**:

| Nº | Capa OSI | PDU | Funciones Principales | Protocolos / Dispositivos |
|---|----------|-----|----------------------|---------------------------|
| **7** | **Aplicación** | Datos | Interfaz de servicios de red con las aplicaciones de usuario | HTTP, DNS, SMTP, SNMP, FTP, SSH |
| **6** | **Presentación** | Datos | Formateo, sintaxis, compresión y cifrado de datos | ASN.1, MIME, TLS/SSL, ASCII, JPEG |
| **5** | **Sesión** | Datos | Establecimiento, mantenimiento y sincronización de sesiones (puntos de control) | NetBIOS, RPC, PPTP, SCP |
| **4** | **Transporte** | Segmento | Comunicación extremo a extremo, control de flujo, multiplexación por puertos | TCP (orientado a conexión), UDP (no orientado) |
| **3** | **Red** | Paquete | Direccionamiento lógico global, enrutamiento y selección de ruta | IPv4, IPv6, ICMP, IPsec, OSPF, BGP / Routers |
| **2** | **Enlace de Datos** | Trama (*Frame*) | Direccionamiento físico (MAC), control de acceso al medio (MAC/LLC), detección de errores (CRC) | Ethernet (802.3), Wi-Fi (802.11), PPP, STP / Switches, Bridges |
| **1** | **Física** | Bit | Transmisión binaria no estructurada sobre el medio físico, voltajes, conectores | Cables UTP, Fibra, Hubs, Repetidores |

- **Primitivas de Comunicación OSI**: `Petición (Request)`, `Indicación (Indication)`, `Respuesta (Response)`, `Confirmación (Confirm)`.

### 2. Protocolo IPv4 (Internet Protocol Version 4)
- Definido en **RFC 791**. Direcciones de **32 bits (4 bytes)** en notación decimal con puntos (`192.168.1.1`).
- **Clases Históricas de Red**:
  - **Clase A**: `0.0.0.0` a `127.255.255.255` (Primer bit `0`, máscara `/8`, 126 redes, 16.7 millones de hosts).
  - **Clase B**: `128.0.0.0` a `191.255.255.255` (Primeros bits `10`, máscara `/16`, 16.384 redes, 65.534 hosts).
  - **Clase C**: `192.0.0.0` a `223.255.255.255` (Primeros bits `110`, máscara `/24`, 2 millones de redes, 254 hosts).
  - **Clase D**: `224.0.0.0` a `239.255.255.255` (Primeros bits `1110`, reservada para **Multicast**).
  - **Clase E**: `240.0.0.0` a `255.255.255.255` (Primeros bits `1111`, reservada para experimentación/investigación).
- **Rangos Privados (RFC 1918)**:
  - `10.0.0.0/8` (`10.0.0.0` - `10.255.255.255`)
  - `172.16.0.0/12` (`172.16.0.0` - `172.31.255.255`)
  - `192.168.0.0/16` (`192.168.0.0` - `192.255.255.255`)
- **Direcciones Especiales**:
  - `127.0.0.0/8`: Bucle local (*Loopback* - `127.0.0.1`).
  - `169.254.0.0/16`: Direcciones APIPA (Auto-IP si DHCP falla, RFC 3927).
  - `0.0.0.0/0`: Ruta por defecto / Red actual.
  - Dirección de Red (todos los bits de host a 0) y Dirección de Broadcast (todos los bits de host a 1).
- **Subnetting y CIDR (RFC 1519)**: Enrutamiento interdominio sin clases con máscaras de longitud variable (**VLSM**).
- **Cabecera IPv4**: Tamaño mínimo **20 bytes** (máximo 60 con opciones). Campos: Versión (4 bits), IHL (4 bits), Tipo de Servicio/DSCP (8 bits), Longitud Total (16 bits), Identificador (16 bits), Flags (3 bits: Reserved, DF-Don't Fragment, MF-More Fragments), Desplazamiento de Fragmento (13 bits), **TTL** (8 bits), **Protocolo** (8 bits: `1` ICMP, `6` TCP, `17` UDP, `89` OSPF), Checksum de Cabecera (16 bits), IP Origen (32 bits), IP Destino (32 bits).

### 3. Protocolo IPv6 (Internet Protocol Version 6)
- Definido en **RFC 8200** (estándar de Internet). Direcciones de **128 bits (16 bytes)** en notación hexadecimal separada por dos puntos (`2001:0db8:85a3::8a2e:0370:7334`).
- **Reglas de Abreviatura**: Omisión de ceros a la izquierda en bloques; sustitución de una secuencia contigua de bloques de ceros por `::` (una sola vez por dirección).
- **Ámbitos de Direcciones IPv6**:
  - **Enlace Local (Link-Local)**: `fe80::/10` (no enrutable fuera del enlace local; autoconfigurada obligatoria en cada interfaz activa).
  - **Global Unicast (GUA)**: `2000::/3` (públicas y enrutables globalmente en Internet).
  - **Unique Local (ULA)**: `fc00::/7` (equivalente a RFC 1918 privado; típicamente `fd00::/8`).
  - **Multicast**: `ff00::/8` (ej. `ff02::1` todos los nodos, `ff02::2` todos los routers).
  - **Loopback**: `::1/128`.
  - **No especificada**: `::/128`.
- **Autoconfiguración Sin Estado (SLAAC - RFC 4862)**:
  - El host envía peticiones *Router Solicitation* (RS) y recibe *Router Advertisement* (RA) con el prefijo de red `/64`.
  - **EUI-64 Modificado**: Genera el ID de interfaz de 64 bits a partir de la MAC de 48 bits: inserta `FF:FE` en el centro y conmuta el 7º bit del primer byte (bit Universal/Local).
  - **DAD (Duplicate Address Detection)**: Verifica con ICMPv6 Neighbor Solicitation que la dirección no esté duplicada en la red.
- **Cabecera IPv6 Simplificada**:
  - Tamaño fijo de **40 bytes** (procesamiento por hardware ultrarrápido).
  - Sin checksum de cabecera (delegado a capas 2 y 4), sin fragmentación en routers (solo el host emisor fragmenta mediante *Path MTU Discovery*).
  - Campos: Versión (4 bits), Traffic Class (8 bits), Flow Label (20 bits), Payload Length (16 bits), **Next Header** (8 bits), **Hop Limit** (8 bits, equivale a TTL), IP Origen (128 bits), IP Destino (128 bits).
  - **Cabeceras de Extensión**: Encadenadas mediante el campo *Next Header* (Hop-by-Hop, Routing, Fragment, ESP, AH, Destination Options).

### 4. Modelo TCP/IP y Protocolos de Transporte
- **Pila TCP/IP de 4 Capas (RFC 1122)**:
  1. Aplicación (combina capas 5, 6 y 7 de OSI).
  2. Transporte (TCP, UDP).
  3. Internet (IPv4, IPv6, ICMP, IGMP).
  4. Acceso a la Red (combina capas 1 y 2 de OSI: Ethernet, Wi-Fi, PPP).
- **TCP (Transmission Control Protocol - RFC 793 / 9293)**:
  - Conexión fiable orientada a conexión, control de flujo por ventana deslizante (*sliding window*), control de congestión (Tahoe, Reno, CUBIC), retransmisión de segmentos perdidos (ARQ con ACK acumulativo).
  - Establecimiento de conexión: **Three-Way Handshake** (`SYN` → `SYN-ACK` → `ACK`).
  - Cierre de conexión: **Four-Way Handshake** (`FIN` → `ACK` → `FIN` → `ACK`).
  - Cabecera: Mínimo **20 bytes** (máximo 60 con opciones). Flags: `URG`, `ACK`, `PSH`, `RST`, `SYN`, `FIN`.
- **UDP (User Datagram Protocol - RFC 768)**:
  - No orientado a conexión, no fiable, sin control de flujo ni retransmisión, mínimo overhead.
  - Cabecera fija de **8 bytes**: Puerto Origen (16 bits), Puerto Destino (16 bits), Longitud (16 bits), Checksum (16 bits).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Protocolo | Especificación Técnica |
|-----------------------|------------------------|
| Capas Modelo OSI | **7 capas** (Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación) |
| Capas Modelo TCP/IP | **4 capas** (Acceso a Red, Internet, Transporte, Aplicación) |
| Tamaño Cabecera IPv4 | **20 bytes mínimo** (hasta 60 bytes con opciones) |
| Tamaño Cabecera IPv6 | **40 bytes FIJOS** (sin checksum, usa cabeceras de extensión) |
| Tamaño Cabecera TCP | **20 bytes mínimo** (hasta 60 bytes con opciones) |
| Tamaño Cabecera UDP | **8 bytes FIJOS** |
| Rango APIPA IPv4 | `169.254.0.0/16` |
| Rango Loopback IPv4 / IPv6 | `127.0.0.0/8` / `::1/128` |
| Prefijo Link-Local IPv6 | `fe80::/10` |
| Prefijo Global Unicast IPv6 | `2000::/3` |
| Prefijo Multicast IPv6 | `ff00::/8` |
| Generación EUI-64 | Inserta `FFFE` en el medio de la MAC e invierte el **bit 7 (U/L)** |
| RIR para Europa | **RIPE NCC** (Réseaux IP Européens Network Coordination Centre) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Capa de Enlace]]
- [[wiki/entities/bgp-and-ospf|Protocolos de Enrutamiento: OSPF y BGP]]

### Conceptos Teóricos:
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]

### Síntesis de Estudio:
- [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI frente a TCP-IP]]
- [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema07.md", TEMA07_MD)

TEMA08_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 08: Arquitectura de Internet, Protocolos Web y Servicios"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema08
  - internet
  - http
  - tls
  - voip
  - bgp
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitectura de Internet, Protocolos Web y Servicios"
  - "bloque4-tema08"
---

# Resumen Fuente: Bloque 4 - Tema 08: Arquitectura de Internet, Protocolos Web y Servicios

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema08.md|bloque4-tema08.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en la infraestructura global de Internet, su jerarquía de operadores y puntos neutros (IXP), la evolución del protocolo HTTP (desde HTTP/1.0 hasta HTTP/3 sobre QUIC), el protocolo criptográfico TLS 1.3, los servicios de transferencia de ficheros (FTP, FTPS, SFTP), la telefonía sobre IP (VoIP con SIP y RTP), el sistema global de nombres de dominio (DNS jerárquico y registros) y la evolución de la World Wide Web hacia la Web Semántica (Web 3.0).

---

## 🧩 Estructura y Desglose Temático

### 1. Arquitectura y Enrutamiento Global en Internet
- **Jerarquía de Proveedores de Servicios de Internet (ISPs)**:
  - **Tier 1**: Operadores troncales globales (Tier 1 Backbones: Lumen, AT&T, Telia, NTT). No pagan por tránsito; intercambian tráfico entre sí mediante acuerdos de **Peering libre de liquidación** (*Settlement-Free Peering*).
  - **Tier 2**: Operadores regionales o nacionales. Hacen peering con otros Tier 2 y compran **Tránsito IP** a operadores Tier 1.
  - **Tier 3**: Proveedores de acceso final a empresas y usuarios residenciales. Compran tránsito a operadores Tier 2/1.
- **Puntos Neutros de Intercambio (IXP - Internet Exchange Points)**:
  - Infraestructuras físicas de conmutación donde múltiples ISPs, CDNs (Cloudflare, Akamai) y proveedores cloud intercambian tráfico directamente reduciendo costes y latencia (ej. **ESpanix** y **DE-CIX** en Madrid).
- **Sistemas Autónomos (AS) y Protocolos de Enrutamiento**:
  - **BGP (Border Gateway Protocol v4 - RFC 4271)**: Protocolo de Vector de Caminos (*Path Vector*) que intercambia rutas entre Sistemas Autónomos distintos mediante sesiones TCP (puerto **179**). Utiliza el atributo AS-PATH para prevenir bucles.
  - **OSPF (Open Shortest Path First - RFC 2328)**: Protocolo IGP de Estado de Enlace (*Link-State*) que calcula rutas óptimas dentro de un mismo Sistema Autónomo usando el algoritmo de **Dijkstra** (protocolo IP número **89**).

### 2. Protocolo HTTP y Evolución de la Web
- **HTTP (Hypertext Transfer Protocol)**: Protocolo cliente-servidor sin estado de la capa de aplicación.
- **Evolución de Versiones**:
  - **HTTP/1.0 (RFC 1945)**: Abre y cierra una conexión TCP por cada objeto solicitado (muy ineficiente).
  - **HTTP/1.1 (RFC 2616 / RFC 9112)**:
    - Conexiones persistentes por defecto (`Keep-Alive`).
    - *Pipelining* de peticiones (limitado por el bloqueo en cabeza de línea o *Head-of-Line Blocking* a nivel de aplicación).
    - Cabecera obligatoria `Host` (permite alojamiento virtual de múltiples dominios en una misma IP).
    - Transferencia fragmentada (*Chunked Transfer Encoding*).
  - **HTTP/2 (RFC 7540 / RFC 9113)** (Basado en SPDY de Google):
    - Protocolo binario (no texto plano).
    - **Multiplexación total**: Múltiples peticiones y respuestas simultáneas intercaladas en *streams* bidireccionales sobre una **única conexión TCP**.
    - Compresión de cabeceras mediante el algoritmo **HPACK** (RFC 7541).
    - *Server Push* (el servidor envía recursos anticipadamente).
    - Priorización de flujos (*Stream Prioritization*).
  - **HTTP/3 (RFC 9114)** (Basado en QUIC):
    - Funciona sobre el protocolo de transporte **QUIC** (RFC 9000), que opera sobre **UDP** (puerto **443 UDP**).
    - Elimina el bloqueo en cabeza de línea (*HoL Blocking*) a nivel de transporte de TCP.
    - Cifrado integrado nativo con **TLS 1.3** desde el primer paquete (0-RTT y 1-RTT connection setup).
    - Migración transparente de conexión (*Connection ID*) ante cambios de red (ej. de Wi-Fi a 4G/5G sin reiniciar conexión).
    - Algoritmo de compresión de cabeceras **QPACK** (RFC 9204).

### 3. Protocolo TLS (Transport Layer Security)
- Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación entre aplicaciones sobre la capa de transporte.
- **Evolución**: SSL 2.0/3.0 (inseguros/obsoletos) → TLS 1.0/1.1 (deprecados) → **TLS 1.2** (RFC 5246) → **TLS 1.3** (RFC 8446).
- **Mejoras Radicales en TLS 1.3**:
  - Negociación (*Handshake*) reducida de 2 viajes de ida y vuelta (2-RTT) a **1 solo RTT** (o **0-RTT** para conexiones reanudadas).
  - Eliminación de algoritmos obsoletos e inseguros (DES, 3DES, RC4, MD5, SHA-1, suites CBC, intercambio RSA estático sin secreto perfecto hacia adelante).
  - Obligatoriedad de **PFS (Perfect Forward Secrecy)** mediante Diffie-Hellman efímero (ECDHE).
  - Cifrado de las extensiones del Handshake (incluido el certificado del servidor).

### 4. Servicios de Transferencia de Archivos y Acceso Remoto
- **FTP (File Transfer Protocol - RFC 959)**:
  - Puertos: **21 TCP** (canal de control) y **20 TCP** (canal de datos en modo activo).
  - Modo Activo (`PORT`) vs. Modo Pasivo (`PASV` - el servidor abre puerto efímero, compatible con NAT/Firewall).
  - En texto plano; vulnerable a intercepción.
- **FTPS (FTP over SSL/TLS - RFC 4217)**: FTP tradicional protegido mediante TLS (modo explícito en puerto 21 o implícito en puerto 990).
- **SFTP (SSH File Transfer Protocol)**: Protocolo completamente diferente que opera encapsulado dentro del túnel seguro de **SSH** (puerto **22 TCP**).
- **SSH (Secure Shell - RFC 4253)**: Puerto **22 TCP**; sustituto seguro y cifrado de Telnet (puerto 23) y `rsh/rlogin`.

### 5. Telefonía sobre IP (VoIP)
- **SIP (Session Initiation Protocol - RFC 3261)**:
  - Protocolo de señalización de la capa de aplicación (puertos **5060 TCP/UDP** para texto plano, **5061 TCP** para TLS).
  - Responsable de iniciar, modificar y terminar sesiones multimedia (llamadas de voz y videoconferencia).
  - Utiliza **SDP** (Session Description Protocol - RFC 4566) para negociar códecs de audio/vídeo (G.711, G.729, Opus).
- **RTP / RTCP (Real-time Transport Protocol - RFC 3550)**:
  - Protocolos de transporte de datos multimedia en tiempo real sobre **UDP** (puertos efímeros pares para RTP y puertos impares para RTCP de control y estadísticas de jitter/paquetes perdidos).
  - **SRTP**: RTP seguro con cifrado AES.

---

## 🎯 Datos Clave para Oposiciones TAI

| Servicio / Protocolo | Puerto Estándar y RFC |
|----------------------|-----------------------|
| HTTP / HTTPS | **80 TCP** (RFC 9112) / **443 TCP** (TLS) |
| HTTP/3 (QUIC) | **443 UDP** (RFC 9114 / RFC 9000) |
| BGP v4 | **179 TCP** (RFC 4271) |
| OSPF v2 | Protocolo IP **89** (RFC 2328) |
| FTP Control / Datos Activo | **21 TCP** / **20 TCP** (RFC 959) |
| SSH / SFTP | **22 TCP** (RFC 4253) |
| SIP / SIPS | **5060 TCP/UDP** / **5061 TLS** (RFC 3261) |
| Compresión cabeceras HTTP/2 / HTTP/3 | **HPACK** (RFC 7541) / **QPACK** (RFC 9204) |
| Latencia Handshake TLS 1.3 | **1-RTT** (primera conexión) / **0-RTT** (reanudación) |
| IXP principal en España | **ESpanix** / **DE-CIX Madrid** |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/http-protocol|Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3]]
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL y Criptografía Web]]
- [[wiki/entities/bgp-and-ospf|Protocolos de Enrutamiento: OSPF y BGP]]
- [[wiki/entities/dns-protocol|Protocolo DNS]]

### Conceptos Teóricos:
- [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema08.md", TEMA08_MD)

TEMA09_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 09: Seguridad en Redes, Perímetros, Organismos y VPN"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema09
  - seguridad-redes
  - ens
  - ccn-cert
  - magerit
  - firewalls
  - vpn
  - ids-ips
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Seguridad en Redes, Perímetros, Organismos y VPN"
  - "bloque4-tema09"
---

# Resumen Fuente: Bloque 4 - Tema 09: Seguridad en Redes, Perímetros, Organismos y VPN

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema09.md|bloque4-tema09.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la seguridad en redes corporativas y en la Administración Pública española. Detalla el marco normativo e institucional español (CCN, CCN-CERT, Guías CCN-STIC, Esquema Nacional de Seguridad regulado por el **Real Decreto 311/2022**, metodología de análisis de riesgos **MAGERIT v3** y herramienta PILAR); la arquitectura de seguridad perimetral (cortafuegos de filtrado de paquetes, estado de inspección, proxies y NGFW); sistemas de protección activa de comunicaciones (IDS/IPS basados en firmas, anomalías y comportamiento; SIEM para correlación de eventos); y tecnologías de Redes Privadas Virtuales (IPsec en modos transporte/túnel con protocolos AH y ESP, OpenVPN, WireGuard y SSL/TLS VPNs).

---

## 🧩 Estructura y Desglose Temático

### 1. Marco Institucional y Normativo de Ciberseguridad en España
- **Centro Criptológico Nacional (CCN)**:
  - Organismo adscrito al **Centro Nacional de Inteligencia (CNI)** (Ley 11/2002).
  - Competente en la seguridad de las TIC en las administraciones públicas y en sistemas que procesan información clasificada.
- **CCN-CERT**:
  - Capacidad de Respuesta a Incidentes de Seguridad de la Información del CCN.
  - Alertas, guías técnicas, gestión de cibercrisis y herramientas de seguridad del Sector Público (**LUCIA**, **CARMEN**, **CLARA**, **INES**, **PILAR**, **REYES**).
- **Serie de Guías CCN-STIC**:
  - Normas, instrucciones y guías de buenas prácticas para la protección de sistemas TIC en la Administración (ej. Guía CCN-STIC 800 para el ENS).
- **Esquema Nacional de Seguridad (ENS)**:
  - Marco legal obligatorio para todo el Sector Público y sus proveedores tecnológicos privados.
  - Actualizado por el **Real Decreto 311/2022** (derogando el RD 3/2010).
  - **Principios Básicos**: Seguridad integral, gestión de riesgos, prevención/reacción/recuperación, líneas de defensa, vigilancia continua y reevaluación periódica.
  - **Dimensiones de Seguridad**: Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad (**CITAD**).
  - **Categorías del Sistema**: **BÁSICA**, **MEDIA**, **ALTA** (determinadas por el impacto de un incidente en las dimensiones).
- **Metodología MAGERIT v3**:
  - Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información desarrollada por el Consejo Superior de Administración Electrónica (CSAE).
  - Estructura: Activos, Amenazas, Salvaguardas, Impacto y Riesgo Residual. Herramienta asociada: **PILAR**.

### 2. Seguridad Perimetral y Cortafuegos (Firewalls)
- **Evolución de los Cortafuegos**:
  - **1ª Generación (Filtrado de paquetes sin estado / Stateless)**: Inspecciona cabeceras de red y transporte (IP origen/destino, puerto, protocolo). No mantiene estado de la conexión.
  - **2ª Generación (Inspección con estado / Stateful Inspection)**: Mantiene una tabla de conexiones activas. Permite automáticamente el tráfico de retorno de conexiones legítimas salientes (`ESTABLISHED, RELATED`).
  - **3ª Generación (Pasarela a nivel de aplicación / Proxy)**: Termina la conexión del cliente y abre una nueva conexión con el servidor. Inspecciona el payload a nivel de aplicación (Nivel 7).
  - **NGFW (Next-Generation Firewall)**: Combina inspección con estado, prevención de intrusiones (IPS) en línea, inspección profunda de paquetes (**DPI**), descifrado SSL/TLS, control de aplicaciones (independiente del puerto) e integración con inteligencia de amenazas.

### 3. Sistemas de Protección y Monitorización (IDS, IPS, SIEM)
- **IDS (Intrusion Detection System)**: Sistema pasivo que monitoriza el tráfico mediante una copia (puerto espejo / SPAN o TAP). Detecta actividades sospechosas y genera alarmas sin bloquear el tráfico.
  - **NIDS** (Network-based IDS, ej. Snort, Suricata): Monitoriza el tráfico de la subred.
  - **HIDS** (Host-based IDS, ej. OSSEC, Wazuh): Monitoriza registros, integridad de archivos del sistema (`syscheck`) y llamadas al sistema en un equipo individual.
- **IPS (Intrusion Prevention System)**: Sistema activo colocado en línea (*in-line*) en el flujo de paquetes. Detecta y bloquea activamente los ataques en tiempo real (descartando paquetes o reseteando la sesión TCP con flags `RST`).
- **Técnicas de Detección**:
  - **Basada en Firmas / Patrones**: Compara el tráfico con reglas de vulnerabilidades conocidas (muy eficaz contra ataques conocidos, ineficaz contra ataques de día cero / *Zero-Day*).
  - **Basada en Anomalías / Comportamiento**: Define una línea base de comportamiento normal y alerta sobre desviaciones estadísticas (detecta ataques novedosos pero produce mayores tasas de falsos positivos).
- **SIEM (Security Information and Event Management)**:
  - Plataforma centralizada que recopila, normaliza, almacena y correlaciona eventos y logs de seguridad de múltiples fuentes (firewalls, servidores, routers, IDS, antivirus) en tiempo real (ej. Splunk, Elastic SIEM, Microsoft Sentinel).

### 4. Redes Privadas Virtuales (VPN)
- Una VPN permite extender de forma segura una red local privada sobre una red pública no confiable (Internet) mediante cifrado, autenticación e integridad.
- **Tipos de VPN**:
  - **Site-to-Site (LAN-to-LAN)**: Interconexión permanente de dos sedes o centros de datos a través de routers/firewalls VPN.
  - **Remote Access (Roadwarrior / Punto-a-Sitio)**: Conexión segura de un usuario remoto a la red corporativa mediante software cliente.

#### 4.1 Arquitectura IPsec (IP Security - RFC 4301)
- Conjunto de protocolos que operan en la **Capa de Red (Nivel 3)**:
- **Protocolos de Seguridad**:
  - **AH (Authentication Header - RFC 4302, protocolo IP 51)**: Proporciona autenticación de origen e integridad de datos de todo el paquete (incluyendo la cabecera IP). **NO cifra datos** (sin confidencialidad). Incompatible con NAT (el cambio de IP por NAT invalida el checksum de AH).
  - **ESP (Encapsulating Security Payload - RFC 4303, protocolo IP 50)**: Proporciona confidencialidad (cifrado), autenticación de origen e integridad. Permite atravesar NAT mediante encapsulación **NAT-Traversal (NAT-T)** en UDP puerto **4500**.
- **Modos de Operación de IPsec**:
  - **Modo Transporte**: Protege solo la carga útil (*payload*) del paquete IP; la cabecera IP original queda visible. Utilizado para comunicación host-a-host directa.
  - **Modo Túnel**: Encapsula el paquete IP original completo (cabecera + payload) dentro de un **nuevo paquete IP** con una nueva cabecera externa. Modo estándar para VPNs Site-to-Site y Remote Access.
- **IKE (Internet Key Exchange - IKEv1 RFC 2409, IKEv2 RFC 7296)**:
  - Protocolo de negociación y gestión de claves sobre **puerto 500 UDP**.
  - Establece las Asociaciones de Seguridad (**SA - Security Associations**) en dos fases (Fase 1: Canal seguro IKE SA; Fase 2: SAs de IPsec para transferencia de datos).

#### 4.2 Otras Tecnologías VPN
- **SSL/TLS VPN (OpenVPN / WireGuard)**:
  - **OpenVPN**: Opera sobre SSL/TLS en espacio de usuario (puerto por defecto **1194 UDP/TCP**), usa interfaces virtuales `tun`/`tap`.
  - **WireGuard**: Protocolo moderno de VPN ultrarrápido y ligero integrado en el kernel de Linux (criptografía moderna: ChaCha20, Curve25519, Poly1305, BLAKE2s).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Norma | Especificación Técnica |
|-------------------|------------------------|
| Marco Legal ENS | **Real Decreto 311/2022** (2 de mayo de 2022) |
| Adscripción del CCN | **Centro Nacional de Inteligencia (CNI)** |
| Dimensiones ENS | **CITAD** (Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad) |
| Metodología de Riesgos | **MAGERIT v3** (Herramienta PILAR) |
| Protocolos IPsec | **AH** (Protocolo IP 51, sin cifrado) y **ESP** (Protocolo IP 50, con cifrado) |
| Puertos IKE / NAT-T | **500 UDP** (IKE) / **4500 UDP** (NAT-Traversal) |
| Modos IPsec | **Transporte** (solo datos) vs. **Túnel** (paquete completo encapsulado) |
| Diferencia IDS vs IPS | IDS es pasivo (alerta fuera de banda); IPS es activo (bloquea en línea) |
| Herramientas CCN-CERT | **LUCIA** (gestión incidentes), **CARMEN** (APT), **CLARA** (auditoría Windows), **INES** (ENS) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ccn-cert-and-ens|CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, VPN e IPsec]]
- [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]

### Conceptos Teóricos:
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
- [[wiki/concepts/cryptography-and-digital-signatures|Criptografía y Firma Digital]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación]]

### Síntesis de Estudio:
- [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema09.md", TEMA09_MD)

TEMA10_MD = """---
title: "Resumen Fuente: Bloque 4 - Tema 10: Topologías LAN, Arquitectura IEEE 802 y Control de Acceso al Medio"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - tema10
  - topologias-lan
  - ieee-802
  - ethernet
  - csma-cd
  - switching
sources:
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Topologías LAN, Arquitectura IEEE 802 y Control de Acceso al Medio"
  - "bloque4-tema10"
---

# Resumen Fuente: Bloque 4 - Tema 10: Topologías LAN, Arquitectura IEEE 802 y Control de Acceso al Medio

Resumen exhaustivo procesado desde la fuente original [[raw/sources/bloque4-tema10.md|bloque4-tema10.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en los fundamentos de las redes de área local (LAN): topologías físicas y lógicas (bus, estrella, estrella extendida, anillo, doble anillo, malla, árbol, celular), la arquitectura y subcapas del comité **IEEE 802** (subcapa LLC 802.2 y subcapa MAC 802.3/802.11), los protocolos de control de acceso al medio compartido (**CSMA/CD** con algoritmo de retroceso exponencial binario y **CSMA/CA** con marcos RTS/CTS), la evolución de los estándares Ethernet (10BASE-T hasta 400GBASE-R), formatos de trama Ethernet II y 802.3, y técnicas de conmutación en switches (*Store-and-Forward*, *Cut-Through*, *Fragment-Free*).

---

## 🧩 Estructura y Desglose Temático

### 1. Topologías de Red (Físicas y Lógicas)
- **Topología en Bus**: Todos los nodos conectados a un medio compartido común con terminadores en los extremos (50 ohmios en coaxial). Ventaja: simplicidad y bajo coste inicial. Desventaja: una rotura del cable interrumpe toda la red; colisiones elevadas bajo carga.
- **Topología en Estrella**: Todos los nodos conectados a un nodo central concentrador (Hub o Switch). Ventaja: el fallo de un cable afecta solo a ese nodo; fácil diagnóstico y aislamiento. Desventaja: punto único de fallo en el concentrador central.
- **Topología en Estrella Extendida**: Jerarquía de estrellas donde conmutadores secundarios se conectan a un conmutador central/distribuidor.
- **Topología en Anillo (Ring)**: Los nodos se conectan en un circuito cerrado unidireccional donde la señal se regenera en cada nodo (ej. Token Ring IEEE 802.5, FDDI con doble anillo contrarrotatorio tolerante a cortes de fibra).
- **Topología en Malla (Mesh)**:
  - Malla Completa: Cada nodo conectado directamente a todos los demás. Número de enlaces: `N * (N - 1) / 2`. Máxima redundancia y tolerancia a fallos.
  - Malla Parcial: Interconexión redundante solo entre nodos críticos.
- **Topología en Árbol (Tree)**: Estructura jerárquica con nodo raíz y nodos hojas; común en redes corporativas con capas Núcleo (*Core*), Distribución y Acceso.
- **Topología Celular**: División geográfica en celdas hexagonales con estación base central (telefonía móvil, redes de sensores).

### 2. Estructura y Subcapas del Comité IEEE 802
El proyecto IEEE 802 divide la **Capa de Enlace de Datos (Nivel 2 de OSI)** en dos subcapas complementarias:
1. **Subcapa Superior: LLC (Logical Link Control - IEEE 802.2)**:
   - Proporciona una interfaz uniforme e independiente del medio físico a la capa de red (Nivel 3).
   - Utiliza puntos de acceso al servicio (**SAP**: SSAP y DSAP).
   - Tipos de servicio: Tipo 1 (No orientado a conexión sin acuse), Tipo 2 (Orientado a conexión con acuse), Tipo 3 (No orientado a conexión con acuse).
2. **Subcapa Inferior: MAC (Media Access Control)**:
   - Responsable del direccionamiento físico (direcciones MAC de 48 bits), delimitación de tramas, detección de errores (FCS / CRC-32) y control de acceso al medio de transmisión.

#### 2.1 Principales Estándares del Comité IEEE 802
- **IEEE 802.1**: Arquitectura general de redes, gestión, puenteo (*Bridging*) y protocolos:
  - **802.1D**: Protocolo Spanning Tree (STP).
  - **802.1w**: Rapid Spanning Tree Protocol (RSTP).
  - **802.1Q**: Etiquetado de VLANs (añade tag de 4 bytes con VLAN ID de 12 bits: 1 a 4094).
  - **802.1X**: Control de acceso a la red basado en puertos (Autenticación EAP con servidor RADIUS).
  - **802.1AX / 802.3ad**: Agregación de enlaces (LACP - Link Aggregation Control Protocol).
- **IEEE 802.2**: Logical Link Control (LLC).
- **IEEE 802.3**: Redes CSMA/CD (Ethernet cableado).
- **IEEE 802.5**: Token Ring (paso de testigo, en desuso).
- **IEEE 802.11**: Redes inalámbricas WLAN (Wi-Fi).
- **IEEE 802.15**: Redes de área personal inalámbricas (WPAN: 802.15.1 Bluetooth, 802.15.4 Zigbee).
- **IEEE 802.16**: Acceso inalámbrico de banda ancha (WiMAX).

### 3. Protocolos de Control de Acceso al Medio (MAC)

#### 3.1 CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
- Protocolo de contienda utilizado en Ethernet clásico sobre medios compartidos (Half-Duplex).
- **Mecanismo de Funcionamiento**:
  1. **Escucha (*Carrier Sense*)**: El nodo escucha el canal antes de transmitir (*Listen Before Talk*).
  2. **Transmisión**: Si el canal está libre (*Idle*), comienza a transmitir. Si está ocupado, espera.
  3. **Detección de Colisión**: Mientras transmite, sigue escuchando el medio. Si dos nodos transmiten a la vez, se detecta un aumento anómalo de voltaje (colisión).
  4. **Señal de Atasco (*Jam Signal*)**: El nodo emite una ráfaga de 32 a 48 bits de señal *Jam* para asegurar que todos los demás nodos detecten la colisión.
  5. **Algoritmo de Retroceso Exponencial Binario (BEB - *Binary Exponential Backoff*)**:
     - Tras la colisión número $k$ (donde $k = \min(n, 10)$ en el intento $n$), el nodo espera un tiempo aleatorio $r$ intervalos de ranura (*slot time* de 512 bits = 51.2 µs en Ethernet 10 Mbps), donde $r \in [0, 2^k - 1]$.
     - Si tras **16 colisiones consecutivas** no se logra transmitir, se descarta la trama y se reporta error a la capa superior.
- **Tamaño Mínimo de Trama en Ethernet**:
  - Fijado en **64 bytes (512 bits)** para asegurar que el emisor siga transmitiendo cuando la señal reflejada por una colisión en el extremo más alejado de la red regrese al emisor (*Slot Time > 2 * Tiempo de propagación máximo*). Tramas menores a 64 bytes son descartadas como *Runt Frames*.

#### 3.2 CSMA/CA (Collision Avoidance)
- Utilizado en redes inalámbricas Wi-Fi (IEEE 802.11) donde la detección física de colisiones es inviable debido a que el emisor satura su propio receptor (*Problema del Nodo Oculto*).
- Utiliza tiempos de espera intertramas (**IFS**: SIFS, PIFS, DIFS) y opcionalmente el mecanismo de reserva de canal mediante tramas de control **RTS** (*Request to Send*) y **CTS** (*Clear to Send*) con vector de reserva virtual **NAV** (*Network Allocation Vector*).

### 4. Formato de Trama Ethernet y Métodos de Conmutación
- **Estructura de Trama Ethernet II (DIX v2)**:
  - **Preámbulo**: 7 bytes de sincronismo (`10101010`).
  - **SFD (Start Frame Delimiter)**: 1 byte (`10101011`).
  - **MAC Destino**: 6 bytes (48 bits).
  - **MAC Origen**: 6 bytes (48 bits).
  - **EtherType**: 2 bytes (indica el protocolo de capa 3: `0x0800` IPv4, `0x86DD` IPv6, `0x8100` VLAN 802.1Q, `0x0806` ARP).
  - **Payload (Datos)**: 46 a 1500 bytes (MTU estándar de 1500 bytes; tramas *Jumbo Frames* soportan hasta 9000 bytes).
  - **FCS (Frame Check Sequence)**: 4 bytes (código de redundancia cíclica CRC-32).
  - **Tamaño total de trama**: Mínimo **64 bytes**, máximo **1518 bytes** (1522 bytes con etiqueta VLAN 802.1Q).
- **Métodos de Reenvío en Switches**:
  - **Store-and-Forward**: El switch recibe la trama completa, verifica el CRC-32 en el FCS y, si no tiene errores, la reenvía. Mayor latencia, máxima fiabilidad (descarta tramas corruptas).
  - **Cut-Through (Fast-Forward)**: El switch lee solo los primeros 6 bytes (MAC destino) e inmediatamente empieza a reenviar la trama sin verificar errores. Mínima latencia.
  - **Fragment-Free**: Lee los primeros **64 bytes** (tamaño mínimo) para filtrar colisiones antes de reenviar.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Estándar | Especificación Técnica |
|----------------------|------------------------|
| Subcapas Capa Enlace IEEE 802 | **LLC (802.2)** + **MAC (802.3 / 802.11)** |
| Tamaño Mínimo Trama Ethernet | **64 bytes** (512 bits / Slot Time) |
| Tamaño Máximo Trama Ethernet | **1518 bytes** estándar (**1522 bytes** con 802.1Q) |
| MTU Estándar Ethernet | **1500 bytes** |
| Max Intentos Colisión CSMA/CD | **16 intentos** (Backoff exponencial hasta intento 10: $2^{10} = 1024$) |
| EtherType IPv4 / IPv6 / ARP | `0x0800` (IPv4), `0x86DD` (IPv6), `0x0806` (ARP), `0x8100` (802.1Q) |
| Enlaces en Malla Completa | `N * (N - 1) / 2` |
| Estándar Etiquetado VLAN | **IEEE 802.1Q** (Tag de 4 bytes, VLAN ID 12 bits = 4094 VLANs) |
| Estándar Autenticación Puertos | **IEEE 802.1X** (EAP / RADIUS) |
| Estándar Spanning Tree | **IEEE 802.1D** (STP clásico) / **IEEE 802.1w** (RSTP rápido) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- [[wiki/entities/wi-fi-and-mobile-standards|Estándares Wi-Fi y Redes Inalámbricas]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos y Conmutación Segura]]

### Conceptos Teóricos:
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
"""

write_file("wiki/sources/bloque4-tema10.md", TEMA10_MD)

print("[*] 10 fuentes estructuradas ampliadas exitosamente.")
