---
title: "Seguridad en Redes y Defensa Perimetral"
type: "concept"
tags:
  - network-security
  - perimeter-defense
  - dmz
  - defense-in-depth
sources:
  - "raw/sources/bloque4-tema05.md"
  - "raw/sources/bloque4-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Seguridad Perimetral"
  - "Defensa en Profundidad"
---

# Seguridad en Redes y Defensa Perimetral

La **defensa en profundidad (*Defense-in-Depth*)** articula múltiples capas concéntricas de controles de seguridad físicos, de red, de host y de aplicación para proteger los activos de información corporativos.

---

## 🏛️ Arquitecturas Perimetrales y Zonas DMZ

1. **Zona Desmilitarizada (DMZ / Zona Neutra)**:
   - Subred aislada que aloja servidores accesibles públicamente desde Internet (Web, Correo externo, DNS público).
   - **Regla de Oro**: Ninguna conexión iniciada desde la DMZ puede tener acceso directo no filtrado a la red interna confidencial (*LAN Corporativa*).
2. **Topología con Cortafuegos de 3 Patas (Three-Pronged)**:
   - Un solo cortafuegos con 3 interfaces dedicadas: Internet (No confiable), DMZ (Semiconfiable) e Intranet (Confiable).
3. **Topología con Cortafuegos en Cascada (Back-to-Back)**:
   - La DMZ se sitúa entre un cortafuegos perimetral externo y un cortafuegos interno de distinto fabricante, garantizando que el compromiso de un cortafuegos no comprometa automáticamente la red interna.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Regla de Diseño Perimetral |
|----------|----------------------------|
| Ubicación Servidores Web | Siempre en **DMZ** (nunca en la LAN interna directa) |
| Tráfico DMZ $\rightarrow$ LAN | **Estrictamente bloqueado** por defecto (solo respuestas o servicios autenticados) |
| Cortafuegos Back-to-Back | Utiliza **fabricantes distintos** para evitar vulnerabilidades de software compartidas |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema09|Resumen Bloque 4 - Tema 09]]
- Entidad: [[wiki/entities/firewalls-and-vpn|Cortafuegos y VPN]]
- Entidad: [[wiki/entities/siem-and-ids-ips|Sistemas SIEM, IDS e IPS]]
