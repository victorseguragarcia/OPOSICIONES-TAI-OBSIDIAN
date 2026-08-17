---
title: "Guía Comparativa de Servicios Web: REST vs SOAP"
type: "synthesis"
tags:
  - synthesis
  - comparison
  - rest
  - soap
  - apis
sources:
  - "raw/sources/bloque3-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Comparativa REST vs SOAP"
  - "REST vs SOAP Guía"
---

# Guía Comparativa de Servicios Web: REST vs SOAP

Matriz de contraste técnico entre servicios web tradicionales SOAP y APIs RESTful.

---

## 🏛️ Matriz Técnica Comparativa

| Criterio | SOAP | REST |
|----------|------|------|
| **Tipo** | Protocolo formal W3C | Estilo arquitectónico (Roy Fielding) |
| **Formato de Carga Útil** | **Exclusivamente XML** | **JSON** (predominante), XML, YAML, HTML |
| **Contrato Formal** | **WSDL** (XML) | OpenAPI / Swagger |
| **Transporte** | HTTP, SMTP, TCP, JMS | Exclusivamente sobre **HTTP / HTTPS** |
| **Manejo de Estado** | Opcionalmente con estado (*Stateful*) | Estrictamente **Sin Estado (*Stateless*)** |
| **Seguridad** | **WS-Security** (a nivel de mensaje) | **HTTPS/TLS + OAuth 2.0 / JWT** |
| **Rendimiento y Sobrecarga** | Pesado (envoltorios XML grandes) | Ligero y optimizado para web y móviles |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema04|Resumen Bloque 3 - Tema 04]]
- Entidad: [[wiki/entities/rest-and-soap-web-services|Servicios REST y SOAP]]
