---
title: "Bloque 2 - Tema 01: Arquitectura de Ordenadores, CPU, Memoria y Buses"
type: "raw-source"
topic: "arquitectura-ordenadores"
date: "2026-08-17"
---

# Bloque 2 - Tema 01: Concepto de Informática, Arquitectura de Ordenadores, CPU, Jerarquía de Memoria y Buses

## 1. Arquitectura de Ordenadores: Modelo Von Neumann vs Modelo Harvard
- **Modelo Von Neumann (1945)**:
  - Estructura básica: **Unidad Central de Proceso (CPU)**, **Memoria Principal**, **Sistema de Entrada/Salida** y **Buses del sistema**.
  - Principio fundamental: **Memoria única compartida** que almacena tanto datos como instrucciones de programa en el mismo espacio de direccionamiento.
  - Cuello de botella de Von Neumann (*Von Neumann Bottleneck*): La velocidad del procesador está limitada por el ancho de banda del bus único compartido para transferir instrucciones y datos secuencialmente.
- **Modelo Harvard**:
  - Posee **memorias físicas y buses de comunicación físicamente separados e independientes para datos y para instrucciones**.
  - Permite el acceso simultáneo a una instrucción y a un operando de datos en el mismo ciclo de reloj. Ampliamente utilizado en Procesadores de Señal Digital (DSP) y en la arquitectura interna de cachés L1 de microprocesadores modernos (caché L1 de datos y caché L1 de instrucciones separadas).

## 2. La Unidad Central de Proceso (CPU)
La CPU ejecuta las instrucciones del programa almacenado en memoria mediante ciclos continuos de instrucción (*Fetch-Decode-Execute*).
- **Componentes Fundamentales**:
  1. **Unidad de Control (UC)**: Dirige y coordina la actividad de todo el ordenador. Genera las microórdenes y señales de control necesarias.
     - Componentes: **Contador de Programa (PC - Program Counter)** que contiene la dirección de memoria de la siguiente instrucción a ejecutar; **Registro de Instrucción (IR - Instruction Register)** que almacena la instrucción en curso de ejecución; **Decodificador de Instrucción**; **Secuenciador** y **Reloj del sistema**.
  2. **Unidad Aritmético-Lógica (ALU)**: Realiza las operaciones aritméticas (suma, resta, multiplicación) y lógicas (AND, OR, NOT, XOR, desplazamientos).
     - Componentes: Circuitos operacionales (sumadores, comparadores), **Registro Acumulador (ACC)** y **Registro de Estado / Flags (PSW - Program Status Word)** con indicadores de acarreo (Carry), cero (Zero), signo (Sign/Negative) y desbordamiento (Overflow).
  3. **Registros de la CPU**:
     - *Registros visibles para el programador*: Registros de propósito general (datos y direcciones), registro de puntero de pila (SP - Stack Pointer), registros índice y registro de segmento.
     - *Registros de control y estado*: PC, IR, **Registro de Dirección de Memoria (MAR - Memory Address Register)** conectado al bus de direcciones, y **Registro de Datos de Memoria (MBR / MDR - Memory Buffer/Data Register)** conectado al bus de datos.

### Filosofías de Diseño: CISC vs RISC
- **CISC (Complex Instruction Set Computer)**: Gran repertorio de instrucciones complejas de longitud variable, múltiples modos de direccionamiento, instrucciones que realizan operaciones compuestas de memoria y cálculo (ej. arquitectura x86/IA-32).
- **RISC (Reduced Instruction Set Computer)**: Repertorio reducido de instrucciones simples de longitud fija (típicamente 32 bits), formato Load/Store (solo las instrucciones `LOAD` y `STORE` acceden a memoria principal; el resto opera sobre registros), ejecución en un único ciclo de reloj mediante segmentación (*pipelining*) intensiva (ej. ARM, RISC-V, MIPS).

## 3. Jerarquía de Memoria
Organizada en niveles según el compromiso entre velocidad de acceso, coste por bit y capacidad de almacenamiento:
1. **Nivel 0: Registros del Procesador**: Capacidad en bytes/kilobytes, tiempo de acceso $<1$ ns (velocidad de reloj).
2. **Nivel 1: Memoria Caché L1**: Integrada en el núcleo del procesador, dividida en L1i (instrucciones) y L1d (datos). Capacidad de 32 a 64 KB por núcleo, tiempo de acceso de 1 a 2 ns.
3. **Nivel 2: Memoria Caché L2**: Dedicada por núcleo o compartida, capacidad de 256 KB a 2 MB, tiempo de acceso de 3 a 10 ns.
4. **Nivel 3: Memoria Caché L3**: Compartida por todos los núcleos del procesador (*Last Level Cache*), capacidad de 8 a 128 MB, tiempo de acceso de 10 a 20 ns.
5. **Nivel 4: Memoria Principal (RAM - Random Access Memory)**: Volátil. Tecnologías DRAM (Dynamic RAM) con celdas de un transistor y un condensador (requiere refresco periódico). Módulos DDR4, DDR5 (Dual Data Rate). Capacidad de Gigabytes, tiempo de acceso de 50 a 100 ns.
6. **Nivel 5: Almacenamiento Secundario Masivo**: No volátil. Unidades de estado sólido SSD (NVMe/PCIe, SATA) basadas en memoria Flash NAND (SLC, MLC, TLC, QLC) y discos duros magnéticos HDD. Capacidad de Terabytes, tiempos de acceso de microsegundos (SSD) a milisegundos (HDD).

### Políticas de Gestión de Memoria Caché
- **Principio de Localidad**:
  - *Localidad Temporal*: Si una posición de memoria es referenciada, es muy probable que vuelva a ser referenciada pronto en el tiempo (ej. bucles).
  - *Localidad Espacial*: Si una posición de memoria es referenciada, es muy probable que las posiciones contiguas sean referenciadas pronto (ej. vectores, código secuencial).
- **Mapeo / Correspondencia de Bloques**:
  - *Mapeo Directo*: Cada bloque de memoria principal se mapea en una única línea fija de caché. Fácil y rápido, pero con alta tasa de fallos por conflicto.
  - *Totalmente Asociativo*: Un bloque de memoria puede ubicarse en cualquier línea de la caché. Máxima flexibilidad, pero búsqueda asociativa costosa.
  - *Asociativo por Conjuntos (Set-Associative)*: La caché se divide en $S$ conjuntos de $K$ líneas ($K$-way). Compromiso óptimo estándar en CPUs modernas (ej. 8-way, 16-way).
- **Políticas de Reemplazo**: LRU (*Least Recently Used* - menos recientemente usado), FIFO (*First In, First Out*), LFU (*Least Frequently Used*), Aleatorio (*Random*).
- **Políticas de Escritura**:
  - *Write-Through (Escritura directa)*: Cada escritura en caché se escribe inmediatamente en memoria principal. Datos siempre coherentes, pero penaliza el bus.
  - *Write-Back (Copia posterior)*: La escritura se realiza solo en caché, marcando la línea con un bit sucio (*dirty bit*). Solo se escribe en memoria principal cuando la línea es expulsada por reemplazo.

## 4. Buses de Comunicación del Sistema
Conjunto de líneas conductoras paralelas que transmiten señales binarias entre los componentes del computador.
- **Clasificación por Función**:
  1. **Bus de Datos**: Bidireccional. Transporta las palabras de datos e instrucciones. Su ancho ($8, 16, 32, 64$ bits) determina el tamaño de palabra que la CPU puede transferir en un ciclo.
  2. **Bus de Direcciones**: Unidireccional (desde la CPU hacia la memoria y periféricos). Transporta la dirección física de la posición de memoria a la que se desea acceder. Si el bus tiene $N$ líneas de dirección, el espacio direccionable máximo es de $2^N$ posiciones (bytes). *Ejemplo: 32 bits de direcciones direccionan $2^{32} = 4\text{ GB}$; 64 bits direccionan $2^{64} = 16\text{ Exabytes}$*.
  3. **Bus de Control**: Líneas unidireccionales y bidireccionales que transportan señales de sincronización, reloj, lectura/escritura (R/W), peticiones y concesiones de bus (Bus Request / Grant), e interrupciones (IRQ).
