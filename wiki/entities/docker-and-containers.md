---
title: "Docker y Tecnologías de Contenedores"
type: "entity"
tags:
  - containers
  - docker
  - devops
  - virtualization
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Docker"
  - "Contenedores"
  - "Containerization"
---

# Docker y Tecnologías de Contenedores

**Docker** es una plataforma de virtualización a nivel de sistema operativo que permite empaquetar aplicaciones y sus dependencias en contenedores ligeros, portables y reproducibles.

## Mecanismos del Kernel Subyacentes
- **Linux Namespaces**: Proveen aislamiento de recursos (`pid`, `net`, `ipc`, `mnt`, `uts`, `user`).
- **Control Groups (cgroups)**: Limitan y monitorizan el consumo de CPU, memoria, I/O y red.
- **Union File Systems (Overlay2)**: Capas de almacenamiento de solo lectura con una capa superior modificable (Copy-on-Write).

## Objetos Docker
- **Dockerfile**: Receta declarativa de construcción de imágenes.
- **Docker Image**: Plantilla inmutable de solo lectura.
- **Container**: Instancia en ejecución de una imagen.

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Orquestación: [[wiki/entities/kubernetes|Kubernetes]]
- Concepto: [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Cloud Computing]]

