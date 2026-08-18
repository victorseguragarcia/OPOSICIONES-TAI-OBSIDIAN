---
title: "Resumen Completo Tema 10 (Bloque 4): Seguridad Perimetral, Firewall IPTables, IDS/IPS y VPN"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-10
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema10]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|⬅️ Tema 09]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏁 Fin de Bloque ➡️]]

# 🔴 Resumen Completo Tema 10 (Bloque 4): Seguridad Perimetral, Firewall IPTables, IDS/IPS y VPN

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 10**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema profundiza en los fundamentos de las redes de área local (LAN): topologías físicas y lógicas (bus, estrella, estrella extendida, anillo, doble anillo, malla, árbol, celular), la arquitectura y subcapas del comité **IEEE 802** (subcapa LLC 802.2 y subcapa MAC 802.3/802.11), los protocolos de control de acceso al medio compartido (**CSMA/CD** con algoritmo de retroceso exponencial binario y **CSMA/CA** con marcos RTS/CTS), la evolución de los estándares Ethernet (10BASE-T hasta 400GBASE-R), formatos de trama Ethernet II y 802.3, y técnicas de conmutación en switches (*Store-and-Forward*, *Cut-Through*, *Fragment-Free*).

---

## 🧩 Estructura y Desglose Temático

### 1. Topologías de Red (Físicas y Lógicas)
- **Topología en Bus**: Todos los nodos conectados a un medio compartido común con terminadores en los extremos (50 ohmios en coaxial). Ventaja: simplicidad y bajo coste inicial. Desventaja: una rotura del cable interrumpe toda la red; colisiones elevadas bajo carga.
- **Topología en Estrella**: Todos los nodos conectados a un nodo central concentrador (Hub o Switch). Ventaja: el fallo de un cable afecta solo a ese nodo; fácil diagnóstico y aislamiento. Desventaja: punto único de fallo en el concentrador central.
- **Topología en Estrella Extendida**: Jerarquía de estrellas donde conmutadores secundarios se conectan a un conmutador central/distribuidor.
- **Topología en Anillo (Ring)**: Los nodos se conectan en un circuito cerrado unidireccional donde la señal se regenera en cada nodo (ej. Token Ring IEEE 802.5, FDDI con doble anillo contrarrotatorio tolerante a cortes de fibra).
- **Topología en Malla (Mesh)**:
  - Malla Completa: Cada nodo conectado directamente a todos los demás. Número de enlaces: `N * (N - 1) / 2`. Máxima redundancia y tolerancia a fallos.
  - Malla Parcial: Interconexión redundante solo entre nodos críticos.
- **Topología en Árbol (Tree)**: Estructura jerárquica con nodo raíz y nodos hojas; común en redes corporativas con capas Núcleo (*Core*), Distribución y Acceso.
- **Topología Celular**: División geográfica en celdas hexagonales con estación base central (telefonía móvil, redes de sensores).

### 2. Estructura y Subcapas del Comité IEEE 802
El proyecto IEEE 802 divide la **Capa de Enlace de Datos (Nivel 2 de OSI)** en dos subcapas complementarias:
1. **Subcapa Superior: LLC (Logical Link Control - IEEE 802.2)**:
   - Proporciona una interfaz uniforme e independiente del medio físico a la capa de red (Nivel 3).
   - Utiliza puntos de acceso al servicio (**SAP**: SSAP y DSAP).
   - Tipos de servicio: Tipo 1 (No orientado a conexión sin acuse), Tipo 2 (Orientado a conexión con acuse), Tipo 3 (No orientado a conexión con acuse).
2. **Subcapa Inferior: MAC (Media Access Control)**:
   - Responsable del direccionamiento físico (direcciones MAC de 48 bits), delimitación de tramas, detección de errores (FCS / CRC-32) y control de acceso al medio de transmisión.

#### 2.1 Principales Estándares del Comité IEEE 802
- **IEEE 802.1**: Arquitectura general de redes, gestión, puenteo (*Bridging*) y protocolos:
  - **802.1D**: Protocolo Spanning Tree (STP).
  - **802.1w**: Rapid Spanning Tree Protocol (RSTP).
  - **802.1Q**: Etiquetado de VLANs (añade tag de 4 bytes con VLAN ID de 12 bits: 1 a 4094).
  - **802.1X**: Control de acceso a la red basado en puertos (Autenticación EAP con servidor RADIUS).
  - **802.1AX / 802.3ad**: Agregación de enlaces (LACP - Link Aggregation Control Protocol).
- **IEEE 802.2**: Logical Link Control (LLC).
- **IEEE 802.3**: Redes CSMA/CD (Ethernet cableado).
- **IEEE 802.5**: Token Ring (paso de testigo, en desuso).
- **IEEE 802.11**: Redes inalámbricas WLAN (Wi-Fi).
- **IEEE 802.15**: Redes de área personal inalámbricas (WPAN: 802.15.1 Bluetooth, 802.15.4 Zigbee).
- **IEEE 802.16**: Acceso inalámbrico de banda ancha (WiMAX).

### 3. Protocolos de Control de Acceso al Medio (MAC)

#### 3.1 CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
- Protocolo de contienda utilizado en Ethernet clásico sobre medios compartidos (Half-Duplex).
- **Mecanismo de Funcionamiento**:
  1. **Escucha (*Carrier Sense*)**: El nodo escucha el canal antes de transmitir (*Listen Before Talk*).
  2. **Transmisión**: Si el canal está libre (*Idle*), comienza a transmitir. Si está ocupado, espera.
  3. **Detección de Colisión**: Mientras transmite, sigue escuchando el medio. Si dos nodos transmiten a la vez, se detecta un aumento anómalo de voltaje (colisión).
  4. **Señal de Atasco (*Jam Signal*)**: El nodo emite una ráfaga de 32 a 48 bits de señal *Jam* para asegurar que todos los demás nodos detecten la colisión.
  5. **Algoritmo de Retroceso Exponencial Binario (BEB - *Binary Exponential Backoff*)**:
     - Tras la colisión número $k$ (donde $k = \min(n, 10)$ en el intento $n$), el nodo espera un tiempo aleatorio $r$ intervalos de ranura (*slot time* de 512 bits = 51.2 µs en Ethernet 10 Mbps), donde $r \in [0, 2^k - 1]$.
     - Si tras **16 colisiones consecutivas** no se logra transmitir, se descarta la trama y se reporta error a la capa superior.
- **Tamaño Mínimo de Trama en Ethernet**:
  - Fijado en **64 bytes (512 bits)** para asegurar que el emisor siga transmitiendo cuando la señal reflejada por una colisión en el extremo más alejado de la red regrese al emisor (*Slot Time > 2 * Tiempo de propagación máximo*). Tramas menores a 64 bytes son descartadas como *Runt Frames*.

#### 3.2 CSMA/CA (Collision Avoidance)
- Utilizado en redes inalámbricas Wi-Fi (IEEE 802.11) donde la detección física de colisiones es inviable debido a que el emisor satura su propio receptor (*Problema del Nodo Oculto*).
- Utiliza tiempos de espera intertramas (**IFS**: SIFS, PIFS, DIFS) y opcionalmente el mecanismo de reserva de canal mediante tramas de control **RTS** (*Request to Send*) y **CTS** (*Clear to Send*) con vector de reserva virtual **NAV** (*Network Allocation Vector*).

### 4. Formato de Trama Ethernet y Métodos de Conmutación
- **Estructura de Trama Ethernet II (DIX v2)**:
  - **Preámbulo**: 7 bytes de sincronismo (`10101010`).
  - **SFD (Start Frame Delimiter)**: 1 byte (`10101011`).
  - **MAC Destino**: 6 bytes (48 bits).
  - **MAC Origen**: 6 bytes (48 bits).
  - **EtherType**: 2 bytes (indica el protocolo de capa 3: `0x0800` IPv4, `0x86DD` IPv6, `0x8100` VLAN 802.1Q, `0x0806` ARP).
  - **Payload (Datos)**: 46 a 1500 bytes (MTU estándar de 1500 bytes; tramas *Jumbo Frames* soportan hasta 9000 bytes).
  - **FCS (Frame Check Sequence)**: 4 bytes (código de redundancia cíclica CRC-32).
  - **Tamaño total de trama**: Mínimo **64 bytes**, máximo **1518 bytes** (1522 bytes con etiqueta VLAN 802.1Q).
- **Métodos de Reenvío en Switches**:
  - **Store-and-Forward**: El switch recibe la trama completa, verifica el CRC-32 en el FCS y, si no tiene errores, la reenvía. Mayor latencia, máxima fiabilidad (descarta tramas corruptas).
  - **Cut-Through (Fast-Forward)**: El switch lee solo los primeros 6 bytes (MAC destino) e inmediatamente empieza a reenviar la trama sin verificar errores. Mínima latencia.
  - **Fragment-Free**: Lee los primeros **64 bytes** (tamaño mínimo) para filtrar colisiones antes de reenviar.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Estándar | Especificación Técnica |
|----------------------|------------------------|
| Subcapas Capa Enlace IEEE 802 | **LLC (802.2)** + **MAC (802.3 / 802.11)** |
| Tamaño Mínimo Trama Ethernet | **64 bytes** (512 bits / Slot Time) |
| Tamaño Máximo Trama Ethernet | **1518 bytes** estándar (**1522 bytes** con 802.1Q) |
| MTU Estándar Ethernet | **1500 bytes** |
| Max Intentos Colisión CSMA/CD | **16 intentos** (Backoff exponencial hasta intento 10: $2^{10} = 1024$) |
| EtherType IPv4 / IPv6 / ARP | `0x0800` (IPv4), `0x86DD` (IPv6), `0x0806` (ARP), `0x8100` (802.1Q) |
| Enlaces en Malla Completa | `N * (N - 1) / 2` |
| Estándar Etiquetado VLAN | **IEEE 802.1Q** (Tag de 4 bytes, VLAN ID 12 bits = 4094 VLANs) |
| Estándar Autenticación Puertos | **IEEE 802.1X** (EAP / RADIUS) |
| Estándar Spanning Tree | **IEEE 802.1D** (STP clásico) / **IEEE 802.1w** (RSTP rápido) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- [[wiki/entities/wi-fi-and-mobile-standards|Estándares Wi-Fi y Redes Inalámbricas]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos y Conmutación Segura]]

### Conceptos Teóricos:
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema10|Nota Fuente del Tema 10]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema10-topologias-ieee802-wifi|Test Tema 10]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|⬅️ Tema 09]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏁 Fin de Bloque ➡️]]
