---
title: "Test de Autoevaluación: Bloque 4 - Tema 09 (Seguridad en Redes, Criptografía y ENS RD 311/2022)"
type: "test"
target: "wiki/sources/bloque4-tema09.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-4
  - seguridad
  - ens
  - criptografia
  - rsa
  - pki
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test de Autoevaluación: Bloque 4 - Tema 09 (Seguridad en Redes, Criptografía y ENS RD 311/2022)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 4 - Tema 09 (Seguridad en Redes, Criptografía y ENS RD 311/2022)",
  "questions": [
    {
      "question": "¿Cuáles son las 5 dimensiones de seguridad de la información definidas en el Esquema Nacional de Seguridad (ENS - RD 311/2022)?",
      "options": [
        "Rendimiento, Escalabilidad, Disponibilidad, Latencia y Ancho de banda.",
        "Disponibilidad (D), Autenticidad (A), Integridad (I), Confidencialidad (C) y Trazabilidad (T) [DADIT].",
        "Prevención, Detección, Reacción, Recuperación y Auditoría.",
        "Licitud, Lealtad, Transparencia, Minimización y Exactitud."
      ],
      "answer": "b",
      "explanation": "Las 5 dimensiones del ENS son **Disponibilidad, Autenticidad, Integridad, Confidencialidad y Trazabilidad**."
    },
    {
      "question": "Según el principio de la 'dimensión más exigente' del ENS, si un sistema tiene niveles: D=Bajo, A=Medio, I=Medio, C=Alto, T=Bajo, ¿cuál es la Categoría de Seguridad Global del sistema?",
      "options": [
        "Básica.",
        "Media.",
        "Alta.",
        "Crítica."
      ],
      "answer": "c",
      "explanation": "La categoría global es el máximo entre las 5 dimensiones ($\\max(\text{Bajo, Medio, Medio, Alto, Bajo}) = \\mathbf{ALTA}$)."
    },
    {
      "question": "En criptografía asimétrica, para firmar digitalmente un documento garantizando la autenticidad y el no repudio del emisor, ¿con qué clave se cifra el hash resumen del documento?",
      "options": [
        "Con la clave pública del receptor.",
        "Con la clave privada del emisor.",
        "Con la clave pública del emisor.",
        "Con una clave simétrica de sesión compartida."
      ],
      "answer": "b",
      "explanation": "La firma digital se genera cifrando el hash con la **clave privada del emisor** (cualquiera puede verificar con la clave pública)."
    },
    {
      "question": "¿Cuál de los siguientes algoritmos de cifrado es SIMÉTRICO por bloques?",
      "options": [
        "RSA.",
        "AES (Advanced Encryption Standard - Rijndael).",
        "ECC (Criptografía de Curva Elíptica).",
        "Diffie-Hellman."
      ],
      "answer": "b",
      "explanation": "AES es simétrico por bloques (128 bits con claves de 128, 192 o 256 bits). RSA, ECC y Diffie-Hellman son asimétricos."
    },
    {
      "question": "¿Qué organismo público del Centro Nacional de Inteligencia (CNI) es la autoridad responsable de la seguridad de las tecnologías de la información en el sector público español y elabora las Guías CCN-STIC?",
      "options": [
        "INCIBE.",
        "CCN-CERT (Centro Criptológico Nacional).",
        "AEPD.",
        "Secretaría General de Administración Digital (SGAD)."
      ],
      "answer": "b",
      "explanation": "El CCN-CERT (Centro Criptológico Nacional del CNI) vela por la ciberseguridad en el sector público y emite las guías CCN-STIC."
    }
  ]
}
```
