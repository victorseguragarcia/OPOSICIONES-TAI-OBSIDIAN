---
title: "Resumen Exhaustivo Tema 06 (Bloque 4): Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-06
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema06.md]]"
  - "[[wiki/sources/bloque4-tema06]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|⬅️ Tema 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|Tema 07 ➡️]]

# 🔴 Resumen Exhaustivo Tema 06 (Bloque 4): Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 06**
> Medios guiados (Par trenzado UTP/FTP/STP Cat 5e/6/6A/7/8, Fibra Óptica Monomodo vs Multimodo), estándar IEEE 802.3 Ethernet (CSMA/CD, Fast/Gigabit/10GbE), estándares Wi-Fi IEEE 802.11 (Wi-Fi 4/5/6/6E/7, OFDMA, MU-MIMO), conmutación de paquetes, Spanning Tree Protocol (STP 802.1D / RSTP 802.1w) y VLANs (IEEE 802.1Q).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Medios de Transmisión Guiados: Cobre y Fibra Óptica
- **Cables de Par Trenzado (Twisted Pair)**:
  - *Categorías*: Cat 5e (100 MHz, 1 Gbps a 100m), Cat 6 (250 MHz, 1 Gbps a 100m / 10 Gbps a 55m), **Cat 6A (500 MHz, 10 Gbps a 100m)**, Cat 7 (600 MHz, 10 Gbps), Cat 8 (2000 MHz, 25/40 Gbps a 30m).
  - *Apantallamiento*: UTP (sin apantallar), FTP (pantalla global de lámina), STP (pantalla por par), S/FTP (pantalla por par + malla global).
  - Conector estándar: **RJ-45** con normas de cableado **T568A** y **T568B**.
- **Fibra Óptica**:

| Característica | Fibra Óptica Monomodo (SMF - Single Mode Fiber) | Fibra Óptica Multimodo (MMF - Multi Mode Fiber) |
|:---|:---|:---|
| **Diámetro del Núcleo** | Muy fino: **$9 \ \mu\text{m}$** (Revestimiento estándar $125 \ \mu\text{m}$). | Más grueso: **$50 \ \mu\text{m}$** o **$62.5 \ \mu\text{m}$** ($50/125$ o $62.5/125$). |
| **Fuente de Luz** | **Láser (Diodo Láser)** (longitudes de onda $1310\text{ nm}$ y $1550\text{ nm}$). | **LED** o **VCSEL** (longitudes de onda $850\text{ nm}$ y $1300\text{ nm}$). |
| **Dispersión Modal** | ❌ **NULA** (la luz viaja en un único rayo recto paralelo). | ⚠️ **Alta dispersión modal** (múltiples rayos rebotando). |
| **Distancia Máxima** | **Largas distancias (WAN, enlaces MAN, decenas de km)**. | **Distancias cortas / medias (CPD, LANs de campus, hasta 300-550m)**. |

### 2. Redes LAN Ethernet (IEEE 802.3) y Redes Inalámbricas Wi-Fi (IEEE 802.11)
- **Ethernet (IEEE 802.3)**:
  - Protocolo de acceso al medio: **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**. En redes conmutadas (*Switched Ethernet*) en modo Full-Duplex se eliminan las colisiones.
  - *Estructura de la Trama Ethernet II*: Preámbulo (7 bytes) + SFD (1 byte) + **MAC Destino (6 bytes)** + **MAC Origen (6 bytes)** + **EtherType (2 bytes)** + **Datos Payload (46 a 1500 bytes)** + **FCS / CRC (4 bytes)**. Tamaño total: Mínimo **64 bytes**, Máximo **1518 bytes** (sin tags VLAN).
- **Evolución de Estándares Wi-Fi (IEEE 802.11)**:

| Generación Wi-Fi | Estándar IEEE | Bandas de Frecuencia | Velocidad Máxima Teórica | Tecnologías Clave de Rendimiento |
|:---|:---|:---|:---:|:---|
| **Wi-Fi 4** | **802.11n** | 2,4 GHz y 5 GHz | 600 Mbps | MIMO (Multiple Input Multiple Output), canales de 40 MHz. |
| **Wi-Fi 5** | **802.11ac** | **Exclusivamente 5 GHz** | 6,9 Gbps | MU-MIMO (Downlink), canales de 80 y 160 MHz, modulación 256-QAM. |
| **Wi-Fi 6** | **802.11ax** | 2,4 GHz y 5 GHz | **9,6 Gbps** | **OFDMA**, **MU-MIMO bidireccional (UL/DL)**, 1024-QAM, BSS Coloring, TWT. |
| **Wi-Fi 6E** | 802.11ax extendido | 2,4 GHz, 5 GHz y **6 GHz** | 9,6 Gbps | Añade la banda limpia de 6 GHz (canales sin interferencias). |
| **Wi-Fi 7** | **802.11be** | 2,4 GHz, 5 GHz y 6 GHz | **hasta 46 Gbps** | Canales de 320 MHz, 4096-QAM, MLO (Multi-Link Operation). |

### 3. Redes Virtuales VLAN (IEEE 802.1Q) y Spanning Tree (STP)
- **VLANs (Virtual Local Area Networks)**: Segmentan el dominio de broadcast en el switch a nivel 2 de enlace.
  - *Etiquetado IEEE 802.1Q*: Añade una cabecera de **4 bytes** a la trama Ethernet (incluye el **VLAN ID de 12 bits**, permitiendo hasta **4096 VLANs** - $0$ a $4095$, reservadas 0 y 4095).
  - *Tipos de Puertos*: **Access Port** (tráfico sin etiquetar de 1 sola VLAN) vs **Trunk Port** (transporta múltiples VLANs etiquetadas con 802.1Q).
- **Spanning Tree Protocol (STP - IEEE 802.1D / RSTP 802.1w)**: Algoritmo que desactiva enlaces redundantes en la red de conmutadores para **evitar bucles de nivel 2 y tormentas de broadcast**, seleccionando un *Root Bridge* (Puente Raíz).

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 06 (Bloque 4)**
> 1. **Tamaño Mínimo y Máximo de Trama Ethernet**: Mínimo **64 bytes** (payload mínimo 46 bytes); Máximo **1518 bytes** (sin 802.1Q) o **1522 bytes** (con tag 802.1Q de 4 bytes).
> 2. **VLAN ID en 802.1Q**: Tiene **12 bits** de longitud (permite hasta 4096 VLANs).
> 3. **Wi-Fi 5 (802.11ac)**: Funciona **ÚNICAMENTE en la banda de 5 GHz** (no opera en 2,4 GHz; el 802.11ax Wi-Fi 6 volvió a operar en ambas).
> 4. **Fibra Monomodo vs Multimodo**: Monomodo tiene núcleo pequeño ($9\ \mu\text{m}$) y usa **Láser**; Multimodo tiene núcleo grande ($50/62.5\ \mu\text{m}$) y usa **LED/VCSEL**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Fibra**: **Monomodo $=$ 9 micras $+$ Láser $+$ Larga distancia** / **Multimodo $=$ 50 micras $+$ LED $+$ Corta distancia**.
> - **Tag 802.1Q**: **4 Bytes Totales / 12 Bits para VLAN ID**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema06|Fuente Oficial del Tema 06]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema06|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema06-medios-transmision-fibra|Test Tema 06]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|⬅️ Tema 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|Tema 07 ➡️]]
