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

# 🔴 Test de Autoevaluación: Bloque 2 - Tema 02 (Periféricos, Puertos y Conectividad)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 2 - Tema 02 (Periféricos, Puertos y Conectividad)",
  "questions": [
    {
      "question": "¿Cuál es la tasa de transferencia máxima teórica del estándar USB 2.0 (High Speed)?",
      "options": [
        "12 Mbps.",
        "480 Mbps.",
        "5 Gbps.",
        "10 Gbps."
      ],
      "answer": "b",
      "explanation": "USB 2.0 ofrece 480 Mbps (High Speed). (USB 1.1 = 12 Mbps, USB 3.0 = 5 Gbps)."
    },
    {
      "question": "¿Qué velocidad teórica máxima alcanza la interfaz Thunderbolt 4 / USB4?",
      "options": [
        "10 Gbps.",
        "20 Gbps.",
        "40 Gbps.",
        "80 Gbps."
      ],
      "answer": "c",
      "explanation": "Thunderbolt 4 y USB4 alcanzan 40 Gbps sobre conectores USB Tipo C."
    },
    {
      "question": "En la arquitectura PCI Express (PCIe), ¿qué tipo de comunicación se utiliza?",
      "options": [
        "Bus paralelo compartido de 32/64 bits.",
        "Enlaces serie punto a punto full-dúplex organizados en líneas (*lanes* $x1, x4, x8, x16$).",
        "Transmisión síncrona en anillo unidireccional.",
        "Transmisión óptica asíncrona sobre interfaz SCSI."
      ],
      "answer": "b",
      "explanation": "PCIe es serie punto a punto con líneas (*lanes*) dedicadas sin contienda de bus."
    },
    {
      "question": "¿Cuál es la principal ventaja técnica del protocolo NVMe (Non-Volatile Memory Express) frente a AHCI/SATA?",
      "options": [
        "Utiliza una única cola de 32 comandos para reducir la latencia de interrupciones.",
        "Soporta hasta 64.000 colas con hasta 64.000 comandos por cola en paralelo aprovechando PCIe.",
        "No requiere controladores de hardware.",
        "Es compatible con cables IDE ribbon."
      ],
      "answer": "b",
      "explanation": "AHCI soporta 1 cola de 32 comandos; NVMe soporta 64K colas con 64K comandos cada una."
    },
    {
      "question": "¿Qué interfaz de almacenamiento empresarial permite conectar discos duros y SSDs tanto en topología punto a punto como mediante expansores (*expanders*) sustituyendo al antiguo bus SCSI paralelo?",
      "options": [
        "SATA III.",
        "SAS (Serial Attached SCSI).",
        "PATA (Parallel ATA).",
        "FireWire 800."
      ],
      "answer": "b",
      "explanation": "SAS (Serial Attached SCSI) es el estándar serie empresarial de almacenamiento."
    }
  ]
}
```
