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

# 🔴 Test Tema 09: Seguridad en Redes, Criptografía y ENS (RD 311/2022)

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. ¿Cuáles son las 5 dimensiones de seguridad de la información definidas en el Esquema Nacional de Seguridad (ENS - RD 311/2022)?
- [ ] a) Rendimiento, Escalabilidad, Disponibilidad, Latencia y Ancho de banda.
- [ ] b) Disponibilidad (D), Autenticidad (A), Integridad (I), Confidencialidad (C) y Trazabilidad (T) [DADIT].
- [ ] c) Prevención, Detección, Reacción, Recuperación y Auditoría.
- [ ] d) Licitud, Lealtad, Transparencia, Minimización y Exactitud.

### 2. Según el principio de la 'dimensión más exigente' del ENS, si un sistema tiene niveles: D=Bajo, A=Medio, I=Medio, C=Alto, T=Bajo, ¿cuál es la Categoría de Seguridad Global del sistema?
- [ ] a) Básica.
- [ ] b) Media.
- [ ] c) Alta.
- [ ] d) Crítica.

### 3. En criptografía asimétrica, para firmar digitalmente un documento garantizando la autenticidad y el no repudio del emisor, ¿con qué clave se cifra el hash resumen del documento?
- [ ] a) Con la clave pública del receptor.
- [ ] b) Con la clave privada del emisor.
- [ ] c) Con la clave pública del emisor.
- [ ] d) Con una clave simétrica de sesión compartida.

### 4. ¿Cuál de los siguientes algoritmos de cifrado es SIMÉTRICO por bloques?
- [ ] a) RSA.
- [ ] b) AES (Advanced Encryption Standard - Rijndael).
- [ ] c) ECC (Criptografía de Curva Elíptica).
- [ ] d) Diffie-Hellman.

### 5. ¿Qué organismo público del Centro Nacional de Inteligencia (CNI) es la autoridad responsable de la seguridad de las tecnologías de la información en el sector público español y elabora las Guías CCN-STIC?
- [ ] a) INCIBE.
- [ ] b) CCN-CERT (Centro Criptológico Nacional).
- [ ] c) AEPD.
- [ ] d) Secretaría General de Administración Digital (SGAD).

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **c** | 3. **b** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: Las 5 dimensiones del ENS son **Disponibilidad, Autenticidad, Integridad, Confidencialidad y Trazabilidad**.
> - **Pregunta 2 (c)**: La categoría global es el máximo entre las 5 dimensiones ($\max(	ext{Bajo, Medio, Medio, Alto, Bajo}) = \mathbf{ALTA}$).
> - **Pregunta 3 (b)**: La firma digital se genera cifrando el hash con la **clave privada del emisor** (cualquiera puede verificar con la clave pública).
> - **Pregunta 4 (b)**: AES es simétrico por bloques (128 bits con claves de 128, 192 o 256 bits). RSA, ECC y Diffie-Hellman son asimétricos.
> - **Pregunta 5 (b)**: El CCN-CERT (Centro Criptológico Nacional del CNI) vela por la ciberseguridad en el sector público y emite las guías CCN-STIC.
