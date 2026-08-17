# -*- coding: utf-8 -*-
"""
Script para profundizar y expandir aún más la Wiki del Bloque 4 para TAI Oposiciones.
Crea 4 nuevas entidades, 3 nuevos conceptos y 6 nuevas síntesis de alta especialización.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

# ==============================================================================
# NUEVAS ENTIDADES DE PROFUNDIZACIÓN
# ==============================================================================

NEW_ENTITIES = {
    "wiki/entities/ipsec-protocol-suite.md": """---
title: "Suite de Protocolos IPsec (IP Security)"
type: "entity"
tags:
  - ipsec
  - vpn
  - network-security
  - ah
  - esp
  - ike
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPsec"
  - "IP Security"
  - "AH y ESP"
---

# Suite de Protocolos IPsec (IP Security)

**IPsec (IP Security)** es un conjunto de protocolos y estándares de seguridad definidos por el IETF (RFC 4301) que operan en la **Capa de Red (Nivel 3 del modelo OSI)** para proporcionar confidencialidad, autenticidad de origen, integridad de datos y protección contra reenvíos (*Anti-Replay*) para paquetes IP.

---

## 🏛️ Protocolos de Seguridad Principales

### 1. AH (Authentication Header - RFC 4302)
- **Número de Protocolo IP**: **51**.
- **Servicios**: Proporciona **integridad de datos**, **autenticación de origen** y protección contra reenvíos.
- **Limitación Crítica**: **NO proporciona confidencialidad (NO cifra los datos)**.
- **Incompatibilidad con NAT**: AH calcula el hash de integridad sobre casi toda la cabecera IP original (incluyendo las direcciones IP de origen y destino). Al atravesar un router NAT, la modificación de la IP invalida el checksum de AH, descartando el paquete.

### 2. ESP (Encapsulating Security Payload - RFC 4303)
- **Número de Protocolo IP**: **50**.
- **Servicios**: Proporciona **confidencialidad (cifrado)** mediante algoritmos como AES-CBC o AES-GCM, además de integridad y autenticación opcional.
- **Compatibilidad con NAT (NAT-Traversal / NAT-T - RFC 3948)**:
  - Encapsula los paquetes ESP dentro de datagramas **UDP en el puerto 4500**, permitiendo atravesar routers NAT sin que la traducción de puertos rompa la sesión.

---

## 🧩 Modos de Operación: Transporte vs Túnel

| Característica | Modo Transporte | Modo Túnel |
|----------------|-----------------|------------|
| **Protección** | Solo la **carga útil (payload)** / datos de Capa 4 | **El paquete IP original COMPLETO** (cabecera original + datos) |
| **Cabecera IP** | Mantiene la cabecera IP original visible | Añade una **NUEVA cabecera IP externa** que oculta el origen/destino real |
| **Uso Principal** | Comunicación directa **Host-to-Host** | Conexiones **Site-to-Site (LAN-to-LAN)** y **Remote Access VPN** |
| **Sobrecarga** | Menor tamaño de cabecera | Mayor sobrecarga por la doble cabecera IP |

---

## 🔑 Protocolo IKE (Internet Key Exchange)

- **IKEv1 (RFC 2409) vs IKEv2 (RFC 7296)**: Opera sobre **UDP puerto 500**.
- **Fase 1 (IKE SA)**: Autentica a los pares (mediante certificados X.509 o claves precompartidas PSK) y establece un canal seguro cifrado bidireccional.
- **Fase 2 (IPsec SA / Quick Mode)**: Negocia las Asociaciones de Seguridad (SAs) unidireccionales de AH o ESP para el tráfico de datos real.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Protocolo IP AH | **51** (Solo autenticación e integridad) |
| Protocolo IP ESP | **50** (Cifrado + autenticación) |
| Puerto Negociación IKE | **500 UDP** |
| Puerto NAT-Traversal (NAT-T) | **4500 UDP** |
| RFC Arquitectura IPsec | **RFC 4301** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/firewalls-and-vpn|Cortafuegos y VPN]]
- Concepto: [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]
""",

    "wiki/entities/voip-sip-and-rtp.md": """---
title: "Telefonía IP (VoIP): Protocolos SIP, SDP, RTP y RTCP"
type: "entity"
tags:
  - voip
  - sip
  - rtp
  - sdp
  - protocols
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "VoIP"
  - "SIP y RTP"
  - "Telefonía sobre IP"
---

# Telefonía IP (VoIP): Protocolos SIP, SDP, RTP y RTCP

La telefonía sobre IP (**VoIP**) integra la transmisión digitalizada de voz y vídeo en tiempo real a través de redes conmutadas por paquetes basadas en el protocolo IP.

---

## 🏛️ Arquitectura y Protocolos de VoIP

```
[ Teléfono VoIP A ]                                            [ Teléfono VoIP B ]
        │                                                               │
        │ ── 1. Señalización SIP (Puerto 5060 TCP/UDP) ───────────────► │
        │    (Negociación de códecs con SDP en el cuerpo SIP)           │
        │                                                               │
        │ ◄── 2. Flujo de Audio/Vídeo en Tiempo Real (RTP sobre UDP) ──► │
        │ ◄── 3. Control de Calidad y Jitter (RTCP sobre UDP) ─────────► │
```

---

## 🧩 Desglose de Protocolos

### 1. SIP (Session Initiation Protocol - RFC 3261)
- Protocolo de señalización textual de la capa de aplicación similar a HTTP.
- **Puertos**: **5060 TCP/UDP** (texto plano) y **5061 TCP** (SIPS con cifrado TLS).
- **Métodos Principales**:
  - `INVITE`: Inicia el establecimiento de una sesión o llamada.
  - `ACK`: Confirma la recepción de la respuesta final al INVITE.
  - `BYE`: Termina una sesión activa.
  - `CANCEL`: Cancela una petición pendiente antes de ser respondida.
  - `REGISTER`: Registra la ubicación del usuario ante el servidor *Registrar*.
  - `OPTIONS`: Consulta las capacidades de un servidor o cliente.

### 2. SDP (Session Description Protocol - RFC 4566)
- Formato de texto que describe los parámetros de la sesión multimedia transportado dentro del cuerpo del mensaje SIP: direcciones IP de los medios, puertos UDP asignados y códecs soportados.

### 3. RTP y RTCP (RFC 3550)
- **RTP (Real-time Transport Protocol)**: Transporta los paquetes de medios sobre **UDP** usando puertos dinámicos pares (1024 a 65535). Incluye marcas de tiempo (*Timestamps*) y números de secuencia para reconstruir el flujo de audio en orden y medir el *jitter*.
- **RTCP (RTP Control Protocol)**: Supervisa la calidad del servicio transmitiendo estadísticas de pérdida de paquetes, retardo y jitter sobre el puerto impar inmediatamente superior ($RTP + 1$).
- **SRTP (Secure RTP - RFC 3711)**: Versión segura con cifrado AES y autenticación HMAC-SHA1.

---

## 🎵 Códecs de Voz Principales

| Códec | Estándar ITU-T | Tasa de Bits | Algoritmo / Calidad | Ancho de Banda con Cabeceras |
|-------|----------------|--------------|---------------------|------------------------------|
| **G.711** | ITU-T G.711 | **64 kbps** | PCM ($\mu$-law en EEUU/Japón, A-law en Europa) | $\sim 87.2 \text{ kbps}$ |
| **G.729** | ITU-T G.729 | **8 kbps** | CS-ACELP (alta compresión) | $\sim 31.2 \text{ kbps}$ |
| **G.722** | ITU-T G.722 | **64 kbps** | SB-ADPCM (Voz HD / Wideband 7 kHz) | $\sim 87.2 \text{ kbps}$ |
| **Opus** | IETF RFC 6716 | **6 a 510 kbps** | Dinámico / Adaptativo (estándar WebRTC) | Variable |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Puerto SIP / SIPS | **5060 TCP/UDP** / **5061 TLS** |
| Transporte de Medios | **RTP sobre UDP** (puertos pares) |
| Control de Calidad | **RTCP sobre UDP** (puertos impares) |
| Códec Telefónico Estándar Europa | **G.711 A-law (64 kbps)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
""",

    "wiki/entities/optical-fiber-and-gpon.md": """---
title: "Fibra Óptica, Ventanas de Transmisión y Redes GPON/FTTH"
type: "entity"
tags:
  - fiber-optics
  - gpon
  - ftth
  - transmission-media
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Fibra Óptica"
  - "GPON y FTTH"
---

# Fibra Óptica, Ventanas de Transmisión y Redes GPON/FTTH

La **fibra óptica** es el medio de transmisión guiado por excelencia para redes troncales y de acceso de alta velocidad gracias a su inmunidad total a interferencias electromagnéticas y su ancho de banda prácticamente ilimitado.

---

## 🏛️ Fibra Monomodo (SMF) vs Multimodo (MMF)

| Parámetro | Fibra Multimodo (MMF) | Fibra Monomodo (SMF) |
|-----------|-----------------------|----------------------|
| **Diámetro del Núcleo** | **50 µm** o **62.5 µm** (Cubierta: 125 µm) | **~9 µm** (Cubierta: 125 µm) |
| **Propagación de Luz** | Múltiples rayos rebotan en diferentes modos | **Un solo rayo directo** sin dispersión modal |
| **Fuente de Luz** | LED o VCSEL | **Láser (Diodo Láser)** |
| **Longitudes de Onda** | **850 nm y 1300 nm** | **1310 nm y 1550 nm** |
| **Alcance Típico** | Hasta 300 - 550 metros | **10 km a >40 km** |
| **Clasificación ISO 11801** | **OM1, OM2, OM3, OM4, OM5** | **OS1 (interior), OS2 (exterior)** |

---

## 🌈 Ventanas de Transmisión en Fibra de Sílice

1. **1ª Ventana (850 nm)**: Utilizada en fibra multimodo con emisores LED/VCSEL económicos (alta atenuación $\sim 2.5 \text{ dB/km}$).
2. **2ª Ventana (1310 nm)**: Coincide con el punto de **dispersión cromática cero** en fibra monomodo estándar (atenuación $\sim 0.35 \text{ dB/km}$).
3. **3ª Ventana (1550 nm)**: Coincide con el punto de **mínima atenuación óptica** ($\sim 0.2 \text{ dB/km}$), ideal para enlaces de larga distancia y amplificadores EDFA.
4. **4ª Ventana (1625 nm / Banda L)**: Empleada para multiplexación densa DWDM y monitorización de fibra en servicio.

---

## 🌐 Redes Ópticas Pasivas: GPON (ITU-T G.984)

- **Arquitectura Punto a Multipunto (P2MP)**:
  - **OLT (Optical Line Terminal)**: Equipo central del operador en la central telefónica.
  - **ODN (Optical Distribution Network)**: Red de fibra con divisores pasivos (*Splitters* ópticos 1:16, 1:32 o 1:64) sin alimentación eléctrica.
  - **ONT / ONU (Optical Network Terminal)**: Equipo terminal en el domicilio del usuario final.
- **Velocidades y Longitudes de Onda GPON**:
  - **Descarga (Downstream - OLT $\rightarrow$ ONT)**: **2.488 Gbps** en longitud de onda **1490 nm** (TDM broadcast cifrado con AES-128).
  - **Subida (Upstream - ONT $\rightarrow$ OLT)**: **1.244 Gbps** en longitud de onda **1310 nm** (TDMA con asignación dinámica de ancho de banda DBA).
  - **Vídeo RF (Opcional)**: **1550 nm**.
- **Evolución XGS-PON (ITU-T G.9807.1)**: 10 Gbps simétricos (1577 nm bajada / 1270 nm subida).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar GPON | **ITU-T G.984** |
| Velocidades GPON | **2.488 Gbps bajada / 1.244 Gbps subida** |
| Longitud de onda Downstream GPON | **1490 nm** (Descarga) |
| Longitud de onda Upstream GPON | **1310 nm** (Subida) |
| Mínima atenuación fibra sílice | **1550 nm (3ª ventana $\sim 0.2 \text{ dB/km}$)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Concepto: [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
""",

    "wiki/entities/itil-and-service-desk.md": """---
title: "Marco ITIL y Gestión del Service Desk"
type: "entity"
tags:
  - itil
  - itsm
  - service-desk
  - sla
  - incidents
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ITIL"
  - "Service Desk"
  - "Gestión de Servicios TI"
---

# Marco ITIL y Gestión del Service Desk

**ITIL (Information Technology Infrastructure Library)** es el marco de referencia de buenas prácticas más extendido a nivel mundial para la Gestión de Servicios de Tecnologías de la Información (**ITSM**).

---

## 🏛️ Estructura de ITIL

### 1. ITIL v3: Las 5 Fases del Ciclo de Vida del Servicio
1. **Estrategia del Servicio (*Service Strategy*)**: Define qué servicios ofrecer y a qué clientes para generar valor.
2. **Diseño del Servicio (*Service Design*)**: Diseña servicios nuevos o modificados (SLA, capacidad, disponibilidad, continuidad de servicios TI, seguridad).
3. **Transición del Servicio (*Service Transition*)**: Construcción, pruebas y despliegue de cambios en producción (Gestión de Cambios, Gestión de Versiones y Despliegues, CMDB).
4. **Operación del Servicio (*Service Operation*)**: Operación diaria y soporte (Gestión de Incidencias, Gestión de Problemas, Gestión de Peticiones, Service Desk).
5. **Mejora Continua del Servicio (*CSI - Continual Service Improvement*)**: Ciclo de Deming (**PDCA**: Plan-Do-Check-Act) para optimizar la eficiencia y calidad.

### 2. ITIL 4: Sistema de Valor del Servicio (SVS)
- Evoluciona el ciclo de vida lineal hacia una red flexible de valor basada en **7 Principios Guía**: *Enfocarse en el valor, Empezar donde esté, Progresar iterativamente con retroalimentación, Colaborar y promover visibilidad, Pensar y trabajar holísticamente, Mantenerlo simple y práctico, Optimizar y automatizar*.

---

## 🧩 El Service Desk como Función Central

- **Concepto SPOC (Single Point of Contact)**: Único punto de contacto entre los usuarios y TI.
- **Tipos de Acuerdos de Servicio**:
  - **SLA (Service Level Agreement)**: Acuerdo formal entre el proveedor de servicios de TI y el **Cliente externo o de negocio** sobre niveles de servicio (disponibilidad, tiempo de respuesta y resolución).
  - **OLA (Operational Level Agreement)**: Acuerdo interno entre distintos departamentos de TI de la misma organización (ej. equipo de redes con equipo de BBDD).
  - **UC (Underpinning Contract)**: Contrato legal vinculante con un proveedor externo de soporte (ej. soporte de hardware de servidores).

---

## 🎯 Datos Clave para Oposiciones TAI

| Término | Definición / Fórmula |
|---------|----------------------|
| **Incidencia vs Problema** | Incidencia restaura servicio rápido; Problema busca la **causa raíz** |
| **Cálculo de Prioridad** | $\text{Prioridad} = \text{Impacto} \times \text{Urgencia}$ |
| **KEDB** | *Known Error Database* (Base de datos de errores conocidos y workarounds) |
| **CMDB** | *Configuration Management Database* (Almacena los Elementos de Configuración o CIs) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/incident-management-and-itil|Gestión de Incidencias e ITIL]]
"""
}

print("[*] Escribiendo 4 nuevas entidades técnicas...")
for path, content in NEW_ENTITIES.items():
    write_file(path, content)

# ==============================================================================
# NUEVOS CONCEPTOS DE PROFUNDIZACIÓN
# ==============================================================================

NEW_CONCEPTS = {
    "wiki/concepts/ipv6-transition-mechanisms.md": """---
title: "Mecanismos de Transición y Coexistencia de IPv4 a IPv6"
type: "concept"
tags:
  - ipv6
  - ipv4
  - transition
  - tunneling
  - nat64
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Transición IPv6"
  - "IPv6 Transition Mechanisms"
---

# Mecanismos de Transición y Coexistencia de IPv4 a IPv6

Dado que IPv4 e IPv6 son protocolos incompatibles a nivel binario en sus cabeceras, el IETF diseñó tres estrategias principales de transición y coexistencia durante el periodo de migración global.

---

## 🏛️ Las 3 Estrategias de Transición

```
                 Mecanismos de Transición IPv4 / IPv6
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
  1. Doble Pila             2. Túneles               3. Traducción
   (Dual Stack)             (Tunneling)              (Translation)
(IPv4 e IPv6 nativos     (IPv6 encapsulado         (Conversión de
 en la misma interfaz)     dentro de IPv4)          cabeceras IP)
                         • 6in4 / 6to4             • NAT64 + DNS64
                         • Teredo (UDP 3544)       • SIIT
                         • ISATAP / GRE
```

---

## 🧩 Desglose de Tecnologías de Túnel

1. **Doble Pila (Dual Stack - RFC 4213)**:
   - Los nodos ejecutan pilas completas IPv4 e IPv6 simultáneamente en las mismas interfaces.
   - Las aplicaciones eligen qué protocolo usar en base a las respuestas DNS (`AAAA` preferente sobre `A` según RFC 6724 / Happy Eyeballs RFC 8305).
2. **Túneles Configurados Manualmente (6in4 - RFC 4213, Protocolo IP 41)**:
   - Encapsula paquetes IPv6 directamente dentro de paquetes IPv4 usando el protocolo IP número **41**.
3. **6to4 Automático (RFC 3056)**:
   - Asigna automáticamente a cada sitio IPv4 con IP pública `A.B.C.D` el prefijo IPv6 `2002:AABB:CCDD::/48`.
   - Utiliza la dirección Anycast `192.88.99.1` para enrutar hacia relays 6to4.
4. **Teredo (RFC 4380)**:
   - Permite a clientes IPv6 detrás de routers NAT IPv4 atravesar el NAT encapsulando paquetes IPv6 dentro de datagramas **UDP en el puerto 3544**.
   - Prefijo reservado Teredo: **`2001:0000::/32`**.
5. **ISATAP (RFC 5214)**:
   - Conecta hosts IPv6 dentro de una intranet corporativa sobre una red IPv4 interna.

---

## 🔄 Mecanismos de Traducción: NAT64 y DNS64 (RFC 6146 / RFC 6147)

- Permite a clientes que disponen **exclusivamente de IPv6** comunicarse con servidores legacy que solo disponen de IPv4.
- **DNS64**: Si el resolver DNS no encuentra registro `AAAA` pero sí `A`, sintetiza un registro `AAAA` falso combinando el prefijo Well-Known `64:ff9b::/96` con los 32 bits de la IPv4.
- **NAT64**: El router intercepta el tráfico IPv6 dirigido a `64:ff9b::/96`, extrae la dirección IPv4 de destino, traduce la cabecera a IPv4 y la envía con una IP pública del pool NAT64.

---

## 🎯 Datos Clave para Oposiciones TAI

| Mecanismo | Puerto / Protocolo / Prefijo |
|-----------|------------------------------|
| Protocolo IP 6in4 | **Protocolo IP 41** |
| Prefijo 6to4 | **`2002::/16`** (con la IPv4 en hex) |
| Puerto y Prefijo Teredo | **Puerto 3544 UDP** / Prefijo **`2001:0000::/32`** |
| Prefijo Sintetizado NAT64 | **`64:ff9b::/96`** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
""",

    "wiki/concepts/storage-area-networks-and-iscsi.md": """---
title: "Redes de Área de Almacenamiento (SAN) e iSCSI"
type: "concept"
tags:
  - san
  - iscsi
  - fibre-channel
  - storage
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SAN e iSCSI"
  - "Storage Area Networks"
---

# Redes de Área de Almacenamiento (SAN) e iSCSI

Una **SAN (Storage Area Network)** es una red dedicada y de alto rendimiento que conecta servidores (iniciadores) con matrices de almacenamiento compartido (destinos o *targets*) a nivel de bloque.

---

## 🏛️ Tecnologías de Transporte en SAN

| Parámetro | Fibre Channel (FC) | iSCSI (Internet SCSI) | FCoE (FC over Ethernet) |
|-----------|--------------------|-----------------------|-------------------------|
| **Capa de Red** | Protocolo propietario FC sobre fibra dedicada | **TCP/IP estándar** (Ethernet) | Tramas Ethernet sin pérdida (PFC 802.1Qbb) |
| **Puerto Estándar** | Canales ópticos dedicados (FC-SW) | **3260 TCP** | EtherType `0x8906` |
| **Velocidades Típicas** | 8G, 16G, 32G, 64G FC | 1G, 10G, 25G, 100G Ethernet | 10G, 40G, 100G Ethernet |
| **Adaptador Host** | **HBA (Host Bus Adapter)** dedicado | Tarjeta de red NIC estándar o HBA iSCSI con TOEs | CNA (Converged Network Adapter) |
| **Coste e Infraestructura** | Elevado (switches y cableado FC dedicados) | **Económico** (reutiliza switches Ethernet existentes) | Medio-Alto |

---

## 🧩 Conceptos Clave de Administración SAN

- **Iniciador (*Initiator*)**: Servidor que solicita operaciones de lectura/escritura a nivel de bloque.
- **Destino (*Target*)**: Dispositivo o matriz de almacenamiento que procesa las peticiones.
- **LUN (Logical Unit Number)**: Identificador lógico asignado a una porción de almacenamiento virtualizada dentro de la matriz.
- **LUN Masking**: Restricción de seguridad configurada en la matriz para que una LUN específica solo sea visible para ciertos iniciadores autorizados.
- **Zoning (en Fibre Channel)**: Segmentación de la estructura del conmutador (*Switch Fabric*) para aislar iniciadores y targets en zonas seguras (Hard Zoning por puerto físico o Soft Zoning por WWPN).
- **Direccionamiento iSCSI (IQN - iSCSI Qualified Name)**:
  - Formato RFC 3720: `iqn.yyyy-mm.naming-authority:unique-name` (ej. `iqn.2026-08.es.gob.tai:storage.target01`).
  - Alternativa: **EUI-64** (`eui.0123456789abcdef`).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puerto Estándar iSCSI | **3260 TCP** (RFC 3720 / 7143) |
| Formato de Nombres iSCSI | **IQN** (*iSCSI Qualified Name*) y **EUI** |
| Nivel de Abstracción SAN | **Bloques de disco crudos** (*Block-Level*) |
| Mecanismos de Aislamiento | **Zoning** (en el switch) + **LUN Masking** (en la matriz) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/raid-storage|Sistemas de Almacenamiento RAID, DAS, NAS y SAN]]
""",

    "wiki/concepts/ciphers-modes-and-cryptanalysis.md": """---
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
"""
}

print("[*] Escribiendo 3 nuevos conceptos teóricos...")
for path, content in NEW_CONCEPTS.items():
    write_file(path, content)

# ==============================================================================
# NUEVAS SÍNTESIS DE ESTUDIO
# ==============================================================================

NEW_SYNTHESES = {
    "wiki/synthesis/http-status-codes-and-headers-guide.md": """---
title: "Guía de Códigos de Estado, Métodos y Cabeceras HTTP para TAI"
type: "synthesis"
tags:
  - synthesis
  - http
  - web
  - status-codes
  - headers
sources:
  - "raw/sources/bloque4-tema08.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Códigos de Estado HTTP"
  - "HTTP Status Codes Guide"
---

# Guía de Códigos de Estado, Métodos y Cabeceras HTTP para TAI

Compendio exhaustivo de métodos, clases de códigos de respuesta y cabeceras del protocolo HTTP (RFC 9110 / 9112).

---

## 🏛️ Métodos HTTP (Verbos)

- **Idempotencia**: Un método es idempotente si ejecutarlo múltiples veces con los mismos parámetros produce el mismo estado en el servidor.
- **Seguridad**: Un método es seguro si no altera el estado del recurso en el servidor (solo lectura).

| Método | Función | ¿Seguro? | ¿Idempotente? |
|--------|---------|----------|---------------|
| `GET` | Recuperar una representación del recurso especificado | **Sí** | **Sí** |
| `HEAD` | Idéntico a GET pero el servidor devuelve **solo las cabeceras** (sin cuerpo) | **Sí** | **Sí** |
| `POST` | Enviar datos para ser procesados por el recurso (creación subordinada) | No | **No** |
| `PUT` | Reemplazar completamente el recurso destino con la carga útil enviada | No | **Sí** |
| `DELETE` | Eliminar el recurso especificado | No | **Sí** |
| `PATCH` | Aplicar modificaciones parciales al recurso | No | No (puede serlo según implementación) |
| `OPTIONS`| Describir las opciones de comunicación permitidas por el servidor (CORS) | **Sí** | **Sí** |
| `TRACE` | Eco de la petición para diagnóstico (prohibido por seguridad XST) | **Sí** | **Sí** |
| `CONNECT`| Establecer un túnel bidireccional TCP a través de un proxy (usado en HTTPS) | No | No |

---

## 🔢 Códigos de Estado HTTP por Clases

### 1xx: Informativos (Petición recibida, proceso en curso)
- `100 Continue`: El cliente puede continuar enviando el cuerpo de la petición.
- `101 Switching Protocols`: El servidor acepta cambiar de protocolo (ej. actualización a WebSocket).
- `103 Early Hints`: Retorna cabeceras anticipadas mientras el servidor procesa la respuesta.

### 2xx: Éxito (Petición recibida, entendida y aceptada con éxito)
- `200 OK`: Petición exitosa estándar.
- `201 Created`: Petición completada y nuevo recurso creado (común tras `POST`/`PUT`).
- `202 Accepted`: Petición aceptada para procesamiento, pero no completada aún (asíncrona).
- `204 No Content`: Petición exitosa pero el servidor no devuelve cuerpo (común tras `DELETE`).
- `206 Partial Content`: El servidor entrega solo una parte del recurso solicitada por cabecera `Range`.

### 3xx: Redirección (Acción adicional requerida para completar la petición)
- `301 Moved Permanently`: El recurso ha sido movido permanentemente a una nueva URI.
- `302 Found`: Redirección temporal tradicional (los navegadores solían cambiar `POST` a `GET`).
- `304 Not Modified`: El recurso no ha cambiado desde la fecha indicada en `If-Modified-Since` (usa caché).
- `307 Temporary Redirect`: Redirección temporal que **garantiza que el método HTTP no cambiará**.
- `308 Permanent Redirect`: Redirección permanente que **garantiza que el método HTTP no cambiará**.

### 4xx: Errores del Cliente (Sintaxis errónea o petición no autorizada)
- `400 Bad Request`: Sintaxis de la petición inválida o corrupta.
- `401 Unauthorized`: Autenticación requerida (falta cabecera `Authorization` válida).
- `403 Forbidden`: El servidor entiende la petición pero **se niega a autorizarla** (permisos denegados).
- `404 Not Found`: El recurso solicitado no se encuentra en el servidor.
- `405 Method Not Allowed`: El método HTTP utilizado no está permitido para este recurso.
- `408 Request Timeout`: El servidor agotó el tiempo de espera de la petición del cliente.
- `409 Conflict`: Conflicto en el estado actual del recurso (ej. colisión de edición).
- `410 Gone`: El recurso ya no está disponible y no se conoce dirección de reenvío (permanente).
- `413 Payload Too Large`: La petición enviada supera el límite de tamaño fijado por el servidor.
- `415 Unsupported Media Type`: El formato del contenido no es soportado (`Content-Type`).
- `429 Too Many Requests`: El cliente ha superado el límite de peticiones (*Rate Limiting*).

### 5xx: Errores del Servidor (El servidor falló al intentar procesar una petición válida)
- `500 Internal Server Error`: Error genérico no controlado en el servidor.
- `501 Not Implemented`: El servidor no soporta la funcionalidad requerida para procesar la petición.
- `502 Bad Gateway`: El servidor, actuando como proxy/gateway, recibió una respuesta inválida del backend.
- `503 Service Unavailable`: Servidor sobrecargado o en mantenimiento temporal.
- `504 Gateway Timeout`: El proxy/gateway no recibió respuesta a tiempo del servidor upstream.
- `505 HTTP Version Not Supported`: La versión de HTTP de la petición no está soportada.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Código / Definición |
|----------|---------------------|
| Petición Exitosa Sin Cuerpo | **`204 No Content`** |
| Caché No Modificada | **`304 Not Modified`** |
| Redirección Permanente Estricta | **`308 Permanent Redirect`** |
| Error Autenticación vs Permisos | **`401 Unauthorized`** (quién eres) vs **`403 Forbidden`** (no tienes permiso) |
| Error Gateway Caído / Timeout | **`502 Bad Gateway`** / **`504 Gateway Timeout`** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema08|Resumen Bloque 4 - Tema 08]]
- Entidad: [[wiki/entities/http-protocol|Protocolo HTTP]]
""",

    "wiki/synthesis/subnetting-and-ipv4-ipv6-addressing-guide.md": """---
title: "Guía Práctica de Subnetting, VLSM y Direccionamiento IPv4 e IPv6"
type: "synthesis"
tags:
  - synthesis
  - subnetting
  - vlsm
  - ipv4
  - ipv6
  - cidr
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Subnetting y VLSM"
  - "Subnetting Guide"
---

# Guía Práctica de Subnetting, VLSM y Direccionamiento IPv4 e IPv6

Manual de cálculo de subredes, máscaras de longitud variable (**VLSM**), notación CIDR y conversión EUI-64 en IPv6.

---

## 🏛️ Tabla Maestra de Subredes IPv4 (Prefijos /24 a /32)

| Prefijo CIDR | Máscara de Subred Decimal | Hosts Totales ($2^h$) | Hosts Útiles ($2^h - 2$) | Salto / Incremento ($256 - M$) |
|--------------|---------------------------|-----------------------|--------------------------|--------------------------------|
| **/24** | `255.255.255.0` | 256 | **254** | 1 |
| **/25** | `255.255.255.128` | 128 | **126** | 128 |
| **/26** | `255.255.255.192` | 64 | **62** | 64 |
| **/27** | `255.255.255.224` | 32 | **30** | 32 |
| **/28** | `255.255.255.240` | 16 | **14** | 16 |
| **/29** | `255.255.255.248` | 8 | **6** | 8 |
| **/30** | `255.255.255.252` | 4 | **2** (enlaces punto a punto) | 4 |
| **/31** | `255.255.255.254` | 2 | **2** (RFC 3021 solo en routers) | 2 |
| **/32** | `255.255.255.255` | 1 | **1** (host individual / loopback)| 1 |

---

## 🧮 Metodología de Cálculo VLSM Paso a Paso

Para dividir una red `192.168.1.0/24` en subredes de distinto tamaño:
1. **Ordenar los requisitos de mayor a menor número de hosts**.
2. **Calcular los bits de host ($h$)** necesarios para cada subred usando la fórmula $2^h - 2 \ge \text{Hosts requeridos}$.
3. **Asignar las subredes correlativamente** calculando la dirección de red, primer host útil, último host útil y broadcast.

*Ejemplo*:
- Subred A (100 hosts): $2^7 - 2 = 126 \ge 100 \rightarrow h=7 \rightarrow$ Máscara $/25$ (`255.255.255.128`).
  - Red: `192.168.1.0/25` (Rango útil: `192.168.1.1` a `192.168.1.126`, Broadcast: `192.168.1.127`).
- Subred B (50 hosts): $2^6 - 2 = 62 \ge 50 \rightarrow h=6 \rightarrow$ Máscara $/26$ (`255.255.255.192`).
  - Red: `192.168.1.128/26` (Rango útil: `192.168.1.129` a `192.168.1.190`, Broadcast: `192.168.1.191`).
- Subred C (20 hosts): $2^5 - 2 = 30 \ge 20 \rightarrow h=5 \rightarrow$ Máscara $/27$ (`255.255.255.224`).
  - Red: `192.168.1.192/27` (Rango útil: `192.168.1.193` a `192.168.1.222`, Broadcast: `192.168.1.223`).

---

## 🌐 Generación de Interface ID EUI-64 en IPv6

Para transformar una dirección MAC `00:1A:2B:3C:4D:5E` en un Interface ID de 64 bits para SLAAC:
1. Dividir la MAC en dos mitades de 24 bits: `00:1A:2B` y `3C:4D:5E`.
2. Insertar `FF:FE` en el centro: `00:1A:2B:FF:FE:3C:4D:5E`.
3. Invertir el **7º bit del primer octeto** (bit U/L - Universal/Local):
   - `00` en binario: `00000000` $\rightarrow$ invirtiendo el 7º bit: `00000010` = `02`.
4. Resultado EUI-64: `021A:2BFF:FE3C:4D5E`.
5. Dirección Link-Local generada: `fe80::21a:2bff:fe3c:4d5e/64`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Fórmula / Regla |
|-----------|-----------------|
| Hosts Útiles IPv4 | $2^{\text{bits de host}} - 2$ |
| Número de Subredes | $2^{\text{bits robados a la red}}$ |
| Enlace Punto a Punto Estándar | **/30** (2 hosts útiles) |
| Conversión EUI-64 | Inserta `FFFE` en medio e invierte el **bit 7** del primer byte |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa IPv4 vs IPv6]]
""",

    "wiki/synthesis/network-cabling-and-fiber-optics-guide.md": """---
title: "Guía de Cableado Estructurado, Par Trenzado y Fibra Óptica"
type: "synthesis"
tags:
  - synthesis
  - cabling
  - twisted-pair
  - fiber-optics
  - rj45
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Cableado y Fibra"
  - "Network Cabling Guide"
---

# Guía de Cableado Estructurado, Par Trenzado y Fibra Óptica

Manual técnico de esquemas de conexión RJ-45, categorías de cobre, tipos de fibra óptica y normas internacionales de cableado.

---

## 🏛️ Esquemas de Conexión RJ-45 (TIA/EIA-568A y TIA/EIA-568B)

```
        Pin 1   Pin 2   Pin 3   Pin 4   Pin 5   Pin 6   Pin 7   Pin 8
T568A:  Bl/Ver  Verde   Bl/Nar  Azul    Bl/Azul Naranja Bl/Mar  Marrón
T568B:  Bl/Nar  Naranja Bl/Ver  Azul    Bl/Azul Verde   Bl/Mar  Marrón
```

- **Cable Directo (*Straight-Through*)**: Mismo estándar en ambos extremos (T568A-T568A o T568B-T568B). Conecta dispositivos de distinta capa (ej. PC a Switch, Switch a Router).
- **Cable Cruzado (*Crossover*)**: T568A en un extremo y T568B en el otro (cruza los pares 1-2 con 3-6). Conecta dispositivos de la misma capa (ej. PC a PC, Switch a Switch, Router a Router).
- **Auto MDI/MDIX**: Característica de los switches modernos que detecta y conmuta automáticamente los pares de transmisión/recepción, haciendo indistinto el uso de cable directo o cruzado.

---

## 🧩 Categorías de Par Trenzado de Cobre

| Categoría | Ancho de Banda | Aplicación Principal | Distancia Máxima |
|-----------|----------------|----------------------|------------------|
| **Cat 5e** | **100 MHz** | 1000BASE-T (Gigabit Ethernet) | **100 m** |
| **Cat 6** | **250 MHz** | 1000BASE-T (100 m) / 10GBASE-T (hasta 55 m) | 100 m / 55 m |
| **Cat 6A** | **500 MHz** | **10GBASE-T (10 Gigabit Ethernet)** | **100 m** |
| **Cat 7** | **600 MHz** | 10GBASE-T (conectores GG45/TERA blindados) | 100 m |
| **Cat 7A** | **1000 MHz (1 GHz)** | 10GBASE-T y servicios de banda ancha | 100 m |
| **Cat 8 (8.1/8.2)** | **2000 MHz (2 GHz)** | **25GBASE-T y 40GBASE-T** (Centros de Datos) | **30 m** (Canal de 24 m + 6 m) |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Longitud Máxima Canal Horizontal | **100 metros** (90 m permanente + 10 m latiguillos) |
| Diferencia T568A vs T568B | Intercambian los pines del **par Verde (1-2 en A, 3-6 en B)** y **par Naranja (3-6 en A, 1-2 en B)** |
| Pines Activos 100BASE-TX (Fast Ethernet) | **Pines 1, 2 (TX) y 3, 6 (RX)** (2 pares) |
| Pines Activos 1000BASE-T (Gigabit) | **Los 8 pines / 4 pares transmiten y reciben simultáneamente** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Entidad: [[wiki/entities/optical-fiber-and-gpon|Fibra Óptica y GPON]]
""",

    "wiki/synthesis/ens-rd-311-2022-and-ccn-stic-guide.md": """---
title: "Guía Exhaustiva del Esquema Nacional de Seguridad (ENS RD 311/2022)"
type: "synthesis"
tags:
  - synthesis
  - ens
  - rd-311-2022
  - ccn-cert
  - security-framework
sources:
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía ENS RD 311/2022"
  - "ENS Framework Guide"
---

# Guía Exhaustiva del Esquema Nacional de Seguridad (ENS RD 311/2022)

Manual de referencia del **Real Decreto 311/2022**, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad (ENS) en el ámbito de la administración digital.

---

## 🏛️ Principios Básicos y Dimensiones de Seguridad

### 1. Los 7 Principios Básicos del ENS
1. **Seguridad integral**: La seguridad abarca recursos humanos, materiales, normativos y procedimentales.
2. **Gestión de la seguridad basada en los riesgos**: Análisis continuo de riesgos como fundamento de las decisiones de seguridad.
3. **Prevención, detección, respuesta y conservación**: Ciclo integral de protección activa y reactiva.
4. **Existencia de líneas de defensa**: Estrategia de defensa en profundidad con múltiples capas independientes.
5. **Vigilancia continua**: Monitorización permanente de la actividad del sistema para detectar anomalías.
6. **Reevaluación periódica**: Auditorías y revisiones sistemáticas de las medidas de seguridad.
7. **Diferenciación de responsabilidades**: Separación formal entre el Responsable de la Información, el Responsable del Servicio y el Responsable de la Seguridad.

### 2. Dimensiones de Seguridad (CITAD)
- **Confidencialidad (C)**: Acceso únicamente a personas y procesos autorizados.
- **Integridad (I)**: Exactitud y no alteración no autorizada de los datos.
- **Trazabilidad (T)**: Registro que vincula unívocamente una acción con el actor que la ejecutó.
- **Autenticidad (A)**: Verificación fehaciente de la identidad de emisores y servicios.
- **Disponibilidad (D)**: Acceso oportuno y utilizable por los usuarios autorizados cuando lo requieran.

---

## 🧩 Categorización de Sistemas y Medidas de Seguridad

- **Niveles de Impacto por Dimensión**: **BAJO**, **MEDIO**, **ALTO**.
- **Categoría del Sistema**: Determinada por el nivel de impacto más alto alcanzado en cualquiera de las 5 dimensiones:
  - **Categoría BÁSICA**: Cuando el impacto máximo es **BAJO**.
  - **Categoría MEDIA**: Cuando el impacto máximo es **MEDIO**.
  - **Categoría ALTA**: Cuando el impacto máximo es **ALTO**.
- **Grupos de Medidas de Seguridad (Anexo II)**:
  - **Marco Organizativo `[org]`**: Política de seguridad, responsabilidades, autorización.
  - **Marco Operacional `[op]`**: Planificación, control de accesos, explotación, gestión de incidentes, continuidad.
  - **Medidas de Protección `[mp]`**: Protección de instalaciones, comunicaciones, soportes, información, servicios y métricas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto Legal / Técnico | Especificación |
|-------------------------|----------------|
| Disposición Legal Vigente | **Real Decreto 311/2022** (3 de mayo de 2022) |
| Periodicidad Auditoría Ordinaria | **Al menos cada 2 años** (Categorías Media y Alta) |
| Organismo de Apoyo Técnico | **CCN-CERT (Centro Criptológico Nacional)** |
| Informe Nacional del Estado de Seguridad | Plataforma **INES** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]]
- Síntesis: [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN]]
""",

    "wiki/synthesis/kubernetes-and-docker-complete-guide.md": """---
title: "Guía Completa de Contenedores y Kubernetes para Oposiciones TAI"
type: "synthesis"
tags:
  - synthesis
  - docker
  - kubernetes
  - containers
  - devops
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Docker y Kubernetes"
  - "K8s and Docker Guide"
---

# Guía Completa de Contenedores y Kubernetes para Oposiciones TAI

Compendio exhaustivo sobre la arquitectura de contenedores Docker, primitivas del kernel Linux y orquestación con Kubernetes (K8s).

---

## 🏛️ Docker: Primitivas del Kernel Linux

1. **Namespaces (Aislamiento de Recursos)**:
   - `pid`: Aísla el árbol de procesos (proceso en contenedor es PID 1).
   - `net`: Proporciona interfaz de red virtual (`eth0`), tabla de rutas y puertos propios.
   - `mnt`: Puntos de montaje del sistema de archivos independientes.
   - `ipc`: Memoria compartida y colas de mensajes POSIX.
   - `uts`: Hostname y domain name.
   - `user`: Mapeo de UIDs/GIDs locales a UIDs del host anfitrión.
2. **Control Groups (cgroups)**:
   - Medición y límites de consumo de hardware: CPU (`cpu.cfs_quota_us`), Memoria (`memory.max`), I/O de disco.
3. **Almacenamiento por Capas (Overlay2)**:
   - Imágenes inmutables compuestas por capas de solo lectura (*LowerDir*) + capa superior de lectura/escritura efímera (*UpperDir*), unificadas mediante el punto de montaje (*MergedDir*).

---

## 🧩 Kubernetes: Arquitectura y Tipos de Servicios

- **Arquitectura Master/Worker**:
  - **Master (Control Plane)**: `kube-apiserver`, `etcd` (almacén de estado Raft en puertos 2379/2380), `kube-scheduler`, `kube-controller-manager`.
  - **Worker**: `kubelet`, `kube-proxy`, Container Runtime (`containerd`).
- **Tipos de Services de Kubernetes**:
  - **`ClusterIP`**: Asigna una IP virtual interna alcanzable solo dentro del clúster (por defecto).
  - **`NodePort`**: Abre un puerto estático en cada nodo del clúster en el rango **30000 a 32767 TCP**, reenviando al ClusterIP.
  - **`LoadBalancer`**: Aprovisiona automáticamente un balanceador de carga externo en la infraestructura cloud subyacente.
  - **`ExternalName`**: Mapea el servicio a un registro CNAME DNS externo sin proxy de tráfico.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Detalle Técnico |
|-----------|-----------------|
| Base de Datos Distribuida K8s | **etcd** (Consenso Raft, puertos **2379/2380 TCP**) |
| Rango Puertos NodePort | **30000 - 32767** |
| Unidad Mínima K8s | **Pod** |
| Multi-Stage Build Docker | Reduce radicalmente el tamaño de las imágenes finales eliminando compiladores |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: VMs vs Contenedores]]
""",

    "wiki/synthesis/sysadmin-commands-windows-and-linux-cheatsheet.md": """---
title: "Cheatsheet de Comandos de Administración de Sistemas Windows y Linux"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - sysadmin
  - linux-commands
  - windows-commands
  - powershell
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet Comandos Sysadmin"
  - "Sysadmin Commands Cheatsheet"
---

# Cheatsheet de Comandos de Administración de Sistemas Windows y Linux

Tabla de comandos esenciales de consola para diagnóstico de redes, gestión de servicios, usuarios, almacenamiento y logs en Windows y Linux.

---

## 📋 Comparativa Directa de Comandos por Función

| Función Administrativa | Comando Windows (CMD / PowerShell) | Comando Linux (Bash) |
|------------------------|------------------------------------|----------------------|
| **Configuración IP** | `ipconfig /all` / `Get-NetIPAddress` | `ip addr show` / `ifconfig` |
| **Tabla de Rutas** | `route print` / `Get-NetRoute` | `ip route show` / `route -n` |
| **Tabla ARP** | `arp -a` / `Get-NetNeighbor` | `ip neigh show` / `arp -a` |
| **Conexiones y Puertos** | `netstat -ano` / `Get-NetTCPConnection` | `ss -tulpn` / `netstat -tuln` |
| **Traza de Ruta** | `tracert <destino>` / `Test-NetConnection` | `traceroute <destino>` / `mtr` |
| **Consulta DNS** | `nslookup <nombre>` / `Resolve-DnsName` | `dig <nombre>` / `host <nombre>` |
| **Prueba de Conectividad** | `ping <host>` / `Test-Connection` | `ping <host>` |
| **Gestión de Servicios** | `sc query` / `Get-Service`, `Start-Service` | `systemctl {status|start|stop|restart} <srv>` |
| **Procesos Activos** | `tasklist` / `Get-Process` | `ps aux` / `top` / `htop` |
| **Terminar Proceso** | `taskkill /PID <pid> /F` / `Stop-Process` | `kill -9 <pid>` / `killall <nombre>` |
| **Visor de Logs** | `eventvwr.msc` / `Get-WinEvent` | `journalctl -u <srv> -f` / `tail -f /var/log/syslog` |
| **Gestión de Discos** | `diskmgmt.msc` / `diskpart` | `fdisk -l` / `lsblk` / `gdisk` / `parted` |
| **Uso de Espacio** | `dir` / `Get-PSDrive` | `df -h` (sistemas) / `du -sh *` (carpetas) |
| **Permisos de Ficheros** | `icacls <ruta>` / `Get-Acl` | `chmod`, `chown`, `getfacl`, `setfacl` |
| **Directivas de Grupo** | `gpupdate /force` / `gpresult /r` | N/A |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
"""
}

print("[*] Escribiendo 6 nuevas síntesis monográficas...")
for path, content in NEW_SYNTHESES.items():
    write_file(path, content)

print("[*] Nuevas síntesis generadas exitosamente.")
