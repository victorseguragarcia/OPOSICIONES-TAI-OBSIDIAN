---
title: "Resumen Completo Tema 09 (Bloque 4): Seguridad de la Información, Criptografía y ENS (RD 311/2022)"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-09
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema09]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|⬅️ Tema 08]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema10|Tema 10 ➡️]]

# 🔴 Resumen Completo Tema 09 (Bloque 4): Seguridad de la Información, Criptografía y ENS (RD 311/2022)

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 09**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema aborda la seguridad en redes corporativas y en la Administración Pública española. Detalla el marco normativo e institucional español (CCN, CCN-CERT, Guías CCN-STIC, Esquema Nacional de Seguridad regulado por el **Real Decreto 311/2022**, metodología de análisis de riesgos **MAGERIT v3** y herramienta PILAR); la arquitectura de seguridad perimetral (cortafuegos de filtrado de paquetes, estado de inspección, proxies y NGFW); sistemas de protección activa de comunicaciones (IDS/IPS basados en firmas, anomalías y comportamiento; SIEM para correlación de eventos); y tecnologías de Redes Privadas Virtuales (IPsec en modos transporte/túnel con protocolos AH y ESP, OpenVPN, WireGuard y SSL/TLS VPNs).

---

## 🧩 Estructura y Desglose Temático

### 1. Marco Institucional y Normativo de Ciberseguridad en España
- **Centro Criptológico Nacional (CCN)**:
  - Organismo adscrito al **Centro Nacional de Inteligencia (CNI)** (Ley 11/2002).
  - Competente en la seguridad de las TIC en las administraciones públicas y en sistemas que procesan información clasificada.
- **CCN-CERT**:
  - Capacidad de Respuesta a Incidentes de Seguridad de la Información del CCN.
  - Alertas, guías técnicas, gestión de cibercrisis y herramientas de seguridad del Sector Público (**LUCIA**, **CARMEN**, **CLARA**, **INES**, **PILAR**, **REYES**).
- **Serie de Guías CCN-STIC**:
  - Normas, instrucciones y guías de buenas prácticas para la protección de sistemas TIC en la Administración (ej. Guía CCN-STIC 800 para el ENS).
- **Esquema Nacional de Seguridad (ENS)**:
  - Marco legal obligatorio para todo el Sector Público y sus proveedores tecnológicos privados.
  - Actualizado por el **Real Decreto 311/2022** (derogando el RD 3/2010).
  - **Principios Básicos**: Seguridad integral, gestión de riesgos, prevención/reacción/recuperación, líneas de defensa, vigilancia continua y reevaluación periódica.
  - **Dimensiones de Seguridad**: Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad (**CITAD**).
  - **Categorías del Sistema**: **BÁSICA**, **MEDIA**, **ALTA** (determinadas por el impacto de un incidente en las dimensiones).
- **Metodología MAGERIT v3**:
  - Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información desarrollada por el Consejo Superior de Administración Electrónica (CSAE).
  - Estructura: Activos, Amenazas, Salvaguardas, Impacto y Riesgo Residual. Herramienta asociada: **PILAR**.

### 2. Seguridad Perimetral y Cortafuegos (Firewalls)
- **Evolución de los Cortafuegos**:
  - **1ª Generación (Filtrado de paquetes sin estado / Stateless)**: Inspecciona cabeceras de red y transporte (IP origen/destino, puerto, protocolo). No mantiene estado de la conexión.
  - **2ª Generación (Inspección con estado / Stateful Inspection)**: Mantiene una tabla de conexiones activas. Permite automáticamente el tráfico de retorno de conexiones legítimas salientes (`ESTABLISHED, RELATED`).
  - **3ª Generación (Pasarela a nivel de aplicación / Proxy)**: Termina la conexión del cliente y abre una nueva conexión con el servidor. Inspecciona el payload a nivel de aplicación (Nivel 7).
  - **NGFW (Next-Generation Firewall)**: Combina inspección con estado, prevención de intrusiones (IPS) en línea, inspección profunda de paquetes (**DPI**), descifrado SSL/TLS, control de aplicaciones (independiente del puerto) e integración con inteligencia de amenazas.

### 3. Sistemas de Protección y Monitorización (IDS, IPS, SIEM)
- **IDS (Intrusion Detection System)**: Sistema pasivo que monitoriza el tráfico mediante una copia (puerto espejo / SPAN o TAP). Detecta actividades sospechosas y genera alarmas sin bloquear el tráfico.
  - **NIDS** (Network-based IDS, ej. Snort, Suricata): Monitoriza el tráfico de la subred.
  - **HIDS** (Host-based IDS, ej. OSSEC, Wazuh): Monitoriza registros, integridad de archivos del sistema (`syscheck`) y llamadas al sistema en un equipo individual.
- **IPS (Intrusion Prevention System)**: Sistema activo colocado en línea (*in-line*) en el flujo de paquetes. Detecta y bloquea activamente los ataques en tiempo real (descartando paquetes o reseteando la sesión TCP con flags `RST`).
- **Técnicas de Detección**:
  - **Basada en Firmas / Patrones**: Compara el tráfico con reglas de vulnerabilidades conocidas (muy eficaz contra ataques conocidos, ineficaz contra ataques de día cero / *Zero-Day*).
  - **Basada en Anomalías / Comportamiento**: Define una línea base de comportamiento normal y alerta sobre desviaciones estadísticas (detecta ataques novedosos pero produce mayores tasas de falsos positivos).
- **SIEM (Security Information and Event Management)**:
  - Plataforma centralizada que recopila, normaliza, almacena y correlaciona eventos y logs de seguridad de múltiples fuentes (firewalls, servidores, routers, IDS, antivirus) en tiempo real (ej. Splunk, Elastic SIEM, Microsoft Sentinel).

### 4. Redes Privadas Virtuales (VPN)
- Una VPN permite extender de forma segura una red local privada sobre una red pública no confiable (Internet) mediante cifrado, autenticación e integridad.
- **Tipos de VPN**:
  - **Site-to-Site (LAN-to-LAN)**: Interconexión permanente de dos sedes o centros de datos a través de routers/firewalls VPN.
  - **Remote Access (Roadwarrior / Punto-a-Sitio)**: Conexión segura de un usuario remoto a la red corporativa mediante software cliente.

#### 4.1 Arquitectura IPsec (IP Security - RFC 4301)
- Conjunto de protocolos que operan en la **Capa de Red (Nivel 3)**:
- **Protocolos de Seguridad**:
  - **AH (Authentication Header - RFC 4302, protocolo IP 51)**: Proporciona autenticación de origen e integridad de datos de todo el paquete (incluyendo la cabecera IP). **NO cifra datos** (sin confidencialidad). Incompatible con NAT (el cambio de IP por NAT invalida el checksum de AH).
  - **ESP (Encapsulating Security Payload - RFC 4303, protocolo IP 50)**: Proporciona confidencialidad (cifrado), autenticación de origen e integridad. Permite atravesar NAT mediante encapsulación **NAT-Traversal (NAT-T)** en UDP puerto **4500**.
- **Modos de Operación de IPsec**:
  - **Modo Transporte**: Protege solo la carga útil (*payload*) del paquete IP; la cabecera IP original queda visible. Utilizado para comunicación host-a-host directa.
  - **Modo Túnel**: Encapsula el paquete IP original completo (cabecera + payload) dentro de un **nuevo paquete IP** con una nueva cabecera externa. Modo estándar para VPNs Site-to-Site y Remote Access.
- **IKE (Internet Key Exchange - IKEv1 RFC 2409, IKEv2 RFC 7296)**:
  - Protocolo de negociación y gestión de claves sobre **puerto 500 UDP**.
  - Establece las Asociaciones de Seguridad (**SA - Security Associations**) en dos fases (Fase 1: Canal seguro IKE SA; Fase 2: SAs de IPsec para transferencia de datos).

#### 4.2 Otras Tecnologías VPN
- **SSL/TLS VPN (OpenVPN / WireGuard)**:
  - **OpenVPN**: Opera sobre SSL/TLS en espacio de usuario (puerto por defecto **1194 UDP/TCP**), usa interfaces virtuales `tun`/`tap`.
  - **WireGuard**: Protocolo moderno de VPN ultrarrápido y ligero integrado en el kernel de Linux (criptografía moderna: ChaCha20, Curve25519, Poly1305, BLAKE2s).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Norma | Especificación Técnica |
|-------------------|------------------------|
| Marco Legal ENS | **Real Decreto 311/2022** (2 de mayo de 2022) |
| Adscripción del CCN | **Centro Nacional de Inteligencia (CNI)** |
| Dimensiones ENS | **CITAD** (Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad) |
| Metodología de Riesgos | **MAGERIT v3** (Herramienta PILAR) |
| Protocolos IPsec | **AH** (Protocolo IP 51, sin cifrado) y **ESP** (Protocolo IP 50, con cifrado) |
| Puertos IKE / NAT-T | **500 UDP** (IKE) / **4500 UDP** (NAT-Traversal) |
| Modos IPsec | **Transporte** (solo datos) vs. **Túnel** (paquete completo encapsulado) |
| Diferencia IDS vs IPS | IDS es pasivo (alerta fuera de banda); IPS es activo (bloquea en línea) |
| Herramientas CCN-CERT | **LUCIA** (gestión incidentes), **CARMEN** (APT), **CLARA** (auditoría Windows), **INES** (ENS) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/ccn-cert-and-ens|CCN-CERT, Guías CCN-STIC y Esquema Nacional de Seguridad]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, VPN e IPsec]]
- [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL]]

### Conceptos Teóricos:
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
- [[wiki/concepts/cryptography-and-digital-signatures|Criptografía y Firma Digital]]
- [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD y Recuperación]]

### Síntesis de Estudio:
- [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]

> [!trampa] ⚠️ Trampas Frecuentes de Examen: ENS RD 311/2022 y Criptografía
> 1. **Las 5 Dimensiones de Seguridad del ENS (Regla DADIT)**: **D**isponibilidad, **A**utenticidad, **I**ntegridad, **C**onfidencialidad (o D), **T**razabilidad. Ojo: La 'C' es Confidencialidad y la 'T' es Trazabilidad.
> 2. **Categorización del Sistema en el ENS**: La categoría del sistema (BÁSICA, MEDIA, ALTA) se determina por la **regla del máximo**: la categoría global del sistema es la de la dimensión que haya obtenido el nivel MÁS ALTO.
> 3. **Firma Digital (Criptografía Asimétrica)**: La firma digital se genera cifrando el hash del mensaje con la **CLAVE PRIVADA del emisor** (garantiza autenticidad y no repudio); y se verifica descifrando con la **CLAVE PÚBLICA del emisor**.
> 4. **Diferencia entre Firma Avanzada y Firma Cualificada (eIDAS)**: La Firma Cualificada es una firma avanzada creada mediante un dispositivo cualificado de creación de firmas (QSCD / DNIe) y basada en un certificado cualificado. **Es la única que tiene efecto jurídico equivalente a la firma manuscrita en toda la UE**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema09|Nota Fuente del Tema 09]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema09-seguridad-criptografia-ens|Test Tema 09]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|⬅️ Tema 08]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema10|Tema 10 ➡️]]
