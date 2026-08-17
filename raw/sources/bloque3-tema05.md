---
title: "Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD"
type: "raw-source"
topic: "calidad-pruebas-cicd"
date: "2026-08-17"
---

# Bloque 3 - Tema 05: Calidad del Software, Niveles y Tipos de Pruebas (Caja Blanca / Negra), Complejidad de McCabe e Integración Continua (CI/CD)

## 1. Niveles y Tipos de Pruebas de Software
- **Niveles de Pruebas**:
  1. **Pruebas Unitarias**: Verifican el funcionamiento aislado de componentes individuales (métodos, clases). Automatizadas con frameworks como JUnit o NUnit.
  2. **Pruebas de Integración**: Verifican la interacción correcta y el intercambio de datos entre múltiples módulos o con servicios externos y bases de datos.
  3. **Pruebas de Sistema**: Evalúan el sistema completo e integrado respecto a los requisitos funcionales y no funcionales especificados.
  4. **Pruebas de Aceptación**: Realizadas por el usuario final o cliente (*Alpha testing* en entorno de desarrollo, *Beta testing* en entorno real) para validar que el software cumple las expectativas de negocio.
- **Otros Tipos de Pruebas**:
  - **Pruebas de Regresión**: Verifican que los cambios recientes o correcciones de bugs no hayan introducido nuevos errores en funcionalidades existentes.
  - **Pruebas No Funcionales**: Rendimiento, Carga, Estrés, Seguridad y Accesibilidad.

## 2. Técnicas de Diseño de Casos de Prueba

### 1. Pruebas de Caja Blanca (Estructurales)
Basadas en el conocimiento de la estructura interna y el código fuente del programa.
- **Criterios de Cobertura**:
  - *Cobertura de Sentencias / Instrucciones*: Garantiza que cada línea de código se ejecute al menos una vez.
  - *Cobertura de Decisiones / Ramas*: Garantiza que cada rama condicional (True y False) se evalúe al menos una vez.
  - *Cobertura de Condiciones*: Garantiza que cada condición booleana individual tome ambos valores.
  - *Cobertura de Caminos*: Garantiza que se ejecuten todos los caminos independientes posibles.
- **Complejidad Ciclomática de McCabe ($V(G)$)**:
  - Métrica de la ingeniería del software que mide la complejidad lógica de un programa y determina el **número mínimo de casos de prueba necesarios para garantizar la cobertura de todos los caminos básicos independientes**:
  $$V(G) = E - N + 2P$$
  Donde:
  - $E$ = Número de aristas (*Edges*) del grafo de flujo de control.
  - $N$ = Número de nodos (*Nodes*) del grafo.
  - $P$ = Número de componentes conexos ($P=1$ para un único programa/método).
  - *Fórmula Alternativa*: $V(G) = 	ext{Número de Nodos Predicado (Decisiones)} + 1$.
  - *Fórmula por Regiones*: $V(G) = 	ext{Número de Regiones del Grafo Plano}$.

### 2. Pruebas de Caja Negra (Funcionales)
Basadas en la especificación de requisitos sin conocer el código interno.
- **Particiones o Clases de Equivalencia**: Divide el dominio de entrada en subconjuntos de datos equivalentes (válidos e inválidos), seleccionando un caso representativo de cada clase.
- **Análisis de Valores Límite (BVA - Boundary Value Analysis)**: Se diseñan casos de prueba en los bordes extremos de las particiones (valor mínimo, justo por debajo del mínimo, justo por encima, valor máximo, justo por encima del máximo). Los errores suelen concentrarse en los límites de los rangos.
- **Tablas de Decisión** y **Pruebas de Transición de Estados**.

## 3. Integración y Despliegue Continuo (CI/CD) y Análisis Estático
- **Integración Continua (CI)**: Práctica de fusionar los cambios de código frecuentemente en una rama compartida, ejecutando automáticamente la compilación y la batería de pruebas unitarias/integración en cada commit.
- **Entrega Continua (Continuous Delivery)**: Automatiza el empaquetado del software para que cualquier versión probada esté lista para ser desplegada en producción con un clic manual.
- **Despliegue Continuo (Continuous Deployment)**: Automatiza el paso a producción de forma completamente desatendida tras superar con éxito todas las pruebas del pipeline.
- **Herramientas**: Jenkins, GitLab CI, GitHub Actions, Azure DevOps, ArgoCD.
- **Análisis Estático de Código (SonarQube)**: Inspección automatizada del código fuente sin ejecutarlo para detectar bugs, vulnerabilidades de seguridad (*Security Hotspots*), olores de código (*Code Smells*), duplicidades y calcular la **Deuda Técnica** (*Technical Debt*) frente a **Quality Gates**.
