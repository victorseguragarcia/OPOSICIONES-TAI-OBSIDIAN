---
title: "Infraestructura de CPD y Recuperación ante Desastres"
type: "concept"
tags:
  - datacenter
  - cpd
  - disaster-recovery
  - bcp
  - drp
  - raid
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Infraestructura CPD"
  - "Disaster Recovery"
  - "Alta Disponibilidad"
---

# Infraestructura de CPD y Recuperación ante Desastres

Diseño de Centros de Proceso de Datos (CPD), continuidad de negocio y arquitecturas de almacenamiento de alta disponibilidad.

## Clasificación TIER (Uptime Institute)
- **TIER I (Básico)**: 99.671% disponibilidad (~28.8h caída/año). Sin componentes redundantes.
- **TIER II (Redundancia Parcial)**: 99.741% disponibilidad. Componentes redundantes N+1.
- **TIER III (Mantenimiento Concurrente)**: 99.982% disponibilidad (~1.6h caída/año). Rutas de distribución redundantes, equipos mantenibles sin interrumpir servicio.
- **TIER IV (Tolerante a Fallos)**: 99.995% disponibilidad (~26 min caída/año). Sistemas 2(N+1) con tolerancia total a cualquier fallo simple.

## Métricas de Continuidad
- **RTO (Recovery Time Objective)**: Tiempo máximo admisible para restaurar los servicios tras un incidente.
- **RPO (Recovery Point Objective)**: Volumen máximo de pérdida de datos admisible medido en tiempo.

## Arquitecturas RAID
- **RAID 0**: Fraccionamiento (*striping*) sin redundancia.
- **RAID 1**: Espejo (*mirroring*).
- **RAID 5**: Fraccionamiento con paridad distribuida (requiere $\ge 3$ discos, tolera 1 fallo).
- **RAID 6**: Doble paridad distribuida (requiere $\ge 4$ discos, tolera 2 fallos simultáneos).
- **RAID 10**: Combinación de espejo y fraccionamiento (RAID 1+0).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Seguridad: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM e IDS/IPS]]

