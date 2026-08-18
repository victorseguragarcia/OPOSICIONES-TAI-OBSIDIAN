---
title: "Fibra Óptica, Ventanas de Transmisión y Redes GPON/FTTH"
type: "entity"
tags:
  - fiber-optics
  - gpon
  - ftth
  - transmission-media
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Fibra Óptica"
  - "GPON y FTTH"
---

# Fibra Óptica, Ventanas de Transmisión y Redes GPON/FTTH

La **fibra óptica** es el medio de transmisión guiado por excelencia para redes troncales y de acceso de alta velocidad gracias a su inmunidad total a interferencias electromagnéticas y su ancho de banda prácticamente ilimitado.

---

## 🏛️ Fibra Monomodo (SMF) vs Multimodo (MMF)

| Parámetro | Fibra Multimodo (MMF) | Fibra Monomodo (SMF) |
|-----------|-----------------------|----------------------|
| **Diámetro del Núcleo** | **50 µm** o **62.5 µm** (Cubierta: 125 µm) | **~9 µm** (Cubierta: 125 µm) |
| **Propagación de Luz** | Múltiples rayos rebotan en diferentes modos | **Un solo rayo directo** sin dispersión modal |
| **Fuente de Luz** | LED o VCSEL | **Láser (Diodo Láser)** |
| **Longitudes de Onda** | **850 nm y 1300 nm** | **1310 nm y 1550 nm** |
| **Alcance Típico** | Hasta 300 - 550 metros | **10 km a >40 km** |
| **Clasificación ISO 11801** | **OM1, OM2, OM3, OM4, OM5** | **OS1 (interior), OS2 (exterior)** |

---

## 🌈 Ventanas de Transmisión en Fibra de Sílice

1. **1ª Ventana (850 nm)**: Utilizada en fibra multimodo con emisores LED/VCSEL económicos (alta atenuación $\sim 2.5 	ext{ dB/km}$).
2. **2ª Ventana (1310 nm)**: Coincide con el punto de **dispersión cromática cero** en fibra monomodo estándar (atenuación $\sim 0.35 	ext{ dB/km}$).
3. **3ª Ventana (1550 nm)**: Coincide con el punto de **mínima atenuación óptica** ($\sim 0.2 	ext{ dB/km}$), ideal para enlaces de larga distancia y amplificadores EDFA.
4. **4ª Ventana (1625 nm / Banda L)**: Empleada para multiplexación densa DWDM y monitorización de fibra en servicio.

---

## 🌐 Redes Ópticas Pasivas: GPON (ITU-T G.984)

- **Arquitectura Punto a Multipunto (P2MP)**:
  - **OLT (Optical Line Terminal)**: Equipo central del operador en la central telefónica.
  - **ODN (Optical Distribution Network)**: Red de fibra con divisores pasivos (*Splitters* ópticos 1:16, 1:32 o 1:64) sin alimentación eléctrica.
  - **ONT / ONU (Optical Network Terminal)**: Equipo terminal en el domicilio del usuario final.
- **Velocidades y Longitudes de Onda GPON**:
  - **Descarga (Downstream - OLT $\rightarrow$ ONT)**: **2.488 Gbps** en longitud de onda **1490 nm** (TDM broadcast cifrado con AES-128).
  - **Subida (Upstream - ONT $\rightarrow$ OLT)**: **1.244 Gbps** en longitud de onda **1310 nm** (TDMA con asignación dinámica de ancho de banda DBA).
  - **Vídeo RF (Opcional)**: **1550 nm**.
- **Evolución XGS-PON (ITU-T G.9807.1)**: 10 Gbps simétricos (1577 nm bajada / 1270 nm subida).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Estándar GPON | **ITU-T G.984** |
| Velocidades GPON | **2.488 Gbps bajada / 1.244 Gbps subida** |
| Longitud de onda Downstream GPON | **1490 nm** (Descarga) |
| Longitud de onda Upstream GPON | **1310 nm** (Subida) |
| Mínima atenuación fibra sílice | **1550 nm (3ª ventana $\sim 0.2 	ext{ dB/km}$)** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Concepto: [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
