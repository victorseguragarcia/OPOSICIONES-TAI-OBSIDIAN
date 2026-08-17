---
title: "Test Tema 10: Topologías de Red, Arquitectura IEEE 802 y Estándares Wi-Fi"
type: "test"
target: "wiki/sources/bloque4-tema10-topologias-ieee802-wifi.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 10: Topologías de Red, Arquitectura IEEE 802 y Estándares Wi-Fi

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 10: Topologías de Red, Arquitectura IEEE 802 y Estándares Wi-Fi",
  "questions": [
    {
      "question": "¿Qué mecanismo de control de acceso al medio compartido utiliza el estándar IEEE 802.11 (Wi-Fi) debido a la imposibilidad práctica de detectar colisiones en el medio inalámbrico?",
      "options": [
        "CSMA/CD (Carrier Sense Multiple Access with Collision Detection).",
        "CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance con tramas RTS/CTS).",
        "Paso de testigo (*Token Passing*).",
        "TDMA síncrono."
      ],
      "answer": "b",
      "explanation": "Wi-Fi usa **CSMA/CA** (evitación de colisiones) con temporizadores DIFS/SIFS y tramas RTS/CTS; Ethernet cableado usa **CSMA/CD** (detección)."
    },
    {
      "question": "¿Qué denominación comercial corresponde al estándar inalámbrico IEEE 802.11ax, que introduce modulación 1024-QAM y tecnología OFDMA?",
      "options": [
        "Wi-Fi 4 (802.11n).",
        "Wi-Fi 5 (802.11ac).",
        "Wi-Fi 6 / 6E (802.11ax).",
        "Wi-Fi 7 (802.11be)."
      ],
      "answer": "c",
      "explanation": "IEEE 802.11ax es **Wi-Fi 6** (opera en 2.4 GHz y 5 GHz, y 6 GHz en Wi-Fi 6E). Wi-Fi 5 es 802.11ac y Wi-Fi 4 es 802.11n."
    },
    {
      "question": "¿Qué protocolo de seguridad inalámbrica WPA introdujo el protocolo SAE (Simultaneous Authentication of Equals) sustituyendo la clave precompartida (PSK) para evitar ataques de diccionario offline?",
      "options": [
        "WEP.",
        "WPA con TKIP.",
        "WPA2-Personal.",
        "WPA3-Personal."
      ],
      "answer": "d",
      "explanation": "WPA3 utiliza SAE (*Simultaneous Authentication of Equals*, basado en Dragonfly) proporcionando confidencialidad hacia adelante (*Forward Secrecy*)."
    },
    {
      "question": "¿En qué subcapas divide el modelo IEEE 802 la Capa 2 (Enlace de Datos) del modelo de referencia OSI?",
      "options": [
        "Subcapa LLC (Logical Link Control - 802.2) y Subcapa MAC (Media Access Control).",
        "Subcapa Física y Subcapa de Red.",
        "Subcapa de Transporte y Subcapa de Sesión.",
        "Subcapa de Enrutamiento y Subcapa de Conmutación."
      ],
      "answer": "a",
      "explanation": "IEEE 802 divide la Capa 2 en: **LLC (IEEE 802.2)** (control de enlace lógico independiente del medio) y **MAC** (acceso al medio específico: 802.3, 802.11)."
    },
    {
      "question": "¿Qué topología de red física conecta todos los nodos a un dispositivo central conmutador (Switch) de forma que la caída de un cable de un nodo individual no interrumpe la comunicación del resto de la red?",
      "options": [
        "Topología en Bus lineal.",
        "Topología en Anillo simple.",
        "Topología en Estrella.",
        "Topología en Malla no dirigida."
      ],
      "answer": "c",
      "explanation": "La topología en Estrella conecta cada estación al switch central mediante enlaces punto a punto dedicados."
    }
  ]
}
```
