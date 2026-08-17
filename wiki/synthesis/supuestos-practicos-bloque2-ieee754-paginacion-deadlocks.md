---
title: "Supuesto Práctico Oficial TAI: IEEE 754, Paginación de Memoria y Algoritmo del Banquero (Bloque II)"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-2
  - hardware
  - ieee-754
  - sistemas-operativos
  - memoria-virtual
  - deadlocks
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Supuesto Práctico Bloque 2 TAI"
  - "Ejercicios Resueltos SO y Hardware TAI"
---

# 🔴 Supuesto Práctico Oficial TAI: IEEE 754, Paginación y Algoritmo del Banquero

Cuaderno de ejercicios técnicos resueltos paso a paso típicos de preguntas de cálculo y supuestos prácticos de Bloque II.

---

## 🧮 Ejercicio 1: Representación en Coma Flotante IEEE 754 (Simple Precisión - 32 bits)

### Enunciado:
Representar el número decimal **$-13,625$** en formato IEEE 754 de 32 bits (Simple Precisión) y obtener su expresión en código **Hexadecimal**.

### Resolución Paso a Paso:

1. **Bit de Signo ($S$)**:
   - Como el número es negativo: **$S = 1$**.

2. **Conversión a Binario Puro**:
   - Parte entera ($13_{10}$): $13 = 8 + 4 + 1 = \mathbf{1101_2}$.
   - Parte fraccionaria ($0,625_{10}$):
     - $0,625 	imes 2 = 1,25 ightarrow \mathbf{1}$
     - $0,25 	imes 2 = 0,5 ightarrow \mathbf{0}$
     - $0,5 	imes 2 = 1,0 ightarrow \mathbf{1}$
     - Fracción binaria: $\mathbf{0,101_2}$.
   - Número completo: $-1101,101_2$.

3. **Normalización en Notación Científica Binaria ($1,M 	imes 2^E$)**:
   $$-1101,101_2 = -1,101101_2 	imes 2^3$$
   - Exponente real: $e = 3$.
   - Mantisa ($M$): $101101$ (el 1 inicial queda implícito).

4. **Cálculo del Exponente Sesgado ($E$)**:
   - En simple precisión el sesgo es $127$:
     $$E = e + 127 = 3 + 127 = 130_{10} = \mathbf{10000010_2}$$

5. **Ensamblado de los 32 bits**:
   - Signo (1 bit): `1`
   - Exponente (8 bits): `10000010`
   - Mantisa (23 bits): `10110100000000000000000`

   Cadena binaria de 32 bits:
   `1100 0001 0101 1010 0000 0000 0000 0000`

6. **Conversión a Hexadecimal**:
   - `1100` = `C`
   - `0001` = `1`
   - `0101` = `5`
   - `1010` = `A`
   - `0000` = `0`
   - `0000` = `0`
   - `0000` = `0`
   - `0000` = `0`

   $$\mathbf{Resultado:}\quad 	ext{0xC15A0000}$$

---

## 🧮 Ejercicio 2: Algoritmos de Reemplazo de Páginas (FIFO vs LRU)

### Enunciado:
Un sistema operativo gestiona una memoria física con **3 marcos de página** (*Frames*) inicialmente vacíos.
La secuencia de referencias a páginas que solicita un proceso es:
$$\mathbf{7, 0, 1, 2, 0, 3, 0, 4, 2, 3}$$

Calcular el número total de **Fallos de Página** (*Page Faults*) mediante los algoritmos **FIFO** y **LRU**.

---

### A. Algoritmo FIFO (First-In, First-Out)

| Paso | Referencia | Marco 1 | Marco 2 | Marco 3 | ¿Fallo de Página? | Notas |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | **7** | [7] | - | - | **SÍ (Fallo 1)** | Entra 7 |
| 2 | **0** | [7] | [0] | - | **SÍ (Fallo 2)** | Entra 0 |
| 3 | **1** | [7] | [0] | [1] | **SÍ (Fallo 3)** | Entra 1 (memoria llena) |
| 4 | **2** | [2] | [0] | [1] | **SÍ (Fallo 4)** | Sale el más antiguo (7), entra 2 |
| 5 | **0** | [2] | [0] | [1] | **NO (Acierto)** | 0 ya está en Marco 2 |
| 6 | **3** | [2] | [3] | [1] | **SÍ (Fallo 5)** | Sale el siguiente más antiguo (0), entra 3 |
| 7 | **0** | [2] | [3] | [0] | **SÍ (Fallo 6)** | Sale 1, entra 0 |
| 8 | **4** | [4] | [3] | [0] | **SÍ (Fallo 7)** | Sale 2, entra 4 |
| 9 | **2** | [4] | [2] | [0] | **SÍ (Fallo 8)** | Sale 3, entra 2 |
| 10 | **3** | [4] | [2] | [3] | **SÍ (Fallo 9)** | Sale 0, entra 3 |

$$	ext{Total Fallos FIFO} = \mathbf{9	ext{ Fallos de Página}}$$

---

### B. Algoritmo LRU (Least Recently Used)

| Paso | Referencia | Marco 1 | Marco 2 | Marco 3 | ¿Fallo de Página? | Notas (Uso reciente) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | **7** | [7] | - | - | **SÍ (Fallo 1)** | Entra 7 |
| 2 | **0** | [7] | [0] | - | **SÍ (Fallo 2)** | Entra 0 |
| 3 | **1** | [7] | [0] | [1] | **SÍ (Fallo 3)** | Entra 1 |
| 4 | **2** | [2] | [0] | [1] | **SÍ (Fallo 4)** | Menos usado recientemente es 7; sale 7 |
| 5 | **0** | [2] | [0] | [1] | **NO (Acierto)** | 0 se refresca como el más reciente |
| 6 | **3** | [2] | [0] | [3] | **SÍ (Fallo 5)** | Menos usado recientemente es 1; sale 1 |
| 7 | **0** | [2] | [0] | [3] | **NO (Acierto)** | 0 ya está en memoria |
| 8 | **4** | [4] | [0] | [3] | **SÍ (Fallo 6)** | Menos usado recientemente es 2; sale 2 |
| 9 | **2** | [4] | [0] | [2] | **SÍ (Fallo 7)** | Menos usado recientemente es 3; sale 3 |
| 10 | **3** | [4] | [3] | [2] | **SÍ (Fallo 8)** | Menos usado recientemente es 0; sale 0 |

$$	ext{Total Fallos LRU} = \mathbf{8	ext{ Fallos de Página}}$$

---

## 🧮 Ejercicio 3: Algoritmo del Banquero de Dijkstra (Evasión de Deadlocks)

### Enunciado:
Un sistema dispone de 3 tipos de recursos: $A$ (10 unidades), $B$ (5 unidades) y $C$ (7 unidades).
El estado actual de asignación y demanda máxima es:

| Proceso | Asignación Actual ($A, B, C$) | Demanda Máxima ($A, B, C$) | Necesidad Restante ($Need = Max - Alloc$) |
|:---|:---:|:---:|:---:|
| **P0** | $(0, 1, 0)$ | $(7, 5, 3)$ | $(7, 4, 3)$ |
| **P1** | $(2, 0, 0)$ | $(3, 2, 2)$ | $(1, 2, 2)$ |
| **P2** | $(3, 0, 2)$ | $(9, 0, 2)$ | $(6, 0, 0)$ |
| **P3** | $(2, 1, 1)$ | $(2, 2, 2)$ | $(0, 1, 1)$ |
| **P4** | $(0, 0, 2)$ | $(4, 3, 3)$ | $(4, 3, 1)$ |

Recursos Totales Disponibles inicialmente:
$$Available = Total - \sum Alloc = (10, 5, 7) - (7, 2, 5) = \mathbf{(3, 3, 2)}$$

### Pregunta:
¿Se encuentra el sistema en un **Estado Seguro**? Encuentre una secuencia segura de ejecución.

### Resolución:
1. Con $Available = (3, 3, 2)$:
   - ¿Puede ejecutarse $P0$? $Need(7, 4, 3) \le (3, 3, 2) ightarrow$ NO.
   - ¿Puede ejecutarse $P1$? $Need(1, 2, 2) \le (3, 3, 2) ightarrow$ **SÍ**.
     - $P1$ termina y libera sus recursos:
       $$Available = (3, 3, 2) + (2, 0, 0) = \mathbf{(5, 3, 2)}$$
2. Con $Available = (5, 3, 2)$:
   - ¿Puede ejecutarse $P3$? $Need(0, 1, 1) \le (5, 3, 2) ightarrow$ **SÍ**.
     - $P3$ termina y libera sus recursos:
       $$Available = (5, 3, 2) + (2, 1, 1) = \mathbf{(7, 4, 3)}$$
3. Con $Available = (7, 4, 3)$:
   - ¿Puede ejecutarse $P0$? $Need(7, 4, 3) \le (7, 4, 3) ightarrow$ **SÍ**.
     - $P0$ termina y libera sus recursos:
       $$Available = (7, 4, 3) + (0, 1, 0) = \mathbf{(7, 5, 3)}$$
4. Con $Available = (7, 5, 3)$:
   - ¿Puede ejecutarse $P2$? $Need(6, 0, 0) \le (7, 5, 3) ightarrow$ **SÍ**.
     - $P2$ termina y libera sus recursos:
       $$Available = (7, 5, 3) + (3, 0, 2) = \mathbf{(10, 5, 5)}$$
5. Con $Available = (10, 5, 5)$:
   - ¿Puede ejecutarse $P4$? $Need(4, 3, 1) \le (10, 5, 5) ightarrow$ **SÍ**.
     - $P4$ termina y todos los procesos finalizan.

$$\mathbf{Conclusión:}\quad 	ext{El sistema está en ESTADO SEGURO con la secuencia }\langle P1, P3, P0, P2, P4 angle.$$
