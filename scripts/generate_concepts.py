# -*- coding: utf-8 -*-
"""
Script generador exhaustivo de Conceptos y Síntesis de Estudio para la Wiki del Bloque 4 (TAI).
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
# CONCEPTOS (15 Conceptos Técnicos)
# ==============================================================================

CONCEPTS = {
    "wiki/concepts/operating-system-architecture.md": """---
title: "Arquitectura de Sistemas Operativos y Software de Base"
type: "concept"
tags:
  - operating-systems
  - os-architecture
  - kernel
  - firmware
  - sysadmin
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de Sistemas Operativos"
  - "OS Architecture"
---

# Arquitectura de Sistemas Operativos y Software de Base

La **arquitectura del sistema operativo** define la organización estructural, las capas de abstracción y los mecanismos de comunicación entre el hardware, el núcleo (kernel), los controladores de dispositivos y el software de aplicación.

---

## 🏛️ Modelos de Arquitectura de Kernel

1. **Kernel Monolítico Puro**: Todos los componentes del sistema operativo (planificador, gestión de memoria, sistemas de archivos, drivers de dispositivos y red) se ejecutan en un único espacio de direcciones con el máximo nivel de privilegio (**Ring 0**). Alta velocidad por llamadas a funciones directas, pero menor robustez ante fallos de controladores.
2. **Kernel Monolítico Modular (Linux)**: Mantiene el alto rendimiento monolítico pero permite cargar y descargar controladores dinámicamente en caliente (*Loadable Kernel Modules - LKM*).
3. **Microkernel (Mach, MINIX, QNX)**: Reduce el núcleo a las funciones estrictamente mínimas: comunicación entre procesos (IPC), gestión básica de memoria y planificación. Los servicios como sistemas de archivos y drivers corren en espacio de usuario (**Ring 3**). Máxima tolerancia a fallos y seguridad a costa de una pequeña penalización de rendimiento por cambios de contexto e IPC.
4. **Kernel Híbrido (Windows NT, macOS XNU)**: Combina la velocidad del monolito con la estructura modular del microkernel.

---

## 🧩 Firmware de Arranque: BIOS vs UEFI

| Característica | BIOS Tradicional (Legacy) | UEFI (Unified Extensible Firmware Interface) |
|----------------|---------------------------|----------------------------------------------|
| **Lenguaje de Programación** | Ensamblador | **Lenguaje C** |
| **Modo de Operación CPU** | 16 bits en modo real | **32 bits o 64 bits** en modo protegido |
| **Tabla de Particiones** | **MBR** (máx 2 TB, 4 particiones primarias) | **GPT** (hasta 128 particiones, soporte >2 TB) |
| **Seguridad en el Arranque** | Sin validación de firmas | **Secure Boot** (firmas digitales obligatorias) |
| **Soporte de Red Pre-SO** | Limitado | Nativo (PXE, diagnósticos, IPv4/IPv6) |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tipo de Kernel Linux | **Monolítico Modular** |
| Anillos de Privilegio x86 | **Ring 0** (Kernel) y **Ring 3** (Usuario) |
| Límite Direccionamiento MBR | **2 Terabytes** |
| Especificación UEFI | Escrita en **C**, sucesor de BIOS, soporte Secure Boot |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
""",

    "wiki/concepts/process-and-memory-management.md": """---
title: "Gestión de Procesos y Memoria en Sistemas Operativos"
type: "concept"
tags:
  - processes
  - memory-management
  - virtual-memory
  - operating-systems
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Gestión de Procesos y Memoria"
  - "Process and Memory Management"
---

# Gestión de Procesos y Memoria en Sistemas Operativos

La gestión eficiente de los procesadores y de la memoria principal constituye una de las tareas esenciales de cualquier sistema operativo multiprogramado.

---

## 🏛️ Gestión de Procesos y Planificación

- **Definición de Proceso**: Programa en ejecución junto con su espacio de memoria (código, datos, pila, montículo) y su **PCB (Process Control Block)**.
- **Transición de Estados de un Proceso**:
  - `Nuevo` $\rightarrow$ `Listo (Ready)` $\leftrightarrow$ `Ejecución (Running)` $\rightarrow$ `Terminado (Zombie/Exit)`.
  - `Ejecución` $\rightarrow$ `Bloqueado/Esperando (Waiting/Sleep)` $\rightarrow$ `Listo`.
- **Algoritmos de Planificación de CPU**:
  - **FCFS (First-Come, First-Served)**: No apropiativo; sufre del efecto convoy.
  - **SJF (Shortest Job First)**: Óptimo en tiempo medio de espera; puede causar inanición (*Starvation*).
  - **Round Robin (RR)**: Apropiativo basado en un cuanto de tiempo (*Quantum*).
  - **Colas Multinivel con Realimentación (MLFQ)**: Prioridades dinámicas según el comportamiento del proceso (I/O bound vs. CPU bound).
  - **CFS (Completely Fair Scheduler)**: Planificador de Linux basado en tiempo de ejecución virtual (*vruntime*) y árboles rojo-negro.

---

## 🧩 Gestión de Memoria Virtual y Paginación

- **Memoria Virtual**: Permite ejecutar procesos cuyo tamaño supera la memoria RAM física disponible mediante la abstracción del espacio de direcciones.
- **Paginación**:
  - La memoria lógica se divide en **Páginas** de tamaño fijo (típicamente 4 KB).
  - La memoria física se divide en **Marcos de Página (Frames)** del mismo tamaño.
  - La **MMU (Memory Management Unit)** traduce direcciones virtuales a físicas mediante la **Tabla de Páginas** y acelera las consultas con la **TLB (Translation Lookaside Buffer)**.
- **Fallo de Página (Page Fault)**: Ocurre cuando un proceso intenta acceder a una página que no está cargada en RAM física. El SO suspende el proceso, lee la página desde el disco (área de *Swap* o fichero de paginación) y actualiza la tabla de páginas.
- **Hiperpaginación (Thrashing)**: Situación crítica donde el sistema dedica más tiempo a transferir páginas entre RAM y disco que a ejecutar instrucciones útiles.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Detalle Técnico |
|----------|-----------------|
| Tamaño Página Estándar | **4 Kilobytes (4096 bytes)** |
| Planificador Linux | **CFS (Completely Fair Scheduler)** |
| Acelerador de Traducción MMU | **TLB (Translation Lookaside Buffer)** |
| Algoritmo de Reemplazo Óptimo Teórico | Algoritmo de **Belady** (reemplaza la página que tardará más en usarse) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
""",

    "wiki/concepts/directory-services-and-identity.md": """---
title: "Servicios de Directorio y Gestión de Identidades"
type: "concept"
tags:
  - directory-services
  - identity
  - ldap
  - active-directory
  - sso
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Servicios de Directorio"
  - "Directory Services"
---

# Servicios de Directorio y Gestión de Identidades

Un **servicio de directorio** es un sistema de software especializado que almacena, organiza y proporciona acceso seguro y jerárquico a información sobre usuarios, grupos, equipos y recursos de red en una organización.

---

## 🏛️ Características y Diferencias frente a RDBMS

| Característica | Servicio de Directorio (LDAP / AD) | Base de Datos Relacional (RDBMS) |
|----------------|-------------------------------------|----------------------------------|
| **Perfil de Carga** | **Altamente optimizado para LECTURAS** ($>90\%$) | Equilibrado entre Lecturas y Escrituras masivas |
| **Estructura de Datos** | **Jerárquica en Árbol (DIT)** | Tablas bidimensionales normalizadas |
| **Esquema** | Extensible mediante clases de objetos y atributos | Esquema estricto de tablas y claves |
| **Protocolo de Acceso** | **LDAPv3 (RFC 4511)** / Kerberos | SQL (DDL, DML) vía ODBC/JDBC |
| **Replicación** | Multimaestro o maestro-esclavo optimizada para WAN | Replicación transaccional síncrona/asíncrona |

---

## 🧩 Protocolos y Autenticación Centralizada

- **X.500 / LDAPv3**: Estándares de consulta y esquema de nombrado mediante nombres distinguidos (**DN**).
- **Kerberos v5 (RFC 4120)**: Protocolo de autenticación basado en un Centro de Distribución de Claves (**KDC**) que emite tickets de concesión de tickets (**TGT**) y tickets de servicio (**TGS**), evitando el envío de contraseñas por la red.
- **Single Sign-On (SSO)**: Permite al usuario autenticarse una sola vez y acceder a múltiples sistemas autorizados (mediante Kerberos, SAML 2.0, OpenID Connect / OAuth 2.0).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Técnica |
|----------|------------------------|
| Puerto LDAP / LDAPS | **389 TCP/UDP** / **636 TCP** |
| Puerto Kerberos KDC | **88 TCP/UDP** |
| Estándar de Certificados | **X.509** |
| Formato de Exportación | **LDIF** (RFC 2849) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
- Síntesis: [[wiki/synthesis/active-directory-and-ldap-guide|Guía Active Directory y LDAP]]
""",

    "wiki/concepts/database-normalization-and-acid.md": """---
title: "Normalización de Bases de Datos y Propiedades ACID"
type: "concept"
tags:
  - databases
  - normalization
  - acid
  - transactions
  - sql
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Normalización y ACID"
  - "Database Normalization"
---

# Normalización de Bases de Datos y Propiedades ACID

El diseño formal de bases de datos relacionales garantiza la integridad de los datos, la eliminación de anomalías de inserción/borrado/actualización y la fiabilidad de las transacciones.

---

## 🏛️ Formas Normales (1FN a BCNF)

1. **Primera Forma Normal (1FN)**:
   - Todos los atributos contienen valores atómicos e indivisibles (sin grupos repetitivos o listas).
   - Existe una clave primaria definida para la tabla.
2. **Segunda Forma Normal (2FN)**:
   - Cumple 1FN.
   - Todo atributo no principal tiene **dependencia funcional completa** de la clave primaria (no depende de una parte de una clave compuesta).
3. **Tercera Forma Normal (3FN)**:
   - Cumple 2FN.
   - No existen **dependencias transitivas** entre atributos no clave (ningún atributo no clave depende de otro atributo no clave).
4. **Forma Normal de Boyce-Codd (BCNF)**:
   - Versión estricta de 3FN.
   - Para toda dependencia funcional no trivial $X \rightarrow Y$, el determinante $X$ debe ser una **superclave** (o clave candidata).

---

## 🧩 Propiedades ACID de las Transacciones

- **A (Atomicidad / Atomicity)**: Principio del "todo o nada". La transacción se ejecuta completamente con éxito (`COMMIT`) o sus efectos se revierten íntegramente (`ROLLBACK`).
- **C (Consistencia / Consistency)**: La transacción traslada la base de datos de un estado válido y consistente a otro estado válido, respetando todas las reglas de integridad.
- **I (Aislamiento / Isolation)**: La ejecución concurrente de múltiples transacciones produce el mismo resultado que si se ejecutaran secuencialmente.
  - **Niveles de Aislamiento SQL-92**:
    - *Read Uncommitted*: Permite lecturas sucias (*Dirty Reads*).
    - *Read Committed*: Evita lecturas sucias; permite lecturas no repetibles.
    - *Repeatable Read*: Evita lecturas no repetibles; permite lecturas fantasma (*Phantom Reads*).
    - *Serializable*: Máximo aislamiento; previene todos los fenómenos anómalos.
- **D (Durabilidad / Durability)**: Una vez confirmada una transacción (`COMMIT`), sus cambios persisten permanentemente en el almacenamiento no volátil mediante el registro de transacciones (*Write-Ahead Logging / WAL*).

---

## 🎯 Datos Clave para Oposiciones TAI

| Nivel de Aislamiento SQL | Lectura Sucia | Lectura No Repetible | Lectura Fantasma |
|--------------------------|---------------|----------------------|------------------|
| **Read Uncommitted** | Sí | Sí | Sí |
| **Read Committed** | **No** | Sí | Sí |
| **Repeatable Read** | **No** | **No** | Sí |
| **Serializable** | **No** | **No** | **No** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
""",

    "wiki/concepts/virtualization-and-cloud-computing.md": """---
title: "Virtualización, Hipervisores y Modelos Cloud Computing"
type: "concept"
tags:
  - virtualization
  - hypervisors
  - cloud-computing
  - iaas
  - paas
  - saas
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Virtualización y Cloud"
  - "Virtualization and Cloud"
---

# Virtualización, Hipervisores y Modelos Cloud Computing

La **virtualización** abstrae el hardware físico para crear entornos lógicos independientes, constituyendo el habilitador tecnológico esencial de la **computación en la nube (Cloud Computing)**.

---

## 🏛️ Clasificación de Hipervisores (VMM)

- **Hipervisores Tipo 1 (Bare-Metal / Nativos)**:
  - Se instalan y ejecutan directamente sobre el hardware físico del servidor sin sistema operativo intermedio.
  - Ofrecen máximo rendimiento, menor latencia y mayor seguridad.
  - Ejemplos líderes: **VMware ESXi**, **Microsoft Hyper-V**, **KVM (Kernel-based Virtual Machine)**, **Xen**.
- **Hipervisores Tipo 2 (Hosted / Alojados)**:
  - Se ejecutan como una aplicación sobre un sistema operativo anfitrión (*Host OS*).
  - Utilizados principalmente para desarrollo, pruebas y puestos de trabajo locales.
  - Ejemplos: **Oracle VirtualBox**, **VMware Workstation / Fusion**, **QEMU**.

---

## 🧩 Modelos de Servicio y Despliegue en Cloud (NIST SP 800-145)

| Modelo de Servicio | Descripción | Qué Gestiona el Proveedor | Qué Gestiona el Cliente | Ejemplos |
|-------------------|-------------|---------------------------|-------------------------|----------|
| **IaaS** | Infraestructura como Servicio | Hardware, Red, Almacenamiento, Hipervisor | **SO, Middleware, Runtime, Datos, Aplicación** | AWS EC2, Azure VMs, Google Compute Engine |
| **PaaS** | Plataforma como Servicio | Hardware, Hipervisor, SO, Middleware, Runtime | **Datos y Código de la Aplicación** | AWS Elastic Beanstalk, Heroku, Azure App Service |
| **SaaS** | Software como Servicio | **Toda la pila completa** de infraestructura y software | Únicamente configuración de usuario | Microsoft 365, Google Workspace, Salesforce |
| **FaaS** | Serverless / Funciones | Pila completa y escalado de micro-instancias | **Solo el código de la función invocada** | AWS Lambda, Azure Functions, Cloud Functions |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar Definición Cloud | **NIST SP 800-145** |
| Extensiones CPU Virtualización | **Intel VT-x** / **AMD-V** |
| Funcionalidad Migración en Caliente | **vMotion** (VMware) / **Live Migration** (Hyper-V/KVM) |
| Balanceo Dinámico de Carga | **DRS** (Distributed Resource Scheduler) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
""",

    "wiki/concepts/datacenter-infrastructure-and-disaster-recovery.md": """---
title: "Infraestructura de Centros de Proceso de Datos (CPD) y Recuperación ante Desastres"
type: "concept"
tags:
  - cpd
  - datacenter
  - tia-942
  - disaster-recovery
  - rto-rpo
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Infraestructura de CPD"
  - "Datacenter Architecture"
---

# Infraestructura de Centros de Proceso de Datos (CPD) y Recuperación ante Desastres

El diseño físico de un **Centro de Proceso de Datos (CPD)** y la planificación de la continuidad de negocio garantizan la operación ininterrumpida de los servicios de TI frente a contingencias.

---

## 🏛️ Clasificación TIER de CPDs (Estándar ANSI/TIA-942)

| Nivel TIER | Nombre / Descripción | Disponibilidad Anual | Inactividad Máxima Anual | Redundancia Componentes | Rutas de Distribución |
|------------|----------------------|----------------------|--------------------------|-------------------------|-----------------------|
| **TIER I** | Básico | **99.671%** | **28.8 horas/año** | $N$ (Sin redundancia) | 1 ruta única |
| **TIER II** | Componentes Redundantes | **99.741%** | **22.0 horas/año** | $N + 1$ | 1 ruta única |
| **TIER III** | Mantenimiento Concurrente | **99.982%** | **1.6 horas/año** | $N + 1$ (Mantenible sin parar) | 1 activa + 1 pasiva (2 rutas) |
| **TIER IV** | Tolerante a Fallos | **99.995%** | **26.3 minutos/año** | $2(N + 1)$ o $2N + 1$ | **2 rutas activas simultáneas** |

---

## 🧩 Métricas de Continuidad y Sitios de Respaldo

- **RPO (Recovery Point Objective)**: Volumen máximo de datos perdidos tolerables medido en tiempo transcurrido desde el último punto de respaldo.
- **RTO (Recovery Time Objective)**: Tiempo máximo admisible para restaurar la operatividad de los sistemas tras una interrupción.
- **Tipos de Sedes Secundarias (Recovery Sites)**:
  - **Hot Site (Sitio Caliente)**: Réplica exacta totalmente equipada y sincronizada en tiempo real. RTO/RPO cercanos a cero.
  - **Warm Site (Sitio Templado)**: Equipamiento informático preinstalado pero datos no sincronizados en tiempo real (requiere restaurar último backup). RTO de horas a días.
  - **Cold Site (Sitio Frío)**: Espacio físico acondicionado con energía y climatización pero sin hardware ni datos informáticos. RTO de semanas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Estándar |
|-----------|----------------|
| Norma de Clasificación CPDs | **ANSI/TIA-942** |
| Disponibilidad TIER IV | **99.995%** (26.3 min caída/año) |
| Temperatura Óptima CPD (ASHRAE) | **18 °C a 27 °C** |
| Humedad Relativa Óptima | **40% a 60%** |
| Gases de Extinción Limpios | **Novec 1230**, **FM-200**, **Inergen** (no destructivos) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Entidad: [[wiki/entities/raid-storage|Sistemas de Almacenamiento RAID, DAS, NAS y SAN]]
- Síntesis: [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
""",

    "wiki/concepts/microservices-and-middleware.md": """---
title: "Microservicios, Arquitecturas Distribuidas y Middleware"
type: "concept"
tags:
  - microservices
  - middleware
  - api-gateway
  - cloud-native
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Microservicios y Middleware"
  - "Microservices Architecture"
---

# Microservicios, Arquitecturas Distribuidas y Middleware

La **arquitectura de microservicios** estructura una aplicación como una colección de servicios autónomos, débilmente acoplados, desplegables independientemente y organizados en torno a capacidades de negocio.

---

## 🏛️ Monolito frente a Microservicios

| Criterio | Arquitectura Monolítica | Arquitectura de Microservicios |
|----------|-------------------------|--------------------------------|
| **Base de Código** | Unificada y fuertemente acoplada | Repositorios o módulos independientes |
| **Despliegue** | Todo-o-nada (*Big Bang*) | Despliegues independientes y continuos (CI/CD) |
| **Escalabilidad** | Escalado vertical o replicación de todo el monolito | Escalado granular de los servicios con mayor carga |
| **Gestión de Datos** | Base de datos relacional compartida | Base de datos por servicio (*Database-per-Service*) |
| **Resiliencia** | Un fallo en un módulo puede tumbar toda la app | Aislamiento de fallos con patrones Circuit Breaker |

---

## 🧩 Patrones de Microservicios y Middleware

- **API Gateway**: Punto único de entrada para clientes que gestiona autenticación, enrutamiento, limitación de tasa (*Rate Limiting*) y terminación SSL.
- **Service Mesh (Malla de Servicios)**: Capa de infraestructura dedicada para la comunicación segura este-oeste entre microservicios (mediante proxies sidecar como Envoy en Istio).
- **Middleware Orientado a Mensajes (MOM)**: Desacopla servicios mediante comunicación asíncrona por colas de mensajes (RabbitMQ, Apache Kafka).

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Componente | Función Principal |
|---------------------|-------------------|
| API Gateway | Punto de entrada, autenticación y enrutamiento perimetral |
| Circuit Breaker | Corta peticiones a servicios caídos para evitar fallos en cascada |
| Service Mesh | Gestión de tráfico, observabilidad y mTLS servicio a servicio |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
""",

    "wiki/concepts/routing-and-switching-mechanisms.md": """---
title: "Mecanismos de Conmutación (Switching) y Enrutamiento LAN"
type: "concept"
tags:
  - switching
  - routing
  - vlan
  - stp
  - lan
sources:
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Conmutación y Enrutamiento"
  - "Switching and Routing"
---

# Mecanismos de Conmutación (Switching) y Enrutamiento LAN

Los switches y routers constituyen los dispositivos activos fundamentales para el control de tráfico y segmentación en redes locales y corporativas.

---

## 🏛️ Conmutación de Nivel 2 y Protocolos STP

- **Tabla de Direcciones MAC (CAM Table)**: Los switches aprenden dinámicamente las direcciones MAC de origen de las tramas entrantes asociándolas a sus puertos físicos con un temporizador de envejecimiento (*Aging Time* de 300 s).
- **Protocolo Spanning Tree (STP - IEEE 802.1D)**:
  - Previene bucles de capa 2 y tormentas de broadcast en topologías redundantes bloqueando puertos lógicamente.
  - Elección del **Bridge Raíz (Root Bridge)**: Switch con el menor valor de **Bridge ID (BID)** (prioridad + MAC).
  - Estados de puerto STP: *Bloqueo (Blocking)* $\rightarrow$ *Escucha (Listening)* $\rightarrow$ *Aprendizaje (Learning)* $\rightarrow$ *Reenvío (Forwarding)*.
- **Rapid Spanning Tree Protocol (RSTP - IEEE 802.1w)**: Reduce el tiempo de convergencia de 30-50 segundos a unos pocos milisegundos mediante negociación de propuestas y acuerdos.

---

## 🧩 Segmentación con VLANs y Enrutamiento Inter-VLAN

- **VLANs (Virtual Local Area Networks - IEEE 802.1Q)**:
  - Dividen un switch físico en múltiples dominios de difusión lógicos aislados.
  - Etiqueta 802.1Q de **4 bytes**: Contiene el TPID (`0x8100`) y el **VLAN ID (12 bits: 1 a 4094)**.
  - Puertos de Acceso (*Access Ports* - sin etiquetar) vs. Puertos Troncales (*Trunk Ports* - etiquetados).
- **Enrutamiento Inter-VLAN**:
  - **Router-on-a-Stick**: Un único router conectado por un enlace troncal al switch mediante subinterfaces con encapsulación 802.1Q.
  - **Switch de Capa 3 (Multilayer Switch)**: Enrutamiento por hardware a velocidad de cable mediante interfaces virtuales de switch (**SVI**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar STP Clásico / RSTP | **IEEE 802.1D** / **IEEE 802.1w** |
| Tamaño Tag VLAN 802.1Q | **4 bytes** (VLAN ID de **12 bits**) |
| Rango de VLAN IDs | **1 a 4094** |
| Criterio Elección Root Bridge | **Menor Bridge ID (Prioridad + MAC)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema04|Resumen Bloque 4 - Tema 04]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- Concepto: [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Acceso al Medio]]
""",

    "wiki/concepts/transmission-media-and-modes.md": """---
title: "Medios de Transmisión Guiados y No Guiados"
type: "concept"
tags:
  - transmission-media
  - fiber-optics
  - twisted-pair
  - cabling
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Medios de Transmisión"
  - "Transmission Media"
---

# Medios de Transmisión Guiados y No Guiados

La capa física de comunicaciones utiliza medios guiados (cables de cobre y fibras ópticas) y no guiados (ondas electromagnéticas en el espacio libre) para transportar señales entre emisor y receptor.

---

## 🏛️ Medios Guiados: Par Trenzado vs Fibra Óptica

| Característica | Par Trenzado de Cobre (UTP/STP) | Fibra Óptica (Monomodo / Multimodo) |
|----------------|---------------------------------|--------------------------------------|
| **Medio Físico** | Conductores de cobre aislados y trenzados | Hilos de sílice/vidrio ultrapuro |
| **Señal** | Impulsos eléctricos de voltaje | Pulsos de luz (reflexión interna total) |
| **Inmunidad EMI** | Vulnerable a ruido electromagnético | **100% Inmune a interferencias EMI/RFI** |
| **Atenuación** | Alta con la distancia | Extremadamente baja |
| **Distancia Máxima Estándar** | **100 metros** en canal estructurado | Cientos de metros (MMF) a **>40 km** (SMF) |
| **Seguridad Física** | Fácilmente interceptable | Muy difícil de pinchar sin ser detectado |

---

## 🧩 Categorías de Cable y Cableado Estructurado

- **Normas**: **ISO/IEC 11801** y **ANSI/TIA/EIA-568**.
- **Canal Horizontal**: Máximo **90 metros** de cable permanente + **10 metros** de latiguillos = **100 metros totales**.
- **Categorías de Cobre**:
  - **Cat 5e**: 100 MHz $\rightarrow$ 1000BASE-T (1 Gbps a 100 m).
  - **Cat 6**: 250 MHz $\rightarrow$ 1000BASE-T (100 m) / 10GBASE-T (55 m).
  - **Cat 6A**: **500 MHz** $\rightarrow$ **10GBASE-T (10 Gbps a 100 m)**.
  - **Cat 8**: 2000 MHz (2 GHz) $\rightarrow$ 25G/40GBASE-T (hasta 30 m).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Longitud Canal Horizontal | **100 metros máximo** (90 m fijo + 10 m latiguillos) |
| Longitudes de Onda Fibra Monomodo | **1310 nm y 1550 nm** (Láser, núcleo ~9 µm) |
| Longitudes de Onda Fibra Multimodo | **850 nm y 1300 nm** (LED/VCSEL, núcleo 50/62.5 µm) |
| Conectores de Fibra Óptica | **LC, SC, ST, FC, MPO** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet]]
""",

    "wiki/concepts/osi-and-tcp-ip-models.md": """---
title: "Modelos Arquitectónicos ISO-OSI y TCP-IP"
type: "concept"
tags:
  - osi-model
  - tcp-ip
  - networking-models
  - encapsulation
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelos OSI y TCP/IP"
  - "OSI vs TCP/IP"
---

# Modelos Arquitectónicos ISO-OSI y TCP-IP

Los modelos arquitectónicos estratificados proporcionan un marco modular y estandarizado para el diseño e interoperabilidad de redes de comunicación.

---

## 🏛️ Mapeo y Comparativa: 7 Capas OSI vs 4 Capas TCP/IP

```
    Modelo OSI (ISO 7498-1)                Modelo TCP/IP (RFC 1122)
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ 7. Aplicación (Application)   │        │                               │
├───────────────────────────────┤        │ 4. Aplicación (Application)   │
│ 6. Presentación (Presentation)│  ───►  │    (HTTP, DNS, SMTP, SSH)     │
├───────────────────────────────┤        │                               │
│ 5. Sesión (Session)           │        │                               │
├───────────────────────────────┤        ├───────────────────────────────┤
│ 4. Transporte (Transport)     │  ───►  │ 3. Transporte (TCP, UDP)      │
├───────────────────────────────┤        ├───────────────────────────────┤
│ 3. Red (Network)              │  ───►  │ 2. Internet (IPv4, IPv6, ICMP)│
├───────────────────────────────┤        ├───────────────────────────────┤
│ 2. Enlace (Data Link)         │        │ 1. Acceso a la Red            │
├───────────────────────────────┤  ───►  │    (Network Access)           │
│ 1. Física (Physical)          │        │    (Ethernet, Wi-Fi, PPP)     │
└───────────────────────────────┘        └───────────────────────────────┘
```

---

## 🧩 Proceso de Encapsulación de Datos

A medida que los datos descienden por las capas del emisor, cada nivel añade su propia cabecera de control (**PCI - Protocol Control Information**):
1. **Capa de Aplicación**: Genera el mensaje o flujo de datos original.
2. **Capa de Transporte**: Añade cabecera TCP o UDP (puertos) $\rightarrow$ **Segmento** (TCP) o **Datagrama** (UDP).
3. **Capa de Red**: Añade cabecera IP (direcciones IP origen/destino) $\rightarrow$ **Paquete** o **Datagrama IP**.
4. **Capa de Enlace**: Añade cabecera MAC y cola de comprobación (**FCS / CRC-32**) $\rightarrow$ **Trama (Frame)**.
5. **Capa Física**: Convierte la trama en una secuencia de señales binarias $\rightarrow$ **Bits**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Nivel OSI | PDU | Funcionalidad Clave |
|-----------|-----|---------------------|
| Capa 7 (Aplicación) | Datos | Interfaz de servicios de red con el usuario |
| Capa 6 (Presentación) | Datos | Sintaxis, compresión y cifrado (ASN.1, MIME) |
| Capa 5 (Sesión) | Datos | Sincronización y diálogo de sesión (RPC) |
| Capa 4 (Transporte) | **Segmento** | Comunicación extremo a extremo y puertos |
| Capa 3 (Red) | **Paquete** | Direccionamiento lógico y enrutamiento global |
| Capa 2 (Enlace) | **Trama** | Direccionamiento físico MAC y detección CRC |
| Capa 1 (Física) | **Bit** | Transmisión eléctrica/óptica sobre el medio |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI frente a TCP-IP]]
""",

    "wiki/concepts/internet-architecture-and-web-protocols.md": """---
title: "Arquitectura de Internet y Protocolos Web (HTTP/1-3)"
type: "concept"
tags:
  - internet
  - web
  - http
  - http2
  - http3
  - quic
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de Internet"
  - "Web Protocols"
---

# Arquitectura de Internet y Protocolos Web (HTTP/1-3)

La infraestructura de Internet opera mediante una jerarquía global descentralizada de proveedores de servicios interconectados a través de puntos neutros y protocolos de aplicación web.

---

## 🏛️ Jerarquía de Tráfico Global en Internet

- **Tier 1 (Troncales Globales)**: Operadores con redes de fibra transoceánicas que no pagan por tránsito (*Settlement-Free Peering*).
- **IXP (Internet Exchange Points)**: Conmutadores de alta capacidad donde ISPs y CDNs intercambian tráfico localmente (ej. ESpanix en España).
- **CDNs (Content Delivery Networks)**: Redes distribuidas geográficamente que cachean contenido estático y dinámico cerca de los usuarios finales (Cloudflare, Akamai).

---

## 🧩 Evolución de los Protocolos Web HTTP

- **HTTP/1.1**: Conexiones persistentes (`Keep-Alive`) pero limitado por bloqueo en cabeza de línea (*Head-of-Line Blocking*) a nivel de aplicación.
- **HTTP/2**: Formato binario con multiplexación de múltiples flujos sobre una sola conexión TCP y compresión **HPACK**.
- **HTTP/3**: Elimina el transporte TCP sustituyéndolo por **QUIC (RFC 9000)** sobre **UDP** (puerto 443), eliminando el bloqueo en cabeza de línea de transporte, integrando **TLS 1.3** nativo (0-RTT/1-RTT) y permitiendo migración transparente de conexión por *Connection ID*.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo | Transporte | Puerto | Compresión Cabeceras |
|-----------|------------|--------|----------------------|
| HTTP/1.1 | TCP | 80 / 443 (TLS) | Ninguna |
| HTTP/2 | TCP | 443 (TLS) | **HPACK** |
| HTTP/3 | **QUIC (UDP)** | **443 UDP** | **QPACK** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
- Entidad: [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]
""",

    "wiki/concepts/network-security-and-perimeter-defense.md": """---
title: "Seguridad en Redes y Defensa Perimetral"
type: "concept"
tags:
  - network-security
  - perimeter-defense
  - dmz
  - defense-in-depth
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Seguridad Perimetral"
  - "Defensa en Profundidad"
---

# Seguridad en Redes y Defensa Perimetral

La **defensa en profundidad (*Defense-in-Depth*)** articula múltiples capas concéntricas de controles de seguridad físicos, de red, de host y de aplicación para proteger los activos de información corporativos.

---

## 🏛️ Arquitecturas Perimetrales y Zonas DMZ

1. **Zona Desmilitarizada (DMZ / Zona Neutra)**:
   - Subred aislada que aloja servidores accesibles públicamente desde Internet (Web, Correo externo, DNS público).
   - **Regla de Oro**: Ninguna conexión iniciada desde la DMZ puede tener acceso directo no filtrado a la red interna confidencial (*LAN Corporativa*).
2. **Topología con Cortafuegos de 3 Patas (Three-Pronged)**:
   - Un solo cortafuegos con 3 interfaces dedicadas: Internet (No confiable), DMZ (Semiconfiable) e Intranet (Confiable).
3. **Topología con Cortafuegos en Cascada (Back-to-Back)**:
   - La DMZ se sitúa entre un cortafuegos perimetral externo y un cortafuegos interno de distinto fabricante, garantizando que el compromiso de un cortafuegos no comprometa automáticamente la red interna.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Regla de Diseño Perimetral |
|----------|----------------------------|
| Ubicación Servidores Web | Siempre en **DMZ** (nunca en la LAN interna directa) |
| Tráfico DMZ $\rightarrow$ LAN | **Estrictamente bloqueado** por defecto (solo respuestas o servicios autenticados) |
| Cortafuegos Back-to-Back | Utiliza **fabricantes distintos** para evitar vulnerabilidades de software compartidas |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/firewalls-and-vpn|Cortafuegos y VPN]]
- Entidad: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
""",

    "wiki/concepts/lan-topologies-and-mac-protocols.md": """---
title: "Topologías LAN y Protocolos de Acceso al Medio (MAC)"
type: "concept"
tags:
  - lan
  - topologies
  - csma-cd
  - csma-ca
  - ieee-802
sources:
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Topologías LAN y Control de Acceso"
  - "MAC Protocols"
---

# Topologías LAN y Protocolos de Acceso al Medio (MAC)

Las redes de área local organizan sus nodos mediante disposiciones geométricas (topologías físicas y lógicas) y gestionan la contienda sobre medios compartidos mediante protocolos de control de acceso al medio (**MAC**).

---

## 🏛️ Topologías de Red Principales

- **Bus**: Todos los nodos comparten un mismo canal físico lineal con terminadores en los extremos. Punto único de fallo en el cable troncal.
- **Estrella**: Todos los nodos se conectan a un conmutador central. Es la topología física dominante en las redes Ethernet modernas.
- **Anillo (Ring)**: Circuito cerrado donde cada nodo reenvía al siguiente (Token Ring, FDDI con doble anillo).
- **Malla Completa**: Cada nodo se conecta con todos los demás. Requiere $N(N-1)/2$ enlaces. Máxima tolerancia a fallos.

---

## 🧩 Protocolos de Contienda: CSMA/CD frente a CSMA/CA

| Parámetro | CSMA/CD (IEEE 802.3 - Ethernet Cableado) | CSMA/CA (IEEE 802.11 - Wi-Fi Inalámbrico) |
|-----------|------------------------------------------|-------------------------------------------|
| **Principio** | Detección de Colisiones (*Collision Detection*) | Prevención de Colisiones (*Collision Avoidance*) |
| **Mecanismo** | Escucha mientras transmite; si detecta colisión envía señal *Jam* y ejecuta Backoff | Escucha antes de hablar; utiliza IFS (DIFS/SIFS) y reservas virtuales **RTS/CTS** |
| **Motivo** | Los cables permiten detectar variaciones anómalas de voltaje durante la transmisión | En radio, la potencia de transmisión del propio nodo ensordece su receptor |
| **Backoff** | **Retroceso Exponencial Binario (BEB)** tras colisión | Ventana de contienda aleatoria antes de transmitir |
| **Límite Intentos** | **16 intentos máximos** (descarte de trama) | Límite de retransmisiones de tramas |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Tamaño Mínimo Trama Ethernet | **64 bytes (512 bits / Slot Time)** |
| Tamaño Máximo Trama Ethernet | **1518 bytes** (1522 bytes con 802.1Q) |
| Enlaces Malla Completa | $N(N-1)/2$ |
| Algoritmo de Espera Ethernet | **Binary Exponential Backoff** (hasta intento 10) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema10|Resumen Bloque 4 - Tema 10]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
""",

    "wiki/concepts/cryptography-and-digital-signatures.md": """---
title: "Criptografía Simétrica, Asimétrica y Firma Digital"
type: "concept"
tags:
  - cryptography
  - digital-signature
  - pki
  - x509
  - security
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Criptografía y Firma Digital"
  - "Cryptography and PKI"
---

# Criptografía Simétrica, Asimétrica y Firma Digital

La criptografía proporciona los mecanismos matemáticos para garantizar la confidencialidad, autenticidad, integridad y no repudio de la información en entornos digitales.

---

## 🏛️ Tipos de Criptografía

1. **Criptografía Simétrica (Clave Secreta)**:
   - Misma clave para cifrar y descifrar.
   - Algoritmo estándar: **AES (Advanced Encryption Standard / Rijndael)** con bloques de 128 bits y claves de **128, 192 o 256 bits**.
2. **Criptografía Asimétrica (Clave Pública / Privada)**:
   - Clave pública para cifrar/verificar; clave privada para descifrar/firmar.
   - Algoritmos: **RSA** (factorización de primos), **Diffie-Hellman** (intercambio de claves), **ECDSA / Ed25519** (curvas elípticas).
3. **Criptografía Híbrida**: Cifra el mensaje con una clave de sesión simétrica efímera y cifra dicha clave de sesión con la clave pública asimétrica del receptor (utilizado en TLS, SSH, PGP).

---

## 🧩 Firma Digital y Certificados X.509

- **Mecanismo de Firma Digital**:
  1. El emisor genera un **resumen hash** del mensaje original ($H = \text{Hash}(M)$).
  2. El emisor cifra el hash $H$ con su **Clave Privada** $\rightarrow$ obteniendo la **Firma Digital**.
  3. El receptor descifra la firma con la **Clave Pública del Emisor** obteniendo $H_1$, calcula su propio hash $H_2 = \text{Hash}(M)$ y verifica que $H_1 == H_2$.
- **Formatos de Firma Electrónica Avanzada**:
  - **CAdES** (CMS Advanced Electronic Signature): Para ficheros binarios genéricos.
  - **XAdES** (XML Advanced Electronic Signature): Para documentos XML.
  - **PAdES** (PDF Advanced Electronic Signature): Integrada nativamente en ficheros PDF (ISO 32000-1).
- **Jerarquía de Certificados X.509**:
  - Autoridad de Certificación (CA) Raíz $\rightarrow$ CAs Subordinadas $\rightarrow$ Certificado Final de Usuario/Servidor.
  - Verificación de Revocación: **CRL** (Listas de Revocación) y **OCSP** (Online Certificate Status Protocol, RFC 6960 en puerto 80 HTTP).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| Algoritmo Simétrico Estándar | **AES** (128, 192, 256 bits de clave) |
| Formato Certificados Digitales | **ITU-T X.509** |
| Formatos Firma Avanzada | **CAdES** (binario), **XAdES** (XML), **PAdES** (PDF) |
| Protocolo Validación en Línea | **OCSP** (RFC 6960, puerto 80 HTTP) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Síntesis: [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital]]
""",

    "wiki/concepts/incident-management-and-itil.md": """---
title: "Gestión de Incidencias y Marco ITIL en Servicios TI"
type: "concept"
tags:
  - itil
  - incident-management
  - service-desk
  - sla
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Gestión de Incidencias e ITIL"
  - "ITIL Incident Management"
---

# Gestión de Incidencias y Marco ITIL en Servicios TI

El marco **ITIL (Information Technology Infrastructure Library)** proporciona un conjunto de mejores prácticas para la gestión y entrega eficiente de servicios de tecnologías de la información.

---

## 🏛️ Gestión de Incidencias frente a Gestión de Problemas

- **Incidencia**: Cualquier interrupción no planificada o reducción en la calidad de un servicio de TI. Su objetivo prioritario es **restaurar el servicio lo más rápido posible** (mediante parches, reinicios o soluciones temporales / *Workarounds*).
- **Problema**: Causa subyacente desconocida de una o múltiples incidencias. Su objetivo es **identificar la causa raíz** y proporcionar una solución definitiva.

---

## 🧩 Service Desk y Ciclo de Vida de una Incidencia

- **Service Desk (Centro de Servicios)**: Actúa como el **Único Punto de Contacto (SPOC - Single Point of Contact)** entre los usuarios finales y el departamento de TI.
- **Fases del Ciclo de Vida de Incidencias**:
  1. *Registro*: Creación formal del ticket.
  2. *Categorización*: Clasificación temática del fallo.
  3. *Priorización*: Determinada por la fórmula $\text{Prioridad} = \text{Impacto} \times \text{Urgencia}$.
  4. *Diagnóstico Inicial*: Soporte de Nivel 1.
  5. *Escalado*: Funcional (a Nivel 2/3 especialistas) o Jerárquico.
  6. *Resolución y Recuperación*: Aplicación de solución o workaround.
  7. *Cierre*: Verificación formal con el usuario y registro en la base de conocimiento de errores conocidos (**KEDB**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Término ITIL | Definición |
|--------------|------------|
| **SPOC** | Single Point of Contact (**Service Desk**) |
| **SLA** | Service Level Agreement (Acuerdo de Nivel de Servicio con el cliente) |
| **OLA** | Operational Level Agreement (Acuerdo interno entre equipos de TI) |
| **KEDB** | Known Error Database (Base de datos de errores conocidos) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
"""
}

print("[*] Escribiendo 15 conceptos técnicos ampliados...")
for path, content in CONCEPTS.items():
    write_file(path, content)

print("[*] Conceptos generados con éxito.")
