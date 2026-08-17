---
title: "Test de Autoevaluación: Bloque 2 - Tema 02 (Periféricos, Puertos y Conectividad)"
type: "test"
target: "wiki/sources/bloque2-tema02.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - perifericos
  - usb
  - pcie
  - nvme
  - thunderbolt
sources:
  - "raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 02: Periféricos, Puertos y Buses de E/S

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---

## ❓ Preguntas

### 1. ¿Cuál es la tasa de transferencia máxima teórica del estándar USB 2.0 (High Speed)?
- [ ] a) 12 Mbps.
- [ ] b) 480 Mbps.
- [ ] c) 5 Gbps.
- [ ] d) 10 Gbps.

### 2. ¿Qué velocidad teórica máxima alcanza la interfaz Thunderbolt 4 / USB4?
- [ ] a) 10 Gbps.
- [ ] b) 20 Gbps.
- [ ] c) 40 Gbps.
- [ ] d) 80 Gbps.

### 3. En la arquitectura PCI Express (PCIe), ¿qué tipo de comunicación se utiliza?
- [ ] a) Bus paralelo compartido de 32/64 bits.
- [ ] b) Enlaces serie punto a punto full-dúplex organizados en líneas (*lanes* $x1, x4, x8, x16$).
- [ ] c) Transmisión síncrona en anillo unidireccional.
- [ ] d) Transmisión óptica asíncrona sobre interfaz SCSI.

### 4. ¿Cuál es la principal ventaja técnica del protocolo NVMe (Non-Volatile Memory Express) frente a AHCI/SATA?
- [ ] a) Utiliza una única cola de 32 comandos para reducir la latencia de interrupciones.
- [ ] b) Soporta hasta 64.000 colas con hasta 64.000 comandos por cola en paralelo aprovechando PCIe.
- [ ] c) No requiere controladores de hardware.
- [ ] d) Es compatible con cables IDE ribbon.

### 5. ¿Qué interfaz de almacenamiento empresarial permite conectar discos duros y SSDs tanto en topología punto a punto como mediante expansores (*expanders*) sustituyendo al antiguo bus SCSI paralelo?
- [ ] a) SATA III.
- [ ] b) SAS (Serial Attached SCSI).
- [ ] c) PATA (Parallel ATA).
- [ ] d) FireWire 800.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **c** | 3. **b** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: USB 2.0 ofrece 480 Mbps (High Speed). (USB 1.1 = 12 Mbps, USB 3.0 = 5 Gbps).
> - **Pregunta 2 (c)**: Thunderbolt 4 y USB4 alcanzan 40 Gbps sobre conectores USB Tipo C.
> - **Pregunta 3 (b)**: PCIe es serie punto a punto con líneas (*lanes*) dedicadas sin contienda de bus.
> - **Pregunta 4 (b)**: AHCI soporta 1 cola de 32 comandos; NVMe soporta 64K colas con 64K comandos cada una.
> - **Pregunta 5 (b)**: SAS (Serial Attached SCSI) es el estándar serie empresarial de almacenamiento.
