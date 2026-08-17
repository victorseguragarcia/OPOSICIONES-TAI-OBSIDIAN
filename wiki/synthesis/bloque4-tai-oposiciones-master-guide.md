---
title: "Guía Maestra de Bloque 4: Sistemas, Comunicaciones, Redes y Seguridad (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-4
  - oposiciones
  - tai
  - redes
  - tcp-ip
  - windows-server
  - linux
  - virtualizacion
  - ens
  - seguridad
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema03.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema06.md"
  - "raw/sources/bloque4-tema07.md"
  - "raw/sources/bloque4-tema08.md"
  - "raw/sources/bloque4-tema09.md"
  - "raw/sources/bloque4-tema10.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 4"
  - "Bloque 4 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 4: Sistemas, Comunicaciones, Redes y Seguridad (TAI)

Compendio estructurado de estudio para el **Bloque 4**, integrando modelos de red ISO/OSI y TCP/IP, subnetting IPv4/IPv6, protocolos de transporte y aplicación, administración avanzada de Windows Server y Linux, virtualización y Esquema Nacional de Seguridad (ENS).

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 4 (10 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis y Cheatsheets |
|:---|:---|:---|:---|:---|
| **Tema 01** | Conceptos de SO y Arquitectura | [[wiki/sources/bloque4-tema01|Resumen Tema 01]] | [[wiki/entities/docker-and-containers|Docker y Contenedores]] | [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa VMs vs Contenedores]] |
| **Tema 02** | Administración de Windows Server | [[wiki/sources/bloque4-tema02|Resumen Tema 02]] | [[wiki/entities/windows-server|Windows Server]], [[wiki/entities/active-directory|Active Directory]] | [[wiki/synthesis/windows-server-administration-guide|Guía Maestra Windows Server]], [[wiki/synthesis/active-directory-and-ldap-guide|LDAP / Kerberos]] |
| **Tema 03** | Administración de Sistemas Linux | [[wiki/sources/bloque4-tema03|Resumen Tema 03]] | [[wiki/entities/linux-kernel|Linux Kernel]], [[wiki/entities/bash-and-shell-scripting|Bash Scripting]] | [[wiki/synthesis/sysadmin-commands-windows-and-linux-cheatsheet|Cheatsheet Comandos Sysadmin]] |
| **Tema 04** | Redes LAN, DHCP y DNS | [[wiki/sources/bloque4-tema04|Resumen Tema 04]] | [[wiki/entities/dns-protocol|DNS]], [[wiki/entities/dhcp-protocol|DHCP]] | [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet Puertos de Red]] |
| **Tema 05** | Almacenamiento, CPD, RAID y Backup | [[wiki/sources/bloque4-tema05|Resumen Tema 05]] | [[wiki/entities/raid-storage|Sistemas RAID]] | [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía TIER, RAID y DRP]] |
| **Tema 06** | Medios de Transmisión y Cableado | [[wiki/sources/bloque4-tema06|Resumen Tema 06]] | [[wiki/entities/optical-fiber-and-gpon|Fibra Óptica y GPON]] | [[wiki/synthesis/network-cabling-and-fiber-optics-guide|Guía Cableado y Fibras]] |
| **Tema 07** | Modelo OSI, TCP/IP e IPv4/IPv6 | [[wiki/sources/bloque4-tema07|Resumen Tema 07]] | [[wiki/entities/tcp-and-udp|TCP y UDP]], [[wiki/entities/ipv4-and-ipv6|IPv4 e IPv6]] | [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa OSI vs TCP/IP]], [[wiki/synthesis/subnetting-and-ipv4-ipv6-addressing-guide|Subnetting VLSM]] |
| **Tema 08** | Internet, Protocolos Web y Correo | [[wiki/sources/bloque4-tema08|Resumen Tema 08]] | [[wiki/entities/http-protocol|Protocolo HTTP]], [[wiki/entities/smtp-imap-pop3|SMTP, IMAP, POP3]] | [[wiki/synthesis/http-status-codes-and-headers-guide|Guía Códigos HTTP]], [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Email]] |
| **Tema 09** | Seguridad, Criptografía y ENS | [[wiki/sources/bloque4-tema09|Resumen Tema 09]] | [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]], [[wiki/entities/tls-ssl-protocols|TLS / SSL]] | [[wiki/synthesis/ens-rd-311-2022-and-ccn-stic-guide|Guía Exhaustiva ENS]], [[wiki/synthesis/cryptography-algorithms-comparison|Criptografía]] |
| **Tema 10** | Topologías LAN, IEEE 802 y Switching | [[wiki/sources/bloque4-tema10|Resumen Tema 10]] | [[wiki/entities/ethernet-and-ieee-standards|Estándares IEEE Ethernet]] | CSMA/CD vs CSMA/CA, Spanning Tree (STP) |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Modelo OSI vs Pila TCP/IP y Protocolos Clave
- **OSI (7 Capas)**: *Física, Enlace, Red, Transporte, Sesión, Presentación, Aplicación*.
- **TCP/IP (4 Capas)**: *Acceso a Red, Internet, Transporte, Aplicación*.
- **Puertos Esenciales**:
  - **DNS**: 53 (UDP consultas, TCP transferencias de zona).
  - **DHCP**: 67 (Servidor), 68 (Cliente).
  - **HTTP**: 80 | **HTTPS / TLS**: 443 | **HTTP/3**: 443 (sobre protocolo **QUIC / UDP**).
  - **SSH**: 22 | **Telnet**: 23 | **FTP**: 20 (Datos) y 21 (Control).
  - **SMTP**: 25 / 587 | **IMAP**: 143 / 993 (SSL) | **POP3**: 110 / 995 (SSL).
  - **LDAP**: 389 / 636 (LDAPS) | **Kerberos**: 88.

---

### B. Subnetting IPv4 y Direccionamiento IPv6
- **Subnetting IPv4**:
  - `/24`: $256$ IPs ($254$ hosts) | Máscara `255.255.255.0`
  - `/25`: $128$ IPs ($126$ hosts) | Máscara `255.255.255.128`
  - `/26`: $64$ IPs ($62$ hosts) | Máscara `255.255.255.192`
  - `/27`: $32$ IPs ($30$ hosts) | Máscara `255.255.255.224`
  - `/28`: $16$ IPs ($14$ hosts) | Máscara `255.255.255.240`
  - `/29`: $8$ IPs ($6$ hosts) | Máscara `255.255.255.248`
  - `/30`: $4$ IPs ($2$ hosts - enlaces punto a punto) | Máscara `255.255.255.252`
- **IPv6**: 128 bits expresados en 8 grupos hexadecimales de 16 bits. Sin broadcast (sustituido por *Multicast* y *Anycast*). Autoconfiguración SLAAC mediante EUI-64 (invierte el 7º bit del OUI MAC e inserta `FF:FE`).

---

### C. Esquema Nacional de Seguridad (ENS - RD 311/2022)
- **7 Principios Básicos**: Seguridad integral, gestión de riesgos, prevención/reacción/recuperación, líneas de defensa, reevaluación periódica, función diferenciada de seguridad y vigilancia continua.
- **5 Dimensiones de Seguridad**: **Disponibilidad (D), Autenticidad (A), Integridad (I), Confidencialidad (C) y Trazabilidad (T)**.
- **3 Categorías de Seguridad**: **Básica, Media y Alta** (determinadas por el impacto mayor de las dimensiones).

---

## 🔵 3. Batería de Autoevaluación del Bloque 4
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet Completo de Puertos y Protocolos]]
- [[wiki/synthesis/subnetting-and-ipv4-ipv6-addressing-guide|Guía Práctica de Subnetting VLSM]]
- [[wiki/tests/bloques/index-tests-bloques|Simulacros Globales de Bloque 4]]
