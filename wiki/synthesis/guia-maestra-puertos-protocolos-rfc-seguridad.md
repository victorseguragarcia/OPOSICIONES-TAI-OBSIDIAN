---
title: "Guía Maestra de Puertos TCP/UDP, Protocolos de Red, RFCs y Seguridad"
type: "synthesis"
tags:
  - sintesis
  - redes
  - puertos
  - protocolos
  - rfc
  - bloque-4
sources:
  - "[[raw/sources/bloque4-tema07.md]]"
  - "[[raw/sources/bloque4-tema08.md]]"
  - "[[raw/sources/bloque4-tema09.md]]"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Guía Maestra de Puertos TCP/UDP, Protocolos de Red y RFCs

Esta guía de referencia rápida recopila **todos los puertos de red bien conocidos (*Well-Known Ports* 0-1023)**, registrados (*Registered Ports* 1024-49151), protocolos de seguridad y RFCs imprescindibles para el examen de TAI.

---

## 🟣 1. Tabla Maestra de Puertos de Red (Inseguro vs Seguro TLS)

| Servicio / Protocolo | Puerto Inseguro (Texto Plano) | Puerto Seguro (Cifrado SSL/TLS) | Capa Transporte | RFC Principal |
|:---|:---:|:---:|:---:|:---|
| **Web HTTP / HTTPS** | **80** (HTTP) | **443** (HTTPS) | TCP | RFC 9110 / RFC 9112 / RFC 9113 |
| **Transferencia FTP** | **20** (Datos) / **21** (Control) | **989** / **990** (FTPS) \| **22** (SFTP sobre SSH) | TCP | RFC 959 / RFC 4251 |
| **Acceso Remoto Terminal** | **23** (Telnet) | **22** (SSH - Secure Shell) | TCP | RFC 854 / RFC 4253 |
| **Envío de Correo (SMTP)** | **25** (Servidor a Servidor) | **465** (SMTPS) \| **587** (Envío Cliente / Submission STARTTLS) | TCP | RFC 5321 / RFC 6409 |
| **Recepción Correo (POP3)** | **110** (POP3) | **995** (POP3S) | TCP | RFC 1939 / RFC 2595 |
| **Recepción Correo (IMAP)** | **143** (IMAP4) | **993** (IMAPS) | TCP | RFC 9051 / RFC 8314 |
| **Directorio LDAP** | **389** (LDAP) | **636** (LDAPS sobre TLS) | TCP / UDP | RFC 4511 |
| **Servicio DNS** | **53** (Consultas y Transferencia de Zona) | **853** (DNS over TLS - DoT) \| **443** (DoH) | UDP (Consultas) / TCP (Zonas > 512B) | RFC 1035 / RFC 7858 |
| **Configuración Dinámica DHCP** | **67** (Servidor) / **68** (Cliente) | **546** (Cliente IPv6) / **547** (Servidor IPv6) | UDP | RFC 2131 / RFC 8415 |
| **Gestión de Red SNMP** | **161** (Agente) / **162** (Trap) | **10161** / **10162** (SNMPv3 TLS) | UDP | RFC 3411 (SNMPv3) |
| **Sincronización Horaria NTP** | **123** | **123** (NTS sobre 4460) | UDP | RFC 5905 |
| **Bases de Datos MySQL / MariaDB** | **3306** | **3306** (con TLS) | TCP | Estándar Oracle/MySQL |
| **Bases de Datos PostgreSQL** | **5432** | **5432** (con TLS) | TCP | Estándar PostgreSQL |
| **Bases de Datos Microsoft SQL Server** | **1433** | **1433** (con TLS) | TCP | Microsoft TDS |
| **Bases de Datos Oracle Database** | **1521** | **1521** / **2484** (TCPS) | TCP | Oracle TNS |
| **Autenticación Kerberos** | **88** | **88** (Tickets KDC) | UDP / TCP | RFC 4120 |
| **Escritorio Remoto Windows (RDP)** | **3389** | **3389** (NLA / TLS) | TCP / UDP | Microsoft RDP |

---

## 🟣 2. Rangos de Puertos según la IANA (RFC 6335)

```
 [ 0 ────────────── 1023 ] [ 1024 ──────────────── 49151 ] [ 49152 ─────────────── 65535 ]
   Puertos del Sistema        Puertos Registrados              Puertos Dinámicos / Privados
   (Well-Known / Sistema)     (Servicios y Software)           (Efemérides / Clientes)
```

1. **Puertos del Sistema (*Well-Known Ports*)**: Del **0 al 1023**. Asignados a protocolos estándar universales (HTTP, SSH, DNS, etc.). En sistemas Unix requieren privilegios de `root` para abrir sockets.
2. **Puertos Registrados (*Registered Ports*)**: Del **1024 al 49151**. Asignados por IANA a aplicaciones y servicios específicos (ej. MySQL 3306, RDP 3389, Tomcat 8080).
3. **Puertos Dinámicos o Privados (*Dynamic / Ephemeral Ports*)**: Del **49152 al 65535**. Utilizados por los sistemas operativos como puertos origen temporales en conexiones salientes cliente-servidor.

---

## 🟣 3. Tabla de RFCs Fundamentales en Oposiciones TAI

| RFC | Título y Materia | Concepto Clave de Examen |
|:---|:---|:---|
| **RFC 791** | IPv4 (Internet Protocol v4) | Formato de cabecera de 20 a 60 bytes, TTL, Fragmentación. |
| **RFC 793** | TCP (Transmission Control Protocol) | Conexión orientada a circuito fiable, *Three-Way Handshake* (SYN, SYN-ACK, ACK). |
| **RFC 768** | UDP (User Datagram Protocol) | Protocolo no orientado a conexión, no fiable, cabecera de **8 bytes**. |
| **RFC 1918** | Direccionamiento Privado IPv4 | `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. |
| **RFC 8200** | IPv6 (sustituye a RFC 2460) | Direcciones de **128 bits**, cabecera fija de **40 bytes**, eliminación de broadcast (usa Anycast/Multicast). |
| **RFC 2131** | Protocolo DHCP | Proceso **DORA** (*Discover, Offer, Request, Acknowledge*), puertos 67 y 68. |
| **RFC 1035** | Sistema DNS | Tipos de registros (A, AAAA, CNAME, MX, PTR, NS, SOA, TXT). |
| **RFC 9110** | Semántica HTTP | Métodos HTTP (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD), idempotencia. |
| **RFC 8446** | Protocolo TLS 1.3 | Cifrado seguro, eliminación de algoritmos obsoletos (RC4, 3DES), *Handshake* 1-RTT y 0-RTT. |
| **RFC 4120** | Kerberos v5 | Autenticación mediante tickets (AS, TGS, Service Ticket) en Active Directory (puerto 88). |
