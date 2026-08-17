---
title: "Resumen Fuente: Bloque 3 - Tema 04: Arquitecturas Web, Servicios SOAP, RESTful y Microservicios"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema04
  - arquitecturas-web
  - rest
  - soap
  - microservicios
  - apis
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitecturas Web, REST y SOAP"
  - "bloque3-tema04"
---

# Resumen Fuente: Bloque 3 - Tema 04: Arquitecturas Web, Servicios SOAP, RESTful y Microservicios

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema04.md|bloque3-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema examina las arquitecturas distribuidas modernas: el modelo multicapa (*N-Tier*: Presentación, Lógica de Negocio y Persistencia), la comparativa técnica entre servicios web **SOAP** (basado en XML, con Envelope/Header/Body/Fault, descriptores WSDL, UDDI y seguridad WS-Security) y servicios **REST / RESTful** (basado en HTTP, sin estado *Stateless*, con recursos identificados por URIs, representaciones JSON, verbos GET/POST/PUT/PATCH/DELETE y madurez Richardson/HATEOAS), y las arquitecturas de **microservicios** con patrones API Gateway, Service Discovery, Circuit Breaker y mensajería asíncrona con brokers como RabbitMQ y Apache Kafka.

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología / Criterio | SOAP | REST |
|-----------------------|------|------|
| **Naturaleza** | Protocolo formal W3C | Estilo arquitectónico (Roy Fielding) |
| **Formato de Mensaje** | **Exclusivamente XML** | **JSON** (predominante), XML, texto |
| **Descripción de Servicio** | **WSDL** (Web Services Description Language) | OpenAPI / Swagger |
| **Estado de Sesión** | Puede mantener estado | Estrictamente **Sin Estado (Stateless)** |
| **Seguridad Estándar** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Verbos HTTP** | Habitualmente solo POST con payload XML | **GET, POST, PUT, PATCH, DELETE** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios Web RESTful y SOAP]]
- Concepto: [[wiki/concepts/multitier-and-microservices-architectures|Arquitecturas Multicapa y Microservicios]]
- Síntesis: [[wiki/synthesis/rest-vs-soap-comparison-guide|Guía Comparativa REST vs SOAP]]
