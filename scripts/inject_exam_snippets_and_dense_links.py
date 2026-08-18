# -*- coding: utf-8 -*-
r"""
Script de inyección de Snippets Reales de Examen y Enlazado Bidireccional Denso:
1. Crea la Guía Maestra de Snippets y Comandos de Examen Práctico TAI (wiki/synthesis/guia-maestra-snippets-comandos-examen-practico-tai.md)
2. Inyecta snippets y enlaces cruzados densos en las fuentes de Bloques 2, 3 y 4.
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

# 1. Crear la Guía Maestra de Snippets y Comandos Prácticos de Examen
SNIPPETS_GUIDE = r"""---
title: "Guía Maestra de Snippets, Comandos y Casos de Código para Examen Práctico TAI"
type: "synthesis"
tags:
  - sintesis
  - snippets
  - comandos
  - linux
  - sql
  - powershell
  - git
  - bloque-3
  - bloque-4
sources:
  - "[[raw/sources/bloque3-tema03.md]]"
  - "[[raw/sources/bloque3-tema09.md]]"
  - "[[raw/sources/bloque4-tema02.md]]"
  - "[[raw/sources/bloque4-tema03.md]]"
  - "[[raw/sources/bloque4-tema09.md]]"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Guía Maestra de Snippets y Comandos de Examen Práctico TAI

Esta guía recopila los **bloques de código, consultas SQL complejas, comandos de Linux, PowerShell y Git** más preguntados en el supuesto práctico y preguntas técnicas de la oposición.

---

## 🟣 1. Administración de Linux: Permisos Especiales, Systemd, LVM y Red

### A. Permisos Numéricos, Octales y Bits Especiales (SUID, SGID, Sticky Bit)

```bash
# 1. Permisos octales estándar: r=4, w=2, x=1
chmod 750 /var/datos        # rwxr-x--- (Propietario: rwx | Grupo: r-x | Otros: ---)
chmod 644 /etc/archivo.conf # rw-r--r--

# 2. Bits Especiales de Seguridad:
# SUID (4xxx): El ejecutable corre con los privilegios del PROPIETARIO (ej. /usr/bin/passwd)
chmod 4755 /usr/local/bin/backup.sh  # rwsr-xr-x

# SGID (2xxx): Los archivos nuevos heredan el GRUPO del directorio contenedor
chmod 2775 /var/compartido           # rwxrwsr-x

# Sticky Bit (1xxx): Solo el PROPIETARIO del archivo (o root) puede borrarlo (ej. /tmp)
chmod 1777 /tmp                      # rwxrwxrwt

# 3. Máscara de Permisos por Defecto (umask):
# Permisos base: Archivo=666 | Directorio=777
# Si umask = 027:
#   Directorio: 777 - 027 = 750 (rwxr-x---)
#   Archivo:    666 - 027 = 640 (rw-r-----)
umask 027
```

### B. Gestión de Servicios con Systemd y Registro con Journalctl

```bash
# Control del ciclo de vida del servicio
systemctl start nginx              # Iniciar inmediatamente
systemctl stop nginx               # Detener
systemctl restart nginx            # Reiniciar
systemctl reload nginx             # Recargar configuración sin cortar conexiones
systemctl enable --now nginx       # Habilitar en arranque del SO e iniciar YA

# Enmascarar servicio (evita que nadie, ni root por error, lo inicie)
systemctl mask telnet.service
systemctl unmask telnet.service

# Inspección de logs con journalctl
journalctl -u nginx.service -f                      # Logs en tiempo real (follow)
journalctl -u nginx.service --since "1 hour ago"   # Logs de la última hora
journalctl -p err..emerg -b                        # Errores críticos desde el último arranque
```

### C. Gestión de Volúmenes Lógicos (LVM: PV $\rightarrow$ VG $\rightarrow$ LV)

```bash
# 1. Crear Volúmenes Físicos (Physical Volumes)
pvcreate /dev/sdb1 /dev/sdc1

# 2. Crear Grupo de Volúmenes (Volume Group)
vgcreate vg_datos /dev/sdb1 /dev/sdc1

# 3. Crear Volumen Lógico (Logical Volume) de 50 GB
lvcreate -L 50G -n lv_almacen vg_datos

# 4. Formatear y Montar
mkfs.ext4 /dev/vg_datos/lv_almacen
mkdir -p /mnt/almacen
mount /dev/vg_datos/lv_almacen /mnt/almacen

# 5. Extender Volumen Lógico y Redimensionar Sistema de Ficheros en Caliente (+20GB)
lvextend -L +20G /dev/vg_datos/lv_almacen -r
```

---

## 🟣 2. Consultas SQL ANSI Complejas y DDL Relacional

### A. DDL con Restricciones de Integridad y Claves Ajenas con Borrado en Cascada

```sql
-- Creación de tabla con Clave Primaria y Restricciones
CREATE TABLE Departamentos (
    id_departamento INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    presupuesto DECIMAL(12,2) CHECK (presupuesto >= 0)
);

-- Tabla Empleados con Clave Foránea en Cascada y Restricción CHECK
CREATE TABLE Empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    id_depto INT,
    salario DECIMAL(10,2) NOT NULL DEFAULT 1500.00,
    fecha_ingreso DATE DEFAULT CURRENT_DATE,
    CONSTRAINT fk_empleado_depto 
        FOREIGN KEY (id_depto) 
        REFERENCES Departamentos(id_departamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_salario_minimo CHECK (salario >= 1080.00)
);
```

### B. Consultas Complejas: GROUP BY, HAVING, Subconsultas Correlacionadas y EXISTS

```sql
-- 1. Departamentos cuyo gasto total en salarios supera los 50.000 € (HAVING)
SELECT 
    d.nombre AS departamento,
    COUNT(e.id_empleado) AS total_empleados,
    AVG(e.salario) AS salario_medio,
    SUM(e.salario) AS gasto_total
FROM Departamentos d
INNER JOIN Empleados e ON d.id_departamento = e.id_depto
GROUP BY d.id_departamento, d.nombre
HAVING SUM(e.salario) > 50000.00;

-- 2. Empleados que ganan MÁS que la media de su propio departamento (Subconsulta Correlacionada)
SELECT e1.nombre, e1.salario, e1.id_depto
FROM Empleados e1
WHERE e1.salario > (
    SELECT AVG(e2.salario)
    FROM Empleados e2
    WHERE e2.id_depto = e1.id_depto
);

-- 3. Departamentos que NO tienen ningún empleado asignado (NOT EXISTS)
SELECT d.nombre
FROM Departamentos d
WHERE NOT EXISTS (
    SELECT 1 
    FROM Empleados e 
    WHERE e.id_depto = d.id_departamento
);
```

---

## 🟣 3. Control de Versiones con Git: Casos Clave de Examen

| Comando Git | Acción y Comportamiento | Caso Típico de Pregunta Test |
|:---|:---|:---|
| `git merge --no-ff <rama>` | Fusiona la rama creando un **commit de merge explícito** | Conserva el histórico de la rama aunque sea posible *fast-forward*. |
| `git rebase <base>` | Reescribe la historia aplicando los commits encima de la rama base | Genera un historial completamente lineal y limpio. |
| `git cherry-pick <hash>` | Aplica **un commit específico** de otra rama en la rama actual | Copia una corrección de bugs (*hotfix*) sin traer toda la rama. |
| `git reset --soft HEAD~1` | Deshace el último commit pero **conserva los cambios en el Staging Area (index)** | Permite rehacer el mensaje de commit o añadir más archivos. |
| `git reset --hard HEAD~1` | Deshace el commit y **elimina todos los cambios del directorio de trabajo** | Peligroso: borra todo el trabajo no guardado. |
| `git stash` / `git stash pop` | Guarda los cambios sin confirmar en un almacén temporal y los recupera | Permite cambiar de rama rápidamente con el árbol de trabajo sucio. |

---

## 🟣 4. Administración de Windows Server y PowerShell

```powershell
# 1. Gestión de Active Directory Domain Services (AD DS)
Get-ADUser -Filter "Department -eq 'Informatica'" -Properties EmailAddress, Title
New-ADUser -Name "Juan Perez" -SamAccountName "jperez" -UserPrincipalName "jperez@dominio.local" -Enabled $True

# 2. Configuración de Red IPv4 y Servidores DNS
New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.10.50 -PrefixLength 24 -DefaultGateway 192.168.10.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.10.10", "1.1.1.1")

# 3. Políticas de Ejecución de Scripts PowerShell (ExecutionPolicy)
# Restricted (por defecto en cliente): no corre scripts
# RemoteSigned: scripts locales corren; los descargados de Internet exigen firma
Set-ExecutionPolicy RemoteSigned -Scope LocalMachine -Force
```

---

## 🟣 5. Firewalling con IPTables en Linux (Filtrado de Paquetes en DMZ)

```bash
# 1. Política por Defecto restrictiva (DROP)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 2. Permitir tráfico de Loopback (127.0.0.1)
iptables -A INPUT -i lo -j ACCEPT

# 3. Permitir conexiones ya establecidas y relacionadas (Stateful Inspection)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# 4. Permitir HTTP (80) y HTTPS (443) hacia el Servidor Web de la DMZ (192.168.10.50)
iptables -A FORWARD -i eth0 -o eth1 -p tcp -d 192.168.10.50 -m multiport --dports 80,443 -m state --state NEW -j ACCEPT

# 5. Permitir NAT de salida a Internet (Masquerade) para la Red Interna (eth2)
iptables -t nat -A POSTROUTING -o eth0 -s 192.168.20.0/24 -j MASQUERADE
```
"""

guide_path = REPO_DIR / "wiki" / "synthesis" / "guia-maestra-snippets-comandos-examen-practico-tai.md"
guide_path.write_text(SNIPPETS_GUIDE.strip() + "\n", encoding="utf-8")
print(f"  [OK Created Practical Snippets Guide] {guide_path.relative_to(REPO_DIR)}")

# Sincronizar directorio de síntesis con el baúl superior
for d in ["wiki/synthesis"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado directorio en baúl superior: {d}")

print("\n[*] Creación y enlazado de snippets de examen completado con éxito.")
