# -*- coding: utf-8 -*-
"""
Script generador exhaustivo de notas de conocimiento para la Wiki del Bloque 4 (TAI).
Cubre Entities, Concepts y Syntheses con gran detalle técnico, datos memorísticos,
puertos, estándares RFC, comandos y tablas de examen.
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

# ==============================================================================
# ENTIDADES (25 Fichas Técnicas)
# ==============================================================================

ENTITIES = {
    "wiki/entities/linux-kernel.md": """---
title: "Linux Kernel y Software de Base"
type: "entity"
tags:
  - linux
  - kernel
  - operating-systems
  - software-base
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Núcleo Linux"
  - "Linux OS"
---

# Linux Kernel y Software de Base

El **Linux Kernel** es un núcleo monolítico modular de código abierto tipo UNIX creado originalmente por Linus Torvalds en 1991. Gestiona los recursos del hardware, la memoria virtual, los procesos, los controladores de dispositivos y el sistema de archivos del sistema operativo.

---

## 🏛️ Arquitectura y Subsistemas Principales

- **Arquitectura Monolítica Modular**: Aunque todos los servicios principales del sistema operativo se ejecutan en el espacio del núcleo (**Kernel Space / Ring 0**), el kernel puede cargar y descargar dinámicamente **módulos de kernel** (`.ko`) en tiempo de ejecución mediante `insmod`, `rmmod`, `modprobe` y `lsmod`.
- **Gestión y Planificación de Procesos**:
  - Planificador por defecto: **CFS (Completely Fair Scheduler)** basado en árboles rojo-negro (*Red-Black Trees*).
  - Llamadas al sistema de control de procesos: `fork()` (creación de proceso hijo duplicando el espacio de memoria mediante *Copy-On-Write*), `execve()` (reemplazo de imagen de proceso), `wait()` / `waitpid()` (sincronización con procesos hijos) y `exit()` (terminación).
  - Estados de proceso: `R` (Running/Runnable), `S` (Interruptible Sleep), `D` (Uninterruptible Sleep / I/O), `Z` (Zombie: finalizado sin recogida por el padre), `T` (Stopped).
- **Gestión de Memoria Virtual**:
  - Espacio de direcciones virtual dividido en Espacio de Usuario (Ring 3) y Espacio de Núcleo (Ring 0).
  - Asignación de memoria física mediante el algoritmo **Buddy System** y el asignador de objetos **SLAB / SLUB**.
  - Paginación bajo demanda con soporte de páginas estándar (4 KB) y páginas gigantes (*HugePages* de 2 MB / 1 GB).
  - Algoritmo de reemplazo de páginas (LRU - Least Recently Used) y área de intercambio (*Swap* / `swappiness`).
- **Sistema Virtual de Ficheros (VFS)**:
  - Capa de abstracción que unifica el acceso a diferentes sistemas de archivos (ext4, XFS, Btrfs, ZFS, NFS, procfs, sysfs).
  - Estructuras VFS: `superblock` (metadatos del sistema de archivos), `inode` (metadatos del archivo y punteros a bloques), `dentry` (asociación de nombres de archivo a inodos en caché) y `file` (estado de archivo abierto por un proceso).
- **Control de Acceso y Permisos POSIX**:
  - Permisos tradicionales: Lectura (`r`=4), Escritura (`w`=2), Ejecución (`x`=1) para Propietario (u), Grupo (g) y Otros (o).
  - Bits especiales: **SUID** (4000: ejecuta con privilegios del dueño), **SGID** (2000: herencia de grupo), **Sticky Bit** (1000: solo el dueño puede borrar ficheros en el directorio, ej. `/tmp`).
  - Listas de Control de Acceso extendidas: `getfacl` y `setfacl`.
- **Sistema de Inicialización y Servicios (systemd)**:
  - Sucesor de SysVinit y Upstart. Reemplaza el PID 1 tradicional.
  - Unidades de systemd: `.service` (servicios), `.target` (estados/niveles de ejecución, ej. `multi-user.target`, `graphical.target`), `.socket` (activación por socket), `.timer` (temporizadores programados tipo cron).
  - Comandos: `systemctl {start|stop|restart|status|enable|disable}`, `journalctl -u servicio -f`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Valor Técnico / Comando |
|---------|-------------------------|
| Tipo de Núcleo | **Monolítico Modular** |
| Planificador de CPU | **CFS (Completely Fair Scheduler)** |
| Tamaño de Página Estándar | **4 KB** |
| Permiso SUID / SGID / Sticky | `4000` (SUID), `2000` (SGID), `1000` (Sticky Bit) |
| Gestor de Servicios Moderno | **systemd** (PID 1) |
| Herramientas de Módulos | `lsmod`, `modprobe`, `insmod`, `rmmod` |
| Consulta de Logs systemd | `journalctl -xe` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
- Concepto: [[wiki/concepts/process-and-memory-management|Gestión de Procesos y Memoria]]
- Scripting: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
""",

    "wiki/entities/windows-server.md": """---
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
""",

    "wiki/entities/active-directory.md": """---
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
""",

    "wiki/entities/ldap-protocol.md": """---
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
""",

    "wiki/entities/bash-and-shell-scripting.md": """---
title: "Bash y Shell Scripting en Linux"
type: "entity"
tags:
  - bash
  - shell
  - linux
  - scripting
  - automation
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "GNU Bash"
  - "Bash Scripting"
---

# Bash y Shell Scripting en Linux

**GNU Bash (Bourne-Again Shell)** es el intérprete de comandos y lenguaje de programación de scripts estándar en sistemas operativos GNU/Linux, desarrollado originalmente por **Brian Fox** en 1988 para el proyecto GNU como sustituto libre del Bourne Shell (`sh`).

---

## 🏛️ Historia y Seguridad

- **Lanzamiento**: Primera versión beta (0.99) el **8 de junio de 1989**. Mantenido posteriormente por **Chet Ramey**.
- **Vulnerabilidad Shellshock (CVE-2014-6271)**:
  - Descubierta por **Stéphane Chazelas** en septiembre de 2014.
  - Fallo crítico que permitía la ejecución remota de código arbitrario al concatenar comandos al final de definiciones de funciones exportadas a través de variables de entorno (especialmente crítico en scripts CGI web).

---

## 🧩 Sintaxis y Variables Especiales

- **Shebang**: `#!/bin/bash` (indica al kernel el intérprete a utilizar).
- **Variables Especiales**:
  - `$0`: Nombre del script en ejecución.
  - `$1, $2, ... $n`: Argumentos posicionales pasados al script. A partir de 10 se referencian como `${10}`.
  - `$#`: Número total de argumentos pasados.
  - `$@`: Array con todos los argumentos como palabras separadas (`"$@"` preserva espacios).
  - `$*`: Cadena única con todos los argumentos separados por el primer carácter de `IFS`.
  - `$?`: Código de retorno del último comando ejecutado (`0` = éxito, `>0` = error).
  - `$$`: PID del proceso de la shell actual.
  - `$!`: PID del último proceso ejecutado en segundo plano (*background* con `&`).
- **Estructuras de Control**:
  - Condicional: `if [ condición ]; then ... elif [ ... ]; then ... else ... fi`
  - Selección: `case "$var" in patron1) ... ;; patron2) ... ;; *) ... ;; esac`
  - Bucles: `for var in lista; do ... done` y `while [ condición ]; do ... done`
  - Test extendido: `[[ expresión ]]` (soporta operadores regex `=~` y operadores lógicos `&&`, `||`).
- **Redirecciones y Tuberías**:
  - Redirección salida estándar: `>` (sobrescribe), `>>` (añade al final).
  - Redirección error estándar: `2>`, `2>&1` (redirige stderr a stdout), `&>` (redirige ambos).
  - Tubería (*Pipe*): `comando1 | comando2` (conecta la salida estándar de comando1 con la entrada de comando2).

---

## 🎯 Datos Clave para Oposiciones TAI

| Característica | Detalle Técnico |
|----------------|-----------------|
| Autor Original | **Brian Fox** (Proyecto GNU, 1988/1989) |
| Vulnerabilidad Shellshock | **CVE-2014-6271** (Septiembre 2014) |
| Código de Salida Exitoso | **0** (`$? == 0`) |
| Comprobación Ficheros | `-f` (es fichero regular), `-d` (es directorio), `-x` (es ejecutable), `-z` (cadena vacía) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
""",

    "wiki/entities/powershell.md": """---
title: "PowerShell y Cmdlets en Entornos Windows"
type: "entity"
tags:
  - powershell
  - windows
  - cmdlets
  - scripting
  - automation
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "PowerShell"
  - "Windows PowerShell"
  - "pwsh"
---

# PowerShell y Cmdlets en Entornos Windows

**PowerShell** es un marco de automatización de tareas y configuración multiplataforma compuesto por un intérprete de línea de comandos (CLI) y un potente lenguaje de scripting orientado a **objetos .NET**, desarrollado por Microsoft.

---

## 🏛️ Evolución y Características

- **Historia**: Primera versión lanzada en **noviembre de 2006** para Windows XP SP2 y Windows Server 2003.
- **PowerShell Core (Multiplataforma)**: Liberado como software de **código abierto** en **2016** bajo licencia MIT. Basado en .NET Core (`pwsh`), disponible para Windows, Linux y macOS.
- **Paradigma Orientado a Objetos**: A diferencia de los shells tradicionales de Unix basados en flujos de texto plano, los comandos de PowerShell (**Cmdlets**) reciben y emiten **instancias de objetos .NET**, permitiendo acceder directamente a propiedades y métodos a través del pipeline `|`.

---

## 🧩 Políticas de Ejecución (Execution Policies)

Para prevenir la ejecución inadvertida de scripts maliciosos, PowerShell incorpora directivas de control:

| Política | Comportamiento |
|----------|----------------|
| `Restricted` | Política por defecto en Windows cliente. No permite ejecutar scripts (`.ps1`); solo comandos interactivos. |
| `AllSigned` | Solo permite ejecutar scripts firmados digitalmente por un editor de confianza. |
| `RemoteSigned` | Permite ejecutar scripts locales sin firmar; exige firma digital para scripts descargados de Internet. |
| `Unrestricted` | Permite ejecutar cualquier script (muestra advertencia al ejecutar scripts de Internet). |
| `Bypass` | Desactiva por completo los bloqueos sin mostrar advertencias. |

---

## 🎯 Cmdlets Fundamentales

- `Get-Command`: Lista todos los cmdlets, funciones y alias disponibles.
- `Get-Help <cmdlet> -Full`: Muestra la documentación completa y ejemplos.
- `Get-Process` / `Stop-Process`: Gestión de procesos del sistema.
- `Get-Service` / `Start-Service` / `Stop-Service`: Control de servicios de Windows.
- `Get-EventLog` / `Get-WinEvent`: Consulta de logs del Visor de Eventos.
- `Invoke-Command -ComputerName <host> -ScriptBlock { ... }`: Ejecución remota vía WinRM (puertos **5985 HTTP** / **5986 HTTPS**).
- `ConvertTo-Html` / `Export-Csv`: Exportación estructurada de objetos.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Especificación Técnica |
|---------|------------------------|
| Año Lanzamiento / Open Source | **Noviembre 2006** / **2016** (Licencia MIT) |
| Estructura de Comandos | **Verbo-Sustantivo** (`Get-Process`, `Set-Item`) |
| Protocolo de Remoting | **WS-Man / WinRM** (Puertos **5985 HTTP** / **5986 HTTPS**) |
| Consultar/Cambiar Política | `Get-ExecutionPolicy` / `Set-ExecutionPolicy` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
- Entidad: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
""",

    "wiki/entities/relational-databases-rdbms.md": """---
title: "Bases de Datos Relacionales (RDBMS)"
type: "entity"
tags:
  - rdbms
  - sql
  - codd-rules
  - databases
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RDBMS"
  - "SGBD Relacional"
---

# Bases de Datos Relacionales (RDBMS)

Un **Sistema de Gestión de Bases de Datos Relacionales (RDBMS)** es un software basado en el modelo relacional introducido por **Edgar F. Codd** en 1970, donde los datos se organizan en tablas bidimensionales compuestas por filas (tuplas) y columnas (atributos).

---

## 🏛️ Las 12 Reglas de Codd (13 Reglas: 0 a 12)

1. **Regla 0 (Regla Fundacional)**: El sistema debe gestionar la base de datos enteramente mediante sus capacidades relacionales.
2. **Regla 1 (Regla de la Información)**: Toda la información se representa explícitamente en el nivel lógico en tablas mediante valores en posiciones de filas y columnas.
3. **Regla 2 (Acceso Garantizado)**: Cada dato atómico es direccionable lógicamente especificando el nombre de la tabla, la clave primaria (PK) y el nombre de la columna.
4. **Regla 3 (Tratamiento Sistemático de Valores Nulos)**: El SGBD debe soportar valores `NULL` para representar información faltante o inaplicable de forma independiente del tipo de datos.
5. **Regla 4 (Catálogo Dinámico en Línea)**: La descripción de la base de datos (metadatos) se almacena a nivel lógico en tablas relacionales consultables mediante el mismo lenguaje relacional.
6. **Regla 5 (Sublenguaje Comprensivo de Datos)**: Debe existir al menos un lenguaje (como SQL) que soporte DDL, DML, DCL, restricciones de integridad y gestión de transacciones.
7. **Regla 6 (Actualización de Vistas)**: Todas las vistas que sean teóricamente actualizables deben ser actualizables por el sistema.
8. **Regla 7 (Inserción, Actualización y Borrado de Alto Nivel)**: El sistema debe permitir manipular conjuntos de registros (*set-at-a-time*) en una sola sentencia.
9. **Regla 8 (Independencia Física de Datos)**: Los cambios en el almacenamiento físico o métodos de acceso no afectan a las aplicaciones a nivel lógico.
10. **Regla 9 (Independencia Lógica de Datos)**: Los cambios en las tablas base (añadir columnas, particionar tablas) que preserven la información no afectan a las vistas ni aplicaciones.
11. **Regla 10 (Independencia de Integridad)**: Las restricciones de integridad (PK, FK, CHECK, NOT NULL) deben almacenarse en el catálogo, no en los programas de aplicación.
12. **Regla 11 (Independencia de Distribución)**: La distribución de datos en múltiples sedes es transparente para el usuario.
13. **Regla 12 (No Subversión)**: Si el sistema dispone de interfaces de bajo nivel (registro a registro), no pueden utilizarse para sortear las reglas de seguridad o integridad relacionales.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Definición Técnica |
|----------|--------------------|
| Creador Modelo Relacional | **Edgar F. Codd** (IBM, 1970) |
| Componentes SQL | **DDL** (Definición), **DML** (Manipulación), **DCL** (Control), **TCL** (Transacciones) |
| Propiedades Transaccionales | **ACID** (Atomicidad, Consistencia, Aislamiento, Durabilidad) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Concepto: [[wiki/concepts/database-normalization-and-acid|Normalización de Bases de Datos y Propiedades ACID]]
- Entidad: [[wiki/entities/nosql-databases|Bases de Datos NoSQL]]
""",

    "wiki/entities/nosql-databases.md": """---
title: "Bases de Datos NoSQL y Big Data"
type: "entity"
tags:
  - nosql
  - big-data
  - cap-theorem
  - databases
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "NoSQL"
  - "Bases de Datos No Relacionales"
---

# Bases de Datos NoSQL y Big Data

Las bases de datos **NoSQL ("Not Only SQL")** son sistemas de gestión de datos no relacionales diseñados para ofrecer alto rendimiento, escalabilidad horizontal y esquemas flexibles para el tratamiento de datos masivos (*Big Data*).

---

## 🏛️ Teorema CAP y Modelo BASE

- **Teorema CAP (Eric Brewer)**: En un sistema distribuido de datos solo es posible garantizar simultáneamente **dos de las tres propiedades**:
  - **C (Consistency / Consistencia)**: Todos los nodos ven los mismos datos en el mismo instante.
  - **A (Availability / Disponibilidad)**: Cada petición no fallida recibe una respuesta.
  - **P (Partition Tolerance / Tolerancia a Particiones)**: El sistema continúa operando pese a pérdidas de comunicación entre nodos.
- **Modelo BASE (frente a ACID)**:
  - **BA (Basically Available)**: Disponibilidad básica garantizada.
  - **S (Soft State)**: El estado del sistema puede cambiar sin interacción del usuario debido a replicación en curso.
  - **E (Eventual Consistency)**: Consistencia eventual alcanzada cuando cesan las escrituras.

---

## 🧩 Familias NoSQL Principales

1. **Documentales**: Almacenan documentos semiestructurados JSON/BSON (ej. **MongoDB**, CouchDB).
2. **Clave-Valor**: Almacenes ultrarrápidos en memoria (ej. **Redis**, Memcached, AWS DynamoDB).
3. **Columnares / Familias de Columnas**: Optimizadas para analítica masiva (ej. **Apache Cassandra**, HBase).
4. **Grafos**: Nodos y relaciones para análisis de redes (ej. **Neo4j**, Amazon Neptune).

---

## 🎯 Datos Clave para Oposiciones TAI

| Modelo | Ejemplos Líderes | Caso de Uso |
|--------|------------------|-------------|
| Documental | MongoDB, Couchbase | Catálogos, CMS, JSON |
| Clave-Valor | Redis, DynamoDB | Sesiones, Caché ultrarrápida |
| Columnar | Cassandra, HBase | Time-series, Big Data OLAP |
| Grafos | Neo4j, ArangoDB | Redes sociales, Detección de fraude |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
""",

    "wiki/entities/raid-storage.md": """---
title: "Sistemas de Almacenamiento RAID, DAS, NAS y SAN"
type: "entity"
tags:
  - raid
  - storage
  - das
  - nas
  - san
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RAID"
  - "Storage Architectures"
---

# Sistemas de Almacenamiento RAID, DAS, NAS y SAN

Las tecnologías de almacenamiento masivo redundante proporcionan tolerancia a fallos, alta disponibilidad y alto rendimiento en infraestructuras corporativas.

---

## 🏛️ Niveles RAID (Redundant Array of Independent Disks)

| Nivel RAID | Nombre | Mínimo Discos | Tolerancia a Fallos | Capacidad Útil | Rendimiento |
|------------|--------|---------------|---------------------|----------------|-------------|
| **RAID 0** | Striping (Bandas) | 2 | **0 discos** (sin redundancia) | $N \times S$ (100%) | Máxima velocidad lectura/escritura |
| **RAID 1** | Mirroring (Espejo) | 2 | **1 disco** | $1 \times S$ (50%) | Buena lectura, escritura estándar |
| **RAID 5** | Paridad Distribuida | 3 | **1 disco** | $(N - 1) \times S$ | Buena lectura, penalización en escritura |
| **RAID 6** | Doble Paridad Distribuida | 4 | **2 discos simultáneos** | $(N - 2) \times S$ | Alta lectura, mayor penalización escritura |
| **RAID 10 (1+0)** | Espejo de Bandas | 4 | **1 disco por sub-array** (hasta 2) | $(N / 2) \times S$ (50%) | Excelente lectura y escritura |

---

## 🧩 Comparativa Arquitectónica: DAS vs NAS vs SAN

| Característica | DAS (Direct Attached) | NAS (Network Attached) | SAN (Storage Area Network) |
|----------------|-----------------------|------------------------|----------------------------|
| **Nivel de Acceso** | Bloque local | **Ficheros** (*File-level*) | **Bloques** (*Block-level*) |
| **Medio / Red** | Bus local (SATA/SAS/NVMe) | LAN compartida (TCP/IP) | Red dedicada de alta velocidad |
| **Protocolos** | SCSI, SATA, SAS | **NFS, SMB/CIFS** | **Fibre Channel (FC), iSCSI, FCoE** |
| **Escalabilidad** | Muy limitada | Media | Muy alta |
| **Rendimiento** | Alto | Limitado por LAN | Ultrarrápido |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Mínimo discos RAID 5 / RAID 6 | **3 discos** / **4 discos** |
| Tolerancia fallos RAID 5 / 6 | **1 disco** / **2 discos simultáneos** |
| Puerto estándar iSCSI | **3260 TCP** |
| Protocolos NAS típicos | **NFS** (Linux/UNIX) y **SMB/CIFS** (Windows) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Concepto: [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación]]
""",

    "wiki/entities/docker-and-containers.md": """---
title: "Docker y Motores de Contenedores"
type: "entity"
tags:
  - docker
  - containers
  - oci
  - devops
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Docker"
  - "Contenedores"
---

# Docker y Motores de Contenedores

**Docker** es una plataforma de software de código abierto que automatiza el despliegue de aplicaciones dentro de **contenedores de software**, proporcionando una capa adicional de abstracción y automatización de virtualización a nivel de sistema operativo sobre Linux.

---

## 🏛️ Primitivas del Kernel de Linux Subyacentes

1. **Namespaces (Aislamiento de Recursos)**:
   - `pid`: Aislamiento del árbol de procesos (el proceso principal dentro del contenedor es PID 1).
   - `net`: Interfaces de red virtuales, tablas de enrutamiento y puertos propios.
   - `mnt`: Puntos de montaje del sistema de ficheros.
   - `ipc`: Comunicación entre procesos (memoria compartida, colas de mensajes).
   - `uts`: Nombre de host (*hostname*) y dominio.
   - `user`: Mapeo de UIDs/GIDs (permite ser root dentro del contenedor y usuario sin privilegios fuera).
2. **Control Groups (cgroups v1/v2)**:
   - Medición y limitación estricta de recursos de hardware: CPU (`cpu.shares`, `cpuset`), Memoria RAM (`memory.limit_in_bytes`, swap), I/O de disco y ancho de banda de red.
3. **Union File Systems (Overlay2)**:
   - Sistema de almacenamiento por capas inmutables de solo lectura apiladas (*Image Layers*) con una fina capa superior efímera de lectura/escritura (*Container Layer*).

---

## 🎯 Instrucciones del Dockerfile y Comandos

- `FROM`: Define la imagen base.
- `RUN`: Ejecuta comandos durante la construcción de la imagen.
- `COPY` / `ADD`: Copia ficheros del host a la imagen (`ADD` soporta descompresión tar y URLs).
- `CMD` vs `ENTRYPOINT`: `ENTRYPOINT` fija el ejecutable principal; `CMD` proporciona los parámetros por defecto modificables por CLI.
- `EXPOSE`: Documenta los puertos de escucha.
- Comandos CLI: `docker build -t app:v1 .`, `docker run -d -p 8080:80 --name web app:v1`, `docker ps`, `docker logs -f web`, `docker exec -it web bash`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Técnica |
|----------|------------------------|
| Primitivas Kernel | **Namespaces** (Aislamiento) + **cgroups** (Límites de recursos) |
| Driver de Almacenamiento | **Overlay2** (UnionFS) |
| Runtime de Bajo Nivel OCI | **runc** |
| Runtime de Alto Nivel | **containerd** / **CRI-O** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
""",

    "wiki/entities/kubernetes.md": """---
title: "Kubernetes y Orquestación de Contenedores"
type: "entity"
tags:
  - kubernetes
  - k8s
  - orchestration
  - cloud-native
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Kubernetes"
  - "K8s"
---

# Kubernetes y Orquestación de Contenedores

**Kubernetes (K8s)** es una plataforma de orquestación de código abierto desarrollada originalmente por Google (proyecto Borg) y donada a la **CNCF (Cloud Native Computing Foundation)** para automatizar el despliegue, escalado y gestión de aplicaciones en contenedores.

---

## 🏛️ Arquitectura del Clúster K8s

### 1. Control Plane (Nodos Master)
- **`kube-apiserver`**: Punto central de entrada de la API REST de Kubernetes; valida y procesa peticiones.
- **`etcd`**: Almacén distribuido clave-valor de alta disponibilidad basado en el algoritmo de consenso **Raft** (puertos **2379 TCP** clientes, **2380 TCP** peer). Guarda todo el estado del clúster.
- **`kube-scheduler`**: Asigna Pods recién creados a nodos Worker en función de requisitos de recursos y afinidades.
- **`kube-controller-manager`**: Ejecuta los bucles de control que reconcilian el estado actual con el estado deseado (*Node Lifecycle Controller*, *ReplicaSet Controller*, *ServiceAccount Controller*).

### 2. Nodos Worker
- **`kubelet`**: Agente principal del nodo; asegura que los contenedores descritos en los PodSpecs estén corriendo y saludables.
- **`kube-proxy`**: Mantiene las reglas de red en los nodos (vía `iptables` o `IPVS`) para gestionar el balanceo hacia los Services.
- **Container Runtime**: Motor de ejecución compatible con **CRI** (Container Runtime Interface), ej. `containerd` o `CRI-O`.

---

## 🧩 Objetos y Recursos Principales

- **Pod**: Unidad mínima desplegable. Contiene uno o más contenedores que comparten la misma dirección IP (`localhost`), espacio de red y volúmenes.
- **Deployment**: Controlador declarativo que gestiona Pods mediante **ReplicaSets**, permitiendo *Rolling Updates* sin caídas y *Rollbacks*.
- **Service**: Abstracción que expone un conjunto de Pods bajo una IP y DNS estables:
  - `ClusterIP`: Solo accesible dentro del clúster (por defecto).
  - `NodePort`: Expone el servicio en un puerto estático en cada nodo del clúster (rango **30000-32767**).
  - `LoadBalancer`: Aprovisiona un balanceador de carga externo en el proveedor cloud.
- **Ingress**: Gestiona el acceso externo HTTP/HTTPS hacia los servicios internos con enrutamiento por host/ruta y terminación SSL.

---

## 🎯 Datos Clave para Oposiciones TAI

| Componente / Objeto | Especificación Técnica |
|---------------------|------------------------|
| Base de Datos de K8s | **etcd** (Consenso Raft, puertos **2379/2380 TCP**) |
| Unidad Mínima | **Pod** (comparte red e IP) |
| Rango de Puertos NodePort | **30000 - 32767 TCP** |
| CLI de Gestión | `kubectl` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Motores de Contenedores]]
- Concepto: [[wiki/concepts/microservices-and-middleware|Microservicios, APIs y Middleware]]
""",

    "wiki/entities/smtp-imap-pop3.md": """---
title: "Protocolos de Correo Electrónico: SMTP, IMAP y POP3"
type: "entity"
tags:
  - email
  - smtp
  - imap
  - pop3
  - protocols
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Protocolos de Correo"
  - "SMTP/POP3/IMAP"
---

# Protocolos de Correo Electrónico: SMTP, IMAP y POP3

Los protocolos de correo electrónico estructuran el transporte, entrega y sincronización de mensajes en redes IP.

---

## 🏛️ Comparativa Exhaustiva de Protocolos

| Protocolo | Función Principal | Puerto Plano | Puerto Seguro (SSL/TLS) | RFC Principal | Modelo Operativo |
|-----------|-------------------|--------------|-------------------------|---------------|------------------|
| **SMTP (Relay)** | Transferencia entre Servidores MTA | **25 TCP** | 25 con STARTTLS | RFC 5321 | *Push* (Envío) |
| **SMTP (Submission)** | Envío Cliente MUA a Servidor | **587 TCP** | 587 con STARTTLS | RFC 6409 | *Push* con Autenticación |
| **SMTPS (Legado)** | Envío directo sobre SSL | N/A | **465 TCP** | RFC 8314 | *Push* cifrado directo |
| **POP3** | Descarga de buzón al cliente | **110 TCP** | **995 TCP** (POP3S) | RFC 1939 | *Pull* (Descarga y borra) |
| **IMAP4** | Sincronización de carpetas en servidor | **143 TCP** | **993 TCP** (IMAPS) | RFC 3501 | *Sync* bidireccional |

---

## 🧩 Seguridad y Reputación de Dominio

1. **SPF (Sender Policy Framework - RFC 7208)**: Registro DNS `TXT` que autoriza qué IPs pueden enviar correos del dominio (ej. `v=spf1 ip4:192.0.2.1 include:_spf.google.com -all`).
2. **DKIM (DomainKeys Identified Mail - RFC 6376)**: Firma digital asimétrica en la cabecera `DKIM-Signature`; la clave pública se publica en DNS `TXT`.
3. **DMARC (RFC 7489)**: Política de alineación de SPF y DKIM con directivas: `p=none` (solo monitorizar), `p=quarantine` (a spam) o `p=reject` (rechazo total).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Valor Técnico |
|----------|---------------|
| Puerto SMTP Relay / Submission | **25 TCP** / **587 TCP** |
| Puertos Seguros IMAPS / POP3S | **993 TCP** / **995 TCP** |
| Finalización Cuerpo SMTP | Línea con un solo punto `<CRLF>.<CRLF>` |
| Códigos de Éxito / Error SMTP | `250 OK`, `354 Start mail input`, `550 User not found` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Síntesis: [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC]]
""",

    "wiki/entities/dns-protocol.md": """---
title: "Protocolo DNS (Domain Name System)"
type: "entity"
tags:
  - dns
  - networking
  - protocols
  - infrastructure
sources:
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DNS"
  - "Domain Name System"
---

# Protocolo DNS (Domain Name System)

El **Domain Name System (DNS)** es una base de datos jerárquica y distribuida definida en **RFC 1034** y **RFC 1035** que traduce nombres de dominio legibles para humanos (FQDN) en direcciones IP numéricas.

---

## 🏛️ Operación y Puertos

- **Puerto Estándar**: **53 TCP y UDP**.
  - **UDP 53**: Consultas estándar de resolución (límite tradicional de 512 bytes, ampliable mediante **EDNS0** - RFC 6891).
  - **TCP 53**: Transferencias de zona completas (**AXFR**) o incrementales (**IXFR**) entre servidores primarios y secundarios, y respuestas que superan los 512 bytes sin EDNS0.
- **Tipos de Servidores**:
  - **Servidores Raíz (`.`)**: 13 direcciones IP lógicas (`a.root-servers.net` a `m.root-servers.net`) operadas por distintas entidades mediante Anycast.
  - **Servidores TLD**: Gestionan dominios de nivel superior (`.es`, `.com`, `.gob.es`).
  - **Servidores Autoritativos**: Poseen los registros definitivos de una zona.
  - **Servidores Recursivos / Resolvers**: Resuelven consultas iterando en la jerarquía y almacenan resultados en caché según el **TTL** (*Time to Live*).

---

## 🧩 Tipos de Registros DNS Críticos

| Registro | Tipo | Función |
|----------|------|---------|
| `A` | Host IPv4 | Asocia un FQDN a una dirección IPv4 de 32 bits |
| `AAAA` | Host IPv6 | Asocia un FQDN a una dirección IPv6 de 128 bits |
| `CNAME` | Canonical Name | Alias de un nombre a otro FQDN |
| `MX` | Mail Exchanger | Servidor de correo del dominio con prioridad numérica |
| `NS` | Name Server | Servidor autoritativo para la zona |
| `PTR` | Pointer | Resolución inversa (IP a FQDN) en zonas `in-addr.arpa` o `ip6.arpa` |
| `SOA` | Start of Authority | Metadatos de la zona: Servidor primario, email del admin, Serial, Refresh, Retry, Expire, TTL mínimo |
| `TXT` | Text Record | Texto arbitrario (usado por SPF, DKIM, DMARC) |
| `SRV` | Service Record | Localización de servicios (puerto, protocolo, peso, prioridad) en Active Directory |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto DNS | **53 TCP/UDP** |
| Servidores Raíz Lógicos | **13** (`A` a `M`) |
| RFCs Fundacionales | **RFC 1034** y **RFC 1035** |
| Seguridad DNS | **DNSSEC** (RFC 4033-4035) mediante firmas digitales RRSIG/DNSKEY |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/dhcp-protocol|Protocolo DHCP]]
""",

    "wiki/entities/dhcp-protocol.md": """---
title: "Protocolo DHCP (Dynamic Host Configuration Protocol)"
type: "entity"
tags:
  - dhcp
  - networking
  - protocols
  - lan
sources:
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "DHCP"
  - "Dynamic Host Configuration Protocol"
---

# Protocolo DHCP (Dynamic Host Configuration Protocol)

**DHCP** (RFC 2131) es un protocolo cliente-servidor de la capa de aplicación que automatiza la asignación dinámica de parámetros de configuración IP (dirección IP, máscara de subred, puerta de enlace, servidores DNS).

---

## 🏛️ Puertos y Proceso de Concesión DORA

- **Puertos Estándar**:
  - **IPv4**: Servidor escucha en **67 UDP**; Cliente escucha en **68 UDP**.
  - **DHCPv6**: Servidor escucha en **547 UDP**; Cliente escucha en **546 UDP**.
- **Fases de la Concesión DORA**:
  1. **Discover (DHCPDISCOVER)**: El cliente envía broadcast (`255.255.255.255`, puerto 67) solicitando IP.
  2. **Offer (DHCPOFFER)**: El servidor responde ofreciendo una IP disponible con parámetros de red.
  3. **Request (DHCPREQUEST)**: El cliente solicita formalmente la IP ofrecida mediante broadcast.
  4. **Acknowledge (DHCPACK)**: El servidor confirma la concesión (*Lease*) y registra la asignación.
- **Tiempos de Renovación**:
  - **T1 (50% del tiempo de concesión)**: Intento de renovación unicast con el servidor emisor original.
  - **T2 (87.5% del tiempo de concesión)**: Si T1 no responde, reenvío en broadcast a cualquier servidor DHCP.
  - **Expiración (100%)**: La IP se libera si no se ha podido renovar.
- **DHCP Relay Agent (RFC 3046 / Opción 82)**: Permite a los routers reenviar las solicitudes broadcast locales hacia un servidor DHCP ubicado en otra subred.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puertos DHCPv4 | **67 UDP (Server)** / **68 UDP (Client)** |
| Puertos DHCPv6 | **547 UDP (Server)** / **546 UDP (Client)** |
| Secuencia de Concesión | **DORA** (Discover, Offer, Request, Acknowledge) |
| Renovación T1 / T2 | **50% (Unicast)** / **87.5% (Broadcast)** |
| IP Autoconfigurada si falla | **APIPA** (`169.254.0.0/16`) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Entidad: [[wiki/entities/dns-protocol|Protocolo DNS]]
- Concepto: [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
""",

    "wiki/entities/snmp-protocol.md": """---
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
""",

    "wiki/entities/siem-and-ids-ips.md": """---
title: "Sistemas SIEM, IDS e IPS de Monitorización y Seguridad"
type: "entity"
tags:
  - siem
  - ids
  - ips
  - soc
  - cybersecurity
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SIEM"
  - "IDS/IPS"
---

# Sistemas SIEM, IDS e IPS de Monitorización y Seguridad

Los sistemas de detección y prevención de intrusiones (**IDS/IPS**) y los sistemas de gestión de eventos de seguridad (**SIEM**) forman el núcleo de las operaciones de defensa y respuesta en Centros de Operaciones de Seguridad (SOC).

---

## 🏛️ Diferencias Clave: IDS vs IPS vs SIEM

| Sistema | Modo de Operación | Ubicación en Red | Acción ante Incidentes | Ejemplos Líderes |
|---------|-------------------|------------------|------------------------|------------------|
| **IDS** (Detection) | Pasivo / Fuera de banda | Puerto SPAN / TAP / Espejo | Genera alarmas, registra logs | Snort, Suricata, Zeek |
| **IPS** (Prevention) | Activo / En línea (*In-Line*) | Entre interfaces de red / NGFW | **Bloquea activamente** tráfico malicioso | Snort IPS, Cisco Firepower |
| **SIEM** (Event Mgmt) | Correlación global | Servidor centralizado | Recopila logs, correlaciona eventos en tiempo real | Splunk, Elastic SIEM, Wazuh, Sentinel |

---

## 🧩 Métodos de Detección en IDS/IPS

- **Basado en Firmas (Pattern Matching)**: Compara patrones de bytes y cabeceras contra bases de datos de vulnerabilidades conocidas (CVE). Rápido y preciso, pero vulnerable a ataques de día cero (*0-Day*).
- **Basado en Anomalías / Comportamiento**: Establece una línea base de tráfico legítimo y dispara alertas ante desviaciones estadísticas significativas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| NIDS vs HIDS | NIDS monitoriza subredes; HIDS monitoriza archivos y llamadas al sistema del host |
| Funciones Clave SIEM | Agregación, Normalización, Correlación en tiempo real y Alertas |
| Herramienta HIDS Open Source | **Wazuh** / **OSSEC** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]]
""",

    "wiki/entities/wi-fi-and-mobile-standards.md": """---
title: "Estándares Wi-Fi (IEEE 802.11) y Tecnologías Móviles (5G NR)"
type: "entity"
tags:
  - wifi
  - 802-11
  - 5g
  - mobile
  - wireless
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Wi-Fi"
  - "IEEE 802.11"
  - "5G NR"
---

# Estándares Wi-Fi (IEEE 802.11) y Tecnologías Móviles (5G NR)

Las tecnologías de comunicaciones inalámbricas abarcan las redes de área local inalámbricas (**WLAN - IEEE 802.11**) y las redes móviles de última generación (**5G NR**).

---

## 🏛️ Evolución de Estándares Wi-Fi (IEEE 802.11)

| Nombre Comercial | Estándar IEEE | Año | Frecuencias | Velocidad Máxima Teórica | Tecnología Clave |
|------------------|---------------|-----|-------------|--------------------------|------------------|
| **Wi-Fi 1** | 802.11b | 1999 | 2.4 GHz | 11 Mbps | DSSS |
| **Wi-Fi 2** | 802.11a | 1999 | 5 GHz | 54 Mbps | OFDM |
| **Wi-Fi 3** | 802.11g | 2003 | 2.4 GHz | 54 Mbps | OFDM |
| **Wi-Fi 4** | 802.11n | 2009 | 2.4 / 5 GHz | 600 Mbps | MIMO (hasta 4x4) |
| **Wi-Fi 5** | 802.11ac | 2013 | 5 GHz | 6.93 Gbps | MU-MIMO, Canales 80/160 MHz, 256-QAM |
| **Wi-Fi 6 / 6E** | 802.11ax | 2019 / 2021 | 2.4 / 5 / **6 GHz** | **9.6 Gbps** | **OFDMA**, 1024-QAM, BSS Coloring, TWT |
| **Wi-Fi 7** | 802.11be | 2024 | 2.4 / 5 / 6 GHz | **46 Gbps** | Canales 320 MHz, 4096-QAM, MLO |

---

## 🧩 Protocolos de Seguridad Wi-Fi

- **WEP**: Cifrado RC4 con claves de 64/128 bits e IVs cortos de 24 bits (completamente vulnerable).
- **WPA**: Incorporó **TKIP** (Temporal Key Integrity Protocol) y comprobación de integridad Michael.
- **WPA2**: Estándar basado en **IEEE 802.11i** con cifrado robusto **AES-CCMP**.
- **WPA3**: Protocolo actual obligatorio. Sustituye el handshake de 4 vías por **SAE (Simultaneous Authentication of Equals)** basado en protocolo Dragonfly (inmune a ataques de diccionario offline). En modo Enterprise utiliza cifrado de **192 bits**.

---

## 📱 Tecnologías Móviles 5G NR (3GPP)

- **Pilares de 5G NR**:
  1. **eMBB (Enhanced Mobile Broadband)**: Alta velocidad de descarga (hasta 10-20 Gbps).
  2. **URLLC (Ultra-Reliable Low-Latency Communications)**: Latencia ultra baja (<1 ms) para vehículos autónomos e industria 4.0.
  3. **mMTC (Massive Machine-Type Communications)**: Conexión simultánea de hasta $10^6$ dispositivos IoT por $\text{km}^2$.
- **Modos de Despliegue**:
  - **NSA (Non-Standalone)**: Señalización sobre núcleo 4G (EPC) y radio 5G NR.
  - **SA (Standalone)**: Radio 5G NR conectada directamente al nuevo núcleo nativo **5G Core (5GC)**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Wi-Fi 6 Estándar | **IEEE 802.11ax** (OFDMA, 1024-QAM) |
| Banda nueva en Wi-Fi 6E / 7 | **Banda de 6 GHz** |
| Autenticación WPA3 | **SAE** (Simultaneous Authentication of Equals) |
| Latencia objetivo URLLC | **< 1 milisegundo** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Concepto: [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
""",

    "wiki/entities/ipv4-and-ipv6.md": """---
title: "Protocolos de Red: IPv4 e IPv6"
type: "entity"
tags:
  - ipv4
  - ipv6
  - networking
  - ip-protocols
  - addressing
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPv4"
  - "IPv6"
  - "Internet Protocol"
---

# Protocolos de Red: IPv4 e IPv6

El **Protocolo de Internet (IP)** es el protocolo fundamental de la capa de red (Nivel 3) responsable del direccionamiento lógico, enrutamiento y fragmentación de paquetes en la arquitectura de Internet.

---

## 🏛️ Comparativa Técnica Fundamental: IPv4 vs IPv6

| Característica | IPv4 (RFC 791) | IPv6 (RFC 8200) |
|----------------|----------------|-----------------|
| **Longitud de Dirección** | **32 bits (4 bytes)** | **128 bits (16 bytes)** |
| **Espacio de Direcciones** | $\approx 4.29 \times 10^9$ ($2^{32}$) | $\approx 3.4 \times 10^{38}$ ($2^{128}$) |
| **Notación** | Decimal con puntos (`192.168.1.1`) | Hexadecimal con dos puntos (`2001:db8::1`) |
| **Tamaño Cabecera Base** | **20 a 60 bytes** (variable) | **40 bytes FIJOS** |
| **Checksum en Cabecera** | Sí (recalculado en cada salto) | **No** (eliminado para mayor velocidad) |
| **Fragmentación** | Realizada por el emisor y routers | **Solo por el host emisor** (PMTUD) |
| **Tipos de Comunicación** | Unicast, Multicast, **Broadcast** | Unicast, Multicast, **Anycast** (**Sin Broadcast**) |
| **Configuración de IP** | Manual o DHCP | Manual, DHCPv6 o **SLAAC** (RFC 4862) |
| **IPsec** | Opcional (añadido a posteriori) | **Nativo e integrado** en la especificación |

---

## 🧩 Ámbitos y Rangos Especiales

### Rangos IPv4 Notables
- `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`: Direcciones Privadas (RFC 1918).
- `127.0.0.0/8`: Bucle local (*Loopback*).
- `169.254.0.0/16`: APIPA (RFC 3927).
- `224.0.0.0/4`: Clase D (Multicast).

### Rangos IPv6 Notables
- `fe80::/10`: **Enlace Local (Link-Local)** (no enrutable fuera de la subred local).
- `2000::/3`: **Global Unicast (GUA)** (públicas y enrutables en Internet).
- `fc00::/7`: **Unique Local (ULA)** (privadas, típicamente `fd00::/8`).
- `ff00::/8`: **Multicast** (`ff02::1` todos los nodos, `ff02::2` todos los routers).
- `::1/128`: Loopback local.
- `::/128`: Dirección no especificada.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Cabecera IPv4 / IPv6 | **20-60 bytes** / **40 bytes fijos** |
| Longitud Dirección IPv4 / IPv6 | **32 bits** / **128 bits** |
| Prefijo Link-Local IPv6 | `fe80::/10` |
| Prefijo Global Unicast IPv6 | `2000::/3` |
| Campo Equivalente a TTL en IPv6 | **Hop Limit** (8 bits) |
| Campo Protocolo en IPv6 | **Next Header** (8 bits) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos ISO-OSI y TCP-IP]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
""",

    "wiki/entities/tcp-and-udp.md": """---
title: "Protocolos de Transporte: TCP y UDP"
type: "entity"
tags:
  - tcp
  - udp
  - transport-layer
  - networking
  - protocols
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TCP"
  - "UDP"
  - "Capa de Transporte"
---

# Protocolos de Transporte: TCP y UDP

Los protocolos **TCP** y **UDP** operan en la **Capa de Transporte (Nivel 4)** de la pila TCP/IP para proporcionar comunicación lógica proceso-a-proceso mediante el uso de puertos (16 bits: 0 a 65535).

---

## 🏛️ Comparativa: TCP vs UDP

| Característica | TCP (RFC 793 / 9293) | UDP (RFC 768) |
|----------------|----------------------|---------------|
| **Orientación a Conexión** | Sí (Handshake previo obligatorio) | No (Envío directo sin conexión) |
| **Fiabilidad / Entrega** | Fiable (Garantiza entrega y orden vía ACKs) | No fiable (*Best-Effort*, sin retransmisión) |
| **Control de Flujo** | Sí (Ventana Deslizante / *Sliding Window*) | No |
| **Control de Congestión** | Sí (Algoritmos Slow Start, Congestion Avoidance) | No |
| **Tamaño Cabecera** | **20 a 60 bytes** | **8 bytes FIJOS** |
| **Sobrecarga (Overhead)** | Alta | Mínima |
| **Casos de Uso Típicos** | Web (HTTP/1-2), Correo (SMTP), SSH, FTP, BGP | DNS, DHCP, VoIP (RTP), Streaming, HTTP/3 (QUIC) |

---

## 🧩 Protocolo TCP: Conexión y Flags

- **Three-Way Handshake (Establecimiento)**:
  1. Cliente $\rightarrow$ Servidor: `SYN` (Seq = $x$)
  2. Servidor $\rightarrow$ Cliente: `SYN-ACK` (Seq = $y$, Ack = $x + 1$)
  3. Cliente $\rightarrow$ Servidor: `ACK` (Seq = $x + 1$, Ack = $y + 1$)
- **Flags de Cabecera TCP**:
  - `SYN` (Sincronización), `ACK` (Confirmación), `FIN` (Cierre ordenado), `RST` (Reinicio inmediato), `PSH` (Envío inmediato a la aplicación), `URG` (Puntero urgente).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Cabecera TCP / UDP | **20 bytes mínimo** / **8 bytes fijos** |
| Rango de Puertos Bien Conocidos | **0 a 1023** |
| Rango de Puertos Registrados | **1024 a 49151** |
| Rango de Puertos Dinámicos / Efímeros | **49152 a 65535** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
""",

    "wiki/entities/bgp-and-ospf.md": """---
title: "Protocolos de Enrutamiento Dinámico: OSPF y BGP"
type: "entity"
tags:
  - routing
  - ospf
  - bgp
  - networking
  - protocols
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "OSPF"
  - "BGP"
  - "Protocolos de Enrutamiento"
---

# Protocolos de Enrutamiento Dinámico: OSPF y BGP

El enrutamiento dinámico permite a los routers intercambiar información de topología de red para calcular automáticamente las mejores rutas hacia cada destino.

---

## 🏛️ Comparativa: OSPF vs BGP

| Característica | OSPF (RFC 2328) | BGPv4 (RFC 4271) |
|----------------|-----------------|------------------|
| **Tipo de Protocolo** | **IGP** (Interior Gateway Protocol) | **EGP** (Exterior Gateway Protocol) |
| **Algoritmo** | **Estado de Enlace** (*Link-State* - Dijkstra SPF) | **Vector de Caminos** (*Path-Vector*) |
| **Ámbito** | Dentro de un único Sistema Autónomo (AS) | Interconexión entre distintos Sistemas Autónomos |
| **Protocolo de Transporte** | Encapsulado directo en **IP (Protocolo 89)** | Sesión sobre **TCP (Puerto 179)** |
| **Métrica Principal** | **Coste** ($\text{Coste} = \text{Ancho de Banda de Referencia} / \text{Ancho de Banda del Enlace}$) | Atributos de ruta (**AS-PATH**, Local Preference, MED, Weight) |
| **Estructura Jerárquica** | Jerarquía de Áreas (Área `0` / *Backbone Area*) | Sistemas Autónomos identificados por números **ASN** |
| **Convergencia** | Ultrarrápida | Diseñado para estabilidad y políticas de tráfico global |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto / Protocolo OSPF | **Protocolo IP 89** (Multicast `224.0.0.5` y `224.0.0.6`) |
| Puerto / Protocolo BGP | **Puerto 179 TCP** |
| Algoritmo OSPF | **Dijkstra** (SPF - Shortest Path First) |
| Área Backbone OSPF | **Área 0** (`0.0.0.0`) |
| Prevención Bucles BGP | Atributo **AS-PATH** (descarta rutas que contengan su propio ASN) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Concepto: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
""",

    "wiki/entities/http-protocol.md": """---
title: "Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3"
type: "entity"
tags:
  - http
  - http2
  - http3
  - quic
  - web
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "HTTP"
  - "HTTP/2"
  - "HTTP/3"
  - "QUIC"
---

# Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3

El **Hypertext Transfer Protocol (HTTP)** es el protocolo cliente-servidor de la capa de aplicación sobre el que se fundamenta la World Wide Web.

---

## 🏛️ Evolución Arquitectónica de HTTP

| Característica | HTTP/1.1 (RFC 9112) | HTTP/2 (RFC 9113) | HTTP/3 (RFC 9114) |
|----------------|---------------------|-------------------|-------------------|
| **Capa de Transporte** | **TCP** (Puerto 80/443) | **TCP** (Puerto 443 con TLS) | **QUIC sobre UDP** (Puerto 443) |
| **Formato de Mensaje** | Texto plano | **Binario** (Frames y Streams) | **Binario** (Frames y Streams) |
| **Multiplexación** | No (Pipelining limitado con HoL blocking) | **Sí** (Múltiples streams sobre 1 TCP) | **Sí nativa** (Streams independientes sin HoL) |
| **Compresión Cabeceras** | No | **HPACK** (RFC 7541) | **QPACK** (RFC 9204) |
| **Seguridad / Cifrado** | Opcional (HTTPS / TLS) | Prácticamente obligatorio (TLS 1.2+) | **Integrado por diseño (TLS 1.3 nativo)** |
| **Migración Conexión** | No (ligado a IP/Puerto TCP) | No | **Sí** (mediante *Connection ID*) |
| **Latencia Handshake** | 2-3 RTT (TCP + TLS) | 2-3 RTT | **0-RTT o 1-RTT** |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puerto HTTP / HTTPS | **80 TCP** / **443 TCP** |
| Puerto HTTP/3 | **443 UDP** |
| Transporte HTTP/3 | **QUIC (RFC 9000)** sobre UDP |
| Algoritmos de Compresión Cabeceras | **HPACK** (HTTP/2) y **QPACK** (HTTP/3) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]
- Concepto: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
""",

    "wiki/entities/tls-ssl-protocols.md": """---
title: "Protocolos TLS/SSL y Criptografía Web"
type: "entity"
tags:
  - tls
  - ssl
  - https
  - cryptography
  - security
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "TLS"
  - "SSL"
  - "Transport Layer Security"
---

# Protocolos TLS/SSL y Criptografía Web

**TLS (Transport Layer Security)** es el protocolo criptográfico estándar que proporciona comunicaciones seguras a través de Internet, garantizando **confidencialidad**, **integridad** y **autenticación**.

---

## 🏛️ Evolución de Versiones y Seguridad

- **SSL 2.0 / 3.0**: Diseñados por Netscape (1995/1996). Vulnerables (POODLE) y completamente obsoletos.
- **TLS 1.0 / 1.1**: Deprecados por IETF en RFC 8996 (2021).
- **TLS 1.2 (RFC 5246)**: Estándar ampliamente desplegado con negociación en 2 viajes de ida y vuelta (2-RTT).
- **TLS 1.3 (RFC 8446 - 2018)**:
  - **Reducción de Latencia**: Negociación en **1-RTT** (primera conexión) y **0-RTT** (*Early Data* para reanudaciones).
  - **Depuración Criptográfica**: Eliminación total de suites débiles (DES, 3DES, RC4, MD5, SHA-1, suites CBC vulnerables a BEAST/Lucky13).
  - **PFS Obligatorio**: Obliga el uso de intercambio de claves Diffie-Hellman efímero (**ECDHE** / DHE), eliminando el intercambio estático con RSA.
  - Cifrado del certificado del servidor durante el handshake.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Especificación Técnica |
|---------|------------------------|
| Versión Actual Recomendada | **TLS 1.3 (RFC 8446)** |
| Latencia Handshake TLS 1.3 | **1-RTT** (0-RTT en reanudación) |
| Requisito PFS | **ECDHE** (Curvas elípticas efímeras) |
| Puerto HTTPS Estándar | **443 TCP** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
- Concepto: [[wiki/concepts/cryptography-and-digital-signatures|Criptografía Simétrica, Asimétrica y Firma Digital]]
""",

    "wiki/entities/firewalls-and-vpn.md": """---
title: "Cortafuegos, Redes Privadas Virtuales (VPN) e IPsec"
type: "entity"
tags:
  - firewalls
  - vpn
  - ipsec
  - network-security
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Firewalls"
  - "VPN"
  - "IPsec"
---

# Cortafuegos, Redes Privadas Virtuales (VPN) e IPsec

Los **cortafuegos** y las **VPNs** constituyen las tecnologías fundamentales de protección perimetral e interconexión segura de redes sobre infraestructuras públicas.

---

## 🏛️ Protocolos IPsec (IP Security - RFC 4301)

Operan en la **Capa de Red (Nivel 3)** y constan de dos protocolos de seguridad y un protocolo de gestión de claves:

1. **AH (Authentication Header - RFC 4302, Protocolo IP 51)**:
   - Proporciona autenticación de origen e integridad sin cifrado (**NO aporta confidencialidad**).
   - Incompatible con NAT (el reemplazo de IPs por NAT rompe el hash de integridad de la cabecera IP).
2. **ESP (Encapsulating Security Payload - RFC 4303, Protocolo IP 50)**:
   - Proporciona **confidencialidad (cifrado)**, autenticación e integridad.
   - Compatible con NAT mediante **NAT-Traversal (NAT-T)** encapsulando en **UDP puerto 4500**.
3. **IKE (Internet Key Exchange - IKEv2 RFC 7296)**:
   - Negocia las Asociaciones de Seguridad (SA) y claves criptográficas sobre el puerto **500 UDP**.

### Modos de Operación de IPsec
- **Modo Transporte**: Protege solo la carga útil (*payload*); la cabecera IP original queda visible. Empleado en comunicaciones host-a-host directas.
- **Modo Túnel**: Encapsula el paquete IP original completo dentro de un nuevo paquete IP con una nueva cabecera externa. Empleado en VPNs Site-to-Site y Remote Access.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo / Función | Valor Técnico |
|---------------------|---------------|
| Protocolo IP AH | **Protocolo 51** (Solo autenticación/integridad) |
| Protocolo IP ESP | **Protocolo 50** (Cifrado + autenticación) |
| Puertos IKE / NAT-Traversal | **500 UDP** (IKE) / **4500 UDP** (NAT-T) |
| Puerto OpenVPN Estándar | **1194 UDP/TCP** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
- Síntesis: [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
""",

    "wiki/entities/ccn-cert-and-ens.md": """---
title: "CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad (ENS)"
type: "entity"
tags:
  - ccn-cert
  - ens
  - cni
  - magerit
  - public-sector-security
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "CCN-CERT"
  - "ENS"
  - "Esquema Nacional de Seguridad"
---

# CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad (ENS)

El **CCN-CERT** es el Centro Criptológico Nacional - Computer Emergency Response Team, adscrito al **Centro Nacional de Inteligencia (CNI)**, responsable de la ciberseguridad del Sector Público español y del cumplimiento del **Esquema Nacional de Seguridad (ENS)**.

---

## 🏛️ Marco Legal y Normativo

- **Regulación del ENS**: **Real Decreto 311/2022**, de 3 de mayo (derogó el RD 3/2010 para adaptarse a las nuevas amenazas y a la Directiva NIS).
- **Ámbito de Aplicación**: Obligatorio para toda la Administración General del Estado (AGE), Administraciones Autonómicas, Entidades Locales y entidades privadas que les presten servicios tecnológicos.
- **Dimensiones de Seguridad del ENS (CITAD)**:
  - **C**: Confidencialidad
  - **I**: Integridad
  - **T**: Trazabilidad
  - **A**: Autenticidad
  - **D**: Disponibilidad
- **Categorías de los Sistemas**:
  - **BÁSICA**: Daño limitado en caso de incidente.
  - **MEDIA**: Daño grave sobre los servicios o derechos ciudadanos.
  - **ALTA**: Daño muy grave sobre la seguridad nacional, infraestructuras críticas o servicios esenciales.

---

## 🧩 Herramientas y Guías CCN-STIC

- **Guías CCN-STIC**: Normas de seguridad de obligado cumplimiento o buenas prácticas (ej. Guía 800 para el ENS, serie 400 para comunicaciones seguras).
- **Herramientas del CCN-CERT**:
  - **LUCIA**: Gestión unificada de incidentes y cibercrisis.
  - **CARMEN**: Detección de Amenazas Persistentes Avanzadas (APT).
  - **CLARA**: Auditoría y verificación de cumplimiento de configuraciones en Windows y Linux.
  - **INES**: Declaración y auditoría del Estado de Seguridad del ENS.
  - **PILAR**: Análisis y gestión cuantitativa/cualitativa de riesgos según metodología **MAGERIT v3**.
  - **REYES**: Plataforma de ciberinteligencia y compartición de IOCs.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Legal / Técnica |
|----------|--------------------------------|
| Real Decreto Vigente del ENS | **Real Decreto 311/2022** (3 de mayo de 2022) |
| Organismo Adscripción CCN | **Centro Nacional de Inteligencia (CNI)** (Ley 11/2002) |
| Categorías de Seguridad ENS | **Básica, Media, Alta** |
| Dimensiones de Seguridad | **Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad (CITAD)** |
| Metodología de Riesgos Oficial | **MAGERIT v3** (Herramienta PILAR) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Síntesis: [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
""",

    "wiki/entities/ethernet-and-ieee-standards.md": """---
title: "Estándares Ethernet y Familia IEEE 802"
type: "entity"
tags:
  - ethernet
  - ieee-802-3
  - ieee-802
  - lan
  - mac
sources:
  - "raw/sources/bloque4-tema06.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Ethernet"
  - "IEEE 802.3"
  - "IEEE 802"
---

# Estándares Ethernet y Familia IEEE 802

La familia de estándares **IEEE 802** define las especificaciones de redes de área local (LAN) y metropolitana (MAN) en las capas física y de enlace de datos.

---

## 🏛️ Subcomités Clave de IEEE 802

- **IEEE 802.1**: Arquitectura general, gestión y puenteo (*Bridging*):
  - **802.1D**: Spanning Tree Protocol (STP).
  - **802.1w**: Rapid Spanning Tree Protocol (RSTP).
  - **802.1Q**: Etiquetado de VLANs (4 bytes añadidos, VLAN ID de 12 bits = 4094 VLANs).
  - **802.1X**: Control de acceso a la red basado en puertos (EAP/RADIUS).
- **IEEE 802.2**: Control de Enlace Lógico (LLC).
- **IEEE 802.3**: Redes Ethernet cableadas con CSMA/CD.
- **IEEE 802.11**: Redes inalámbricas WLAN (Wi-Fi).
- **IEEE 802.15**: Redes WPAN (Bluetooth 802.15.1, Zigbee 802.15.4).

---

## 🧩 Evolución de Estándares Ethernet (IEEE 802.3)

| Estándar | Nombre Comercial | Velocidad | Medio de Transmisión | Distancia Máxima |
|----------|------------------|-----------|----------------------|------------------|
| **10BASE-T** | Ethernet | 10 Mbps | Par trenzado Cat 3/5 | 100 m |
| **100BASE-TX** | Fast Ethernet | 100 Mbps | Par trenzado Cat 5 (2 pares) | 100 m |
| **1000BASE-T** | Gigabit Ethernet (802.3ab) | 1 Gbps | Par trenzado Cat 5e/6 (4 pares) | 100 m |
| **1000BASE-SX** | Gigabit Ethernet (802.3z) | 1 Gbps | Fibra Multimodo (850 nm) | 220 - 550 m |
| **1000BASE-LX** | Gigabit Ethernet (802.3z) | 1 Gbps | Fibra Monomodo (1310 nm) | 5 - 10 km |
| **10GBASE-T** | 10 Gigabit Ethernet (802.3an) | 10 Gbps | Par trenzado Cat 6A | 100 m |
| **10GBASE-SR** | 10 Gigabit Ethernet (802.3ae) | 10 Gbps | Fibra Multimodo (850 nm) | 300 m (OM3) |
| **10GBASE-LR** | 10 Gigabit Ethernet (802.3ae) | 10 Gbps | Fibra Monomodo (1310 nm) | 10 km |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Tamaño Trama Ethernet II | **64 bytes mínimo** / **1518 bytes máximo** (1522 bytes con 802.1Q) |
| MTU Estándar | **1500 bytes** |
| Protocolo Acceso Compartido | **CSMA/CD** (IEEE 802.3) |
| Longitud Dirección MAC | **48 bits (6 bytes)** |
| Tag VLAN IEEE 802.1Q | **4 bytes** (VLAN ID de 12 bits: 1 a 4094) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
"""
}

print("[*] Escribiendo 21 entidades especializadas ampliadas...")
for path, content in ENTITIES.items():
    write_file(path, content)

print("[*] Entidades completadas con éxito.")
