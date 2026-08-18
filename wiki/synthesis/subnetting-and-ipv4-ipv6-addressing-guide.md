---
title: "Guía Práctica de Subnetting, VLSM y Direccionamiento IPv4 e IPv6"
type: "synthesis"
tags:
  - synthesis
  - subnetting
  - vlsm
  - ipv4
  - ipv6
  - cidr
sources:
  - "raw/sources/bloque4-tema07.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Subnetting y VLSM"
  - "Subnetting Guide"
---

# Guía Práctica de Subnetting, VLSM y Direccionamiento IPv4 e IPv6

Manual de cálculo de subredes, máscaras de longitud variable (**VLSM**), notación CIDR y conversión EUI-64 en IPv6.

---

## 🏛️ Tabla Maestra de Subredes IPv4 (Prefijos /24 a /32)

| Prefijo CIDR | Máscara de Subred Decimal | Hosts Totales ($2^h$) | Hosts Útiles ($2^h - 2$) | Salto / Incremento ($256 - M$) |
|--------------|---------------------------|-----------------------|--------------------------|--------------------------------|
| **/24** | `255.255.255.0` | 256 | **254** | 1 |
| **/25** | `255.255.255.128` | 128 | **126** | 128 |
| **/26** | `255.255.255.192` | 64 | **62** | 64 |
| **/27** | `255.255.255.224` | 32 | **30** | 32 |
| **/28** | `255.255.255.240` | 16 | **14** | 16 |
| **/29** | `255.255.255.248` | 8 | **6** | 8 |
| **/30** | `255.255.255.252` | 4 | **2** (enlaces punto a punto) | 4 |
| **/31** | `255.255.255.254` | 2 | **2** (RFC 3021 solo en routers) | 2 |
| **/32** | `255.255.255.255` | 1 | **1** (host individual / loopback)| 1 |

---

## 🧮 Metodología de Cálculo VLSM Paso a Paso

Para dividir una red `192.168.1.0/24` en subredes de distinto tamaño:
1. **Ordenar los requisitos de mayor a menor número de hosts**.
2. **Calcular los bits de host ($h$)** necesarios para cada subred usando la fórmula $2^h - 2 \ge \text{Hosts requeridos}$.
3. **Asignar las subredes correlativamente** calculando la dirección de red, primer host útil, último host útil y broadcast.

*Ejemplo*:
- Subred A (100 hosts): $2^7 - 2 = 126 \ge 100 
ightarrow h=7 $\rightarrow$ Máscara $/25$ (`255.255.255.128`).
  - Red: `192.168.1.0/25` (Rango útil: `192.168.1.1` a `192.168.1.126`, Broadcast: `192.168.1.127`).
- Subred B (50 hosts): $2^6 - 2 = 62 \ge 50 
ightarrow h=6 $\rightarrow$ Máscara $/26$ (`255.255.255.192`).
  - Red: `192.168.1.128/26` (Rango útil: `192.168.1.129` a `192.168.1.190`, Broadcast: `192.168.1.191`).
- Subred C (20 hosts): $2^5 - 2 = 30 \ge 20 
ightarrow h=5 $\rightarrow$ Máscara $/27$ (`255.255.255.224`).
  - Red: `192.168.1.192/27` (Rango útil: `192.168.1.193` a `192.168.1.222`, Broadcast: `192.168.1.223`).

---

## 🌐 Generación de Interface ID EUI-64 en IPv6

Para transformar una dirección MAC `00:1A:2B:3C:4D:5E` en un Interface ID de 64 bits para SLAAC:
1. Dividir la MAC en dos mitades de 24 bits: `00:1A:2B` y `3C:4D:5E`.
2. Insertar `FF:FE` en el centro: `00:1A:2B:FF:FE:3C:4D:5E`.
3. Invertir el **7º bit del primer octeto** (bit U/L - Universal/Local):
   - `00` en binario: `00000000` $\rightarrow$ invirtiendo el 7º bit: `00000010` = `02`.
4. Resultado EUI-64: `021A:2BFF:FE3C:4D5E`.
5. Dirección Link-Local generada: `fe80::21a:2bff:fe3c:4d5e/64`.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Fórmula / Regla |
|-----------|-----------------|
| Hosts Útiles IPv4 | $2^{\text{bits de host}} - 2$ |
| Número de Subredes | $2^{\text{bits robados a la red}}$ |
| Enlace Punto a Punto Estándar | **/30** (2 hosts útiles) |
| Conversión EUI-64 | Inserta `FFFE` en medio e invierte el **bit 7** del primer byte |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema07|Resumen Bloque 4 - Tema 07]]
- Entidad: [[wiki/entities/ipv4-and-ipv6|Protocolos de Red: IPv4 e IPv6]]
- Síntesis: [[wiki/synthesis/ipv4-vs-ipv6-comparison|Comparativa IPv4 vs IPv6]]
