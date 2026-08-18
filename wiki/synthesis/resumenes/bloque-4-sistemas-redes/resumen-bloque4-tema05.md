---
title: "Resumen Exhaustivo Tema 05 (Bloque 4): Copias de Seguridad, Regla 3-2-1, RPO/RTO y Continuidad de Negocio"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-05
  - sistemas
  - redes
  - seguridad
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema05.md]]"
  - "[[wiki/sources/bloque4-tema05]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|Tema 06 ➡️]]

# 🔴 Resumen Exhaustivo Tema 05 (Bloque 4): Copias de Seguridad, Regla 3-2-1, RPO/RTO y Continuidad de Negocio

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 05**
> Políticas y tipos de copias de seguridad (Completa, Incremental, Diferencial, Sintética), uso del bit de archivo, la Regla 3-2-1 de backup, métricas de recuperación RPO y RTO, disponibilidad MTBF y MTTR, esquemas de rotación (Grandfather-Father-Son) y Planes de Continuidad de Negocio (BCP) y Recuperación ante Desastres (DRP).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Tipos de Copias de Seguridad y Uso del Bit de Modificación (Archive Bit)
- **El Bit de Archivo (Archive Bit / Modified Bit)**: Indicador de metadato en sistemas de ficheros que se pone a `1` cada vez que un archivo es creado o modificado.
- **Tipos de Copia y Comportamiento**:

| Tipo de Backup | ¿Qué Datos Copia? | ¿Limpia el Bit de Archivo? ($A \rightarrow 0$) | Velocidad de Copia | Velocidad y Complejidad de Restauración |
|:---|:---|:---:|:---:|:---|
| **Copia Completa (Full Backup)** | **Todos los archivos seleccionados al 100%**. | **SÍ (Pone bit a 0)** | Más lenta / Mayor espacio | **Máxima rapidez**: Solo se necesita restaurar el último backup completo. |
| **Copia Incremental** | Solo los archivos creados o modificados **desde el ÚLTIMO backup (Completo o Incremental)**. | **SÍ (Pone bit a 0)** | **Muy rápida** / Mínimo espacio | **Más compleja y lenta**: Requiere restaurar el último Completo + **TODOS los incrementales en orden secuencial**. |
| **Copia Diferencial** | Solo los archivos creados o modificados **desde el ÚLTIMO backup COMPLETO**. | ❌ **NO (Mantiene bit en 1)** | Media / Crece cada día | **Rápida**: Requiere restaurar solo el **último Completo + el ÚLTIMO Diferencial**. |

- **La Regla de Oro del Backup: Regla 3-2-1**:
  - **3** copias de los datos (1 original de producción + 2 copias de seguridad).
  - **2** soportes/medios de almacenamiento diferentes (ej. Disco local + Cinta LTO o NAS).
  - **1** copia custodiada **fuera de la sede (Off-site)** o en la nube (inmutable / air-gapped para protección anti-ransomware).
- **Esquema de Rotación GFS (Grandfather-Father-Son)**:
  - *Son (Hijo)*: Backups diarios incrementales/diferenciales.
  - *Father (Padre)*: Backup semanal completo.
  - *Grandfather (Abuelo)*: Backup mensual completo archivado a largo plazo.

### 2. Métricas de Continuidad de Negocio y Recuperación (BCP / DRP)
- **RPO (Recovery Point Objective - Punto Objetivo de Recuperación)**: Cantidad máxima tolerable de **pérdida de datos** medida en tiempo entre el último backup y el desastre (ej. si se hace backup diario a las 00:00 y el fallo ocurre a las 18:00, se pierden 18 horas de datos; si $RPO = 0$, exige replicación síncrona en tiempo real).
- **RTO (Recovery Time Objective - Tiempo Objetivo de Recuperación)**: Tiempo máximo admisible para **restaurar el servicio y volver a estar operativo** tras el desastre.
- **Métricas de Fiabilidad Hardware**:
  - **MTBF (Mean Time Between Failures)**: Tiempo medio entre fallos (mide la fiabilidad del componente).
  - **MTTR (Mean Time To Repair)**: Tiempo medio de reparación/sustitución.
  - $$\text{Disponibilidad } A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 05 (Bloque 4)**
> 1. **Bit de Archivo en Backup Diferencial**: El backup diferencial **NO desactiva ni limpia el bit de archivo** (por eso cada diferencial contiene todos los cambios desde el último completo).
> 2. **Restauración de Copias Incrementales**: Para restaurar hasta el jueves necesitas: **Completo del domingo + Incremental Lunes + Incremental Martes + Incremental Miércoles + Incremental Jueves**.
> 3. **RPO vs RTO**: **RPO mide PÉRDIDA DE DATOS en tiempo**; **RTO mide TIEMPO DE CAÍDA/PARADA del sistema**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **RPO vs RTO**: **RPO $=$ Pérdida de Datos** / **RTO $=$ Tiempo de Recuperación**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema05|Fuente Oficial del Tema 05]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema05|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema05-almacenamiento-cpd-raid|Test Tema 05]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|Tema 06 ➡️]]
