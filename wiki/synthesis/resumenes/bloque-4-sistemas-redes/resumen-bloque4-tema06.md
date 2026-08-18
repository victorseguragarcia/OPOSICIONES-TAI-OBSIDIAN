---
title: "Resumen Completo Tema 06 (Bloque 4): Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-06
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema06]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|⬅️ Tema 05]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|Tema 07 ➡️]]

# 🔴 Resumen Completo Tema 06 (Bloque 4): Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 06**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema profundiza en los fundamentos de la capa física de comunicaciones: modos de transmisión de datos (Simplex, Half-Duplex, Full-Duplex; Unicast, Multicast, Broadcast, Anycast; síncrona, asíncrona, isócrona), técnicas de multiplexación (FDM, TDM, WDM, DWDM) y modulación analógica/digital (ASK, FSK, PSK, QAM). Analiza detalladamente los medios guiados (par trenzado UTP/FTP/STP y categorías Cat 5e a Cat 8, cable coaxial, fibra óptica monomodo/multimodo y tecnologías FTTH/GPON), sistemas de cableado estructurado según norma ISO/IEC 11801 y TIA/EIA-568, y medios no guiados inalámbricos (estándares Wi-Fi IEEE 802.11a/b/g/n/ac/ax/be y generaciones móviles desde 1G hasta 5G NR).

---

## 🧩 Estructura y Desglose Temático

### 1. Modos de Comunicación y Transmisión
- **Según el Sentido del Flujo**:
  - **Simplex**: Transmisión unidireccional estricta (ej. radiodifusión, televisión comercial).
  - **Semi-Dúplex (Half-Duplex)**: Bidireccional no simultáneo; ambos transmiten pero no al mismo tiempo (ej. Walkie-talkie, CSMA/CD en Ethernet con hubs).
  - **Dúplex Completo (Full-Duplex)**: Bidireccional simultáneo en ambos sentidos (ej. telefonía, Ethernet con conmutadores).
- **Según el Destino**:
  - **Unicast**: Envío de un emisor a un único receptor específico.
  - **Broadcast**: Envío de un emisor a todos los hosts del dominio de difusión (`255.255.255.255`). Inexistente en IPv6 (reemplazado por multicast).
  - **Multicast**: Envío a un grupo suscrito de receptores (IPv4 Clase D `224.0.0.0/4`; IPv6 `ff00::/8`).
  - **Anycast**: Envío al nodo más cercano (según métrica de enrutamiento) de un grupo que comparte la misma dirección IP.
- **Sincronismo de Bits**:
  - **Asíncrona**: Cada carácter lleva bits de inicio (*start bit*) y parada (*stop bit*); relojes emisor/receptor no sincronizados permanentemente.
  - **Síncrona**: Trama continua delimitada por flags; emisor y receptor sincronizados con reloj común o recuperado de la señal.
  - **Isócrona**: Garantía de retardo máximo y tasa constante, esencial para audio/vídeo en tiempo real.

### 2. Multiplexación y Modulación
- **Técnicas de Multiplexación**:
  - **FDM (Frequency Division Multiplexing)**: División del espectro en canales de distinta frecuencia portadora (radio, ADSL).
  - **TDM (Time Division Multiplexing)**: Asignación de ranuras de tiempo (*time slots*) rotativas (telefonía digital PCM, E1/T1). Puede ser síncrona o estadística.
  - **WDM / DWDM (Wavelength Division Multiplexing)**: Multiplexación por longitud de onda en fibra óptica. DWDM (*Dense WDM*) permite cientos de canales ópticos en una sola fibra.
- **Técnicas de Modulación**:
  - Digital sobre portadora analógica: **ASK** (Amplitud), **FSK** (Frecuencia), **PSK** (Fase: BPSK, QPSK), **QAM** (Amplitud en Cuadratura: 16-QAM, 64-QAM, 256-QAM, 1024-QAM, combinando fase y amplitud).

### 3. Medios Guiados de Transmisión

#### 3.1 Par Trenzado de Cobre
- El trenzado reduce interferencias electromagnéticas externas y diafonía (*crosstalk*).
- **Blindajes (ISO/IEC 11801)**:
  - **U/UTP**: Sin apantallar (el más común y económico).
  - **F/UTP**: Pantalla global de papel de aluminio sobre todos los pares.
  - **S/FTP**: Pantalla de malla metálica global + cada par blindado con papel de aluminio (máximo blindaje).
- **Categorías de Cable de Cobre**:
  - **Cat 5e**: Ancho de banda **100 MHz**, soporta Gigabit Ethernet (**1000BASE-T** hasta 100 m).
  - **Cat 6**: Ancho de banda **250 MHz**, soporta 1000BASE-T (100 m) y 10GBASE-T (hasta 55 m).
  - **Cat 6A**: Ancho de banda **500 MHz**, soporta **10GBASE-T** a **100 m**.
  - **Cat 7 / 7A**: Ancho de banda **600 / 1000 MHz** (conectores GG45/TERA).
  - **Cat 8 (8.1 / 8.2)**: Ancho de banda **2000 MHz (2 GHz)**, soporta **25GBASE-T** y **40GBASE-T** (hasta 30 m).
- **Conexiones**: Conector **RJ-45** (8P8C) según esquemas **T568A** y **T568B**.

#### 3.2 Fibra Óptica
- Transmisión de pulsos de luz mediante reflexión interna total en núcleo de sílice/vidrio rodeado de cubierta (*cladding*). Inmune a interferencias electromagnéticas (EMI) y sin radiación de señal.
- **Tipos de Fibra**:
  - **Monomodo (SMF - Single Mode Fiber)**: Núcleo muy pequeño (~9 µm), un solo rayo de luz viaja sin dispersión modal. Fuente: Láser (longitudes de onda **1310 nm** y **1550 nm**). Gran alcance (>10-40 km).
  - **Multimodo (MMF - Multi Mode Fiber)**: Núcleo más grueso (**50 µm** o **62.5 µm**), múltiples modos de propagación sufren dispersión modal. Fuente: LED o VCSEL (longitudes de onda **850 nm** y **1300 nm**). Alcance típico hasta 300-550 m (OM1, OM2, OM3, OM4, OM5).
- **Conectores Ópticos**: SC (*Subscriber Connector*), LC (*Lucent Connector* - estándar en switches SFP), ST (*Straight Tip*), FC (*Ferrule Connector*), MPO/MTP.
- **Topologías FTTx y GPON**:
  - **FTTH (Fiber to the Home)**: Fibra directa hasta la ONT del abonado.
  - **GPON (Gigabit Passive Optical Network - ITU-T G.984)**: Red óptica pasiva punto a multipunto mediante divisores ópticos (*splitters* pasivos sin alimentación). Velocidades: **2.488 Gbps bajada / 1.244 Gbps subida**.
  - **XG-PON / XGS-PON**: GPON de 10 Gbps simétricos.

#### 3.3 Sistema de Cableado Estructurado (SCE)
- Normas: **ISO/IEC 11801**, **ANSI/TIA/EIA-568**.
- Elementos:
  - **Cableado Horizontal**: Desde rosetas de puesto (área de trabajo) hasta el distribuidor de planta (máx **90 m** de cable horizontal fijo + **10 m** de latiguillos = **100 m canal total**).
  - **Cableado Troncal / Backbone (Vertical)**: Interconecta distribuidores de planta con el distribuidor de edificio o de campus (típicamente fibra óptica).
  - Cuarto de telecomunicaciones (*Racks*, paneles de parcheo).

### 4. Comunicaciones Inalámbricas y Móviles
- **Familia Wi-Fi (IEEE 802.11)**:
  - **802.11b** (1999): 2.4 GHz, hasta 11 Mbps (DSSS).
  - **802.11a** (1999): 5 GHz, hasta 54 Mbps (OFDM).
  - **802.11g** (2003): 2.4 GHz, hasta 54 Mbps (OFDM).
  - **802.11n (Wi-Fi 4)** (2009): 2.4 / 5 GHz, hasta 600 Mbps (MIMO).
  - **802.11ac (Wi-Fi 5)** (2013): 5 GHz exclusivo, hasta 6.9 Gbps (MU-MIMO, canales de 80/160 MHz, 256-QAM).
  - **802.11ax (Wi-Fi 6 / 6E)** (2019/2021): 2.4, 5 y **6 GHz** (Wi-Fi 6E), hasta 9.6 Gbps (**OFDMA**, 1024-QAM, Target Wake Time).
  - **802.11be (Wi-Fi 7)**: Hasta 46 Gbps, canales de 320 MHz, 4096-QAM, MLO (Multi-Link Operation).
- **Seguridad Wi-Fi**: WEP (roto), WPA (TKIP), WPA2 (AES-CCMP), **WPA3** (SAE - *Simultaneous Authentication of Equals*, cifrado de 192 bits en modo Enterprise).
- **Evolución de Telefonía Móvil (3GPP)**:
  - **1G**: Analógica (AMPS, TACS).
  - **2G**: Digital GSM (900/1800 MHz, TDMA, SMS). Evolución GPRS (2.5G) y EDGE (2.75G).
  - **3G**: UMTS (WCDMA, hasta 2 Mbps). Evolución HSPA / HSPA+ (hasta 42 Mbps).
  - **4G**: **LTE / LTE-Advanced** (Todo IP, OFDM, MIMO, hasta 1 Gbps).
  - **5G NR (New Radio)**: Bandas sub-6 GHz y onda milimétrica (mmWave). Modos **NSA** (*Non-Standalone*, sobre núcleo 4G EPC) y **SA** (*Standalone*, sobre núcleo nativo 5G Core). Características: eMBB (banda ancha mejorada), URLLC (ultra baja latencia <1 ms), mMTC (comunicaciones masivas máquina a máquina / IoT).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Parámetro | Especificación Técnica |
|------------------------|------------------------|
| Longitud máxima canal horizontal UTP | **100 metros** (90 m fijo + 10 m latiguillos) |
| Cat 5e / Cat 6 / Cat 6A anchos de banda | **100 MHz / 250 MHz / 500 MHz** |
| Velocidad 10GBASE-T sobre Cat 6A | **10 Gbps hasta 100 metros** |
| Longitudes de onda Fibra Monomodo | **1310 nm y 1550 nm** (Láser, núcleo ~9 µm) |
| Longitudes de onda Fibra Multimodo | **850 nm y 1300 nm** (LED/VCSEL, núcleo 50/62.5 µm) |
| Velocidades GPON (ITU-T G.984) | **2.488 Gbps Downstream / 1.244 Gbps Upstream** |
| Estándar Wi-Fi 6 | **IEEE 802.11ax** (OFDMA, 2.4/5/6 GHz, 1024-QAM) |
| Protocolo autenticación WPA3 | **SAE** (Simultaneous Authentication of Equals) |
| Pilares 5G NR | **eMBB** (Banda ancha), **URLLC** (Baja latencia), **mMTC** (IoT masivo) |
| Estándar Cableado Estructurado | **ISO/IEC 11801** y **ANSI/TIA/EIA-568** |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Familia IEEE 802]]
- [[wiki/entities/wi-fi-and-mobile-standards|Estándares Wi-Fi y Tecnologías Móviles]]

### Conceptos Teóricos:
- [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Cableado]]

### Síntesis de Estudio:
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema06|Nota Fuente del Tema 06]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema06-medios-transmision-fibra|Test Tema 06]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|⬅️ Tema 05]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|Tema 07 ➡️]]
