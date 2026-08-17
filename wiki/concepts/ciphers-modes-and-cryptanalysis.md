---
title: "Modos de Operación en Cifrado en Bloque y Criptoanálisis"
type: "concept"
tags:
  - cryptography
  - block-ciphers
  - aes
  - gcm
  - cbc
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modos de Cifrado en Bloque"
  - "Block Cipher Modes"
---

# Modos de Operación en Cifrado en Bloque y Criptoanálisis

Los algoritmos de cifrado simétrico en bloque (como AES con bloques de 128 bits) requieren **modos de operación** para transformar mensajes de longitud arbitraria de forma segura.

---

## 🏛️ Modos de Operación Principales

| Modo | Nombre Completo | Vector de Inicialización (IV) | Seguridad / Resistencia | Paralelizable | Uso Típico |
|------|-----------------|-------------------------------|-------------------------|---------------|------------|
| **ECB** | *Electronic Codebook* | No usa IV | **INSEGURO**: Bloques idénticos producen texto cifrado idéntico (revela patrones) | Sí | **Prohibido** para datos > 1 bloque |
| **CBC** | *Cipher Block Chaining* | Requiere IV aleatorio | Seguro frente a análisis de patrones, pero vulnerable a ataques de oráculo de padding | Solo descifrado | TLS 1.2 legado, IPsec |
| **CFB** | *Cipher Feedback* | Requiere IV | Convierte el cifrado en bloque en cifrado en flujo | Solo descifrado | Streaming de datos |
| **OFB** | *Output Feedback* | Requiere IV | Genera una secuencia pseudoaleatoria independiente del texto plano | No | Canales con errores de bit |
| **CTR** | *Counter Mode* | Requiere *Nonce* + Contador | **Muy seguro y altamente paralelizable** (acceso aleatorio) | **Sí (Cifrado y Descifrado)** | IPSec, SSH |
| **GCM** | *Galois/Counter Mode* | Requiere *Nonce* | **AEAD (Cifrado Autenticado con Datos Asociados)**: Aporta confidencialidad e integridad integrada | **Sí (Excelente rendimiento por hardware)** | **Estándar en TLS 1.3, IPsec y SSH** |

---

## 🧩 Conceptos Fundamentales de Criptoanálisis

- **Confusión (Shannon)**: Oculta la relación entre el texto plano y el texto cifrado (mediante sustituciones, cajas S-Box).
- **Difusión (Shannon)**: Propaga la influencia de un solo bit de texto plano o clave sobre muchos bits del texto cifrado (efecto avalancha, mediante permutaciones).
- **Secreto Perfecto hacia Adelante (PFS - Perfect Forward Secrecy)**: Garantía de que el compromiso de la clave privada a largo plazo de un servidor en el futuro **no permitirá descifrar sesiones pasadas** grabadas por un atacante. Se logra mediante el intercambio de claves Diffie-Hellman efímero (**DHE / ECDHE**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| Modo de Cifrado Inseguro Prohibido | **ECB (Electronic Codebook)** |
| Modo AEAD Estándar Moderno | **GCM (Galois/Counter Mode)** con AES |
| Principio Criptográfico Clave | **PFS (Perfect Forward Secrecy)** mediante **ECDHE** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/cryptography-and-digital-signatures|Criptografía y Firma Digital]]
- Síntesis: [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa de Algoritmos Criptográficos]]
