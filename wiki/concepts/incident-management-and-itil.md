---
title: "Gestión de Incidencias y Marco ITIL en Servicios TI"
type: "concept"
tags:
  - itil
  - incident-management
  - service-desk
  - sla
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Gestión de Incidencias e ITIL"
  - "ITIL Incident Management"
---

# Gestión de Incidencias y Marco ITIL en Servicios TI

El marco **ITIL (Information Technology Infrastructure Library)** proporciona un conjunto de mejores prácticas para la gestión y entrega eficiente de servicios de tecnologías de la información.

---

## 🏛️ Gestión de Incidencias frente a Gestión de Problemas

- **Incidencia**: Cualquier interrupción no planificada o reducción en la calidad de un servicio de TI. Su objetivo prioritario es **restaurar el servicio lo más rápido posible** (mediante parches, reinicios o soluciones temporales / *Workarounds*).
- **Problema**: Causa subyacente desconocida de una o múltiples incidencias. Su objetivo es **identificar la causa raíz** y proporcionar una solución definitiva.

---

## 🧩 Service Desk y Ciclo de Vida de una Incidencia

- **Service Desk (Centro de Servicios)**: Actúa como el **Único Punto de Contacto (SPOC - Single Point of Contact)** entre los usuarios finales y el departamento de TI.
- **Fases del Ciclo de Vida de Incidencias**:
  1. *Registro*: Creación formal del ticket.
  2. *Categorización*: Clasificación temática del fallo.
  3. *Priorización*: Determinada por la fórmula $\text{Prioridad} = \text{Impacto} \times \text{Urgencia}$.
  4. *Diagnóstico Inicial*: Soporte de Nivel 1.
  5. *Escalado*: Funcional (a Nivel 2/3 especialistas) o Jerárquico.
  6. *Resolución y Recuperación*: Aplicación de solución o workaround.
  7. *Cierre*: Verificación formal con el usuario y registro en la base de conocimiento de errores conocidos (**KEDB**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Término ITIL | Definición |
|--------------|------------|
| **SPOC** | Single Point of Contact (**Service Desk**) |
| **SLA** | Service Level Agreement (Acuerdo de Nivel de Servicio con el cliente) |
| **OLA** | Operational Level Agreement (Acuerdo interno entre equipos de TI) |
| **KEDB** | Known Error Database (Base de datos de errores conocidos) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
