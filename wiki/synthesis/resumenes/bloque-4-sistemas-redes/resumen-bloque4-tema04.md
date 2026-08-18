---
title: "Resumen Completo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-04
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]

# 🔴 Resumen Completo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 04**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema profundiza en el diseño, administración, segmentación y servicios fundamentales de las redes de área local (LAN). Se analizan los esquemas de arquitectura de red perimetral (esquemas simples, con DMZ o zona neutra, múltiples zonas internas y DMZs compuestas), conceptos de Intranet y Extranet, direccionamiento MAC e IP (herramientas `ipconfig`, `ifconfig`, `ip`), servicios de infraestructura crítica (DHCP y el ciclo DORA, DNS y resolución recursiva/iterativa), administración de usuarios y grupos en sistemas cliente y servidor (Windows y Linux), y gestión de almacenamiento de discos y periféricos compartidos.

---

## 🧩 Estructura y Desglose Temático

### 1. Esquemas de Arquitectura de Red y DMZ
- **Concepto de DMZ (Zona Desmilitarizada / Zona Neutra)**: Subred intermedia ubicada entre la red no confiable (Internet) y la red corporativa interna protegida.
- **Topologías Perimetrales**:
  - **Esquema Básico**: Router con cortafuegos conectando red interna con Internet.
  - **Esquema con DMZ y un solo cortafuegos (Three-Pronged / Cortafuegos de 3 patas)**: Una interfaz para Internet, otra para la DMZ (servidores web, correo externo, DNS público) y otra para la LAN interna.
  - **Esquema con DMZ entre dos cortafuegos (Back-to-Back)**: Máxima seguridad; cortafuegos perimetral externo y cortafuegos interno (idealmente de fabricantes distintos para evitar vulnerabilidades comunes).
  - **Esquemas con múltiples DMZs**: Separación de DMZ pública (servicios web) y DMZ de aplicaciones/datos intermedias.
- **Intranets y Extranets**:
  - **Intranet**: Red privada basada en protocolos de Internet (HTTP, TCP/IP) accesible exclusivamente por los miembros de la organización.
  - **Extranet**: Extensión controlada de la intranet accesible a usuarios externos autorizados (proveedores, socios, clientes) mediante túneles VPN o TLS.

### 2. Direccionamiento y Configuración de Red
- **Dirección MAC (Media Access Control)**:
  - Identificador físico de 48 bits (6 bytes) en la capa de enlace (Nivel 2).
  - Primeros 24 bits: **OUI** (Organizationally Unique Identifier) asignado por el IEEE.
  - Últimos 24 bits: Asignados por el fabricante (NIC).
- **Herramientas de Configuración y Diagnóstico**:
  - **Windows**: `ipconfig /all`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
  - **Linux clásico**: `ifconfig` (paquete `net-tools`, en desuso).
  - **Linux moderno**: Comando `ip` (paquete `iproute2`): `ip addr show`, `ip link set dev eth0 up`, `ip route show`.

### 3. Servicios de Infraestructura Básica

#### 3.1 Protocolo DHCP (Dynamic Host Configuration Protocol)
- Definido en **RFC 2131** (IPv4) y **RFC 8415** (DHCPv6).
- Puertos estándar: **67 UDP** (Servidor) y **68 UDP** (Cliente). En DHCPv6: **546 UDP** (Cliente) y **547 UDP** (Servidor).
- **Proceso de Concesión DORA**:
  1. **Discover**: Cliente envía broadcast (`255.255.255.255`, puerto 67) buscando servidores DHCP.
  2. **Offer**: Servidor responde con unicast/broadcast ofreciendo IP, máscara, gateway, DNS y tiempo de concesión (*lease time*).
  3. **Request**: Cliente solicita formalmente la IP ofrecida.
  4. **Acknowledge (ACK)**: Servidor confirma la concesión y el cliente activa la configuración.
- **Tiempos de Renovación**:
  - **T1 (0.5 * Lease Time)**: Cliente intenta renovar con el mismo servidor vía Unicast (`DHCPREQUEST`).
  - **T2 (0.875 * Lease Time)**: Si no hay respuesta, cliente envía Broadcast a cualquier servidor DHCP disponible.
- **DHCP Relay Agent (RFC 3046 / Opción 82)**: Permite a routers reenviar peticiones DHCP broadcast de clientes de subredes locales a un servidor DHCP centralizado en otra subred.

#### 3.2 Protocolo DNS (Domain Name System)
- Definido en **RFC 1034** y **RFC 1035**.
- Puerto estándar: **53 TCP y UDP** (UDP para consultas estándar de hasta 512 bytes / EDNS0; TCP para transferencias de zona AXFR/IXFR y respuestas mayores a 512 bytes).
- **Espacio de Nombres Jerárquico**:
  - Nodo raíz (`.` gestionado por los 13 servidores raíz lógicos `a.root-servers.net` a `m.root-servers.net`).
  - **TLD (Top-Level Domain)**: gTLD (`.com`, `.org`, `.gob`), ccTLD (`.es`, `.fr`).
  - Dominios de segundo nivel y subdominios.
- **Tipos de Registros DNS Críticos**:
  - `A` (IPv4, 32 bits), `AAAA` (IPv6, 128 bits), `CNAME` (Alias canónico).
  - `MX` (Mail Exchanger con prioridad), `NS` (Servidor de nombres autoritativo).
  - `PTR` (Puntero de resolución inversa bajo `in-addr.arpa` o `ip6.arpa`).
  - `SOA` (Start of Authority: número de serie, refresh, retry, expire, TTL mínimo).
  - `TXT` (Texto arbitrario, usado por SPF, DKIM, DMARC), `SRV` (Localización de servicios en AD).
- **Consultas**: Recursivas (el servidor DNS resuelve hasta el final y devuelve el resultado) vs. Iterativas (el servidor devuelve la mejor referencia que conoce).

### 4. Gestión de Dispositivos y Almacenamiento en Clientes/Servidores
- **Windows**: Consola de Administración de discos (`diskmgmt.msc`), comando `diskpart`. Tablas MBR (máx 2 TB, 4 particiones primarias) vs. GPT (hasta 128 particiones, soporte >2 TB con UEFI).
- **Linux**: Herramientas `fdisk`, `gdisk` (para GPT), `parted`, `mkfs.ext4`, `mkfs.xfs`, montaje en `/etc/fstab`, y gestión de volúmenes lógicos con **LVM** (PV: Physical Volumes, VG: Volume Groups, LV: Logical Volumes).

---

## 🎯 Datos Clave para Oposiciones TAI

| Servicio / Parámetro | Valor Técnico |
|----------------------|---------------|
| Puertos DHCPv4 | **67 UDP** (Server), **68 UDP** (Client) |
| Puertos DHCPv6 | **547 UDP** (Server), **546 UDP** (Client) |
| Fases DHCP | **DORA** (Discover, Offer, Request, Acknowledge) |
| Tiempos renovación DHCP | **T1 = 50%** del lease time (unicast); **T2 = 87.5%** (broadcast) |
| Puerto DNS | **53 TCP/UDP** |
| Longitud Dirección MAC | **48 bits (6 bytes)**; 24 bits OUI + 24 bits NIC |
| Servidores Raíz DNS | **13 nombres lógicos** (`A` hasta `M`), operados con Anycast |
| Límite MBR vs GPT | MBR máx **2 TB** y 4 particiones primarias; GPT sin límite práctico (requiere UEFI) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/dhcp-protocol|Protocolo DHCP y Concesiones DORA]]
- [[wiki/entities/dns-protocol|Protocolo DNS y Resolución de Nombres]]
- [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet y Direcciones MAC]]
- [[wiki/entities/firewalls-and-vpn|Cortafuegos, DMZ y Redes Privadas Virtuales]]

### Conceptos Teóricos:
- [[wiki/concepts/routing-and-switching-mechanisms|Mecanismos de Conmutación y Enrutamiento LAN]]
- [[wiki/concepts/lan-topologies-and-mac-protocols|Topologías LAN y Protocolos de Acceso al Medio]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]
- [[wiki/synthesis/bloque4-tai-oposiciones-master-guide|Guía Maestra de Bloque 4: Sistemas y Comunicaciones (TAI)]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema04|Nota Fuente del Tema 04]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema04-redes-lan-dhcp-dns|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]
