---
title: "Microservicios, Arquitecturas Distribuidas y Middleware"
type: "concept"
tags:
  - microservices
  - middleware
  - api-gateway
  - cloud-native
sources:
  - "raw/sources/bloque4-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Microservicios y Middleware"
  - "Microservices Architecture"
---

# Microservicios, Arquitecturas Distribuidas y Middleware

La **arquitectura de microservicios** estructura una aplicación como una colección de servicios autónomos, débilmente acoplados, desplegables independientemente y organizados en torno a capacidades de negocio.

---

## 🏛️ Monolito frente a Microservicios

| Criterio | Arquitectura Monolítica | Arquitectura de Microservicios |
|----------|-------------------------|--------------------------------|
| **Base de Código** | Unificada y fuertemente acoplada | Repositorios o módulos independientes |
| **Despliegue** | Todo-o-nada (*Big Bang*) | Despliegues independientes y continuos (CI/CD) |
| **Escalabilidad** | Escalado vertical o replicación de todo el monolito | Escalado granular de los servicios con mayor carga |
| **Gestión de Datos** | Base de datos relacional compartida | Base de datos por servicio (*Database-per-Service*) |
| **Resiliencia** | Un fallo en un módulo puede tumbar toda la app | Aislamiento de fallos con patrones Circuit Breaker |

---

## 🧩 Patrones de Microservicios y Middleware

- **API Gateway**: Punto único de entrada para clientes que gestiona autenticación, enrutamiento, limitación de tasa (*Rate Limiting*) y terminación SSL.
- **Service Mesh (Malla de Servicios)**: Capa de infraestructura dedicada para la comunicación segura este-oeste entre microservicios (mediante proxies sidecar como Envoy en Istio).
- **Middleware Orientado a Mensajes (MOM)**: Desacopla servicios mediante comunicación asíncrona por colas de mensajes (RabbitMQ, Apache Kafka).

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Componente | Función Principal |
|---------------------|-------------------|
| API Gateway | Punto de entrada, autenticación y enrutamiento perimetral |
| Circuit Breaker | Corta peticiones a servicios caídos para evitar fallos en cascada |
| Service Mesh | Gestión de tráfico, observabilidad y mTLS servicio a servicio |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema03|Resumen Bloque 4 - Tema 03]]
- Entidad: [[wiki/entities/docker-and-containers|Docker y Contenedores]]
- Entidad: [[wiki/entities/kubernetes|Kubernetes]]
