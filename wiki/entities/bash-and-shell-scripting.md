---
title: "Bash y Shell Scripting en Linux"
type: "entity"
tags:
  - bash
  - shell
  - linux
  - scripting
  - automation
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "GNU Bash"
  - "Bash Scripting"
---

# Bash y Shell Scripting en Linux

**GNU Bash (Bourne-Again Shell)** es el intérprete de comandos y lenguaje de programación de scripts estándar en sistemas operativos GNU/Linux, desarrollado originalmente por **Brian Fox** en 1988 para el proyecto GNU como sustituto libre del Bourne Shell (`sh`).

---

## 🏛️ Historia y Seguridad

- **Lanzamiento**: Primera versión beta (0.99) el **8 de junio de 1989**. Mantenido posteriormente por **Chet Ramey**.
- **Vulnerabilidad Shellshock (CVE-2014-6271)**:
  - Descubierta por **Stéphane Chazelas** en septiembre de 2014.
  - Fallo crítico que permitía la ejecución remota de código arbitrario al concatenar comandos al final de definiciones de funciones exportadas a través de variables de entorno (especialmente crítico en scripts CGI web).

---

## 🧩 Sintaxis y Variables Especiales

- **Shebang**: `#!/bin/bash` (indica al kernel el intérprete a utilizar).
- **Variables Especiales**:
  - `$0`: Nombre del script en ejecución.
  - `$1, $2, ... $n`: Argumentos posicionales pasados al script. A partir de 10 se referencian como `${10}`.
  - `$#`: Número total de argumentos pasados.
  - `$@`: Array con todos los argumentos como palabras separadas (`"$@"` preserva espacios).
  - `$*`: Cadena única con todos los argumentos separados por el primer carácter de `IFS`.
  - `$?`: Código de retorno del último comando ejecutado (`0` = éxito, `>0` = error).
  - `$$`: PID del proceso de la shell actual.
  - `$!`: PID del último proceso ejecutado en segundo plano (*background* con `&`).
- **Estructuras de Control**:
  - Condicional: `if [ condición ]; then ... elif [ ... ]; then ... else ... fi`
  - Selección: `case "$var" in patron1) ... ;; patron2) ... ;; *) ... ;; esac`
  - Bucles: `for var in lista; do ... done` y `while [ condición ]; do ... done`
  - Test extendido: `[[ expresión ]]` (soporta operadores regex `=~` y operadores lógicos `&&`, `||`).
- **Redirecciones y Tuberías**:
  - Redirección salida estándar: `>` (sobrescribe), `>>` (añade al final).
  - Redirección error estándar: `2>`, `2>&1` (redirige stderr a stdout), `&>` (redirige ambos).
  - Tubería (*Pipe*): `comando1 | comando2` (conecta la salida estándar de comando1 con la entrada de comando2).

---

## 🎯 Datos Clave para Oposiciones TAI

| Característica | Detalle Técnico |
|----------------|-----------------|
| Autor Original | **Brian Fox** (Proyecto GNU, 1988/1989) |
| Vulnerabilidad Shellshock | **CVE-2014-6271** (Septiembre 2014) |
| Código de Salida Exitoso | **0** (`$? == 0`) |
| Comprobación Ficheros | `-f` (es fichero regular), `-d` (es directorio), `-x` (es ejecutable), `-z` (cadena vacía) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
