---
title: "Resumen Fuente: Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces (USB, PCIe, NVMe)"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema02
  - perifericos
  - usb
  - pcie
  - nvme
  - thunderbolt
sources:
  - "raw/sources/bloque2-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Periféricos y Conectividad"
  - "bloque2-tema02"
---

# Resumen Fuente: Bloque 2 - Tema 02: Periféricos, Conectividad e Interfaces (USB, PCIe, NVMe)

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema02.md|bloque2-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza la clasificación funcional de los periféricos (entrada, salida y mixtos), los métodos de control de transferencia de E/S con el procesador (E/S programada con *busy waiting*, E/S por interrupciones IRQ y **Acceso Directo a Memoria DMA**), y las especificaciones técnicas de los buses y puertos de alta velocidad modernos: el estándar **USB** (USB 2.0 a 480 Mbps, USB 3.2 Gen 1 a 5 Gbps, Gen 2 a 10 Gbps, Gen 2x2 a 20 Gbps, USB4 a 40/80 Gbps y USB-PD de hasta 240W en conector Type-C), **Thunderbolt 3/4** (40 Gbps sobre Type-C multiplexando PCIe y DisplayPort), el bus serie punto a punto **PCI Express (PCIe Gen 3, 4, 5 y 6)** y el protocolo de estado sólido **NVMe** con sus 64.000 colas paralelas frente al estándar SATA III (AHCI).

---

## 🎯 Datos Clave para Oposiciones TAI

| Interfaz / Estándar | Tasa de Transferencia / Característica |
|---------------------|----------------------------------------|
| **USB 2.0 (High-Speed)** | **480 Mbps** (60 MB/s teóricos) |
| **USB 3.2 Gen 1 (SuperSpeed)** | **5 Gbps** (~500 MB/s) |
| **USB 3.2 Gen 2 (SuperSpeed+)**| **10 Gbps** (~1.2 GB/s) |
| **USB 3.2 Gen 2x2** | **20 Gbps** (conector USB Type-C) |
| **USB4 / Thunderbolt 3 y 4** | **40 Gbps** (USB4 2.0 hasta 80 Gbps) |
| **USB Power Delivery (USB-PD)**| Hasta **240W (48V / 5A)** en modo EPR |
| **SATA III vs NVMe** | SATA III: **6 Gbps / 1 cola (32 comandos)** \| NVMe: **PCIe / 64.000 colas (64.000 comandos c/u)** |
| **DMA (Direct Memory Access)**| Transfiere bloques entre periférico y RAM **sin consumir ciclos de CPU** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|Interfaces Periféricas: USB, PCIe, NVMe y Thunderbolt]]
- Síntesis: [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet de Puertos, Buses y Velocidades]]
