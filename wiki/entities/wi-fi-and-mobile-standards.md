---
title: "Estándares Wi-Fi (IEEE 802.11) y Tecnologías Móviles (5G NR)"
type: "entity"
tags:
  - wifi
  - 802-11
  - 5g
  - mobile
  - wireless
sources:
  - "raw/sources/bloque4-tema06.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Wi-Fi"
  - "IEEE 802.11"
  - "5G NR"
---

# Estándares Wi-Fi (IEEE 802.11) y Tecnologías Móviles (5G NR)

Las tecnologías de comunicaciones inalámbricas abarcan las redes de área local inalámbricas (**WLAN - IEEE 802.11**) y las redes móviles de última generación (**5G NR**).

---

## 🏛️ Evolución de Estándares Wi-Fi (IEEE 802.11)

| Nombre Comercial | Estándar IEEE | Año | Frecuencias | Velocidad Máxima Teórica | Tecnología Clave |
|------------------|---------------|-----|-------------|--------------------------|------------------|
| **Wi-Fi 1** | 802.11b | 1999 | 2.4 GHz | 11 Mbps | DSSS |
| **Wi-Fi 2** | 802.11a | 1999 | 5 GHz | 54 Mbps | OFDM |
| **Wi-Fi 3** | 802.11g | 2003 | 2.4 GHz | 54 Mbps | OFDM |
| **Wi-Fi 4** | 802.11n | 2009 | 2.4 / 5 GHz | 600 Mbps | MIMO (hasta 4x4) |
| **Wi-Fi 5** | 802.11ac | 2013 | 5 GHz | 6.93 Gbps | MU-MIMO, Canales 80/160 MHz, 256-QAM |
| **Wi-Fi 6 / 6E** | 802.11ax | 2019 / 2021 | 2.4 / 5 / **6 GHz** | **9.6 Gbps** | **OFDMA**, 1024-QAM, BSS Coloring, TWT |
| **Wi-Fi 7** | 802.11be | 2024 | 2.4 / 5 / 6 GHz | **46 Gbps** | Canales 320 MHz, 4096-QAM, MLO |

---

## 🧩 Protocolos de Seguridad Wi-Fi

- **WEP**: Cifrado RC4 con claves de 64/128 bits e IVs cortos de 24 bits (completamente vulnerable).
- **WPA**: Incorporó **TKIP** (Temporal Key Integrity Protocol) y comprobación de integridad Michael.
- **WPA2**: Estándar basado en **IEEE 802.11i** con cifrado robusto **AES-CCMP**.
- **WPA3**: Protocolo actual obligatorio. Sustituye el handshake de 4 vías por **SAE (Simultaneous Authentication of Equals)** basado en protocolo Dragonfly (inmune a ataques de diccionario offline). En modo Enterprise utiliza cifrado de **192 bits**.

---

## 📱 Tecnologías Móviles 5G NR (3GPP)

- **Pilares de 5G NR**:
  1. **eMBB (Enhanced Mobile Broadband)**: Alta velocidad de descarga (hasta 10-20 Gbps).
  2. **URLLC (Ultra-Reliable Low-Latency Communications)**: Latencia ultra baja (<1 ms) para vehículos autónomos e industria 4.0.
  3. **mMTC (Massive Machine-Type Communications)**: Conexión simultánea de hasta $10^6$ dispositivos IoT por $	ext{km}^2$.
- **Modos de Despliegue**:
  - **NSA (Non-Standalone)**: Señalización sobre núcleo 4G (EPC) y radio 5G NR.
  - **SA (Standalone)**: Radio 5G NR conectada directamente al nuevo núcleo nativo **5G Core (5GC)**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro | Especificación Técnica |
|-----------|------------------------|
| Wi-Fi 6 Estándar | **IEEE 802.11ax** (OFDMA, 1024-QAM) |
| Banda nueva en Wi-Fi 6E / 7 | **Banda de 6 GHz** |
| Autenticación WPA3 | **SAE** (Simultaneous Authentication of Equals) |
| Latencia objetivo URLLC | **< 1 milisegundo** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema06|Resumen Bloque 4 - Tema 06]]
- Concepto: [[wiki/concepts/transmission-media-and-modes|Medios de Transmisión Guiados y No Guiados]]
