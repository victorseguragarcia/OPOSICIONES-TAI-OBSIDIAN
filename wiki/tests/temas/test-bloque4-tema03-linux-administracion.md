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

# 🔴 Test Tema 03: Administración de Sistemas Linux, Systemd y Permisos

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---

## ❓ Preguntas

### 1. En Linux, si un fichero tiene permisos `rwxr-x---`, ¿cuál es su representación numérica en notación octal?
- [ ] a) 750
- [ ] b) 755
- [ ] c) 760
- [ ] d) 640

### 2. Si la máscara de usuario (*umask*) está fijada en `027`, ¿cuáles serán los permisos predeterminados de un nuevo FICHERO ordinario creado en el sistema?
- [ ] a) `640` (`rw-r-----`)
- [ ] b) `750` (`rwxr-x---`)
- [ ] c) `644` (`rw-r--r--`)
- [ ] d) `664` (`rw-rw-r--`)

### 3. En el sistema de inicio Systemd de Linux, ¿qué comando se utiliza para habilitar un servicio para que se inicie automáticamente en el arranque y arrancarlo en el momento actual?
- [ ] a) `service nginx restart`
- [ ] b) `systemctl enable --now nginx`
- [ ] c) `systemctl start --boot nginx`
- [ ] d) `chkconfig nginx on`

### 4. En la arquitectura de Logical Volume Manager (LVM), ¿cuál es la jerarquía correcta de abstracción desde el almacenamiento físico hasta el sistema de ficheros?
- [ ] a) LV (Logical Volume) $ightarrow$ VG (Volume Group) $ightarrow$ PV (Physical Volume)
- [ ] b) PV (Physical Volume) $ightarrow$ VG (Volume Group) $ightarrow$ LV (Logical Volume) $ightarrow$ Filesystem
- [ ] c) VG $ightarrow$ PV $ightarrow$ LV
- [ ] d) LUN $ightarrow$ RAID $ightarrow$ PV

### 5. ¿Qué comando de Linux permite consultar los logs centralizados gestionados por el demonio `systemd-journald` en tiempo real?
- [ ] a) `dmesg -f`
- [ ] b) `journalctl -f -u <servicio>`
- [ ] c) `tail -f /var/log/syslog`
- [ ] d) `cat /proc/kmsg`

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **a** | 2. **a** | 3. **b** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (a)**: `rwx` = $4+2+1 = 7$; `r-x` = $4+0+1 = 5$; `---` = $0 ightarrow$ **750**.
> - **Pregunta 2 (a)**: Ficheros base máxima `666` (`rw-rw-rw-`). Con umask `027`: `666 - 027 = 640` (`rw-r-----`).
> - **Pregunta 3 (b)**: `systemctl enable --now` habilita el symlink en el target y arranca el servicio simultáneamente.
> - **Pregunta 4 (b)**: PVs (discos/particiones) se agrupan en VGs, que se dividen en LVs donde se formatea el sistema de ficheros.
> - **Pregunta 5 (b)**: `journalctl -f` sigue el log en tiempo real del journal binario de systemd.
