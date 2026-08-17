---
title: "Sistemas SIEM, IDS e IPS de Monitorización y Seguridad"
type: "entity"
tags:
  - siem
  - ids
  - ips
  - soc
  - cybersecurity
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SIEM"
  - "IDS/IPS"
---

# Sistemas SIEM, IDS e IPS de Monitorización y Seguridad

Los sistemas de detección y prevención de intrusiones (**IDS/IPS**) y los sistemas de gestión de eventos de seguridad (**SIEM**) forman el núcleo de las operaciones de defensa y respuesta en Centros de Operaciones de Seguridad (SOC).

---

## 🏛️ Diferencias Clave: IDS vs IPS vs SIEM

| Sistema | Modo de Operación | Ubicación en Red | Acción ante Incidentes | Ejemplos Líderes |
|---------|-------------------|------------------|------------------------|------------------|
| **IDS** (Detection) | Pasivo / Fuera de banda | Puerto SPAN / TAP / Espejo | Genera alarmas, registra logs | Snort, Suricata, Zeek |
| **IPS** (Prevention) | Activo / En línea (*In-Line*) | Entre interfaces de red / NGFW | **Bloquea activamente** tráfico malicioso | Snort IPS, Cisco Firepower |
| **SIEM** (Event Mgmt) | Correlación global | Servidor centralizado | Recopila logs, correlaciona eventos en tiempo real | Splunk, Elastic SIEM, Wazuh, Sentinel |

---

## 🧩 Métodos de Detección en IDS/IPS

- **Basado en Firmas (Pattern Matching)**: Compara patrones de bytes y cabeceras contra bases de datos de vulnerabilidades conocidas (CVE). Rápido y preciso, pero vulnerable a ataques de día cero (*0-Day*).
- **Basado en Anomalías / Comportamiento**: Establece una línea base de tráfico legítimo y dispara alertas ante desviaciones estadísticas significativas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| NIDS vs HIDS | NIDS monitoriza subredes; HIDS monitoriza archivos y llamadas al sistema del host |
| Funciones Clave SIEM | Agregación, Normalización, Correlación en tiempo real y Alertas |
| Herramienta HIDS Open Source | **Wazuh** / **OSSEC** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/ccn-cert-and-ens|CCN-CERT y ENS]]
