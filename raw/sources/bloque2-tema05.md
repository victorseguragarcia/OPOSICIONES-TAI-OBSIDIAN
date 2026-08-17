---
title: "Bloque 2 - Tema 05: Ficheros, Organización y Sistemas de Archivos: FAT32, NTFS, ext4, XFS"
type: "raw-source"
topic: "ficheros-sistemas-archivos"
date: "2026-08-17"
---

# Bloque 2 - Tema 05: Ficheros, Métodos de Organización y Acceso, y Sistemas de Archivos (FAT32, NTFS, ext4, XFS)

## 1. Conceptos Fundamentales de Ficheros
- **Fichero**: Colección estructurada de registros de información relacionada almacenada en un soporte no volátil.
- **Registro Lógico**: Unidad básica de información desde el punto de vista del programa o usuario (conjunto de campos).
- **Registro Físico / Bloque**: Unidad mínima de transferencia de datos entre la memoria secundaria y la memoria principal gestionada por el sistema operativo (típicamente 4096 bytes / 4 KB).
- **Factor de Bloqueo ($Bf$)**: Número de registros lógicos contenidos en un registro físico ($Bf = \lfloor \text{Tamaño Bloque} / \text{Tamaño Registro} \rfloor$).

## 2. Tipos de Organización y Modos de Acceso a Ficheros
- **Organizaciones de Ficheros**:
  1. **Secuencial**: Los registros se almacenan físicamente en el soporte uno a continuación del otro en orden cronológico o por campo clave. Muy eficiente para procesamiento masivo por lotes (*batch*); ineficiente para búsquedas puntuales ($O(n)$).
  2. **Directa / Relativa (Hash / Clave a Dirección)**: La posición física del registro se calcula directamente a partir del valor de su clave mediante una función matemática o tabla de conversión. Permite acceso directo inmediato en $O(1)$ sin leer registros intermedios.
  3. **Indexada / Secuencial-Indexada (ISAM - Indexed Sequential Access Method)**: Combina un área de datos secuencial con uno o más ficheros de índices auxiliares (tablas clave-puntero). Permite tanto el acceso secuencial ordenado como el acceso directo rápido a través del índice.
- **Modos de Acceso**:
  - *Acceso Secuencial*: Lee o escribe los registros en orden estricto de principio a fin.
  - *Acceso Directo / Aleatorio*: Permite posicionar el puntero de lectura/escritura directamente en un registro cualquiera mediante su posición o clave relativa.
  - *Acceso Dinámico*: Capacidad de alternar entre acceso directo para localizar un registro inicial y acceso secuencial a partir de dicho punto.

## 3. Comparativa de Sistemas de Archivos en Sistemas Operativos

### 1. FAT32 (File Allocation Table 32)
- Desarrollado por Microsoft para Windows 95 OSR2. Utiliza una tabla de asignación con entradas de 28 bits efectivos.
- **Límites Críticos**: Tamaño máximo de archivo individual: **4 GB (4.294.967.295 bytes / $2^{32}-1$)**. Tamaño máximo de partición/volumen: **2 TB** (en implementaciones nativas) o 16 TB teóricos.
- Inconvenientes: No tiene soporte de permisos ACL ni seguridad nativa, sin compresión ni cifrado, carece de registro por diario (*journaling*), alta susceptibilidad a la fragmentación.

### 2. NTFS (New Technology File System)
- Sistema de archivos empresarial por defecto de Windows Server y Windows cliente (desde Windows NT).
- **Estructura Interna**: Se basa en la **Tabla Maestra de Archivos (MFT - Master File Table)**, donde cada archivo o carpeta tiene al menos una entrada de 1024 bytes que describe sus atributos y localización de clusters.
- **Características Avanzadas**:
  - **Journaling (Registro por Diario)** mediante el log `$LogFile` para garantizar la integridad de metadatos ante caídas.
  - **Permisos de Seguridad**: Listas de Control de Acceso (ACLs) discrecionales (DACL) y de auditoría (SACL).
  - **Cifrado Transparente**: EFS (*Encrypting File System*).
  - **Compresión de Archivos** nativa en tiempo real.
  - **Cuotas de Disco** por usuario.
  - **Instantáneas en Caliente**: Soporte nativo para VSS (*Volume Shadow Copy Service*).
  - Límites: Tamaño máximo de archivo de **16 TB** (clusters de 4 KB) hasta 8 PB (clusters de 2 MB); volúmenes de hasta 8 PB.

### 3. ext4 (Fourth Extended Filesystem)
- Sistema de archivos estándar en distribuciones GNU/Linux modernas.
- **Estructura Interna de Inodos**: Cada archivo se describe mediante una estructura denominada **Inodo (*index node*)** que contiene los metadatos (tamaño, permisos POSIX, propietario UID/GID, marcas de tiempo atime/mtime/ctime) y punteros a bloques de datos.
- **Características**:
  - **Journaling** configurable en 3 modos: `journal` (datos y metadatos), `ordered` (por defecto, metadatos garantizados tras datos) y `writeback` (solo metadatos).
  - **Extents (Asignación por Extensiones)**: Sustituye los antiguos punteros a bloques indirectos por extensiones (bloque inicial + número de bloques contiguos), reduciendo drásticamente la fragmentación y el tamaño de metadatos para archivos grandes.
  - **Asignación Retardada (*Delayed Allocation / Allocate-on-flush*)**: Optimiza la contigüidad de bloques en memoria antes de escribir en disco.
  - Límites: Tamaño máximo de archivo de **16 TB**; tamaño máximo de volumen de **1 Exabyte (EB)**.

### 4. XFS
- Sistema de archivos de 64 bits de alto rendimiento con registro por diario desarrollado originalmente por Silicon Graphics (SGI) para IRIX y adoptado como sistema de archivos por defecto en Red Hat Enterprise Linux (RHEL) / CentOS desde RHEL 7.
- Diseñado para escalabilidad masiva, gestión de archivos gigantescos y alta concurrencia de operaciones de E/S mediante **Grupos de Asignación (Allocation Groups - AG)** independientes que operan en paralelo.
- Soporta asignación basada en extensiones (*extents*), asignación retardada y defragmentación en línea.
- Límites: Tamaño máximo de archivo y volumen de **8 Exabytes (EB)**.
