---
title: "Marco ITIL y Gestión del Service Desk"
type: "entity"
tags:
  - itil
  - itsm
  - service-desk
  - sla
  - incidents
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ITIL"
  - "Service Desk"
  - "Gestión de Servicios TI"
---

# Marco ITIL y Gestión del Service Desk

**ITIL (Information Technology Infrastructure Library)** es el marco de referencia de buenas prácticas más extendido a nivel mundial para la Gestión de Servicios de Tecnologías de la Información (**ITSM**).

---

## 🏛️ Estructura de ITIL

### 1. ITIL v3: Las 5 Fases del Ciclo de Vida del Servicio
1. **Estrategia del Servicio (*Service Strategy*)**: Define qué servicios ofrecer y a qué clientes para generar valor.
2. **Diseño del Servicio (*Service Design*)**: Diseña servicios nuevos o modificados (SLA, capacidad, disponibilidad, continuidad de servicios TI, seguridad).
3. **Transición del Servicio (*Service Transition*)**: Construcción, pruebas y despliegue de cambios en producción (Gestión de Cambios, Gestión de Versiones y Despliegues, CMDB).
4. **Operación del Servicio (*Service Operation*)**: Operación diaria y soporte (Gestión de Incidencias, Gestión de Problemas, Gestión de Peticiones, Service Desk).
5. **Mejora Continua del Servicio (*CSI - Continual Service Improvement*)**: Ciclo de Deming (**PDCA**: Plan-Do-Check-Act) para optimizar la eficiencia y calidad.

### 2. ITIL 4: Sistema de Valor del Servicio (SVS)
- Evoluciona el ciclo de vida lineal hacia una red flexible de valor basada en **7 Principios Guía**: *Enfocarse en el valor, Empezar donde esté, Progresar iterativamente con retroalimentación, Colaborar y promover visibilidad, Pensar y trabajar holísticamente, Mantenerlo simple y práctico, Optimizar y automatizar*.

---

## 🧩 El Service Desk como Función Central

- **Concepto SPOC (Single Point of Contact)**: Único punto de contacto entre los usuarios y TI.
- **Tipos de Acuerdos de Servicio**:
  - **SLA (Service Level Agreement)**: Acuerdo formal entre el proveedor de servicios de TI y el **Cliente externo o de negocio** sobre niveles de servicio (disponibilidad, tiempo de respuesta y resolución).
  - **OLA (Operational Level Agreement)**: Acuerdo interno entre distintos departamentos de TI de la misma organización (ej. equipo de redes con equipo de BBDD).
  - **UC (Underpinning Contract)**: Contrato legal vinculante con un proveedor externo de soporte (ej. soporte de hardware de servidores).

---

## 🎯 Datos Clave para Oposiciones TAI

| Término | Definición / Fórmula |
|---------|----------------------|
| **Incidencia vs Problema** | Incidencia restaura servicio rápido; Problema busca la **causa raíz** |
| **Cálculo de Prioridad** | $	ext{Prioridad} = 	ext{Impacto} 	imes 	ext{Urgencia}$ |
| **KEDB** | *Known Error Database* (Base de datos de errores conocidos y workarounds) |
| **CMDB** | *Configuration Management Database* (Almacena los Elementos de Configuración o CIs) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema05|Resumen Bloque 4 - Tema 05]]
- Concepto: [[wiki/concepts/incident-management-and-itil|Gestión de Incidencias e ITIL]]
