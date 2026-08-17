# -*- coding: utf-8 -*-
r"""
Script para adaptar y enriquecer toda la base de conocimiento del Bloque 2 (Tecnología Básica)
a partir de los 5 PDFs oficiales (UD011929 a UD012106).
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

WIKI_SOURCES_B2 = {
    "wiki/sources/bloque2-tema01.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema01
  - representacion-informacion
  - von-neumann
  - ieee-754
  - complemento-a-dos
  - unicode
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Informática Básica y Representación"
  - "bloque2-tema01"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema01-informatica-basica-representacion.md|bloque2-tema01-informatica-basica-representacion.md]] (88 páginas).

---

## 📖 1. Unidades de Medida y Sistemas de Numeración

- **Unidades de Medida (SI vs IEC)**:
  - Sistema Internacional (decimal): $1\text{ KB} = 10^3 = 1.000\text{ bytes}$, $1\text{ MB} = 10^6\text{ bytes}$, $1\text{ GB} = 10^9\text{ bytes}$.
  - Estándar IEC (binario): $1\text{ KiB} = 2^{10} = 1.024\text{ bytes}$, $1\text{ MiB} = 2^{20}\text{ bytes}$, $1\text{ GiB} = 2^{30}\text{ bytes}$, $1\text{ TiB} = 2^{40}\text{ bytes}$.
- **Sistemas de Numeración**: Binario (base 2), Octal (base 8: grupos de 3 bits), Decimal (base 10) y Hexadecimal (base 16: grupos de 4 bits).

---

## 🟣 2. Representación de Datos: Enteros y Coma Flotante

### A. Representación de Enteros con Signo ($n$ bits):
1. **Signo y Magnitud (SM)**: Bit más significativo (MSB) para el signo ($0$ positivo, $1$ negativo). Rango: $[-(2^{n-1}-1), +(2^{n-1}-1)]$. Doble cero ($+0$ y $-0$).
2. **Complemento a 1 (C1)**: Se invierten todos los bits para números negativos. Doble cero ($+0$ y $-0$).
3. **Complemento a 2 (C2)**: Estándar universal. Se calcula invirtiendo los bits y sumando $1$ ($\text{C2}(x) = \overline{x} + 1 = 2^n - |x|$).
   - Rango: $[-2^{n-1}, +(2^{n-1}-1)]$. **Cero único** ($00...0$). Para 8 bits: $[-128, +127]$.

### B. Coma Flotante Estándar IEEE 754:
$$N = (-1)^S \times 1.M \times 2^{E - \text{Sesgo}}$$
- **Simple Precisión (32 bits)**: 1 bit de signo ($S$), **8 bits de exponente ($E$)** con sesgo **127**, y **23 bits de mantisa ($M$)**.
- **Doble Precisión (64 bits)**: 1 bit de signo ($S$), **11 bits de exponente ($E$)** con sesgo **1023**, y **52 bits de mantisa ($M$)**.
- **Valores Especiales**:
  - Exponente todo 1s y Mantisa 0: **$\pm\infty$** (Infinito).
  - Exponente todo 1s y Mantisa $\ne 0$: **NaN** (*Not a Number*).
  - Exponente todo 0s y Mantisa $\ne 0$: **Números desnormalizados** (sin el 1 implícito).

---

## 🔵 3. Codificación de Caracteres

- **ASCII (7 bits)**: 128 caracteres (0 a 127). Códigos de control 0 a 31; 'A' = 65 (0x41), 'a' = 97 (0x61), '0' = 48 (0x30).
- **ASCII Extendido / ISO 8859-1 (Latin-1 - 8 bits)**: 256 caracteres para lenguas de Europa occidental (incluye 'ñ', 'ç', vocales con tilde).
- **ISO 8859-15 (Latin-9)**: Reemplaza caracteres poco usados de ISO 8859-1 para incorporar el símbolo del **Euro (€)** y las letras 'Š', 'š', 'Ž', 'ž', 'Œ', 'œ', 'Ÿ'.
- **Unicode**:
  - **UTF-8**: Longitud variable (1 a 4 bytes). Totalmente compatible hacia atrás con ASCII (los primeros 128 caracteres ocupan 1 byte).
  - **UTF-16**: Longitud variable (2 o 4 bytes mediante pares sustitutos / *surrogates*).
  - **UTF-32**: Longitud fija de 4 bytes (32 bits) por carácter.

---

## 🔵 4. Arquitectura de Computadores (Von Neumann vs Harvard)

- **Von Neumann**: Memoria unificada para instrucciones de programa y datos. Un único bus compartido genera el **cuello de botella de Von Neumann**.
- **Harvard**: Memorias y buses físicos separados para instrucciones y datos (permite lecturas simultáneas).
- **Componentes CPU**:
  - **Unidad de Control (UC)**: Contador de Programa (PC), Registro de Instrucción (RI), Decodificador, Reloj.
  - **Unidad Aritmético-Lógica (ALU)**: Operaciones lógicas y aritméticas, Acumulador, Registro de Estado (*Flags*).
  - **Buses del Sistema**: Bus de Datos (bidireccional), Bus de Direcciones (unidireccional desde CPU hacia memoria/periféricos) y Bus de Control.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica de Examen |
|----------|----------------------------------|
| **Rango C2 en 8 bits** | **$-128$ a $+127$** ($-128$ se representa como `10000000`) |
| **Sesgo IEEE 754 32 bits** | **127** ($2^{8-1} - 1$) \| 64 bits: **1023** ($2^{11-1} - 1$) |
| **UTF-8 Longitud** | **1 a 4 bytes** (compatible con ASCII en el byte 1) |
| **Bus de Direcciones** | Si el bus tiene $N$ líneas, puede direccionar un espacio de memoria de $2^N$ posiciones. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/cpu-architecture-von-neumann|Arquitectura de CPU Von Neumann y Harvard]]
- Entidad: [[wiki/entities/ieee-754-floating-point|Estándar IEEE 754 de Coma Flotante]]
- Entidad: [[wiki/entities/character-encoding-unicode-utf8|Codificación de Caracteres: ASCII, ISO 8859 y Unicode]]
- Concepto: [[wiki/concepts/two-complement-and-binary-arithmetic|Complemento a Dos y Aritmética Binaria]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de IEEE 754 y Representación Binaria]]
""",

    "wiki/sources/bloque2-tema02.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 02 (UD012103): Periféricos, Conectividad, Puertos Físicos y Buses de Expansión"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema02
  - perifericos
  - usb
  - pcie
  - nvme
  - puertos
  - dma
  - interrupciones
sources:
  - "raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Periféricos e Interfaces"
  - "bloque2-tema02"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 02 (UD012103): Periféricos, Conectividad, Puertos Físicos y Buses de Expansión

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md|bloque2-tema02-perifericos-conectividad-interfaces.md]] (112 páginas).

---

## 📖 1. Clasificación de Periféricos y Mecanismos de Entrada/Salida

- **Clasificación Funcional**:
  - **Entrada**: Teclados, ratones, escáneres ópticos, digitalizadores biométricos, lectores de tarjetas inteligentes.
  - **Salida**: Monitores (CRT, LCD, LED, OLED con conexiones HDMI, DisplayPort, DVI, VGA), impresoras (láser electrofotográficas, inyección de tinta, matriciales de impacto, térmicas), trazadores gráficos (*plotters*).
  - **Entrada/Salida (Mixtos)**: Pantallas táctiles, tarjetas de sonido, tarjetas de red, módems.
  - **Almacenamiento**: Discos magnéticos (HDD), discos de estado sólido (SSD SATA / NVMe), cintas magnéticas LTO, discos ópticos (CD, DVD, Blu-ray).
- **Mecanismos de Transferencia de E/S**:
  1. **E/S Programada**: La CPU comprueba continuamente mediante sondeo (*polling*) el estado del periférico (alto consumo de CPU).
  2. **E/S por Interrupciones**: El periférico genera una señal hardware (**IRQ**) cuando está listo para transferir datos, interrumpiendo a la CPU.
  3. **Acceso Directo a Memoria (DMA - Direct Memory Access)**: Un controlador DMA transfiere bloques enteros de datos entre el periférico y la memoria principal sin intervención de la CPU, avisando al finalizar mediante una interrupción.

---

## 🟣 2. Puertos Físicos y Estándares de Conectividad Externa

| Puerto / Estándar | Norma / Especificación | Velocidad Máxima de Transferencia | Conectores / Características |
|-------------------|------------------------|-----------------------------------|------------------------------|
| **Puerto Serie** | **RS-232C** / EIA-232 | Hasta 115.2 kbps (asíncrono) | Conector DB-9 o DB-25 |
| **Puerto Paralelo** | **IEEE 1284** / Centronics | Hasta 2 MB/s (modo ECP / EPP) | Conector DB-25 / Centronics 36 pines |
| **PS/2** | Mini-DIN 6 pines | Puerto serie síncrono dedicado | Verde para ratón, Morado para teclado |
| **USB 1.1** | Full Speed | **12 Mbps** (1.5 Mbps en Low Speed) | Conectores Tipo A y Tipo B |
| **USB 2.0** | High Speed | **480 Mbps** (60 MB/s) | Incorpora conector Mini-USB y Micro-USB |
| **USB 3.0 (USB 3.1 Gen 1)** | SuperSpeed | **5 Gbps** (~500 MB/s) | Conectores azulados; añade 5 pistas extra |
| **USB 3.1 Gen 2 (USB 3.2 Gen 2x1)** | SuperSpeed+ | **10 Gbps** (~1.2 GB/s) | Conector **USB Type-C** reversible |
| **USB 3.2 Gen 2x2** | SuperSpeed+ Dual-Lane | **20 Gbps** (usando dos carriles Tipo-C) | Solo conector USB Type-C |
| **USB4** | Basado en Thunderbolt 3 | **40 Gbps** (con entrega de energía USB-PD 100W/240W) | Conector USB Type-C |
| **FireWire 400** | **IEEE 1394a** | **400 Mbps** | 6 pines (con alimentación) o 4 pines |
| **FireWire 800** | **IEEE 1394b** | **800 Mbps** | 9 pines bilingüe |
| **Thunderbolt 3 / 4** | Intel / Apple | **40 Gbps** (soporta PCIe 3.0 x4 + DisplayPort) | Conector USB Type-C |

---

## 🔵 3. Buses Internos de Expansión: PCI Express y NVMe

- **PCI Express (PCIe)**: Arquitectura serie punto a punto basada en carriles (*lanes* $x1, x4, x8, x16$ full-duplex con codificación 8b/10b o 128b/130b):
  - **PCIe 3.0**: ~1 GB/s por carril ($\approx 16\text{ GB/s}$ en $x16$).
  - **PCIe 4.0**: ~2 GB/s por carril ($\approx 32\text{ GB/s}$ en $x16$).
  - **PCIe 5.0**: ~4 GB/s por carril ($\approx 64\text{ GB/s}$ en $x16$).
- **Protocolo NVMe (Non-Volatile Memory Express)**:
  - Diseñado específicamente para almacenamiento SSD sobre bus PCIe (reemplazando el cuello de botella del protocolo AHCI sobre SATA).
  - Soporta hasta **64.000 colas de comandos**, con hasta **64.000 comandos por cola** en paralelo.

---

## 🎯 Datos Clave para Oposiciones TAI

| Puerto / Protocolo | Dato Clave de Examen |
|-------------------|----------------------|
| **Velocidad USB 2.0 vs 3.0** | USB 2.0 = **480 Mbps** \| USB 3.0 = **5 Gbps** \| USB4 = **40 Gbps** |
| **IEEE 1394** | Nombre oficial del estándar **FireWire** |
| **IEEE 1284** | Nombre oficial del estándar de **Puerto Paralelo (Centronics/ECP/EPP)** |
| **Ventaja de NVMe sobre AHCI** | Permite 64.000 colas paralelas (frente a 1 única cola de 32 comandos en AHCI/SATA) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|Interfaces y Periféricos: USB, PCIe, NVMe y Thunderbolt]]
- Síntesis: [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos, Interfaces y Buses]]
""",

    "wiki/sources/bloque2-tema03.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Algoritmos"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema03
  - estructuras-datos
  - arboles-avl
  - grafos
  - algoritmos-ordenacion
  - organizacion-ficheros
  - big-o
sources:
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Estructuras de Datos y Ficheros"
  - "bloque2-tema03"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Algoritmos

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md|bloque2-tema03-estructuras-ficheros-algoritmos.md]] (99 páginas).

---

## 📖 1. Estructuras de Datos Lineales y No Lineales

- **Estructuras Lineales**:
  - **Arrays (Vectores/Matrices)**: Colección contigua en memoria con acceso aleatorio en tiempo constante $O(1)$.
  - **Listas Enlazadas**: Nodos enlazados por punteros (simples, dobles, circulares). Inserción/borrado en $O(1)$ conocida la posición; búsqueda en $O(n)$.
  - **Pilas (Stack - LIFO)**: *Last-In, First-Out*. Operaciones `push`, `pop`, `peek` en $O(1)$.
  - **Colas (Queue - FIFO)**: *First-In, First-Out*. Operaciones `enqueue`, `dequeue` en $O(1)$.
- **Estructuras No Lineales**:
  - **Árboles Binarios de Búsqueda (BST)**: El subárbol izquierdo contiene valores menores y el derecho mayores. Búsqueda en promedio $O(\log n)$, peor caso $O(n)$ si está desbalanceado.
  - **Árboles AVL**: BST auto-balanceados donde la diferencia de alturas entre subárboles (Factor de Equilibrio $FE = h_d - h_i$) pertenece a $\{-1, 0, +1\}$. Balanceo mediante 4 tipos de rotaciones: Simple Izquierda (LL), Simple Derecha (RR), Doble Izquierda-Derecha (LR) y Doble Derecha-Izquierda (RL). Búsqueda garantizada en $O(\log n)$.
  - **Árboles B / B+**: Árboles multicamino balanceados diseñados para almacenamiento secundario e índices de bases de datos.
  - **Grafos**: Nodos (Vértices) y Aristas (dirigidas o no dirigidas, ponderadas). Representación mediante **Matriz de Adyacencia** (espacio $O(V^2)$, eficiente para grafos densos) o **Listas de Adyacencia** (espacio $O(V + E)$, eficiente para grafos dispersos).

---

## 🟣 2. Complejidad Algorítmica y Algoritmos de Ordenación

| Algoritmo | Mejor Caso | Caso Medio | Peor Caso | Complejidad Espacial | Estable | Método / Estrategia |
|-----------|------------|------------|-----------|----------------------|---------|---------------------|
| **Burbuja (Bubble Sort)** | $O(n)$ (optimizado) | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Intercambio directo |
| **Inserción Directa** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Inserción ordenada |
| **Selección Directa** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | NO | Búsqueda del mínimo |
| **Quicksort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ (pivote malo) | $O(\log n)$ | NO | Divide y Vencerás (partición) |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **SÍ** | Divide y Vencerás (mezcla) |
| **Heapsort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | NO | Estructura Montículo (*Heap*) |
| **Búsqueda Lineal** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | - | Recorrido secuencial |
| **Búsqueda Binaria** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | - | Divide y Vencerás (requiere array ordenado) |

---

## 🔵 3. Tipos y Métodos de Organización de Ficheros

- **Estructura**: Registros lógicos (unidad de información de la aplicación) agrupados en **registros físicos o bloques** (unidad de transferencia de E/S con factor de bloqueo $FB = \text{Tamaño Bloque} / \text{Tamaño Registro}$).
- **Métodos de Organización**:
  1. **Secuencial**: Los registros se graban uno tras otro. Búsqueda secuencial $O(n)$. Rápido para procesamiento por lotes (*batch*); ineficiente para acceso aleatorio.
  2. **Secuencial Encadenado**: Los registros se enlazan mediante punteros físicos.
  3. **Secuencial Indexado (ISAM)**: Área de datos secuencial + Área de índices ordenada por clave + Área de desbordamiento (*overflow*). Permite acceso tanto secuencial como directo en $O(\log n)$.
  4. **Directa / Aleatoria (Hash / Direccionamiento Calculado)**: La posición física en disco se calcula mediante una función matemática de dispersión $H(\text{clave})$.
     - **Resolución de Colisiones**: Direccionamiento abierto (prueba lineal/cuadrática, doble hashing) o encadenamiento separado en listas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Pregunta / Concepto | Respuesta / Especificación |
|---------------------|---------------------------|
| **Factor de Equilibrio AVL** | $FE = \text{Altura(Derecho)} - \text{Altura(Izquierdo)} \in \{-1, 0, +1\}$ |
| **Peor caso de Quicksort** | **$O(n^2)$** cuando el array está ordenado y se elige el primer/último elemento como pivote |
| **Algoritmo de ordenación con $O(n \log n)$ garantizado y estable** | **Mergesort** (a costa de $O(n)$ de memoria auxiliar) |
| **Condición de Búsqueda Binaria** | La colección debe estar previamente **ordenada** y permitir **acceso aleatorio** ($O(1)$). |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/data-structures-trees-and-graphs|Estructuras de Datos: Árboles AVL, B-Trees y Grafos]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación, Búsqueda y Complejidad]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Computacional y Notación Big-O]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización y Métodos de Acceso a Ficheros]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Algoritmos de Ordenación y Complejidad]]
""",

    "wiki/sources/bloque2-tema04.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Gestión de Procesos, Memoria y Sistemas de Archivos"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema04
  - sistemas-operativos
  - procesos
  - planificacion-cpu
  - memoria-virtual
  - deadlocks
  - sistemas-archivos
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Sistemas Operativos y Procesos"
  - "bloque2-tema04"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Gestión de Procesos, Memoria y Sistemas de Archivos

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md|bloque2-tema04-sistemas-operativos-procesos-memoria.md]] (122 páginas).

---

## 📖 1. Arquitectura del Sistema Operativo y Estados del Proceso

- **Modos de Ejecución**: **Modo Kernel / Supervisor** (acceso total al hardware e instrucciones privilegiadas) vs **Modo Usuario** (ejecución restringida mediante llamadas al sistema / *system calls*).
- **Estructura del Proceso**: Representado en el SO por el **Bloque de Control de Proceso (PCB / Task Struct)** que almacena: PID, Estado, Contador de Programa (PC), Registros de CPU, Información de Gestión de Memoria y Descriptores de Ficheros abiertos.
- **Transiciones de Estados**:
  - `Nuevo` $\rightarrow$ `Listo (Ready)`: Admitido a la cola de listos.
  - `Listo` $\rightarrow$ `Ejecutando (Running)`: Seleccionado por el planificador de CPU (*Dispatcher*).
  - `Ejecutando` $\rightarrow$ `Listo`: Por expiración de quantum de tiempo (interrupción de reloj).
  - `Ejecutando` $\rightarrow$ `Bloqueado (Waiting)`: Por espera de una operación de E/S o evento.
  - `Bloqueado` $\rightarrow$ `Listo`: Al completarse la operación de E/S.
  - `Ejecutando` $\rightarrow$ `Terminado`: Fin de ejecución (liberación de recursos).

---

## 🟣 2. Algoritmos de Planificación de CPU y Bloqueos Mutuos (Deadlocks)

### A. Algoritmos de Planificación de CPU:
1. **FCFS (First-Come, First-Served)**: No apropiativo. Sufre el *efecto convoy* ante ráfagas largas de CPU.
2. **SJF (Shortest Job First)**: Óptimo en tiempo medio de espera. Versión apropiativa: **SRTF (Shortest Remaining Time First)**.
3. **Round Robin (RR)**: Apropiativo con rodaja de tiempo o **quantum ($q$)**. Si $q$ es muy grande degenera en FCFS; si $q$ es muy pequeño la sobrecarga por cambio de contexto es excesiva.
4. **Colas Multinivel con Realimentación (MLFQ)**: Múltiples colas con prioridades dinámicas según el comportamiento de la ráfaga de CPU.

### B. Interbloqueos (Deadlocks):
- **Las 4 Condiciones Necesarias de Coffman**:
  1. *Exclusión Mutua*: Al menos un recurso no compartible.
  2. *Retención y Espera (Hold and Wait)*: Un proceso retiene recursos mientras espera otros.
  3. *No Apropiación (No Preemption)*: Los recursos no pueden ser arrebatados forzosamente.
  4. *Espera Circular*: Existe una cadena de procesos $\{P_0, P_1, ..., P_n\}$ donde $P_0$ espera un recurso de $P_1$, etc.
- **Tratamiento**:
  - *Prevención*: Invalidar al menos una de las 4 condiciones de Coffman.
  - *Evasión*: **Algoritmo del Banquero de Dijkstra** (asegurar estados siempre seguros).
  - *Detección y Recuperación*: Algoritmo de grafo de asignación de recursos y terminación forzosa de procesos.

---

## 🔵 3. Gestión de Memoria Virtual y Algoritmos de Reemplazo

- **Paginación**: División del espacio lógico en **Páginas** de tamaño fijo ($4\text{ KB}$) y la memoria física en **Marcos de Página (*Frames*)**.
  - **Tabla de Páginas**: Traduce dirección lógica (número de página + desplazamiento) a física.
  - **TLB (Translation Lookaside Buffer)**: Caché hardware asociativa para acelerar la traducción de direcciones.
- **Algoritmos de Reemplazo de Páginas**:
  - **FIFO**: Reemplaza la página más antigua (puede sufrir la **Anomalía de Belady**: más marcos asignados provocan más fallos de página).
  - **LRU (Least Recently Used)**: Reemplaza la página que no ha sido usada durante más tiempo.
  - **Óptimo de Belady (OPT)**: Reemplaza la página que tardará más tiempo en ser usada en el futuro (teórico).
  - **Reloj (Segunda Oportunidad)**: Aproximación a LRU mediante un bit de referencia.
- **Hiperpaginación (*Thrashing*)**: El sistema pasa más tiempo intercambiando páginas entre RAM y disco que ejecutando instrucciones útiles.

---

## 🔵 4. Comparativa de Sistemas de Archivos

| Sistema de Archivos | Tamaño Máximo de Archivo | Tamaño Máximo de Volumen | Características Clave de Examen |
|---------------------|--------------------------|--------------------------|---------------------------------|
| **FAT32** | **4 GB** ($2^{32}-1\text{ bytes}$) | **2 TB** (8 TB teórico) | Sin permisos avanzados, sin journaling, máxima compatibilidad |
| **exFAT** | 16 EB | 128 PB | Diseñado para memorias flash extraíbles |
| **NTFS** | **16 TB** (hasta 8 PB en Win10/Srv) | 256 TB | **Journaling**, permisos **ACLs**, compresión, cifrado nativo **EFS**, cuotas |
| **ext4** | **16 TB** | **1 EB** | **Journaling** (Journal, Ordered, Writeback), asignación multiloque (*Extents*), inodos |
| **XFS** | 8 EB | 8 EB | Sistema de archivos transaccional de 64 bits de alto rendimiento en Linux |
| **Btrfs / ZFS** | 16 EB | 16 EB / 256 ZiB | Copy-on-Write (CoW), snapshots instantáneas, RAID integrado, autorreparación |

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| **Límite de archivo FAT32** | **4 GB** (si se intenta copiar un archivo $>4\text{ GB}$ da error) |
| **Anomalía de Belady** | Fenómeno donde aumentar el número de marcos de memoria física incrementa el número de fallos de página (ocurre en **FIFO**). |
| **Condiciones de Coffman** | **4 condiciones simultáneas** para que ocurra un Deadlock. |
| **Journaling** | Registro de transacciones previas a la escritura para garantizar la recuperación rápida tras fallos de energía. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU]]
- Entidad: [[wiki/entities/process-synchronization-and-deadlocks|Sincronización de Procesos, Condiciones de Coffman y Deadlocks]]
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual, Paginación y Algoritmos de Reemplazo]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos: FAT32, NTFS, ext4, XFS y Btrfs]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual y Algoritmos de Paginación]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
""",

    "wiki/sources/bloque2-tema05.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 05 (UD012106): Sistemas Gestores de Bases de Datos, NoSQL y Teorema CAP"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema05
  - sgbd
  - rdbms
  - nosql
  - teorema-cap
  - base-model
  - big-data
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen SGBD, NoSQL y Teorema CAP"
  - "bloque2-tema05"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 05 (UD012106): Sistemas Gestores de Bases de Datos, NoSQL y Teorema CAP

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md|bloque2-tema05-sgbd-relacionales-nosql-cap.md]] (46 páginas).

---

## 📖 1. Arquitectura y Componentes de un SGBD

Un Sistema Gestor de Bases de Datos (SGBD / DBMS) proporciona una interfaz unificada entre los usuarios/aplicaciones y los datos físicos almacenados.
- **Componentes Principales**:
  1. **Motor de Almacenamiento (*Storage Engine*)**: Gestiona la asignación de espacio en disco, buffers en RAM y estructuras de datos de bajo nivel.
  2. **Procesador y Optimizador de Consultas**: Traduce las sentencias SQL en un árbol algebraico relacional y selecciona el plan de ejecución de menor coste (**CBO - Cost-Based Optimizer**).
  3. **Gestor de Transacciones y Recuperación**: Garantiza las propiedades **ACID** mediante el registro de transacciones (*Write-Ahead Logging* / WAL).
  4. **Gestor de Concurrencia y Bloqueos**: Controla el acceso simultáneo mediante bloqueos compartidos (S) y exclusivos (X) y control de versiones multi-versión (**MVCC**).
  5. **Diccionario de Datos / Catálogo del Sistema**: Almacena metadatos (definiciones de tablas, columnas, índices, vistas, permisos).

---

## 🟣 2. Clasificación de SGBD: Relacionales, Orientados a Objetos y NoSQL

- **Relacionales (RDBMS)**: Basados en el modelo de Codd y álgebra relacional (PostgreSQL, Oracle, MySQL, SQL Server, MariaDB).
- **Orientados a Objetos (OODBMS)**: Almacenan objetos complejos de forma nativa sin necesidad de mapeo relacional (estándar ODMG).
- **Objeto-Relacionales (ORDBMS)**: Híbridos que combinan el modelo relacional con tipos de datos definidos por el usuario, herencia y métodos (PostgreSQL, Oracle).
- **NoSQL (*Not Only SQL*)**: Diseñados para escalabilidad horizontal en clústeres distribuidos, alta velocidad y esquemas flexibles/dinámicos (*Schema-less*).

---

## 🔵 3. El Teorema CAP de Brewer y el Modelo BASE

### A. Teorema CAP (Eric Brewer, 2000):
En cualquier sistema de datos distribuido, es imposible garantizar simultáneamente las tres propiedades:
1. **Consistencia (C - Consistency)**: Todos los nodos ven exactamente los mismos datos en el mismo instante.
2. **Disponibilidad (A - Availability)**: Cada petición no fallida recibe una respuesta (sin garantía de ser la más reciente).
3. **Tolerancia a Particiones (P - Partition Tolerance)**: El sistema sigue funcionando a pesar de la pérdida o retraso de mensajes entre nodos.

> [!important]
> Como las redes reales siempre pueden sufrir particiones ($P$), los sistemas distribuidos deben elegir entre **Consistencia y Partición (CP)** o **Disponibilidad y Partición (AP)**.

```
                          TEOREMA CAP DE BREWER
                                    ▲
                                   / \
                                  /   \
                                 /  P  \  (Tolerancia a Particiones)
                                /       \
                               /         \
                              /  HBase    \
                             /   MongoDB   \
                            /     Redis     \
                           /                 \
                          / CP             AP \
                         /                     \
       (Consistencia)   /                       \   (Disponibilidad)
               C <─────────────────────────────────> A
                    \                             /
                     \           CA              /
                      \     PostgreSQL, MySQL   /
                       \     Oracle, SQL Server/
                        ───────────────────────
```

### B. Modelo BASE frente a ACID:
- **ACID** (RDBMS tradicionales): *Atomicity, Consistency, Isolation, Durability* (Consistencia inmediata y estricta).
- **BASE** (Sistemas NoSQL distribuidos):
  - **Basically Available**: Disponibilidad básica del sistema garantizada.
  - **Soft state**: El estado del sistema puede cambiar con el tiempo sin interacción del usuario.
  - **Eventual consistency**: Consistencia eventual (los datos convergen a un estado coherente tras un periodo de tiempo).

---

## 🔵 4. Familias de Bases de Datos NoSQL

| Familia NoSQL | Modelo de Datos | Casos de Uso Típicos | Tecnologías Líderes |
|---------------|-----------------|----------------------|---------------------|
| **Clave-Valor (*Key-Value*)** | Pares clave-valor opacos; acceso ultrarrápido por clave | Cachés de sesión, carritos de compra, contadores | **Redis**, **Memcached**, AWS DynamoDB |
| **Documentales (*Document-Store*)** | Documentos semiestructurados jerárquicos (**JSON**, **BSON**, XML) | Catálogos de productos, CMS, perfiles de usuario | **MongoDB**, **CouchDB** |
| **Columnas Anchas (*Column-Family*)** | Tablas bidimensionales dispersas orientadas a columnas | Análisis de series temporales, telemetría, IoT | **Apache Cassandra**, **Apache HBase**, Google Bigtable |
| **Grafos (*Graph Databases*)** | Nodos (entidades), Relaciones (aristas con propiedades) | Redes sociales, detección de fraude, motores de recomendación | **Neo4j**, Amazon Neptune |

---

## 🎯 Datos Clave para Oposiciones TAI

| Pregunta / Concepto | Respuesta de Examen |
|---------------------|---------------------|
| **Elección en Teorema CAP** | En sistemas distribuidos, ante una partición de red se elige entre **CP** (Consistencia) o **AP** (Disponibilidad). |
| **MongoDB y BSON** | MongoDB almacena internamente los documentos en formato **BSON** (Binary JSON). |
| **Cassandra** | Base de datos NoSQL columnar distribuida orientada a **AP** (Alta disponibilidad y consistencia eventual). |
| **Redis** | Base de datos clave-valor en memoria RAM de altísimo rendimiento con soporte de estructuras complejas. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL, Familias y Teorema CAP]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP de Brewer y Modelo BASE]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía de Familias NoSQL y Teorema CAP]]
- Síntesis: [[wiki/synthesis/bloque2-tai-oposiciones-master-guide|Guía Maestra de Bloque 2: Tecnología Básica (TAI)]]
"""
}

print("[*] Escribiendo 5 notas fuente adaptadas del Bloque 2...")
for path, content in WIKI_SOURCES_B2.items():
    write_file(path, content)

print("[*] 5 fuentes de wiki del Bloque 2 generadas exitosamente.")
