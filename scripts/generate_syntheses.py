# -*- coding: utf-8 -*-
"""
Script generador exhaustivo de Síntesis y Reconstrucción del Catálogo Maestro (index.md y log.md).
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

SYNTHESES = {
    "wiki/synthesis/bloque4-tai-oposiciones-master-guide.md": """---
title: "Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-4
  - oposiciones
  - tai
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

# Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)

Esta guía de síntesis reúne el mapa integral de conocimientos del **Bloque 4 (Sistemas y Comunicaciones)** del temario de Técnicos Auxiliares de Informática (TAI) de la Administración General del Estado.

---

## 🗺️ Mapa Temático del Bloque 4

| Tema | Área Temática Principal | Resumen de Fuente | Entidades Clave | Conceptos Clave |
|------|-------------------------|-------------------|-----------------|-----------------|
| **Tema 01** | Administración de Sistemas Operativos y Software de Base | [[wiki/sources/bloque4-tema01\|Resumen Tema 01]] | [[wiki/entities/linux-kernel\|Linux Kernel]], [[wiki/entities/windows-server\|Windows Server]], [[wiki/entities/active-directory\|Active Directory]], [[wiki/entities/ldap-protocol\|LDAP]], [[wiki/entities/bash-and-shell-scripting\|Bash]], [[wiki/entities/powershell\|PowerShell]] | [[wiki/concepts/operating-system-architecture\|Arquitectura SO]], [[wiki/concepts/process-and-memory-management\|Gestión Procesos/Memoria]], [[wiki/concepts/directory-services-and-identity\|Servicios Directorio]] |
| **Tema 02** | Administración de BBDD, Virtualización y Cloud | [[wiki/sources/bloque4-tema02\|Resumen Tema 02]] | [[wiki/entities/relational-databases-rdbms\|RDBMS]], [[wiki/entities/nosql-databases\|NoSQL]], [[wiki/entities/raid-storage\|Almacenamiento RAID/SAN]] | [[wiki/concepts/database-normalization-and-acid\|Normalización/ACID]], [[wiki/concepts/virtualization-and-cloud-computing\|Virtualización/Cloud]], [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery\|CPD y Continuidad]] |
| **Tema 03** | Servidores de Correo, Contenedores y Microservicios | [[wiki/sources/bloque4-tema03\|Resumen Tema 03]] | [[wiki/entities/smtp-imap-pop3\|SMTP/IMAP/POP3]], [[wiki/entities/docker-and-containers\|Docker]], [[wiki/entities/kubernetes\|Kubernetes]] | [[wiki/concepts/microservices-and-middleware\|Microservicios/Middleware]] |
| **Tema 04** | Administración de Redes LAN y Servicios Básicos | [[wiki/sources/bloque4-tema04\|Resumen Tema 04]] | [[wiki/entities/dns-protocol\|DNS]], [[wiki/entities/dhcp-protocol\|DHCP]] | [[wiki/concepts/routing-and-switching-mechanisms\|Switching/Routing LAN]], [[wiki/concepts/network-security-and-perimeter-defense\|Seguridad Perimetral]] |
| **Tema 05** | Seguridad, Criptografía, CPDs y Gestión de Incidencias | [[wiki/sources/bloque4-tema05\|Resumen Tema 05]] | [[wiki/entities/tls-ssl-protocols\|TLS/SSL]], [[wiki/entities/siem-and-ids-ips\|SIEM/IDS/IPS]], [[wiki/entities/snmp-protocol\|SNMP]] | [[wiki/concepts/cryptography-and-digital-signatures\|Criptografía/Firma]], [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery\|Niveles TIER TIA-942]], [[wiki/concepts/incident-management-and-itil\|ITIL/Incidencias]] |
| **Tema 06** | Medios de Transmisión, Modulación y Wi-Fi/5G | [[wiki/sources/bloque4-tema06\|Resumen Tema 06]] | [[wiki/entities/wi-fi-and-mobile-standards\|Wi-Fi (802.11) y 5G NR]], [[wiki/entities/ethernet-and-ieee-standards\|Ethernet]] | [[wiki/concepts/transmission-media-and-modes\|Medios Transmisión/Fibra]] |
| **Tema 07** | Modelos ISO-OSI / TCP-IP, IPv4 e IPv6 | [[wiki/sources/bloque4-tema07\|Resumen Tema 07]] | [[wiki/entities/ipv4-and-ipv6\|IPv4 e IPv6]], [[wiki/entities/tcp-and-udp\|TCP y UDP]] | [[wiki/concepts/osi-and-tcp-ip-models\|Modelos OSI vs TCP/IP]] |
| **Tema 08** | Arquitectura de Internet, Protocolos Web y Servicios | [[wiki/sources/bloque4-tema08\|Resumen Tema 08]] | [[wiki/entities/http-protocol\|HTTP/1-3]], [[wiki/entities/bgp-and-ospf\|OSPF y BGP]], [[wiki/entities/tls-ssl-protocols\|TLS 1.3]] | [[wiki/concepts/internet-architecture-and-web-protocols\|Arquitectura Internet]] |
| **Tema 09** | Seguridad en Redes, ENS, CCN-CERT y VPNs | [[wiki/sources/bloque4-tema09\|Resumen Tema 09]] | [[wiki/entities/ccn-cert-and-ens\|CCN-CERT y ENS]], [[wiki/entities/firewalls-and-vpn\|Firewalls, IPsec y VPN]] | [[wiki/concepts/network-security-and-perimeter-defense\|Seguridad Redes]] |
| **Tema 10** | Topologías LAN, IEEE 802 y Control de Acceso | [[wiki/sources/bloque4-tema10\|Resumen Tema 10]] | [[wiki/entities/ethernet-and-ieee-standards\|Familia IEEE 802]] | [[wiki/concepts/lan-topologies-and-mac-protocols\|Topologías y CSMA/CD]] |

---

## 📚 Síntesis Monográficas Recomendadas
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI vs TCP-IP]]
- [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
- [[wiki/synthesis/active-directory-and-ldap-guide|Guía Comparativa de Active Directory y LDAP]]
- [[wiki/synthesis/cryptography-algorithms-comparison|Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital]]
- [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
- [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC]]
- [[wiki/synthesis/security-frameworks-ens-magerit-ccn|Marco de Seguridad Pública: ENS, MAGERIT y CCN-STIC]]
""",

    "wiki/synthesis/network-ports-and-protocols-cheatsheet.md": """---
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
""",

    "wiki/synthesis/osi-vs-tcpip-model-comparison.md": """---
title: "Comparativa: Modelo de Referencia ISO-OSI vs Pila de Protocolos TCP-IP"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - osi
  - tcp-ip
  - networking
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "OSI vs TCP/IP"
  - "Comparativa OSI y TCP/IP"
---

# Comparativa: Modelo de Referencia ISO-OSI vs Pila de Protocolos TCP-IP

Matriz de contraste técnico y conceptual entre los dos modelos fundamentales de redes de ordenadores.

---

## 🏛️ Matriz Comparativa Estructural

| Criterio | Modelo de Referencia ISO-OSI | Pila de Protocolos TCP/IP |
|----------|------------------------------|---------------------------|
| **Origen / Organismo** | Desarrollado por ISO e ITU-T (estándar formal teórico) | Desarrollado por DARPA y formalizado por IETF (estándar práctico) |
| **Número de Capas** | **7 Capas** estrictamente definidas | **4 Capas** (o 5 en modelo híbrido didáctico) |
| **Filosofía de Diseño** | Define claramente **Servicios, Interfaces y Protocolos** antes de su implementación | Los protocolos surgieron primero; el modelo describió la arquitectura existente |
| **Capa de Transporte** | Soporta servicios orientados a conexión y no orientados | Soporta ambos (**TCP** orientado a conexión, **UDP** no orientado) |
| **Capa de Red** | Soporta servicios con conexión (X.25) y sin conexión (CLNS) | **Solo sin conexión (Protocolo IP / Datagramas)** |
| **Sesión y Presentación** | Capas independientes dedicadas (5 y 6) | Integradas directamente en la **Capa de Aplicación** |
| **Adopción en el Mundo Real** | Éxito teórico conceptual; escasa adopción comercial directa | **El estándar de facto absoluto de Internet y redes modernas** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Concepto: [[wiki/concepts/osi-and-tcp-ip-models|Modelos Arquitectónicos ISO-OSI y TCP-IP]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Entidad: [[wiki/entities/tcp-and-udp|Protocolos de Transporte: TCP y UDP]]
""",

    "wiki/synthesis/ipv4-vs-ipv6-comparison.md": """---
title: "Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - ipv4
  - ipv6
  - networking
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IPv4 vs IPv6"
  - "Comparativa IPv4 e IPv6"
---

# Comparativa de Direccionamiento y Protocolo: IPv4 vs IPv6

Matriz comparativa de características técnicas entre el protocolo IPv4 tradicional y la siguiente generación IPv6.

---

## 🏛️ Matriz de Características Técnicas

| Parámetro | IPv4 (RFC 791) | IPv6 (RFC 8200) |
|-----------|----------------|-----------------|
| **Tamaño de Dirección** | **32 bits (4 octetos)** | **128 bits (16 octetos)** |
| **Número Total de Direcciones** | $2^{32} \approx 4.29 \times 10^9$ | $2^{128} \approx 3.4 \times 10^{38}$ |
| **Notación Textual** | Decimal con puntos: `192.168.1.254` | Hexadecimal con dos puntos: `2001:db8::1` |
| **Tamaño Cabecera Base** | **20 a 60 bytes** (variable) | **40 bytes FIJOS** (procesamiento óptimo por hardware) |
| **Checksum en Cabecera** | Sí (debe recalcularse en cada router) | **No** (se delega la detección de errores a L2 y L4) |
| **Fragmentación** | Realizada por routers intermedios y emisor | **Exclusivamente por el host emisor** (PMTUD) |
| **Transmisión de Difusión** | **Broadcast** (`255.255.255.255`) | **Inexistente** (sustituido por Multicast optimizado) |
| **Tipos de Direccionamiento** | Unicast, Multicast, Broadcast | Unicast, Multicast, **Anycast** |
| **Mecanismo de Autoconfiguración** | Manual o mediante servidor DHCP | Manual, DHCPv6 o **SLAAC sin estado** (RFC 4862) |
| **Resolución de Direcciones (L2)** | Protocolo **ARP** (Broadcast) | **ICMPv6 Neighbor Discovery (NDP)** (Multicast) |
| **Seguridad (IPsec)** | Opcional | **Nativo y obligatorio por especificación** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
""",

    "wiki/synthesis/virtualization-vs-containerization-comparison.md": """---
title: "Comparativa Arquitectónica: Máquinas Virtuales vs Contenedores"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - virtualization
  - containers
  - docker
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "VM vs Containers"
  - "Virtualización vs Contenedores"
---

# Comparativa Arquitectónica: Máquinas Virtuales vs Contenedores

Análisis comparativo entre la virtualización basada en hipervisores (máquinas virtuales completas) y la virtualización ligera a nivel de sistema operativo (contenedores).

---

## 🏛️ Matriz de Comparación Arquitectónica

| Característica | Máquinas Virtuales (VMs) | Contenedores (Docker / OCI) |
|----------------|--------------------------|-----------------------------|
| **Nivel de Abstracción** | **Hardware completo** (CPU, RAM, Disco, BIOS) | **Sistema Operativo (Espacio de Usuario)** |
| **Capa de Virtualización** | **Hipervisor** (ESXi, Hyper-V, KVM) | **Motor de Contenedores** (Docker, containerd) |
| **Sistema Operativo Invitado** | Requiere un **Guest OS completo e independiente** | **Comparte el Kernel del SO Anfitrión (Host)** |
| **Tiempo de Arranque** | Minutos (arranque de SO completo) | **Milisegundos a Segundos** |
| **Consumo de Recursos** | Alto (Gigabytes de RAM/disco por VM) | Muy bajo (Megabytes de memoria por contenedor) |
| **Densidad de Despliegue** | Decenas de VMs por host físico | Cientos o miles de contenedores por host |
| **Aislamiento y Seguridad** | **Muy alto** (Aislamiento por hardware/anillos) | Alto (Basado en **Namespaces** y **cgroups**) |
| **Portabilidad** | Dependiente del formato de disco virtual (VMDK/VHDX) | **Total** mediante imágenes estándar OCI |
| **Orquestación Típica** | VMware vSphere, OpenStack, Proxmox | **Kubernetes (K8s)**, Docker Swarm |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Concepto: [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Cloud]]
""",

    "wiki/synthesis/active-directory-and-ldap-guide.md": """---
title: "Guía Comparativa y Práctica de Active Directory y LDAP"
type: "synthesis"
tags:
  - synthesis
  - active-directory
  - ldap
  - identity
  - windows-server
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía AD y LDAP"
  - "Active Directory & LDAP Guide"
---

# Guía Comparativa y Práctica de Active Directory y LDAP

Estudio exhaustivo de los servicios de directorio empresariales, el estándar LDAPv3 y la arquitectura de Active Directory Domain Services (AD DS).

---

## 🏛️ Comparativa: LDAP Abierto vs Active Directory

| Aspecto | Servidor LDAP Abierto (OpenLDAP) | Active Directory Domain Services (AD DS) |
|---------|-----------------------------------|------------------------------------------|
| **Proveedor / Licencia** | Código abierto (OpenLDAP License) | Propietario de Microsoft (Windows Server) |
| **Protocolo de Directorio** | LDAPv3 estricto (RFC 4511) | LDAPv3 + Extensiones propietarias de Microsoft |
| **Autenticación Primaria** | Simple Bind / SASL | **Kerberos v5** nativo integrado |
| **Gestión de Políticas** | No integrada (requiere herramientas externas) | **GPO (Group Policy Objects)** integradas |
| **Resolución de Nombres** | Independiente | Estrechamente acoplado con **DNS dinámico** |
| **Replicación** | Syncrepl (Maestro-Esclavo / Multimaestro) | Replicación Multimaestro de particiones de directorio |

---

## 🎯 Datos Clave para Oposiciones TAI

- **Puertos**: LDAP (**389**), LDAPS (**636**), Kerberos (**88**), GC (**3268**), GC-SSL (**3269**).
- **Esquema de Nombres Distinguidos (DN)**: `CN=Nombre,OU=Unidad,DC=dominio,DC=com`.
- **Estructura AD**: Dominios $\rightarrow$ Árboles $\rightarrow$ Bosques.
- **Roles FSMO**: 5 roles (2 de bosque: Schema Master, Domain Naming Master; 3 de dominio: PDC Emulator, RID Master, Infrastructure Master).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/active-directory|Active Directory Domain Services]]
- Entidad: [[wiki/entities/ldap-protocol|Protocolo LDAP y Estándar X.500]]
""",

    "wiki/synthesis/cryptography-algorithms-comparison.md": """---
title: "Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital"
type: "synthesis"
tags:
  - synthesis
  - cryptography
  - encryption
  - hashing
  - digital-signature
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa Criptográfica"
  - "Cryptography Comparison"
---

# Comparativa Exhaustiva de Algoritmos Criptográficos y Firma Digital

Matriz técnica de algoritmos de cifrado simétrico, asimétrico, funciones resumen (hash) y estándares de firma electrónica para el Sector Público.

---

## 🏛️ Matriz de Algoritmos Criptográficos

| Tipo de Criptografía | Algoritmo | Tamaño de Clave / Bloque | Seguridad / Estado Actual | Uso Principal |
|----------------------|-----------|--------------------------|---------------------------|---------------|
| **Simétrica (Bloque)** | **AES (Rijndael)** | Claves: **128, 192, 256 bits**; Bloque: **128 bits** | **Estándar mundial seguro** | Cifrado masivo de datos, TLS, BitLocker, IPsec |
| **Simétrica (Bloque)** | **3DES** | Claves: 112 o 168 bits; Bloque: 64 bits | Deprecado (vulnerable a Sweet32) | Sistemas legados |
| **Simétrica (Bloque)** | **DES** | Clave: 56 bits; Bloque: 64 bits | **Roto / Inseguro** | Obsoleto |
| **Simétrica (Flujo)** | **ChaCha20** | Clave: 256 bits | **Excelente seguridad y velocidad** | TLS 1.3, WireGuard, SSH |
| **Simétrica (Flujo)** | **RC4** | Clave: 40 a 2048 bits | **Roto / Prohibido en TLS** | Obsoleto |
| **Asimétrica** | **RSA** | Claves: **2048, 3072, 4096 bits** | Seguro con $\ge 2048$ bits | Firma digital, certificados X.509 |
| **Asimétrica** | **Diffie-Hellman (DH/ECDH)** | Claves: 2048+ bits / Curvas 256+ bits | **Seguro** | Intercambio de claves con PFS en TLS/IPsec |
| **Asimétrica** | **ECDSA / Ed25519** | Claves: **256, 384, 521 bits** | **Excelente eficiencia y seguridad** | Firmas digitales modernas, TLS 1.3, SSH |
| **Función Hash** | **SHA-2 (SHA-256/512)** | Resumen: **256 / 512 bits** | **Estándar seguro obligatorio** | Firma digital, HMAC, certificados |
| **Función Hash** | **SHA-3 (Keccak)** | Resumen: 224, 256, 384, 512 bits | **Muy seguro (esponja)** | Criptografía avanzada |
| **Función Hash** | **SHA-1** | Resumen: 160 bits | **Deprecado / Colisiones encontradas** | Obsoleto |
| **Función Hash** | **MD5** | Resumen: 128 bits | **Roto completamente** | Solo checksums no criptográficos |

---

## 🎯 Formatos de Firma Electrónica Avanzada (ETSI / eIDAS)
- **CAdES** (ETSI TS 101 733): Para ficheros binarios generales (*CMS Advanced Electronic Signatures*).
- **XAdES** (ETSI TS 101 903): Para documentos estructurados en formato XML.
- **PAdES** (ETSI TS 102 778): Para documentos en formato Adobe PDF (ISO 32000-1).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/cryptography-and-digital-signatures|Criptografía y Firma Digital]]
""",

    "wiki/synthesis/cpd-tier-levels-and-disaster-recovery.md": """---
title: "Guía de Niveles TIER de CPD, RAID y Planes de Continuidad de Negocio"
type: "synthesis"
tags:
  - synthesis
  - cpd
  - tier
  - raid
  - disaster-recovery
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Niveles TIER y RAID"
  - "Datacenter & RAID Guide"
---

# Guía de Niveles TIER de CPD, RAID y Planes de Continuidad de Negocio

Guía integrada sobre la resiliencia en Centros de Proceso de Datos (CPD), matrices de discos RAID y métricas de recuperación ante contingencias.

---

## 🏛️ Resumen de Niveles TIER (ANSI/TIA-942)

```
TIER I: Básico (99.671% / 28.8h caída) ──────► 1 vía, sin componentes redundantes (N)
TIER II: Componentes Redundantes (99.741%) ──► 1 vía, componentes redundantes (N+1)
TIER III: Mantenimiento Concurrente (99.982%) ► 2 vías (1 activa + 1 pasiva), N+1
TIER IV: Tolerante a Fallos (99.995%) ───────► 2 vías activas simultáneas, 2(N+1) / 2N+1
```

---

## 🧩 Comparativa Rápida de Matrices RAID

| Nivel RAID | Mínimo Discos | Discos Tolerados | Capacidad Útil |
|------------|---------------|------------------|----------------|
| **RAID 0** | 2 | **0** | $100\%$ ($N \times S$) |
| **RAID 1** | 2 | **1** | $50\%$ ($1 \times S$) |
| **RAID 5** | 3 | **1** | $(N - 1) \times S$ |
| **RAID 6** | 4 | **2 simultáneos** | $(N - 2) \times S$ |
| **RAID 10**| 4 | **1 por sub-espejo** | $50\%$ |

---

## 🎯 Datos Clave para Oposiciones TAI

- **Estrategia Backup**: **3-2-1** (3 copias, 2 soportes distintos, 1 off-site).
- **Métricas**: **RPO** (Punto temporal de pérdida) y **RTO** (Tiempo de recuperación de servicio).
- **Condiciones CPD**: Temperatura 18-27 °C, Humedad 40-60%.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/datacenter-infrastructure-and-disaster-recovery|Infraestructura de CPD]]
""",

    "wiki/synthesis/email-protocols-smtp-pop-imap-guide.md": """---
title: "Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC"
type: "synthesis"
tags:
  - synthesis
  - email
  - smtp
  - pop3
  - imap
  - dkim
  - spf
  - dmarc
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Protocolos de Correo"
  - "Email Protocols Guide"
---

# Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC

Manual de referencia sobre la arquitectura de correo electrónico corporativo, flujo entre agentes y mecanismos criptográficos contra el phishing y spoofing.

---

## 🏛️ Flujo de Mensajería y Agentes

```
[ Emisor ]
    │ (MUA)
    ▼  [Puerto 587 TCP / STARTTLS]
[ MTA Origen ] (Postfix / Sendmail)
    │  Consulta DNS (Registros MX del dominio destino)
    ▼  [Puerto 25 TCP]
[ MTA Destino ] ──► [ MDA / Mail Store ] (Dovecot)
                          │
                          ▼  [Puerto 993 TCP (IMAPS) / 995 TCP (POP3S)]
                     [ Destinatario (MUA) ]
```

---

## 🧩 Seguridad y Autenticación del Remitente

1. **SPF (Sender Policy Framework - RFC 7208)**: Publica en DNS `TXT` las IPs autorizadas a enviar correos del dominio.
2. **DKIM (DomainKeys Identified Mail - RFC 6376)**: Añade firma criptográfica asimétrica en la cabecera validable con la clave pública en DNS `TXT`.
3. **DMARC (RFC 7489)**: Establece la política de alineación y rechazo (`p=none`, `p=quarantine`, `p=reject`) ante fallos de SPF/DKIM.

---

## 🎯 Datos Clave para Oposiciones TAI

- **Puertos**: SMTP Relay (**25**), Submission (**587**), SMTPS (**465**), POP3/POP3S (**110 / 995**), IMAP/IMAPS (**143 / 993**).
- **Formato Mensaje**: Cabeceras + Línea en blanco + Cuerpo + Finalización con `<CRLF>.<CRLF>`.
- **Extensiones MIME**: RFC 2045-2049 para contenido no ASCII y ficheros binarios.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
""",

    "wiki/synthesis/security-frameworks-ens-magerit-ccn.md": """---
title: "Marco de Seguridad Pública: Esquema Nacional de Seguridad (ENS), MAGERIT y CCN-STIC"
type: "synthesis"
tags:
  - synthesis
  - ens
  - magerit
  - ccn-cert
  - public-sector
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Marco ENS y MAGERIT"
  - "ENS and MAGERIT Framework"
---

# Marco de Seguridad Pública: Esquema Nacional de Seguridad (ENS), MAGERIT y CCN-STIC

Compendio del marco legal, metodologías de análisis de riesgos y organismos rectores de la ciberseguridad en el Sector Público español.

---

## 🏛️ Esquema Nacional de Seguridad (Real Decreto 311/2022)

- **Objeto**: Establecer los principios básicos, requisitos mínimos y medidas de protección para garantizar la seguridad de los sistemas, datos y servicios del Sector Público español.
- **Dimensiones de Seguridad (CITAD)**:
  - **Confidencialidad**: Acceso exclusivo a usuarios autorizados.
  - **Integridad**: Exactitud y completitud de la información.
  - **Trazabilidad**: Registro inmutable de acciones realizadas.
  - **Autenticidad**: Garantía de la identidad de personas y procesos.
  - **Disponibilidad**: Continuidad y accesibilidad del servicio.
- **Categorización de Sistemas**:
  - Determinada por el impacto máximo de un fallo en cualquiera de las 5 dimensiones.
  - **BÁSICA** (Impacto Bajo) $\rightarrow$ **MEDIA** (Impacto Medio) $\rightarrow$ **ALTA** (Impacto Alto).

---

## 🧩 Metodología de Análisis de Riesgos MAGERIT v3

- Desarrollada por el Consejo Superior de Administración Electrónica (CSAE).
- **Fases del Análisis**:
  1. *Identificación de Activos*: Información, servicios, software, hardware, redes, personal.
  2. *Identificación y Valoración de Amenazas*: Desastres naturales, fallos técnicos, ataques intencionados.
  3. *Evaluación de Salvaguardas*: Medidas de prevención, detección, contención y recuperación existentes.
  4. *Estimación del Impacto y Riesgo Residual*: Cálculo de la probabilidad y degradación económica/operativa.
- **Herramienta Oficial**: **PILAR** (desarrollada con apoyo del CCN).

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Legal / Técnica |
|----------|--------------------------------|
| Real Decreto del ENS | **Real Decreto 311/2022** (3 de mayo de 2022) |
| Organismo Rector Ciberseguridad AGE | **Centro Criptológico Nacional (CCN / CNI)** |
| Dimensiones de Seguridad | **CITAD** (Confidencialidad, Integridad, Trazabilidad, Autenticidad, Disponibilidad) |
| Categorías de Seguridad | **Básica, Media, Alta** |
| Herramienta Oficial de Riesgos | **PILAR** (Metodología MAGERIT v3) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]]
"""
}

print("[*] Escribiendo 10 síntesis y guías de estudio monográficas...")
for path, content in SYNTHESES.items():
    write_file(path, content)

print("[*] Síntesis generadas exitosamente.")
