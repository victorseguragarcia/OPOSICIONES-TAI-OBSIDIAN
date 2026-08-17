---
title: "Cheatsheet de Puertos y Protocolos de Red para Oposiciones TAI"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - network-ports
  - protocols
  - tai
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema03.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema07.md"
  - "raw/sources/bloque4-tema08.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet de Puertos"
  - "Network Ports Cheatsheet"
---

# Cheatsheet de Puertos y Protocolos de Red para Oposiciones TAI

Tabla de referencia rápida y memorización obligatoria de los puertos estándar, capas del modelo OSI y especificaciones RFC más preguntadas en las oposiciones de Informática.

---

## 📋 Tabla Maestra de Puertos y Protocolos

| Puerto | Protocolo / Servicio | Capa Transporte | RFC | Función Principal |
|--------|----------------------|-----------------|-----|-------------------|
| **20 / 21** | **FTP (Datos / Control)** | TCP | RFC 959 | Transferencia de archivos clásica en texto plano |
| **22** | **SSH / SFTP** | TCP | RFC 4253 | Shell remota segura y transferencia cifrada |
| **23** | **Telnet** | TCP | RFC 854 | Acceso terminal en texto plano (inseguro/obsoleto) |
| **25** | **SMTP (Relay)** | TCP | RFC 5321 | Transferencia de correo entre servidores MTA |
| **53** | **DNS** | TCP y UDP | RFC 1035 | Resolución de nombres de dominio |
| **67 / 68** | **DHCP (Servidor / Cliente)** | UDP | RFC 2131 | Asignación dinámica de configuración IP (IPv4) |
| **69** | **TFTP** | UDP | RFC 1350 | Protocolo trivial de transferencia de ficheros (PXE) |
| **80** | **HTTP** | TCP | RFC 9112 | Navegación web en texto plano |
| **88** | **Kerberos v5** | TCP y UDP | RFC 4120 | Autenticación centralizada en Active Directory |
| **110** | **POP3** | TCP | RFC 1939 | Descarga de correo del buzón local |
| **123** | **NTP** | UDP | RFC 5905 | Sincronización horaria en red |
| **143** | **IMAP4** | TCP | RFC 3501 | Sincronización bidireccional de buzones de correo |
| **161 / 162** | **SNMP / SNMP Traps** | UDP | RFC 3411 | Monitorización y alertas asíncronas de dispositivos |
| **179** | **BGP v4** | TCP | RFC 4271 | Enrutamiento dinámico interdominio exterior (EGP) |
| **389** | **LDAP** | TCP y UDP | RFC 4511 | Consulta de servicios de directorio en texto plano |
| **443** | **HTTPS (TLS) / HTTP/3** | TCP / **UDP (QUIC)** | RFC 8446 / 9114 | Web segura sobre TLS y HTTP/3 sobre QUIC |
| **445** | **SMB / CIFS** | TCP | MS-SMB2 | Compartición de archivos e impresoras Windows |
| **465** | **SMTPS** | TCP | RFC 8314 | SMTP encapsulado en SSL/TLS directo |
| **500** | **IKE (IPsec)** | UDP | RFC 7296 | Negociación de claves para túneles IPsec |
| **514** | **Syslog** | UDP | RFC 5424 | Registro y recopilación remota de logs del sistema |
| **546 / 547** | **DHCPv6 (Cliente / Servidor)** | UDP | RFC 8415 | Asignación dinámica de IPs en redes IPv6 |
| **587** | **SMTP (Submission)** | TCP | RFC 6409 | Envío autenticado de correo desde clientes MUA |
| **636** | **LDAPS** | TCP | RFC 4511 | LDAP seguro encapsulado en SSL/TLS |
| **993** | **IMAPS** | TCP | RFC 8314 | IMAP seguro con cifrado TLS/SSL directo |
| **995** | **POP3S** | TCP | RFC 8314 | POP3 seguro con cifrado TLS/SSL directo |
| **1194** | **OpenVPN** | UDP y TCP | Proprietary | Conexiones VPN basadas en SSL/TLS |
| **3260** | **iSCSI** | TCP | RFC 3720 | Almacenamiento a nivel de bloque sobre IP (SAN) |
| **3268 / 3269** | **Catálogo Global AD (LDAP/LDAPS)** | TCP | Microsoft | Búsquedas de directorio en todo el bosque AD |
| **3389** | **RDP (Remote Desktop)** | TCP y UDP | MS-RDP | Escritorio remoto de Microsoft Windows |
| **4500** | **IPsec NAT-Traversal (NAT-T)** | UDP | RFC 3948 | Encapsulación de paquetes IPsec ESP sobre routers NAT |
| **5060 / 5061** | **SIP / SIPS (VoIP)** | TCP y UDP / TLS | RFC 3261 | Señalización y establecimiento de llamadas VoIP |
| **5985 / 5986** | **WinRM (HTTP / HTTPS)** | TCP | Microsoft | Administración remota mediante PowerShell |

---

## 🔗 Referencias Cruzadas
- Guía Maestra: [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos ISO-OSI y TCP-IP]]
