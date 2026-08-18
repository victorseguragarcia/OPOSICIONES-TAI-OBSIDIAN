---
title: "Resumen Exhaustivo Tema 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-08
  - sistemas
  - redes
  - seguridad
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema08.md]]"
  - "[[wiki/sources/bloque4-tema08]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|⬅️ Tema 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|Tema 09 ➡️]]

# 🔴 Resumen Exhaustivo Tema 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 08**
> Capa de transporte TCP/IP, protocolo TCP (RFC 793, orientado a conexión, 3-way handshake, control de flujo con ventana deslizante, control de congestión), protocolo UDP (RFC 768, no orientado a conexión), cabeceras de transporte y Tabla Maestra de Puertos IANA (Well-Known Ports 0-1023, Registered Ports 1024-49151, Dynamic/Private Ports 49152-65535).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Protocolo TCP vs Protocolo UDP

| Característica | TCP (Transmission Control Protocol - RFC 793) | UDP (User Datagram Protocol - RFC 768) |
|:---|:---|:---|
| **Orientación a Conexión** | **Orientado a conexión** (requiere 3-way handshake previo). | **Sin conexión (Connectionless)** (envía datagramas directamente). |
| **Fiabilidad** | **Fiable**: Garantiza entrega mediante ACKs y retransmisiones. | **No fiable**: Sin confirmación de entrega ni retransmisión. |
| **Orden de Paquetes** | **Garantiza el orden** mediante números de secuencia. | No garantiza el orden de llegada. |
| **Control de Flujo** | **SÍ (Ventana Deslizante / Sliding Window)**. | ❌ NO |
| **Control de Congestión** | **SÍ** (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery). | ❌ NO |
| **Tamaño Cabecera** | **20 bytes mínima** (hasta 60 bytes con opciones). | **8 bytes fija**. |
| **Casos de Uso Típicos** | Web (HTTP/HTTPS), Correo (SMTP/IMAP), Ficheros (FTP/SSH), BBDD. | Streaming en tiempo real (VoIP, RTP), DNS, DHCP, SNMP, NTP, Gaming. |

- **Establecimiento y Cierre de Conexión TCP**:
  - *Handshake de 3 Vías (3-Way Handshake)*:
    1. Cliente $\rightarrow$ Servidor: `SYN` (Seq = $x$).
    2. Servidor $\rightarrow$ Cliente: `SYN-ACK` (Seq = $y$, Ack = $x+1$).
    3. Cliente $\rightarrow$ Servidor: `ACK` (Seq = $x+1$, Ack = $y+1$).
  - *Cierre de Conexión (4 Pasos)*: `FIN` $\rightarrow$ `ACK` $\rightarrow$ `FIN` $\rightarrow$ `ACK`.

### 2. Tabla Maestra de Puertos de Examen (IANA)

| Puerto TCP/UDP | Protocolo | Descripción del Servicio |
|:---:|:---|:---|
| **20 / 21 TCP** | **FTP** | File Transfer Protocol (20 Datos en modo activo / 21 Control y comandos). |
| **22 TCP** | **SSH / SFTP** | Secure Shell (acceso remoto seguro y transferencia SFTP cifrada). |
| **23 TCP** | **Telnet** | Acceso a terminal remoto en texto plano sin cifrar. |
| **25 TCP** | **SMTP** | Simple Mail Transfer Protocol (envío/retransmisión de correo entre servidores). |
| **53 TCP/UDP** | **DNS** | Domain Name System (UDP resolución / TCP transferencias de zona). |
| **67 / 68 UDP** | **DHCP / BOOTP** | Dynamic Host Configuration Protocol (67 Servidor / 68 Cliente). |
| **69 UDP** | **TFTP** | Trivial FTP (transferencia de imágenes y firmware por UDP sin autenticación). |
| **80 TCP** | **HTTP** | HyperText Transfer Protocol (web en texto claro). |
| **110 TCP** | **POP3** | Post Office Protocol v3 (descarga de correo del buzón). |
| **123 UDP** | **NTP** | Network Time Protocol (sincronización de reloj horario). |
| **143 TCP** | **IMAP** | Internet Message Access Protocol (gestión de correo sincronizado en servidor). |
| **161 / 162 UDP** | **SNMP** | Simple Network Management Protocol (161 Consultas / 162 Traps del agente). |
| **389 TCP/UDP** | **LDAP** | Lightweight Directory Access Protocol (texto claro o StartTLS). |
| **443 TCP** | **HTTPS** | HTTP sobre TLS/SSL (web segura cifrada). |
| **445 TCP** | **SMB / CIFS** | Microsoft Server Message Block (compartición de archivos en red). |
| **465 TCP** | **SMTPS** | SMTP sobre SSL/TLS implícito. |
| **587 TCP** | **SMTP Submission** | Envío de correo autenticado desde clientes de correo (STARTTLS). |
| **636 TCP** | **LDAPS** | LDAP sobre SSL/TLS. |
| **993 TCP** | **IMAPS** | IMAP sobre SSL/TLS. |
| **995 TCP** | **POP3S** | POP3 sobre SSL/TLS. |
| **2049 TCP/UDP** | **NFS** | Network File System (almacenamiento compartido Linux). |
| **3260 TCP** | **iSCSI** | Almacenamiento en bloque IP SAN. |
| **3268 / 3269 TCP** | **Global Catalog** | Catálogo Global de Active Directory (3268 plano / 3269 SSL). |
| **3306 TCP** | **MySQL / MariaDB** | Conexión al servidor de base de datos MySQL. |
| **3389 TCP/UDP** | **RDP** | Remote Desktop Protocol de Microsoft. |
| **5432 TCP** | **PostgreSQL** | Conexión al servidor de base de datos PostgreSQL. |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 08 (Bloque 4)**
> 1. **FTP Puertos 20 y 21**: Puerto **21 es para Control/Comandos**; puerto **20 es para Datos** (en modo activo).
> 2. **Tamaño de Cabecera**: Cabecera **UDP fija de 8 bytes**; Cabecera **TCP mínima de 20 bytes**.
> 3. **SNMP Puertos**: Puerto **161 UDP** para consultas (Get/Set); Puerto **162 UDP** para alarmas/notificaciones (**Traps**).
> 4. **Buzón de Correo Seguro**: IMAPS usa el puerto **993**; POP3S usa el puerto **995**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Puertos de Correo**:
>   - **Envío**: **25 (SMTP) / 587 (Submission)**.
>   - **Recepción**: **110 (POP3) / 143 (IMAP)**.
>   - **Recepción Segura**: **993 (IMAPS) / 995 (POP3S)**.
> - **Cabeceras Transporte**: **UDP $= 8$ Bytes / TCP $= 20$ Bytes**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema08|Fuente Oficial del Tema 08]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema08|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema08-internet-web-correo|Test Tema 08]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema07|⬅️ Tema 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|Tema 09 ➡️]]
