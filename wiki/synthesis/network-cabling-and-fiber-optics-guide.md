---
title: "Guía de Cableado Estructurado, Par Trenzado y Fibra Óptica"
type: "synthesis"
tags:
  - synthesis
  - cabling
  - twisted-pair
  - fiber-optics
  - rj45
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Cableado y Fibra"
  - "Network Cabling Guide"
---

# Guía de Cableado Estructurado, Par Trenzado y Fibra Óptica

Manual técnico de esquemas de conexión RJ-45, categorías de cobre, tipos de fibra óptica y normas internacionales de cableado.

---

## 🏛️ Esquemas de Conexión RJ-45 (TIA/EIA-568A y TIA/EIA-568B)

```
        Pin 1   Pin 2   Pin 3   Pin 4   Pin 5   Pin 6   Pin 7   Pin 8
T568A:  Bl/Ver  Verde   Bl/Nar  Azul    Bl/Azul Naranja Bl/Mar  Marrón
T568B:  Bl/Nar  Naranja Bl/Ver  Azul    Bl/Azul Verde   Bl/Mar  Marrón
```

- **Cable Directo (*Straight-Through*)**: Mismo estándar en ambos extremos (T568A-T568A o T568B-T568B). Conecta dispositivos de distinta capa (ej. PC a Switch, Switch a Router).
- **Cable Cruzado (*Crossover*)**: T568A en un extremo y T568B en el otro (cruza los pares 1-2 con 3-6). Conecta dispositivos de la misma capa (ej. PC a PC, Switch a Switch, Router a Router).
- **Auto MDI/MDIX**: Característica de los switches modernos que detecta y conmuta automáticamente los pares de transmisión/recepción, haciendo indistinto el uso de cable directo o cruzado.

---

## 🧩 Categorías de Par Trenzado de Cobre

| Categoría | Ancho de Banda | Aplicación Principal | Distancia Máxima |
|-----------|----------------|----------------------|------------------|
| **Cat 5e** | **100 MHz** | 1000BASE-T (Gigabit Ethernet) | **100 m** |
| **Cat 6** | **250 MHz** | 1000BASE-T (100 m) / 10GBASE-T (hasta 55 m) | 100 m / 55 m |
| **Cat 6A** | **500 MHz** | **10GBASE-T (10 Gigabit Ethernet)** | **100 m** |
| **Cat 7** | **600 MHz** | 10GBASE-T (conectores GG45/TERA blindados) | 100 m |
| **Cat 7A** | **1000 MHz (1 GHz)** | 10GBASE-T y servicios de banda ancha | 100 m |
| **Cat 8 (8.1/8.2)** | **2000 MHz (2 GHz)** | **25GBASE-T y 40GBASE-T** (Centros de Datos) | **30 m** (Canal de 24 m + 6 m) |

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Longitud Máxima Canal Horizontal | **100 metros** (90 m permanente + 10 m latiguillos) |
| Diferencia T568A vs T568B | Intercambian los pines del **par Verde (1-2 en A, 3-6 en B)** y **par Naranja (3-6 en A, 1-2 en B)** |
| Pines Activos 100BASE-TX (Fast Ethernet) | **Pines 1, 2 (TX) y 3, 6 (RX)** (2 pares) |
| Pines Activos 1000BASE-T (Gigabit) | **Los 8 pines / 4 pares transmiten y reciben simultáneamente** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Entidad: [[wiki/entities/optical-fiber-and-gpon|Fibra Óptica y GPON]]
