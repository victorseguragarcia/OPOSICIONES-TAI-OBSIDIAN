# -*- coding: utf-8 -*-
r"""
Script generador de las notas fuente estructuradas para wiki/sources/ del Bloque 2 (TAI).
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
title: "Resumen Fuente: Bloque 2 - Tema 01: Arquitectura de Ordenadores, CPU, Memoria y Buses"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema01
  - arquitectura-ordenadores
  - cpu
  - jerarquia-memoria
  - buses
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitectura de Ordenadores y CPU"
  - "bloque2-tema01"
---

# Resumen Fuente: Bloque 2 - Tema 01: Arquitectura de Ordenadores, CPU, Memoria y Buses

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema01.md|bloque2-tema01.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en la estructura y funcionamiento interno de un sistema informático: los modelos arquitectónicos **Von Neumann** (memoria única compartida para datos e instrucciones) frente a **Harvard** (memorias y buses físicos separados), los componentes y registros de la **CPU** (Unidad de Control con PC, IR, decodificador; Unidad Aritmético-Lógica ALU con acumulador y registro de estado PSW; y registros de memoria MAR/MBR), el ciclo de instrucción (*fetch-decode-execute*), las filosofías **CISC vs RISC**, la **jerarquía de memoria** (registros, cachés L1/L2/L3, memoria RAM DRAM y almacenamiento secundario) con sus principios de localidad y políticas de correspondencia/reemplazo/escritura, y la clasificación y capacidad de direccionamiento de los **buses del sistema** (datos, direcciones y control).

---

## 🎯 Datos Clave para Oposiciones TAI

| Componente / Concepto | Función / Fórmula de Examen |
|-----------------------|-----------------------------|
| **Modelo Von Neumann** | Memoria **única compartida** para datos e instrucciones (Cuello de botella de bus único) |
| **Modelo Harvard** | Memorias y buses **separados físicamente** para datos e instrucciones |
| **Contador de Programa (PC)** | Contiene la **dirección de memoria de la siguiente instrucción** a ejecutar |
| **Registro de Instrucción (IR)** | Almacena la **instrucción que se está ejecutando** actualmente |
| **Registro MAR / MBR** | **MAR**: Dirección física conectada al bus de direcciones \| **MBR**: Datos conectados al bus de datos |
| **Espacio Direccionable Bus Direcciones** | $2^N$ bytes, donde $N$ es el número de líneas de dirección ($2^{32} = 4\\text{ GB}$) |
| **Caché Write-Through vs Write-Back** | **Write-Through**: Escribe en caché y RAM a la vez \| **Write-Back**: Escribe solo en caché (bit sucio) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/cpu-architecture-von-neumann|Arquitectura de CPU y Modelo Von Neumann]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria y Memoria RAM]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
- Síntesis: [[wiki/synthesis/bloque2-tai-oposiciones-master-guide|Guía Maestra de Bloque 2: Tecnología Básica (TAI)]]
""",

    "wiki/sources/bloque2-tema02.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces (USB, PCIe, NVMe)"
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
  - thunderbolt
sources:
  - "raw/sources/bloque2-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Periféricos y Conectividad"
  - "bloque2-tema02"
---

# Resumen Fuente: Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces (USB, PCIe, NVMe)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema02.md|bloque2-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza la clasificación funcional de los periféricos (entrada, salida y mixtos), los métodos de control de transferencia de E/S con el procesador (E/S programada con *busy waiting*, E/S por interrupciones IRQ y **Acceso Directo a Memoria DMA**), y las especificaciones técnicas de los buses y puertos de alta velocidad modernos: el estándar **USB** (USB 2.0 a 480 Mbps, USB 3.2 Gen 1 a 5 Gbps, Gen 2 a 10 Gbps, Gen 2x2 a 20 Gbps, USB4 a 40/80 Gbps y USB-PD de hasta 240W en conector Type-C), **Thunderbolt 3/4** (40 Gbps sobre Type-C multiplexando PCIe y DisplayPort), el bus serie punto a punto **PCI Express (PCIe Gen 3, 4, 5 y 6)** y el protocolo de estado sólido **NVMe** con sus 64.000 colas paralelas frente al estándar SATA III (AHCI).

---

## 🎯 Datos Clave para Oposiciones TAI

| Interfaz / Estándar | Tasa de Transferencia / Característica |
|---------------------|----------------------------------------|
| **USB 2.0 (High-Speed)** | **480 Mbps** (60 MB/s teóricos) |
| **USB 3.2 Gen 1 (SuperSpeed)** | **5 Gbps** (~500 MB/s) |
| **USB 3.2 Gen 2 (SuperSpeed+)**| **10 Gbps** (~1.2 GB/s) |
| **USB 3.2 Gen 2x2** | **20 Gbps** (conector USB Type-C) |
| **USB4 / Thunderbolt 3 y 4** | **40 Gbps** (USB4 2.0 hasta 80 Gbps) |
| **USB Power Delivery (USB-PD)**| Hasta **240W (48V / 5A)** en modo EPR |
| **SATA III vs NVMe** | SATA III: **6 Gbps / 1 cola (32 comandos)** \| NVMe: **PCIe / 64.000 colas (64.000 comandos c/u)** |
| **DMA (Direct Memory Access)**| Transfiere bloques entre periférico y RAM **sin consumir ciclos de CPU** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|Interfaces Periféricas: USB, PCIe, NVMe y Thunderbolt]]
- Síntesis: [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos, Buses y Velocidades]]
""",

    "wiki/sources/bloque2-tema03.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema03
  - complemento-a-dos
  - ieee-754
  - ascii
  - unicode
  - utf-8
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Representación de la Información"
  - "bloque2-tema03"
---

# Resumen Fuente: Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema03.md|bloque2-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la codificación matemática y digital de los datos: la conversión entre sistemas de numeración (binario, octal, hexadecimal y BCD), la representación de números enteros con signo destacando el **Complemento a 2 (C2)** (rango asimétrico $[-2^{n-1}, +2^{n-1}-1]$, cero único y regla de cálculo), la representación de números reales en coma flotante bajo el estándar **IEEE 754** (precisión simple de 32 bits con sesgo 127 y precisión doble de 64 bits con sesgo 1023, junto a valores especiales $\pm 0, \pm\infty$, NaN y desnormalizados), y la evolución de los códigos de caracteres desde **ASCII** (7 bits / 128 caracteres) e **ISO 8859-1 (Latin-1)** (8 bits), hasta **Unicode** y la codificación de longitud variable **UTF-8** (1 a 4 bytes, compatible hacia atrás con ASCII).

---

## 🎯 Datos Clave para Oposiciones TAI

| Sistema / Norma | Estructura / Rango / Sesgo |
|-----------------|----------------------------|
| **Rango C2 en 8 bits ($n=8$)** | **$[-128, +127]$** (Cero único: `00000000`) |
| **IEEE 754 Precisión Simple (32 bits)** | **1 bit Signo** + **8 bits Exponente (Sesgo = 127)** + **23 bits Mantisa** |
| **IEEE 754 Precisión Doble (64 bits)** | **1 bit Signo** + **11 bits Exponente (Sesgo = 1023)** + **52 bits Mantisa** |
| **IEEE 754 Infinito ($\pm\\infty$)** | Exponente todo a '1' ($E=255$) y Mantisa todo a '0' ($M=0$) |
| **IEEE 754 NaN (Not a Number)** | Exponente todo a '1' ($E=255$) y Mantisa **distinta de cero** ($M \\neq 0$) |
| **ASCII Estándar** | **7 bits** (128 caracteres del 0 al 127) |
| **UTF-8** | Longitud variable de **1 a 4 bytes** (primeros 128 caracteres idénticos a ASCII en 1 byte) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ieee-754-floating-point|Estándar IEEE 754 de Coma Flotante]]
- Entidad: [[wiki/entities/character-encoding-unicode-utf8|Codificación de Caracteres: ASCII y Unicode/UTF-8]]
- Concepto: [[wiki/concepts/two-complement-and-binary-arithmetic|Complemento a Dos y Aritmética Binaria]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo IEEE 754 y Binario]]
""",

    "wiki/sources/bloque2-tema04.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema04
  - estructuras-datos
  - arboles-avl
  - algoritmos-ordenacion
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Estructuras de Datos y Algoritmos"
  - "bloque2-tema04"
---

# Resumen Fuente: Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema04.md|bloque2-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema constituye la base algorítmica de la informática: las estructuras de datos lineales (**listas**, **pilas LIFO**, **colas FIFO** y colas de prioridad), las estructuras no lineales (**árboles binarios de búsqueda BST**, recorridos preorden/inorden/postorden, **árboles balanceados AVL** con rotaciones simples y dobles, **árboles B y B+**, y **grafos** con matrices/listas de adyacencia y algoritmos de caminos mínimos como **Dijkstra**), el análisis de complejidad asintótica mediante **notación Big-O**, y el estudio comparativo exhaustivo de los algoritmos de ordenación (**Quicksort**, **Mergesort**, **Heapsort**, Burbuja, Inserción y Selección) evaluando tiempo, memoria auxiliar y estabilidad.

---

## 🎯 Datos Clave para Oposiciones TAI

| Algoritmo / Estructura | Complejidad Temporal Promedio | Peor Caso | Complejidad Espacial | ¿Estable? |
|------------------------|-------------------------------|-----------|----------------------|-----------|
| **Quicksort** | **$O(n \\log n)$** | **$O(n^2)$** | $O(\\log n)$ | No |
| **Mergesort** | **$O(n \\log n)$** | **$O(n \\log n)$** | **$O(n)$** | **Sí** |
| **Heapsort** | **$O(n \\log n)$** | **$O(n \\log n)$** | **$O(1)$** | No |
| **Búsqueda Binaria** | **$O(\\log n)$** | **$O(\\log n)$** | $O(1)$ | N/A (requiere array ordenado) |
| **Tabla Hash (Búsqueda)**| **$O(1)$** | **$O(n)$** | $O(n)$ | N/A |
| **Árbol AVL (Búsqueda/Ins)**| **$O(\\log n)$** | **$O(\\log n)$** | $O(n)$ | Auto-balanceado (Factor $\\pm 1$) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación y Búsqueda]]
- Entidad: [[wiki/entities/data-structures-trees-and-graphs|Estructuras de Datos: Árboles y Grafos]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Computacional y Notación Big-O]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz Comparativa de Algoritmos de Ordenación]]
""",

    "wiki/sources/bloque2-tema05.md": """---
title: "Resumen Fuente: Bloque 2 - Tema 05: Ficheros, Organización y Sistemas de Archivos: FAT32, NTFS, ext4, XFS"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema05
  - ficheros
  - sistemas-archivos
  - fat32
  - ntfs
  - ext4
  - xfs
sources:
  - "raw/sources/bloque2-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Ficheros y Sistemas de Archivos"
  - "bloque2-tema05"
---

# Resumen Fuente: Bloque 2 - Tema 05: Ficheros, Organización y Sistemas de Archivos: FAT32, NTFS, ext4, XFS

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema05.md|bloque2-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza los fundamentos del almacenamiento a nivel de sistema operativo: la estructura lógica de ficheros (registros lógicos, bloques físicos y factor de bloqueo), las organizaciones de ficheros (**secuencial**, **directa/relativa por hash** e **indexada/ISAM**) y sus modos de acceso (secuencial, directo y dinámico), y la arquitectura y límites de los principales sistemas de archivos modernos: **FAT32** (límite estricto de 4 GB por archivo), **NTFS** (basado en la tabla MFT, con soporte de journaling `$LogFile`, permisos ACL, cifrado EFS, cuotas y VSS), **ext4** (basado en inodos con extensiones *extents*, asignación retardada y journaling de 3 modos) y **XFS** (diseñado para escalabilidad masiva con Grupos de Asignación paralelos y volúmenes de hasta 8 Exabytes).

---

## 🎯 Datos Clave para Oposiciones TAI

| Sistema de Archivos | Tamaño Máximo de Archivo | Tamaño Máximo de Volumen | Journaling | Estructura Principal |
|---------------------|--------------------------|--------------------------|------------|----------------------|
| **FAT32** | **4 GB ($2^{32}-1$ bytes)** | **2 TB** | **No** | File Allocation Table (28 bits) |
| **NTFS** | **16 TB** a 8 PB | **8 PB** | **Sí (`$LogFile`)** | **MFT (Master File Table)** |
| **ext4** | **16 TB** | **1 Exabyte (EB)** | **Sí** | **Inodos + Extents** |
| **XFS** | **8 Exabytes (EB)** | **8 Exabytes (EB)** | **Sí** | **Allocation Groups (AG)** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos: FAT32, NTFS, ext4 y XFS]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización de Ficheros y Métodos de Acceso]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]
"""
}

print("[*] Escribiendo 5 notas fuente estructuradas en wiki/sources/bloque2-tema*.md...")
for path, content in WIKI_SOURCES_B2.items():
    write_file(path, content)

print("[*] 5 fuentes de wiki del Bloque 2 generadas exitosamente.")
