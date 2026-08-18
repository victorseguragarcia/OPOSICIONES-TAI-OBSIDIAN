---
title: "Criptografía Simétrica, Asimétrica y Firma Digital"
type: "concept"
tags:
  - cryptography
  - digital-signature
  - pki
  - x509
  - security
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Criptografía y Firma Digital"
  - "Cryptography and PKI"
---

# Criptografía Simétrica, Asimétrica y Firma Digital

La criptografía proporciona los mecanismos matemáticos para garantizar la confidencialidad, autenticidad, integridad y no repudio de la información en entornos digitales.

---

## 🏛️ Tipos de Criptografía

1. **Criptografía Simétrica (Clave Secreta)**:
   - Misma clave para cifrar y descifrar.
   - Algoritmo estándar: **AES (Advanced Encryption Standard / Rijndael)** con bloques de 128 bits y claves de **128, 192 o 256 bits**.
2. **Criptografía Asimétrica (Clave Pública / Privada)**:
   - Clave pública para cifrar/verificar; clave privada para descifrar/firmar.
   - Algoritmos: **RSA** (factorización de primos), **Diffie-Hellman** (intercambio de claves), **ECDSA / Ed25519** (curvas elípticas).
3. **Criptografía Híbrida**: Cifra el mensaje con una clave de sesión simétrica efímera y cifra dicha clave de sesión con la clave pública asimétrica del receptor (utilizado en TLS, SSH, PGP).

---

## 🧩 Firma Digital y Certificados X.509

- **Mecanismo de Firma Digital**:
  1. El emisor genera un **resumen hash** del mensaje original ($H = 	ext{Hash}(M)$).
  2. El emisor cifra el hash $H$ con su **Clave Privada** $\rightarrow$ obteniendo la **Firma Digital**.
  3. El receptor descifra la firma con la **Clave Pública del Emisor** obteniendo $H_1$, calcula su propio hash $H_2 = 	ext{Hash}(M)$ y verifica que $H_1 == H_2$.
- **Formatos de Firma Electrónica Avanzada**:
  - **CAdES** (CMS Advanced Electronic Signature): Para ficheros binarios genéricos.
  - **XAdES** (XML Advanced Electronic Signature): Para documentos XML.
  - **PAdES** (PDF Advanced Electronic Signature): Integrada nativamente en ficheros PDF (ISO 32000-1).
- **Jerarquía de Certificados X.509**:
  - Autoridad de Certificación (CA) Raíz $\rightarrow$ CAs Subordinadas $\rightarrow$ Certificado Final de Usuario/Servidor.
  - Verificación de Revocación: **CRL** (Listas de Revocación) y **OCSP** (Online Certificate Status Protocol, RFC 6960 en puerto 80 HTTP).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| Algoritmo Simétrico Estándar | **AES** (128, 192, 256 bits de clave) |
| Formato Certificados Digitales | **ITU-T X.509** |
| Formatos Firma Avanzada | **CAdES** (binario), **XAdES** (XML), **PAdES** (PDF) |
| Protocolo Validación en Línea | **OCSP** (RFC 6960, puerto 80 HTTP) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Síntesis: [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital]]
