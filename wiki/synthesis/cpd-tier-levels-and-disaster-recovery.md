---
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
