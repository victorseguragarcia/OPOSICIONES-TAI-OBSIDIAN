---
title: "Kubernetes y Orquestación de Contenedores"
type: "entity"
tags:
  - kubernetes
  - k8s
  - containers
  - orchestration
  - cloud
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "K8s"
  - "Kubernetes Engine"
---

# Kubernetes y Orquestación de Contenedores

**Kubernetes (K8s)** es un orquestador open-source para la automatización del despliegue, escalado, balanceo de carga y gestión de aplicaciones en contenedores.

## Arquitectura de Clúster
- **Control Plane**: `kube-apiserver`, `etcd` (almacén de estado), `kube-scheduler`, `kube-controller-manager`.
- **Nodos de Trabajo (Worker Nodes)**: `kubelet`, `kube-proxy`, Container Runtime (CRI como containerd/CRI-O).

## Objetos Primarios
- **Pod**: Unidad atómica mínima de despliegue que agrupa uno o más contenedores compartiendo red y almacenamiento.
- **Deployment / ReplicaSet**: Gestión declarativa de réplicas y actualizaciones sin parada (Rolling Updates).
- **Service**: Abstracción para exponer pods con IP estable y balanceo de carga (ClusterIP, NodePort, LoadBalancer).
- **Ingress**: Controlador de acceso HTTP/HTTPS perimetral.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Contenedores: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Arquitectura: [[wiki/concepts/microservices-and-middleware|Microservicios y Middleware]]

