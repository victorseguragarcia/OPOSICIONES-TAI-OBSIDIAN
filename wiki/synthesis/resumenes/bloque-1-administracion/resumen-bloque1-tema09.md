---
title: "Resumen Completo y Profundo Tema 09 (Bloque 1): Protección de Datos Personales (RGPD y LOPDGDD 3/2018)"
type: "synthesis"
tags:
  - resumen
  - resumen-profundo
  - temario-completo
  - bloque-1
  - tema-09
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque1-tema09.md]]"
  - "[[wiki/sources/bloque1-tema09]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-1-administracion/resumen-bloque1-tema08|⬅️ Tema 08]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque1|🏠 Índice Bloque 1]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-1-administracion/resumen-bloque1-tema10|Tema 10 ➡️]]

# 🔴 Resumen Completo y Profundo Tema 09 (Bloque 1): Protección de Datos Personales (RGPD y LOPDGDD 3/2018)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 09**
> Guía completa y exhaustiva que recopila todo el temario oficial, marco legal/normativo, detalles de arquitectura, tablas de datos críticos, protocolos, comandos de consola y casos prácticos.

---

## 🟣 1. Desarrollo Temático Completo e Íntegro

## 1. Marco Normativo de Protección de Datos
- **Reglamento (UE) 2016/679 (RGPD / GDPR)**: Aplicable directamente en toda la Unión Europea desde el **25 de mayo de 2018**.
- **Ley Orgánica 3/2018, de 5 de diciembre (LOPDGDD)**: De Protección de Datos Personales y garantía de los derechos digitales. Adapta el ordenamiento español al RGPD e introduce el Título X dedicado a los Derechos Digitales.

## 2. Principios Fundamentales del Tratamiento de Datos (Art. 5 RGPD)
1. **Licitud, lealtad y transparencia**: Tratado de forma lícita, leal y transparente en relación con el interesado.
2. **Limitación de la finalidad**: Recogidos con fines determinados, explícitos y legítimos, y no tratados ulteriormente de manera incompatible.
3. **Minimización de datos**: Adecuados, pertinentes y limitados a lo necesario en relación con los fines (**"data minimization"**).
4. **Exactitud**: Exactos y actualizados; supresión o rectificación inmediata de datos inexactos.
5. **Limitación del plazo de conservación**: Mantenidos durante no más tiempo del necesario para los fines del tratamiento.
6. **Integridad y confidencialidad**: Tratados garantizando una seguridad adecuada contra el tratamiento no autorizado o ilícito y contra su pérdida, destrucción o daño accidental mediante medidas técnicas u organizativas.
7. **Responsabilidad proactiva (*Accountability*)**: El responsable del tratamiento será responsable del cumplimiento y capaz de demostrarlo.

## 3. Bases de Legitimación del Tratamiento (Art. 6 RGPD)
- Consentimiento explícito del interesado.
- Ejecución de un contrato.
- Cumplimiento de una obligación legal aplicable al responsable.
- Protección de intereses vitales del interesado o de otra persona.
- Cumplimiento de una misión realizada en **interés público o en el ejercicio de poderes públicos**.
- Satisfacción de intereses legítimos del responsable o de un tercero (salvo cuando prevalezcan los derechos fundamentales del interesado, especialmente niños). *Nota*: Las autoridades públicas NO pueden acogerse al interés legítimo en el ejercicio de sus funciones.

## 4. Derechos de los Ciudadanos (Derechos ARCO-POL)
- **Acceso (Art. 15 RGPD)**: Conocer si se tratan sus datos y obtener copia gratuita.
- **Rectificación (Art. 16 RGPD)**: Modificación de datos inexactos o incompletos.
- **Supresión ("Derecho al Olvido" - Art. 17 RGPD)**: Eliminación de datos cuando ya no sean necesarios o se retire el consentimiento.
- **Limitación del Tratamiento (Art. 18 RGPD)**: Marcar los datos para suspender su tratamiento mientras se verifica su exactitud o licitud.
- **Portabilidad (Art. 20 RGPD)**: Recibir los datos en formato estructurado, de uso común y lectura mecánica interoperable (ej. JSON, XML, CSV).
- **Oposición (Art. 21 RGPD)**: Oponerse al tratamiento por motivos relacionados con su situación particular.
- **Decisiones individuales automatizadas (Art. 22 RGPD)**: Derecho a no ser objeto de una decisión basada únicamente en el tratamiento automatizado, incluida la elaboración de perfiles (*profiling*).
- **Plazo de Respuesta**: El responsable debe responder en el plazo máximo de **1 mes** a partir de la recepción de la solicitud (prorrogable 2 meses más en casos complejos).

## 5. El Delegado de Protección de Datos (DPD / DPO - Art. 37 RGPD y Art. 34 LOPDGDD)
- **Designación Obligatoria**:
  - Cuando el tratamiento lo realice una **autoridad u organismo público** (salvo tribunales en ejercicio de función judicial).
  - Cuando las actividades principales requieran observación habitual y sistemática de interesados a gran escala.
  - Cuando las actividades consistan en el tratamiento a gran escala de categorías especiales de datos.
- **Posición y Funciones**: Nombrado por sus cualidades profesionales y conocimientos especializados. Debe comunicarse su designación a la AEPD en **10 días**. Actúa con total independencia y no puede recibir instrucciones sobre el ejercicio de sus funciones.

## 6. La Agencia Española de Protección de Datos (AEPD)
- Autoridad administrativa independiente de ámbito estatal con personalidad jurídica propia y plena independencia.
- Potestades de investigación, correctivas (apercibimientos, órdenes de cumplimiento) y sancionadoras.
- Sanciones económicas: Hasta 10 o 20 millones de euros (o del 2% al 4% del volumen de negocio anual global para empresas). *En el sector público*, la sanción económica es sustituida por un **apercibimiento** formal y propuesta de iniciación de expediente disciplinario a los responsables (Art. 77 LOPDGDD).

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial**: [[wiki/sources/bloque1-tema09|Fuente Oficial del Tema 09]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque1-tema09-rgpd-lopdgdd|Test Tema 09]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque1-administracion|Mazo Flashcards Bloque 1]]
- 🏠 **Portada e Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque1|Resumen Maestro Bloque 1]]

---

> [[wiki/synthesis/resumenes/bloque-1-administracion/resumen-bloque1-tema08|⬅️ Tema 08]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque1|🏠 Índice Bloque 1]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-1-administracion/resumen-bloque1-tema10|Tema 10 ➡️]]
