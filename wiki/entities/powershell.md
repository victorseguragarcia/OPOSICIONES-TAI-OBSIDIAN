---
title: "PowerShell y Cmdlets en Entornos Windows"
type: "entity"
tags:
  - powershell
  - windows
  - cmdlets
  - scripting
  - automation
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "PowerShell"
  - "Windows PowerShell"
  - "pwsh"
---

# PowerShell y Cmdlets en Entornos Windows

**PowerShell** es un marco de automatización de tareas y configuración multiplataforma compuesto por un intérprete de línea de comandos (CLI) y un potente lenguaje de scripting orientado a **objetos .NET**, desarrollado por Microsoft.

---

## 🏛️ Evolución y Características

- **Historia**: Primera versión lanzada en **noviembre de 2006** para Windows XP SP2 y Windows Server 2003.
- **PowerShell Core (Multiplataforma)**: Liberado como software de **código abierto** en **2016** bajo licencia MIT. Basado en .NET Core (`pwsh`), disponible para Windows, Linux y macOS.
- **Paradigma Orientado a Objetos**: A diferencia de los shells tradicionales de Unix basados en flujos de texto plano, los comandos de PowerShell (**Cmdlets**) reciben y emiten **instancias de objetos .NET**, permitiendo acceder directamente a propiedades y métodos a través del pipeline `|`.

---

## 🧩 Políticas de Ejecución (Execution Policies)

Para prevenir la ejecución inadvertida de scripts maliciosos, PowerShell incorpora directivas de control:

| Política | Comportamiento |
|----------|----------------|
| `Restricted` | Política por defecto en Windows cliente. No permite ejecutar scripts (`.ps1`); solo comandos interactivos. |
| `AllSigned` | Solo permite ejecutar scripts firmados digitalmente por un editor de confianza. |
| `RemoteSigned` | Permite ejecutar scripts locales sin firmar; exige firma digital para scripts descargados de Internet. |
| `Unrestricted` | Permite ejecutar cualquier script (muestra advertencia al ejecutar scripts de Internet). |
| `Bypass` | Desactiva por completo los bloqueos sin mostrar advertencias. |

---

## 🎯 Cmdlets Fundamentales

- `Get-Command`: Lista todos los cmdlets, funciones y alias disponibles.
- `Get-Help <cmdlet> -Full`: Muestra la documentación completa y ejemplos.
- `Get-Process` / `Stop-Process`: Gestión de procesos del sistema.
- `Get-Service` / `Start-Service` / `Stop-Service`: Control de servicios de Windows.
- `Get-EventLog` / `Get-WinEvent`: Consulta de logs del Visor de Eventos.
- `Invoke-Command -ComputerName <host> -ScriptBlock { ... }`: Ejecución remota vía WinRM (puertos **5985 HTTP** / **5986 HTTPS**).
- `ConvertTo-Html` / `Export-Csv`: Exportación estructurada de objetos.

---

## 🎯 Datos Clave para Oposiciones TAI

| Aspecto | Especificación Técnica |
|---------|------------------------|
| Año Lanzamiento / Open Source | **Noviembre 2006** / **2016** (Licencia MIT) |
| Estructura de Comandos | **Verbo-Sustantivo** (`Get-Process`, `Set-Item`) |
| Protocolo de Remoting | **WS-Man / WinRM** (Puertos **5985 HTTP** / **5986 HTTPS**) |
| Consultar/Cambiar Política | `Get-ExecutionPolicy` / `Set-ExecutionPolicy` |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/windows-server|Windows Server]]
- Entidad: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
