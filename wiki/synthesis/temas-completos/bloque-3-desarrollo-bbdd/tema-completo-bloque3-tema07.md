---
title: "Tema Completo Extendido 07 (Bloque 3): Accesibilidad Web (WCAG 2.1 POUR y RD 1112/2018 Nivel AA)"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-3
  - tema-07
  - oposiciones-tai\nestado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque3-tema07-desarrollo-web-frontend.md]]"
  - "[[wiki/sources/bloque3-tema07]]"
created: "2026-08-18"
updated: "2026-08-18"
---
> [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema06|⬅️ Tema Completo 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema08|Tema Completo 08 ➡️]]

# 🔴 Tema Completo Extendido 07 (Bloque 3): Accesibilidad Web (WCAG 2.1 POUR y RD 1112/2018 Nivel AA)

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 07 correspondiente al Bloque 3 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

# 🔴 Bloque 3 - Tema 07 (UD012114): Aplicaciones y Desarrollo Web: HTML5, DOM, CSS, JavaScript, Servlets y JSP

<!-- Page 1 -->

 
 
Aplicaciones y desarrollo web 

<!-- Page 2 -->

ÍNDICE 
1. Conceptos básicos 
7 
1.1. Www. Link. Uri. 
7 
1.2. Lenguaje de marca 
9 
1.3. DOM 
10 
1.3.1. Shadow DOM 
13 
1.4. Etiqueta 
14 
1.5. Hojas de estilo 
15 
1.6. Estándar SGML 
15 
1.6.1. Un documento en SGML 
20 
1.6.2. Partes de un documento SGML 
21 
1.6.2.1. La declaración SGML 
21 
1.6.2.2. La DTD 
22 
1.6.2.3. Instancia de Documento 
25 
1.7. Script 
27 
1.8. Shell 
30 
1.9. Renderizado web 
30 
1.9.1. Primeros días del renderizado 
31 
1.9.2. La llegada de JavaScript: CSR y las SPA 
31 
1.9.3. Emergen las soluciones híbridas: SSR y la hidratación 
32 
1.9.4. El papel fundamental de los motores de renderizado 
32 
1.9.5. Conclusión 
32 
1.10. Motor de renderizado 
33 
2. Aplicaciones web 
34 
2.1. Protocolo HTTP 
36 
2.2. Servidor web Apache 
39 
2.3. Internet Information Services (IIS) 
43 
2.4. Servidor Web Nginx 
45 
2.5. Patrones de diseño GoF 
46 
2.6. Automatización de pruebas 
47 
2.7. Seguridad en aplicaciones web 
48 

<!-- Page 3 -->

 
 
3. Desarrollo web: cliente y servidor 
49 
3.1. Front-end: aplicaciones cliente 
50 
3.1.1. HTML 
51 
3.1.1.1. Estructura básica de una página web en HTML 
54 
3.1.1.2. Atributos 
58 
3.1.1.3. Principales elementos 
64 
3.1.1.4. HTML5 
78 
3.1.1.4.1. Elementos y atributos desaparecidos en HTML5 
81 
3.1.1.4.2. Novedades en HTML5 
84 
3.1.2. XSL 
88 
3.1.3. CSS 
89 
3.1.3.1. Formas de agregar CSS a HTML 
91 
3.1.3.2. Selectores de CSS 
94 
3.1.3.3. Tipos de selectores de CSS 
97 
3.1.3.3.1. Selector universal asterisco * 
97 
3.1.3.3.2. Selector de identificador único o ID '#' 
97 
3.1.3.3.3. Selector de clase 'E.E' 
97 
3.1.3.3.4. Selector de pseudo-clase 
99 
3.1.3.3.5. Pseudo-elemento 
101 
3.1.3.3.6. Selector de descendientes e f 
102 
3.1.3.3.7. Selector de hijos E>F 
103 
3.1.3.3.8. Selector de consecutivos: E+F (Adyacente) 
105 
3.1.3.3.9. Selector de hermanos: E~F 
106 
3.1.3.3.10. Selector de atributo a (letra a minúscula) 
106 
3.1.3.3.11. Otros selectores 
109 
3.1.3.4. Lista de selectores 
110 
3.1.3.5. Especificidad en CSS 
110 
3.1.3.6. Unidades de Medida CSS 
111 
3.1.3.7. CSS Flexible Box Layout Flexbox 
113 
3.1.3.8. Preprocesadores CSS 
115 

<!-- Page 4 -->

 
 
3.1.4. JavaScript 
115 
3.1.4.1. Atributos de eventos 
120 
3.1.4.2. Comparaciones en JavaScript 
122 
3.1.4.3. Framework de JavaScript 
124 
3.1.4.4. ECMAScript 7 
126 
3.1.5. Bootstrap 
127 
3.1.6. AJAX 
128 
3.2. Back-end: aplicaciones servidor 
129 
3.2.1. CGI (Common Gateway Interface) 
131 
3.2.2. ASP.NET (Active Server Pages) 
131 
3.2.3. Perl 
133 
3.2.4. Java 
133 
3.2.5. JSP (Java Server Pages) 
134 
3.2.6. Node.js 
134 
3.2.7. PHP (Hipertext Preprocesor) 
135 
3.2.8. Python 
141 
3.2.9. Apache Web Server 
146 
3.2.9.1. Apache Hadoop 
147 
3.2.9.2. JMeter 
148 
3.2.10. Ruby 
148 
3.3. Full stack 
148 
4. XML 
149 
4.1. Entidades 
153 
4.2. Tipos de nodos de XML 
154 
4.2.1. Nodo Raíz 
155 
4.2.2. Elemento 
155 
4.2.3. Cadenas de texto 
156 
4.2.4. Atributo 
156 
4.2.5. Espacio de nombres 
160 
4.2.6. Instrucción de procesamiento 
162 
4.2.7. Comentario 
163 

<!-- Page 5 -->

 
 
4.3. Extensiones 
163 
4.3.1. Estructurar documentos 
164 
4.3.1.1. DTD 
164 
4.3.1.2. XSD 
171 
4.3.2. Enlaces y direccionamiento 
172 
4.3.3. XPath 
172 
4.3.4. XPointer 
176 
4.3.5. XLink (XML Linking Language) 
176 
4.3.6. XSL (eXtensible Stylesheet Language) 
176 
4.3.7. WML (Wireless Markup Language) 
177 
4.3.8. KML: Keyhole Markup Languaje 
177 
4.4. Consultas XQuery 
177 
4.5. Programación. Análisis XML 
178 
4.6. Lenguaje de marcado para confirmaciones de seguridad 
182 
5. JSON 
182 
6. Content Management System (CMS) 
185 
6.1. WCMS (Web Content Management Systems) 
186 
6.1.1. Principales WCMS 
186 
6.1.2. Ciclo completo de gestión de contenidos: publicación, retirada y archivado 
187 
6.2. Constructores web y plataformas SaaS 
189 
6.3. Sistemas de gestión documental (ECM/DMS) 
189 
7. Desarrollo de aplicaciones móviles 
190 
7.1. Aplicación nativa o app nativa 
190 
7.2. Aplicación web o web app 
192 
7.3. Aplicaciones híbridas 
193 
7.3.1. Plataformas para el desarrollo de Apps 
193 
7.4. NDK y SDK: Herramientas complementarias para Android 
195 
7.4.1. Android SDK (Software Development Kit) 
195 
7.4.2. Android NDK (Native Development Kit) 
196 
7.5. Herramientas de Desarrollo para iOS 
196 

<!-- Page 6 -->

 
 
8. Navegadores web 
197 
8.1. Navegadores más usados 
198 
8.2. Comparativa de navegadores 
203 
9. Bibliografía 
204 
 

<!-- Page 7 -->

 
 
Aplicaciones y desarrollo web 
7 
1. Conceptos básicos 
Para entender bien lo que vamos a estudiar en este tema, vamos a definir primero unos conceptos que 
serán nombrados en multitud de ocasiones, que seguramente ya conocerás, y añadiremos algunos más 
importantes. 
• WWW, siglas de World Wide Web. 
• Link. 
• URI. 
• Lenguaje de marca. 
• Etiqueta. 
• Hojas de estilo. 
• Estándar SGML. 
• Script. 
• Shell. 
• Motor de renderizado. 
1.1. Www. Link. Uri. 
WWW, siglas de World Wide Web o red informática mundial. 
Es un sistema de distribución de documentos de hipertexto o hipermedia interconectados y accesibles a 
través de Internet. 
Con un navegador web, un usuario visualiza sitios web compuestos de páginas web que pueden 
contener textos, imágenes, vídeos u otros contenidos multimedia, y navega a través de esas páginas 
usando hiperenlaces. 
Un Hiperenlace o hipervínculo (del inglés hyperlink), o sencillamente enlace o vínculo (link), es un \nelemento de un documento electrónico que hace referencia a otro recurso, como por ejemplo un punto \nespecífico de un documento o de otro documento. 
URI, siglas de Uniform Resource Identifier, o identificador uniforme de recursos. 

<!-- Page 8 -->

 
 
Aplicaciones y desarrollo web 
8 
Se considera una URI a una cadena de carácteres que identifica de manera única un recurso o 
localización del mismo. Se utilizan para acceder a un recurso por Internet, estos recursos, pueden ser de 
muchos tipos. 
Un URI puede identificar una página web, al remitente o destinatario de un email. 
Un URI, está constituida por un URL más un URN, o por uno solo de ellos. 
 
• URL 
Siglas de Uniform Resource Locator. 
Una URL, es un localizador de recursos uniforme, cuyos recursos referidos pueden cambiar, esto \nes, la dirección puede apuntar a recursos variables en el tiempo. 
Están formados por una secuencia de caracteres de acuerdo con un formato modélico y \nestándar que designa recursos en una red como, por ejemplo, Internet. 
La URL (Uniform Resource Locator) indica la localización pero no contiene el recurso en sí (no 
siempre hay la misma información en la localización). Por ejemplo https://elpais.com, es una 
URL cuyo contenido cambia a diario, incluso un mismo artículo puede ser actualizado, así que 
nunca podrá ser URN. La metáfora sería decir que una URL sería la librería, estante y ubicación. 
Fueron usados por primera vez por Tim Berners-Lee en 1991, para permitir a los autores de 
documentos establecer hiperenlaces en la World Wide Web (WWW). 
Desde 1994, en los estándares de Internet, el concepto de LRU ha sido incorporado dentro del 
más general de URI, pero el término URL todavía se utiliza ampliamente. 

<!-- Page 9 -->

 
 
Aplicaciones y desarrollo web 
9 
• URN 
Acrónimo inglés de Uniform Resource Name (Nombre de Recurso Uniforme). 
La URN apuntaría al recurso en sí. Por ejemplo: 
Un documento técnico con su esquema DOI -digital object identifier ("Accelerating the 
Appropriate Adoption of Artificial Intelligence in Health Care: Protocol for a Multistepped 
Approach", doi:10.2196/30940), etc. 
Un libro con su esquema ISBN (La Isla del Tesoro en Tapa dura de Anaya isbn:9780195811391), 
un documento técnico con su esquema DOI -digital object identifier- ("Accelerating the 
Appropriate Adoption of Artificial Intelligence in Health Care: Protocol for a Multistepped 
Approach", doi:10.2196/30940), etc. 
El número de bastidor sería una URN si su esquema (VIN siglas americanas) fuera un estandar 
internacional, al no serlo no puede considerarse como tal. 
 
 
 
 
+ Info 
Una URI mixta es poco frecuente e incluiría dos esquemas y partes: 
urn:doi:10.1000/12345678/ftp://ftp.ejemplo.com/archivo.pdf 
https://www.ejemplo.com/documento/urn:isbn:978-1-234567-
89-0 
 
1.2. Lenguaje de marca 
Un lenguaje de marca, o de marcado es una forma de codificar un documento utilizando una notación \nespecial para marcar las diferentes secciones de dicho documento. Junto con el texto, incorpora \netiquetas o marcas que contienen información adicional acerca de la estructura del texto o su 
presentación. 
Un lenguaje de marcado, no es un lenguaje de programación, no tiene funciones aritméticas ni 
variables. 
Los desarrolladores de software pueden diseñar aplicaciones para leer los documentos escritos en un 
determinado lenguaje de marcado. 
 

<!-- Page 10 -->

 
 
Aplicaciones y desarrollo web 
10 
 
 
 
Atención 
Los documentos escritos en XML pueden leerse por medio de 
aplicaciones personalizadas utilizando diferentes objetos de análisis 
gramatical o pueden combinarse con el lenguaje de estilo \nextensible (XSL- Ex-tensible Stylesheet Language) para poder 
mostrarse en un navegador. 
Conclusión: 
Los navegadores de Web leerán los documentos HTML y Microsoft 
Office leerá los documentos de Office. 
 
1.3. DOM 
DOM (Document Object Model, traducido como Modelo de Objeto de Documento), es un modelo de 
representación jerárquica para los documentos HTML y XML, que facilita una representación \nestructurada jerárquicamente del documento web, donde existen varios objetos y unos dependen de 
otros estableciendo de qué forma pueden acceder los programas, para modificar, su estructura, estilo 
y/o contenido. 
DOM tiene como finalidad poder modificar el HTML de una página web de forma dinámica 
mediante Javascript. 
Con DOM, un documento XML se representa como un árbol jerárquico, permitiendo navegar desde un 
Node (nodo) a su padre, sus hijos o sus hermanos si los hay. Algunos Nodos pueden no tener hijos 
porque son finales, como, por ejemplo, los nodos de Text (texto). Las etiquetas XML se representan 
como Elements (elementos). 
Así pues, un navegador, utiliza el DOM, para representar una página web de forma estructurada, como 
un árbol con ramas, definiendo métodos para que se puedan estructurar el estilo y el contenido del 
archivo. 
A través del DOM se puede acceder a cualquier elemento, (párrafos, divisiones, tablas, formularios y sus 
campos, etc.) por medio de Javascript. Los programadores pueden construir scripts, navegar por su \nestructura, y añadir, modificar o eliminar elementos (alterar las propiedades de los objetos o invocar a 
sus métodos). 
Se pueden crear aplicaciones que sean personalizables por el usuario, y también es posible cambiar el 
layout de la página (cambio que no requiere actualización). 

<!-- Page 11 -->

 
 
Aplicaciones y desarrollo web 
11 
 
 
 
+ Info 
Se denomina con el término layout de la página web, al esquema 
de la distribución de los elementos dentro de ella. Este esquema \nestá compuesto por una serie de bloques en los que se coloca el 
contenido. El layout sería la presentación del documento. 
 
 
En ocasiones, se utilizan librerías y frameworks de JavaScript para simplificar el trabajo de 
programación, como jQuery. 
jQuery, nace en 2006 de la mano de John Resig y es una biblioteca de JavaScript creada para simplificar 
la manipulación del Modelo de Objetos del Documento (DOM). Su principal utilidad radica en permitir 
la selección de elementos, modificación de contenido, manejo de estilos y gestión de eventos de forma 
sencilla y con una sintaxis concisa. Además, ofrece herramientas avanzadas para trabajar con 
propiedades de elementos y realizar peticiones AJAX. Gracias a su enfoque intuitivo, jQuery se convirtió \nen una solución popular para el desarrollo web, especialmente antes del auge de frameworks modernos. 
Aunque su uso ha disminuido, sigue siendo relevante en proyectos heredados y entornos simples. 
Otras herramientas, como React o Lit, permiten manipular la página mediante componentes \nencapsulados, evitando trabajar directamente con el DOM y utilizando sistemas de plantillas web y \nenlaces de datos para gestionar el contenido dinámico de manera eficiente. 
 
 
 
 
+ Info 
La diversidad de funcionamiento de los navegadores y las 
diferencias de interpretación del código HTML y JavaScript 
motivaron la aparición de librerías que solventarían este problema 
al crear una capa de abstracción que permitiera a los 
desarrolladores web realizar su trabajo evitando problemas de 
compatibilidades. La primera de ellas fue CrossBrowser DHTML, 
que no llegó a utilizarse mucho. Posteriormente apareció jQuery 
que sí fue y continúa siendo muy utilizada. 
 
 
La constante evolución de Intenet empujada por la demanda popular de interactividad en las páginas 
web obligó a los grandes fabricantes, a buscar soluciones en un lenguaje script que la hiciera posible. 
Netscape Communications Corporation desarrolla e implementa un lenguaje script, JavaScript, en su 
navegador en 1995. Lenguaje que llegó a ser usado posteriormente por su rival de Microsoft, Internet 
Explorer, entre otros. 

<!-- Page 12 -->

 
 
Aplicaciones y desarrollo web 
12 
La necesidad de obtener un funcionamiento estable y coherente del lenguaje lleva a la organización 
ECMA, nacida en 1961, a desarrollar una especificación el ECMAScript (aceptado hoy como estándar 
ISO/IEC 22275:2018) publicada por primera vez en 1997. 
El DOM Nivel 1 aparece al surgir la necesidad de manipular documentos HTML y XML en los 
navegadores. Varios actores entre los que encontraremos Netscape, Microsoft, participan en su 
desarrollo. La ECMA, como veíamos, creadora de la especificación de JavaScript y la W3C (a través del 
grupo Web Platform Working Group) como organización lider en la estandarización fueron partícipes \nen su desarrollo. 
Desde la creación del DOM, se han ido creando muchas versiones, agregando distintas funcionalidades, 
como, por ejemplo, querySelector, la Manipulación de eventos y Serialization. 
La estandarización del DOM ha permitido que todos los navegadores funcionen de igual modo, 
respondiendo a un API muy consistente de funcionalidades sobre los elementos de la página, facilitando \nel trabajo de los programadores, por lo que actualmente es posible crear código Javascript nativo, que 
funcione correctamente en todos los navegadores sin la necesidad de preguntar en qué navegador se \nestá ejecutando el código, ni necesidad del uso de librerías. 
 
 
 
 
+ Info 
HeadingsMap 
Es una extensión gratuita para un navegador web, específica para 
poder mostrar la estructura del documento según HTML5 (los \nencabezados). 
Permite: 
• Visualizar un listado de los encabezados de la página y su 
nivel. 
• Mostrar los anidamientos entre encabezados. 
• Alertar de los casos en que no hay encabezados o se 
produce un salto incorrecto entre ellos. 
• Resaltar el encabezado seleccionado para así poder 
localizarlo más fácilmente en la página. 
 

<!-- Page 13 -->

 
 
Aplicaciones y desarrollo web 
13 
Niveles del DOM 
A medida que han ido evolucionando los navegadores con sus nuevas versiones, también el soporte que 
daban a las especificaciones del DOM ha ido aumentando, y a esta aplicación en mayor o menor medida 
las características del DOM se le ha llamado "Niveles del DOM". 
El primer nivel, fue el DOM nivel 0, cuando Netscape 2.0 comenzó a disponibilizar por medio de objetos 
los componentes de la página. 
Actualmente, la última especificación publicada es DOM nivel 4, desde 2014. 
 
 
 
 
+ Info 
Puedes consultar información sobre DOM en el organismo W3C: 
https://www.w3.org/TR/2011/WD-dom-20110915/ 
Puedes consultar la última actualización de 31 de marzo de 2023 en: 
https://dom.spec.whatwg.org/ 
 
1.3.1. Shadow DOM 
Los Shadow DOM son cápsulas independientes de código dentro de un DOM convencional, pero con su 
propio rango de validez, son definidos y creados por los programadores y gestionados y renderizados 
por los navegadores por los navegadores (igual que los DOM), pero en este caso solo se aplican a los 
componentes de proyecto que se indiquen en ese código, aislándolos de cualquier indicación de diseño 
o de estructura que se aplique a todo el proyecto. 
Al igual que DOM, es una interfaz para acceder a datos. 
Shadow DOM es una subvariedad del DOM y es uno de los cuatro pilares fundamentales de los 
componentes web estandarizados por el consorcio W3C en 2012. 
Por tanto, tenemos el DOM con la estructura de todo el proyecto, y el Shadow DOM, que puede 
generar un número indefinido de Shadow Trees (árboles de sombra), cada uno de ellos tiene su propia 
raíz llamada Shadow Root (raíz de sombra) que cuenta con sus propios elementos y también con su 
propio estilo, no recibe influencias externas ni tampoco afecta a los contenidos externos. Con este uso 
tenemos que los Trees siempre se asignan a un elemento determinado (al que se le llama Shadow Host) 
del árbol de documento de orden superior o a otro Shadow Tree. 

<!-- Page 14 -->

 
 
Aplicaciones y desarrollo web 
14 
La transición entre DOM normal y DOM oculto se denomina Shadow Boundary (en español, "frontera 
de sombra"). 
Para utilizar la interfaz Shadow DOM no es necesario instalar ningún software adicional, se puede hacer 
mediante el documento HTML de la aplicación web, puesto que únicamente se trata de crear un 
subárbol en el código fuente. La renderización (transformación en una representación visual) del 
navegador se realiza automáticamente junto con el DOM completo de orden superior. 
 
 
 
 
Virtual DOM 
Es una representación del DOM en memoria que se crea cada vez 
que se produce un cambio en el DOM, para poder compararlos y 
así determinar los cambios que se deben hacer en el DOM real. 
React y otras bibliotecas lo utilizan para hacer el mínimo número 
de cambios en el DOM real. 
 
1.4. Etiqueta 
Una etiqueta (término a veces reemplazado por el anglicismo tag) es una marca con nombre que 
delimita una región en los lenguajes basados en XML. 
Con la llegada de la World Wide Web ha habido una invasión de tags. 
La Web se basa en el HTML, o «lenguaje de marcado de hipertexto», que está basado en el uso de \netiquetas. 
Las etiquetas (entre otras muchas cosas) le dicen al programa visualizador de páginas web (o 
navegador): 
• En qué juego de caracteres está la página. 
• De qué tipo es cada uno de los fragmentos de texto que contiene (por ejemplo, \nencabezamiento, texto normal, etc.). 
• Si están alineados a un lado o centrados, en qué tipo de letra está el texto (cursiva, negrita, \netc.), si hay tablas, de qué anchura son etc. 

<!-- Page 15 -->

 
 
Aplicaciones y desarrollo web 
15 
1.5. Hojas de estilo 
En inglés: CSS, Cascading Style Sheets. 
Traducido es Hojas de Estilo en Cascada. 
En el inicio del HTML, el código contenía la información y la forma de representarla, es decir: 
• El contenido. 
• El diseño y formato. 
Lo normal, actualmente, es hacer el desarrollo de forma separada. 
La página web sólo debe contener información, y el formato se define en las hojas de estilo (El 
funcionamiento de las hojas de estilo es el siguiente: 
• En la página web, que es el archivo .html: 
Se escriben las etiquetas que definen categorías o elementos, y qué hoja de estilo deseamos 
usar. 
• En la hoja de estilo, que es un archivo .css: 
Se indica cómo queremos que sea el formato de presentación (fuente, tamaño, color, márgenes, 
bordes, posición, etc). 
 
 
 
 
Atención 
Estudiaremos CSS con mayor profundidad en el epígrafe de 
Desarrollo web. 
 
1.6. Estándar SGML 
SGML, siglas del inglés Standard Generalized Markup Language, es un estándar para definir lenguajes de 
marcado, marcar y describir documentos con independencia total del hardware y software utilizados. 
Fue definido por la norma ISO 8879 en 1986 y desde entonces ha sido considerado el lenguaje estándar 
para mantener los depósitos centrales de la estructura documental. 

<!-- Page 16 -->

 
 
Aplicaciones y desarrollo web 
16 
SGML es el conjunto de normas utilizadas por autores y editores para preparar escritos electrónicos, 
cuyo objetivo es crear un fichero electrónico que sea fácilmente transferible y procesable por 
muchos sistemas, ordenadores, plataformas y medios. 
 
 
 
+ Info 
En 1978 el Instituto Nacional Americano de Normalización (ANSI) \nempezó a trabajar en las especificaciones para los procesadores de 
textos y el resultado fue el lenguaje SGML que, en 1986, pasó a 
manos de la ISO y se convirtió en la norma 8879, SGML (Standart 
Generalized Markup Language). 
 
 
• ISO / IEC TR 9573 - Procesamiento de información - Servicios de apoyo para SGML - Técnicas 
para utilizar SGML (Parte 13: Entidad Pública establecida para las matemáticas y la ciencia). 
• En 2007, el grupo de trabajo del W3C MathML acordó asumir el mantenimiento de estos 
conjuntos de entidades. 
ISO lo define así: 
"Lenguaje independiente de la aplicación que provee una sintaxis coherente y sin ambigüedades, apta 
para describir documentos construidos de acuerdo con ODA (Office Document Architecture), o 
cualquier otro modelo de documento, que pueden ser creados y leídos tanto por seres humanos como 
máquinas". 
SGML utiliza códigos que indican la estructura del documento, de forma que sus diferentes elementos 
como título principal, títulos secundarios, notas de pie de página, etc. reciben una serie de 
codificaciones específicas, logrando que cada documento sea como un registro con sus respectivos 
campos. (Al contrario que en la forma tradicional de señalar textos, en la cual las instrucciones se dan 
directamente al tipógrafo). 
Así, con sólo un conjunto de códigos, tanto el texto como los gráficos, de un documento, puede ser 
utilizado para diversos productos en diferentes medios o soportes, lo que es un gran avance para los \neditores, en tiempo y costos de producción (no es necesario volver a teclear los escritos), el mismo 
original puede ser utilizado tanto para productos electrónicos como impresos en papel. 
El estándar "ISO 8879:1986 Tratamiento de la información - Sistemas de texto y de oficina - Lenguaje 
de marcado generalizado estándar (SGML)", tiene tres versiones: 
• Originalmente SGML, fue aceptado en octubre de 1986, seguido de una Rectificación Técnica 
menor. 

<!-- Page 17 -->

 
 
Aplicaciones y desarrollo web 
17 
• SGML (ENR), en 1996, fue el resultado de una Rectificación Técnica para añadir reglas de 
nomenclatura extendidos (extended naming rules) que permiten lenguajes arbitrarios y 
marcados de script. 
• SGML (ENR + WWW o WebSGML), en 1998, fue el resultado de una Corrección de errores 
técnicos para satisfacer mejor los requerimientos de XML y la WWW. 
SGML es parte de un trío de normas ISO para documentos electrónicos desarrollados por ISO/IEC JTC 
1/SC 34 (ISO/IEC se une al Comité Técnico 1, Subcomité 34 - Descripción del documento y los 
lenguajes de procesamiento): 
• SGML (ISO 8879) - Lenguaje de Marcado Generalizado. 
SGML se extiende a XML, siglas en inglés de eXtensible Markup Language, traducido como 
'Lenguaje de Marcado Extensible' o 'Lenguaje de Marcas Extensible', es un metalenguaje que 
permite definir lenguajes de marcas desarrollado por el World Wide Web Consortium (W3C) 
utilizado para almacenar datos en forma legible. 
XML proviene entonces del lenguaje SGML, y permite definir la gramática de lenguajes \nespecíficos para estructurar documentos grandes, y diferenciándose de otros lenguajes, XML da 
soporte a bases de datos, lo que resulta de gran utilidad cuando varias aplicaciones deben 
comunicarse entre sí o integrar información. 
• DSSSL (ISO / IEC 10179) - (Document Style Semantics and Specification Language) es un 
lenguaje para describir estilos en documentos basado en el Scheme (lenguaje de programación 
funcional y un dialecto de Lisp). 
DSSSL se utiliza junto con jade/openjade para transformar documentos DocBook SGML/XML \nen archivos pdf o html. Actualmente los documentos sgml/xml se pueden transformar a otros 
formatos como ps, rtf, doc, etc. 
DSSSL fue trabajado dentro de W3C XSLT y XSL-FO que utilizan una sintaxis XML. Hoy en día, 
DSSSL se utiliza muy poco en nuevos proyectos, aparte de la documentación de Linux. 
• HyTime, norma internacional publicada por la ISO y la IEC. La primera edición se publicó en 
1992, y la segunda edición se publicó en 1997. 
HyTime (Hypermedia/Time-based Structuring Languagem), es un lenguaje de marcado, es una 
aplicación de SGML, y define un conjunto de tipos de elementos orientados al hipertexto que, 
complementan SGML y permiten a los autores de documentos SGML crear presentaciones de 
hipertexto y multimedia de una manera estandarizada, se utiliza muy poco. 
HyTime fue trabajado parcialmente dentro de W3C XLink. 
 

<!-- Page 18 -->

 
 
Aplicaciones y desarrollo web 
18 
 
 
 
+ Info 
SGML es apoyado entre otros por: 
• ISO / IEC TR 9573 - Procesamiento de información - 
Servicios de apoyo para SGML - Técnicas para utilizar 
SGML (Parte 13: Entidad Pública establecida para las 
matemáticas y la ciencia). 
• En 2007, el grupo de trabajo del W3C MathML acordó 
asumir el mantenimiento de estos conjuntos de entidades. 
 
La historia de SGML 
SGML proviene del lenguaje de marcado generalizado de IBM (GML, Generalized Markup Language), El 
cual Charles Goldfarb, Edward Mosher, y Raymond Lorie desarrollaron en la década de 1960. 
Goldfarb, director de la norma internacional, acuñó el término "GML" usando las iniciales de su apellido. 
Goldfarb también escribió la obra definitiva sobre la sintaxis de SGML en "El manual de SGML". 
SGML se diseñó originalmente para permitir el intercambio de grandes documentos en el gobierno, 
leyes, e industrias, ya que esos documentos debían permanecer intactos durante un largo periodo de 
tiempo, por ello también fue aplicado ampliamente por militares, y la industria aeroespacial, para 
referencias técnicas, y por la industria editorial. 
Con su derivación a XML se ha logrado que sea adecuado para la aplicación generalizada de pequeña \nescala, y el uso de propósito general. 
Los lenguajes de marcas no son lenguajes de programación, en ocasiones su definición como 
"lenguajes" puede inducir a esa confusión. 
Los lenguajes de marcas son sistemas complejos de descripción de información, normalmente 
documentos que, si se ajustan a SGML, se pueden controlar desde cualquier editor ASCII. Las marcas 
más usadas se suelen representar por textos descriptivos encerrados entre los signos de "menor" (<) y 
"mayor" (>), y normalmente se indica una marca de principio y otra de final. 
Hay que distinguir entre un lenguaje de marcas o de etiquetado y un lenguaje de marcas generalizado, 
ya que no es lo mismo: 
• Con un lenguaje de marcas también denominados lenguajes de marcado o lenguajes de 
descripción de documentos, se describen las reglas para el procesamiento de un texto. 
Se describen los diferentes caracteres y sus características de impresión. 

<!-- Page 19 -->

 
 
Aplicaciones y desarrollo web 
19 
• Un lenguaje de marcas generalizado no especifica cómo deben verse las cosas o el proceso que 
se ha de realizar. 
Solo provee de información sobre la estructura del documento, identifica las partes lógicas y el 
tipo de elementos que constituyen el documento. 
El lenguaje SGML: 
• Utiliza un conjunto de caracteres que se basan en el estándar ASCII (American Standard Coding 
for the Interchange of Information), que puede ser reconocido por cualquier tipo de plataforma 
y de sistema informático. 
• Los caracteres especiales, que no están contemplados en el conjunto de caracteres ASCII se 
transforman en representaciones ASCII y se denominan referencias de entidad. 
• Subordina el etiquetado a los aspectos lógicos de la estructura de los documentos. 
Se basa en el criterio de que existe una relación directa entre cuestiones como el cambio de 
tipografía y una cabecera, la utilización de la cursiva para resaltar un término, el dibujo de un 
recuadro con un gráfico, etc. 
• Todo el etiquetado es lógico. 
Se utilizan "nombres de elementos" en vez de caracteres aleatorios, delimitados por marcas que 
indican el comienzo y final de los objetos lógicos. 
Estos delimitadores permiten que el software reconozca qué caracteres deben ser leídos en 
modo de "etiqueta" o "marca", y qué otros como "contenido". 
Características de SGML: 
• Es un lenguaje muy potente y flexible que permite que se definan lenguajes de marcas de forma 
independiente. 
• Facilita el intercambio y conservación de documentos y recursos digitales estructurados. 
• Debe utilizarse cuando: 
• Exista la necesidad de intercambiar documentos entre diferentes sistemas de computación 
o de edición. 
• Los documentos tengan una larga vida de uso. 
• Sea fundamental la estructura de un documento. 
• SGML no es un lenguaje de marcas en sí mismo. 
Es un metalenguaje o marco general para la descripción de lenguajes de marcado, en particular 
para aquellos usados en el intercambio electrónico, manejo y publicación de documentos. 
La complejidad de SGML, hace que no sea adecuado para la web, surgiendo HTML, que es un 
lenguaje definido en SGML, más simplificado. 

<!-- Page 20 -->

 
 
Aplicaciones y desarrollo web 
20 
HTML es una DTD (es una DTD (descripción del tipo de documento) de SGML que 
originalmente, en versiones anteriores a HTML2, no era completamente compatible con SGML, 
por tener algunas deficiencias sintácticas por su mayor simplicidad. 
• SGML ofrece un enfoque lógico en el tratamiento de la información basado en la estructura, los 
objetos y los atributos. 
El estándar SGML, ha dado origen a HTML, y ha servido de punto de partida para otros muchos 
subconjuntos de lenguajes como el Extensible Markup Language (XML), publicado como una 
Recomendación del W3C en 1998. 
1.6.1. Un documento en SGML 
Un documento se puede constituir por tantos diferentes archivos, como sean necesarios, cada uno de \nellos contendrá una información diferente, como, por ejemplo: la portada, la introducción, una parte de 
una hoja de cálculo, un gráfico, un organigrama, bibliografía, etc. 
Estos archivos pueden estar además almacenados en un sistema distribuido, es decir en varios 
ordenadores, y cada uno de los ordenadores recibe el nombre de entidad y: 
• Son concebidos como objetos independientes. 
• Pueden tener cualquier tamaño. 
• Pueden haber sido creadas por cualquier programa de software. 
• Pueden ser compartidas por distintos documentos. 
Un documento estará definido en función de la estructura de las entidades que lo conforman. 
En el índice de materias de un documento no se encontrará ninguna referencia a los archivos que 
contienen las entidades. 
Las entidades se organizan en una estructura lógica de manera jerarquizada, en la que se definen 
conceptos como capítulos, tablas y párrafos y que configuran lo que se denomina estructura de los \nelementos del documento. 
Elementos y entidades pueden coincidir: un elemento lógico como tabla puede ser también una entidad \nen un archivo hoja de cálculo. 
Un documento SGML se marca de tal modo que no dice nada respecto a su representación en la 
pantalla o en papel. Un programa de presentación (filtro) debe unir el documento marcado con un \nesquema de estilo, a fin de producir una representación impresa en la pantalla o en papel del contenido 
del documento. Con SGML se pueden definir varias características que dependan de las necesidades de 
cada documento: 
SGML es un estándar internacionalmente aceptado que soporta diferentes tipos de contenido, así como 
la estructuración lógica del documento. Como su propio nombre indica, constituye un lenguaje y una 
notación para la descripción de tipos de documentos. Un documento codificado según este estándar se \nestructura en una serie de elementos (párrafos, subsecciones, apéndices, figuras, etc.) delimitados con 
"strings" o cadenas de caracteres comúnmente llamados "tags" o marcas. 
 

<!-- Page 21 -->

 
 
Aplicaciones y desarrollo web 
21 
 
 
 
Resumiendo 
SGML es un estándar internacional, no propietario y abierto. 
Proporciona un método para la descripción de la estructura de 
documentos basándose en la relación lógica de sus partes. 
Indica una codificación estándar para la transmisión de 
documentos entre sistemas de computación diferentes 
independientemente de su grado de complejidad, como diferentes 
plataformas, soportes físicos y lógicos, sistemas de 
almacenamiento y presentación. 
 
1.6.2. Partes de un documento SGML 
Un documento SGML se compone de tres partes o archivos: 
• Declaración SGML. 
• Declaración de tipo de documento (DTD). 
• Instancia de Documento. 
1.6.2.1. La declaración SGML 
La declaración SGML se puede omitir, asumiendo entonces unos grupos de caracteres por defecto y 
ninguna característica opcional. 
La declaración SGML caracteriza la DTD y, por tanto, las instancias de documento (que incluyen el 
contenido propiamente dicho) que se generen a partir de ella, en cuanto a conjunto de caracteres 
usados y otras opciones de SGML. 
La declaración SGML: 
• Es un diagrama formal y normalizado que le indica al sistema receptor el conjunto de caracteres, 
los delimitadores y las características opcionales de SGML que se están utilizando. 
• Puede ser parte de la Muestra de Documento. 

<!-- Page 22 -->

 
 
Aplicaciones y desarrollo web 
22 
• Es necesaria para cada documento SGML que se transmite y también puede utilizarse desde 
cualquier ubicación considerada no local. 
A través de ella se identifican de manera inmediata los parámetros para la marca generalizada 
contenida en la DTD. 
Se puede omitir, y suele omitirse, cuando tanto el sistema emisor como el receptor utilizan la 
sintaxis por defecto o una sintaxis de referencia concreta. 
• La declaración SGML indica al usuario: 
• Qué puede y qué no puede estar contenido en el documento SGML. 
• Qué caracteres serán usados. 
• Qué características específicas de SGML serán implementadas. 
• Qué sintaxis se utilizará en el documento. 
La declaración SGML y la DTD deben trabajar de forma conjuntan, es decir, si la declaración SGML dice 
que una función en particular no podrá ser usada, la DTD debe respetarlo, de lo contrario existirán \nerrores en el documento. 
1.6.2.2. La DTD 
En la DTD (Document Type Definition o Definición del Tipo de Documento) se especifica la estructura 
del documento. 
Se indican aquellos elementos que son necesarios en la elaboración de un documento o un grupo de 
documentos estructurados de manera similar. 
Contiene las reglas de dichos elementos: el nombre, su significado, dónde pueden ser utilizados y qué 
pueden contener. 
 
 
 
 
+ Info 
Una clase de documentos tiene en común: 
• Una gramática que define el marcado permitido en esa 
clase. 
• El marcado requerido. 
• Y cómo debe ser utilizado dicho marcado en la instancia de 
documento. 
El estándar define esta gramática mediante la DTD. 
 

<!-- Page 23 -->

 
 
Aplicaciones y desarrollo web 
23 
La DTD es necesaria ya que: 
• El conjunto particular de elementos que pueden utilizarse no se especifica en SGML, se definen \nen la DTD. 
• También existe la posibilidad de hacer referencia a una DTD pública, mezclar definiciones 
originales con la DTD pública o generar una DTD original. 
Si la DTD se almacena en un archivo separado (con la extensión .dtd), éste se puede referenciar sin 
residir dentro del documento SGML, porque es corriente que se sustituya la DTD completa por una 
línea que indique que la DTD se edita como un texto público o se encuentra ya disponible en el sistema 
receptor. 
Sin la DTD (o una referencia a él), el documento SGML no será validado apropiadamente por el "parser" 
El parser es una herramienta que asegura la adecuada conformación de SGML dentro de las múltiples \nespecificaciones que un documento SGML puede tener. Un documento no será validado por el parser si 
no cumple con las especificaciones de la DTD, por ejemplo, si carece de título, ya que éste es un \nelemento obligatorio. 
Las denominadas formalmente "declaraciones de elementos", que son las definiciones de los elementos, 
tienen 2 funciones: 
• Dar un nombre formal a las etiquetas. 
• Describir lo que cada elemento puede contener -el denominado "modelo de contenido"-. El 
nombre formal aparecerá dentro de los delimitadores, por ejemplo: <capitulo> que será el 
nombre formal con el que nos refiramos a un capítulo. 
Ejemplo de definición de la DTD, donde puede verse claramente que existe una estructura organizada y 
jerárquica: 
<!ELEMENT DOCUMENTO - - (titulo, contenido, autor?) > 
     <!ELEMENT CONTENIDO - - (capitulo+) > 
     <!ELEMENT CAPITULO - (subtitulo, parrafo?) 
En el ejemplo: 
• Lo que está situado dentro de los paréntesis especifica qué puede o debe contener el elemento 
y es llamado el contenido del modelo. 
• Es obligatorio que haya un título y un contenido, pero es opcional que tenga autor. 
• Dentro de CONTENIDO puede haber uno o más capítulos, que a su vez también es otro \nelemento que contiene subtítulo y párrafos. 

<!-- Page 24 -->

 
 
Aplicaciones y desarrollo web 
24 
En la definición del tipo de documento o DTD (Document Type Definition) se utilizan los comandos: 
• ELEMENT. 
El comando ELEMENT sirve, a su vez, para definir una etiqueta. 
• ENTITY. 
Con el comando ENTITY se pueden indicar ciertos elementos del texto en forma de sucesiones 
de caracteres ASCII y también utilizar dentro del texto los caracteres reservados para la sintaxis 
de SGML, como los signos 'menor que' o 'mayor que'. 
• ATTLIST. 
El comando ATTLIST permite establecer atributos complementarios para determinados \nelementos concretos. 
Todos los atributos pertenecientes a un elemento se resumen aquí en una sola lista en la que se \nestablecen los nombres de los atributos, así como los valores autorizados de cada atributo. 
Otros comandos importantes son: 
• USEMAP y SHORTREF. 
Sirven para establecer abreviaturas. 
• NOTATION. 
Para fijar anotaciones en la llamada hoja de estilo. 
• DOCTYPE. 
Para incluir un DTD o para llamar a un archivo con la extensión .dtd que lo contiene. 
Para escribir la DTD hay que analizar los documentos y tener en cuenta los posibles cambios y 
necesidades futuras como las revisiones, borrado de los documentos etc. 
Hay que recordar que las etiquetas definidas en la DTD servirán para que editores, motores de 
búsqueda y visualizadores interpreten los documentos SGML. 
Puesto que los documentos no tienen una estructura generalizada, es decir, cada texto tiene una \nestructura diferente hay que analizar y definir bien la estructura de los documentos para poder 
jerarquizar y seccionar adecuadamente las partes que contendrá la DTD (por ejemplo, la estructura de 
un texto en prosa tiene una estructura muy diferente a la de un poema o a la de un artículo científico e, 
incluso, existen variaciones entre los documentos del mismo tipo, por tanto). 
El documento debe contener, por tanto, un subconjunto de la declaración del tipo de documento o 
conjunto formal de declaraciones de elementos, atributos y entidades que le indican a un sistema \nexactamente el tipo de etiquetado que se utiliza en dicho documento. 

<!-- Page 25 -->

 
 
Aplicaciones y desarrollo web 
25 
Secciones marcadas 
Es un concepto importante dentro del SGML y del DTD, una sección marcada se inicia con la secuencia 
de caracteres "". 
Las claves para la especificación de las secciones marcadas son principalmente: 
• INCLUDE. 
• IGNORE. 
• CDATA. 
• RCDATA. 
• TEMP. 
1.6.2.3. Instancia de Documento 
La instancia de documento lleva el contenido estructurado según el marco definido en la DTD y con las 
características fijadas por la declaración SGML. 
Pero, SGML no permite incorporar información de apariencia (layout) del documento, y para cubrir \nesta carencia se ha desarrollado otro estándar, el Document Style and Semantics Specification 
Language (DSSSL). 
La Muestra o instancia de Documento contiene el documento en sí que incluye tanto el texto como el 
marcado. 
El contenido del documento tiene objetos SGML que siguen la estructura del árbol definido en la DTD. 
Los objetos SGML son principalmente dos: 
• Elementos (insertados como etiquetas y sus atributos locales). 
• Entidades (para caracteres especiales, texto almacenado y archivos externos). 
Ejemplo del marcado de un texto: 
<titulo>HIPERTEXTO</titulo> 
<autor>curso</autor> 
<contenido> 
     <capitulo> 
          <subtitulo>aprendiendo SGML</subtitulo> 
          <parrafo> conceptos principales.</parrafo> 
     </capitulo> 
</contenido> 

<!-- Page 26 -->

 
 
Aplicaciones y desarrollo web 
26 
Análisis del ejemplo: 
• Las etiquetas se distinguen del resto del texto porque están delimitadas por los caracteres < > 
para abrir y por </ > para cerrar. 
Se divide un documento en partes y no se dice cómo debe diseñarse cada una de esas partes. 
Para este efecto debe hacerse un filtro, u hoja de estilo, un programa que traducirá las etiquetas 
SGML en cualquiera de las aplicaciones con las cuales es compatible. 
• Los delimitadores o etiquetas de inicio y final permiten que el software reconozca qué 
caracteres deben leerse en modo etiqueta y cuáles en modo contenido. 
• Los caracteres básicos utilizados en el lenguaje SGML vienen descritos en la ISO 8879. Además, 
de los caracteres < > con el nombre de un elemento en su interior), si encontramos el signo & 
seguido por un nombre, y éste a su vez seguido de un punto y coma, sabremos que se están 
representando entidades tales como imágenes gráficas o caracteres especiales. 
SGML ha logrado simplificar estos 3 pasos para construir un documento SGML sin la intervención del 
usuario, pues, en este sistema, cada componente establece los valores y parámetros para el siguiente 
componente. 
El único etiquetado que aparece ha sido declarado en la DTD y la sintaxis de la DTD se ha indicado 
mediante la declaración SGML definida por el estándar. 
Esta secuenciación de indicaciones permite que los ordenadores pueden seguirla para comprobar si los 
documentos se adaptan a las reglas establecidas. 
SGML, es un lenguaje informático muy preciso ya que un programa llamado parser puede leer la 
declaración SGML y aprender sus reglas. A continuación, lee la DTD y aprende las reglas del marcado y \netiquetado y, finalmente, determina si la muestra de documento cumple dichas reglas. 
Por tanto, el procesamiento de un documento SGML se realiza de forma automática, es la máquina 
quien valida el documento, puesto que el parser lee el documento SGML y separa los datos del \netiquetado. Por ejemplo: 
• Si el parser detecta que el etiquetado ha sido minimizado, lo expande. 
• Si el contenido incluye una referencia a una hoja de cálculo o a un gráfico, dará las instrucciones 
al sistema para encontrar dichas entidades y que aparezca la imagen de dicho gráfico. 
• Si el contenido incluye alguna instrucción especial para el sistema de edición en su propio 
lenguaje interno (llamada en SGML instrucción de procesamiento), ésta pasará directamente a 
la aplicación. 
• Si se utiliza el componente de sección marcada y se ha indicado que algunas partes de su 
documento no han de aparecer en la versión editada, el parser sabrá que no tiene que enviarlas, 
al igual que si se utiliza el componente de declaración de comentarios para enviar y recibir una 
nota o un mensaje entre autor y editor, el "parser" sabrá que no ha de enviarlo a la aplicación 
receptora. 

<!-- Page 27 -->

 
 
Aplicaciones y desarrollo web 
27 
1.7. Script 
En informática, un script, secuencia de comandos o guion (traduciendo desde inglés) es un término 
informal que se usa para designar a un programa relativamente simple. 
Los administradores de sistemas utilizan scripts para automatizar la realización de tareas pesadas, de 
forma que no es necesario repetirlas, como la creación de cuentas de usuario. 
Los scripts regularmente no se compilan con anticipación a código máquina, sino que son ejecutados 
por un intérprete que lee el archivo de código fuente al momento; o incluso por una consola interactiva 
donde el usuario suministra el programa al intérprete paso a paso. 
Los scripts o guiones se pueden usar para prototipar programas, automatizar tareas repetitivas, hacer 
procesamiento por lotes e interactuar con el sistema operativo y el usuario (debido a esto, los 
intérpretes de comandos o shells suelen diseñarse con funcionalidades de programación). 
Algunos lenguajes de programación son considerados "lenguajes de scripts" (scripting languages) sí son 
idóneos para realizar guiones con soltura, aunque también se utilizan para codificar programas mucho 
más complejos. 
Los lenguajes de script se utilizan para dar instrucciones a otros softwares, como servidores, 
navegadores o aplicaciones independientes. Puesto que facilitan y agilizan la codificación, son cada vez 
más empleados para diseñar webs y aplicaciones, y programar videojuegos, etc. 
Algunos de los lenguajes de Sript más destacados son: 
• JavaScript. 
• PHP. 
Acrónimo recursivo en inglés de PHP: Hypertext Preprocessor. 
Es un lenguaje de programación de uso general de script del lado del servidor, que permite el 
desarrollo web de contenido dinámico. 
• PYTHON. 
• RUBY. 
• GROOVY. 
• PERL. 
• BASH. 
 

<!-- Page 28 -->

 
 
Aplicaciones y desarrollo web 
28 
 
 
 
Ejemplo 
Por ejemplo, aunque Python es un lenguaje de guiones popular, 
programas escritos enteramente en Python como Deluge o 
bibliotecas como SciPy no son más que simples guiones. 
 
Terminología 
El término inglés script se tomó del guion escrito de las artes escénicas, el cual es interpretado por una 
serie de actores/actrices (o, en este caso, programas) siguiendo un orden establecido. 
En algunos textos se traduce script como «guion», traducción que es bastante frecuente en el ámbito 
de algunas comunidades y publicaciones sobre software libre (como el equipo de traducción de KDE, 
que traduce en la mayoría de las aplicaciones para este escritorio, script como «guion»), o diversas 
guías y manuales de software. Su uso se une al de las expresiones «secuencia de comandos» y «archivo 
de órdenes», empleada esta última en América, es la castellanización más difundida. 
Ventajas frente a los lenguajes de programación 
Un script es un simple fichero de texto ASCII (American Standard Code for Information Interchange) en \nel cual se suceden todas las instrucciones que lo componen, de manera similar a cualquier código 
fuente. 
La diferencia entre un lenguaje de script y un lenguaje de programación propiamente dicho es que un 
script no se compila, es decir que no se transforma en un archivo binario que puede ejecutar 
directamente la máquina, sino que hace falta obligatoriamente un intérprete de comandos llamado 
«anfitrión de script» o «shell» para ejecutarlo. 
Usando un script se necesitan pocas instrucciones para llegar a realizar una operación. La sintaxis está 
simplificada y la programación es menos restrictiva (no hace falta declarar las variables, existen pocos 
tipos de datos, etc.). 
El uso de los scripts permite: 
• Simplificación de trabajo y ahorro de tiempo: 
Permiten realizar tareas complejas y ser ejecutados automáticamente por el sistema, sin 
intervención humana. 
Gracias a su simplicidad, las tareas de administración se realizan más rápidamente, siendo muy 
útiles para los administradores que ahorran mucho tiempo y esfuerzo con el uso de los mismos. 

<!-- Page 29 -->

 
 
Aplicaciones y desarrollo web 
29 
• Reutilización Limitar los errores: 
Un script solo necesita escribirse una vez y puede utilizarse un número indefinido de veces. 
• Eliminación de errores: 
Una vez que se realiza un script y se prueba, el resto de veces en que se reutilice, garantiza estar 
libre de errores. 
• Aumento de flexibilidad: 
Con pequeñas modificaciones de lógica en el programa, los scripts pueden adaptarse a muchas 
situaciones. 
• El código fuente de un script siempre es accesible. 
Ámbitos de uso 
Vamos a ver el uso en UNIX, WINDOWS y en Diseño web: 
• En UNIX. 
Los archivos guion suelen ser identificados por el sistema a través de uno de los siguientes \nencabezamientos en el contenido del archivo, conocido como "shebang": 
#!/bin/bash ; #!/bin/ksh ; #!/bin/csh 
Aunque en entornos UNIX la mayoría de los guiones son identificados por dicho \nencabezamiento, también pueden ser identificados a través de la extensión ".sh", siendo esta 
quizá menos importante que el encabezamiento, ya que casi todos los sistemas no necesitan 
dicha extensión para ejecutar el guion, por lo tanto, esta suele ser añadida por tradición, o más 
bien, es útil para que el usuario pueda identificar estos archivos a través de una interfaz de línea 
de comandos sin necesidad de abrirlo. 
Difieren de los programas de aplicación, debido a que los últimos son más complejos; además, 
los guiones son más bien, un programa que le da instrucciones a otros más avanzados. 
• En Windows y DOS. 
En el sistema operativo DOS, a los scripts creados para ser interpretados por cmd.exe o el 
obsoleto COMMAND.COM se les conoce como archivos «batch» (procesamiento por lotes) y 
acaban en .bat p .cmd 
En el sistema operativo Windows, existen varios lenguajes interpretados como Visual Basic 
Script (VBScript), JScript, Batch, y PowerShell. 

<!-- Page 30 -->

 
 
Aplicaciones y desarrollo web 
30 
• En diseño web. 
Los scripts en Internet se pueden clasificar en guiones del lado del cliente y del lado del servidor. 
• Scripts del lado del cliente. 
Los guiones del lado del cliente se deben incluir con la etiqueta <script>, incluyendo el 
atributo type con el tipo MIME. 
Generalmente se usa JavaScript, pero se puede usar VBScript (solo Internet Explorer o 
Google Chrome). Tiene como objetivo, por lo general, AJAX o manipulación del DOM. 
• Scripts del lado del servidor. 
No tienen los problemas de accesibilidad que pueden presentar los guiones del lado del 
cliente. También permiten modificar las cabeceras HTTP, u obtenerlas. Además, permiten 
acceso a bases de datos y otros archivos internos. 
1.8. Shell 
En informática, el shell o intérprete de órdenes o intérprete de comandos es el programa informático 
que provee una interfaz de usuario para acceder a los servicios del sistema operativo. 
Dependiendo del tipo de interfaz que empleen, los shells pueden ser: 
• De líneas texto. 
(CLI, Command-Line Interface, interfaz de línea de comandos). 
• Gráficos. 
(GUI, Graphical User Interface, interfaz gráfica de usuario) 
• De lenguaje natural. 
(NUI, Natural User Interface, interfaz natural de usuario). 
Los shell son necesarios para invocar o ejecutar los distintos programas disponibles en el ordenador, (un \nejemplo de Shell en Windows es Power Shell). 
1.9. Renderizado web 
El renderizado web es el proceso mediante el cual los navegadores transforman el contenido \nestructurado de una página web, como HTML, CSS y otros recursos, en una representación visual 
interactiva que el usuario puede ver e interactuar. Este proceso ha evolucionado significativamente a lo 
largo de los años, adaptándose a las necesidades crecientes de las aplicaciones web y a la mejora de la \nexperiencia de usuario. 

<!-- Page 31 -->

 
 
Aplicaciones y desarrollo web 
31 
1.9.1. Primeros días del renderizado 
En los primeros días de la web, el renderizado era un proceso bastante sencillo. Los navegadores de la 
época, como Mosaic y Netscape, tomaban los documentos HTML enviados por el servidor y los 
mostraban tal cual, sin mucha interactividad. En este contexto, el navegador simplemente "mostraba" 
la página, sin que hubiera una gran diferenciación entre el servidor y el cliente. Este enfoque era \nestático, y todas las interacciones del usuario significaban una nueva solicitud al servidor, lo que 
provocaba tiempos de carga elevados y una experiencia web limitada. 
1.9.2. La llegada de JavaScript: CSR y las SPA 
La introducción de JavaScript a finales de los años 90 cambió la manera en que las páginas web podían 
interactuar con los usuarios. En sus primeros años, JavaScript se utilizaba principalmente para añadir 
interactividad en el cliente, como formularios dinámicos o la validación de entradas. Sin embargo, no 
fue hasta principios de los 2000 que JavaScript pasó a desempeñar un papel clave en la creación de 
aplicaciones web más dinámicas. 
Una de las primeras tecnologías que permitió a JavaScript revolucionar la web fue AJAX (Asynchronous 
JavaScript and XML). Esta técnica permitió que el navegador realizara solicitudes HTTP al servidor en 
segundo plano, sin tener que recargar toda la página. Aunque originalmente estaba diseñado para \nenviar y recibir datos en formato XML, AJAX permitió a los desarrolladores cargar solo partes del 
contenido, mejorando significativamente la experiencia de usuario. 
A medida que AJAX se fue adoptando, comenzó a surgir un nuevo enfoque para las aplicaciones web: las 
Single Page Applications (SPA). En lugar de recargar toda la página con cada interacción del usuario, las 
SPA cargan la aplicación en una sola página HTML y luego actualizan dinámicamente el contenido 
cuando el usuario interactúa con la interfaz. JavaScript se convierte en el núcleo de este enfoque, ya que \nes responsable de manejar la lógica y actualizar el contenido en el cliente. 
En este contexto, Client-Side Rendering (CSR) emerge como una técnica esencial para SPA. En lugar de 
que el servidor envíe HTML pre-renderizado, todo el contenido se maneja y se renderiza directamente \nen el cliente, permitiendo una experiencia más fluida y rápida. 
A medida que el desarrollo web continuó evolucionando, el estándar de Fetch API reemplazó a AJAX 
como la opción más moderna para realizar solicitudes asíncronas. Fetch simplifica las peticiones HTTP y 
proporciona una sintaxis más limpia y moderna, convirtiéndose en una herramienta esencial para las SPA. 
Este enfoque de CSR, basado en JavaScript, permite que las SPA sean rápidas y eficientes, ya que se 
minimizan las interacciones con el servidor y solo se envían y reciben los datos necesarios para 
actualizar el contenido dinámico de la página. 
Sin embargo, como ventaja y desafío a la vez, las SPA también enfrentaron problemas con el SEO 
(optimización para motores de búsqueda). Dado que el contenido de la página se genera 
dinámicamente en el navegador mediante JavaScript, los motores de búsqueda tradicionales no podían 
indexar adecuadamente estas aplicaciones sin el uso de técnicas como la renderización del lado del 
servidor (SSR) o la prerenderización. 

<!-- Page 32 -->

 
 
Aplicaciones y desarrollo web 
32 
1.9.3. Emergen las soluciones híbridas: SSR y la hidratación 
Para abordar los problemas de SEO y rendimiento del CSR, surgió una nueva estrategia: Server-Side 
Rendering (SSR). Con SSR, el servidor procesa el contenido y envía una página ya renderizada al 
navegador, lo que mejora significativamente el tiempo de carga inicial y la visibilidad en motores de 
búsqueda. Sin embargo, la interactividad dinámica de las SPA seguía siendo necesaria, por lo que el 
concepto de hidratación apareció para combinar lo mejor de ambos mundos. En este proceso, el 
servidor envía la versión pre-renderizada de la página (HTML estático) y luego el JavaScript en el 
navegador se encarga de hacerla interactiva, añadiendo la funcionalidad que antes solo se lograba con 
renderizado en el cliente. 
Este enfoque híbrido es lo que ha permitido que herramientas como React, Next.js y Vue.js evolucionen 
y sigan siendo esenciales en el desarrollo de aplicaciones web modernas. Los desarrolladores ahora 
pueden construir aplicaciones rápidas y accesibles sin sacrificar la interactividad dinámica del cliente. 
1.9.4. El papel fundamental de los motores de renderizado 
En todo este proceso, los motores de renderizado son componentes esenciales. Son los encargados de 
interpretar el código HTML, CSS y otros recursos (como imágenes o archivos de fuentes) para crear la 
visualización final que el usuario verá en su navegador. Estos motores también gestionan la 
interactividad de la página, permitiendo que el usuario haga clic, se desplace o interactúe con otros \nelementos. 
El primer motor de renderizado ampliamente reconocido fue Gecko, desarrollado por Mozilla en 1998. 
A lo largo de los años, otros motores como WebKit y Blink han tomado protagonismo. WebKit, 
utilizado inicialmente por Safari y Opera, representó un paso hacia la optimización del rendimiento y la 
compatibilidad con nuevas tecnologías. En 2013, Google Chrome adoptó Blink, una bifurcación de 
WebKit, para mejorar aún más la velocidad de procesamiento y la compatibilidad con HTML5 y otros \nestándares modernos. Microsoft Edge, que originalmente usaba EdgeHTML, se unió a la tendencia en 
2020 al adoptar Blink, el motor de Chrome. 
Estos motores no solo se utilizan en navegadores, sino que también se aplican en otras aplicaciones que 
necesitan mostrar o editar contenido web, como clientes de correo electrónico o aplicaciones móviles. 
La mejora constante en los motores de renderizado ha sido clave para permitir una experiencia web 
más rica y dinámica. 
Dependiendo del conexto los motores de renderizado también pueden denominarse como motor de 
diseño, de representación, de browser o de navegación. 
1.9.5. Conclusión 
El renderizado web ha pasado de ser un proceso estático, basado en servidores, a uno altamente 
interactivo y dinámico gracias al auge de JavaScript y los motores de renderizado modernos. Con la \nevolución hacia enfoques híbridos como SSR y la hidratación, los navegadores y aplicaciones han 
mejorado tanto en rapidez como en interactividad, permitiendo crear experiencias web más ricas y \neficientes. Los motores de renderizado juegan un papel crucial en este proceso, ya que hacen posible 
que todo este flujo funcione correctamente, desde la carga inicial de la página hasta la interactividad 
completa del usuario. 

<!-- Page 33 -->

 
 
Aplicaciones y desarrollo web 
33 
1.10. Motor de renderizado 
Es un componente de software básico necesario en todos los principales navegadores web. 
Su función principal, es transformar los documentos HTML y otros recursos de una página web en una 
representación visual interactiva en el dispositivo del usuario (esta función se denomina renderización). 
El motor de renderizado, es software, que toma contenido marcado (como HTML, XML, archivos de 
imágenes, etc.) e información de formateo (como CSS, XSL, etc.) y luego muestra el contenido ya 
formateado en la pantalla de aplicaciones. 
Los motores de renderizado se usan típicamente en navegadores web, clientes de correo electrónico, u 
otras aplicaciones que deban mostrar y editar contenidos web. ("pinta" en el área de contenido de una 
ventana, la cual es mostrada en un monitor o una impresora). 
 
 
 
 
Anécdota 
El término "motor de renderizado", se hizo popular, cuando Mozilla 
diseñó el motor de su navegador, al que llamo "Gecko" como un 
componente aparte del propio navegador. 
Gecko era reutilizable por otros navegadores diferentes, y se \nempezó a referirse a él como un "motor de renderizado" en sí, en 
lugar de como una parte del navegador. 
 
 
Tras el lanzamiento del motor Gecko en 1998, apareció WebKit en 2002, que fue utilizado inicialmente 
por Safari y anteriormente por Opera. Posteriormente, Blink se desarrolló en 2013 como una 
bifurcación de WebKit para Google Chrome. Finalmente, EdgeHTML fue introducido en 2015 para 
Microsoft Edge, pero acabaría sustituido por Blink en 2020. 
Un motor de renderizado, es también conocido como: 
• Motor de diseño. 
• Motor de representación. 
• Motor de browser. 
• Motor de navegación. 

<!-- Page 34 -->

 
 
Aplicaciones y desarrollo web 
34 
2. Aplicaciones web 
 
En la ingeniería de software se denomina aplicación web a aquellas que los usuarios pueden utilizar 
accediendo a un servidor web a través de internet o de una intranet mediante un navegador. 
Es un programa que se codifica en un lenguaje interpretable por los navegadores web. Los navegadores 
realizan la ejecución del programa web. 
Unas de las ventajas más importantes son, lo práctico del navegador web como cliente, la 
independencia del sistema operativo, y la facilidad para actualizar y mantener aplicaciones web (sin 
tener que instalar el software a miles de usuarios). 
Una aplicación web es un tipo de aplicación basada en la arquitectura cliente/servidor. 
Una aplicación web podemos dividirla en 3 elementos: 
• Front-end: 
"El cliente de los servicios (normalmente un navegador)". 
El cliente web es el programa con el que interacciona el usuario para solicitar a un servidor web \nel envío de los recursos que desea obtener. 
• Back-end: 
"El servidor que los proporciona". 
El servidor web es un programa que está "a la escucha" (esperando solicitudes) de clientes web 
a través del protocolo HTTP. 
A estos programas se les suele llamar servicio o daemon (demonio). 
• Protocolo: 
"Sirve de comunicación entre cliente y servidor, (HTTP) están estandarizados y no hay que 
crearlos". 

<!-- Page 35 -->

 
 
Aplicaciones y desarrollo web 
35 
 
Esquema básico de una aplicación web 
Una página web, debe contener obligatoriamente código HTML. 
En las aplicaciones web, también podemos hacer una distinción en tres niveles (similares a los de la 
arquitectura cliente/servidor de tres niveles): 
• Nivel de presentación (o interfaz de usuario): 
Cliente web (normalmente es un navegador). 
Interacciona con el usuario para recibir solicitudes y presentar los resultados. 
Es la visualización por parte del usuario, (cliente web) de las páginas web que el usuario ha 
solicitado al servidor web. está compuesto por las páginas HTML que el usuario solicita a un 
servidor web y que visualiza en un cliente web. 
• Nivel de lógica de negocio: 
Está en el servidor. 
Procesa la solicitud enviada por el cliente web, solicita los datos al nivel de datos, formatea los 
datos recibidos de este y los envía al nivel de presentación. 
Es el intermediario entre los otros dos niveles. 
• Nivel de datos: 
Es la base de datos que, gestionada por un SGBD, son usados por la aplicación web. 
Puede estar en el servidor de la lógica de negocio o en otro servidor distinto. 

<!-- Page 36 -->

 
 
Aplicaciones y desarrollo web 
36 
2.1. Protocolo HTTP 
HTTP es el Protocolo de transferencia de hipertexto, es el protocolo de comunicación que permite las 
transferencias de información en la World Wide Web. 
HTTP fue desarrollado por el World Wide Web Consortium y la Internet Engineering Task Force, 
colaboración que culminó en 1999 con la publicación de una serie de RFC, siendo el más importante de \nellos el RFC 2616 que especifica la versión 1.1. HTTP define la sintaxis y la semántica que utilizan los \nelementos de software de la arquitectura web para comunicarse. 
 
 
 
 
Anécdota 
La versión inicial de HTTP, no tenía número de versión, era \nextremadamente sencillo: una petición consistía simplemente en 
una única línea, que comenzaba por el único método posible GET, 
seguido por la dirección del recurso a solicitar: 
• Protocolo, el servidor y el puerto se asumían 
implícitamente después de la conexión inicial al servidor. 
• GET /ejemplo.html 
Posteriormente se la denominó como 0.9 para distinguirla de las 
versiones siguientes. 
 
 
HTTP es un protocolo sin estado, es decir, no guarda ninguna información sobre conexiones anteriores. 
El desarrollo de aplicaciones web necesita frecuentemente mantener estado. Para esto se usan las 
cookies, que es información que un servidor puede almacenar en el sistema cliente. 
Esto permite a las aplicaciones web instituir la noción de sesión, y también permite rastrear usuarios ya 
que las cookies pueden guardarse en el cliente por tiempo indeterminado. 
Existen diferentes versiones de HTTP: 
• HTTP/0.9 – 1991. 
• HTTP/1.0 – 1996 (RFC 1945). 
• HTTP/1.1 – 1997 (RFC 2616). 
• HTTP/2.0 – 2015 (RFC 7540). 
• HTTP/3.0 – 2019. 
Se puede comprobar si un sitio web funciona con HTTP3 utilizando páginas web de chequeo. 

<!-- Page 37 -->

 
 
Aplicaciones y desarrollo web 
37 
 
 
 
+Info 
A continuación, te dejamos un ejemplo de una página de testeo de 
HTTP/3.0 
https://domsignal.com/http3-test 
 
 
Otra manera de saber con qué tecnología está funcionando un sitio web es usando un navegador web 
como Mozilla Firefox, desplegar el Inspector con la tecla F12, pulsar sobre «Red», «Cabeceras» y 
hallaremos la versión de HTTP que está usando si nos colocamos sobre el recurso pertinente, en el caso 
de la imagen siguiente vemos que en este sitio web la versión HTTP es la 1.1. 
 
Métodos HTTP 
Para realizar solicitudes a un servidor por medio del protocolo HTTP, necesitamos obligatoriamente 
utilizar unos métodos predefinidos en el protocolo. 
Estos métodos indican al servidor, cuál es la acción que deseamos realizar sobre uno o varios recursos. 

<!-- Page 38 -->

 
 
Aplicaciones y desarrollo web 
38 
A estos métodos también se les conoce por el nombre de "verbos". 
En la versión 1.0 de HTTP se definieron los 3 primeros métodos de este protocolo: 
• Método GET: 
Se utiliza es cuando se necesita adquirir un archivo o recurso que se encuentra en un servidor web. 
Este método devuelve las cabeceras que contienen los metadatos del recurso solicitado, y el 
recurso en sí. 
• Método HEAD: 
Realiza una acción similar al método GET, pero solo solicita los metadatos de un recurso o 
archivo y no todo elemento como tal. 
• Método POST: 
Se usa cuando se necesita enviar información o un elemento al servidor y que lo enviado sea 
almacenado como un "hijo" o subelemento de un elemento o recurso ya existentes en el 
servidor. 
No se utiliza para cargar/crear un elemento nuevo como tal. 
Este método se usa principalmente en el envío de formularios que se encuentran en las páginas 
web. 
A partir de la versión 1.1 de HTTP se agregaron otros 5 métodos nuevos adicionales: 
• Método OPTIONS: 
Sirve para averiguar qué métodos HTTP soporta el servidor web con respecto a un recurso en 
concreto o en caso de que haya un * en la URI se devuelven todos los métodos soportados por el 
servidor. 
• Método PUT: 
Crea/Carga un nuevo recurso al servidor, o en caso de que el objeto ya exista en el servidor 
reemplaza el recurso existente con el recurso que se carga. 
• Método DELETE: 
Le solicita al servidor web que se borre un recurso en específico. 
• Método TRACE: 
Permite monitorear los mensajes que hay entre el cliente y el servidor web. 
Principalmente se usa con propósitos de diagnósticos de fallas o para revisar si existen 
servidores intermediarios en la conexión. 

<!-- Page 39 -->

 
 
Aplicaciones y desarrollo web 
39 
• Método CONNECT: 
Se utiliza para solicitar una conexión de tipo túnel TCP/IP. 
Principalmente se utiliza cuando se necesita utilizar un proxy para una conexión segura cifrada 
HTTPS o para comunicaciones vía SSL. 
(Se estudiará en el Bloque IV). 
Cualquier cliente web puede hacer uso de estos métodos y que adicionalmente se puede configurar un 
servidor web para que reciba cualquier combinación de ellos. 
 
 
 
 
+ Info 
Han ido surgiendo nuevos métodos para determinadas 
necesidades del software: 
Ejemplos: 
• Los Métodos definidos en la extensión de HTTP llamada 
WebDAV (Web Distributed Authoring and Versioning) 
creada por un grupo de trabajo de la Internet Engineering 
Task Force (IETF) que tenía el mismo nombre. 
• El método PATCH, creado por la IETF, el cual sirve para 
aplicar modificaciones parciales a un recurso. 
 
 
Los métodos HTTP más usados en la actualidad y que conforman la mayoría de las peticiones en la red, 
son: 
• GET, PUT, DELETE, POST y HEAD: 
Siendo GET y POST los métodos principales de las comunicaciones en la red. 
2.2. Servidor web Apache 
Apache es un servidor web o servidor HTTP de código abierto gratuito, para plataformas Unix (BSD, 
GNU/Linux, etc.), Microsoft Windows, macOS y otras, que implementa el protocolo HTTP. Es el 
servidor web más extendido de Internet, y es multiplataforma. 

<!-- Page 40 -->

 
 
Aplicaciones y desarrollo web 
40 
La mayoría de los servidores web de todo el mundo está publicado bajo la plataforma Apache, aunque 
su cuota de mercado va decayendo. 
La fundación Apache, es una organización sin ánimo de lucro responsable de una cantidad enorme de 
proyectos, entre los que destaca este servidor HTTP. 
Con Apache se pueden servir sitios estáticos, pero también dispone de módulos para dar soporte a 
múltiples lenguajes, como Perl, Python o PHP, el más popular. 
Arquitectura interna de Apache 
El funcionamiento de Apache se basa en un proceso maestro que se encarga de arrancar y gestionar 
varios procesos o hilos de trabajo encargados de atender las peticiones de los clientes. Según el modelo 
de multiprocesamiento configurado, Apache puede trabajar en distintos modos: 
• Prefork: crea múltiples procesos independientes, cada uno atendiendo una única petición a la 
vez. Es estable, pero consume más memoria. 
• Worker: combina procesos con múltiples hilos, lo que reduce el consumo de recursos y mejora \nel rendimiento. 
• Event: evolución del modo worker, optimizado para conexiones persistentes como HTTPS o 
webs con muchas conexiones simultáneas. 
Ficheros y estructura de configuración 
La configuración principal de Apache se encuentra en los ficheros: 
• httpd.conf (en distribuciones clásicas) o apache2.conf (en Debian/Ubuntu). 
• Carpetas sites-available y sites-enabled, que permiten activar o desactivar fácilmente sitios 
web mediante enlaces simbólicos. 
• Archivos de registro: access.log (peticiones) y error.log (errores del servidor). 
Directivas más importantes 
Algunas de las directivas más habituales que aparecen en la configuración de Apache son: 
• DocumentRoot: define el directorio donde se encuentra el contenido web. 
• Directory: establece reglas específicas de acceso y permisos sobre carpetas. 
• AllowOverride: determina si se pueden usar archivos .htaccess para sobreescribir 
configuraciones locales. 
• Options: controla funciones como ejecución de scripts, seguimiento de enlaces simbólicos o 
listado de directorios. 

<!-- Page 41 -->

 
 
Aplicaciones y desarrollo web 
41 
VirtualHost 
La función esencial de un servidor Web, como su nombre indica es proveer de páginas web a los 
navegantes. Un servidor Apache puede servir páginas de un solo dominio o de varios dominios o 
subdominios, es una distinción importante ya que habrá que especificarla en el archivo de configuración 
del servidor apache2.conf. 
 
Seguridad en Apache 
Para garantizar comunicaciones seguras y un servicio robusto, Apache incluye opciones y módulos 
como: 
• mod_ssl: habilita el uso de certificados digitales para HTTPS. 
• Control de acceso mediante autenticación básica o avanzada. 
• Archivos .htaccess para definir reglas de seguridad locales (redirecciones, contraseñas, 
limitación de acceso por IP). 
• Monitorización mediante logs y compatibilidad con herramientas SIEM. 
 

<!-- Page 42 -->

 
 
Aplicaciones y desarrollo web 
42 
 
 
 
+ Info 
Un stack tecnológico, o stack de soluciones o ecosistema de datos, \nes una lista de todos los servicios tecnológicos utilizados para 
construir y ejecutar una sola aplicación. 
Stack es una palabra inglesa, que significa pila de cosas o 
apilamiento. 
 
Stack de tecnologías de Apache: 
• LAMP: 
Contiene: Linux, Apache, MySQL, PHP. 
• XAMPP: 
Contiene: el sistema de gestión de bases de datos MySQL, y los intérpretes para lenguajes de 
script PHP y Perl. 
 
 
 
 
Importante 
Apache CXF: Es una librería para la implementación de servicios 
web de la API Java JAX-WS. 
Apache Axis2: Es un motor nuclear para servicios web. Es un 
rediseño total y una reimplementación completa de la 
ampliamente difundida pila SOAP "Apache Axis". Existen 
implementaciones de Axis2 en Java y en C. 
Axis2 no solo provee la capacidad de agregar servicios web a las 
aplicaciones web, sino que además puede funcionar como servidor 
autónomo. 
 

<!-- Page 43 -->

 
 
Aplicaciones y desarrollo web 
43 
Apache en topologías cliente-servidor 
Apache se despliega de distintas formas según la arquitectura: 
• 2 capas: cliente web y servidor Apache (sirviendo páginas estáticas o dinámicas simples). 
• 3 capas: Apache como servidor frontal, recibiendo peticiones y enviándolas a un servidor de 
aplicaciones (Tomcat, JBoss, GlassFish) que contiene la lógica de negocio, y a un servidor de 
bases de datos para la persistencia. 
• N capas / balanceadas: uso de varios servidores Apache en paralelo detrás de un balanceador 
de carga, con réplicas para escalabilidad y alta disponibilidad. 
Proyectos relacionados 
• Apache CXF: librería para implementar servicios web en Java (JAX-WS). 
• Apache Axis2: motor de servicios web que permite trabajar con SOAP. 
2.3. Internet Information Services (IIS) 
Internet Information Services (IIS) es el servidor web desarrollado por Microsoft, incluido en los 
sistemas operativos Windows Server y en algunas versiones de Windows cliente. Su función es alojar 
sitios web, aplicaciones y servicios, sirviendo contenidos a través de los protocolos HTTP y HTTPS. IIS 
se integra de forma nativa con el ecosistema Windows, lo que facilita la gestión mediante Active 
Directory, PowerShell o las propias herramientas de administración de Windows. 
Arquitectura y componentes 
IIS se apoya en un conjunto de servicios y procesos que definen su arquitectura. En el núcleo se \nencuentra HTTP.sys, un controlador en modo kernel que recibe las peticiones web y las enruta a los 
procesos de trabajo. Sobre él opera el servicio WAS (Windows Process Activation Service), que se \nencarga de activar y gestionar los procesos de IIS, conocidos como worker processes (w3wp.exe). 
Estos procesos se agrupan en application pools, que aíslan sitios o aplicaciones entre sí para mejorar la 
seguridad y estabilidad. 
La arquitectura se organiza en torno a tres elementos clave: 
• HTTP.sys: controlador que gestiona las solicitudes a nivel kernel. 
• WAS: servicio encargado de la activación de procesos. 
• Worker processes y application pools: donde se ejecutan las aplicaciones web. 

<!-- Page 44 -->

 
 
Aplicaciones y desarrollo web 
44 
Sitios, aplicaciones y directorios virtuales 
IIS organiza los recursos en varios niveles. Un sitio web es el conjunto de bindings (IP, puerto y nombre 
de host) que apunta a un directorio físico. Dentro de un sitio se pueden definir aplicaciones, que 
representan unidades lógicas con configuración independiente, y también directorios virtuales, que 
permiten mapear rutas a carpetas físicas o a ubicaciones en red. 
En este ámbito, los bindings son esenciales porque determinan cómo los usuarios acceden al sitio (por 
IP, nombre de dominio o puerto), y permiten, entre otras cosas, el uso de SNI (Server Name Indication) 
para alojar múltiples certificados en una misma dirección IP. 
Configuración 
La configuración de IIS se realiza a través de ficheros XML y herramientas específicas. El archivo 
principal es applicationHost.config, que guarda la configuración global del servidor, mientras que cada 
aplicación puede tener su propio fichero web.config, donde se definen reglas específicas (autenticación, 
autorización, reescritura de URL, etc.). 
Para administrar estos parámetros, IIS ofrece diferentes herramientas: 
• IIS Manager (inetmgr): interfaz gráfica para gestionar sitios, pools y certificados. 
• AppCmd: utilidad de línea de comandos que permite crear, iniciar y detener sitios o aplicaciones. 
• PowerShell (módulo WebAdministration): la vía recomendada para la administración avanzada 
y automatizada. 
Seguridad 
La seguridad en IIS combina opciones de autenticación, autorización y cifrado. IIS admite múltiples 
métodos de autenticación, desde la básica y la anónima hasta la autenticación integrada de Windows 
con Kerberos o NTLM. Para proteger las comunicaciones utiliza certificados digitales y el módulo 
TLS/SSL, lo que permite desplegar HTTPS y habilitar funciones como HSTS. 
Además, IIS incluye mecanismos para endurecer el servidor, como Request Filtering, que bloquea 
peticiones sospechosas, y el uso de archivos web.config para aplicar reglas de seguridad específicas. A 
nivel práctico, la seguridad se refuerza con: 
• Autenticación configurable (anónima, básica, Windows, certificados). 
• Uso de TLS/SSL y gestión de certificados. 
• Request Filtering y control de acceso mediante reglas en web.config. 

<!-- Page 45 -->

 
 
Aplicaciones y desarrollo web 
45 
Rendimiento y disponibilidad 
IIS permite configurar políticas de rendimiento a través del reciclado de los application pools, que 
pueden reiniciarse automáticamente en función del tiempo o del consumo de memoria. Esto garantiza 
que los servicios sigan funcionando aunque se produzcan fugas de recursos. 
Otros mecanismos habituales son la compresión de contenidos, el uso de caché en memoria y el 
soporte de balanceo mediante Application Request Routing (ARR), que convierte a IIS en un proxy 
inverso capaz de distribuir la carga entre varios servidores. De este modo, IIS puede usarse tanto en 
topologías simples de dos capas como en arquitecturas de tres capas o en entornos de alta 
disponibilidad. 
Diagnóstico y monitorización 
IIS proporciona varias formas de supervisar el funcionamiento del servidor. Los logs de acceso y error 
registran cada petición y facilitan auditorías y análisis de seguridad. Además, IIS incorpora el sistema 
Failed Request Tracing (FREB), que permite capturar trazas detalladas de peticiones que fallan. La 
información se complementa con el Visor de Eventos de Windows, donde se reportan errores del 
servicio y de los procesos de trabajo, así como con contadores de rendimiento que monitorizan el uso 
de CPU, memoria y conexiones. 
Integración con plataformas y lenguajes 
Aunque IIS está optimizado para aplicaciones basadas en ASP.NET, también soporta otros lenguajes y 
frameworks gracias a módulos de integración. Por ejemplo, FastCGI permite ejecutar aplicaciones PHP, 
mientras que ARR posibilita que IIS actúe como proxy inverso para aplicaciones Java, Node.js o ASP.NET 
Core que se ejecutan en servidores externos. 
Comandos básicos 
Además de las herramientas gráficas, IIS puede administrarse desde la línea de comandos. Algunos 
comandos útiles son: 
• Iniciar un servicio web específico: appcmd start site /site.name:"Nombre del sitio" 
• Detener un servicio web concreto: appcmd stop site /site.name:"Nombre del sitio" 
• Reiniciar Internet Information Services: iisreset 
• Reiniciar Internet Information Services sin reiniciar todos los servicios: iisreset /noforce 
2.4. Servidor Web Nginx 
Nginx (pronunciado engine-x) es un servidor web y proxy inverso de código abierto, diseñado para 
ofrecer alto rendimiento, bajo consumo de recursos y gran capacidad de concurrencia. Se desarrolló 
inicialmente en 2004 para solucionar el problema conocido como C10k (atender decenas de miles de 
conexiones simultáneas). 

<!-- Page 46 -->

 
 
Aplicaciones y desarrollo web 
46 
A diferencia de Apache, que se basa en procesos o hilos, Nginx utiliza un modelo de eventos asíncrono y 
no bloqueante, lo que le permite gestionar muchas conexiones de forma eficiente con muy pocos 
recursos. 
Nginx puede funcionar en varios roles: 
• Servidor web para entregar contenido estático. 
• Proxy inverso y balanceador de carga, distribuyendo peticiones a varios servidores de 
aplicaciones (Node.js, Tomcat, Gunicorn, etc.). 
• Terminador TLS para gestionar el cifrado HTTPS antes de reenviar peticiones. 
Gracias a estas características, es ampliamente utilizado en arquitecturas de microservicios y 
contenedores, siendo habitual verlo en combinación con Docker y Kubernetes. Actualmente, gran parte 
de los sitios web de alto tráfico (como Netflix o Airbnb) lo utilizan como servidor frontal. 
2.5. Patrones de diseño GoF 
En el ámbito del desarrollo de aplicaciones web también se aplican los patrones de diseño orientado a 
objetos descritos por el grupo GoF (Gang of Four). Estos patrones, ya estudiados en la unidad 4 de este 
mismo bloque "Diseño y programación orientada a objetosProgramación Orientada a Objetos...", 
proporcionan soluciones reutilizables a problemas comunes de diseño y se clasifican en patrones 
creacionales, estructurales y de comportamiento. 
En el desarrollo web resultan especialmente relevantes porque permiten organizar la lógica de 
presentación y de negocio de forma clara y mantenible. Frameworks y entornos muy extendidos, como 
los basados en MVC (Model-View-Controller), incorporan en su funcionamiento principios derivados de \nestos patrones. Gracias a ello, las aplicaciones web logran una mayor cohesión, escalabilidad y facilidad 
de mantenimiento. 
Además de MVC, los patrones GoF se manifiestan de manera práctica en distintos componentes del 
desarrollo web: 
• El patrón Singleton se emplea, por ejemplo, para centralizar la gestión de la conexión a la base 
de datos en aplicaciones PHP, Java o .NET. 
• El Factory Method aparece en la creación dinámica de objetos de petición y respuesta que 
maneja el servidor. 
• El Observer resulta clave en la programación orientada a eventos en navegadores y frameworks 
JavaScript. 
Estos casos evidencian cómo los patrones contribuyen a mejorar la reutilización del código y a 
mantener una arquitectura más flexible en proyectos web modernos. 

<!-- Page 47 -->

 
 
Aplicaciones y desarrollo web 
47 
2.6. Automatización de pruebas 
Selenium WebDriver es la herramienta de código abierto más extendida para la automatización de 
pruebas de aplicaciones web. Permite controlar un navegador de forma programática, simulando las 
interacciones de un usuario real (clic, escritura, navegación) para validar el funcionamiento y la 
compatibilidad de una web en distintos entornos (navegadores como Chrome, Firefox, Edge y sistemas 
operativos como Windows, Linux, macOS). Es parte del proyecto Selenium, que también incluye 
Selenium IDE (para grabar y reproducir tests) y Selenium Grid (para ejecución en paralelo). 
Arquitectura y funcionamiento 
WebDriver sigue una arquitectura cliente-servidor basada en el Protocolo W3C WebDriver: 
• Cliente: El script escrito por el tester en lenguajes como Java, Python, C#, Ruby, etc., usando las 
librerías de Selenium. 
• Servidor (Driver): Un ejecutable específico para cada navegador (e.g., chromedriver para 
Chrome, geckodriver para Firefox). Este driver recibe los comandos HTTP del cliente y los 
translate en acciones nativas sobre el navegador. 
• Navegador: Ejecuta las acciones y devuelve las respuestas al driver. 
Esta arquitectura permite que un mismo test pueda reproducirse en distintos entornos sin modificar el 
código. 
Características y conceptos técnicos 
Selenium WebDriver se caracteriza por su soporte multiplataforma y multilenguaje, además de por su 
capacidad de interactuar con cualquier elemento de una página. Para ello utiliza diferentes estrategias 
de localización de elementos (locators): By.id(), By.name(), By.xpath() y By.cssSelector(), siendo esta 
última la más potente. Otro concepto esencial es el manejo de esperas (waits), necesario para trabajar 
con aplicaciones que cargan contenido de forma asíncrona: 
• Implicit Waits: establecen un tiempo global de espera para localizar elementos. 
• Explicit Waits: aplican una condición específica, como que un botón sea clicable o un texto 
visible, usando la clase WebDriverWait. 
Asimismo, para mejorar la mantenibilidad de los tests se utiliza el patrón Page Object Model (POM), 
que organiza las pruebas creando una clase por cada página. Cada clase encapsula tanto los 
localizadores como los métodos que representan las interacciones, lo que facilita el mantenimiento y 
reduce la duplicación de código. 

<!-- Page 48 -->

 
 
Aplicaciones y desarrollo web 
48 
Ventajas, Desventajas y Ecosistema más Amplio 
La automatización de pruebas ofrece repetibilidad, eficiencia y reduce errores humanos en las pruebas 
de regresión. Su principal desventaja es el esfuerzo inicial y de mantenimiento continuo para adaptarse 
a los cambios en la interfaz de la aplicación. 
Selenium WebDriver se especializa en pruebas end-to-end (E2E) de la UI. El testing automatizado 
abarca más tipos, para los que se usan otras herramientas: 
• Pruebas Unitarias: JUnit (Java), TestNG (Java), pytest (Python). 
• Pruebas de Carga/Rendimiento: JMeter, Gatling. 
• Alternativas Modernas para E2E: Cypress y Playwright. 
Integración en CI/CD 
El papel de la automatización dentro de los procesos de Integración y Entrega Continua (CI/CD) es 
fundamental. Los tests automatizados se integran en pipelines (Jenkins, GitLab CI, GitHub Actions) 
para ejecutarse de forma automática tras cada integración de código. Esto valida las nuevas versiones 
del software de forma rápida y fiable, actuando como una red de seguridad que previene el despliegue 
de errores en producción y garantizando la calidad del software. 
2.7. Seguridad en aplicaciones web 
La seguridad es un aspecto fundamental en el desarrollo y despliegue de aplicaciones web, ya que estas 
se encuentran expuestas de forma directa a internet y, por tanto, a posibles ataques. Una de las 
medidas básicas es el uso de HTTPS, que cifra la comunicación entre cliente y servidor mediante los 
protocolos SSL/TLS, garantizando confidencialidad e integridad en la transmisión de datos. 
Además, organismos como OWASP (Open Web Application Security Project) publican guías de 
referencia, como el conocido OWASP Top 10, que recopilan las vulnerabilidades más frecuentes en 
aplicaciones web y las mejores prácticas para mitigarlas. Entre las amenazas más habituales se \nencuentran las inyecciones de código (SQLi), el Cross-Site Scripting (XSS), el Cross-Site Request 
Forgery (CSRF) y los problemas de gestión de sesiones. 
La seguridad en aplicaciones web no depende solo del uso de HTTPS, sino también de políticas de 
desarrollo seguro y de una correcta configuración del servidor. Esto incluye aspectos como: 
• Validación de entradas. 
• Gestión adecuada de credenciales y permisos. 
• Protección contra ataques de fuerza bruta. 
• Actualización constante de servidores, frameworks y librerías. 
En este sentido, la seguridad se entiende como un proceso continuo que acompaña a la aplicación en 
todas sus fases: diseño, desarrollo, pruebas y despliegue en producción. 

<!-- Page 49 -->

 
 
Aplicaciones y desarrollo web 
49 
3. Desarrollo web: cliente y servidor 
Para desarrollar una aplicación web, hay que tener en cuenta la división entre el cliente y el servidor. 
El desarrollo requiere un amplio conjunto de conocimientos y habilidades. Por eso, existen distintas \nespecialidades, y los desarrolladores suelen especializarse en la parte de desarrollo Cliente, o la parte 
Servidor, para poder dominar y estar actualizado en los conocimientos enfocados a ese apartado, ya 
que constantemente aparecen novedades, siendo expertos profesionales en su campo. 
Normalmente, el desarrollo de una aplicación web lo realiza un equipo en el que cada profesional, se \nencarga de una parte del desarrollo, con funciones perfectamente definidas. 
 
 
 
 
+ Info 
Sea cual sea tu especialidad, también tendrás que tener habilidades 
sociales, como facilidad de aprendizaje y comunicación, capacidad 
resolutiva etc. 
Están de moda los términos: 
• "Soft Skills": habilidades blandas. 
Se adquieren en la vida diaria, socializando, y ayuda a 
integrarse en cualquier ambiente sea o no laboral. 
• "Hard skills": habilidades duras. 
Se adquieren mediante formación y experiencia 
profesional. 
 
 
Ya hemos visto las tres divisiones que se utilizan para nombrar dichas especialidades de forma genérica 
son: 
• Front-end: enfocada a la parte de las aplicaciones cliente. 
• Back-end: enfocada a la parte de las aplicaciones servidor. 
• Full stack: una mezcla de conocimientos de las 2 anteriores. 
 

<!-- Page 50 -->

 
 
Aplicaciones y desarrollo web 
50 
 
 
 
+ Info 
JHipster: 
• Es un framework Java para desarrollar aplicaciones con 
Angular y Spring Boot. 
• Es un generador de aplicaciones gratuito y de código 
abierto, que se utiliza para desarrollar rápidamente 
aplicaciones web modernas y microservicios. 
• Proporciona herramientas para generar un proyecto con 
una pila Java en el lado del servidor (usando Spring Boot) y 
un front-end web receptivo en el lado del cliente (con 
Angular y Bootstrap). 
 
Veamos a estudiarlo estas divisiones más detenidamente. 
3.1. Front-end: aplicaciones cliente 
Son las aplicaciones del lado cliente, lo que se ve, los navegadores. 
Los desarrolladores se ocupan principalmente de los componentes externos del sitio web o de la 
aplicación web. Como consecuencia, deben dominar obligatoriamente lenguajes como: 
• Son los más importantes: 
• HTML. 
• CSS. 
• JavaScript. 
• Otros como: 
• DHTML. 
• Lenguajes de script: VBScript, etcétera. 

<!-- Page 51 -->

 
 
Aplicaciones y desarrollo web 
51 
• ActiveX. 
• Applets programados en Java. 
• Plug-ins (Adobe Acrobat Reader, Macromedia Flash, etcetera). 
En general se asocia a los desarrolladores front-end con los principios de diseño y de estructura de 
páginas. 
El programador también debe tener en cuenta usabilidad y legibilidad de la página o aplicación web, y 
que la información no se almacena en el lado Cliente. 
La parte cliente de las aplicaciones web suele ser una página web que contiene: 
• Código HTML. 
• Opcionalmente: 
• Applets de Java. 
• Código ejecutable en un lenguaje de script. 
• Plug-ins. 
Por tanto, la misión del cliente web es interpretar las páginas HTML y los diferentes recursos que 
contienen (imágenes, sonidos, etcétera). 
 
 
 
 
Nota 
Hoy en día, las altas capacidades de los navegadores los han 
convertido en lo que podríamos denominar "sistemas operativos 
de la Web", con APIs avanzadas. 
 
Vamos a ver con detenimiento los 3 lenguajes más importantes en Front-End: HTML, CSS y 
JavaScript. Y también hablaremos de AJAX, que combina varias tecnologías. 
3.1.1. HTML 
HTML: (HyperText Markup Language). 
HTML es el lenguaje de marcado estándar para crear páginas web (lenguaje por etiquetas). 

<!-- Page 52 -->

 
 
Aplicaciones y desarrollo web 
52 
Sin HTML, las páginas web no pueden existir, es el componente estructural clave de todas las webs de 
internet. 
 
 
 
 
Imprescindible 
HTML, NO es un lenguaje de programación, es un lenguaje de 
marcado. 
 
 
Algunas características son: 
• HTML significa lenguaje de marcado de hipertexto. 
• HTML describe la estructura de las páginas web mediante etiquetas. 
• Los elementos HTML son los componentes básicos de las páginas HTML. 
• Los elementos HTML están representados por etiquetas. 
• Las etiquetas HTML etiquetan fragmentos de contenido, como "encabezado", "párrafo", "tabla", \netcétera. 
• Los navegadores no muestran las etiquetas HTML, pero las usan para representar el contenido 
de la página. 
 
 
 
 
El experto opina 
Se pueden generar páginas HTML con editores de texto (como 
Word) de una forma mucho más sencilla, pero el código no será 
tan eficiente. 
Vamos a estudiar cómo hacer este código a mano. 
 

<!-- Page 53 -->

 
 
Aplicaciones y desarrollo web 
53 
Etiquetas 
Las etiquetas se presentan entre < >. 
La sintaxis es la siguiente: 
<nombre_etiqueta> Contenido </nombre_etiqueta> 
Las etiquetas HTML normalmente vienen en pares (una de apertura y otra de cierre. Por ejemplo, 
<p> y </p>). 
• La primera etiqueta se denomina etiqueta de inicio o de apertura. 
• La segunda etiqueta se le denomina de fin o de cierre. 
La mayoría de etiquetas HTML encierran un contenido de texto entre la etiqueta de apertura y la \netiqueta de cierre, pero existen algunas etiquetas especiales denominadas "etiquetas vacías" que no 
necesitan encerrar ningún texto. 
Una de estas "etiquetas vacías" es por ejemplo <br> (para realizar un salto de línea) que nunca encierra 
ningún contenido de texto. 
Como el estándar XHTML obliga a cerrar todas las etiquetas abiertas, siempre que se incluya la etiqueta 
<br> se debería cerrar, de forma que había que indicar: <br></br>, para que la escritura del código 
resulte más cómoda, XHTML permite en estos casos escribir de forma abreviada una etiqueta que se 
abre y se cierra de forma consecutiva, y en lugar de indicar <br></br>, se permite indicar la sintaxis 
<br/> en su lugar, para indicar que es una etiqueta vacía que se abre y se cierra en ese mismo punto. 
Ejemplo: 
• correcto en XHTML: <br/> 
• incorrecto en XHTML (pero correcto en HTML): <br> 
Navegadores 
El propósito de los navegadores es leer los documentos en formato HTML. 
No mostrará las etiquetas, pero las utiliza para determinar qué formato darle al documento (como 
mostrarlo). 

<!-- Page 54 -->

 
 
Aplicaciones y desarrollo web 
54 
3.1.1.1. Estructura básica de una página web en HTML 
Todos los documentos HTML deben comenzar con una declaración del tipo de documento 
(<!DOCTYPE html>) 
El DOCTYPE o "Declaración del tipo de documento (DTD)" es una instrucción especial que debe 
indicarse al principio del documento HTML y que permite al navegador entender qué versión de HTML \nestamos utilizando. El DTD Indica que nuestro documento está escrito siguiendo la estructura 
determinada por un DTD concreto. 
Sintaxis del DOCTYPE en la versión HTML5, se ha simplificado a indicar únicamente <!DOCTYPE html>, 
mientras que en versiones anteriores se indicaba más información, como la disponibilidad, versión de 
HTML, idioma etc. 
 
 
 
 
+ Info 
La W3C tiene definidos un gran número de DTD, que son 
resumidos en su listado de declaraciones de DOCTYPE . 
https://www.w3.org/QA/2002/04/valid-dtd-list.html 
 
 
Una página HTML tiene 3 elementos contenedores, que se indican después de la declaración del tipo de 
documento, siguiendo la siguiente estructura: 
• Indicar que es un documento HTML. 
El documento se abre con la etiqueta <html> y se cierra con la correspondiente </html>. 
• A continuación, se indica la cabecera (head). 
Se abre con la etiqueta de apertura <head> y se cierra con la correspondiente </head>. 
Entre ambas etiquetas se específica la información técnica para el navegador. 
• Por último, está el cuerpo (body) del documento. 
Se abre con la etiqueta de apertura <body> y se cierra con la correspondiente </body>. 
Entre ambas etiquetas se específica el contenido que será mostrado en la página web, como \nencabezados, párrafos, etc. 

<!-- Page 55 -->

 
 
Aplicaciones y desarrollo web 
55 
 
Estructura básica de un documento HTML 
<head> 
Se indica la información que no será visible en la página web, pero que es necesaria para su 
funcionamiento y para el navegador. 
Estas informaciones son los metadatos (datos que describen otros datos), como, por ejemplo: 
• Meta Charset (encoding de la página): 
Indica la codificación de caracteres utilizada (charset). El UTF-8 es el estándar para de 
UNICODE para HTML5, por lo que la etiqueta es: 
<meta charset="utf-8" /> 
• Otros atributos para la etiqueta Meta. 
Permiten añadir el autor de la página y descripción concisa del contenido de la misma. 
Atributos: 
• name especifica el tipo de metadato del que se trata; es decir, qué tipo de información 
contiene. 

<!-- Page 56 -->

 
 
Aplicaciones y desarrollo web 
56 
• content especifica el contenido del metadato en sí. 
Ejemplos: 
<meta name="author" content="Piluca Tomás"> 
<meta name="description" content="Aprendizaje de creación de páginas web con HTML> 
• Etiqueta Base. 
La etiqueta HTML <base> sirve para especificar la dirección URL base que será empleada en 
todas las direcciones relativas que se encuentran dentro del documento HTML en cuestión. En 
todo el documento, solo puede existir un único elemento <base> 
El elemento <base> cuenta con los siguientes atributos globales: 
• href: definimos la dirección URL base que se empleará en todo el documento para todas las 
URL relativas. 
Ejemplo: 
<base href="https://ejemplos.com/html/"/> 
Allá donde existan direcciones relativas, como las que vemos en el ejemplo siguiente, el 
navegador cambiará de manera interna la ruta completando la base de las mismas con la 
indicada en la etiqueta base. 
Ejemplo: 
<a href="pagina1.html"/>Página 1</a><img src="imagen1.jpg"/> 
<script type='text/javascript' src="script.js"><script> 
• Meta Viewport (para webs responsive). 
La etiqueta viewport permite a los desarrolladores de web apps, definir el ancho, alto y escala 
del área usada por el navegador para mostrar contenido, es la etiqueta que mejor representa la 
web en movilidad. Define qué área de pantalla está disponible al renderizar un documento, la 
parte del documento que el usuario está viendo, ya sea en su ventana o en la pantalla si está 
usando el modo pantalla completa. (El contenido fuera del viewport no es visible en la pantalla 
hasta que sea desplazado dentro de él). 

<!-- Page 57 -->

 
 
Aplicaciones y desarrollo web 
57 
• Title. 
Indica el título de la página web, (lo que muestra el navegador en la barra de título cuando carga 
la página). 
Cuando un usuario, crea un marcador para la página, el navegador emplea el título para \netiquetarlo en el menú Marcadores (o favoritos). 
También, cuando la página aparece en una búsqueda Web, se suele mostrar este título como 
primera línea en los resultados, seguido de un fragmento del contenido de la página. 
Ejemplo: <title>Unidad didáctica: Aplicaciones y Diseño web</title> 
También puede incluir palabras clave de búsqueda, hoja de estilo css para aplicar a la página o enlace a 
ficheros CSS externos, así como JavaScript. 
<body> 
Toda la parte visible del documento está dentro de la etiqueta <body>, es el cuerpo de la web. 
En su interior definiremos todo lo que será visible para el usuario. 
Finalizar todo ese contenido visible para el usuario con la etiqueta </body>. 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
     <body> 
     <h1>Esto es una cabecera</h1> 
     <p>Esto es un párrafo</p> 
     </body> 
     </html> 
El navegador devolvería lo siguiente: 
 
Respuesta del navegador 

<!-- Page 58 -->

 
 
Aplicaciones y desarrollo web 
58 
3.1.1.2. Atributos 
Los atributos proporcionan información adicional sobre los elementos HTML. 
Características generales 
• Los atributos siempre se especifican en la etiqueta de inicio de un elemento. Se colocan dentro 
de la etiqueta de apertura y después del nombre del elemento, antes del signo de cierre >. 
• Los atributos generalmente vienen en pares de nombre/valor. 
Ejemplo: lang = "es-ES". lang es utilizado para especificar el idioma del contenido dentro de un \nelemento HTML. 
A continuación ponemos ejemplos de atributos comunes en HTML, la versión en la que fueron 
implementados y describimos su funcionalidad. 
• accesskey (HTML 4.0): Permite establecer una tecla para acceder de forma rápida a cualquier \nelemento. Aunque la tecla de acceso rápido se establece mediante HTML, la combinación de 
teclas necesarias para activar ese acceso rápido depende del navegador. 
• Internet Explorer: se pulsa la tecla ALT + la tecla definida. 
• Google Chrome: se pulsa Alt + tecla, Control + Alt + tecla. 
• Firefox: se pulsa Alt + Shift + la tecla definida 
• Opera: se pulsa Shift + Esc + la tecla definida 
• Safari: se pulsa Ctrl + la tecla definida 
• action (HTML 2.0): acompaña a la etiqueta form y especifica su url de destino. 
<form action="registro.php" method="post" enctype="multipart/form-data"> 
• alt (HTML 2.0): atributo que permite especificar un texto alternativo para una imagen, cuando \nesta no puede cargar por el motivo que sea. 
• autocomplete (HTML 5): guarda y sugiere datos previamente ingresados por el usuario en un 
campo de entrada cuando vuelve a interactuar con él 
<input type="text" id="nombre" name="nombre" autocomplete> 

<!-- Page 59 -->

 
 
Aplicaciones y desarrollo web 
59 
• autofocus (HTML 5): este atributo llevará el foco a la etiqueta que lo contiene al cargar la 
página, solo puede asignarse a una etiqueta por página web, 
<input type="text" id="nombre" name="nombre" autofocus> 
• disabled (HTML 4.0): atributo que deshabilita una etiqueta y la convierte en una etiqueta no 
modificable, no enfocable y no seleccionable. Los valores que tenga no serán enviados con el 
resto al sevidor. 
<input type="text" id="nombre" value="nombre" disabled> 
• El atributo enctype (HTML 4.0) en HTML se utiliza principalmente en la etiqueta <form> para \nespecificar el tipo de codificación que se utilizará al enviar los datos de un formulario a un 
servidor. 
• for (HTML 4.01): atributo usado fundamentalmente para la etiqueta label en el que se sugiere al 
usuario indicaciones explicando la etiqueta a la que pertenece. 
<label for="edad">Introduce tu edad<input id="edad" type="number"></label> 
• hidden (HTML 5): atributo que oculta la etiqueta que lo contiene al usuario pero sí está 
presente en el árbol DOM, puede usarse para almacenar algún valor de utilidad para el sistema. 
<input type="text" hidden name="token" value="12345abcde"> 
• href (HTML 2.0): abreviatura de hypertext reference especifica la dirección web (URL) de un \nenlace. 
• id (HTML 4.0): atributo introducido en 1997 y uno de los más importantes pues permite asignar 
un identificador único a una etiqueta o elemento asegurando que no habrá duplicados del 
mismo. Asimismo este atributo puede servir de ancla para enlaces internos. 

<!-- Page 60 -->

 
 
Aplicaciones y desarrollo web 
60 
<a href="#seccion2">Ir a la Sección 2</a> 
<a href="https://lagarcetadelaribera.org">La gaRceta de la ribera</a> 
<section id='seccion1'> 
     <h2>Esta es la Sección 1</h2> 
</section> 
<section id='seccion2'> 
     <h2>Esta es la Sección 2</h2> 
</section> 
• list (HTML 5): atributo que se combina con la etiqueta datalist y que propone determinados 
valores en un input. 
<input type="text" id="pais" name="pais" list="paises"> 
     <datalist id="paises"> 
       <option value="España"> 
       <option value="México"> 
       <option value="Argentina"> 
       <option value="Colombia"> 
     </datalist> 
• maxlength (HTML 4.0): atributo que especifica el número de caracteres alfanuméricos 
aceptados por una etiqueta de entrada de texto. 
<input type="text" id="username" name="username" maxlength="15"> 
• min, max (HTML 5): estos atributos pueden usarse con inputs de tipo, number, range, date, 
datetime-local, month, week, time en los que se podrán especificar valores mínimos y máximos. 
<input id="edad" type="number" max="60"> 

<!-- Page 61 -->

 
 
Aplicaciones y desarrollo web 
61 
• multiple (HTML 5): permite que un usuario seleccione más de una opción dentro de un \nelemento, permite que el usuario seleccione varias opciones sin necesidad de mantener 
presionada la tecla Ctrl o Shift en el teclado. 
<select multiple> 
  <option value="option1">Opción 1</option> 
  <option value="option2">Opción 2</option> 
  <option value="option3">Opción 3</option> 
</select> 
• name (HTML 2.0): se utiliza en varios elementos HTML para identificar y nombrar esos \nelementos y mandar sus valores al sevidor en pares nombre (name) y valor. 
<input type="text" name="usuario" /> 
• pattern (HTML 5): permite especificar una expresión regular que deber cumplirse para poder \nenviar un formulario. 
<input type="text" id="codigo" name="codigo" pattern="[A-Za-z0-9]+" title="Solo 
letras y números"> 
• placeholder (HTML 5): atributo que cumple una función parecida al label pero dentro de la 
propia etiqueta. 
<input id="edad" placeholder="Introduce tu edad"> 
• readonly (HTML 4.0): atributo que no permite modificar o insertar valores en una etiqueta y 
aunque sí permite seleccionar y tener el foco, la convierte en una etiqueta de solo lectura, pero 
los valores que tenga se envían con el resto. 
<input type="text" id="info" value="Solo lectura" readonly> 

<!-- Page 62 -->

 
 
Aplicaciones y desarrollo web 
62 
• required (HTML 5): atributo que impide enviar un formulario si no se ha complicado la etiqueta 
a la que pertenece. 
<input id="edad" required> 
• rows, cols (HTML 2.0): atributos específicos del textarea que establecerán sus dimensiones, 
filas y columnas. 
<textarea id="comentarios" name="comentarios" rows="4" cols="50"></textarea> 
• step (HTML 5): esepecifica el intervalo permitido entre dos valores. 
<input type="number" min="0" max="10" step="2"> 
• size (HTML 2.0): determina el número de carácteres que el campo puede mostrar 
simultáneamente, no confundir con maxlength pues este último no te permite escribir más de 
los caracteres especificados, size en cambio establece el tamaño de la caja de texto. 
<input type="text" id="username" name="username" size="15"> 
• spellcheck="[true/false]" (HTML 5): activa/desactiva, según se especifique true o false la 
comprobación de ortografía en la etiqueta que lo contiene: 
<textextarea id="observaciones" name="observaciones" 
spellcheck="false"></textarea> 
• src (HTML 2.0): atributo esencial para elementos que cargan recursos externos, como 
imágenes, scripts, y multimedia. 

<!-- Page 63 -->

 
 
Aplicaciones y desarrollo web 
63 
<audio src="audio.mp3" controls></audio> 
<img src='https://elpais.com/images/imagenbonita.jpg'> 
• style (HTML 4.0): proporciona una manera de definir reglas de estilo en línea. 
<p style="color: blue; font-size: 1em;">El color de este texto es azul y el tamaño 
de la fuente de 1em.</p> 
• tabindex (HTML 4.01): permite alterar el orden en el que se seleccionan los elementos, resulta 
muy útil para controlar de forma precisa cómo se seleccionan los campos de un formulario 
complejo. 
• title (HTML 4.0): muestra un texto emergente (tooltip) cuando un usuario pasa el cursor sobre \nel elemento al que está asociado. 
<img src='perro.jpg' title="Cocker Spaniel"> 
• value (HTML 2.0): establece un valor por defecto en una etiqueta de entrada, 
<input type="text" id="defecto" name="defecto" value="Valor inicial"> 
Atributo 
Descripción 
accesskey = 
"letra" 
Establece una tecla de acceso rápido a un elemento HTML. 
tabindex = 
"numero" 
Establece la posición del elemento en el orden de tabulación de la página. Su valor debe \nestar comprendido entre 0 y 32.767. 
onfocus, onblur 
Controlan los eventos JavaScript que se ejecutan cuando el elemento obtiene o pierde el 
foco. 

<!-- Page 64 -->

 
 
Aplicaciones y desarrollo web 
64 
3.1.1.3. Principales elementos 
Los elementos van dentro del cuerpo (etiqueta <body>) a excepción del elemento <head>. 
Head 
Es un contenedor de metadatos. No podemos verlo salvo que entremos en el código fuente de la 
página. 
Se coloca entre la etiqueta <html> y la etiqueta <body>. 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <meta name="description" content="Ejemplo de una etiqueta head en HTML5"> 
    <meta name="keywords" content="HTML5, head, ejemplo, meta tags"> 
    <meta name="author" content="Tu Nombre"> 
    <title>Ejemplo de Head en HTML5</title> 
    <link rel="stylesheet" href="styles.css"> 
    <link rel="icon" href="favicon.ico" type="image/x-icon"> 
    <script src="script.js" defer></script> 
</head> 
<body> 
    <h1>Contenido de la página</h1> 
</body> 
</html> 
Encabezados 
Se definen con las etiquetas <h1> hasta <h6>. Es decir, puede haber 6 encabezados. 
<h1> es el más importante (más grande) y <h6> el menos importante. 

<!-- Page 65 -->

 
 
Aplicaciones y desarrollo web 
65 
Ejemplo: 
<!DOCTYPE html> 
    <html> 
      <body> 
      <h1>Cabecera tipo 1</h1> 
      <h2>Cabecera tipo 2</h2> 
      <h3>Cabecera tipo 3</h3> 
      <h4>Cabecera tipo 4</h4> 
      <h5>Cabecera tipo 5</h5> 
      <h6>Cabecera tipo 6</h6> 
      </body> 
    </html> 
 
Respuesta del navegador 
Párrafos 
Los párrafos se definen con la etiqueta <p>. 
Enlaces HTML 
Los enlaces se definen con la etiqueta <a>. 
El destino del enlace se especifica con el atributo "href". Los atributos se utilizan para proporcionar 
información adicional sobre elementos HTML. 

<!-- Page 66 -->

 
 
Aplicaciones y desarrollo web 
66 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <body> 
       <a href="https://www.masterd.es/">Enlace a la página web de MasterD</a> 
       </body> 
     </html> 
 
Respuesta del navegador 
Si pulsamos en el enlace nos llevará a la página indicada. Otros atributos que puede tener el elemento 
<a> son: 
• Target: 
Se usa para definir dónde abrir el documento vinculado. Puede tener los siguientes valores: 
• _blank. Abre el documento vinculado en una nueva ventana o pestaña. 
• _self. Abre el documento vinculado en la misma ventana / pestaña en la que está el enlace 
(valor predeterminado). 
• _parent. Abre el documento vinculado en el marco (frame) principal. 
• _top. Abre el documento vinculado en el marco (frame) superior. 
• nombreFrame. Abre el documento vinculado en un marco con dicho nombre. 
• Id: 
Para definir marcadores dentro de la página. Para crear un enlace al identificador se utiliza <a 
href="#marcador">. 
Ejemplo: 
<h3 id="Cap1">Capítulo 1</h3> 
     <a href="#Cap1"> Volver al capítulo 1 </a> 

<!-- Page 67 -->

 
 
Aplicaciones y desarrollo web 
67 
Imágenes 
Para poder insertar una imagen en HTML, se definen con la etiqueta <img>. 
Puede tener varios atributos, como el archivo de origen (src), el texto alternativo (alt), la anchura 
(width) y la altura (height). 
El texto alternativo se mostrará cuando no pueda cargar la imagen (por ejemplo, porque no esté en esa 
ruta). 
 
 
 
 
Imprescindible 
Podemos utilizar <img> dentro de <a> para usar una imagen como \nenlace (accede al enlace al pinchar sobre la imagen). 
Ejemplo: 
<a href="https://www.masterd.es/"> 
<img src="https://imgcom.masterd.es/1/38125.jpg"> 
</a> 
 
 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <body> 
       <img src="https://imgcom.masterd.es/1/blog/2017/05/38125.jpg" alt="MasterD" 
width="500" height="200"> 
       </body> 
     </html> 

<!-- Page 68 -->

 
 
Aplicaciones y desarrollo web 
68 
 
Respuesta del navegador 
 
 
 
Importante 
En HTML5, con el atributo usemap indicamos el nombre del mapa 
de imágenes que queramos utilizar. 
La sintaxis es usemap="#nombremapa". 
 
Botones 
Los botones HTML se definen con la etiqueta <button>. 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <body> 
       <button>Haz click aquí</button> 
       </body> 
     </html> 
 
Respuesta del 
navegador 
Listas 
Hay dos tipos de listas: 
• Ordenadas. Utilizan la etiqueta <ol> (ordered list). 
• Desordenadas. Utilizan la etiqueta <ul> (unordered list). 

<!-- Page 69 -->

 
 
Aplicaciones y desarrollo web 
69 
Los elementos de la lista se añaden con la etiqueta <li>. 
<!DOCTYPE html> 
    <html> 
      <body> 
      <h3>Lista ordenada</h3> 
      <ol> 
      <li>HTML</li> 
      <li>CSS</li> 
      <li>JAVASCRIPT</li> 
      </ol> 
      <h3>Lista desordenada</h3> 
      <ul> 
      <li>HTML</li> 
      <li>CSS</li> 
      <li>JAVASCRIPT</li> 
      </ul> 
      </body> 
    </html> 
 
Respuesta del navegador 

<!-- Page 70 -->

 
 
Aplicaciones y desarrollo web 
70 
Comentarios 
Los comentarios en HTML tienen la siguiente sintaxis: 
<!-- comentario --> 
Los comentarios se utilizan como notas para el desarrollador, pero no se muestran en el navegador al 
cliente. 
Salto de línea 
Para introducir un salto de línea en el texto (retorno de carro de página utilizamos la etiqueta <br>) 
 
 
 
 
Atención 
No utilices <br> para incrementar el espacio entre líneas de texto; 
para ello utiliza<p> (o la propiedad margin de CSS). 
 
Línea de separación 
Para introducir una línea de separación utilizamos la etiqueta <hr>. 
Formatos de texto 
HTML utiliza diversos elementos para dar formato a un texto. Estos son: 
• <b>: 
Texto en negrita. 
• <strong>: 
Texto considerado importante, produce en el navegador el efecto de aplicar negrita. 
Obligatoriamente hay que definir el texto entre <strong> y </strong>. 

<!-- Page 71 -->

 
 
Aplicaciones y desarrollo web 
71 
• <i>: 
Texto en cursiva. 
• <em>: 
Texto enfatizado. 
• <mark>: 
Texto marcado. 
• <small>: 
Texto pequeño. 
• <del>: 
Texto tachado. 
• <u>: 
Utilizado para definir texto subrayado hasta HTML 4.01, actualmente se considera obsoleto. 
• <ins>: 
A partir de HTML5. 
Aunque el resultado es texto subrayado, su uso es para representar una parte del texto que 
debe ser estilísticamente diferente de texto normal. 
Se le da un uso para representar contenido que ha sido agregado al documento. Junto con el \nelemento <del>, permite indicar a los autores los cambios que se producen en el documento, lo 
que resulta muy útil para lectores que deben conocer los cambios que han sido aplicados a éste. 
 
 
 
 
+ Info 
También pueden usarse los atributos cite y datetime, para proveer 
información acerca de la actualización de un documento. 
cite contiene el URI del recurso que provee una explicación acerca 
de la actualización, y datetime puede aportar la fecha y hora en 
que los cambios se llevaron a cabo. 
 

<!-- Page 72 -->

 
 
Aplicaciones y desarrollo web 
72 
• <sub>: 
Texto de subíndice. 
• <sup>: 
Texto superíndice. 
 
 
 
 
+ Info 
Algunos navegadores, al presentar el texto, no distinguen entre: 
• <strong>y <b>. 
• <em>e <i>. 
 
 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <body> 
       <b>Texto en negrita</b><br> 
       <strong>Texto importante</strong><br> 
       <i>Texto en cursiva</i><br> 
       <em>Texto enfatizado</em><br> 
       <mark>Texto marcado</mark><br> 
       <small>Texto pequeño</small><br> 
       <del>Texto tachado</del><br> 
       <ins>Texto subrayado</ins><br> 
       Texto <sub>subíndice</sub><br> 
       Texto <sup>superíndice</sup><br> 
       </body> 
     </html> 

<!-- Page 73 -->

 
 
Aplicaciones y desarrollo web 
73 
 
Respuesta del navegador 
Tablas 
Una table se define con la etiqueta <table>. 
• <thead>: 
Sección de encabezado de una tabla. 
• <tr>: 
Definen cada fila de la tabla y encierran todas las columnas. Son parte de la sección de \nencabezado <thead>. 
• <td>: 
Define celdas de datos, aunque a veces se intrerpreta como que define cada una de las columnas 
de las filas. 
(HTML no define columnas sino celdas de datos). 
• <th>: 
Define una celda como el encabezado de un grupo de celdas en una tabla. 
Las celdas de encabezado están pensadas para proveer información de encabezado para las 
celdas de datos (td). 
• <tfoot>: 
Pie de una tabla. 
Veamos un ejemplo para entenderlo mejor. Vamos a crear una tabla con borde. 

<!-- Page 74 -->

 
 
Aplicaciones y desarrollo web 
74 
<!DOCTYPE html> 
     <html> 
       <head> 
       <style> 
       table, th, td { 
       border: 1px solid black; 
       } 
       </style> 
       </head> 
       <body> 
       <table style="width:100%"> 
       <tr> 
       <th>Nombre</th> 
       <th>Apodo</th> 
       <th>Edad</th> 
       </tr> 
       <tr> 
       <td>Miguel Ángel Nadal Homar</td> 
       <td>El loco</td> 
       <td>52</td> 
       </tr> 
       <tr> 
       <td>Robert Prosine?ki</td> 
       <td>Lesioneki</td> 
       <td>49</td> 
       </tr> 
       <tr> 
       <td>Uli Stielike</td> 
       <td>Tanque</td> 
       <td>63</td> 
       </tr> 
       </table> 
       </body> 
     </html> 

<!-- Page 75 -->

 
 
Aplicaciones y desarrollo web 
75 
 
Respuesta del navegador 
Secciones o bloques 
La etiqueta <div> se utiliza para definir una sección o bloque dentro de la página. 
De esa forma, podemos definir un formato distinto para dicha sección. 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <body> 
       <p>Texto fuera del bloque</p> 
       <div style="background-color:cyan;"> 
       <h3>Texto dentro del bloque</h3> 
       </div> 
       <p>Texto fuera del bloque</p> 
       </body> 
     </html> 
 
Respuesta del navegador 

<!-- Page 76 -->

 
 
Aplicaciones y desarrollo web 
76 
Marcos: frames e iframes 
Ambas etiquetas tienen una función muy similar, pero utilizan distinta tecnología, podemos decir que 
iframe ha reemplazado en HTML5 a la etiqueta frame ya obsoleta. 
La traducción literal de frame en español es marco, y es algo que realmente explica de manera clara su 
funcionalidad. Estas etiquetas permiten incrustar otras páginas o documentos HTML dentro de la 
página web en la que se encuentran. 
Otra de las diferencias fundamentales al margen de la obsolescencia es que la etiqueta frame requerirá 
de una etiqueta padre frameset que permitirá incrustar uno o más marcos en su interior como 
indicamos en el ejemplo que sigue. La etiqueta iframe por su lado no necesitará de etiqueta padre. 
La flexibilidad, el control del comportamiento del contenido incrustado y la seguridad evidencian la \nevolución de la etiqueta iframe frente a su antecesora. 
Ejemplo: 
Podemos crear un marco a la izquierda con el índice del contenido, y cuando pulsemos sobre uno de \nestos índices, se mostrará su contenido en el marco de la derecha, manteniendo el índice en el marco de 
la izquierda. 
Con <iframe> podemos crear un marco en el que cargar otra página web dentro de la principal. 
Entre sus etiquetas de inicio y cierre podemos escribir un texto que será mostrado en caso de que el 
navegador web no soporte frames. 
La sintaxis básica de estas etiquetas sería: 
<frameset> 
<frame src="pagina1.html"> 
<frame src="pagina2.html"> 
</frameset> 
 
<iframe src="ejemplo.html"></iframe> 
Por defecto, los marcos se muestran con un borde que permite redimensionarlos según necesitemos. 
Para crear un marco, se usa la etiqueta <frameset>, y dentro de ella insertaremos una etiqueta <frame> 
por cada marco que deseemos crear. 
También añadiremos la etiqueta <noframes>, cuyo contenido se mostrará en los navegadores web que 
no soportan frames. 

<!-- Page 77 -->

 
 
Aplicaciones y desarrollo web 
77 
Atributos de la etiqueta frame: 
Además de id, name y el resto de atributos estándar, existen otros aplicables: 
• Frameborder: 
Indica si se mostrará el border del frame o marco o no (1 | 0). 
• Marginheight: 
Margen entre el contenido del frame y sus bordes superior e inferior (en píxels). 
• Marginwidth: 
Margen entre el contenido del frame y sus bordes izquierdo y derecho (en píxels). 
• Noresize: 
Si indicamos este atributo el frame o marco no se podrá redimensionar (en HTML no hay que 
asignarle valor alguno, pero según las especificaciones de XHTML es necesario asignarle como 
valor el mismo nombre de dicho atributo). 
• Scrolling: 
Especifica si se mostrarán barras de desplazamiento en el frame, pudiendo tomar como valores 
auto (se mostrarán sólo en caso necesario para poder hacer scroll en el contenido del marco), 
no (no se mostrarán nunca) o yes (estarán siempre visibles). 
• Src: 
La URL que se cargará en el frame. 
Principales atributos para <iframe>: 
• Align: 
Alineación horizontal del iframe con respecto a la página. 
(Bottom | left | middle | right | top). 
• Height: 
Alto del iframe. 
• Marginheight: 
Margen entre el contenido del iframe y sus bordes superior e inferior (en píxels). 
• Marginwidth: 
Margen entre el contenido del iframe y sus bordes izquierdo y derecho (en píxels). 

<!-- Page 78 -->

 
 
Aplicaciones y desarrollo web 
78 
• Scrolling: 
Especifica si se mostrarán barras de desplazamiento en el iframe, pudiendo tener valor auto. 
(Se mostrarán sólo en caso necesario para poder hacer scroll en el contenido del marco), no (no 
se mostrarán nunca) o yes (estarán siempre visibles). 
• Src: 
La URL que se cargará en el frame. 
• Width: 
Ancho del iframe (en pixels o porcentaje). 
3.1.1.4. HTML5 
HTML y XHTML son las dos variantes que existen en el lenguaje HTML 5. 
Las diferencias entre ambas son básicamente sintácticas: 
• La sintaxis HTML está inspirada en la norma SGML (aunque no la cumple estrictamente). 
• La sintaxis XHTML está basada en la recomendación XML (aunque tampoco la cumple \nestrictamente). 
• Los documentos deben estar bien formados. 
• Los elementos que no estén vacíos necesitan etiqueta de cierre. 
• Los nombres de atributos y elementos deben ir en minúscula. 
• Todos los valores de atributos que sean numéricos deben ir entre comillas. (si no son 
valores numéricos no se exigen comillas). 
Es la última versión de HTML. Las nuevas características que incorpora son: 
• Geolocalización: 
A través del navegador es posible obtener la ubicación del usuario (con su consentimiento). 
• Arrastrar & Soltar: 
Ahora cualquier elemento web puede ser arrastrable. 
• Almacenamiento Local (local storage): 
Cada navegador cuenta ahora con la capacidad de almacenar información de una página web en 
un almacenamiento local. De esta forma se pueden reemplazar las cookies. 

<!-- Page 79 -->

 
 
Aplicaciones y desarrollo web 
79 
• Cache de Aplicación: 
Esta característica consiste en un conjunto de métodos que permiten al usuario acceder a 
nuestra aplicación web incluso estando sin conexión a Internet. 
• Web Workers: 
Cuando ejecutas código JavaScript, el navegador tiende a detener cualquier otro proceso de 
nuestra página hasta que nuestro script termina de ejecutarse. 
Con los web workers podemos crear un espacio dedicado a la ejecución de nuestros scripts sin 
afectar los demás procesos de nuestro sitio y de la computadora de nuestros usuarios. 
 
 
 
 
Atención 
Seguramente alguna vez te habrá salido un mensaje de Windows 
indicando que un script está tardando mucho y te pregunta si 
deseas pararlo. A veces incluso es necesario cerrar el navegador. 
Esto lo evitan los web workers. 
 
 
• Nuevos "Elementos Semánticos": 
HTML es un lenguaje que describe su funcionalidad lógica y estructural con etiquetas. 
Se han incluido nuevas etiquetas de carácter semántico que ayudan a definir la estructura, como 
<header>, <footer>, <nav> y <article>. 
Ejemplo: <footer>, para el pie de página. 
Una de las mejores ventajas es que buscadores web pueden más fácilmente encontrar nuestro 
sitio web y enlistarlo, gracias a que ahora estos saben en qué etiquetas encontrar la información 
más importante de nuestra página. 
• Nuevos controles para formularios que antes sólo eran posibles con JavaScript o CSS. 
• Podemos dibujar con etiquetas como <canvas>. 
• Elementos multimedia: 
Soporta vídeo y audio de forma nativa. 

<!-- Page 80 -->

 
 
Aplicaciones y desarrollo web 
80 
Existen nuevas etiquetas en HTML5 para mostrar vídeos, audio e imágenes. 
Esto permite que mostremos vídeo en nuestro sitio y este pueda visualizarse en cualquier 
navegador o dispositivo sin necesitar software adicional. 
• Se han modificado, eliminado etiquetas y atributos no necesarios: 
• Ya no es necesario el uso de comillas dobles en los atributos, siendo posible algo como: <div 
id=contenedor> Esto es un div</div>. 
• Etiqueta doctype simplificada. 
• No hay una sintaxis tan estricta y no es necesario cerrar las etiquetas vacías, por lo que 
<br> sería válido. 
• Eliminados los <frames>. 
• Las etiquetas html, head y body no son obligatorias. 
• Las etiquetas de tablas thead, tbody y tfoot no son obligatorias. 
Estructura HTML5 
HTML presenta una nueva estructura, como puedes ver en el siguiente gráfico: 
 
Fuente: https://commons.wikimedia.org/wiki/File:Html-5.png 

<!-- Page 81 -->

 
 
Aplicaciones y desarrollo web 
81 
WebM 
Es un formato multimedia abierto y libre desarrollado por Google y orientado para usarse con HTML5. 
Es un proyecto de software libre. 
Inicialmente pensado para ser utilizado con códec de vídeo VP8 (códec de vídeo de formato abierto) y \nel códec de audio Vorbis. 
Desde julio de 2013, el formato WebM es capaz de integrar los respectivos sucesores de video y audio 
de VP8 y Vorbis, que son VP9 y Opus.3. 
3.1.1.4.1. Elementos y atributos desaparecidos en HTML5 
La versión estandarizada de HTML, deja obsoletos los siguientes elementos: 
Etiquetas Obsoletas 
• Basefont: 
Usado para establecer un tamaño de fuente por defecto. 
• Big: 
Tamaño grande de texto. 
• Center: 
Centrar el contenido. 
• Font: 
Para establecer la fuente del texto. 
• Strike: 
Tachar texto. 
• Tt: 
Texto con fuente de teletipo. 
• Xmp: 
Texto preformateado. 
• Frame: 
Inserción de marcos. 

<!-- Page 82 -->

 
 
Aplicaciones y desarrollo web 
82 
• Frameset: 
Grupo de marcos. 
• Noframes: 
Contenido alternativo a marcos. 
• Acronym: 
Usado para representar acrónimos, sustituida por la etiqueta abbr. 
• Applet: 
Usado para insertar scripts externos. 
• Dir: 
Para listados. Usar etiqueta <ul>. 
• U: 
Texto subrayado. 
• Isindex: 
Posiciona un campo de texto en una página para buscar en el. 
Atributos obsoletos 
• Align: 
<caption>, <img>, <table>, <hr>,<div>, <h1..h6>,<p> 
• Alink: 
<body> 
• Background: 
<body> 
• Bgcolor: 
<body>, <table> <tr> <td> <th> 
• Clear: 
<br> 

<!-- Page 83 -->

 
 
Aplicaciones y desarrollo web 
83 
• Compact: 
<ol>, <ul> 
• Color: 
<basefont>, <font> 
• Border: 
<img>, <object> 
• Hspace: 
<img>,<object> 
• Link: 
<body> 
• Noshade: 
<hr> 
• Nowrap: 
<td>, <th> 
• Size: 
<basefont>, <font>, <hr> 
• Start: 
<ol> 
• Text: 
<body> 
• Type: 
<li> 
• Value: 
<li> 
• Vlink: 
<body> 

<!-- Page 84 -->

 
 
Aplicaciones y desarrollo web 
84 
• Width: 
<hr>, <pre>, <td>, <th> 
• Vspace: 
<img>, <object> 
3.1.1.4.2. Novedades en HTML5 
Elemento abbr 
Es la forma correcta de representar acrónimos, siglas o abreviaturas. 
Sustituye a <acronym> de HTML que se ha declarado obsoleto. 
Ejemplo: 
<abbr title="Técnico Auxiliar Informático">TAI</abbr> 
Etiquetas incorporadas en HTML5 
Vamos a ver algunas de las etiquetas más interesantes: 
• <aside>: 
Se usa para el contenido tangencial (sección con contenido no relacionado) al contenido 
principal de la página. 
Representa una sección de una web que consiste en información que no tiene que estar 
necesariamente relacionada con el contenido principal de la web, (no es necesario para su 
comprensión), es decir, que está indirectamente relacionada con el contenido principal del 
documento. (debe estar relacionado al contenido circundante). 
• <article>: 
Su uso es para incluir información que tiene sentido de forma independiente, como una noticia. 
Permite incluir dentro de ella header y footer. 
• <dialog>: 
Es una nueva etiqueta introducida en la versión HTML5. 

<!-- Page 85 -->

 
 
Aplicaciones y desarrollo web 
85 
Se utiliza para poder mostrar cuadros de diálogo por pantalla. 
Su uso permite mostrar mensajes por pantalla dentro de unos cuadros de dialogo (similares a los 
mostrados con alert). 
Sintaxis: 
<dialog open>Esto muestra un cuadro de diálogo</dialog> 
Opcionalmente se puede utilizar el atributo open, con este atributo el cuadro de diálogo está 
activo. 
• <details>: 
Sirve para representar información adicional en un menú que el usuario puede mostrar u ocultar. 
Podemos indicar si está abierto o cerrado con el atributo open (="open" para abierto). 
Si incluimos la etiqueta summary en su interior, podemos indicar en la parte superior un 
resumen de la información contenida. 
• <keygen>: 
Generar la clave con una RSA alogrithm. 
En criptografía, RSA (Rivest, Shamir y Adleman) es un sistema criptográfico de clave pública 
desarrollado en 1979. Es el primer y más utilizado algoritmo de este tipo y es válido tanto para 
cifrar como para firmar digitalmente. 
Su atributo keytype, especifica un tipo de clave a utilizar, puede tener diferentes valores. 
• RSA: 
Es el valor por defecto. 
Especifica un algoritmo de seguridad RSA. El usuario puede tener una selección de los 
puntos fuertes de claves RSA. 
• DSA: 
Especifica un algoritmo de seguridad DSA. El usuario puede tener una variedad de tamaños 
de clave DSA. 
• EC: 
Especifica un algoritmo de seguridad de la CE. El usuario puede tener una selección de los 
puntos fuertes de la CE. 

<!-- Page 86 -->

 
 
Aplicaciones y desarrollo web 
86 
• <header>: 
Para incluir información en la parte superior de la página o cabecera. 
Logos, títulos, descripciones, formularios de búsqueda, etc. 
Al usarla creamos secciones, y podemos crear tantas como queramos. 
• <summary>: 
Permite añadir un sumario en la etiqueta details (muestra información adicional de un elemento 
de la web). 
• <footer>: 
Va al final, como pie de página, está pensada para incluir información como email, contacto, 
ayuda, textos legales, etc. 
Se puede usar varias veces creando secciones. 
• <nav>: 
Su uso es incluir el menú principal de la página, que nos dara acceso al resto de páginas 
principales de un sitio web. 
Se recomienda usar solo una vez, aunque se puede usar las veces que queramos. 
• <progress>: 
Incluimos una barra de progreso. 
Usamos los atributos value y max. 
<progress value="33" max="100"></progress> 
• <section>: 
Para crear secciones y agrupar artículos relacionados entre sí (mismo tema etc.) 
 
 
 
 
+ Info 
También podemos utilizar la etiqueta <main> para especificar el 
contenido principal de la página. 
 

<!-- Page 87 -->

 
 
Aplicaciones y desarrollo web 
87 
Atributos 
• Atributo usemap: 
Para poder insertar una imagen en HTML, se definen con la etiqueta <img>. 
Puede tener varios atributos, como el archivo de origen (src), el texto alternativo (alt), la 
anchura (width) y la altura (height). 
Ya hemos visto en HTML como insertar una imagen y darle el formato de su área (alt), la 
anchura (width) y la altura (height). 
Además, en HTML5, con el atributo usemap indicamos el nombre del mapa de imágenes que 
queramos utilizar. 
La sintaxis es usemap="#nombremapa". 
• Atributo TARGET: 
El atributo TARGET nos permite mostrar el resultado de un enlace en el frame que queramos 
indicando el nombre de dicho frame. 
Vamos a ver valores que puede tomar el atributo TARGER y su significado especial: 
• TARGET="_blank". 
Fuerza que el documento referenciado por el enlace sea mostrado en una nueva ventana 
del navegador. 
• TARGET="_self". 
Usando este valor el documento enlazado será mostrado en el mismo frame o ventana 
donde está el enlace. Este valor es especialmente útil cuando se ha usado la etiqueta BASE 
para especificar un frame destino por defecto distinto del actual. 
• TARGET="_parent". 
Este valor provoca que el documento sea mostrado en el FRAMESET padre del frame 
actual. 
• TARGET="_top". 
Fuerza a que el enlace sea mostrado usando todo el espacio de la ventana del navegador 
destruyendo toda estructura deframes. Este valor debe ser usado siempre que creemos un \nenlace a una página externa a nuestro sitio web. 

<!-- Page 88 -->

 
 
Aplicaciones y desarrollo web 
88 
• Atributo role: 
Este atributo permite que las webs sean mucho más legibles para usuarios discapacitados. 
Podemos asignar los siguientes valores: 
• Main. 
• Secondary: parte secundaria del documento. 
• Navigation. 
• Banner: banners, logos, etc. 
• Contentinfo: para elementos que aportan información sobre el contenido de la página 
(autores, copyrights, legal…). 
• Definition: definiciones. 
• Note: notas adicionales. 
• Seealso: para información relacionada. 
• Search: para formularios de búsqueda. 
• Atributo required: 
En las versiones anteriores al Html5, cuando queríamos que alguno de los campos del formulario 
fuera rellenado obligatoriamente, era necesario realizar la comprobación de que no estuviera 
vacío después de que el usuario pulsara sobre el botón de envió de los datos. 
Pero en HTML5, la incorporación del atributo required, se puede comprobar que el campo ha 
sido rellenado antes incluso de pulsar ese botón de envío. 
En caso de que el usuario deje este campo en blanco, algunos navegadores mostrarán un 
mensaje de error, o colocarán el cursor de escritura en el primer campo vacío. 
Este atributo se coloca dentro de la etiqueta del input, a continuación del nombre del campo 
que deseamos que se rellene obligatoriamente. 
3.1.2. XSL 
XSL, siglas en inglés de eXtensible Stylesheet Language (Lenguaje extensible de hojas de estilo) 
Las hojas de estilo XSL se escriben en XML (un lenguaje de marca, que se usa para almacenar y 
transportar datos y que puede utilizarse tanto en front-end como en back-end. Se estudia más adelante \nen esta unidad). 

<!-- Page 89 -->

 
 
Aplicaciones y desarrollo web 
89 
XSL es un método de presentación de datos para documentos XML, análogo a CSS para HTML, pero 
XSL permite crear hojas de estilo más elaboradas. 
XSL se inspiró en DSSSL (lenguaje de estilo de SGML) y CSS, (lenguaje de estilo de HTML). 
Es una familia de lenguajes desarrollados por el World Wide Web Consortium que permiten describir 
cómo debe ser presentada la información contenida en un documento XML. 
 
 
 
 
+ Info 
Recomendaciones del W3C para el lenguaje XSL: 
• XSL Transformations (XSLT): estándar que permite 
transformar documentos XML de una sintaxis a otra. 
Especifica una definición de idioma para transformaciones 
de datos XML. XSLT se usa para transformar: 
• Documentos XML en documentos XHTML. 
• Documentos XML en otros documentos XML. 
• XSL Formatting Objects (XSL-FO): especifica el formato 
visual con el cual se quiere presentar el documento. 
• XML Path Language (XPath): permite buscar y acceder a 
los nodos del documento, así como seleccionar partes de \neste. 
 
3.1.3. CSS 
CSS: Cascading Style Sheets u hojas de estilo en cascada) 
CSS es un lenguaje usado para definir la presentación de un documento estructurado escrito en HTML o 
XML (y por extensión en XHTML). 
Son hojas de estilo, es decir, proporciona estilo a HTML, describe cómo se mostrarán los \nelementos HTML. 

<!-- Page 90 -->

 
 
Aplicaciones y desarrollo web 
90 
CSS tiene como objetivo, separar la estructura de un documento de su presentación. 
El W3C (World Wide Web Consortium) es el encargado de formular la especificación de las hojas de \nestilo que servirán de estándar para los agentes de usuario o navegadores. 
La información de estilo puede ser adjuntada como un documento separado o en el mismo documento 
HTML. En este último caso podrían definirse estilos generales en la cabecera del documento o en cada \netiqueta particular mediante el atributo "<style>". 
Hemos visto que en HTML podemos dar formato a muchos elementos, pero esto puede ser tedioso en 
páginas con mucho código o en portales de una empresa. Si todas las páginas deben tener un formato 
común, se deben usar las hojas de estilo. 
Con las hojas de estilo definimos el diseño que va a tener cada uno de los elementos. De esta forma, 
cuando insertemos un elemento, no necesitaremos añadir información del formato, ya que esta se le 
aplica directamente. 
Los documentos a los que se puede aplicar una hoja de estilos pueden ser HTML, XHTML, XLM, SVG etc. 
Esto es muy útil por varias razones fundamentales: 
• Ahorra tiempo. 
No hay que volver a escribir todos los formatos en cada elemento. 
• Evita fallos. 
Podemos equivocarnos y darles un formato distinto a dos elementos iguales (al estar trabajando 
con muchas páginas). Usando hojas de estilo conseguimos una imagen corporativa que se 
replicará en cada página que hagamos. 
• Mantenimiento. 
Si queremos modificar el formato de un elemento, bastaría con modificarlo en la hoja de estilo y 
se aplicaría sobre todas las páginas que la utilizan. 
 
 
 
 
+ Info 
CSS2 (Cascading Style Sheets level 2). 
Es una nueva versión del lenguaje CSS de HTML para poder ser 
usado con XML. Es más sencillo que XSL, por lo que es conveniente 
usarlo siempre que no sea necesaria una transformación. 
Permite describir el formato en el que queremos que aparezcan las \nentidades definidas en un documento. 
 

<!-- Page 91 -->

 
 
Aplicaciones y desarrollo web 
91 
3.1.3.1. Formas de agregar CSS a HTML 
CSS se puede agregar a los elementos HTML de tres maneras: 
• En línea: 
Utilizando el atributo "style" en los elementos HTML. 
• Interno: 
Creando un elemento <style> en la sección <head>. 
• Externo: 
Utilizando un archivo CSS externo. 
 
 
 
 
El experto opina 
Por norma general, se deben agregar de forma externa. 
De esta forma, si queremos modificar la hoja de estilos no 
tendremos que entrar en cada página para modificarla. 
Es aconsejable tener un repositorio con las hojas de estilo utilizadas 
que sea accesible desde las distintas páginas. 
 
En línea 
Un CSS en línea se usa para aplicar un estilo único a un solo elemento HTML. Un CSS en línea usa el 
atributo de estilo "style" de un elemento HTML. 
La sintaxis es la siguiente: 
<etiqueta style="propiedad:valor;"> 

<!-- Page 92 -->

 
 
Aplicaciones y desarrollo web 
92 
Algunas de las propiedades que puede aplicar este atributo son: 
Propiedad 
Descripción 
background-color 
Establece el color de fondo de la página. Se aplica sobre la etiqueta <body> 
color 
Especifica el color del texto 
font-family 
Indica la fuente del texto 
font-size 
Especifica el tamaño del texto 
text-align 
Indica la alineación del texto 
Ejemplo: 
<!DOCTYPE html> 
    <html> 
      <body style="background-color:Cyan;"> 
      <p style="text-align:center;">Texto centrado</p> 
      <p style="color:red;">Texto rojo</p> 
      <p style="color:blue;">Texto azul</p> 
      <p style="font-size:50px;">Texto grande</p> 
      <h1 style="font-family:Courier;">Fuente Courier</h1> 
      <h1 style="font-family:Verdana;">Fuente Verdana</h1> 
      </body> 
    </html> 
 
Respuesta del navegador 

<!-- Page 93 -->

 
 
Aplicaciones y desarrollo web 
93 
Interno 
Un CSS interno se usa para definir un estilo para una sola página HTML. Se define en la sección <head> 
dentro del elemento <style>. 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <head> 
       <style> 
       body {background-color: cyan;} 
       h1 {color: blue;} 
       p {color: red;} 
       </style> 
       </head> 
       <body> 
       <h1>Cabecera en azul</h1> 
       <p>Párrafo en rojo</p> 
       </body> 
     </html> 
 
Respuesta del navegador 
Externo 
La información de estilo está en un fichero externo. 
Para usar una hoja de estilo externa tenemos que agregar un enlace a la hoja en la sección <head>. 
Los ficheros de hojas de estilo tienen la extensión .css 

<!-- Page 94 -->

 
 
Aplicaciones y desarrollo web 
94 
Ejemplo: 
<!DOCTYPE html> 
     <html> 
       <head> 
       <link rel="stylesheet" href="hojaDeEstilos.css"> 
       </head> 
       <body> 
       <h1>Cabecera en azul</h1> 
       <p>Párrafo en rojo</p> 
       </body> 
     </html> 
 
Respuesta del navegador 
3.1.3.2. Selectores de CSS 
Los selectores se utilizan para delimitar a qué elementos de la página web queremos aplicar un 
determinado estilo, que será indicado en la propia sintaxis del selector. 
Al elemento (o elementos) al que aplica el selector CSS se le denomina sujeto del selector. 
Se indican en la cabecera del documento (<head>) 
 
 
 
 
+ Info 
Actualmente, existen muchos selectores, y para que los selectores 
funcionen correctamente, es necesario que los navegadores los 
sepan interpretar. Esta información se puede consultar en la \nespecificación del W3C. 
https://www.w3.org/TR/selectors-3/ 
 

<!-- Page 95 -->

 
 
Aplicaciones y desarrollo web 
95 
Existe una clasificación de cuatro tipos, basándose en la clasificación de su nombre, son: 
• selector CSS simple 
Los selectores simples son aquellos que solamente está formado por una única cadena de texto 
(no utiliza ningún combinador). 
Son selectores simples: 
• El selector universal (asterisco *) 
• El selector por tipo de elemento del DOM (div | p | article...,) 
• El selector de ID (almohadilla #) 
• El de pseudoclase (símbolo de dos puntos :) 
• El depseudoelemento 
• En la notación actual se indica mediante la repetición doble del símbolo de dos puntos :: 
• En la notación antigua o clásica de CSS2 los pseudoelementos también se representan 
como las pseudoclases: 
• El selector de clase . 
• El selector de atributo (a minúscula) 
• selector CSS compuesto 
Son aquellos formados por una cadena de selectores simples sin combinadores (excluyendo 
también el espacio en blanco por ser un combinador). 
Se incluyen en esta categoría aquellos que en su nombre tienen un selector de pseudoclase. 
• selector CSS complejo 
Los selectores complejos son una secuencia de selectores separados por combinadores. 
Los combinadores permiten delimitar mejor el efecto del selector (sobre qué elementos se 
aplicará). 
• una lista de selectores CSS 
Dos o más selectores de cualquier tipo separados por una coma , 
Para mejorar el uso de los selectores, y que su función sea más precisa, se utilizan los combinadores de 
selectores CSS, que aumentan la precisión del selector, al relacionar varios de ellos en función de que 
cumplan o no alguna o todas las condiciones definidas por el combinador. 

<!-- Page 96 -->

 
 
Aplicaciones y desarrollo web 
96 
Los combinadores pueden ser: 
• Signos gráficos. 
• Caracteres especiales. 
• Espacio en blanco. 
• Palabras o expresiones reservadas utilizadas en el nombre del selector. 
Indicamos a continuación algún combinador de selectores CSS: 
• Combinador barra vertical | 
La barra vertical '|' se emplea para acotar el sujeto del selector al "namespace" (espacio de 
nombre) indicado. 
• Combinador de columna de dos barras verticales || 
Selecciona las celdas pertenecientes a una columna dada. En caso de que una celda ocupase 2 o 
más columnas diferentes se verá afectado por cualquiera de éstas. 
(Es nuevo en el DOM Selectores de nivel 4 de W3C, para la accesibilidad) 
• Combinador "Para iluminar las sombras" /deep/ (renombrado recientemente como <<<) 
Este combinador es de reciente formulación. Se utiliza para poder "saltar la barrera" de \nencapsulamiento que existe con el uso de Shadow DOM. El combinador /deep/ atraviesa ese \nencapsulamiento, y se puede apuntar a los elementos creados o incluidos en el Shadow DOM. 
(Los descendientes de un host en la sombra no deben generar cuadros en el árbol de formato. 
En su lugar, el contenido del árbol de sombra activo genera cuadros como si fueran el contenido 
del elemento) 
Con este combinador, se pueden aplicar estilos desde el DOM principal al Shadow DOM.  
 
 
 
 
+ Info 
Puedes ampliar la información de este combinador en: 
https://drafts.csswg.org/css-scoping-1/#deep-combinato 
 

<!-- Page 97 -->

 
 
Aplicaciones y desarrollo web 
97 
3.1.3.3. Tipos de selectores de CSS 
Vamos a ver alguno de los tipos de selectores de CSS más utilizados. 
3.1.3.3.1. Selector universal asterisco * 
Este selector representa a cualquier elemento del DOM, por tanto, al ser utilizado como selector CSS se 
aplicará a cualquier elemento contenido en el documento. 
3.1.3.3.2. Selector de identificador único o ID '#' 
El selector de identificador único ID o #, se utiliza para seleccionar elementos definidos con un ID. El 
nombre debe ser idéntico, ya que es sensible a mayúsculas y minúsculas (tampoco se pueden utilizar \nespacios en blanco). 
El combinador que se utiliza es el símbolo almohadilla # 
Sintaxis: 
#nombreID{propiedades_estilo} 
3.1.3.3.3. Selector de clase 'E.E' 
Selecciona todos los elementos que tienen el atributo de class especificado. 
El combinador que se utiliza es el punto, seguido del valor que tenga el atributo class del elemento de 
HTML. 
Sintaxis: 
.ejemploclase{propiedades_estilo} 
Primero se declara la clase (class="ejemploclase") 
Así, el selector .ejemploclase afectará a todos los elementos del documento que tengan declarado 
class="ejemploclase". 
El uso de class admite valores múltiples, para ello hay que separarlos por un espacio en blanco. 

<!-- Page 98 -->

 
 
Aplicaciones y desarrollo web 
98 
Para seleccionar un elemento que tiene dos clases en su atributo, el selector se indica con mediante el 
punto y a continuación ambos valores sin espacio entre ellos. 
Por tanto, permite que en una misma página HTML varios elementos diferentes pueden utilizar el 
mismo valor en el atributo class. 
Hay que crear en el archivo CSS una nueva regla, con todos los estilos que se van a aplicar al elemento. 
Para que el navegador distinga este tipo de selector de otros, se coloca delante del atributo class un 
punto (.) 
Los selectores de clases son los más usados junto con los selectores de ID. 
Ejemplo: creamos la regla OTAI en CSS. 
Se aplicarán todos los estilos que definamos en OTAI a todos los elementos con atributo class="OTAI" 
definido en CSS. 
HTML: 
<!DOCTYPE html> 
    <html> 
      <body> 
      <span class="OTAI">Prueba Selectores CSS.</span> 
      <br> <br> con formato <br> <br> 
      <span class="OTAI">color rojo, marco verde grosor 1px, margen respecto al 
texto 4px</span> 
      </body> 
    </html> 
CSS: 
.OTAI {color: red;border: green 1px solid; margin: 10px; padding: 4px} 
RESULTADO: 
 

<!-- Page 99 -->

 
 
Aplicaciones y desarrollo web 
99 
Comparación entre selector ID y Clase 
La diferencia entre el selector de ID #, y el selector de clase . es que, en un documento HTML, solo se 
puede tener un elemento que pertenezca a un ID, y, en cambio, se pueden tener varios elementos que 
usen el mismo nombre de clase. (Un elemento HTML sólo puede tener un ID que pertenecerá a ese 
único elemento, y, sin embargo, varios elementos pueden usar un mismo nombre de clase). 
3.1.3.3.4. Selector de pseudo-clase 
Se utiliza para aplicar el estilo a los elementos que se encuentran en un estado específico. 
La sintaxis es: 
selector:estado{propiedades_estilo} 
Un mismo elemento puede verse afectado por varias pseudo-clases diferentes de forma simultánea, por \nejemplo, como comprobarás a continuación, viendo algunas psedo-clases, si se pulsa en un enlace que 
ha sido visitado, este tendrá las pseudo-clases :visited, :hover y :active. 
Esta posibilidad de varias pseudo-clases en un mismo elemento (y al comportamiento en cascacada de 
los estilos CSS), hace que sea importante tener en cuenta el orden en el que se establecen las diferentes 
pseudo-clases. 
Son pseudo-clases: 
• :hover 
El estilo se aplicará sobre el elemento solo cuando el usuario se desplace sobre ese elemento con \nel ratón. 
• :active 
El estilo se aplicará cuando el usuario presione el botón principal del ratón sobre el elemento, es 
decir, cuando activa un elemento. El tiempo es casi imperceptible, ya que dura solo desde que el 
usuario pulsa el botón del ratón hasta que lo deja de pulsar. 
• :focus 
El estilo se aplicará cuando el elemento tiene el foco del navegador (cuando está seleccionado). 
Se suele utilizar para los elementos <input> de los formularios cuando están activados y así, se 
puede escribir directamente en esos campos. 

<!-- Page 100 -->

 
 
Aplicaciones y desarrollo web 
100 
• :visited 
El estilo se aplicará a los enlaces que el usuario haya visitado. 
• :link 
El estilo se aplicará a los enlaces que el usuario no haya visitado. 
• :invalid 
El estilo se aplicará en los elementos cuyos contenidos no se puedan validar. 
• :first-child 
Selecciona el primer elemento hijo de un elemento. 
Puede utilizarse en los selectores simples. 
 
 
 
 
Comparativa 
Las pseudo-clases :hover, :active y :focus varian los estilos de un \nelemento en respuesta a las acciones del usuario, y pueden 
aplicarse a cualquier elemento. Las pseudo-clases :link y :visited 
sólo se pueden aplicar a los enlaces. 
 
 
• :lang 
La pseudo-clase se utiliza para poder seleccionar elementos en función de su idioma. 
Ya sabemos que los navegadores utilizan los atributos lang y las etiquetas <meta> para 
determinar el idioma de cada elemento. También utilizan esa pseudo-clase, por ejemplo, si 
tenemos el código (con un atributo lang que no tenga español como idioma): 
p { color: green; } 
p:lang(es) { color: red; } 
Los párrafos se ven de color verde, excepto los escritos en español, que se ven de color rojo. 

<!-- Page 101 -->

 
 
Aplicaciones y desarrollo web 
101 
Hay que diferenciar lo siguiente: 
• Si indicamos el selector *[lang|=es] serán seleccionados todos los elementos de la página 
que tengan un atributo llamado lang cuyo valor empiece por es. 
• Si indicamos el selector *:lang(es) serán seleccionados todos los elementos de la página 
cuyo idioma sea el español, sin tener en cuenta el método que el navegador utilice para 
saber el idioma de cada elemento. 
3.1.3.3.5. Pseudo-elemento 
Han sido definidos por CSS para poder aplicar estilos a determinados elementos especiales, como, por \nejemplo, cambiar el estilo de la primera línea de texto de un elemento, que normalmente es variable, ya 
que los usuarios pueden disponer de más o menos resolución en su monitor, y, además, pueden realizar 
varias cosas como, aumentar y disminuir la ventana del navegador o el tamaño de letra del texto. Para \nestos elementos especiales no es suficiente el uso de los elementos de HTML, los selectores de CSS y las 
pseudo-clases. 
Vamos a ver algunos pseudo-elementos: 
• :first-line 
Permite seleccionar la primera línea de texto de un elemento. Así, la siguiente regla CSS muestra \nen mayúsculas la primera línea de cada párrafo: 
Sólo se puede utilizar con los elementos de bloque y las celdas de datos de las tablas. 
Se pueden combinar varios pseudo-elementos de tipo :first-line para crear efectos avanzados, 
como por ejemplo una apariencia en mayúsculas y además de un determinado color. 
Ejemplo: 
p:first-line { text-transform: uppercase; } 
div:first-line { color: red; } 
• :first-letter 
Permite seleccionar la primera letra de la primera línea de texto de un elemento. De esta forma, 
la siguiente regla CSS muestra en mayúsculas la primera letra del texto de cada párrafo. 
También afecta a los signos de puntuación y los caracteres como las comillas que se encuentran 
antes y después de la primera letra. 
Este pseudo-elemento sólo se puede utilizar con los elementos de bloque y las celdas de datos 
de las tablas. 

<!-- Page 102 -->

 
 
Aplicaciones y desarrollo web 
102 
Ejemplo: 
p:first-letter { text-transform: uppercase; } 
• Los pseudo-elementos :before y :after 
Se utilizan en combinación con la propiedad content de CSS para añadir contenidos antes o 
después del contenido original de un elemento. 
Por ejemplo, las siguientes reglas CSS añadirán el texto Capítulo - delante de cada título de 
sección <h1> y el carácter punto . detrás de cada párrafo de la página: 
h1:before { content: "Capítulo - "; } 
p:after { content: "."; } 
El contenido insertado con :before y :after se tendrá en cuenta en los pseudo-elementos :first-
line y :first-letter. 
3.1.3.3.6. Selector de descendientes e f 
Las propiedades afectan a los elementos de una segunda etiqueta F contenidos dentro de una primera \netiqueta E, aunque haya etiquetas intermedias, es decir, que no importa los descendientes interpuestos \nentre E y F. 
El combinador que se utiliza es el espacio en blanco o el símbolo >> 
En el ejemplo siguiente, todos los párrafos <p> dentro de una división <div> se ven de color rojo. 
div p {color:red} 
 
 
 
 
Recuerda 
En una hoja de estilos CSS3, el estilo definido en el selector div + p 
(div p) se aplicará a todos los elementos situados justo después de 
un elemento <div> 
 

<!-- Page 103 -->

 
 
Aplicaciones y desarrollo web 
103 
3.1.3.3.7. Selector de hijos E>F 
Se utiliza para seleccionar un elemento que es hijo de otro elemento y se indica mediante el combinador 
> (signo de mayor que). 
Sintaxis: 
E>F{propiedades_estilo} 
Se aplicará el estilo indicado solamente a los elementos F contenidos directamente en E. La condición es 
F es hijo directo de E 
Ejemplo: 
p>span{ color: blue; } 
La condición es "cualquier elemento <span> que sea hijo directo de un elemento <p>" 
Veamos cómo afectará al siguiente código: 
<p> 
   <span>Texto1</span> 
<!-- se aplicará ya que se cumple la condición de ser hijo directo--> 
</p> 
<p> 
   <a href="#"> 
      <span>Texto2</span> 
<!-- no se aplicará, ya que no se cumple la condición. Es descendiente pero no es 
hijo directo de <p> --> 
   </a> 
</p> 
 

<!-- Page 104 -->

 
 
Aplicaciones y desarrollo web 
104 
 
 
 
Atención 
Diferencia entre selector de descendientes y selector de hijos: 
• El selector descendente sólo importa que un elemento esté 
dentro de otro, da igual los elementos interpuestos. 
• En el selector de hijos el elemento debe ser hijo directo de 
otro elemento. 
 
Comparación entre selector de descendientes y de hijos 
Aunque son similares, la condición tiene una diferencia: 
• El selector descendente sólo importa que un elemento esté dentro de otro, da igual los \nelementos interpuestos.  
• En el selector de hijos el elemento debe ser hijo directo de otro elemento. 
Ejemplo: 
p a{color: red;} //selector de descendientes 
p>a{font-weight;} //selector de hijo 
Veamos cómo afectará al siguiente código: 
<p> 
  <a href="#">Enlace1</a> 
</p> 
<p> 
  <span> 
    <a href="#">Enlace2</a> 
  </span> 
</p> 

<!-- Page 105 -->

 
 
Aplicaciones y desarrollo web 
105 
El selector descendente (p a) se aplicará a todos los elementos <a> que se encuentran dentro de \nelementos <p> por lo que en este ejemplo a los dos enlaces (Enlace1 y Enlace2). 
El selector de hijos obliga a que se cumpla que el elemento <a> sea hijo directo de un elemento <p>, por 
lo que en este ejemplo no se aplicará al segundo enlace (Enlace2). 
3.1.3.3.8. Selector de consecutivos: E+F (Adyacente) 
Se utiliza el combinador + para indicar la obligatoriedad de que F sea hermano de E (que ambos estén 
contenidos directamente dentro del mismo elemento, mismo padre) y, además, estén subyacentes, es 
decir, deben aparecer inmediatamente después de cerrar el elemento E (no puede haber otro hermano 
que se interponga o que los separe). 
En este caso sí que importa que haya otros elementos hermanos interpuestos, lo que no sucede en el 
selector de hermanos ~). 
Sintaxis: 
E+F{propiedades_estilo} 
El selector adyacente se emplea para seleccionar elementos que son hermanos (su elemento padre es el 
mismo) y están seguidos en el código HTML. Este selector emplea en su sintaxis el símbolo + 
Ejemplo: 
h1+h2{color:blue} 
Veamos cómo afectará al siguiente código: 
<body> 
<h1>Titulo1</h1> 
<h2>Subtítulo</h2> 
<!-- se aplicará ya que se cumple la condición de que h1 y h2 son hermanos, y 
también de que h2 es adyacente a h1--> 
... 
<h2>Otro subtítulo</h2> 
<!-- NO se aplicará ya que, aunque se cumple la condición de que h1 y h2 son 
hermanos, no se cumple la segunda condición de que sea adyacente, no aparece 
después de h1--> 
... 
</body> 

<!-- Page 106 -->

 
 
Aplicaciones y desarrollo web 
106 
3.1.3.3.9. Selector de hermanos: E~F 
Se utiliza el combinador virgulilla ~ para indicar la obligatoriedad de que F sea hermano de E , es decir, 
que ambos contenidos directamente dentro del mismo elemento, sin importar que haya otros \nelementos hermanos interpuestos. 
Sintaxis: 
E~F{propiedades_estilo} 
Ejemplo: 
h4~p {color:blue;} 
Veamos cómo afectará al siguiente código: 
<article> 
    <h4>título</h4> 
    <p>texto párrafo1</p> 
    <img src='...' /> 
    <p>texto párrafo2</p> 
</article> 
El selector afectará por igual a los dos párrafos (texto párrafo1 y texto párrafo2), puesto que ambos 
son hermanos contenidos directamente en el mismo elemento <article> (como padre). 
3.1.3.3.10. Selector de atributo a (letra a minúscula) 
Estos selectores se han creado para seleccionar todos los elementos que correspondan con un atributo \nespecífico, o que correspondan con un valor definido de atributo. 
De esta forma es muy sencillo crear reglas CSS para modificar un estilo a todos los elementos que 
tengan un valor determinado, por ejemplo, cambiar el estilo de los elementos que contengan master.d \nen su URL, utilizando a[href*="master.d"]. (Si indicáramos a[href] se elegirían todos los enlaces para 
aplicar el estilo). 

<!-- Page 107 -->

 
 
Aplicaciones y desarrollo web 
107 
También se puede utilizar un espacio de nombre combinándolo con este selector para restringir la 
búsqueda a elementos que estén dentro de ese espacio. 
Hay diferentes posibilidades de uso de este selector de atributo, en función de si se desea seleccionar 
los elementos que tienen atributos coincidentes con un valor específico, indicamos algunas de ellas, con 
las cuales se seleccionara a todos los elementos que tengan establecido el atributo llamado 
nombre_atributo, y, que además, cumplan la condición que establezca la opción elegida: 
• a[nombre_atributo] {propiedades de estilo} 
todos, independientemente de su valor. 
• a[nombre_atributo=value] {propiedades de estilo} 
y, cuyo valor sea igual a value. (Distingue entre mayúsculas y minúsculas). 
• a[nombre_atributo~=valor] {propiedades de estilo} 
y, cuyo valor es una lista de palabras separadas por espacios en blanco en la que al menos una de \nellas es exactamente igual a valor. 
• a[nombre_atributo|=valor] {propiedades de estilo} 
y, cuyo valor tenga exactamente el valor value o empiece por value seguido de un guión - 
(U+002D). 
Este tipo de selector sólo es útil para los atributos de tipo lang que indican el idioma del contenido del \nelemento. 
Se puede usar para coincidencias de subcódigos en otros idiomas. 
• a[nombre_atributo ^=value] {propiedades de estilo} 
y, tenga un valor prefijado por value. 
• a[nombre_atributo$=value] {propiedades de estilo} 
y, cuyo valor tiene el sufijo (seguido) de value. 
• a[nombre_atributo*=value] {propiedades de estilo} 
y, cuyo atributo attr tenga un valor que contenga value. 
Ejemplo: Queremos que todos los links que contengan la palabra master.d aparezcan con un color de la 
URL naranja, ya que es el color corporativo. 

<!-- Page 108 -->

 
 
Aplicaciones y desarrollo web 
108 
El código será: 
<!DOCTYPE html> 
<html> 
<head> 
<style> 
a[href*="masterd"] { 
    background-color: orange;} 
</style> 
</head> 
<body> 
<ul> 
    <li><a href="http://pilucatomas">pilufacetica</a></li> 
    <li><a href="http://www.masterd.es/">master.com</a></li> 
    <li><a href="https://www.masterd.es/oposiciones-tecnicos-auxiliares-
informatica">OTAI.com</a></li> 
    <li><a href="http://pilufacetica.com">autentica piluca</a></li> 
</ul> 
</body> 
</html> 
El resultado obtenido será: 
 
Vemos ahora otros ejemplos: 
• Selecciona todos los elementos de la página cuyo atributo "lang" sea igual a "en", es decir, todos 
los elementos en inglés. 
*[lang=en] { ... } 

<!-- Page 109 -->

 
 
Aplicaciones y desarrollo web 
109 
• Selecciona todos los elementos de la página cuyo atributo "lang" empiece por "es", es decir, "es", 
"es-ES", "es-AR", etc.  
*[lang|="es"] { color : red } 
• Se muestran de color naranja todos los enlaces que tengan un atributo "class", 
independientemente de su valor.  
a[class] { color: orange; } 
• Se muestran de color rojo todos los enlaces que tengan un atributo "class" con el valor 
"externo".  
a[class="externo"] { color: red; } 
• Se muestran de color verde todos los enlaces que apunten al sitio "http://www.piluca.com" . 
a[href="http://www.piluca.com"] { color: green; } 
• Se muestran de color azul todos los enlaces que tengan un atributo "class" en el que al menos 
uno de sus valores sea "externo". 
a[class~="externo"] { color: blue; } 
3.1.3.3.11. Otros selectores 
Vamos a indicar muy brevemente otros combinadores de CSS: 
• Combinador | 
Se utiliza para acotar el sujeto del selector al "namespace" (espacio de nombre) indicado. 

<!-- Page 110 -->

 
 
Aplicaciones y desarrollo web 
110 
• Combinador de columna || 
Representado por dos barras verticales, selecciona las celdas pertenecientes a una columna 
dada. 
3.1.3.4. Lista de selectores 
Si tenemos varios elementos que utilizan el mismo CSS (el mismo estilo), podemos combinar los 
selectores en una lista (separando los selectores con una coma) para que la regla se aplique a todos \nellos, (en lugar de especificar la regla en cada uno de los selectores). 
Si tenemos el mismo estilo CSS para un h1 y para una clase .special, los podemos escribir: 
• Como dos reglas separadas: 
h1{color: blue} 
.special{color: blue} 
Combinar en una lista de selectores, separándolos con una coma. 
h1,.special{color: blue} 
Se puede dejar un espacio en blanco antes y después de la coma, para que resulte más legible, y también 
se puede indicar cada selector en una línea distinta. 
El inconveniente de indicar los selectores agrupados en una lista, es que, si alguno de ellos no es válido, \nel navegador ignora toda la regla. 
3.1.3.5. Especificidad en CSS 
La especificidad en CSS es una regla que determina qué estilo se aplica cuando múltiples selectores 
apuntan al mismo elemento. Se calcula considerando el número de selectores de tipo (como input), 
selectores de clase o pseudo-clases (:hover), y selectores de ID en un formato jerárquico. 
Aparece con el CSS2 y se trata de un método para calcular la prioridad de las reglas de formateo en 
función de los selectores, anteriormente se resolvía de manera secuencial. 

<!-- Page 111 -->

 
 
Aplicaciones y desarrollo web 
111 
Se establece en base al selector un órden de prioridades a-b-c-d en el que prevalecen los estilos en línea, 
seguidos de selectores de identificador, posteriormente las clases/pseudoclases/atributos y por último 
los selectores genéricos o pseudo elementos. 
En ocasiones podemos encontrar que los estilos en línea son obviados, empezando en ese caso la 
ordenación en los selectores ID y acabando en los selectores de tipo y pseudoelementos siendo solo a, 
b, c. 
a (identificadores en línea): Se incrementa por reglas CSS aplicadas directamente en el atributo style de 
un elemento. 
b (selectores ID): Se incrementa por cada ID presente en el selector. 
c (selectores de clase, atributos y pseudoclases): Se incrementa por cada clase, selector de atributo 
([attr]) o pseudoclase (:hover, :nth-child, etc.). 
d (selectores de tipo y pseudoelementos): Se incrementa por cada elemento (como div, p) o 
pseudoelemento (::before, ::after). 
A continuación ponemos un ejemplo completo. 
<style>  
   div {color: red; } /* (0, 0, 0, 1) */ 
   .clase {color: blue; } /* (0, 0, 1, 0) */ 
   #id {color: green; } /* (0, 1, 0, 0) */ 
   input#nombre.calle{color:yellow} /* (0, 1, 1, 1) */ 
   input#nombre.calle[type=text] { color:orange } /* (0, 1, 2, 1) */ 
   input#nombre.calle[type=text]:hover {color:violet} /* (0, 1, 3, 1) */ 
</style> 
3.1.3.6. Unidades de Medida CSS 
Unidades Absolutas 
• px, píxeles, unidad básica en plantillas. 
• q, cuarto de milímetro (0.25 mm) -usado en impresión. 
• mm, milímetros. 

<!-- Page 112 -->

 
 
Aplicaciones y desarrollo web 
112 
• cm, centímetros. 
• in, pulgadas. 
• pt, puntos tipográficos (1pt = 1/72 pulgadas). 
• pc, picas (1pc = 12pt). 
Unidades relativas 
• em, relativo al tamaño de la fuente del elemento padre. 
• rem, relativo al tamaño de la fuente de la raíz (generalmente <html>). 
• ex, altura de la letra "x" en la fuente actual. 
• ch, anchor del carácter "0" en la fuente catual. 
• %, relativo al valor de su elemento contenedor. 
Basadas en el ViewPort 
• vw, 1% del ancho del viewport. 
• vh, 1% de la altura del viewport. 
• vmin, 1% de la dimensión menor del viewport (ancho o altura). 
• vmx, 1% de la dimensión mayor del viewport (ancho o altura). 
Basadas en el Contenedor 
• lvw, 1% del ancho del viewport grande (large viewport). 
• svw, 1% del ancho del viewport pequeño (small viewport). 
• dvw, 1% del ancho dinámico del viewport (dynamic viewport). 
Unidades de tiempo 
• s, segundos. 
• ms, milisegundos. 

<!-- Page 113 -->

 
 
Aplicaciones y desarrollo web 
113 
Unidades de ángulo 
• deg, grados (1 círculo: 360º). 
• rad, radianes (1 círculo: 2&pi; radianes). 
• grad, grados centesimales (1 círculo: 400 gradianes). 
• turn, vueltas completas (1 círculo: 1 vuelta). 
Unidades de Frecuencia 
• Hz, hercios, número de ciclos por segundo. 
• kHz, kilohercios (100 hercios). 
Densidad de píxeles en imágenes y medios 
• dpi, puntos por pulgada. 
• dpcm, puntos por centímetro. 
• dppx, píxeles por unidad CSS (1 dppx = 96 dpi). 
3.1.3.7. CSS Flexible Box Layout Flexbox 
Con el uso de los dispositivos móviles y sus características, (tamaños de pantalla variables, el cambio de 
formato de visualización al inclinarlos), no se puede realizar un diseño de cajas rígidas con un buen 
resultado. 
Por ello se utiliza el CSS Flexible Box Layout, (diseño de caja flexible CSS) o flexbox, donde el diseño se 
adapta de forma flexible a la pantalla donde se muestra, siguiendo el concepto del diseño receptivo. 
Con CSS Flexible Box, las cajas flexibles se distribuyen automáticamente en la página, pero existen 
muchas opciones para permitir al diseñador modificar y adaptar la disposición. 
Flexbox se basa en un contenedor flexible (flex container), que otorga sus propiedades a los elementos 
que contiene, (contiene varios elementos flexibles (flex ítems o flexboxes). Es decir, flexboxes deben su 
flexibilidad al hecho de estar dentro del contenedor. 
Para una correcta visualización, donde el espacio se llena o los elementos se desplazan de modo que 
todo permanezca visible, flexbox funciona con dos ejes, mediante los cuales se logra que los elementos 
se organizan dentro de la caja y se distribuyen en relación unos con otros, una vez hecha esa 
distribución, CSS Flexbox garantizar que el espacio que hay alrededor de estos elementos se llene 
correctamente. 

<!-- Page 114 -->

 
 
Aplicaciones y desarrollo web 
114 
Estos ejes siguen una dirección, y son: 
• El eje principal, que suele ser el horizontal. 
Va de izquierda a derecha. 
• Y el eje transversal o vertical. 
Va de arriba abajo. 
 
 
 
 
+ Info 
Flexbox se describe como un sistema unidimensional, donde los \nelementos se pueden organizar en filas o columnas, y nunca se 
pretende combinar ambas. 
El estándar es en filas, si se elige esa opción, CSS Flexbox intentará 
organizar todos los elementos en una sola fila, aunque también es 
posible evitarlo y forzar un salto de línea. 
 
La propiedad display: flex habilita la flexbox. 
Si no se define una posición, los elementos se distribuyen de izquierda a derecha. Y para indicar una 
posición determinada tenemos cinco opciones distintas, configurables con el comando justify-content: 
• flex-start: justificado a la izquierda. 
• flex-end: justificado a la derecha. 
• center: justificado en el centro. 
• space-around: distribuye uniformemente el espacio alrededor de las cajas. 
• space-between: distribuye uniformemente el espacio entre las cajas. 
Aunque el modelo CSS Flexbox parte de la alineación horizontal, también se puede invertir la dirección, 
de izquierda a derecha o de abajo a arriba, utilizando el comando flex-direction: 
• row: de izquierda a derecha. 
• row-reverse: de derecha a izquierda. 
• column: de arriba abajo. 
• column-reverse: de abajo a arriba. 

<!-- Page 115 -->

 
 
Aplicaciones y desarrollo web 
115 
 
 
 
Conclusiones 
Diferencias: 
• justify-content: flex-end. 
Se ajusta el último elemento al borde derecho. 
• flex-direction: row-reverse. 
El primer elemento del código aparece en el borde derecho. 
 
3.1.3.8. Preprocesadores CSS 
Los preprocesadores CSS son programas que sirven como herramientas para poder añadir algunas 
características que no existen en CSS, como son selectores anidados, condiciones, variables etc. 
Con los preprocesadores CSS, podemos traducir hojas de estilo comunes a un código estándar y 
reconocible por los navegadores, economizando tiempo al escribir menos código, y mejorando la 
legibilidad y el mantenimiento. Sin embargo, también implica conocer un nuevo lenguaje que debe ser 
compilado en CSS, hay que instalar un compilador CSS en tu web server. 
Algunos de los preprocesadores CSS principales son: 
• LESS. 
• SASS. 
• Stylus. 
• PostCSS. 
3.1.4. JavaScript 
 
Fuente: Wilkimedia Commons 

<!-- Page 116 -->

 
 
Aplicaciones y desarrollo web 
116 
JavaScript (JS) es un lenguaje de programación cuyo objetivo es que las páginas HTML sean 
dinámicas e interactivas, sin su uso las páginas son estáticas. 
JavaScript es un lenguaje de programación interpretado, dialecto del estándar ECMAScript. Se define 
como orientado a objetos, basado en prototipos, imperativo, débilmente tipado y dinámico. 
Es un lenguaje en Front-End, es decir en el Navegador Web del Cliente, del lado del cliente, ya que es 
implementado como parte de un navegador web permitiendo mejoras en la interfaz de usuario y 
páginas web dinámicas. 
 
 
 
 
+ Info 
JavaScript del lado del servidor (Server-side JavaScript o SSJS). 
El desarrollo en JavaScript del lado del servidor se hace instalando \nen el servidor herramientas que permiten el uso de JavaScript del 
lado del servidor como Node. Js, que es quizás la herramienta más 
utilizada dentro de los desarrollos que usan JavaScript del lado del 
servidor. 
 
 
Características destacadas de JS: 
• Imperativo y estructurado. 
Paradigma de programación imperativo (o procedimental), ya que utiliza un conjunto de 
instrucciones que se ejecutan una por una, de principio a fin, de modo secuencial, aunque este 
flujo puede ser modificado por instrucciones de salto o de control. 
• Compatibilidad con estructuras de C. 
JavaScript es compatible con gran parte de la estructura de programación de C como sentencias 
if, bucles for, sentencias switch, etc. 
JavaScript no es compatible con el hecho de que, en C, el ámbito de las variables alcanza al 
bloque en el cual fueron definidas, pero en JavaScript el ámbito de las variables es el de la 
función en la cual fueron declaradas. A partir de la versión ECMAScript 2015, esto cambia, ya 
que se añade compatibilidad con block scoping por medio de la palabra clave "let". 

<!-- Page 117 -->

 
 
Aplicaciones y desarrollo web 
117 
Al igual que en C, JavaScript hace distinción entre expresiones (combinación de constantes, 
variables o funciones, que es interpretada de acuerdo a las normas particulares de precedencia y 
asociación) y sentencias. 
También hay que destacar una diferencia sintáctica con respecto a C, que es la inserción 
automática de punto y coma, en JavaScript los puntos y coma que finalizan una sentencia 
pueden ser omitidos. 
• Tipado dinámico. 
El tipo está asociado al valor, no a la variable. 
Un sistema de tipos clasifica los valores y las expresiones en tipos, cómo se pueden manipular \nestos tipos y cómo interactúan. 
Por ejemplo, una variable "x" en un momento dado puede estar ligada a un número y más 
adelante, cambiar a una cadena de caracteres. 
JavaScript es compatible con varias formas de comprobar el tipo de un objeto, incluyendo duck 
typing (se conoce como duck typing o tipado pato el estilo de tipificación dinámica de datos en 
que el conjunto actual de métodos y propiedades determina la validez semántica, en vez de que 
lo hagan la herencia de una clase en particular o la implementación de una interfaz específica). 
Una forma de saberlo es por medio de la palabra clave typeof, que devuelve el tipo de operando 
al que se aplica, como, por ejemplo: 
• string: para una cadena de tipo variable. 
• number: para una variable que contiene un valor entero o de coma flotante. 
• boolean: para una variable que contenga valores true o false, typeof devuelve booleano. 
• undefined: para variables no declaradas, caso de que no asignemos valores a una variable. 
• object: para variables que contienen un array, o un objeto en {}, o variables asignadas con 
valor null, que son consideradas por JavaScript como un objeto. 
• function: cuando el tipo de la variable tiene asignadas funciones. (JavaScript permite 
asignar funciones a una variable). 
• Objetual. 
JavaScript casi en su totalidad está formado por objetos. Los objetos en JavaScript son como 
arrays asociativos (es un array cuyos índices no son numéricos sino cadenas de texto (claves), 
mejorados con el uso de prototipos. 
Realmente en JavaScript no existen arrays asociativos, pero son simulados creando objetos y 
accediendo a sus propiedades. 

<!-- Page 118 -->

 
 
Aplicaciones y desarrollo web 
118 
Los nombres de las propiedades de los objetos son claves de tipo cadena, y las propiedades y sus 
valores pueden ser creados, cambiados o eliminados en tiempo de ejecución. 
Casi todas las propiedades de un objeto (y también aquellas que son incluidas por la cadena de 
la herencia prototípica) pueden ser enumeradas por medio de la instrucción de bucle for… in. 
JavaScript utiliza lo denominado "azúcar sintáctico" para que las construcciones más fáciles de \nexpresar o leer, de forma que obj.x = 10 es equivalente a obj ['x'] = 10, resultando más fácil la 
notación con punto. 
• Funciones de primera clase. 
En JavaScript, las funciones son objetos de primera clase, es decir, son objetos en sí mismos, que 
poseen propiedades y métodos, y se pueden manipular y transmitir al igual que cualquier otro 
objeto. 
Una función anidada es una función definida dentro de otra, se crea cada vez que la función \nexterna es invocada. 
Cada función creada forma una clausura. 
Clausula o cerradura (del inglés closure) es un registro que contiene una función junto con el 
ámbito donde fue declarada (partes del programa donde una entidad puede ser usada). La 
clausura permite que la función acceda a los valores de las variables declaradas en el mismo 
ámbito, aun cuando la invocación ocurra fuera de este. 
El resultado de la evaluación de dicha clausura forma parte del estado interno de cada objeto 
función, incluso después de que la función exterior concluya su evaluación. 
• Prototípico. 
JavaScript usa prototipos en vez de clases para el uso de herencia. 
Los objetos no son creados mediante la instanciación de clases sino mediante la clonación de 
otros objetos o mediante la escritura de código por parte del programador. De esta forma los 
objetos ya existentes pueden servir de prototipos para los que el programador necesite crear. 
JavaScript es un lenguaje muy amplio. Veremos lo más destacado. 
Para añadir código JavaScript en un documento HTML se utiliza la etiqueta: 
<script> 
El elemento <script> puede contener: 
• Instrucciones de JavaScript. 
• La dirección de un archivo script externo con extensión .js que contiene el código JavaScript. 

<!-- Page 119 -->

 
 
Aplicaciones y desarrollo web 
119 
Los usos más comunes para JavaScript son: 
• Manipulación de imágenes. 
• Validación de formularios. 
• Cambios dinámicos de contenido. 
Para seleccionar un elemento HTML, JavaScript muy a menudo usa el método 
document.getElementById() 
Ejemplo: 
Primero, vamos a crear un elemento párrafo vacío al que llamaremos "demo". A continuación, a través 
de JavaScript, le asignaremos el valor de la fecha actual y le daremos formato. 
Finalmente, crearemos tres botones que cambiarán cada uno de ellos un tipo de formato. 
<!DOCTYPE html> 
     <html> 
       <body> 
         <p id="demo"></p> 
       <script> 
       document.getElementById("demo").innerHTML = Date(); 
       document.getElementById("demo").style.fontSize = "25px"; 
       document.getElementById("demo").style.color = "red"; 
       document.getElementById("demo").style.backgroundColor = "yellow"; 
       </script> 
       <button type="button" 
onclick="document.getElementById('demo').style.fontSize = '50px' "> 
        Tamaño</button> 
       <button type="button" onclick="document.getElementById('demo').style.color 
= 'orange' "> 
        Color texto</button> 
       <button type="button" 
onclick="document.getElementById('demo').style.backgroundColor = 'cyan' "> 
        Color fondo</button> 
       </body> 
     </html> 

<!-- Page 120 -->

 
 
Aplicaciones y desarrollo web 
120 
Al abrirlo en el navegador, nos muestra lo siguiente: 
 
Respuesta del navegador 
Si pulsamos el botón "tamaño", este cambiará: 
 
Respuesta del navegador 
Si pulsamos el botón "Color texto" cambiará el color de este: 
 
Respuesta del navegador 
Finalmente, si pulsamos el botón "Color fondo", mostrará: 
 
Respuesta del navegador 
3.1.4.1. Atributos de eventos 
Estos atributos se utilizan para realizar acciones dinámicas sobre los elementos de la página. 
Cada vez que el usuario pulsa una tecla, mueve su ratón o pulsa cualquier botón del ratón, se produce 
un evento dentro del navegador. Utilizando los siguientes atributos JavaScript, se responde de forma 
adecuada a cada evento. 

<!-- Page 121 -->

 
 
Aplicaciones y desarrollo web 
121 
Atributo 
Descripción 
Elementos que pueden usarlo 
onblur 
Deseleccionar el elemento 
<button>, <input>, <label>, <select>, 
<textarea>, <body> 
onchange 
Deseleccionar un elemento que se ha 
modificado 
<input>, <select>, <textarea> 
onclick 
Pinchar y soltar el ratón 
Todos los elementos 
ondblclick 
Pinchar dos veces seguidas con el ratón 
Todos los elementos 
onfocus 
Seleccionar un elemento 
<button>, <input>, <label>, <select>, 
<textarea>, <body> 
onkeydown 
Pulsar una tecla (sin soltar) 
Elementos de formulario y <body> 
onkeypress 
Pulsar una tecla 
Elementos de formulario y <body> 
onkeyup 
Soltar una tecla pulsada 
Elementos de formulario y <body> 
onload 
La página se ha cargado completamente 
<body> 
onmousedown 
Pulsar (sin soltar) un botón del ratón 
Todos los elementos 
onmousemove 
Mover el ratón 
Todos los elementos 
onmouseout 
El ratón "sale" del elemento (pasa por encima 
de otro elemento) 
Todos los elementos 
onmouseover 
El ratón "entra" en el elemento (pasa por \nencima del elemento) 
Todos los elementos 
onmouseup 
Soltar el botón que estaba pulsado en el ratón 
Todos los elementos 
onreset 
Inicializar el formulario (borrar todos sus datos) 
<form> 
onresize 
Se ha modificado el tamaño de la ventana del 
navegador 
<body> 
onselect 
Seleccionar un texto 
<input>, <textarea> 
onsubmit 
Enviar el formulario 
<form> 
onunload 
Se abandona la página (por ejemplo al cerrar el 
navegador) 
<body> 

<!-- Page 122 -->

 
 
Aplicaciones y desarrollo web 
122 
3.1.4.2. Comparaciones en JavaScript 
En JavaScript, se realizan comparaciones, viendo si los valores, son iguales, diferentes, mayores, 
menores, etc., para poder realizar acciones. 
Características de las comparaciones 
• Dos cadenas son estrictamente iguales cuando tienen la misma secuencia de caracteres, la 
misma longitud y los mismos caracteres en las posiciones correspondientes. 
• Dos objetos distintos nunca son iguales para comparaciones estrictas o abstractas. 
• Dos números son estrictamente iguales cuando son numéricamente iguales (tienen el mismo 
valor numérico). NaN no es igual a nada, incluido NaN. Los ceros positivos y negativos son 
iguales entre sí. 
• Dos operandos booleanos son estrictamente iguales si ambos son true o ambos son false. 
• Una expresión que compara objetos solo es verdadera si los operandos hacen referencia al 
mismo objeto. 
• Los tipos Null y Undefined son estrictamente iguales a ellos mismos y abstractivamente iguales \nentre sí. 
Operadores de comparación de JavaScript 
JavaScript tiene comparaciones de dos tipos: 
• Estrictas. 
Solo es verdadera si los operandos son del mismo tipo y los contenidos coinciden. 
Ejemplo: === 
• De conversión de tipos (abstracta). 
Antes de realizar la comparación, los operandos se convierten al mismo tipo. 
Ejemplo: == 
Es una de las comparaciones abstracta más utilizada: 
• En las comparaciones abstractas relacionales, antes de la comparación: 
» Primero los operandos se convierten en primitivos. 
» A continuación se convierten en el mismo tipo. 
Ejemplo: <= 

<!-- Page 123 -->

 
 
Aplicaciones y desarrollo web 
123 
Operadores de igualdad 
• Igualdad (==). 
• Desigualdad (!=). 
• Identidad / igualdad estricta (===). 
• El resultado es verdadero si los operandos son estrictamente iguales, sin conversión de tipo. 
• Sin identidad / desigualdad estricta (!==). 
• El resultado es verdadero si los operandos no son iguales y / o no del mismo tipo. 
Operadores relacionales 
Cada uno de estos operadores llamará a la función valueOf() en cada operando antes de realizar una 
comparación. 
• Operador mayor que (>). 
• Operador mayor o igual (>=). 
• Operador menor que (<). 
• Operador menor o igual (<=). 
 
 
 
 
Reto 
Te proponemos que diseñes una página web simple con los 
conceptos que has estudiado de HTML, CSS y JavaScript. Para ello 
puedes seguir los siguientes pasos: 
1. Escribe tu página web en cualquier editor de testo (bloc de 
notas, Word…) 
2. Guarda el archivo con extensión .html 
3. Abre el archivo con un navegador para que veas el 
resultado. 
Solución: 
Puedes utilizar un visor HTML en lugar de un editor y un navegador, de esta 
forma, vas viendo los resultados al mismo tiempo que escribes la página. 
 

<!-- Page 124 -->

 
 
Aplicaciones y desarrollo web 
124 
En JavaScript hay dos funciones para decodificar y codificar cadenas base64, son las funciones: 
• Window.atob(): decodifica. 
• Window.btoa(): codifica. 
 
 
 
 
+ Info 
Base 64 es un sistema de numeración posicional que usa 64 como 
base. 
Es la mayor potencia que puede ser representada usando 
únicamente los caracteres imprimibles de ASCII. 
Esto ha propiciado su uso para codificación de correos \nelectrónicos, PGP y otras aplicaciones. 
Todas las variantes famosas que se conocen con el nombre de 
Base64 usan el rango de caracteres A-Z, a-z y 0-9 en este orden 
para los primeros 62 dígitos, pero los símbolos escogidos para los 
últimos dos dígitos varían considerablemente de unas a otras. 
 
3.1.4.3. Framework de JavaScript 
Indicamos algunas de las bibliotecas más destacadas de JavaScript y su función: 
• Angular 
AngularJS o también llamado Angular.js o AngularJS 1), es de código abierto, creado y 
mantenido por Google. 
Se utiliza para crear sitios web de una sola página (SPA, single-page application) con elementos 
interactivos y mantenerlos. Destaca la posibilidad de realizar actualizaciones en tiempo real 
desde diferentes dispositivos, de forma que cualquier diseño se cambia de manera simultánea en 
la web y en la aplicación (a esto se le llama enlace de datos bidireccional). 
Su objetivo es facilitar el desarrollo y las pruebas de código, aumentando las aplicaciones 
basadas en navegador con capacidad de Modelo Vista Controlador (MVC). 
Angular forma parte MEAN Stack, por lo que puede combinarse con el entorno en tiempo de \nejecución de Node.js y la base de datos MongoDB. 

<!-- Page 125 -->

 
 
Aplicaciones y desarrollo web 
125 
MEAN, acrónimo para MongoDB, Express.js, AngularJS y Node.js, se considera un framework o 
conjunto de subsistemas de software para el desarrollo de aplicaciones y páginas web dinámicas 
que están basadas. Cada subsistema del Mean stack es de código abierto y de uso gratuito. 
• React 
Implementada por Facebook Se usa para desarrollar y operar la interfaz de usuario dinámica de 
las páginas web de tráfico entrante, creando aplicaciones web intuitivas. Hace uso del DOM 
virtual facilitando así la integración con cualquier aplicación. 
Las aplicaciones de Instagram o Airbnb están realizadas con esta tecnología. 
• Vue.js 
Su principal característica es que ofrece la posibilidad utilizar módulos, el programador 
seleccionar aquellos que le interesan y descarta los demás. 
Aunque utiliza una interfaz de programación muy simple, permite desarrollar elementos 
dinámicos de interconexiones realmente sofisticadas. 
Vue es utilizado por la empresa japonesa Nintendo en varios de sus sitios web oficiales. 
• Ember 
Se lanzó al mercado en 2015 y ha ido ganando popularidad desde entonces. Permite la 
actualización en tiempo real cuando se accede desde diferentes dispositivos. 
LinkedIn lo utiliza. 
• Node JS 
Hay que destacar que no se utiliza en el navegador, sino en el lado del servidor, y su uso es \nespecialmente el de crear aplicaciones escalables, muy efectivo para apps con un elevado tráfico \nen tiempo real. 
Netflix y PayPal lo han empleado en su desarrollo. 
• Meteor 
Gratuito y de código abierto. Se usa en aplicaciones web de tiempo real, con una estructura 
basada en eventos, y para creación de forma rápida de prototipos. 
Es un framework que está entre la base de datos y la interfaz de usuario, sincronizando ambas 
partes. 
• Jest 
Es un marco de prueba diseñado para probar las aplicaciones React, y también se puede utilizar \nen otros marcos de JavaScript. 

<!-- Page 126 -->

 
 
Aplicaciones y desarrollo web 
126 
3.1.4.4. ECMAScript 7 
ECMAScript es el estándar que da soporte al popular lenguaje de programación JavaScript que 
utilizamos en la web. Curiosamente JavaScript es anterior, nace en 1995 como un proyecto de Brendan 
Eich construido en Netscape Communications Corporation, en el tiempo récord de 10 días. 
JavaScript, fue diseñado para agregar interactividad a las páginas web estáticas de la época. Para que el 
lenguaje no se diluyera en distintas versiones, se presentó a ECMA Internacional para ser estandarizado 
dando lugar a ECMAScript. 
A partir de ese momento, ECMAScript no ha cesado de evolucionar, desde su primera versión ES1, 
publicada en 1997. Cada versión tiene su propia numeración, como por ejemplo ES7, versión 
ECMAScript del año 2016. ES7 es una versión destacada pues además de incorporar nuevas 
funcionalidades pone el foco en la claridad de la sintaxis (syntax sugar). 
 
 
 
 
+ Info 
Syntax sugar (azúcar sintáctico). 
Es un término acuñado por Peter J. Landin en 1964 para referirse a 
los añadidos a la sintaxis de un lenguaje de programación 
diseñados para hacer algunas construcciones más fáciles de leer o \nexpresar. 
 
 
ECMAScript define un lenguaje de tipos dinámicos ligeramente inspirado en Java y otros lenguajes del \nestilo de C. Soporta algunas características de la programación orientada a objetos mediante objetos 
basados en prototipos y pseudoclases. 
La mayoría de navegadores de Internet incluyen una implementación del estándar ECMAScript, al igual 
que un acceso al Document Object Model para manipular páginas web. 
Características añadidas en ECMAScript 7: 
• Array.includes() 
Determina si una matriz incluye un determinado elemento, devolviendo el valor true o false. 
• Operador de exponenciación ** 
Para elevar un número X a una potencia Y. 

<!-- Page 127 -->

 
 
Aplicaciones y desarrollo web 
127 
Tanto ECMAScript como en JavaScript la expresión console.log(4*3**2) evaluaría en primera 
instancia la potencia y posteriormente la multiplicación. Así pues el resultado de la operación 
4*3**2 sería 36. 
El término "ECMAScript" se usa a menudo como sinónimo de la versión más reciente que en \neste caso sería la ES2024. 
3.1.5. Bootstrap 
Bootstrap es un framework frontend creado por Twitter y puesto en común como proyecto de código 
abierto en el verano de 2011. 
El propósito inicial de este framework era que la parte frontend de Twitter tuviera un diseño y una 
consistencia común en todos los dispositivos que pudieran usarlo. Para ello se desarrolla un framework 
que combina el lenguaje de marcas HTML, el lenguaje script Javascript y las hojas de estilo CSS. 
Su caracter de código abierto y consiguiente apoyo de los componentes de Bootstrap acelera el 
desarrollo de interfaces de usuario responsivas. La clave de esta herramienta es el diseño responsivo 
apoyado en una cuadrícula flexible sustentada en las clases de las etiquetas css. 
La de cuadrícula Bootstrap se divide en seis tamaños, con sus clases respectivas que entrarán en juego 
dependiendo del tamaño en píxeles de la pantalla: 
• .col-xs–: ancho de pantalla inferior a 576 pixeles. 
• .col-sm-: ancho de pantalla igual o superior a 576 pixeles. 
• .col-md-: ancho de pantalla igual o mayor que 768 pixeles. 
• .col-lg-: ancho de pantalla igual o mayor que 992 pixeles. 
• .col-xl-: ancho de pantalla igual o mayor que 1200 pixeles. 
• .col-xxl-: ancho de pantalla igual o mayor que 1400 pixeles. 
El nombre de la clase se completaría con el número de columnas que definiríamos para una resolución \nen concreto. En este caso establecemos 6 columnas para pantallas pequeñas y 4 para medias. 
 

<!-- Page 128 -->

 
 
Aplicaciones y desarrollo web 
128 
Si bien en una pregunta del examen año 2023 dejaba entender y daba por válido que Bootstrap era un 
framework JavaScript, es principalmente un framework CSS que también incluye componentes 
JavaScript para mejorar interactividad y funcionalidad. 
3.1.6. AJAX 
AJAX acrónimo de Asynchronous JavaScript And XML. 
 
Fuente: Wilkimedia Conmons 
Es la técnica de desarrollo web para crear aplicaciones que se ejecuten en el cliente, mientras 
mantiene la comunicación con el servidor en segundo plano 
Es una técnica de desarrollo web para crear aplicaciones interactivas o RIA (Rich Internet Applications). 
Estas aplicaciones se ejecutan en el cliente, es decir, en el navegador de los usuarios, mientras se 
mantiene la comunicación asíncrona con el servidor en segundo plano. De esta forma es posible realizar 
cambios sobre las páginas sin necesidad de recargarlas, mejorando la interactividad, velocidad y 
usabilidad en las aplicaciones. 
Ajax es una tecnología asíncrona, en el sentido de que los datos adicionales se solicitan al servidor y se 
cargan en segundo plano sin interferir con la visualización ni el comportamiento de la página, aunque \nexiste la posibilidad de configurar las peticiones como síncronas de tal forma que la interactividad de la 
página se detiene hasta la espera de la respuesta por parte del servidor. 
JavaScript es un lenguaje de programación (scripting language) en el que normalmente se efectúan las 
funciones de llamada de Ajax mientras que el acceso a los datos se realiza mediante XMLHttpRequest, 
objeto disponible en los navegadores actuales. En cualquier caso, no es necesario que el contenido 
asíncrono esté formateado en XML. 
Ajax es una técnica válida para múltiples plataformas y utilizable en muchos sistemas operativos y 
navegadores dado que está basado en estándares abiertos como JavaScript y Document Object Model 
(DOM). 

<!-- Page 129 -->

 
 
Aplicaciones y desarrollo web 
129 
Ajax es una combinación de cuatro tecnologías ya existentes: 
 
• XHTML (o HTML) y hojas de estilos en cascada (CSS) para el diseño que acompaña a la 
información. 
• Document Object Model (DOM) accedido con un lenguaje de scripting por parte del usuario, \nespecialmente implementaciones ECMAScript como JavaScript y JScript, para mostrar e 
interactuar dinámicamente con la información presentada. 
• El objeto XMLHttpRequest para intercambiar datos de forma asíncrona con el servidor web. En 
algunos frameworks y en algunas situaciones concretas, se usa un objeto iframe en lugar del 
XMLHttpRequest para realizar dichos intercambios. 
• XML es el formato usado generalmente para la transferencia de datos solicitados al servidor, 
aunque cualquier formato puede funcionar, incluyendo HTML preformateado, texto plano, 
JSON y hasta EBML. 
Como el DHTML, LAMP o SPA, Ajax no constituye una tecnología en sí, sino que es un término que \nengloba a un grupo de éstas que trabajan conjuntamente. 
3.2. Back-end: aplicaciones servidor 
Son las aplicaciones del lado servidor, detrás del escenario, lo que no se ve. 
El desarrollador back-end trabaja del lado Servidor, permitiendo que el usuario navegue por la red, y lo 
haga de forma agradable, que disfrute de ello. 
Para la parte de programación del lado Servidor, existen numerosos lenguajes y frameworks. 

<!-- Page 130 -->

 
 
Aplicaciones y desarrollo web 
130 
 
 
 
Anécdota 
Al principio, los navegadores web tan solo visualizaban información \nestática, que resultaba "aburrido y poco útil" al usuario, por lo que 
se buscaron soluciones para poder ejecutar programas en el 
servidor, proporcionando dinámica etc. 
 
 
La parte servidor de las aplicaciones web está formada por: 
• Páginas estáticas (documentos HTML). 
• Recursos adicionales (multimedia, documentos adicionales…) que se pueden emplear dentro de 
las páginas o estar disponibles para ser descargados. 
• Programas o scripts que son ejecutados por el servidor web cuando el navegador del cliente 
solicita una página. La salida de este script suele ser una página HTML. 
Para crear las aplicaciones web, del lado servidor, el desarrollador back-end debe dominar un lenguaje y 
un framework, pero puesto que que todas las aplicaciones web almacenan datos, también debe conocer 
alguna de las bases de datos principales. 
Los lenguajes y frameworks más comunes son: 
• CGI (Perl). 
• ASP.NET ( C# y Visual Basic con sus tecnologías ASP/ASP.NET. 
• JSP. 
• PHP. 
• Node.js: 
Es la modalidad SSJS: Server Side Javascrip, de JavaScript, para las aplicaciones-servidor. 
Es cada vez más utilizado ya que usa el mismo lenguaje que en el lado cliente: JavaScript. 
• Python. 
• Ruby (junto con su framework Ruby on rails). 
• Java (con sus tecnologías Java Servlets y JavaServer Pages (JSP). 

<!-- Page 131 -->

 
 
Aplicaciones y desarrollo web 
131 
Las bases de datos más comunes son: 
• SQL Server. 
• MySQL. 
• Oracle. 
• PostgreSQL. 
• MongoDB, que es un almacén de datos no-relacional o NoSQL. 
 
 
 
 
Nota 
Al igual que hemos comentado antes, el entorno en el que trabajes, 
te obligará a especializarte en una u otra. 
 
Vamos a ver con detenimiento los lenguajes lenguajes y frameworks más importantes en Back-End. 
3.2.1. CGI (Common Gateway Interface) 
Fue el primer sistema que apareció para la creación de páginas dinámicas en servidor. Actualmente está 
obsoleto, debido a que los programas son difíciles de desarrollar y suponen una pesada carga para el 
servidor. 
Los CGI se escriben habitualmente en el lenguaje Perl, aunque puede utilizar otros lenguajes como C, 
C++ o Visual Basic. 
3.2.2. ASP.NET (Active Server Pages) 
ASP.NET es la plataforma de desarrollo web comercializado por Microsoft. 
Es muy usado por programadores para desarrollar especialmente sitios web. 
El lenguaje consiste en una serie de clases .NET utilizadas para crear aplicaciones web, tanto del lado 
cliente, como del lado servidor. 

<!-- Page 132 -->

 
 
Aplicaciones y desarrollo web 
132 
Tiene las variantes: 
• Web Forms. 
Formulario web dentro de una página web permite al usuario introducir datos que se envían a 
un servidor para ser procesados. 
Son similares a los formularios de papel, usando casillas de selección, botones de opción, o 
campos de texto. 
• Ahora también ASP.NET (con Core MVC: modelo vista controlador). 
ASP.NET se desarrolló para resolver las limitaciones de su tecnología antecesora ASP. 
Los archivos ASP.NET tienen la extensión (aspx). 
Para el desarrollo de ASP.NET se puede utilizar C#, VB.NET o J#. . 
La integración nativa de .NET Framework con el sistema operativo Windows Server hace que su \nejecución sea más estable y rápida que otros lenguajes de programación. 
Las páginas creadas con la tecnología ASP.NET funcionan en todo tipo de navegadores. 
Almacenamiento de los datos de sesión 
ASP .NET, ya sea web form o mvc (modelo vista controlador), controla el almacenamiento de los datos 
de sesión configurando el modo de estado de sesión fuera del proceso. 
ASP .NET tiene los siguientes modos de estado de sesión: 
• Modo InProc: 
Almacena el estado de sesión en memoria en el servidor Web. 
Éste es el valor predeterminado. 
• Modo StateServer: 
Almacena el estado de sesión en un proceso distinto denominado "servicio de estado de 
ASP.NET". 
Este modo garantiza que el estado de sesión se mantiene si se reinicia la aplicación Web y que \nesté disponible también para varios servidores Web en una batería de servidores Web. 
• Modo SQLServer: 
Almacena el estado de sesión en una base de datos de SQL Server. 
Este modo garantiza que el estado de sesión se mantiene si se reinicia la aplicación Web y que \nesté disponible también para varios servidores Web en una batería de servidores Web. 

<!-- Page 133 -->

 
 
Aplicaciones y desarrollo web 
133 
 
 
 
+ Info 
DevExpress es una herramienta que ofrece a los desarrolladores de 
aplicaciones una de las suites más completas de componentes de 
interfaz de usuario (UI) en todas las plataformas .NET tales como 
Windows Forms, MVC, ASP.NET, Silverlight y Windows XAML. 
Incluye distintos componentes tales como tablas, calendarios, \neditor de HTML, Hojas de cálculo, editores de datos o gráficas. 
 
3.2.3. Perl 
Es un lenguaje de programación inspirado en otras herramientas de UNIX, como Grep y c-Shell para la 
administración de tareas propias de sistemas UNIX. 
Su punto fuerte son las labores de procesamiento de textos y archivos. 
Es un lenguaje de programación basado en scripts portable a casi cualquier plataforma. 
Uno de sus elementos más potentes son las expresiones regulares, que a partir de su versión en Perl han 
sido adoptadas por otros lenguajes. 
3.2.4. Java 
Es el lenguaje clásico de los más demandados. 
Aunque Java es un lenguaje multipropósito y utiliza JSP y servlets para la programación en servidor, 
puede utilizarse también como lenguaje back-end. 
Aporta robustez y seguridad, por lo que es aconsejable para grandes proyectos. Sin embargo, para 
proyectos normales hay otras alternativas más aconsejables. 
Las API programadas en Java necesitan un contenedor de aplicaciones que manejen con solvencia el 
trabajo, y los requisitos de hardware suelen ser más elevados que en un servidor Apache usando PHP. 
Por lo tanto, solamente se usa en el ámbito empresarial. 

<!-- Page 134 -->

 
 
Aplicaciones y desarrollo web 
134 
3.2.5. JSP (Java Server Pages) 
Es un lenguaje multiplataforma basado en Java para la creación de sitios web dinámicos. 
Comparte ventajas similares a las de ASP.NET, desarrollado para la creación de aplicaciones web 
potentes. 
Características 
• El código está separado de la lógica del programa. 
• Las páginas se compilan en la primera petición. 
• Permite separar la parte dinámica de la estática en las páginas web. 
• El código JSP puede ser incrustado en código HTML. 
• Para su funcionamiento se necesita tener instalado un servidor Tomcat. 
• Posee un motor de páginas basado en los servlets de Java. 
• Los ficheros tienen la extensión .jsp. 
• Un comentario en JSP se realiza con la sintaxis: 
<%-- comentario --%> 
3.2.6. Node.js 
Node.js es un entorno de ejecución para JavaScript construido con el motor de JavaScript V8 de 
Chrome. 
Uno de los usos más habituales de NodeJS es la programación back-end. 
Permite programar aplicaciones que son capaces de ejecutarse en el servidor, proporcionando acceso a 
bases de datos, al sistema de archivos y cualquier otro recurso del lado del servidor. 
Sin embargo, NodeJS es tan amplio que se puede usar para muchas otras tareas, como la 
automatización, optimización o despliegue de aplicaciones, entre otras operaciones. El framework más 
importante es Express.js. 
Otros frameworks son: 
• Koa. 
• Next. 
• Nodal. 

<!-- Page 135 -->

 
 
Aplicaciones y desarrollo web 
135 
GULP 
Es un sistema de construcción (build system), una herramienta, en forma de script en NodeJS, que 
permite automatizar tareas comunes en el desarrollo de una aplicación web, como, por ejemplo: 
minimizar (técnica minify), procesar, subir al servidor, hacer FTP, hacer SSH, dar formato etc. 
Atom 
Atom es un editor de código fuente de código abierto para macOS, Linux, y Windows. Con soporte para 
múltiples plug-in escritos en Node.js y control de versiones Git integrado, desarrollado por GitHub. 
Atom es una aplicación de escritorio construida utilizando tecnologías web. 
3.2.7. PHP (Hipertext Preprocesor) 
En español, preprocesador de hipertexto. 
Es un lenguaje de programación de propósito general de código del lado del servidor originalmente 
diseñado para el preprocesado de texto plano en UTF-8, ampliamente reconocido por el estándar 
HTML, dando como resultado, en los exploradores, una salida al usuario perfectamente entendible. 
 
 
 
 
Anécdota 
Fue uno de los primeros lenguajes que se podían incorporar 
directamente en un documento HTML en lugar de llamar a un 
archivo externo que procese los datos. 
 
 
El cliente solamente recibe una página con el código HTML resultante de la ejecución de la PHP. Como 
la página resultante contiene únicamente código HTML, es compatible con todos los navegadores. 
 
 
 
 
+ Info 
UTF-8 es un formato de codificación de caracteres Unicode e ISO 
10646 que utiliza símbolos de longitud variable. 
 

<!-- Page 136 -->

 
 
Aplicaciones y desarrollo web 
136 
Tiene las siguientes características: 
• Del lado del servidor. 
• Gratuito. 
• Independiente de plataforma. 
• Rápido. 
• Permite el desarrollo web de contenido dinámico. 
• PHP no genera HTML, sino que ofrece una salida de texto con codificación UTF-8 compatible 
con los documentos HTML. 
• El programador puede dotar a la salida de los tag's propios del HTML y los exploradores más 
comunes para navegar por internet, reconocerán muy rápidamente el formato UTF-8 y lo 
adaptarán ofreciendo una salida entendible. 
• Posee una gran librería de funciones. 
• Existe mucha documentación. 
• Es de código abierto. 
 
 
 
 
Ejemplo 
El famoso gestor de contenidos WordPress usa por detrás PHP. 
Laravel es uno de los frameworks usados con este lenguaje. 
 
Frameworks de PHP 
Los principales frameworks de PHP son: 
• Laravel. 
• Symfony. 

<!-- Page 137 -->

 
 
Aplicaciones y desarrollo web 
137 
Ventajas y Desventajas de PHP 
Sus principales ventajas son: 
• Forma parte de la infraestructura de servidor web LAMP (Linux, Apache, MySQL y PHP). 
• Es fácil de aprender. 
• Es multiplataforma. 
• Se conecta fácilmente a todo tipo de bases de datos. 
Sus principales desventajas son: 
• Todo el trabajo recae sobre el servidor. 
• Poco legible al mezclarse con HTML. 
Sintaxis 
La sintaxis de PHP, se fundamenta en los principios de programación de C. 
El intérprete de PHP solo ejecuta el código que se encuentra entre sus delimitadores. 
• Para separar el código PHP del resto de código, utilizamos el delimitador <?php para abrir una 
sección PHP y ?> para cerrarla. 
En los archivos que contienen solo código PHP, el delimitador ?> se puede omitir. 
• Las variables se prefijan con el símbolo del dólar ($) y no es necesario indicar su tipo. 
Las variables, a diferencia de las funciones, distinguen entre mayúsculas y minúsculas. 
Las cadenas de caracteres pueden ser encapsuladas tanto en dobles comillas como en comillas 
simples, aunque en el caso de las primeras, se pueden insertar variables en la cadena 
directamente, sin necesidad de concatenación. 
• Los comentarios se pueden escribir bien con dos barras al principio de la línea, o con una 
almohadilla. 
También permite comentarios multi-línea encapsulados en /* */. 
• En cuanto a las palabras clave, PHP comparte con la mayoría de otros lenguajes con sintaxis C 
las condiciones con if, los bucles con for, while, do…while, y los retornos de funciones. 
Como es habitual en este tipo de lenguajes, las sentencias deben acabar con punto y coma (;). 

<!-- Page 138 -->

 
 
Aplicaciones y desarrollo web 
138 
Funciones 
Existen muchas funciones integradas en PHP. Para utilizarlas hay que realizar la llamada (invocar la 
función) y especificar los parámetros necesarios para que la función realice su tarea. 
También es posible crear funciones propias en PHP. 
Funciones para trabajar con arrays: 
• implode(): Convierte un array en una cadena de texto. 
• explode(): Convierte un string en un array. 
• foreach(): Función para recorrer arrays. 
• count(): Cuenta todos los elementos de un array, o algo de un objeto. 
• sizeof(): Alias de la función count(). 
• array_push(): Añade nuevos elementos. 
• sort(), asort() y ksort(): Ordena los arrays. 
• unset(): Elimina elementos. 
• var_export(): Muestra el valor. 
• var_dump(): Muestra el valor 
• print() y print_r(): Muestra el valor. 
• shuffle(): Desordena un array. 
• array_merge(): Une varios arrays en uno. 
• array_search(): Busca valores en un array. 
• array_rand(): Devuelve una clave aleatoria. 
• array_chunk(): Divide arrays en varios arrays. 
• str_split(): Convierte un string en un array. 
• preg_split(): Convierte un string en un array con expresiones regulares. 
• array_unique: Eliminar los valores duplicados de un array. 
Cada una de estas funciones tienen opciones de parámetros. 

<!-- Page 139 -->

 
 
Aplicaciones y desarrollo web 
139 
Ejemplo: 
• Dado el siguiente array: $bebidas = array("agua", "refrescos", "zumos"). 
• Sentencia echo count($bebidas). 
• Resultado: 3 (número de elementos que tiene el array $bebidas). 
Operadores 
Un operador es algo que toma uno más valores (o expresiones, en la jerga de programación) y produce 
otro valor (de modo que la construcción en si misma se convierte en una expresión). 
Los operadores se pueden agrupar de acuerdo con el número de valores que toman. 
• Los operadores unarios toman sólo un valor, por ejemplo: ! (el operador lógico de negación) o 
++ (el operador de incremento). 
• Los operadores binarios toman dos valores, como los familiares operadores aritméticos + 
(suma) y - (resta), y la mayoría de los operadores de PHP entran en esta categoría. 
• Finalmente, hay sólo un operador ternario, ? :, el cual toma tres valores; usualmente a este se le 
refiere simplemente como "el operador ternario" (aunque podría tal vez llamarse más 
correctamente como el operador condicional). 
Hay que tener en cuenta, que los operadores tienen precedencia (al igual que en las operaciones 
matemáticas). La Precedencia de operadores, define exactamente cómo son evaluadas expresiones que 
contienen varios diferentes operadores. 
Tipos de operadores: 
• Operadores aritméticos. 
• Operadores de asignación. 
• Operadores bit a bit. 
• Operadores de comparación. 
Ejemplo: 
• $a == $b 
Igual: Devuelve TRUE si $a es igual a $b después de la manipulación de tipos. 
• $a === $b 
Idéntico: Devuelve TRUE si $a es igual a $b, y son del mismo tipo. 

<!-- Page 140 -->

 
 
Aplicaciones y desarrollo web 
140 
• Operadores de control de errores. 
• Operadores de ejecución. 
• Operadores de incremento/decremento. 
• Operadores lógicos. 
• Operadores para strings. 
• Operadores para arrays. 
• Operadores de tipo. 
Variables Superglobales 
Cuando hablamos en PHP de variables superglobales estamos hablando de variables que están 
disponibles desde todos los ámbitos del script, podremos invocarlas desde cualquier punto, funciones, 
métodos, etc. sin que haya que declararlas en ningún sitio. 
A continuación, detallamos una lista de las más usadas: 
• $_SESSION: las variables de sesión mantendrán los datos ente múltiples solicitudes del mismo 
usuario. Esto eso que se almacenará información persistente en el servidor hasta que se cierre el 
navegador o pase un determinado tiempo. Los valores almacenados permanecerán aun 
abriendo diversas ventanas o pestañas. 
• $_SERVER: esta superglobal contiene informaciones tales como cabeceras, rutas o ubicaciones 
de script. Dependiendo del elemento del array invocado nos devolverá los valores solicitados: 
• $_SERVER['SERVER_ADDR'] -> dirección IP del servidor 
• $_SERVER['SERVER_NAME'] -> nombre del servidor donde se está ejecutando el script 
• $_SERVER['REQUEST_METHOD'] -> método empleado para acceder a la página (GET, 
HEAD, POST, PUT) 
• Hay muchos más elementos, puedes consultar en el enlace siguiente para conocerlos todos 
Superglobales o Variables Reservadas al Servidor 
• $_GET: recoge los datos trasladados mediante el método GET que serán accesibles usando las 
claves de la matriz asociativa. Si tenemos una url https://ejemplo.com?nombre='Guillermo', 
capturaríamos el valor a través de esta superglobal $_GET['nombre']. 
• $_POST: contiene al igual que la anterior los datos transmitidos mediante el método POST, en \neste caso no sería a través de URL sino en el cuerpo de la solicitud HTTP. Un método elegido 
cuando la información a trasladar es sensible o muy extensa. 

<!-- Page 141 -->

 
 
Aplicaciones y desarrollo web 
141 
• $_FILES: cuando un archivo es enviado desde una página web (el cliente), el script php que 
recibe ese archivo usará la superglobal $_FILES para manejar la información relacionada con ese 
archivo, su ubicación temporal $_FILES[tmp_name], su tamaño $_FILES['size'], el nombre 
original en el sistema de archivos del cliente $_FILES['name'], el tipo MIME del archivo 
$_FILES['type'], la ubicación temporal del archivo $_FILES['tmp_name'] o si ha existido un \nerror en la carga $_FILES['error']. 
• $_REQUEST: esta superglobal nos servirá de comodín para acceder tanto a los datos enviados 
por el método GET como por el método POST. Se puede usar si se desconoce qué metodo de \nenvío va a ser usado, para recibir igualmente los datos. Con la URL citada en $_GET podríamos 
capturar el nombre enviado usando $_REQUEST['nombre']. 
 
 
 
 
Recomendación 
Recomendación Las opciones de PHP, son muchas, por lo que te 
recomendamos profundices en su estudio, si lo deseas, en su 
página oficial: https://www.php.net/ 
 
3.2.8. Python 
Es un lenguaje de código abierto, y es muy recomendado para empezar a programar, ya que su 
aprendizaje es fácil. 
Es un lenguaje orientado a la legibilidad, de escritura clara y comprensible, ya que su formato es 
visualmente ordenado, ejemplos de su simplicidad son: 
• Frecuentemente, utiliza palabras en inglés en lugar de símbolos. 
Por ejemplo, los operandos lógicos !, || y &&, en Python se escriben not, or y and 
respectivamente. 
• No utiliza corchetes para delimitar bloques. 
• Se permiten puntos y coma después de las declaraciones, pero rara vez se utilizan. 
• Cada línea del bloque debe estar precedida por el mismo número de espacios en blanco, con la 
misma sangría. 
El contenido de los bloques de código (bucles, funciones, clases, etc.) es delimitado mediante \nespacios o tabuladores, conocidos como indentación (término usado en informática, \nequivalente a sangrado), antes de cada línea de órdenes pertenecientes al bloque. (Otros 
lenguajes suelen declarar los bloques mediante un conjunto de caracteres, como por ejemplo \nentre llaves). 

<!-- Page 142 -->

 
 
Aplicaciones y desarrollo web 
142 
Pueden utilizarse tanto espacios como tabuladores para sangrar el código, pero es 
recomendable no mezclarlos. 
Cada instrucción debe estar contenida en una sola línea, pero si es necesario dividirla en varias 
líneas por legibilidad se puede hacer añadiendo una barra invertida \ al final de una línea, que 
indica que la instrucción continúa en la siguiente. 
• Los comentarios se pueden indicar de dos formas. 
Python permite elegir entre los dos siguientes métodos: 
• Utilizar el símbolo # antes del comentario, que se entiende que es toda la línea. 
• La más recomendada, y además necesaria para comentarios largos, es la notación de tres 
apóstrofos ''' antes y después del comentario. 
En los vectores, matrices y todo tipo de Arrays, los índices empiezan en cero y no en uno. 
Python es un lenguaje de programación multiparadigma, permite estilos de programación orientada a 
objetos, programación imperativa y programación funcional. Otros paradigmas están soportados 
mediante el uso de extensiones. 
Python usa tipado dinámico (una variable puede tomar valores de distinto tipo) y conteo de referencias 
para la gestión de memoria. 
Los nombres de variables pueden contener números y letras, pero deben comenzar por una letra. Se 
usa el símbolo = para asignar valores. 
 
 
 
 
+ Info 
Conteo de referencias, en inglés Reference counting, es una 
técnica de muy fácil implementación para contabilizar las veces 
que un determinado recurso está siendo referido. Por lo general \nese recurso son bloques de memoria y la técnica permite \nestablecer cuando no existe ninguna referencia a ese bloque y este 
puede ser liberado. 
tiene una importante desventaja: Si las referencias forman un ciclo 
los objetos involucrados no se liberarán nunca, por lo que resulta 
más efectivo el uso de un recolector de basura. 
 

<!-- Page 143 -->

 
 
Aplicaciones y desarrollo web 
143 
Una característica importante de Python es la resolución dinámica de nombres, también llamado enlace 
dinámico de métodos; es decir, lo que enlaza un método y un nombre de variable durante la ejecución 
del programa (). También la facilidad de extensión, se pueden escribir nuevos módulos fácilmente en C 
o C++. 
Python puede incluirse en aplicaciones que necesitan una interfaz programable. 
 
 
 
 
+ Info 
Python incluye en su intérprete estándar un modo interactivo, 
donde en una especie de intérprete de comandos, las expresiones 
pueden ser introducidas una a una, pudiendo verse el resultado de 
su evaluación inmediatamente. 
Posibilita probar porciones de código en el modo interactivo antes 
de integrarlo como parte de un programa. 
 
 
Su principal framework es Django. Django es un framework de código abierto para desarrollo web, que 
ofrece varias librerías para poder sincronizar los archivos estáticos con un servicio de almacenamiento 
remoto, y que respeta el patrón de diseño MVC (modelo-vista-controlador). La meta fundamental de 
Django es facilitar la creación de sitios web complejos, pone énfasis en el re-uso, la conectividad y \nextensibilidad de componentes, el desarrollo rápido y el principio "no te repitas" (DRY, del inglés Don't 
Repeat Yourself). 
Tiene la ventaja de poder ejecutarse en cualquier tipo de servidor (como Java) pero siendo interpretado 
(como PHP). 
Palabras reservadas 
En función de la versión, las palabras reservadas pueden variar. Indicamos las principales: 
• and: Operador lógico. 
• assert: Se utiliza con fines de depuración. 
• break: Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal. 
• class: Se usa para definir una nueva clase definida por el usuario. 
• continue: Se utiliza en el interior de los bucles for y while para alterar su comportamiento 
normal. 

<!-- Page 144 -->

 
 
Aplicaciones y desarrollo web 
144 
• def: se usa para definir una función definida por el usuario. 
• del: Para eliminar un objeto. 
• elif: Se usa en declaraciones condicionales, igual 'else' e 'if'. 
• else: Se usa en declaraciones condicionales, igual 'elif' e 'if'. 
• except: Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que 'raise' 
y 'try'. 
• finally: Su uso garantiza que el bloque de código dentro de él se ejecute incluso si hay una \nexcepción no controlada. 
• for: Utilizado para hacer bucles. Generalmente lo usamos cuando sabemos la cantidad de veces 
que queremos que se ejecute ese bucle. 
• from: Para importar partes específicas de un módulo. 
• global: Para declarar una variable global. 
• if: Se usa en declaraciones condicionales, igual 'else' y 'elif'. 
• import: Para importar un módulo. 
• in: para comprobar si un valor está presente en una lista, tupla, etc. Devuelve True si el valor \nestá presente, de lo contrario devuelve False. 
• is: Se usa para probar si las dos variables se refieren al mismo objeto. Devuelve True si los 
objetos son idénticos y False si no. 
• lambda: Para crear una función anónima. 
• not: Operador lógico. 
• nonlocal: Para declarar una variable no local. 
• or: Operador lógico. 
• pass: Es una declaración nula en Python. No pasa nada cuando se ejecuta. Se utiliza como 
marcador de posición. 
• raise: Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que 'except 
y 'try'. 
• return: Se usa dentro de una función para salir y devolver un valor. 
• try: Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que 'raise' y 
'except. 

<!-- Page 145 -->

 
 
Aplicaciones y desarrollo web 
145 
• while: Se usa para realizar bucles. 
• with: Se usa para simplificar el manejo de excepciones. 
• yield: Se usa dentro de una función al igual que 'return', salvo que 'yield' devuelve un generador. 
 
 
 
 
+ Info 
Según la versión que usamos de Python, las palabras reservadas 
pueden variar. 
Para consultarlas podemos teclear en consola el comando help() 
(entraremos en help>) 
A continuación, podemos teclear keywords para ver el listado. 
 
Tipos de Datos 
Indicamos tipos de datos en la siguiente tabla: 
Tipo 
Clase 
Notas 
Ejemplo 
str 
Cadena 
Inmutable 
Cadena' 
unicode 
Cadena 
Versión Unicode de str 
u'Cadena' 
list 
Secuencia 
Mutable, puede contener objetos de diversos 
tipos 
[4.0, 'Cadena', True] 
tuple 
Secuencia 
Inmutable, puede contener objetos de 
diversos tipos 
(4.0, 'Cadena', True) 
set 
Conjunto 
Mutable, sin orden, no contiene duplicados 
set([4.0, 'Cadena', True]) 
frozenset 
Conjunto 
Inmutable, sin orden, no contiene duplicados 
frozenset([4.0, 'Cadena', 
True]) 
dict 
Mapping 
Grupo de pares clave:valor 
{'key1': 1.0, 'key2': False} 
int 
Número entero 
Precisión fija, convertido en long en caso de 
overflow. 
42 

<!-- Page 146 -->

 
 
Aplicaciones y desarrollo web 
146 
Tipo 
Clase 
Notas 
Ejemplo 
long 
Número entero 
Precisión arbitraria 
42L o 456966786151987643L 
float 
Número 
decimal 
Coma flotante de doble precisión 
31.415.927 
complex 
Número 
complejo 
Parte real y parte imaginaria j. 
(4.5 + 3j) 
bool 
Booleano 
Valor booleano verdadero o falso 
True o False 
3.2.9. Apache Web Server 
El servidor HTTP Apache es un servidor web HTTP de código abierto. 
El servidor Apache es desarrollado y mantenido por una comunidad de usuarios bajo la supervisión de la 
Apache Software Foundation dentro del proyecto HTTP Server (httpd). 
 
 
 
 
Anécdota 
Su nombre se debe a que alguien quería que tuviese la connotación 
de algo que es firme y enérgico pero no agresivo, y la tribu Apache 
fue la última en rendirse al que pronto se convertiría en gobierno 
de Estados Unidos. 
Además, Apache consistía al principio, solamente en un conjunto 
de parches a aplicar al servidor de NCSA. En inglés, a patchy server 
(un servidor "parcheado") suena igual que Apache Server. 
 
 
Destacaremos de Apache: 
• Se utiliza para plataformas Unix (BSD, GNU/Linux, etc.), Microsoft Windows, Macintosh y 
otras, (puede ejecutarse en casi las principales plataformas y sistemas operativos). 
• Implementa el protocolo HTTP/1.1 y la noción de sitio virtual según la normativa RFC 2616. 
• Presenta características altamente configurables. 

<!-- Page 147 -->

 
 
Aplicaciones y desarrollo web 
147 
• Dispone de bases de datos de autenticación y negociado de contenido. 
• Desde 1996, Apache ha sido uno de los servidores HTTP más usado. (El más usado bastantes 
años). 
 
 
 
 
Atención 
Apache Derby es un sistema gestor de base de datos relacional \nescrito en Java que puede ser empotrado en aplicaciones Java. 
Java DB es una distribución de Oracle para la base de datos de 
código abierto Apache Derby. 
 
3.2.9.1. Apache Hadoop 
Apache Hadoop es tipo de programa framework, de licencia libre, desarrollado por Apache Software 
Foundation, y lanzado el 1 de abril de 2006. Usa plataforma Java. 
Hadoop se usa para programar aplicaciones distribuidas que manejen grandes volúmenes de datos (big 
data), permite a las aplicaciones trabajar con miles de nodos en red y petabytes de datos. 
Es un proyecto de la organización Apache que está siendo construido y usado por una comunidad global 
de contribuyentes, mediante el lenguaje de programación Java. 
Yahoo! ha sido el mayor contribuyente al proyecto, y usa Hadoop extensivamente en su negocio. 
 
 
 
 
Importante 
Avro: 
Es un marco de serialización de datos y llamadas de 
procedimiento remoto orientado a filas desarrollado dentro del 
proyecto Hadoop de Apache. Utiliza JSON para definir tipos de 
datos y protocolos, y serializa datos en un formato binario 
compacto. 
 

<!-- Page 148 -->

 
 
Aplicaciones y desarrollo web 
148 
3.2.9.2. JMeter 
JMeter es un proyecto de Apache. 
JMeter puede: 
• Ser utilizado como una herramienta de prueba de carga para analizar y medir el rendimiento de 
una variedad de servicios, con énfasis en aplicaciones web. 
• Ser usado como una herramienta de pruebas unitarias para conexiones de bases de datos con 
JDBC, FTP, LDAP, Servicios web, JMS, HTTP y conexiones TCP genéricas. 
• Puede también ser configurado como un monitor, aunque es comúnmente considerado una 
solución ad-hoc respecto de soluciones avanzadas de monitoreo. 
A veces se clasifica JMeter como herramienta de "generación de carga", pero esto no es una descripción 
completa de la herramienta. JMeter soporta aserciones para asegurar que los datos recibidos son 
correctos, por lo que es una herramienta de realización de pruebas automáticas. 
Jmeter es una herramienta para realizar pruebas de estrés en Java. 
3.2.10. Ruby 
Posee las siguientes características: 
• Es un lenguaje de programación interpretado, reflexivo y orientado a objetos y de código 
abierto. 
• Combina una sintaxis inspirada en Python y Perl con características de programación orientada 
a objetos similares a Smalltalk. 
• Comparte también funcionalidad con otros lenguajes de programación como Lisp, Lua, Dylan 
y CLU. 
• Es un lenguaje dinámico enfocado en la simplicidad y productividad. 
• Principal framework: Ruby on Rails. 
3.3. Full stack 
El desarrollador full stack, es un programador "multiusos", responsable del desarrollo del proyecto, 
desde el montaje de los servidores, hasta el diseño con CSS. 

<!-- Page 149 -->

 
 
Aplicaciones y desarrollo web 
149 
 
 
 
Anécdota 
El departamento de ingeniería de Facebook, fue quién popularizo 
hace unos años este rol de programador full-stack. 
 
 
Realmente, un buen desarrollador Full Stack, es el encargado de manejar cada uno de los aspectos 
relacionados con la creación y el mantenimiento de una aplicación web, por lo que es necesario que 
dicho desarrollador tenga conocimientos en Front-End y Back-End, y lenguajes de programación, lo que 
hoy en día es prácticamente imposible en una sola persona. 
El perfil de un desarrollador full stack, suele darse en pequeñas empresas, dónde puede encargarse de 
todo el desarrollo web. 
El constante avance de la tecnología impide estar al día y dominar toda la arquitectura cliente-servidor 
para el desarrollo web necesario en una gran empresa. 
Normalmente un programador full stack, está más especializado en una de las partes front-end o back-\nend, y tiene conocimientos básicos de la otra parte para poder realizar su trabajo. 
 
 
 
 
Conclusiones 
El desarrollador Full Stack, es muy demandado en las empresas, ya 
que debe establecer y controlar estrategias para cada parte del 
proceso de desarrollo web. Debe saber cómo se diseña la 
aplicación web y como programarla. 
 
4. XML 
XML, significa eXtensible Markup Language. Es un lenguaje de marca, independiente del hardware y 
software utilizado, que se usa para almacenar y transportar datos. 
XML es una especificación de W3C como lenguaje de marcado de propósito general. Esto que significa 
que, a diferencia de otros lenguajes de marcado, XML no está predefinido, el desarrollador debe definir 
tus propias etiquetas. 

<!-- Page 150 -->

 
 
Aplicaciones y desarrollo web 
150 
El propósito principal del lenguaje es compartir datos a través de diferentes sistemas, como Internet. 
Para que un documento XML sea correcto, debe ser un "documento bien formado". 
Esto significa, que debe cumplir reglas de semántica que son generalmente definidas en un esquema 
XML o en una Definición de Tipo de Documento (DTD). 
 
 
 
 
Ejemplo 
Ejemplo de un documento que no está bien formado: 
• Aquel que tiene una etiqueta de apertura y no de cierre. 
• Un documento que contiene una etiqueta no definida es 
inválido. 
 
 
Normalmente, casi todos los navegadores ofrecen un depurador que puede identificar documentos 
XML mal formados. 
Para utilizar en un documento XML una hoja de estilos XSL, se utiliza la instrucción de procesamiento 
xml-stylesheet, y debe ir al principio del documento, después a continuación de la declaración de 
documento <?xml>. 
Ejemplo: 
<?xml version="1.0" encoding="UTF-8"?> 
<?xml-stylesheet type="texto_en_xsl" href="ficheroejemplo.xsl"?> 
Hay muchos lenguajes basados en XML como: 
• XHTML. 
• MathML. 
• SVG. 
• XUL. 

<!-- Page 151 -->

 
 
Aplicaciones y desarrollo web 
151 
• XBL. 
• RSS. 
• OWL: 
Es el acrónimo del inglés Web Ontology Language, un lenguaje de marcado para publicar y 
compartir datos en la WWW. 
Tiene como objetivo facilitar un modelo de marcado construido sobre RDF y codificado en XML. 
• Etc. Y también puedes crear uno propio. 
Utilizar XML es opcional, pero si se incluye, tiene que aparecer obligatoriamente en la primera línea del 
documento, y deber ser el carácter "<" el primero de dicha línea, (antes no puede haber ni siquiera \nespacios en blanco). 
No pertenece ni a front-end ni a back-end, puede ser utilizado por cualquiera de ellos. 
Objetivos 
• Debe ser utilizable directamente por los navegadores. 
• Debe soportar una amplia variedad de aplicaciones. 
• Debe ser compatible con SGML. 
• Debe ser fácil procesar documentos XML. 
• Los documentos XML deben ser claros y legibles por un humano. 
• La especificación de XML debe ser formal y concisa. 
• Los documentos XML deben ser fáciles de producir. 
 
 
 
 
+ Info 
Los XML-Firewall, (software cortafuegos ) analizan mensajes XML, 
por lo que son especialmente indicados para arquitecturas basadas \nen servicios web, para proteger las aplicaciones expuestas a través 
de interfaces basadas en XML (como WSDL y RES), y escanear el 
tráfico XML que entra y sale de una organización. 
 

<!-- Page 152 -->

 
 
Aplicaciones y desarrollo web 
152 
Características de XML 
• Es un lenguaje de marcas (etiquetas) parecido a HTML. 
• Ha sido diseñado para almacenar y transportar datos. 
• Es auto descriptivo. 
• Es una recomendación de W3C. 
• Puede integrar datos estructurados (tablas relacionales) y poco estructurados (documentos). 
• XML no hace nada por sí mismo. 
Únicamente es información estructurada mediante etiquetas. 
Es necesario utilizar algún tipo de software para enviarlo, almacenarlo o visualizarlo. 
• Versátil. Separa contenido, estructura y presentación. 
• Abierto. Es independiente de plataformas, empresas, lenguajes de programación o entornos de 
desarrollo. 
• Sencillo. Fácil de aprender y de usar. 
• XML no utiliza etiquetas predefinidas. El diseñador debe definir las etiquetas y la estructura del 
documento. 
• La mayoría de las aplicaciones XML funcionarán como se espera, incluso si se agregan (o \neliminan) datos nuevos. 
• Es extensible. Las aplicaciones que trabajen sobre un fichero XML seguirán funcionando, incluso 
si se agregan o eliminan datos. 
• XML se puede utilizar para separar los datos recibidos del servidor de la capa de presentación. 
XML contiene los datos y HTML le dará el formato apropiado según el caso y mostrará los datos. 
• El lenguaje XML tiene una estructura de árbol que comienza en la raíz y termina en las hojas. 
(Sólo puede tener un elemento raíz). 
• Si un documento cumple todas las reglas de sintaxis de XML, se dice que es un documento XML 
well formed (bien formado). También se puede validar frente a un DTD/Schema. 
• Un fichero XML puede ser validado para determinar si está bien formado o si tiene algún error. 
• Un elemento XML está formado por una etiqueta de apertura y otra de cierre, junto a todo lo 
que haya en su interior, que puede ser: 
• Texto. 
• Atributos. 
• Otros elementos. 
• Mezcla de todo lo anterior. 

<!-- Page 153 -->

 
 
Aplicaciones y desarrollo web 
153 
4.1. Entidades 
Una entidad es una declaración para establecer un nombre que se utilizará en el código XML en lugar de 
contenido. 
Hay que realizar una declaración de entidad para poder utilizarla después en el XML. El hecho de 
utilizarla se conoce como "referencia de entidad" 
La declaración de entidad, que asocia un nombre al contenido de reemplazo, se realiza mediante la 
sintaxis: 
<!ENTITY name "value"> 
Hay diferentes tipos de entidades, indicamos una clasificación de las mismas: 
 
Debes conocer las 5 entidades predefinidas de caracteres: 
Entidad 
Carácter 
Descripción 
&lt; 
< 
Menor que 
&gt; 
> 
Mayor que 

<!-- Page 154 -->

 
 
Aplicaciones y desarrollo web 
154 
Entidad 
Carácter 
Descripción 
&amp; 
& 
Ampersand 
&quot; 
" 
Comilla doble 
&apos; 
‘ 
Apóstrofe (o comilla sencilla) 
 
 
 
 
+ Info 
Se pueden añadir más entidades usando el DTD del documento. 
También puedes usar referencias a caracteres numéricas para \nespecificar caracteres especiales. 
Por ejemplo: 
&#xA9; es el símbolo "©" 
 
4.2. Tipos de nodos de XML 
El World Wide Web Consortium (W3C), determina varias clases de tipos de nodos. Se indican las clases 
de nodos en el modelo de objetos de documento (DOM). 
Un documento XML se representa como un árbol jerárquico con siete tipos de nodos: 
 

<!-- Page 155 -->

 
 
Aplicaciones y desarrollo web 
155 
4.2.1. Nodo Raíz 
Es el nodo principal que contiene a los demás. 
El nodo raíz siempre es el nodo de tipo Document, del que derivan todos los demás nodos del documento. 
Este nodo es común para todas las páginas HTML y todos los documentos XML. 
4.2.2. Elemento 
Elements es un componente de un documento XML. 
Los elementos XML se pueden definir como bloques dentro de XML, que pueden contener una mezcla 
de texto, atributos, objetos de comunicación… 
El contenido de un elemento es todo lo que se encuentra entre las etiquetas de apertura y cierre. 
Dentro del contenido de un elemento incluso puede haber también elementos, en cuyo caso se llaman \nelementos hijos. 
 
 
 
 
Atención 
Todos los nombres de los elementos son case sensitive, es decir, 
sensibles a letras minúsculas y mayúsculas. 
 
 
Un elemento debe cumplir unas reglas: 
• Debe comenzar por una etiqueta de apertura y terminar por la etiqueta de cierre 
correspondiente, o puede consistir en una única etiqueta vacía. 
• El primer carácter tiene que ser una letra o un guion bajo "_". 
• Pueden contener: 
• Letras minúsculas. 
• Letras mayúsculas. 
• Números. 

<!-- Page 156 -->

 
 
Aplicaciones y desarrollo web 
156 
• Puntos ".". 
• Guiones medios "-". 
• Guiones bajos "_". 
• El carácter dos puntos ":". 
Se usa únicamente para cuando se definan espacios de nombres. 
• Detrás del nombre de una etiqueta se permite escribir un espacio en blanco o un salto de línea. 
Ejemplo: hay un espacio detrás de ciudad (en la primera vez que aparece), y un salto de línea 
después (en la segunda vez que aparece). 
<ciudad >Pamplona</ciudad 
                         > 
• No puede haber un salto de línea o un espacio en blanco antes del nombre de una etiqueta. 
Ejemplo: salto de línea antes de ciudad. 
< 
                         ciudad>Pamplona</ ciudad> 
4.2.3. Cadenas de texto 
XmlText 
Indica que el campo o propiedad debe ser tratado como texto. 
Texto que pertenece a un elemento o atributo. 
4.2.4. Atributo 
Attributes es un componente de las etiquetas. Consiste en una pareja name/value (nombre/valor) 
Un atributo, puede estar en las etiquetas de apertura o en las etiquetas vacías, pero no puede estar en 
las de cierre. 

<!-- Page 157 -->

 
 
Aplicaciones y desarrollo web 
157 
En una etiqueta no puede haber dos atributos con el mismo nombre. 
La sintaxis es: 
nombreAtributo="valorAtributo" 
Los atributos contienen datos relacionados con el elemento: 
• Todos los atributos tienen valores de tipo cadena. 
• No pueden contener múltiples valores. 
• No pueden contener una estructura de árbol. 
• No son fácilmente expandibles. 
Veamos algunos atributos destacables: 
• Version: 
Ya sabemos que escribir la declaración XML es opcional, pero, si se escribe, es obligatorio indicar \nel atributo versión. 
Indica la versión de XML que estamos utilizando. 
• Encoding: 
Es opcional, si se utiliza debe aparecer a continuación de versión. 
Por defecto su valor es "UTF-8". Si se omit se entiende que la codificación de caracteres es 
UNICODE. 
• Standalone: 
También es opcional, si se utiliza debe aparecer en el último lugar. 
Puede tomar dos valores: yes y no (por defecto en valor es no). 
• Yes. 
Indica que el documento es independiente de otros. 
• No. 
Indica que el documento NO es independiente de otros. 
Ejemplo: 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 

<!-- Page 158 -->

 
 
Aplicaciones y desarrollo web 
158 
 
 
 
+ Info 
Aunque HTML y XML son parecidos, tienen dos diferencias muy 
claras: 
• HTML fue se diseñó centrándose en la forma en que se 
visualizan los datos, mientras que XML se diseñó 
centrándose en qué datos son y en su transporte. 
• Las etiquetas HTML están predefinidas y las XML no 
(nosotros ponemos los nombres de las etiquetas). 
 
 
Ejemplo: 
Vamos a crear una base de datos simple llamada librería. En ella se guardarán libros que contendrán: 
• Un atributo denominado "categoría". 
• Un campo denominado "título". 
• El campo título tendrá un atributo denominado "idioma". 
• Un campo denominado "autor". 
• Un campo denominado "fecha_publicacion". 
• Un campo denominado "precio". 
El código con dos ejemplos de libros sería: 
<?xml version="1.0" encoding="UTF-8"?> 
     <libreria> 
       <libro categoría="Literatura fantástica"> 
       <titulo idioma="espanol">Juego de tronos</titulo> 
       <autor>George R.R. Martin</autor> 
       <fecha_publicacion>2005</fecha_publicacion> 
       <precio>26.00</precio> 
       </libro> 

<!-- Page 159 -->

 
 
Aplicaciones y desarrollo web 
159 
       <libro categoría="Inteligencia artificial"> 
       <titulo idioma="english">Speech and language processing</titulo> 
       <autor>Daniel Jurafsky and James H. Martin</autor> 
       <fecha_publicacion>2014</fecha_publicacion> 
       <precio>40.00</precio> 
       </libro> 
     </libreria> 
Usando HTML podemos darle un formato más interpretable. 
Vamos a mostrarlo en forma de árbol de varias formas. En ninguna de ellas hay que modificar el código 
XML. 
 
Estructura en árbol de fichero XML 

<!-- Page 160 -->

 
 
Aplicaciones y desarrollo web 
160 
 
Estructura en árbol en forma de tabla 
En este último ejemplo, podemos ver que primeramente ha validado el código (arriba se puede ver en 
rojo que ha comprobado que el texto está bien formateado). 
 
 
 
 
Reto 
Te proponemos que diseñes una base de datos sencilla con XML 
para ver si has asimilado los conceptos básicos. 
Por ejemplo, un fichero con información de las películas que más te 
gustan. 
Solución: 
Puedes utilizar un XML Viewer para comprobar si tu documento está bien \nestructurado y ver el resultado. 
 
4.2.5. Espacio de nombres 
System.Xml 
Es un ámbito semántico propio para cada uno de los vocabularios XML. 

<!-- Page 161 -->

 
 
Aplicaciones y desarrollo web 
161 
Un archivo XML, puede contener nombres de elementos o atributos procedentes de más de un 
vocabulario XML. 
Si en cada uno de estos vocabularios, damos un espacio de nombres, referenciado a la URI donde se 
incluyen los términos, se resuelve el problema de que un elemento y un atributo puedan llamarse igual 
(problema denominado homonimia). 
 
 
 
 
+ Info 
Homonimia: 
Coincidencia en dos palabras que tienen distinto significado (banco 
para sentarse o banco para guardar dinero). 
 
Los nombres de elementos, dentro de cada espacio de nombres, deben ser únicos. 
Ejemplo: 
Una instancia XML que contuviera referencias a un vendedor y a un producto. 
Tanto el elemento que representa el vendedor como el que representa el producto pueden tener un \nelemento hijo llamado "claveID", por tanto, las referencias al elemento "claveID" podrían ser ambiguas. 
¿A cuál de los dos nos referimos, a "claveID del vendedor" o "claveID del producto"? 
Para evitar esto, los elementos, con igual nombre, pero significado distinto, se llevarán a espacios de 
nombres distintos que los diferenciarán. 
Los espacios de nombres XML asocian nombres de elementos y de atributos de un documento XML con 
identificadores URI personalizados y predefinidos. 
Para crear estas asociaciones, puede definir los prefijos de los URI del espacio de nombres y usar dichos 
prefijos para calificar los nombres de los elementos y de los atributos en los datos XML. Los espacios de 
nombres evitan conflictos de nombres de elementos y atributos y permiten que los elementos y 
atributos con el mismo nombre se traten y se validen de forma diferente. 

<!-- Page 162 -->

 
 
Aplicaciones y desarrollo web 
162 
Declarar espacios de nombres 
Para declarar un espacio de nombres en un elemento, se usa el atributo xmlns, cuyo valor debe ser 
un identificador uniforme de recurso. 
Un espacio de nombres se declarará en una etiqueta padre de los elementos que la vayan a requerir. 
Dichos espacios pueden usarse fundamentalmente para dos objetivos, evitar conflictos de nombres y 
validar la correcta sintaxis de las etiquetas. 
Ejemplo: dsc y lib son los prefijos de espacio de nombres que son acompañadas por la URI que identifica \nese espacio de nombres. 
<etiqueta xmlns:dsc="http://www.espaciodenombres.com/discos" 
xmlns:lib="http://www.espaciodenombres.com/libros> 
   <disco> 
     <dsc:titulo>L.A. Woman</dsc:titulo> 
   </disco> 
   <libro> 
     <lib:titulo>El Principito</lib:titulo> 
   </libro> 
</etiqueta> 
En el ejemplo anterior las etiquetas anidadas <titulo> de disco y libro podrían entrar en conflicto si no se 
hubiera declarado el espacio de nombres correspondiente y se usara el prefijo. 
4.2.6. Instrucción de procesamiento 
Processing instruction 
Se utilizan para indicar cierta información al programa que procese dicho documento. 
Para indicar una instrucción de proceso, se escribe entre <? y ¿>. 
Con una instrucción de proceso, podemos asociar un archivo CSS al documento XML. 

<!-- Page 163 -->

 
 
Aplicaciones y desarrollo web 
163 
<?xml-stylesheet type="text/css" href="estilo-bebidas.css"?> 
Esta instrucción sirve para asociar el archivo CSS "estilo-bebidas.css" al documento XML. 
4.2.7. Comentario 
Comments 
Su sintaxis es igual que en HTML. 
Un comentario es una etiqueta que comienza por <!-- y acaba por -->. 
<!-- Así se indican los comentarios --> 
Los comentarios: 
• No pueden estar dentro de otras marcas. 
• No pueden contener los caracteres "--". 
4.3. Extensiones 
Para añadir nuevas funcionalidades a XML se han creado extensiones para: 
• Estructurar documentos. 
• Enlaces y direccionamiento. 
• Transformación y presentación. 
• Consultas. 
• Programación. 
• Otras menos importantes: Namespaces, XInclude, XBase, … 
Vamos a ver con detenimiento estas extensiones. 

<!-- Page 164 -->

 
 
Aplicaciones y desarrollo web 
164 
4.3.1. Estructurar documentos 
La gramática de los lenguajes XML (estructura y elementos permitidos en un documento) se puede 
definir mediante: 
• DTD (Document Type Definition): documento ASCII plano que especifica tanto los elementos 
que forman un tipo de documento dado, como las relaciones que se dan entre ellos. 
• XSD (XML Schema Definition): mejoran los DTD porque están escritos en XML y permiten 
nuevas características. 
DTD y XSD representan un modelo de datos jerárquico, estructurando los datos según un esquema 
semántico. 
Estos lenguajes se definen especificando los elementos y atributos permitidos. Esta especificación se 
realiza mediante reglas gramaticales. Un conjunto concreto y bien formado de tales reglas forman un \nesquema XML (representado por un DTD o un XSD). 
4.3.1.1. DTD 
Es un documento que proporciona medios para validar archivos XML en relación con un conjunto de 
normas específicas. Específica, por tanto, restricciones. 
El documento DTD define la estructura de un documento XML, los elementos (ELEMENT) que pueden 
aparecer, el orden y el número de veces que pueden aparecer, cuáles pueden ser hijos de cuáles, etc. 
Estos elementos son atributos, entidades, notaciones, etc. 
 
 
 
 
+ Info 
También hay DTD para SGML, como has visto anteriormente, pero 
difieren en la sintaxis (es similar). 
 
 
Una DTD puede: 
• Contener declaraciones que definen los elementos, atributos, anotaciones y entidades para el 
archivo XML. 
• Definir las relaciones de los elementos. 

<!-- Page 165 -->

 
 
Aplicaciones y desarrollo web 
165 
• Establecer limitaciones sobre cómo se puede utilizar cada elemento, atributo, anotación y \nentidad en el archivo XML. 
• Indica instrucciones y comentarios sobre su procesamiento. 
El procesador XML utiliza la DTD para verificar si el documento cumple las reglas del DTD, es decir, si es 
válido. 
 
 
 
 
Recuerda 
Para que un archivo XML se considere válido, debe estar 
acompañado de una DTD o XSD, y debe ajustarse a todas las normas 
(declaraciones) que se especifiquen él. (en el DTD o el XSD). 
 
El documento DTD hace referencia al XML que debe cumplir las normas que específica. 
 
 
 
Analizador de validación 
Se encargan de comprobar si el archivo XML cumple todas las 
normas indicadas en el DTD, comprueba cada línea y si no se ajusta 
a las normas genera un error indicando el lugar del archivo XML 
donde se produce. 
 
 
La DTD puede indicarse incluyéndola en el propio documento, o ser un documento externo (es lo más 
común, que se almacene en un fichero ASCII), o pueden combinarse ambas formas. Vamos a ver la 
sintaxis de estos modos, teniendo en cuenta que: 
• Incluida en el propio documento. 
Sintaxis: 
<!DOCTYPE nombredoc [ 
... declaraciones_normas ... 
]> 

<!-- Page 166 -->

 
 
Aplicaciones y desarrollo web 
166 
Siendo "nombredoc" el nombre del tipo de documento XML, que ha de coincidir con el nombre 
del elemento raíz del documento XML. 
• En un documento externo. 
Hay dos formas, si: 
• Sólo va a ser utilizada por una única aplicación. 
Sintaxis: 
<!DOCTYPE nombre SYSTEM "uri"> 
Si se quiere combinar este método con la DTD incluida en el propio documento, la sintaxis es: 
Siendo "uri" el camino absoluto o relativo hasta la DTD. 
• Va a ser utilizado por varias aplicaciones. 
Sintaxis: 
<!DOCTYPE nombre PUBLIC "fpi" "uri"> 
Si se quiere combinar este método con la DTD incluida en el propio documento, la sintaxis es: 
<!DOCTYPE nombredoc PUBLIC "fpi" "uri" [ 
 ... declaraciones_normas ... 
]> 
Siendo "fpi" el Formal Public Identifier (identificador público formal). 
Las declaraciones que se indican en un DTD, para describir la estructura que debe cumplir el XML, son 
de 4 tipos: 
• Declaraciones de entidades. 
Una entidad consiste en un nombre y su valor. 
Con algunas excepciones, El procesador XML sustituye las referencias a entidades por sus 
valores antes de procesar el documento (salvo algunas excepciones) 

<!-- Page 167 -->

 
 
Aplicaciones y desarrollo web 
167 
Una vez definida la entidad, se puede utilizar en el documento escribiendo una referencia a la \nentidad, que empieza con el carácter "&", sigue con el nombre de la entidad y termina con ";". 
(es decir, &nombreEntidad;) 
Las entidades pueden ser: 
• internas (que pueden ser generales o paramétricas) 
• externas (que pueden ser generales o paramétricas) 
• Declaraciones de elementos. 
Indican los elementos permitidos en un documento y el contenido que pueden tener. 
• Declaraciones de atributos. 
Indican los atributos permitidos en cada elemento y el tipo o valores permitidos de cada \nelemento. 
• Declaraciones de notaciones. 
En XML se utilizan las notaciones para definir las entidades externas que no serán analizadas por \nel procesador XML. 
Para definirlas en lugar de la notación &nombreEntidad; se utiliza directamente el nombre de la \nentidad. 
Ampliamos la información sobre la declaración de un elemento. 
Un elemento DTD se declara con la siguiente sintaxis: 
<!ELEMENT nombre_elemento (contenido_posible)> 
• !ELEMENT indica que estamos definiendo un elemento. 
• A continuación, indicamos el nombre del elemento que estamos definiendo, (también llamado 
identificador genérico). 
• Por último, entre paréntesis, indicamos qué contenido, si hubiera alguno, (puede estar vacío), 
puede ir en el elemento. 
En elemento puede tener distintos contenidos: 
• Con contenido vacío. 
• Con contenido de elemento. 
• Con contenido mixto. 
• Con cualquier contenido. 

<!-- Page 168 -->

 
 
Aplicaciones y desarrollo web 
168 
Con contenido Vacío 
Para declarar un elemento vacío en una DTD, hay que indicar que su contenido es EMPTY. El elemento 
se declara con la palabra clave EMPTY. 
<!ELEMENT nombre_elemento EMPTY> 
EMPTY debe escribirse sin paréntesis. 
Significa que el elemento ejemplo es vacío, no puede tener contenido. 
Con contenido de elementos 
El contenido son los elementos indicados entre paréntesis, puede ser más de uno. 
Ejemplo de definición de un elemento que contiene 3 elementos: 
<!ELEMENT nombre_elemento (contenido1, contenido2, contenido3)> 
A los elementos contenidos o secundarios, es decir los indicados entre paréntesis, podemos indicarles 
unas normas a cumplir, indicando un símbolo a continuación del nombre que le damos: 
• Símbolo multiplicación * 
Indica que el elemento secundario se puede dar cero o más veces dentro. 
• Símbolo suma + 
Indica que el elemento secundario se puede dar una o más veces. 
• Símbolo interrogante ? 
Indica que el elemento secundario se puede dar cero veces o una vez. 
• Carácter coma , 
Da una secuencia de los elementos secundarios separados por comas. 
• Carácter pleca o barra vertical | 
Permite hacer elecciones en el elemento secundario, es decir elegir entre los elementos 
secundarios (definidos entre paréntesis) que forman parte del elemento principal (definido 
con ! ). 

<!-- Page 169 -->

 
 
Aplicaciones y desarrollo web 
169 
Cuando tenemos un contenido de más de 1 elemento, hay que seguir unas reglas: 
• Secuencias: 
Si queremos que los elementos aparezcan en un orden tenemos que definir los elementos 
secundarios mediante una secuencia. 
Ejemplo: 
<!ELEMENT alumno (oposicion,matricula,delegacion)> 
La declaración indica que el elemento "alumno"> debe tener ni más ni menos que 3 elementos 
secundarios: oposicion, matricula, y delegación y tienen que aparecer en ese orden. 
Si queremos elegir sólo un elemento, (no ambos) entonces usaremos el carácter de barra vertical (|) \nentre ellos. 
<!ELEMENT telefono (fijo | movil)> 
Con contenido de elemento mixto 
Es una combinación de #PCDATA (Parsed Character Data) y de sus elementos secundarios. El 
contenido de PCDATA representa datos carácter analizados, como por ejemplo texto que no está 
revisado. 
Sintaxis: 
<!ELEMENT nombre_elemento (#PCDATA|elemento1|elemento2)*> 
#PCDATA debe ir al inicio en la declaración de contenido mixto. PCDATA es el texto no revisado. 
Cada uno de los elementos (elemento1 y elemento2), deben ser separados por (|), y deben tener su 
propia definición en el DTD. 
A continuación del cierre de paréntesis debe indicarse el operador * si los elementos secundarios se 
incluyen. 
Podemos indicar que un elemento es mixto utilizando la palabra ANY. 

<!-- Page 170 -->

 
 
Aplicaciones y desarrollo web 
170 
<!ELEMENT persona ANY> 
Se ha indicado que el elemento "persona" puede contener texto y otros elementos, es decir, contenido 
mixto, ANY. 
 
 
 
 
+ Info 
Puedes consultar más información sobre DTD en el siguiente \nenlace: 
https://www.mclibre.org/consultar/xml/lecciones/xml-dtd.html 
 
Formas de guardar un DTD 
Un DTD XML puede ser de 2 formas según lo guardemos: 
• DTD Interno: 
Un DTD se denomina DTD interno cuando los elementos se han declarado dentro del archivo 
XML. 
Para referenciarlo como DTD interno, el atributo standalone en la declaración XML se debe 
marcar con un SI. 
De esta forma la declaración funciona al margen de la fuente externa. 
Sintaxis: donde root-element es el nombre del elemento raíz y element-declarations es donde se 
declaran los elementos. 
<!DOCTYPE root-element [element-declarations]> 
• DTD externo: 
Los elementos declarados se guardan en un documento independiente (fuera del archivo XML), 
con extensión .dtd 
Es necesario relacionarlo con el DTD para poder usarlo. 

<!-- Page 171 -->

 
 
Aplicaciones y desarrollo web 
171 
Para referenciarlo como DTD externo, el atributo standalone en la declaración XML se debe 
marcar con un NO. 
Pueden ser o un archivo .dtd o una dirección URL válida. (por tanto la que la declaración incluye 
información de una fuente externa). 
Sintaxis: donde file-name es el archivo con la extensión .dtd. 
<!DOCTYPE root-element SYSTEM "file-name.dtd"> 
4.3.1.2. XSD 
XSD, siglas de XML Schema Definition, es un documento que define la estructura y restricciones de los 
contenidos de los documentos XML de una forma muy precisa. Contiene únicamente datos con un 
determinado formato y estructura. Está escrito en XML, y la extensión del documento es .xsd. 
Su objetivo es validar la estructura de un documento XML. Aunque el XSD no es obligatorio, asegura 
que el XML se pueda utilizar para determinados fines. 
Ha sido desarrollado por el World Wide Web Consortium (W3C), y el nivel de recomendación se dio en 
mayo de 2001. 
Los XSD se crearon como una alternativa a las DTD, con el objetivo de ser menos complejas, y de 
superar sus puntos débiles, aportando nuevas capacidades en la definición de estructuras para 
documentos XML, ya que incorpora un gran número de tipos de datos, incluyendo tipos de datos 
complejos como fechas, números y strings. Así aumenta las posibilidades y funcionalidades de 
aplicaciones de procesado de datos. 
Un esquema se define pensando en su uso final, XSD mejora los DTD porque están escritos en XML y 
permiten nuevas características como: 
• Definir tipos de datos. 
Soporta tipos de datos típicos de los lenguajes de programación, como también tipos 
personalizados simples y complejos. 
Puede definir el tipo de datos de los valores de los nodos, por ejemplo, que no tenga ningún otro 
valor que no sea un número. 
También puede definir tipos de datos personalizados, como sería que un dato para el mes, solo 
pudiera contener el nombre de los 12 meses, que estarían incluidos en el documento XSD, de lo 
contrario daría un error. 
Hay que tener en cuenta la restricción de que un elemento definido en el archivo XSD debe 
definirse solo con un tipo de datos. 

<!-- Page 172 -->

 
 
Aplicaciones y desarrollo web 
172 
• Utilizar namespaces (espacios de nombre). 
Se diseñó completamente en base a ello. 
• Definir intervalos de valores para los atributos y elementos. 
• Características orientadas a objetos. 
Puede comprobar la correcta jerarquía de los nodos xml, por ejemplo, indicando que nodo hijo 
debe estar bajo qué nodo padre, o que no pueda ser hijo inmediato, etc. Indica jerarquías. 
No se puede validar un atributo utilizando el valor de otro atributo. 
Se puede poner una restricción de ocurrencia a un elemento (sería usando minOc-curs y 
maxOccurs) 
4.3.2. Enlaces y direccionamiento 
Todo el procesamiento realizado con un fichero XML está basado en la posibilidad de direccionar o 
acceder a cada una de las partes que lo componen, de modo que podamos tratar cada uno de los \nelementos de forma diferenciada. 
El tratamiento del fichero XML comienza por la localización del mismo a lo largo del conjunto de 
documentos existentes en el mundo. 
Para llevar a cabo esta localización de forma unívoca, se utilizan los URI. 
4.3.3. XPath 
XPath, abreviación de lo que se conoce como XML Path Language. 
Hemos dicho, que el tratamiento de un fichero XML, comienza por su localización, una vez localizado, la 
forma de seleccionar información dentro de él es mediante el uso de XPath. 
XPath es un lenguaje declarativo para localizar nodos y fragmentos (texto, elementos, atributos…) \nen el árbol de un documento XML. 
Veamos algunas características de XPath: 
• Fue definido por el consorcio W3C. 
• Permite construir expresiones que recorren y procesan un documento XML. 
• Permite buscar y seleccionar teniendo en cuenta la estructura jerárquica del XML. 

<!-- Page 173 -->

 
 
Aplicaciones y desarrollo web 
173 
• Podemos seleccionar y hacer referencia a texto, elementos, atributos y cualquier otra 
información contenida dentro de un fichero XML sirve para decir cómo una hoja de estilo debe 
procesar el contenido de una página XML. 
• Sirve para poder poner enlaces o cargar en un navegador zonas determinadas de una página 
XML, en vez de toda la página. 
• Fue creado para su uso en el estándar XSLT, en el que se usa para seleccionar y examinar la \nestructura del documento de entrada de la transformación. 
• XPath en sí es un lenguaje sofisticado y complejo, pero distinto de los lenguajes procedurales 
que solemos usar (C, C++, Basic, Java...). 
• Aún está en estado de desarrollo, por lo que no es fácil encontrar herramientas que incorporen 
todas sus funcionalidades. 
La idea es parecida a las expresiones regulares para seleccionar partes de un texto sin atributos (plain 
text). 
También es la base sobre la que se han especificado nuevas herramientas como XPointer, XLink y 
XQuery, para el tratamiento de documentos XML. Herramientas tales. 
Se utiliza XPath para referir partes de documentos XML. Anteriormente XSL eran dos estándares 
separados: 
• XSLT: XSL Transformations: lenguaje que permite transformar un documento XML para 
obtener otro documento XML, un documento HTML o un documento de texto plano. 
La hoja de estilos XSLT con las reglas de transformación es también un documento de texto 
XML en sí, normalmente con extensión .xsl, por lo tanto, se podrá comprobar si está bien 
formado o no. 
XSLT es un lenguaje declarativo, no contiene una secuencia de instrucciones, sino plantillas a 
aplicar. 
• XSL Formatting Objects (XSL-FO): vocabulario para definir cómo presentar un documento XML. 
Una hoja de estilo XSL es una serie de reglas que determinan como va a ocurrir la transformación. 
Cada regla se compone de: 
• Pattern. Patrón de localización. 
• Template. Plantilla. 
Ventajas de usar hojas de estilo XML: 
• Centralizar la forma de presentación (formato). 
• Separar la estructura del contenido. 
• Reutilización de datos. 
• Diferentes formatos de salida para los mismos datos. 
• Unificar el estilo de presentación. 

<!-- Page 174 -->

 
 
Aplicaciones y desarrollo web 
174 
 
 
 
+ Info 
XQuery es el lenguaje que maneja los documentos XML como si de 
una base de datos se tratase. 
 
Localización con Xpath 
Una vez localizado, con Xpath, se selecciona la información que hay dentro de dicho fichero XML. 
Este "camino" puede presentar diversas formas: 
• Con sintaxis completa o abreviada: 
• Completa: se utiliza en caso de nodos y ejes a los que se accede con menor frecuencia. 
Ejemplo: 
/child::pelicula/child::director/child::nombre/attribut::apellido 
• Abreviada: se usa normalmente cuando se trata de nodos y ejes que son seleccionados con 
mucha frecuencia. 
Ejemplo: 
/pelicula/director/nombre/@apellido 
Hemos prescindido del nombre del eje child:: y el atributo se introduce anteponiendo el 
carácter @. 
• Como ruta de localización absoluta o relativa. 
• Absoluta: comienza por el nodo raíz, que es el nodo situado directamente sobre el \nelemento raíz. Esta distinción es necesaria, ya que desde el elemento raíz no sería posible 
acceder, por ejemplo, a comentarios o instrucciones que se encuentran fuera del mismo. 
Las rutas de localización constan de pasos de localización separados por /. 

<!-- Page 175 -->

 
 
Aplicaciones y desarrollo web 
175 
Ejemplo: 
/child::pais/child::capital/child::nombre 
En este caso se trata de una ruta absoluta que parte del nodo raíz que se indica mediante 
una barra diagonal. 
Desde ahí se selecciona el elemento raíz <pais>. 
La expresión generará un resultado si el elemento raíz tiene un nodo hijo <capital> y éste a 
su vez contiene un nodo hijo <nombre>. 
Los ejes se definen mediante el nombre del eje seguido de dos signos de dos puntos. 
• Relativa: al contrario de las absolutas, las rutas de localización relativas necesitan un nodo 
de contexto. La ruta se evaluará desde esta posición. 
En el eje child, puede omitirse la expresión child:: 
Así, la ruta de localización pais/capital/nombre equivale a la ruta del ejemplo con sintaxis 
abreviada. 
child::capital/child::nombre 
De igual forma que en la ruta absoluta, en este caso se generará un resultado si el nodo de 
contexto tiene un nodo hijo <capital>, que a su vez posee un nodo hijo <nombre>. 
Instrucciones en lenguaje XPath 
Una instrucción en lenguaje XPath se denomina una expresión. 
Una expresión puede incluir cierta variedad de operaciones sobre distintos tipos de operandos. 
Una expresión puede tener opcionalmente predicados. 
Un predicado es una «condición» que permite seleccionar un nodo con unos determinados atributos o 
características, es decir incluye un tipo de condición durante el paso de localización. 
Los predicados se indican entre corchetes y dan un valor booleano. 

<!-- Page 176 -->

 
 
Aplicaciones y desarrollo web 
176 
• Ejemplo de expresión: 
/oposicion/convocatoria/curso 
Esta expresión, hace referencia a todos los elementos "curso" que dependen de cualquier \nelemento "convocatoria" que dependen a su vez de cualquier elemento "oposición". 
XPath indicara la ruta a varios nodos en base a la estructura del documento XML. 
• Ejemplo de expresión con predicado: 
/oposicion/convocatoria/curso[@nombre=»unidad_didactica»]/alumno 
Hace referencia a todos los "alumnos", que pertenecen a los "cursos" que tiene como atributo 
nombre "unidad_didactica". 
Indicamos dentro de los corchetes [ ], que se cumpla una condición (<, =, > ) 
4.3.4. XPointer 
XPointer describe cómo se puede apuntar a un lugar específico dentro de un documento XML. 
Es una extensión de XPath que permite asociar a una dirección URI con una expresión XPath con 
algunas propiedades extras. 
4.3.5. XLink (XML Linking Language) 
Define la forma en la que los documentos XML se pueden relacionar entre sí definiendo nuevos tipos de \nelementos XML que representan enlaces. 
Utiliza XPointer para localizar recursos. 
4.3.6. XSL (eXtensible Stylesheet Language) 
Permite definir el estilo que se aplicará a cada elemento XML y transformar y/o presentar 
documentos XML. 

<!-- Page 177 -->

 
 
Aplicaciones y desarrollo web 
177 
El resultado puede ser: 
• Un documento HTML. 
• WML (para WAP). 
• Texto plano. 
• RTF. 
• PDF. 
4.3.7. WML (Wireless Markup Language) 
Es otro lenguaje cuyo origen es XML. 
Se utiliza para construir las páginas que aparecen en las pantallas de los teléfonos móviles dotados de 
tecnología WAP. 
WAP (Wireless Application Protocol o protocolo de aplicaciones inalámbricas) es un estándar abierto 
internacional para aplicaciones que utilizan las comunicaciones inalámbricas, como el acceso a servicios 
de Internet desde un teléfono móvil. 
4.3.8. KML: Keyhole Markup Languaje 
Es un lenguaje de marcado basado en XML para representar datos geográficos en tres dimensiones. 
4.4. Consultas XQuery 
XQuery proporciona un modo flexible de consulta para extraer datos de los documentos XML. Su 
objetivo es poder acceder a grupos de documentos XML como si fueran bases de datos relacionales de 
la misma forma que funciona SQL. 
Está basado en varias propuestas de lenguajes previas: 
• XMLQL. 
• YATL. 
• Lorel. 
• Quilt. 
Se ha integrado con XPath (versión 2.0). 

<!-- Page 178 -->

 
 
Aplicaciones y desarrollo web 
178 
4.5. Programación. Análisis XML 
El análisis XML es la interpretación de documentos XML para manipular su contenido, utilizando 
construcciones sensibles, ya sean "nodos", "atributos", "espacios de nombres", "documentos", o eventos 
relacionados con estas construcciones. 
Para manipular documentos XML (procesamiento de documentos en formato XML) desde programas, 
se utilizan APIs, que proporcionan un conjunto estándar de llamadas a funciones. 
Api de Java: JAXP (Java Api XML Procesing) 
Java tiene una API nativa para el manejo de documentos XML, llamada JAXP, o API de Java para el 
procesamiento XML. 
JAXP y una implementación de referencia se han incluido en todas las versiones de Java (desde JAXP 
v1.1 para Java 1.4, evolucionando hasta JAXP 1.6 para Java 8). 
La API JAXP, proporciona diferentes formas de interactuar con documentos XML, que son: 
• La interfaz DOM (Document Object Model): 
Modelo de Objeto de Documento, es una especificación de W3C orientada a objetos que facilita \nel acceso al documento XML completo. 
Los programadores pueden construir documentos, navegar por su estructura, y añadir, modificar, 
o eliminar elementos y contenido. Se puede acceder casi a cualquier cosa que se encuentre en un 
documento HTML o XML, modificando, borrando o añadiendo utilizando DOM. 
Varias versiones de JAXP han admitido varios niveles de especificación de DOM (hasta el nivel 3). 
Con DOM, un documento XML se representa como un árbol, permite navegar de un Node a su 
padre, sus hijos o sus hermanos (aunque, no todos los Node pueden tener hijos, por ejemplo, los 
nodos de Text son finales en el árbol, y nunca tener hijos). Las etiquetas XML se representan 
como Elementos, que amplían notablemente el Node con métodos relacionados con atributos. 
Como el árbol reside en la memoria, los árboles DOM no siempre son prácticos para grandes 
documentos XML, la construcción del árbol no es siempre la forma más rápida de tratar con el 
contenido XML, especialmente si no se está interesado en todas las partes del documento XML. 
• La interfaz SAX (Simple API for XML): 
Está pensada para leer con rapidez documentos XML y reaccionar en función de su contenido. 
SAX es una API orientada a eventos para tratar con documentos XML, donde los componentes 
del documento XML se interpretan como eventos (por ejemplo, "se ha abierto una etiqueta", 
"se ha cerrado una etiqueta", "se ha encontrado un nodo de texto", "se ha encontrado un 
comentario"). 

<!-- Page 179 -->

 
 
Aplicaciones y desarrollo web 
179 
SAX utiliza un enfoque de "análisis de inserción", donde un Parser SAX es responsable de 
interpretar el documento XML e invoca métodos en un delegado (un ContentHandler) para 
tratar cualquier evento que se encuentre en el documento XML. 
Características: 
• Está orientado a eventos. 
• El documento se procesa de manera secuencial. 
• Cada elemento XML dispara un evento. 
• Ventaja respecto a DOM: 
SAX supera las limitaciones de la interfaz DOM ya que mantiene solo los datos mínimos 
necesarios en el nivel del analizador (por ejemplo, contextos de espacios de nombres, \nestado de validación), por lo tanto, solo las informaciones que guarda ContentHandler, son 
guardado en la memoria, siendo el responsable el desarrollador. 
• Desventaja respecto a DOM: 
Con SAX, no es posible "retroceder en el tiempo / el documento XML", mientras que DOM 
permite que un Node regrese a su padre, (posibilidad que no existe en SAX). 
• La interfaz StAX (Streaming API para XML). 
Es la más actual de JAXP, provee una alternativa a SAX y DOM, otorgando el control del parseo 
al programador, basándose en iterador simple. StAX permite lograr un alto rendimiento en la 
iteración, procesado y modificación de documentos XML especialmente en entornos donde se 
disponga de poca cantidad de memoria y limitada capacidad de extensibilidad. 
StAX comienza con XMLStreamReader (o XMLEventReader), para que el desarrollador puede 
preguntar a nextEvent() 
StAX consta realmente de 2 distintas API: 
• Cursor API: Representa un cursor con el cual se puede ir hacia adelante en un documento 
XML desde el principio hasta el final, siempre se mueve hacia adelante, nunca hacia atrás, y 
puede apuntar un elemento a la vez. 
• Iterator API: Representa un flujo de un documento XML como un conjunto de objetos de \neventos discretos, que son sacados por la aplicación y provistos por el parseador en el 
orden en que son leídos en la fuente del documento XML. 
En este caso, uno puede aferrarse a los objetos de eventos ubicados al principio de XML, lo 
que no puede realizarse cuando utilizamos la Cursor API, (cuando se mueve el cursor hacia \nel próximo evento, no se tiene información sobre el evento previo). 
Es menos eficiente en cuanto a memoria que el Cursor. 

<!-- Page 180 -->

 
 
Aplicaciones y desarrollo web 
180 
 
 
 
Conclusiones 
La API StAX al igual que SAX tiene un enfoque impulsado por \neventos, pero StAX es un analizador de extracción, y SAX un 
analizador de inserción. 
En SAX, el "Parser" está en control y utiliza devoluciones de 
llamada en el "ContentHandler". 
En StAX, el programador llama al analizador y controla cuándo 
obtener el siguiente "evento" XML (si lo requiere). 
 
 
• TrAX. 
Es un grupo de clases que permiten interoperabilidad Java entre los diversos XSL Engines, esto 
permite migración entre herramientas utilizadas en XSL. 
XSL Engine es un software requerido para poder utilizar XSL. Todos los diversos "XSL Engines" 
ya incluyen un "Parser" en su distribución (Xalan incluye el "parser" Xerces, LotusXSL también 
utiliza Xerces...etc) 
Api de Java: JDOM 
Es una biblioteca de código abierto para manipulaciones de datos XML optimizados para Java. 
JDOM es recomendable para la edición o cambios en documentos XML. 
Aunque es similar a DOM del consorcio World Wide Web (W3C), es una alternativa como documento 
para modelado de objetos que no está incluido en DOM. 
La principal diferencia, es que, mientras que DOM fue creado para ser un lenguaje neutral e inicialmente 
usado para manipulación de páginas HTML con JavaScript, JDOM se creó específicamente para usarse 
con Java, y por lo tanto, beneficiarse de las características de Java, incluyendo sobrecarga de métodos, 
colecciones, etc. 
Para los programadores de Java, JDOM es una extensión más natural y correcta. 
 

<!-- Page 181 -->

 
 
Aplicaciones y desarrollo web 
181 
 
 
 
Anécdota 
Aunque lo parezca… 
El propio proyecto de JDOM, ha desmentido que JDOM, no es un 
acrónimo de Java Document Object Model (Documento de 
Modelado de Objetos en Java). 
 
El Análisis y la Programación con XML en JAVA: JAXB 
El análisis y la programación con XML en Java pueden beneficiarse de diversas tecnologías que permiten 
trabajar con datos XML de manera eficiente. Una de las herramientas más destacadas es JAXB (Java 
Architecture for XML Binding), que facilita el mapeo entre elementos XML y clases Java de manera 
sencilla y flexible. 
JAXB es una tecnología estándar de Java que permite convertir entre XML y objetos Java. A través de este 
proceso de vinculación (binding), JAXB permite la conversión automática entre los elementos de un 
archivo XML y las clases Java correspondientes, lo que simplifica el proceso de deserialización (convertir 
XML a objetos) y serialización (convertir objetos a XML). Este proceso es especialmente útil cuando se 
trabaja con datos XML que necesitan ser procesados en aplicaciones Java de manera estructurada. 
JAXB utiliza anotaciones en las clases Java para definir cómo se debe mapear el XML a los objetos Java. 
Automatiza el proceso de serialización y deserialización, lo que simplifica el manejo de datos XML. 
Es Compatible con esquemas XML (XSD). Se integra fácilmente con esquemas XML, permitiendo que el 
mapeo se ajuste a las restricciones definidas en un esquema XSD. 
Otras tecnologías relacionadas con XML en Java 
Si bien JAXB es una excelente opción para trabajar con XML, existen otras tecnologías que también 
pueden ser útiles dependiendo de los requerimientos específicos de la aplicación. 
• JAXP (Java API for XML Processing): Esta API permite trabajar con XML de manera más general, 
proporcionando herramientas para procesar XML a través de SAX (Simple API for XML) y DOM 
(Document Object Model). JAXP es útil cuando se necesita leer y manipular XML de manera 
más flexible, sin necesidad de hacer el mapeo directo a objetos Java como en JAXB. 
• JAX-RS (Java API for RESTful Web Services): Aunque no está directamente orientado al mapeo 
de XML, JAX-RS es relevante si se están desarrollando servicios web RESTful en los que los datos 
se intercambian en formato XML o JSON. Se puede integrar con JAXB para convertir los datos 
XML recibidos o enviados en los servicios REST a objetos Java. 
• JAX-B (Java Architecture for XML Binding): Algunas veces se hace referencia a JAXB como JAX-
B, ya que forma parte de las especificaciones de Java API para XML (JAX) y es fundamental para \nel manejo de datos XML en Java. 

<!-- Page 182 -->

 
 
Aplicaciones y desarrollo web 
182 
Para trabajar con XML en Java, JAXB es una de las opciones más destacadas, especialmente cuando se 
busca un mapeo directo entre XML y objetos Java. Sin embargo, tecnologías como JAXP ofrecen mayor 
control y flexibilidad en la manipulación de XML, y JAX-RS es esencial si se desarrollan servicios web que 
intercambian datos en formato XML. Dependiendo de la complejidad y los requisitos del proyecto, se 
puede elegir la tecnología adecuada o combinarlas para aprovechar lo mejor de cada una. 
4.6. Lenguaje de marcado para confirmaciones de seguridad 
Conocido como SAML, del inglés, Security Assertion Markup Language. 
SAML es un estándar abierto que define un esquema XML para el intercambio de datos de autenticación 
y autorización. Este estándar fue creado por el Security Services Technical Committee (SSTC), bajo la 
supervisión de OASIS (Organization for the Advancement of Structured Information Standards). 
La especificación SAML define tres roles: 
• Principal. 
• Proveedor de identidad: entidad que dispone de la infraestructura necesaria para la 
autenticación de los usuarios. 
• Proveedor de servicio: entidad que concede a un usuario el acceso o no a un recurso. 
El funcionamiento, consiste en que, el rol principal solicita un servicio al proveedor de servicios, quien a 
su vez solicita y obtiene en caso de éxito, una confirmación de identidad desde el proveedor de 
identidad. Teniendo como base la confirmación recibida, el proveedor de servicio puede tomar 
decisiones acerca del acceso autorizado a un usuario. 
5. JSON 
 
Fuente: 
https://ca.wikipedia.org/wiki/Fit
xer:JSON_vector_logo.svg 
JSON es el acrónimo de JavaScript Object Notation, en castellano notación de objeto de JavaScript. 

<!-- Page 183 -->

 
 
Aplicaciones y desarrollo web 
183 
Es un formato de texto sencillo para el intercambio de datos. 
Se trata de un subconjunto de la notación literal de objetos de JavaScript, aunque, debido a su amplia 
adopción como alternativa a XML, se considera, a partir de 2019, un formato independiente del 
lenguaje. 
Una de las supuestas ventajas de JSON sobre XML como formato de intercambio de datos es que resulta 
mucho más sencillo escribir un analizador sintáctico (parser) para él. 
En JavaScript, un texto JSON se puede analizar fácilmente usando la función eval(), algo que (debido a 
la ubicuidad de JavaScript en casi cualquier navegador web) ha sido fundamental para que haya sido 
aceptado por parte de la comunidad de desarrolladores AJAX. 
En la práctica, los argumentos a favor de la facilidad de desarrollo de analizadores o de sus rendimientos 
son poco relevantes, debido a las cuestiones de seguridad que plantea el uso de eval() y el auge del 
procesamiento nativo de XML incorporado en los navegadores modernos. 
Por esa razón, JSON se emplea habitualmente en entornos donde el tamaño del flujo de datos entre 
cliente y servidor es de vital importancia (de aquí su uso por Yahoo!, Google, Mozilla, etc., que atienden 
a millones de usuarios) cuando la fuente de datos es explícitamente de fiar y donde no es importante el 
hecho de no disponer de procesamiento XSLT para manipular los datos en el cliente. 
Si bien se tiende a considerar JSON como una alternativa a XML, lo cierto es que no es infrecuente el uso 
de JSON y XML en la misma aplicación; así, una aplicación de cliente que integra datos de Google Maps 
con datos meteorológicos en SOAP necesita hacer uso de ambos formatos. 
En diciembre de 2005, Yahoo! comenzó a dar soporte opcional de JSON en algunos de sus servicios web. 
Sintaxis de JSON 
Indicamos unas reglas de sintaxis que deben cumplirse en JSON: 
• Todos los datos del archivo deben estar rodeados de llaves { } 
• Objects (objetos): 
Los objetos son listas de parejas nombre / valor 
• Los objetos se escriben entre llaves { } 
• El nombre y el valor están separados por dos puntos : 
• Las parejas están separadas por comas , 
• Los nombres de las parejas se escriben siempre entre comillas dobles " " 
• Un arreglo se indica entre corchetes [ ] 

<!-- Page 184 -->

 
 
Aplicaciones y desarrollo web 
184 
• Las comillas simples no están permitidas. 
• Los números no deben ir entre comillas dobles. 
• Si se indican entre comillas dobles se tratan como cadenas de texto en lugar de como números. 
• Un tipo de dato null no debe ir entre comillas dobles. 
• Terminaciones: 
• A excepción del último elemento, cada par llave:valor debe terminar con una coma , 
• Si hay un solo objeto dentro de un arreglo debe terminar con una coma , 
• Los valores booleanos únicamente pueden ser verdaderos o falsos. 
Tipos de datos en JSON 
Los tipos de datos disponibles con JSON son: 
• Números: 
Se permiten números negativos y opcionalmente pueden contener parte fraccional separada 
por puntos. Ejemplo: 123.456. 
• Cadenas: 
Representan secuencias de cero o más caracteres. Se ponen entre doble comilla y se permiten 
cadenas de escape. Ejemplo: "Hola". 
• Booleanos: 
Representan valores booleanos y pueden tener dos valores: true y false. 
• Null: 
Representan el valor nulo. 
• Array: 
Representa una lista ordenada de cero o más valores los cuales pueden ser de cualquier tipo. Los 
valores se separan por comas y el vector se mete entre corchetes. Ejemplo 
["juan","pedro","jacinto"]. 
• Objetos: 
Son colecciones no ordenadas de pares de la forma <nombre>: <valor> separados por comas y 
puestas entre llaves. El nombre tiene que ser una cadena y entre ellas. El valor puede ser de 
cualquier tipo. 

<!-- Page 185 -->

 
 
Aplicaciones y desarrollo web 
185 
Ejemplo: 
{"departamento":7,"nombredepto":"Docentes","director": "Jose Parra", "empleados": 
[{"nombre":"Pedro", "apellido": "Fernadez},{"nombre": Micaela","apellido":Escobar}]} 
JavaScript cuenta con dos funciones nativas que forman parte del estándar ECMAScript y tienen por fin 
facilitar el manejo de datos JSON (JavaScript Objetc Notation). 
• JSON.parse(): convertirá una cadena JSON en un objeto de JavaScript. 
• JSON.stringify(): tendrá la función inversa, convertir un objeto JavaScript en cadena JSON. 
Ambas funciones operativas en la gran mayoría de navegadores modernos. 
6. Content Management System (CMS) 
CMS son las siglas de Content Management System (Sistema de Gestión de Contenidos). Un CMS es un 
software diseñado para facilitar la creación, administración y gestión de contenido digital, permitiendo 
a los usuarios -administradores, editores o colaboradores- manejar dicho contenido en una plataforma 
sin necesidad de conocimientos de programación. 
Aunque tradicionalmente se ha vinculado a la creación y mantenimiento de sitios web, un CMS también 
puede utilizarse en otros entornos como blogs, portales, intranets o sistemas de gestión documental. 
El CMS proporciona una interfaz que interactúa con una o varias bases de datos donde se almacena el 
contenido. Esta arquitectura permite separar el contenido del diseño o presentación, lo que facilita 
modificaciones visuales sin alterar la información. Esta separación mejora el mantenimiento, la 
flexibilidad del sistema y la posibilidad de reutilizar contenidos en distintos contextos. Además, permite 
una publicación controlada y colaborativa: múltiples usuarios pueden gestionar, revisar o publicar 
contenido de forma simultánea, con control de versiones, asignación de roles y flujos de trabajo 
definidos. 
Aunque todos los CMS comparten la finalidad de gestionar información digital, no todos están 
orientados al mismo tipo de contenido ni al mismo entorno. Podemos distinguir principalmente tres 
categorías: 
• WCMS (Web Content Management Systems). 
• Constructores web y plataformas SaaS. 
• Sistemas de gestión documental (ECM/DMS). 

<!-- Page 186 -->

 
 
Aplicaciones y desarrollo web 
186 
6.1. WCMS (Web Content Management Systems) 
Los WCMS están diseñados específicamente para la creación, organización y publicación de contenido \nen sitios web. Permiten a los usuarios gestionar desde textos hasta contenido multimedia, sin necesidad 
de conocimientos técnicos. Suelen incluir funciones como edición visual, plantillas de diseño, 
programación de publicaciones, SEO integrado y gestión de usuarios y permisos. 
• Edición visual (WYSIWYG). 
• Plantillas de diseño personalizables. 
• Programación de publicaciones. 
• Herramientas SEO integradas. 
• Gestión de usuarios y permisos. 
Estos sistemas son especialmente útiles en proyectos web con múltiples editores, ya que facilitan flujos 
de aprobación, control editorial y análisis del rendimiento del contenido. 
6.1.1. Principales WCMS 
• WordPress: El WCMS de código abierto más popular (impulsa más o menos el 40% de webs a 
nivel global). Desarrollado por la comunidad WordPress, con contribuciones de Automattic 
(empresa detrás de WordPress.com). En España, es la base de medios como Marca o El 
Confidencial, y del 37% del e-commerce gracias a WooCommerce. 
• Joomla: Lanzado en 2005, Joomla ha mantenido una cuota de mercado modesta, pero estable, 
gracias a su flexibilidad. Es una solución sólida para proyectos que requieren estructuras de 
contenido más complejas que las que WordPress permite sin extensiones. 
• Drupal: Es un WCMS especialmente valorado por su seguridad, escalabilidad y control granular. 
Su uso es habitual en portales institucionales, universidades y organismos públicos. En España, 
sustenta diversos sitios del Gobierno y de universidades públicas. Ofrece una arquitectura muy 
flexible, pero con una curva de aprendizaje más pronunciada. 
• Magnolia CMS: Destinado al entorno empresarial, Magnolia es un WCMS de código abierto 
desarrollado en Java. Utiliza el estándar JSR-170 (Java Content Repository), lo que le permite 
integrarse con sistemas corporativos antiguos (legacy). Su arquitectura modular y su soporte 
multicanal lo hacen ideal para grandes organizaciones que requieren personalización avanzada e 
integración con herramientas de marketing digital. Su tecnología es Java + JCR.  
 

<!-- Page 187 -->

 
 
Aplicaciones y desarrollo web 
187 
 
 
 
+Info 
JSR-170 es un estándar Java que permite a distintos CMS basados \nen Java, como AEM (Adobe Experience Manager) o Magnolia, 
gestionar contenidos mediante una misma API, evitando depender 
de APIs propietarias. 
 
 
Aunque comparten propósito, estos sistemas tienen diferencias en su enfoque técnico. WordPress, 
Joomla y Drupal están basados en PHP y utilizan bases de datos como MySQL o MariaDB, mientras que 
Magnolia apuesta por una arquitectura Java más compleja y adaptable. 
WCMS especializados en e-commerce 
• PrestaShop: Aunque su objetivo principal es el comercio electrónico, incluye herramientas de 
CMS para crear páginas informativas. Nació en 2007 y ha sido ampliamente adoptado por su 
buena adaptación al mercado español, permitiendo operar con TPVs, normas fiscales locales y 
gestión multitienda. Marcas como Druni o Sprinter confiaron en él en sus primeras etapas. Es 
una solución open-source para tiendas online, desarrollada por PrestaShop SA (ahora parte de 
Symfony SAS). Trabaja con la tecnología: PHP + MySQL. 
6.1.2. Ciclo completo de gestión de contenidos: publicación, 
retirada y archivado 
El ciclo de publicación y retirada de contenidos es un proceso fundamental en cualquier Web Content 
Management System (WCMS). Este flujo de trabajo organizado permite gestionar de manera integral el 
contenido digital, desde su creación hasta su retirada o archivado, facilitando la administración 
centralizada de todos los elementos de un sitio web. 
Creación y aprobación: 
El proceso comienza con la elaboración del contenido mediante las herramientas integradas en el 
WCMS. Los creadores pueden redactar textos, incorporar elementos multimedia y aplicar formatos sin 
necesidad de conocimientos técnicos avanzados. Una vez finalizado, el material pasa por un proceso de 
validación, donde editores y responsables verifican su calidad, precisión y adecuación antes de autorizar 
su publicación. 

<!-- Page 188 -->

 
 
Aplicaciones y desarrollo web 
188 
Publicación: 
Tras la aprobación, el sistema ofrece diversas opciones de publicación, desde la activación inmediata 
hasta la programación automatizada en fechas específicas. Esta flexibilidad permite mantener el sitio 
web actualizado, incluso con contenidos que deben publicarse fuera del horario laboral o en momentos \nestratégicos. 
Mantenimiento y actualización: 
Los WCMS facilitan la edición continua del contenido publicado a través de interfaces intuitivas. Cada 
modificación queda registrada en un historial de versiones, lo que permite comparar cambios o 
restaurar ediciones anteriores si es necesario. Además, el sistema puede generar alertas cuando el 
contenido requiere revisión por obsolescencia o cambios en el contexto informativo. 
Retirada del contenido: 
Cuando el contenido pierde relevancia o es reemplazado, se procede a su retirada. Los WCMS permiten \neliminarlo de la vista pública sin borrarlo definitivamente, preservando así la integridad del sitio. En 
algunos casos, el contenido retirado no se elimina, sino que se archiva para su conservación o posible 
recuperación futura. 
Archivado estratégico: 
El archivado representa la última fase del ciclo de gestión de contenidos en un WCMS, completando el 
recorrido que inicia con la creación, pasa por la publicación, actualización y retirada. Esta etapa no es un 
simple almacenamiento, sino un proceso activo de preservación digital, donde los contenidos retirados 
se organizan sistemáticamente en repositorios especializados. Mediante metadatos estructurados 
(fechas, autores, etiquetas temáticas), el sistema permite recuperar fácilmente cualquier material 
archivado cuando sea necesario. 
Esta fase se caracteriza por tres aspectos clave: 
• La preservación del valor a largo plazo de la información. 
• El cumplimiento de normativas legales sobre conservación de datos. 
• La gestión del conocimiento institucional. 
Plataformas como WordPress y Drupal incluyen funcionalidades específicas para este proceso, desde 
plugins de conversión a formatos archivables hasta módulos que automatizan la transferencia de 
contenidos según fechas de expiración. El archivado garantiza que, aunque los contenidos ya no estén 
activos, sigan accesibles para auditorías, consultas históricas o posibles reactivaciones, preservando el 
patrimonio digital de la organización. 
Este ciclo no solo optimiza la gestión del contenido, sino que también asegura que el sitio web se 
mantenga actualizado y organizado, al tiempo que conserva un historial completo de todas las 
versiones para cumplir con requisitos legales o de referencia futura. 

<!-- Page 189 -->

 
 
Aplicaciones y desarrollo web 
189 
6.2. Constructores web y plataformas SaaS 
Además de los WCMS tradicionales, han emergido plataformas de tipo SaaS (Software as a Service) que 
permiten crear y gestionar sitios web sin necesidad de instalar software ni gestionar servidores. Aunque 
ofrecen funcionalidades de gestión de contenidos, no se consideran WCMS en sentido técnico estricto por 
su arquitectura cerrada y falta de acceso al núcleo del sistema. Las dos más destacadas en España son: 
• Shopify: Plataforma canadiense orientada al comercio electrónico, desarrollada principalmente \nen Ruby on Rails + Liquid. Se ha convertido en una de las opciones más populares por su 
facilidad de uso y su modelo todo-en-uno: incluye hosting, actualizaciones y soporte técnico. 
Ofrece plantillas, gestión de productos, herramientas de marketing y pasarelas de pago 
integradas. En España, ha ganado cuota de mercado entre emprendedores digitales gracias a su 
rapidez de despliegue y su integración con medios de pago locales como Bizum.  
• Wix: Plataforma israelí que permite crear sitios web mediante un editor visual (drag-and-drop). 
Está programada principalmente en JavaScript (Node.js y React) y cuenta con su propio \nentorno de desarrollo llamado Velo by Wix. Está orientada a pequeños negocios y profesionales 
autónomos que necesitan una solución rápida y sin complicaciones técnicas. Según datos 
recientes, cerca del 65 % de sus usuarios en España son micropymes que valoran su relación 
calidad-precio. 
Ambas plataformas permiten gestionar contenido, pero su naturaleza cerrada, su dependencia del 
proveedor y sus limitaciones para desarrolladores hacen que no se clasifiquen como WCMS 
tradicionales. 
6.3. Sistemas de gestión documental (ECM/DMS) 
Sistemas de gestión documental (ECM/DMS) 
Más allá de la gestión de contenidos web, existen CMS especializados en la gestión documental dentro 
de organizaciones. Estos sistemas se conocen como ECM (Enterprise Content Management) y DMS 
(Document Management Systems) y están diseñados para gestionar documentos, automatizar flujos 
de trabajo, cumplir normativas y organizar información interna. Su objetivo no es publicar contenido 
web, sino garantizar un acceso seguro, trazable y estructurado al contenido digital de la empresa. Entre 
los más destacados están: 
• Alfresco: Plataforma de código abierto muy utilizada en la administración pública y grandes \nempresas. Permite controlar versiones, gestionar permisos, crear flujos de trabajo documentales 
y garantizar el cumplimiento normativo. 
• SharePoint (Microsoft): Integrado en el ecosistema Microsoft 365, es una herramienta 
ampliamente adoptada para la creación de intranets, gestión documental y colaboración en \nequipos. Permite compartir documentos, automatizar procesos y acceder a los archivos desde 
cualquier lugar. 

<!-- Page 190 -->

 
 
Aplicaciones y desarrollo web 
190 
• Nuxeo: Solución orientada a la gestión de activos digitales (DAM), como imágenes, vídeos y 
documentos multimedia. Es conocida por su escalabilidad y capacidad de personalización en \nentornos empresariales complejos. 
• OpenText Content Suite: Sistema robusto, especialmente enfocado a sectores regulados como 
la sanidad o las finanzas. Ofrece control de acceso, cumplimiento legal, archivado digital y 
trazabilidad completa de documentos. 
7. Desarrollo de aplicaciones móviles 
Una aplicación móvil es un pequeño programa creado para ser utilizado en los dispositivos móviles 
(Tablets y móviles). 
El término app es una abreviatura de la palabra en inglés application, utilizado para referirse a las 
aplicaciones móviles. 
Para poder crear aplicaciones que se puedan utilizar en móviles con diferentes resoluciones, debes 
realizar un desarrollo de aplicaciones multiplataforma. 
La aplicación creada debe adaptarse a la pantalla, sea cual sea el dispositivo que utilice el usuario. 
Tipos de desarrollo de apps 
Podemos crear Apps para Android o Apps para iOS. 
Hay tres tipos de tecnologías de desarrollo de aplicaciones móviles, (dónde el coste económico es 
diferente): 
• Desarrollo de aplicaciones nativas. 
• Desarrollo de aplicaciones web. 
• Desarrollo de aplicaciones híbridas. 
7.1. Aplicación nativa o app nativa 
Una app nativa está desarrollada y optimizada para una plataforma concreta (sistema operativo), con 
un lenguaje de programación específico, por tanto, está 100% adaptada a las funcionalidades y 
características del dispositivo para ofrecer una mejor experiencia de usuario y de uso. 
• Ventajas de las Apps nativas: 
• Acceso a todas las características del dispositivo. 
• Tienen capacidades de uso de funcionalidades hardware. 
• Ofrecen funcionalidades en segundo plano. 

<!-- Page 191 -->

 
 
Aplicaciones y desarrollo web 
191 
• Las apps nativas envían y reciben notificaciones push (mensajes que informan al usuario de 
novedades las apps que tienen instaladas). 
• Funcionan en un entorno offline, es decir, no es necesario tener conexión a Internet para 
utilizar la App, se realizar todo el código en el dispositivo móvil. 
Como consecuencia, tanto el tiempo de carga, la ejecución y velocidad es más rápida, 
mejorando la experiencia del usuario, interactúan mucho mejor con el dispositivo. 
• Desventajas de las apps nativas: 
• El desarrollo es más complejo, lento y más caro. 
La aplicación hay que desarrollarla para todas las versiones de cada sistema operativo. 
• Ejemplos Apps Nativas: 
• Facebook. 
• Twitter. 
• Instagram. 
• Whatsapp. 
• Wallapop. 
Dentro de las aplicaciones web nativas, están las autocontenidas. 
En estas aplicaciones, todo su contenido se encuentra autocontenido dentro de la misma aplicación, por 
lo que contenido es estático; información, menús, imágenes…, no cambian casi nunca. 
Un ejemplo sería una calculadora, dónde no es necesario hace ningún cambio, si lo deseamos podemos 
cambiar el color de los números, o tamaño… pero son cambios no necesarios para que siga funcionando 
correctamente. 
 
 
 
 
+ Info 
Spring Boot es una plataforma que permite el desarrollo de 
aplicaciones web "autocontenidas" que llevan embebido el 
contenedor servlets. 
(El servlet es una clase en el lenguaje de programación JAVA). 
 

<!-- Page 192 -->

 
 
Aplicaciones y desarrollo web 
192 
7.2. Aplicación web o web app 
Son Apps universales, multiplataforma cuyo uso es desde cualquier sistema operativo. 
La característica principal de este tipo es que no consume memoria interna del teléfono, ya que se 
almacena en la red, por tanto, requiere una única instalación, y cualquier navegador puede ejecutarla. 
Normalmente este tipo de aplicación es utilizada por empresas y multinacionales, para que los \nempleados puedan utilizar programas específicos para realizar su trabajo sin tener que instalar las 
aplicaciones en sus ordenadores, lo que también mejora el mantenimiento de dichos ordenadores, al 
igual que de la aplicación. 
• Ventajas de las Apps web: 
• Menor tiempo para el desarrollo app web y coste más económico que en las aplicaciones 
nativas. 
• Mantenimiento rápido y sencillo. 
» Solo es necesario un navegador actualizado. 
» Siempre se accede a la última versión. 
• No hay de incompatibilidades. 
Funcionan por el navegador, por lo que es compatible con ordenadores, portátiles, tablets y 
Smartphone siendo indiferente el sistema operativo. 
• No ocupa espacio en el disco duro, ni ocupan memoria en los móviles. 
El ahorro en espacio es disco duro, es especialmente importante con la reciente aparición \nen el mercado de los "ordenadores ultrabooks", que son muy potentes, pero con poca 
capacidad de almacenamiento. 
• Desventajas de las aplicaciones web: 
• Requieren de conexión a Internet para funcionar. 
• No son aplicaciones multitareas ni permiten funcionalidades en segundo plano. 
• Necesitan espacio web. 
• Las web apps pueden ser más lentas que las apps nativas. 
• Ejemplos Apps web: 
• Google Docs: 
Utilizada para crear y guardar documentos a través de la cuenta de Drive. 

<!-- Page 193 -->

 
 
Aplicaciones y desarrollo web 
193 
• Pixlr.com: 
Aplicación web diseñada para la edición fotográfica. 
• Evernote o Trello: 
Son dos aplicaciones web para organizar tareas mediante tarjetas. Evernote está más 
pensado para el uso particular mientras Trello está orientado a las empresas por su 
flexibilidad para compartir tareas. 
• Netflix: 
La plataforma de vídeo en streaming más importante del momento. 
7.3. Aplicaciones híbridas 
Los usuarios solicitan cada vez más aplicaciones móviles multiplataforma, por lo que las empresas 
deben poder realizar un desarrollo rápido. 
Para ello, una de las mejores respuestas que se puede dar a esa petición de los usuarios son las 
aplicaciones móviles híbridas. 
Una aplicación móvil híbrida es aquella que intenta mezclar lo mejor de las apps nativas y de las apps web. 
Las aplicaciones híbridas tienen la versatilidad del desarrollo web y la capacidad de adaptación a los 
dispositivos como si fuera una app nativa. 
Un ejemplo de App híbrida es Ulabox, un supermercado online. 
Ionic Framework 
Está diseñado para el desarrollo de aplicaciones móviles híbridas. 
Fue creado por Max Lynch, Ben Sperry y Adam Bradley de Drifty Co. en 2013. 
La versión original fue lanzada en 2013 y construida sobre AngularJS y Apache Cordova. 
7.3.1. Plataformas para el desarrollo de Apps 
Debido al gran uso de los dispositivos móviles y el gran avance en sus prestaciones y en el aumento de la 
velocidad de transmisión de redes, cada vez los desarrolladores de apps disponen de más opciones para 
desarrollar proyectos multiplataforma para iOS, Android y Windows Phone. 

<!-- Page 194 -->

 
 
Aplicaciones y desarrollo web 
194 
Algunas de las más populares son: 
(Fuente: https://www.cice.es/noticia/top-5-plataformas-desarrollo-ios-android/) 
• Xamarin. 
Es la plataforma favorita de muchos desarrolladores, interesados en ofrecer apps nativas para 
iOS, Android. Y ahora, que ha sido adquirida por Microsoft, también para Windows. 
Su principal ventaja frente a las soluciones oficiales de Apple y Google, es su versatilidad para el 
desarrollo multiplataforma. 
Xamarin.Forms 
Es un framework de desarrollo (que forma parte de Xamarin), de interfaces de usuario comunes para 
iOS y Android. Los desarrolladores pueden usar una API (interfaz de programación de aplicaciones) 
unificada y compartir el código resultante entre plataformas. Práctica que evita el código redundate y la 
reutilización del mismo a la hora de crear interfaces de usuario para sus aplicaciones. 
.NET MAUI 
.NET MAUI es la evolución de Xamarin.Forms y su finalidad es el desarrollo en C# y .NET de aplicaciones 
de escritorio nativas para macOS, iOS, Android y Windows con el uso de un único código base en el \necosistema .NET. De hecho forma parte del planteamiento de unificación de .NET, por esta razón se 
integra con .NET 6 y versiones posteriores. 
• AppMachine. 
Es una plataforma de pago para principiantes. Ofrece un constructor visual con un asistente 
organizado por diferentes categorías de diseño, desarrollo, configuración, promoción, 
publicación y análisis de métricas, y además permite importar datos desde una web, redes 
sociales o servicios web mediante ficheros Excel, XML o JSON. 
• PhoneGap. 
Producido por Nitobi, y comprado posteriormente por Adobe Systems, permite a los 
programadores desarrollar aplicaciones para dispositivos móviles utilizando herramientas 
genéricas tales como JavaScript, HTML5 y CSS3. Las aplicaciones resultantes son híbridas. 
• Appery.ip. 
Esta plataforma, está basada en la nube y no requiere de instalación en el disco duro local. 
• Appcelerator. 
Es una plataforma de pago basada en Eclipse, utilizar la tecnología web y los estándares abiertos 
como JavaScript para crear apps compatibles y también ofrece funcionalidades de verificación 
automatizada para depurar errores. 

<!-- Page 195 -->

 
 
Aplicaciones y desarrollo web 
195 
7.4. NDK y SDK: Herramientas complementarias 
para Android 
SDK y NDK pueden usarse conjuntamente, siguen filosofías diferentes. Mientras el SDK prioriza 
productividad y abstracción, el NDK se centra en rendimiento y control. En la práctica, muchas 
aplicaciones utilizan ambos: el SDK para la mayoría de componentes y el NDK solo para las partes 
críticas que requieren optimización extrema. 
Ejemplos notables incluyen aplicaciones de realidad aumentada, donde la interfaz puede desarrollarse 
con SDK (Kotlin/Java) mientras los algoritmos de visión por computador se implementan con NDK 
(C/C++). Esta aproximación híbrida permite equilibrar productividad y rendimiento. 
7.4.1. Android SDK (Software Development Kit) 
El Android SDK (Software Development Kit) constituye la base fundamental para el desarrollo de 
aplicaciones Android. Desde su creación, ha proporcionado a los desarrolladores las herramientas 
necesarias para crear aplicaciones utilizando principalmente Java y, posteriormente, Kotlin. Este kit 
incluye componentes esenciales como Android Studio (el entorno de desarrollo oficial), el emulador de 
Android para pruebas, y un completo conjunto de bibliotecas estándar para interactuar con el sistema 
operativo. 
Originalmente basado en Java, el SDK evolucionó para incorporar Kotlin como lenguaje preferente, \nespecialmente después de que Google lo declarara lenguaje oficial en 2019. Kotlin ofrece ventajas 
significativas como una sintaxis más concisa (reduciendo aproximadamente un 40% de código 
comparado con Java), seguridad nula que elimina los NullPointerException, y características modernas 
como corrutinas para programación asíncrona. Sin embargo, Java sigue siendo relevante en proyectos 
heredados y equipos con experiencia consolidada en este lenguaje. 
El SDK está diseñado para la mayoría de casos de uso en desarrollo móvil, permitiendo crear 
aplicaciones con interfaces gráficas complejas y funcionalidades estándar sin necesidad de acceder 
directamente al hardware. Su arquitectura basada en APIs de alto nivel ofrece productividad y facilidad 
de mantenimiento, siendo ideal para aplicaciones convencionales como redes sociales, herramientas de 
productividad o plataformas de comercio electrónico. 
El SDK destaca por su enfoque en productividad y mantenibilidad, ofreciendo un entorno de desarrollo 
completo con herramientas como Android Studio y un amplio conjunto de APIs de alto nivel. Al basarse \nen lenguajes gestionados (Java/Kotlin), simplifica procesos como la gestión de memoria o la 
depuración, aunque introduce cierta sobrecarga en el rendimiento. Su arquitectura está optimizada 
para el desarrollo rápido de aplicaciones estándar, con especial énfasis en interfaces de usuario y 
conectividad, pero muestra limitaciones en escenarios que requieren acceso directo al hardware o 
máximo control sobre los recursos del sistema. La interoperabilidad con Kotlin como lenguaje prioritario 
permite reducir significativamente la cantidad de código necesario, aunque manteniendo 
compatibilidad con el amplio ecosistema existente en Java. 

<!-- Page 196 -->

 
 
Aplicaciones y desarrollo web 
196 
7.4.2. Android NDK (Native Development Kit) 
El Android NDK surgió de la necesidad de complementar el SDK con herramientas más especializadas. 
Este kit fue desarrollado específicamente para abordar las limitaciones del SDK en aplicaciones que 
requieren máximo rendimiento o acceso directo al hardware. 
El NDK permite implementar secciones críticas de código en lenguajes de bajo nivel como C y C++, 
generando librerías nativas compiladas para arquitecturas específicas (ARM, x86, MIPS). Estas librerías 
se integran con la aplicación principal mediante JNI (Java Native Interface), que actúa como puente \nentre el código nativo y el código Java/Kotlin. 
Las aplicaciones más adecuadas para el NDK incluyen: 
• Motores de videojuegos 3D avanzados. 
• Sistemas de simulación física compleja. 
• Procesamiento intensivo de gráficos, audio o vídeo. 
• Algoritmos que requieren máximo rendimiento computacional. 
• Interacción con hardware específico. 
La ventaja clave del NDK radica en el control preciso sobre los recursos del sistema. Al trabajar más 
cerca del hardware, los desarrolladores pueden optimizar al máximo el rendimiento, especialmente 
importante en dispositivos con capacidades limitadas. Lenguajes como C y C++ permiten ejecutar 
operaciones críticas sin la sobrecarga de los lenguajes gestionados. 
El NDK sacrifica comodidad de desarrollo por rendimiento extremo, permitiendo un control preciso 
sobre los recursos del hardware mediante lenguajes nativos (C/C++). Esta aproximación elimina la 
sobrecarga de las máquinas virtuales y entornos gestionados, pero exige a los desarrolladores asumir 
responsabilidades como la gestión manual de memoria o la coordinación entre componentes nativos y 
Java/Kotlin. Su arquitectura está especializada en tareas computacionalmente intensivas, ofreciendo 
acceso directo a instrucciones del procesador y optimizaciones específicas por arquitectura (ARM, 
x86), aunque incrementa la complejidad en mantenimiento y tamaño de la aplicación. El rendimiento 
superior viene acompañado de requisitos técnicos más exigentes, necesitando equipos con 
conocimientos especializados en desarrollo nativo y debugging a bajo nivel. 
7.5. Herramientas de Desarrollo para iOS 
SwiftUI 
SwiftUI es un framework de Apple diseñado para simplificar la creación de interfaces de usuario en 
todas sus plataformas. Utiliza una sintaxis declarativa que permite a los desarrolladores escribir menos 
código para obtener resultados más eficientes y adaptables. 
Tiene beneficios como la posibilidad de tener código más limpio y reutilizable; compatibilidad con iOS, 
macOS, watchOS y tvOS; diseño visual con vista previa en tiempo real en Xcode; soporte para 
accesibilidad y animaciones avanzadas sin necesidad de código extenso. 

<!-- Page 197 -->

 
 
Aplicaciones y desarrollo web 
197 
Xcode 
Xcode es un entorno de desarrollo integrado (IDE) creado por Apple para el desarrollo de software en 
sus plataformas. Incluye herramientas para programar, depurar y probar aplicaciones en macOS, iOS, 
watchOS y tvOS. Proporciona un entorno gráfico intuitivo con herramientas como Interface Builder, 
que permite diseñar interfaces de usuario visualmente, y el depurador LLDB. 
Sus características principales son: Soporte para múltiples lenguajes de programación, incluyendo Swift 
y Objective-C; dispone de herramientas avanzadas de depuración y análisis de rendimiento; tiene la 
posibilidad de integración con Swift Package Manager para la gestión de dependencias y dispone de 
simuladores para probar aplicaciones en diferentes dispositivos sin necesidad de hardware físico. 
IOS SDK 
El iOS Software Development Kit (iOS SDK) es un conjunto de herramientas y bibliotecas proporcionado 
por Apple para el desarrollo de aplicaciones en sus plataformas. Entre sus características clave se 
distinguen que incluye APIs y frameworks esenciales para interactuar con el hardware y software del 
dispositivo; permite el desarrollo de aplicaciones para iOS, macOS, watchOS y tvOS; dispone de soporte 
para funcionalidades avanzadas como ARKit (realidad aumentada), Core ML (aprendizaje automático) y 
HealthKit y se integra con Xcode para proporcionar un entorno de desarrollo unificado. 
El iOS SDK es fundamental para cualquier desarrollador que desee crear aplicaciones para el ecosistema 
de Apple, ya que proporciona los recursos necesarios para aprovechar al máximo las capacidades del 
hardware y software de la compañía. 
8. Navegadores web 
Un navegador web es una aplicación que permite recuperar y visualizar la información que contiene un 
sitio web. 
Este sitio web puede estar ubicado en servidores de cualquier parte del mundo (accediendo a través de 
la World Wide Web), en ordenadores de la red en la que está el usuario o incluso en su propio equipo. 
La palabra navegador deriva del concepto de navegación web, es decir, el proceso de seguimiento de los \nenlaces de una página a otra. 
Los navegadores pueden ampliar sus funcionalidades mediante la instalación de extensiones, 
complementos o plug-ins. Estos términos add-on, extensión, complemento y plug-in suelen usarse de 
forma intercambiable, aunque históricamente los plug-ins (como Adobe Flash Player o Java) eran 
aplicaciones más complejas que requerían integración más profunda con el navegador. 
En cambio, las extensiones actuales suelen centrarse en modificar o mejorar aspectos concretos de la \nexperiencia del usuario (como bloquear publicidad o gestionar contraseñas). Ejemplos populares de \nextensiones son AdBlock, LastPass o Grammarly. 
La seguridad de estas herramientas no depende del término que se use para describirlas, sino de la 
calidad del código y de los mecanismos de verificación del navegador (como los certificados digitales o 
las políticas de las tiendas de extensiones). 

<!-- Page 198 -->

 
 
Aplicaciones y desarrollo web 
198 
Funcionamiento 
Los navegadores se comunican con los servidores web por medio del protocolo de comunicaciones 
HTTP (Hypertext Transfer Protocol) para acceder a las direcciones de Internet (URL). 
La mayoría de los navegadores web modernos admiten diversos protocolos de red además del HTTP \nestándar. Entre los más importantes se encuentran el HTTPS y el FTP, cada uno con sus características 
particulares. 
• HTTPS (Hypertext Transfer Protocol Secure): es la versión segura y cifrada del protocolo HTTP. 
Inicialmente utilizaba SSL (Secure Sockets Layer) como sistema de cifrado, pero actualmente \nemplea su sucesor más avanzado, TLS (Transport Layer Security). Este protocolo proporciona 
tres ventajas principales: autenticación reforzada mediante certificados digitales, cifrado 
robusto de los datos transmitidos y mayor eficiencia en las comunicaciones, lo que lo hace \nesencial para transacciones seguras en internet. 
• FTP (File Transfer Protocol): los navegadores también soportan FTP (File Transfer Protocol), el 
protocolo clásico para transferencia de archivos. Este sistema permite tanto la subida como la 
descarga de ficheros, además de la navegación por directorios remotos. Existen varias variantes 
de FTP: la versión básica sin cifrado, FTPS (que añade seguridad mediante SSL/TLS) y SFTP 
(que utiliza SSH para la transferencia segura de archivos). Aunque su uso directo en 
navegadores ha disminuido, sigue siendo relevante para ciertas aplicaciones web especializadas. 
8.1. Navegadores más usados 
Vamos a ver la evolución del uso de los navegadores según W3Counter: 
Evolucion historica del uso de navegadores web: 
 
Evolucion historica del uso de navegadores web. Fuente: W3Counter 

<!-- Page 199 -->

 
 
Aplicaciones y desarrollo web 
199 
Cuota de mercado de navegadores web en abril de 2025 es: 
 
Cuota de mercado de navegadores web en abril de 2025. Fuente: https://www.w3counter.com/globalstats.php 
 
 
 
+ Info 
Existen una gran cantidad de navegadores poco usados y 
conocidos como: 
Brave, Vivaldi, Tor Browser, Yandex Browser, Epic Privacy 
Browser, Waterfox, Pale Moon, Torch, Comodo Dragon, Midori, 
Falkon, Otter Browser, Basilisk. 
 
Vamos a estudiar los navegadores más utilizados. 
Google Chrome 
 
Navegador web desarrollado por Google en 2008. Está compilado basándose en componentes de 
código abierto, como el motor de renderizado de WebKit y su estructura de desarrollo de aplicaciones 
(framework). 

<!-- Page 200 -->

 
 
Aplicaciones y desarrollo web 
200 
Está disponible gratuitamente bajo condiciones de servicio específicas. El nombre del navegador deriva 
del término usado para el marco de la interfaz gráfica de usuario ("Chrome"). Es el navegador más 
utilizado a nivel mundial. 
Características: 
• Interfaz sencilla y funcional. 
• Pestañas de navegación independientes y movimiento de estas. 
• Seguridad (especialmente desde que dejó de admitir complementos Java). 
• Estabilidad. 
• Velocidad. 
• Modo incógnito. 
• Motor de búsqueda Google (aunque se puede cambiar). 
• Marcadores instantáneos. 
• Aislamiento de procesos (sandboxing). 
• Listas negras. 
Safari 
 
Safari se lanzó al mercado en 2003. Es un navegador web de código cerrado desarrollado por Apple Inc. 
Está disponible para Mac OS X, iOS (el sistema usado por el iPhone, iPod Touch e iPad) y Microsoft 
Windows. (No funciona en Linux). 
Características: 
• Navegación por pestañas. 
• Corrector ortográfico. 
• Búsqueda progresiva. 
• Vista del historial en CoverFlow. 
• Administrador de descargas. 
• Sistema de búsqueda integrado. 

<!-- Page 201 -->

 
 
Aplicaciones y desarrollo web 
201 
Firefox 
 
Mozilla Firefox fue desarrollado a finales de 2004. Es un navegador web libre y de código abierto 
desarrollado para Linux, Android, IOS, OS X y Microsoft Windows coordinado por la Corporación 
Mozilla y la Fundación Mozilla. Usa el motor Gecko para renderizar páginas web. 
Características: 
• Navegación por pestañas. 
• Corrector ortográfico. 
• Búsqueda progresiva. 
• Marcadores dinámicos. 
• Administrador de descargas. 
• Navegación privada. 
• Navegación con georreferenciación. 
• Sistema de búsqueda integrado que utiliza el motor de búsqueda que desee el usuario. 
Internet Explorer 
 
Ha sido el navegador web más utilizado de Internet durante muchos años. 
Microsoft presentó Internet Explorer en 1995, basándose en una versión de Mosaic. En agosto de 2014, 
Microsoft anunció que a partir de enero de 2016 dejaba de publicar actualizaciones de seguridad para IE 8. 

<!-- Page 202 -->

 
 
Aplicaciones y desarrollo web 
202 
Internet Explorer siempre ha sido el navegador predeterminado de Windows, estaba incluido en las 
versiones de Windows, es decir se instalaba al instalar Windows. En la versión Windows 10, se sustituye 
por el navegador Microsoft Edge, pero sigue estando también disponible Internet Explorer. 
En la versión Windows 11, lanzada el 5 de octubre de 2021, Internet Explorer está completamente \neliminado y reemplazado por el motor Blink en el que se basa Microsoft Edge. 
 
 
 
 
+ Info 
De momento no se ha retirado porque hay páginas antiguas que 
solo son compatibles con este navegador. Especialmente sucede 
con algunas páginas de administraciones públicas. 
Sin embargo, pronto desaparecerá. El motivo es que tiene muchas 
vulnerabilidades de seguridad (no es seguro). Microsoft desaconseja 
su uso y ya no da soporte desde el 15 de junio de 2022. 
 
Microsoft Edge 
 
En julio de 2015, Microsoft publicó Edge para sustituir a Internet Explorer. 
Es una versión mejorada, modernizada y distinta de Internet Explorer con una línea de desarrollo 
independiente. 
El navegador se encuentra disponible para iOS, Android 4.4+ y Windows 10 (que lo trae integrado). 
Utiliza un nuevo motor de renderizado llamado "EdgeHTML", el cual deriva de Trident. 
Edge tiene integrado Adobe Flash Player, un lector PDF, un lector EPUB y soporte para asm.js. 
No es compatible con tecnologías existentes tales como ActiveX y Browser Helper Object (BHO), 
reemplazando su uso mediante un sistema de extensiones. 
Edge se integra con las plataformas en línea de Microsoft como el asistente digital Cortana. Los usuarios 
pueden hacer anotaciones en páginas web y poder almacenarlas y compartirlas mediante OneDrive. 
También integra la función "lista de lectura", que tiene la capacidad de sincronizar contenido entre 
dispositivos y proporciona un modo de lectura que oculta formatos innecesarios de las páginas para 
mejorar su lectura. 

<!-- Page 203 -->

 
 
Aplicaciones y desarrollo web 
203 
Opera 
 
Opera es un navegador que comenzó en 1994 como proyecto de investigación de Telenor. La primera 
versión, Opera 2.1, la publicó Opera Software en diciembre de 1996. Su principal característica ha sido 
siempre el cumplimiento de las recomendaciones del W3C. Hasta el año 2000 se trataba de un 
navegador de pago (con versión de prueba temporal), pero desde entonces es gratuito. 
Desde la versión Opera 15 (julio de 2013) utiliza el motor de renderizado Blink. Está disponible para 
Windows, Mac OS X, GNU/Linux, OS/2, Solaris y FreeBSD. 
Características: 
• Alta compatibilidad con distintos sistemas operativos. 
• Almacena miniaturas de las páginas de favoritos. 
• Permite navegación privada. 
• Detecta el phishing y páginas web no seguras. 
• Permite hacer búsquedas de palabras contenidas dentro de las páginas del historial. 
8.2. Comparativa de navegadores 
 

<!-- Page 204 -->

 
 
Aplicaciones y desarrollo web 
204 
 
 
9. Bibliografía 
• https://www.w3schools.com/. 
• LUJÁN MORA, S. Programación de aplicaciones web: historia, principios básicos y clientes web. 
Editorial Club Universitario. 
• https://alarcos.esi.uclm.es/per/fruiz/conf/xml/xml.htm. 
• https://codigoenpuntonet.blogspot.com/2016/11/configuracion-de-modo-de-estado-
de.html. 
• http://www.it.uc3m.es/~xml/enlaces.html#xml.db. 
• http://www.w3.org/XML/. 
• http://michelletorres.mx/lenguajes-de-programacion-del-lado-servidor/. 

<!-- Page 205 -->

 
 
Aplicaciones y desarrollo web 
205 
• https://es.wikipedia.org. 
• https://en.wikipedia.org. 
• https://es.wikipedia.org/wiki/ECMAScript. 
• https://es.wikipedia.org/wiki/AJAX. 
• https://es.wikipedia.org/wiki/Servidor_HTTP_Apache#Adopción_de_Apache. 
• http://www.hipertexto.info/documentos/rdf.htm. 
• https://www.cice.es/noticia/top-5-plataformas-desarrollo-ios-android/. 
• https://es.wikipedia.org/wiki/Sistema_de_gestión_de_contenidos. 
• https://conectasoftware.com/apps/devexpress/. 
• https://www.axarnet.es/blog/lenguajes-del-lado-del-servidor/. 
• https://www.desarrolloweb.com/manuales/manual-javascript.html. 
• https://www.ecured.cu/Aplicaci%C3%B3n_web. 
• https://www.ecured.cu/Lenguaje_de_marcado. 
• https://www.pcworld.es/mejores-productos/internet/mejores-navegadores-web-3672988/. 
• https://indexdesarrollo.com/lenguajes-de-programacion-web-mas-recomendables/. 
• https://programacion.net/articulo/lo_que_debes_aprender_en_2017_backend_y_frontend_
1687. 
• https://hackernoon.com/7-best-web-development-backend-frameworks-in-2018-
22a5e276cdd. 
• https://www.w3counter.com/globalstats.php. 
• http://cv.uoc.edu/web/~mmonzonisn/Practica-1/safari.html. 
• https://www.caracteristicas.co/google-chrome. 
• http://www.ajpdsoft.com/modules.php?name=Encyclopedia&op=content&tid=711. 
• https://www.php.net/. 
• https://docs.microsoft.com/es-es/internet-explorer/ie11-deploy-guide/updated-features-
and-tools-with-ie11. 

<!-- Page 206 -->

 
 
Aplicaciones y desarrollo web 
206 
• http://navegadores-internet.com/caracteristicas-del-navegador-opera. 
• https://www.pcworld.es/mejores-productos/internet/mejores-navegadores-web-3672988/. 
• https://www.infospyware.com. 
• https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods 
• https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html. 
• http://www.profesordeinformatica.com/servicios/http/metodos. 
• https://www.pcworld.es/mejores-productos/internet/mejores-navegadores-web-3672988/. 
• https://developer.mozilla.org/es/docs/Web/XML/Introducción_a_XML. 
• https://www.ibiblio.org/pub/Linux/docs/LuCaS/Manuales-LuCAS/doc-curso-html/doc-
curso-html/x4275.html. 
• https://www.abrirllave.com/xml/normas-de-sintaxis-basicas.php. 
• https://www.mclibre.org/consultar/xml/lecciones/xml-conceptos-basicos.html. 
• https://www.data2type.de/es/xml-xslt-xslfo/xpath/introduccion-a-xpath/localizacion/. 
• https://nubeser.com/tipo-desarrollo-aplicaciones-moviles/. 
• https://informaticapc.com/tutorial-html/frames.php. 
• https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Operadores/Comparison
_Operators. 
• https://docs.microsoft.com/es-es/dotnet/standard/data/xml/managing-namespaces-in-an-
xml-document. 
• https://es.wikipedia.org/wiki/Patrón_de_diseño#Categorías_de_patrones. 
• https://es.wikipedia.org/wiki/Extensible_Markup_Language. 
• https://en.wikipedia.org/wiki/HyTime. 
• http://www.hipertexto.info/documentos/sgml.htm. 
• https://uniwebsidad.com/libros/xhtml/. 
• https://es.wikipedia.org/wiki/JavaScript. 
• https://es.wikipedia.org/wiki/Python. 
• https://www.ionos.es/digitalguide/paginas-web/creacion-de-paginas-web/css-flexbox/.

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|Ficha Resumen del Tema 07]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque3-tema07|Nota Fuente Oficial del Tema 07]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema07-aplicaciones-web-frontend|Test Tema 07]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Flashcards Bloque 3]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema06|⬅️ Tema Completo 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema08|Tema Completo 08 ➡️]]
