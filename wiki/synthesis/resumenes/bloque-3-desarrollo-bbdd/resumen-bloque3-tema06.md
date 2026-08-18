---
title: "Resumen Completo Tema 06 (Bloque 3): Servicios Web y Arquitecturas Orientadas a Servicios (SOAP vs REST)"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-3
  - tema-06
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque3-tema06]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|⬅️ Tema 05]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|Tema 07 ➡️]]

# 🔴 Resumen Completo Tema 06 (Bloque 3): Servicios Web y Arquitecturas Orientadas a Servicios (SOAP vs REST)

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 06**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

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

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque3-tema06|Nota Fuente del Tema 06]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema06-arquitecturas-web-servicios|Test Tema 06]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema05|⬅️ Tema 05]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|Tema 07 ➡️]]
