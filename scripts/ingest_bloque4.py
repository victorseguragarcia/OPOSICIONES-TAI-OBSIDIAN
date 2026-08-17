#!/usr/bin/env python3
"""
Automated Ingestion Script for Bloque 4 TAI Oposiciones Sources
Ingests all 10 raw sources from raw/sources/ into:
- wiki/sources/ (10 structured summary notes)
- wiki/entities/ (key technologies, standards, tools, protocols)
- wiki/concepts/ (theoretical paradigms, models, security & networking concepts)
- wiki/synthesis/ (master syllabus overview & comparative study guides)
And updates index.md and log.md.
"""

import os
import sys
import datetime
from pathlib import Path

# Force UTF-8 on Windows stdout
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
RAW_SOURCES_DIR = ROOT_DIR / "raw" / "sources"
TODAY = datetime.date.today().strftime("%Y-%m-%d")

# 10 Source definitions with takeaways, entities, and concepts
SOURCES_DATA = [
    {
        "id": "bloque4-tema01",
        "title": "Resumen Fuente: Bloque 4 - Tema 01: Administración del Sistema Operativo y Software de Base",
        "raw_file": "raw/sources/bloque4-tema01.md",
        "topic_name": "Administración del Sistema Operativo y Software de Base",
        "summary": "Fundamentos del software de base, arquitectura de sistemas operativos (kernel, espacio de usuario, llamadas al sistema), gestión de procesos, memoria virtual, sistemas de archivos (ext4, NTFS, ZFS) y administración en entornos Linux/UNIX y Windows Server.",
        "key_takeaways": [
            "Arquitectura del SO dividida en [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]] y [[wiki/concepts/process-and-memory-management|Gestión de Procesos y Memoria]].",
            "Sistemas de archivos modernos: control de permisos POSIX, ACLs, journaling y estructuras de inodos.",
            "Herramientas de scripting y automatización: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]] y [[wiki/entities/powershell|PowerShell]].",
            "Gestores de arranque (GRUB2, UEFI) y niveles de ejecución / `systemd`."
        ],
        "entities": ["linux-kernel", "windows-server", "bash-and-shell-scripting", "powershell"],
        "concepts": ["operating-system-architecture", "process-and-memory-management"]
    },
    {
        "id": "bloque4-tema02",
        "title": "Resumen Fuente: Bloque 4 - Tema 02: Administración de Bases de Datos, Virtualización y Cloud",
        "raw_file": "raw/sources/bloque4-tema02.md",
        "topic_name": "Administración de Bases de Datos, Virtualización y Cloud",
        "summary": "Arquitectura de sistemas gestores de bases de datos relacionales y no relacionales, principios ACID, optimización SQL, tecnologías de virtualización (hipervisores Tipo 1 y Tipo 2) y modelos de servicio Cloud Computing (IaaS, PaaS, SaaS).",
        "key_takeaways": [
            "Propiedades [[wiki/concepts/database-normalization-and-acid|ACID y Normalización de Bases de Datos]] para integridad transaccional.",
            "Comparativa de modelos de datos: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]] vs. [[wiki/entities/nosql-databases|Bases de Datos NoSQL]].",
            "Tecnologías de [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Cloud Computing]] con hipervisores KVM, VMware ESXi y Hyper-V.",
            "Modelos de despliegue en nube (Pública, Privada, Híbrida) y arquitecturas multitenant."
        ],
        "entities": ["relational-databases-rdbms", "nosql-databases"],
        "concepts": ["database-normalization-and-acid", "virtualization-and-cloud-computing"]
    },
    {
        "id": "bloque4-tema03",
        "title": "Resumen Fuente: Bloque 4 - Tema 03: Servidores de Correo, Contenedores y Middleware",
        "raw_file": "raw/sources/bloque4-tema03.md",
        "topic_name": "Servidores de Correo, Contenedores y Middleware",
        "summary": "Arquitectura de correo electrónico (MTA, MDA, MUA), protocolos de mensajería (SMTP, IMAP, POP3), tecnologías de contenerización (Docker, Kubernetes) y capas intermedias de software (Middleware, Message Brokers, Servidores de Aplicaciones).",
        "key_takeaways": [
            "Flujo de correo y protocolos estándar: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo SMTP, IMAP y POP3]].",
            "Mecanismos de autenticación y reputación de correo: SPF, DKIM y DMARC.",
            "Aislamiento a nivel de SO mediante [[wiki/entities/docker-and-containers|Docker y Contenedores]] y orquestación con [[wiki/entities/kubernetes|Kubernetes]].",
            "Arquitectura de software desacoplada mediante [[wiki/concepts/microservices-and-middleware|Microservicios y Middleware]]."
        ],
        "entities": ["smtp-imap-pop3", "docker-and-containers", "kubernetes"],
        "concepts": ["microservices-and-middleware"]
    },
    {
        "id": "bloque4-tema04",
        "title": "Resumen Fuente: Bloque 4 - Tema 04: Administración de Redes de Área Local",
        "raw_file": "raw/sources/bloque4-tema04.md",
        "topic_name": "Administración de Redes de Área Local",
        "summary": "Diseño, segmentación y gestión de redes locales (LAN). Configuración de VLANs (IEEE 802.1Q), protocolos Spanning Tree (STP/RSTP), agregación de enlaces (LACP), direccionamiento automático DHCP y resolución de nombres DNS.",
        "key_takeaways": [
            "Segmentación de tráfico en Capa 2 mediante VLANs y enlaces troncales 802.1Q.",
            "Prevención de bucles de topología mediante Spanning Tree Protocol (STP / RSTP).",
            "Servicios esenciales de infraestructura: [[wiki/entities/dns-protocol|Protocolo DNS]] y [[wiki/entities/dhcp-protocol|Protocolo DHCP]].",
            "Gestión y monitorización de dispositivos con [[wiki/entities/snmp-protocol|Protocolo SNMP]]."
        ],
        "entities": ["dns-protocol", "dhcp-protocol", "snmp-protocol"],
        "concepts": ["routing-and-switching-mechanisms"]
    },
    {
        "id": "bloque4-tema05",
        "title": "Resumen Fuente: Bloque 4 - Tema 05: Seguridad de Sistemas, Infraestructura CPD, Gestión Incidentes",
        "raw_file": "raw/sources/bloque4-tema05.md",
        "topic_name": "Seguridad de Sistemas, Infraestructura CPD, Gestión de Incidentes",
        "summary": "Diseño físico y lógico de Centros de Proceso de Datos (CPD), climatización, redundancia eléctrica (SAI, grupos electrógenos), planes de contingencia y continuidad de negocio (BCP, DRP), almacenamiento masivo (SAN, NAS, RAID) y gestión de incidentes.",
        "key_takeaways": [
            "Disponibilidad e infraestructura física según clasificación TIER I-IV en [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación ante Desastres]].",
            "Niveles de almacenamiento RAID (0, 1, 5, 6, 10) y redes de almacenamiento SAN (Fibre Channel, iSCSI) vs. NAS.",
            "Métricas clave de continuidad: RPO (Recovery Point Objective) y RTO (Recovery Time Objective).",
            "Gestión de incidentes de seguridad y monitorización con [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]."
        ],
        "entities": ["siem-and-ids-ips"],
        "concepts": ["datacenter-infrastructure-and-disaster-recovery"]
    },
    {
        "id": "bloque4-tema06",
        "title": "Resumen Fuente: Bloque 4 - Tema 06: Comunicaciones: Modos, Medios, Redes Móviles",
        "raw_file": "raw/sources/bloque4-tema06.md",
        "topic_name": "Comunicaciones: Modos, Medios, Equipos, Redes Móviles e Inalámbricas",
        "summary": "Teoría de transmisión de señales, medios de transmisión guiados (par trenzado Cat 5e/6/6A/7/8, fibra óptica monomodo/multimodo) y no guiados (radiofrecuencia, microondas), redes inalámbricas Wi-Fi (802.11a/b/g/n/ac/ax/be) y evolución móvil (4G LTE, 5G NR).",
        "key_takeaways": [
            "Medios guiados: atenuación, diafonía (crosstalk), ancho de banda y reflectometría.",
            "Fibra óptica: diferencias entre Monomodo (SMF, largo alcance) y Multimodo (MMF, CPDs).",
            "Estándares Wi-Fi y protocolos de seguridad (WPA2, WPA3-SAE).",
            "Arquitectura de redes celulares móviles y tecnologías 5G (eMBB, URLLC, mMTC)."
        ],
        "entities": ["wi-fi-and-mobile-standards"],
        "concepts": ["transmission-media-and-modes"]
    },
    {
        "id": "bloque4-tema07",
        "title": "Resumen Fuente: Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6",
        "raw_file": "raw/sources/bloque4-tema07.md",
        "topic_name": "Modelo ISO-OSI, Modelo TCP-IP, Protocolo IP (IPv4 e IPv6)",
        "summary": "Arquitectura de capas de comunicaciones, estudio exhaustivo de las 7 capas del Modelo OSI frente a las 4 capas de TCP/IP, cabeceras IP, direccionamiento, subnetting, CIDR, VLSM y transición a IPv6.",
        "key_takeaways": [
            "Comparación de capas y encapsulación en [[wiki/concepts/osi-and-tcp-ip-models|Modelos ISO-OSI y TCP-IP]].",
            "Estructura de cabeceras y fragmentación en [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]].",
            "Mecanismos de transición IPv6: Dual Stack, Tunneling (6in4, Teredo) y Traducción (NAT64/DNS64).",
            "Cálculo de subredes con máscaras de longitud variable (VLSM) y enrutamiento sin clases (CIDR)."
        ],
        "entities": ["ipv4-and-ipv6", "tcp-and-udp"],
        "concepts": ["osi-and-tcp-ip-models"]
    },
    {
        "id": "bloque4-tema08",
        "title": "Resumen Fuente: Bloque 4 - Tema 08: Internet: Protocolos HTTP, HTTPS, TLS y OSPF",
        "raw_file": "raw/sources/bloque4-tema08.md",
        "topic_name": "Internet: Arquitectura, Servicios, Protocolos HTTP, HTTPS, TLS y OSPF",
        "summary": "Topología global de Internet (Sistemas Autónomos, IXP, ISP Tier 1-3), protocolos de enrutamiento interior (IGP como OSPF, IS-IS) y exterior (EGP como BGP), evolución del protocolo web (HTTP/1.1, HTTP/2, HTTP/3 QUIC) y capa criptográfica TLS 1.3.",
        "key_takeaways": [
            "Enrutamiento dinámico basado en estado de enlace: [[wiki/entities/bgp-and-ospf|Protocolos OSPF y BGP]].",
            "Protocolos de transferencia hipertexto: HTTP/1.1 (conexiones persistentes), HTTP/2 (multiplexación binaria) y HTTP/3 (QUIC sobre UDP).",
            "Seguridad en capa de transporte mediante [[wiki/entities/tls-ssl-protocols|Protocolos TLS y SSL]] y certificados X.509.",
            "Arquitectura de jerarquía de Sistemas Autónomos (AS)."
        ],
        "entities": ["bgp-and-ospf", "tls-ssl-protocols"],
        "concepts": ["internet-architecture-and-web-protocols"]
    },
    {
        "id": "bloque4-tema09",
        "title": "Resumen Fuente: Bloque 4 - Tema 09: Seguridad en Redes, CCN, VPN, Perimetral",
        "raw_file": "raw/sources/bloque4-tema09.md",
        "topic_name": "Seguridad en Redes, CCN, Seguridad Perimetral, VPN, Accesos",
        "summary": "Arquitectura de seguridad perimetral (DMZ, Cortafuegos Stateful / NGFW, WAF, Proxies), Redes Privadas Virtuales (IPsec, OpenVPN, WireGuard), Esquema Nacional de Seguridad (ENS) y guías CCN-STIC del Centro Criptológico Nacional.",
        "key_takeaways": [
            "Seguridad perimetral y túneles seguros: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]].",
            "Marco normativo español de ciberseguridad pública: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]].",
            "Técnicas de defensa en profundidad y segmentación en zonas seguras (DMZ, LAN interna, Bastion Hosts).",
            "Principios de [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]."
        ],
        "entities": ["firewalls-and-vpn", "ccn-cert-and-ens"],
        "concepts": ["network-security-and-perimeter-defense"]
    },
    {
        "id": "bloque4-tema10",
        "title": "Resumen Fuente: Bloque 4 - Tema 10: Redes Locales: Tipología y Métodos de Acceso",
        "raw_file": "raw/sources/bloque4-tema10.md",
        "topic_name": "Redes Locales: Tipología, Técnicas de Transmisión, Métodos de Acceso",
        "summary": "Topologías físicas y lógicas de redes LAN (Estrella, Árbol, Malla, Anillo), técnicas de conmutación (circuitos, paquetes, datagramas, circuitos virtuales), estándares IEEE 802.3 (Ethernet) y métodos de acceso al medio (CSMA/CD y CSMA/CA).",
        "key_takeaways": [
            "Métodos de contienda y acceso al medio: CSMA/CD (Ethernet cableado) y CSMA/CA (Inalámbrico).",
            "Evolución del estándar Ethernet: Fast Ethernet (100 Mbps), Gigabit Ethernet (1 Gbps), 10G/40G/100G Ethernet.",
            "Topologías de red estructurada y cableado normalizado (ANSI/TIA/EIA-568, ISO/IEC 11801).",
            "Principios de conmutación y reenvío (Store-and-Forward, Cut-Through)."
        ],
        "entities": ["ethernet-and-ieee-standards"],
        "concepts": ["lan-topologies-and-mac-protocols"]
    }
]

def ensure_dirs():
    (WIKI_DIR / "sources").mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "entities").mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "concepts").mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "synthesis").mkdir(parents=True, exist_ok=True)

def write_wiki_sources():
    print("[*] Generating 10 structured source summaries in wiki/sources/...")
    for s in SOURCES_DATA:
        slug = f"{s['id']}.md"
        out_path = WIKI_DIR / "sources" / slug
        
        entities_links = [f"- [[wiki/entities/{e}|{e.replace('-', ' ').title()}]]" for e in s["entities"]]
        concepts_links = [f"- [[wiki/concepts/{c}|{c.replace('-', ' ').title()}]]" for c in s["concepts"]]
        takeaways_bullets = "\n".join([f"- {t}" for t in s["key_takeaways"]])
        
        content = f"""---
title: "{s['title']}"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-4
  - {s['id'].replace('bloque4-', '')}
sources:
  - "{s['raw_file']}"
created: "{TODAY}"
updated: "{TODAY}"
aliases:
  - "Resumen {s['topic_name']}"
  - "{s['id']}"
---

# {s['title']}

Resumen estructurado y puntos clave procesados desde la fuente original [[{s['raw_file']}|{s['raw_file'].split('/')[-1]}]].

---

## 📖 Resumen Ejecutivo
{s['summary']}

---

## 🎯 Puntos Clave para Oposiciones TAI
{takeaways_bullets}

---

## 🔗 Entidades y Conceptos Extraídos

### Entidades Relacionadas:
{chr(10).join(entities_links)}

### Conceptos Teóricos:
{chr(10).join(concepts_links)}

---

## 📚 Síntesis de Referencia
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Redes y Sistemas (TAI)]]
"""
        out_path.write_text(content, encoding="utf-8")
        print(f"    [OK] wiki/sources/{slug}")

def write_entities_and_concepts():
    print("\n[*] Generating extracted entities and concepts...")
    
    # 1. ENTITIES
    entities_data = [
        {
            "slug": "linux-kernel.md",
            "title": "Linux Kernel y Software de Base",
            "tags": ["linux", "kernel", "operating-systems", "software-base"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["Núcleo Linux", "Linux OS"],
            "content": """# Linux Kernel y Software de Base

El **Linux Kernel** es un núcleo monolítico modular que gestiona recursos de hardware, memoria virtual, planificación de procesos y controladores de dispositivos en sistemas tipo UNIX.

## Componentes Clave
- **Gestión de Procesos**: Planificador CFS (Completely Fair Scheduler), estados de proceso (R, S, D, Z, T), llamadas `fork()`, `exec()`, `wait()`.
- **Memoria Virtual**: Paginación bajo demanda, swap, TLB y asignador Buddy System.
- **Sistemas de Archivos**: VFS (Virtual File System) soportando ext4, XFS, Btrfs y ZFS.
- **Gestión de Servicios**: Init tradicional vs. `systemd` (unidades `.service`, `.target`, `systemctl`, `journalctl`).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
- Scripting: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
"""
        },
        {
            "slug": "windows-server.md",
            "title": "Windows Server y Administración de Dominios",
            "tags": ["windows", "windows-server", "active-directory", "operating-systems"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["Windows Server OS", "Active Directory"],
            "content": """# Windows Server y Administración de Dominios

**Windows Server** es la plataforma de servidor empresarial de Microsoft basada en el núcleo Windows NT.

## Servicios Principales
- **Active Directory Domain Services (AD DS)**: Base de datos distribuida de objetos (usuarios, equipos, grupos) basada en LDAP, Kerberos y DNS.
- **Directivas de Grupo (GPO)**: Gestión centralizada de configuraciones y políticas de seguridad en el dominio.
- **Servicios de Red**: Roles integrados de DNS, DHCP, NPS (Network Policy Server) y Remote Desktop Services.
- **Sistemas de Archivos**: NTFS (con soporte de ACLs, cifrado EFS y cuotas) y ReFS (Resilient File System).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Automatización: [[wiki/entities/powershell|PowerShell]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
"""
        },
        {
            "slug": "bash-and-shell-scripting.md",
            "title": "Bash y Shell Scripting en Entornos UNIX/Linux",
            "tags": ["bash", "shell", "scripting", "linux", "automation"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["Bash Scripting", "Shell Scripting"],
            "content": """# Bash y Shell Scripting en Entornos UNIX/Linux

**Bash (Bourne Again Shell)** es el intérprete de comandos y lenguaje de scripting predeterminado en la mayoría de distribuciones GNU/Linux.

## Características Fundamentales
- **Redirecciones y Tuberías**: Canales estándar `stdin` (0), `stdout` (1), `stderr` (2), pipelines `|` y redirecciones `>`, `>>`, `2>&1`.
- **Variables y Parámetros Especiales**: `$0` (nombre script), `$#` (nº argumentos), `$?` (código de salida), `$$` (PID).
- **Control de Flujo**: Estructuras `if/then/elif/else`, bucles `for`, `while`, `until` y sentencias `case`.
- **Filtros de Procesamiento de Texto**: `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `find`, `xargs`.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Kernel: [[wiki/entities/linux-kernel|Linux Kernel y Software de Base]]
"""
        },
        {
            "slug": "powershell.md",
            "title": "PowerShell y Automatización de Administración",
            "tags": ["powershell", "windows", "automation", "scripting"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["PowerShell Core", "pwsh"],
            "content": """# PowerShell y Automatización de Administración

**PowerShell** es un entorno de automatización de tareas y administración de configuración multiplataforma basado en el framework .NET.

## Arquitectura Basada en Objetos
- A diferencia de las shells tradicionales que transmiten texto sin formato, los cmdlets de PowerShell transmiten **objetos tipados .NET** a través del pipeline `|`.
- **Nomenclatura Verbo-Sustantivo**: Estandarización de comandos como `Get-Process`, `Set-Service`, `New-Item`, `Restart-Computer`.
- **Módulos y Remoting**: Administración remota segura mediante WinRM y SSH (PowerShell Remoting / Enter-PSSession).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Sistema: [[wiki/entities/windows-server|Windows Server]]
"""
        },
        {
            "slug": "relational-databases-rdbms.md",
            "title": "Bases de Datos Relacionales (RDBMS) y SQL",
            "tags": ["databases", "rdbms", "sql", "postgres", "oracle", "mysql"],
            "sources": ["raw/sources/bloque4-tema02.md"],
            "aliases": ["RDBMS", "Relational Databases", "SGBD Relacionales"],
            "content": """# Bases de Datos Relacionales (RDBMS) y SQL

Los **Sistemas Gestores de Bases de Datos Relacionales (RDBMS)** organizan los datos en tablas estructuradas con filas y columnas, gobernadas por el álgebra relacional y el estándar SQL.

## Motores Principales
- **PostgreSQL**: SGBD relacional orientado a objetos, altamente extensible y conforme con el estándar SQL.
- **Oracle Database / Microsoft SQL Server**: Soluciones empresariales de alto rendimiento con soporte clustering (RAC, AlwaysOn).
- **MySQL / MariaDB**: Motores relacionales ampliamente desplegados en servicios web.

## Propiedades Fundamentales
- Cumplimiento estricto de principios [[wiki/concepts/database-normalization-and-acid|ACID y Normalización de Bases de Datos]].
- Mecanismos de indexación (B-Tree, Hash, GIN, GiST), planes de ejecución y transacciones con niveles de aislamiento (Read Committed, Serializable).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Comparativa: [[wiki/entities/nosql-databases|Bases de Datos NoSQL]]
"""
        },
        {
            "slug": "nosql-databases.md",
            "title": "Bases de Datos NoSQL y Almacenamiento Distribuido",
            "tags": ["databases", "nosql", "mongodb", "redis", "cassandra"],
            "sources": ["raw/sources/bloque4-tema02.md"],
            "aliases": ["NoSQL", "Non-relational Databases"],
            "content": """# Bases de Datos NoSQL y Almacenamiento Distribuido

Las **Bases de Datos NoSQL** están diseñadas para modelos de datos flexibles, escalabilidad horizontal masiva y gestión de datos no estructurados o semiestructurados.

## Familias de Modelos NoSQL
1. **Documentales** (MongoDB, CouchDB): Almacenamiento en documentos JSON/BSON con esquemas dinámicos.
2. **Clave-Valor** (Redis, Memcached): Acceso ultra-rápido en memoria para caché y sesiones.
3. **Columnares** (Apache Cassandra, ScyllaDB): Optimizado para consultas analíticas sobre grandes volúmenes distribuidos.
4. **Grafos** (Neo4j): Optimizado para relaciones complejas entre entidades y redes.

## Teorema CAP y Consistencia
- Teorema de Brewer (CAP): En un sistema distribuido solo se pueden garantizar dos de las tres propiedades: Consistencia (C), Disponibilidad (A) y Tolerancia a Particiones (P).
- Modelo **BASE** (Basically Available, Soft state, Eventual consistency).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Alternativa Relacional: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
"""
        },
        {
            "slug": "docker-and-containers.md",
            "title": "Docker y Tecnologías de Contenedores",
            "tags": ["containers", "docker", "devops", "virtualization"],
            "sources": ["raw/sources/bloque4-tema03.md"],
            "aliases": ["Docker", "Contenedores", "Containerization"],
            "content": """# Docker y Tecnologías de Contenedores

**Docker** es una plataforma de virtualización a nivel de sistema operativo que permite empaquetar aplicaciones y sus dependencias en contenedores ligeros, portables y reproducibles.

## Mecanismos del Kernel Subyacentes
- **Linux Namespaces**: Proveen aislamiento de recursos (`pid`, `net`, `ipc`, `mnt`, `uts`, `user`).
- **Control Groups (cgroups)**: Limitan y monitorizan el consumo de CPU, memoria, I/O y red.
- **Union File Systems (Overlay2)**: Capas de almacenamiento de solo lectura con una capa superior modificable (Copy-on-Write).

## Objetos Docker
- **Dockerfile**: Receta declarativa de construcción de imágenes.
- **Docker Image**: Plantilla inmutable de solo lectura.
- **Container**: Instancia en ejecución de una imagen.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Orquestación: [[wiki/entities/kubernetes|Kubernetes]]
- Concepto: [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Cloud Computing]]
"""
        },
        {
            "slug": "kubernetes.md",
            "title": "Kubernetes y Orquestación de Contenedores",
            "tags": ["kubernetes", "k8s", "containers", "orchestration", "cloud"],
            "sources": ["raw/sources/bloque4-tema03.md"],
            "aliases": ["K8s", "Kubernetes Engine"],
            "content": """# Kubernetes y Orquestación de Contenedores

**Kubernetes (K8s)** es un orquestador open-source para la automatización del despliegue, escalado, balanceo de carga y gestión de aplicaciones en contenedores.

## Arquitectura de Clúster
- **Control Plane**: `kube-apiserver`, `etcd` (almacén de estado), `kube-scheduler`, `kube-controller-manager`.
- **Nodos de Trabajo (Worker Nodes)**: `kubelet`, `kube-proxy`, Container Runtime (CRI como containerd/CRI-O).

## Objetos Primarios
- **Pod**: Unidad atómica mínima de despliegue que agrupa uno o más contenedores compartiendo red y almacenamiento.
- **Deployment / ReplicaSet**: Gestión declarativa de réplicas y actualizaciones sin parada (Rolling Updates).
- **Service**: Abstracción para exponer pods con IP estable y balanceo de carga (ClusterIP, NodePort, LoadBalancer).
- **Ingress**: Controlador de acceso HTTP/HTTPS perimetral.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Contenedores: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Arquitectura: [[wiki/concepts/microservices-and-middleware|Microservicios y Middleware]]
"""
        },
        {
            "slug": "smtp-imap-pop3.md",
            "title": "Protocolos de Correo Electrónico: SMTP, IMAP y POP3",
            "tags": ["email", "smtp", "imap", "pop3", "protocols", "networking"],
            "sources": ["raw/sources/bloque4-tema03.md"],
            "aliases": ["SMTP", "IMAP", "POP3", "Servidores de Correo"],
            "content": """# Protocolos de Correo Electrónico: SMTP, IMAP y POP3

La arquitectura de correo electrónico estándar define agentes especializados (MUA, MTA, MDA) comunicados mediante protocolos de aplicación específicos.

## Protocolos de Transporte y Acceso
| Protocolo | Puerto Estándar | Puerto Seguro (TLS) | Función |
| :--- | :--- | :--- | :--- |
| **SMTP** (Simple Mail Transfer Protocol) | 25 / 587 | 465 (SMTPS) | Envío y retransmisión entre servidores (MTA a MTA). |
| **IMAP4** (Internet Message Access Protocol) | 143 | 993 (IMAPS) | Consulta y sincronización bidireccional en servidor. |
| **POP3** (Post Office Protocol) | 110 | 995 (POP3S) | Descarga local de mensajes desde el servidor. |

## Seguridad y Mecanismos Antispam
- **SPF (Sender Policy Framework)**: Registro DNS TXT que declara IPs autorizadas para enviar correos desde un dominio.
- **DKIM (DomainKeys Identified Mail)**: Firma criptográfica en cabeceras validada con clave pública en DNS.
- **DMARC**: Política que define la acción a tomar si SPF o DKIM fallan (none, quarantine, reject).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Seguridad Criptográfica: [[wiki/entities/tls-ssl-protocols|Protocolos TLS y SSL]]
"""
        },
        {
            "slug": "dns-protocol.md",
            "title": "Protocolo DNS (Domain Name System)",
            "tags": ["dns", "networking", "protocols", "infrastructure"],
            "sources": ["raw/sources/bloque4-tema04.md"],
            "aliases": ["DNS", "Domain Name System", "Servidores DNS"],
            "content": """# Protocolo DNS (Domain Name System)

El **Domain Name System (DNS)** es una base de datos jerárquica y distribuida que traduce nombres de dominio legibles para humanos en direcciones IP binarias.

## Jerarquía y Tipos de Servidores
- **Root Servers**: 13 servidores raíz nombrados de la A a la M.
- **TLD Servers**: Gestionan dominios de nivel superior (`.es`, `.com`, `.gob.es`).
- **Servidores Autoritativos**: Contienen los registros oficiales de una zona.
- **Servidores Recursivos (Resolvers)**: Realizan la búsqueda iterativa en nombre del cliente.

## Tipos de Registros DNS Críticos
- `A` (IPv4) / `AAAA` (IPv6): Mapeo nombre a dirección IP.
- `CNAME`: Alias canónico hacia otro nombre de dominio.
- `MX`: Servidores de intercambio de correo con prioridad.
- `PTR`: Registro de resolución inversa (IP a nombre).
- `NS`: Servidor autoritativo de la zona.
- `TXT`: Registros de texto (usados por SPF, DKIM, verificación de dominio).

## Seguridad DNS
- **DNSSEC**: Firma digital de registros DNS para evitar envenenamiento de caché (DNS Cache Poisoning / Spoofing).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Correo: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
- Direccionamiento: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]
"""
        },
        {
            "slug": "dhcp-protocol.md",
            "title": "Protocolo DHCP (Dynamic Host Configuration Protocol)",
            "tags": ["dhcp", "networking", "protocols", "lan"],
            "sources": ["raw/sources/bloque4-tema04.md"],
            "aliases": ["DHCP", "Dynamic Host Configuration Protocol"],
            "content": """# Protocolo DHCP (Dynamic Host Configuration Protocol)

**DHCP** es un protocolo cliente-servidor (UDP puertos 67 y 68) que automatiza la asignación dinámica de parámetros de red a dispositivos en una LAN.

## Proceso de Asignación DORA
1. **Discover** (Cliente ➔ Broadcast `255.255.255.255`): El cliente solicita configuración IP.
2. **Offer** (Servidor ➔ Unicast/Broadcast): El servidor ofrece una IP con tiempo de concesión (*lease time*).
3. **Request** (Cliente ➔ Broadcast): El cliente acepta formalmente la oferta elegida.
4. **Acknowledge** (Servidor ➔ Unicast/Broadcast): Confirmación final con máscara, puerta de enlace y servidores DNS.

## Parámetros Clave
- **Lease Time**: Tiempo de validez del alquiler IP antes de renovación (T1 al 50%, T2 al 87.5%).
- **DHCP Relay Agent**: Reenvía peticiones DHCP entre subredes a través de routers (Opción 82).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Nombres: [[wiki/entities/dns-protocol|Protocolo DNS]]
- Conmutación: [[wiki/concepts/routing-and-switching-mechanisms|Enrutamiento y Conmutación]]
"""
        },
        {
            "slug": "snmp-protocol.md",
            "title": "Protocolo SNMP (Simple Network Management Protocol)",
            "tags": ["snmp", "monitoring", "networking", "protocols"],
            "sources": ["raw/sources/bloque4-tema04.md"],
            "aliases": ["SNMP", "Network Management"],
            "content": """# Protocolo SNMP (Simple Network Management Protocol)

**SNMP** es el estándar de la capa de aplicación (UDP puertos 161 y 162) para la monitorización y administración remota de dispositivos de red.

## Arquitectura SNMP
- **NMS (Network Management Station)**: Estación central de monitorización.
- **Agente SNMP**: Proceso ejecutándose en el dispositivo administrado.
- **MIB (Management Information Base)**: Base de datos estructurada en árbol jerárquico de variables y métricas.
- **OID (Object Identifier)**: Identificador numérico único de cada variable en la MIB.

## Versiones de SNMP
- **SNMPv1 / SNMPv2c**: Autenticación simple mediante cadenas de comunidad en texto plano (Community Strings `public`/`private`). Inseguro.
- **SNMPv3**: Incorpora seguridad criptográfica con autenticación (HMAC-MD5/SHA) y cifrado de privacidad (DES, AES), además de control de acceso basado en usuarios (USM y VACM).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Monitorización CPD: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]
"""
        },
        {
            "slug": "siem-and-ids-ips.md",
            "title": "Sistemas SIEM, IDS e IPS de Ciberseguridad",
            "tags": ["security", "siem", "ids", "ips", "soc", "incident-management"],
            "sources": ["raw/sources/bloque4-tema05.md"],
            "aliases": ["SIEM", "IDS", "IPS", "SOC Tools"],
            "content": """# Sistemas SIEM, IDS e IPS de Ciberseguridad

Sistemas de detección, prevención y correlación de eventos de seguridad fundamentales en centros de operaciones de seguridad (SOC).

## Tecnologías Principales
- **IDS (Intrusion Detection System)**: Analiza tráfico pasivamente mediante copia en puerto SPAN/Mirroring y genera alertas ante patrones maliciosos conocidos (firmas) o anomalías de comportamiento.
- **IPS (Intrusion Prevention System)**: Dispositivo en línea (*in-line*) capaz de bloquear paquetes y cortar flujos de ataque en tiempo real (ej: Snort, Suricata).
- **SIEM (Security Information and Event Management)**: Agrega, normaliza y correlaciona registros (logs) procedentes de cortafuegos, servidores, routers y aplicaciones (ej: Splunk, Elastic SIEM, Wazuh, QRadar).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Perímetro: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]]
- Normativa: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]]
"""
        },
        {
            "slug": "wi-fi-and-mobile-standards.md",
            "title": "Estándares Inalámbricos Wi-Fi y Redes Móviles (4G/5G)",
            "tags": ["wifi", "mobile", "5g", "lte", "wireless", "communications"],
            "sources": ["raw/sources/bloque4-tema06.md"],
            "aliases": ["Wi-Fi", "802.11", "5G NR", "Redes Inalámbricas"],
            "content": """# Estándares Inalámbricos Wi-Fi y Redes Móviles (4G/5G)

Evolución de las tecnologías de comunicación por radiofrecuencia y acceso inalámbrico para entornos locales y metropolitanos.

## Evolución de Estándares Wi-Fi (IEEE 802.11)
- **802.11n (Wi-Fi 4)**: 2.4 / 5 GHz, MIMO, hasta 600 Mbps.
- **802.11ac (Wi-Fi 5)**: 5 GHz, MU-MIMO, modulación 256-QAM, hasta 6.9 Gbps.
- **802.11ax (Wi-Fi 6 / 6E)**: 2.4, 5 y 6 GHz, OFDMA, 1024-QAM, Target Wake Time (TWT).
- **802.11be (Wi-Fi 7)**: Anchos de canal de 320 MHz, 4096-QAM, Multi-Link Operation (MLO).

## Pilares de 5G New Radio (NR)
1. **eMBB (Enhanced Mobile Broadband)**: Velocidades pico superiores a 10 Gbps.
2. **URLLC (Ultra-Reliable Low Latency Communications)**: Latencias inferiores a 1 ms para vehículos autónomos e industria.
3. **mMTC (Massive Machine Type Communications)**: Densidad masiva de dispositivos IoT (1 millón de disp/km²).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Medios: [[wiki/concepts/transmission-media-and-modes|Medios y Modos de Transmisión]]
"""
        },
        {
            "slug": "ipv4-and-ipv6.md",
            "title": "Protocolos de Red: IPv4 e IPv6",
            "tags": ["ipv4", "ipv6", "networking", "ip-protocols", "addressing"],
            "sources": ["raw/sources/bloque4-tema07.md"],
            "aliases": ["IPv4", "IPv6", "Protocolo IP"],
            "content": """# Protocolos de Red: IPv4 e IPv6

El **Protocolo de Internet (IP)** es el protocolo principal de la capa de red del modelo TCP/IP encargado del direccionamiento no orientado a conexión y del enrutamiento de datagramas.

## IPv4 vs. IPv6
- **IPv4**: Direcciones de 32 bits (4 octetos decimales con punto), espacio de 4.300 millones de direcciones. Fragmentación realizada por routers y host emisor.
- **IPv6**: Direcciones de 128 bits (8 grupos hexadecimales), espacio prácticamente inagotable ($3.4 \\times 10^{38}$). Cabecera simplificada de tamaño fijo (40 bytes), fragmentación delegada exclusivamente al host emisor mediante cabeceras de extensión.

## Tipos de Direcciones IPv6
- **Unicast**: Global Unicast (`2000::/3`), Link-Local (`fe80::/10`), Unique Local (`fc00::/7`).
- **Multicast** (`ff00::/8`): Reemplaza a las difusiones broadcast de IPv4.
- **Anycast**: Identificador para un conjunto de interfaces donde el paquete se entrega a la más cercana.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Comparativa: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Detallada IPv4 vs IPv6]]
- Capas: [[wiki/concepts/osi-and-tcp-ip-models|Modelos OSI y TCP-IP]]
"""
        },
        {
            "slug": "tcp-and-udp.md",
            "title": "Protocolos de Transporte: TCP y UDP",
            "tags": ["tcp", "udp", "transport-layer", "networking", "protocols"],
            "sources": ["raw/sources/bloque4-tema07.md"],
            "aliases": ["TCP", "UDP", "Capa de Transporte"],
            "content": """# Protocolos de Transporte: TCP y UDP

Protocolos fundamentales de la capa de transporte que gestionan la comunicación extremo a extremo entre procesos.

## TCP (Transmission Control Protocol)
- **Orientado a conexión**: Establecimiento mediante *Three-Way Handshake* (SYN ➔ SYN-ACK ➔ ACK) y cierre (FIN ➔ ACK).
- **Garantías**: Entrega ordenada, control de flujo por ventana deslizante (*Sliding Window*), control de congestión (Tahoe, Reno, CUBIC) y retransmisión por temporizador de ACK (ARQ).

## UDP (User Datagram Protocol)
- **No orientado a conexión**: Cabecera ultra-ligera de 8 bytes (Source Port, Dest Port, Length, Checksum).
- **Uso**: Aplicaciones en tiempo real sensibles al retardo y streaming (DNS, DHCP, VoIP, HTTP/3 QUIC).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Modelos: [[wiki/concepts/osi-and-tcp-ip-models|Modelos OSI y TCP-IP]]
- Web: [[wiki/entities/bgp-and-ospf|Protocolos OSPF y BGP]]
"""
        },
        {
            "slug": "bgp-and-ospf.md",
            "title": "Protocolos de Enrutamiento Dinámico: OSPF y BGP",
            "tags": ["routing", "ospf", "bgp", "networking", "internet"],
            "sources": ["raw/sources/bloque4-tema08.md"],
            "aliases": ["OSPF", "BGP", "Dynamic Routing"],
            "content": """# Protocolos de Enrutamiento Dinámico: OSPF y BGP

Protocolos encargados de calcular las mejores rutas en topologías de red complejas mediante intercambio de información entre routers.

## OSPF (Open Shortest Path First)
- **Tipo**: IGP (Interior Gateway Protocol) de estado de enlace (*Link-State*).
- **Algoritmo**: Algoritmo de Dijkstra (SPF - Shortest Path First) con métrica de coste inversamente proporcional al ancho de banda.
- **Topología**: Organización jerárquica en Áreas centradas en el Área Troncal (Área 0 / Backbone Area).

## BGP (Border Gateway Protocol)
- **Tipo**: EGP (Exterior Gateway Protocol) de vector de caminos (*Path-Vector*).
- **Función**: Es el protocolo que interconecta los **Sistemas Autónomos (AS)** en el núcleo de Internet. Utiliza TCP puerto 179.
- **Toma de Decisiones**: Basada en atributos y políticas de enrutamiento (AS-Path, Local Preference, MED, Weight).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Arquitectura: [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
"""
        },
        {
            "slug": "tls-ssl-protocols.md",
            "title": "Protocolos Criptográficos TLS y SSL",
            "tags": ["tls", "ssl", "cryptography", "https", "security"],
            "sources": ["raw/sources/bloque4-tema08.md"],
            "aliases": ["TLS", "SSL", "TLS 1.3", "HTTPS Encryption"],
            "content": """# Protocolos Criptográficos TLS y SSL

**Transport Layer Security (TLS)** es el estándar criptográfico sucesor de SSL que provee confidencialidad, integridad y autenticación sobre canales de comunicación en redes IP.

## Principios Criptográficos
- **Criptografía Asimétrica (Clave Pública)**: RSA o Curvas Elípticas (ECDHE) para el intercambio seguro de claves y autenticación mediante certificados digitales X.509.
- **Criptografía Simétrica**: Cifrado masivo de datos mediante AES-GCM o ChaCha20-Poly1305.
- **Integridad**: Funciones hash seguras (SHA-256 / SHA-384).

## Avances en TLS 1.3 (RFC 8446)
- Reducción del apretón de manos (*Handshake*) a 1 solo RTT (y soporte de 0-RTT para reconexiones).
- Eliminación de algoritmos obsoletos e inseguros (DES, 3DES, RC4, MD5, SHA-1, suites CBC).
- Cifrado obligatorio de la mayoría de mensajes del handshake.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Perímetro: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]]
- Correo: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
"""
        },
        {
            "slug": "firewalls-and-vpn.md",
            "title": "Cortafuegos y Redes Privadas Virtuales (VPN)",
            "tags": ["firewalls", "vpn", "ipsec", "wireguard", "security", "network-security"],
            "sources": ["raw/sources/bloque4-tema09.md"],
            "aliases": ["Firewalls", "VPN", "IPsec", "Seguridad Perimetral"],
            "content": """# Cortafuegos y Redes Privadas Virtuales (VPN)

Tecnologías centrales para el aislamiento perimetral y la interconexión cifrada de sedes y usuarios remotos.

## Tipologías de Cortafuegos
1. **Filtrado de Paquetes Stateless**: Inspección básica de IPs, puertos y flags TCP en Capa 3/4.
2. **Stateful Inspection**: Mantiene una tabla de estado de conexiones para autorizar respuestas legítimas.
3. **Next-Generation Firewalls (NGFW)**: Inspección profunda de paquetes (DPI) en Capa 7, control de aplicaciones y prevención de amenazas integrada.
4. **WAF (Web Application Firewall)**: Protección especializada contra ataques web (OWASP Top 10: SQLi, XSS, CSRF).

## Tecnologías VPN
- **IPsec**: Protocolo en Capa 3 con modos Transporte y Túnel. Protocolos AH (autenticación e integridad) y ESP (cifrado y autenticación).
- **SSL/TLS VPN** (OpenVPN): Opera en Capa de Transporte/Aplicación.
- **WireGuard**: Protocolo VPN moderno, simple y de alto rendimiento en el kernel Linux.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Normativa: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
"""
        },
        {
            "slug": "ccn-cert-and-ens.md",
            "title": "CCN-CERT y Esquema Nacional de Seguridad (ENS)",
            "tags": ["ens", "ccn-cert", "ciberseguridad", "administracion-publica", "regulacion"],
            "sources": ["raw/sources/bloque4-tema09.md"],
            "aliases": ["ENS", "CCN-CERT", "Esquema Nacional de Seguridad", "Guías CCN-STIC"],
            "content": """# CCN-CERT y Esquema Nacional de Seguridad (ENS)

Marco normativo y organizativo de la ciberseguridad en el sector público español (Real Decreto 311/2022 regulador del ENS).

## El CCN-CERT
- Es la Capacidad de Respuesta a Incidentes de Seguridad del **Centro Criptológico Nacional (CCN)** adscrito al CNI.
- Responsable de la coordinación de ciberincidentes de origen estatal y administración pública.
- Emite las reconocidas **Guías CCN-STIC** con directrices de bastionado y configuración segura.

## Dimensiones de Seguridad del ENS
El ENS categoriza los sistemas en niveles **Básico, Medio o Alto** en función de 5 dimensiones:
1. **Disponibilidad (D)**
2. **Autenticidad (A)**
3. **Integridad (I)**
4. **Confidencialidad (C)**
5. **Trazabilidad (T)**

## Principios Básicos del ENS
- Seguridad integral, gestión de riesgos, prevención, detección, respuesta, vigilancia continua y reevaluación periódica.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Detección: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]
- Perímetro: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]]
"""
        },
        {
            "slug": "ethernet-and-ieee-standards.md",
            "title": "Estándares Ethernet y Familia IEEE 802.3",
            "tags": ["ethernet", "ieee-802-3", "lan", "networking", "cables"],
            "sources": ["raw/sources/bloque4-tema10.md"],
            "aliases": ["Ethernet", "IEEE 802.3", "Fast Ethernet", "Gigabit Ethernet"],
            "content": """# Estándares Ethernet y Familia IEEE 802.3

**Ethernet** es la tecnología dominante de red de área local cableada estandarizada en el grupo IEEE 802.3.

## Trama Ethernet II (802.3)
- **Preámbulo y SFD**: 8 bytes de sincronización.
- **Dirección MAC Destino / Origen**: 6 bytes cada una (OUI + serial fabricante).
- **EtherType / Longitud**: 2 bytes (ej: `0x0800` IPv4, `0x86DD` IPv6, `0x8100` VLAN 802.1Q).
- **Carga Útil (Payload)**: 46 a 1500 bytes (MTU estándar).
- **FCS (Frame Check Sequence)**: 4 bytes de verificación CRC-32.

## Método de Acceso CSMA/CD
- *Carrier Sense Multiple Access with Collision Detection*: Escuchar el medio antes de transmitir, detectar colisiones y aplicar retroceso exponencial aleatorio (*Exponential Backoff*). Obsoleto en redes conmutadas Full-Duplex modernas.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Métodos de Acceso]]
"""
        }
    ]

    for e in entities_data:
        out_path = WIKI_DIR / "entities" / e["slug"]
        sources_fm = "\n".join([f'  - "{src}"' for src in e["sources"]])
        tags_fm = "\n".join([f"  - {t}" for t in e["tags"]])
        aliases_fm = "\n".join([f'  - "{a}"' for a in e["aliases"]])
        
        full_content = f"""---
title: "{e['title']}"
type: "entity"
tags:
{tags_fm}
sources:
{sources_fm}
created: "{TODAY}"
updated: "{TODAY}"
aliases:
{aliases_fm}
---

{e['content']}
"""
        out_path.write_text(full_content, encoding="utf-8")
        print(f"    [OK] wiki/entities/{e['slug']}")

    # 2. CONCEPTS
    concepts_data = [
        {
            "slug": "operating-system-architecture.md",
            "title": "Arquitectura de Sistemas Operativos y Software de Base",
            "tags": ["operating-systems", "kernel", "os-architecture", "concepts"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["Arquitectura del SO", "Operating System Architecture"],
            "content": """# Arquitectura de Sistemas Operativos y Software de Base

El Sistema Operativo es la capa de software intermediaria entre el hardware físico y los programas de usuario, garantizando abstracción y asignación equitativa de recursos.

## Niveles Arquitectónicos
1. **Espacio del Kernel (Kernel Space)**: Ejecución en modo privilegiado (Ring 0), acceso directo a registros, memoria física e interrupciones.
2. **Espacio de Usuario (User Space)**: Aplicaciones ejecutándose en modo no privilegiado (Ring 3).
3. **Llamadas al Sistema (System Calls)**: Interfaz controlada que permite a las aplicaciones solicitar servicios al kernel (`read`, `write`, `fork`, `execve`).

## Tipos de Núcleo
- **Monolítico** (Linux): Todos los servicios del SO (gestión de memoria, red, IPC, drivers) residen en el mismo espacio de memoria privilegiado.
- **Microkernel** (Mach, QNX): Solo las funciones esenciales residen en el kernel; servidores en espacio de usuario se comunican mediante IPC.
- **Híbrido** (Windows NT, macOS XNU): Estructura monolítica con componentes modulares organizados por capas.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel y Software de Base]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
"""
        },
        {
            "slug": "process-and-memory-management.md",
            "title": "Gestión de Procesos, Hilos y Memoria Virtual",
            "tags": ["processes", "memory", "virtual-memory", "threads", "operating-systems"],
            "sources": ["raw/sources/bloque4-tema01.md"],
            "aliases": ["Gestión de Procesos y Memoria", "Process and Memory Management"],
            "content": """# Gestión de Procesos, Hilos y Memoria Virtual

Mecanismos de control y aislamiento que permiten la multiprogramación concurrente y segura en sistemas operativos modernos.

## Planificación de Procesos
- **Estados de Proceso**: Nuevo, Listo (Ready), Ejecutando (Running), Bloqueado (Waiting), Terminado (Zombie).
- **Algoritmos de Planificación**: Round Robin (RR), Shortest Job First (SJF), Colas Multinivel con Retroalimentación (MLFQ), Completely Fair Scheduler (CFS).
- **Concurrencia y Sincronización**: Semáforos, Mutex, Monitores, problemas clásicos (Sección Crítica, Bloqueo Mutuo / *Deadlock* - Condiciones de Coffman).

## Memoria Virtual
- **Paginación**: División de memoria en marcos físicos (*frames*) y páginas lógicas (*pages*), gestionadas mediante tablas de páginas y la MMU (*Memory Management Unit*).
- **Fallo de Página (Page Fault)**: Interrupción generada cuando una página requerida no reside en RAM física y debe cargarse desde el espacio de intercambio (*swap*).
- **Algoritmos de Reemplazo**: LRU (Least Recently Used), FIFO, Segunda Oportunidad (Reloj).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Arquitectura: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
"""
        },
        {
            "slug": "database-normalization-and-acid.md",
            "title": "Normalización de Bases de Datos y Principios ACID",
            "tags": ["databases", "acid", "normalization", "sql", "transactions"],
            "sources": ["raw/sources/bloque4-tema02.md"],
            "aliases": ["ACID", "Normalización", "Transacciones SQL"],
            "content": """# Normalización de Bases de Datos y Principios ACID

Fundamentos de diseño y consistencia en sistemas gestores de bases de datos relacionales.

## Formas Normales (Normalización)
- **1FN**: Todos los atributos contienen valores atómicos y no existen grupos repetitivos.
- **2FN**: Está en 1FN y todos los atributos no clave tienen dependencia funcional completa de la clave primaria.
- **3FN**: Está en 2FN y no existen dependencias funcionales transitivas entre atributos no clave.
- **FNBC (Boyce-Codd)**: Refinamiento estricto donde todo determinante es superclave.

## Principios ACID de las Transacciones
1. **Atomicidad (Atomicity)**: La transacción se ejecuta completamente o no se ejecuta en absoluto (*Commit* o *Rollback*).
2. **Consistencia (Consistency)**: La base de datos pasa de un estado válido a otro cumpliendo todas las restricciones de integridad.
3. **Aislamiento (Isolation)**: Las transacciones concurrentes se ejecutan sin interferencias mutuas (niveles: Read Uncommitted, Read Committed, Repeatable Read, Serializable).
4. **Durabilidad (Durability)**: Una vez confirmada la transacción, sus efectos persisten ante fallos del sistema (Write-Ahead Logging / WAL).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
"""
        },
        {
            "slug": "virtualization-and-cloud-computing.md",
            "title": "Virtualización y Computación en la Nube (Cloud Computing)",
            "tags": ["virtualization", "cloud", "iaas", "paas", "saas", "hypervisors"],
            "sources": ["raw/sources/bloque4-tema02.md"],
            "aliases": ["Virtualización", "Cloud Computing", "IaaS PaaS SaaS"],
            "content": """# Virtualización y Computación en la Nube (Cloud Computing)

Tecnologías de abstracción de hardware y provisión elástica de servicios bajo demanda según el estándar NIST SP 800-145.

## Tipologías de Hipervisores
- **Hipervisores Tipo 1 (Bare-Metal)**: Se ejecutan directamente sobre el hardware físico (ej: VMware ESXi, KVM, Microsoft Hyper-V, Xen). Máximo rendimiento y uso en CPD.
- **Hipervisores Tipo 2 (Hosted)**: Se ejecutan como una aplicación sobre un sistema operativo anfitrión (ej: VMware Workstation, VirtualBox).

## Modelos de Servicio Cloud
- **IaaS (Infrastructure as a Service)**: Provisión de cómputo, almacenamiento y redes virtuales (ej: AWS EC2, Azure VMs).
- **PaaS (Platform as a Service)**: Entorno de ejecución y base de datos sin gestión de infraestructura subyacente (ej: AWS Elastic Beanstalk, Heroku, Azure App Services).
- **SaaS (Software as a Service)**: Aplicaciones completas listas para el usuario final (ej: Microsoft 365, Google Workspace).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Comparativa: [[wiki/synthesis/virtualization-vs-containerization-comparison|Virtualización vs Contenedores]]
- Contenedores: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
"""
        },
        {
            "slug": "microservices-and-middleware.md",
            "title": "Arquitecturas de Microservicios y Middleware",
            "tags": ["microservices", "middleware", "api", "software-architecture"],
            "sources": ["raw/sources/bloque4-tema03.md"],
            "aliases": ["Microservicios", "Middleware", "Message Brokers"],
            "content": """# Arquitecturas de Microservicios y Middleware

Estrategias de descomposición de sistemas monolíticos en servicios independientes, desacoplados y comunicados a través de redes.

## Patrones de Microservicios
- **API Gateway**: Punto de entrada único que gestiona enrutamiento, autenticación, rate limiting y balanceo hacia los microservicios internos.
- **Comunicación Asíncrona (Message Brokers)**: Desacoplamiento temporal mediante colas y tópicos pub/sub (ej: RabbitMQ, Apache Kafka).
- **Service Mesh**: Capa de infraestructura dedicada para gestionar la comunicación servicio a servicio, observabilidad y mTLS (ej: Istio, Linkerd).

## Capa Middleware
Software que conecta componentes dispares (servidores de aplicaciones web como Apache Tomcat, Nginx, WildFly, brokers de mensajería y drivers de integración).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Orquestación: [[wiki/entities/kubernetes|Kubernetes y Orquestación]]
"""
        },
        {
            "slug": "routing-and-switching-mechanisms.md",
            "title": "Mecanismos de Conmutación (Switching) y Enrutamiento LAN",
            "tags": ["switching", "routing", "vlan", "stp", "lan", "networking"],
            "sources": ["raw/sources/bloque4-tema04.md"],
            "aliases": ["Switching", "Conmutación LAN", "VLAN y STP"],
            "content": """# Mecanismos de Conmutación (Switching) y Enrutamiento LAN

Tecnologías de reenvío de tramas en Capa 2 y paquetes en Capa 3 en redes de área local.

## Conmutación en Capa 2
- **Tabla CAM (Content Addressable Memory)**: Asocia direcciones MAC con puertos físicos mediante aprendizaje dinámico (*MAC Learning*).
- **VLANs (IEEE 802.1Q)**: Segmentación lógica de dominios de broadcast. Inserción de cabecera de 4 bytes con VLAN ID (1-4094).
- **STP / RSTP (IEEE 802.1D / 802.1w)**: Algoritmo de árbol de expansión que bloquea enlaces redundantes para evitar tormentas de broadcast causadas por bucles.

## Enrutamiento Inter-VLAN
- **Router-on-a-Stick**: Un router conectado al switch mediante un único enlace troncal con subinterfaces lógicas 802.1Q.
- **Switches Multicapa (Capa 3)**: Reenvío a velocidad de cable mediante interfaces virtuales de switch (SVI) y hardware ASIC especializado.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Protocolos LAN: [[wiki/entities/dhcp-protocol|Protocolo DHCP]] y [[wiki/entities/dns-protocol|Protocolo DNS]]
"""
        },
        {
            "slug": "datacenter-infrastructure-and-disaster-recovery.md",
            "title": "Infraestructura de CPD y Recuperación ante Desastres",
            "tags": ["datacenter", "cpd", "disaster-recovery", "bcp", "drp", "raid"],
            "sources": ["raw/sources/bloque4-tema05.md"],
            "aliases": ["Infraestructura CPD", "Disaster Recovery", "Alta Disponibilidad"],
            "content": """# Infraestructura de CPD y Recuperación ante Desastres

Diseño de Centros de Proceso de Datos (CPD), continuidad de negocio y arquitecturas de almacenamiento de alta disponibilidad.

## Clasificación TIER (Uptime Institute)
- **TIER I (Básico)**: 99.671% disponibilidad (~28.8h caída/año). Sin componentes redundantes.
- **TIER II (Redundancia Parcial)**: 99.741% disponibilidad. Componentes redundantes N+1.
- **TIER III (Mantenimiento Concurrente)**: 99.982% disponibilidad (~1.6h caída/año). Rutas de distribución redundantes, equipos mantenibles sin interrumpir servicio.
- **TIER IV (Tolerante a Fallos)**: 99.995% disponibilidad (~26 min caída/año). Sistemas 2(N+1) con tolerancia total a cualquier fallo simple.

## Métricas de Continuidad
- **RTO (Recovery Time Objective)**: Tiempo máximo admisible para restaurar los servicios tras un incidente.
- **RPO (Recovery Point Objective)**: Volumen máximo de pérdida de datos admisible medido en tiempo.

## Arquitecturas RAID
- **RAID 0**: Fraccionamiento (*striping*) sin redundancia.
- **RAID 1**: Espejo (*mirroring*).
- **RAID 5**: Fraccionamiento con paridad distribuida (requiere $\\ge 3$ discos, tolera 1 fallo).
- **RAID 6**: Doble paridad distribuida (requiere $\\ge 4$ discos, tolera 2 fallos simultáneos).
- **RAID 10**: Combinación de espejo y fraccionamiento (RAID 1+0).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Seguridad: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]
"""
        },
        {
            "slug": "transmission-media-and-modes.md",
            "title": "Medios y Modos de Transmisión de Comunicaciones",
            "tags": ["transmission-media", "cables", "fiber-optic", "wireless", "communications"],
            "sources": ["raw/sources/bloque4-tema06.md"],
            "aliases": ["Medios de Transmisión", "Fibra Óptica y Cobre"],
            "content": """# Medios y Modos de Transmisión de Comunicaciones

Fundamentos físicos de la transmisión guiada y no guiada de información.

## Modos de Transmisión
- **Simplex**: Transmisión unidireccional permanente (ej: radiodifusión).
- **Half-Duplex**: Transmisión bidireccional no simultánea (ej: walkie-talkie, CSMA/CD).
- **Full-Duplex**: Transmisión bidireccional simultánea sobre canales independientes (ej: telefonía, Ethernet conmutado).

## Medios Guiados
- **Par Trenzado (UTP, FTP, STP)**: Categorías Cat 5e (100 MHz, 1 Gbps), Cat 6 (250 MHz, 1/10 Gbps en distancias cortas), Cat 6A (500 MHz, 10 Gbps a 100 m).
- **Fibra Óptica**:
  - *Monomodo (SMF)*: Núcleo fino ($\\sim 9\\,\\mu\\text{m}$), luz láser, alcance de decenas de kilómetros sin repetidores.
  - *Multimodo (MMF)*: Núcleo mayor ($50$ o $62.5\\,\\mu\\text{m}$), luz LED/VCSEL, alcance corto (hasta 550 m en OM4 a 10 Gbps).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Inalámbrico: [[wiki/entities/wi-fi-and-mobile-standards|Estándares Wi-Fi y 5G]]
"""
        },
        {
            "slug": "osi-and-tcp-ip-models.md",
            "title": "Modelos Arquitectónicos ISO-OSI y TCP-IP",
            "tags": ["osi-model", "tcp-ip", "networking-models", "encapsulation"],
            "sources": ["raw/sources/bloque4-tema07.md"],
            "aliases": ["Modelo OSI", "Modelo TCP-IP", "Capas de Red"],
            "content": """# Modelos Arquitectónicos ISO-OSI y TCP-IP

Estructuras de referencia estratificadas para la estandarización de las comunicaciones entre sistemas heterogéneos.

## Comparativa de Capas
| Capa OSI (7 Niveles) | Capa TCP/IP (4 Niveles) | PDU (Protocol Data Unit) | Protocolos Representativos |
| :--- | :--- | :--- | :--- |
| **7. Aplicación** | **Aplicación** | Datos | HTTP, DNS, SMTP, SSH, FTP |
| **6. Presentación** | **Aplicación** | Datos | TLS/SSL, ASCII, JPEG, JSON |
| **5. Sesión** | **Aplicación** | Datos | RPC, NetBIOS, Sockets |
| **4. Transporte** | **Transporte** | Segmento (TCP) / Datagrama (UDP) | [[wiki/entities/tcp-and-udp\|TCP, UDP]] |
| **3. Red** | **Internet** | Paquete / Datagrama IP | [[wiki/entities/ipv4-and-ipv6\|IPv4, IPv6]], ICMP, [[wiki/entities/bgp-and-ospf\|OSPF, BGP]] |
| **2. Enlace de Datos**| **Acceso a Red** | Trama (*Frame*) | [[wiki/entities/ethernet-and-ieee-standards\|Ethernet (802.3)]], Wi-Fi (802.11), PPP |
| **1. Física** | **Acceso a Red** | Bits | Cables UTP, Fibra Óptica, Radio |

## Concepto de Encapsulación
A medida que los datos descienden por las capas del emisor, cada nivel añade su propia cabecera (*Header*) y pie (*Trailer*), convirtiéndose en la PDU del nivel inferior.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Síntesis: [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa Detallada OSI vs TCP-IP]]
- Protocolos IP: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]
"""
        },
        {
            "slug": "internet-architecture-and-web-protocols.md",
            "title": "Arquitectura de Internet y Protocolos Web (HTTP/1-3)",
            "tags": ["internet", "web", "http", "http2", "http3", "quic"],
            "sources": ["raw/sources/bloque4-tema08.md"],
            "aliases": ["Arquitectura de Internet", "Protocolos Web", "HTTP Evolution"],
            "content": """# Arquitectura de Internet y Protocolos Web (HTTP/1-3)

Evolución de la topología interconectada global y los protocolos de entrega de aplicaciones web.

## Topología de Internet
- **ISP Tier 1**: Operadores de tránsito global interconectados libremente entre sí mediante acuerdos de *Peering*.
- **Puntos Neutros (IXP - Internet Exchange Points)**: Infraestructuras físicas donde múltiples ISPs y CDNs intercambian tráfico localmente.

## Evolución de HTTP
- **HTTP/1.1**: Protocolo de texto plano, cabeceras redundantes, bloqueo en cabeza de línea a nivel de aplicación (*Head-of-Line Blocking*).
- **HTTP/2**: Enmarcado binario, multiplexación completa de peticiones sobre una única conexión TCP, compresión de cabeceras HPACK, Server Push.
- **HTTP/3**: Reemplaza TCP por **QUIC** (basado en UDP) con TLS 1.3 integrado, eliminando el bloqueo en cabeza de línea a nivel de transporte ante pérdida de paquetes.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Seguridad Web: [[wiki/entities/tls-ssl-protocols|Protocolos Criptográficos TLS y SSL]]
- Enrutamiento: [[wiki/entities/bgp-and-ospf|Protocolos OSPF y BGP]]
"""
        },
        {
            "slug": "network-security-and-perimeter-defense.md",
            "title": "Seguridad en Redes y Defensa Perimetral",
            "tags": ["network-security", "perimeter-defense", "dmz", "defense-in-depth"],
            "sources": ["raw/sources/bloque4-tema09.md"],
            "aliases": ["Seguridad en Redes", "Defensa Perimetral"],
            "content": """# Seguridad en Redes y Defensa Perimetral

Estrategias de protección y contención de amenazas para infraestructuras de comunicaciones corporativas.

## Principios de Defensa en Profundidad
1. **Perímetro Exterior**: Cortafuegos de borde, protección anti-DDoS, enrutamiento seguro.
2. **Zona Desmilitarizada (DMZ)**: Subred aislada que aloja servicios accesibles públicamente (Web, Correo, DNS externo) sin acceso directo a la red interna.
3. **Red Interna (LAN Segura)**: Segmentación por VLANs, autenticación de puertos (802.1X), inspección de tráfico interno con IDS/IPS.
4. **Endpoint**: Antivirus/EDR, bastionado de sistemas operativos según guías CCN-STIC.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Dispositivos: [[wiki/entities/firewalls-and-vpn|Cortafuegos y VPN]]
- Marco Público: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]]
"""
        },
        {
            "slug": "lan-topologies-and-mac-protocols.md",
            "title": "Topologías LAN y Métodos de Control de Acceso al Medio (MAC)",
            "tags": ["lan-topologies", "mac", "csma-cd", "csma-ca", "ethernet"],
            "sources": ["raw/sources/bloque4-tema10.md"],
            "aliases": ["Topologías LAN", "Métodos de Acceso MAC"],
            "content": """# Topologías LAN y Métodos de Control de Acceso al Medio (MAC)

Organización geométrica de nodos y protocolos de compartición de canales de difusión en redes de área local.

## Topologías de Red
- **Estrella**: Todos los nodos se conectan a un dispositivo central (switch/concentrador). Tolera fallos en cables individuales.
- **Árbol (Jerárquica)**: Estructura de niveles (Acceso, Distribución, Núcleo) estándar en redes corporativas.
- **Malla Completa / Parcial**: Múltiples rutas redundantes entre nodos. Utilizada en centros de datos y backbones de telecomunicaciones.

## Métodos de Acceso al Medio
- **CSMA/CD (Acceso Múltiple por Detección de Portadora con Detección de Colisiones)**: Utilizado en redes cableadas Ethernet compartidas.
- **CSMA/CA (con Prevención de Colisiones)**: Utilizado en redes inalámbricas Wi-Fi (802.11) mediante tramas RTS/CTS (*Request to Send / Clear to Send*).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Estándar: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet e IEEE 802.3]]
"""
        }
    ]

    for c in concepts_data:
        out_path = WIKI_DIR / "concepts" / c["slug"]
        sources_fm = "\n".join([f'  - "{src}"' for src in c["sources"]])
        tags_fm = "\n".join([f"  - {t}" for t in c["tags"]])
        aliases_fm = "\n".join([f'  - "{a}"' for a in c["aliases"]])
        
        full_content = f"""---
title: "{c['title']}"
type: "concept"
tags:
{tags_fm}
sources:
{sources_fm}
created: "{TODAY}"
updated: "{TODAY}"
aliases:
{aliases_fm}
---

{c['content']}
"""
        out_path.write_text(full_content, encoding="utf-8")
        print(f"    [OK] wiki/concepts/{c['slug']}")

def write_syntheses():
    print("\n[*] Generating high-level synthesis documents in wiki/synthesis/...")
    
    syntheses_data = [
        {
            "slug": "bloque4-tai-oposiciones-master-guide.md",
            "title": "Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)",
            "tags": ["synthesis", "master-guide", "bloque-4", "oposiciones", "tai"],
            "sources": ["raw/sources/bloque4-tema01.md", "raw/sources/bloque4-tema02.md", "raw/sources/bloque4-tema03.md", "raw/sources/bloque4-tema04.md", "raw/sources/bloque4-tema05.md", "raw/sources/bloque4-tema06.md", "raw/sources/bloque4-tema07.md", "raw/sources/bloque4-tema08.md", "raw/sources/bloque4-tema09.md", "raw/sources/bloque4-tema10.md"],
            "aliases": ["Guía Maestra Bloque 4", "Bloque 4 TAI Resumen General"],
            "content": """# Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)

Visión general y mapa estructurado de los 10 temas de Sistemas y Comunicaciones para la preparación de oposiciones del Cuerpo de Técnicos Auxiliares de Informática (TAI) de la Administración General del Estado.

---

## 🗺️ Mapa de Temas y Enlaces Directos

| Tema | Área Temática | Resumen Fuente | Entidades & Conceptos Clave |
| :--- | :--- | :--- | :--- |
| **Tema 01** | Sistemas Operativos & Software de Base | [[wiki/sources/bloque4-tema01\|Resumen Tema 01]] | [[wiki/entities/linux-kernel\|Linux Kernel]], [[wiki/entities/windows-server\|Windows Server]], [[wiki/concepts/operating-system-architecture\|Arquitectura SO]] |
| **Tema 02** | BBDD, Virtualización & Cloud | [[wiki/sources/bloque4-tema02\|Resumen Tema 02]] | [[wiki/entities/relational-databases-rdbms\|RDBMS]], [[wiki/entities/nosql-databases\|NoSQL]], [[wiki/concepts/virtualization-and-cloud-computing\|Virtualización/Cloud]] |
| **Tema 03** | Correo, Contenedores & Middleware | [[wiki/sources/bloque4-tema03\|Resumen Tema 03]] | [[wiki/entities/docker-and-containers\|Docker]], [[wiki/entities/kubernetes\|Kubernetes]], [[wiki/entities/smtp-imap-pop3\|SMTP/IMAP]] |
| **Tema 04** | Administración de Redes LAN | [[wiki/sources/bloque4-tema04\|Resumen Tema 04]] | [[wiki/entities/dns-protocol\|DNS]], [[wiki/entities/dhcp-protocol\|DHCP]], [[wiki/entities/snmp-protocol\|SNMP]], [[wiki/concepts/routing-and-switching-mechanisms\|Switching/VLAN]] |
| **Tema 05** | Seguridad, CPD & Incidentes | [[wiki/sources/bloque4-tema05\|Resumen Tema 05]] | [[wiki/entities/siem-and-ids-ips\|SIEM/IDS]], [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery\|Infraestructura CPD/RAID]] |
| **Tema 06** | Medios, Comunicaciones & Móvil | [[wiki/sources/bloque4-tema06\|Resumen Tema 06]] | [[wiki/entities/wi-fi-and-mobile-standards\|Wi-Fi/5G]], [[wiki/concepts/transmission-media-and-modes\|Medios de Transmisión]] |
| **Tema 07** | Modelos OSI / TCP-IP, IPv4 & IPv6 | [[wiki/sources/bloque4-tema07\|Resumen Tema 07]] | [[wiki/concepts/osi-and-tcp-ip-models\|Modelos OSI/TCP-IP]], [[wiki/entities/ipv4-and-ipv6\|IPv4/IPv6]], [[wiki/entities/tcp-and-udp\|TCP/UDP]] |
| **Tema 08** | Internet, HTTP, TLS & OSPF | [[wiki/sources/bloque4-tema08\|Resumen Tema 08]] | [[wiki/entities/bgp-and-ospf\|OSPF/BGP]], [[wiki/entities/tls-ssl-protocols\|TLS/SSL]], [[wiki/concepts/internet-architecture-and-web-protocols\|HTTP/1-3]] |
| **Tema 09** | Ciberseguridad, CCN & VPN | [[wiki/sources/bloque4-tema09\|Resumen Tema 09]] | [[wiki/entities/ccn-cert-and-ens\|CCN-CERT / ENS]], [[wiki/entities/firewalls-and-vpn\|Cortafuegos/VPN]] |
| **Tema 10** | Topologías LAN & Acceso al Medio | [[wiki/sources/bloque4-tema10\|Resumen Tema 10]] | [[wiki/entities/ethernet-and-ieee-standards\|Ethernet 802.3]], [[wiki/concepts/lan-topologies-and-mac-protocols\|Topologías LAN]] |

---

## 📊 Comparativas y Guías Específicas
- [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo OSI vs Modelo TCP-IP]]
- [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa: Direccionamiento IPv4 vs IPv6]]
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
"""
        },
        {
            "slug": "osi-vs-tcpip-model-comparison.md",
            "title": "Comparativa de Arquitecturas: Modelo ISO-OSI vs TCP-IP",
            "tags": ["synthesis", "comparison", "osi", "tcp-ip", "networking"],
            "sources": ["raw/sources/bloque4-tema07.md"],
            "aliases": ["OSI vs TCP-IP", "Comparativa Modelos de Red"],
            "content": """# Comparativa de Arquitecturas: Modelo ISO-OSI vs TCP-IP

Análisis comparativo de los dos modelos de referencia más importantes en ingeniería de redes para oposiciones de informática.

## Tabla Comparativa

| Dimensión | [[wiki/concepts/osi-and-tcp-ip-models\\|Modelo ISO-OSI]] | [[wiki/concepts/osi-and-tcp-ip-models\\|Modelo TCP-IP]] |
| :--- | :--- | :--- |
| **Desarrollo** | Teórico / Académico (ISO / ITU-T) | Práctico / Operativo (DARPA / IETF) |
| **Número de Capas** | 7 Capas | 4 Capas |
| **Capa Aplicación** | Descompuesta en Aplicación (7), Presentación (6) y Sesión (5) | Una única capa de Aplicación integrando formateo y sesión |
| **Capa de Red** | Soporta servicios orientados y no orientados a conexión | Solo servicio de datagramas no orientado a conexión (IP) |
| **Capa de Transporte** | Solo orientada a conexión | Orientada a conexión (TCP) y No orientada (UDP) |
| **Adopción Real** | Modelo de referencia conceptual | Estándar universal de Internet |

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Protocolos: [[wiki/entities/ipv4-and-ipv6|IPv4 e IPv6]], [[wiki/entities/tcp-and-udp|TCP y UDP]]
"""
        },
        {
            "slug": "ipv4-vs-ipv6-comparison.md",
            "title": "Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6",
            "tags": ["synthesis", "comparison", "ipv4", "ipv6", "networking"],
            "sources": ["raw/sources/bloque4-tema07.md"],
            "aliases": ["IPv4 vs IPv6", "Comparativa IP"],
            "content": """# Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6

Matriz comparativa de características técnicas entre el protocolo IPv4 tradicional y la siguiente generación IPv6.

## Matriz Técnica

| Característica | [[wiki/entities/ipv4-and-ipv6\\|IPv4]] | [[wiki/entities/ipv4-and-ipv6\\|IPv6]] |
| :--- | :--- | :--- |
| **Longitud de Dirección** | 32 bits (4 bytes) | 128 bits (16 bytes) |
| **Espacio de Direcciones** | $\\sim 4.29 \\times 10^9$ | $\\sim 3.4 \\times 10^{38}$ |
| **Formato de Notación** | Decimal con puntos (ej: `192.168.1.1`) | Hexadecimal con dos puntos (ej: `2001:db8::1`) |
| **Tamaño Cabecera Base** | Variable (20 a 60 bytes con opciones) | Fijo (40 bytes), opciones en cabeceras de extensión |
| **Checksum en Cabecera** | Sí (recalculado en cada salto de router) | No (eliminado para acelerar el reenvío) |
| **Fragmentación** | Realizada por el host origen y routers intermedios | Realizada **únicamente por el host emisor** |
| **Difusión (Broadcast)** | Soportado extensivamente mediante direcciones broadcast | **No existe broadcast**, reemplazado por Multicast |
| **Configuración Automática**| DHCPv4 o manual | SLAAC (Stateless Address Autoconfiguration) o DHCPv6 |

## Mecanismos de Transición
- **Dual-Stack**: Las interfaces de red operan pilas IPv4 e IPv6 simultáneamente.
- **Túneles (Tunneling)**: Encapsulación de paquetes IPv6 dentro de datagramas IPv4 (6to4, Teredo, ISATAP).
- **Traducción**: NAT64 / DNS64 para permitir a clientes IPv6 conectarse a servidores solo IPv4.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos IPv4 e IPv6]]
"""
        },
        {
            "slug": "virtualization-vs-containerization-comparison.md",
            "title": "Comparativa de Arquitecturas: Máquinas Virtuales vs Contenedores",
            "tags": ["synthesis", "comparison", "virtualization", "containers", "docker"],
            "sources": ["raw/sources/bloque4-tema02.md", "raw/sources/bloque4-tema03.md"],
            "aliases": ["VMs vs Contenedores", "Virtualización vs Contenedores"],
            "content": """# Comparativa de Arquitecturas: Máquinas Virtuales vs Contenedores

Evaluación de trade-offs entre aislamiento a nivel de hardware (Virtualización tradicional) y aislamiento a nivel de sistema operativo (Contenedores).

## Matriz de Arquitectura

| Parámetro | [[wiki/concepts/virtualization-and-cloud-computing\\|Máquinas Virtuales (VMs)]] | [[wiki/entities/docker-and-containers\\|Contenedores (Docker)]] |
| :--- | :--- | :--- |
| **Capa de Aislamiento** | Aislamiento completo de hardware mediante hipervisor | Aislamiento de procesos mediante namespaces y cgroups en el kernel anfitrión |
| **Sistema Operativo Invitado** | Cada VM ejecuta su propio SO completo (Guest OS) | Comparten el mismo kernel del SO anfitrión |
| **Tiempo de Arranque** | Minutos / decenas de segundos | Milisegundos / pocos segundos |
| **Consumo de Recursos** | Alto (requiere asignar RAM, vCPU y almacenamiento dedicado) | Mínimo (comparte memoria y binarios base con Copy-on-Write) |
| **Rendimiento I/O** | Ligera penalización por emulación/paravirtualización | Rendimiento cercano al nativo (*Near-Bare-Metal*) |
| **Orquestación Típica** | VMware vSphere, OpenStack, Proxmox | [[wiki/entities/kubernetes\|Kubernetes (K8s)]], Docker Swarm |

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]] y [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidades: [[wiki/entities/docker-and-containers|Docker]], [[wiki/entities/kubernetes|Kubernetes]]
"""
        }
    ]

    for s in syntheses_data:
        out_path = WIKI_DIR / "synthesis" / s["slug"]
        sources_fm = "\n".join([f'  - "{src}"' for src in s["sources"]])
        tags_fm = "\n".join([f"  - {t}" for t in s["tags"]])
        aliases_fm = "\n".join([f'  - "{a}"' for a in s["aliases"]])
        
        full_content = f"""---
title: "{s['title']}"
type: "synthesis"
tags:
{tags_fm}
sources:
{sources_fm}
created: "{TODAY}"
updated: "{TODAY}"
aliases:
{aliases_fm}
---

{s['content']}
"""
        out_path.write_text(full_content, encoding="utf-8")
        print(f"    [OK] wiki/synthesis/{s['slug']}")

def rebuild_index():
    print("\n[*] Rebuilding master index.md...")
    
    # Read all files in wiki/ and build categorized lists
    syntheses = sorted((WIKI_DIR / "synthesis").glob("*.md"))
    concepts = sorted((WIKI_DIR / "concepts").glob("*.md"))
    entities = sorted((WIKI_DIR / "entities").glob("*.md"))
    sources = sorted((WIKI_DIR / "sources").glob("*.md"))
    tutorials = sorted((ROOT_DIR / "tutorials").glob("*.md"))
    
    def get_title(md_path):
        content = md_path.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.startswith("title:"):
                return line.replace("title:", "").strip().strip('"').strip("'")
            if line.startswith("# "):
                return line.replace("# ", "").strip()
        return md_path.stem

    index_text = """# Master Index - LLM Wiki

Welcome to the Master Index of the LLM Wiki. This catalog indexes all knowledge pages organized by category with concise descriptions and metadata.

---

## 📚 Synthesis & Topics
*High-level overviews, comparison matrices, and consolidated domain guides.*

- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]] — Mapa de los 10 temas oficiales de redes, sistemas y ciberseguridad.
- [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI vs TCP-IP]] — Matriz comparativa de capas, PDUs y principios de diseño de redes.
- [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa: Direccionamiento IPv4 vs IPv6]] — Diferencias de longitud de dirección, cabeceras, broadcast y mecanismos de transición.
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]] — Evaluación de arquitecturas hipervisor vs contenedores Docker/K8s.
- [[wiki/synthesis/llm-wiki-vs-rag-comparison|Comparativa: LLM Wiki vs Retrieval-Augmented Generation (RAG)]] — Matriz de trade-offs entre sistemas RAG y wikis persistentes de conocimiento.

---

## 🧠 Concepts
*Theoretical concepts, architectural models, and foundational principles.*

- [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos y Software de Base]] — Kernel monolítico vs microkernel, espacio de usuario y llamadas al sistema.
- [[wiki/concepts/process-and-memory-management|Gestión de Procesos, Hilos y Memoria Virtual]] — Planificación CFS, paginación, memoria virtual, swap y sincronización.
- [[wiki/concepts/database-normalization-and-acid|Normalización de Bases de Datos y Principios ACID]] — Formas normales 1FN a FNBC y propiedades ACID transaccionales.
- [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Computación en la Nube (Cloud Computing)]] — Hipervisores Tipo 1/2 y modelos IaaS, PaaS, SaaS.
- [[wiki/concepts/microservices-and-middleware|Arquitecturas de Microservicios y Middleware]] — Desacoplamiento, API Gateways, Message Brokers y capas intermedias.
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación (Switching) y Enrutamiento LAN]] — Tablas CAM, VLANs 802.1Q, STP/RSTP y enrutamiento inter-VLAN.
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación ante Desastres]] — Clasificación TIER I-IV, métricas RTO/RPO y niveles RAID.
- [[wiki/concepts/transmission-media-and-modes|Medios y Modos de Transmisión de Comunicaciones]] — Par trenzado, fibra óptica monomodo/multimodo y modos simplex/duplex.
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]] — Estudio de las 7 capas OSI y las 4 capas de la arquitectura TCP/IP.
- [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web (HTTP/1-3)]] — Jerarquía de ISPs, evolución HTTP/1.1, HTTP/2 y HTTP/3 QUIC.
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]] — Defensa en profundidad, zonas DMZ y control de acceso.
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Métodos de Control de Acceso al Medio (MAC)]] — Topologías en estrella/árbol y contienda CSMA/CD y CSMA/CA.
- [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki Pattern]] — Principios de bases de conocimiento compounding mantenidas por agentes LLM.
- [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation (RAG)]] — Mecánica y limitaciones del modelo RAG sin persistencia.

---

## ⚙️ Entities & Tools
*Specific systems, libraries, protocols, standards, and tools.*

- [[wiki/entities/linux-kernel|Linux Kernel y Software de Base]] — Núcleo Linux, VFS, módulos y systemd.
- [[wiki/entities/windows-server|Windows Server y Administración de Dominios]] — Active Directory DS, GPOs, DNS/DHCP y NTFS.
- [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting en Entornos UNIX/Linux]] — Pipelines, redirecciones, filtros y scripts de automatización.
- [[wiki/entities/powershell|PowerShell y Automatización de Administración]] — Cmdlets, arquitectura basada en objetos .NET y remoting.
- [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS) y SQL]] — Motores PostgreSQL, Oracle, MySQL y estándares SQL.
- [[wiki/entities/nosql-databases|Bases de Datos NoSQL y Almacenamiento Distribuido]] — Modelos documentales, clave-valor, columnares, grafos y teorema CAP.
- [[wiki/entities/docker-and-containers|Docker y Tecnologías de Contenedores]] — Namespaces, cgroups, imágenes y Dockerfile.
- [[wiki/entities/kubernetes|Kubernetes y Orquestación de Contenedores]] — Pods, Deployments, Services, Ingress y plano de control K8s.
- [[wiki/entities/smtp-imap-pop3|Protocolos de Correo Electrónico: SMTP, IMAP y POP3]] — Transporte de correo, puertos seguros, SPF, DKIM y DMARC.
- [[wiki/entities/dns-protocol|Protocolo DNS (Domain Name System)]] — Resolución jerárquica, tipos de registros A/AAAA/MX/TXT y DNSSEC.
- [[wiki/entities/dhcp-protocol|Protocolo DHCP (Dynamic Host Configuration Protocol)]] — Proceso DORA, lease times y DHCP relay.
- [[wiki/entities/snmp-protocol|Protocolo SNMP (Simple Network Management Protocol)]] — MIB, OIDs, NMS y diferencias entre SNMPv1/v2c y SNMPv3.
- [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS de Ciberseguridad]] — Monitorización SOC, Snort, Suricata y correlación de eventos.
- [[wiki/entities/wi-fi-and-mobile-standards|Estándares Inalámbricos Wi-Fi y Redes Móviles (4G/5G)]] — IEEE 802.11a/b/g/n/ac/ax/be y pilares 5G NR.
- [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]] — Direccionamiento, cabeceras fijas vs variables y tipos de unicast/multicast.
- [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]] — Control de flujo, 3-way handshake y datagramas ligeros.
- [[wiki/entities/bgp-and-ospf|Protocolos de Enrutamiento Dinámico: OSPF y BGP]] — Enrutamiento interior por estado de enlace y vector de caminos en Internet.
- [[wiki/entities/tls-ssl-protocols|Protocolos Criptográficos TLS y SSL]] — Certificados X.509, cifrado simétrico/asimétrico y handshake TLS 1.3.
- [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]] — Stateful inspection, NGFW, WAF, túneles IPsec y WireGuard.
- [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]] — Marco español de ciberseguridad pública y guías CCN-STIC.
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802.3]] — Formato de trama Ethernet II, direcciones MAC y CSMA/CD.
- [[wiki/entities/transformer-architecture|Transformer Architecture]] — Arquitectura de aprendizaje profundo basada en atención paralela.
- [[wiki/entities/attention-mechanism|Attention Mechanism]] — Mecanismos de auto-atención y atención multi-cabezal.

---

## 📑 Source Summaries
*Ingested source summaries from `raw/`.*

- [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01: Administración del Sistema Operativo y Software de Base]]
- [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02: Administración de Bases de Datos, Virtualización y Cloud]]
- [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03: Servidores de Correo, Contenedores y Middleware]]
- [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04: Administración de Redes de Área Local]]
- [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05: Seguridad de Sistemas, Infraestructura CPD, Gestión Incidentes]]
- [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06: Comunicaciones: Modos, Medios, Redes Móviles]]
- [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07: Modelo ISO-OSI, TCP-IP, IPv4 e IPv6]]
- [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08: Internet: Protocolos HTTP, HTTPS, TLS y OSPF]]
- [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09: Seguridad en Redes, CCN, VPN, Perimetral]]
- [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10: Redes Locales: Tipología y Métodos de Acceso]]
- [[wiki/sources/transformers-and-llms-overview|Resumen Fuente: Transformer Architecture and LLM Knowledge Systems]]

---

## 🛠️ Tutorials & Operations
- [[tutorials/01-raw-ingest|Tutorial 01: Raw Source Ingestion]] — Ingestion pipeline from `raw/` to `wiki/sources/`.
- [[tutorials/02-schema-and-agents|Tutorial 02: Schema and Agents]] — Defining frontmatter schemas, agent directives, and system prompts.
- [[tutorials/03-entity-and-concept-extraction|Tutorial 03: Entity and Concept Extraction]] — Extracting structured entities and concepts.
- [[tutorials/04-cross-referencing|Tutorial 04: Cross-Referencing and Graph Topology]] — Building bidirectional links and graph density.
- [[tutorials/05-index-and-logging|Tutorial 05: Indexing and Logging]] — Maintaining `index.md` and `log.md`.
- [[tutorials/06-synthesis-and-filing|Tutorial 06: Synthesis and Filing Back]] — Generating syntheses and filing back into `wiki/synthesis/`.
- [[tutorials/07-query-and-lint|Tutorial 07: Query and Lint]] — Querying the wiki and validating health with linter.
"""
    (ROOT_DIR / "index.md").write_text(index_text, encoding="utf-8")
    print("[OK] Master index.md rebuilt successfully.")

def update_log():
    print("\n[*] Updating log.md...")
    log_file = ROOT_DIR / "log.md"
    current_log = log_file.read_text(encoding="utf-8") if log_file.exists() else "# LLM Wiki Operation Log\n\n"
    
    new_entry = f"""
## [{TODAY}] ingest | Bloque 4 TAI Oposiciones (Temas 01 al 10)
- Ingested 10 raw sources from `raw/sources/bloque4-tema01.md` through `bloque4-tema10.md`.
- Created 10 structured summaries in `wiki/sources/`.
- Extracted 21 specialized entities in `wiki/entities/` covering operating systems, databases, containers, protocols and cybersecurity standards.
- Extracted 12 foundational concepts in `wiki/concepts/` covering networking models, memory management, architectures and security paradigms.
- Generated 4 high-level synthesis documents in `wiki/synthesis/` (Master guide, OSI vs TCP/IP, IPv4 vs IPv6, VMs vs Containers).
- Rebuilt `index.md` master catalog.
"""
    log_file.write_text(current_log.strip() + "\n" + new_entry, encoding="utf-8")
    print("[OK] log.md updated.")

def main():
    ensure_dirs()
    write_wiki_sources()
    write_entities_and_concepts()
    write_syntheses()
    rebuild_index()
    update_log()
    print("\n" + "=" * 60)
    print("[OK] INGESTION OF 10 SOURCES COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
