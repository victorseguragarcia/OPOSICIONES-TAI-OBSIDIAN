---
title: "Medios de Transmisión Guiados y No Guiados"
type: "concept"
tags:
  - transmission-media
  - fiber-optics
  - twisted-pair
  - cabling
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Medios de Transmisión"
  - "Transmission Media"
---

# Medios de Transmisión Guiados y No Guiados

La capa física de comunicaciones utiliza medios guiados (cables de cobre y fibras ópticas) y no guiados (ondas electromagnéticas en el espacio libre) para transportar señales entre emisor y receptor.

---

## 🏛️ Medios Guiados: Par Trenzado vs Fibra Óptica

| Característica | Par Trenzado de Cobre (UTP/STP) | Fibra Óptica (Monomodo / Multimodo) |
|----------------|---------------------------------|--------------------------------------|
| **Medio Físico** | Conductores de cobre aislados y trenzados | Hilos de sílice/vidrio ultrapuro |
| **Señal** | Impulsos eléctricos de voltaje | Pulsos de luz (reflexión interna total) |
| **Inmunidad EMI** | Vulnerable a ruido electromagnético | **100% Inmune a interferencias EMI/RFI** |
| **Atenuación** | Alta con la distancia | Extremadamente baja |
| **Distancia Máxima Estándar** | **100 metros** en canal estructurado | Cientos de metros (MMF) a **>40 km** (SMF) |
| **Seguridad Física** | Fácilmente interceptable | Muy difícil de pinchar sin ser detectado |

---

## 🧩 Categorías de Cable y Cableado Estructurado

- **Normas**: **ISO/IEC 11801** y **ANSI/TIA/EIA-568**.
- **Canal Horizontal**: Máximo **90 metros** de cable permanente + **10 metros** de latiguillos = **100 metros totales**.
- **Categorías de Cobre**:
  - **Cat 5e**: 100 MHz $ightarrow$ 1000BASE-T (1 Gbps a 100 m).
  - **Cat 6**: 250 MHz $ightarrow$ 1000BASE-T (100 m) / 10GBASE-T (55 m).
  - **Cat 6A**: **500 MHz** $ightarrow$ **10GBASE-T (10 Gbps a 100 m)**.
  - **Cat 8**: 2000 MHz (2 GHz) $ightarrow$ 25G/40GBASE-T (hasta 30 m).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Longitud Canal Horizontal | **100 metros máximo** (90 m fijo + 10 m latiguillos) |
| Longitudes de Onda Fibra Monomodo | **1310 nm y 1550 nm** (Láser, núcleo ~9 µm) |
| Longitudes de Onda Fibra Multimodo | **850 nm y 1300 nm** (LED/VCSEL, núcleo 50/62.5 µm) |
| Conectores de Fibra Óptica | **LC, SC, ST, FC, MPO** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Entidad: [[wiki/entities/ethernet-and-ieee-standards|Estándares Ethernet]]
