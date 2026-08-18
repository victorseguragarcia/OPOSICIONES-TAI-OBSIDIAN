---
title: "Resumen Completo Tema 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-08
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema08]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|⬅️ Tema 07]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|Tema 09 ➡️]]

# 🔴 Resumen Completo Tema 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 08**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema profundiza en la infraestructura global de Internet, su jerarquía de operadores y puntos neutros (IXP), la evolución del protocolo HTTP (desde HTTP/1.0 hasta HTTP/3 sobre QUIC), el protocolo criptográfico TLS 1.3, los servicios de transferencia de ficheros (FTP, FTPS, SFTP), la telefonía sobre IP (VoIP con SIP y RTP), el sistema global de nombres de dominio (DNS jerárquico y registros) y la evolución de la World Wide Web hacia la Web Semántica (Web 3.0).

---

## 🧩 Estructura y Desglose Temático

### 1. Arquitectura y Enrutamiento Global en Internet
- **Jerarquía de Proveedores de Servicios de Internet (ISPs)**:
  - **Tier 1**: Operadores troncales globales (Tier 1 Backbones: Lumen, AT&T, Telia, NTT). No pagan por tránsito; intercambian tráfico entre sí mediante acuerdos de **Peering libre de liquidación** (*Settlement-Free Peering*).
  - **Tier 2**: Operadores regionales o nacionales. Hacen peering con otros Tier 2 y compran **Tránsito IP** a operadores Tier 1.
  - **Tier 3**: Proveedores de acceso final a empresas y usuarios residenciales. Compran tránsito a operadores Tier 2/1.
- **Puntos Neutros de Intercambio (IXP - Internet Exchange Points)**:
  - Infraestructuras físicas de conmutación donde múltiples ISPs, CDNs (Cloudflare, Akamai) y proveedores cloud intercambian tráfico directamente reduciendo costes y latencia (ej. **ESpanix** y **DE-CIX** en Madrid).
- **Sistemas Autónomos (AS) y Protocolos de Enrutamiento**:
  - **BGP (Border Gateway Protocol v4 - RFC 4271)**: Protocolo de Vector de Caminos (*Path Vector*) que intercambia rutas entre Sistemas Autónomos distintos mediante sesiones TCP (puerto **179**). Utiliza el atributo AS-PATH para prevenir bucles.
  - **OSPF (Open Shortest Path First - RFC 2328)**: Protocolo IGP de Estado de Enlace (*Link-State*) que calcula rutas óptimas dentro de un mismo Sistema Autónomo usando el algoritmo de **Dijkstra** (protocolo IP número **89**).

### 2. Protocolo HTTP y Evolución de la Web
- **HTTP (Hypertext Transfer Protocol)**: Protocolo cliente-servidor sin estado de la capa de aplicación.
- **Evolución de Versiones**:
  - **HTTP/1.0 (RFC 1945)**: Abre y cierra una conexión TCP por cada objeto solicitado (muy ineficiente).
  - **HTTP/1.1 (RFC 2616 / RFC 9112)**:
    - Conexiones persistentes por defecto (`Keep-Alive`).
    - *Pipelining* de peticiones (limitado por el bloqueo en cabeza de línea o *Head-of-Line Blocking* a nivel de aplicación).
    - Cabecera obligatoria `Host` (permite alojamiento virtual de múltiples dominios en una misma IP).
    - Transferencia fragmentada (*Chunked Transfer Encoding*).
  - **HTTP/2 (RFC 7540 / RFC 9113)** (Basado en SPDY de Google):
    - Protocolo binario (no texto plano).
    - **Multiplexación total**: Múltiples peticiones y respuestas simultáneas intercaladas en *streams* bidireccionales sobre una **única conexión TCP**.
    - Compresión de cabeceras mediante el algoritmo **HPACK** (RFC 7541).
    - *Server Push* (el servidor envía recursos anticipadamente).
    - Priorización de flujos (*Stream Prioritization*).
  - **HTTP/3 (RFC 9114)** (Basado en QUIC):
    - Funciona sobre el protocolo de transporte **QUIC** (RFC 9000), que opera sobre **UDP** (puerto **443 UDP**).
    - Elimina el bloqueo en cabeza de línea (*HoL Blocking*) a nivel de transporte de TCP.
    - Cifrado integrado nativo con **TLS 1.3** desde el primer paquete (0-RTT y 1-RTT connection setup).
    - Migración transparente de conexión (*Connection ID*) ante cambios de red (ej. de Wi-Fi a 4G/5G sin reiniciar conexión).
    - Algoritmo de compresión de cabeceras **QPACK** (RFC 9204).

### 3. Protocolo TLS (Transport Layer Security)
- Protocolo criptográfico que proporciona confidencialidad, integridad y autenticación entre aplicaciones sobre la capa de transporte.
- **Evolución**: SSL 2.0/3.0 (inseguros/obsoletos) → TLS 1.0/1.1 (deprecados) → **TLS 1.2** (RFC 5246) → **TLS 1.3** (RFC 8446).
- **Mejoras Radicales en TLS 1.3**:
  - Negociación (*Handshake*) reducida de 2 viajes de ida y vuelta (2-RTT) a **1 solo RTT** (o **0-RTT** para conexiones reanudadas).
  - Eliminación de algoritmos obsoletos e inseguros (DES, 3DES, RC4, MD5, SHA-1, suites CBC, intercambio RSA estático sin secreto perfecto hacia adelante).
  - Obligatoriedad de **PFS (Perfect Forward Secrecy)** mediante Diffie-Hellman efímero (ECDHE).
  - Cifrado de las extensiones del Handshake (incluido el certificado del servidor).

### 4. Servicios de Transferencia de Archivos y Acceso Remoto
- **FTP (File Transfer Protocol - RFC 959)**:
  - Puertos: **21 TCP** (canal de control) y **20 TCP** (canal de datos en modo activo).
  - Modo Activo (`PORT`) vs. Modo Pasivo (`PASV` - el servidor abre puerto efímero, compatible con NAT/Firewall).
  - En texto plano; vulnerable a intercepción.
- **FTPS (FTP over SSL/TLS - RFC 4217)**: FTP tradicional protegido mediante TLS (modo explícito en puerto 21 o implícito en puerto 990).
- **SFTP (SSH File Transfer Protocol)**: Protocolo completamente diferente que opera encapsulado dentro del túnel seguro de **SSH** (puerto **22 TCP**).
- **SSH (Secure Shell - RFC 4253)**: Puerto **22 TCP**; sustituto seguro y cifrado de Telnet (puerto 23) y `rsh/rlogin`.

### 5. Telefonía sobre IP (VoIP)
- **SIP (Session Initiation Protocol - RFC 3261)**:
  - Protocolo de señalización de la capa de aplicación (puertos **5060 TCP/UDP** para texto plano, **5061 TCP** para TLS).
  - Responsable de iniciar, modificar y terminar sesiones multimedia (llamadas de voz y videoconferencia).
  - Utiliza **SDP** (Session Description Protocol - RFC 4566) para negociar códecs de audio/vídeo (G.711, G.729, Opus).
- **RTP / RTCP (Real-time Transport Protocol - RFC 3550)**:
  - Protocolos de transporte de datos multimedia en tiempo real sobre **UDP** (puertos efímeros pares para RTP y puertos impares para RTCP de control y estadísticas de jitter/paquetes perdidos).
  - **SRTP**: RTP seguro con cifrado AES.

---

## 🎯 Datos Clave para Oposiciones TAI

| Servicio / Protocolo | Puerto Estándar y RFC |
|----------------------|-----------------------|
| HTTP / HTTPS | **80 TCP** (RFC 9112) / **443 TCP** (TLS) |
| HTTP/3 (QUIC) | **443 UDP** (RFC 9114 / RFC 9000) |
| BGP v4 | **179 TCP** (RFC 4271) |
| OSPF v2 | Protocolo IP **89** (RFC 2328) |
| FTP Control / Datos Activo | **21 TCP** / **20 TCP** (RFC 959) |
| SSH / SFTP | **22 TCP** (RFC 4253) |
| SIP / SIPS | **5060 TCP/UDP** / **5061 TLS** (RFC 3261) |
| Compresión cabeceras HTTP/2 / HTTP/3 | **HPACK** (RFC 7541) / **QPACK** (RFC 9204) |
| Latencia Handshake TLS 1.3 | **1-RTT** (primera conexión) / **0-RTT** (reanudación) |
| IXP principal en España | **ESpanix** / **DE-CIX Madrid** |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/http-protocol|Protocolo HTTP: Evolución HTTP/1.1, HTTP/2 y HTTP/3]]
- [[wiki/entities/tls-ssl-protocols|Protocolos TLS/SSL y Criptografía Web]]
- [[wiki/entities/bgp-and-ospf|Protocolos de Enrutamiento: OSPF y BGP]]
- [[wiki/entities/dns-protocol|Protocolo DNS]]

### Conceptos Teóricos:
- [[wiki/concepts/internet-architecture-and-web-protocols|Arquitectura de Internet y Protocolos Web]]
- [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema08|Nota Fuente del Tema 08]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema08-internet-web-correo|Test Tema 08]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|⬅️ Tema 07]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|Tema 09 ➡️]]
