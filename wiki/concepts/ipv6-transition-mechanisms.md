---
title: "Mecanismos de Transición y Coexistencia de IPv4 a IPv6"
type: "concept"
tags:
  - ipv6
  - ipv4
  - transition
  - tunneling
  - nat64
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Transición IPv6"
  - "IPv6 Transition Mechanisms"
---

# Mecanismos de Transición y Coexistencia de IPv4 a IPv6

Dado que IPv4 e IPv6 son protocolos incompatibles a nivel binario en sus cabeceras, el IETF diseñó tres estrategias principales de transición y coexistencia durante el periodo de migración global.

---

## 🏛️ Las 3 Estrategias de Transición

```
                 Mecanismos de Transición IPv4 / IPv6
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
  1. Doble Pila             2. Túneles               3. Traducción
   (Dual Stack)             (Tunneling)              (Translation)
(IPv4 e IPv6 nativos     (IPv6 encapsulado         (Conversión de
 en la misma interfaz)     dentro de IPv4)          cabeceras IP)
                         • 6in4 / 6to4             • NAT64 + DNS64
                         • Teredo (UDP 3544)       • SIIT
                         • ISATAP / GRE
```

---

## 🧩 Desglose de Tecnologías de Túnel

1. **Doble Pila (Dual Stack - RFC 4213)**:
   - Los nodos ejecutan pilas completas IPv4 e IPv6 simultáneamente en las mismas interfaces.
   - Las aplicaciones eligen qué protocolo usar en base a las respuestas DNS (`AAAA` preferente sobre `A` según RFC 6724 / Happy Eyeballs RFC 8305).
2. **Túneles Configurados Manualmente (6in4 - RFC 4213, Protocolo IP 41)**:
   - Encapsula paquetes IPv6 directamente dentro de paquetes IPv4 usando el protocolo IP número **41**.
3. **6to4 Automático (RFC 3056)**:
   - Asigna automáticamente a cada sitio IPv4 con IP pública `A.B.C.D` el prefijo IPv6 `2002:AABB:CCDD::/48`.
   - Utiliza la dirección Anycast `192.88.99.1` para enrutar hacia relays 6to4.
4. **Teredo (RFC 4380)**:
   - Permite a clientes IPv6 detrás de routers NAT IPv4 atravesar el NAT encapsulando paquetes IPv6 dentro de datagramas **UDP en el puerto 3544**.
   - Prefijo reservado Teredo: **`2001:0000::/32`**.
5. **ISATAP (RFC 5214)**:
   - Conecta hosts IPv6 dentro de una intranet corporativa sobre una red IPv4 interna.

---

## 🔄 Mecanismos de Traducción: NAT64 y DNS64 (RFC 6146 / RFC 6147)

- Permite a clientes que disponen **exclusivamente de IPv6** comunicarse con servidores legacy que solo disponen de IPv4.
- **DNS64**: Si el resolver DNS no encuentra registro `AAAA` pero sí `A`, sintetiza un registro `AAAA` falso combinando el prefijo Well-Known `64:ff9b::/96` con los 32 bits de la IPv4.
- **NAT64**: El router intercepta el tráfico IPv6 dirigido a `64:ff9b::/96`, extrae la dirección IPv4 de destino, traduce la cabecera a IPv4 y la envía con una IP pública del pool NAT64.

---

## 🎯 Datos Clave para Oposiciones TAI

| Mecanismo | Puerto / Protocolo / Prefijo |
|-----------|------------------------------|
| Protocolo IP 6in4 | **Protocolo IP 41** |
| Prefijo 6to4 | **`2002::/16`** (con la IPv4 en hex) |
| Puerto y Prefijo Teredo | **Puerto 3544 UDP** / Prefijo **`2001:0000::/32`** |
| Prefijo Sintetizado NAT64 | **`64:ff9b::/96`** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa Técnica de Direccionamiento: IPv4 vs IPv6]]
