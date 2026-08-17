---
title: "Docker y Motores de Contenedores"
type: "entity"
tags:
  - docker
  - containers
  - oci
  - devops
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Docker"
  - "Contenedores"
---

# Docker y Motores de Contenedores

**Docker** es una plataforma de software de código abierto que automatiza el despliegue de aplicaciones dentro de **contenedores de software**, proporcionando una capa adicional de abstracción y automatización de virtualización a nivel de sistema operativo sobre Linux.

---

## 🏛️ Primitivas del Kernel de Linux Subyacentes

1. **Namespaces (Aislamiento de Recursos)**:
   - `pid`: Aislamiento del árbol de procesos (el proceso principal dentro del contenedor es PID 1).
   - `net`: Interfaces de red virtuales, tablas de enrutamiento y puertos propios.
   - `mnt`: Puntos de montaje del sistema de ficheros.
   - `ipc`: Comunicación entre procesos (memoria compartida, colas de mensajes).
   - `uts`: Nombre de host (*hostname*) y dominio.
   - `user`: Mapeo de UIDs/GIDs (permite ser root dentro del contenedor y usuario sin privilegios fuera).
2. **Control Groups (cgroups v1/v2)**:
   - Medición y limitación estricta de recursos de hardware: CPU (`cpu.shares`, `cpuset`), Memoria RAM (`memory.limit_in_bytes`, swap), I/O de disco y ancho de banda de red.
3. **Union File Systems (Overlay2)**:
   - Sistema de almacenamiento por capas inmutables de solo lectura apiladas (*Image Layers*) con una fina capa superior efímera de lectura/escritura (*Container Layer*).

---

## 🎯 Instrucciones del Dockerfile y Comandos

- `FROM`: Define la imagen base.
- `RUN`: Ejecuta comandos durante la construcción de la imagen.
- `COPY` / `ADD`: Copia ficheros del host a la imagen (`ADD` soporta descompresión tar y URLs).
- `CMD` vs `ENTRYPOINT`: `ENTRYPOINT` fija el ejecutable principal; `CMD` proporciona los parámetros por defecto modificables por CLI.
- `EXPOSE`: Documenta los puertos de escucha.
- Comandos CLI: `docker build -t app:v1 .`, `docker run -d -p 8080:80 --name web app:v1`, `docker ps`, `docker logs -f web`, `docker exec -it web bash`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Especificación Técnica |
|----------|------------------------|
| Primitivas Kernel | **Namespaces** (Aislamiento) + **cgroups** (Límites de recursos) |
| Driver de Almacenamiento | **Overlay2** (UnionFS) |
| Runtime de Bajo Nivel OCI | **runc** |
| Runtime de Alto Nivel | **containerd** / **CRI-O** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
- Síntesis: [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
