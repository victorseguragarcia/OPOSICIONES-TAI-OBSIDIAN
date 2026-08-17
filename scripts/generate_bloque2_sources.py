# -*- coding: utf-8 -*-
r"""
Script generador del temario oficial y notas fuente del Bloque 2 (TAI Oposiciones - Tecnología Básica).
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
# 1. RAW SOURCES BLOQUE 2 (Temas 01 al 05)
# ==============================================================================

RAW_SOURCES_B2 = {
    "raw/sources/bloque2-tema01.md": """---
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
  2. **Bus de Direcciones**: Unidireccional (desde la CPU hacia la memoria y periféricos). Transporta la dirección física de la posición de memoria a la que se desea acceder. Si el bus tiene $N$ líneas de dirección, el espacio direccionable máximo es de $2^N$ posiciones (bytes). *Ejemplo: 32 bits de direcciones direccionan $2^{32} = 4\\text{ GB}$; 64 bits direccionan $2^{64} = 16\\text{ Exabytes}$*.
  3. **Bus de Control**: Líneas unidireccionales y bidireccionales que transportan señales de sincronización, reloj, lectura/escritura (R/W), peticiones y concesiones de bus (Bus Request / Grant), e interrupciones (IRQ).
""",

    "raw/sources/bloque2-tema02.md": """---
title: "Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces de Comunicación"
type: "raw-source"
topic: "perifericos-conectividad"
date: "2026-08-17"
---

# Bloque 2 - Tema 02: Periféricos: Tipos, Controladores y Puertos de Conectividad (USB, PCIe, NVMe, Thunderbolt)

## 1. Clasificación de Periféricos
- **Periféricos de Entrada**: Teclado, ratón, escáner, tableta digitalizadora, lectores ópticos/biométricos, micrófonos, cámaras web.
- **Periféricos de Salida**: Monitores (tecnologías IPS, OLED, MiniLED, frecuencias de refresco), impresoras (láser electrofotográfico, inyección de tinta piezoeléctrica/térmica, 3D), altavoces.
- **Periféricos de Entrada/Salida (Mixtos)**: Pantallas táctiles, unidades de almacenamiento masivo extraíbles, tarjetas de red (NIC Ethernet, Wi-Fi), módems, gafas de realidad virtual.

## 2. Mecanismos de Transferencia de E/S con la CPU
1. **E/S Programada (Polling / Encuesta)**: La CPU comprueba periódicamente mediante un bucle de software el estado del controlador de periférico. Desperdicia tiempo de CPU (*busy waiting*).
2. **E/S Controlada por Interrupciones (Interrupt-driven I/O)**: El dispositivo periférico genera una señal física de interrupción (**IRQ**) cuando está listo para transferir datos. La CPU suspende la ejecución del programa actual, guarda el contexto y ejecuta la **Rutina de Servicio de Interrupción (ISR)**.
3. **Acceso Directo a Memoria (DMA - Direct Memory Access)**: Un controlador especializado de DMA transfiere bloques enteros de datos directamente entre el periférico y la memoria principal sin pasar por los registros de la CPU. La CPU solo interviene al inicio (configurando dirección origen, destino y longitud) y al final cuando el DMA emite una interrupción de finalización.

## 3. Puertos e Interfaces de Conectividad de Alta Velocidad

### Estándar USB (Universal Serial Bus)
Bus serie diferencial punto a punto con topología en árbol estratificado (hasta 127 dispositivos mediante concentradores/hubs y 5 niveles de cascada).
- **USB 1.1**: Low-Speed (1.5 Mbps) y Full-Speed (12 Mbps).
- **USB 2.0 (High-Speed)**: Tasa bruta de **480 Mbps** (60 MB/s teóricos, ~40 MB/s reales). Conectores Tipo A, Tipo B, Mini-USB y Micro-USB.
- **USB 3.0 / USB 3.1 Gen 1 / USB 3.2 Gen 1 (SuperSpeed)**: **5 Gbps** (codificación 8b/10b, ~500 MB/s). Color azul característico en conector Tipo-A.
- **USB 3.1 Gen 2 / USB 3.2 Gen 2 (SuperSpeed+)**: **10 Gbps** (codificación 128b/132b, ~1.2 GB/s).
- **USB 3.2 Gen 2x2**: **20 Gbps** (utiliza dos pares diferenciales en conector USB Type-C).
- **USB4 (basado en Thunderbolt 3)**:
  - **USB4 Gen 2x2**: 20 Gbps.
  - **USB4 Gen 3x2**: **40 Gbps**.
  - **USB4 2.0**: Hasta **80 Gbps** bidireccional y 120 Gbps asimétrico.
- **USB Type-C**: Conector reversible de 24 pines que soporta transmisión de datos, modos alternativos (DisplayPort Alt Mode, Thunderbolt) y alimentación eléctrica **USB Power Delivery (USB-PD)** de hasta **240W (48V / 5A en EPR)**.

### Thunderbolt (Intel / Apple)
Tecnología de comunicación serie que multiplexa paquetes **PCI Express** y **DisplayPort** sobre un único cable.
- **Thunderbolt 1**: 10 Gbps por canal (2 canales, 20 Gbps total). Conector Mini DisplayPort.
- **Thunderbolt 2**: 20 Gbps agregado.
- **Thunderbolt 3**: **40 Gbps**, utiliza conector USB Type-C y proporciona alimentación USB-PD.
- **Thunderbolt 4**: 40 Gbps garantizados, soporte para dos pantallas 4K o una 8K y PCIe a 32 Gbps mínimo.

### PCI Express (PCIe)
Arquitectura de bus serie punto a punto con canales dúplex dedicados denominados **líneas (lanes: x1, x2, x4, x8, x16)**.
- **PCIe 3.0**: 8 GT/s por línea (codificación 128b/130b) $\approx$ **985 MB/s por línea** (~15.75 GB/s en ranura x16).
- **PCIe 4.0**: 16 GT/s por línea $\approx$ **1.969 GB/s por línea** (~31.5 GB/s en ranura x16).
- **PCIe 5.0**: 32 GT/s por línea $\approx$ **3.938 GB/s por línea** (~63 GB/s en ranura x16).
- **PCIe 6.0**: 64 GT/s utilizando modulación multinivel **PAM4** $\approx$ **7.877 GB/s por línea**.

### NVMe (Non-Volatile Memory Express) vs SATA
- **SATA III (Serial ATA Revision 3.0)**: Diseñado para discos mecánicos, protocolo AHCI, velocidad máxima teórica de **6 Gbps (600 MB/s)**, 1 cola de comandos con profundidad máxima de 32 comandos.
- **NVMe**: Protocolo optimizado diseñado específicamente para almacenamiento en estado sólido Flash no volátil conectado directamente sobre el bus **PCI Express**. Admite hasta **64.000 colas de comandos**, cada una con una profundidad de hasta **64.000 comandos simultáneos**, con paralelismo masivo multicore y mínimas latencias. Formatos físicos: M.2 (2280), U.2, E1.S / E3.
""",

    "raw/sources/bloque2-tema03.md": """---
title: "Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode"
type: "raw-source"
topic: "representacion-informacion"
date: "2026-08-17"
---

# Bloque 2 - Tema 03: Sistemas de Numeración, Representación de Enteros y Reales (IEEE 754) y Codificación de Caracteres

## 1. Sistemas de Numeración y Conversiones
- **Sistema Binario (Base 2)**: Dígitos 0 y 1.
- **Sistema Octal (Base 8)**: Dígitos 0 a 7. Cada dígito octal equivale a un grupo de 3 bits binarios.
- **Sistema Hexadecimal (Base 16)**: Dígitos 0 a 9 y letras A ($=10$), B ($=11$), C ($=12$), D ($=13$), E ($=14$), F ($=15$). Cada dígito hexadecimal equivale a un cuarteto (*nibble*) de 4 bits binarios.
- **Decimal Codificado en Binario (BCD - Binary-Coded Decimal)**: Cada dígito decimal (0-9) se codifica de forma independiente en 4 bits binarios (ej. $25_{10} = 0010\\ 0101_{BCD}$).

## 2. Representación de Números Enteros con Signo en $n$ bits
1. **Signo y Magnitud (SM)**:
   - El bit más significativo (MSB) es el bit de signo: 0 para positivo, 1 para negativo. Los $n-1$ bits restantes representan el valor absoluto.
   - Rango en $n$ bits: $[-(2^{n-1}-1), +(2^{n-1}-1)]$.
   - Inconveniente: Doble representación del cero ($+0 = 0000$ y $-0 = 1000$).
2. **Complemento a 1 (C1)**:
   - Los números positivos se representan en binario natural con bit de signo 0.
   - Los números negativos se obtienen invirtiendo todos los bits (bit a bit) del número positivo correspondiente.
   - Rango en $n$ bits: $[-(2^{n-1}-1), +(2^{n-1}-1)]$. Doble cero ($+0 = 0000$, $-0 = 1111$).
3. **Complemento a 2 (C2) - Estándar Universal en CPUs**:
   - Los positivos comienzan con bit 0 seguido de la magnitud en binario natural.
   - Los negativos se obtienen aplicando la operación lógica: $\\text{C2}(X) = \\text{C1}(X) + 1$ (invertir todos los bits y sumar 1 al bit menos significativo).
   - **Regla Práctica Inmediata**: Dejar invariables todos los bits de derecha a izquierda hasta encontrar el primer '1' inclusive, e invertir todos los bits restantes a su izquierda.
   - **Rango Asimétrico en $n$ bits**: $[-2^{n-1}, +(2^{n-1}-1)]$. Posee **una única representación para el cero** ($0000\\dots0$).
   - *Ejemplo en 8 bits ($n=8$)*: Rango $[-128, +127]$. El valor $-128 = 10000000_2$, $-1 = 11111111_2$, $0 = 00000000_2$, $+127 = 01111111_2$.

## 3. Representación de Números Reales: Estándar IEEE 754
Estándar internacional que normaliza la representación binaria en coma flotante según la fórmula:
$$X = (-1)^S \\times 1.M \\times 2^{E - \\text{Sesgo}}$$
Donde $S$ es el bit de signo (0 positivo, 1 negativo), $E$ es el exponente desplazado/polarizado con un sesgo (*bias*), y $M$ es la mantisa fraccionaria con bit implícito ('1.M').

### Precisión Simple (32 bits / Single Precision - `float`)
- **Estructura de 32 bits**:
  - **1 bit de Signo ($S$)**: Bit 31.
  - **8 bits de Exponente ($E$)**: Bits 30 a 23. **Sesgo = 127** ($2^{8-1}-1$). Exponente real $e = E - 127$.
  - **23 bits de Mantisa ($M$)**: Bits 22 a 0.
- **Valores Especiales en Precisión Simple**:
  - **Cero ($\pm 0$)**: $E = 00000000_2$ ($0$), $M = 0$.
  - **Números Desnormalizados / Subnormales**: $E = 00000000_2$ ($0$), $M \\neq 0$. Valor: $(-1)^S \\times 0.M \\times 2^{-126}$.
  - **Infinito ($\pm\\infty$)**: $E = 11111111_2$ ($255$), $M = 0$.
  - **No es un Número (NaN - Not a Number)**: $E = 11111111_2$ ($255$), $M \\neq 0$ (errores como $0/0$ o $\\sqrt{-1}$).

### Precisión Doble (64 bits / Double Precision - `double`)
- **Estructura de 64 bits**:
  - **1 bit de Signo ($S$)**: Bit 63.
  - **11 bits de Exponente ($E$)**: Bits 62 a 52. **Sesgo = 1023** ($2^{11-1}-1$). Exponente real $e = E - 1023$.
  - **52 bits de Mantisa ($M$)**: Bits 51 a 0.

## 4. Codificación de Caracteres
- **ASCII (American Standard Code for Information Interchange)**: Estándar de **7 bits** (128 caracteres del 0 al 127). Contiene caracteres de control (0-31: NUL, CR, LF, TAB) y caracteres imprimibles (32 espacio a 126 tilde, '0' en 48 / 0x30, 'A' en 65 / 0x41, 'a' en 97 / 0x61).
- **ASCII Extendido / ISO 8859-1 (Latin-1)**: Código de **8 bits** (256 caracteres). Añade caracteres de idiomas de Europa occidental (ñ, acentos, diéresis).
- **EBCDIC (Extended BCD Interchange Code)**: Código de **8 bits** desarrollado por IBM para sus mainframes System/360. Incompatible con ASCII.
- **Unicode**: Estándar universal que asigna a cada carácter un identificador único denominado punto de código (*Code Point*, notación `U+XXXX`), cubriendo más de 149.000 caracteres de todas las lenguas y símbolos.
  - **UTF-8**: Codificación de **longitud variable de 1 a 4 bytes**. Totalmente compatible hacia atrás con ASCII (los primeros 128 caracteres ocupan exactamente 1 byte: `0xxxxxxx`). Caracteres latinos europeos ocupan 2 bytes (`110xxxxx 10xxxxxx`), caracteres asiáticos 3 bytes (`1110xxxx 10xxxxxx 10xxxxxx`) y emojis 4 bytes (`11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`). Es la codificación estándar dominante en Internet (>98% de la web).
  - **UTF-16**: Codificación de 2 o 4 bytes (utiliza pares sustitutos para caracteres fuera del plano multilingüe básico BMP).
  - **UTF-32**: Codificación de longitud fija de 4 bytes (32 bits) por carácter.
""",

    "raw/sources/bloque2-tema04.md": """---
title: "Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O"
type: "raw-source"
topic: "estructuras-datos-algoritmos"
date: "2026-08-17"
---

# Bloque 2 - Tema 04: Estructuras de Datos Lineales y No Lineales, Algoritmos de Ordenación y Búsqueda, y Complejidad Computacional

## 1. Estructuras de Datos Lineales
- **Listas Enlazadas**: Colección de nodos donde cada nodo contiene un dato y uno o más punteros al siguiente (simple) o anterior y siguiente (doblemente enlazada). Inserción y borrado en $O(1)$ con puntero; acceso aleatorio en $O(n)$.
- **Pilas (Stacks - LIFO: Last In, First Out)**: Inserción y extracción se realizan exclusivamente por el mismo extremo (la cima / *top*). Operaciones elementales: `push` (apilar) y `pop` (desapilar) en $O(1)$. Aplicaciones: gestión de llamadas a funciones (pila de llamadas), evaluación de expresiones en notación polaca inversa (RPN), algoritmos de *backtracking*.
- **Colas (Queues - FIFO: First In, First Out)**: Inserción por el final (*rear/tail*) y extracción por el frente (*front/head*). Operaciones: `enqueue` (encolar) y `dequeue` (desencolar) en $O(1)$. Aplicaciones: colas de impresión, planificación de procesos CPU (Round Robin), buffers de E/S.
- **Colas de Prioridad (Priority Queues)**: Los elementos se extraen según su nivel de prioridad, implementadas típicamente mediante montículos binarios (*Heaps*).

## 2. Estructuras de Datos No Lineales
- **Árboles Binarios**: Estructura jerárquica donde cada nodo tiene a lo sumo dos hijos (izquierdo y derecho).
  - **Árbol Binario de Búsqueda (BST - Binary Search Tree)**: Para cada nodo $X$, todos los elementos de su subárbol izquierdo son menores que $X$, y todos los de su subárbol derecho son mayores que $X$. Búsqueda, inserción y borrado promedio en $O(\\log n)$, pero degrada a $O(n)$ si está desbalanceado (árbol degenerado en lista).
  - **Recorridos de Árboles**:
    - *Preorden*: Raíz $\\rightarrow$ Izquierda $\\rightarrow$ Derecha.
    - *Inorden*: Izquierda $\\rightarrow$ Raíz $\\rightarrow$ Derecha (produce la secuencia ordenada en un BST).
    - *Postorden*: Izquierda $\\rightarrow$ Derecha $\\rightarrow$ Raíz.
    - *Por Niveles (Anchura / BFS)*: Nivel 0, nivel 1, nivel 2...
  - **Árboles Balanceados AVL**: Árbol BST auto-balanceable donde para cada nodo la diferencia de altura entre sus subárboles izquierdo y derecho (factor de equilibrio) es a lo sumo $\\pm 1$. Restablece el equilibrio mediante **rotaciones simples (LL, RR)** o **rotaciones dobles (LR, RL)**. Garantiza operaciones en $O(\\log n)$ en el peor caso.
  - **Árboles B y B+**: Árboles multicamino balanceados de orden $M$. Cada nodo puede contener múltiples claves y múltiples hijos. Diseñados para sistemas de archivos y motores de bases de datos relacionales para minimizar accesos a disco. En el árbol B+, todos los datos se almacenan exclusivamente en las hojas enlazadas secuencialmente.
- **Grafos**: Conjunto de vértices (nodos) y aristas (relaciones).
  - Tipos: Dirigidos (Dígrafos), No dirigidos, Ponderados/Valorados.
  - Representaciones: **Matriz de Adyacencia** (espacio $O(V^2)$, eficiente para grafos densos) y **Lista de Adyacencia** (espacio $O(V+E)$, eficiente para grafos dispersos).
  - Algoritmos: Búsqueda en Anchura (BFS con cola), Búsqueda en Profundidad (DFS con pila/recursión), Camino Mínimo (**Dijkstra** para aristas con pesos positivos en $O((V+E)\\log V)$, Bellman-Ford para aristas con pesos negativos) y Árbol de Recubrimiento Mínimo (Kruskal, Prim).

## 3. Algoritmos de Ordenación y Complejidad Big-O

| Algoritmo de Ordenación | Mejor Caso | Caso Promedio | Peor Caso | Complejidad Espacial | ¿Estable? | Técnica Algorítmica |
|-------------------------|------------|---------------|-----------|----------------------|-----------|---------------------|
| **Burbuja (Bubble Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Intercambio |
| **Inserción (Insertion Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Inserción directa |
| **Selección (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Selección |
| **Quicksort (Hoare)** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n^2)$* | $O(\\log n)$ | No | Divide y Vencerás |
| **Mergesort (Von Neumann)** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n \\log n)$ | $O(n)$ | **Sí** | Divide y Vencerás |
| **Heapsort (Williams)** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n \\log n)$ | $O(1)$ | No | Selección sobre Montículo |

*\*El peor caso de Quicksort ($O(n^2)$) ocurre cuando el pivote seleccionado es sistemáticamente el elemento mínimo o máximo (ej. lista ya ordenada sin pivote aleatorio).*

## 4. Algoritmos de Búsqueda
- **Búsqueda Secuencial / Lineal**: Recorre el vector elemento a elemento. Complejidad: Mejor caso $O(1)$, promedio y peor caso $O(n)$. Funciona sobre listas desordenadas.
- **Búsqueda Binaria / Dicotómica**: Requiere que el vector esté **previamente ordenado**. Compara con el elemento central y descarta la mitad del vector en cada paso. Complejidad: Mejor caso $O(1)$, promedio y peor caso **$O(\\log n)$**.
- **Búsqueda por Dispersión (Hashing)**: Aplica una función hash $h(K)$ sobre la clave para obtener la dirección directa del índice en la tabla hash. Acceso en **$O(1)$ caso promedio**; degrada a $O(n)$ en el peor caso de colisiones masivas. Métodos de resolución de colisiones: encadenamiento separado (listas enlazadas) y direccionamiento abierto (sondeo lineal, cuadrático o doble hashing).
""",

    "raw/sources/bloque2-tema05.md": """---
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
- **Factor de Bloqueo ($Bf$)**: Número de registros lógicos contenidos en un registro físico ($Bf = \\lfloor \\text{Tamaño Bloque} / \\text{Tamaño Registro} \\rfloor$).

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
"""
}

print("[*] Escribiendo 5 fuentes brutas de Tecnología Básica en raw/sources/bloque2-tema*.md...")
for path, content in RAW_SOURCES_B2.items():
    write_file(path, content)

print("[*] 5 fuentes brutas del Bloque 2 generadas exitosamente.")
