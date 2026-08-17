---
title: "Arquitecturas de Microservicios y Middleware"
type: "concept"
tags:
  - microservices
  - middleware
  - api
  - software-architecture
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Microservicios"
  - "Middleware"
  - "Message Brokers"
---

# Arquitecturas de Microservicios y Middleware

Estrategias de descomposición de sistemas monolíticos en servicios independientes, desacoplados y comunicados a través de redes.

## Patrones de Microservicios
- **API Gateway**: Punto de entrada único que gestiona enrutamiento, autenticación, rate limiting y balanceo hacia los microservicios internos.
- **Comunicación Asíncrona (Message Brokers)**: Desacoplamiento temporal mediante colas y tópicos pub/sub (ej: RabbitMQ, Apache Kafka).
- **Service Mesh**: Capa de infraestructura dedicada para gestionar la comunicación servicio a servicio, observabilidad y mTLS (ej: Istio, Linkerd).

## Capa Middleware
Software que conecta componentes dispares (servidores de aplicaciones web como Apache Tomcat, Nginx, WildFly, brokers de mensajería y drivers de integración).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Orquestación: [[wiki/entities/kubernetes|Kubernetes y Orquestación]]

