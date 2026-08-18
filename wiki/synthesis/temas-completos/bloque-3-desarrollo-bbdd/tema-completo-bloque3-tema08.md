---
title: "Tema Completo Extendido 08 (Bloque 3): Control de Versiones con Git y Metodologías Ágiles (Scrum, Kanban)"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-3
  - tema-08
  - oposiciones-tai
estado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md]]"
  - "[[wiki/sources/bloque3-tema08]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema07|⬅️ Tema Completo 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema09|Tema Completo 09 ➡️]]

# 🔴 Tema Completo Extendido 08 (Bloque 3): Control de Versiones con Git y Metodologías Ágiles (Scrum, Kanban)

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 08 correspondiente al Bloque 3 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro

# Bloque 3 - Tema 08 (UD012115): Accesibilidad, Diseño Universal, Usabilidad, Confidencialidad y Seguridad en Puesto de Usuario

<!-- Page 1 -->

 
 
Accesibilidad, Diseño Universal 
y Usabilidad. Confidencialidad y 
Disponibilidad de la información 
en puestos de usuario final. 
Conceptos de seguridad 

<!-- Page 2 -->

ÍNDICE 
1. Accesibilidad, diseño universal y usabilidad 
5 
1.1. Accesibilidad 
5 
1.2. Diseño universal 
6 
1.2.1. 7 Principios del diseño universal 
7 
1.3. Usabilidad 
10 
2. Organismos reguladores W3C, WAI 
13 
2.1. W3C (The World Wide Web Consortium) 
14 
2.2. WAI (Web Accessibility Initiative) 
15 
3. Las WCAG - Capas de orientación para entenderlas 
17 
3.1. Principios Generales 
18 
3.2. Pautas Generales 
19 
3.3. Criterios de Conformidad Verificables 
19 
3.3.1. Conformidad para que una aplicación web sea WCAG 2.X 
20 
3.4. Técnicas suficientes y Técnicas recomendables (o de Asesoramiento), y Fallas 23 
4. Las WCAG. Versiones 
24 
4.1. WCAG 1.0 
24 
4.2. WCAG 2.0 
31 
4.3. WCAG 2.1 
34 
4.4. WCAG 2.2 
36 
5. Las WCAG 2.X - Pautas y sus criterios 
38 
5.1. Pautas Principio 1: Perceptible 
38 
5.1.1. Pauta 1.1 Alternativas textuales 
38 
5.1.2. Pauta 1.2 Medios tempodependientes 
40 
5.1.3. Pauta 1.3 Adaptable 
41 
5.1.4. Pauta 1.4 Distinguible 
42 
5.2. Pautas Principio 2: Operable 
46 
5.2.1. Pauta 2.1 Accesible por teclado 
47 
5.2.2. Pauta 2.2 Tiempo suficiente 
48 
5.2.3. Pauta 2.3 Convulsiones 
50 

<!-- Page 3 -->

 
 
5.2.4. Pauta 2.4 Navegable 
50 
5.2.5. Pauta 2.5 Modalidades de entrada (Añadida en WCAG 2.1) 
53 
5.3. Pautas Principio 3: Comprensible 
56 
5.3.1. Pauta 3.1 Legible 
56 
5.3.2. Pauta 3.2 Predecible 
57 
5.3.3. Pauta 3.3 Entrada de datos asistida 
58 
5.4. Pautas Principio 4: Robusto 
61 
5.4.1. Pauta 4.1 Compatible 
62 
5.5. Resumen de los criterios de conformidad (A, AA Y AAA) 
62 
6. Diseño Inclusivo o Inclusive Design 
63 
7. RDF (Resource Description Framework) 
64 
8. Legislación sobre accesibilidad en España, Europa y otros países 
65 
8.1. Real Decreto 1112/2018, de 7 de septiembre, sobre accesibilidad de los sitios 
web y aplicaciones para dispositivos móviles del sector público 
68 
9. ISO/IEC 10026-1 (Concepto ACID) 
69 
9.1. Requisitos ACID 
69 
9.1.1. Atomicidad 
69 
9.1.2. Consistencia (integridad) 
70 
9.1.3. Aislamiento 
70 
9.1.4. Durabilidad (persistencia) 
72 
9.2. Puesta en práctica 
74 
10. ANSI/ISO SQL 92: efectos en lectura 
74 
11. Herramientas para mejora de acceso y usabilidad 
75 
11.1. Telefonía móvil 
76 
11.2. Ordenadores personales (hardware) 
77 
11.3. Software 
78 
11.3.1. Aplicaciones para ayudar a personas con problemas de Accesibilidad 
80 
11.4. Internet 
84 
11.5. Diseño de interfaces: las ocho reglas de oro 
86 

<!-- Page 4 -->

 
 
11.6. Atributos ARIA 
88 
11.7. Patrones de interacción en el diseño de interfaces de usuario 
90 
12. Herramientas de evaluación automática de accesibilidad 
91 
13. Confidencialidad y disponibilidad de la información en puestos de usuario final 93 
13.1. Disponibilidad e integridad de la información 
94 
13.1.1. La confidencialidad de la información 
95 
13.1.2. Responsabilidades del usuario 
98 
14. Conceptos de seguridad 
100 
14.1. Control de acceso a la información 
101 
14.2. Cifrado de la información 
102 
14.3. Copias de seguridad 
103 
14.4. Desechado y reutilización de soportes y equipos 
103 
15. Bibliografía 
104 
 

<!-- Page 5 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
5 
1. Accesibilidad, diseño universal y usabilidad 
Los conceptos de accesibilidad, diseño universal y usabilidad pueden aplicarse a muchos aspectos de 
nuestra vida cotidiana. 
Nosotros, como informáticos, nos centraremos en la aplicación de estos conceptos sobre el acceso a la 
información mediante el diseño de aplicaciones informáticas (especialmente aplicaciones o páginas web). 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
1.1. Accesibilidad 
 
El concepto de accesibilidad es hablar de un acceso universal a la Web, independientemente del tipo de 
hardware, software, infraestructura de red, idioma, cultura, localización geográfica y capacidades de los 
usuarios. Se utiliza para nombrar el grado o nivel en el que cualquier ser humano, más allá de su 
condición física o de sus facultades cognitivas, puede usar un objeto, disfrutar de un servicio o hacer uso 
de una infraestructura. 

<!-- Page 6 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
6 
La aplicación de la accesibilidad universal en el ámbito de las telecomunicaciones y sociedad de la 
información está regulada por ley. 
En los años 80 el arquitecto y profesor Ron L. Mace, usuario de silla de ruedas, fue el principal pionero 
del diseño accesible, participando en la elaboración de la Ley de Americanos con Discapacidad (ADA). 
Existen diversas ayudas técnicas para impulsar la accesibilidad y equiparar las posibilidades de todas las 
personas. 
En función de las limitaciones de las personas se ha diseñado unas ayudas como pueden ser: 
• Problemas de visión: El alfabeto Braille, y las señales auditivas de los semáforos. 
• Problemas auditivos: la lengua de signos. 
• Problemas cognitivos, de movilidad o locomotrices: Rampas o ascensores para discapacitados, la 
eliminación de barreras arquitectónicas. 
• Edad avanzada. Barras asideras para la ducha. 
Del mismo modo es necesario hacerlo en el desarrollo de aplicaciones. 
1.2. Diseño universal 
 
Fuente: Pixabay 
Ron Mace, en 1989, realiza una valoración sobre el concepto "Accesibilidad Física" convirtiéndolo en un 
nuevo término denominándolo "Diseño Universal", definiéndolo de la siguiente manera: 
"El Diseño Universal es la creación de productos y entornos diseñados de modo que sean utilizables 
por todas las personas, independientemente de su edad, tamaño o discapacidad. Esto incluye lugares 
públicos en el entorno construido tales como edificios, calles o espacios a los que el público tiene 
acceso; productos y servicios prestados en esos lugares; y los sistemas que están disponibles, 
incluyendo la tecnología de la información y las comunicaciones." 

<!-- Page 7 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
7 
El objetivo del diseño universal tiene como objetivos: 
• Simplificar la vida de todas las personas, haciendo que los productos, las comunicaciones y el 
entorno construido por el hombre sean más utilizables por la mayor cantidad posible de 
personas con un costo nulo o mínimo. 
• Beneficiar a personas de todas las edades y capacidades. 
• Dirigir sus acciones al desarrollo de productos y entornos de fácil acceso para el mayor número 
de personas posible, sin la necesidad de adaptarlos o rediseñarlos de una forma especial. El 
concepto surge del diseño sin barreras y del diseño accesible. 
• Alcanzar todos los aspectos de la accesibilidad, y se dirige a todas las personas, incluidas las 
personas con discapacidad. 
• Resolver el problema partiendo de la idea de la diversidad humana, simplificar la realización de 
las tareas cotidianas mediante la construcción de productos, servicios y entornos más sencillos 
de usar por todas las personas y sin esfuerzo alguno. 
Así pues, el diseño universal beneficia a todas las personas de todas las edades y habilidades. 
1.2.1. 7 Principios del diseño universal 
Los siete principios del diseño universal o diseño para todos deben tener en cuenta aspectos como el 
coste, la cultura en la que será usado, etcétera. 
Están regulados por el W3C, que estudiaremos en un punto posterior. 
Estos principios generales del diseño son aplicables en la arquitectura, la ingeniería y, por supuesto, las 
páginas y aplicaciones web. 
A continuación, mostramos la versión 2.0 de los principios del diseño universal proporcionados por el 
Centro para el Diseño Universal, traducidos y adaptados por Emmanuelle Gutiérrez y Restrepo. 
Los principios del diseño universal son: 
1. Primer principio: uso equiparable. 
El diseño es útil y vendible a personas con diversas capacidades. 
Pautas: 
• Que proporcione las mismas maneras de uso para todos los usuarios: idénticas cuando es 
posible, equivalentes cuando no lo es. 
• Que evite segregar o estigmatizar a cualquier usuario. 

<!-- Page 8 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
8 
• Las características de privacidad, garantía y seguridad deben estar igualmente disponibles 
para todos los usuarios. 
• Que el diseño sea atractivo para todos los usuarios. 
2. Segundo principio: uso flexible. 
El diseño se acomoda a un amplio rango de preferencias y habilidades individuales. 
Pautas: 
• Que ofrezca posibilidades de elección en los métodos de uso. 
• Que pueda accederse y usarse tanto con la mano derecha como con la izquierda. 
• Que facilite al usuario la exactitud y precisión. 
• Que se adapte al paso o ritmo del usuario. 
3. Tercer principio: simple e intuitivo. 
El uso del diseño es fácil de entender, atendiendo a la experiencia, conocimientos, habilidades 
lingüísticas o grado de concentración actual del usuario. 
Pautas: 
• Que elimine la complejidad innecesaria. 
• Que sea consistente con las expectativas e intuición del usuario. 
• Que se acomode a un amplio rango de alfabetización y habilidades lingüísticas. 
• Que dispense la información de manera consistente con su importancia. 
• Que proporcione avisos eficaces y métodos de respuesta durante y tras la finalización de la 
tarea. 
4. Cuarto principio: información perceptible. 
El diseño comunica de manera eficaz la información necesaria para el usuario, atendiendo a las 
condiciones ambientales o a las capacidades sensoriales del usuario. 
Pautas: 
• Que use diferentes modos para presentar de manera redundante la información esencial 
(gráfica, verbal o táctilmente). 
• Que proporcione contraste suficiente entre la información esencial y sus alrededores. 

<!-- Page 9 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
9 
• Que amplíe la legibilidad de la información esencial. 
• Que diferencie los elementos en formas que puedan ser descritas (por ejemplo, que haga 
fácil dar instrucciones o direcciones). 
• Que proporcione compatibilidad con varias técnicas o dispositivos usados por personas con 
limitaciones sensoriales. 
5. Quinto principio: tolerancia al error. 
El diseño minimiza los riesgos y las consecuencias adversas de acciones involuntarias o 
accidentales. 
Pautas: 
• Que disponga los elementos para minimizar los riesgos y errores (elementos más usados, 
más accesibles) y los elementos peligrosos eliminados, aislados o tapados. 
• Que proporcione advertencias sobre peligros y errores. 
• Que proporcione características seguras de interrupción. 
• Que desaliente acciones inconscientes en tareas que requieren vigilancia. 
6. Sexto principio: que exija poco esfuerzo físico. 
El diseño puede ser usado eficaz y confortablemente y con un mínimo de fatiga. 
Pautas: 
• Que permita que el usuario mantenga una posición corporal neutra. 
• Que utilice de manera razonable las fuerzas necesarias para operar. 
• Que minimice las acciones repetitivas. 
• Que minimice el esfuerzo físico continuado. 
7. Séptimo principio: tamaño y espacio para el acceso y uso. 
Que proporcione un tamaño y espacio apropiados para el acceso, alcance, manipulación y uso, 
atendiendo al tamaño del cuerpo, la postura o la movilidad del usuario. 
Pautas: 
• Que proporcione una línea de visión clara hacia los elementos importantes, tanto para un 
usuario sentado como para uno que está de pie. 
• Que el alcance de cualquier componente sea confortable para cualquier usuario sentado o 
de pie. 

<!-- Page 10 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
10 
• Que se acomode a variaciones de tamaño de la mano o del agarre. 
• Que proporcione el espacio necesario para el uso de ayudas técnicas o de asistencia 
personal. 
1.3. Usabilidad 
 
Fuente: Wikipedia 
La usabilidad hace referencia a la facilidad con la que un usuario puede utilizar un objeto, infraestructura 
o servicio fabricado por otras personas con el fin de alcanzar un cierto objetivo. 
Para alcanzar la mayor usabilidad posible, se debe diseñar pensando en el usuario, es decir, producir por 
y para el usuario. La usabilidad está vinculada a la simpleza, la facilidad, la comodidad y la practicidad. 
La Web, por su carácter global, debe dar respuesta a una gran variedad de usuarios (diversidad cultural, 
social, cognitiva, psicológica, capacitiva, etcétera). 
Algunas de las diversidades que debemos tener en cuenta son: 
• Las capacidades cognitivas y perceptivas: 
• Memoria a corto y largo plazo. 
• Comprensión del lenguaje. 
• Capacidad de aprendizaje. 
• Asimilación de conceptos. 
• Capacidad para la resolución de problemas. 

<!-- Page 11 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
11 
• Personalidad del usuario: 
• Extrovertidos o Introvertidos. 
• Sensoriales o intuitivos. 
• Sentimentales o racionales. 
• Culturales: 
• Desde el punto de vista étnico. 
• Desde el punto de vista lingüístico. 
• Nivel cultural. 
• Las discapacidades. 
• Edad: 
• Personas mayores. 
• Niños. 
• Tecnología: 
• Conexión a Internet. 
• Tamaños de pantalla. 
• Requisitos de memoria y procesamiento. 
Requisitos y medidas de usabilidad 
Existen muchos requisitos de usabilidad, pero todos están centrados en el usuario y en la consecución 
de sus objetivos de forma fácil y eficiente. Para determinar este nivel de usabilidad se suelen utilizar una 
serie de medidas. 
A continuación, te mostramos algunas de ellas: 
• El tiempo que necesitan los usuarios para aprender a realizar sus tareas. 
• La velocidad para realizar las tareas. 
• La cantidad de errores que se cometen al realizar las tareas. 
• El tiempo de espera entre acciones. 
• La satisfacción subjetiva del usuario (es la más importante, pero difícil de medir). 

<!-- Page 12 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
12 
Prueba de usabilidad 
La prueba de usabilidad por parte del usuario es una técnica usada en el diseño de interacciones 
centrado en el usuario para evaluar un producto. 
• Consisten en seleccionar a un grupo de usuarios de una aplicación y solicitarles que lleven a cabo 
las tareas para las cuales fue diseñada, en tanto el equipo de diseño, desarrollo y otros 
involucrados toman nota de la interacción, particularmente de los errores y dificultades con las 
que se encuentren los usuarios. 
• Miden la usabilidad, o facilidad de uso, de un objeto específico o un conjunto de objetos, mientras 
que los estudios de interacción persona-computador intentan formular los principios generales. 
• Se enfocan en medir la capacidad de un producto de fabricación humana en cumplir el propósito 
para el cual fue diseñado. 
• Puedes verse como pruebas irreemplazables, dado que entrega información directa de cómo los 
usuarios reales utilizan el sistema, no son como los métodos de inspección de usabilidad donde 
expertos usan diferentes métodos para evaluar una interfaz de usuario sin involucrar a usuarios 
reales. 
• No es necesario que se trate de una aplicación completamente terminada, pueden realizarse en 
un prototipo. 
Usabilidad en la sociedad de la información 
El estándar ISO 9241-11 define usabilidad como: 
El grado en que un producto puede ser utilizado por usuarios específicos para lograr objetivos 
específicos de manera efectiva, eficiente y satisfactoria en un contexto de uso específico. 
Por lo tanto, la usabilidad está determinada por el usuario y debe estar centrada en este, marcándose 
como objetivo satisfacer sus necesidades. 
Está comprobado que vende más una interfaz llamativa y cómoda de usar que la estructura interna de 
la aplicación y sus funcionalidades. 
 
 
 
 
+ Info 
En una ocasión, Apple encargó a una empresa externa el diseño de 
su portal web de compras. 
Realizaron un diseño espectacular que invitaba a comprar. 
 

<!-- Page 13 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
13 
 
 
 
Sin embargo, olvidaron incluir el botón "Comprar". 
Es importante saber a quién va dirigida una página y asegurarse de 
cumplir los requisitos (obviamente, que los clientes puedan 
comprar era uno de ellos). 
 
2. Organismos reguladores W3C, WAI 
El consorcio W3C, tiene varias ramas de trabajo, una de ellas La Web Accessibility Initiative (WAI) o 
Iniciativa para la Accesibilidad Web. 
Dentro de WAI, está el grupo de trabajo de protocolos y formatos (PFWG), autores del desarrollo de 
distintas pautas, destacando las siguientes: 
• XAG: Directrices de Accesibilidad para XML. 
• ATAG: Pautas de Accesibilidad para las Herramientas de Creación de Contenido (Herramientas 
de autor). 
• UAAG: Pautas de Accesibilidad para el Agente de Usuario. 
• ARIA: Aplicaciones de Internet enriquecidas accesibles. 
Acrónimo de: Accessible Rich Internet Applications. 
• AG WG: Pautas de Accesibilidad. 
(Tiene el grupo de trabajo de las Pautas de Accesibilidad anteriormente conocido como el 
Grupo de Trabajo de las Pautas de Accesibilidad para el Contenido Web). 
A estas pautas se les denomina WCAG, siglas de Web Content Accessibility Guidelines, en 
castellano Pautas de accesibilidad del contenido en la Web. 
WCAG es una guía de recomendaciones para realizar webs más accesibles: 
• WCAG 2.0 y WCAG 2.1 son estándares técnicos estables y de referencia. 
Contienen 12 pautas en WCAG 2.0, y 13 pautas en WCAG 2.1 que se agrupan en cuatro 
principios: 
» - perceptible - operable - comprensible - robusto. 

<!-- Page 14 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
14 
Cada pauta incluye criterios de conformidad, que se pueden comprobar y que se clasifican 
en tres niveles: 
» A – AA – AAA. 
Vamos a ir estudiándolo con detenimiento. 
2.1. W3C (The World Wide Web Consortium) 
 
Fuente: 
https://commons.wikimedia.org/wiki/File:W
3C%C2%AE_Icon.svg 
El W3C (Consorcio para la World Wide Web) fue fundado en octubre de 1994 para conducir a la World 
Wide Web a su máximo potencial, desarrollando protocolos de uso común que promocionaran su 
evolución y aseguraran su interoperabilidad. 
Inicialmente, el W3C fue creado en colaboración con el CERN (Laboratorio Europeo de Partículas 
Físicas), donde se originó la web, con el apoyo de DARPA (Agencia Norteamericana de Investigación 
Avanzada en Proyectos de Defensa) y la Comisión Europea. 
Objetivo de W3C: Guiar la web hacia su máximo potencial. 
La W3C proporciona una guía sobre la accesibilidad de los sitios web para las personas con 
discapacidad. Indica una especificación, desarrollada, por la Iniciativa de Accesibilidad en la Web (WAI) 
del W3C, dónde se indican Las Pautas de Accesibilidad al Contenido en la Web 1.0 (WCAG 1.0). 
El W3C cuenta con una oficina en Oviedo y está hospedada por la Fundación para el Fomento de la 
Investigación Científica y la Tecnología (FICYT). 
El Consorcio está liderado por Tim Berners-Lee, director y creador de la World Wide Web. 

<!-- Page 15 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
15 
Los servicios que ofrece el Consorcio incluyen: 
• Un banco de información sobre la World Wide Web (la Web) para desarrolladores y usuarios. 
• Realización de códigos de referencia para incorporar y promover estándares. 
• Prototipos y aplicaciones de demostración para demostrar el uso de las nuevas tecnologías. 
 
 
 
 
Nota 
El Consorcio W3C, no ofrece asesoramiento a organismos e 
instituciones sobre diseño universal. 
 
El compromiso del W3C de encaminar a la web a su máximo potencial incluye promover un alto 
grado de accesibilidad para las personas con discapacidad. 
2.2. WAI (Web Accessibility Initiative) 
 
Fuente: https://commons.wikimedia.org/wiki/File:WCAG2AAA-v.svg 
Una de las ramas del consorcio W3C, es el grupo de trabajo permanente WAI (Web Accessibility 
Initiative o Iniciativa para la Accesibilidad de la Red), que fue anunciada por W3C el 7 de abril de 1997. 
Se coordina con organizaciones de todo el mundo para desarrollar estrategias y pautas que hagan 
posible la accesibilidad para personas con discapacidad, creando recursos y herramientas de ayuda para 
los desarrolladores web. 
La WAI, Web Accesibility Initiative, define mediante la WCAG, una serie de guías para la generación 
de contenidos accesible. 

<!-- Page 16 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
16 
 
 
 
+ Info 
Los documentos oficiales del W3C están escritos en inglés, y algunos 
se han traducido al castellano: 
• Introducción a la Accesibilidad Web 
http://www.w3c.es/Traducciones/es/WAI/intro/accessibility 
• Guía Breve de Accesibilidad Web 
http://www.w3c.es/divulgacion/guiasbreves/Accesibilidad 
• Guía breve para crear sitios web accesibles 
http://www.w3.org/WAI/quicktips/qt.es.htm 
• Para comenzar: Creando un Sitio Web Accesible 
http://www.w3.org/WAI/gettingstarted/Overview.html.es 
 
 
La Web Accesibility Initiative indica una serie de componentes esenciales en la accesibilidad web, y 
define una serie de guías, ¿cuál de entre las siguientes corresponde a la generación de contenidos 
accesibles? 
La WAI, persigue la accesibilidad de la Web a través de cinco áreas de trabajo principales: 
• Tecnología. 
• Directrices. 
• Herramientas. 
• Formación y difusión. 
• Investigación y desarrollo. 
Las directrices o pautas 
El WAI ha desarrollado diversas directrices: 
• Directrices de accesibilidad para el contenido de la Web. 
• Directrices de accesibilidad para XML. 
• Directrices para las herramientas de autor. 
• Directrices para los navegadores. 

<!-- Page 17 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
17 
Estas directrices son consideradas en la Unión Europea como normas de facto y son citadas como 
referencia obligada en la mayoría de las legislaciones sobre tecnologías de la información de todo el 
mundo. 
Control de la aplicación de las directrices 
El WAI ha creado una lista de verificación de los puntos de control de las directrices de accesibilidad 
para el contenido web. 
Esto facilita la verificación manual de la aplicación de las pautas de accesibilidad cuando creamos una web. 
 
 
 
 
+ Info 
Existen múltiples aplicaciones web que revisan de manera 
automática nuestro contenido web (al menos de forma 
superficial). 
 
Revisión de la accesibilidad de las páginas 
Cualquier persona puede revisar la accesibilidad de cualquier página web utilizando una herramienta de 
evaluación automática. 
Sin embargo, determinadas cuestiones deben ser evaluadas por un profesional. 
Declaración de conformidad con las directrices 
Si en el diseño de una página se han seguido las directrices de accesibilidad para el contenido web y, tras 
su revisión, se está seguro de alcanzar alguno de los niveles de accesibilidad, puede colocarse el logo 
correspondiente que el WAI ofrece para declarar la conformidad con las directrices. 
3. Las WCAG - Capas de orientación para entenderlas 
Los individuos y organizaciones que emplean las WCAG son un grupo amplio y variado que incluye 
diseñadores y desarrolladores web, reguladores, agentes de compra, profesores y estudiantes. 
La estructura de las WCAG, se define en las "Capas de orientación para entender las WCAG", que son 
los 4 niveles de orientación que se proporcionan. 

<!-- Page 18 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
18 
 
Los 4 niveles de orientación 
3.1. Principios Generales 
Los principios, es el nivel más alto de orientación que proporciona la WCAG. 
Son cuatro principios y proporcionan los fundamentos de la accesibilidad web: 
1. Perceptible. 
(Perceptibilidad). 
La información y los componentes de la interfaz de usuario deben ser mostrados a los usuarios 
en formas que ellos puedan percibir. 
2. Operable. 
(Operabilidad). 
Los componentes de la interfaz de usuario y la navegación deben ser manejables. 
3. Comprensible. 
(Comprensibilidad). 
La información y las operaciones de usuarios deben ser comprensibles. 
4. Robusto. 
El contenido deber ser suficientemente robusto para que pueda ser bien interpretado por una 
gran variedad de agentes de usuario, incluyendo tecnologías de asistencia. 

<!-- Page 19 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
19 
3.2. Pautas Generales 
Debajo de cada principio hay una lista de pautas que abordan el principio, es decir, dentro de cada 
principio, existen unas pautas. 
Estas Pautas, proporcionan los objetivos básicos que los desarrolladores deben lograr con el fin de crear 
un contenido más accesible para los usuarios con distintos tipos de discapacidad. 
Estas Pautas no son verificables, lo son los criterios contenidos en ellas. 
Indicamos todas las pautas en un punto posterior, indicando en cada una de ellas sus criterios de 
conformidad, el nivel de conformidad al que pertenecen, y si han sido añadidas en la versión WCAG 2.1, 
o añadidas, modificadas o eliminadas en la versión WCAG 2.2 
3.3. Criterios de Conformidad Verificables 
Para cada Pauta (que actúa como una directriz), existen los "Criterios de Conformidad" (que son 
verificables), y que describen específicamente lo que se debe tratar relacionado con esa Pauta. 
Cada uno de estos criterios, tiene un enlace a la sección del documento "Cómo Cumplir", donde se 
proporciona: 
• Técnicas suficientes para lograr el complimiento del Criterio de Conformidad. 
• Técnicas opcionales de asesoramiento. 
• Descripciones de lo que se pretende lograr con ese criterio, indicando los beneficios y también 
ejemplos. 
Cada criterio, a la hora de comprobar el contenido web, dará un resultado de Verdadero o Falso, en 
función de si se cumple o no. 
Los niveles de prioridad asociados a los puntos de verificación son: 
• Prioridad 1. 
Son puntos de verificación imprescindibles, que si no se cumplen provocan que algunos grupos 
de personas sean incapaces de acceder a la información. Un desarrollador debe satisfacer este 
punto de verificación. 
• Prioridad 2. 
Si no se cumplen los puntos de verificación de esta prioridad, ciertas personas encontrarán 
muchas dificultades para acceder a esta información. 
• Prioridad 3. 
Los puntos de prioridad 3 pueden cumplirse, en caso contrario algunas personas hallarán 
dificultades para acceder a la información. 

<!-- Page 20 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
20 
Con el fin de cumplir con las necesidades de los diferentes grupos y situaciones, se definen tres niveles 
de conformidad (o adecuación): 
Se definen tres niveles de conformidad (o adecuación): 
1. Nivel de Adecuación (A): "A" el menos exigente, el más bajo: 
Cuando se cumplen los puntos de verificación de prioridad 1. 
2. Nivel de Adecuación (AA) "Doble A": 
Cuando se cumplen los puntos de verificación de prioridad 1 y 2. 
3. Nivel de Adecuación (AAA) "Triple A" el más exigente, el más alto: 
Cuando se cumplen los puntos de verificación de prioridad 1, 2 y 3. 
La comprobación de una aplicación, estudiando los puntos de verificación con sus niveles de prioridad, 
da lugar a obtener el Nivel de Adecuación correspondiente a esa aplicación. 
3.3.1. Conformidad para que una aplicación web sea WCAG 2.X 
Dependiendo de si se toman los criterios de conformidad de la versión WCAG 2.0, la aplicación web será 
2.0, o, si se toman los de la versión 2.1, la aplicación será WCAG 2.1 
Para que una página web sea conforme con las WCAG 2.x, deben satisfacerse todos los requisitos de 
conformidad siguientes: 
1. Nivel de conformidad: Uno de los siguientes niveles de conformidad se satisface por completo. 
• Nivel A: Para lograr conformidad con el Nivel A (el mínimo), la página web satisface todos 
los Criterios de Conformidad del Nivel A, o proporciona una versión alternativa conforme. 
• Nivel AA: Para lograr conformidad con el Nivel AA, la página web satisface todos los 
Criterios de Conformidad de los Niveles A y AA, o se proporciona una versión alternativa 
conforme al Nivel AA. 
• Nivel AAA: Para lograr conformidad con el Nivel AAA, la página web satisface todos los 
Criterios de Conformidad de los Niveles A, AA y AAA, o proporciona una versión alternativa 
conforme al Nivel AAA. 
Nota 1: Aunque la conformidad sólo puede alcanzarse en los niveles mencionados, se alienta a 
los autores a notificar en sus declaraciones cualquier avance que hayan realizado para satisfacer 
los criterios de conformidad de un nivel de conformidad mayor al que hayan alcanzado. 
Nota 2: No se recomienda que el Nivel de Conformidad AAA sea requerido como política 
general para la totalidad de un sitio web, ya que en algunos contenidos no es posible satisfacer 
todos los Criterios de Conformidad de Nivel AAA. 

<!-- Page 21 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
21 
Significado de proporcionar una versión alternativa: 
(información extraída de: http://accesibilidadweb.dlsi.ua.es/?menu=version-alternativa-
conforme) 
Es una que cumple: 
a. Que es conforme según un nivel designado. 
b. Que proporciona igual funcionalidad e información, y en el mismo idioma. 
c. Que se mantiene actualizada con la misma frecuencia que el contenido no conforme. 
d. Que para la cual al menos una de las siguientes condiciones es verdadera: 
» Se puede acceder a la versión conforme desde la página no conforme a través de un 
mecanismo compatible con la accesibilidad. 
» Sólo se puede acceder a la versión no conforme desde la versión conforme. 
» Sólo se puede acceder a la versión no conforme desde una página conforme que 
además proporciona un mecanismo para llegar a la versión conforme. 
Nota 1: En esta definición, "sólo se puede acceder" significa que hay algún mecanismo, como 
una redirección condicional, que previene que el usuario "acceda" (cargue) la página no 
conforme a menos que el usuario haya llegado desde la versión conforme. 
Nota 2: La versión alternativa no necesita ser un equivalente página a página del original (por 
ejemplo, la versión alternativa conforme podría consistir en varias páginas). 
Nota 3: Si están disponibles versiones en diversos idiomas, las versiones alternativas conformes 
son necesarias para cada idioma ofrecido. 
Nota 4: Se pueden proporcionar versiones alternativas diferentes adaptadas a diferentes 
tecnologías o grupos de usuarios. Cada versión debería ser tan conforme como fuera posible. 
Una versión necesitaría ser totalmente conforme para cumplir el requisito de conformidad 1. 
Nota 5: La versión conforme alternativa no necesita pertenecer al mismo alcance de 
conformidad, ni siquiera al mismo sitio web, que la versión no conforme en la medida en que 
esté disponible tan libremente como la versión no conforme. 
Nota 6: Las versiones alternativas no deben confundirse con contenidos complementarios, que 
sirven de material de apoyo a la página original y mejoran su comprensión. 
Nota 7: Permitir que el usuario establezca sus preferencias sobre el contenido para acceder a 
una versión conforme es un mecanismo aceptable para acceder a otra versión, siempre que el 
método empleado para establecer las preferencias sea compatible con la accesibilidad. 

<!-- Page 22 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
22 
2. Páginas Completas: La conformidad (y el nivel de conformidad) se aplica a páginas web 
completas, y no se puede alcanzar si se excluye una parte de la página. 
• Nota 1: Con el fin de determinar el nivel de conformidad, se considera que las alternativas 
aparte del contenido de una página son parte de esa página si se puede acceder a ellas 
directamente desde la página, por ejemplo, en el caso de una descripción extensa o la 
presentación alternativa de un vídeo. 
• Nota 2: Los autores de las páginas web que no cumplen con los requisitos debido a que 
parte del contenido está fuera de su control, pueden considerar la opción de una 
Declaración de Conformidad Parcial. 
3. Procesos completos: Cuando una página web es parte de una serie de páginas web que 
presentan un proceso (es decir, una secuencia de pasos que es necesario completar para realizar 
una actividad), todas las páginas en ese proceso deben ser conformes con el nivel especificado o 
uno superior. (No es posible lograr conformidad con un nivel en particular si una de las páginas 
del proceso no cumple con ese nivel o uno superior) 
Ejemplo: Una tienda en línea tiene una serie de páginas en las que se pueden seleccionar y 
comprar productos. Todas y cada una de las páginas de la serie de páginas de principio a fin (el 
pago) deben cumplir con los requisitos de conformidad para que se considere que cada una de 
ellas es también conforme. 
4. Uso de tecnologías exclusivamente según métodos que sean compatibles con la accesibilidad: 
Para satisfacer los criterios de conformidad sólo se depende de aquellos usos de las tecnologías 
que sean compatibles con la accesibilidad. Toda información o funcionalidad que se proporcione 
de una forma que no sea compatible con la accesibilidad debe estar disponible de una forma que 
sí sea compatible con la accesibilidad. (Véase Comprender Compatible con la Accesibilidad). 
5. Sin interferencia: Si las tecnologías se usan de una forma que no es compatible con la 
accesibilidad, o está usada de una forma que no cumple los requisitos de conformidad, no debe 
impedir a los usuarios acceder al contenido del resto de la página. Además, es necesario que la 
página web como un todo siga cumpliendo con los requisitos de conformidad en las siguientes 
circunstancias: 
1. Cuando cualquier tecnología de la que no se depende está activada en una aplicación de 
usuario. 
2. Cuando cualquier tecnología de la que no se depende está desactivada en una aplicación de 
usuario. 
3. Cuando cualquier tecnología de la que no se depende no es soportada por una aplicación de 
usuario. 

<!-- Page 23 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
23 
Además, los siguientes criterios de conformidad se aplican a todo el contenido de la página, 
incluyendo el contenido del que, de todos modos, no se depende para alcanzar la conformidad, 
ya que su incumplimiento puede interferir con el uso de la página: 
• 1.4.2 - Control del audio. 
• 2.1.2 - Sin trampas para el foco del teclado. 
• 2.3.1 - Umbral de tres destellos o menos. 
• 2.2.2 - Poner en pausa, detener, ocultar. 
Nota: Si una página no puede cumplir con los requisitos (por ejemplo, una página de prueba de 
conformidad o una página de ejemplo), no puede ser incluida en el ámbito de la conformidad ni en la 
declaración de conformidad. 
 
 
 
 
+ Info 
La conformidad se aplica sólo a las páginas web. Sin embargo, la 
declaración de conformidad puede cubrir una sola página, una serie 
de páginas o múltiples páginas web relacionadas. 
 
3.4. Técnicas suficientes y Técnicas recomendables 
(o de Asesoramiento), y Fallas 
Para cada uno de los criterios de conformidad, se ha documentado una amplia variedad de técnicas 
informativas que se dividen en dos categorías: 
• Aquellas que son suficientes para satisfacer los criterios de conformidad. 
• Aquellas que son de asesoramiento (o recomendables). 
Estas van más allá de los requisitos de cada criterio de conformidad individual, y permiten a los 
desarrolladores afrontar mejor las Pautas. 
Algunas técnicas recomendables tratan sobre barreras de accesibilidad que no han sido 
cubiertas por los criterios de conformidad verificables. 
También se han documentado los errores frecuentes, llamados fallas comunes, que son conocidos. 
Puedes consultar, Técnicas Suficientes y Asesoras en la Comprensión de las WCAG 2.2: 
https://www.w3.org/WAI/WCAG22/Understanding/understanding-techniques 

<!-- Page 24 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
24 
4. Las WCAG. Versiones 
Como ya hemos indicado, las WCAG, son pautas de Accesibilidad al Contenido Web, desarrolladas por 
la WAI del W3C, para las personas con discapacidad. 
Hay diferentes versiones que explicamos a continuación a modo introductorio antes de ver con detalle 
las recomendaciones que se han ido añadiendo en cada versión. 
Resumiendo 
WCAG 1.0 fue publicada como recomendación del W3C el 5 de mayo de 1999. 
WCAG 2.0 se convirtió en recomendación oficial el 11 de diciembre de 2008. 
WCAG 2.1 fue publicada como recomendación del W3C el 5 de junio de 2018. 
WCAG 2.2 fue publicada oficialmente como "W3C Recommendation" el 5 de octubre de 2023. Es una 
versión retro‑compatibles con las versiones anteriores, por lo que cumplir con 2.2 implica también 
cumplir con 2.0 y 2.1, salvo algunas excepciones (como la eliminación del criterio 4.1.1 Parsing). 
Se espera que WCAG 3.0 sea la próxima generación, pero por ahora sigue en fase de desarrollo y no es 
recomendación oficial. 
4.1. WCAG 1.0 
Es una recomendación del 5 de mayo de 1999 del W3C que explica cómo hacer el contenido web 
accesible a las personas con discapacidad, y es reconocido como el estándar de facto a nivel 
internacional en cuanto a accesibilidad web. Es el estándar de iure en muchos países. 
WCAG 1.0, indica 14 pautas que engloban los principios generales del diseño accesible. En total poseen 
65 puntos de verificación y cada uno de ellos está asociado a una prioridad: (A, AA, y AAA). 
1. Proporcionar alternativas equivalentes al contenido sonoro y visual. 
2. No valerse únicamente del color. 
3. Utilizar marcadores y hojas de estilo y hacerlo apropiadamente. 
4. Identificar el idioma usado. 
5. Crear tablas que se transformen correctamente. 
6. Asegurarse de que las páginas que incorporan nuevas tecnologías se transformen 
correctamente. 

<!-- Page 25 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
25 
7. Asegurarse de que el usuario puede controlar los cambios de contenidos en la página. 
8. Asegurar la accesibilidad directa de las interfaces de usuario incrustadas. 
9. Diseñar páginas con independencia del dispositivo. 
10. Utilizar soluciones provisionales. 
11. Utilizar las tecnologías y pautas del W3C. 
12. Proporcionar información de contexto y orientación. 
13. Proporcionar mecanismos claros de navegación. 
14. Asegurarse de que los documentos sean claros y simples. 
Cada pauta tiene uno o más puntos de verificación que explican cómo se aplica la pauta en 
determinadas áreas. En la Tabla de puntos de verificación están todos los puntos de verificación 
ordenados por nivel de prioridad y por elemento del documento (imagen, tabla, marco, etc.) al que 
hace referencia. 
 
Ahora vamos a ver los 65 puntos de verificación, agrupados por niveles de Prioridad. 

<!-- Page 26 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
26 
Prioridad 1 
• En general (Prioridad 1). 
• Proporcione un texto equivalente para todo elemento no textual (Por ejemplo, a través de 
"alt", "longdesc" o en el contenido del elemento). Esto incluye: imágenes, representaciones 
gráficas del texto, mapas de imagen, animaciones (Por ejemplo, GIFs animados), "applets" 
y objetos programados, "ascii art", marcos, scripts, imágenes usadas como viñetas en las 
listas, espaciadores, botones gráficos, sonidos (ejecutados con o sin interacción del 
usuario), archivos exclusivamente auditivos, banda sonora del vídeo y vídeos. 
• Asegúrese de que toda la información transmitida a través de los colores también esté 
disponible sin color, por ejemplo, mediante el contexto o por marcadores. 
• Identifique claramente los cambios en el idioma del texto del documento y en cualquier 
texto equivalente (por ejemplo, leyendas). 
• Organice el documento de forma que pueda ser leído sin hoja de estilo. Por ejemplo, 
cuando un documento HTML es interpretado sin asociarlo a una hoja de estilo, tiene que 
ser posible leerlo. 
• Asegúrese de que los equivalentes de un contenido dinámico son actualizados cuando 
cambia el contenido dinámico. 
• Hasta que las aplicaciones de usuario permitan controlarlo, evite provocar destellos en la 
pantalla. 
• Utilice el lenguaje apropiado más claro y simple para el contenido de un sitio. 
• Y si utiliza imágenes y mapas de imagen (Prioridad 1). 
• Proporcione vínculos redundantes en formato texto para cada zona activa de un mapa de 
imagen del servidor. 
• Proporcione mapas de imagen controlados por el cliente en lugar de por el servidor, 
excepto donde las zonas sensibles no puedan ser definidas con una forma geométrica. 
• Y si utiliza tablas (Prioridad 1). 
• En las tablas de datos, identifique los encabezamientos de fila y columna. 
• Para las tablas de datos que tienen dos o más niveles lógicos de encabezamientos de fila o 
columna, utilice marcadores para asociar las celdas de encabezamiento y las celdas de 
datos. 
• Y si utiliza marcos ("frames") (Prioridad 1). 
• Titule cada marco para facilitar su identificación y navegación. 

<!-- Page 27 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
27 
• Y si utiliza "applets" y "scripts" (Prioridad 1). 
• Asegure que las páginas sigan siendo utilizables cuando se desconecten o no se soporten 
los scripts, applets u otros objetos programados. Si esto no es posible, proporcione 
información equivalente en una página alternativa accesible. 
• Y si utiliza multimedia (Prioridad 1). 
• Hasta que las aplicaciones de usuario puedan leer en voz alta automáticamente el texto 
equivalente de la banda visual, proporcione una descripción auditiva de la información 
importante de la banda visual de una presentación multimedia. 
• Para toda presentación multimedia tempodependiente (por ejemplo, una película o 
animación) sincronice alternativas equivalentes (por ejemplo, subtítulos o descripciones de 
la banda visual) con la presentación. 
• Y si todo lo demás falla (Prioridad 1). 
• Si, después de los mayores esfuerzos, no puede crear una página accesible, proporcione un 
vínculo a una página alternativa que use tecnologías W3C, sea accesible, tenga información 
(o funcionalidad) equivalente y sea actualizada tan a menudo como la página (original) 
inaccesible. 
Prioridad 2 
• En general (Prioridad 2). 
• Asegúrese de que las combinaciones de los colores de fondo y primer plano tengan el 
suficiente contraste para que sean percibidas por personas con deficiencias de percepción 
de color o en pantallas en blanco y negro [Prioridad 2 para las imágenes. Prioridad 3 para 
los textos]. 
• Cuando exista un marcador apropiado, use marcadores en vez de imágenes para transmitir 
la información. 
• Cree documentos que estén validados por las gramáticas formales publicadas. 
• Utilice hojas de estilo para controlar la maquetación y la presentación. 
• Utilice unidades relativas en lugar de absolutas al especificar los valores en los atributos de 
los marcadores de lenguaje y en los valores de las propiedades de las hojas de estilo. 
• Utilice elementos de encabezado para transmitir la estructura lógica y utilícelos de acuerdo 
con la especificación. 
• Marque correctamente las listas y los ítems de las listas. 
• Marque las citas. No utilice el marcador de citas para efectos de formato tales como 
sangrías. 

<!-- Page 28 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
28 
• Asegúrese de que los contenidos dinámicos son accesibles o proporcione una página o 
presentación alternativa. 
• Hasta que las aplicaciones de usuario permitan controlarlo, evite el parpadeo del contenido 
(por ejemplo, cambio de presentación en periodos regulares, así como el encendido y 
apagado). 
• Hasta que las aplicaciones de usuario proporcionen la posibilidad de detener las 
actualizaciones, no cree páginas que se actualicen automáticamente de forma periódica. 
• Hasta que las aplicaciones de usuario proporcionen la posibilidad de detener el 
redireccionamiento automático, no utilice marcadores para redirigir las páginas 
automáticamente. En su lugar, configure el servidor para que ejecute esta posibilidad. 
• Hasta que las aplicaciones de usuario permitan desconectar la apertura de nuevas ventanas, 
no provoque apariciones repentinas de nuevas ventanas y no cambie la ventana actual sin 
informar al usuario. 
• Utilice tecnologías W3C cuando estén disponibles y sean apropiadas para la tarea y use las 
últimas versiones que sean soportadas. 
• Evite características desaconsejadas por las tecnologías W3C. 
• Divida los bloques largos de información en grupos más manejables cuando sea natural y 
apropiado. 
• Identifique claramente el objetivo de cada vínculo. 
• Proporcione metadatos para añadir información semántica a las páginas y sitios. 
• Proporcione información sobre la maquetación general de un sitio (por ejemplo, mapa del 
sitio o tabla de contenidos). 
• Utilice los mecanismos de navegación de forma coherente. 
• Y si utiliza tablas (Prioridad 2). 
• No utilice tablas para maquetar, a menos que la tabla tenga sentido cuando se alinee. Por 
otro lado, si la tabla no tiene sentido, proporcione una alternativa equivalente (la cual debe 
ser una versión alineada). 
• Si se utiliza una tabla para maquetar, no utilice marcadores estructurales para realizar un 
efecto visual de formato. 
• Y si utiliza marcos ("frames") (Prioridad 2). 
• Describa el propósito de los marcos y cómo éstos se relacionan entre sí, si no resulta obvio 
solamente con el título del marco. 

<!-- Page 29 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
29 
• Y si utiliza formularios (Prioridad 2). 
• Hasta que las aplicaciones de usuario soporten explícitamente la asociación entre control 
de formulario y etiqueta, para todos los controles de formularios con etiquetas asociadas 
implícitamente, asegúrese de que la etiqueta está colocada adecuadamente. 
• Asocie explícitamente las etiquetas con sus controles. 
• Y si utiliza "applets" y "scripts" (Prioridad 2). 
• Para los scripts y applets, asegúrese de que los manejadores de eventos sean 
independientes del dispositivo de entrada. 
• Hasta que las aplicaciones de usuario permitan congelar el movimiento de los contenidos, 
evite los movimientos en las páginas. 
• Haga los elementos de programación, tales como scripts y applets, directamente accesibles 
o compatibles con las ayudas técnicas [Prioridad 1 si la funcionalidad es importante y no se 
presenta en otro lugar; de otra manera, Prioridad 2]. 
• Asegúrese de que cualquier elemento que tiene su propia interfaz pueda manejarse de 
forma independiente del dispositivo. 
• Para los "scripts", especifique manejadores de evento lógicos mejor que manejadores de 
evento dependientes de dispositivos. 
Prioridad 3 
• En general (Prioridad 3). 
• Especifique la expansión de cada abreviatura o acrónimo cuando aparezcan por primera vez 
en el documento. 
• Identifique el idioma principal de un documento. 
• Cree un orden lógico para navegar con el tabulador a través de vínculos, controles de 
formulario y objetos. 
• Proporcione atajos de teclado para los vínculos más importantes (incluidos los de los mapas 
de imagen de cliente), los controles de formulario y los grupos de controles de formulario. 
• Hasta que las aplicaciones de usuario (incluidas las ayudas técnicas) interpreten claramente 
los vínculos contiguos, incluya caracteres imprimibles (rodeados de espacios), que no 
sirvan como vínculo, entre los vínculos contiguos. 
• Proporcione la información de modo que los usuarios puedan recibir los documentos según 
sus preferencias (por ejemplo, idioma, tipo de contenido, etc.). 
• Proporcione barras de navegación para destacar y dar acceso al mecanismo de navegación. 
• Agrupe los vínculos relacionados, identifique el grupo (para las aplicaciones de usuario) y, 
hasta que las aplicaciones de usuario lo hagan, proporcione una manera de evitar el grupo. 

<!-- Page 30 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
30 
• Si proporciona funciones de búsqueda, permita diferentes tipos de búsquedas para diversos 
niveles de habilidad y preferencias. 
• Localice la información destacada al principio de los encabezamientos, párrafos, listas, etc. 
• Proporcione información sobre las colecciones de documentos (por ejemplo, los 
documentos que comprendan múltiples páginas). 
• Proporcione un medio para saltar sobre un ASCII art de varias líneas. 
• Complemente el texto con presentaciones gráficas o auditivas cuando ello facilite la 
comprensión de la página. 
• Cree un estilo de presentación que sea coherente para todas las páginas. 
• Y si utiliza imágenes o mapas de imagen (Prioridad 3). 
• Hasta que las aplicaciones de usuario interpreten el texto equivalente para los vínculos de 
los mapas de imagen de cliente, proporcione vínculos de texto redundantes para cada zona 
activa del mapa de imagen de cliente. 
• Y si utiliza tablas (Prioridad 3). 
• Proporcione resúmenes de las tablas. 
• Proporcione abreviaturas para las etiquetas de encabezamiento. 
• Hasta que las aplicaciones de usuario (incluidas las ayudas técnicas) interpreten 
correctamente los textos contiguos, proporcione un texto lineal alternativo (en la página 
actual o en alguna otra) para todas las tablas que maquetan texto en paralelo, en columnas 
de palabras. 
• Y si utiliza formularios (Prioridad 3). 
• Hasta que las aplicaciones de usuario manejen correctamente los controles vacíos, incluya 
caracteres por defecto en los cuadros de edición y áreas de texto. 
 
 
 
 
+ Info 
El W3C proporciona un tutorial de explicaciones y ejemplos para 
ayudar a su entendimiento, en el Curriculum for Web Content 
Accessibility Guidelines 1.0 
http://www.w3.org/WAI/wcag-curric/ 
 

<!-- Page 31 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
31 
4.2. WCAG 2.0 
El 11 de diciembre de 2008, tras años de modificaciones y discusiones sobre el tema, se aprobaron las 
WCAG 2.0. 
Supuso un cambio importante, ya que sus recomendaciones dejaron de estar centradas únicamente en 
HTML y pasaron a aplicarse a todo tipo de contenido y tecnologías web. 
• Principio 1: PERCEPTIBLE. 
• Pauta 1.1 Alternativas textuales. 
» Criterio 1.1.1 Contenido no textual: (A) 
• Pauta 1.2 Medios tempodependientes. 
» Criterio 1.2.1 Sólo audio y sólo vídeo (grabado): (A) 
» Criterio 1.2.2 Subtítulos (grabados): (A) 
» Criterio 1.2.3 Audiodescripción o Medio Alternativo (grabado): (A) 
» Criterio 1.2.4 Subtítulos (en directo): (AA) 
» Criterio 1.2.5 Audiodescripción (grabado): (AA) 
» Criterio 1.2.6 Lengua de signos (grabado): (AAA) 
» Criterio 1.2.7 Audiodescripción ampliada (grabada): (AAA) 
» Criterio 1.2.8 Medio alternativo (grabado): (AAA) 
» Criterio 1.2.9 Sólo audio (en directo): (AAA) 
• Pauta 1.3 Adaptable. 
» Criterio 1.3.1 Información y relaciones: (A) 
» Criterio 1.3.2 Secuencia significativa: (A) 
» Criterio 1.3.3 Características Sensoriales (A) 
• Pauta 1.4 Distinguible. 
» Criterio 1.4.1 Uso del color: (A) 
» Criterio 1.4.2 Control del audio: (A) 

<!-- Page 32 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
32 
» Criterio 1.4.3 Contraste (mínimo): (AA) 
» Criterio 1.4.4 Cambio de tamaño del texto: (AA) 
» Criterio 1.4.5 Imágenes de texto: (AA) 
» Criterio 1.4.6 Contraste (mejorado): (AAA) 
» Criterio 1.4.7 Sonido de fondo bajo o ausente: (AAA) 
» Criterio 1.4.8 Presentación visual: (AAA) 
» Criterio 1.4.9 Imágenes de texto (sin excepciones): (AAA) 
• Principio 2: OPERABLE. 
• Pauta 2.1 Accesible por teclado. 
» Criterio 2.1.1 Teclado: (A) 
» Criterio 2.1.2 Sin trampas para el foco del teclado: (A) 
» Criterio 2.1.3 Teclado (sin excepciones): (AA) 
• Pauta 2.2 Tiempo suficiente. 
» Criterio 2.2.1 Tiempo ajustable: (A) 
» Criterio 2.2.2 Poner en pausa, detener, ocultar: (A) 
» Criterio 2.2.3 Sin tiempo: (AAA) 
» Criterio 2.2.4 Interrupciones: (AAA) 
» Criterio 2.2.5 Re-autentificación: (AAA) 
• Pauta 2.3 Convulsiones. 
» Criterio 2.3.1 Umbral de tres destellos o menos: (A) 
» Criterio 2.3.2 Tres destellos: (AAA) 
• Pauta 2.4 Navegable. 
» Criterio 2.4.1 Evitar bloques: (A) 
» Criterio 2.4.2 Titulado de páginas: (A) 
» Criterio 2.4.3 Orden del foco: (A) 

<!-- Page 33 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
33 
» Criterio 2.4.4 Propósito de los enlaces (en contexto): (A) 
» Criterio 2.4.5 Múltiples vías: (AA) 
» Criterio 2.4.6 Encabezados y etiquetas: (AA) 
» Criterio 2.4.7 Foco visible: (AA) En la versión WCAG 2.2 pasa a nivel A 
» Criterio 2.4.8 Ubicación: (AAA) 
» Criterio 2.4.9 Propósito de los enlaces (sólo enlaces): (AAA) 
» Criterio 2.4.10 Encabezados de sección: (AAA) 
• Principio 3: COMPRENSIBLE. 
• Pauta 3.1 Legible. 
» Criterio 3.1.1 Idioma de la página: (A) 
» Criterio 3.1.2 Idioma de las partes: (AA) 
» Criterio 3.1.3 Palabras inusuales: (AAA) 
» Criterio 3.1.4 Abreviaturas: (AAA) 
» Criterio 3.1.5 Nivel de lectura: (AAA) 
» Criterio 3.1.6 Pronunciación: (AAA) 
• Pauta 3.2 Predecible. 
» Criterio 3.2.1 Al recibir el foco: (A) 
» Criterio 3.2.2 Al recibir entradas: (A) 
» Criterio 3.2.3 Navegación coherente: (AA) 
» Criterio 3.2.4 Identificación coherente: (AA) 
» Criterio 3.2.5 Cambios a petición: (AAA) 
• Pauta 3.3 Entrada de datos asistida. 
» Criterio 3.3.1 Identificación de errores: (A) 
» Criterio 3.3.2 Etiquetas o instrucciones: (A) 
» Criterio 3.3.3 Sugerencias ante errores: (AA) 

<!-- Page 34 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
34 
» Criterio 3.3.4 Prevención de errores (legales, financieros, datos): (AA) 
» Criterio 3.3.5 Ayuda: (AAA) 
» Criterio 3.3.6 Prevención de errores (todos): (AAA) 
• Principio 4: ROBUSTO. 
• Pauta 4.1 Compatible. 
» Criterio 4.1.1 Procesamiento- Análisis sintáctico (Parsing): (A)  
» Criterio 4.1.2 Nombre, función (rol), valor: (A) 
Lo estudiamos con más detalle en otro apartado. 
 
 
 
 
Atención 
WCAG 2.0 es ISO/IEC 40500:2012 
Es decir, ISO/IEC 40500:2012 recoge las pautas de accesibilidad 
web WCAG 2.0 
El contenido de ISO/IEC 40500 está disponible gratuitamente en: 
https://www.w3.org/TR/WCAG20/ 
También puede ser comprado en el catálogo ISO: 
https://www.iso.org/standard/58625.html 
 
4.3. WCAG 2.1 
Después de casi 10 años desde la publicación de WCAG 2.0, el 5 de junio de 2018 se publicó la 
recomendación definitiva de las WCAG 2.1. 
Contiene 17 nuevos criterios, que indicamos a continuación: 
• 7 criterios en el Principio 1 Perceptible. 
• 3 criterios en la Pauta 1.3 Adaptable, que son: 
» 1.3.4 Orientación (AA) 
» 1.3.5 Identificar el propósito de entrada (AA) 
» 1.3.6 Identificar el propósito (AAA) 

<!-- Page 35 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
35 
• 4 criterios en la Pauta 1.4 Distinguible, que son: 
» 1.4.10 Reflujo (AA) 
» 1.4.11 Contraste no textual (AA) 
» 1.4.12 Espaciado de texto (AA) 
» 1.4.13 Contenido en puntero flotante o foco (Hover o Focus) (AA) 
• 9 criterios en el principio 2 Operable. 
• 1 criterio en la Pauta 2.1 Accesible por teclado, que es: 
» 2.1.4 Atajos de teclas de carácter (A) 
• 1 criterio en la Pauta 2.2 Tiempo suficiente, que es: 
» 2.2.6 Timeouts (AAA) 
• 1 criterio en la Pauta 2.3 Convulsiones, que es: 
» 2.3.3 Animación de interacciones (AAA) 
• 6 de ellos en una nueva pauta: Pauta 2.5 Modalidades de entrada: 
» 2.5.1 Gestos de puntero (A) 
» 2.5.2 Cancelación de puntero (A) 
» 2.5.3 Etiqueta en el nombre (A) 
» 2.5.4 Activación por movimiento (A) 
» 2.5.5 Tamaño objetivo (AAA) 
» 2.5.6 Mecanismos de entrada simultáneos (AAA) 
• 1 criterio en el principio 4 Robusto. 
• En la Pauta 4.1 Compatible, que es: 
» 4.1.3 Mensajes de estado (AA) 
 

<!-- Page 36 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
36 
 
 
 
Atención 
Consulta toda la información en la web oficial de W3C: 
https://www.w3.org/WAI/WCAG21/quickref/ 
https://www.w3.org/WAI/standards-guidelines/wcag/new-in-
21/es 
 
4.4. WCAG 2.2 
La versión de las Pautas de Accesibilidad para el Contenido Web (Web Content Accessibility Guidelines, 
WCAG 2.2) que fue publicada en octubre del año 23, añade 9 criterios adicionales con respecto a la 
versión anterior. 
Los nuevos criterios de éxito observan: 
• La visibilidad y apariencia del foco del cursor, 2.4.11, 2.4.12, 2.4.13. 
• La trayectoria de arrastre de elementos (especialmente en dispositivos móviles), 2.5.7. 
• Se agrega al criterio 2.5.5 el término enhanced (mejorado) pues aparece el criterio 2.5.8, ambos 
apuntan al tamaño mínimo de los elementos interactivos, pero con distinto nivel de exigencia 
AAA y AA respectivamente. 
• La consistencia y accesibilidad de la ayuda, 3.2.6. 
• La eliminación de redundancias en la captación de información del usuario, 3.3.7. 
• La accesibilidad de los procesos de autenticación para personas con diversas capacidades, 3.3.8, 
3.3.9. 
Igual que con las versiones anteriores, los sitios que cumplen con WCAG 2.2 también cumplen con 
WCAG 2.0 y WCAG 2.1. 
Aunque en el listado de pautas y criterios que veremos posteriormente aparece indicado, vemos aquí 
los cambios de la versión 2.2, de forma resumida, para destacarlo: 
• Se ha eliminado el criterio de conformidad 4.1.1 Procesamiento-Análisis sintáctico de nivel A 
(Principio 4 Robusto, Pauta 4.1 Compatible) 

<!-- Page 37 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
37 
• Criterios Añadidos: 
• En Principio 2 Operable, Pauta 2.4 Navegable, añadidos: 
» 2.4.11 Aspecto de foco (AA) 
» 2.4.12 Foco no oscurecido (AA) 
» 2.4.13 Foco no oscurecido (mejorado) (AAA) 
• En Principio 2 Operable, Pauta 2.5 Modalidades de entrada, añadidos: 
» 2.5.7 Movimientos de Arrastre (AA) 
» 2.5.8 Tamaño del objetivo (mínimo) (AA) 
• En Principio 3 Comprensible, Pauta 3.2 Predecible, añadidos: 
» 3.2.6 Ayuda consistente (A) 
» Pauta 3.3 Entrada de datos asistida: 
» 3.3.7 Autenticación Accesible (AA) 
» 3.3.8 Autenticación accesible (mejorada) (AAA) 
» 3.3.9 Entrada redundante (A) 
 
 
 
 
Atención 
Puedes consultar la web oficial sobre WCAG 2.2  
https://www.w3.org/TR/WCAG22/ 
https://www.w3.org/TR/ 
 
BORRADOR WCAG 3.0 
La versión WCAG 3.0 está ahora mismo en una fase desarrollo que incluye distintos niveles de madurez 
para las distintas secciones del estándar. Algunas secciones pueden estar en etapas más avanzadas de 
desarrollo, mientras que otras aún están en fases preliminares. 

<!-- Page 38 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
38 
Según parece la idea es cambiar de enfoque, del enfoque prescriptivo tradicional, basado en reglas y 
criterios específicos al enfoque basado en resultados. Si bien se menciona que las directrices estarán 
respaldadas por resultados y los métodos tecnológicos adecuados, no existe demasiada información 
que indique cual será la manera de proceder. 
A continuación, dejamos el enlace al borrador de las pautas de accesibilidad en su versión 3.0 
https://www.w3.org/TR/wcag3/. 
Recomendamos la lectura y comprensión de los enlaces facilitados en esta página, enlaces oficiales de 
las recomendaciones W3C. 
5. Las WCAG 2.X - Pautas y sus criterios 
Nos referimos aquí a las versiones WCAG 2.0, WCAG 2.1 y WCAG 2.2. 
Ya hemos indicado que las pautas están por debajo de los 4 principios generales (perceptible, operable, 
comprensible y robusto), y que la pautas proporcionan los objetivos básicos que los desarrolladores 
deben lograr con el fin de crear un contenido más accesible para los usuarios con distintas 
discapacidades. 
Las pautas en sí mismas no son verificables directamente: la verificación se realiza a través de los 
criterios de conformidad asociados a cada pauta, que sí son comprobables y que establecen el nivel de 
conformidad (A, AA o AAA). 
Vamos a ver: 
• Las Pautas (que son normativa), indicadas, dentro del principio al que pertenecen: 
• Por cada Pauta, sus criterios de conformidad, indicando entre paréntesis el nivel de 
conformidad. 
• En cada criterio se indica si se ha añadido en WCAG 2.1, o modificado, eliminado o añadido 
en WCAG 2.2. 
5.1. Pautas Principio 1: Perceptible 
(La información y los componentes de la interfaz de usuario deben ser presentados a los usuarios de 
modo que ellos puedan percibirlos.) 
5.1.1. Pauta 1.1 Alternativas textuales 
Proporcionar alternativas textuales para todo contenido no textual de modo que se pueda modificar 
(convertir a otros formatos) para ajustarse a las personas que lo necesiten, como textos ampliados, 
braille, lenguaje oral (voz), símbolos o en un lenguaje más simple. 

<!-- Page 39 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
39 
• 1.1.1 Contenido no textual: (A) 
Todo contenido no textual que se presenta al usuario tiene una alternativa textual que cumple 
el mismo propósito, excepto en las situaciones enumeradas a continuación: 
• Controles, Entrada de datos: 
Si el contenido no textual es un control o acepta datos introducidos por el usuario, 
entonces tiene un nombre que describe su propósito. (Véase la Pauta 4.1 para requisitos 
adicionales sobre los controles y el contenido que aceptan entrada de datos). 
• Contenido multimedia tempodependiente: 
Si el contenido no textual es una presentación multimedia con desarrollo temporal, 
entonces las alternativas textuales proporcionan al menos una identificación descriptiva del 
contenido no textual. (Véase la Pauta 1.2 para requisitos adicionales sobre contenido 
multimedia). 
• Pruebas: 
Si el contenido no textual es una prueba o un ejercicio que no sería válido si se presentara 
en forma de texto, entonces las alternativas textuales proporcionan al menos una 
identificación descriptiva del contenido no textual. 
• Sensorial: 
Si el contenido no textual tiene como objetivo principal el crear una experiencia sensorial 
específica, entonces las alternativas textuales proporcionan al menos una identificación 
descriptiva del contenido no textual. 
• CAPTCHA: 
Si el propósito del contenido no textual es confirmar que quien está accediendo al 
contenido es una persona y no una computadora, entonces se proporcionan alternativas 
textuales que identifican y describen el propósito del contenido no textual y se 
proporcionan formas alternativas de CAPTCHA con modos de salida para distintos tipos de 
percepciones sensoriales, con el fin de acomodarse a las diferentes discapacidades. 
• Decoración, Formato, Invisible: 
Si el contenido no textual es simple decoración, se utiliza únicamente para definir el 
formato visual o no se presenta a los usuarios, entonces se implementa de forma que pueda 
ser ignorado por las ayudas técnicas. 

<!-- Page 40 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
40 
5.1.2. Pauta 1.2 Medios tempodependientes 
Proporcionar alternativas para los medios tempodependientes, (alternativas para contenidos 
multimedia sincronizados dependientes del tiempo. 
• 1.2.1 Sólo audio y sólo vídeo (grabado): (A) 
Para contenido sólo audio grabado y contenido sólo vídeo grabado, se cumple lo siguiente, 
excepto cuando el audio o el vídeo es un contenido multimedia alternativo al texto y está 
claramente identificado como tal: 
• Sólo audio grabado: 
Se proporciona una alternativa para los medios tempodependientes que presenta 
información equivalente para el contenido sólo audio grabado. 
• Sólo vídeo grabado: 
Se proporciona una alternativa para los medios tempodependientes o se proporciona una 
pista sonora que presenta información equivalente al contenido del medio de sólo vídeo 
grabado. 
• 1.2.2 Subtítulos (grabados): (A) 
Se proporcionan subtítulos para el contenido de audio grabado dentro de contenido multimedia 
sincronizado, excepto cuando la presentación es un contenido multimedia alternativo al texto y 
está claramente identificado como tal. 
• 1.2.3 Audiodescripción o Medio Alternativo (grabado): (A) 
Se proporciona una alternativa para los medios tempodependientes o una audiodescripción para 
el contenido de vídeo grabado en los multimedia sincronizados, excepto cuando ese contenido 
es un contenido multimedia alternativo al texto y está claramente identificado como tal. 
• 1.2.4 Subtítulos (en directo): (AA) 
Se proporcionan subtítulos para todo el contenido de audio en directo de los multimedia 
sincronizados. 
• 1.2.5 Audiodescripción (grabado): (AA) 
Se proporciona una audiodescripción para todo el contenido de vídeo grabado dentro de 
contenido multimedia sincronizado. 
• 1.2.6 Lengua de señas (grabado): (AAA) 
Se proporciona una interpretación en lengua de señas para todo el contenido de audio grabado 
dentro de contenido multimedia sincronizado. 

<!-- Page 41 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
41 
• 1.2.7 Audiodescripción ampliada (grabada): (AAA) 
Cuando las pausas en el audio de primer plano son insuficientes para permitir que la 
audiodescripción comunique el significado del vídeo, se proporciona una audiodescripción 
ampliada para todos los contenidos de vídeo grabado dentro de contenido multimedia 
sincronizado. 
• 1.2.8 Medio alternativo (grabado): (AAA) 
Se proporciona una alternativa para los medios tempodependientes, tanto para todos los 
contenidos multimedia sincronizados grabados como para todos los medios de sólo vídeo 
grabado. 
• 1.2.9 Sólo audio (en directo): (AAA) 
Se proporciona una alternativa para los medios tempodependientes que presenta información 
equivalente para el contenido de sólo audio en directo. 
5.1.3. Pauta 1.3 Adaptable 
Crear contenido que pueda presentarse de diferentes formas (por ejemplo, con una disposición más 
simple) sin perder información o estructura. 
• 1.3.1 Información y relaciones: (A) 
La información, estructura y relaciones comunicadas a través de la presentación pueden ser 
determinadas por software o están disponibles como texto. 
• 1.3.2 Secuencia significativa: (A) 
Cuando la secuencia en que se presenta el contenido afecta a su significado, se puede 
determinar por software la secuencia correcta de lectura. 
• 1.3.3 Características sensoriales: (A) 
Las instrucciones proporcionadas para entender y operar el contenido no dependen 
exclusivamente en las características sensoriales de los componentes como su forma, tamaño, 
ubicación visual, orientación o sonido. 
• 1.3.4 Orientación: (Nivel AA) - Añadido en WCAG 2.1. 
El contenido no restringe su vista y funcionamiento a una única orientación de pantalla, como 
vertical u horizontal, a menos que sea esencial una orientación de visualización específica. 

<!-- Page 42 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
42 
• 1.3.5 Identificar el propósito de entrada: (Nivel AA) - Añadido en WCAG 2.1. 
El propósito de cada campo de entrada que recopila información sobre el usuario se puede 
determinar mediante programación cuando: 
• El campo de entrada sirve para un propósito identificado en la sección Propósitos de 
entrada para componentes de interfaz de usuario. 
• El contenido se implementa utilizando tecnologías con soporte para identificar el 
significado esperado para los datos de entrada de formularios. 
• 1.3.6 Identificar el propósito: (Nivel AAA) - Añadido en WCAG 2.1. 
En el contenido implementado mediante lenguajes de marcado, el propósito de los 
componentes, iconos y regiones de la interfaz de usuario se puede determinar mediante 
programación. 
5.1.4. Pauta 1.4 Distinguible 
Facilitar a los usuarios ver y oír el contenido, incluyendo la separación entre el primer plano y el fondo, 
(entre lo más y menos importante). 
• 1.4.1 Uso del color: (A) 
El color no se usa como único medio visual para transmitir la información, indicar una acción, 
solicitar una respuesta o distinguir un elemento visual. 
 
 
 
 
Nota 
Este criterio de conformidad trata específicamente acerca de la 
percepción del color. En la Pauta 1.3 se recogen otras formas de 
percepción, incluyendo el acceso por software al color y a otros 
códigos de presentación visual. 
 
 
• 1.4.2 Control del audio: (A) 
Si el audio de una página web suena automáticamente durante más de 3 segundos, se 
proporciona ya sea un mecanismo para pausar o detener el audio, o un mecanismo para 
controlar el volumen del sonido, que es independiente del nivel de volumen global del sistema. 

<!-- Page 43 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
43 
 
 
 
Nota 
En la medida en que cualquier contenido que no satisfaga este 
criterio puede interferir con la capacidad del usuario de emplear la 
página en su conjunto, todo contenido de la página web (tanto si 
satisface o no otros criterios de conformidad) debe satisfacer este 
criterio. Véase Requisito de Conformidad 5: Sin interferencia. 
 
 
• 1.4.3 Contraste (mínimo): (AA) 
La presentación visual de texto e imágenes de texto tiene una relación de contraste de, al 
menos, 4.5:1, excepto en los siguientes casos: 
• Textos grandes: 
Los textos de gran tamaño y las imágenes de texto de gran tamaño tienen una relación de 
contraste de, al menos, 3:1. 
• Incidental: 
Los textos o imágenes de texto que forman parte de un componente inactivo de la interfaz 
de usuario, que son simple decoración, que no resultan visibles para nadie o forman parte 
de una imagen que contiene otros elementos visuales significativos, no tienen requisitos de 
contraste. 
• Logotipos: 
El texto que forma parte de un logo o nombre de marca no tiene requisitos de contraste 
mínimo. 
• 1.4.4 Cambio de tamaño del texto: (AA) 
A excepción de los subtítulos y las imágenes de texto, todo el texto puede ser ajustado sin 
ayudas técnicas hasta un 200 por ciento sin que se pierdan el contenido o la funcionalidad. 
• 1.4.5 Imágenes de texto: (AA) 
Si con las tecnologías que se están utilizando se puede conseguir la presentación visual deseada, 
se utiliza texto para transmitir la información en vez de imágenes de texto, excepto en los 
siguientes casos. 
• Configurable: 
La imagen de texto es visualmente configurable según los requisitos del usuario. 

<!-- Page 44 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
44 
• Esencial: 
Una forma particular de presentación del texto resulta esencial para la información que se 
transmite. 
Nota: Los logotipos (textos que son parte de un logo o de un nombre de marca) se 
consideran esenciales. 
• 1.4.6 Contraste (mejorado): (AAA) 
La presentación visual de texto e imágenes de texto tiene una relación de contraste de, al 
menos, 7:1, excepto en los siguientes casos. 
• Textos grandes: 
Los textos de gran tamaño y las imágenes de texto de gran tamaño tienen una relación de 
contraste de, al menos, 4.5:1. 
• Incidental: 
Los textos o imágenes de texto que forman parte de un componente de la interfaz de 
usuario inactivo, que son simple decoración, que no resultan visibles para nadie o forman 
parte de una imagen que contiene otros elementos visuales significativos, no tienen 
requisitos de contraste. 
• Logotipos: 
El texto que forma parte de un logo o nombre de marca no tiene requisitos de contraste 
mínimo. 
• 1.4.7 Sonido de fondo bajo o ausente: (AAA) 
Para el contenido de sólo audio grabado que (1) contiene habla en primer plano, (2) no es un 
CAPTCHA sonoro o un audiologo, y (3) que no es una vocalización cuya intención principal es 
servir como expresión musical (como el canto o el rap), se cumple al menos uno de los 
siguientes casos: 
• Ningún sonido de fondo: 
El audio no contiene sonidos de fondo. 
• Apagar: 
Los sonidos de fondo pueden ser apagados. 
• 20 dB: 
Los sonidos de fondo son, al menos, 20 decibelios más bajos que el discurso en primer 
plano, con la excepción de sonidos ocasionales que duran solamente uno o dos segundos. 
Nota: Por la definición de "decibelio", el sonido de fondo que cumple con este requisito es 
aproximadamente cuatro veces más silencioso que la locución principal. 

<!-- Page 45 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
45 
• 1.4.8 Presentación visual: (AAA) 
En la presentación visual de bloques de texto, se proporciona algún mecanismo para lograr lo 
siguiente: 
1. Los colores de fondo y primer plano pueden ser elegidos por el usuario. 
2. El ancho no es mayor de 80 caracteres o signos (40 si es CJK). 
3. El texto no está justificado (alineado a los márgenes izquierdo y derecho a la vez). 
4. El espacio entre líneas (interlineado) es de, al menos, un espacio y medio dentro de los 
párrafos y el espacio entre párrafos es, al menos, 1.5 veces mayor que el espacio entre 
líneas. 
5. El texto se ajusta sin ayudas técnicas hasta un 200 por ciento de modo tal que no requiere 
un desplazamiento horizontal para leer una línea de texto en una ventana a pantalla 
completa. 
• 1.4.9 Imágenes de texto (sin excepciones): (AAA) 
Las imágenes de texto sólo se utilizan como simple decoración o cuando una forma de 
presentación particular del texto resulta esencial para la información transmitida. (Nivel AAA). 
Nota: Los logotipos (textos que son parte de un logo o de un nombre de marca) se consideran 
esenciales. 
• 1.4.10 Reflujo: (AA) - Añadido en WCAG 2.1. 
El contenido se puede presentar sin pérdida de información o funcionalidad, y sin necesidad de 
desplazarse en dos dimensiones para: 
• Contenido de desplazamiento vertical a un ancho equivalente a 320 píxeles CSS. 
• Contenido de desplazamiento horizontal a una altura equivalente a 256 píxeles CSS. 
Excepto para las partes del contenido que requieren un diseño bidimensional para su uso o 
significado. 
• 1.4.11 Contraste no text: (AA) - Añadido en WCAG 2.1. 
La presentación visual de lo siguiente tiene una relación de contraste de al menos 3:1 contra los 
colores adyacentes: 
• Componentes de la interfaz de usuario: Información visual necesaria para identificar 
componentes y estados de la interfaz de usuario, excepto para componentes inactivos o 
cuando la apariencia del componente es determinada por el agente de usuario y no 
modificada por el autor. 
• Objetos gráficos: Partes de gráficos necesarias para comprender el contenido, excepto 
cuando una presentación particular de gráficos es esencial para la información que se 
transmite. 

<!-- Page 46 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
46 
• 1.4.12 Espaciado de texto: (AA) - Añadido en WCAG 2.1. 
En el contenido implementado mediante lenguajes de marcado que admiten las siguientes 
propiedades de estilo de texto, no se produce ninguna pérdida de contenido o funcionalidad al 
establecer todo lo siguiente y al no cambiar ninguna otra propiedad de estilo: 
• Altura de línea (interlineado) a al menos 1,5 veces el tamaño de fuente. 
• Espaciar los párrafos siguientes a al menos 2 veces el tamaño de la fuente. 
• Espaciado de letras (seguimiento) a al menos 0,12 veces el tamaño de fuente. 
• Espaciado de palabras a al menos 0,16 veces el tamaño de fuente. 
Excepción: los lenguajes humanos y los scripts que no utilizan una o más de estas propiedades 
de estilo de texto en el texto escrito pueden conformarse utilizando solo las propiedades que 
existen para esa combinación de lenguaje y script. 
• 1.4.13 Contenido en puntero flotante o foco (Hover o Focus): (AA) - Añadido en WCAG 2.1. 
Cuando recibir y, a continuación, quitar el puntero o el enfoque del teclado desencadena 
contenido adicional para que se vuelva visible y, a continuación, oculto, se cumple lo siguiente: 
• Descartable: Hay un mecanismo disponible para descartar el contenido adicional sin mover 
el puntero o el enfoque del teclado, a menos que el contenido adicional comunique un error 
de entrada o no oscurezca o reemplace otro contenido. 
• Superponible: Si el desplazamiento del puntero puede activar el contenido adicional, 
entonces el puntero se puede mover sobre el contenido adicional sin que el contenido 
adicional desaparezca. 
• Persistente: El contenido adicional permanece visible hasta que se elimina el botón de 
desplazamiento o enfoque, el usuario lo descarta o su información ya no es válida. 
Excepción: La presentación visual del contenido adicional es controlada por el agente de usuario 
y no es modificada por el autor. 
5.2. Pautas Principio 2: Operable 
Los componentes de la interfaz de usuario y la navegación deben ser operables. 
La operabilidad es un principio fundamental de la accesibilidad web que exige que los componentes y la 
navegación de la interfaz de usuario sean utilizables por cualquier persona usuaria. 

<!-- Page 47 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
47 
5.2.1. Pauta 2.1 Accesible por teclado 
Proporcionar acceso a toda la funcionalidad mediante el teclado: 
• 2.1.1 Teclado: (A) 
Toda la funcionalidad del contenido es operable a través de una interfaz de teclado sin que se 
requiera una determinada velocidad para cada pulsación individual de las teclas, excepto cuando 
la función interna requiere de una entrada que depende del trayecto de los movimientos del 
usuario y no sólo de los puntos inicial y final. 
Nota 1: Esta excepción se refiere a la función subyacente, no a la técnica de entrada de datos. Por 
ejemplo, si la entrada de texto se hace por medio de escritura a mano, la técnica de entrada 
(escritura a mano) depende del trazo (ruta trazada) pero la función interna (introducir texto) no. 
Nota 2: Esto no prohíbe ni debería desanimar a los autores a proporcionar entrada de ratón u 
otros métodos de entrada de datos adicionales a la operabilidad a través del teclado. 
• 2.1.2 Sin trampas para el foco del teclado: (A) 
Si es posible mover el foco a un componente de la página usando una interfaz de teclado, 
entonces el foco se puede quitar de ese componente usando sólo la interfaz de teclado y, si se 
requiere algo más que las teclas de dirección o de tabulación, se informa al usuario el método 
apropiado para mover el foco. 
Nota: En la medida en que cualquier contenido que no satisfaga este criterio puede interferir 
con la capacidad del usuario para emplear la página por completo, todo contenido de la página 
web (tanto si satisface o no otros criterios de conformidad) debe satisfacer este criterio. 
• 2.1.3 Teclado (sin excepciones): (AAA) 
Toda la funcionalidad del contenido se puede operar a través de una interfaz de teclado sin 
requerir una determinada velocidad en la pulsación de las teclas. 
• 2.1.4 Atajos de teclas de carácter: (A) - Añadido en WCAG 2.1. 
Si se implementa un método abreviado de teclado en el contenido utilizando solo letras 
(incluidas las letras mayúsculas y minúsculas), signos de puntuación, números o caracteres de 
símbolo, se cumple al menos una de las siguientes condiciones: 
• Apagar: Hay un mecanismo disponible para desactivar el acceso directo. 
• Reasignar: Hay un mecanismo disponible para reasignar el acceso directo para incluir una o 
más teclas de teclado no imprimibles (por ejemplo, Ctrl, Alt). 
• Activo solo en el enfoque: El método abreviado de teclado para un componente de interfaz 
de usuario solo está activo cuando ese componente tiene foco. 

<!-- Page 48 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
48 
5.2.2. Pauta 2.2 Tiempo suficiente 
Proporcionar a los usuarios el tiempo suficiente para leer y usar el contenido. 
• 2.2.1 Tiempo ajustable: (A) 
Para cada límite de tiempo impuesto por el contenido, se cumple al menos uno de los siguientes 
casos: 
• Apagar: 
El usuario puede detener el límite de tiempo antes de alcanzar el límite de tiempo. 
• Ajustar: 
El usuario puede ajustar el límite de tiempo antes de alcanzar dicho límite en un rango 
amplio que es, al menos, diez veces mayor al tiempo fijado originalmente. 
• Extender: 
Se advierte al usuario antes de que el tiempo expire y se le conceden al menos 20 segundos 
para extender el límite temporal con una acción simple (por ejemplo, "presione la barra de 
espacio") y el usuario puede extender ese límite de tiempo al menos diez veces. 
• Excepción de tiempo real: 
El límite de tiempo es un requisito que forma parte de un evento en tiempo real (por 
ejemplo, una subasta) y no resulta posible ofrecer una alternativa al límite de tiempo. 
• Excepción por ser esencial: 
El límite de tiempo es esencial y, si se extendiera, invalidaría la actividad. 
• Excepción de 20 horas: 
El límite de tiempo es mayor a 20 horas. 
Nota: Este criterio de conformidad (2.2.1 Tiempo ajustable), ayuda a asegurarse de que los 
usuarios puedan completar una tarea sin cambios inesperados en el contenido o contexto que 
sean el resultado de un límite de tiempo. Este criterio de conformidad debe considerarse en 
combinación con el Criterio de Conformidad 3.2.1, que impone límites a los cambios de 
contenido o contexto como resultado de una acción del usuario. 

<!-- Page 49 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
49 
• 2.2.2 Poner en pausa, detener, ocultar: (A) 
Para la información que tiene movimiento, parpadeo, se desplaza o se actualiza 
automáticamente, se cumplen todos los casos siguientes: 
• Movimiento, parpadeo, desplazamiento: 
Para toda información que se mueve, parpadea o se desplaza, que (1) comienza 
automáticamente, (2) dura más de cinco segundos y (3) se presenta en paralelo con otro 
contenido, existe un mecanismo para que el usuario la pueda poner en pausa, detener u 
ocultar, a menos que el movimiento, parpadeo o desplazamiento sea parte esencial de una 
actividad. 
• Actualización automática: 
Para toda información que se actualiza automáticamente, que (1) se inicia 
automáticamente y (2) se presenta en paralelo con otro contenido, existe un mecanismo 
para que el usuario la pueda poner en pausa, detener u ocultar, o controlar la frecuencia de 
actualización a menos que la actualización automática sea parte esencial de una actividad. 
Nota 1: Para los requisitos relacionados con el parpadeo o el destello de contenido, véase la 
Pauta 2.3. 
Nota 2: En la medida en que cualquier contenido que no satisfaga este criterio puede interferir 
con la capacidad del usuario para emplear la página como un todo, todo contenido de la página 
web (tanto si satisface o no otros criterios de conformidad) debe satisfacer este criterio. Véase 
Requisito de Conformidad 5: Sin interferencia. 
Nota 3: Para el contenido que es actualizado periódicamente por medio de un software, o que 
se sirve a la aplicación de usuario por medio de streaming, no hay obligación de preservar o 
presentar la información que ha sido generada o recibida entre el inicio de la pausa y el reinicio 
de la presentación; no sólo podría no ser técnicamente posible, sino que además en muchas 
ocasiones podría ser erróneo o engañoso hacerlo. 
Nota 4: Una animación que ocurre como parte de una fase de precarga de un contenido o una 
situación similar puede ser considerada esencial si no se permite interacción a ningún usuario 
durante esa fase, y si el hecho de no indicar el progreso pudiera confundir a los usuarios y 
hacerles creer que ha habido un fallo en el contenido. 
• 2.2.3 Sin tiempo: (AAA) 
El tiempo no es parte esencial del evento o actividad presentada por el contenido, exceptuando 
los multimedia sincronizados no interactivos y los eventos en tiempo real. 
• 2.2.4 Interrupciones: (AAA) 
El usuario puede postergar o suprimir las interrupciones, excepto cuando las interrupciones 
implican una emergencia. 

<!-- Page 50 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
50 
• 2.2.5 Re-autentificación: (AAA) 
Cuando expira una sesión autentificada, el usuario puede continuar la actividad sin pérdida de 
datos tras volver a identificarse. 
• 2.2.6 Timeouts: (AAA) - Añadido en WCAG 2.1. 
Se advierte a los usuarios de la duración de cualquier inactividad del usuario que pueda causar la 
pérdida de datos, a menos que los datos se conserven durante más de 20 horas cuando el 
usuario no realice ninguna acción. 
5.2.3. Pauta 2.3 Convulsiones 
No diseñar contenido de un modo que se sepa podría provocar ataques, espasmos o convulsiones. 
• 2.3.1 Umbral de tres destellos o menos: (A) 
Las páginas web no contienen nada que destelle más de tres veces en un segundo, o el destello 
está por debajo del umbral de destello general y de destello rojo. 
Nota: En la medida en que cualquier contenido que no satisfaga este criterio puede interferir 
con la capacidad del usuario para emplear la página como un todo, todo contenido de la página 
web (tanto si satisface o no otros criterios de conformidad) debe satisfacer este criterio. Véase 
Requisito de Conformidad 5: Sin interferencia. 
• 2.3.2 Tres destellos: (AAA) 
Las páginas web no contienen nada que destelle más de tres veces por segundo. 
• 2.3.3 Animación de interacciones: (AAA) - Añadido en WCAG 2.1. 
La animación de movimiento desencadenada por la interacción se puede desactivar, a menos 
que la animación sea esencial para la funcionalidad o la información que se transmite. 
5.2.4. Pauta 2.4 Navegable 
Proporcionar medios para ayudar a los usuarios a navegar, encontrar contenido y determinar dónde se 
encuentran. 
• 2.4.1 Evitar bloques: (A) 
Existe un mecanismo para evitar los bloques de contenido que se repiten en múltiples páginas 
web. 
• 2.4.2 Titulado de páginas: (A) 
Las páginas web tienen títulos que describen su temática o propósito. 

<!-- Page 51 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
51 
• 2.4.3 Orden del foco: (A) 
Si se puede navegar secuencialmente por una página web y la secuencia de navegación afecta su 
significado o su operación, los componentes que pueden recibir el foco lo hacen en un orden 
que preserva su significado y operabilidad. 
• 2.4.4 Propósito de los enlaces (en contexto): (A) 
El propósito de cada enlace puede ser determinado con sólo el texto del enlace o a través del 
texto del enlace sumado al contexto del enlace determinado por software, excepto cuando el 
propósito del enlace resultara ambiguo para los usuarios en general. 
• 2.4.5 Múltiples vías: (AA) 
Se proporciona más de un camino para localizar una página web dentro de un conjunto de 
páginas web, excepto cuando la página es el resultado, o un paso intermedio, de un proceso. 
• 2.4.6 Encabezados y etiquetas: (AA) 
Los encabezados y etiquetas describen el tema o propósito. 
• 2.4.7 Foco visible: (AA) 
Cualquier interfaz de usuario operable por teclado tiene una forma de operar en la cual el 
indicador del foco del teclado resulta visible. 
• 2.4.8 Ubicación: (AAA) 
Se proporciona información acerca de la ubicación del usuario dentro de un conjunto de páginas 
web. 
• 2.4.9 Propósito de los enlaces (sólo enlaces): (AAA) 
Se proporciona un mecanismo que permite identificar el propósito de cada enlace con sólo el 
texto del enlace, excepto cuando el propósito del enlace resultara ambiguo para los usuarios en 
general. 
• 2.4.10 Encabezados de sección: (AAA) 
Se usan encabezados de sección para organizar el contenido. 
Nota 1: "Encabezados" se usa en sentido general e incluye los títulos y otras formas de agregar 
encabezados a los distintos tipos de contenido. 
Nota 2: Este criterio de conformidad se refiere al contenido propiamente dicho, no a los 
componentes de la interfaz de usuario. Los componentes de la interfaz de usuario se tratan en 
el Criterio de Conformidad 4.1.2. 

<!-- Page 52 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
52 
• 2.4.11: Apariencia de enfoque (Focus Appearance): (AA) añadida en WCAG 2.2 
Complementa a los criterios 2.4.7 y 1.4.11 
El criterio 2.4.7 Foco visible, que en WCAG 2.2 pasa a ser de nivel A, exige que el foco de teclado 
sea visible. Este nuevo criterio 2.4.11, tiene como objetivo complementarlo, asegurando que el 
foco de teclado sea además claramente visible y discernible, para lo que este nuevo criterio 
define un nivel mínimo de visibilidad, basado en el tamaño y en el contraste. 
El criterio 1.4.11 Contraste no textual AA, de WCAG 2.1, requiere además que el foco de 
teclado tenga al menos un contraste de 3:1, y que un componente de interacción tenga un 
contraste adecuado con el fondo, tanto en su estado por defecto como en su estado con el 
foco. Con este nuevo criterio 2.4.11, se complementa requiriendo un contraste suficiente entre 
los dos estados del componente, su estado con el foco y su estado sin el foco. 
El nuevo criterio 2.4.11 especifica que, cuando el indicador del foco de teclado es visible, uno o 
ambos de estos 2 requisitos se cumplen: 
• Requisito 1: Todo el indicador del foco cumple tres condiciones: 
» Rodea al componente que tiene el foco. Se refiere a un borde sólido, normalmente un 
recuadro, pero que también puede tener la forma del elemento (por ejemplo, forma de 
estrella). Para esta condición no se admite el borde puntuado. 
» Hay una ratio de contraste de al menos 3:1 entre los mismos píxeles en su estado con y 
sin el foco. 
» Hay una ratio de contraste de al menos 3:1 con los colores adyacentes que no forman 
parte del indicador del foco. Por ejemplo, si una estrella al coger el foco tiene un 
borde negro pegado a la estrella, este debe contrastar no solo con el fondo sino 
también con la estrella. 
• Requisito 2: Un área del indicador del foco cumple tres condiciones: 
» Es al menos tan grande como el área de un perímetro de 1 píxel CSS de grosor del 
componente sin el foco, o es al menos tan grande como una línea de 4 píxeles CSS de 
grosor a lo largo del lado más corto de la caja delimitadora mínima del componente sin 
el foco. Es decir, define un área mínima mediante el perímetro y un mínimo secundario 
basado en el lado más corto. 
» Hay una ratio de contraste de al menos 3:1 entre los mismos píxeles en su estado con y 
sin el foco; 
» Hay una ratio de contraste de al menos 3:1 con los colores adyacentes que no forman 
parte del indicador del foco, o no es más delgado que 2 píxeles CSS. 
Hay dos excepciones: 
• Si el indicador del foco lo determina el agente de usuario y no puede ser ajustado por el 
autor. 
• El indicador del foco y el color de fondo del indicador no son modificados por el autor. 

<!-- Page 53 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
53 
También se añaden varias notas y ejemplos, que puedes consultar en el enlace: 
Understanding Success Criterion 2.4.11: Focus Appearance (AA) 
https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html 
• 2.4.12: Foco no oscurecido (Focus Not Obscured): (AA) añadida en WCAG 2.2 
Cuando un componente de la interfaz de usuario recibe el foco de teclado, el componente no 
puede estar completamente oculto por un contenido creado por el autor. 
Esto hace referencia, por ejemplo, al contenido que se superpone a un elemento con el foco, son 
los pies y encabezados fijos o las capas no modales. 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 2.4.12 Focus Not Obscured (Minimum) (AA) 
https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html 
También tienes información sobre las Técnicas suficientes en: 
C43: Uso del margen CSS y el margen de desplazamiento para eliminar el contenido oscuro 
https://www.w3.org/WAI/WCAG22/Techniques/css/C43 
• 2.4.13: Apariencia de enfoque (Focus Appearance): (AAA) añadida en WCAG 2.2: 
Es como el criterio anterior, pero más estricto, por ello este es de nivel AAA. 
Cuando un componente de la interfaz de usuario recibe el foco del teclado, el contenido creado 
por el autor no oculta ninguna parte del indicador del foco. 
Es decir, en este criterio se requiere que la totalidad del componente con el foco esté visible. 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 2.4.13 Focus Not Obscured (Enhanced) (AAA) 
https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-enhanced.html 
5.2.5. Pauta 2.5 Modalidades de entrada (Añadida en WCAG 2.1) 
Esta Pauta se añadió en WCAG 2.1 con 6 criterios. En WCAG 2.2 se añadieron 2 criterios más: 
2.5.7 y 2.5.8. 
Se añadió en WCAG 2.1 con el objetivo de facilitar a los usuarios el funcionamiento de la funcionalidad a 
través de varias entradas más allá del teclado. Incluye 6 criterios. En la versión WCAG 2.2 se añadieron 
dos criterios más (2.5.7 y 2.5.8). 

<!-- Page 54 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
54 
• 2.5.1 Gestos de puntero: (A) 
Toda la funcionalidad que utiliza gestos multipunto o basados en trazado para la operación se 
puede operar con un solo puntero sin un gesto basado en trazado, a menos que sea esencial un 
gesto multipunto o basado en trazado. 
• 2.5.2 Cancelación del puntero: (A) 
Para la funcionalidad que se puede operar con un solo puntero, se cumple al menos una de las 
siguientes condiciones: 
• Sin down-event: El evento descendente del puntero no se utiliza para ejecutar ninguna 
parte de la función. 
• Abortar o deshacer: La finalización de la función está en el evento up, y hay un mecanismo 
disponible para abortar la función antes de completarla o para deshacer la función después 
de la finalización. 
• Reversión hacia arriba: El evento hacia arriba revierte cualquier resultado del evento 
descendente anterior. 
• Imprescindible: Completar la función en el evento descendente es esencial. 
• 2.5.3 Etiqueta en el nombre: (A) 
Para los componentes de la interfaz de usuario con etiquetas que incluyen texto o imágenes de 
texto, el nombre contiene el texto que se presenta visualmente. 
• 2.5.4 Accionamiento de movimiento: (A) 
La funcionalidad que puede ser operada por el movimiento del dispositivo o el movimiento del 
usuario también puede ser operada por los componentes de la interfaz de usuario y responder al 
movimiento se puede desactivar para evitar el accionamiento accidental, excepto cuando: 
• Interfaz soportada: El movimiento se utiliza para operar la funcionalidad a través de una 
interfaz compatible con la accesibilidad. 
• Imprescindible: El movimiento es esencial para la función y hacerlo invalidaría la actividad. 
• 2.5.5 Tamaño objetivo: (AAA) 
El tamaño del destino para las entradas de puntero es de al menos 44 por 44 píxeles CSS, 
excepto cuando: 
• Equivalente: El destino está disponible a través de un enlace o control equivalente en la 
misma página que tiene al menos 44 por 44 píxeles CSS. 
• En línea: El objetivo está en una oración o bloque de texto. 

<!-- Page 55 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
55 
• Control de agente de usuario: El tamaño del destino es determinado por el agente de 
usuario y no es modificado por el autor. 
• Imprescindible: Una presentación particular del objetivo es esencial para la información que 
se transmite. 
• 2.5.6 Mecanismos de entrada simultáneos: (AAA) 
El contenido web no restringe el uso de las modalidades de entrada disponibles en una 
plataforma, excepto cuando la restricción es esencial, requerida para garantizar la seguridad del 
contenido o requerida para respetar la configuración del usuario. 
• 2.5.7 Movimientos de Arrastre (Dragging Movements): (AA) añadida en WCAG 2.2. 
Toda aquella funcionalidad que utilice un movimiento de arrastre para la operación (por 
ejemplo, controles deslizantes o interfaces de arrastrar y soltar) debe poderse utilizar mediante 
un "single pointer" sin arrastrar, a menos que arrastrar sea esencial, o a menos que la 
funcionalidad sea determinada por el agente de usuario y no sea modificada por el autor. 
No se aplica a las acciones necesarias para operar con el agente de usuario o el producto de 
apoyo. 
Hay que tener en cuenta que algunas personas no pueden realizar movimientos de arrastre de 
forma precisa. Otras, utilizan un dispositivo de entrada, como un puntero de cabeza, control por 
voz o de seguimiento ocular, que hace que el arrastre sea complicado, propenso al error o 
totalmente imposible. 
"Single pointer", es la activación mediante un solo punto: un toque (clic), doble toque (doble 
clic) o una pulsación larga. (Se indica en el criterio "2.5.1 Gestos del puntero" de las WCAG 2.1) 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 2.5.7: Dragging Movements (AA) 
https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html 
• 2.5.8 Tamaño Objetivo (Target Size): (AA) añadida en WCAG 2.2. 
El tamaño de la zona interacción con el puntero debe tener un área con un ancho y alto de al 
menos 24 píxeles CSS, excepto cuando se den estas situaciones en: 
• Espaciado: la zona de interacción no se superpone a ninguna otra y tiene una zona de 
interacción offset (la distancia entre el punto más lejano de una zona de interacción al 
punto más cercano de la segunda zona de interacción) de al menos de 24 píxeles CSS, 
respecto a cada zona de interacción adyacente. 
• Es decir, si la zona de interacción es menor de 24 px, pero, junto al margen, hasta la 
siguiente zona de interacción suma 24 px, es válido. 

<!-- Page 56 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
56 
• Equivalente: la función se puede lograr a través de un control diferente en la misma página 
que cumpla con este criterio. 
• En línea: el área de interacción está dentro de una oración, o está en una lista (numerada o 
con viñetas), o su tamaño está restringido por la altura de línea del texto que no forma 
parte del área de interacción. 
• Control de agente de usuario: el tamaño del área de interacción lo determina el agente de 
usuario y el autor no lo modifica. 
• Esencial: una presentación particular del área de interacción es esencial o es legalmente 
requerida para la información que se transmite. 
Este requisito es independiente del zoom de la página. Cuando los usuarios hacen zoom, el 
tamaño de píxel CSS de los elementos no cambia. Esto significa que los autores no pueden 
cumplirlo afirmando que el objetivo tendrá suficiente espacio o tamaño si el usuario hace zoom 
en la página, por eso es la versión menos estricta para el nivel AA del criterio "2.5.5 Tamaño del 
área de interacción" de nivel AAA, que establece el tamaño mínimo en 44 x 44 píxeles. 
Consulta más información y ejemplos en el enlace: 
Understanding Success Criterion 2.5.8: Target Size (Minimum) (AA) 
https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html 
5.3. Pautas Principio 3: Comprensible 
La información y el manejo de la interfaz de usuario deben ser comprensibles. 
5.3.1. Pauta 3.1 Legible 
Hacer que los contenidos textuales resulten legibles y comprensibles. 
• 3.1.1 Idioma de la página: (A) 
El idioma predeterminado de cada página web puede ser determinado por software. 
• 3.1.2 Idioma de las partes:(AA) 
El idioma de cada pasaje o frase en el contenido puede ser determinado por software, excepto 
los nombres propios, términos técnicos, palabras en un idioma indeterminado y palabras o 
frases que se hayan convertido en parte natural del texto que las rodea. 
• 3.1.3 Palabras inusuales: (AAA) 
Se proporciona un mecanismo para identificar las definiciones específicas de palabras o frases 
usadas de modo inusual o restringido, incluyendo expresiones idiomáticas y jerga. 

<!-- Page 57 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
57 
• 3.1.4 Abreviaturas: (AAA) 
Se proporciona un mecanismo para identificar la forma expandida o el significado de las 
abreviaturas. 
• 3.1.5 Nivel de lectura: (AAA) 
Cuando un texto requiere un nivel de lectura más avanzado que el nivel mínimo de educación 
secundaria una vez que se han eliminado nombres propios y títulos, se proporciona un 
contenido suplementario o una versión que no requiere un nivel de lectura mayor a ese nivel 
educativo. 
• 3.1.6 Pronunciación: (AAA) 
Se proporciona un mecanismo para identificar la pronunciación específica de las palabras 
cuando el significado de esas palabras, dentro del contexto, resulta ambiguo si no se conoce su 
pronunciación. 
5.3.2. Pauta 3.2 Predecible 
Hacer que las páginas web aparezcan y operen de manera predecible. 
• 3.2.1 Al recibir el foco: (A) 
Cuando cualquier componente recibe el foco, no inicia ningún cambio en el contexto. 
• 3.2.2 Al recibir entradas: (A) 
El cambio de estado en cualquier componente de la interfaz de usuario no provoca 
automáticamente un cambio en el contexto, a menos que el usuario haya sido advertido de ese 
comportamiento antes de usar el componente. 
• 3.2.3 Navegación coherente: (AA) 
Los mecanismos de navegación que se repiten en múltiples páginas web dentro de un conjunto 
de páginas web aparecen siempre en el mismo orden relativo cada vez que se repiten, a menos 
que el cambio sea provocado por el propio usuario. 
• 3.2.4 Identificación coherente: (AA) 
Los componentes que tienen la misma funcionalidad dentro de un conjunto de páginas web son 
identificados de manera coherente. 
• 3.2.5 Cambios a petición: (AAA) 
Los cambios en el contexto son iniciados únicamente a solicitud del usuario o se proporciona un 
mecanismo para detener tales cambios. 

<!-- Page 58 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
58 
• 3.2.6 Ayuda consistente (Consistent Help): (A) añadida en WCAG 2.2. 
Si una página web contiene algunos de los mecanismos de ayuda que se van a listar, y estos 
mecanismos de ayuda se repiten en varias páginas web dentro de un conjunto de páginas web, 
se ofrecen en el mismo orden relativo, a menos que un cambio sea iniciado por el usuario: 
• Datos de contacto humano (número de teléfono, dirección de correo electrónico, horario 
de atención, etc.) 
• Mecanismo de contacto humano (chat, formulario de contacto, canal de redes sociales, etc.) 
• Opción de autoayuda (una página de preguntas frecuentes) 
• Un mecanismo de contacto totalmente automatizado (un chatbot) 
El acceso a los mecanismos de ayuda se puede proporcionar directamente en la página, o se 
puede proporcionar a través de un enlace directo a una página diferente que contiene la 
información. 
El objetivo NO es exigir opciones de ayuda, sino garantizar que, si las hay, los usuarios puedan 
encontrarlas para completar las tareas del sitio web porque se incluyen en una ubicación 
consistente en todas las páginas. 
Es, por tanto, un criterio muy similar al "3.2.3 Navegación consistente", pero aplicado a los 
mecanismos de contacto y ayuda en vez de a los mecanismos de navegación. 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 3.2.6: Consistent Help (A) 
https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html 
5.3.3. Pauta 3.3 Entrada de datos asistida 
Ayudar a los usuarios a evitar y corregir los errores. (Asistencia a la entrada de datos). 
• 3.3.1 Identificación de errores: (A) 
Si se detecta automáticamente un error en la entrada de datos, el elemento erróneo es 
identificado y el error se describe al usuario mediante un texto. 
• 3.3.2 Etiquetas o instrucciones: (A) 
Se proporcionan etiquetas o instrucciones cuando el contenido requiere la introducción de 
datos por parte del usuario. 

<!-- Page 59 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
59 
• 3.3.3 Sugerencias ante errores: (AA) 
Si se detecta automáticamente un error en la entrada de datos y se dispone de sugerencias para 
hacer la corrección, entonces se presentan las sugerencias al usuario, a menos que esto ponga 
en riesgo la seguridad o el propósito del contenido. 
• 3.3.4 Prevención de errores (legales, financieros, datos): (AA) 
Para las páginas web que representan para el usuario compromisos legales o transacciones 
financieras; que modifican o eliminan datos controlables por el usuario en sistemas de 
almacenamiento de datos; o que envían las respuestas del usuario a una prueba, se cumple al 
menos uno de los siguientes casos: 
1. Reversible: El envío es reversible. 
2. Revisado: Se verifica la información para detectar errores en la entrada de datos y se 
proporciona al usuario una oportunidad de corregirlos. 
3. Confirmado: Se proporciona un mecanismo para revisar, confirmar y corregir la 
información antes de finalizar el envío de los datos. 
• 3.3.5 Ayuda: (AAA) 
Se proporciona ayuda dependiente del contexto. 
• 3.3.6 Prevención de errores (todos): (AAA) 
Para las páginas web que requieren al usuario el envío de información, se cumple al menos uno 
de los siguientes casos. 
1. Reversible: El envío es reversible. 
2. Revisado: Se verifica la información para detectar errores en la entrada de datos y se 
proporciona al usuario una oportunidad de corregirlos. 
3. Confirmado: Se proporciona un mecanismo para revisar, confirmar y corregir la 
información antes de finalizar el envío de los datos. 
• 3.3.7 Entrada Redundante (Redundant entry): (A) añadida en WCAG 2.2: 
La información ingresada previamente por el usuario o proporcionada al usuario y que debe 
ingresar nuevamente en el mismo proceso, debe rellenarse automáticamente o estar disponible 
para que el usuario la seleccione. 
Hay tres excepciones: 
1. Volver a ingresar la información es esencial. 
2. La información es necesaria para garantizar la seguridad del contenido. 
3. La información ingresada anteriormente ya no es válida. 

<!-- Page 60 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
60 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 3.3.7: Redundant Entry | WAI | W3C 
https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html 
• 3.3.8 Accessible Authentication (Accessible Authentication): (AA) añadida en WCAG 2.2. 
Este criterio tiene como objetivo garantizar que exista un método accesible, fácil de usar y 
seguro para iniciar sesión y acceder al contenido, y beneficia especialmente a las personas con 
discapacidad cognitiva. 
Si un proceso de autenticación se basa en una "cognitive function test" (como recordar una 
contraseña o resolver un puzzle) no se requiere para ningún paso en un proceso de 
autenticación (procedimiento informático que permite asegurar que un usuario de un sitio web 
es auténtico o quien dice ser) a menos que ese paso proporcione al menos una de las siguientes 
opciones: 
• Alternativa: otro método de autenticación que no se basa en una prueba de función 
cognitiva. 
• Mecanismo: hay un mecanismo disponible para ayudar al usuario a completar la prueba 
cognitiva. 
• Reconocimiento de objetos: la prueba de función cognitiva consiste en reconocer objetos 
(pueden ser imágenes, vídeos o audios). 
• Contenido personal: la prueba de función cognitiva es para identificar contenido no textual 
que el usuario proporcionó al sitio web (pueden ser imágenes, vídeos o audios). 
Los siguientes son ejemplos de mecanismos que satisfacen este criterio: 
• Soporte para la entrada de contraseñas por administradores de contraseñas para reducir la 
necesidad de memoria. 
• Copiar y pegar para reducir la carga cognitiva de volver a escribir. 
Puedes obtener más información sobre este criterio 3.3.8 Accessible Authentication en el 
enlace: 
Understanding Success Criterion 3.3.8: Accessible Authentication | WAI | W3C 
https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication.html 
 

<!-- Page 61 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
61 
 
 
 
Significado 
Se entiende por "cognitive function test" (prueba de función 
cognitiva), una tarea que requiere que el usuario recuerde, 
manipule o transcriba información, por ejemplo: 
• Memorización, como recordar un nombre de usuario, 
contraseña, conjunto de caracteres, imágenes o patrones. 
Los identificadores comunes de nombre, correo electrónico 
y número de teléfono no se consideran pruebas de función 
cognitiva, ya que son personales para el usuario y 
coherentes en todos los sitios web. 
• Transcripción, como escribir caracteres. 
• Uso de ortografía correcta. 
• Realización de cálculos. 
• Resolución de rompecabezas. 
 
 
• 3.3.9 Accessible Authentication Mejorada (Enhanced): (AAA) añadida en WCAG 2.2. 
Como el criterio anterior pero más estricto. 
Únicamente, se admite como alternativa a la prueba de función cognitiva otro método de 
autenticación alternativo o un mecanismo de ayuda, pero no que la prueba consista en el 
reconocimiento de objetos o la identificación de contenido personal no textual. 
Puedes obtener más información en el enlace: 
Understanding Success Criterion 3.3.8: Accessible Authentication | WAI | W3C 
https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-no-
exception.html 
5.4. Pautas Principio 4: Robusto 
El contenido debe ser suficientemente robusto como para ser interpretado de forma fiable por una 
amplia variedad de aplicaciones de usuario, incluyendo las ayudas técnicas. 

<!-- Page 62 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
62 
5.4.1. Pauta 4.1 Compatible 
• 4.1.1 Procesamiento- Análisis sintáctico: (A) Desaparecece en WCAG 2.2 
En los contenidos implementados mediante el uso de lenguajes de marcas, los elementos tienen 
las etiquetas de apertura y cierre completas; los elementos están anidados de acuerdo a sus 
especificaciones; los elementos no contienen atributos duplicados y los ID son únicos, excepto 
cuando las especificaciones permitan estas características. 
Nota: Las etiquetas de apertura y cierre a las que les falte un carácter crítico para su formación, 
como un signo de "mayor qué", o en las que falten las comillas de apertura o cierre en el valor de 
un atributo, no se consideran completas. 
• 4.1.2 Nombre, función (rol), valor: (A) 
Para todos los componentes de la interfaz de usuario (incluyendo, pero no limitado a: 
elementos de formulario, enlaces y componentes generados por scripts), el nombre y la función 
pueden ser determinados por software; los estados, propiedades y valores que pueden ser 
asignados por el usuario pueden ser especificados por software; y los cambios en estos 
elementos se encuentran disponibles para su consulta por las aplicaciones de usuario, 
incluyendo las ayudas técnicas. 
Nota: Este criterio de conformidad se dirige principalmente a los autores web que desarrollan o 
programan sus propios componentes de interfaz de usuario. Por ejemplo, los controles estándar 
de HTML satisfacen automáticamente este criterio cuando se emplean de acuerdo con su 
especificación. 
• 4.1.3 Mensajes de estado: (AA) - Añadido en WCAG 2.1 
En el contenido implementado mediante lenguajes de marcado, los mensajes de estado se 
pueden determinar mediante programación a través de roles o propiedades, de modo que 
puedan ser presentados al usuario por tecnologías de asistencia sin recibir enfoque. 
5.5. Resumen de los criterios de conformidad (A, AA Y AAA) 
En WCAG 2.0: 
• 12 PAUTAS 
• 61 Criterios de conformidad. 
• De nivel A (25 criterios). 
• De nivel AA (13 criterios). 
• De nivel AAA (23 criterios). 

<!-- Page 63 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
63 
En WCAG 2.1: 
• 12 PAUTAS (Se añade la Pauta 2.5 en el principio 2 Operable, respecto a la WCAG 2.0) 
• 78 Criterios de conformidad (Se añaden 17 criterios respecto a WCAG 2.0) 
• De nivel A (30 criterios). 
• De nivel AA (20 criterios). 
• De nivel AAA (28 criterios). 
En WCAG 2.2 
• 13 PAUTAS (se añade una nueva pauta: 2.4. Navegable) 
• 86 criterios de conformidad (Se elimina 1 criterio y se añaden 9 criterios respecto a WCAG 2.0) 
• De nivel A (31 criterios). 
• De nivel AA (24 criterios). 
• De nivel AAA (31 criterios). 
En el Borrador 3.0 
• Estructura: cambia de principios, pautas y criterios A/AA/AAA a outcomes (resultados 
verificables). 
• Niveles de conformidad: desaparecen A, AA y AAA; se plantean niveles de puntuación (bronze, 
silver, gold). 
• Estado: documento en evolución, sin número definitivo de outcomes ni requisitos cerrados. 
• Enfoque: de un modelo prescriptivo (reglas fijas) a un modelo basado en resultados y 
experiencia del usuario. 
6. Diseño Inclusivo o Inclusive Design 
Si hablamos de diseño inclusivo o Incluse Design estaremos contemplando un enfoque cuyo propósito es 
el de crear entornos accesibles y usables por el mayor número posible de usuarios, independientemente 
de sus facultades o particularidades. Dentro del Inclusive Design o Diseño Inclusivo existen 
especificaciones como las WCAG que ya hemos visto, pero también otras como WAI-ARIA ambas 
desarrolladas por la W3C. 

<!-- Page 64 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
64 
WAI-ARIA 
La especificación WAI-ARIA (Web Accessibility Initiative - Accesible Rich Internet Applications) 
proporciona atributos adicionales que se superponen a las etiquetas HTML y serán requeridas por las 
tecnologías de asistencia, como lectores de pantalla, para ofrecer una experiencia web accesible. La 
WAI-ARIA pone el foco en los elementos web interactivos de aplicaciones web complejas. 
 
Aquí tenemos el ejemplo de algunos atributos WAI-ARIA que serán usados por las tecnologías de 
asistencia con el fin de facilitar la interacción a los usuarios que las usen. 
MATERIAL DESIGN 
Por otro lado, cabe mencionar, Material Design, especificación que no se ocupa específicamente de la 
accesibilidad, pero sí contempla principios de diseño que contribuyen a experiencias de usuario, entre 
otras más inclusivas. Es una especificación promovida por Google que marca unas directrices de diseño 
y principios estéticos para el desarrollo de interfaces de usuario consistentes y atractivos. 
7. RDF (Resource Description Framework) 
En castellano Marco de Descripción de Recursos. 
Es una familia de especificaciones de W3C, originalmente diseñado como un modelo de datos para 
metadatos. 

<!-- Page 65 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
65 
Ha llegado a ser usado como un método general para la descripción conceptual o modelado de la 
información que se implementa en los recursos Web, utilizando una variedad de notaciones de sintaxis 
y formatos de serialización de datos. 
El modelo de datos RDF es similar a los enfoques de modelado conceptual clásicos como entidad-
relación o diagramas de clases, ya que se basa en la idea de hacer declaraciones sobre los recursos (en 
particular, recursos web) en forma de expresiones sujeto-predicado-objeto. Estas expresiones son 
conocidos como triples en terminología RDF. El sujeto indica el recurso y el predicado denota rasgos o 
aspectos del recurso y expresa una relación entre el sujeto y el objeto. 
8. Legislación sobre accesibilidad en España, Europa 
y otros países 
 
Las principales leyes, decretos y normas en materia de accesibilidad web son: 
• Norma UNE 139802:1998 EX: 
Informática para la salud: aplicaciones informáticas para personas con discapacidad: requisitos 
de accesibilidad de las plataformas informáticas: soporte lógico. 
• LEY 34/2002, de 11 de julio: 
De servicios de la sociedad de la información y de comercio electrónico. 
• ORDEN PRE/1551/2003, de 10 de junio: 
Por la que se desarrolla la Disposición final primera del Real Decreto 209/2003, de 21 de 
febrero, por el que se regulan los registros y las notificaciones telemáticas, así como la 
utilización de medios telemáticos para la sustitución de la aportación de certificados por los 
ciudadanos. 
• LEY 51/2003, de 2 de diciembre: 
De igualdad de oportunidades, no discriminación y accesibilidad universal de las personas con 
discapacidad. 

<!-- Page 66 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
66 
• REAL DECRETO 1414/2006, de 1 de diciembre: 
Por el que se determina la consideración de persona con discapacidad a los efectos de la Ley 
51/2003, de 2 de diciembre, de Igualdad de oportunidades, no discriminación y accesibilidad 
universal de las personas con discapacidad. 
• REAL DECRETO 366/2007, de 16 de marzo: 
Por el que se establecen las condiciones de accesibilidad y no discriminación de las personas con 
discapacidad en sus relaciones con la Administración General del Estado. 
• LEY 11/2007, de 22 de junio: 
De acceso electrónico de los ciudadanos a los Servicios Públicos. 
• REAL DECRETO 1494/2007: 
De 12 de noviembre, por el que se aprueba el Reglamento sobre las condiciones básicas para el 
acceso de las personas con discapacidad a las tecnologías, productos y servicios relacionados 
con la sociedad de la información y medios de comunicación social. 
• LEY 27/2007, de 23 de octubre: 
Por la que se reconocen las lenguas de signos españolas y se regulan los medios de apoyo a la 
comunicación oral de las personas sordas, con discapacidad auditiva y sordociegas. 
• LEY 49/2007, de 26 de diciembre: 
Por la que se establece el régimen de infracciones y sanciones en materia de igualdad de 
oportunidades, no discriminación y accesibilidad universal de las personas con discapacidad. 
• LEY 56/2007, de 28 de diciembre: 
De Medidas de Impulso de la Sociedad de la Información. 
• LEY 7/2010, de 31 de marzo: 
General de la Comunicación Audiovisual. 
• LEY 26/2011, de 1 de agosto: 
De adaptación normativa a la Convención Internacional sobre los Derechos de las Personas con 
Discapacidad. 

<!-- Page 67 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
67 
• Norma UNE 139803:2012: 
La legislación española establece que la Norma UNE 139803:2012: "Requisitos de accesibilidad 
para contenidos en la Web" define los requisitos de accesibilidad para los contenidos web, 
mediante leyes, decretos y normas en materia de accesibilidad web. 
• Anula y sustituye la UNE 139803:2004. 
Aplicaciones informáticas para personas con discapacidad. Requisitos de accesibilidad para 
contenidos en la Web. 
• Establece los requisitos de accesibilidad para los contenidos web. 
• No es aplicable al software utilizado para acceder a los contenidos web. 
• Real Decreto Legislativo 1/2013, de 29 de noviembre: 
Por el que se aprueba el Texto Refundido de la Ley General de derechos de las personas con 
discapacidad y de su inclusión social. 
Esquema Nacional de Interoperabilidad en el ámbito de la Administración Electrónica 
El Real Decreto 4/2010, de 8 de enero, regula el Esquema Nacional de Interoperabilidad en el ámbito de 
la Administración Electrónica. 
Es importante conocer el contenido de este Real Decreto, destacamos la siguiente información: 
Principios básicos: 
• Artículo 4. Principios básicos del Esquema Nacional de Interoperabilidad. 
La aplicación del Esquema Nacional de Interoperabilidad se desarrollará de acuerdo con los 
principios generales establecidos en el artículo 4 de la Ley 11/2007, de 22 de junio, y con los 
siguientes principios específicos de la interoperabilidad: 
a. La interoperabilidad como cualidad integral. 
b. Carácter multidimensional de la interoperabilidad. 
c. Enfoque de soluciones multilaterales. 
• Artículo 5. La interoperabilidad como cualidad integral. 
La interoperabilidad se tendrá presente de forma integral desde la concepción de los servicios y 
sistemas y a lo largo de su ciclo de vida: planificación, diseño, adquisición, construcción, 
despliegue, explotación, publicación, conservación y acceso o interconexión con los mismos. 

<!-- Page 68 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
68 
• Artículo 6. Carácter multidimensional de la interoperabilidad. 
La interoperabilidad se entenderá contemplando sus dimensiones organizativa, semántica y 
técnica. La cadena de interoperabilidad se manifiesta en la práctica en los acuerdos 
interadministrativos, en el despliegue de los sistemas y servicios, en la determinación y uso de 
estándares, en las infraestructuras y servicios básicos de las Administraciones públicas y en la 
publicación y reutilización de las aplicaciones de las Administraciones públicas, de la 
documentación asociada y de otros objetos de información. Todo ello sin olvidar la dimensión 
temporal que ha de garantizar el acceso a la información a lo largo del tiempo. 
• Artículo 7. Enfoque de soluciones multilaterales. 
Se favorecerá la aproximación multilateral a la interoperabilidad de forma que se puedan 
obtener las ventajas derivadas del escalado, de la aplicación de las arquitecturas modulares y 
multiplataforma, de compartir, de reutilizar y de colaborar. 
 
 
 
 
Atención 
El Real Decreto, es muy amplio, ya lo has estudiado en el Bloque I, y 
puedes consultarlo en la página oficial. 
https://www.boe.es/eli/es/rd/2010/01/08/4/con 
 
8.1. Real Decreto 1112/2018, de 7 de septiembre, 
sobre accesibilidad de los sitios web y aplicaciones 
para dispositivos móviles del sector público 
Este Real Decreto, tiene como objeto, a fin de mejorar el funcionamiento del mercado interior, 
aproximar las disposiciones legales, reglamentarias y administrativas de los Estados miembros de la UE, 
relativas a los requisitos de accesibilidad, entendiendo la accesibilidad como un conjunto de principios y 
técnicas que se deben respetar a la hora de diseñar, construir, mantener y actualizar los sitios web y las 
aplicaciones para dispositivos móviles. 
 

<!-- Page 69 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
69 
 
 
 
Imprescindible 
Debes conocer el contenido de este Real Decreto, puedes 
consultarlo en la web oficial. 
https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699 
También debes consultar información sobre accesibilidad en: 
https://administracionelectronica.gob.es/ 
 
9. ISO/IEC 10026-1 (Concepto ACID) 
El Concepto ACID se describe en ISO/IEC 10026-1: 1992 sección 4. 
ACID es un acrónimo de Atomicity, Consistency, Isolation and Durability. En español: Atomicidad, 
Consistencia, Aislamiento y Durabilidad. 
En bases de datos relacionales, se denomina ACID a las características de los parámetros que permiten 
clasificar las transacciones de los sistemas de gestión de bases de datos. Cuando se dice que es ACID 
compliant se indica que, en diversos grados, éste permite realizar transacciones. 
Cumpliendo estos 4 requisitos un sistema gestor de bases de datos puede ser considerado ACID 
Compliant. 
9.1. Requisitos ACID 
Vamos a profundizar en los cuatro requisitos un sistema gestor de bases de datos relacionales. 
9.1.1. Atomicidad 
Si cuando una operación consiste en una serie de pasos, de los que o bien se ejecutan todos o ninguno, 
es decir, las transacciones son completas. 

<!-- Page 70 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
70 
Es la propiedad que asegura que una operación se ha realizado o no, y por lo tanto ante un fallo del 
sistema no puede quedar a medias. Se dice que una operación es atómica cuando es imposible para otra 
parte de un sistema encontrar pasos intermedios. Si esta operación consiste en una serie de pasos, 
todos ellos ocurren o ninguno. Por ejemplo, en el caso de una transacción bancaria o se ejecuta tanto el 
depósito y la deducción o ninguna acción es realizada. 
9.1.2. Consistencia (integridad) 
Es la propiedad que asegura que sólo se empieza aquello que se puede acabar. Por lo tanto, se ejecutan 
aquellas operaciones que no van a romper las reglas y directrices de Integridad de la base de datos. La 
propiedad de consistencia sostiene que cualquier transacción llevará a la base de datos desde un estado 
válido a otro también válido. "La Integridad de la Base de Datos nos permite asegurar que los datos son 
exactos y consistentes, es decir que estén siempre intactos, sean siempre los esperados y que de 
ninguna manera cambian ni se deformen. De esta manera podemos garantizar que la información que 
se presenta al usuario será siempre la misma." 
Los lenguajes de alto nivel, tales como C, C++ y Java, respetan parcialmente este modelo traduciendo 
operaciones de memoria en operaciones de bajo nivel para preservar la memoria semántica. Para 
mantener el modelo, los compiladores pueden reordenar algunas instrucciones de memoria, y las 
llamadas a las bibliotecas como pthread_mutex_lock(), encapsular la sincronización necesaria. 
Los ejemplos incluyen: 
• Linealizable (también conocido como el estricta o consistencia atómica). 
• Consistencia secuencial. 
• Consistencia de causalidad. 
• Consistencia liberada. 
• Consistencia eventual. 
• Consistencia delta. 
• Consistencia PRAM (también conocido como consistencia FIFO). 
• Consistencia débil. 
• Consistencia vector campo. 
9.1.3. Aislamiento 
Esta propiedad, asegura que una operación no puede afectar a otras, es decir, que la realización de dos 
transacciones sobre la misma información, sean independientes, y no generen ningún tipo de error. 
Esta propiedad define cómo y cuándo los cambios producidos por una operación se hacen visibles para 
las demás operaciones concurrentes. El aislamiento puede alcanzarse en distintos niveles, siendo el 
parámetro esencial a la hora de seleccionar SGBDs. 

<!-- Page 71 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
71 
Para obtener el mayor nivel de aislamiento, un SGBDR generalmente hace un bloqueo de los datos o 
implementa un Control de concurrencia mediante versiones múltiples (MVCC), lo que puede producir 
una pérdida de concurrencia. Por ello se necesita añadir lógica adicional al programa que accede a los 
datos para su funcionamiento correcto. 
La mayor parte de los SGBDR ofrecen unos ciertos niveles de aislamiento que controlan el grado de 
bloqueo durante el acceso a los datos. Para la mayor parte de aplicaciones, el acceso a los datos se 
puede realizar de modo que se eviten altos niveles de aislamiento (i.e. nivel SERIALIZABLE), reduciendo 
así la sobrecarga debida a la necesidad de bloqueos por el sistema. El programador debe analizar 
detenidamente el código que accede a la base de datos para asegurarse de que el descenso del nivel de 
aislamiento que ofrece el SGBD no produce errores en el programa. Recíprocamente, si se usan altos 
niveles de aislamiento la posibilidad de bloqueo aumenta, lo que también requiere análisis cuidadoso del 
código. 
Los niveles de aislamiento están definidos por ANSI/ISO SQL, y se listan a continuación: 
• Serializable. 
Este es el nivel de aislamiento más alto. Especifica que todas las transacciones ocurran de modo 
aislado, o, dicho de otro modo, como si todas las transacciones se ejecutaran de modo serie 
(una tras otra). La sensación de ejecución simultánea de dos o más transacciones que perciben 
los usuarios sería una ilusión producida por el SGBD. 
Si el SGBDR hace una implementación basada en bloqueos, la serialización requiere que los 
bloques de lectura y escritura se liberen al final de la transacción. Del mismo modo deben 
realizarse bloqueos de rango -sobre los datos seleccionados con SELECT usando WHERE- para 
evitar el efecto de las lecturas fantasma (ver más abajo). 
Cuando se hace una implementación no basada en bloqueos, si el SGBDR detecta una colisión de 
escritura entre transacciones solo a una de ellas se le autoriza cometer. 
• Lecturas repetibles (Repeatable reads). 
En este nivel de aislamiento, un SGBDR que implemente el control de concurrencia basado en 
bloqueos mantiene los bloqueos de lectura y escritura -de los datos seleccionados- hasta el final 
de la transacción. Sin embargo, no se gestionan los bloqueos de rango, por lo que las lecturas 
fantasma pueden ocurrir (ver más abajo). 
• Lecturas comprometidas (Read committed). 
En este nivel de aislamiento, un SGBDR que implemente el control de concurrencia basado en 
bloqueos mantiene los bloqueos de escritura -de los datos seleccionados- hasta el final de la 
transacción, mientras que los bloqueos de lectura se cancelan tan pronto como acaba la 
operación de SELECT (por lo que el efecto de las lecturas no repetibles puede ocurrir, como se 
explica más abajo). Al igual ocurría en el nivel anterior, no se gestionan los bloqueos de rango. 
• Lecturas no comprometidas (Read uncommitted). 
Este es el menor nivel de aislamiento. En él se permiten las lecturas sucias (ver más abajo), por 
lo que una transacción puede ver cambios no cometidos aún por otra transacción. 

<!-- Page 72 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
72 
Nivel de aislamiento por defecto 
La mayoría de bases de datos que gestionan transacciones permiten al usuario establecer cualquier nivel 
de aislamiento. Algunos SGBDR requieren una sintaxis especial cuando se realiza una operación SELECT 
que efectúa bloqueos (e.g. SELECT ... FOR UPDATE para bloquear para escritura aquellas filas 
accedidas). 
Sin embargo, la definición anterior ha sido criticada en el artículo A Critique of ANSI SQL Isolation Levels 
por ambigua, y por no reflejar de modo preciso el aislamiento proporcionado por muchas bases de 
datos. 
Hay también otras críticas sobre las definiciones de aislamiento SQL de ANSI, en cuanto a que incita a 
los implementadores a realizar "trabajos sucios". 
9.1.4. Durabilidad (persistencia) 
Esta propiedad asegura que, una vez realizada la operación, esta persistirá y no se podrá deshacer, 
aunque falle el sistema, y que, de esta forma, los datos sobrevivan de alguna manera. 
En programación, la persistencia es la acción de preservar la información de un objeto de forma 
permanente (guardado), pero a su vez también se refiere a poder recuperar la información del mismo 
(leerlo) para que pueda ser nuevamente utilizado. 
Tipos de persistencia de dato 
Se consideran varios tipos de persistencia. 
• Persistencia en memoria. 
La persistencia en memoria es la capacidad de un dato u objeto para seguir existiendo tras 
determinadas operaciones. 
La operación más común que se presta a la persistencia en memoria es la asignación. Existen dos 
ideas respecto de lo que debe suceder con un dato, estructura u objeto una vez asignado desde 
el original. 
• Colecciones. 
En unos casos lo que se desea es que haya dos referencias a los mismos datos. Es decir: un 
mismo dato tiene dos punteros desde los que es posible acceder a ellos. Un tipo de dato que 
utiliza este método se dice que tiene persistencia si cuando se elimina uno de los punteros, los 
datos siguen aún en memoria. En este caso el tipo de datos utiliza un contador de referencias, 
de modo que cada vez que se crea una referencia se aumenta la cuenta en uno (+1) y cuando se 
elimina una referencia se disminuye el contador en uno (-1). El tipo de datos, por tanto, sólo es 
realmente eliminado cuando la cuenta del contador llega a cero (0); es decir, cuando no tiene 
referencias apuntando a los datos. 

<!-- Page 73 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
73 
• Vectores o arrays. 
En otros casos lo que interesa cuándo se hace una asignación es copiar, crear totalmente aparte 
un duplicado de los datos a asignar (hay preferencias para llamar a este tipo de copia clonar en 
vez de copiar). Por tanto, no necesitan o no utilizan nunca más de una referencia, ni por tanto 
precisan tener un contador de referencias. Estos casos se dice que no tienen persistencia. Al 
eliminar la referencia los datos quedan perdidos, nunca tienen más de una referencia, ya que 
cuando se hace una asignación se realiza un duplicado de los datos con su propia referencia. 
• Persistencia de aplicación. 
Es la capacidad para que los datos sobrevivan a la ejecución del programa que los ha creado. Sin 
esta capacidad, los datos solo existen en memoria RAM, y se pierden cuando la memoria pierde 
energía, como cuando se apaga el computador. 
Este tipo de persistencia requiere que los datos sean almacenados en un medio secundario, no 
volátil, para su posterior reconstrucción y utilización, por lo que su tiempo de vida es 
independiente del proceso que los creó. Por lo tanto, deberán permanecer almacenados en 
memoria que no sea volátil. Es decir, que en caso de interrupción de la energía que alimenta al 
computador, una copia de estos datos debe permanecer almacenada. 
• Persistencia de objetos. 
En el caso de persistencia de objetos la información que persiste en la mayoría de los casos son 
los valores que contienen los atributos en ese momento, no necesariamente la funcionalidad 
que proveen sus métodos. 
La persistencia de objetos puede ser fácilmente confundida con la persistencia en memoria; 
incluso con la persistencia de aplicación. 
La persistencia de objetos consiste en la inicialización de objetos con sus atributos 
predeterminados o atributos por defecto. Esto es posible con dos maneras de proceder. 
• Sobre un medio de almacenamiento fijo se guarda (cuando el objeto fue definido) un 
conjunto de datos que son recuperados cuando el tipo de objeto en cuestión es creado; 
dichos datos son transferidos a las propiedades del objeto. 
• Otro objeto mantiene los datos que serán transferidos a las propiedades del nuevo objeto 
creado. En este caso los datos están en memoria. 
Para guardar los datos de objetos en disco se recurre a un mecanismo conocido como 
serialización (serializar), que dispone en una secuencia de bytes todos los datos (o sólo aquellos 
que se desee) que definen el objeto. 
Desde la óptica de la persistencia, se podrían clasificar los objetos en: 
• Transitorios: cuyo tiempo de vida depende directamente del ámbito del proceso que los 
instanció. 
• Persistentes: cuyo estado es almacenado en un medio secundario para su posterior 
reconstrucción y utilización, por lo que su tiempo de vida es independiente del proceso que 
los instanció. 

<!-- Page 74 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
74 
Al programador, la persistencia permite almacenar, transferir y recuperar el estado de los 
objetos. Para esto existen varias técnicas: 
• Serialización. 
• Motores de persistencia. 
• Bases de datos orientadas a objetos. 
9.2. Puesta en práctica 
Poner las características ACID en ejecución no es tan sencillo. El proceso de una transacción requiere a 
menudo un número de cambios pequeños al ser realizado, incluyendo la puesta al día de los índices que 
son utilizados en el sistema para acelerar búsquedas. 
Esta secuencia de operaciones puede fallar por un número de razones; por ejemplo, el sistema puede no 
tener ningún sitio disponible en sus accionamientos de disco, o puede haber sobrepasado su tiempo de 
CPU asignado. 
ACID sugiere que la base de datos pueda realizar todas estas operaciones inmediatamente. De hecho, 
esto es difícil de conseguir. 
En ambos casos, los bloqueos se deben implantar antes que la información sea actualizada, y 
dependiendo de la técnica puesta en práctica, todos los datos se tienen que haber leído. 
Hay dos clases de técnicas populares: 
• Escribir a un registro antes de continuar. 
En escribir a un registro antes de continuar, la atomicidad es garantizada asegurándose que toda 
la información esté escrita a un registro antes que se escriba a la base de datos. Eso permite que 
la base de datos vuelva a un estado anterior en caso de un desplome. 
• La paginación de la sombra. 
En sombrear, las actualizaciones se aplican a una copia de la base de datos, y se activa la nueva 
copia cuando la transacción sea confiable. La copia refiere a partes sin cambios de la vieja 
versión de la base de datos, en vez de ser un duplicado entero. 
10. ANSI/ISO SQL 92: efectos en lectura 
El estándar ANSI/ISO SQL 92 se refiere a tres efectos de lectura diferentes cuando la transacción 1 lee 
datos que podría haber cambiado la transacción 2. 
En los siguientes ejemplos se ejecutan dos transacciones. La primera ejecuta la consulta 1. Entonces una 
segunda transacción ejecuta la consulta 2 y la comete. Por último, la primera transacción ejecuta la 
consulta 1 de nuevo. 

<!-- Page 75 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
75 
• Lecturas sucias. 
Una lectura sucia ocurre cuando se le permite a una transacción la lectura de una fila que ha sido 
modificada por otra transacción concurrente pero todavía no ha sido cometida. 
Las lecturas sucias funcionan de modo similar a las lecturas no repetibles; sin embargo, la 
segunda transacción no necesita ser cometida para que la primera dé un resultado diferente. Lo 
único que se puede prevenir en el nivel de aislamiento LECTURAS NO COMETIDAS es que las 
actualizaciones aparezcan en desorden en el resultado; esto es, que las primeras actualizaciones 
siempre aparecerán antes que las actualizaciones posteriores. 
• Lecturas no repetibles. 
Una lectura no repetible ocurre cuando en el curso de una transacción una fila se lee dos veces y 
los valores no coinciden. 
El efecto de lecturas no repetible puede ocurrir en una implementación de concurrencia 
mediante bloqueos cuando no se efectúan éstos al hacer un SELECT, o cuando los bloqueos se 
liberan nada más terminar la operación SELECT. Cuando se usa el método MVCC, las lecturas no 
repetibles pueden aparecer cuando se relaja el requisito de que al cometer una transacción 
afectada por un conflicto ésta deba deshacerse. 
• Lecturas fantasma. 
Una lectura fantasma ocurre cuando, durante una transacción, se ejecutan dos consultas 
idénticas, y los resultados de la segunda no son iguales a los de la primera. 
Esto puede ocurrir cuando no se realizan bloqueos de rango al realizar una operación SELECT ... 
WHERE. 
La anomalía de las lecturas fantasma, es un caso particular de las lecturas no repetibles, cuando 
la transacción 1 repite una consulta acotada en rango SELECT ... WHERE y, entre ambas 
operaciones la transacción 2 crea (INSERT) nuevas filas (en la misma tabla) que entran dentro 
de esa cláusula WHERE. 
11. Herramientas para mejora de acceso y usabilidad 
 
Hoy en día, la sociedad de la información nos ofrece grandes posibilidades para acceder a la información 
a través de diversas tecnologías y servicios. 

<!-- Page 76 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
76 
Sin embargo, para ciertos colectivos (personas con discapacidad o personas mayores) este avance 
tecnológico supone grandes beneficios, pero por otro lado supone un obstáculo grave (a veces 
insalvable) cuando estas no son accesibles. 
A continuación, indicamos algunas de estas dificultades y soluciones básicas de accesibilidad y veremos 
también herramientas de hardware y software para solucionar los problemas de determinados 
colectivos. 
Veamos algunas herramientas para el acceso y usabilidad de las tecnologías, productos y servicios 
relacionados con la sociedad de la información. 
11.1. Telefonía móvil 
 
Fuente: https://pxhere.com/en/photo/514291 
Soluciones básicas de accesibilidad para telefonía móvil. 
• Terminal: 
• Debe ser fácil de sujetar y manipular. 
• Teclado: 
• Deben ser fácilmente visibles. 
• Su tamaño debe ser adecuado para la marcación. 
• Debe existir una distancia adecuada entre las teclas. 
• Las teclas de función deben tener una forma diferente. 
• Las pulsaciones en las teclas deben confirmarse acústicamente. 
• El teléfono debería contar con un botón que permita al usuario escuchar la función de cada 
tecla, el contenido del visor de pantalla, los menús, etcétera. 
• Marcación: 
• Se debe permitir marcación abreviada y marcación por voz. 

<!-- Page 77 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
77 
• Pantalla: 
• Debe ser suficientemente grande. 
• El tamaño de las letras debe ser suficiente. 
• Se debe permitir la opción de zoom. 
• El contraste entre las letras y el fondo de pantalla debe ser alto. 
• Señales acústicas: 
• Debe de ofrecer la posibilidad de reconvertir señales auditivas en mensajes escritos y 
viceversa. 
• Debe tener timbre de llamada, avisador vibratorio y avisador visual. 
• El volumen de los tonos debe ser configurable. 
• Equipos auxiliares: 
• El teléfono debe contar con conectores para: 
» Auriculares. 
» Elementos de fijación. 
» Dispositivos auxiliares de escucha. 
• La conexión con otros equipos debe ser sencilla. 
• La conexión con el cargador de batería debe ser sencilla. 
11.2. Ordenadores personales (hardware) 
 
Soluciones básicas de accesibilidad para ordenadores. 

<!-- Page 78 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
78 
• Elegir los elementos prioritarios y dejarlos al alcance. Podrían ser: 
• Botón de encendido. 
• Teclado. 
• Ratón. 
• Sonidos. Debe poder regularse el volumen del sonido: 
• Por mando físico. 
• Por software, mediante. 
• Botones de control: 
• Los interruptores de las piezas más importantes deben estar en la parte frontal. 
• Deben poder diferenciarse por la forma o color. 
• Deben evitar pulsaciones accidentales. 
• Monitor: 
• El color, brillo y contraste se deben poder ajustar. 
• Debe evitar parpadeos. 
• Conexiones USB y de audio frontales. 
11.3. Software 
 
Soluciones básicas de accesibilidad para Software. 
• Los programas (y el SO) deben permitir: 
• Elegir el dispositivo de control estándar de entrada (teclado, ratón u otro alternativo). 
• La utilización de dispositivos especiales para personas con discapacidad (como ratón de 
cabeza). 

<!-- Page 79 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
79 
• Deben poder configurarse las características de accesibilidad. 
• Debe existir la posibilidad de salida de información en diferentes formatos: 
• Audio. 
• Braille. 
• Texto. 
• Imágenes. 
• Etcétera. 
• El lenguaje debe ser claro, sencillo y directo: 
• Debe adaptarse al nivel del usuario, evitar anglicismos y jerga informática. 
• Los mensajes de aviso deben: 
• Ser sonoros. 
• Ser visuales. 
• Permanecer hasta que el usuario confirme que los ha leído. 
• Debe haber protección de errores accidentales: 
• Debe permitir deshacer la acción. 
• Debe avisar antes de realizar una acción si no puede deshacerse. 
• No debe haber elementos parpadeantes que puedan producir ataques epilépticos. 
• El sistema operativo debe disponer de un emulador de teclado manejado por ratón y de un 
emulador de ratón manejado por el teclado. 
• Debe poder variarse el tamaño y forma del puntero del ratón, así como su velocidad. 
• Se podrá configurar el tiempo de pulsación de un botón para que se reconozca la pulsación. 
• Los programas y el sistema operativo deben ser compatibles con la incorporación de ayudas 
técnicas. 
• Debe poder modificarse el tipo de letra, el tamaño y el color de los textos. 
• El color no debe ser la única forma de información. 

<!-- Page 80 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
80 
• Debe ofrecerse la descripción verbal de procesos e imágenes que aparecen en pantalla. 
• Los iconos e imágenes deben llevar una etiqueta de texto asociada que explique su significado. 
• Los programas y el sistema operativo deben ser compatibles con programas de reconocimiento 
de voz y con soportes en lengua de signos. 
 
 
 
 
Ejemplo 
Clic: 
Es una herramienta para crear un curso web que permite crear 
aplicaciones multimedia para Windows, siendo además de libre 
distribución. 
 
11.3.1. Aplicaciones para ayudar a personas con problemas 
de Accesibilidad 
Puesto que la sociedad actual, desde hace algunos años, está muy concienciada de barreras de 
determinados colectivos para el uso de las tecnologías, y también para utilizarlas en ayuda de personas 
con discapacidades, que les impiden que puedan comunicarse, se han ido desarrollando diferentes 
elementos de hardware y/o software que proporcionan soluciones a estos colectivos. 
Vamos a indicar algunas aplicaciones: 
• NVDA. 
Acrónimo de Non Visual Desktop Access. 
Es un lector de pantalla libre y gratuito (de código abierto), que funciona con Microsoft 
Windows, y que permite a personas ciegas o con discapacidad visual usar ordenadores. 
Puede convertir el texto en braille (para lo cual, el usuario debe disponer de "pantalla Braille"), o 
puede leer el texto de la pantalla mediante una voz sintética. 
Se puede controlar lo que NVDA lee moviendo el cursor (mediante el ratón o las teclas de 
flechas del teclado) al área relevante que contiene el texto. 
Actualmente es el más popular en todo el mundo. 

<!-- Page 81 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
81 
NVDA facilita la educación y empleo a personas con discapacidad visual y también les da acceso 
a redes sociales, servicios online (compra, bancos…). 
Se puede descargar y llevarlo en un pen drive… para poderlo instalar en un ordenador con 
Windows. 
NVDA es desarrollado por NV Access. 
• JAWS. 
Acrónimo de Job Access With Speech. 
Es un software lector de pantalla para personas ciegas o con visión reducida. 
Se trata de identificar e interpretar aquello que se muestra en pantalla, convirtiéndolo en sonido 
o en una pantalla Braille actualizable, de manera que el usuario puede acceder o navegar por él 
sin necesidad de verlo. 
JAWS era el primer lector de pantalla más popular en todo el mundo, actualmente ha sido 
desplazado por NonVisual Desktop Access. 
• Licornio. 
Es un dispositivo físico ergonómico que consistente en un casco con una varilla metálica 
incorporada, a la que se puede fijar en el extremo un puntero o lápiz permitiendo e el control de 
diferentes elementos mediante la cabeza (como teclear…). 
Indicado para personas con parálisis cerebral, o discapacidad física (lesión medular, esclerosis 
múltiple, ELA, enfermedades neuromusculares...). 
• WebCT. 
Siglas de Web Course Tools, en castellano Herramientas para Cursos Web. 
Es un sistema comercial de aprendizaje virtual en línea, el cual es usado principalmente por 
instituciones educativas para el aprendizaje a través de Internet. 
La flexibilidad de las herramientas para el diseño de clases hace este entorno muy atractivo 
tanto para principiantes como usuarios experimentados en la creación de cursos en línea. 
Es posible añadir a los cursos WebCT varias herramientas interactivas (tableros de discusión o 
foros, sistemas de correos electrónicos, chats…). 
El espacio WebCT es fácil de usar e innovador. El sistema está instalado en un servidor del web 
de la Oficina Central Sistémica (OCS) de la Universidad Interamericana de Puerto Rico. 

<!-- Page 82 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
82 
• Virtea. 
Ha sido desarrollada por la compañía murciana Answare Tech, con el objetivo de ayudar a 
personas con Trastorno del Espectro Austista (TEA). 
Es una aplicación de Realidad Virtual móvil que recrea distintos escenarios de la vida cotidiana, 
que pueden crear desasosiego en estas personas, para ayudarlas a afrontar situaciones fuera de 
su rutina habitual como, por ejemplo: esperar el autobús, ir al médico, cortarse el pelo, etc. 
• Tur4all. 
Es una aplicación promovida por la Plataforma Representativa Estatal de Personas con 
Discapacidad Física (Predif) y elaborada con el apoyo de la Fundación Vodafone. 
Este software ayuda a encontrar todo tipo de puntos turísticos (alojamientos, bares, 
restaurantes, museos, etc.) sin barreras para una silla de ruedas o para personas con movilidad 
reducida. 
• Be my eyes. 
Se crea en 2012 en Dinamarca por Hans Jorgen Wiberg. 
Su objetivo es ayudar a personas con visibilidad nula o reducida a reconocer objetos de su vida 
cotidiana con la ayuda de otras personas con una visión normal, poniendo en contacto a ambas 
partes por videollamada, que suele tener una duración inferior a 30 segundos. 
Por ejemplo, para diferenciar un jersey de diferente color o encontrar algo que se haya caído al 
suelo. 
El usuario con déficit visual solicita ayuda a través de la aplicación, y esta envía una notificación 
a un voluntario, teniendo en cuenta el idioma y la zona horaria. 
• Soy Cappaz. 
Es una aplicación gratuita, lanzada por la Fundación Mapfre y la Fundación GMP para ayudar a 
las personas con discapacidad a incorporarse al mundo laboral. 
Incluye funcionalidades como: 
• Un calendario sincronizado con Google Calendar para que las personas de apoyo puedan 
actualizar citas importantes y actividades programadas. 
• Facilita la puesta en contacto con el personal de apoyo cuando el usuario necesite ayuda. 
• Una función para realizar desplazamientos de forma autónoma y segura, marcando las 
rutas a seguir y también informando a las personas de apoyo de retrasos o desviaciones que 
puedan darse durante el recorrido. 
• Muestra mediante vídeos, cómo realizar determinadas tareas rutinarias en el área laboral y 
personal, por ejemplo, cómo escanear o imprimir documentos, cómo utilizar un 
electrodoméstico. 

<!-- Page 83 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
83 
• Día a día. 
Se trata de un diario visual desarrollado para ayudar a las personas con autismo o con 
dificultades en todo lo relacionado con la comunicación. 
Desarrollado por la Fundación Orange y BJ Adaptacione. 
Permite guardar de forma estructurada las acciones realizadas a lo largo de la jornada mediante 
fotografías o ilustraciones, y revisarlas, de forma que se avisará de cambios de rutina según las 
fechas del calendario, para que el usuario pueda ser consciente con anticipación de la llegada de 
la Navidad o de las vacaciones de verano. 
Puede ajustarse a las necesidades de cada usuario, por ejemplo, añadiendo fotos o imágenes 
representativas de las personas de su entorno en las actividades programadas, para 
identificarlas. 
• Lazzus. 
Es una aplicación de origen asturiano, que crea un asistente mediante un campo de visión 
auditivo, para acompañar a personas con discapacidad visual en sus desplazamientos. 
Proporciona la información que va encontrando a su alrededor, (en un radio de 100 m) tanto de 
pasos de peatones, cruces, escaleras, bocas de metro, como de establecimientos, museos, 
parques y otros espacios de referencia a los que se acerque. 
Tiene diferentes formas de uso, por ejemplo, el modo transporte, que se activa 
automáticamente cuando se viaja en autobús o coche, indicando al usuario en qué lugar se 
encuentra a medida que avanza, para evitar su desorientación. 
• Wheelguide. 
Es una aplicación para ayudar a personas con movilidad reducida. Se informa sobre las 
dificultades de movilidad para sensibilizar al público en general de las dificultades para personas 
con problemas de movilidad. Se evalúan edificios en función de su accesibilidad. 
• Race Together! 
Es un juego para personas con problemas de visión, donde se escucha el sonido del coche que 
llevas por delante y hay que seguirlo sin chocar con él. Se basa en la aplicación de carreras de 
Run with me. 
• TintVision. 
Esta aplicación está orientada especialmente para personas con dislexia u otros problemas de 
visión. Utiliza la superposición de colores para facilitar a estas personas la navegación, utilizando 
un esquema de color de alta densidad. 

<!-- Page 84 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
84 
• WheeLog! 
Es una aplicación para personas con problemas de movilidad, que trabaja conjuntamente con 
Google MAps, y crea un mapa interactivo ofreciendo datos de lugares accesibles como 
restaurantes y baños, y también las rutas que usuarios en sillas de ruedas han realizado. 
Los usuarios interactúan entre sí compartiendo sus experiencias y solicitando información sobre 
lugares concretos. 
11.4. Internet 
 
Fuente: Pixabay 
Soluciones básicas de accesibilidad para Internet. 
• Imágenes y animaciones: 
• Se deberá usar el atributo "alt" para describir la función de cada elemento visual. 
• Mapas de imagen: 
• Se deberá usar el elemento "map" y texto para las zonas activas. 

<!-- Page 85 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
85 
• Texto: 
• Debe ser claro y simple. 
• El lenguaje debe estar adaptado al nivel comprensivo del usuario, evitando anglicismos y 
jerga informática. 
• Sería útil incluir un vídeo en lengua de signos que complemente al texto. 
• Multimedia. Se deben proporcionar: 
• Subtítulos. 
• Transcripción del sonido. 
• Descripción del vídeo. 
• Organización de las páginas: 
• Se deberán usar encabezados, listas y estructura consistente. 
• Usar CSS para la maquetación siempre que sea posible. 
• Figuras y diagramas: 
• Se deben describir brevemente en la página o usar el atributo "longdesc". 
• Scripts, apletts y plug-ins: 
• Se ofrecerá contenido alternativo si las funciones no son accesibles. 
• Marcos: 
• Se deberá usar el elemento "noframes" para cuando no se admitan. 
• Tablas: 
• Se deberá facilitar la lectura línea a línea. 
• Revisar la accesibilidad: 
• Se deberá verificar mediante el uso de las herramientas, puntos de comprobación y pautas 
de WCAG. 
Revisar una página web es muy sencillo con herramientas automáticas, ya que estas pueden encontrar 
los problemas de accesibilidad más importantes. 
Sin embargo, una revisión formal para adaptar un sitio web a las directrices del W3C requiere 
profesionales especializados. 

<!-- Page 86 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
86 
 
 
 
+ Info 
Puedes realizar un test de accesibilidad web en la página web que 
te proponemos. 
www.tawdis.net 
 
11.5. Diseño de interfaces: las ocho reglas de oro 
Existen multitud de autores y organizaciones que proponen principios generales de diseño de 
interfaces. 
Uno de los resúmenes más conocidos e interesante son las Ocho reglas de oro del diseño de interfaces 
(Shneiderman, B., Plaisant, C.): 
1. Consistencia: 
En situaciones parecidas deberían exigirse secuencias de acciones parecidas. 
2. Usabilidad universal: 
Se debería reconocer la diversidad de usuarios y permitir la transformación del contenido para 
adaptarse a estos. 
Por ejemplo: 
• Por diferencias de nivel (principiante-experto). 
• Rangos de edad. 
• Discapacidades. 
• Diversidad tecnológica. 
3. Realimentación informativa: 
Cada acción del usuario debe tener una realimentación del sistema, proporcional en la medida 
de la importancia de las primeras. 
Por ejemplo: 
• Acciones comunes deberían realimentar de manera que no entorpezca el trabajo del 
usuario pero que el mismo esté seguro de la realización de su acción. 
• Acciones poco comunes deben alertar de la situación y las consecuencias de manera 
precisa. 

<!-- Page 87 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
87 
4. Guiar hacia la consecución de la tarea: 
• Las tareas se deben organizar como secuencia de acciones con principio y fin. 
• La interfaz debe guiar, mediante diálogos y mensajes de realimentación, desde el principio 
al final de la tarea. 
5. Prevención de errores: 
Se debe evitar en lo posible que el usuario pueda cometer errores: 
• Restringiendo los tipos y tamaños de entrada. 
• Deshabilitando elementos no adecuados para el estado de tarea actual. 
• Permitiendo la recuperación a partir de errores. 
6. Deshacer acciones: 
• Las acciones realizadas por el usuario deberían poder deshacerse fácilmente. 
• Se fomenta la exploración de nuevas funcionalidades sin miedo, al poder deshacer cualquier 
acción. 
7. Dar soporte al locus de control interno: 
• El usuario debe tener la sensación de mandar sobre la interfaz y no al revés. 
• La interfaz debe responder de manera determinista a las acciones de este. 
8. Reducción de la carga de memoria a corto plazo: 
• El ser humano tiene una memoria a corto plazo muy limitada. 
• El usuario debe saber en todo momento: 
» Dónde está. 
» Cómo ha llegado. 
» Hacia dónde va. 
• Se debe proporcionar ayuda en línea y ayuda contextual del modo de realización de 
acciones complejas que no estén claras de manera visual. 
 

<!-- Page 88 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
88 
 
 
 
+ Info 
El término locus de control hace referencia al grado en que las 
personas sienten que tienen el control de lo que ocurre en sus 
vidas. 
Existen dos tipos según a qué o quién atribuimos el mando de 
nuestro destino: 
• Locus de control interno. Nuestras decisiones o 
capacidades. 
• Locus de control externo: a fuerzas externas como Dios, la 
suerte o el karma. 
 
11.6. Atributos ARIA 
Los atributos ARIA son herramientas esenciales para mejorar la accesibilidad de las aplicaciones web 
interactivas, proporcionando información adicional a las tecnologías de asistencia sobre el 
comportamiento y la estructura de los elementos web. Los atributos ARIA permiten a los 
desarrolladores de sitios web mejorar la accesibilidad de interfaces dinámicas, especialmente cuando los 
elementos HTML no son suficientes para describir el comportamiento o los estados de ciertos 
componentes interactivos. ARIA es especialmente útil en aplicaciones web interactivas que utilizan 
tecnologías como JavaScript y AJAX, donde el contenido puede cambiar de manera dinámica. Los 
atributos son interpretados por tecnologías de asistencia, como lectores de pantalla, para proporcionar 
una experiencia de usuario más inclusiva y accesible para personas con discapacidades. 
El objetivo es que las aplicaciones web sean accesibles para todos los usuarios, cumpliendo con 
estándares como las WCAG (Web Content Accessibility Guidelines). Como ejemplo podemos poner el 
de un botón con un ícono (sin texto visible) podría usar aria-label="Buscar" para describir su función a 
un lector de pantalla. 
Lo usan herramientas como lectores de pantalla (NVDA, JAWS, VoiceOver, etc.), magnificadores de 
pantalla, o dispositivos Braille que interpretan los atributos ARIA para comunicar información a los 
usuarios con discapacidades visuales, auditivas, motrices o cognitivas. 
No deben ser usados estos atributos si el elemento HTML estándar ya cubre la funcionalidad de 
accesibilidad. Se debe actualizar los atributos ARIA si el estado de un elemento cambia. Los valores de 
los atributos deben ser precisos y fáciles de entender para los usuarios de tecnologías de asistencia. 
• aria-live: Indica que un área de la página web se actualizará dinámicamente y define la prioridad 
con la que las tecnologías de asistencia deben anunciar los cambios en el contenido. Valores 
comunes: off, polite, assertive. 

<!-- Page 89 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
89 
<div aria-live="assertive">Este mensaje debe ser leído de inmediato.</div> 
• aria-checked: Indica el estado de un elemento que puede ser marcado o desmarcado, como una 
casilla de verificación o un botón de opción. Valores comunes: true, false, mixed. 
<input type="checkbox" aria-checked="true" /> Acepto los términos y condiciones 
• aria-flowto: Define el flujo de navegación entre elementos en la página, indicando la secuencia 
de enfoque para los usuarios de tecnologías de asistencia. Este atributo especifica a qué 
elementos se deben mover al navegar a través de la interfaz. 
<div aria-flowto="nextSection">Contenido interactivo</div> 
• aria-valuenow: Representa el valor actual de un control de interfaz de usuario que tiene un 
rango, como un control deslizante. También se utilizan otros atributos como aria-valuemin y 
aria-valuemax para especificar los valores mínimo y máximo, respectivamente. 
<input type="range" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" /> 
• aria-hidden: Indica que un elemento es completamente oculto a las tecnologías de asistencia, es 
decir, no debe ser anunciado ni considerado por las herramientas como lectores de pantalla. 
Valores comunes: true, false. 
• aria-label: Proporciona una etiqueta accesible para un elemento cuando no es adecuado o 
posible usar un texto visible. Por ejemplo, para un botón con solo un ícono. 
• aria-labelledby: Proporciona una referencia a un o más elementos en la página que sirven como 
etiquetas para el elemento. Es útil cuando el texto visible no es adecuado para describir un 
elemento de manera completa. 
• aria-describedby: Similar a aria-labelledby, pero se utiliza para proporcionar una descripción 
adicional sobre el propósito o la función de un elemento. Esto puede ayudar a los usuarios a 
comprender mejor el contexto. 
• aria-role: Define el rol de un elemento en la interfaz. Ejemplos de roles incluyen button, link, 
alert, navigation, dialog, entre otros. Define el tipo de interacción o el propósito del elemento en 
el contexto de la accesibilidad. 

<!-- Page 90 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
90 
• aria-expanded: Indica si un elemento, como un menú desplegable o un acordeón, está 
expandido o colapsado. Valores comunes: true, false. 
• aria-required: Indica que un campo de entrada es obligatorio para la presentación de un 
formulario. Valores comunes: true, false. 
• aria-invalid: Indica que el valor de un campo de entrada es inválido. Usado en formularios 
cuando los datos ingresados no cumplen con los requisitos. Valores comunes: true, false. 
• aria-disabled: Indica que un elemento interactivo está deshabilitado y no se puede interactuar 
con él. Valores comunes: true, false. 
• aria-controls: Define la relación de control entre un elemento (por ejemplo, un botón) y el 
contenido que controla (por ejemplo, una sección oculta). Este atributo ayuda a las tecnologías 
de asistencia a identificar qué áreas de la página son controladas por un elemento. 
• aria-autocomplete: Se utiliza en los campos de entrada de texto para indicar el tipo de 
autocompletado disponible para el campo. Valores comunes: none, inline, list. 
• aria-modal: Indica que un elemento es una ventana modal que bloquea la interacción con el 
resto de la página hasta que se cierra. Valores comunes: true, false. 
11.7. Patrones de interacción en el diseño de interfaces 
de usuario 
Los patrones de interacción son soluciones reutilizables a problemas comunes en el diseño de 
interfaces. Su objetivo es optimizar la experiencia del usuario, facilitar el diseño de sistemas usables y 
ayudar a los desarrolladores -especialmente a los menos experimentados- a aplicar prácticas 
consolidadas. 
A diferencia de los patrones de diseño orientados a objetos (como los GoF), estos patrones no se 
centran en el código, sino en la forma en que el usuario interactúa con la interfaz. 
Los primeros en aplicar este enfoque al diseño de interfaces fueron Ward Cunningham y Kent Beck, 
quienes propusieron cinco patrones básicos: 
• Window per task. 
• Few panes. 
• Standard panes. 
• Nouns and verbs. 
• Short Menu. 

<!-- Page 91 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
91 
Posteriormente, diseñadores e investigadores como Martijn van Welie y Jennifer Tidwell ampliaron este 
trabajo, recopilando colecciones de patrones de interacción aplicables a la Web y a entornos gráficos 
modernos, basándose en la experiencia práctica de expertos en usabilidad. 
Estos patrones ayudan a crear interfaces más eficientes, intuitivas y coherentes, al tiempo que reducen 
los errores y el esfuerzo de aprendizaje del usuario. 
12. Herramientas de evaluación automática 
de accesibilidad 
Existen diferentes programas que escanean sitios web completos en busca de problemas de calidad. 
Vamos a ver algunos de ellos. 
• Achecker. 
Permite evaluar el contenido de una página web siguiendo los estándares de WCGA. 
AChecker realiza una evaluación de forma interactiva, cuando es incapaz de identificar un 
problema potencial, solicita ayuda al evaluador para realizar esta tarea manualmente. De código 
abierto y personalizable da soporte a WCAG 2.0 y 2.1. 
Desarrollada por ATRC (Adaptive Technology Resource Centre) y mayormente basada en web. 
• SortSite. 
Es una herramienta comercial con versión de prueba limitada, un rastreador web que escanea 
sitios web completos en busca de problemas de calidad que incluyen: accesibilidad; 
compatibilidad del navegador; vínculos rotos; Cómplice legal; optimización de búsqueda; 
usabilidad y cumplimiento de estándares web. Versión de escritorio y web disponibles. 
• Wave. 
Web Accessibility Tool. 
Es una extensión de Firefox y Chrome, sirve de herramienta para validar la accesibilidad de una 
página web, indicando la URL de la página a analizar o subiendo directamente la página. 
Permite elegir el nivel de análisis. 
No genera reportes tan detallados y amplios como SortSite. Wave es más útil para análisis 
rápidos y específicos de accesibilidad. 
• eXaminator. 
Es una herramienta en línea, que revisa el código de una página web y efectúa una serie de 
pruebas, adjudicando según los errores y aciertos detectados, una puntuación entre 1 y 10. Se 
distingue principalmente por sus funcionalidades específicas en términos de accesibilidad y 
usabilidad. 

<!-- Page 92 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
92 
Realiza la revisión mediante pruebas relacionadas con técnicas y fallos de las Pautas de 
Accesibilidad para el Contenido Web 2.0 (WCAG 2.0). 
Su calificación no puede considerarse una medida de la accesibilidad general de la página, 
algunas pruebas pueden estar sujetas a interpretación según la configuración de la página 
evaluada. 
• QualWeb. 
Una herramienta que evalúa la accesibilidad de un sitio web según los estándares WCAG. 
Proporciona un análisis automático de la página, destacando áreas donde la accesibilidad puede 
mejorarse y proporcionando informes detallados para guiar a los desarrolladores en el 
cumplimiento de los requisitos de accesibilidad. Proporciona informes detallados y es 
particularmente útil para proyectos que requieren validación exhaustiva de accesibilidad tanto 
en plataformas de escritorio como móviles. 
• Axe. 
Es una herramienta de código abierto que realiza auditorías de accesibilidad y se integra bien en 
entornos de desarrollo, como Chrome DevTools y Firefox. Axe facilita la identificación de 
problemas de accesibilidad y su solución rápida. Es una de las herramientas más potentes y 
utilizadas para la auditoría de accesibilidad web. Su integración con navegadores y herramientas 
de automatización la convierte en una opción preferida para equipos de desarrollo que buscan 
integrar la accesibilidad en sus flujos de trabajo ágiles. 
• Tenon. 
Destaca por su capacidad de integrarse en flujos de trabajo personalizados mediante una API, su 
enfoque detallado en los informes y su utilidad tanto para pruebas automatizadas como 
manuales, lo que lo convierte en una opción robusta y flexible para equipos de desarrollo que 
buscan cumplir con las normas de accesibilidad web. 
• Lighthouse. 
Extensión de Google Chrome que realiza auditorías de accesibilidad, rendimiento y mejores 
prácticas. Ofrece un análisis completo del sitio web. Facilita auditorías de accesibilidad, 
rendimiento y mejores prácticas. 
• Accessi.org. 
Es una plataforma online que facilita la evaluación y mejora de la accesibilidad web. Planteada 
específicamente para personas con diversidad funcional, proporcionando herramientas que 
permiten evaluar la accesibilidad web y mejorar la experiencia de usuario para personas con 
discapacidades. Su capacidad para detectar problemas relacionados con los estándares WCAG, 
junto con su interfaz fácil de usar, la convierte en una herramienta útil tanto para 
desarrolladores novatos como experimentados que deseen garantizar que sus sitios sean 
accesibles para todos los usuarios, incluidas personas con discapacidades. 

<!-- Page 93 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
93 
• Pally. 
Herramienta de código abierto para realizar pruebas automáticas de accesibilidad, generando 
informes detallados basados en las pautas WCAG. Es útil tanto para desarrolladores como para 
auditores de accesibilidad. Se distingue por su enfoque en la simplicidad. Pally está pensada para 
facilitar el acceso a la información para los propios usuarios con discapacidades, ayudándoles a 
navegar por sitios web de manera más efectiva. 
13. Confidencialidad y disponibilidad de la 
información en puestos de usuario final 
La información de la empresa constituye uno de los activos más importantes (junto con el personal). 
Por lo tanto, la seguridad de la información es un punto vital en cualquier empresa. 
Hay un estándar para controlar la seguridad de la información. 
Es e ISO/IEC 27002 (anteriormente denominada ISO 17799), publicado por la Organización 
Internacional de Normalización y la Comisión Electrotécnica Internacional. 
La versión más reciente es la ISO/IEC 27002:2013. 
Su objetivo de es proporcionar una base común para desarrollar normas de seguridad dentro de las 
organizaciones y ser una práctica eficaz de la gestión de la seguridad. 
La adaptación española de la norma se denomina UNE-ISO/IEC 17799. 
UNE-ISO/IEC 17799 
Se trata de una norma NO CERTIFICABLE, pero que recoge la relación de controles a aplicar (o al 
menos, a evaluar) para establecer un Sistema de Gestión de la Seguridad de la Información (SGSI) 
según la norma UNE 71502, CERTIFICABLE. 
La seguridad de la información se define como la preservación de: 
• Confidencialidad. 
Aseguramiento de que la información es accesible sólo para aquellos autorizados a tener acceso. 
• Integridad. 
Garantía de la exactitud y completitud de la información y de los métodos de su procesamiento. 
• Disponibilidad. 
Aseguramiento de que los usuarios autorizados tienen acceso cuando lo requieran a la 
información y sus activos asociados. 

<!-- Page 94 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
94 
 
Pilares de la protección de la información 
 
 
 
Recuerda 
La seguridad de la información se articula sobre tres dimensiones, 
que son los pilares sobre los que aplicar las medidas de protección 
de nuestra información: 
• Disponibilidad de la información. 
• Integridad de la información. 
• Confidencialidad de la información. 
 
13.1. Disponibilidad e integridad de la información 
La disponibilidad de la información se refiere a que la información esté accesible cuando la necesitemos. 
Algunos ejemplos de falta de disponibilidad de la información son: 
• Cuando no podemos acceder al correo electrónico corporativo: 
• Por un error de configuración. 
• Cuando se sufre un ataque de denegación de servicio. 
Hace referencia a que la información sea correcta y esté libre de modificaciones y errores. La 
información ha podido ser alterada (posiblemente de forma intencionada) o ser incorrecta. 

<!-- Page 95 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
95 
Esto es un problema grave, ya que, normalmente, basamos nuestras decisiones en dicha información. 
Algunos ejemplos de ataques contra la integridad de la información son: 
• La alteración malintencionada de los ficheros del sistema informático mediante la explotación 
de una vulnerabilidad. 
• La modificación de un informe de ventas por un empleado malintencionado o por error humano. 
13.1.1. La confidencialidad de la información 
Implica que la información sea accesible solamente por el personal autorizado. Es lo que se conoce 
como need-to-know. 
Este término hace referencia a que la información solo debe ponerse en conocimiento de las personas, 
entidades o sistemas autorizados para su acceso y que realmente necesiten utilizarla. 
Ejemplos de falta de confidencialidad son: 
• El robo de información confidencial por parte de un atacante a través de Internet. 
• La divulgación no autorizada a través de las redes sociales de información confidencial. 
• El acceso por parte de un empleado a información crítica de la compañía ubicada en carpetas sin 
permisos asignados, a las que no debería tener acceso. 
La evaluación de los activos de información de la organización en relación con estas tres dimensiones de 
la seguridad determina la dirección a seguir en la implantación y selección de medidas (controles o 
salvaguardas). 
También debemos tener en cuenta que la adopción de un determinado control para mejorar la 
seguridad en una dimensión puede afectar de forma negativa o positiva a otra de las dimensiones. 
Es esencial conocer cuál de estas dimensiones es más importante proteger en cada sistema de 
información y llegar a una solución de compromiso entre las tres dimensiones. 
 
 
 
 
Ejemplo 
Implantar un control de acceso para proteger la confidencialidad 
en un aparato médico de una sala de operaciones. 
Esto produciría un retardo en el acceso a la información. Por lo 
tanto, se ve afectada su disponibilidad. 
 

<!-- Page 96 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
96 
Importancia de la información 
Dependiendo del sector de negocio el tratamiento será diferente. Por ejemplo: 
• Ámbito sanitario. Se maneja gran cantidad de información sensible de pacientes, por lo que se 
deben aplicar medidas para evitar el acceso no autorizado y la pérdida de información. También 
será necesario llevar un registro de accesos y modificaciones. 
• Sector financiero. La difusión no autorizada de información confidencial puede conllevar 
pérdidas económicas y perjuicio para los clientes. 
• Sector industrial o de desarrollo de servicios. Hay que salvaguardar los procesos, técnicas, 
patentes, etc. que suponen una ventaja frente a la competencia. 
Hay dos tipos de datos que tienen especial importancia. 
• Datos personales: 
Gestionados por la legislación sobre protección de datos de carácter personal. 
Esta legislación exige la protección de la seguridad de los datos de carácter personal ante 
posibles riesgos que afecten a la privacidad de las personas. 
• Datos sensibles: 
Estos datos exigen una protección reforzada y están sujetas a un régimen jurídico especial. 
• Datos personales que revelan: 
» Ideología. 
» Afiliación sindical. 
» Opiniones políticas. 
» Creencias religiosas y otras creencias. 
• Datos personales que revelan: 
» El origen racial o étnico. 
» Relativos a la salud. 
» Relativos a la vida sexual. 
» Relativos a la orientación sexual. 
» Datos genéticos. 
» Datos biométricos. 
• Datos de condenas penales o administrativas. 

<!-- Page 97 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
97 
Clasificar la información 
En primer lugar, revisaremos qué información tratamos y seleccionaremos: 
• La información crítica. 
• La que está sujeta a la ley. 
• La que, si nos faltara, o si se corrompiera, paralizaría nuestra actividad. 
A continuación, podemos clasificarla en niveles. Por ejemplo: 
• Confidencial. 
Datos sensibles para la organización y datos de carácter personal. 
Tratamiento: 
• Esta información debe marcarse adecuadamente. 
• Se deben implementar todos los controles necesarios para limitar el acceso a la misma 
únicamente a aquellos empleados que necesiten conocerla. 
• En caso de sacarla de las instalaciones de la empresa en formato digital, debe cifrarse. 
• Para los datos de carácter personal, se deben tener en cuenta la protección y garantías 
indicadas en la legislación sobre la materia. 
• Interna. 
Información accesible solo por los empleados. 
Tratamiento: 
• Esta información debe estar adecuadamente etiquetada. 
• Debe estar accesible para todo el personal. 
• No debe difundirse a terceros salvo autorización expresa de la dirección de la empresa. 
• Pública. 
Sin restricciones de difusión, como la página web de la empresa. 
No necesita ningún tratamiento especial. 

<!-- Page 98 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
98 
13.1.2. Responsabilidades del usuario 
• Acceso a la información. 
• Los usuarios de la información son responsables, mientras tengan la información bajo su 
control, de mantener los niveles de protección establecidos para la misma en todo 
momento. 
• Es responsabilidad de los usuarios identificar riesgos asociados a disponer de la información 
en su puesto de trabajo e iniciar las acciones para mitigarlos. 
• Copias de seguridad. 
• Los usuarios son responsables de alojar la información que necesita ser respaldada en los 
lugares establecidos para ello. 
• Escritorio limpio: 
• Las oficinas son visitadas por personal externo (clientes, limpieza, proveedores, etcétera). 
• El puesto de trabajo debe estar limpio y organizado. En caso contrario podría no darse 
cuenta de que le falta algo. 
• Se deben guardar los documentos sensibles y los elementos de almacenamiento de 
información en los cajones bajo llave mientras no los esté utilizando. 
• Es responsabilidad de cada usuario la protección de los sistemas de información a su cargo, 
por lo que debe asegurar físicamente su computador portátil con cables de seguridad en 
todo momento, para evitar robos. 
• Es responsabilidad de cada usuario la protección de la información a su cargo, por lo que no 
debe publicar o dejar a la vista documentos sobre datos sensibles, como: 
» Nombre de usuario y passwords. 
» Direcciones IP. 
» Contratos. 
» Números de cuenta. 
» Listas de clientes. 
» Propiedad intelectual. 
• Datos de empleado. 
• Cualquier información que no sea pública. 
• Los usuarios deberán tomarse el tiempo necesario antes de abandonar la oficina para 
recoger y asegurar el material sensible. 

<!-- Page 99 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
99 
• Bloqueo de sesión: 
• Los equipos informáticos deben permanecer bloqueados cuando el usuario no esté en su 
lugar de trabajo. 
• Protección contra software nocivo: 
• Cualquier usuario que sospeche de una infección por virus debe: 
» Apagar inmediatamente el computador involucrado. 
» Desconectarlo de la red. 
» Llamar al departamento encargado de la seguridad informática. 
• En ningún caso debe intentar eliminar el virus por su cuenta. 
• Solamente el personal encargado de la seguridad debe tratar la infección por virus de un 
ordenador. 
• El usuario no debe descargar e instalar software de distribuidores no confiables o 
desconocidos. 
• Protección durante la navegación en Internet: 
• Los usuarios deberán acudir a los cursos sobre los peligros de Internet y asimilarlos. Por 
ejemplo, no deberá: 
» Acceder a sitios desconocidos o de baja confianza. 
» Aceptar mensajes sobre instalación de software. 
» Descargar archivos sospechosos. 
• Los usuarios deberán abstenerse de visitar sitios restringidos por la organización de manera 
explícita o implícita. 
• Deberán evitar el acceso a sitios relacionados con la pornografía (especialmente si estos 
involucran a menores de edad, lo cual debe ser denunciado). 
• Está prohibida la descarga y uso de software malicioso o documentos que brinden 
información sobre cómo atentar contra la seguridad de la información. 
• Los usuarios no deben publicar información de la institución en sitios no autorizados (foros, 
etcétera). 
• No se deben descargar textos, imágenes, audio o vídeo protegidos por derechos de autor 
sin la previa autorización del autor. 

<!-- Page 100 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
100 
• En algunos casos, la descarga e instalación de cualquier tipo de software puede estar 
prohibida para el usuario, teniendo que realizar esta labor el personal informático. 
• Los usuarios deben ser conscientes de que la información transmitida desde su puesto de 
trabajo (incluida la de navegación) es propiedad de la institución y puede ser monitoreada 
por personal autorizado. 
14. Conceptos de seguridad 
 
Para la selección de las medidas de seguridad debemos tener en cuenta cuatro factores: 
• Determinar la importancia de la información que manejamos. Normalmente dependerá del 
sector de negocio. 
• Identificar, clasificar y valorar la información según su necesidad de seguridad. 
• Conocer la naturaleza de los controles que podemos implantar. 
• El coste de las medidas (que debe ser proporcional al riesgo). 
Naturaleza de los controles 
• Técnica. 
Medidas de carácter tecnológico dentro del ámbito de la seguridad. 
Son medidas técnicas: 
• Antivirus. 
• Cortafuegos. 
• Sistemas de copias de seguridad. 

<!-- Page 101 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
101 
• Organizativa. 
Medidas que se centran en la mejora de la seguridad teniendo en cuenta a las personas. 
Ejemplos: 
• Formación en seguridad. 
• Identificación de responsables. 
• Implantación de procedimientos formales de alta y baja de usuarios. 
• Física. 
Medidas físicas para proteger nuestra organización. 
Ejemplos: 
• Acondicionar adecuadamente la sala de servidores frente a riesgos de incendio, 
inundaciones o accesos no autorizados. 
• Establecer un sistema de control de acceso para entrar en las oficinas. 
• Poner cerraduras en los despachos y armarios. 
• Guardar las copias de seguridad en una caja ignífuga. 
• Legal. 
Medidas que persiguen el cumplimiento de la legislación vigente. 
14.1. Control de acceso a la información 
Por defecto, toda organización debe seguir el principio del mínimo privilegio. 
Este principio se traduce en que un usuario sólo debe tener acceso a aquella información estrictamente 
necesaria para desempeñar sus funciones diarias. 
Para conseguir este objetivo debemos realizar los siguientes pasos: 
• Definir los diferentes tipos de información que existen en nuestra organización. 
• Establecer quién puede acceder a cada tipo de información. 

<!-- Page 102 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
102 
La asignación de permisos sobre los recursos que contienen la información puede realizarse: 
• Individualmente. 
• Por perfiles. 
• Por grupos de usuarios. 
Es vital escoger medios que permitan la trazabilidad y que sean proporcionales al volumen de 
información. 
El uso correcto de contraseñas es primordial para la seguridad de la información. 
En todos los sistemas operativos podemos gestionar y controlar los usuarios, privilegios, contraseñas etc. 
14.2. Cifrado de la información 
La criptografía es una disciplina cuyo objeto es garantizar confidencialidad, integridad y autenticidad 
de los datos mediante diversas técnicas y herramientas. Las herramientas criptográficas, gracias a los 
algoritmos matemáticos que las componen, permiten el envío seguro de información a través de 
canales inseguros. Una de las técnicas que se emplean en criptografía es la del cifrado. 
El cifrado consiste en ofuscar la información mediante técnicas de codificación, evitando que los datos 
sean legibles por cualquier persona que desconozca la clave de decodificación. 
Estas técnicas son la mejor opción para el almacenamiento y transmisión de información sensible, ya 
que: 
• Permiten controlar el acceso a la información. 
• Limitan la difusión no autorizada en caso de pérdida o robo de soportes. 
Sin embargo, hay que tener en cuenta una serie de aspectos: 
• La clave debe ser robusta para dificultar el acceso no autorizado a la información. 
• La pérdida de la clave de acceso imposibilita el acceso a la información. 
 
 
 
 
+ Info 
En el Bloque IV, estudiaras la Criptografía para el cifrado de 
información, y tipos de algoritmos criptográficos. 
 

<!-- Page 103 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
103 
14.3. Copias de seguridad 
Las copias de seguridad son la salvaguarda básica para proteger la información. 
Dependiendo del tamaño y necesidades de la empresa, los soportes, la frecuencia y los procedimientos 
para realizar las copias de seguridad pueden ser distintos. 
El soporte escogido dependerá del sistema de copia seleccionado, de la fiabilidad que sea necesaria y de 
la inversión que deseemos realizar. 
En la implantación de un sistema de copias debemos tener en cuenta al menos las siguientes 
consideraciones: 
• Analizar la información que debemos respaldar y dónde se encuentra. 
• Establecer una política de copias de seguridad. 
• Realizar pruebas de restauración periódicas. 
• Controlar los soportes de copia mediante su correcto etiquetado y almacenamiento. 
• Si la información es confidencial, podría ser conveniente cifrarla. 
• Mantener copias fuera de la organización para protegernos de peligros como incendios o robo. 
14.4. Desechado y reutilización de soportes y equipos 
Antes de eliminar o reutilizar un soporte que haya almacenado información corporativa debemos 
aplicar las medidas de seguridad necesarias para evitar la recuperación de la información que tenían. 
Esto incluye: 
• Discos duros. 
• Cintas de copias. 
• CDs y DVDs. 
• Memorias USB. 
• Información en formato papel. 
Existen dos medidas básicas en relación con la información que almacene el soporte, según su destino: 
• Si vamos a reutilizarlo o entregarlo a otra persona, debemos realizar un borrado seguro del 
soporte. 
Un formateo simple no es suficiente. Se puede recuperar la información. 

<!-- Page 104 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
104 
El formateo de un disco marca el espacio como borrado, pero sigue conteniendo la información. 
Existen herramientas que sobrescriben la información con información aleatoria de forma que 
no se pueda recuperar. 
• Si vamos a desechar el soporte debemos garantizar que nadie lo reutilice. 
La mejor opción es "la destrucción física del soporte." 
15. Bibliografía 
• SHNEIDERMAN, B., PLAISANT, C. Diseño de interfaces de usuario. Estrategias para una 
interacción persona-computadora efectiva. Editorial Pearson. 
• https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/. 
• https://www.incibe.es/sites/default/files/contenidos/dosieres/metad_proteccion-de-la-
informacion.pdf. 
• http://accesibilidadweb.dlsi.ua.es/?menu=puntos-1.0. 
• http://accesibilidadweb.dlsi.ua.es/?menu=espanola. 
• http://accesibilidadweb.dlsi.ua.es/?menu=criterios-2.0. 
• https://es.wikipedia.org/wiki/Prueba_de_usabilidad. 
• http://du-accesibilidad.blogspot.com/2011/04/diseno-universal-definicion-y-sus-siete.html. 
• http://www.sidar.org/. 
• http://sidar.org/traducciones/wcag20/es/#visual-audio-contrast. 
• http://riberdis.cedd.net/bitstream/handle/11181/4655/la%20accesibilidad%20y%20el%20di
se%C3%B1o%20universal%20entendido%20por%20todos.pdf?sequence=1. 
• https://olgacarreras.blogspot.com/2005/01/referencia-sobre-legislacin-espaola.html. 
• https://es.wikipedia.org/wiki/ACID. 
• https://definicion.de/. 
• http://es.wikipedia.org. 
• https://es.wikipedia.org/wiki/Resource_Description_Framework. 
• http://grupofivasa.blogspot.com/2009/09/diseno-de-interfaces.html. 

<!-- Page 105 -->

 
 
Accesibilidad, Diseño Universal y Usabilidad. Confidencialidad y Disponibilidad de la información en puestos 
de usuario final. Conceptos de seguridad 
105 
• http://www.kicorangel.com/accesibilidad-y-usabilidad-en-la-web/. 
• https://www.psyciencia.com/locus-control-interno-externo/. 
• https://www.utp.edu.co/cms-
utp/data/bin/UTP/web/uploads/media/calidad/documentos/politicas_sgsi.pdf. 
• https://es.wikipedia.org/wiki/Algoritmo_criptográfico. 
 

<!-- Page 106 -->

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema08|Ficha Resumen del Tema 08]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque3-tema08|Nota Fuente Oficial del Tema 08]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema08-accesibilidad-wcag-usabilidad|Test Tema 08]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Flashcards Bloque 3]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema07|⬅️ Tema Completo 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema09|Tema Completo 09 ➡️]]
