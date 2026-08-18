---
title: "Tarjetas de Memoria Rápida (Flashcards): Bloque 4 - Sistemas, Redes, Comunicaciones y Seguridad"
type: "synthesis"
tags:
  - flashcards
  - tarjetas-memoria
  - active-recall
  - bloque-4
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Tarjetas de Memoria Rápida (Flashcards): Bloque 4 - Sistemas, Redes, Comunicaciones y Seguridad

> [!info] 🧠 **Modo de Estudio con Tarjetas (Active Recall & Spaced Repetition)**
> Intenta responder mentalmente a la pregunta antes de desplegar el bloque de solución. Compatible con el formato estándar de tarjetas de Obsidian (`Pregunta :: Respuesta`).

### 🃏 Tarjeta 01: ¿En qué puertos operan respectivamente DNS, DHCP y Kerberos?
**Pregunta / Anverso**:: **DNS: 53 (UDP/TCP) | DHCP: 67/68 (UDP) | Kerberos: 88 (TCP/UDP)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **DNS: 53 (UDP/TCP) | DHCP: 67/68 (UDP) | Kerberos: 88 (TCP/UDP)**
> 
> 💡 **Explicación / Norma**: DNS usa TCP para transferencias de zona > 512 bytes; DHCP cliente 68 / servidor 67.

---

### 🃏 Tarjeta 02: ¿En qué puertos operan IMAPS y POP3S (seguros sobre TLS)?
**Pregunta / Anverso**:: **IMAPS: 993 | POP3S: 995**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **IMAPS: 993 | POP3S: 995**
> 
> 💡 **Explicación / Norma**: Versiones inseguras: IMAP 143 / POP3 110. SMTP envío cliente seguro: 587 (Submission) / 465.

---

### 🃏 Tarjeta 03: ¿Cuál es la fórmula de cálculo de Hosts Útiles en una subred IPv4 con $h$ bits de host?
**Pregunta / Anverso**:: **$2^h - 2$**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **$2^h - 2$**
> 
> 💡 **Explicación / Norma**: Se restan 2: la dirección de red (todo ceros) y la de broadcast (todo unos). En `/27` $\implies 30$ hosts.

---

### 🃏 Tarjeta 04: ¿Existe la dirección de Broadcast en IPv6?
**Pregunta / Anverso**:: **NO, en IPv6 no existe broadcast**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **NO, en IPv6 no existe broadcast**
> 
> 💡 **Explicación / Norma**: Se sustituye por Anycast y Multicast (ej. `ff02::1` todos los nodos).

---

### 🃏 Tarjeta 05: ¿Cuál es el tamaño fijo de la cabecera base de IPv6?
**Pregunta / Anverso**:: **40 bytes fijos**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **40 bytes fijos**
> 
> 💡 **Explicación / Norma**: IPv4 tiene longitud variable de 20 a 60 bytes. IPv6 usa cabeceras de extensión encadenadas (*Next Header*).

---

### 🃏 Tarjeta 06: ¿Cuáles son las 5 Dimensiones de Seguridad del ENS RD 311/2022 (DADIT)?
**Pregunta / Anverso**:: **Disponibilidad, Autenticidad, Integridad, Confidencialidad, Trazabilidad**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Disponibilidad, Autenticidad, Integridad, Confidencialidad, Trazabilidad**
> 
> 💡 **Explicación / Norma**: La categoría del sistema (Básica, Media, Alta) se rige por la **regla del máximo**.

---

### 🃏 Tarjeta 07: ¿Con qué clave se genera y con cuál se verifica una Firma Digital?
**Pregunta / Anverso**:: **Se genera con la CLAVE PRIVADA del emisor y se verifica con la CLAVE PÚBLICA del emisor**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Se genera con la CLAVE PRIVADA del emisor y se verifica con la CLAVE PÚBLICA del emisor**
> 
> 💡 **Explicación / Norma**: Garantiza autenticidad, integridad y no repudio.

---

### 🃏 Tarjeta 08: ¿Cuál es la capacidad útil y tolerancia a fallos de un RAID 5 con $N$ discos de tamaño $S$?
**Pregunta / Anverso**:: **Capacidad: $(N-1) \times S$ | Tolerancia: 1 disco**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **Capacidad: $(N-1) \times S$ | Tolerancia: 1 disco**
> 
> 💡 **Explicación / Norma**: Requiere mínimo 3 discos y distribuye la paridad entre todos ellos.

---

### 🃏 Tarjeta 09: ¿Qué estándar IEEE define el etiquetado de tramas para VLANs (*Trunking*)?
**Pregunta / Anverso**:: **IEEE 802.1Q**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **IEEE 802.1Q**
> 
> 💡 **Explicación / Norma**: Inserta una etiqueta de 4 bytes en la trama Ethernet con el VLAN ID (12 bits, hasta 4094 VLANs).

---

### 🃏 Tarjeta 10: ¿Qué algoritmo de prevención de bucles en conmutación define IEEE 802.1D?
**Pregunta / Anverso**:: **STP (Spanning Tree Protocol)**
> [!question]- 🔍 Ver Solución y Fundamento Oficial
> **Respuesta Directa**: **STP (Spanning Tree Protocol)**
> 
> 💡 **Explicación / Norma**: Bloquea enlaces redundantes para evitar tormentas de difusión (*broadcast storms*).
