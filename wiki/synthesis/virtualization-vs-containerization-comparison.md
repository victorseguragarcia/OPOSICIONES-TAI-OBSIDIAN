---
title: "Comparativa de Arquitecturas: Máquinas Virtuales vs Contenedores"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - virtualization
  - containers
  - docker
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "VMs vs Contenedores"
  - "Virtualización vs Contenedores"
---

# Comparativa de Arquitecturas: Máquinas Virtuales vs Contenedores

Evaluación de trade-offs entre aislamiento a nivel de hardware (Virtualización tradicional) y aislamiento a nivel de sistema operativo (Contenedores).

## Matriz de Arquitectura

| Parámetro | [[wiki/concepts/virtualization-and-cloud-computing\|Máquinas Virtuales (VMs)]] | [[wiki/entities/docker-and-containers\|Contenedores (Docker)]] |
| :--- | :--- | :--- |
| **Capa de Aislamiento** | Aislamiento completo de hardware mediante hipervisor | Aislamiento de procesos mediante namespaces y cgroups en el kernel anfitrión |
| **Sistema Operativo Invitado** | Cada VM ejecuta su propio SO completo (Guest OS) | Comparten el mismo kernel del SO anfitrión |
| **Tiempo de Arranque** | Minutos / decenas de segundos | Milisegundos / pocos segundos |
| **Consumo de Recursos** | Alto (requiere asignar RAM, vCPU y almacenamiento dedicado) | Mínimo (comparte memoria y binarios base con Copy-on-Write) |
| **Rendimiento I/O** | Ligera penalización por emulación/paravirtualización | Rendimiento cercano al nativo (*Near-Bare-Metal*) |
| **Orquestación Típica** | VMware vSphere, OpenStack, Proxmox | [[wiki/entities/kubernetes\|Kubernetes (K8s)]], Docker Swarm |

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]] y [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidades: [[wiki/entities/docker-and-containers|Docker]], [[wiki/entities/kubernetes|Kubernetes]]

