---
title: "Virtualización, Hipervisores y Modelos Cloud Computing"
type: "concept"
tags:
  - virtualization
  - hypervisors
  - cloud-computing
  - iaas
  - paas
  - saas
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Virtualización y Cloud"
  - "Virtualization and Cloud"
---

# Virtualización, Hipervisores y Modelos Cloud Computing

La **virtualización** abstrae el hardware físico para crear entornos lógicos independientes, constituyendo el habilitador tecnológico esencial de la **computación en la nube (Cloud Computing)**.

---

## 🏛️ Clasificación de Hipervisores (VMM)

- **Hipervisores Tipo 1 (Bare-Metal / Nativos)**:
  - Se instalan y ejecutan directamente sobre el hardware físico del servidor sin sistema operativo intermedio.
  - Ofrecen máximo rendimiento, menor latencia y mayor seguridad.
  - Ejemplos líderes: **VMware ESXi**, **Microsoft Hyper-V**, **KVM (Kernel-based Virtual Machine)**, **Xen**.
- **Hipervisores Tipo 2 (Hosted / Alojados)**:
  - Se ejecutan como una aplicación sobre un sistema operativo anfitrión (*Host OS*).
  - Utilizados principalmente para desarrollo, pruebas y puestos de trabajo locales.
  - Ejemplos: **Oracle VirtualBox**, **VMware Workstation / Fusion**, **QEMU**.

---

## 🧩 Modelos de Servicio y Despliegue en Cloud (NIST SP 800-145)

| Modelo de Servicio | Descripción | Qué Gestiona el Proveedor | Qué Gestiona el Cliente | Ejemplos |
|-------------------|-------------|---------------------------|-------------------------|----------|
| **IaaS** | Infraestructura como Servicio | Hardware, Red, Almacenamiento, Hipervisor | **SO, Middleware, Runtime, Datos, Aplicación** | AWS EC2, Azure VMs, Google Compute Engine |
| **PaaS** | Plataforma como Servicio | Hardware, Hipervisor, SO, Middleware, Runtime | **Datos y Código de la Aplicación** | AWS Elastic Beanstalk, Heroku, Azure App Service |
| **SaaS** | Software como Servicio | **Toda la pila completa** de infraestructura y software | Únicamente configuración de usuario | Microsoft 365, Google Workspace, Salesforce |
| **FaaS** | Serverless / Funciones | Pila completa y escalado de micro-instancias | **Solo el código de la función invocada** | AWS Lambda, Azure Functions, Cloud Functions |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar Definición Cloud | **NIST SP 800-145** |
| Extensiones CPU Virtualización | **Intel VT-x** / **AMD-V** |
| Funcionalidad Migración en Caliente | **vMotion** (VMware) / **Live Migration** (Hyper-V/KVM) |
| Balanceo Dinámico de Carga | **DRS** (Distributed Resource Scheduler) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
