---
title: "Resumen Completo Tema 05 (Bloque 4): Copias de Seguridad, Regla 3-2-1, RPO/RTO y Continuidad de Negocio"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-05
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema05]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|⬅️ Tema 04]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|Tema 06 ➡️]]

# 🔴 Resumen Completo Tema 05 (Bloque 4): Copias de Seguridad, Regla 3-2-1, RPO/RTO y Continuidad de Negocio

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 05**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema aborda con profundidad cuatro grandes áreas de la seguridad física y lógica: los conceptos fundamentales de seguridad (dimensiones CIDAN, análisis de riesgos, amenazas, vulnerabilidades y taxonomía de ciberataques); los algoritmos criptográficos (simétricos, asimétricos, funciones hash, firma digital, formatos XAdES/PAdES/CAdES y certificados digitales X.509); el diseño y acondicionamiento físico de Centros de Proceso de Datos bajo la norma **ANSI/TIA-942** y la clasificación **TIER I a IV**; y los sistemas de gestión de incidencias y gobierno de servicios TI según el marco **ITIL** (Service Desk, ciclo de vida de incidencias, SLA).

---

## 🧩 Estructura y Desglose Temático

### 1. Seguridad de la Información: Principios y Amenazas
- **Dimensiones de la Seguridad (CIDAN / ENS)**:
  - **Confidencialidad**: Acceso exclusivo a personas autorizadas.
  - **Integridad**: Garantía de que la información no ha sido alterada indebidamente.
  - **Disponibilidad**: Acceso y utilización de los sistemas cuando se requiera.
  - **Autenticidad**: Garantía de la identidad del emisor/origen.
  - **Trazabilidad (No Repudio)**: Registro auditable de las acciones realizadas sin posibilidad de negar su autoría.
- **Taxonomía de Amenazas y Ciberataques**:
  - Ataques de Malware: Virus, Gusanos, Troyanos, Ransomware, Spyware, Rootkits, Botnets.
  - Ataques de Red: Man-in-the-Middle (MitM), Spoofing (IP, ARP, DNS), DoS/DDoS (SYN Flood, Amplificación DNS/NTP, Smurf), Inyecciones SQL (SQLi), Cross-Site Scripting (XSS).
  - Ataques de Canal Lateral (Side-Channel): Análisis de consumo energético, radiación electromagnética (TEMPEST) y tiempos de ejecución.
  - Ingeniería Social: Phishing, Spear Phishing, Vishing, Smishing, Baiting.
- **Auditorías de Seguridad**: Test de intrusión (*Penetration Testing*: Caja Negra, Caja Gris, Caja Blanca) y Análisis Forense Digital (cadena de custodia, adquisición de evidencias volátiles en RAM antes que almacenamiento persistente).

### 2. Criptografía y Firma Digital
- **Criptografía Simétrica (Clave Secreta)**:
  - Misma clave para cifrar y descifrar. Muy rápida, ideal para grandes volúmenes de datos.
  - Algoritmos de bloque: **AES** (Rijndael, bloques de 128 bits, claves de 128/192/256 bits), **DES** (56 bits, obsoleto), **3DES** (112/168 bits), **Blowfish**, **Twofish**, **IDEA**, **RC4** (flujo, obsoleto).
- **Criptografía Asimétrica (Clave Pública / Privada)**:
  - Clave pública para cifrar/verificar; clave privada para descifrar/firmar.
  - Basada en problemas matemáticos difíciles (factorización de números primos grandes, logaritmo discreto, curvas elípticas).
  - Algoritmos: **RSA** (longitudes típicas 2048, 4096 bits), **Diffie-Hellman** (intercambio de claves), **DSA**, **ECDSA / Ed25519** (Criptografía de Curva Elíptica).
- **Criptografía Híbrida**: Combina la velocidad del cifrado simétrico (para el payload con una clave de sesión efímera) con la seguridad del asimétrico (para cifrar la clave de sesión). Empleado en TLS, PGP y SSH.
- **Funciones Hash (Resumen Unidireccional)**:
  - Propiedades: Unidireccionalidad (imposible obtener el mensaje original del hash), resistencia a colisiones (dos mensajes distintos no producen el mismo hash) y efecto avalancha.
  - Algoritmos: **MD5** (128 bits, roto), **SHA-1** (160 bits, deprecado), **SHA-2** (SHA-256, SHA-512), **SHA-3** (Keccak).
- **Firma Digital y Certificados X.509**:
  - Proceso: `Hash(Mensaje)` cifrado con la `Clave Privada del Emisor`. El receptor descifra con la `Clave Pública del Emisor` y compara con su propio cálculo del hash.
  - Formatos de Firma Electrónica Avanzada:
    - **CAdES** (CMS Advanced Electronic Signatures): Para ficheros binarios genéricos.
    - **XAdES** (XML Advanced Electronic Signatures): Para documentos basados en XML.
    - **PAdES** (PDF Advanced Electronic Signatures): Integrada nativamente en ficheros PDF (ISO 32000-1).
  - **Jerarquía de Certificados**: Autoridad de Certificación Raíz (CA), CA Subordinadas, Autoridad de Registro (RA), Listas de Revocación de Certificados (**CRL**) y protocolo de consulta en tiempo real **OCSP** (RFC 6960, puerto 80 HTTP).

### 3. Infraestructura Física de CPDs: Estándar ANSI/TIA-942
El estándar **ANSI/TIA-942** (*Telecommunications Infrastructure Standard for Data Centers*) define los requisitos de arquitectura, climatización, suministro eléctrico y telecomunicaciones organizados en **4 niveles TIER**:

| Nivel TIER | Nombre / Tipo | Disponibilidad | Redundancia | Tiempo Inactividad Anual | Vías de Distribución |
|------------|---------------|----------------|-------------|--------------------------|---------------------|
| **TIER I** | Básico | 99.671% | N (Sin redundancia) | 28.8 horas/año | 1 vía única (sin tolerancia a fallos) |
| **TIER II** | Componentes Redundantes | 99.741% | N+1 (Componentes redundantes) | 22.0 horas/año | 1 vía única |
| **TIER III** | Mantenimiento Concurrente | 99.982% | N+1 (Mantenible sin parar) | 1.6 horas/año | 1 activa + 1 pasiva (2 vías) |
| **TIER IV** | Tolerante a Fallos | 99.995% | 2(N+1) o 2N+1 | 26.3 minutos/año | 2 vías activas simultáneas |

- **Condiciones Ambientales en CPD (ASHRAE TC 9.9)**:
  - Temperatura recomendada: **18 °C a 27 °C**.
  - Humedad relativa: **40% a 60%** (prevenir condensación y descargas electrostáticas ESD).
  - Diseño de pasillos: **Pasillo frío / Pasillo caliente** (*Hot/Cold Aisle containment*).
  - Sistemas de extinción de incendios: Gases limpios no conductores que no dañan componentes electrónicos (Novec 1230, FM-200, Inergen) sustituyendo al gas Halón (prohibido).
  - Suministro eléctrico: SAIs (*UPS* Online de doble conversión), grupos electrógenos diésel y doble acometida desde subestaciones eléctricas independientes (TIER IV).

### 4. Gestión de Servicios e Incidencias (ITIL)
- **ITIL (Information Technology Infrastructure Library)**: Marco de buenas prácticas para la Gestión de Servicios TI (ITSM).
- **Service Desk (Centro de Servicios)**: Único punto de contacto (SPOC) entre los usuarios y el departamento de TI.
  - Diferencia: *Help Desk* (soporte técnico reactivo de primer nivel) vs. *Service Desk* (enfoque global integrado en la estrategia del negocio).
- **Ciclo de Vida de una Incidencia**:
  1. Identificación y Registro (Ticket).
  2. Clasificación y Categorización.
  3. Priorización (Impacto x Urgencia).
  4. Diagnóstico Inicial.
  5. Escalamiento (Funcional a Nivel 2/3 o Jerárquico).
  6. Investigación y Diagnóstico.
  7. Resolución y Recuperación.
  8. Cierre de la Incidencia y Encuesta de Satisfacción.
- **SLA (Service Level Agreement)**: Acuerdo de nivel de servicio que define los tiempos máximos comprometidos de respuesta y resolución.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Estándar | Especificación Técnica |
|----------------------|------------------------|
| Estándar de CPDs | **ANSI/TIA-942** |
| Disponibilidad TIER I | **99.671%** (28.8 h caída/año, N) |
| Disponibilidad TIER II | **99.741%** (22.0 h caída/año, N+1) |
| Disponibilidad TIER III | **99.982%** (1.6 h caída/año, Mantenimiento concurrente) |
| Disponibilidad TIER IV | **99.995%** (26.3 min caída/año, Tolerante a fallos 2N+1) |
| AES Tamaños de Clave | **128, 192 y 256 bits** (bloques fijos de 128 bits) |
| SHA-2 Tamaños Hash | **SHA-224, SHA-256, SHA-384, SHA-512** |
| Formatos Firma Avanzada | **CAdES** (binario), **XAdES** (XML), **PAdES** (PDF) |
| Protocolo Estado Certificado | **OCSP** (RFC 6960, puerto 80 HTTP) vs **CRL** |
| SPOC en ITIL | **Service Desk** (Single Point of Contact) |
| Prioridad de Incidencia | `Prioridad = Impacto * Urgencia` |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL y Criptografía Híbrida]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, VPN y Defensa Perimetral]]
- [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
- [[wiki/entities/ccn-cert-and-ens|CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad]]

### Conceptos Teóricos:
- [[wiki/concepts/cryptography-and-digital-signatures|Criptografía Simétrica, Asimétrica y Firma Digital]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Niveles TIER]]
- [[wiki/concepts/incident-management-and-itil|Gestión de Incidencias y Marco ITIL]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital]]
- [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
- [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema05|Nota Fuente del Tema 05]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema05-almacenamiento-cpd-raid|Test Tema 05]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|⬅️ Tema 04]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|Tema 06 ➡️]]
