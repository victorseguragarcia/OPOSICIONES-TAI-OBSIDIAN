---
title: "Test de Autoevaluación: Bloque 4 - Tema 05 (Almacenamiento, RAID, CPD TIER y Backup)"
type: "test"
target: "wiki/sources/bloque4-tema05.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-4
  - raid
  - cpd
  - tier
  - backup
  - rpo-rto
sources:
  - "raw/sources/bloque4-tema05.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test de Autoevaluación: Bloque 4 - Tema 05 (Almacenamiento, RAID, CPD TIER y Backup)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 4 - Tema 05 (Almacenamiento, RAID, CPD TIER y Backup)",
  "questions": [
    {
      "question": "¿Cuántos discos duros como mínimo requiere una matriz RAID 5 y cuántos discos pueden fallar simultáneamente sin pérdida de datos?",
      "options": [
        "Mínimo 2 discos; soporta fallo de 1 disco.",
        "Mínimo 3 discos; soporta fallo de 1 disco.",
        "Mínimo 4 discos; soporta fallo de 2 discos.",
        "Mínimo 5 discos; soporta fallo de 2 discos."
      ],
      "answer": "b",
      "explanation": "RAID 5 requiere mínimo 3 discos, distribuye 1 bloque de paridad por franja y tolera el fallo de 1 disco. Capacidad útil: $(n-1) \times C$."
    },
    {
      "question": "¿Cuál es la principal ventaja de RAID 6 frente a RAID 5?",
      "options": [
        "No requiere cálculo de paridad.",
        "Utiliza doble paridad distribuida y soporta el fallo simultáneo de hasta 2 discos sin pérdida de datos (requiere mínimo 4 discos).",
        "Ofrece el doble de velocidad de escritura que RAID 0.",
        "No consume espacio para paridad."
      ],
      "answer": "b",
      "explanation": "RAID 6 usa doble paridad (código Reed-Solomon), requiere mínimo 4 discos y tolera la caída simultánea de 2 discos."
    },
    {
      "question": "En la clasificación de Centros de Proceso de Datos (CPD) de Uptime Institute, ¿qué nivel TIER garantiza una disponibilidad del 99,995% con tolerancia a fallos y mantenimiento simultáneo sin interrupción de servicio?",
      "options": [
        "TIER I",
        "TIER II",
        "TIER III",
        "TIER IV"
      ],
      "answer": "d",
      "explanation": "TIER IV exige tolerancia a fallos con componentes y rutas $2(N+1)$ y $99,995\\%$ de disponibilidad ($< 26,3\text{ min/año}$ de parada)."
    },
    {
      "question": "En un Plan de Recuperación ante Desastres (DRP), ¿qué métrica define el tiempo máximo tolerable transcurrido desde el último punto de copia de respaldo que determina la cantidad de datos que una organización puede permitirse perder?",
      "options": [
        "RTO (Recovery Time Objective).",
        "RPO (Recovery Point Objective).",
        "MTBF (Mean Time Between Failures).",
        "MTTR (Mean Time To Repair)."
      ],
      "answer": "b",
      "explanation": "**RPO** mide la pérdida máxima de datos admisible en tiempo; **RTO** mide el tiempo necesario para recuperar el servicio tras el desastre."
    },
    {
      "question": "¿Qué tipo de copia de seguridad (backup) respalda únicamente los archivos que han sido creados o modificados desde la ÚLTIMA copia de cualquier tipo, desactivando el bit de modificado/archivo?",
      "options": [
        "Copia Completa (*Full*).",
        "Copia Incremental.",
        "Copia Diferencial.",
        "Copia Espejo (*Mirror*)."
      ],
      "answer": "b",
      "explanation": "Backup Incremental respalda cambios desde el último backup (completo o incremental) y limpia el bit de archivo."
    }
  ]
}
```
