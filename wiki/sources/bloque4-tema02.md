---
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
