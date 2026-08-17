---
title: "Test Tema 06: Medios de Transmisión, Par Trenzado y Fibra Óptica"
type: "test"
target: "wiki/sources/bloque4-tema06-medios-transmision-fibra.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 06: Medios de Transmisión, Par Trenzado y Fibra Óptica

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 06: Medios de Transmisión, Par Trenzado y Fibra Óptica",
  "questions": [
    {
      "question": "¿Cuál es la principal diferencia entre la fibra óptica Monomodo (SMF) y la fibra óptica Multimodo (MMF)?",
      "options": [
        "La fibra monomodo tiene un núcleo muy estrecho (~9 µm) que propaga un único rayo láser sin dispersión modal, permitiendo distancias de decenas de kilómetros; la multimodo tiene núcleo más ancho (50/62.5 µm), usa fuentes LED/VCSEL y está limitada a distancias cortas de red local.",
        "La fibra multimodo no admite transmisiones bidireccionales.",
        "La fibra monomodo está fabricada exclusivamente de plástico barato.",
        "La fibra monomodo solo puede transmitir señales de radiofrecuencia analógicas."
      ],
      "answer": "a",
      "explanation": "Monomodo (núcleo ~9 µm, láser, grandes distancias WAN); Multimodo (núcleo 50/62.5 µm, distancias LAN cortas hasta 550m)."
    },
    {
      "question": "¿Qué categoría de cable de par trenzado garantiza transmisiones de 10 Gigabit Ethernet (10GBASE-T) a una distancia de hasta 100 metros con frecuencias de hasta 500 MHz?",
      "options": [
        "Categoría 5e.",
        "Categoría 6.",
        "Categoría 6A.",
        "Categoría 3."
      ],
      "answer": "c",
      "explanation": "Cat 6A soporta 10 Gbps a 100m (500 MHz). (Cat 6 estándar solo soporta 10 Gbps hasta 37-55 metros a 250 MHz)."
    },
    {
      "question": "En redes de acceso de fibra óptica hasta el hogar/edificio (FTTH), ¿qué tecnología de red óptica pasiva punto a multipunto utiliza divisores ópticos (*splitters*) sin elementos activos entre la OLT y las ONTs?",
      "options": [
        "HFC (Híbrido Fibra-Coaxial).",
        "GPON (Gigabit Passive Optical Network - ITU-T G.984).",
        "DOCSIS 3.1.",
        "ADSL2+."
      ],
      "answer": "b",
      "explanation": "GPON utiliza divisores ópticos pasivos (sin alimentación eléctrica en planta externa) con velocidades de 2.488 Gbps bajada / 1.244 Gbps subida."
    },
    {
      "question": "¿Cuál es el conector estándar de 8 pines utilizado en cables de red Ethernet de par trenzado RJ45 bajo las normas TIA/EIA-568A y 568B?",
      "options": [
        "Conector RJ11.",
        "Conector 8P8C (conocido habitualmente como RJ45).",
        "Conector BNC.",
        "Conector SC/APC."
      ],
      "answer": "b",
      "explanation": "El conector físico de 8 pines es el 8P8C (modular de 8 posiciones y 8 contactos), llamado coloquialmente RJ45."
    },
    {
      "question": "¿Qué fenómeno físico en fibras ópticas multimodo provoca que diferentes rayos de luz lleguen al receptor en instantes ligeramente distintos ensanchando el pulso y limitando el ancho de banda?",
      "options": [
        "Dispersión Modal.",
        "Atenuación por curvatura macroscópica.",
        "Reflexión interna total.",
        "Diafonía (*Crosstalk*)."
      ],
      "answer": "a",
      "explanation": "La dispersión modal ocurre en fibras multimodo porque los diferentes modos/caminos de luz viajan a diferentes distancias dentro del núcleo."
    }
  ]
}
```
