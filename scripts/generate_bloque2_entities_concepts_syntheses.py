# -*- coding: utf-8 -*-
r"""
Script generador de Entidades, Conceptos y Síntesis del Bloque 2 (Tecnología Básica) para TAI.
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
# ENTIDADES BLOQUE 2 (8 Entidades)
# ==============================================================================

BLOQUE2_ENTITIES = {
    "wiki/entities/cpu-architecture-von-neumann.md": """---
title: "Arquitectura de CPU y Modelo Von Neumann"
type: "entity"
tags:
  - cpu
  - von-neumann
  - harvard
  - hardware
  - registros
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de CPU"
  - "Modelo Von Neumann"
  - "Procesador"
---

# Arquitectura de CPU y Modelo Von Neumann

La **Unidad Central de Proceso (CPU)** es el núcleo computacional del ordenador encargado de interpretar y ejecutar las instrucciones de los programas almacenados en memoria.

---

## 🏛️ Componentes y Registros de la CPU

```
                         Estructura Interna de la CPU
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
Unidad de Control (UC)      Unidad Aritmético-Lógica (ALU)     Banco de Registros
• Contador de Programa (PC) • Acumulador (ACC)                 • MAR (Direcciones)
• Registro Instrucción (IR) • Flags / Estado (PSW)             • MBR / MDR (Datos)
• Decodificador y Reloj     • Circuitos Operacionales          • Propósito General (R0-Rn)
```

---

## 🎯 Datos Clave para Oposiciones TAI

| Registro / Arquitectura | Definición Técnica |
|-------------------------|--------------------|
| **Contador de Programa (PC)** | Contiene la dirección de la **siguiente instrucción a ejecutar** |
| **Registro de Instrucción (IR)** | Almacena el código de operación de la **instrucción actual** |
| **Registro MAR** | Contiene la dirección física conectada al **bus de direcciones** |
| **Registro MBR/MDR** | Contiene la palabra de datos conectada al **bus de datos** |
| **CISC vs RISC** | CISC: Instrucciones complejas variables \| RISC: Instrucciones simples fijas tipo *Load/Store* |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
""",

    "wiki/entities/memory-hierarchy-and-ram.md": """---
title: "Jerarquía de Memoria, Memoria RAM y Memorias ROM"
type: "entity"
tags:
  - memoria
  - ram
  - rom
  - cache
  - dram
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Jerarquía de Memoria"
  - "Memoria RAM"
  - "DRAM y SRAM"
---

# Jerarquía de Memoria, Memoria RAM y Memorias ROM

La jerarquía de memoria organiza los diferentes tipos de dispositivos de almacenamiento en función de la velocidad, coste y capacidad.

---

## 🏛️ Niveles de la Jerarquía de Memoria

1. **Registros de CPU**: $<1$ ns, Bytes.
2. **Caché L1 / L2 / L3 (SRAM)**: 1 a 20 ns, Kilobytes a Megabytes.
3. **Memoria Principal (DRAM - DDR4/DDR5)**: 50 a 100 ns, Gigabytes (requiere refresco periódico de condensadores).
4. **Almacenamiento Secundario (SSD NVMe / SATA, HDD)**: Microsegundos a Milisegundos, Terabytes (no volátil).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología | Características |
|------------|-----------------|
| **SRAM (Static RAM)** | Celdas de biestables (flip-flops, 4-6 transistores), muy rápida, sin refresco, usada en **memorias caché** |
| **DRAM (Dynamic RAM)** | Celdas de 1 transistor + 1 condensador, requiere **refresco periódico**, usada en **memoria principal** |
| **ROM / EEPROM / Flash** | No volátiles; Flash permite borrado y reescritura eléctrica por bloques |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
""",

    "wiki/entities/peripheral-interfaces-usb-pcie-nvme.md": """---
title: "Interfaces Periféricas: USB, PCIe, NVMe y Thunderbolt"
type: "entity"
tags:
  - perifericos
  - conectividad
  - usb
  - pcie
  - nvme
  - thunderbolt
sources:
  - "raw/sources/bloque2-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Interfaces Periféricas"
  - "USB y PCIe"
  - "NVMe"
---

# Interfaces Periféricas: USB, PCIe, NVMe y Thunderbolt

Estándares modernos de interconexión y transferencia de datos de alta velocidad para periféricos y almacenamiento masivo.

---

## 🏛️ Comparativa de Velocidades de Buses

| Bus / Interfaz | Versión / Modo | Ancho de Banda Teórico | Conector Frecuente |
|----------------|----------------|------------------------|--------------------|
| **USB 2.0** | High-Speed | **480 Mbps** (60 MB/s) | Tipo-A / Micro-USB |
| **USB 3.2 Gen 1** | SuperSpeed | **5 Gbps** (~500 MB/s) | Tipo-A (Azul) / Tipo-C |
| **USB 3.2 Gen 2** | SuperSpeed+ | **10 Gbps** (~1.2 GB/s) | Tipo-A / Tipo-C |
| **USB 3.2 Gen 2x2**| Doble Línea | **20 Gbps** | USB Type-C |
| **USB4 / TB3 / TB4**| Gen 3x2 | **40 Gbps** | USB Type-C |
| **PCIe 4.0 (x16)** | Gen 4 | **~31.5 GB/s** (~2 GB/s por línea) | Ranura PCIe |
| **PCIe 5.0 (x16)** | Gen 5 | **~63 GB/s** (~4 GB/s por línea) | Ranura PCIe |
| **SATA III** | 6 Gbps | **600 MB/s** | Cable SATA 7 pines |
| **NVMe** | PCIe Gen 4 x4 | **Hasta 7.5 GB/s** (64.000 colas) | Ranura M.2 / U.2 |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema02|Resumen Bloque 2 - Tema 02]]
- Síntesis: [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos y Buses]]
""",

    "wiki/entities/ieee-754-floating-point.md": """---
title: "Estándar IEEE 754 de Representación en Coma Flotante"
type: "entity"
tags:
  - ieee-754
  - coma-flotante
  - representacion-datos
  - float
  - double
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IEEE 754"
  - "Coma Flotante"
---

# Estándar IEEE 754 de Representación en Coma Flotante

El estándar **IEEE 754** normaliza la representación binaria de números reales mediante la descomposición en **Signo ($S$)**, **Exponente sesgado ($E$)** y **Mantisa normalizada ($M$)**:
$$X = (-1)^S \\times 1.M \\times 2^{E - \\text{Sesgo}}$$

---

## 🏛️ Formatos de Precisión

| Precisión | Tamaño Total | Signo ($S$) | Exponente ($E$) | Sesgo (*Bias*) | Mantisa ($M$) |
|-----------|--------------|-------------|-----------------|----------------|---------------|
| **Simple (`float`)** | **32 bits** | 1 bit (bit 31) | 8 bits (bits 30-23) | **127** | 23 bits (bits 22-0) |
| **Doble (`double`)** | **64 bits** | 1 bit (bit 63) | 11 bits (bits 62-52) | **1023** | 52 bits (bits 51-0) |

---

## 🎯 Valores Especiales

- **Cero ($\pm 0$)**: $E = 0$, $M = 0$.
- **Infinito ($\pm\infty$)**: $E = 255$ (simple) / $E = 2047$ (doble), $M = 0$.
- **NaN (Not a Number)**: $E = 255$ (simple) / $E = 2047$ (doble), $M \\neq 0$.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo IEEE 754]]
""",

    "wiki/entities/character-encoding-unicode-utf8.md": """---
title: "Codificación de Caracteres: ASCII, ISO 8859-1 y Unicode/UTF-8"
type: "entity"
tags:
  - codificacion-caracteres
  - ascii
  - unicode
  - utf-8
  - utf-16
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Unicode"
  - "UTF-8"
  - "ASCII"
---

# Codificación de Caracteres: ASCII, ISO 8859-1 y Unicode/UTF-8

Evolución de los estándares internacionales para la representación informática de texto y caracteres alfanuméricos.

---

## 🏛️ Comparativa de Esquemas

- **ASCII**: 7 bits (128 caracteres). Letra 'A' = 65 ($01000001_2$), 'a' = 97 ($01100001_2$), '0' = 48 ($00110000_2$).
- **ISO 8859-1 (Latin-1)**: 8 bits (256 caracteres, incluye caracteres de idiomas europeos occidentales).
- **Unicode**: Espacio universal de más de 1,1 millones de puntos de código (`U+0000` a `U+10FFFF`).
- **UTF-8**: Codificación de longitud variable (1 a 4 bytes). **Compatible 100% con ASCII** en el primer byte (`0xxxxxxx`).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Síntesis: [[wiki/synthesis/bloque2-tai-oposiciones-master-guide|Guía Maestra de Bloque 2 (TAI)]]
""",

    "wiki/entities/sorting-and-searching-algorithms.md": """---
title: "Algoritmos de Ordenación y Búsqueda"
type: "entity"
tags:
  - algoritmos
  - ordenacion
  - busqueda
  - quicksort
  - mergesort
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Algoritmos de Ordenación"
  - "Quicksort y Mergesort"
---

# Algoritmos de Ordenación y Búsqueda

Estudio comparativo de los métodos fundamentales para organizar y localizar información en estructuras de datos.

---

## 🏛️ Matriz de Rendimiento

| Algoritmo | Tiempo Promedio | Peor Caso | Espacio Auxiliar | ¿Estabilidad? |
|-----------|-----------------|-----------|------------------|---------------|
| **Quicksort** | **$O(n \\log n)$** | **$O(n^2)$** | $O(\\log n)$ | No |
| **Mergesort** | **$O(n \\log n)$** | **$O(n \\log n)$** | **$O(n)$** | **Sí** |
| **Heapsort** | **$O(n \\log n)$** | **$O(n \\log n)$** | **$O(1)$** | No |
| **Búsqueda Binaria** | **$O(\\log n)$** | **$O(\\log n)$** | $O(1)$ | Requiere vector ordenado |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Big-O]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Complejidad de Algoritmos]]
""",

    "wiki/entities/data-structures-trees-and-graphs.md": """---
title: "Estructuras de Datos: Pilas, Colas, Árboles y Grafos"
type: "entity"
tags:
  - estructuras-datos
  - pilas
  - colas
  - arboles-avl
  - grafos
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Estructuras de Datos"
  - "Árboles y Grafos"
---

# Estructuras de Datos: Pilas, Colas, Árboles y Grafos

Modelos de organización de información en memoria para procesamiento eficiente en computación.

---

## 🏛️ Estructuras Clave

- **Pila (Stack)**: LIFO (*Last In, First Out*). Operaciones `push` y `pop` en $O(1)$.
- **Cola (Queue)**: FIFO (*First In, First Out*). Operaciones `enqueue` y `dequeue` en $O(1)$.
- **Árbol AVL**: Árbol binario de búsqueda auto-balanceado con factor de equilibrio $\\pm 1$. Búsqueda e inserción en **$O(\\log n)$**.
- **Árbol B / B+**: Árboles multicamino optimizados para minimizar accesos a disco en bases de datos y sistemas de archivos.
- **Grafos**: Algoritmo de **Dijkstra** (caminos mínimos con pesos no negativos), recorridos BFS y DFS.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación]]
""",

    "wiki/entities/file-systems-ntfs-ext4-fat32.md": """---
title: "Sistemas de Archivos: FAT32, NTFS, ext4 y XFS"
type: "entity"
tags:
  - sistemas-archivos
  - fat32
  - ntfs
  - ext4
  - xfs
  - inodos
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Sistemas de Archivos"
  - "NTFS y ext4"
---

# Sistemas de Archivos: FAT32, NTFS, ext4 y XFS

Arquitectura y características técnicas de los sistemas de archivos más utilizados en Windows y GNU/Linux.

---

## 🏛️ Comparativa de Límites y Características

| Sistema | Tamaño Máx Archivo | Tamaño Máx Volumen | Journaling | Estructura Central |
|---------|-------------------|-------------------|------------|--------------------|
| **FAT32** | **4 GB ($2^{32}-1$)** | **2 TB** | No | File Allocation Table |
| **NTFS** | **16 TB** a 8 PB | **8 PB** | **Sí (`$LogFile`)** | **MFT (Master File Table)** |
| **ext4** | **16 TB** | **1 Exabyte** | **Sí** | **Inodos + Extents** |
| **XFS** | **8 Exabytes** | **8 Exabytes** | **Sí** | **Allocation Groups (AG)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización de Ficheros]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
"""
}

print("[*] Escribiendo 8 entidades del Bloque 2...")
for path, content in BLOQUE2_ENTITIES.items():
    write_file(path, content)

# ==============================================================================
# CONCEPTOS BLOQUE 2 (4 Conceptos)
# ==============================================================================

BLOQUE2_CONCEPTS = {
    "wiki/concepts/two-complement-and-binary-arithmetic.md": """---
title: "Complemento a Dos y Aritmética Binaria"
type: "concept"
tags:
  - complemento-a-dos
  - aritmetica-binaria
  - enteros-signo
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Complemento a 2"
  - "Aritmética en Complemento a Dos"
---

# Complemento a Dos y Aritmética Binaria

El sistema de **Complemento a 2 (C2)** es el estándar universal en arquitectura de computadores para la representación de números enteros con signo.

---

## 🏛️ Propiedades y Reglas

- **Rango en $n$ bits**: $[-2^{n-1}, +(2^{n-1}-1)]$. Para 8 bits: $[-128, +127]$.
- **Cero Único**: $0 = 00000000_2$ (a diferencia de Signo y Magnitud y C1 que tienen doble cero).
- **Cálculo Negativo**: Invertir todos los bits (C1) y sumar 1 al bit menos significativo ($\text{C2} = \text{C1} + 1$).
- **Regla Rápida**: Conservar los bits desde la derecha hasta el primer '1' inclusive, e invertir todos los demás.
- **Detección de Overflow en Sumas**: Se produce desbordamiento cuando al sumar dos números del mismo signo se obtiene un resultado de signo contrario.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo Binario e IEEE 754]]
""",

    "wiki/concepts/computational-complexity-and-big-o.md": """---
title: "Complejidad Computacional y Notación Asintótica Big-O"
type: "concept"
tags:
  - complejidad-algoritmica
  - big-o
  - algoritmos
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Notación Big-O"
  - "Complejidad Asintótica"
---

# Complejidad Computacional y Notación Asintótica Big-O

La notación asintótica describe el comportamiento del tiempo de ejecución y el consumo de memoria de un algoritmo a medida que el tamaño de entrada $n$ tiende a infinito.

---

## 🏛️ Jerarquía de Complejidades (de Mejor a Peor)

$$O(1) < O(\\log n) < O(n) < O(n \\log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

- **$O(1)$ Constante**: Acceso a vector por índice, `push`/`pop` en pila.
- **$O(\\log n)$ Logarítmica**: Búsqueda binaria, operaciones en árbol AVL.
- **$O(n)$ Lineal**: Búsqueda secuencial, recorrido de lista enlazada.
- **$O(n \\log n)$ Cuasi-lineal**: Mergesort, Heapsort, Quicksort promedio (límite teórico de ordenación por comparaciones).
- **$O(n^2)$ Cuadrática**: Ordenación por burbuja, selección o inserción.
- **$O(2^n)$ Exponencial**: Torres de Hanoi, subconjuntos.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación]]
""",

    "wiki/concepts/cache-memory-and-coherence.md": """---
title: "Memoria Caché, Principios de Localidad y Coherencia"
type: "concept"
tags:
  - cache
  - localidad-memoria
  - coherencia-cache
  - hardware
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Memoria Caché"
  - "Coherencia de Caché"
---

# Memoria Caché, Principios de Localidad y Coherencia

La memoria caché es una memoria de alta velocidad intermedia entre la CPU y la RAM principal que aprovecha el principio de localidad.

---

## 🏛️ Principios y Políticas de Caché

- **Principio de Localidad**:
  - *Temporal*: Reutilización de datos recientes (bucles).
  - *Espacial*: Acceso a datos contiguos en memoria (vectores).
- **Políticas de Escritura**:
  - *Write-Through*: Escribe simultáneamente en caché y RAM.
  - *Write-Back*: Escribe solo en caché marcando el *dirty bit*; escribe en RAM al expulsar la línea.
- **Políticas de Reemplazo**: LRU (*Least Recently Used*), FIFO, LFU, Random.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria]]
""",

    "wiki/concepts/file-organization-and-access-methods.md": """---
title: "Organización de Ficheros y Métodos de Acceso"
type: "concept"
tags:
  - ficheros
  - organizacion-ficheros
  - acceso-secuencial
  - acceso-directo
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Organización de Ficheros"
  - "Métodos de Acceso"
---

# Organización de Ficheros y Métodos de Acceso

Estructuración lógica de los datos sobre soportes de almacenamiento no volátil.

---

## 🏛️ Clasificación de Organizaciones

1. **Secuencial**: Registros contiguos en orden físico. Muy rápida para procesar el 100% de registros en lotes; lenta para búsquedas individuales.
2. **Directa / Relativa (Hash)**: Ubicación calculada mediante función de dispersión sobre la clave. Acceso en $O(1)$.
3. **Indexada / Secuencial-Indexada (ISAM)**: Área secuencial más tabla de índices auxiliar. Soporta tanto acceso secuencial ordenado como acceso directo por clave.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos]]
"""
}

print("[*] Escribiendo 4 conceptos de Tecnología Básica...")
for path, content in BLOQUE2_CONCEPTS.items():
    write_file(path, content)

# ==============================================================================
# SÍNTESIS BLOQUE 2 (5 Fichas)
# ==============================================================================

BLOQUE2_SYNTHESES = {
    "wiki/synthesis/bloque2-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 2: Tecnología Básica (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-2
  - oposiciones
  - tai
sources:
  - "raw/sources/bloque2-tema01.md"
  - "raw/sources/bloque2-tema02.md"
  - "raw/sources/bloque2-tema03.md"
  - "raw/sources/bloque2-tema04.md"
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 2"
  - "Bloque 2 TAI Master Guide"
---

# Guía Maestra de Bloque 2: Tecnología Básica (TAI)

Mapa integral de conocimientos del **Bloque 2 (Tecnología Básica)** para las oposiciones de Técnicos Auxiliares de Informática de la AGE.

---

## 🗺️ Mapa Temático del Bloque 2

| Tema | Materia Oficial | Resumen Fuente | Entidades Clave | Conceptos Clave |
|------|-----------------|----------------|-----------------|-----------------|
| **Tema 01** | Arquitectura CPU, Memoria y Buses | [[wiki/sources/bloque2-tema01\|Resumen Tema 01]] | [[wiki/entities/cpu-architecture-von-neumann\|CPU Von Neumann]], [[wiki/entities/memory-hierarchy-and-ram\|Jerarquía Memoria]] | [[wiki/concepts/cache-memory-and-coherence\|Memoria Caché]] |
| **Tema 02** | Periféricos y Conectividad (USB, PCIe, NVMe) | [[wiki/sources/bloque2-tema02\|Resumen Tema 02]] | [[wiki/entities/peripheral-interfaces-usb-pcie-nvme\|Interfaces USB/PCIe/NVMe]] | DMA e Interrupciones |
| **Tema 03** | Representación de Datos: C2, IEEE 754, Unicode | [[wiki/sources/bloque2-tema03\|Resumen Tema 03]] | [[wiki/entities/ieee-754-floating-point\|IEEE 754]], [[wiki/entities/character-encoding-unicode-utf8\|Unicode / UTF-8]] | [[wiki/concepts/two-complement-and-binary-arithmetic\|Complemento a 2]] |
| **Tema 04** | Estructuras de Datos, Ordenación y Big-O | [[wiki/sources/bloque2-tema04\|Resumen Tema 04]] | [[wiki/entities/sorting-and-searching-algorithms\|Ordenación/Búsqueda]], [[wiki/entities/data-structures-trees-and-graphs\|Árboles y Grafos]] | [[wiki/concepts/computational-complexity-and-big-o\|Complejidad Big-O]] |
| **Tema 05** | Ficheros y Sistemas de Archivos | [[wiki/sources/bloque2-tema05\|Resumen Tema 05]] | [[wiki/entities/file-systems-ntfs-ext4-fat32\|FAT32, NTFS, ext4, XFS]] | [[wiki/concepts/file-organization-and-access-methods\|Organización de Ficheros]] |

---

## 📚 Síntesis Monográficas de Examen
- [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo IEEE 754 y Binario]]
- [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz Comparativa de Algoritmos de Ordenación]]
- [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos, Buses y Velocidades]]
- [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
""",

    "wiki/synthesis/ieee-754-and-binary-representation-cheatsheet.md": """---
title: "Cheatsheet de Cálculo Binario, Complemento a 2 y Coma Flotante IEEE 754"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - ieee-754
  - complemento-a-dos
  - binario
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet IEEE 754"
  - "Cálculo en Complemento a 2"
---

# Cheatsheet de Cálculo Binario, Complemento a 2 y Coma Flotante IEEE 754

Guía práctica de resolución paso a paso para preguntas prácticas de cálculo en oposiciones TAI.

---

## 🔢 1. Procedimiento de Cálculo en Complemento a 2 (8 bits)
- **Representar un número positivo (ej. $+25$)**:
  - $25_{10} = 16 + 8 + 1 = 00011001_2$ (Bit MSB 0).
- **Representar el negativo correspondiente (ej. $-25$)**:
  - Invertir todos los bits (C1): $11100110_2$.
  - Sumar 1: $11100110 + 1 = \mathbf{11100111_2}$.
- **Rango en $n=8$ bits**: $[-128, +127]$. El valor $-128 = 10000000_2$, $-1 = 11111111_2$.

---

## 📐 2. Procedimiento de Conversión a IEEE 754 Simple Precisión (32 bits)

Ejemplo: Convertir el número decimal **$-13.625$** a formato IEEE 754 de 32 bits.
1. **Determinar el Signo**: Al ser negativo, **$S = 1$**.
2. **Convertir la parte entera y fraccionaria a binario**:
   - $13_{10} = 1101_2$.
   - $0.625_{10} = 0.5 + 0.125 = 0.101_2$.
   - Número en binario sin signo: $1101.101_2$.
3. **Normalizar en formato $1.M \times 2^e$**:
   - Desplazar la coma 3 posiciones a la izquierda: $1.101101_2 \times 2^3$.
   - Mantisa ($M$): $10110100000000000000000_2$ (rellenada con ceros hasta 23 bits).
4. **Calcular el Exponente sesgado ($E$)**:
   - Exponente real $e = 3$.
   - $E = e + 127 = 3 + 127 = 130_{10} = 10000010_2$.
5. **Ensamblar los 32 bits ($S + E + M$)**:
   - `1 | 10000010 | 10110100000000000000000`
   - Agrupado en hexadecimal: `1100 0001 0101 1010 0000 0000 0000 0000` $\rightarrow$ **`0xC15A0000`**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Entidad: [[wiki/entities/ieee-754-floating-point|IEEE 754]]
""",

    "wiki/synthesis/algorithms-complexity-and-sorting-matrix.md": """---
title: "Matriz Comparativa de Algoritmos de Ordenación y Complejidad Big-O"
type: "synthesis"
tags:
  - synthesis
  - algoritmos
  - ordenacion
  - complejidad
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Matriz de Algoritmos de Ordenación"
  - "Complejidad de Algoritmos"
---

# Matriz Comparativa de Algoritmos de Ordenación y Complejidad Big-O

Cuadro sinóptico de algoritmos de ordenación y búsqueda para preguntas teóricas de examen.

---

## 🏛️ Matriz Comparativa Completa

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso | Memoria Auxiliar | ¿Es Estable? | Método |
|-----------|------------|---------------|-----------|------------------|--------------|--------|
| **Burbuja (Bubble Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Intercambio |
| **Inserción (Insertion Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Inserción |
| **Selección (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Selección |
| **Quicksort (Hoare)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n^2)$** | $O(\log n)$ | No | Divide y Vencerás |
| **Mergesort (Von Neumann)**| **$O(n \log n)$** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n)$** | **Sí** | Divide y Vencerás |
| **Heapsort (Montículo)** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(1)$** | No | Selección / Heap |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación]]
""",

    "wiki/synthesis/hardware-ports-and-buses-cheatsheet.md": """---
title: "Cheatsheet de Puertos, Buses y Velocidades de Transferencia"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - buses
  - puertos
  - velocidades
  - hardware
sources:
  - "raw/sources/bloque2-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet de Puertos y Buses"
  - "Velocidades USB y PCIe"
---

# Cheatsheet de Puertos, Buses y Velocidades de Transferencia

Tabla de consulta rápida de anchos de banda teóricos y características físicas de interfaces de hardware.

---

## ⚡ Tabla Maestra de Velocidades

| Bus / Conector | Estándar | Velocidad Bruta / Tasa Teórica |
|----------------|----------|--------------------------------|
| **USB 2.0** | High-Speed | **480 Mbps** (60 MB/s) |
| **USB 3.2 Gen 1** | SuperSpeed (antiguo USB 3.0) | **5 Gbps** (~500 MB/s) |
| **USB 3.2 Gen 2** | SuperSpeed+ (antiguo USB 3.1) | **10 Gbps** (~1.2 GB/s) |
| **USB 3.2 Gen 2x2** | Doble línea Type-C | **20 Gbps** |
| **USB4 / TB3 / TB4**| Gen 3x2 | **40 Gbps** |
| **USB Power Delivery** | USB-PD EPR | **Hasta 240W (48V / 5A)** |
| **SATA III (AHCI)** | Rev 3.0 | **6 Gbps (600 MB/s)** |
| **PCIe 3.0 (x16)** | Gen 3 | **~15.75 GB/s** (~985 MB/s por línea) |
| **PCIe 4.0 (x16)** | Gen 4 | **~31.5 GB/s** (~1.97 GB/s por línea) |
| **PCIe 5.0 (x16)** | Gen 5 | **~63 GB/s** (~3.94 GB/s por línea) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema02|Resumen Bloque 2 - Tema 02]]
- Entidad: [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|Interfaces Periféricas]]
""",

    "wiki/synthesis/file-systems-comparison-matrix.md": """---
title: "Matriz Comparativa de Sistemas de Archivos: FAT32, NTFS, ext4 y XFS"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - file-systems
  - fat32
  - ntfs
  - ext4
  - xfs
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Sistemas de Archivos"
  - "FAT32 vs NTFS vs ext4"
---

# Matriz Comparativa de Sistemas de Archivos: FAT32, NTFS, ext4 y XFS

Contraste técnico de capacidades, seguridad y tolerancia a fallos entre sistemas de archivos.

---

## 🏛️ Matriz Técnica Comparativa

| Característica | FAT32 | NTFS | ext4 | XFS |
|----------------|-------|------|------|-----|
| **Sistema Operativo Principal** | Multiplataforma | Windows Server / 11 | GNU/Linux | Linux (RHEL/CentOS) |
| **Tamaño Máximo de Archivo** | **4 GB ($2^{32}-1$)** | **16 TB** (hasta 8 PB) | **16 TB** | **8 Exabytes (EB)** |
| **Tamaño Máximo de Volumen** | **2 TB** | **8 PB** | **1 Exabyte (EB)** | **8 Exabytes (EB)** |
| **Registro por Diario (Journaling)**| **No** | **Sí (`$LogFile`)** | **Sí (3 modos)** | **Sí** |
| **Estructura Interna de Metadatos** | Tabla FAT (28 bits) | **MFT (Master File Table)**| **Inodos + Extents** | **Allocation Groups** |
| **Permisos de Seguridad** | No | ACLs (DACL / SACL) | Permisos POSIX + ACLs | Permisos POSIX + ACLs |
| **Cifrado y Compresión Nativos** | No | **Sí (EFS / LZNT1)** | Opcional | No nativo |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos]]
"""
}

print("[*] Escribiendo 5 síntesis del Bloque 2...")
for path, content in BLOQUE2_SYNTHESES.items():
    write_file(path, content)

print("[*] Generación del Bloque 2 completada exitosamente.")
