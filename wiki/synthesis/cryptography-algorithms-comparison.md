---
title: "Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital"
type: "synthesis"
tags:
  - synthesis
  - cryptography
  - encryption
  - hashing
  - digital-signature
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Criptográfica"
  - "Cryptography Comparison"
---

# Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital

Matriz técnica de algoritmos de cifrado simétrico, asimétrico, funciones resumen (hash) y estándares de firma electrónica para el Sector Público.

---

## 🏛️ Matriz de Algoritmos Criptográficos

| Tipo de Criptografía | Algoritmo | Tamaño de Clave / Bloque | Seguridad / Estado Actual | Uso Principal |
|----------------------|-----------|--------------------------|---------------------------|---------------|
| **Simétrica (Bloque)** | **AES (Rijndael)** | Claves: **128, 192, 256 bits**; Bloque: **128 bits** | **Estándar mundial seguro** | Cifrado masivo de datos, TLS, BitLocker, IPsec |
| **Simétrica (Bloque)** | **3DES** | Claves: 112 o 168 bits; Bloque: 64 bits | Deprecado (vulnerable a Sweet32) | Sistemas legados |
| **Simétrica (Bloque)** | **DES** | Clave: 56 bits; Bloque: 64 bits | **Roto / Inseguro** | Obsoleto |
| **Simétrica (Flujo)** | **ChaCha20** | Clave: 256 bits | **Excelente seguridad y velocidad** | TLS 1.3, WireGuard, SSH |
| **Simétrica (Flujo)** | **RC4** | Clave: 40 a 2048 bits | **Roto / Prohibido en TLS** | Obsoleto |
| **Asimétrica** | **RSA** | Claves: **2048, 3072, 4096 bits** | Seguro con $\ge 2048$ bits | Firma digital, certificados X.509 |
| **Asimétrica** | **Diffie-Hellman (DH/ECDH)** | Claves: 2048+ bits / Curvas 256+ bits | **Seguro** | Intercambio de claves con PFS en TLS/IPsec |
| **Asimétrica** | **ECDSA / Ed25519** | Claves: **256, 384, 521 bits** | **Excelente eficiencia y seguridad** | Firmas digitales modernas, TLS 1.3, SSH |
| **Función Hash** | **SHA-2 (SHA-256/512)** | Resumen: **256 / 512 bits** | **Estándar seguro obligatorio** | Firma digital, HMAC, certificados |
| **Función Hash** | **SHA-3 (Keccak)** | Resumen: 224, 256, 384, 512 bits | **Muy seguro (esponja)** | Criptografía avanzada |
| **Función Hash** | **SHA-1** | Resumen: 160 bits | **Deprecado / Colisiones encontradas** | Obsoleto |
| **Función Hash** | **MD5** | Resumen: 128 bits | **Roto completamente** | Solo checksums no criptográficos |

---

## 🎯 Formatos de Firma Electrónica Avanzada (ETSI / eIDAS)
- **CAdES** (ETSI TS 101 733): Para ficheros binarios generales (*CMS Advanced Electronic Signatures*).
- **XAdES** (ETSI TS 101 903): Para documentos estructurados en formato XML.
- **PAdES** (ETSI TS 102 778): Para documentos en formato Adobe PDF (ISO 32000-1).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/cryptography-and-digital-signatures|Criptografía y Firma Digital]]
