---
title: "PowerShell y Automatización de Administración"
type: "entity"
tags:
  - powershell
  - windows
  - automation
  - scripting
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "PowerShell Core"
  - "pwsh"
---

# PowerShell y Automatización de Administración

**PowerShell** es un entorno de automatización de tareas y administración de configuración multiplataforma basado en el framework .NET.

## Arquitectura Basada en Objetos
- A diferencia de las shells tradicionales que transmiten texto sin formato, los cmdlets de PowerShell transmiten **objetos tipados .NET** a través del pipeline `|`.
- **Nomenclatura Verbo-Sustantivo**: Estandarización de comandos como `Get-Process`, `Set-Service`, `New-Item`, `Restart-Computer`.
- **Módulos y Remoting**: Administración remota segura mediante WinRM y SSH (PowerShell Remoting / Enter-PSSession).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Sistema: [[wiki/entities/windows-server|Windows Server]]

