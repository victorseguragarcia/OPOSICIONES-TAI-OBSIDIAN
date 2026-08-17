---
title: "Guía Completa de Contenedores y Kubernetes para Oposiciones TAI"
type: "synthesis"
tags:
  - synthesis
  - docker
  - kubernetes
  - containers
  - devops
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Docker y Kubernetes"
  - "K8s and Docker Guide"
---

# Guía Completa de Contenedores y Kubernetes para Oposiciones TAI

Compendio exhaustivo sobre la arquitectura de contenedores Docker, primitivas del kernel Linux y orquestación con Kubernetes (K8s).

---

## 🏛️ Docker: Primitivas del Kernel Linux

1. **Namespaces (Aislamiento de Recursos)**:
   - `pid`: Aísla el árbol de procesos (proceso en contenedor es PID 1).
   - `net`: Proporciona interfaz de red virtual (`eth0`), tabla de rutas y puertos propios.
   - `mnt`: Puntos de montaje del sistema de archivos independientes.
   - `ipc`: Memoria compartida y colas de mensajes POSIX.
   - `uts`: Hostname y domain name.
   - `user`: Mapeo de UIDs/GIDs locales a UIDs del host anfitrión.
2. **Control Groups (cgroups)**:
   - Medición y límites de consumo de hardware: CPU (`cpu.cfs_quota_us`), Memoria (`memory.max`), I/O de disco.
3. **Almacenamiento por Capas (Overlay2)**:
   - Imágenes inmutables compuestas por capas de solo lectura (*LowerDir*) + capa superior de lectura/escritura efímera (*UpperDir*), unificadas mediante el punto de montaje (*MergedDir*).

---

## 🧩 Kubernetes: Arquitectura y Tipos de Servicios

- **Arquitectura Master/Worker**:
  - **Master (Control Plane)**: `kube-apiserver`, `etcd` (almacén de estado Raft en puertos 2379/2380), `kube-scheduler`, `kube-controller-manager`.
  - **Worker**: `kubelet`, `kube-proxy`, Container Runtime (`containerd`).
- **Tipos de Services de Kubernetes**:
  - **`ClusterIP`**: Asigna una IP virtual interna alcanzable solo dentro del clúster (por defecto).
  - **`NodePort`**: Abre un puerto estático en cada nodo del clúster en el rango **30000 a 32767 TCP**, reenviando al ClusterIP.
  - **`LoadBalancer`**: Aprovisiona automáticamente un balanceador de carga externo en la infraestructura cloud subyacente.
  - **`ExternalName`**: Mapea el servicio a un registro CNAME DNS externo sin proxy de tráfico.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Detalle Técnico |
|-----------|-----------------|
| Base de Datos Distribuida K8s | **etcd** (Consenso Raft, puertos **2379/2380 TCP**) |
| Rango Puertos NodePort | **30000 - 32767** |
| Unidad Mínima K8s | **Pod** |
| Multi-Stage Build Docker | Reduce radicalmente el tamaño de las imágenes finales eliminando compiladores |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: VMs vs Contenedores]]
