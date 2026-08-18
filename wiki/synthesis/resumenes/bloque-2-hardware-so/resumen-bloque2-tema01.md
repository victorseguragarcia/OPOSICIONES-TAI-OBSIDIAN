---
title: "Resumen Exhaustivo Tema 01 (Bloque 2): Estructura y Componentes de un Sistema Informático (C2, IEEE 754, Buses)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-2
  - tema-01
  - hardware
  - sistemas-operativos
  - bbdd\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema01.md]]"
  - "[[wiki/sources/bloque2-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Portada Bloque 2]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|Tema 02 ➡️]]

# 🔴 Resumen Exhaustivo Tema 01 (Bloque 2): Estructura y Componentes de un Sistema Informático (C2, IEEE 754, Buses)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 01**
> Sistemas de numeración (binario, octal, hexadecimal), representación de enteros (Signo-Magnitud, Complemento a 1, Complemento a 2), representación en coma flotante estándar IEEE 754 (Simple y Doble precisión), códigos alfanuméricos (ASCII, Unicode UTF-8/16/32), detección y corrección de errores (Paridad, Hamming, CRC) y buses de comunicación (PCIe, USB, SATA, Thunderbolt).

---

## 🟣 1. Desarrollo Técnico y Arquitectónico Exhaustivo

### 1. Representación de la Información y Aritmética Binaria
- **Sistemas de Numeración**:
  - Binario (base 2: $0, 1$), Octal (base 8: $0-7$), Decimal (base 10: $0-9$), Hexadecimal (base 16: $0-9, A-F$).
  - Conversión rápida: Cada dígito hexadecimal equivale exactamente a **4 bits (nibble)**; cada dígito octal equivale a **3 bits**.
- **Representación de Enteros con Signo ($n$ bits)**:

| Sistema de Representación | Fórmula Rango de Representación ($n$ bits) | Rango con 8 bits ($n=8$) | Características / Cero |
|:---|:---|:---:|:---|
| **Signo y Magnitud (SM)** | $[-(2^{n-1}-1) \text{ a } +(2^{n-1}-1)]$ | $[-127 \text{ a } +127]$ | MSB es signo ($0=+$, $1=-$). Doble representación del cero ($+0 = 00000000_2$, $-0 = 10000000_2$). |
| **Complemento a 1 (C1)** | $[-(2^{n-1}-1) \text{ a } +(2^{n-1}-1)]$ | $[-127 \text{ a } +127]$ | Los negativos se obtienen invirtiendo todos los bits. Doble cero ($+0 = 00000000_2$, $-0 = 11111111_2$). |
| **Complemento a 2 (C2)** | $[-2^{n-1} \text{ a } +(2^{n-1}-1)]$ | **$[-128 \text{ a } +127]$** | **Estándar universal**. Se invierten los bits y se suma 1 ($C2 = \overline{A} + 1$). **Cero único ($00000000_2$)**. Asimetría: permite representar un número negativo más. |
| **Exceso a $2^{n-1}$ (Sesgo)** | $[-2^{n-1} \text{ a } +(2^{n-1}-1)]$ | $[-128 \text{ a } +127]$ | Se suma un sesgo $K=2^{n-1}$ al valor real. Usado en los exponentes de coma flotante. |

- **Estándar IEEE 754 para Coma Flotante**:
  - Fórmula general: $V = (-1)^S \times (1.M) \times 2^{E - \text{Sesgo}}$ (para números normalizados con bit implícito 1).

| Formato IEEE 754 | Total Bits | Signo ($S$) | Exponente ($E$) | Mantisa ($M$) | Sesgo del Exponente ($K$) | Rango del Exponente Almacenado |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Simple Precisión (float)** | **32 bits** | **1 bit** | **8 bits** | **23 bits** | **127** ($2^{8-1}-1$) | $E \in [1, 254]$ ($E=0$ subnormales/cero; $E=255$ $\pm\infty$/NaN) |
| **Doble Precisión (double)** | **64 bits** | **1 bit** | **11 bits** | **52 bits** | **1023** ($2^{11-1}-1$) | $E \in [1, 2046]$ ($E=0$ subnormales/cero; $E=2047$ $\pm\infty$/NaN) |

### 2. Códigos Alfanuméricos y Detección/Corrección de Errores
- **Codificación de Caracteres**:
  - *ASCII Estándar*: 7 bits (128 caracteres, $0-127$).
  - *ASCII Extendido (ISO 8859-1 / Latin-1)*: 8 bits (256 caracteres, incluye caracteres europeos).
  - *Unicode*: Espacio de direccionamiento de **21 bits** ($1.114.112$ puntos de código organizados en 17 planos de $65.536$ caracteres; el Plano 0 es el BMP - Basic Multilingual Plane).
    - **UTF-8**: Longitud variable de **1 a 4 bytes**. Compatible 100% con ASCII en su primer byte. Estándar dominante de Internet.
    - **UTF-16**: Longitud variable de **2 o 4 bytes** (1 o 2 code units de 16 bits; utiliza pares subrogados).
    - **UTF-32**: Longitud fija de **4 bytes (32 bits)** por carácter.
  - *Código Gray*: Código binario no ponderado y continuo donde entre dos números consecutivos **solo cambia 1 bit** (evita errores en sensores rotatorios y codificadores ópticos).
  - *Código BCD (Binary Coded Decimal)*: Codifica cada dígito decimal ($0-9$) en un nibble de 4 bits ($0000_2$ a $1001_2$).
- **Detección y Corrección de Errores**:
  - *Distancia de Hamming ($d$)*: Número de posiciones en que dos palabras de código difieren.
    - Para **detectar $e$ errores**: Se requiere $d \ge e + 1$.
    - Para **corregir $t$ errores**: Se requiere $d \ge 2t + 1$ (ej. para corregir 1 error se necesita distancia $d \ge 3$).
  - *Código de Hamming (SEC-DED)*: Añade bits de paridad en posiciones que son potencias de 2 ($1, 2, 4, 8, \dots$). Corrige 1 error (Single Error Correction) y detecta 2 errores (Double Error Detection).
  - *CRC (Cyclic Redundancy Check)*: Detección de errores basada en división de polinomios en aritmética módulo 2.

### 3. Buses de Comunicación e Interfaces de Entrada/Salida
- **Clasificación de Buses**:
  - *Bus del Sistema*: Bus de Direcciones (unidireccional, define espacio de memoria direccionable $2^n$), Bus de Datos (bidireccional, ancho de palabra) y Bus de Control (señales de lectura/escritura, reloj, interrupciones).
- **Estándares de Buses de Alta Velocidad**:

| Interfaz / Bus | Tipo de Transmisión | Velocidad Teórica / Rendimiento | Topología y Características Clave |
|:---|:---:|:---|:---|
| **PCI Express (PCIe)** | Serie punto a punto | • PCIe 3.0: ~1 GB/s por carril (lane x1)<br>• PCIe 4.0: ~2 GB/s por carril<br>• PCIe 5.0: ~4 GB/s por carril (un slot x16 alcanza 64 GB/s) | Comunicación fullduplex mediante enlaces diferenciales punto a punto agrupados en carriles ($x1, x4, x8, x16$). Reemplazó al bus paralelo PCI/PCI-X. |
| **SATA (Serial ATA)** | Serie | • SATA I: 1,5 Gbps (150 MB/s)<br>• SATA II: 3 Gbps (300 MB/s)<br>• SATA III: 6 Gbps (600 MB/s) | Interfaz para discos duros y SSDs de 2,5". Protocolo AHCI con soporte de hot-plug y NCQ (Native Command Queuing). |
| **NVMe (Non-Volatile Memory Express)** | Serie sobre PCIe | • PCIe 3.0 x4: ~3.500 MB/s<br>• PCIe 4.0 x4: ~7.000 MB/s<br>• PCIe 5.0 x4: ~14.000 MB/s | Protocolo optimizado para memorias flash no volátiles sobre bus PCIe. Soporta hasta **64.000 colas de comandos con 64.000 comandos por cola** (frente a 1 cola de 32 comandos en SATA AHCI). |
| **USB (Universal Serial Bus)** | Serie | • USB 2.0: **480 Mbps** (High Speed)<br>• USB 3.0 / 3.1 Gen 1 / 3.2 Gen 1: **5 Gbps** (SuperSpeed)<br>• USB 3.1 Gen 2 / 3.2 Gen 2: **10 Gbps** (SuperSpeed+)<br>• USB 3.2 Gen 2x2: **20 Gbps**<br>• USB4: **40 Gbps** | Conexión plug-and-play con topología en estrella escalonada (árbol) mediante hubs (máx. **127 dispositivos** direccionables por controlador). |
| **Thunderbolt** | Serie multiplexada (PCIe + DisplayPort) | • TB 3 / TB 4: **40 Gbps**<br>• TB 5: **hasta 80/120 Gbps** | Conector físico USB-C. Permite conexión en cadena (daisy chain) de hasta 6 dispositivos y entrega de energía (USB-PD hasta 100-240W). |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 01 (Bloque 2)**
> 1. **Rango de Complemento a 2 con 8 bits**: Es **$[-128 \text{ a } +127]$** (el valor $-128$ se representa como $10000000_2$, sin equivalente positivo).
> 2. **Campos del IEEE 754 Simple Precisión (32 bits)**: **1 bit signo**, **8 bits exponente** (sesgo $127$), **23 bits mantisa**. Los distractores suelen cambiar el orden o los tamaños (ej. 1-11-20).
> 3. **Límite de Dispositivos USB**: Un controlador USB puede direccionar un máximo de **127 dispositivos** (dirección de 7 bits, la dirección 0 es reservada para configuración).
> 4. **Distancia de Hamming**: Para *corregir* 1 error se necesita distancia $d=3$; para *detectar* 1 error basta $d=2$.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **IEEE 754 Simple (32b)**: **1 - 8 - 23** (Signo 1, Exponente 8, Mantisa 23, Sesgo 127).
> - **IEEE 754 Doble (64b)**: **1 - 11 - 52** (Signo 1, Exponente 11, Mantisa 52, Sesgo 1023).
> - **Distancia Hamming**: **Detectar $= e+1$** / **Corregir $= 2t+1$**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque2-tema01|Fuente Oficial del Tema 01]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema01-informatica-basica|Test Tema 01]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque 2**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Portada Bloque 2]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|Tema 02 ➡️]]
