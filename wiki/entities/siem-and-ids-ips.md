---
title: "Sistemas SIEM, IDS e IPS de Ciberseguridad"
type: "entity"
tags:
  - security
  - siem
  - ids
  - ips
  - soc
  - incident-management
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SIEM"
  - "IDS"
  - "IPS"
  - "SOC Tools"
---

# Sistemas SIEM, IDS e IPS de Ciberseguridad

Sistemas de detección, prevención y correlación de eventos de seguridad fundamentales en centros de operaciones de seguridad (SOC).

## Tecnologías Principales
- **IDS (Intrusion Detection System)**: Analiza tráfico pasivamente mediante copia en puerto SPAN/Mirroring y genera alertas ante patrones maliciosos conocidos (firmas) o anomalías de comportamiento.
- **IPS (Intrusion Prevention System)**: Dispositivo en línea (*in-line*) capaz de bloquear paquetes y cortar flujos de ataque en tiempo real (ej: Snort, Suricata).
- **SIEM (Security Information and Event Management)**: Agrega, normaliza y correlaciona registros (logs) procedentes de cortafuegos, servidores, routers y aplicaciones (ej: Splunk, Elastic SIEM, Wazuh, QRadar).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Perímetro: [[wiki/entities/firewalls-and-vpn|Cortafuegos y Redes Privadas Virtuales (VPN)]]
- Normativa: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y Esquema Nacional de Seguridad (ENS)]]

