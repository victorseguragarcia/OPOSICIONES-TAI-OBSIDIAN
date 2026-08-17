---
title: "Cheatsheet: Hardware, Registros de CPU, Jerarquía de Memoria y Buses (Bloque II)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-2
  - hardware
  - cpu
  - buses
  - memoria
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
  - "raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Hardware y Buses Cheatsheet"
  - "Jerarquía de Memoria y CPU TAI"
---

# 🔴 Cheatsheet: Hardware, Registros de CPU, Jerarquía de Memoria y Buses

Resumen de datos técnicos y especificaciones de alta frecuencia de examen para el Bloque II.

---

## ⚡ 1. Registros Fundamentales de la CPU

| Registro | Acrónimo | Función en el Ciclo de Instrucción |
|:---|:---:|:---|
| **Contador de Programa** | **PC** (*Program Counter*) | Contiene la **dirección de memoria** de la siguiente instrucción a ejecutar. |
| **Registro de Instrucción** | **IR** (*Instruction Register*) | Almacena el **código binario de la instrucción** que se está decodificando y ejecutando. |
| **Registro de Dirección de Memoria** | **MAR** (*Memory Address Reg.*) | Almacena la dirección de memoria física a la que se desea acceder (lectura o escritura). |
| **Registro de Datos de Memoria** | **MBR / MDR** (*Memory Buffer Reg.*) | Almacena el dato leído de memoria o el dato a escribir en memoria. |
| **Palabra de Estado del Programa** | **PSW** (*Program Status Word*) | Contiene los flags de condición (Zero $Z$, Carry $C$, Overflow $V$, Signo $N$, Interrupciones). |
| **Puntero de Pila** | **SP** (*Stack Pointer*) | Apunta a la cima de la pila en memoria para llamadas a funciones e interrupciones. |

---

## 📊 2. Jerarquía de Memoria (Velocidad vs Capacidad)

```
                            JERARQUÍA DE MEMORIA
                                     │
                 ▲   ┌───────────────────────────────┐   Menor Capacidad
                 │   │     Registros de la CPU       │   < 1 ns (< 1 ciclo)
                 │   ├───────────────────────────────┤   Caché L1 (1-4 ciclos)
   Mayor         │   │      Memoria Caché L1/L2/L3   │   Caché L2/L3 (10-40 ciclos)
 Velocidad y     │   ├───────────────────────────────┤   RAM DDR4/DDR5 (50-100 ns)
   Coste/bit     │   │      Memoria Principal (RAM)  │
                 │   ├───────────────────────────────┤   NVMe / SSD PCIe (10-100 µs)
                 │   │      SSD (NVMe / SATA)        │   HDD magnético (5-10 ms)
                 ▼   ├───────────────────────────────┤   Cintas magnéticas / Backup
                     │    Discos Magnéticos / Cintas │   Mayor Capacidad
                     └───────────────────────────────┘
```

---

## 🔌 3. Tabla de Velocidades de Puertos y Buses de E/S

| Estándar de Bus | Tipo | Ancho de Banda Teórico | Conector / Notas |
|:---|:---:|:---:|:---|
| **USB 2.0 (High Speed)** | Serie | **480 Mbps** ($60	ext{ MB/s}$) | Tipo A / Tipo B / Micro-USB |
| **USB 3.0 / USB 3.1 Gen 1** | Serie | **5 Gbps** ($500	ext{ MB/s}$) | Tipo A azul / Tipo C |
| **USB 3.1 Gen 2 / USB 3.2 Gen 2** | Serie | **10 Gbps** ($1,25	ext{ GB/s}$) | Tipo C |
| **USB 3.2 Gen 2x2** | Serie | **20 Gbps** | Tipo C (doble carril) |
| **USB4 / Thunderbolt 3 / 4** | Serie | **40 Gbps** ($5	ext{ GB/s}$) | Tipo C (túnel PCIe + DisplayPort) |
| **Thunderbolt 5** | Serie | **80 / 120 Gbps** | Tipo C |
| **SATA III (SATA 6Gbps)** | Serie | **6 Gbps** ($600	ext{ MB/s}$) | Discos duros y SSDs de 2.5" |
| **PCIe 3.0 (por línea x1)** | Serie | **1 GB/s** ($x16 = 16	ext{ GB/s}$) | Ranuras de expansión placa base |
| **PCIe 4.0 (por línea x1)** | Serie | **2 GB/s** ($x16 = 32	ext{ GB/s}$) | Ranuras M.2 NVMe y GPUs |
| **PCIe 5.0 (por línea x1)** | Serie | **4 GB/s** ($x16 = 64	ext{ GB/s}$) | Servidores y SSDs Gen5 |
