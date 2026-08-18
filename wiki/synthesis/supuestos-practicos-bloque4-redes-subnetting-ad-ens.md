---
title: "Supuesto Práctico Oficial TAI: Redes, Subnetting VLSM, Active Directory y Seguridad ENS (Bloque IV)"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-4
  - redes
  - subnetting
  - active-directory
  - ens
  - windows-server
sources:
  - "raw/sources/bloque4-tema02.md"
  - "raw/sources/bloque4-tema04.md"
  - "raw/sources/bloque4-tema07.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Supuesto Práctico Bloque 4 TAI"
  - "Caso Práctico Redes y Sistemas TAI"
---

# 🔴 Supuesto Práctico Oficial TAI: Redes, Subnetting VLSM, Active Directory y ENS

Guía integral de resolución de supuestos prácticos para la segunda parte del examen de Técnicos Auxiliares de Informática (TAI) del Estado, integrando diseño de red IP, servicios de directorio y cumplimiento del Esquema Nacional de Seguridad (RD 311/2022).

---

## 📋 Enunciado del Caso Práctico

Un Organismo Público Estatal dispone del direccionamiento privado `10.20.0.0/22` asignado por la Red SARA para interconectar su sede central y tres delegaciones provinciales. Se requiere diseñar la arquitectura técnica y de seguridad con los siguientes requerimientos:

### Requerimientos de Red (VLSM):
1. **Sede Central (Servidores y CPD)**: Requiere soporte para un mínimo de **480 hosts**.
2. **Delegación A**: Requiere soporte para un mínimo de **120 hosts**.
3. **Delegación B**: Requiere soporte para un mínimo de **60 hosts**.
4. **Delegación C**: Requiere soporte para un mínimo de **28 hosts**.
5. **Enlaces WAN Punto a Punto**: 3 enlaces punto a punto entre la Sede Central y cada una de las 3 delegaciones (2 hosts por enlace).

### Requerimientos de Sistemas y Directorio Activo (AD DS):
- Configuración de un dominio `organismo.age.es` en Windows Server 2022.
- Se debe implementar una directiva de grupo (GPO) que bloquee el uso de dispositivos de almacenamiento USB a los usuarios del departamento administrativo y fuerce el bloqueo de pantalla tras 10 minutos de inactividad.

### Requerimientos de Seguridad ENS (RD 311/2022):
- El sistema gestiona datos de carácter personal y expedientes sancionadores. La pérdida de confidencialidad o integridad causaría un perjuicio grave al organismo. Determinar la categoría del sistema y las medidas de seguridad preceptivas.

---

## 🛠️ Resolución Técnica Paso a Paso

---

### 1. Diseño del Plan de Direccionamiento IPv4 mediante VLSM

El bloque base disponible es `10.20.0.0/22` ($2^{32-22} = 2^{10} = 1024$ direcciones IP totales, desde `10.20.0.0` hasta `10.20.3.255`).

Ordenamos las subredes de **mayor a menor** número de hosts requeridos:

| Subred | Hosts Requeridos | Bits Host ($h$) | Tamaño Total ($2^h$) | Prefijo | Máscara de Red | Dirección de Red | Rango IPs Útiles | Dirección Broadcast |
|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---|
| **1. Sede Central** | 480 | 9 ($2^9=512$) | 512 | `/23` | `255.255.254.0` | `10.20.0.0` | `10.20.0.1` - `10.20.1.254` | `10.20.1.255` |
| **2. Delegación A** | 120 | 7 ($2^7=128$) | 128 | `/25` | `255.255.255.128` | `10.20.2.0` | `10.20.2.1` - `10.20.2.126` | `10.20.2.127` |
| **3. Delegación B** | 60 | 6 ($2^6=64$) | 64 | `/26` | `255.255.255.192` | `10.20.2.128` | `10.20.2.129` - `10.20.2.190` | `10.20.2.191` |
| **4. Delegación C** | 28 | 5 ($2^5=32$) | 32 | `/27` | `255.255.255.224` | `10.20.2.192` | `10.20.2.193` - `10.20.2.222` | `10.20.2.223` |
| **5. Enlace WAN 1** | 2 | 2 ($2^2=4$) | 4 | `/30` | `255.255.255.252` | `10.20.2.224` | `10.20.2.225` - `10.20.2.226` | `10.20.2.227` |
| **6. Enlace WAN 2** | 2 | 2 ($2^2=4$) | 4 | `/30` | `255.255.255.252` | `10.20.2.228` | `10.20.2.229` - `10.20.2.230` | `10.20.2.231` |
| **7. Enlace WAN 3** | 2 | 2 ($2^2=4$) | 4 | `/30` | `255.255.255.252` | `10.20.2.232` | `10.20.2.233` - `10.20.2.234` | `10.20.2.235` |

> [!tip] 💡 Espacio Libre de Crecimiento
> El bloque `10.20.3.0/24` (256 direcciones) queda completamente libre para futuras ampliaciones o redes de contingencia.

---

### 2. Configuración de Active Directory y GPOs

#### Estructura de Unidades Organizativas (OUs):
```
organismo.age.es (Dominio)
└── OU_Organismo
    ├── OU_Servidores
    ├── OU_Direccion
    └── OU_Administracion
        ├── Usuarios
        └── Equipos
```

#### Configuración de la GPO `GPO_Seguridad_Puestos`:
1. **Bloqueo de USBs**:
   - Ruta: `Configuración del equipo` $\rightarrow$ `Directivas` $\rightarrow$ `Plantillas administrativas` $\rightarrow$ `Sistema` $\rightarrow$ `Acceso de almacenamiento extraíble`.
   - Directiva: **"Todas las clases de almacenamiento extraíble: denegar todo acceso"** $\rightarrow$ `Habilitada`.
2. **Bloqueo por Inactividad (10 minutos = 600 segundos)**:
   - Ruta: `Configuración de usuario` $\rightarrow$ `Plantillas administrativas` $\rightarrow$ `Panel de control` $\rightarrow$ `Personalización`.
   - Directivas:
     - *"Habilitar protector de pantalla"*: `Habilitada`.
     - *"Proteger el protector de pantalla mediante contraseña"*: `Habilitada`.
     - *"Tiempo de espera del protector de pantalla"*: **`600`** segundos.

---

### 3. Cumplimiento del Esquema Nacional de Seguridad (ENS - RD 311/2022)

#### A. Determinación del Nivel de las 5 Dimensiones de Seguridad (DADIT):
- **Disponibilidad (D)**: Nivel **MEDIO** (indisponibilidad de horas tolerable pero con impacto grave en plazos administrativos).
- **Autenticidad (A)**: Nivel **ALTO** (expedientes con firma electrónica reconocida y trámites formales).
- **Integridad (I)**: Nivel **ALTO** (expedientes sancionadores cuya alteración viciaría de nulidad los procedimientos).
- **Confidencialidad (C)**: Nivel **ALTO** (datos de infracciones, sanciones y datos personales de especial protección).
- **Trazabilidad (T)**: Nivel **ALTO** (registro obligatorio de accesos y auditoría de firmas según NTI).

#### B. Categoría Global del Sistema:
$$\text{Categoría Global} = \max(D, A, I, C, T) = \mathbf{ALTA}$$

#### C. Medidas Obligatorias Destacadas del Anexo II del RD 311/2022:
1. **[op.acc.4] Identificación y Autenticación**: Doble factor de autenticación (**MFA**) preceptivo para todos los accesos de administradores y usuarios con acceso a datos de nivel Alto.
2. **[op.exp.8] Registro de Actividad**: Registros de auditoría protegidos contra modificación, con sincronización horaria mediante servidor NTP de estrato seguro y retención mínima de **1 año**.
3. **[mp.info.4] Cifrado de Información**: Cifrado obligatorio de datos en tránsito (**TLS 1.3 / IPsec**) y de datos en reposo (**AES-256**) con claves custodiadas en dispositivos HSM (*Hardware Security Module*).
4. **[org.2] Auditoría de Seguridad**: Auditoría formal ordinaria bianual por entidad certificadora acreditada por ENAC y el CCN.
