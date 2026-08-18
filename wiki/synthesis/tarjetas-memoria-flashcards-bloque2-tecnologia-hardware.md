---
title: "Tarjetas de Memoria Rápida (Flashcards): Bloque 2 - Tecnología Básica, Hardware, SO y SGBD"
type: "synthesis"
tags:
  - flashcards
  - tarjetas-memoria
  - active-recall
  - bloque-2
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Tarjetas de Memoria Rápida (Flashcards): Bloque 2 - Tecnología Básica, Hardware, SO y SGBD

> [!info] 🧠 **Modo de Estudio con Tarjetas (Active Recall & Spaced Repetition)**
> Intenta responder mentalmente a la pregunta antes de desplegar el bloque de solución. Compatible con el formato estándar de tarjetas de Obsidian (`Pregunta :: Respuesta`).

### 🃏 Tarjeta 01: ¿Cuál es el rango representable en Complemento a 2 para $n$ bits?
**Pregunta / Anverso**:: **$[-2^{n-1}, +(2^{n-1}-1)]$**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **$[-2^{n-1}, +(2^{n-1}-1)]$**
> 
> 💡 **Explicación / Norma**: Para 8 bits: de -128 a +127 (cero único '00000000').

---

### 🃏 Tarjeta 02: ¿Cuál es el sesgo (*bias*) del exponente en IEEE 754 Simple Precisión (32 bits)?
**Pregunta / Anverso**:: **127 ($2^{8-1}-1$)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **127 ($2^{8-1}-1$)**
> 
> 💡 **Explicación / Norma**: 1 bit signo, 8 bits exponente ($e+127$), 23 bits mantisa con bit implícito '1.'.

---

### 🃏 Tarjeta 03: ¿Cuál es el sesgo del exponente en IEEE 754 Doble Precisión (64 bits)?
**Pregunta / Anverso**:: **1023 ($2^{11-1}-1$)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **1023 ($2^{11-1}-1$)**
> 
> 💡 **Explicación / Norma**: 1 bit signo, 11 bits exponente, 52 bits mantisa.

---

### 🃏 Tarjeta 04: ¿Qué bus de expansión serie utiliza carriles punto a punto dúplex (x1, x4, x8, x16)?
**Pregunta / Anverso**:: **PCI Express (PCIe)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **PCI Express (PCIe)**
> 
> 💡 **Explicación / Norma**: PCIe 4.0 rinde ~2 GB/s por carril; PCIe 5.0 rinde ~4 GB/s por carril.

---

### 🃏 Tarjeta 05: ¿Qué protocolo de interfaz SSD NVMe opera sobre el bus PCIe sustituyendo a AHCI?
**Pregunta / Anverso**:: **NVMe (Non-Volatile Memory Express)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **NVMe (Non-Volatile Memory Express)**
> 
> 💡 **Explicación / Norma**: Soporta hasta 64.000 colas con 64.000 comandos cada una frente a 1 cola de 32 comandos en AHCI.

---

### 🃏 Tarjeta 06: ¿En qué algoritmo de reemplazo de páginas se produce la Anomalía de Bélády?
**Pregunta / Anverso**:: **En el algoritmo FIFO (First-In, First-Out)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **En el algoritmo FIFO (First-In, First-Out)**
> 
> 💡 **Explicación / Norma**: Aumentar marcos de memoria física puede aumentar el número de fallos de página (LRU y OPT son inmunes).

---

### 🃏 Tarjeta 07: ¿Qué función realiza la MMU (Memory Management Unit)?
**Pregunta / Anverso**:: **Traduce direcciones lógicas/virtuales a físicas y gestiona la protección de memoria**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Traduce direcciones lógicas/virtuales a físicas y gestiona la protección de memoria**
> 
> 💡 **Explicación / Norma**: Utiliza la tabla de páginas y la memoria caché TLB (Translation Lookaside Buffer).

---

### 🃏 Tarjeta 08: ¿Qué estructura de datos es un Árbol AVL?
**Pregunta / Anverso**:: **Un Árbol Binario de Búsqueda auto-balanceado con factor de equilibrio $\in \{-1, 0, +1\}$**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Un Árbol Binario de Búsqueda auto-balanceado con factor de equilibrio $\in \{-1, 0, +1\}$**
> 
> 💡 **Explicación / Norma**: Garantiza operaciones de búsqueda, inserción y borrado en tiempo $O(\log n)$.

---

### 🃏 Tarjeta 09: ¿Qué 2 garantías elige un sistema distribuido según el Teorema CAP?
**Pregunta / Anverso**:: **Solo 2 de 3: Consistencia (C), Disponibilidad (A) o Tolerancia a Particiones (P)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Solo 2 de 3: Consistencia (C), Disponibilidad (A) o Tolerancia a Particiones (P)**
> 
> 💡 **Explicación / Norma**: En la práctica se eligen sistemas CP (MongoDB) o AP (Cassandra/Redis).

---

### 🃏 Tarjeta 10: ¿Qué familia NoSQL es Apache Cassandra y ScyllaDB?
**Pregunta / Anverso**:: **Columnares / Wide-Column (Familias de Columnas)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Columnares / Wide-Column (Familias de Columnas)**
> 
> 💡 **Explicación / Norma**: Optimizadas para escrituras masivas de series temporales y Big Data.
