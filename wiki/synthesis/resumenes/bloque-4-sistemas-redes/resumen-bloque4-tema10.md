---
title: "Resumen Exhaustivo Tema 10 (Bloque 4): Seguridad Perimetral, Firewall IPTables, IDS/IPS y VPN"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-10
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema10.md]]"
  - "[[wiki/sources/bloque4-tema10]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|⬅️ Tema 09]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏁 Fin de Bloque 4 ➡️]]

# 🔴 Resumen Exhaustivo Tema 10 (Bloque 4): Seguridad Perimetral, Firewall IPTables, IDS/IPS y VPN

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 10**
> Arquitectura de seguridad perimetral, zonas de red (LAN, DMZ, WAN), cortafuegos de filtrado de paquetes, stateful y de nueva generación (NGFW), cortafuegos Linux IPTables (tablas filter/nat/mangle, cadenas y políticas por defecto), sistemas de detección y prevención de intrusos (IDS vs IPS, basados en firmas y anomalías) y redes privadas virtuales VPN (IPsec con modos Transporte/Túnel y protocolos AH/ESP, SSL/TLS VPNs OpenVPN y WireGuard).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Seguridad Perimetral, Zonas de Red y Cortafuegos
- **Zonas de Seguridad**:
  - *LAN (Red Interna / Confiable)*: Servidores de bases de datos, puestos de trabajo de usuarios internos.
  - *DMZ (Zona Desmilitarizada / Semiconfiable)*: Aloja servidores accesibles desde Internet (Servidor Web, Servidor de Correo, Servidor DNS público). Regla de oro: **El tráfico desde Internet puede entrar a la DMZ, pero la DMZ NUNCA puede iniciar conexiones hacia la LAN interna**.
  - *WAN (Internet / No Confiable)*: Red pública externa.
- **Tipos de Cortafuegos (Firewalls)**:
  - *Filtrado de Paquetes Sin Estado (Stateless)*: Analiza cabeceras IP y puertos de forma aislada (rápido pero vulnerable a spoofing).
  - *Inspección de Estado (Stateful Inspection)*: Rastrea el estado de las conexiones TCP/UDP (mantiene la tabla de estado de conexiones `ESTABLISHED, RELATED`).
  - *Firewalls de Aplicación / Próximos (Proxy Firewall / WAF)*: Inspeccionan el payload de nivel 7 (HTTP, SQL injection, XSS).
  - *NGFW (Next-Generation Firewall)*: Combina stateful, DPI (Deep Packet Inspection), IPS integrado, control de aplicaciones y descifrado TLS.

### 2. Cortafuegos Linux IPTables / Netfilter
- **Arquitectura de IPTables (Tablas y Cadenas)**:
  - **Tabla `filter` (por defecto)**: Filtrado de paquetes. Cadenas:
    - `INPUT`: Paquetes destinados a la propia máquina local.
    - `OUTPUT`: Paquetes generados por la máquina local hacia el exterior.
    - `FORWARD`: Paquetes enrutados a través de la máquina hacia otra red.
  - **Tabla `nat`**: Traducción de direcciones de red. Cadenas:
    - `PREROUTING`: Modifica paquetes antes de la decisión de enrutamiento (DNAT / Port Forwarding hacia servidores en DMZ).
    - `POSTROUTING`: Modifica paquetes tras el enrutamiento (SNAT / Masquerade para dar salida a Internet a la LAN).
    - `OUTPUT`: Paquetes NAT generados localmente.
  - **Tabla `mangle`**: Modificación de campos de cabecera (TTL, TOS, marcas de QoS).
- **Acciones / Objetivos (Targets con `-j`)**:
  - `ACCEPT`: Permite el paso del paquete.
  - `DROP`: Descarta el paquete silenciosamente (sin enviar respuesta).
  - `REJECT`: Descarta el paquete enviando un mensaje ICMP de error (puerto/host inalcanzable).
  - `MASQUERADE`: Aplica SNAT dinámico utilizando la IP pública de la interfaz de salida.

### 3. Sistemas de Detección y Prevención de Intrusos (IDS / IPS)
- **IDS (Intrusion Detection System)**: Funciona en modo **pasivo / promiscuo** recibiendo una copia del tráfico mediante un puerto espejo (*Port Mirroring / SPAN*). Detecta intrusiones y genera alertas/logs sin bloquear el tráfico en línea (ej. Snort en modo sniffer, Zeek).
- **IPS (Intrusion Prevention System)**: Funciona en modo **activo / en línea (In-line)** interceptando todo el tráfico en tiempo real. Puede bloquear, descartar paquetes y reconfigurar el firewall al instante ante un ataque detectado (ej. Suricata, Snort en modo IPS).
- **Técnicas de Detección**:
  - *Basada en Firmas / Patrones*: Compara el tráfico con bases de datos de firmas conocidas (alta precisión para amenazas conocidas, ciega ante ataques Zero-Day).
  - *Basada en Anomalías / Comportamiento*: Establece una línea base de tráfico normal y detecta desviaciones estadísticas (capaz de detectar Zero-Days, mayor tasa de falsos positivos).

### 4. Redes Privadas Virtuales (VPN) y Protocolo IPsec
- **Protocolo IPsec (Internet Protocol Security - Nivel 3 de Red)**:
  - *Protocolos de Seguridad*:
    - **AH (Authentication Header - Protocolo IP 51)**: Proporciona **Autenticidad e Integridad**, pero ❌ **NO proporciona Confidencialidad** (no cifra los datos). Protege la cabecera IP exterior (incompatible con NAT).
    - **ESP (Encapsulating Security Payload - Protocolo IP 50)**: Proporciona **Confidencialidad (Cifrado), Autenticidad e Integridad**.
  - *Modos de Funcionamiento de IPsec*:
    - **Modo Transporte**: Solo cifra/autentica la carga útil (Payload) del paquete original. Conserva la cabecera IP original (usado en comunicación extremo a extremo Host-to-Host).
    - **Modo Túnel**: Cifra el **paquete IP completo original** (cabecera + datos) y añade una **nueva cabecera IP exterior** (estándar para VPNs Gateway-to-Gateway / Site-to-Site y Remote Access).
  - *IKE (Internet Key Exchange - UDP 500 / 4500)*: Negocia las Asociaciones de Seguridad (SA) y el intercambio de claves Diffie-Hellman.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 10 (Bloque 4)**
> 1. **Protocolo AH de IPsec**: **NO CIFRA LOS DATOS** (solo autentica y garantiza integridad). Para cifrar se debe usar **ESP**.
> 2. **Modo Túnel vs Modo Transporte**: En el *Modo Túnel* se crea una **nueva cabecera IP externa** que oculta los extremos reales; en *Modo Transporte* la cabecera IP original no se oculta.
> 3. **DROP vs REJECT en IPTables**: `DROP` tira el paquete en silencio; `REJECT` devuelve un paquete ICMP de rechazo al emisor.
> 4. **Cadenas de la tabla NAT**: `PREROUTING` se usa para **DNAT (Destination NAT)**; `POSTROUTING` se usa para **SNAT (Source NAT / Masquerade)**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **IPsec**: **AH $=$ Autenticidad sin cifrado / ESP $=$ Cifrado total**.
> - **IPTables NAT**: **PREROUTING $\rightarrow$ DNAT / POSTROUTING $\rightarrow$ SNAT (Masquerade)**.
> - **Zonas de Red**: **Internet $\rightarrow$ DMZ (SÍ) / DMZ $\rightarrow$ LAN (NUNCA)**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema10|Fuente Oficial del Tema 10]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema10|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema10-topologias-ieee802-wifi|Test Tema 10]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema09|⬅️ Tema 09]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏁 Fin de Bloque 4 ➡️]]
