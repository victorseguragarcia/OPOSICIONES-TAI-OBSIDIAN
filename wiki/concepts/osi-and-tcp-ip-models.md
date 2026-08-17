---
title: "Modelos Arquitectónicos ISO-OSI y TCP-IP"
type: "concept"
tags:
  - osi-model
  - tcp-ip
  - networking-models
  - encapsulation
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelos OSI y TCP/IP"
  - "OSI vs TCP/IP"
---

# Modelos Arquitectónicos ISO-OSI y TCP-IP

Los modelos arquitectónicos estratificados proporcionan un marco modular y estandarizado para el diseño e interoperabilidad de redes de comunicación.

---

## 🏛️ Mapeo y Comparativa: 7 Capas OSI vs 4 Capas TCP/IP

```
    Modelo OSI (ISO 7498-1)                Modelo TCP/IP (RFC 1122)
┌───────────────────────────────┐        ┌───────────────────────────────┐
│ 7. Aplicación (Application)   │        │                               │
├───────────────────────────────┤        │ 4. Aplicación (Application)   │
│ 6. Presentación (Presentation)│  ───►  │    (HTTP, DNS, SMTP, SSH)     │
├───────────────────────────────┤        │                               │
│ 5. Sesión (Session)           │        │                               │
├───────────────────────────────┤        ├───────────────────────────────┤
│ 4. Transporte (Transport)     │  ───►  │ 3. Transporte (TCP, UDP)      │
├───────────────────────────────┤        ├───────────────────────────────┤
│ 3. Red (Network)              │  ───►  │ 2. Internet (IPv4, IPv6, ICMP)│
├───────────────────────────────┤        ├───────────────────────────────┤
│ 2. Enlace (Data Link)         │        │ 1. Acceso a la Red            │
├───────────────────────────────┤  ───►  │    (Network Access)           │
│ 1. Física (Physical)          │        │    (Ethernet, Wi-Fi, PPP)     │
└───────────────────────────────┘        └───────────────────────────────┘
```

---

## 🧩 Proceso de Encapsulación de Datos

A medida que los datos descienden por las capas del emisor, cada nivel añade su propia cabecera de control (**PCI - Protocol Control Information**):
1. **Capa de Aplicación**: Genera el mensaje o flujo de datos original.
2. **Capa de Transporte**: Añade cabecera TCP o UDP (puertos) $
ightarrow$ **Segmento** (TCP) o **Datagrama** (UDP).
3. **Capa de Red**: Añade cabecera IP (direcciones IP origen/destino) $
ightarrow$ **Paquete** o **Datagrama IP**.
4. **Capa de Enlace**: Añade cabecera MAC y cola de comprobación (**FCS / CRC-32**) $
ightarrow$ **Trama (Frame)**.
5. **Capa Física**: Convierte la trama en una secuencia de señales binarias $
ightarrow$ **Bits**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Nivel OSI | PDU | Funcionalidad Clave |
|-----------|-----|---------------------|
| Capa 7 (Aplicación) | Datos | Interfaz de servicios de red con el usuario |
| Capa 6 (Presentación) | Datos | Sintaxis, compresión y cifrado (ASN.1, MIME) |
| Capa 5 (Sesión) | Datos | Sincronización y diálogo de sesión (RPC) |
| Capa 4 (Transporte) | **Segmento** | Comunicación extremo a extremo y puertos |
| Capa 3 (Red) | **Paquete** | Direccionamiento lógico y enrutamiento global |
| Capa 2 (Enlace) | **Trama** | Direccionamiento físico MAC y detección CRC |
| Capa 1 (Física) | **Bit** | Transmisión eléctrica/óptica sobre el medio |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/osi-vs-tcpip-model-comparison|Comparativa: Modelo ISO-OSI frente a TCP-IP]]
