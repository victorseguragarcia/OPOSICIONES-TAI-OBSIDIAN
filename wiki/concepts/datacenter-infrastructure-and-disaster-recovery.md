---
title: "Infraestructura de Centros de Proceso de Datos (CPD) y Recuperación ante Desastres"
type: "concept"
tags:
  - cpd
  - datacenter
  - tia-942
  - disaster-recovery
  - rto-rpo
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Infraestructura de CPD"
  - "Datacenter Architecture"
---

# Infraestructura de Centros de Proceso de Datos (CPD) y Recuperación ante Desastres

El diseño físico de un **Centro de Proceso de Datos (CPD)** y la planificación de la continuidad de negocio garantizan la operación ininterrumpida de los servicios de TI frente a contingencias.

---

## 🏛️ Clasificación TIER de CPDs (Estándar ANSI/TIA-942)

| Nivel TIER | Nombre / Descripción | Disponibilidad Anual | Inactividad Máxima Anual | Redundancia Componentes | Rutas de Distribución |
|------------|----------------------|----------------------|--------------------------|-------------------------|-----------------------|
| **TIER I** | Básico | **99.671%** | **28.8 horas/año** | $N$ (Sin redundancia) | 1 ruta única |
| **TIER II** | Componentes Redundantes | **99.741%** | **22.0 horas/año** | $N + 1$ | 1 ruta única |
| **TIER III** | Mantenimiento Concurrente | **99.982%** | **1.6 horas/año** | $N + 1$ (Mantenible sin parar) | 1 activa + 1 pasiva (2 rutas) |
| **TIER IV** | Tolerante a Fallos | **99.995%** | **26.3 minutos/año** | $2(N + 1)$ o $2N + 1$ | **2 rutas activas simultáneas** |

---

## 🧩 Métricas de Continuidad y Sitios de Respaldo

- **RPO (Recovery Point Objective)**: Volumen máximo de datos perdidos tolerables medido en tiempo transcurrido desde el último punto de respaldo.
- **RTO (Recovery Time Objective)**: Tiempo máximo admisible para restaurar la operatividad de los sistemas tras una interrupción.
- **Tipos de Sedes Secundarias (Recovery Sites)**:
  - **Hot Site (Sitio Caliente)**: Réplica exacta totalmente equipada y sincronizada en tiempo real. RTO/RPO cercanos a cero.
  - **Warm Site (Sitio Templado)**: Equipamiento informático preinstalado pero datos no sincronizados en tiempo real (requiere restaurar último backup). RTO de horas a días.
  - **Cold Site (Sitio Frío)**: Espacio físico acondicionado con energía y climatización pero sin hardware ni datos informáticos. RTO de semanas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Estándar |
|-----------|----------------|
| Norma de Clasificación CPDs | **ANSI/TIA-942** |
| Disponibilidad TIER IV | **99.995%** (26.3 min caída/año) |
| Temperatura Óptima CPD (ASHRAE) | **18 °C a 27 °C** |
| Humedad Relativa Óptima | **40% a 60%** |
| Gases de Extinción Limpios | **Novec 1230**, **FM-200**, **Inergen** (no destructivos) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Entidad: [[wiki/entities/raid-storage|Sistemas de Almacenamiento RAID, DAS, NAS y SAN]]
- Síntesis: [[wiki/synthesis/cpd-tier-levels-and-disaster-recovery|Guía de Niveles TIER de CPD, RAID y Planes de Continuidad]]
