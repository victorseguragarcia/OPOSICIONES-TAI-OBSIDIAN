---
title: "Virtualización y Computación en la Nube (Cloud Computing)"
type: "concept"
tags:
  - virtualization
  - cloud
  - iaas
  - paas
  - saas
  - hypervisors
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Virtualización"
  - "Cloud Computing"
  - "IaaS PaaS SaaS"
---

# Virtualización y Computación en la Nube (Cloud Computing)

Tecnologías de abstracción de hardware y provisión elástica de servicios bajo demanda según el estándar NIST SP 800-145.

## Tipologías de Hipervisores
- **Hipervisores Tipo 1 (Bare-Metal)**: Se ejecutan directamente sobre el hardware físico (ej: VMware ESXi, KVM, Microsoft Hyper-V, Xen). Máximo rendimiento y uso en CPD.
- **Hipervisores Tipo 2 (Hosted)**: Se ejecutan como una aplicación sobre un sistema operativo anfitrión (ej: VMware Workstation, VirtualBox).

## Modelos de Servicio Cloud
- **IaaS (Infrastructure as a Service)**: Provisión de cómputo, almacenamiento y redes virtuales (ej: AWS EC2, Azure VMs).
- **PaaS (Platform as a Service)**: Entorno de ejecución y base de datos sin gestión de infraestructura subyacente (ej: AWS Elastic Beanstalk, Heroku, Azure App Services).
- **SaaS (Software as a Service)**: Aplicaciones completas listas para el usuario final (ej: Microsoft 365, Google Workspace).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Comparativa: [[wiki/synthesis/virtualization-vs-containerization-comparison|Virtualización vs Contenedores]]
- Contenedores: [[wiki/entities/docker-and-containers|Docker y Contenedores]]

