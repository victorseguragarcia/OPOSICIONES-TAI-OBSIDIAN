---
title: "Test de Autoevaluación: Bloque 4 - Tema 03 (Administración de Sistemas Linux y Bash)"
type: "test"
target: "wiki/sources/bloque4-tema03.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-4
  - linux
  - systemd
  - lvm
  - permisos-octales
  - bash
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test de Autoevaluación: Bloque 4 - Tema 03 (Administración de Sistemas Linux y Bash)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 4 - Tema 03 (Administración de Sistemas Linux y Bash)",
  "questions": [
    {
      "question": "En Linux, si un fichero tiene permisos `rwxr-x---`, ¿cuál es su representación numérica en notación octal?",
      "options": [
        "750",
        "755",
        "760",
        "640"
      ],
      "answer": "a",
      "explanation": "`rwx` = $4+2+1 = 7$; `r-x` = $4+0+1 = 5$; `---` = $0"
    },
    {
      "question": "Si la máscara de usuario (*umask*) está fijada en `027`, ¿cuáles serán los permisos predeterminados de un nuevo FICHERO ordinario creado en el sistema?",
      "options": [
        "`640` (`rw-r-----`)",
        "`750` (`rwxr-x---`)",
        "`644` (`rw-r--r--`)",
        "`664` (`rw-rw-r--`)"
      ],
      "answer": "a",
      "explanation": "Ficheros base máxima `666` (`rw-rw-rw-`). Con umask `027`: `666 - 027 = 640` (`rw-r-----`)."
    },
    {
      "question": "En el sistema de inicio Systemd de Linux, ¿qué comando se utiliza para habilitar un servicio para que se inicie automáticamente en el arranque y arrancarlo en el momento actual?",
      "options": [
        "`service nginx restart`",
        "`systemctl enable --now nginx`",
        "`systemctl start --boot nginx`",
        "`chkconfig nginx on`"
      ],
      "answer": "b",
      "explanation": "`systemctl enable --now` habilita el symlink en el target y arranca el servicio simultáneamente."
    },
    {
      "question": "En la arquitectura de Logical Volume Manager (LVM), ¿cuál es la jerarquía correcta de abstracción desde el almacenamiento físico hasta el sistema de ficheros?",
      "options": [
        "LV (Logical Volume) $",
        "PV (Physical Volume) $",
        "VG $",
        "LUN $"
      ],
      "answer": "b",
      "explanation": "PVs (discos/particiones) se agrupan en VGs, que se dividen en LVs donde se formatea el sistema de ficheros."
    },
    {
      "question": "¿Qué comando de Linux permite consultar los logs centralizados gestionados por el demonio `systemd-journald` en tiempo real?",
      "options": [
        "`dmesg -f`",
        "`journalctl -f -u <servicio>`",
        "`tail -f /var/log/syslog`",
        "`cat /proc/kmsg`"
      ],
      "answer": "b",
      "explanation": "`journalctl -f` sigue el log en tiempo real del journal binario de systemd."
    }
  ]
}
```
