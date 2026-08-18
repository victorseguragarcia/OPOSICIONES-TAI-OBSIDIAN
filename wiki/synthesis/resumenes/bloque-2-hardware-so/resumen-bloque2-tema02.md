---
title: "Resumen Exhaustivo Tema 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-2
  - tema-02
  - hardware
  - sistemas-operativos
  - bbdd
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema02.md]]"
  - "[[wiki/sources/bloque2-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|Tema 03 ➡️]]

# 🔴 Resumen Exhaustivo Tema 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 02**
> Modelo Von Neumann vs Harvard, arquitectura del procesador (UC, ALU, Registros), ciclo de instrucción, CISC vs RISC, paralelismo (Pipelining, Superescalar, VLIW, Multihilo), jerarquía de memoria, memoria caché (niveles L1/L2/L3, mapeo directo, asociativo, políticas de reemplazo LRU/FIFO, políticas de escritura Write-Through vs Write-Back) y mecanismos de Entrada/Salida (Polling, Interrupciones, DMA).

---

## 🟣 1. Desarrollo Técnico y Arquitectónico Exhaustivo

### 1. Modelos de Arquitectura y Estructura de la CPU
- **Arquitectura Von Neumann vs Arquitectura Harvard**:
  - *Von Neumann (1945)*: **Memoria única compartida** para almacenar tanto instrucciones de programa como datos. Utiliza un **único bus común** para datos e instrucciones, lo que genera el cuello de botella de Von Neumann (*Von Neumann Bottleneck*).
  - *Harvard*: **Memorias y buses físicamente separados** para instrucciones y datos. Permite accesos simultáneos a instrucción y dato en el mismo ciclo de reloj. Utilizada internamente en las memorias caché L1 de los procesadores modernos (L1i para instrucciones y L1d para datos).
- **Componentes de la Unidad Central de Procesamiento (CPU)**:
  - **Unidad de Control (UC)**: Decodifica las instrucciones, genera las señales de control y temporización. Componentes: Contador de Programa (**PC** - dirección de la próxima instrucción), Registro de Instrucción (**IR** - almacena la instrucción en ejecución), Decodificador y Secuenciador.
  - **Unidad Aritmético-Lógica (ALU)**: Realiza operaciones aritméticas (+, -, *, /) y lógicas (AND, OR, NOT, XOR, desplazamientos). Contiene el Registro Acumulador (**AC**) y el Registro de Estado (**Flags / PSW** - Zero, Carry, Overflow, Sign).
  - **Registros del Procesador**: Registro de Direcciones de Memoria (**MAR**), Registro de Datos de Memoria (**MBR / MDR**), Registros de Propósito General.
- **Ciclo de Instrucción**:
  1. *Fetch (Búsqueda)*: El PC envía la dirección al MAR, se lee de memoria al MBR y pasa al IR. El PC se incrementa.
  2. *Decode (Decodificación)*: La UC analiza el código de operación (OpCode).
  3. *Execute (Ejecución)*: Se cargan operandos en la ALU y se ejecuta la operación.
  4. *Writeback (Almacenamiento)*: Se guarda el resultado en registro o memoria.

### 2. Clasificación Arquitectónica: CISC vs RISC y Técnicas de Rendimiento

| Criterio de Comparación | Arquitectura CISC (Complex Instruction Set Computer) | Arquitectura RISC (Reduced Instruction Set Computer) |
|:---|:---|:---|
| **Juego de Instrucciones** | Extenso, complejo, instrucciones de longitud variable. | Reducido, simple, **instrucciones de longitud fija** (habitualmente 32 bits). |
| **Ciclos por Instrucción (CPI)** | Variable (muchas instrucciones requieren múltiples ciclos). | **Cercano a 1 CPI** (instrucciones optimizadas de 1 solo ciclo). |
| **Acceso a Memoria** | Complejo (muchas instrucciones pueden operar directamente en memoria). | Arquitectura estricta **Load / Store** (solo instrucciones `LOAD` y `STORE` acceden a memoria; el resto opera sobre registros). |
| **Unidad de Control** | Principalmente **Microprogramada** (ROM de microcódigo). | Totalmente **Cableada** (Hardwired, circuitos lógicos para máxima velocidad). |
| **Registros** | Pocos registros de propósito general especializados. | Gran banco de registros generales (32 o más registros). |
| **Ejemplos Reales** | Intel x86, AMD64 (núcleo CISC decodificado a micro-ops RISC). | ARM, RISC-V, MIPS, SPARC, IBM POWER, Apple Silicon (M1/M2/M3). |

- **Técnicas Avanzadas de Paralelismo y Aceleración**:
  - *Segmentación de Instrucciones (Pipelining)*: División del ciclo de instrucción en etapas independientes (IF, ID, EX, MEM, WB) para ejecutar múltiples instrucciones simultáneamente.
    - *Riesgos del Pipeline*: **Estructurales** (conflicto de recursos hardware), **De Datos** (dependencias RAW, WAR, WAW; mitigado mediante forwarding/bypassing) y **De Control** (saltos y bifurcaciones; mitigado mediante predicción de saltos estática/dinámica y branch target buffers).
  - *Superescalaridad*: Capacidad de la CPU de emitir y ejecutar **múltiples instrucciones por ciclo de reloj** mediante múltiples unidades de ejecución en paralelo.
  - *VLIW (Very Long Instruction Word)*: El compilador empaqueta múltiples operaciones independientes en una única palabra de instrucción muy ancha.

### 3. Jerarquía de Memoria y Memoria Caché
- **Pirámide de Jerarquía**: Registros CPU ($<1	ext{ ns}$) $ightarrow$ Caché L1 ($1-2	ext{ ns}$) $ightarrow$ Caché L2 ($3-5	ext{ ns}$) $ightarrow$ Caché L3 ($10-20	ext{ ns}$) $ightarrow$ Memoria Principal RAM ($50-100	ext{ ns}$) $ightarrow$ Almacenamiento Secundario SSD/NVMe ($\mu	ext{s}$) $ightarrow$ HDD/Cintas ($	ext{ms}$).
- **Principio de Localidad**:
  - *Localidad Temporal*: Si una posición de memoria es referenciada, es muy probable que vuelva a ser referenciada en un futuro cercano (bucles, variables).
  - *Localidad Espacial*: Si una posición de memoria es referenciada, es muy probable que las posiciones contiguas sean referenciadas pronto (vectores, código secuencial).
- **Mapeo de Memoria Caché**:
  - *Mapeo Directo*: Cada bloque de memoria principal se mapea a una única línea fija de caché ($	ext{Línea} = 	ext{Bloque} \pmod{	ext{Total Líneas}}$). Rápido y económico, pero alto índice de fallos por colisión.
  - *Totalmente Asociativo*: Un bloque de memoria puede ubicarse en cualquier línea libre de la caché. Máxima flexibilidad, pero requiere hardware comparador complejo.
  - *Asociativo por Conjuntos ($N$-way Set Associative)*: La caché se divide en conjuntos de $N$ vías. El bloque se mapea a un conjunto fijo, pero dentro de él puede ocupar cualquier vía.
- **Políticas de Reemplazo**: **LRU** (Least Recently Used - menos usado recientemente), **FIFO** (First In, First Out), **LFU** (Least Frequently Used) y **Random**.
- **Políticas de Escritura**:
  - *Write-Through (Escritura Directa)*: Escribe simultáneamente en la caché y en la memoria principal. Consistencia garantizada, mayor tráfico de bus.
  - *Write-Back (Post-escritura / Copia Posterior)*: Escribe solo en la caché y marca la línea como sucia (*dirty bit*). Se actualiza la memoria principal únicamente cuando la línea es desalojada.

### 4. Mecanismos de Entrada/Salida (E/S)
1. **E/S Programada (Polling / Sondeo)**: La CPU comprueba activamente en un bucle continuo el estado del periférico hasta que esté listo. Ineficiente (desperdicio de ciclos de CPU).
2. **E/S Dirigida por Interrupciones**: El periférico envía una señal de interrupción hardware (IRQ) a la CPU cuando está listo. La CPU suspende la tarea actual, guarda el contexto y ejecuta la Rutina de Servicio de Interrupción (ISR).
3. **Acceso Directo a Memoria (DMA - Direct Memory Access)**: Un controlador especializado (DMAC) transfiere bloques enteros de datos **directamente entre el periférico y la memoria principal** sin intervención continua de la CPU, interrumpiendo a la CPU solo al finalizar la transferencia completa.
   - *Modos de DMA*: Por ráfagas (bloque completo tomando control del bus), por robo de ciclo (cycle stealing - aprovecha ciclos donde la CPU no usa el bus) y transparente.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 02 (Bloque 2)**
> 1. **Von Neumann vs Harvard**: En *Von Neumann* los datos y programas comparten el mismo bus de memoria; en *Harvard* existen buses físicos y memorias físicamente separadas.
> 2. **Load/Store en RISC**: En arquitecturas RISC puras las operaciones aritméticas **NUNCA pueden operar sobre memoria**, solo sobre registros (requieren hacer `LOAD` previo a registro y `STORE` posterior).
> 3. **Write-Through vs Write-Back**: En *Write-Back* la memoria principal NO se actualiza al instante, solo cuando la línea marcada con *dirty bit* es reemplazada.
> 4. **DMA**: No elimina las interrupciones; la CPU se libera de la transferencia de datos, pero el controlador DMA genera una **interrupción al terminar el bloque**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **CISC vs RISC**: **CISC Microprogramado / RISC Cableado (Hardwired)**.
> - **Etapas Clásicas del Pipeline**: **IF - ID - EX - MEM - WB** (Instruction Fetch, Instruction Decode, Execute, Memory access, Write-Back).
> - **Políticas de Caché**: **Write-Through $ightarrow$ Directo a RAM** / **Write-Back $ightarrow$ Con Dirty Bit**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque2-tema02|Fuente Oficial del Tema 02]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema02-perifericos-interfaces|Test Tema 02]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque 2**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|Tema 03 ➡️]]
