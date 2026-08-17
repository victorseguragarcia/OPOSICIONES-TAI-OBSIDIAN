---
title: "Test Tema 01: Conceptos de SO, Arquitectura y Virtualización"
type: "test"
target: "wiki/sources/bloque4-tema01-conceptos-so-virtualizacion.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 01: Conceptos de SO, Arquitectura y Virtualización

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 01: Conceptos de SO, Arquitectura y Virtualización",
  "questions": [
    {
      "question": "¿Cuál es la principal diferencia arquitectónica entre la virtualización basada en Hipervisores Tipo 1 (Bare-Metal) y la basada en Contenedores (Docker)?",
      "options": [
        "Los hipervisores Tipo 1 virtualizan el hardware completo ejecutando un SO invitado con su propio kernel; los contenedores comparten el mismo kernel del sistema operativo anfitrión aislando espacios de usuario (*namespaces* y *cgroups*).",
        "Los contenedores consumen más memoria RAM y tardan minutos en arrancar frente a las máquinas virtuales.",
        "Los contenedores requieren obligatoriamente procesadores con extensiones Intel VT-x.",
        "Las máquinas virtuales no permiten conectividad de red."
      ],
      "answer": "a",
      "explanation": "Los contenedores comparten el kernel anfitrión (alta densidad y ligereza); las VMs virtualizan el hardware emulado con kernel propio."
    },
    {
      "question": "¿Cuál de los siguientes hipervisores es de TIPO 1 (Bare-Metal / Nativo)?",
      "options": [
        "Oracle VirtualBox.",
        "VMware Workstation Pro.",
        "VMware ESXi.",
        "QEMU ejecutado en espacio de usuario."
      ],
      "answer": "c",
      "explanation": "VMware ESXi, Proxmox VE, Microsoft Hyper-V Server y KVM (en modo kernel) son hipervisores Tipo 1."
    },
    {
      "question": "En la gestión de memoria de los sistemas operativos modernos, ¿qué función cumple la MMU (Memory Management Unit)?",
      "options": [
        "Compilar código C en tiempo real.",
        "Traducir las direcciones lógicas/virtuales generadas por la CPU a direcciones físicas en memoria RAM y gestionar la protección de memoria.",
        "Gestionar las interrupciones del bus USB.",
        "Realizar el balanceo de carga de procesos entre núcleos."
      ],
      "answer": "b",
      "explanation": "La MMU realiza la traducción dirección virtual $\rightarrow$ dirección física y valida los permisos de acceso a páginas."
    },
    {
      "question": "¿Qué dos características del kernel de Linux son la base fundamental del aislamiento de los contenedores Docker?",
      "options": [
        "Namespaces (aislamiento de procesos, red, mounts) y Cgroups (control y límite de recursos CPU/RAM).",
        "Systemd y SysVinit.",
        "IPTables y SELinux exclusivamente.",
        "LVM y Swap."
      ],
      "answer": "a",
      "explanation": "Namespaces proporcionan aislamiento de vista (PID, NET, MNT, IPC, UTS); Cgroups limitan y miden el consumo de CPU/memoria/E-S."
    },
    {
      "question": "En Kubernetes, ¿cuál es la unidad mínima de ejecución y despliegue que encapsula uno o más contenedores estrechamente acoplados?",
      "options": [
        "Node.",
        "Pod.",
        "Cluster.",
        "Deployment."
      ],
      "answer": "b",
      "explanation": "El Pod es la unidad básica en Kubernetes; comparte almacenamiento, IP de red y contexto de ejecución entre sus contenedores."
    }
  ]
}
```
