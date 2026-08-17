---
title: "Resumen Fuente: Bloque 3 - Tema 06 (UD012113): Arquitecturas Multicapa, Servicios SOAP y RESTful"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema06
  - arquitecturas-sistemas
  - multicapa
  - soap
  - rest
  - apis
sources:
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitecturas Multicapa y Servicios Web"
  - "bloque3-tema06"
---

# Resumen Fuente: Bloque 3 - Tema 06 (UD012113): Arquitecturas Multicapa, Servicios SOAP y RESTful

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema06-arquitecturas-servicios-web.md|bloque3-tema06-arquitecturas-servicios-web.md]] (88 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en las arquitecturas de sistemas distribuidos: modelos Cliente/Servidor (2 capas, 3 capas, N capas, cliente ligero vs cliente pesado), tecnologías de interoperabilidad y servicios web: el estándar **SOAP** (protocolo XML con Envelope, Header, Body, Fault, descriptores **WSDL**, registros **UDDI** y seguridad **WS-Security**) frente al estilo arquitectónico **REST / RESTful** (orientado a recursos, URIs, representaciones JSON, sin estado *Stateless*, métodos HTTP `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, modelo de madurez de Richardson y HATEOAS).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Criterio | SOAP | REST |
|-----------------------|------|------|
| **Formato de Carga Útil** | **Exclusivamente XML** | **JSON** (predominante), XML, texto |
| **Contrato Formal** | **WSDL** (XML) | OpenAPI / Swagger |
| **Estado de Sesión** | Puede mantener estado | Estrictamente **Sin Estado (Stateless)** |
| **Seguridad** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Verbos HTTP** | Habitualmente solo POST con payload XML | **GET, POST, PUT, PATCH, DELETE** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios Web RESTful y SOAP]]
- Concepto: [[wiki/concepts/multitier-and-microservices-architectures|Arquitecturas Multicapa y Microservicios]]
- Síntesis: [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
