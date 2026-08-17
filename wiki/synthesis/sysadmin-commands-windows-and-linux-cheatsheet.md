---
title: "Cheatsheet de Comandos de Administración de Sistemas Windows y Linux"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - sysadmin
  - linux-commands
  - windows-commands
  - powershell
sources:
  - "raw/sources/bloque4-tema01.md"
  - "raw/sources/bloque4-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet Comandos Sysadmin"
  - "Sysadmin Commands Cheatsheet"
---

# Cheatsheet de Comandos de Administración de Sistemas Windows y Linux

Tabla de comandos esenciales de consola para diagnóstico de redes, gestión de servicios, usuarios, almacenamiento y logs en Windows y Linux.

---

## 📋 Comparativa Directa de Comandos por Función

| Función Administrativa | Comando Windows (CMD / PowerShell) | Comando Linux (Bash) |
|------------------------|------------------------------------|----------------------|
| **Configuración IP** | `ipconfig /all` / `Get-NetIPAddress` | `ip addr show` / `ifconfig` |
| **Tabla de Rutas** | `route print` / `Get-NetRoute` | `ip route show` / `route -n` |
| **Tabla ARP** | `arp -a` / `Get-NetNeighbor` | `ip neigh show` / `arp -a` |
| **Conexiones y Puertos** | `netstat -ano` / `Get-NetTCPConnection` | `ss -tulpn` / `netstat -tuln` |
| **Traza de Ruta** | `tracert <destino>` / `Test-NetConnection` | `traceroute <destino>` / `mtr` |
| **Consulta DNS** | `nslookup <nombre>` / `Resolve-DnsName` | `dig <nombre>` / `host <nombre>` |
| **Prueba de Conectividad** | `ping <host>` / `Test-Connection` | `ping <host>` |
| **Gestión de Servicios** | `sc query` / `Get-Service`, `Start-Service` | `systemctl {status|start|stop|restart} <srv>` |
| **Procesos Activos** | `tasklist` / `Get-Process` | `ps aux` / `top` / `htop` |
| **Terminar Proceso** | `taskkill /PID <pid> /F` / `Stop-Process` | `kill -9 <pid>` / `killall <nombre>` |
| **Visor de Logs** | `eventvwr.msc` / `Get-WinEvent` | `journalctl -u <srv> -f` / `tail -f /var/log/syslog` |
| **Gestión de Discos** | `diskmgmt.msc` / `diskpart` | `fdisk -l` / `lsblk` / `gdisk` / `parted` |
| **Uso de Espacio** | `dir` / `Get-PSDrive` | `df -h` (sistemas) / `du -sh *` (carpetas) |
| **Permisos de Ficheros** | `icacls <ruta>` / `Get-Acl` | `chmod`, `chown`, `getfacl`, `setfacl` |
| **Directivas de Grupo** | `gpupdate /force` / `gpresult /r` | N/A |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/bash-and-shell-scripting|Bash y Shell Scripting]]
- Entidad: [[wiki/entities/powershell|PowerShell y Cmdlets]]
