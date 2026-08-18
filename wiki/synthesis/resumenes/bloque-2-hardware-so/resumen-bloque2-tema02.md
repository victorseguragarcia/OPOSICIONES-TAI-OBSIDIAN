---
title: "Resumen Completo Tema 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-2
  - tema-02
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque2-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema01|⬅️ Tema 01]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|Tema 03 ➡️]]

# 🔴 Resumen Completo Tema 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 02**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

# 🔴 Resumen Fuente: Bloque 2 - Tema 02 (UD012103): Periféricos, Conectividad, Puertos Físicos y Buses de Expansión

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md|bloque2-tema02-perifericos-conectividad-interfaces.md]] (112 páginas).

---

## 📖 1. Clasificación de Periféricos y Mecanismos de Entrada/Salida

- **Clasificación Funcional**:
  - **Entrada**: Teclados, ratones, escáneres ópticos, digitalizadores biométricos, lectores de tarjetas inteligentes.
  - **Salida**: Monitores (CRT, LCD, LED, OLED con conexiones HDMI, DisplayPort, DVI, VGA), impresoras (láser electrofotográficas, inyección de tinta, matriciales de impacto, térmicas), trazadores gráficos (*plotters*).
  - **Entrada/Salida (Mixtos)**: Pantallas táctiles, tarjetas de sonido, tarjetas de red, módems.
  - **Almacenamiento**: Discos magnéticos (HDD), discos de estado sólido (SSD SATA / NVMe), cintas magnéticas LTO, discos ópticos (CD, DVD, Blu-ray).
- **Mecanismos de Transferencia de E/S**:
  1. **E/S Programada**: La CPU comprueba continuamente mediante sondeo (*polling*) el estado del periférico (alto consumo de CPU).
  2. **E/S por Interrupciones**: El periférico genera una señal hardware (**IRQ**) cuando está listo para transferir datos, interrumpiendo a la CPU.
  3. **Acceso Directo a Memoria (DMA - Direct Memory Access)**: Un controlador DMA transfiere bloques enteros de datos entre el periférico y la memoria principal sin intervención de la CPU, avisando al finalizar mediante una interrupción.

---

## 🟣 2. Puertos Físicos y Estándares de Conectividad Externa

| Puerto / Estándar | Norma / Especificación | Velocidad Máxima de Transferencia | Conectores / Características |
|-------------------|------------------------|-----------------------------------|------------------------------|
| **Puerto Serie** | **RS-232C** / EIA-232 | Hasta 115.2 kbps (asíncrono) | Conector DB-9 o DB-25 |
| **Puerto Paralelo** | **IEEE 1284** / Centronics | Hasta 2 MB/s (modo ECP / EPP) | Conector DB-25 / Centronics 36 pines |
| **PS/2** | Mini-DIN 6 pines | Puerto serie síncrono dedicado | Verde para ratón, Morado para teclado |
| **USB 1.1** | Full Speed | **12 Mbps** (1.5 Mbps en Low Speed) | Conectores Tipo A y Tipo B |
| **USB 2.0** | High Speed | **480 Mbps** (60 MB/s) | Incorpora conector Mini-USB y Micro-USB |
| **USB 3.0 (USB 3.1 Gen 1)** | SuperSpeed | **5 Gbps** (~500 MB/s) | Conectores azulados; añade 5 pistas extra |
| **USB 3.1 Gen 2 (USB 3.2 Gen 2x1)** | SuperSpeed+ | **10 Gbps** (~1.2 GB/s) | Conector **USB Type-C** reversible |
| **USB 3.2 Gen 2x2** | SuperSpeed+ Dual-Lane | **20 Gbps** (usando dos carriles Tipo-C) | Solo conector USB Type-C |
| **USB4** | Basado en Thunderbolt 3 | **40 Gbps** (con entrega de energía USB-PD 100W/240W) | Conector USB Type-C |
| **FireWire 400** | **IEEE 1394a** | **400 Mbps** | 6 pines (con alimentación) o 4 pines |
| **FireWire 800** | **IEEE 1394b** | **800 Mbps** | 9 pines bilingüe |
| **Thunderbolt 3 / 4** | Intel / Apple | **40 Gbps** (soporta PCIe 3.0 x4 + DisplayPort) | Conector USB Type-C |

---

## 🔵 3. Buses Internos de Expansión: PCI Express y NVMe

- **PCI Express (PCIe)**: Arquitectura serie punto a punto basada en carriles (*lanes* $x1, x4, x8, x16$ full-duplex con codificación 8b/10b o 128b/130b):
  - **PCIe 3.0**: ~1 GB/s por carril ($pprox 16	ext{ GB/s}$ en $x16$).
  - **PCIe 4.0**: ~2 GB/s por carril ($pprox 32	ext{ GB/s}$ en $x16$).
  - **PCIe 5.0**: ~4 GB/s por carril ($pprox 64	ext{ GB/s}$ en $x16$).
- **Protocolo NVMe (Non-Volatile Memory Express)**:
  - Diseñado específicamente para almacenamiento SSD sobre bus PCIe (reemplazando el cuello de botella del protocolo AHCI sobre SATA).
  - Soporta hasta **64.000 colas de comandos**, con hasta **64.000 comandos por cola** en paralelo.

---

## 🎯 Datos Clave para Oposiciones TAI

| Puerto / Protocolo | Dato Clave de Examen |
|-------------------|----------------------|
| **Velocidad USB 2.0 vs 3.0** | USB 2.0 = **480 Mbps** \| USB 3.0 = **5 Gbps** \| USB4 = **40 Gbps** |
| **IEEE 1394** | Nombre oficial del estándar **FireWire** |
| **IEEE 1284** | Nombre oficial del estándar de **Puerto Paralelo (Centronics/ECP/EPP)** |
| **Ventaja de NVMe sobre AHCI** | Permite 64.000 colas paralelas (frente a 1 única cola de 32 comandos en AHCI/SATA) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|Interfaces y Periféricos: USB, PCIe, NVMe y Thunderbolt]]
- Síntesis: [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos, Interfaces y Buses]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque2-tema02|Nota Fuente del Tema 02]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema02-perifericos-interfaces|Test Tema 02]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema01|⬅️ Tema 01]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|Tema 03 ➡️]]
