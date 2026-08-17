---
title: "Guía de Identidad Digital, Reglamento eIDAS, Ley 6/2020 y DNI Electrónico (DNIe)"
type: "synthesis"
tags:
  - synthesis
  - firma-electronica
  - eidas
  - ley-6-2020
  - dnie
  - criptografia
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Firma Electrónica y eIDAS"
  - "eIDAS y Ley 6/2020 Guía"
---

# 🔴 Guía de Identidad Digital, Reglamento eIDAS, Ley 6/2020 y DNI Electrónico (DNIe)

Estudio técnico-jurídico del **Reglamento (UE) 910/2014 (eIDAS)**, la **Ley 6/2020** de servicios electrónicos de confianza y el **DNI Electrónico**.

---

## 🏛️ 1. Tipos de Firma Electrónica según el Reglamento eIDAS

```
                                  JERARQUÍA DE FIRMAS ELECTRÓNICAS
                                                 │
          ┌──────────────────────────────────────┼──────────────────────────────────────┐
          ▼                                      ▼                                      ▼
1. FIRMA SIMPLE                        2. FIRMA AVANZADA                      3. FIRMA CUALIFICADA
• Datos en formato electrónico         • Vinculada al firmante de             • Creada mediante un Dispositivo
  asociados a otros datos para           manera única.                          Cualificado de Creación de Firma
  identificar al firmante.             • Permite identificar al firmante.       (QSCD / tarjeta criptográfica).
• Ejemplo: PIN, usuario/password,      • Creada con datos de creación bajo    • Basada en un Certificado Cualificado.
  casilla acepto condiciones.            control exclusivo del firmante.      • **EQUIVALENCIA PLENA A LA FIRMA**
                                       • Detecta cualquier cambio posterior.    **MANUSCRITA EN TODA LA UE**.
```

---

## 📜 2. Novedades de la Ley 6/2020 (LSEC) frente a la derogada Ley 59/2003

- **Derogación**: La Ley 6/2020, de 11 de noviembre, deroga expresamente la Ley 59/2003 de Firma Electrónica para adaptarse al Reglamento eIDAS.
- **Servicios de Confianza Regulados**:
  1. Creación, verificación y validación de firmas y sellos electrónicos.
  2. Creación, verificación y validación de sellos de tiempo electrónicos.
  3. Servicios de entrega electrónica certificada.
  4. Certificados para autenticación de sitios web (SSL/TLS).
  5. Conservación de firmas y sellos electrónicos.
- **Supervisión**: Corresponde al Ministerio para la Transformación Digital y de la Función Pública.

---

## 🪪 3. El DNI Electrónico (DNIe 3.0 / DNI 4.0)

- **Chip Criptográfico**: Almacena dos pares de claves y sus respectivos certificados X.509 v3 expedidos por la Dirección General de la Policía (DGP):
  1. **Certificado de Autenticación**: Garantiza la identidad electrónica del ciudadano ante sistemas telemáticos.
  2. **Certificado de Firma**: Permite la firma cualificada de documentos electrónicos con validez legal manuscrita.
- **Evolución del DNIe**:
  - **DNIe 1.0/2.0**: Contacto físico mediante chip inteligente (*Smart Card* con lector de tarjetas).
  - **DNIe 3.0**: Incorpora tecnología inalámbrica **NFC (Near Field Communication)** según norma ISO/IEC 14443.
  - **DNI 4.0 (DNI Europeo)**: Conforme al Reglamento (UE) 2019/1157, preparado para integración en el futuro *European Digital Identity Wallet*.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/firma-electronica-y-reglamento-eidas|Firma Electrónica y eIDAS]]
- Entidad: [[wiki/entities/dnie-dni-electronico|DNI Electrónico]]
