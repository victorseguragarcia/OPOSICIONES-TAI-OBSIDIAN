---
title: "Tarjetas de Memoria Rápida (Flashcards): Bloque 3 - Desarrollo de Sistemas, Web, BBDD y QA"
type: "synthesis"
tags:
  - flashcards
  - tarjetas-memoria
  - active-recall
  - bloque-3
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Tarjetas de Memoria Rápida (Flashcards): Bloque 3 - Desarrollo de Sistemas, Web, BBDD y QA

> [!info] 🧠 **Modo de Estudio con Tarjetas (Active Recall & Spaced Repetition)**
> Intenta responder mentalmente a la pregunta antes de desplegar el bloque de solución. Compatible con el formato estándar de tarjetas de Obsidian (`Pregunta :: Respuesta`).

### 🃏 Tarjeta 01: ¿Qué exige la Tercera Forma Normal (3FN)?
**Pregunta / Anverso**:: **Estar en 2FN y que ningún atributo no primo dependa transitivamente de la clave primaria**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Estar en 2FN y que ningún atributo no primo dependa transitivamente de la clave primaria**
> 
> 💡 **Explicación / Norma**: En toda dependencia $X \rightarrow A$, $X$ es superclave o $A$ es atributo primo.

---

### 🃏 Tarjeta 02: ¿Qué diferencia a la Forma Normal de Boyce-Codd (BCNF) de la 3FN?
**Pregunta / Anverso**:: **En BCNF TODO determinante $X$ debe ser estrictamente una superclave (sin excepciones)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **En BCNF TODO determinante $X$ debe ser estrictamente una superclave (sin excepciones)**
> 
> 💡 **Explicación / Norma**: Elimina anomalías cuando existen claves candidatas compuestas superpuestas.

---

### 🃏 Tarjeta 03: ¿Cuál es la fórmula de Complejidad Ciclomática de McCabe?
**Pregunta / Anverso**:: **$V(G) = E - N + 2P$**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **$V(G) = E - N + 2P$**
> 
> 💡 **Explicación / Norma**: $E$ = aristas, $N$ = nodos, $P$ = componentes conexos ($V(G) = \text{Regiones} = \text{Nodos predicado} + 1$).

---

### 🃏 Tarjeta 04: ¿Cuáles son los 4 principios de Accesibilidad Web WCAG 2.1 (regla POUR)?
**Pregunta / Anverso**:: **Perceptible, Operable, Comprensible (*Understandable*) y Robusto**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Perceptible, Operable, Comprensible (*Understandable*) y Robusto**
> 
> 💡 **Explicación / Norma**: El RD 1112/2018 exige Nivel de conformidad **AA** en el sector público.

---

### 🃏 Tarjeta 05: ¿Qué elemento XML es OBLIGATORIO en un mensaje SOAP?
**Pregunta / Anverso**:: **<soap:Body>**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **<soap:Body>**
> 
> 💡 **Explicación / Norma**: <soap:Envelope> contiene opcionalmente <soap:Header> y obligatoriamente <soap:Body>.

---

### 🃏 Tarjeta 06: ¿Qué significa que un método HTTP sea Idempotente?
**Pregunta / Anverso**:: **Que ejecutarlo múltiples veces produce el mismo estado en el servidor que ejecutarlo una sola vez**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Que ejecutarlo múltiples veces produce el mismo estado en el servidor que ejecutarlo una sola vez**
> 
> 💡 **Explicación / Norma**: Son idempotentes: GET, PUT, DELETE, HEAD, OPTIONS. NO es idempotente: POST.

---

### 🃏 Tarjeta 07: ¿Qué patrón GoF garantiza una única instancia de una clase con punto de acceso global?
**Pregunta / Anverso**:: **Patrón Singleton (Creacional)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Patrón Singleton (Creacional)**
> 
> 💡 **Explicación / Norma**: Otros patrones clave: Factory Method, Adapter, Observer, Strategy, Decorator.

---

### 🃏 Tarjeta 08: ¿Qué fase de MÉTRICA v3 diseña la arquitectura física y la interfaz de usuario?
**Pregunta / Anverso**:: **DSI (Diseño del Sistema de Información)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **DSI (Diseño del Sistema de Información)**
> 
> 💡 **Explicación / Norma**: Procesos: EVS, ASI, DSI, CSI, IAS, MSI.

---

### 🃏 Tarjeta 09: ¿Qué comando de Git reescribe la historia aplicando commits sobre una rama base lineal?
**Pregunta / Anverso**:: **`git rebase`**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **`git rebase`**
> 
> 💡 **Explicación / Norma**: `git merge` preserva el historial creando un commit de unión; `git rebase` crea un histórico lineal.
