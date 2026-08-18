---
title: "Resumen Exhaustivo Tema 09 (Bloque 4): Seguridad de la Información, Criptografía y ENS (RD 311/2022)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-09
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema09.md]]"
  - "[[wiki/sources/bloque4-tema09]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|⬅️ Tema 08]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema10|Tema 10 ➡️]]

# 🔴 Resumen Exhaustivo Tema 09 (Bloque 4): Seguridad de la Información, Criptografía y ENS (RD 311/2022)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 09**
> Criptografía simétrica (DES, 3DES, AES), criptografía asimétrica (RSA, Diffie-Hellman, Curvas Elípticas ECC), funciones Hash criptográficas (MD5, SHA-1, SHA-2, SHA-3), firma digital, infraestructura de clave pública (PKI, certificados X.509) y el Esquema Nacional de Seguridad (ENS - RD 311/2022 dimensiones y categorías básica/media/alta).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Criptografía Simétrica, Asimétrica y Funciones Hash
- **Criptografía Simétrica (Clave Secreta Compartida)**:
  - Misma clave para cifrar y descifrar. Muy rápida, óptima para grandes volúmenes de datos.
  - *Cifrado por Bloques*:
    - **DES**: Bloque de 64 bits, clave de 56 bits (obsoleto).
    - **3DES (Triple DES)**: Aplica DES 3 veces con clave efectiva de 112 o 168 bits.
    - **AES (Advanced Encryption Standard - Rijndael)**: Bloque de **128 bits**, tamaños de clave: **128, 192 y 256 bits** (estándar mundial actual).
- **Criptografía Asimétrica (Par de Claves Pública y Privada)**:
  - Basada en problemas matemáticos unidireccionales de computación difícil. Más lenta que la simétrica.
  - **RSA**: Basado en la dificultad de factorizar números enteros grandes producto de dos primos. Tamaños de clave recomendados: $\ge 2048$ o $4096$ bits.
  - **Diffie-Hellman (DH)**: Protocolo de intercambio seguro de claves sobre canal inseguro (no cifra datos directamente).
  - **ECC (Criptografía de Curva Elíptica)**: Ofrece la misma seguridad que RSA con claves mucho más pequeñas (clave ECC de 256 bits $\approx$ clave RSA de 3072 bits), ideal para móviles y TLS.
- **Funciones Hash Criptográficas (Resumen Unidireccional)**:
  - Propiedades: Unidireccionalidad (irreversible) y resistencia a colisiones ($H(m_1) \ne H(m_2)$).
  - *MD5*: Resumen de 128 bits (roto, vulnerable a colisiones).
  - *SHA-1*: Resumen de 160 bits (roto, desaconsejado).
  - *Familia SHA-2*: SHA-256 (256 bits), SHA-512 (512 bits) (ampliamente utilizado).
  - *SHA-3 (Keccak)*: Estándar basado en funciones esponja.

### 2. Firma Digital y Certificados Digitales (X.509)
- **Mecanismo de la Firma Digital**:
  1. El emisor genera el **Hash** del documento original.
  2. El emisor cifra el Hash con su **CLAVE PRIVADA** $\rightarrow$ Este resultado es la **Firma Digital**.
  3. El receptor descifra la firma con la **CLAVE PÚBLICA del emisor** obteniendo el Hash original y lo compara con el Hash que él mismo calcula sobre el documento recibido.
  - Garantiza 3 propiedades: **Autenticidad del origen**, **Integridad del contenido** y **No Repudio**.
- **Infraestructura PKI y Estándar X.509**:
  - Autoridad de Certificación (CA), Autoridad de Registro (RA) y Listas de Revocación de Certificados (**CRL**) o protocolo de consulta en tiempo real **OCSP (Online Certificate Status Protocol - RFC 6960)**.

### 3. El Esquema Nacional de Seguridad (ENS - Real Decreto 311/2022)
- **Principios Básicos del ENS (Art. 5 a 12)**:
  1. Seguridad integral.
  2. Gestión de la seguridad basada en los riesgos.
  3. Prevención, detección, respuesta y conservación.
  4. Líneas de defensa (defensa en profundidad).
  5. Vigilancia continua y monitorización.
  6. Reevaluación periódica.
  7. Diferenciación de responsabilidades.
- **Las 5 Dimensiones de Seguridad del ENS**:
  - **Disponibilidad (D)**: Acceso garantizado en el momento requerido.
  - **Autenticidad (A)**: Certeza sobre la identidad del emisor/origen.
  - **Integridad (I)**: Exactitud e inalterabilidad de la información.
  - **Confidencialidad (C)**: Acceso restringido exclusivamente a personas autorizadas.
  - **Trazabilidad (T)**: Registro y seguimiento de las acciones realizadas sobre el sistema.
- **Categorización de los Sistemas (Básica, Media, Alta)**:
  - Se determina por el nivel de impacto (Bajo, Medio, Alto) en la dimensión más exigente:
    - **Categoría BÁSICA**: Daño limitado ante un incidente. Autoevaluación anual.
    - **Categoría MEDIA**: Daño grave. Exige **Auditoría de Seguridad bienal (cada 2 años)** por entidad independiente.
    - **Categoría ALTA**: Daño muy grave. Exige **Auditoría de Seguridad bienal** independiente.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 09 (Bloque 4)**
> 1. **Firma Digital**: Se cifra con la **CLAVE PRIVADA del emisor** (y se verifica con su clave pública).
> 2. **Cifrado para Confidencialidad**: Se cifra con la **CLAVE PÚBLICA del receptor** (y solo él puede descifrarlo con su clave privada).
> 3. **Las 5 Dimensiones del ENS**: Son **D-A-I-C-T** (**Disponibilidad, Autenticidad, Integridad, Confidencialidad y Trazabilidad**).
> 4. **Periodicidad Auditoría ENS Categoría Media y Alta**: Es **BIENAL (cada 2 años)**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Dimensiones ENS**: **DAICT** $\rightarrow$ **D**isponibilidad, **A**utenticidad, **I**ntegridad, **C**onfidencialidad, **T**razabilidad.
> - **Mecanismo Firma**: **Firma $=$ Hash Cifrado con Clave Privada**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema09|Fuente Oficial del Tema 09]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema09|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema09-seguridad-criptografia-ens|Test Tema 09]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|⬅️ Tema 08]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema10|Tema 10 ➡️]]
