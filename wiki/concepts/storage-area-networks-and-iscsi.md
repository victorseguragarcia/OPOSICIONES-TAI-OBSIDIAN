---
title: "Redes de Área de Almacenamiento (SAN) e iSCSI"
type: "concept"
tags:
  - san
  - iscsi
  - fibre-channel
  - storage
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "SAN e iSCSI"
  - "Storage Area Networks"
---

# Redes de Área de Almacenamiento (SAN) e iSCSI

Una **SAN (Storage Area Network)** es una red dedicada y de alto rendimiento que conecta servidores (iniciadores) con matrices de almacenamiento compartido (destinos o *targets*) a nivel de bloque.

---

## 🏛️ Tecnologías de Transporte en SAN

| Parámetro | Fibre Channel (FC) | iSCSI (Internet SCSI) | FCoE (FC over Ethernet) |
|-----------|--------------------|-----------------------|-------------------------|
| **Capa de Red** | Protocolo propietario FC sobre fibra dedicada | **TCP/IP estándar** (Ethernet) | Tramas Ethernet sin pérdida (PFC 802.1Qbb) |
| **Puerto Estándar** | Canales ópticos dedicados (FC-SW) | **3260 TCP** | EtherType `0x8906` |
| **Velocidades Típicas** | 8G, 16G, 32G, 64G FC | 1G, 10G, 25G, 100G Ethernet | 10G, 40G, 100G Ethernet |
| **Adaptador Host** | **HBA (Host Bus Adapter)** dedicado | Tarjeta de red NIC estándar o HBA iSCSI con TOEs | CNA (Converged Network Adapter) |
| **Coste e Infraestructura** | Elevado (switches y cableado FC dedicados) | **Económico** (reutiliza switches Ethernet existentes) | Medio-Alto |

---

## 🧩 Conceptos Clave de Administración SAN

- **Iniciador (*Initiator*)**: Servidor que solicita operaciones de lectura/escritura a nivel de bloque.
- **Destino (*Target*)**: Dispositivo o matriz de almacenamiento que procesa las peticiones.
- **LUN (Logical Unit Number)**: Identificador lógico asignado a una porción de almacenamiento virtualizada dentro de la matriz.
- **LUN Masking**: Restricción de seguridad configurada en la matriz para que una LUN específica solo sea visible para ciertos iniciadores autorizados.
- **Zoning (en Fibre Channel)**: Segmentación de la estructura del conmutador (*Switch Fabric*) para aislar iniciadores y targets en zonas seguras (Hard Zoning por puerto físico o Soft Zoning por WWPN).
- **Direccionamiento iSCSI (IQN - iSCSI Qualified Name)**:
  - Formato RFC 3720: `iqn.yyyy-mm.naming-authority:unique-name` (ej. `iqn.2026-08.es.gob.tai:storage.target01`).
  - Alternativa: **EUI-64** (`eui.0123456789abcdef`).

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Valor Técnico |
|-----------|---------------|
| Puerto Estándar iSCSI | **3260 TCP** (RFC 3720 / 7143) |
| Formato de Nombres iSCSI | **IQN** (*iSCSI Qualified Name*) y **EUI** |
| Nivel de Abstracción SAN | **Bloques de disco crudos** (*Block-Level*) |
| Mecanismos de Aislamiento | **Zoning** (en el switch) + **LUN Masking** (en la matriz) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/raid-storage|Sistemas de Almacenamiento RAID, DAS, NAS y SAN]]
