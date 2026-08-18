---
title: "Resumen Completo y Profundo Tema 02 (Bloque 4): Servicios de Directorio, Active Directory DS y Kerberos v5"
type: "synthesis"
tags:
  - resumen
  - resumen-profundo
  - temario-completo
  - bloque-4
  - tema-02
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema02.md]]"
  - "[[wiki/sources/bloque4-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema01|⬅️ Tema 01]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|Tema 03 ➡️]]

# 🔴 Resumen Completo y Profundo Tema 02 (Bloque 4): Servicios de Directorio, Active Directory DS y Kerberos v5

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 02**
> Guía completa y exhaustiva que recopila todo el temario oficial, marco legal/normativo, detalles de arquitectura, tablas de datos críticos, protocolos, comandos de consola y casos prácticos.

---

## 🟣 1. Desarrollo Temático Completo e Íntegro

---

Administración de Bases de 
Datos. Virtualización. Cloud 

---

1. Recordando Bases de Datos 
5 
1.1. Sistema Gestor de Bases de Datos 
7 
1.2. Fases del diseño de la Base de Datos 
9 
2. Administración de Bases de Datos 
11 
2.1. Modelo ANSI/X3/SPARC 
12 
2.2. El administrador de Bases de Datos (DBA) 
15 
2.2.1. Funciones y Responsabilidades del DBA 
16 
3. Políticas, sistemas y procedimientos de back up y su recuperación 
21 
3.1. Políticas de backup 
22 
3.2. Copias de seguridad (backup) 
24 
3.2.1. Estrategia de backup 3-2-1 
27 
3.2.2. Secuencia de Respaldo GFS (Grandfather-Father-Son) 
27 
3.2.3. Duplicado de Información en Línea (RAID) 
28 
3.2.4. Software de respaldo y respaldo "On Line" 
29 
3.2.4.1. Respaldo DAS, NAS, SAN 
30 
3.2.5. Snapshots, complemento al Backup 
31 
3.3. Redundancia entre CPDs (Recovery Site) 
32 
4. Backup en sistemas físicos y virtuales 
33 
5. Virtualización de sistemas 
35 
5.1. Fundamentos de Arquitectura de Sistemas 
35 
5.1.1. Mecanismos de Protección del Procesador 
35 
5.1.1.1. Anillos de Protección 
35 
5.1.1.2. Operaciones privilegiadas 
36 
5.2. Conceptos Clave de Virtualización 
37 
5.2.1. Virtualización definición y beneficios 
37 
5.2.2. Máquina virtual 
38 
5.2.3. Hypervisor 
38 
5.2.4. Infraestructura virtual 
39

---

5.3. Virtualización de Plataforma (o Virtualización de Hardware) 
40 
5.3.1. Virtualización Completa 
40 
5.3.1.1. Virtualización Completa sin Asistencia de Hardware 
40 
5.3.1.2. Virtualización asistida por Hardware 
41 
5.3.2. Paravirtualización 
42 
5.4. Virtualización a Nivel de Sistema Operativo (Contenedores) 
44 
5.5. Tipos de virtualización 
45 
5.5.1. Virtualización de Aplicaciones 
45 
5.5.2. Virtualización de puestos de usuario 
46 
5.5.2.1. VDI: Virtual Desktop Infrastructure 
46 
5.5.2.2. RDS (Remote Desktop Services) 
47 
5.5.2.3. DaaS (Desktop as a Service) 
47 
5.5.3. Virtualización de Almacenamiento 
48 
5.5.3.1. Fundamentos y evolución tecnológica 
48 
5.5.3.2. Técnicas clave de virtualización del almacenamiento 
49 
5.5.3.2.1. Configuración de Discos 
49 
5.5.3.2.2. Particionamiento/Zoning 
50 
5.5.3.3. Soluciones comerciales de virtualización 
50 
5.5.4. Virtualización de Datos 
51 
5.5.5. Virtualización de Red 
51 
5.5.6. Virtualización de E/S (Input/Output) 
52 
5.5.7. Software Defined Infrastructure (SDI) 
52 
5.6. Impacto y Tendencias: Virtualización y Green IT 
53 
5.7. Diferencias entre virtualizar un S.O. e instalarlo 
53 
5.8. Seguridad en entornos virtualizados 
56 
5.9. Programas útiles para virtualizar S.O. 
57 
5.9.1. Hyper-V 
58 
5.9.2. vSphere 
60

---

5.10. Infraestructura Hiperconvergente (HCI) 
61 
5.10.1. Definición y características 
61 
5.10.2. Componentes principales (cómputo, red, almacenamiento) 
62 
5.10.3. Ventajas y diferencias frente a infraestructuras tradicionales 
63 
5.10.4. Soluciones comerciales: VMware, vSAN, Dell EMC VxRail, Nutanix 
65 
6. Computacion en la nube 
67 
6.1. Evolucion 
69 
6.2. Caracteriticas 
72 
6.2.1. La importancia de la seguridad 
74 
6.3. Cloud y el Big Data 
75 
6.4. Tipos de servicios en la nube 
76 
6.4.1. SaaS, Software as a Service 
76 
6.4.2. PaaS, Platform as a Service 
77 
6.4.3. IaaS, Infraestructure as a Service 
78 
6.4.4. Nuevas alternativas 
79 
6.4.4.1. iPaaS, Integration Platform as a Service 
79 
6.4.4.2. SECaaS, Security as a Service 
80 
6.4.4.3. FaaS, Function as a Service 
81 
6.4.4.4. MBaaS, Mobile Backend as a Service 
81 
6.4.4.5. IDaaS, Identity as a Service 
81 
6.5. Modelos de implementación 
83 
6.5.1. Nube Pública 
83 
6.5.2. Nube Privada 
84 
6.5.3. Nube Híbrida 
85 
6.5.4. Otras 
85 
7. Bibliografía 
86

---

Administración de Bases de Datos. Virtualización. Cloud 
5 
1. Recordando Bases de Datos 
Ya has estudiado en unidades anteriores, las bases de datos, sus características y objetivos, así como el 
Sistema Gestos de Base de Datos y las fases de Diseño. 
Como recordatorio, pero sin repetir todo lo ya estudiado, vamos a repasar alguno de los conceptos. 
Una de las definiciones de bases de datos más aceptadas es la propuesta por Flory en 1982: "Una base 
de datos es un conjunto exhaustivo, no redundante de datos estructurados, organizados 
independientemente de su utilización y su implementación en máquina, accesibles a tiempo real y 
compatibles por usuarios concurrentes que tienen necesidad de información diferente y no predecible 
en el tiempo." 
Otras definiciones 
• Conjunto, colección o depósito de datos almacenados en un soporte informático. Los datos 
deben estar interrelacionados y estructurados de acuerdo con un modelo capaz de recoger el 
máximo contenido semántico. 
• Consiste en una colección de datos persistentes e independientes usados por una organización 
determinada. 
• Serie de datos organizados y relacionados entre sí, los cuales son recolectados y explotados por 
los sistemas de información de una empresa o negocio en particular. 
• Es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente 
para su posterior uso. 
• Es una colección de información organizada de tal modo que sea fácilmente accesible, 
gestionada y actualizada. 
• Es una representación de objetos y situaciones del mundo real. En el mundo real existen 
restricciones y limitaciones que deben ser reflejadas en la base de datos. Para ello es necesario el 
uso de métodos de diseño riguroso y formalizado. 
Características de las B.D 
• Es un conjunto o colección de datos. 
• Los datos están estructurados. 
• Existen relaciones entre los datos. 
• Los datos no pueden ser redundantes (no debe haber duplicados).

---

Administración de Bases de Datos. Virtualización. Cloud 
6 
• Los datos deben ser independientes de la máquina en que se almacenan o explotan. 
• Debe ser fácilmente accesible, gestionada y almacenada. 
• Debe permitir el acceso concurrente a la misma (de esto se encargan los Sistemas Gestores de 
Base de Datos (SGBD)). 
• Deben dar soporte a usuarios con distintas necesidades. 
• La mayoría de las bases de datos se almacenan en un soporte informático. 
• Son la base de los sistemas de información. 
• Representan una situación del mundo real. 
Principales objetivos de un sistema de base de datos 
• Proporcionar a los usuarios y desarrolladores una visión abstracta de los datos. 
El sistema esconde ciertos detalles de cómo se almacenan y mantienen los datos. 
• Independencia entre datos y aplicaciones. 
Cuando se tenga que cambiar algo en la base de datos (como la forma de almacenar datos), 
esto no repercutirá en los programas de aplicación que trabajan sobre esa base de datos. 
Evitar redundancias de datos (duplicidad de información). 
• Evitar la inconsistencia de datos. 
Se produce una inconsistencia de datos cuando existen varias copias de un mismo dato y no 
todas tienen el mismo valor. 
• Preservar la integridad. 
Los valores de los datos almacenados deben satisfacer ciertos tipos de restricciones de 
consistencia. 
Por ejemplo, el precio de un producto debe ser un número y no una cadena de caracteres. 
• Atomicidad. 
Los procesos deben ser atómicos, es decir, deben ocurrir o no ocurrir, pero no puede ocurrir 
parte del proceso. 
Por ejemplo, si mientras se está realizando un proceso se produce un corte de electricidad y se 
apaga el equipo, Se deberá volver al estado de consistencia anterior al fallo para que no se 
queden operaciones a medio hacer.

---

Administración de Bases de Datos. Virtualización. Cloud 
7 
• Seguridad y Confidencialidad. 
Se debe garantizar la confidencialidad y seguridad de los datos contra accesos incorrectos o no 
autorizados. 
• Acceso concurrente a los datos. 
Debe permitir a múltiples usuarios actualizar los datos simultáneamente. 
Un Sistema de Bases de Datos, está formado por 
• Una base de datos. 
• Un Sistema Gestor de Bases de datos que administra y gestiona la información de la base de 
datos. 
• Un diccionario de datos. Contiene el listado de campos y variables de la B.D. así como su 
descripción, longitud, posibles valores, etc. 
También puede contener otros datos de interés como: 
• Información sobre la representación física de los datos. 
• Asignación a dispositivos. 
• Formas de acceso.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial**: [[wiki/sources/bloque4-tema02|Fuente Oficial del Tema 02]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema02-windows-server|Test Tema 02]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Portada e Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema01|⬅️ Tema 01]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|Tema 03 ➡️]]
