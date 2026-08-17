# -*- coding: utf-8 -*-
r"""
Script generador de Entidades, Conceptos y Síntesis adaptadas para el Bloque 2 (Tecnología Básica).
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

ENTITIES_CONCEPTS_SYNTHESES_B2 = {
    # =========================================================================
    # ENTIDADES BLOQUE 2
    # =========================================================================
    "wiki/entities/nosql-databases-and-cap-theorem.md": """---
title: "Bases de Datos NoSQL, Familias y Teorema CAP"
type: "entity"
tags:
  - nosql
  - sgbd
  - mongodb
  - redis
  - cassandra
  - neo4j
  - teorema-cap
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "NoSQL y Teorema CAP"
  - "Bases de Datos NoSQL"
---

# Bases de Datos NoSQL, Familias y Teorema CAP

Sistemas de almacenamiento no relacionales diseñados para alta concurrencia, escalabilidad horizontal y esquemas dinámicos.

---

## 🏛️ Familias de Bases de Datos NoSQL

1. **Clave-Valor (*Key-Value*)**: Acceso de baja latencia por clave única (**Redis**, **Memcached**, DynamoDB).
2. **Documentales (*Document-Store*)**: Documentos JSON/BSON con esquemas flexibles (**MongoDB**, **CouchDB**).
3. **Columnas Anchas (*Column-Family*)**: Tablas dispersas particionadas por claves de fila (**Apache Cassandra**, **HBase**).
4. **Grafos (*Graph Databases*)**: Nodos y aristas optimizados para consultas de relaciones complejas (**Neo4j**).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP de Brewer y Modelo BASE]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía de Familias NoSQL y Teorema CAP]]
""",

    "wiki/entities/operating-systems-architecture-and-scheduling.md": """---
title: "Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU"
type: "entity"
tags:
  - sistemas-operativos
  - procesos
  - planificacion-cpu
  - round-robin
  - pcb
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Sistemas Operativos y Planificación CPU"
  - "Gestión de Procesos SO"
---

# Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU

El subsistema de gestión de procesos del sistema operativo administra la asignación de la CPU entre los procesos listos para ejecución mediante algoritmos de planificación.

---

## 🏛️ Algoritmos de Planificación de CPU

- **FCFS**: Primero en llegar, primero en ser servido (no apropiativo).
- **SJF / SRTF**: Menor tiempo restante primero (óptimo en tiempo medio de espera).
- **Round Robin (RR)**: Rodaja de tiempo / quantum ($q$) circular apropiativo.
- **Prioridades y MLFQ**: Colas multinivel con realimentación dinámica.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/cpu-scheduling-algorithms|Algoritmos de Planificación de CPU]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
""",

    "wiki/entities/process-synchronization-and-deadlocks.md": """---
title: "Sincronización de Procesos, Condiciones de Coffman y Deadlocks"
type: "entity"
tags:
  - sistemas-operativos
  - deadlocks
  - coffman
  - exclusion-mutua
  - dijkstra
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Deadlocks y Sincronización"
  - "Condiciones de Coffman"
---

# Sincronización de Procesos, Condiciones de Coffman y Deadlocks

Situación de bloqueo mutuo donde un conjunto de procesos se encuentra permanentemente esperando por recursos asignados a otros procesos del mismo conjunto.

---

## 🏛️ Las 4 Condiciones de Coffman

1. **Exclusión Mutua**: Recursos de uso exclusivo.
2. **Retención y Espera**: Proceso retiene recursos mientras solicita nuevos.
3. **No Apropiación**: Los recursos no pueden ser expropiados forzosamente.
4. **Espera Circular**: Cadena cerrada de dependencias entre procesos y recursos.

- **Evasión**: **Algoritmo del Banquero de Dijkstra** (mantiene el sistema en estado seguro).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
""",

    "wiki/entities/virtual-memory-paging-and-segmentation.md": """---
title: "Memoria Virtual, Paginación, Segmentación y Algoritmos de Reemplazo"
type: "entity"
tags:
  - sistemas-operativos
  - memoria-virtual
  - paginacion
  - tlb
  - belady
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Memoria Virtual y Paginación"
  - "Paginación y Reemplazo de Páginas"
---

# Memoria Virtual, Paginación, Segmentación y Algoritmos de Reemplazo

Mecanismo que permite a los programas ejecutar con un espacio de direccionamiento lógico mayor que la memoria física real mediante el intercambio de páginas entre RAM y almacenamiento secundario.

---

## 🏛️ Componentes y Algoritmos de Reemplazo

- **Páginas y Marcos**: Páginas lógicas de tamaño fijo ($4\text{ KB}$) mapeadas a marcos físicos mediante la **Tabla de Páginas** y aceleradas por la **TLB**.
- **Algoritmos de Reemplazo**: **FIFO** (sufre la anomalía de Belady), **LRU** (menos recientemente usada), **Óptimo de Belady** y **Reloj** (segunda oportunidad).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/page-replacement-algorithms-and-thrashing|Algoritmos de Reemplazo de Páginas e Hiperpaginación]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual y Paginación]]
""",

    # =========================================================================
    # CONCEPTOS BLOQUE 2
    # =========================================================================
    "wiki/concepts/cap-theorem-and-base-model.md": """---
title: "Teorema CAP de Brewer y Modelo BASE"
type: "concept"
tags:
  - teorema-cap
  - base-model
  - consistencia-eventual
  - nosql
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Teorema CAP"
  - "Modelo BASE"
---

# Teorema CAP de Brewer y Modelo BASE

Teorema fundamental de la computación distribuida formulado por Eric Brewer que demuestra la imposibilidad de garantizar simultáneamente Consistencia, Disponibilidad y Tolerancia a Particiones.

---

## 🏛️ Principios CAP y BASE

- **Teorema CAP**: Ante una partición de red ($P$), los sistemas deben priorizar **Consistencia (CP)** (ej. HBase, MongoDB, Redis) o **Disponibilidad (AP)** (ej. Cassandra, CouchDB).
- **Modelo BASE**:
  - **Basically Available**: Disponibilidad básica ante fallos.
  - **Soft State**: El estado puede cambiar por propagación interna.
  - **Eventual Consistency**: Los nodos convergen tras un tiempo determinado.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía NoSQL y Teorema CAP]]
""",

    "wiki/concepts/cpu-scheduling-algorithms.md": """---
title: "Algoritmos de Planificación de CPU en Sistemas Operativos"
type: "concept"
tags:
  - planificacion-cpu
  - round-robin
  - sjf
  - fcfs
  - mlfq
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Planificación de CPU"
  - "Algoritmos de Planificación"
---

# Algoritmos de Planificación de CPU en Sistemas Operativos

Estrategias del planificador de corto plazo (*dispatcher*) para seleccionar el siguiente proceso a ejecutar en la CPU.

---

## 🏛️ Métricas y Criterios
- **Tiempo de Espera (*Waiting Time*)**: Tiempo total que un proceso pasa en la cola de listos.
- **Tiempo de Retorno (*Turnaround Time*)**: Tiempo transcurrido desde la creación hasta la terminación.
- **Rendimiento (*Throughput*)**: Procesos completados por unidad de tiempo.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Sistemas Operativos y Planificación]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU]]
""",

    "wiki/concepts/page-replacement-algorithms-and-thrashing.md": """---
title: "Algoritmos de Reemplazo de Páginas e Hiperpaginación (Thrashing)"
type: "concept"
tags:
  - memoria-virtual
  - paginacion
  - lru
  - fifo
  - belady
  - thrashing
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Reemplazo de Páginas y Thrashing"
  - "Hiperpaginación"
---

# Algoritmos de Reemplazo de Páginas e Hiperpaginación (Thrashing)

Políticas de desalojo de páginas en memoria física cuando ocurre un fallo de página y no existen marcos libres disponibles.

---

## 🏛️ Anomalía de Belady e Hiperpaginación
- **Anomalía de Belady**: Fenómeno en el algoritmo **FIFO** donde aumentar el número de marcos asignados provoca más fallos de página.
- **Hiperpaginación (*Thrashing*)**: Condición crítica donde los procesos pasan la mayor parte del tiempo paginando entre disco y RAM debido a falta de marcos en su *Working Set*.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual y Paginación]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual]]
""",

    # =========================================================================
    # SÍNTESIS BLOQUE 2
    # =========================================================================
    "wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet.md": """---
title: "Cheatsheet de Planificación de CPU, Algoritmos y Bloqueos Mutuos (Deadlocks)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-2
  - planificacion-cpu
  - deadlocks
  - coffman
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet Planificación CPU y Deadlocks"
  - "Planificación y Deadlocks Guía"
---

# 🔴 Cheatsheet de Planificación de CPU, Algoritmos y Bloqueos Mutuos (Deadlocks)

Tabla de repaso rápido de algoritmos de CPU, condiciones de Coffman y algoritmo del banquero.

---

## 📋 1. Matriz de Algoritmos de Planificación

| Algoritmo | Tipo | Ventajas | Inconvenientes / Riesgos |
|-----------|------|----------|--------------------------|
| **FCFS** | No Apropiativo | Sencillo de implementar | Efecto convoy (tiempos de espera altos) |
| **SJF** | No Apropiativo | Óptimo en tiempo medio de espera | Inanición (*starvation*) de procesos largos |
| **SRTF** | **Apropiativo** | Variante apropiativa de SJF | Sobrecarga de cambios de contexto |
| **Round Robin (RR)** | **Apropiativo** | Justo y óptimo para tiempo compartido | Sensible al tamaño del quantum ($q$) |
| **MLFQ** | **Apropiativo** | Dinámico y adaptable | Complejo de configurar |

---

## 🔒 2. Las 4 Condiciones de Coffman para Deadlocks

1. **Exclusión Mutua**
2. **Retención y Espera (*Hold & Wait*)**
3. **No Apropiación (*No Preemption*)**
4. **Espera Circular**

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Planificación de CPU]]
- Entidad: [[wiki/entities/process-synchronization-and-deadlocks|Sincronización y Deadlocks]]
""",

    "wiki/synthesis/nosql-families-and-cap-theorem-guide.md": """---
title: "Guía de Familias NoSQL, Teorema CAP de Brewer y Modelo BASE"
type: "synthesis"
tags:
  - synthesis
  - nosql
  - teorema-cap
  - mongodb
  - redis
  - cassandra
  - neo4j
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía NoSQL y Teorema CAP"
  - "Comparativa NoSQL y Teorema CAP"
---

# 🔴 Guía de Familias NoSQL, Teorema CAP de Brewer y Modelo BASE

Comparativa técnica de las 4 familias NoSQL y su clasificación según el Teorema CAP de Eric Brewer.

---

## 🏛️ Matriz Técnica NoSQL vs Teorema CAP

| Familia NoSQL | Tecnologías | Clasificación CAP | Formato / Estructura de Datos |
|---------------|-------------|-------------------|-------------------------------|
| **Clave-Valor** | **Redis**, Memcached, DynamoDB | **CP** / **AP** | Cadenas, hashes, listas, sets en RAM |
| **Documental** | **MongoDB**, CouchDB | **CP** (Consistencia fuerte) | **BSON** / **JSON** |
| **Columnar** | **Apache Cassandra**, HBase | **AP** (Alta disponibilidad) | Familias de columnas dispersas |
| **Grafos** | **Neo4j**, Amazon Neptune | **CA** (Clústeres locales) | Nodos, relaciones y propiedades |

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP]]
""",

    "wiki/synthesis/virtual-memory-and-paging-algorithms-guide.md": """---
title: "Guía de Memoria Virtual, Paginación y Algoritmos de Reemplazo"
type: "synthesis"
tags:
  - synthesis
  - memoria-virtual
  - paginacion
  - tlb
  - lru
  - belady
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Memoria Virtual y Paginación"
  - "Paginación y Reemplazo Guía"
---

# 🔴 Guía de Memoria Virtual, Paginación y Algoritmos de Reemplazo

Manual de resolución de problemas de traducción de direcciones virtuales, tablas de páginas y políticas de reemplazo para TAI.

---

## 📐 1. Estructura de Dirección Virtual

$$\text{Dirección Virtual} = \text{Número de Página (p)} \mathbin{\Vert} \text{Desplazamiento (d)}$$
- Con páginas de $4\text{ KB} = 2^{12}\text{ bytes}$, el desplazamiento $d$ ocupa **12 bits**.
- Si el bus de direcciones es de 32 bits, el número de página $p$ ocupa **20 bits** ($2^{20} = 1.048.576\text{ páginas}$).

---

## 🔄 2. Resumen de Algoritmos de Reemplazo de Página

- **FIFO**: Fácil de implementar, pero sufre la **Anomalía de Belady**.
- **LRU**: Excelente rendimiento, pero requiere soporte hardware (marcas de tiempo o pila).
- **Reloj (Segunda Oportunidad)**: Aproximación a LRU eficiente mediante un bit de referencia circular.
- **Óptimo de Belady (OPT)**: Mínimo número de fallos de página posible (usado como patrón de comparación teórico).

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual]]
- Concepto: [[wiki/concepts/page-replacement-algorithms-and-thrashing|Reemplazo de Páginas y Thrashing]]
"""
}

print("[*] Escribiendo entidades, conceptos y síntesis adaptadas del Bloque 2...")
for path, content in ENTITIES_CONCEPTS_SYNTHESES_B2.items():
    write_file(path, content)

print("[*] Adaptación completa de Bloque 2 finalizada exitosamente.")
