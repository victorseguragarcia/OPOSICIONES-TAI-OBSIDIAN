---
title: "Kubernetes y Orquestación de Contenedores"
type: "entity"
tags:
  - kubernetes
  - k8s
  - orchestration
  - cloud-native
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Kubernetes"
  - "K8s"
---

# Kubernetes y Orquestación de Contenedores

**Kubernetes (K8s)** es una plataforma de orquestación de código abierto desarrollada originalmente por Google (proyecto Borg) y donada a la **CNCF (Cloud Native Computing Foundation)** para automatizar el despliegue, escalado y gestión de aplicaciones en contenedores.

---

## 🏛️ Arquitectura del Clúster K8s

### 1. Control Plane (Nodos Master)
- **`kube-apiserver`**: Punto central de entrada de la API REST de Kubernetes; valida y procesa peticiones.
- **`etcd`**: Almacén distribuido clave-valor de alta disponibilidad basado en el algoritmo de consenso **Raft** (puertos **2379 TCP** clientes, **2380 TCP** peer). Guarda todo el estado del clúster.
- **`kube-scheduler`**: Asigna Pods recién creados a nodos Worker en función de requisitos de recursos y afinidades.
- **`kube-controller-manager`**: Ejecuta los bucles de control que reconcilian el estado actual con el estado deseado (*Node Lifecycle Controller*, *ReplicaSet Controller*, *ServiceAccount Controller*).

### 2. Nodos Worker
- **`kubelet`**: Agente principal del nodo; asegura que los contenedores descritos en los PodSpecs estén corriendo y saludables.
- **`kube-proxy`**: Mantiene las reglas de red en los nodos (vía `iptables` o `IPVS`) para gestionar el balanceo hacia los Services.
- **Container Runtime**: Motor de ejecución compatible con **CRI** (Container Runtime Interface), ej. `containerd` o `CRI-O`.

---

## 🧩 Objetos y Recursos Principales

- **Pod**: Unidad mínima desplegable. Contiene uno o más contenedores que comparten la misma dirección IP (`localhost`), espacio de red y volúmenes.
- **Deployment**: Controlador declarativo que gestiona Pods mediante **ReplicaSets**, permitiendo *Rolling Updates* sin caídas y *Rollbacks*.
- **Service**: Abstracción que expone un conjunto de Pods bajo una IP y DNS estables:
  - `ClusterIP`: Solo accesible dentro del clúster (por defecto).
  - `NodePort`: Expone el servicio en un puerto estático en cada nodo del clúster (rango **30000-32767**).
  - `LoadBalancer`: Aprovisiona un balanceador de carga externo en el proveedor cloud.
- **Ingress**: Gestiona el acceso externo HTTP/HTTPS hacia los servicios internos con enrutamiento por host/ruta y terminación SSL.

---

## 🎯 Datos Clave para Oposiciones TAI

| Componente / Objeto | Especificación Técnica |
|---------------------|------------------------|
| Base de Datos de K8s | **etcd** (Consenso Raft, puertos **2379/2380 TCP**) |
| Unidad Mínima | **Pod** (comparte red e IP) |
| Rango de Puertos NodePort | **30000 - 32767 TCP** |
| CLI de Gestión | `kubectl` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Motores de Contenedores]]
- Concepto: [[wiki/concepts/microservices-and-middleware|Microservicios, APIs y Middleware]]
