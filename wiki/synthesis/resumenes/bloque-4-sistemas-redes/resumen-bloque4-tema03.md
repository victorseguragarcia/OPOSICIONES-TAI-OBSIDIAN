---
title: "Resumen Exhaustivo Tema 03 (Bloque 4): Virtualización, Contenedores (Docker, Kubernetes) y Cloud Computing"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-03
  - sistemas
  - redes
  - seguridad\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema03.md]]"
  - "[[wiki/sources/bloque4-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|Tema 04 ➡️]]

# 🔴 Resumen Exhaustivo Tema 03 (Bloque 4): Virtualización, Contenedores (Docker, Kubernetes) y Cloud Computing

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 03**
> Virtualización de hardware (Hipervisores Tipo 1 Bare-Metal vs Tipo 2 Hosted), contenedores vs máquinas virtuales, Docker (Dockerfile, imágenes, contenedores, volúmenes, redes), orquestación con Kubernetes (Pods, ReplicaSets, Deployments, Services, Ingress, Namespaces) y modelos de Cloud Computing (IaaS, PaaS, SaaS, despliegue público, privado, híbrido).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Virtualización de Servidores e Hipervisores
- **Hipervisor Tipo 1 (Bare-Metal / Nativo)**: Se ejecuta directamente sobre el hardware físico sin sistema operativo anfitrión intermedio. Máximo rendimiento y eficiencia empresarial (VMware ESXi, Microsoft Hyper-V Server, KVM/Proxmox, Xen).
- **Hipervisor Tipo 2 (Hosted / Alojado)**: Se ejecuta como una aplicación sobre un SO anfitrión convencional. Mayor sobrecarga (VMware Workstation, VirtualBox).

### 2. Contenedores y Ecosistema Docker
- **Diferencia Crítica VM vs Contenedor**:
  - *Máquina Virtual (VM)*: Virtualiza el hardware completo; incluye un Sistema Operativo Invitado (*Guest OS*) completo (pesado, arranque en minutos, alto consumo de RAM).
  - *Contenedor*: Virtualiza a nivel de Sistema Operativo; **comparte el mismo Kernel del SO anfitrión** mediante namespaces y cgroups de Linux (ligero, arranque en milisegundos, bajo consumo).
- **Conceptos de Docker**:
  - *Dockerfile*: Archivo de texto declarativo con instrucciones de construcción (`FROM`, `RUN`, `COPY`, `ENV`, `EXPOSE`, `ENTRYPOINT`, `CMD`).
  - *Imagen*: Plantilla inmutable de solo lectura compuesta por capas apiladas.
  - *Contenedor*: Instancia en ejecución de una imagen con una capa superior de lectura/escritura.
  - *Persistencia*: **Volúmenes gestionados por Docker** (`docker volume create`) y *Bind Mounts* (enlace directo a ruta del host).

### 3. Orquestación con Kubernetes (K8s)
- **Arquitectura de Kubernetes**:
  - *Control Plane (Master Node)*: `kube-apiserver` (punto de entrada REST), `etcd` (almacén clave-valor distribuido del estado), `kube-scheduler` (asigna pods a nodos), `kube-controller-manager`.
  - *Worker Nodes*: `kubelet` (agente en nodo que gestiona contenedores), `kube-proxy` (gestiona reglas de red y balanceo), Container Runtime (containerd, CRI-O).
- **Objetos de Kubernetes**:
  - **Pod**: La unidad mínima de despliegue en K8s (contiene 1 o más contenedores que comparten red `localhost` y almacenamiento).
  - **Deployment**: Gestiona la creación, actualización declarativa y escalado de Pods mediante ReplicaSets.
  - **Service**: Abstracción que expone una IP estable y balanceo a un grupo de pods (`ClusterIP` interno, `NodePort` abre puerto en nodos, `LoadBalancer` balanceador cloud).
  - **Ingress**: Controlador que enruta tráfico HTTP/HTTPS externo hacia servicios internos basado en nombres de host y rutas URL.

### 4. Modelos de Cloud Computing (NIST SP 800-145)
- **Modelos de Servicio**:
  - **IaaS (Infrastructure as a Service)**: El proveedor gestiona el hardware, almacenamiento y red; el cliente gestiona SO, middleware, runtime y aplicaciones (AWS EC2, Azure VM, GCP Compute Engine).
  - **PaaS (Platform as a Service)**: El proveedor gestiona hardware, SO, runtime y base de datos; el cliente solo despliega su código y datos (AWS Elastic Beanstalk, Azure App Service, Heroku).
  - **SaaS (Software as a Service)**: El proveedor gestiona toda la pila; el cliente solo consume la aplicación por web/API (Microsoft 365, Google Workspace, Salesforce).

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 03 (Bloque 4)**
> 1. **KVM (Kernel-based Virtual Machine)**: Es considerado un **Hipervisor Tipo 1** (convierte el kernel de Linux en un hipervisor bare-metal).
> 2. **Unidad Mínima en Kubernetes**: Es el **Pod** (Kubernetes nunca despliega contenedores sueltos directamente).
> 3. **etcd en Kubernetes**: Es la base de datos distribuida clave-valor que almacena **todo el estado del cluster**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Modelos Cloud (Control del Cliente)**: **IaaS (Desde el SO) $\rightarrow$ PaaS (Solo Aplicación) $\rightarrow$ SaaS (Solo Usuario)**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema03|Fuente Oficial del Tema 03]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema03|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema03-linux-administracion|Test Tema 03]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|Tema 04 ➡️]]
