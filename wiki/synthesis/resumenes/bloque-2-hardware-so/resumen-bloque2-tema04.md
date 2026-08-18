---
title: "Resumen Exhaustivo Tema 04 (Bloque 2): Sistemas Operativos: Gestión de Procesos, Memoria y Ficheros"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-2
  - tema-04
  - hardware
  - sistemas-operativos
  - bbdd\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema04.md]]"
  - "[[wiki/sources/bloque2-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema05|Tema 05 ➡️]]

# 🔴 Resumen Exhaustivo Tema 04 (Bloque 2): Sistemas Operativos: Gestión de Procesos, Memoria y Ficheros

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 04**
> Arquitectura de SO (Monolítico, Modular, Microkernel, Híbrido), ciclo de vida del proceso (estados y transiciones, PCB), algoritmos de planificación de CPU (FCFS, SJF, SRTF, Round Robin, Prioridades, CFS de Linux), concurrencia y sincronización (Región crítica, Semáforos de Dijkstra, Mutex, Deadlock y Condiciones de Coffman), gestión de memoria (Paginación, Segmentación, Memoria Virtual, Algoritmos de reemplazo de páginas FIFO/LRU/Clock), sistemas de ficheros (FAT32, NTFS, ext4, estructura de Inodos) y permisos Linux (rwx, octal, SUID, SGID, Sticky bit).

---

## 🟣 1. Desarrollo Técnico y Arquitectónico Exhaustivo

### 1. Arquitectura del Sistema Operativo y Gestión de Procesos
- **Tipos de Núcleos (Kernels)**:
  - *Monolítico*: Todos los servicios del SO (gestión de procesos, memoria, drivers de hardware, sistema de ficheros) se ejecutan en el mismo espacio de direcciones del kernel en modo privilegiado (Ring 0). Máximo rendimiento (Linux, Unix BSD clásico, MS-DOS).
  - *Microkernel*: Solo los servicios esenciales mínimos (gestión básica de memoria, planificación y comunicación IPC por paso de mensajes) residen en el kernel; el resto (drivers, sistema de ficheros, red) se ejecutan como procesos servidores en espacio de usuario (*User Space*). Mayor modularidad y tolerancia a fallos a costa de sobrecarga por cambios de contexto (Mach, Minix, QNX).
  - *Híbrido*: Núcleo monolítico con diseño modular y capas de abstracción (Windows NT / 10 / 11, macOS XNU).
- **El Bloque de Control del Proceso (PCB - Process Control Block)**:
  - Estructura de datos que contiene el estado del proceso, PID, contador de programa (PC), registros de la CPU, información de planificación, límites de memoria y tabla de descriptores de ficheros abiertos.
- **Diagrama de Estados del Proceso**:
  - **Nuevo** $
ightarrow$ *Admitido* $
ightarrow$ **Listo (Ready)** $
ightleftharpoons$ *Despachado (Dispatch) / Expiración Quantum* $
ightleftharpoons$ **En Ejecución (Running)** $
ightarrow$ *Espera E/S o evento* $
ightarrow$ **Bloqueado (Waiting)** $
ightarrow$ *Fin de evento* $
ightarrow$ **Listo** $
ightarrow$ *Terminado*.
- **Algoritmos de Planificación de CPU**:
  - *No Apropiativos (Non-Preemptive)*: La CPU no puede ser retirada al proceso hasta que éste termine o se bloquee voluntariamente:
    - **FCFS (First-Come, First-Served)**: Por orden de llegada. Sufre el *efecto convoy* (procesos cortos esperando a uno muy largo).
    - **SJF (Shortest Job First)**: Asigna la CPU al proceso con la ráfaga más corta. Óptimo en tiempo de espera medio, pero puede causar inanición (*starvation*).
  - *Apropiativos (Preemptive)*: El SO puede desalojar el proceso en ejecución mediante interrupciones de reloj:
    - **Round Robin (RR)**: Asigna a cada proceso una rodaja fija de tiempo (**Quantum**). Si el quantum es muy grande degenera a FCFS; si es muy pequeño genera sobrecarga excesiva por cambios de contexto.
    - **SRTF (Shortest Remaining Time First)**: Versión apropiativa de SJF.
    - **CFS (Completely Fair Scheduler)**: Planificador estándar de Linux basado en un árbol rojinegro (*Red-Black Tree*) que equilibra el tiempo de ejecución virtual (`vruntime`) de los procesos.

### 2. Concurrencia, Sincronización y Bloqueo Mutuo (Deadlock)
- **Problema de la Sección Crítica**: Exige cumplir 3 condiciones: **Exclusión Mutua** (solo un proceso a la vez en su sección crítica), **Progreso** (la decisión de entrada no se pospone indefinidamente) y **Espera Limitada** (no inanición).
- **Mecanismos de Sincronización**:
  - *Mutex (Mutual Exclusion)*: Cerrojo binario (bloqueado/desbloqueado) con concepto de propiedad (solo el hilo que adquiere el cerrojo puede liberarlo).
  - *Semáforos de Dijkstra*: Variable entera protegida accesible solo mediante dos operaciones atómicas:
    - `wait(S)` o `P(S)`: Decrementa $S$. Si $S < 0$, el proceso se bloquea.
    - `signal(S)` o `V(S)`: Incrementa $S$. Si hay procesos bloqueados, desbloquea uno.
- **Las Cuatro Condiciones de Coffman para el Bloqueo Mutuo (Deadlock)**:
  Para que se produzca un interbloqueo deben cumplirse **simultáneamente las 4 condiciones**:
  1. **Exclusión Mutua**: Al menos un recurso no compartible.
  2. **Retención y Espera (Hold and Wait)**: Un proceso retiene recursos mientras espera otros adicionales.
  3. **No Apropiación (No Preemption)**: Los recursos no pueden ser confiscados por la fuerza.
  4. **Espera Circular**: Existe una cadena cerrada de procesos $\{P_0, P_1, \dots, P_n\}$ donde cada $P_i$ espera un recurso retenido por $P_{i+1}$.
  - *Prevención/Evitación*: Romper al menos 1 condición o usar el **Algoritmo del Banquero de Dijkstra**.

### 3. Gestión de Memoria y Memoria Virtual
- **Paginación**: División de la memoria física en marcos (*frames*) de tamaño fijo y de la memoria lógica en páginas del mismo tamaño. Elimina la fragmentación externa, aunque produce **fragmentación interna** en la última página.
  - *MMU (Memory Management Unit)*: Traduce direcciones lógicas a físicas mediante la **Tabla de Páginas**.
  - *TLB (Translation Lookaside Buffer)*: Caché hardware de alta velocidad que almacena las traducciones recientes de páginas para evitar accesos repetidos a RAM.
- **Segmentación**: División de la memoria en bloques lógicos de tamaño variable (código, datos, pila). Produce **fragmentación externa** (solucionada mediante compactación).
- **Algoritmos de Reemplazo de Páginas (Fallo de Página)**:
  - **FIFO**: Reemplaza la página más antigua en memoria. Puede sufrir la **Anomalía de Bélády** (aumentar el número de marcos de memoria asignados produce MÁS fallos de página).
  - **Óptimo (OPT / MIN)**: Reemplaza la página que no será usada en el periodo más largo de tiempo en el futuro (teórico, inalcanzable en la práctica).
  - **LRU (Least Recently Used)**: Reemplaza la página que no ha sido referenciada durante más tiempo en el pasado. No sufre la anomalía de Bélády.
  - **Algoritmo del Reloj (Segunda Oportunidad)**: Aproximación eficiente a LRU mediante un bit de referencia.
  - **Hiperpaginación (Thrashing)**: Situación crítica donde el SO pasa más tiempo intercambiando páginas entre RAM y Swap que ejecutando instrucciones reales.

### 4. Sistemas de Ficheros y Permisos Linux
- **Estructuras de Sistemas de Ficheros**:
  - *FAT32*: Tabla de asignación de ficheros de 32 bits. Límite máximo de tamaño de fichero: **4 GB (menos 1 byte)**; tamaño máximo de volumen: 2 TB.
  - *NTFS*: Sistema transaccional de Windows con **MFT (Master File Table)**, journaling, permisos ACL, compresión y cifrado EFS.
  - *ext4 (Linux)*: Sistema con journaling, soporte de extents y asignación retardada.
- **Estructura del Inodo en Linux**:
  - Almacena todos los metadatos del fichero (tamaño, propietario, permisos, timestamps) y los punteros a bloques de datos: **12 punteros directos**, **1 puntero indirecto simple**, **1 puntero indirecto doble** y **1 puntero indirecto triple**. ❌ **El inodo NO contiene el nombre del archivo** (el nombre se almacena en el directorio).
- **Permisos UNIX/Linux y Bits Especiales**:

| Permiso / Bit Especial | Notación Simbólica | Valor Octal | Efecto en Ficheros | Efecto en Directorios |
|:---|:---:|:---:|:---|:---|
| **Lectura** | `r` | **4** | Permite leer el contenido. | Permite listar el contenido (`ls`). |
| **Escritura** | `w` | **2** | Permite modificar el contenido. | Permite crear o borrar ficheros dentro del directorio. |
| **Ejecución** | `x` | **1** | Permite ejecutar como programa/script. | Permite entrar al directorio (`cd`) y acceder a sus ficheros. |
| **SUID (SetUID)** | `s` (en usuario) | **4000** | El archivo se ejecuta con los privilegios del **propietario** del archivo (ej. `/usr/bin/passwd`). | Sin efecto estándar en la mayoría de Linux. |
| **SGID (SetGID)** | `s` (en grupo) | **2000** | El archivo se ejecuta con los privilegios del **grupo propietario**. | Los nuevos archivos creados dentro **heredan automáticamente el grupo** del directorio. |
| **Sticky Bit** | `t` (en otros) | **1000** | Sin efecto estándar. | **Solo el propietario del archivo (o root) puede borrarlo o renombrarlo** dentro del directorio (ej. `/tmp` - permisos `1777`). |

- **Cálculo de Umask**: Define los permisos por defecto restando la máscara a los permisos base:
  - Permiso base directorios: `777` ($rwxrwxrwx$). Con `umask 022` $
ightarrow$ `755` ($rwxr-xr-x$). Con `umask 027` $
ightarrow$ `750` ($rwxr-x---$).
  - Permiso base ficheros: `666` ($rw-rw-rw-$). Con `umask 022` $
ightarrow$ `644` ($rw-r--r--$). Con `umask 027` $
ightarrow$ `640` ($rw-r-----).

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 04 (Bloque 2)**
> 1. **Contenido del Inodo en Linux**: El inodo contiene permisos, propietario, tamaño y punteros a bloques, pero **NUNCA contiene el nombre del fichero** (se guarda en la tabla del directorio).
> 2. **Límite de Fichero en FAT32**: Es de **4 GB** (exactamente $4 \text{ GiB} - 1 \text{ byte} = 4.294.967.295 \text{ bytes}$).
> 3. **Anomalía de Bélády**: Afecta exclusivamente a algoritmos como **FIFO** (donde dar más memoria puede aumentar los fallos de página). Algoritmos de pila como **LRU y Óptimo NUNCA sufren esta anomalía**.
> 4. **Sticky Bit (Valor Octal 1000)**: En directorios como `/tmp` impide que un usuario borre archivos de otros usuarios aunque tenga permisos de escritura en el directorio.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Bits Especiales**: **SUID 4 / SGID 2 / Sticky 1** (Suma octal: $4+2+1=7$).
> - **Permisos R-W-X**: **Read $=4$, Write $=2$, eXecute $=1$** ($rwx = 4+2+1=7$).
> - **Condiciones Deadlock de Coffman**: **EX-RE-NO-CIR** $
ightarrow$ **EX**clusión mutua, **RE**tención y espera, **NO** apropiación, espera **CIR**cular.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque2-tema04|Fuente Oficial del Tema 04]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema04-sistemas-operativos|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque 2**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|⬅️ Tema 03]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema05|Tema 05 ➡️]]
