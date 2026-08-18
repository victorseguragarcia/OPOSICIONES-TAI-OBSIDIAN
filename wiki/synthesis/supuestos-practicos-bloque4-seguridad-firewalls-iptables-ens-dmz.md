---
title: "Supuesto Práctico Bloque 4: Diseño de Arquitectura DMZ, Reglas iptables, Hardening y Categorización ENS"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-4
  - iptables
  - firewall
  - dmz
  - ens
sources:
  - "raw/sources/bloque4-tema09.md"
  - "raw/bloque 1/623849 (3).pdf"
created: "2026-08-18"
updated: "2026-08-18"
aliases:
  - "Supuesto Práctico DMZ e iptables"
  - "Caso Práctico Seguridad Redes y ENS"
---

# 🔴 Supuesto Práctico Bloque 4: Diseño de Arquitectura DMZ, Reglas iptables y Categorización ENS

Cuaderno de resolución de supuestos prácticos de infraestructura segura de red para examen oficial TAI.

---

## 📋 Enunciado del Escenario Práctico

Un Organismo Público necesita desplegar una sede electrónica accesible desde Internet con acceso a base de datos interna cumpliendo con el **Esquema Nacional de Seguridad (ENS RD 311/2022)**.

### Topología de Red:
```
           [ INTERNET ]
                 │
                 ▼ (eth0: IP Pública 203.0.113.1)
          ┌──────────────┐
          │ FIREWALL PER │ (Gateway Linux con iptables)
          └──────┬───────┘
                 ├─── (eth1: 192.168.10.1/24) ──► [ DMZ: Servidor Web Nginx 192.168.10.50 ]
                 │
                 └─── (eth2: 192.168.20.1/24) ──► [ RED INTERNA: BBDD MySQL 192.168.20.100 ]
                                              ──► [ GESTIÓN: PC Admin 192.168.20.10 ]
```

---

## ❓ Preguntas del Ejercicio Práctico

### Pregunta 1: Configuración de Reglas de Filtrado `iptables`
Escriba el script de comandos `iptables` en el Firewall para:
1. Política por defecto `DROP` en todas las cadenas (`INPUT`, `FORWARD`, `OUTPUT`).
2. Permitir tráfico de retorno de conexiones ya establecidas (`ESTABLISHED,RELATED`).
3. Permitir tráfico web HTTP (80) y HTTPS (443) desde Internet hacia el Servidor Web en DMZ (`192.168.10.50`).
4. Permitir que el Servidor Web en DMZ consulte la base de datos MySQL (`192.168.20.100:3306`) en la Red Interna.
5. Permitir administración SSH (22) al Servidor Web y al Firewall **únicamente** desde la IP del Administrador (`192.168.20.10`).

> [!question]- 🔍 Solución Detallada Pregunta 1: Script iptables
> ```bash
> #!/bin/bash
> # 1. Limpieza de reglas previas
> iptables -F
> iptables -X
> iptables -t nat -F
> 
> # 2. Políticas por defecto DROP (Principio de mínimo privilegio)
> iptables -P INPUT DROP
> iptables -P FORWARD DROP
> iptables -P OUTPUT DROP
> 
> # 3. Permitir tráfico en interfaz loopback local
> iptables -A INPUT -i lo -j ACCEPT
> iptables -A OUTPUT -o lo -j ACCEPT
> 
> # 4. Permitir paquetes de conexiones ya establecidas y relacionadas
> iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
> iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
> iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
> 
> # 5. Permitir tráfico HTTP (80) y HTTPS (443) desde Internet hacia la DMZ
> iptables -A FORWARD -i eth0 -o eth1 -p tcp -d 192.168.10.50 -m multiport --dports 80,443 -m state --state NEW -j ACCEPT
> 
> # 6. Permitir consulta del Servidor Web DMZ al MySQL en Red Interna
> iptables -A FORWARD -i eth1 -o eth2 -p tcp -s 192.168.10.50 -d 192.168.20.100 --dport 3306 -m state --state NEW -j ACCEPT
> 
> # 7. Permitir SSH (22) únicamente desde el PC del Administrador (192.168.20.10)
> # Al Firewall local:
> iptables -A INPUT -i eth2 -p tcp -s 192.168.20.10 --dport 22 -m state --state NEW -j ACCEPT
> # Al Servidor Web DMZ:
> iptables -A FORWARD -i eth2 -o eth1 -p tcp -s 192.168.20.10 -d 192.168.10.50 --dport 22 -m state --state NEW -j ACCEPT
> ```

---

### Pregunta 2: Categorización de Seguridad del Sistema según el ENS (RD 311/2022)
El análisis de impacto del sistema arroja los siguientes niveles de exigencia por dimensión de seguridad:
- **Disponibilidad (D)**: Nivel **MEDIO** (el servicio no puede estar ininterrumpido más de 4 horas).
- **Autenticidad (A)**: Nivel **ALTO** (trámites con certificado cualificado y firma electrónica).
- **Integridad (I)**: Nivel **ALTO** (modificación no autorizada invalida actos administrativos).
- **Confidencialidad (C)**: Nivel **MEDIO** (datos personales de categoría básica según RGPD).
- **Trazabilidad (T)**: Nivel **ALTO** (auditoría de accesos y firmas registrada en log no repudiable).

Determine:
1. La **Categoría Global de Seguridad** del sistema.
2. Si es obligatoria una **Auditoría de Seguridad bianual**.
3. La designación obligatoria del **Responsable de la Información** y **Responsable de la Seguridad**.

> [!question]- 🔍 Solución Detallada Pregunta 2
> **1. Categoría Global de Seguridad**:
> - Principio de la dimensión más exigente:
>   $$\text{Categoría Global} = \max(D, A, I, C, T) = \max(\text{Medio}, \text{Alto}, \text{Alto}, \text{Medio}, \text{Alto}) = \mathbf{ALTA}$$
> 
> **2. Obligatoriedad de Auditoría de Seguridad (Art. 34 ENS)**:
> - Para sistemas de categoría **MEDIA o ALTA**, es **OBLIGATORIA una Auditoría de Seguridad periódica al menos cada 2 AÑOS** (o con carácter extraordinario si se producen modificaciones sustanciales en el sistema).
> 
> **3. Roles y Responsabilidades (Art. 12 ENS)**:
> - En categorías Media y Alta, es preceptiva la diferenciación formal entre el **Responsable de la Información** (determina los requisitos de seguridad de los datos), el **Responsable del Servicio** y el **Responsable de la Seguridad** (determina las decisiones para satisfacer los requisitos), garantizando el principio de segregación de funciones.
