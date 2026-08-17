---
title: "Comparativa Arquitectónica: Máquinas Virtuales vs Contenedores"
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
  - "VM vs Containers"
  - "Virtualización vs Contenedores"
---

# Comparativa Arquitectónica: Máquinas Virtuales vs Contenedores

Análisis comparativo entre la virtualización basada en hipervisores (máquinas virtuales completas) y la virtualización ligera a nivel de sistema operativo (contenedores).

---

## 🏛️ Matriz de Comparación Arquitectónica

| Característica | Máquinas Virtuales (VMs) | Contenedores (Docker / OCI) |
|----------------|--------------------------|-----------------------------|
| **Nivel de Abstracción** | **Hardware completo** (CPU, RAM, Disco, BIOS) | **Sistema Operativo (Espacio de Usuario)** |
| **Capa de Virtualización** | **Hipervisor** (ESXi, Hyper-V, KVM) | **Motor de Contenedores** (Docker, containerd) |
| **Sistema Operativo Invitado** | Requiere un **Guest OS completo e independiente** | **Comparte el Kernel del SO Anfitrión (Host)** |
| **Tiempo de Arranque** | Minutos (arranque de SO completo) | **Milisegundos a Segundos** |
| **Consumo de Recursos** | Alto (Gigabytes de RAM/disco por VM) | Muy bajo (Megabytes de memoria por contenedor) |
| **Densidad de Despliegue** | Decenas de VMs por host físico | Cientos o miles de contenedores por host |
| **Aislamiento y Seguridad** | **Muy alto** (Aislamiento por hardware/anillos) | Alto (Basado en **Namespaces** y **cgroups**) |
| **Portabilidad** | Dependiente del formato de disco virtual (VMDK/VHDX) | **Total** mediante imágenes estándar OCI |
| **Orquestación Típica** | VMware vSphere, OpenStack, Proxmox | **Kubernetes (K8s)**, Docker Swarm |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Concepto: [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Cloud]]
