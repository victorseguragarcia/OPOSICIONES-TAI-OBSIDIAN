---
title: "Tema Completo Extendido 02 (Bloque 4): Servicios de Directorio, Active Directory DS y Kerberos v5"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-4
  - tema-02
  - oposiciones-tai\nestado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque4-tema02.md]]"
  - "[[wiki/sources/bloque4-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---
> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema01|⬅️ Tema Completo 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema03|Tema Completo 03 ➡️]]

# 🔴 Tema Completo Extendido 02 (Bloque 4): 

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 02 correspondiente al Bloque 4 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Recordando Bases de Datos
Ya has estudiado en unidades anteriores, las bases de datos, sus características y objetivos, así como el 
Sistema Gestos de Base de Datos y las fases de Diseño. 
Como recordatorio, pero sin repetir todo lo ya estudiado, vamos a repasar alguno de los conceptos. 
Una de las definiciones de bases de datos más aceptadas es la propuesta por Flory en 1982: "Una base 
de datos es un conjunto exhaustivo, no redundante de datos estructurados, organizados 
independientemente de su utilización y su implementación en máquina, accesibles a tiempo real y 
compatibles por usuarios concurrentes que tienen necesidad de información diferente y no predecible \nen el tiempo." 
Otras definiciones 
- Conjunto, colección o depósito de datos almacenados en un soporte informático. Los datos deben estar interrelacionados y estructurados de acuerdo con un modelo capaz de recoger el 
máximo contenido semántico. 
- Consiste en una colección de datos persistentes e independientes usados por una organización determinada. 
- Serie de datos organizados y relacionados entre sí, los cuales son recolectados y explotados por los sistemas de información de una empresa o negocio en particular. 
- Es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso. 
- Es una colección de información organizada de tal modo que sea fácilmente accesible, gestionada y actualizada. 
- Es una representación de objetos y situaciones del mundo real. En el mundo real existen restricciones y limitaciones que deben ser reflejadas en la base de datos. Para ello es necesario el 
uso de métodos de diseño riguroso y formalizado. 
Características de las B.D 
- Es un conjunto o colección de datos.
- Los datos están estructurados.
- Existen relaciones entre los datos.
- Los datos no pueden ser redundantes (no debe haber duplicados).

---

Administración de Bases de Datos. Virtualización. Cloud 
- Los datos deben ser independientes de la máquina en que se almacenan o explotan.
- Debe ser fácilmente accesible, gestionada y almacenada.
- Debe permitir el acceso concurrente a la misma (de esto se encargan los Sistemas Gestores de
Base de Datos (SGBD)). 
- Deben dar soporte a usuarios con distintas necesidades.
- La mayoría de las bases de datos se almacenan en un soporte informático.
- Son la base de los sistemas de información.
- Representan una situación del mundo real.
Principales objetivos de un sistema de base de datos 
- Proporcionar a los usuarios y desarrolladores una visión abstracta de los datos.
El sistema esconde ciertos detalles de cómo se almacenan y mantienen los datos. 
- Independencia entre datos y aplicaciones.
Cuando se tenga que cambiar algo en la base de datos (como la forma de almacenar datos), \nesto no repercutirá en los programas de aplicación que trabajan sobre esa base de datos. 
Evitar redundancias de datos (duplicidad de información). 
- Evitar la inconsistencia de datos.
Se produce una inconsistencia de datos cuando existen varias copias de un mismo dato y no 
todas tienen el mismo valor. 
- Preservar la integridad.
Los valores de los datos almacenados deben satisfacer ciertos tipos de restricciones de 
consistencia. 
Por ejemplo, el precio de un producto debe ser un número y no una cadena de caracteres. 
- Atomicidad.
Los procesos deben ser atómicos, es decir, deben ocurrir o no ocurrir, pero no puede ocurrir 
parte del proceso. 
Por ejemplo, si mientras se está realizando un proceso se produce un corte de electricidad y se 
apaga el equipo, Se deberá volver al estado de consistencia anterior al fallo para que no se 
queden operaciones a medio hacer.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Seguridad y Confidencialidad.
Se debe garantizar la confidencialidad y seguridad de los datos contra accesos incorrectos o no 
autorizados. 
- Acceso concurrente a los datos.
Debe permitir a múltiples usuarios actualizar los datos simultáneamente. 
Un Sistema de Bases de Datos, está formado por 
- Una base de datos.
- Un Sistema Gestor de Bases de datos que administra y gestiona la información de la base de datos. 
- Un diccionario de datos. Contiene el listado de campos y variables de la B.D. así como su descripción, longitud, posibles valores, etc. 
También puede contener otros datos de interés como: 
- Información sobre la representación física de los datos.
- Asignación a dispositivos.
- Formas de acceso.
- Índices.
- Administrador de bases de datos (DBA). Persona o grupo de personas que crean, gestionan y mantienen la Base de Datos. 
- Usuario. Son aquellas personas que utilizan la Base de Datos.
### 🔵 1.1. Sistema Gestor de Bases de Datos
Un Sistema Gestor de Bases de Datos (SGBD) es un conjunto coordinado de programas, 
procedimientos, lenguajes, etc. que suministra tanto a los usuarios como al administrador de la base de 
datos, los medios necesarios para describir, manipular y utilizar los datos almacenados en la base, 
manteniendo la integridad, confidencialidad y seguridad. Su objetivo principal es simplificar y facilitar el 
acceso a datos. 
En relación con este tema es imprescindible habla de Edgar F. Codd, científico informático inglés, es 
conocido por crear 12 reglas para el modelo relacional de bases de datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
Codd se percató de que existían bases de datos en el mercado las cuales decían ser relacionales, pero lo 
único que hacían era guardar la información en tablas, sin estar estas tablas literalmente normalizadas; \nentonces publicó 13 reglas que un verdadero sistema relacional debería cumplir, aunque en la práctica 
algunas de ellas son difíciles de realizar. Un sistema podrá considerarse "más relacional" cuanto más siga \nestas reglas. 
- Regla 0: Regla de fundación. Cualquier sistema que se proclame como relacional, debe ser capaz de gestionar sus bases de datos enteramente mediante sus capacidades relacionales. 
- Regla 1: Regla de la información. Toda la información en la base de datos es representada unidireccionalmente por valores en posiciones de las columnas dentro de filas de tablas. Toda la 
información en una base de datos relacional se representa explícitamente en el nivel Lógico \nexactamente de una manera: con valores en tablas. 
- Regla 2: Regla del acceso garantizado. Todos los datos deben ser accesibles sin ambigüedad.
Esta regla es esencialmente una nueva exposición del requisito fundamental para las llaves 
primarias. Dice que cada valor escalar individual en la base de datos debe ser lógicamente 
direccionable especificando el nombre de la tabla, la columna que lo contiene y la llave primaria. 
- Regla 3: Regla del tratamiento sistemático de valores nulos. El sistema de gestión de base de datos debe permitir que haya campos nulos. Debe tener una representación de la "información 
que falta y de la información inaplicable" que sea sistemática y distinta de todos los valores 
regulares. 
- Regla 4: Catálogo dinámico en línea basado en el modelo relacional. El sistema debe soportar un catálogo en línea, el catálogo relacional, que da acceso a la estructura de la base de datos y 
que debe ser accesible a los usuarios autorizados. 
- Regla 5: Regla comprensiva del sublenguaje de los datos. El sistema debe soportar por lo menos un lenguaje relacional que: 
Tenga una sintaxis lineal. 
Puede ser utilizado de manera interactiva. 
Tenga soporte de operaciones de definición de datos, operaciones de manipulación de datos 
(actualización, así como la recuperación), de control de la seguridad e integridad y operaciones 
de administración de transacciones. 
- Regla 6: Regla de actualización de vistas. Todas las vistas que son teóricamente actualizables deben poder ser actualizadas por el sistema. 
- Regla 7: Alto nivel de inserción, actualización y borrado. El sistema debe permitir la manipulación de alto nivel en los datos, es decir, sobre conjuntos de tuplas. Esto significa que los 
datos no solo se pueden recuperar de una base de datos relacional a partir de filas múltiples y/o 
de tablas múltiples, sino que también pueden realizarse inserciones, actualización y borrados 
sobre varias tuplas y/o tablas al mismo tiempo y no solo sobre registros individuales.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Regla 8: Independencia física de los datos. Los programas de aplicación y actividades del terminal permanecen inalterados a nivel lógico, aunque realicen cambios en las 
representaciones de almacenamiento o métodos de acceso. 
- Regla 9: Independencia lógicas de los datos. Los programas de aplicación y actividades del terminal permanecen inalterados a nivel lógico, aunque se realicen cambios a las tablas base que 
preserven la información. La independencia de datos lógica es más difícil de lograr que la 
independencia física de datos. 
- Regla 10: Independencia de la integridad. Las restricciones de integridad se deben especificar por separado de los programas de aplicación y almacenarse en la base de datos. Debe ser 
posible cambiar esas restricciones sin afectar innecesariamente a las aplicaciones existentes. 
- Regla 11: Independencia de la distribución. La distribución de porciones de base de datos en distintas localizaciones debe ser invisible a los usuarios de la base de datos. Los usos existentes 
deben continuar funcionando con éxito: 
- Cuando una versión distribuida del SGBD se carga por primera vez.
- Cuando los datos existentes se redistribuyen en el sistema.
- Regla 12: La regla de la no subversión. Si el sistema proporciona una interfaz de bajo nivel de registro, aparte de una interfaz relacional, esa interfaz de bajo nivel no debe permitir su 
utilización para subvertir el sistema. Por ejemplo, para sortear las reglas de seguridad relacional 
o las restricciones de integridad. Esto es debido a que a algunos sistemas no relacionales 
previamente existentes se les añadió una interfaz relacional, pero, al mantener la interfaz nativa, 
seguía existiendo la posibilidad de trabajar no relacionalmente. 
### 🔵 1.2. Fases del diseño de la Base de Datos
Las fases del diseño que nos proporcionará una buena Base de Datos son: 
- Estudio inicial: Especificación de requisitos.
- Fase 1: Diseño conceptual.
Consiste en, a partir de la especificación de requisitos, crear un Esquema Conceptual, que 
utilizaras para la siguiente fase 2: Diseño Lógico. 
 
Etapa del diseño conceptual. Entradas y salidas

---

Administración de Bases de Datos. Virtualización. Cloud 
- Fase 2: Diseño Lógico.
Con el esquema conceptual creado en la Fase 1, se realiza La fase 2. 
La Fase 2: Diseño Lógico, la estudiaras en la siguiente unidad. 
 
Etapa del diseño lógico. Entradas y salidas 
- Fase 3: Diseño Físico.
Por último, con el esquema lógico creado en la Fase 2, se realiza la última fase: 
Fase 3: Diseño Físico, la estudiaras en la siguiente unidad. 
 
Etapa del diseño físico. Entradas y salidas 
Esta parte es transparente al usuario. El diseño físico se adapta al SGBD específico que se va a utilizar. Se \nexpresa haciendo uso de un lenguaje de definición de datos soportado por el SGBD. 
 
 
 
 
### 🔵 Ejemplo 
SQL contiene instrucciones para trabajar como lenguaje de 
definición de datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
Algunas de estas instrucciones son: 
- CREATE DATABASE.
- CREATE TABLE.
- CREATE SCHEMA.
- CREATE VIEW.
- CREATE INDEX.
 
## 🟣 2. Administración de Bases de Datos
La información es uno los activos más valiosos de la empresa, es indispensable contar con una persona 
que conozca la información, y las necesidades de la empresa en este aspecto, en un nivel gerencial 
superior. 
Aquí debemos definir dos perfiles diferentes: 
- El administrador de datos.
Es un gerente, no un técnico. 
Su labor es: 
- Decidir qué datos se van a almacenar.
- Establecer políticas para mantener y manejar los datos.
Su alcance es la organización completa. 
- El administrador de bases de datos (DBA o DataBase Administrator).
Es una persona de perfil técnico. Se encarga de poner en práctica las decisiones del 
administrador de datos. 
Su alcance suele ser una base de datos específica y los sistemas que trabajan sobre ella. 
En ocasiones, si la organización no es muy grande o dispone de un solo sistema de base de datos, estos 
roles pueden unirse en el DBA.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
 
 
### 🔵 2.1. Modelo ANSI/X3/SPARC
El grupo de trabajo ANSI/X3/SPARC (Standard Planning and Requirements Committee of the 
American National Standards Institute on Computers and Information Processing) propuso una 
arquitectura general para los Sistemas de Gestión de Bases de Datos (SGBD) basada en 3 esquemas o 
niveles para asegurar la separación entre datos y aplicaciones. 
Los niveles de abstracción propuestos son: 
- Nivel externo (de usuario).
Define las vistas de usuario. 
Una vista muestra a un usuario (o conjunto de usuarios con un determinado perfil) la 
información que es relevante para el/ellos, ocultando la información que no les es necesaria o a 
la que no tienen permisos para acceder. 
Por lo tanto, no muestra la estructura real de la base de datos. 
Aunque este nivel suele corresponder a los desarrolladores y programadores de bases de datos, 
suelen necesitar soporte por parte del personal que conoce la estructura de la base de datos. 
- Nivel conceptual.
En este nivel se define la estructura de la base de datos (cómo se organiza y relaciona la 
información). 
Este nivel está relacionado con las fases de diseño lógico y diseño conceptual. 
En este nivel no se tiene en cuenta cómo se almacena realmente la información. 
Este nivel lo gestionan los analistas y/o diseñadores de la base de datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Nivel interno (físico).
Es la forma real en que se almacena la información en la base de datos. 
Tendría correspondencia con la fase 3 del diseño (diseño físico) y con su materialización. 
Los administradores de bases de datos (DBA) son los encargados de seleccionar el SGBD y crear 
y configurar la base de datos a este nivel. 
 
Sin embargo, este modelo no ha sido adoptado como un estándar. 
La mayoría de los desarrollos utiliza una arquitectura con más niveles. 
A continuación, vamos a mostrar una propuesta de arquitectura más acorde con los modelos actuales 
por orden de realización.

---

Administración de Bases de Datos. Virtualización. Cloud 
Otra propuesta de arquitectura 
- Nivel conceptual.
Se corresponde con la primera fase del diseño de base de datos (diseño conceptual). 
Se suele utilizar el modelo entidad/relación para la realización de esquemas. 
Esta parte la desarrollan los analistas junto al cliente/usuarios en base a la especificación de 
requisitos. 
- Nivel lógico.
Este nivel se corresponde con la segunda fase del diseño de base de datos (diseño lógico). 
En este nivel se diseña la estructura y organización de la información en base al tipo de SGBD 
que se vaya a utilizar. 
En caso de ser relacional, se suele utilizar el modelo relacional para la realización de esquemas. 
Esta parte la desarrollan también los analistas. 
- Nivel interno.
En este nivel se debe seleccionar el SGBD utilizado. 
El modelado se realizará sobre él. 
Se utiliza un lenguaje de definición de datos (DDL) para crear las estructuras que definimos en \nel nivel anterior. 
Algunos SGBD incluyen un interfaz para crear dichas estructuras de forma más sencilla. 
Este nivel lo gestiona el DBA (administrador de la base de datos). 
- Nivel físico.
En este nivel se decide dónde se van a almacenar los datos físicamente. Para ello hay que \nestudiar diversos puntos: 
- En qué ordenador u ordenadores se guardará.
- Como están interconectados los equipos.
- Si es o no un sistema distribuido.
- Servidores.
- Sistemas operativos que se utilizarán.
- Política de seguridad.
- Etc.

---

Administración de Bases de Datos. Virtualización. Cloud 
La persona encargada de este nivel puede ser el propio DBA o un administrador de sistemas. 
En caso de encargarse una persona distinta a la del nivel interno, deben coordinarse porque las 
acciones que se deben realizar en este nivel suelen estar relacionadas con las realizadas en el 
nivel interno. 
Las tareas del nivel físico no se realizan al terminar las tareas del nivel interno, sino que se suelen 
solapar en el tiempo. 
- Nivel externo.
Es el último paso. 
Al igual que en el modelo ANSI/SPARC, aquí se implementan las distintas vistas que necesitarán 
los usuarios de la base de datos. 
Las vistas las crea, por norma general, el administrador de la base de datos según las 
necesidades solicitadas por los programadores y desarrolladores. 
### 🔵 2.2. El administrador de Bases de Datos (DBA)
 
Un administrador de bases de datos es aquel profesional que administra las tecnologías de la 
información y la comunicación. 
Normalmente, un DBA es una persona muy formada con algún título relacionado con las TIC 
(Tecnología de la Información y Comunicación). 
Debe tener competencias y capacidades en uno o más sistemas de gestión de bases de datos. 
Debe conocer lenguajes de definición (DDL), manipulación (DML) y control (DCL) de datos, así como 
de control de transacciones (TCL).

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
+ Info 
Hoy en día, cualquier DBA debería tener amplios conocimientos de 
SQL. 
 
 
Además, debe tener suficientes conocimientos de programación (especialmente en lenguajes de 
scripting) para poder automatizar ciertas tareas. 
 
 
 
 
### 🔵 El experto opina 
Debido al crecimiento exponencial que está teniendo la 
información que debe ser almacenada y tratada, están cogiendo 
fuerza conceptos como la inteligencia artificial, el big data, las 
bases de datos NoSQL y otras tecnologías. 
Debido a ello, los DBAs deberían ir reciclándose y aprendiendo \nestas tecnologías. 
 
#### 🔹 2.2.1. Funciones y Responsabilidades del DBA
Nombramos las funciones y responsabilidades del Administrados de Bases de Datos, y las desarrollamos 
con mayor detalle a continuación: 
- Configurar e instalar el hardware.
- Configurar e instalar el Sistema Operativo.
- Seleccionar, instalar y mantener el SGBD.
- Crear y configurar la base de datos.
- Control de los usuarios y los permisos.
- Gestión de la seguridad.
- Monitorizar y optimizar el rendimiento de la base de datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Realizar tareas de copia de seguridad y recuperación.
- Asegurar la integridad de los datos.
- Asegurar la disponibilidad.
- Desarrollo de aplicaciones.
- Administración de la Actividad de Datos.
- Comprobar espacio en disco.
- Generar documentación.
A continuación, desarrollamos estas funciones y responsabilidades: 
### 🔵 Configurar e instalar el hardware 
Esta tarea debe coordinarse junto al administrador de sistemas. Deben encargarse de instalar el servidor 
o servidores de bases de datos. 
Algunos factores a tener en cuenta son: 
- Memoria de almacenamiento.
- Infraestructura de red.
- Requisitos de la base de datos.
- Etc.
Configurar e instalar el Sistema Operativo 
Esta tarea corresponde al administrador de sistemas, pero puede coordinarse con él para optimizarlo 
para el funcionamiento de la base de datos. 
Seleccionar, instalar y mantener el SGBD 
En primer lugar, debe seleccionar el SGBD que va a instalar en función de diversos factores: 
- Precio.
- Licencias.
- Usuarios que puede soportar.
- Tamaño de base de datos que puede soportar.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Soporte técnico del fabricante.
- Software libre.
- Etc.
Una vez adquirido, debe instalar y configurar el SGBD de manera que se optimice su rendimiento para 
su base de datos. 
El mantenimiento del SGBD consiste en el control de su rendimiento y de las actualizaciones que vayan 
apareciendo. 
### 🔵 Crear y configurar la base de datos 
Se deben crear las estructuras de datos que se han definido en el diseño lógico. Para ello se utilizará un 
lenguaje de definición de datos DDL y las herramientas que nos proporcione el SGBD u otras 
herramientas CASE. 
Algunos de los elementos creados en un SGBD relacional son: 
- Tablas.
- Relaciones.
- Vistas.
- Usuarios.
- Permisos.
- Triggers.
- Reglas de integridad.
- Etc.
### 🔵 Control de los usuarios y los permisos 
Debe definir qué usuarios deben acceder y establecer una política de seguridad para evitar accesos no 
autorizados. 
Puede crear perfiles de usuarios con determinados derechos. 
También se incluyen la gestión de altas, bajas y modificación de usuarios.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 Gestión de la seguridad 
Debe implementar las medidas de seguridad para protegerse de ataques de terceros o de fallos del 
sistema. 
La labor del establecimiento de una política de seguridad es una función del administrador de sistemas. 
Por lo tanto, debe coordinarse con éste para que se incluya la base de datos en dichas medidas (copias 
de seguridad, antivirus, etc.). 
Monitorizar y optimizar el rendimiento de la base de datos 
Un DBA debe detectar las caídas de rendimiento, encontrar las causas y resolverlo. 
También debe estudiar constantemente las formas de mejorar el rendimiento de la base de datos. Esto 
se puede hacer de muchas formas: 
- Mejorando las instrucciones (especialmente, las consultas tipos JOIN pueden causar problemas).
- Mejorar la configuración del hardware y el software o adquirir nuevos elementos.
- Creación de índices.
- Etc.
Realizar tareas de copia de seguridad y recuperación 
Puede ser su labor en caso de que las medidas de copias de seguridad establecidas por el administrador 
del sistema no sean suficientes o no se coordinen adecuadamente. 
Por ejemplo, si los tiempos o tipos de copia (completa, incremental, etc.) no se pueden adaptar a la 
política general, el DBA podría implementar su propia política de copias de seguridad. 
De todas formas, lo aconsejable es que esta labor la realice el administrador de sistemas. 
### 🔵 Asegurar la integridad de los datos 
Debe controlar que no se produzcan incongruencias en los datos (datos duplicados con distintos valores). 
### 🔵 Asegurar la disponibilidad 
Debe asegurarse de que la base de datos está funcionando el mayor tiempo posible. Se buscan dos 
objetivos: 
- Maximizar el tiempo entre fallos.
- Minimizar el tiempo de recuperación.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 Desarrollo de aplicaciones 
En la construcción de aplicaciones que trabajen sobre la base de datos, la labor del DBA consiste en 
prestar apoyo a los programadores y desarrolladores para que puedan optimizar el uso de la base de 
datos. 
 
 
 
 
+ Info 
También podrá darles soporte en la fase de pruebas. 
Por ejemplo, podría crearles una réplica de la base de datos para 
que puedan trabajar sin preocupaciones de causar problemas en 
los datos originales. 
 
### 🔵 Administración de la Actividad de Datos 
El DBA no es usuario del sistema. 
No administra valores de datos, sino la actividad de datos. 
La labor de un DBA no debe ser procesar datos. Esto lo hacen los usuarios. 
La base de datos es un recurso compartido, por lo que el DBA debe proporcionar medias para que los 
usuarios trabajen de forma correcta sobre la base de datos. 
Algunas de esas medidas son: 
- Proporcionar estándares.
- Guías de acción.
- Procedimientos de control.
- Generación y difusión de documentación.
### 🔵 Comprobar espacio en disco 
Debe hacer revisiones periódicas para comprobar si hay suficiente espacio en disco. 
En caso de realizar alguna tarea que requiera mucho espacio adicional, se debe realizar una 
comprobación eventual. 
Si fuese necesario, se deberá ampliar el espacio asignado.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 Generar documentación 
El DBA debe documentar y mantener un registro periódico de: 
- Las labores de mantenimiento.
- Actualizaciones de hardware y software.
- Cambios en las aplicaciones.
- Eventos relacionados con cambios en el entorno de utilización de una base de datos.
## 🟣 3. Políticas, sistemas y procedimientos de back up y su recuperación 
Si determinados dispositivos de hardware ya sean internos como memoria e incluso la CPU, o externos, 
como un monitor etc., de nuestro ordenador se estropean y dejan de funcionar, simplemente se 
reemplazan y ya está, a seguir trabajando. 
En cambio, si falla el disco duro, el daño puede ser irreversible, puede significar la pérdida total de 
nuestra información. Es principalmente por esta razón, por la que debemos respaldar la información. 
Ante la posibilidad de rotura del dispositivo de hardware donde almacenemos la información, 
debemos definir una política de procedimientos de back up, para no perder "nunca" información. 
Si una empresa perdiera la información, las pérdidas económicas podrían ser muy cuantiosas. 
Actualmente cualquier tipo y tamaño de negocios se basa y confía en la información computarizada 
para su funcionamiento. La pérdida de información provoca un gran daño: 
- Pérdida de oportunidades de negocio.
- Clientes decepcionados y por tanto mala reputación.
- Etc.
Al igual que cualquier dispositivo electrónico (frigoríficos, microondas etc.), la tecnología informática 
no está exenta de posibles fallos o roturas, y por ello, debemos definir bien los sistemas de respaldos de 
información (copias de seguridad: back up) para que sean la base de un plan de contingencia en caso de 
que se produzca un error o rotura. 
También hay que tener en cuenta, que determinadas empresas, dependiendo del sector al que se 
dedican, como puede ser la Banca, no pueden interrumpir su funcionamiento en ningún momento, es 
decir, no pueden permitirse la más mínima interrupción informática.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 3.1. Políticas de backup
El diseño de una política de backup efectiva se erigirá teniendo en cuenta los recursos disponibles, los 
costos asociados y la criticidad de los datos y sistemas para el negocio. Por ejemplo, para datos 
altamente críticos y empresas solventes pueden requerirse soluciones de backup continuo y replicación \nen tiempo real entre CPDs para minimizar la pérdida de datos y el tiempo de inactividad en caso de un 
desastre. En el mundo actual, donde la disponibilidad de datos y la continuidad del negocio son 
cruciales, la redundancia de datos es una estrategia fundamental para las empresas. 
El RTO (Recovery Time Objective - Objetivo de Tiempo de Recuperación) es el tiempo máximo 
permitido para la recuperación de los sistemas y datos después de un incidente y que el RPO (Recovery 
Point Objective- Objetivo de Punto de Recuperación) establece el punto en el tiempo hasta el cual una 
organización está dispuesta a aceptar la pérdida de datos en caso de un incidente. 
Podemos decir que la redundancia permite reducir significativamente el RPO, ya que en caso de un 
desastre o fallo, se dispone de una copia reciente de los datos, minimizando la cantidad de información 
perdida. La implementación de redundancia también contribuye a optimizar el RTO, agilizando la 
recuperación de sistemas y datos críticos. Para elegir con rigor el tipo de copias de seguridad, la \nempresa u orgamismo deberé tener en cuenta algunas pautas: 
### 🔵 Medidas técnicas 
Se deben tomar decisiones en cuanto a conceptos técnicos como son: 
- Volumen de información a copiar.
Condicionará las decisiones que se tomen sobre la política de copias de seguridad, en una 
primera consideración está compuesto por el conjunto de datos que deben estar incluidos en la 
copia de seguridad, sin embargo, se pueden adoptar diferentes estrategias respecto a la forma 
de la copia, que condicionan el volumen de información a copiar, para ello la copia puede ser: 
- Qué datos copiar:
- Copia incremental.
- Copia diferencial.
- Copia completa.
- Tiempo disponible para efectuar la copia.
El tiempo disponible para efectuar la copia de seguridad es importante, ya que el soporte 
utilizado, unidad de grabación y volumen de datos a almacenar, puede hacer que el proceso de 
grabación de los datos dure horas, y teniendo en cuenta que mientras se efectúa el proceso es 
conveniente no realizar accesos o modificaciones sobre los datos objeto de la copia, este 
proceso ha de planificarse para que suponga un contratiempo en el funcionamiento habitual del 
sistema de información.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Soporte utilizado.
Es la primera decisión a tomar cuando se planea una estrategia de copia de seguridad, sin \nembargo, esta decisión estará condicionada por un conjunto de variables, tales como la 
frecuencia de realización, el volumen de datos a copiar, la disponibilidad de la copia, el tiempo 
de recuperación del sistema, etc. 
Inicialmente, los soportes más habituales eran: cintas magnéticas, discos compactos (como las 
unidades de Iomega Zip y Jazz), grabadoras de CD-ROM o cualquier dispositivo capaz de 
almacenar los datos que se pretenden salvaguardar. 
Actualmente se suelen realizar en discos duros externos y también en cintas magnéticas. 
Se tiene en cuenta el coste de la opción elegida, sabiendo el número de elementos que 
necesitamos en función de la organización de la realización de las copias: diarias, semanal, 
mensual etc. 
### 🔵 Medidas organizativas 
Una vez estudiadas las medidas de índole técnica, hay que fijar unas medidas organizativas, que 
garanticen un buen sistema de copias de seguridad. 
La política de copias de seguridad debe garantizar la reconstrucción de los ficheros en el estado en que 
se encontraban al tiempo de producirse la pérdida o destrucción. 
- Frecuencia de realización de copias de seguridad y lugar de guardado.
La realización de copias de seguridad ha de realizarse diariamente, éste es el principio que debe 
regir la planificación de las copias, sin embargo, existen condicionantes, tales como la frecuencia 
de actualización de los datos, el volumen de datos modificados, etc., que pueden hacer que las 
copias se realicen cada más tiempo. 
Un posible esquema de copia de seguridad sería realizar una copia de seguridad cada mes y se 
guardara durante un año (preferentemente en algún sitio seguro ajeno a la empresa), una copia 
de seguridad completa semanalmente que se guarda durante un mes y copias de seguridad 
diarias, que se guardan durante una semana y que pueden ser completas, incrementales o 
diferenciales. 
Con este sistema se pueden utilizar 20 soportes que garantizan un alto nivel de seguridad en 
cuanto a recuperaciones de datos. A cada día de la semana se le asigna una cinta, la copia de 
seguridad semanal se irá acumulando en un soporte que corresponderá a un mes, así pues, cada 
soporte mensual irá acumulando sus semanas correspondientes, cuando hayan pasado los 12 
meses se usará otro respaldo para una copia completa anual. 
De esta manera tendremos 20 soportes: 7 + 12 + 1.

---

Administración de Bases de Datos. Virtualización. Cloud 
Como decíamos, esto es uno de los posibles esquemas de seguridad ya que cada empresa posee 
un volumen de datos único, una tasa de cambio de información distinta y requisitos de 
recuperación específicos. Factores que, junto con las regulaciones y la complejidad de los 
sistemas informáticos, hacen que cada plan de respaldo sea personalizado. 
Hay que guardar las copias de seguridad en un lugar seguro, cumpliendo con la normativa de la 
Ley de Protección de Datos, (puede ser una caja de seguridad ignifuga, un lugar externo a la \nempresa etc.). 
- Planificación de la copia.
Las copias de seguridad se pueden realizar en diferentes momentos día, pero se elegirá el 
momento más adecuado dependiendo del funcionamiento de la empresa (normalmente 
durante la noche o al mediodía). 
Si es posible, la copia se debe realizar de forma automática por un programa de copia, y según la 
configuración de éste, se podrá realizar un día concreto, diariamente, semanalmente, 
mensualmente, a una hora concreta, cuando el sistema esté inactivo, etc. 
Con estos programas, se realizará únicamente de las tareas de supervisión. 
- Mecanismos de comprobación.
Se deben definir mecanismos de comprobación de las copias de seguridad, aunque los propios 
programas que las efectúan suelen disponer de ellos para verificar el estado de la copia, es 
conveniente planificar dentro de las tareas de seguridad la restauración de una parte de la copia 
o de la copia completa periódicamente, como mecanismo de prueba y garantía. 
Se debe comprobar, que, en caso necesario, la copia se restaura correctamente, antes de que 
surja la necesidad real de tener que hacerlo. 
- Responsable del proceso.
Debe existir una persona responsable de la supervisión del sistema de backup. 
Se debe designar a una persona que, entre sus funciones, se incluya la supervisión del proceso de 
copias de seguridad, el almacenamiento de los soportes empleados en un lugar designado a tal 
fin e incluso de la verificación de que las copias se han realizado correctamente. 
### 🔵 3.2. Copias de seguridad (backup)
Una copia de seguridad o backups es un respaldo, son sólo duplicados de archivos que se guardan en 
"Tape Drives" de alta capacidad. Los archivos que son respaldados pueden variar desde archivos del 
sistema operativo, Bases de Datos, hasta archivos de un usuario común.

---

Administración de Bases de Datos. Virtualización. Cloud 
Respaldar la información significa copiar el contenido lógico de nuestro sistema informático a un medio 
que cumpla con una serie de exigencias: 
- Ser confiable:
Minimizar las probabilidades de error. 
Muchos medios magnéticos como las cintas de respaldo, los disquetes, o discos duros tienen 
probabilidades de error o son particularmente sensibles a campos magnéticos, elementos todos 
que atentan contra la información que hemos respaldado allí. 
Otras veces la falta de confiabilidad se genera al rehusar los medios magnéticos. Las cintas en 
particular tienen una vida útil concreta. Es común que se subestime este factor y se reutilicen 
más allá de su vida útil, con resultados nefastos. 
- Estar fuera de línea, en un lugar seguro:
Tan pronto se realiza el respaldo de información, el soporte que almacena este respaldo debe 
ser desconectado de la computadora y almacenado en un lugar seguro tanto desde el punto de 
vista de sus requerimientos técnicos (humedad, temperatura, campos magnéticos), como de su 
seguridad física y lógica. 
Si realizamos el respaldo de información y dejamos el dispositivo conectado al ordenador, puede 
potencialmente sufrir un ataque de cualquier índole que lo afecte. 
- La forma de recuperación sea rápida y eficiente:
Es necesario probar la confiabilidad del sistema de respaldo no sólo para respaldar, sino que 
también para recuperar. 
Hay sistemas de respaldo que aparentemente no tienen ninguna falla al generar el respaldo de la 
información pero que fallan completamente al recuperar estos datos al sistema informático. 
Esto depende de la efectividad y calidad del sistema que realiza el respaldo y la recuperación. 
Debemos comprobar que el tipo de sistema de backup que estemos utilizando, realice una 
restauración de información correcta. 
Existen varios softwares que automatizan la ejecución de backups, pero el funcionamiento básico de \nestos paquetes depende del denominado archive bit. 
Este archive bit indica un punto de respaldo, y puede existir por archivo o al nivel de "Bloque de 
Información" (típicamente 4096 bytes), esto dependerá tanto del software que sea utilizado para los 
respaldos, así como del archivo que sea respaldado.

---

Administración de Bases de Datos. Virtualización. Cloud 
Este mismo archive bit es activado en los archivos (o bloques) cada vez que estos sean modificados y es 
mediante este bit, que se realizan los tres tipos de respaldos que se utilizan: 
- Respaldo Completo ("Full"):
Es recomendable, si el soporte, tiempo de copia y frecuencia lo permiten, incluye una copia de 
datos y programas, restaurando el sistema al momento anterior a la copia. 
Guarda todos los archivos que sean especificados al tiempo de ejecutarse el respaldo. El archive 
bit es eliminado de todos los archivos (o bloques), indicando que todos los archivos ya han sido 
respaldados. 
- Respaldo de Incremento ("Incremental"):
Solamente se almacenan las modificaciones realizadas desde la última copia de seguridad, con lo 
que es necesario mantener la copia original sobre la que restaurar el resto de copias. Utilizan un 
mínimo espacio de almacenamiento y minimizan el tipo de desarrollo, a costa de una 
recuperación más complicada. 
Cuando se realiza un Respaldo de Incremento, sólo aquellos archivos que tengan el archive bit 
serán respaldados; estos archivos (o bloques) son los que han sido modificados después de un 
Respaldo Completo. Además, cada Respaldo de Incremento que se realice también eliminará el 
archive bit de estos archivos (o bloques) respaldados. 
- Respaldo Diferencial ("Differential"):
Como la incremental, pero en vez de solamente modificaciones, se almacenan los ficheros 
completos que han sido modificados. También necesita la copia original. 
Este respaldo es muy similar al "Respaldo de Incremento", la diferencia se basa en que el archive 
bit permanece intacto. 
### 🔵 Respaldo 
Archivos en respaldo 
Archive bit 
### 🔵 Ventajas 
Desventajas 
Completo 
("Full") 
### 🔵 Todos 
Eliminado en 
todos los 
archivos 
Con este respaldo 
únicamente es 
posible recuperar 
toda la información 
### 🔵 Tiempo de Ejecución 
De Incremento 
("Incremental") 
Archivos con archive 
bit activo. (Aquellos 
que hayan cambiado 
desde el último 
Respaldo Completo) 
Eliminado en 
los archivos 
que se 
respaldan 
### 🔵 Velocidad 
Requiere del último 
Respaldo Completo y de 
todos los Respaldos de 
Incremento que le 
siguieron para recuperar \nel Sistema 
Diferencial 
("Differential") 
Archivos con archive 
bit activo. (Aquellos 
que hayan cambiado 
desde el último 
Respaldo Completo) 
### 🔵 Intacto 
Sólo requiere del 
último Respaldo 
### 🔵 Completo y del 
último respaldo 
Diferencial 
Ocupa mayor espacio en 
discos comparado con 
Respaldos de Incremento

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 3.2.1. Estrategia de backup 3-2-1
La estrategia 3-2-1 es una regla general ampliamente aceptada en el ámbito de la seguridad de la 
información y la continuidad de negocio, que define una forma robusta y eficaz de gestionar las copias 
de seguridad. Su objetivo principal es garantizar la disponibilidad y recuperación de los datos ante 
incidentes como fallos técnicos, errores humanos, ataques maliciosos o desastres físicos. 
Esta estrategia establece que: 
- 3: Deben existir al menos tres copias de los datos. Una copia primaria (la original) y dos copias de respaldo. 
- 2: Las copias deben almacenarse en al menos dos tipos de soporte diferentes (por ejemplo, disco duro y cinta, o almacenamiento local y en la nube). Esto reduce el riesgo de pérdida 
simultánea por fallo en un mismo medio. 
- 1: Una de las copias debe estar almacenada fuera del sitio (off-site), en una ubicación geográfica diferente o en un entorno de almacenamiento en la nube. Así se protege la 
información frente a incendios, robos o catástrofes naturales. 
Esta estrategia no implica una tecnología concreta, sino una filosofía de redundancia y diversificación. 
Es compatible con otros enfoques y puede complementarse con políticas de retención como GFS 
(Grandfather-Father-Son, que vemos a continuación) o mecanismos adicionales como la inmutabilidad 
del backup. 
En contextos más exigentes, se puede evolucionar hacia la estrategia 3-2-1-1-0, cuyas últimas cifras 
responderían con un: 
- 1 adicional: Específica que suele ser una copia inmutable (no modificable) o air-gapped
(desconectada de la red). 
- 0: Hace referencia a verificaciones automatizadas (ej. checksums, pruebas de restauración).
#### 🔹 3.2.2. Secuencia de Respaldo GFS (Grandfather-Father-Son)
Esta secuencia de respaldo es una de las más utilizadas y consiste en Respaldos Completos cada semana 
y Respaldos de Incremento o Diferenciales cada día de la semana. Suponiendo la siguiente semana: 
Domingo (1) 
Lunes (2) 
Martes (3) 
Miércoles 
(4) 
Jueves (5) 
Viernes 
(6) 
Sábado (7) 
Diferencial/ 
de 
### 🔵 Incremento o 
NADA 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Completo 
Diferencial/ 
de 
### 🔵 Incremento o 
NADA

---

Administración de Bases de Datos. Virtualización. Cloud 
Domingo (8) 
Lunes (9) 
Martes (10) 
Miércoles 
(11) 
Jueves (12) 
Viernes 
(13) 
Sábado (14) 
Diferencial/ 
de 
### 🔵 Incremento o 
NADA 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Diferencial/ 
de 
### 🔵 Incremento 
Completo 
Diferencial/ 
de 
### 🔵 Incremento o 
NADA 
Ejemplo: 
En caso de fallar el Sistema en jueves (12): 
- Será necesario el Respaldo completo del viernes (6) y, si se utilizaron Respaldos Diferenciales:
Sólo el Respaldo Diferencial del miércoles (11). 
- Si se utilizaron Respaldos de Incremento: Se necesitarán todos los Respaldos de Incremento desde el sábado (7) hasta el miércoles (11). 
- En consecuencia, los respaldos completos de cada viernes pasan a formar parte del "Archivo"
mensual de Información. 
#### 🔹 3.2.3. Duplicado de Información en Línea (RAID)
RAID ("Redundant Array of Independent Disks") en palabras simples es: un conjunto de 2 o más "Discos 
Duros" que operan como grupo y logran ofrecer una forma más avanzada de respaldo ya que: 
- Es posible mantener copias en línea ("Redundancy").
- Agiliza las operaciones del Sistema (sobre todo en bases de datos).
- El sistema es capaz de recuperar información sin intervención de un Administrador.
Existen varias configuraciones de Tipo RAID, que ya has estudiado en una unidad anterior. 
 
 
 
 
### 🔵 Atención 
Los Sistemas RAID son muy importantes, por ello te aconsejamos 
que los repases de nuevo, en el Bloque II Tecnología Básica, Unidad 
Didáctica 2. Periféricos: conectividad y administración.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 3.2.4. Software de respaldo y respaldo "On Line"
Los servicios de respaldo en Internet tienen muchas ventajas: 
- Guardan la información fuera del lugar de trabajo.
- Evitan tener que intercambiar medios.
Algunos software y servicios que nos ayudan a mantener un orden en nuestros respaldos, los cuales 
podemos clasificarlos en: 
- Software de respaldo tradicional: Con estos productos, podemos elegir los archivos o carpetas a guardar, seleccionar un dispositivo de almacenamiento, y ejecutar el respaldo sin ayuda. 
Ejemplos: 
- Backup Exec Desktop 4.5 Veritas Software:
Ofrece soporte para una gran variedad de dispositivos de almacenamiento, que incluyen 
cintas y discos duros. Lleva a cabo respaldos que son increméntales o diferenciales. 
- Backup NOW! Desktop Edition 2.2 New Tech Infosystems:
Ofrece soporte únicamente para unidades CD-R y CD-RW. 
- NovaBackup 6.6 Workstation Edition (NovaStor Corp):
Apropiado tanto para una pequeña red empresarial como para un solo sistema. 
- Software de respaldo de fondo: Ideal para los usuarios que no tienen una "disciplina" en respaldar su información. Estos programas hacen una copia de los archivos en forma 
automática, "sin molestar". 
- AutoSave 1.0 VCommunications Inc.
Respalda automáticamente los archivos. 
- QuickSync 3 Iomega Corp.
Al igual que el SW anterior, se ejecuta de fondo, copiando automáticamente los archivos 
nuevos o modificados de carpetas específicas en el dispositivo de almacenamiento de 
destino, que puede ser un disco duro o un medio desmontable. Los Zip Drives de Iomega 
tienen soporte adecuado, no así las unidades CD-R o CD-RW. 
- Servicios de respaldo en Internet.
Hay algunos servicios que dan capacidad de almacenamiento en Internet. Para esto, se 
contrata un plan y la compañía asigna cierta capacidad.

---

Administración de Bases de Datos. Virtualización. Cloud 
##### 3.2.4.1. Respaldo DAS, NAS, SAN
NAS (Network Attached Storage), SAN (Storage Area Network) y DAS (Direct Attached Storage) son 
tres modos de almacenamiento muy utilizados en la actualidad, estudiados en una unidad anterior. 
Resumimos cada uno de ellos: 
- DAS (Direct-Attached Storage).
Son dispositivos de almacenamiento conectados a las maquinas directamente (por ejemplo, 
discos duros). 
Está basado en Tecnologías SCSI (Small Computers System Interface), FC (Fiber Channel), 
SATA e IDE. 
Tradicionalmente, un sistema DAS habilita capacidad extra de almacenamiento a un servidor, 
mientras mantiene alto ancho de banda y tasas de acceso. 
- NAS (Network Attached Storage).
NAS es un sistema de almacenamiento diseñado para almacenar y gestionar archivos en una 
red. Se compone de un servidor de archivos y una red local generalmente TCP/IP, facilitando el 
acceso y la compartición de archivos entre varios dispositivos y usuarios. El sistema centraliza 
físicamente el almacenamiento, permitiendo asimismo las copias de seguridad automáticas, el 
acceso remoto, la reproducción multimedia y la escalabilidad. 
Sin embargo, un posible inconveniente es el cuello de botella que puede originarse en 
transferencias de grandes volúmenes de datos o información de alta densidad, más allá del 
hardware del servidor, por la competencia por el ancho de banda, el tráfico de almacenamiento 
compite con los demás tipos de tráfico en la misma red. 
- SAN (Storage Area Network).
La SAN es una red especializada de alta velocidad formada esencialmente por dispositivos de 
almacenamiento (matrices de discos, unidades de estado sólido) y switches. Dicha red 
proporciona la abstracción de los recursos de almacenamiento que ofrece de manera uniforme y 
transparente a los sistemas que accedan a ella, como si fuera un espacio de almacenamiento 
local. Esta lógica acelera y simplifica el proceso de backup sin congestionar la red. 
Una red SAN ofrece una alta centralización lógica del almacenamiento, mejorando la gestión de 
los datos y su disponibilidad. No obstante, hay que señalar que la distribución física de los datos 
puede variar según la configuración de la SAN y los requisitos específicos de la organización. Son 
comunes los ejemplos de dispositivos o matrices de almacenamiento alejados entre sí cuya 
administración se centraliza a través de una red de alta velocidad.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
### 🔵 Atención 
Debido a la importancia de los Sistemas DAS, NAS y SAN, te 
aconsejamos que los repases de nuevo, en el Bloque II Tecnología 
Básica, Unidad Didáctica 2. Periféricos: conectividad y 
administración. 
 
#### 🔹 3.2.5. Snapshots, complemento al Backup
Los snapshots o instantáneas son capturas puntuales del estado de un sistema, volumen o conjunto de 
datos en un momento determinado. A diferencia de una copia de seguridad tradicional, un snapshot no 
almacena una réplica completa de los datos, sino que registra los cambios realizados a partir de un 
punto inicial, permitiendo revertir el sistema a ese estado previo de manera rápida y eficiente. 
Esta técnica es especialmente útil para recuperaciones inmediatas en casos de errores humanos, 
corrupción de datos o fallos en actualizaciones. Sin embargo, es fundamental entender que los 
snapshots no reemplazan a los backups convencionales, ya que dependen del medio de 
almacenamiento original. En caso de fallo físico del dispositivo, los snapshots almacenados en él 
también se perderían. 
Los snapshots se implementan en diversos entornos: 
- Sistemas físicos: Sistemas de archivos como ZFS, Btrfs o NTFS (a través de Volume Shadow
Copy) permiten crear instantáneas para restaurar versiones anteriores de archivos o sistemas 
completos. 
- Entornos virtualizados: Plataformas como VMware, Hyper-V o KVM utilizan snapshots para facilitar la gestión de máquinas virtuales, permitiendo revertir a un estado anterior antes de 
cambios críticos. 
- Almacenamiento en la nube: Servicios como AWS EBS, Azure Disks o Google Cloud Persistent
Disk ofrecen funcionalidades de snapshot automatizadas para proteger datos en 
infraestructuras cloud. 
Para garantizar una estrategia de protección de datos robusta, los snapshots deben combinarse con 
copias de seguridad externas, cumpliendo así con principios como la regla 3-2-1. De este modo, se logra 
un equilibrio entre recuperación rápida (snapshots) y resiliencia ante desastres (backups tradicionales).

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 3.3. Redundancia entre CPDs (Recovery Site)
Al replicar sus datos en ubicaciones separadas geográficamente, las organizaciones pueden garantizar la 
protección contra fallos, desastres naturales e interrupciones, minimizando el impacto en sus 
operaciones y la pérdida de información crítica. 
Tipos de redundancia de datos entre CPDs: 
- Replicación sincrónica: Los datos se copian en el CPD secundario de forma instantánea o casi instantánea, ofreciendo el RPO más bajo posible pero pudiendo afectar el rendimiento del CPD 
primario. 
- Replicación asincrónica: Los datos se copian con cierto retraso programado, lo que permite un mejor rendimiento en el CPD primario pero aumenta el RPO potencial. 
- Replicación basada en snapshots: Se crean copias periódicas de los datos en el CPD secundario, ofreciendo un equilibrio entre RPO y RTO. 
Beneficios de la redundancia de datos entre CPDs: 
- Alta disponibilidad: Acceso continuo a datos y aplicaciones críticas en caso de fallos del CPD primario. 
- Recuperación ante desastres: Recuperación rápida de desastres naturales o incidentes que afecten al CPD primario. 
- Cumplimiento normativo: Cumplimiento de normativas que exigen un alto nivel de disponibilidad y protección de datos. 
- Reducción del RPO: Minimización de la cantidad de datos perdidos en caso de un desastre.
- Aceleración del RTO: Agilización de la recuperación de sistemas y datos críticos.
Aspectos a tener en cuenta: 
- Costes: Implementar y mantener CPDs redundantes implica costes adicionales de infraestructura, software y gestión. 
- Complejidad: La gestión de la replicación de datos entre CPDs añade complejidad a la infraestructura de TI. 
- Latencia: La distancia geográfica entre CPDs puede introducir latencia en la red, lo que podría afectar el rendimiento de las aplicaciones. 
Por otro lado, para datos menos críticos con RPO y RTO más flexibles, se pueden implementar políticas 
de backup menos costosas y más espaciadas en el tiempo.

---

Administración de Bases de Datos. Virtualización. Cloud 
## 🟣 4. Backup en sistemas físicos y virtuales
Con una infraestructura virtual, en lugar del sistema operativo del servidor, hay cargado un hipervisor 
como vSphere o Hyper-V. El hipervisor es donde realmente crea sus máquinas virtuales. 
Cada VM tiene sus propios dispositivos virtuales: CPU virtual, memoria virtual, tarjetas de interfaz de 
red virtual y su propio disco virtual. Sobre este hardware virtual, carga un sistema operativo guest y 
luego sus aplicaciones del servidor tradicional. 
Como ya hemos visto, los beneficios de la virtualización son obvios: En lugar de tener solo una 
aplicación por servidor, ahora puede ejecutar varios Sistemas operativos guest y una serie de 
aplicaciones con el mismo hardware físico. 
Independencia del hardware y portabilidad de VM 
Como se ha dicho, cada máquina virtual tiene su propio hardware virtual. Por lo que el sistema 
operativo guest cargado en una VM solo conoce esta configuración del hardware y no la del servidor 
físico. En otras palabras, una VM es completamente independiente del hardware. Significa que el 
sistema operativo instalado en una VM ya no está vinculado a un determinado hardware, y así se 
pueden mover fácilmente máquinas virtuales desde un servidor físico a otro, o incluso a otro centro de 
datos. 
Por tanto, las VM son absolutamente portátiles, se puede copiar en una unidad flash, y replicar una 
máquina virtual en WAN o en Internet. 
Características extra de máquinas virtuales 
Existen muchas características útiles creadas a partir de la independencia de hardware y la portabilidad 
de VM: 
- vMotion es una tecnología de VMware que otorga portabilidad de VM e independencia de hardware, ¡permitiendo a una VM en ejecución migrar de un servidor a otro sin tiempo de 
inactividad para el usuario final! 
- Distributed Resource Scheduler (o DRS, por sus siglas en inglés). Esta tecnología de VMware permite equilibrar la infraestructura virtual en el aspecto del consumo de recursos. DRS puede 
mover una VM en ejecución desde un host a otro (mediante vMotion) para poder brindarle 
todos los recursos que necesita para funcionar con eficacia. 
- VMware High Availability (o VMHA, por sus siglas en inglés) es una opción que le permite restaurar VM desde un servidor fallido a otro para que pueda volver a ejecutarla de inmediato.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Distributed Power Management (o DPM, por sus siglas en inglés) es otra fabulosa característica de VMware que puede ayudar a reducir la factura de energía de su empresa! Con esta 
característica, puede fácilmente mantener bajo control el consumo de energía de la 
infraestructura. DPM consolida a las VM en menos servidores físicos cuando el consumo de 
recursos en la infraestructura virtual es bajo. Mientras tanto, aquellos servidores que no sean 
necesarios se desactivarán. 
- La virtualización también facilita la recuperación ante alguna incidencia. Gracias a la independencia de hardware, si una VM dentro de su infraestructura virtual falla, puede ejecutar 
las VM a las que le realizó backup en cualquier servidor ya que los sistemas operativos guest ya 
no están vinculados a un hardware especifico. 
Para aprovechar al máximo la funcionalidad que otorga la virtualización, se deben usar las herramientas 
adecuadas para el monitoreo, la administración y, por supuesto, la protección de datos. 
Dado que las máquinas virtuales difieren notablemente de los servidores físicos, las herramientas 
designadas para estos últimos no sirven para las primeras. Esto aplica en especial para el backup. 
La mejor forma de garantizar que las máquinas virtuales dispongan de una copia de seguridad fiable, \nes realizarlas en la nube. 
Los sistemas de copias de seguridad en la nube, garantiza que las máquinas virtuales y servidores: 
- Disponen del espacio suficiente para realizar la copia de seguridad. El problema de disponer de soportes con espacio suficiente para las copias será eliminado. 
- Realicen las copias de seguridad de forma automatizada sin necesidad de intervención del usuario. La empresa contratada se encarga de realizar la copia externa de las máquinas virtuales 
y los datos, garantizando el proceso y su seguridad. 
- Puedan restaurar las copias de sus máquinas virtuales en muy poco tiempo, reduciendo los parones en la actividad de la empresa, la pérdida de datos, e incluso pérdidas económicas 
derivadas de este tipo de incidencias. 
- Los datos copiados estarán protegidos con encriptación para impedir el acceso de personas no autorizadas. Esta encriptación se realiza en el equipo del cliente, por lo que se garantiza la 
seguridad en todo el proceso de copia de seguridad. 
- La copia de seguridad está replicada (múltiples copias en distintos dispositivos), para proporcionar más tranquilidad. 
Si una empresa hace uso de las ventajas de la virtualización, es recomendable que haga copias 
periódicas de sus datos y máquinas virtuales. Realizando la copia externa a través de una compañía \nespecializada se obtiene la seguridad de disponer de un respaldo en caso de que se produzca alguna 
incidencia.

---

Administración de Bases de Datos. Virtualización. Cloud 
## 🟣 5. Virtualización de sistemas
El sistema de almacenamiento de la información y las copias de seguridad es el valor más importante 
de una empresa o institución. Su gestión debe ser perfecta, y puede resultar compleja. 
Ya conocemos los sistemas de almacenamiento RAID, para no tener pérdidas de información, y también 
para no tener que apagar un servidor lo que evita el paro del funcionamiento de una empresa o 
institución. 
Dependiendo de la empresa, las necesidades de almacenamiento son muy diferentes. 
Se puede hacer un almacenamiento de datos basándonos en diferentes ideas: 
- El uso de la potencia de la nube.
- Buscar la perdurabilidad de los sistemas de cinta.
- Utilizar diferentes dispositivos ofrece una gran versatilidad pero hace más compleja la gestión.
Para facilitar la gestión de diferentes dispositivos de almacenamiento, y evitar que sea una labor 
compleja, tediosa y absorbente para el administrador, está la virtualización de almacenamiento. 
### 🔵 5.1. Fundamentos de Arquitectura de Sistemas
#### 🔹 5.1.1. Mecanismos de Protección del Procesador
Los mecanismos de protección del procesador son un conjunto de características y diseños 
incorporados en la arquitectura de las CPU modernas (como Intel x86/x64 o ARM) que tienen como 
objetivo principal aislar y proteger diferentes niveles de software y procesos entre sí, y especialmente, 
proteger al sistema operativo del software de aplicación y de sí mismo. Sin estos mecanismos, un error \nen una aplicación, o incluso un código malicioso, podría corromper la memoria del sistema operativo, 
acceder a dispositivos críticos o colapsar todo el sistema. 
Estos mecanismos son fundamentales para la estabilidad, seguridad y funcionalidad multiusuario y 
multitarea de los sistemas operativos actuales. En el contexto de la virtualización, también son vitales, 
ya que el hipervisor los utiliza para aislar las máquinas virtuales unas de otras y del hardware 
subyacente. 
##### 5.1.1.1. Anillos de Protección
Los anillos de protección son niveles jerárquicos de privilegios definidos por la arquitectura del 
procesador (especialmente en procesadores x86) para controlar el acceso a recursos críticos del 
sistema. El objetivo es garantizar la seguridad y estabilidad del sistema, evitando que el software no 
confiable afecte directamente al hardware o a otras partes sensibles.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Anillo 0 (Ring 0):
Es el nivel más privilegiado, normalmente reservado para el kernel (núcleo) del sistema 
operativo. Desde aquí se pueden ejecutar todas las operaciones privilegiadas: acceso completo a 
hardware, gestión de memoria, interrupciones, etc. 
- Anillo 3 (Ring 3):
Es el menos privilegiado, donde se ejecutan las aplicaciones y procesos de usuario. Aquí solo 
pueden llevarse a cabo operaciones comunes, sin acceso directo a hardware ni a recursos 
críticos. 
Algunas arquitecturas también definen anillos intermedios (1 y 2), aunque la mayoría de sistemas 
operativos modernos solo utilizan el 0 y el 3. 
##### 5.1.1.2. Operaciones privilegiadas
En esencia, las operaciones privilegiadas son la llave de acceso a los componentes más sensibles del 
hardware, y el mecanismo de virtualización se apoya en controlar rigurosamente su uso para mantener 
tanto la eficiencia como el aislamiento en entornos virtualizado. 
Las operaciones privilegiadas son aquellas instrucciones especiales del procesador que solo pueden \nejecutarse cuando el sistema operativo se encuentra en un modo de alto nivel de privilegio (como el 
modo kernel o supervisor). 
Estas operaciones permiten acceder y modificar recursos críticos del hardware, y su uso está restringido 
precisamente para asegurar la estabilidad y la seguridad del sistema. 
Ejemplos típicos de operaciones privilegiadas incluyen: 
- Modificar o configurar la gestión de memoria (como operar sobre la MMU, unidad de gestión de memoria). 
- Administración y control de interrupciones del sistema.
- Operaciones de entrada/salida directa con hardware.
- Cambios en registros de control del procesador o en las tablas internas utilizadas por el sistema operativo para gestionar recursos

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 5.2. Conceptos Clave de Virtualización
#### 🔹 5.2.1. Virtualización definición y beneficios
La virtualización es una técnica que, mediante un software intermediario (hipervisores, motores de 
contenedores), abstrae recursos físicos (hardware, almacenamiento, red, etc.) para crear entornos 
lógicos independientes (máquinas virtuales, contenedores) sobre una misma infraestructura. 
En un sistema virtualizado, la mayoría de las operaciones que realiza el sistema operativo invitado y sus 
aplicaciones son instrucciones comunes o no privilegiadas. 
Estas se ejecutan directamente en el procesador subyacente a su velocidad nativa. 
Es esta característica lo que la distingue de la emulación en cuyo sistema las instrucciones serán 
simuladas por software, sin llegar a permear al sistema operativo anfitrión, por lo que el conjunto de 
instrucciones del sistema invitado puede ser distinto. En emulación las instrucciones se traducen y 
simulan. 
Sin embargo, en virtualización el sistema físico absorbe y procesa estas operaciones de forma directa, 
contribuyendo significativamente a la alta eficiencia del sistema. 
Es solo cuando una operación requiere acceso privilegiado a los recursos críticos del hardware 
(operaciones privilegiadas) que se necesita un mecanismo de control para asegurar la estabilidad y el 
aislamiento. 
En una computadora física sin virtualización ni emulación, el núcleo del sistema operativo corre en el 
anillo 0 y las aplicaciones en el anillo 3. 
En virtualización, el reto es que cada sistema operativo invitado crea que está corriendo en el anillo 0, 
pero en realidad debe estar bajo el control del hipervisor para asegurar el aislamiento. 
Esto permite: 
- Eficiencia: Optimiza el uso de recursos físicos (consolidación de cargas).
- Aislamiento: Fallos o configuraciones en un entorno no afectan a otros.
- Flexibilidad administrativa: Migración en caliente, snapshots, y gestión centralizada.
- Escalabilidad bajo demanda: Creación/eliminación rápida de recursos virtuales.
- Sostenibilidad: Reduce el consumo energético (Green IT) y costos operativos.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.2.2. Máquina virtual
Una máquina virtual (VM, del inglés "Virtual Machine") es un programa que simula un ordenador real 
dentro de otro ordenador. Así, se pueden tener varios sistemas operativos funcionando al mismo 
tiempo en la misma máquina física. 
Las VMs se ejecutan sobre un sistema operativo principal (host) y cada una tiene su propio sistema 
operativo invitado (guest), además de procesador, memoria y disco duro virtuales. Todo esto se 
gestiona mediante un software especial llamado hipervisor, que reparte los recursos del ordenador real \nentre las distintas máquinas virtuales. 
#### 🔹 5.2.3. Hypervisor
El hipervisor es un software especializado o VMM (Virtual Machine Monitor) encargado de gestionar y 
abstraer el hardware físico, distribuyendo sus recursos entre las diferentes máquinas virtuales. Su 
función principal es exponer recursos de hardware -físicos o simulados- a un entorno virtualizado, 
donde los sistemas invitados los perciben como propios, aunque estén gestionados y compartidos por el 
mismo. 
Esto permite aislar, compartir y optimizar el uso de la infraestructura física subyacente, creando \nentornos seguros, replicables y escalables. 
Cuando un sistema operativo invitado dentro de una máquina virtual intenta ejecutar una operación 
privilegiada, el procesador no permite que esto suceda directamente si está en modo usuario. En su 
lugar, se produce una interrupción especial (trap) que transfiere el control al hipervisor. Este sistema de 
captura y gestión es crucial: el hipervisor es el encargado de decidir cómo y cuándo ejecutar realmente \nesas instrucciones privilegiadas, asegurando el aislamiento entre máquinas virtuales y evitando que un 
sistema invitado pueda afectar a los demás. 
Tipos de hipervisores: 
- Tipo 1 (bare metal): se ejecuta directamente sobre el hardware, sin un sistema operativo por debajo. El hipervisor actúa como un guarda de tráfico. No interpreta nada, pero controla y dirige 
cómo cada sistema operativo invitado accede directamente al hardware. Está entre ellos y el 
procesador, la RAM, los dispositivos… y gestiona el paso, pero no "traduce". Es el más empleado \nen entornos empresariales y centros de datos. 
Ejemplo: VMware ESXi, Microsoft Hyper-V en modo bare-metal, Xen. Ofrecen mayor 
rendimiento y seguridad. 
- Tipo 2 (hosted): se ejecuta como una aplicación sobre un sistema operativo anfitrión (Oracle
VirtualBox, VMware Workstation, Parallels Desktop). Más fáciles de instalar y usar para \nentornos de desarrollo.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.2.4. Infraestructura virtual
La infraestructura virtual constituye la implementación práctica de los modelos de protección 
jerárquica (anillos de ejecución) y gestión de operaciones privilegiadas dentro de un entorno de 
virtualización. Se trata de un conjunto de recursos virtualizados -vCPU, vRAM, vNIC, dispositivos de 
almacenamiento y E/S- proporcionados por el hipervisor mediante técnicas de emulación, 
paravirtualización o virtualización completa, según el tipo de implementación. 
Esta capa de abstracción permite que múltiples entornos invitados (guests) compartan 
simultáneamente un conjunto limitado de recursos físicos (host), garantizando aislamiento, control y \neficiencia. Las instrucciones sensibles emitidas por las VMs son interceptadas por el Virtual Machine 
Monitor (VMM), que las redirige, traduce o emula según la arquitectura del sistema (virtualización 
completa, virtualización asistida por hardware, etc.), mientras que las instrucciones no privilegiadas 
pueden ejecutarse directamente sobre el hardware, si la CPU lo permite (como en Intel VT-x o AMD-V). 
La infraestructura virtual moderna soporta funcionalidades como: 
- Live migration (migración en caliente de VMs entre servidores, incluyendo estado de RAM y
CPU). 
- Overcommitment de memoria y CPU (asignación de recursos virtuales totales superiores a los físicos, compensada dinámicamente). 
- Elasticidad de recursos.
- Snapshots (instantáneas que incluyen sistema, vDisco, vRAM, vCPU y archivos delta que pueden fusionarse para restaurar estados). 
- Balanceo dinámico de carga (DRS, Dynamic Resource Scheduling).
- Control de afinidad NUMA (el hipervisor o sistema operativo priorizan el uso de memoria local sobre memoria de otro nodo NUMA). 
Todo ello preservando la integridad y seguridad mediante mecanismos como zonas de protección por 
anillos, control de acceso basado en políticas del hipervisor y aislamiento de tráfico en redes virtuales. 
Componentes principales: 
- Host físico: hardware que proporciona los recursos computacionales subyacentes.
- Hipervisor o VMM (Virtual Machine Monitor): capa de software responsable de la virtualización, ya sea nativa (bare-metal) o alojada (hosted). 
- Máquinas virtuales (Guests): entornos operativos independientes que acceden a recursos virtuales gestionados por el hipervisor.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 5.3. Virtualización de Plataforma (o Virtualización de Hardware) 
La virtualización de plataforma (también conocida como virtualización de hardware) es una técnica que 
permite crear máquinas virtuales (VMs) que simulan un conjunto completo de componentes físicos 
(CPU, memoria, disco, red, etc.) sobre una máquina real (el host). Cada máquina virtual actúa como si 
fuera un ordenador independiente, capaz de ejecutar su propio sistema operativo y aplicaciones. 
### 🔵 Virtualización de servidores 
Uno de los usos más representativos de esta tecnología es la virtualización de servidores, que permite \nejecutar múltiples instancias virtuales de servidores físicos sobre una única máquina anfitriona. Esta 
capacidad facilita la consolidación de servidores, reduciendo el número de equipos físicos necesarios y 
mejorando significativamente la eficiencia del centro de datos. Gracias a esta arquitectura, se optimiza \nel uso de los recursos, se simplifica la administración de sistemas y se mejora la escalabilidad en \nentornos corporativos y de computación en la nube. 
Características de la virtualización de hardware: 
- Aislamiento: cada VM funciona como si estuviera sola, sin interferir con otras ni con el host.
- Independencia: permite ejecutar distintos sistemas operativos (Linux, Windows…) simultáneamente en el mismo host. 
- Aprovechamiento de recursos: optimiza la utilización del hardware físico al consolidar múltiples cargas de trabajo en un solo equipo. 
Escalabilidad y flexibilidad: facilita la creación, modificación y eliminación rápida de entornos, ideal para \nentornos de nube, desarrollo, pruebas o recuperación ante desastres. 
#### 🔹 5.3.1. Virtualización Completa
El sistema operativo invitado ejecuta directamente la mayoría de las instrucciones, excepto las 
privilegiadas, que requieren intervención del hipervisor. 
Técnicas de Implementación de la Virtualización de Hardware: 
##### 5.3.1.1. Virtualización Completa sin Asistencia de Hardware
En la virtualización completa sin asistencia de hardware surge un problema fundamental: el sistema 
operativo invitado espera ejecutarse en anillo 0, porque así obtiene acceso directo a las instrucciones 
privilegiadas que necesita para gestionar memoria y dispositivos. Sin embargo, ese anillo ya no está libre.

---

Administración de Bases de Datos. Virtualización. Cloud 
- En hipervisores bare-metal (tipo 1), es el propio hipervisor quien ocupa el anillo 0 real. Los sistemas invitados quedan relegados a niveles de menor privilegio (anillo 1 o 3), lo que hace que 
muchas de sus instrucciones privilegiadas fallen si se ejecutan directamente. 
- En hipervisores hosted (tipo 2), el anillo 0 real sigue ocupado por el kernel del sistema anfitrión
(Linux, Windows, etc.). El hipervisor funciona en anillo 3, como una aplicación más, y delega en \nel kernel del host el acceso al hardware. 
En ambos modelos, bare-metal y hosted, se repite el mismo desafío: cuando el guest intenta ejecutar 
instrucciones privilegiadas, la CPU las rechaza porque no tiene permiso. Para que el sistema invitado 
pueda seguir funcionando como si controlara la máquina, el hipervisor debe interceptar esas 
instrucciones y gestionarlas de otra forma. 
### 🔵 Binary translation 
Una de las técnicas clásicas para lograr esto es la traducción binaria dinámica: el hipervisor analiza 
bloques de código antes de ejecutarlos, detecta las instrucciones sensibles, las reemplaza por rutinas \nequivalentes que emulan su comportamiento, guarda el bloque modificado en caché y coloca 
trampolines que redirigían la ejecución hacia y desde ese bloque traducido. 
Los trampolines son fragmentos de código puente que redirigen la ejecución del procesador. En la 
virtualización, desvían el flujo desde el código original del sistema invitado hacia las rutinas seguras del 
hipervisor y viceversa, actuando como puntos de control transparentes. 
##### 5.3.1.2. Virtualización asistida por Hardware
Las extensiones de virtualización del procesador proporcionan mecanismos directamente en el 
hardware para ayudar al hipervisor en el proceso de trap-and-emulate. Esto permite que el hipervisor 
transfiera el control de forma más eficiente y con menos sobrecarga al procesador, acelerando 
significativamente la ejecución de operaciones privilegiadas y el rendimiento general de la VM. Es el 
método más común y eficiente hoy en día. 
La virtualización completa asistida por hardware, el hipervisor puede configurar el procesador 
(mediante tecnologías como Intel VT-x o AMD-V) para que la mayoría de las operaciones privilegiadas 
se ejecuten directamente, con mayor eficiencia y sin comprometer la seguridad. 
Mecanismos clave: 
- Modos de ejecución:
- Root mode: Para el hipervisor.
- Non-root mode: Para los guests (donde se ejecutan los OS invitados).
- VM exit: Cuando una máquina virtual en modo non-root ejecuta una operación privilegiada no permitida, el procesador transfiere el control al hipervisor (que funciona en modo root, con 
privilegios superiores, por encima del anillo 0 del guest, como en Intel VT-x o AMD-V). 
Un VM exit permite al hipervisor gestionar operaciones críticas solicitadas por el sistema invitado.

---

Administración de Bases de Datos. Virtualización. Cloud 
Al producirse un VM exit: 
- El hardware guarda automáticamente el estado para reanudar la VM.
- El hipervisor determina la causa y decide si emular, rechazar o gestionar la operación.
El verdadero núcleo de la virtualización asistida por hardware reside en cómo el hipervisor configura el 
modo non-root del procesador para permitir que el sistema operativo invitado ejecute ciertas 
operaciones privilegiadas directamente, sin intervención constante del hipervisor. Esta configuración se 
basa en las capacidades que ofrece la arquitectura del procesador, como las extensiones Intel VT-x o 
AMD-V. 
Cuando se inicializa una máquina virtual, el hipervisor consulta la arquitectura del procesador mediante 
instrucciones específicas (como CPUID en Intel), lo que le permite conocer qué características de 
virtualización están disponibles. A partir de esta información, define una estructura de control (VMCS -
Virtual Machine Control Structure- en Intel, VMCB -Virtual Machine Control Block- en AMD) en 
memoria RAM. Esta estructura contiene, entre otros datos, una lista detallada de qué operaciones e 
instrucciones ejecutadas por el sistema operativo invitado deben permitirse directamente en non-root 
mode y cuáles deben provocar un cambio de contexto (VM Exit) hacia el hipervisor en root mode. 
Una vez el procesador carga esta estructura en sus registros internos ocultos, puede evaluar cada 
instrucción ejecutada por el invitado. Si la instrucción está permitida según el VMCS, se ejecuta 
directamente en non-root mode, dentro del anillo correspondiente (normalmente el anillo 0 para el 
kernel del invitado). Si no está permitida, el procesador fuerza una transición controlada (VM Exit) para 
que el hipervisor tome el control. 
Este diseño permite aislar eficazmente a los sistemas operativos invitados, reducir el número de 
intervenciones del hipervisor y mejorar el rendimiento general del entorno virtualizado. Además, 
garantiza que el anillo 0 del sistema anfitrión quede protegido de cualquier operación privilegiada 
maliciosa o errónea del invitado, ya que todo se filtra previamente a través de las extensiones del 
procesador y la configuración inicial realizada por el hipervisor. 
### 🔵 Síntesis 
La asistencia por hardware permite que los sistemas operativos invitados mantengan la ilusión de \nejecutarse en anillos 0-3, aunque físicamente se ejecuten en modo non-root. El hipervisor configura 
previamente la estructura de control del procesador (VMCS/VMCB) para indicar qué operaciones 
privilegiadas no son toleradas y deben generar un VM-Exit. Cuando el guest intenta ejecutar este tipo 
de instrucción, el hardware intercepta la operación sin ejecutarla, genera un VM-Exit, y cede el control 
al hipervisor. Este se ejecuta en modo root y emula la instrucción de manera segura. 
#### 🔹 5.3.2. Paravirtualización
La paravirtualización es una técnica de virtualización en la que el sistema operativo invitado es 
consciente de que está siendo virtualizado y colabora activamente con el hipervisor para mejorar el 
rendimiento. A diferencia de la virtualización completa, en la paravirtualización el sistema operativo 
invitado no intenta ejecutar directamente las instrucciones privilegiadas, sino que las sustituye por 
llamadas específicas al hipervisor denominadas hypercalls.

---

Administración de Bases de Datos. Virtualización. Cloud 
Los hypercalls son análogos a las syscalls (llamadas al sistema), pero mientras las syscalls invocan 
servicios del kernel del sistema operativo, las hypercalls se dirigen al hipervisor, que actúa como capa 
intermedia para gestionar recursos de hardware como CPU, memoria o dispositivos de E/S. 
### 🔵 Paravirtualización clásica 
En los primeros sistemas de paravirtualización, el sistema operativo invitado debía ser modificado \nexpresamente para funcionar en un entorno virtualizado. Este enfoque se utilizó, por ejemplo, en el 
hipervisor Xen. 
En Xen, operaciones críticas del kernel, como la gestión de memoria o el control de interrupciones, se 
sustituían por hypercalls específicas. Por ejemplo, la instrucción MOV CR3 -usada para cambiar la tabla 
de páginas en sistemas nativos- era reemplazada por la llamada HYPERVISOR_mmu_update. 
En esta modalidad, ciertas operaciones del sistema operativo invitado, como las de entrada/salida 
(E/S), la gestión de memoria y el control de interrupciones, se modificaban para usar directamente 
hypercalls hacia el hipervisor. Por ejemplo, en lugar de ejecutar las instrucciones IN o OUT para acceder 
a un dispositivo, el sistema invitado llamaba a HYPERVISOR_block_request, delegando la operación al 
hipervisor. 
Este modelo requería modificar el kernel del sistema operativo invitado (por ejemplo, Linux 
paravirtualizado), pero ofrecía un rendimiento muy superior al de la virtualización completa sin 
asistencia de hardware, al eliminar la necesidad de traducir o interceptar instrucciones privilegiadas. 
Sin embargo, su principal desventaja era la falta de compatibilidad: solo podían ejecutarse sistemas 
operativos adaptados, lo que limitaba su uso con sistemas cerrados como Windows. 
### 🔵 Paravirtualización actual 
Con la aparición de procesadores con soporte de virtualización por hardware (Intel VT-x, AMD-V), ya 
no fue necesario modificar el kernel del sistema invitado. Aun así, la idea de colaboración entre el 
sistema invitado y el hipervisor evolucionó hacia un modelo más eficiente y modular, conocido como 
paravirtualización moderna. 
En este enfoque, representado por tecnologías como virtio, PV-on-HVM o Synthetic Drivers de Hyper-
V, no se modifica el sistema operativo, sino que se instalan controladores paravirtualizados 
(paravirtualized drivers). Estos controladores actúan como interfaz entre el sistema operativo invitado 
(frontend) y el hipervisor o emulador (backend), evitando la emulación completa de hardware. 
Como ejemplo, la tecnología virtio implementa la paravirtualización mediante un esquema colaborativo 
guest-host. Los drivers frontend en el sistema invitado envían solicitudes estructuradas (por ejemplo, 
virtio-blk para disco o virtio-net para red) en lugar de emular hardware, mientras el backend (en QEMU, 
Hyper-V o el propio hardware) las traduce a operaciones reales. 
Virtio utiliza virtqueues (memoria compartida) y notificaciones directas para evitar la sobrecarga de la \nemulación tradicional. Esto logra un rendimiento cercano al nativo en operaciones de E/S.

---

Administración de Bases de Datos. Virtualización. Cloud 
La tecnología es modular y se adapta a múltiples entornos, desde clouds (como AWS Nitro) hasta 
implementaciones locales como WSL2 en Windows. 
Virtio reduce la latencia de disco hasta un 80% frente a la emulación IDE y mejora notablemente el 
throughput (cantidad de datos transferidos con éxito en un tiempo determinado) de red. Su \nestandarización abierta -virtio o virtual I/O- lo ha convertido en el modelo dominante para la 
virtualización eficiente, combinando flexibilidad con altísimo rendimiento en operaciones de red y 
almacenamiento. 
Gracias a su estandarización abierta (virtio, o virtual I/O), esta forma de paravirtualización combina 
compatibilidad, flexibilidad y alto rendimiento, siendo hoy el modelo predominante en la virtualización \neficiente de dispositivos. 
### 🔵 5.4. Virtualización a Nivel de Sistema Operativo
(Contenedores) 
La virtualización a nivel de sistema operativo, también conocida como virtualización basada en 
contenedores, es un tipo de virtualización ligera que se diferencia notablemente de la virtualización 
tradicional con hipervisores. 
No cuenta con hipervisor. No se virtualiza hardware. No hay VM, ni anillo 0 virtual, ni non-root mode. 
Todo se ejecuta directamente sobre el kernel del host. 
Cada contenedor actúa como un entorno ligero y autocontenido. 
Incluye todo lo necesario para que una aplicación se ejecute: código, tiempo de ejecución, bibliotecas 
del sistema, herramientas del sistema y configuraciones. Sin embargo, no incluye un sistema operativo 
completo con su propio kernel; en su lugar, utiliza el kernel del sistema operativo del host. 
Ligeros y eficientes: Al compartir el kernel del host, los contenedores son más ligeros y rápidos que las 
VMs. Consumen menos recursos y permiten más instancias por servidor físico. 
Cuando se instala un contenedor, no se incluye un sistema operativo completo como ocurre en una 
máquina virtual. En realidad, lo que se instala es únicamente el userland de una distribución Linux \nespecífica, montado sobre su propio sistema de archivos aislado. Este userland incluye toda la jerarquía 
de directorios (/bin, /etc, /lib), comandos básicos, bibliotecas compartidas, shells y el gestor de 
paquetes correspondiente (apt, yum o apk), pero -crucialmente- excluye el kernel, que se comparte 
con el sistema anfitrión. 
Es decir, se copian al contenedor las herramientas de usuario, bibliotecas, shells, utilidades y gestor de 
paquetes propios de una distribución, pero no el kernel. El contenedor comparte el núcleo del sistema 
operativo anfitrión (host). 
Por tanto, elegir una imagen base como ubuntu, alpine o debian implica elegir el userland de esa 
distribución. Esto define qué herramientas están disponibles dentro del contenedor, qué compatibilidad 
binaria ofrece, cómo se instalan paquetes y cuál es el comportamiento por defecto del entorno. Por \nejemplo, Alpine Linux usa musl y apk, lo que da lugar a imágenes muy ligeras, mientras que Ubuntu o 
Debian utilizan glibc y apt, ofreciendo mayor compatibilidad.

---

Administración de Bases de Datos. Virtualización. Cloud 
Esta separación entre kernel (compartido) y userland (definido por la imagen) es lo que hace que los 
contenedores sean más eficientes que las máquinas virtuales. También permite ajustar cada contenedor 
a las necesidades del servicio que va a ejecutar, eligiendo el userland más adecuado en función del 
tamaño, la seguridad o la compatibilidad que se necesite. 
Aislamiento: Aunque los contenedores comparten el mismo kernel, están aislados entre sí con espacios 
de nombres de procesos, sistemas de archivos e interfaces de red propios, logrando esto mediante 
namespaces y cgroups. 
Las tecnologías clave para el aislamiento en la virtualización a nivel de sistema operativo son los 
namespaces y los cgroups, características fundamentales del kernel de Linux. Los namespaces aíslan la 
visibilidad de los recursos del sistema, creando "burbujas" lógicas donde los procesos de un contenedor 
solo ven sus propios recursos virtualizados, como IDs de proceso (PID), pilas de red, sistemas de 
archivos montados o nombres de host. Esto previene que los contenedores interfieran entre sí o con el 
anfitrión, dando la ilusión de un entorno dedicado. 
Los cgroups (grupos de control) gestionan el consumo de recursos, permitiendo limitar, contabilizar y 
aislar el uso de CPU, memoria, E/S de disco y red por parte de los procesos de un contenedor. 
Esto asegura que un contenedor no monopolice los recursos del sistema anfitrión, garantizando un 
rendimiento predecible y la estabilidad general. Son una herramienta de aislamiento de recursos, no de 
virtualización. Su rol es similar al de un "supervisor" que reparte equitativamente recursos físicos entre 
procesos, pero sin crear capas virtuales. Por eso se combinan con namespaces (para aislamiento) y 
Virtio (en VMs) para lograr soluciones completas como contenedores o paravirtualización. 
La combinación de namespaces para el aislamiento de la visibilidad y cgroups para el control del 
consumo de recursos es lo que permite que múltiples contenedores compartan eficientemente un 
mismo kernel de sistema operativo host de forma segura. 
Portabilidad: Encapsulan la aplicación y dependencias, permitiendo su ejecución consistente en cualquier \nentorno compatible con el motor de contenedores (ej., Docker), desde desarrollo hasta la nube. 
No necesitan hipervisor: A diferencia de la virtualización de plataforma, los contenedores interactúan 
directamente con el kernel del host sin una capa de hardware adicional. 
Mismo sistema operativo base: Una limitación es que todos los contenedores en un host deben usar el 
mismo kernel del SO subyacente (ej., Linux en host Linux, no Windows). 
### 🔵 5.5. Tipos de virtualización
#### 🔹 5.5.1. Virtualización de Aplicaciones
La virtualización de aplicaciones es una técnica que permite ejecutar una aplicación en un entorno 
aislado del sistema, sin necesidad de instalarla de forma tradicional ni modificar el sistema operativo 
base. En este modelo, la aplicación se empaqueta junto con sus bibliotecas y dependencias, creando un \nentorno de ejecución controlado y portátil. Sin embargo, a diferencia de los contenedores, la 
virtualización de aplicaciones no proporciona un userland completo; solo encapsula lo necesario para 
que una única aplicación funcione correctamente.

---

Administración de Bases de Datos. Virtualización. Cloud 
Esta ausencia de userland propio es precisamente la diferencia fundamental con respecto a la 
virtualización a nivel de sistema operativo, donde sí se simula un entorno de usuario completo. 
Los contenedores (como los gestionados con Docker o LXC) incluyen su propio sistema de archivos, 
conjunto de herramientas, bibliotecas del sistema, e incluso gestores de paquetes, aunque todos ellos se \nejecuten sobre el mismo kernel del host. Esto permite que los contenedores reproduzcan entornos más 
complejos y consistentes, adecuados para múltiples procesos o servicios interconectados. 
Por tanto, mientras que la virtualización de aplicaciones aísla solo la ejecución de una aplicación 
concreta y su contexto más inmediato, la virtualización a nivel de sistema operativo aísla un entorno 
completo, con su propio userland, capaz de ejecutar múltiples procesos. En resumen, la virtualización 
de aplicaciones no virtualiza un sistema operativo, sino solo una aplicación, lo que implica menor 
complejidad, menor aislamiento y mayor dependencia del entorno base. 
#### 🔹 5.5.2. Virtualización de puestos de usuario
La virtualización del puesto de trabajo permite a los usuarios acceder a sus entornos de escritorio y 
aplicaciones desde cualquier lugar, sin necesidad de estar físicamente en la oficina. Esta tecnología 
traslada el entorno de trabajo desde dispositivos no gestionados hacia una infraestructura centralizada, 
lo que mejora la seguridad, reduce los riesgos y permite a los administradores un mayor control sobre el 
software y los datos. 
Esta movilidad aporta importantes beneficios a la empresa, como la disminución de costes de IT, la 
optimización del uso de recursos, una mayor disponibilidad de las aplicaciones y la posibilidad de 
impulsar cambios en la cultura organizativa. 
##### 5.5.2.1. VDI: Virtual Desktop Infrastructure
La infraestructura de escritorio virtual (VDI) permite alojar entornos de escritorio completos en 
servidores centralizados. El usuario accede a un escritorio virtual -con su sistema operativo, aplicaciones 
y datos- a través de la red, desde cualquier dispositivo (PC, portátil, tablet, smartphone o cliente 
ligero), obteniendo una experiencia similar a la de un equipo físico. 
Estos escritorios virtuales se encapsulan en máquinas virtuales que se ejecutan en el servidor central 
mediante un hipervisor, lo que garantiza la separación y gestión eficiente de los recursos asignados a 
cada usuario. 
A cada usuario se le proporciona un escritorio virtual dedicado que se ejecuta en una máquina virtual 
propia. Esto implica mayor aislamiento, flexibilidad y capacidad de personalización, ya que cada \nescritorio tiene su propio sistema operativo y sus propias aplicaciones. 
Entre sus ventajas se encuentran el aumento de la seguridad, la reducción del soporte técnico, menores 
costes de hardware, continuidad de negocio y un menor impacto ambiental. Además, los usuarios 
pueden personalizar sus escritorios según sus necesidades, aunque trabajen desde una infraestructura 
compartida.

---

Administración de Bases de Datos. Virtualización. Cloud 
La seguridad se ve reforzada porque la información reside y se respalda en el centro de datos, evitando 
pérdidas locales y garantizando la integridad de los datos. Al mismo tiempo, al centralizar la gestión de 
aplicaciones se reducen los conflictos de software que suelen aparecer cuando cada equipo funciona de 
manera autónoma, lo que marca una diferencia clara con el modelo tradicional de PC independientes. 
Las implementaciones VDI pueden ser: 
- Persistentes: cada usuario conserva su escritorio personalizado entre sesiones.
- No persistentes: los escritorios se restauran a su estado original cada vez que el usuario cierra sesión. 
Entre las limitaciones del modelo VDI destacan los desafíos en la gestión de periféricos (impresoras, 
multimedia), la pérdida de autonomía del usuario, posibles problemas de red si no se gestiona 
adecuadamente y la complejidad en el mantenimiento de la infraestructura. 
La experiencia de uso depende de forma crítica de disponer de una red estable y con baja latencia, ya 
que cualquier interrupción puede afectar directamente al acceso al escritorio virtual. 
##### 5.5.2.2. RDS (Remote Desktop Services)
RDS (Remote Desktop Services) es una tecnología de sesiones compartidas que permite a múltiples 
usuarios trabajar en un mismo servidor, resultando eficiente y económica en consumo de recursos. 
En cambio, VDI (Virtual Desktop Infrastructure) ofrece escritorios dedicados, con mayor aislamiento y 
flexibilidad. Ambas soluciones pueden implementarse en un entorno on-premise, es decir, en un centro 
de datos (CPD) con instalaciones propias, siendo su antónimo más habitual la Cloud. 
Cuando este modelo de escritorios se consume desde la nube bajo un esquema de servicio gestionado, 
hablamos de DaaS (Desktop as a Service), que suele estar más asociado a entornos VDI pero que en 
algunos casos también incorpora variantes multisesión similares a RDS. 
##### 5.5.2.3. DaaS (Desktop as a Service)
DaaS (Escritorio como Servicio) es un modelo cloud en el que un proveedor externo aloja y gestiona 
infraestructura VDI en la nube, entregando escritorios virtuales a los usuarios a través de Internet bajo 
un modelo de suscripción (pago por uso). 
Características clave de DaaS: 
- Gestión por terceros: El proveedor (ej: Microsoft Azure Virtual Desktop, Amazon WorkSpaces,
VMware Horizon Cloud) se encarga del mantenimiento, actualizaciones y seguridad de la 
infraestructura. 
- Acceso bajo demanda: Los usuarios consumen escritorios virtuales sin necesidad de inversión inicial en hardware. 
- Escalabilidad automática: Añadir o reducir escritorios es rápido y flexible.
- Modelo de coste operativo (OpEx): Se paga solo por lo que se usa, sin costes de capital (CapEx).

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.5.3. Virtualización de Almacenamiento
La virtualización del almacenamiento, también conocida como almacenamiento definido por software, 
consiste en abstraer el almacenamiento lógico del físico, permitiendo gestionar múltiples dispositivos de 
almacenamiento como si se tratara de una única unidad. 
Esta técnica unifica recursos físicos y lógicos, simplificando su administración desde una consola central. 
Una de sus principales ventajas es que permite prescindir de la dependencia directa del hardware, 
aportando mayor flexibilidad, escalabilidad y disponibilidad del sistema. 
Tener un sistema RAID, del tipo que sea, permite proteger la información frente a caídas del sistema y \nevitar interrupciones de servicio, ya que no es necesario apagar el servidor. Sin embargo, con la 
virtualización se da un paso más, permitiendo desligarse aún más del hardware físico y gestionar el 
almacenamiento de forma centralizada y dinámica. 
Esta tecnología se utiliza sobre todo en entornos SAN (Storage Area Network), donde se agrupan 
múltiples dispositivos de almacenamiento conectados por una red de alta velocidad, lo que mejora el 
rendimiento en tareas como copias de seguridad, expansión de recursos o recuperación de datos. La 
virtualización puede implementarse mediante software (también denominado SDS, Software Defined 
Storage), hardware dedicado o soluciones de red. 
##### 5.5.3.1. Fundamentos y evolución tecnológica
Los sistemas de almacenamiento pueden presentar sus recursos en dos formas principales: por bloques 
o por ficheros. 
El acceso por bloques se realiza, habitualmente, a través de protocolos como Fibre Channel (FC), iSCSI, 
SAS o FICON, y es típico en infraestructuras de alto rendimiento, como entornos SAN (Storage Area 
Network) o cargas de trabajo críticas (bases de datos, virtualización). 
Por su parte, el acceso por ficheros utiliza protocolos como NFS (Network File System) o SMB/CIFS 
(Server Message Block/Common Internet File System), que permiten a los programas acceder y 
manipular archivos ubicados en ordenadores remotos, siendo comunes en entornos NAS (Network 
Attached Storage) o colaboración empresarial. 
La virtualización del almacenamiento no es una tecnología reciente. Empresas como DataCore trabajan \nen este campo desde finales de los años noventa, y su adopción ha aumentado en los últimos años 
gracias a fabricantes como IBM (SAN Volume Controller), HPE (3PAR), Dell EMC (PowerStore, Unity) 
o VMware (vSAN), que han desarrollado soluciones específicas o integrado capacidades avanzadas en 
sus plataformas. 
El funcionamiento básico de la virtualización consiste en presentar al usuario un espacio lógico para 
almacenar los datos, y encargarse internamente de traducir estas ubicaciones lógicas a ubicaciones 
físicas reales. Este proceso es gestionado por el software de virtualización, que mantiene una tabla de 
mapeo con los metadatos que relacionan ambas ubicaciones.

---

Administración de Bases de Datos. Virtualización. Cloud 
Algunas implementaciones no usan tablas, sino algoritmos que calculan dinámicamente la ubicación, 
como en sistemas distribuidos (Ceph, GlusterFS). En todos los casos, el sistema intercepta las 
operaciones de entrada/salida, traduce las direcciones lógicas en direcciones físicas y ejecuta la 
operación correspondiente sobre el dispositivo físico, permitiendo funcionalidades avanzadas como 
snapshots, réplicas o tiering automático. 
Evolución reciente: 
- La irrupción del almacenamiento definido por software (SDS) ha extendido la virtualización a \nentornos de nube y soluciones hiperconvergentes (Nutanix, vSAN).
- Nuevos protocolos como NVMe over Fabrics (NVMe-oF) optimizan el rendimiento en infraestructuras virtualizadas. 
- La integración con la nube híbrida permite gestionar almacenamiento local y remoto de forma unificada. 
##### 5.5.3.2. Técnicas clave de virtualización del almacenamiento
5.5.3.2.1. Configuración de Discos 
### 🔵 Thick Provisioning 
La asignación de discos virtuales puede hacerse mediante dos modelos principales: thick provisioning y 
thin provisioning. El thick provisioning, también llamado aprovisionamiento grueso o pesado, reserva de 
forma anticipada todo el espacio asignado al disco virtual. Este modelo presenta dos variantes: 
- lazy zeroed, donde los bloques se ponen a cero conforme se van utilizando.
- eager zeroed, donde todos los bloques se inicializan desde el principio, lo que mejora tanto la seguridad como el rendimiento en escrituras iniciales. 
El thick provisioning es particularmente útil en entornos con grandes volúmenes de datos y altos 
requerimientos de rendimiento continuo, como sistemas de bases de datos transaccionales. 
### 🔵 Thin Provisioning 
Por otro lado, el modelo thin provisioning o aprovisionamiento ligero solo ocupa el espacio físico 
necesario en cada momento, permitiendo un uso más eficiente de los recursos de almacenamiento. A 
medida que se escriben nuevos datos, el disco virtual va creciendo dinámicamente hasta alcanzar su 
tamaño máximo configurado. 
Aunque este sistema optimiza la utilización del espacio, puede presentar desafíos de rendimiento 
durante periodos de alta demanda de escritura.

---

Administración de Bases de Datos. Virtualización. Cloud 
Es importante destacar que cuando se eliminan archivos, el espacio físico no se libera automáticamente, 
ya que el sistema simplemente marca los bloques como disponibles para reescritura sin realizar una 
limpieza inmediata. Para recuperar este espacio se requieren herramientas específicas como TRIM para 
SSDs o UNMAP en entornos SAN. 
5.5.3.2.2. Particionamiento/Zoning 
El particionamiento, conocido como zoning en entornos SAN, permite dividir recursos físicos como el \nespacio de disco o el ancho de banda de red en unidades lógicas más manejables y aisladas. En 
implementaciones Fibre Channel, esto puede lograrse mediante hard zoning (aislamiento físico a nivel 
de puerto) o soft zoning (restricción lógica basada en identificadores WWN), cada uno con sus propias 
ventajas en términos de seguridad y flexibilidad. 
##### 5.5.3.3. Soluciones comerciales de virtualización
Actualmente existen diferentes soluciones comerciales que implementan virtualización del 
almacenamiento. IBM, por ejemplo, ofrece su producto SVC (SAN Volume Controller), que utiliza 
servidores con Linux para gestionar múltiples cabinas de almacenamiento IBM (conectadas por fibra) 
desde una interfaz web unificada, incluyendo modelos como los FlashSystem 5000, V7000 y V3700. Se 
trata de una solución robusta, escalable y sencilla de administrar, con soporte para protocolos 
modernos como NVMe over FC. 
HPE dispone de una alternativa flexible con HPE StoreVirtual VSA, una solución basada en software que 
puede implementarse como máquina virtual en entornos VMware o Hyper-V, permitiendo crear pools 
de almacenamiento distribuido. Su arquitectura scale-out facilita la expansión horizontal añadiendo 
nodos adicionales. 
VMware, por su parte, cuenta con vSAN, una solución integrada en su hipervisor ESXi que requiere al 
menos un disco SSD por servidor para caché y un mínimo de tres hosts para configuraciones de alta 
disponibilidad. Aunque es una solución eficaz y optimizada para entornos VMware, su principal 
limitación es el licenciamiento por socket y la dependencia de su ecosistema. 
Una propuesta destacada es la de DataCore SANsymphony, que opera sobre Windows aprovechando su 
amplia compatibilidad con controladores. Esta plataforma soporta prácticamente cualquier tipo de 
almacenamiento: desde FC, FCoE e iSCSI hasta SAS, SATA e incluso dispositivos legacy como SCSI o IDE. 
Para mitigar el impacto de discos lentos, emplea agresivos mecanismos de caching en RAM y técnicas 
de auto-tiering. Su enfoque abierto lo hace independiente de fabricantes, permitiendo configuraciones 
avanzadas como: 
- SAN basado en fibra o iSCSI.
- NAS mediante soporte nativo para SMB/CIFS y NFS.
- Réplica síncrona para alta disponibilidad local.
- Réplica asíncrona para recuperación ante desastres.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.5.4. Virtualización de Datos
Finalmente, es crucial diferenciar entre virtualización de almacenamiento y virtualización de datos. 
Mientras la primera se enfoca en abstraer los recursos físicos de almacenamiento, la virtualización de 
datos actúa como una capa de integración que permite acceder a fuentes de datos dispersas en 
diferentes formatos y ubicaciones sin necesidad de replicación. 
Esta tecnología proporciona una vista unificada que facilita el acceso y análisis de información 
heterogénea, siendo implementada por soluciones como Denodo o IBM Cloud Pak for Data, que 
permiten consultas consolidadas sobre múltiples sistemas manteniendo la gobernanza centralizada. Es 
importante comprender la relación entre virtualización de almacenamiento y virtualización de datos. 
La virtualización de almacenamiento por software crea una capa base que abstrae los recursos físicos, 
mientras que la virtualización de datos opera como una capa superior que se extiende sobre esta 
infraestructura virtualizada. Esta capa adicional integra fuentes de datos diversas sin replicación, 
proporcionando una vista unificada que permite consultas consolidadas sobre múltiples sistemas. 
Soluciones como Denodo o IBM Cloud Pak for Data implementan esta virtualización de datos, que 
depende fundamentalmente de la capa subyacente de virtualización de almacenamiento pero añade 
capacidades avanzadas de integración y gobernanza de datos. 
#### 🔹 5.5.5. Virtualización de Red
La virtualización de red es el proceso mediante el cual los recursos físicos de red, como switches, 
routers, firewalls o interfaces de red, son abstraídos mediante software para generar redes virtuales 
independientes y configurables. 
Esta tecnología permite crear entornos de red definidos por software, en los que las funciones de red se 
gestionan de forma centralizada y programable, sin necesidad de modificar físicamente la 
infraestructura. Las redes virtualizadas se comportan como si fueran redes físicas, pero con la ventaja 
de que pueden desplegarse, reconfigurarse y escalarse de forma más rápida y flexible. 
Uno de los principales beneficios de la virtualización de red es que facilita la movilidad de máquinas 
virtuales entre distintos servidores físicos, manteniendo la configuración de red estable y sin 
interrupciones. También permite aplicar políticas de seguridad, calidad de servicio o aislamiento entre 
redes desde una única consola de gestión, lo que mejora el control y reduce la complejidad operativa. 
Esta tecnología es especialmente importante en centros de datos modernos, donde conviven múltiples \nentornos virtualizados que comparten la misma infraestructura física. Entre las soluciones más 
conocidas destacan las redes definidas por software (SDN) y plataformas como VMware NSX, que 
permiten gestionar topologías de red completas de forma virtual.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.5.6. Virtualización de E/S (Input/Output)
La virtualización de entrada/salida se refiere a la capacidad de compartir y gestionar dispositivos físicos 
de E/S, como tarjetas de red, controladoras de almacenamiento, GPU o adaptadores de fibra, entre 
múltiples entornos virtuales. Esta técnica permite que las máquinas virtuales o contenedores accedan a \nestos dispositivos como si fueran propios, aunque en realidad estén compartiendo un único recurso 
físico. De esta forma, se consigue un uso más eficiente del hardware y se evita que cada máquina virtual 
requiera una tarjeta o dispositivo físico exclusivo. 
En los sistemas tradicionales, el acceso a dispositivos de entrada/salida puede suponer un cuello de 
botella cuando varias máquinas virtuales intentan acceder simultáneamente a los mismos recursos. Para 
mitigar este problema, la virtualización de E/S introduce mecanismos avanzados que permiten acceso 
directo, aislado y seguro. 
Tecnologías como SR-IOV (Single Root I/O Virtualization) permiten a una única tarjeta de red 
presentarse como múltiples interfaces virtuales independientes para distintas VMs, lo que mejora el 
rendimiento y reduce la latencia. 
En el ámbito gráfico, la virtualización de GPU (vGPU) permite asignar una tarjeta gráfica física a varias 
máquinas virtuales, habilitando el uso de aplicaciones con altas demandas visuales, como diseño 3D o 
procesamiento multimedia, en entornos virtualizados. En conjunto, la virtualización de E/S es clave 
para lograr eficiencia, escalabilidad y alto rendimiento en infraestructuras modernas de virtualización. 
#### 🔹 5.5.7. Software Defined Infrastructure (SDI)
La Infraestructura Definida por Software es un enfoque donde todos los componentes de 
infraestructura (computación, almacenamiento, redes) se abstraen y se gestionan como un pool 
unificado de recursos a través de software. 
Su objetivo es lograr centros de datos más flexibles, escalables y fáciles de administrar, con una 
provisión de recursos ágil y alineada a las necesidades de las aplicaciones. 
La SDI se basa en la virtualización y abstracción de los siguientes componentes clave: 
- Computación Definida por Software / Software Defined Compute (SDC): La virtualización de los servidores permite agrupar la capacidad de procesamiento de múltiples servidores físicos en 
un solo pool de recursos. La gestión de estos recursos se realiza a través de un software llamado 
hipervisor. 
- Almacenamiento Definido por Software / Software Defined Storage (SDS): El almacenamiento de datos se desacopla del hardware subyacente. Los discos duros de varios servidores se 
agrupan y se gestionan como un único recurso a través de un software. 
- Redes Definidas por Software / Software Defined Networking (SDN): La red tradicional, con sus dispositivos físicos como routers y switches, se virtualiza. El software de control se separa del 
hardware de reenvío, lo que permite la gestión de la red de manera centralizada y programática. 
La infraestructura definida por software (SDI) busca desacoplar las aplicaciones del entorno físico en el 
que se ejecutan.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 5.6. Impacto y Tendencias: Virtualización y Green IT
La virtualización es una de las principales tecnologías asociadas a Green IT (informática verde), ya que 
permite optimizar el uso de recursos informáticos, reducir el consumo energético y minimizar residuos \nelectrónicos, contribuyendo así a la sostenibilidad ambiental. 
La virtualización consiste en ejecutar múltiples máquinas virtuales o servicios en un solo servidor físico, 
lo que genera varios beneficios: 
- Reducción de hardware físico: Al consolidar servidores y aplicaciones, se necesita menos \nequipamiento, lo que disminuye la fabricación, transporte y disposición final de dispositivos
- Menor consumo energético: Menos servidores implican menos energía para funcionamiento y refrigeración; esto es clave en centros de datos donde la eficiencia energética es crítica 
- Reducción de residuos electrónicos: Con menos dispositivos físicos, hay menos desecho de \nequipos y se prolonga el ciclo de vida de los existentes
- Optimización operativa: Permite apagar o reducir recursos activamente en función de la demanda gracias a la flexibilidad de los entornos virtuales 
- Facilita la transición a la nube: La virtualización es el pilar de muchos servicios cloud, que generalmente tienen una huella energética más baja gracias a la compartición y optimización 
masiva de recursos 
- Contribuye a políticas de teletrabajo y digitalización: Al centralizar recursos y compartir infraestructura, soporta modelos de trabajo remoto y reduce la necesidad de desplazamientos, 
disminuyendo las emisiones indirectas 
- La virtualización, junto con otras prácticas de Green IT como el uso de energías renovables, el reciclaje de equipos y el desarrollo de software eficiente, es fundamental para reducir la huella 
de carbono, mejorar la eficiencia y avanzar hacia la sostenibilidad en las tecnologías de la 
información 
### 🔵 5.7. Diferencias entre virtualizar un S.O. e instalarlo
Podemos instalar diferentes sistemas operativos y elegir cuál usar al encender el ordenador. No 
podremos usarlos al mismo tiempo, y para cambiar de uno a otro debemos reiniciar el ordenador. 
Para no instalar dos sistemas operativos en el mismo, podemos virtualizar el sistema operativo. Si 
utilizamos esta opción, todos los sistemas operativos instalados funcionaran igual que si estuvieran 
instalados en distintos ordenadores, pero los podemos usar al mismo tiempo. Pero, también debemos 
tener en cuenta, que un sistema operativo virtualizado, no es tan potente como uno instalado.

---

Administración de Bases de Datos. Virtualización. Cloud 
Ventajas 
- Índices de utilización más altos.
Antes de la virtualización, los índices de utilización del servidor y almacenamiento en los centros 
de datos de la empresa rondaban menos del 50% (de hecho, los más comunes fueron del 10% al 
15%. 
A través de la virtualización, las cargas de trabajo pueden encapsularse y transferirse a los 
sistemas inactivos o sin uso. Esto significa que los sistemas existentes pueden consolidarse, y 
retrasarse o evitarse las compras de capacidad adicional del servidor. 
Se alcanzan índices de utilización del 60 al 80% para servidores x86. 
- Consolidación de recursos.
La virtualización permite consolidar múltiples recursos de TI; consolidación de almacenamiento, 
consolidar la arquitectura de sistemas, infraestructura de aplicación, datos y base de datos, 
interfaces, redes, escritorios, e incluso procesos de negocios, resultando en ahorros de costes y \nen mayor eficiencia. 
- Uso/coste menor de energía.
- Ahorros de espacio.
La ampliación del servidor aparece como un serio problema en la mayoría de los centros de 
datos empresariales. La virtualización mediante la consolidación de muchos sistemas virtuales \nen menos sistemas físicos, es una opción que soluciona este problema. 
- Recuperación de desastre/continuidad del negocio.
La virtualización puede incrementar la disponibilidad de los índices del nivel de servicio en 
general y proporcionar nuevas opciones de soluciones para la recuperación de desastre. Hasta el 
85% de mejora en tiempo de recuperación de paradas imprevistas. 
- Costes de operación reducidos.
El gasto de una empresa en también disminuye. La virtualización puede cambiar ese ratio, 
reducir la carga total de trabajo administrativo y ahorrar costes de operación. 
- Reutilización de hardware existente.
Utilizar software más moderno y optimizar el aprovechamiento de todos los recursos de 
hardware. 
- Capacidad para el provisioning de nuevas aplicaciones en cuestión de minutos, en lugar de días o semanas. 
- Rápida incorporación de nuevos recursos para los servidores virtualizados.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Reducción de los costes de espacio y consumo necesario de forma proporcional al índice de consolidación logrado (estimación media 10:1). 
- Administración global centralizada y simplificada.
- Permite gestionar el CPD como un pool de recursos o agrupación de toda la capacidad de procesamiento, memoria, red y almacenamiento disponible en nuestra infraestructura. 
- Mejora en los procesos de clonación y copia de sistemas.
Mayor facilidad para crear entornos de test que permiten poner en marcha nuevas aplicaciones 
sin impactar a la producción, agilizando el proceso de las pruebas. 
- Aislamiento.
Un fallo general de sistema de una máquina virtual no afecta al resto de máquinas virtuales. 
- Mejora de TCO y ROI.
- Para decidir invertir en nuevas tecnologías, los directivos utilizan unas métricas para valorar que beneficios retornaran esas inversiones: 
- TCO (Total Cost of Ownership).
Es el Costo total de propiedad, es decir, la medición de los costos involucrados directa o 
indirectamente en la adquisición productos hardware/software, la implantación de nuevos 
sistemas etc. 
- ROI (Return On Investment).
Es el Retorno de la inversión, utilizado para estimar los beneficios que tendrá esa inversión, 
teniendo en cuenta el costo. También se puede considerar el tiempo que se tardará en 
compensar los gastos hasta obtener beneficios. 
- Reduce los tiempos de parada.
- Migración en caliente de máquinas virtuales (sin pérdida de servicio) de un servidor físico a otro, \neliminando la necesidad de paradas planificadas por mantenimiento de los servidores físicos.
- Balanceo dinámico de máquinas virtuales entre los servidores físicos que componen el pool de recursos, garantizando que cada máquina virtual ejecute en el servidor físico más adecuado y 
proporcionando un consumo de recursos homogéneo y óptimo en toda la infraestructura. 
- Contribución al medio ambiente -Green IT- por menor consumo de energía en servidores físicos.
- Alta disponibilidad.

---

Administración de Bases de Datos. Virtualización. Cloud 
Desventajas 
- Alta dependencia de un solo equipo físico.
Se facilita la administración, al disponer de los equipos virtuales en un solo dispositivo, pero se 
pierden las ventajas de la redundancia. 
- El hardware está limitado pues necesita ser compatible con el hypervisor.
- El hardware para virtualizar debe ser abundante en recursos lo cual eleva su precio.
- A medida que se agregan máquinas virtuales, disminuye los recursos para cada uno y aumenta el trabajo de administración y seguridad. 
### 🔵 5.8. Seguridad en entornos virtualizados
La seguridad en entornos virtualizados es un aspecto esencial dentro de la administración de sistemas 
modernos. Aunque la virtualización ofrece ventajas como el aislamiento entre máquinas, la flexibilidad 
y la eficiencia en el uso de recursos, también introduce nuevos riesgos que deben gestionarse 
adecuadamente para evitar vulnerabilidades tanto en los sistemas anfitriones como en las máquinas 
virtuales. 
### 🔵 Riesgos y vulnerabilidades comunes 
Uno de los principales riesgos es la dependencia del hipervisor, ya que cualquier fallo o vulnerabilidad en él 
puede comprometer todas las máquinas virtuales que gestiona. Si un atacante logra acceso al hipervisor, 
puede controlar o manipular los sistemas invitados, generando un punto único de fallo crítico. 
También existen amenazas relacionadas con la configuración incorrecta de redes virtuales, que pueden 
permitir el acceso no autorizado entre máquinas, la exposición de servicios internos o fugas de datos. 
Asimismo, el uso compartido de recursos físicos (CPU, memoria o almacenamiento) puede originar 
ataques de canal lateral si no se implementan medidas de aislamiento adecuadas. 
Otro riesgo frecuente es la fuga de información a través de snapshots o discos virtuales, especialmente 
cuando se almacenan sin cifrado o en ubicaciones compartidas. Del mismo modo, el uso de máquinas 
virtuales obsoletas o no actualizadas puede introducir vulnerabilidades heredadas del sistema operativo 
o de las aplicaciones que contienen. 
### 🔵 Buenas prácticas de seguridad 
Para reducir estos riesgos, se deben aplicar políticas específicas de seguridad adaptadas a entornos 
virtualizados. Algunas de las más relevantes son: 
- Mantener actualizado el hipervisor y los sistemas invitados con los últimos parches de seguridad. 
- Restringir el acceso al hipervisor mediante autenticación fuerte, uso de redes de administración separadas y control de roles (RBAC).

---

Administración de Bases de Datos. Virtualización. Cloud 
- Segregar redes virtuales para aislar tráfico interno, de gestión y de usuario, evitando que una máquina comprometida afecte a otras. 
- Cifrar discos virtuales y snapshots, especialmente en entornos multiusuario o cuando los datos se almacenan fuera del host principal. 
- Utilizar herramientas de monitorización para detectar comportamientos anómalos, consumo irregular de recursos o accesos no autorizados. 
- Deshabilitar dispositivos virtuales innecesarios, como unidades ópticas o puertos USB virtuales, que pueden servir como punto de entrada de malware. 
Seguridad en entornos de producción y nube 
En infraestructuras empresariales o en entornos de nube, la seguridad virtualizada debe complementarse 
con controles adicionales como la segmentación por VLAN, firewalls virtuales, antivirus y sistemas 
IDS/IPS (Intrusion Detection/Prevention Systems) integrados en cada capa de red. 
Además, se recomienda establecer políticas de copia de seguridad cifrada y replicación segura entre 
servidores físicos, asegurando que los datos virtualizados puedan recuperarse sin comprometer su 
confidencialidad. 
La seguridad en sistemas virtualizados depende tanto de la arquitectura como de la disciplina operativa. 
Aplicar medidas preventivas, mantener los entornos actualizados y monitorizar constantemente las 
máquinas virtuales permite reducir riesgos y garantizar la estabilidad de la infraestructura tecnológica. 
5.9. Programas útiles para virtualizar S.O. 
Desde el punto de vista económico, existen tres tipos de software para virtualizar: 
- De pago (privativos).
La empresa VMware proporciona versiones de pago y gratuitas. 
- Gratuitos (freeware).
Tenemos el Virtual PC de Microsoft, compatible con versiones de XP, Vista y Windows 7. 
- Y libres (FOOS).
Como Xen, OpenVZ y VirtualBox, que funcionan en Mac OS, Windows y GNU/Linux. Permiten 
virtualizar la mayoría de S.O actuales y los que están sin soporte.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
+ Info 
Microsoft provee Windows Server 2008 R2 Hyper-V cuya función 
de virtualización está incluida sin cargo en la licencia del servidor. 
También existen webs que permiten rellenar un formulario y 
descargar una máquina virtual a personalizada. 
 
 
A la hora de seleccionar una solución de virtualización, es importante no solo distinguir entre software 
de pago, gratuito o libre, sino también comprender las capacidades, limitaciones y casos de uso de cada 
plataforma. 
A continuación, se describen en detalle dos de las herramientas más representativas del sector, tanto en \nentornos empresariales como personales, comenzando por las soluciones de tipo bare-metal más \nextendidas en el ámbito profesional: Hyper-V, integrada en los sistemas de Microsoft, y vSphere, la 
plataforma de virtualización líder de VMware. 
#### 🔹 5.9.1. Hyper-V
Hyper-V es una plataforma de virtualización de Microsoft integrada en Windows Server y versiones 
Pro/Enterprise de Windows 10/11. Como hipervisor tipo 1 (bare-metal), se ejecuta directamente 
sobre el hardware, permitiendo la creación y gestión de máquinas virtuales (VMs) con sistemas 
operativos invitados. Su diseño optimiza el uso de recursos, facilita la consolidación de servidores y 
mejora la eficiencia operativa en entornos físicos y cloud. 
### 🔵 Arquitectura y Componentes Clave 
Hyper-V utiliza virtualización asistida por hardware para maximizar el rendimiento. Soporta VMs de 
Generación 1 y Generación 2 (UEFI/Secure Boot), con almacenamiento en discos virtuales VHDX 
(hasta 64 TB). Incluye funciones avanzadas como Live Migration (movimiento de VMs sin downtime), 
checkpoints (snapshots) y conmutadores virtuales (vSwitch) para redes aisladas. 
Hyper-V incluye capacidades avanzadas como Live Migration, que permite mover máquinas virtuales 
(VMs) entre hosts físicos sin interrupción del servicio, garantizando alta disponibilidad y mantenimiento 
sin downtime. Otra función clave es la Virtualización Anidada (Nested Virtualization), la cual habilita la \nejecución de Hyper-V dentro de una máquina virtual, ideal para entornos de desarrollo, pruebas y 
formación. Esta última requiere habilitación manual mediante PowerShell y CPUs compatibles con \nextensiones de virtualización.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
### 🔵 Escalabilidad y Rendimiento 
La plataforma soporta escalamiento masivo, con límites de 2048 CPUs lógicas, 24 TB de RAM por host 
y 1024 VMs activas por servidor (Windows Server 2022). Incluye tecnologías como SR-IOV para reducir 
latencia en E/S y Replicación de Hyper-V para recuperación ante desastres. Es compatible con cargas 
de trabajo Windows y Linux (Ubuntu, Red Hat). 
### 🔵 Integración con Ecosistema Microsoft 
Hyper-V se integra con herramientas como System Center Virtual Machine Manager (SCVMM) para 
gestión centralizada y Azure Arc para administración híbrida. Permite replicación en la nube mediante 
Azure Site Recovery y backups con Azure Backup. Además, ofrece soporte para contenedores Windows 
Server y Kubernetes. 
### 🔵 Requisitos y Casos de Uso 
Requiere CPUs con SLAT, mínimo 4 GB de RAM y sistemas Windows Server 2012 R2+ o Windows 
10/11 Pro/Enterprise. Es ideal para: 
- Data Centers: Consolidación de servidores y alta disponibilidad.
- Desarrollo/Testing: Entornos aislados con snapshots reversibles.
- Cloud Híbrido: Migración de cargas de trabajo a Azure.
- Seguridad: Aislamiento de aplicaciones críticas en VMs independientes.

---

Administración de Bases de Datos. Virtualización. Cloud 
#### 🔹 5.9.2. vSphere vSphere es la plataforma de virtualización de VMware para la creación y administración de 
infraestructuras virtuales empresariales. Está compuesta principalmente por VMware ESXi, un 
hipervisor tipo 1 (bare-metal), y vCenter Server, la herramienta de gestión centralizada. vSphere 
permite consolidar servidores físicos, ejecutar múltiples máquinas virtuales (VMs) en un único host y 
facilitar la administración eficiente de recursos en entornos locales y cloud híbridos. 
### 🔵 Arquitectura y Componentes Clave 
La arquitectura de vSphere se basa en VMware ESXi, que se instala directamente sobre el hardware del 
servidor y aloja las VMs. La gestión de múltiples hosts se realiza mediante vCenter Server, que 
centraliza tareas como aprovisionamiento, monitorización, automatización y migración de cargas de 
trabajo. Las VMs utilizan discos virtuales en formato VMDK y pueden aprovechar características como 
vMotion (migración en caliente entre hosts), Snapshots, Distributed Resource Scheduler (DRS) y High 
Availability (HA). 
Además, vSphere soporta redes virtuales mediante vSwitches, vDS (Distributed Switches) y 
controladores SR-IOV para mejorar el rendimiento de E/S. 
Escalabilidad y Rendimiento 
vSphere ofrece una gran capacidad de escalado: hasta 768 CPUs lógicas por host, 24 TB de RAM y miles 
de VMs en un clúster gestionado. Soporta tecnologías como NUMA awareness, vSphere Storage DRS, 
Fault Tolerance (FT) para alta disponibilidad sin pérdida de datos, y DirectPath I/O para acceso directo 
a hardware. Es compatible con sistemas operativos Windows y diversas distribuciones de Linux 
(Debian, Red Hat, Ubuntu, SUSE, etc.). 
Integración con Ecosistema VMware y Cloud 
vSphere se integra con un amplio ecosistema de herramientas VMware como vSAN (almacenamiento 
definido por software), NSX (virtualización de red), vRealize Suite (automatización y monitoreo) y 
VMware Cloud Foundation. Además, permite extender infraestructuras a la nube a través de VMware 
Cloud on AWS, Azure VMware Solution y otras nubes públicas. Incluye soporte para contenedores 
mediante vSphere with Tanzu, que permite gestionar clústeres Kubernetes directamente desde 
vCenter. 
### 🔵 Requisitos y Casos de Uso 
VMware ESXi requiere servidores con procesador x86-64 compatible con virtualización asistida por 
hardware (Intel VT-x o AMD-V), 4 GB de RAM como mínimo (recomendado: 8+ GB), y dispositivos de 
almacenamiento compatibles.

---

Administración de Bases de Datos. Virtualización. Cloud 
Es una solución ideal para: 
- Data Centers empresariales: Consolidación de cargas, balanceo de recursos y alta disponibilidad. 
- Entornos críticos: Tolerancia a fallos, recuperación ante desastres, políticas de seguridad granular. 
- Automatización IT: Implementación de plantillas, aprovisionamiento dinámico y orquestación de servicios. 
- Integración híbrida y cloud-native: Soporte nativo para cargas de trabajo tradicionales y modernas (contenedores y microservicios). 
### 🔵 5.10. Infraestructura Hiperconvergente (HCI)
#### 🔹 5.10.1. Definición y características
La infraestructura hiperconvergente (HCI, Hyper-Converged Infrastructure) es un modelo de 
arquitectura informática que integra en un único sistema físico los recursos de cómputo, 
almacenamiento, red y virtualización, gestionándolos de forma unificada mediante software. 
A diferencia de las infraestructuras tradicionales, donde cada componente (servidores, cabinas de 
almacenamiento y switches) se administra de manera independiente, la HCI consolida todos esos \nelementos en una plataforma centralizada y automatizada. 
Su objetivo principal es simplificar la gestión de los centros de datos y optimizar el uso de los recursos, 
reduciendo la complejidad, el coste y los tiempos de despliegue. Gracias a la virtualización, los recursos 
físicos se abstraen en capas lógicas que pueden asignarse dinámicamente según las necesidades del 
sistema o las aplicaciones que se ejecutan. 
Una infraestructura hiperconvergente está compuesta por nodos (equipos físicos) que combinan 
procesadores, memoria, discos y controladoras de red. Cada nodo se conecta a los demás formando un 
clúster, donde los recursos se agrupan y comparten de manera transparente. Esto permite escalar la 
capacidad del sistema simplemente añadiendo nuevos nodos, sin necesidad de rediseñar toda la 
infraestructura. 
Entre las características más destacadas de la hiperconvergencia se incluyen: 
- Integración total: agrupa cómputo, almacenamiento y red bajo una misma capa de virtualización. 
- Gestión centralizada: permite controlar todo el entorno desde una consola única, reduciendo la complejidad operativa. 
- Escalabilidad horizontal: es posible ampliar la capacidad añadiendo nuevos nodos sin interrupciones ni configuraciones complejas.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Alta disponibilidad: los datos y máquinas virtuales se distribuyen automáticamente entre nodos, garantizando tolerancia a fallos. 
- Automatización: muchas tareas de mantenimiento, balanceo de carga y recuperación se \nejecutan de forma automática.
- Optimización del rendimiento: el software de gestión distribuye los recursos según la demanda \nen tiempo real.
- Reducción de costes: disminuye el gasto en hardware especializado y en administración, al \neliminar cabinas o redes de almacenamiento externas.
En esencia, la infraestructura hiperconvergente representa la evolución natural de la virtualización 
tradicional hacia un modelo más inteligente, escalable y eficiente, que prepara el camino para la 
computación en la nube y los entornos híbridos. 
#### 🔹 5.10.2. Componentes principales (cómputo, red, almacenamiento)
La infraestructura hiperconvergente se basa en la integración de tres componentes fundamentales: 
cómputo, red y almacenamiento, que dejan de funcionar como unidades independientes para 
convertirse en recursos virtualizados gestionados desde una misma plataforma. 
Esta unificación permite crear un entorno flexible y escalable, donde los recursos físicos se abstraen 
mediante software y se asignan dinámicamente según la carga de trabajo. 
Cómputo (procesamiento) 
El componente de cómputo proporciona la capacidad de procesamiento necesaria para ejecutar 
máquinas virtuales, aplicaciones y servicios. 
En una arquitectura hiperconvergente, cada nodo físico incluye uno o varios procesadores (CPU) y 
memoria RAM, formando un clúster distribuido que comparte recursos entre todas las máquinas 
virtuales alojadas. 
El software de virtualización -generalmente un hipervisor como VMware ESXi, Microsoft Hyper-V o 
KVM- gestiona la asignación de CPU y memoria, garantizando equilibrio de carga y tolerancia a fallos. 
Si un nodo deja de funcionar, las máquinas virtuales se migran automáticamente a otros nodos 
disponibles mediante tecnologías de alta disponibilidad (HA) o vMotion, sin interrumpir el servicio. 
### 🔵 Red 
La red en una infraestructura hiperconvergente conecta todos los nodos entre sí, permitiendo la 
comunicación entre las máquinas virtuales, los servicios de gestión y los usuarios finales. 
Esta red se implementa mediante conmutadores virtuales (vSwitches) y adaptadores de red físicos 
(NICs), configurados para ofrecer redundancia y alto rendimiento.

---

Administración de Bases de Datos. Virtualización. Cloud 
El tráfico de red se segmenta en diferentes canales: 
- Red de gestión, que conecta los nodos y permite la administración del clúster.
- Red de almacenamiento, utilizada para sincronizar datos entre nodos.
- Red de usuario o producción, por donde circula el tráfico de las aplicaciones.
Las soluciones de hiperconvergencia suelen emplear tecnologías de red definida por software (SDN), 
que permiten automatizar la configuración, aplicar políticas de seguridad dinámicas y optimizar el flujo 
de datos sin intervención manual. 
### 🔵 Almacenamiento 
El almacenamiento es uno de los pilares más importantes de la arquitectura HCI. 
En lugar de depender de cabinas SAN o NAS externas, cada nodo aporta su propio conjunto de discos 
(HDD y SSD) que se combinan mediante software para formar un pool de almacenamiento virtualizado 
y distribuido. 
Este modelo se conoce como Software-Defined Storage (SDS) y ofrece ventajas como replicación 
automática de datos, deduplicación, compresión y aprovisionamiento dinámico. 
Las tecnologías como VMware vSAN, Nutanix Distributed Storage Fabric o Microsoft Storage Spaces 
Direct (S2D) permiten que los datos se distribuyan y sincronicen entre los nodos, asegurando tanto el 
rendimiento como la disponibilidad. 
En caso de fallo de un nodo o de un disco, los datos permanecen accesibles desde las réplicas 
almacenadas en los demás nodos del clúster, garantizando la continuidad del servicio. 
La combinación de estos tres componentes -procesamiento, red y almacenamiento- bajo una capa de 
software común convierte a la infraestructura hiperconvergente en un sistema modular, tolerante a 
fallos y de gestión unificada. 
Gracias a esta integración, los administradores pueden ampliar los recursos de manera sencilla y 
mantener entornos estables con un esfuerzo operativo significativamente menor. 
#### 🔹 5.10.3. Ventajas y diferencias frente a infraestructuras tradicionales
La infraestructura hiperconvergente (HCI) representa un cambio profundo respecto a los modelos 
tradicionales de centros de datos. 
En las infraestructuras convencionales, los recursos de cómputo, almacenamiento y red se gestionan 
como sistemas separados, lo que implica una mayor complejidad operativa, costes de mantenimiento \nelevados y procesos de escalado poco ágiles. 
Por el contrario, la HCI unifica todos esos recursos en una única capa de software, simplificando su 
administración y ofreciendo una flexibilidad mucho mayor.

---

Administración de Bases de Datos. Virtualización. Cloud 
Entre las principales ventajas de la infraestructura hiperconvergente destacan: 
Gestión centralizada: toda la infraestructura se administra desde una consola única, reduciendo el 
tiempo dedicado a tareas de configuración y supervisión. 
Escalabilidad ágil: basta con añadir nuevos nodos para ampliar la capacidad de procesamiento o 
almacenamiento sin necesidad de rediseñar la arquitectura. 
Alta disponibilidad: la replicación automática de datos y la distribución de cargas entre nodos aseguran 
continuidad del servicio incluso ante fallos de hardware. 
Automatización: las tareas de mantenimiento, copia de seguridad y optimización del rendimiento se \nejecutan de forma automática mediante software inteligente. 
Eficiencia en costes: al eliminar la necesidad de cabinas SAN o redes de almacenamiento dedicadas, se 
reduce la inversión inicial y los gastos de operación. 
Rápida implementación: la infraestructura puede desplegarse en cuestión de horas, frente a las 
semanas o meses requeridos por las infraestructuras tradicionales. 
Mayor rendimiento: el uso de almacenamiento distribuido y tecnología flash mejora significativamente 
la velocidad de acceso a los datos. 
Integración con la nube: muchas soluciones hiperconvergentes se integran con entornos híbridos, 
permitiendo extender cargas de trabajo hacia la nube pública o privada. 
En cuanto a las diferencias clave con las infraestructuras tradicionales, destacan varios aspectos 
técnicos y operativos: 
Arquitectura: 
Tradicional: componentes separados (servidores, almacenamiento, red). 
Hiperconvergente: todos los recursos integrados en nodos modulares gestionados por software. 
Escalabilidad: 
Tradicional: requiere redimensionar la infraestructura completa. 
Hiperconvergente: se amplía horizontalmente añadiendo nodos de manera inmediata. 
Gestión: 
Tradicional: múltiples herramientas y equipos especializados. 
Hiperconvergente: una consola unificada con control centralizado.

---

Administración de Bases de Datos. Virtualización. Cloud 
Costes y mantenimiento: 
Tradicional: inversión elevada en hardware especializado y mantenimiento constante. 
Hiperconvergente: menor coste de adquisición y operación gracias a la automatización y consolidación. 
Resiliencia: 
Tradicional: la tolerancia a fallos depende de configuraciones complejas y sistemas externos. 
Hiperconvergente: la redundancia y replicación están integradas en el propio software de gestión. 
Evolución tecnológica: 
Tradicional: pensada para entornos estáticos y de crecimiento previsible. 
Hiperconvergente: diseñada para entornos dinámicos, virtualizados y orientados a la nube. 
Las infraestructuras hiperconvergentes responden a la necesidad actual de mayor agilidad, reducción de 
costes y simplificación operativa en los centros de datos modernos. 
De esta manera, las organizaciones pueden escalar sus servicios de forma progresiva, optimizando los 
recursos existentes y adaptándose con rapidez a las nuevas demandas tecnológicas. 
#### 🔹 5.10.4. Soluciones comerciales: VMware, vSAN, Dell EMC VxRail,
### 🔵 Nutanix 
Las soluciones comerciales de infraestructura hiperconvergente (HCI) integran en un solo sistema los 
recursos de cómputo, almacenamiento y red, gestionados mediante software especializado. Estas 
plataformas combinan hardware estandarizado con herramientas de virtualización avanzadas, 
ofreciendo entornos escalables, resilientes y de administración centralizada. Entre las más utilizadas \nen entornos profesionales se encuentran VMware vSAN, Dell EMC VxRail y Nutanix, que representan los 
principales enfoques del mercado actual. 
### 🔵 VMware y vSAN 
VMware es una de las empresas pioneras en virtualización y una referencia en entornos corporativos. Su \necosistema HCI se basa en vSphere (para la virtualización de servidores) y vSAN (para la virtualización 
del almacenamiento). 
vSAN (Virtual SAN) permite agrupar los discos duros y unidades SSD de varios servidores físicos (hosts 
ESXi) en un único volumen lógico compartido. De esta forma, el almacenamiento se gestiona como un 
recurso distribuido, con alta disponibilidad, replicación automática y deduplicación de datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
Entre sus ventajas destacan: 
- Integración total con vCenter, que permite la gestión unificada de toda la infraestructura.
- Compatibilidad con funciones avanzadas como vMotion, HA (High Availability) o DRS
(Distributed Resource Scheduler). 
- Optimización del rendimiento mediante caché SSD y escalabilidad horizontal añadiendo nuevos nodos. 
VMware vSAN es ampliamente utilizado en centros de datos virtualizados, entornos cloud híbridos y 
organizaciones que ya utilizan la suite de virtualización de VMware. 
### 🔵 Dell EMC VxRail 
VxRail, desarrollado conjuntamente por Dell EMC y VMware, es una solución hiperconvergente llave en 
mano que integra hardware, software y servicios en un único sistema validado. 
Cada nodo de VxRail combina servidores Dell PowerEdge con vSphere y vSAN, ofreciendo una 
infraestructura completamente integrada y optimizada para entornos virtualizados. 
Sus principales características incluyen: 
- Implementación simplificada: el sistema puede desplegarse en menos de una hora, con configuración automatizada. 
- Gestión centralizada desde vCenter, sin necesidad de herramientas adicionales.
- Escalabilidad modular, añadiendo nodos según las necesidades del negocio.
- Actualizaciones automáticas y alineadas entre hardware y software, lo que reduce los riesgos de incompatibilidad. 
VxRail está orientado a empresas que buscan soluciones hiperconvergentes de alto rendimiento, con 
soporte técnico unificado y fácil integración en entornos de nube híbrida. 
### 🔵 Nutanix 
Nutanix es otra de las principales plataformas de HCI del mercado y se distingue por su arquitectura 
definida por software. Su sistema operativo AOS (Acropolis Operating System) permite la 
virtualización completa de almacenamiento, cómputo y red, gestionada desde la consola central Prism. 
Entre sus ventajas más relevantes se encuentran: 
- Compatibilidad con múltiples hipervisores, incluyendo AHV (propietario), VMware ESXi e
Hyper-V. 
- Gestión simplificada mediante interfaz web, con monitorización y automatización integradas.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Escalabilidad ilimitada mediante el modelo de nodos independientes.
- Recuperación ante desastres y alta disponibilidad mediante replicación de datos y snapshots.
- Integración nativa con servicios de nube pública, permitiendo implementar estrategias híbridas y multi-cloud. 
Nutanix destaca por su flexibilidad, automatización avanzada y gran rendimiento, siendo muy popular \nen entornos corporativos y administraciones públicas que buscan consolidar su infraestructura. 
Estas soluciones comerciales representan el estándar de referencia en entornos empresariales y centros 
de datos modernos. 
Su adopción depende del tamaño de la organización, las necesidades de integración con 
infraestructuras existentes y las políticas de soporte o licenciamiento. 
En conjunto, las tecnologías de VMware, Dell EMC y Nutanix han redefinido la administración de los 
centros de datos al ofrecer plataformas más simples, escalables y resilientes, alineadas con la evolución 
hacia la nube híbrida y la automatización total de los recursos TI. 
## 🟣 6. Computacion en la nube
El uso del término cloud se ha heredado de la representación de los diagramas de flujo con una gran 
nube blanca que aceptaba conexiones y distribuía información. 
Los términos Cloud, Cloud computing y Cloud storage, se utilizan para describir el concepto de 
almacenar y acceder a la información en Internet, por lo general a través de servicios de terceros, como 
son los servicios de Google (Gmail, Google Drive, etc.). Dropbox, aplicaciones de facturación, CRM, etc. 
Podemos hacer una diferenciación entre estos términos: 
- Cloud:
Es utilizado para indicar el hecho de tener datos, aplicaciones o infraestructura fuera de las 
instalaciones de nuestra empresa (Internet en general). 
- Cloud computing:
Indica los productos y servicios que funcionan en la nube (cloud) y a los cuales se accede a 
través de Internet, como el acceso a ordenadores, y aplicaciones de software a través de una 
conexión de red, y almacenamiento de datos en lugar de almacenarlos en el disco duro de 
nuestro ordenador.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Cloud storage:
Se denomina así al almacenamiento de datos en ordenadores-servidores conectados a Internet, 
los datos quedan alojados en espacios de almacenamiento virtuales en vez de físicos. No 
guardamos nuestros datos en sitios físicos como el disco duro del PC, pendrives, discos \nexternos, etc. 
Muchas empresas ofrecen este servicio de almacenamiento en la nube, que es contratado por 
particulares y empresas para hacer uso de este tipo de almacenamiento. 
En este servicio podemos diferenciar dos partes que deben participar para que el servicio 
funcione correctamente: 
- Front End: el ordenador del cliente y la aplicación necesaria para hacer uso del servicio.
- Back End: los servidores y sistemas de almacenamiento de datos que prestan el servicio en la nube. 
En este modelo de almacenamiento, los datos se guardan en agrupaciones lógicas, que 
necesitan también de una ubicación y entorno físico, que gestiona la empresa proveedora del 
servicio de almacenamiento, que también deberá gestionar que los datos estén disponibles, 
accesibles y protegidos. 
Se habrá frecuentemente de una plataforma cloud, se trata ofrecer en la nube un conjunto de servicios 
diseñados que satisfagan las necesidades de una empresa en cuanto al desarrollo de aplicaciones, 
almacenamiento y computación, ejecutándose todo en el hardware del proveedor. Los desarrolladores 
de software, administradores de la nube etc. de la empresa accederán a través de la red mediante una 
conexión segura. 
 
 
 
 
+ Info 
Cloud Security Alliance es una organización sin fines de lucro con la 
misión de "promover el uso de las mejores prácticas para brindar 
garantía de seguridad dentro de la computación en la nube y 
brindar educación sobre los usos de la computación en la nube 
para ayudar a proteger todas las demás formas de computación". 
 
El Cloud Data Management, sustituye al Data Management tradicional. 
Un Data Manager se encarga de toda la gestión referente a los datos, recoger, verificar, almacenar, 
analizar, proteger y procesar datos. Almacena y guarda volúmenes de datos en servidores, debe 
actualizar su información acerca de los propios sistemas de gestión de datos, y tener en cuenta las leyes 
o marco jurídico que se aplican en la preservación de los datos.

---

Administración de Bases de Datos. Virtualización. Cloud 
El Cloud Data Management ofrece ventajas sobre el tradicional data management, como, por ejemplo: 
- Almacenamiento de grandes volúmenes de datos.
- Facilitar la recuperación de desastres.
- Gestión de la creación de copias de seguridad.
- El archivado de datos a largo plazo.
- Ahorro de costes.
El uso de una plataforma Cloud integrada, ofrece a las empresas la mejor posibilidad de innovación, 
reducción del tiempo de salida de nuevos productos al mercado, sincronización entre unidades de 
negocio y mejor optimización del servicio. 
Una plataforma en la nube ofrece servicios: de computación, almacenamiento, redes, Big Data, 
aprendizaje automático e Internet de las cosas (IoT), y herramientas: de gestión, seguridad y desarrollo \nen la nube. 
 
 
 
 
+ Info 
El uso de Cloud se utiliza también para el desarrollo de aplicaciones 
mediante microservicios, por lo que se requiere de un sistema de 
gestión y orquestación para contenedores Docker. 
 
### 🔵 6.1. Evolucion
El surgimiento de la expresión "Cloud Computing" (computación en la nube) es, mayoritariamente 
atribuido a un seminario impartido por Ramnath Chellappa en 1997. 
Esta expresión, ya se había asociado anteriormente con John Mccarthy, que trabajó en el concepto de 
uso compartido del tiempo, permitiendo que dos o más usuarios utilizaran una computadora de forma 
simultánea. John Mccarthy fue el creador del lenguaje de programación LISP y pionero en la tecnología 
de Inteligencia Artificial.

---

Administración de Bases de Datos. Virtualización. Cloud 
La tecnología de computación en la nube, ha ido evolucionando rápidamente, ofreciéndose a partir de 
2006-2008 de manera comercial, considerándose el almacenamiento de datos como un servicio donde \nel usuario pagaba por lo que consumía (como un servicio de suministro de agua etc.) 
Actualmente es un uso común tanto por particulares como por grandes empresas, muchas de las cuales 
utilizan servicios de terceros o servidores propios. 
 
 
 
 
+ Info 
Hay diversidad de opiniones entre la empresa creadora, muchos 
dicen que el creador fue Amazon, mientras otros opinan que fue 
Google. 
También, la revista Fio publicó un video que indica que fue AT&T el 
inventor del concepto de nube, contando que Andy Hertzfeld y Bill 
Atkinson, (dos de los ingenieros de Apple Macintosh), en 1990 
fundaron la empresa General Magic y crearon una plataforma de 
software denominada Telescript, que fue licenciada en 1994. 
 
 
Veamos brevemente un resumen histórico de fechas importantes en la computación en la nube: 
- 1950: Herb Grosch indica que con tan solo 15 centros de datos de gran tamaño y un alto número de terminales conectados, el mundo entero podría funcionar. Así se establecen los 
orígenes de Internet y la prehistoria del cloud computing. 
- 1961: John McCarthy sugiere públicamente que los avances en la informática y las comunicaciones harán que "algún día la computación se organice como un servicio público" 
(como el agua o la electricidad) Es cuando aparece el concepto de cloud computing. 
- 1966: el libro «The Challenge of the Computer Utility» escrito por Douglas Parkhill, indica casi todas las características modernas de la computación en la nube, así como su potencial como 
servicio público. 
- 1969: JCR Licklider comienza a introducir la idea de «redes intergalácticas de computación»
para que algún día cualquier persona desde cualquier lugar del mundo tenga acceso a este tipo 
de programas. 
- 1969: Se dearrolla Arpanet por el Departamento de Defensa de los Estados Unidos, siendo la primera red de computadoras utilizada como medio de comunicación. (La aparición de Internet \nes clave para que pueda desarrollarse el cloud computing ofreciendo servicios en la red).

---

Administración de Bases de Datos. Virtualización. Cloud 
- 1983: con el cambio de ARPANET del protocolo NCP por TCP/IP, se produce la gran \nestandarización de este protocolo, y se introduce así el concepto de una World Wide Web de redes interconectadas. 
- 1989: La Organización Europea para la Investigación Nuclear (CERN) genera el nodo de
Internet más grande de Europa. Tim Berners-Lee ve la oportunidad de unir Internet y el 
hipertexto (HTTP y HTML), y en diciembre de 1990 estableció la primera comunicación entre 
un cliente y un servidor usando el protocolo HTTPS en diciembre de 1990. 
- 1997: Ramnath Chellappa define Cloud Computing como un nuevo "paradigma en la computación donde los límites de la computación serán determinados por razones económicas \nen lugar de los límites técnicos". 
- 1999: Aparecen los servicios Software as a Service (SaaS), donde el proveedor del servicio pone a disposición de los clientes su propio software. 
- 2000: Amazon moderniza sus centros de datos y el desarrollo de productos para ofrecer servicios cloud a clientes externos. 
- 2002: Blackberry presenta el primer teléfono móvil con voz, datos, mensajes, navegador y aplicaciones. Es el primer Smartphone, con el que los usuarios pueden acceder a Internet. 
- 2002: Nace la empresa masvoz cuyo objetivo es comercializar servicios de red inteligente para \nempresas, y en pocos años se constituye como operador, desarrollando una plataforma de productos comercializados en un modelo SaaS (Software as a Service) y pago por uso (telefonía 
inteligente en la nube). 
- 2006: George Gilder publica un artículo en la revista Wired, titulado "Las fábricas de información. Las granjas de servidores", que hace que quede inmortalizado el modelo de 
arquitectura Cloud. 
- 2007: varias universidades norteamericanas con Google e IBM inician un proyecto de investigación a gran escala sobre Cloud computing. Esto hace que en 2008 aparezca Eucalyptus, 
primera plataforma de código abierto AWS API que permite la creación de sistemas en la nube 
compatibles con los servicios web de Amazon. Se facilita así el despliegue de nubes privadas. 
- 2010: la nube comienza a crecer por la necesidad de las empresas de atender a los consumidores de dispositivos móviles y tablets. Aumenta el uso de aplicaciones Cloud alojadas \nen data centers. 
- 2011: la consultora Gartner indica su previsión de que en 2012 el 80% de las grandes compañías de Fortune 1000 utilizará algún tipo de servicio Cloud y anuncia la previsión de las grandes cifras 
de ingresos que se alcanzaran en el sector. 
- 2014: la revista digital Cloud Computing publica que, según diversos estudios, la seguridad y la privacidad del Cloud Computing continúan siendo los temas que más preocupan a los usuarios. 
También en este año, se inicia el modelo Cloud Federation o federación de Clouds, que es una 
alternativa que consiste en utilizar un software de orquestación con el cual se construyen y se 
gestionan recursos de diferentes nubes públicas, de forma que se puede aprovechar el potencial 
de todas ellas.

---

Administración de Bases de Datos. Virtualización. Cloud 
### 🔵 6.2. Caracteriticas
Las características de la computación en la nube son diferentes en función del autor, vamos a indicar la \nesenciales descritas en la publicación "The NIST Definition of Cloud Computing" (National Institute of 
Standards and Technology): 
- Servicio bajo demanda.
- Acceso amplio y ubicuo a toda la red:
Todas las capacidades están disponibles a través de la red y se accede a ellas a través de 
mecanismos estándares y plataformas heterogéneas como, teléfonos móviles, tabletas, 
computadoras portátiles y estaciones de trabajo. 
- Ubicación transparente y agrupación de recursos:
Los recursos informáticos del proveedor de servicios se agrupan para brindar servicio a 
múltiples consumidores, con diferentes recursos físicos virtualizados que se asignan y reasignan 
dinámicamente de acuerdo con la demanda. 
Existe una sensación de independencia de ubicación en el sentido de que el cliente 
generalmente no tiene control o conocimiento sobre la ubicación exacta de los recursos 
proporcionados, pero puede especificar la ubicación en un nivel más alto de abstracción (por \nejemplo, país, estado o centro de datos). 
Ejemplos de recursos: almacenamiento, procesamiento, memoria y ancho de banda de red. 
- Rápida elasticidad:
los recursos se pueden aprovisionar y liberar rápidamente según la demanda. Para el 
consumidor, las capacidades disponibles para el aprovisionamiento a menudo parecen ser 
ilimitadas y pueden ser apropiadas en cualquier cantidad en cualquier momento. 
- Servicio medido:
Los sistemas en la nube tienen mecanismos de medición en alguno de los niveles de abstracción 
para el tipo de servicio (por ejemplo, almacenamiento, procesamiento, ancho de banda y 
cuentas de usuario activas). 
El uso de los recursos se puede monitorear, controlar e informar, proporcionando transparencia 
tanto para el proveedor como para el consumidor del servicio utilizado. A veces esta posibilidad 
de medición deriva en una cobranza por parte del proveedor hacia el cliente según el uso final. 
En otros casos, el servicio medido sirve para alocar un valor referencial a un centro de costos, 
bajo una medida pre-acordada.

---

Administración de Bases de Datos. Virtualización. Cloud 
Vamos a ver otras características clave, más amplias: 
- Autorreparable:
los proveedores incorporan procesos de respaldo de información, para que sea prácticamente 
imposible que exista una pérdida de información. 
- Agilidad:
El proveedor se encarga de tener capacidad de mejora para ofrecer mejores recursos 
tecnológicos al usuario. 
- Costo:
Normalmente los recursos en la nube tienen menores costos que un aprovisionamiento físico 
local. 
La inversión inicial que sería necesaria para tener un aprovisionamiento local desaparece por la 
naturaleza bajo demanda de la nube. 
- Mantenimiento:
Es más sencillo el mantenimiento de las aplicaciones de computación en la nube, ya que no son 
instaladas en el ordenador de cada usuario. 
- Escalabilidad y elasticidad:
Aprovisionamiento de recursos sobre una base de autoservicio casi en tiempo real, sin que los 
usuarios necesiten cargas de alta duración. 
- La versatilidad infraestructural:
Se tiene la posibilidad de compartir datos en nubes privadas y públicas, al mismo tiempo que se 
puede continuar conservando información en un almacenamiento local. 
- Libertad de ubicación:
El usuario puede hacer uso de los servicios con independencia de su ubicación y del dispositivo 
que puedan utilizar (PC, teléfono móvil). 
- Virtualización:
El uso de la tecnología de virtualización permite compartir servidores y dispositivos de 
almacenamiento, las aplicaciones pueden ser migradas fácilmente de un servidor físico a otro. 
Se otorga al usuario libertad de manejar la plataforma que considere necesaria, en cualquier 
sistema operativo (Windows, Unix o Mac) utilizando aplicaciones informáticas de la nube.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Disponibilidad de la información:
Puesto que la información permanece en Internet, el acceso (autorizado) se puede realizar 
desde cualquier dispositivo conectado en la red evitando que el usuario tenga que almacenar la 
información en dispositivos físicos y tenerlos disponibles en el momento que necesite acceder a 
una información. 
- Rendimiento:
Son los sistemas en la nube los que controlan y optimizan el uso de los recursos de manera 
automática, proporcionando un seguimiento, control y notificación del mismo. 
- Seguridad:
La centralización de los datos puede facilitar la gestión de seguridad, aunque es uno de los 
aspectos más preocupantes en el uso de la nube. 
Los proveedores pueden dedicar recursos a la solución de los problemas de seguridad que 
muchos clientes no podrían abordar económicamente. 
El proveedor de la nube es responsable de la seguridad física, y el usuario es responsable de la 
seguridad a nivel de aplicación. 
El uso de una plataforma en la nube también conlleva unos riesgos, destacando: 
- Externalización de servicios, crea una dependencia del proveedor.
- Almacén de datos fuera de la organización, considerando por tanto la seguridad de los mismos.
#### 🔹 6.2.1. La importancia de la seguridad
El gran desafío de la nube es la seguridad, la protección de la información en el cloud. No solo es 
necesario que se realicen las búsquedas, el intercambio, almacenamiento, transferencia, análisis de 
datos y la visualización de estos de la mejor manera posible, sino que es primordial considerar la 
seguridad de ellos en cada instante. 
Amenazas, vulnerabilidades y responsabilidades deben conocerse para poder asegurar la disponibilidad, 
confidencialidad e integridad de los datos almacenados. La replicación de datos debe hacerse de forma 
que no deje posibilidad para el error, y no pueda afectar a los procesos de análisis. 
Es por tanto necesario implementar tecnologías de última generación, de forma que se pueda predecir 
un ataque antes de que se produzca y poder alertar de un incidente de seguridad con el tiempo 
necesario para solucionarlo antes de que cause más daño. Hay que utilizar patrones de detección de 
fraude, encriptaciones y soluciones inteligentes para combatir a los atacantes. 
El uso de ransomware, afecta la reputación y los recursos de una empresa, ataques de denegación de 
servicio, ataques de phishing… son aspectos que hay que tener en cuenta constantemente.

---

Administración de Bases de Datos. Virtualización. Cloud 
Los sistemas Cloud, deben implementar un sistema DBMS manejador de bases de datos (DataBase 
Management System, o SGBD, por sus siglas en inglés), que es un software muy específico para el 
manejo de base de datos y su interfaz con el usuario y las aplicaciones. 
Hay que tener en cuenta aspectos importantes como: 
- Amenazas:
Problemas de acceso, autenticación, secuestros de cuentas, pérdida de información, negación 
de servicio… 
- Vulnerabilidades:
Para poder asegurar la integridad de los datos hay que conocer las vulnerabilidades de las 
aplicaciones. 
- Responsabilidades:
Los usuarios deben estar informados de hasta dónde llega la competencia del proveedor de 
servicios de la nube, y cuál es la protección de los datos responsabilidad única del usuario o \nempresa. Cada usuario que conecta con los servicios Cloud tiene una responsabilidad individual. 
 
 
 
 
+ Info 
Según Cloud Security Alliance, las tres principales amenazas que 
representaron los cortes de seguridad en la nube son: las Interfaces 
Inseguras y la API (29%), Perdida de Datos (25%) y Fugas de 
Hardware (10%) 
La nube privada se considera más segura ya que incorpora mayores 
niveles de control para el propietario. 
 
### 🔵 6.3. Cloud y el Big Data
La necesidad que conlleva el Big Data, de manejar una inmensa cantidad de datos, ha sido motivo de 
éxito de la computación de la nube, las redes sociales generan diariamente una gran cantidad de datos. 
ya que su uso reduce los costes al igual que posibilita la aparición de aplicaciones disponibles.

---

Administración de Bases de Datos. Virtualización. Cloud 
Esta combinación de la nube y el Big Data ofrecen una solución escalable y adaptable, con ventajas 
como son: 
- Reducción de costes:
El uso de la computación en la nube permite pagar únicamente por lo que se necesita, y se irá 
ampliando a medida que crezca la empresa, esto permite no tener que realizar una gran 
inversión inicial. 
- Agilidad:
El hecho de no tener que instalar y configurar los servidores, proporciona una mayor agilidad de 
funcionamiento a las empresas que utilizan la computación Cloud, obteniendo los servicios que 
necesita sin tener que preocuparse de su gestión. 
Por ejemplo, el uso de una base de datos en la nube puede tener miles de servidores virtuales, su 
contratación proporcionara un servicio inmediato y funcionara sin problemas. 
- Procesamiento de datos:
El procesamiento de datos desestructurados y semiestructurados, especialmente los 
procedentes de las redes sociales es complicado, y el uso de Cloud, permite que se pueda 
realizar de forma más fácil y accesible para todo tipo de empresas, mediante plataformas como 
por ejemplo Big Data Analytics y Apache Hadoop. 
- Viabilidad:
Se facilita la escalabilidad de las empresas al nivel que deseen de potencia de procesamiento y \nespacio de almacenamiento con el uso de la nube, mientras que con las soluciones tradicionales 
se necesitaba la adición de más servidores físicos al clúster para conseguirlo. 
### 🔵 6.4. Tipos de servicios en la nube
Aunque todos los servicios asociados al Cloud, tienen características comunes, no todos son iguales, 
pudiendo distinguirse tres modelos principales estándar, y otras opciones que has ido surgiendo para 
cubrir necesidades de usuarios: 
#### 🔹 6.4.1. SaaS, Software as a Service
Traducido al castellano como "software como servicio", se encuentra en la capa más alta y caracteriza 
una aplicación completa ofrecida como un servicio bajo demanda. 
Se ofrece a los usuarios una aplicación en la nube, que es accesible a través de un navegador web, o 
cualquier aplicación diseñada para ello.

---

Administración de Bases de Datos. Virtualización. Cloud 
Es la empresa que proporciona el servicio la que asume el mantenimiento de la aplicación, y costos de 
soporte. También Pueden implementar funciones nuevas para los clientes con mayor facilidad y 
rapidez. 
El usuario no tiene que hacer una inversión de compra de software, (se suele hacer una suscripción), no 
tiene que preocuparse de actualizaciones ni errores. Únicamente el usuario debe invertir en un sistema 
de red rápido para obtener el mejor rendimiento del servicio, ya que depende de la velocidad de 
conexión a Internet. 
Ejemplos de servicios SaaS son Google Docs y Microsoft Office 365. 
#### 🔹 6.4.2. PaaS, Platform as a Service
Traducido como la plataforma como servicio, es la capa del medio. Es la encapsulación de una 
abstracción de un ambiente de desarrollo y el empaquetamiento de una serie de módulos o 
complementos que proporcionan, normalmente, una funcionalidad horizontal (persistencia de datos, 
autenticación, mensajería, etc.) 
Se brinda a los desarrolladores de software acceso a un hosting escalable listo para desarrollar 
productos. Al usuario se le ofrece la plataforma de desarrollo y las herramientas de programación por lo 
que puede desarrollar aplicaciones propias y controlar la aplicación, pero no controla la infraestructura. 
Permiten gran flexibilidad, pero puede ser restringida por las capacidades disponibles a través del 
proveedor. La empresa puede desplegar sus propias aplicaciones en la infraestructura de nube elegida, y \nes el proveedor quien administra la infraestructura subyacente en el cloud. 
PaaS permite evitar el coste y la complejidad de comprar y administrar licencias de software, la 
infraestructura de aplicaciones subyacente y el middleware o las herramientas de desarrollo y otros 
recursos; garantizando la escalabilidad, ya que el cliente adquiere los recursos que necesita de su 
proveedor según lo dicten sus necesidades. 
Las ofertas de plataformas como servicio pueden servir a todas las fases del ciclo de desarrollo y 
pruebas del software, o pueden estar especializadas en cualquier área en particular, tal como la 
administración del contenido. 
Ejemplos comerciales son: 
- Google App Engine, que sirve aplicaciones de la infraestructura Google.
- Microsoft Azure, una plataforma en la nube que permite el desarrollo y ejecución de aplicaciones codificadas en varios lenguajes y tecnologías como .NET, Java, Go y PHP. 
- La Plataforma G, desarrollada en Perl.

---

Administración de Bases de Datos. Virtualización. Cloud 
 
 
 
+ Info 
Microsof Azure Puedes consultar los servicios que ofrece y su 
funcionamiento en la web oficial. 
https://azure.microsoft.com/es-es/ 
 
 
Tipos de PaaS: 
- Mobile PaaS (mPaaS).
Iniciado en 2012, proporciona capacidades de desarrollo para diseñadores y desarrolladores de 
aplicaciones móviles. 
- PaaS Abierto.
No incluye alojamiento, sino que proporciona software de código abierto que permite a un 
proveedor PaaS ejecutar aplicaciones en un entorno de código abierto. 
- PaaS para el Desarrollo Rápido.
En 2014, Forrester Research (empresa independiente de investigación de mercados que brinda 
asesoramiento sobre el impacto existente y potencial de la tecnología) definió Plataformas \nempresariales públicas para desarrolladores rápidos como una tendencia emergente, 
nombrando a varios proveedores incluyendo a Mendix, Salesforce.com, OutSystems y Acquia 
Acquia. 
#### 🔹 6.4.3. IaaS, Infraestructure as a Service
La infraestructura como servicio, es también llamada en algunos casos hardware as a service, (HaaS). 
Se proporciona una infraestructura como servicio, proporcionando a los usuarios equipos virtuales 
para el alojamiento de cargas de trabajo. 
Se encuentra en la capa inferior y es un medio de entregar almacenamiento básico y capacidades de 
cómputo como servicios estandarizados en la red.

---

Administración de Bases de Datos. Virtualización. Cloud 
El proveedor de servicios en la nube otorga a su cliente la capacidad para aprovecharse del 
procesamiento, almacenamiento, redes y otros recursos de computación fundamentales en base a los 
cuales pueda desplegar el software de su elección, incluyendo aplicaciones y sistemas operativos. 
Se ofrecen servidores, sistemas de almacenamiento, conexiones, enrutadores, y otros sistemas, para 
manejar tipos específicos de cargas de trabajo, desde procesamiento en lotes ("batch") hasta aumento 
de servidor/almacenamiento durante las cargas pico, (por ejemplo, a través de la tecnología de 
virtualización). 
La empresa consumidora no tiene control sobre cuestiones relacionadas con la infraestructura en la 
nube, pero en algunos casos sí se le ceden ciertos derechos de control limitado sobre componentes de 
red seleccionados, como suelen ser los relativos a la seguridad. 
Ejemplos son: 
- Amazon Web Services, cuyos servicios EC2 y S3 ofrecen cómputo y servicios de almacenamiento esenciales (respectivamente). 
- Joyent, cuyo producto principal es una línea de servidores virtualizados, que proveen una infraestructura en demanda altamente escalable para manejar sitios web, incluidas aplicaciones 
web complejas escritas en Python, Ruby, PHP y Java. 
#### 🔹 6.4.4. Nuevas alternativas
Han ido apareciendo nuevas alternativas para cubrir determinadas expectativas de empresas que 
deseaban seguir creciendo en este nuevo entorno. 
##### 6.4.4.1. iPaaS, Integration Platform as a Service iPaaS, traducido como Plataforma de integración como servicio. 
iPaaS es una plataforma con capacidad de integrar aplicaciones, servicios y fuentes de datos ya sea 
dentro de la misma nube o en data centers privados, permitiendo entre ellos todo tipo de conectividad. 
La integración puede realizarse a través de un Enterprise Service Bus, si se necesita orquestar un flujo o 
aplicar ciertas reglas de negocio al integrar servicios y fuentes de información, iPaaS puede ofrecer un 
orquestador de procesos. 
iPaaS permite: 
- Realizar una integración B2B (Business to Business) intercambiando información mediante \nestándares como EDI (significa intercambio electrónico de datos, es un formato electrónico \nestándar para intercambio de documentos, que sustituye documentos en papel, como pedidos de compra o facturas.)

---

Administración de Bases de Datos. Virtualización. Cloud 
- Gran conectividad.
Conectarse con sistemas como ERP's o CRM's, bien en el modelo tradicional o como SaaS. 
Pone en comunicación a través de conectores, bases de datos (SQL, MySQL, ORACLE…), y a 
archivos de texto y protocolos como OData y ODBC. 
- Conectarse y exponer API's a través de un gestor que permita intercambiar información
(servicios de tipo REST o SOAP), transformado e intercambiando con formatos como XML y 
JSON. 
Al ser un servicio en la nube, ofrece las ventajas de conexión desde cualquier dispositivo con conexión a 
Internet, sin tener que realizar instalación o adquisición de servidores, no tener que realizar 
mantenimiento ni actualizaciones, ya que es tarea del proveedor que ofrece el servicio. 
Los costes para la empresa que contrata el servicio de iPaas es menor en comparación con sistemas 
anteriores de integración en local, EAI (Enterprise Application Integration, soluciones de software y 
principios de arquitectura de sistemas para integrar un conjunto de aplicaciones, dentro de cualquier \nempresa). 
##### 6.4.4.2. SECaaS, Security as a Service
SECaaS, traducido como Seguridad como Servicio, es aquel servicio que se ofrece consistente en 
proporcionar las aplicaciones de seguridad tradicionales como un servicio basado en Internet, mediante 
suscripción. 
Estos servicios pueden incluir: 
- Seguridad web: antivirus, antimalware, Firewall, análisis de vulnerabilidades, monitorización, detección de phishing… (antispam y DLP para correo de salida para el correo electrónico), 
protección DDoS, monitorización de infraestructuras… Auditorias de servicios Cloud. 
- Control de accesos y gestión de intrusiones: gestión de identidades, firma electrónica, etc. y detección, prevención y reacción ante eventos inusuales. 
Servicio de cifrado, encriptación de las comunicaciones, gestión de claves… (servicios de red 
privada virtual, VPN). 
- Data Loss Prevention (DLP): soluciones de prevención contra la pérdida de datos.
- Gestión de la Información de Seguridad y Gestión de eventos (SIEM): Servicios basado en recopilación de eventos de seguridad de los diferentes elementos de la infraestructura para 
correlacionarlos, analizarlos y proporcionar informes en tiempo real y alertas ante incidentes de 
seguridad. 
- Recuperación ante desastres (Disaster Recovery).

---

Administración de Bases de Datos. Virtualización. Cloud 
##### 6.4.4.3. FaaS, Function as a Service
FAAS, traducido como Funciones como servicio, se conoce como serverless architecture, \nentendiéndose por serverless que los servidores se utilizan como un elemento más de la infraestructura 
(no significa "sin servidor"). 
Permite la ejecución de aplicaciones a través de contenedores momentáneos, de manera que el 
desarrollador no debe preocuparse de la gestión de la infraestructura sobre la que se ejecuta su función, 
solo se centra en la funcionalidad. 
Con la arquitectura serverless se simplifica el ciclo de desarrollo y se favorece el desarrollo de 
arquitecturas basadas en microservicios, por ello se facilita el ciclo de vida y los despliegues continuos. 
 
 
 
 
+ Info 
CaaS (Container as a Service), Contenedor como Servicio, es una 
forma de vi-tualización basada en contenedores en la que los 
motores de contenedores, la orquestación y los recursos 
informáticos subyacentes se entregan a los usuarios como un 
servicio de un proveedor en la Nube. Está en un intermedio entre el 
IaaS y el PaaS. 
 
##### 6.4.4.4. MBaaS, Mobile Backend as a Service
Traducido "Como un Servicio", y conocido también como BaaS (back-end como servicio), es una forma 
de vincular aplicaciones con servicios de cloud computing, y éstos con APIs. 
Esta clase de servicios generalmente incluyen administración de usuarios, servicios analíticos, 
notificaciones push e integración con servicios de redes sociales, y se prestan a través de la utilización 
de kits personalizados de desarrollo de software (SDK) y las interfaces de programación de aplicaciones 
(API). 
##### 6.4.4.5. IDaaS, Identity as a Service
IDaas, traducido como Identidad como servicio, es un servicio cuya función es verificar la identidad de 
los usuarios, de forma que se compruebe y asegure qué realmente sean quienes dicen ser. 
Su objetivo es maximizar la seguridad y bloquear el acceso de cibercriminales o de usuarios no 
autorizados a la información.

---

Administración de Bases de Datos. Virtualización. Cloud 
Un IDaaS puede ofrecer los siguientes servicios de autentificación de identidad: 
- Autenticación Multi-Factorial.
Para verificar la identidad de un usuario, se utilizan múltiples factores de autentificación. 
- Autenticación Única o Single sign-on (SSO).
Traducido como "autenticación única" o "validación única", se le denomina "Inicio de Sesión 
Único" o "Inicio de Sesión Unificado" y se trata de un procedimiento de autenticación que 
habilita a un usuario determinado para acceder a varios sistemas con una sola instancia de 
identificación. 
El objetivo es permitir autenticar a los usuarios en diversas aplicaciones, sin necesidad de volver 
a autenticar. 
Los usuarios acceden una sola vez a un único portal para poder usar todas las aplicaciones del 
SaaS, lo que proporciona una centralización para que se gestione las aplicaciones a las que tiene 
acceso cada usuario. 
Hay cinco tipos principales de SSO, también se les llama reduced sign on systems ("sistemas de 
autenticación reducida"). 
- Enterprise SSO (E-SSO).
Llamado también Legacy SSO, funciona para una autenticación primaria, interceptando los 
requisitos de login presentados por las aplicaciones secundarias para completar los mismos 
con el usuario y contraseña. 
Permite interactuar con sistemas que pueden deshabilitar la presentación de la pantalla de 
login. 
- Web SSO (Web-SSO).
También llamado gestión de acceso web (web access management, Web-AM o WAM). 
Trabaja solamente con aplicaciones y recursos accedidos vía web, y su objetivo es permitir 
autenticar a los usuarios en diversas aplicaciones, sin necesidad de volver a autenticar. 
Los accesos son interceptados con la ayuda de un servidor proxy o de un componente 
instalado en el servidor web o en la aplicación web destino. 
Los usuarios no autenticados que tratan de acceder son redirigidos a un servidor o servicio 
web de autenticación y regresan solamente después de haber logrado un acceso exitoso o 
con un TOKEN de autenticación para la aplicación destino. Se utilizan cookies, parámetros 
por GET (más inseguro) o POST para reconocer aquellos usuarios que acceden y su estado 
de autenticación.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Kerberos.
Es un método popular de externalizar la autenticación de los usuarios. Los usuarios se 
registran en el servidor Kerberos y reciben un tique, luego las aplicaciones cliente lo 
presentan para obtener acceso. 
- Identidad federada.
Es una nueva manera de enfrentar el problema de la autenticación, también para 
aplicaciones Web. Utiliza protocolos basados en estándares para habilitar que las 
aplicaciones puedan identificar los clientes sin necesidad de autenticación redundante. 
- OpenID.
Es un protocolo de enfoque descentralizado y distribuido para la autenticación de usuarios 
(que podrán autenticarse en múltiples sitios), en el que la identidad se especifica a través de 
una URL y puede ser facilitada y gestionada por distintos proveedores de identidad (IdP). 
- Gestión de Identidades o Identity Management.
Consta de un proveedor de identidades que almacena y gestiona las identidades de múltiples 
usuarios, y que se encarga de comprobar la identidad de un usuario por nombre de usuario y 
contraseña y otros factores. 
También puede simplemente proveer una lista de identidades que otro proveedor de servicios 
verifica. 
- Seguridad de Acceso o Access Security.
Se trata de una herramienta que gestiona el acceso a aplicaciones o APIs, basandose en políticas 
más estrictas, con el objetivo de garantizar la seguridad más que cualquier Single sign-on. 
### 🔵 6.5. Modelos de implementación
Un modelo de implementación es un tipo específico de entorno en la nube, basándose principalmente \nen: la propiedad, el tamaño y el acceso. 
Vamos a ver los modelos de implementación más comunes: 
#### 🔹 6.5.1. Nube Pública
Se trata de una infraestructura en base a una red abierta, está disponible para el público en general, se 
ofrece el servicio de computación en la nueva a todos los clientes externos que demandan de esta 
tecnología en internet.

---

Administración de Bases de Datos. Virtualización. Cloud 
Las aplicaciones, el almacenamiento y otros recursos están disponibles al público a través del proveedor 
de servicios, que es propietario de toda la infraestructura en sus centros de datos. Se ofrece el acceso a 
los servicios de manera remota. 
Características: 
- Es mantenida y gestionada por terceras personas no vinculadas con la organización.
- Tanto los datos como los procesos de varios clientes se mezclan en los servidores, sistemas de almacenamiento y otras infraestructuras de la nube. 
- Los usuarios finales de la nube desconocen qué trabajos de otros clientes pueden estar corriendo en el mismo servidor, red, sistemas de almacenamiento, etc. 
- Paas fue originalmente pensado para las nubes públicas, antes de expandirse a las privadas e híbridas. 
Dentro de estas nubes englobamos las nube privada virtual, que son como nubes de dominio público 
pero que mejoran la seguridad de los datos, que se encriptan a través de la implantación de una VPN 
(red privada virtual). 
Algunos de los principales proveedores de nubes públicas son Alibaba Cloud, Amazon Web Services 
(AWS), Google Cloud, IBM Cloud y Microsoft Azure. 
#### 🔹 6.5.2. Nube Privada
Son entornos de nube que se destinan exclusivamente a un usuario o grupo final. 
Permite centralizar el acceso a los recursos de tecnológicos de la organización, utilizando una 
tecnología de Cloud Computing propia, por tanto, el cliente y el proveedor de servicios Cloud coinciden, 
aunque la gestión de este entorno puede llevarla a cabo la misma compañía o subcontratarlo a terceros. 
Aunque los recursos residan físicamente en las instalaciones de la organización, se consideran basados \nen el Cloud, porque son accesibles de forma remota por los usuarios. 
Se diferencian de dos formas según su gestión: 
- Nubes privadas gestionadas:
Los clientes crean y usan una nube privada que implementa, configura y gestiona un proveedor \nexterno. 
Facilita que las empresas sin personal de TI, o con poca formación, o tengan que realizar la 
gestión.

---

Administración de Bases de Datos. Virtualización. Cloud 
- Nubes exclusivas:
Una nube dentro de otra nube. 
Se puede tener una nube exclusiva en una nube pública o en una nube privada, para un 
departamento concreto, por ejemplo, un departamento de contabilidad puede tener su propia 
nube exclusiva dentro de la nube privada de la empresa. (Ejemplo: Red Hat OpenShift 
Dedicated) 
#### 🔹 6.5.3. Nube Híbrida
Consiste en una mezcla de despliegues públicos y privados, esta mezcla variara en función de las 
necesidades del usuario. 
#### 🔹 6.5.4. Otras
Podemos diferenciar otras clasificaciones de implementación: 
- Nube de comunidad:
Es prácticamente como la nube pública, pero en este caso, el acceso queda limitado a una 
comunidad concreta, o bien a algunos de sus miembros, que tendrán que determinar las reglas. 
- Nube privada virtual:
Se trata de un entorno de nube autónomo, alojado y administrado por un proveedor de nube 
pública, quien lo pone a disposición de un consumidor de nube por un determinado coste y 
cumplimiento de unas condiciones de uso establecidas. 
- Intercloud:
Se denomina muchas veces como una nube de nubes, está orientada a fomentar la 
interoperabilidad directa entre proveedores públicos de servicios en la nube. 
- Multicloud:
Se denomina así al uso de múltiples servicios de Cloud Computing en una única arquitectura 
heterogénea, abarcando una amplia variedad de servicios, teniendo así una gran flexibilidad, ya 
que se amplían las posibilidades de elección reduciéndose la dependencia de proveedores 
únicos. 
Está compuesto por al menos dos servicios de nube, que proporcionan por lo menos dos 
proveedores de nube pública o privada. 
Todas las nubes híbridas son multiclouds.

---

Administración de Bases de Datos. Virtualización. Cloud 
No todas las multiclouds son híbridas, se vuelven híbridas cuando se conectan varias nubes con 
algún tipo de integración u organización. 
Un entorno multicloud se crea mejorar el control de los datos confidenciales o como un espacio 
de almacenamiento redundante para una mejor recuperación ante desastres. Pero también 
surge en ocasiones de forma no intencionada, como resultado de la "shadow IT" o o "TI 
Invisible" (cualquier tipo de estructura, los dispositivos, softwares y servicios, que están fuera 
del control del departamento de TI y no cuentan con una aprobación explícita del área de 
Tecnología de la Información de la empresa u organización). 
## 🟣 7. Bibliografía
- Fundamentos de bases de datos 4ª edición. Silberschatz, Korth, Sudarshan. Editorial McGraw-Hill.
- http://www.angelfire.com/nf/tecvirtual/cursos/admonbd/DBA1.htm.
- https://jorgesanchez.net/manuales/abd/bases-sgbd.html.
- http://www.monografias.com/trabajos19/administracion-base-datos/administracion-base-
datos.shtml. 
- http://tics-johana.blogspot.com/2010/12/funciones-de-un-dba.html.
- https://interpolados.wordpress.com/2017/11/24/roles-y-responsabilidades-del-dba-de-
oracle/. 
- http://www.angelfire.com/nf/tecvirtual/cursos/admonbd/DBA1.htm.
- https://slidex.tips/download/instalacion-y-administracion-de-servicios-de-correo-electronico.
- http://www.formacion.andaluciaesdigital.es/c/document_library/get_file?uuid=3381a004-
24d7-4d99-82bf-e47949cc80d7&groupId=20195. 
- https://es.wikipedia.org/wiki/12_reglas_de_Codd.
- https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo.
- https://tools.ietf.org/html/rfc2142.
- https://ayuda.guebs.com/limpiar-cache-dns-red/.
- https://docs.microsoft.com/en-us/exchange/high-availability/database-availability-
groups/database-availability-groups?view=exchserver-2019. 
- https://www.dsi.uclm.es/personal/miguelfgraciani/mikicurri/Docencia/LenguajesInternet091
0/web_LI/Teoria/.

---

Administración de Bases de Datos. Virtualización. Cloud 
- https://www.muycomputerpro.com/2016/03/17/virtualizacion-almacenamiento-fujitsu.
- https://es.wikipedia.org/wiki/Virtualización#Características_principales.
- https://www.alegsa.com.ar/Dic/virtualizacion_de_almacenamiento.php.
- https://www.trizclass.com/tutoriales/virtualizacion/tecnica3.html.
- https://es.wikipedia.org/wiki/Anillo_(seguridad_informática).
- https://www.monografias.com/trabajos14/respaldoinfo/respaldoinfo.shtml.
- https://www.veeam.com/blog/es-lat/why-virtual-machine-backups-different.html.
- https://www.datos101.com/blog/copia-de-seguridad-maquinas-virtuales-y-como-\nexternalizarlas/.
- https://www.serban.es/virtualizacion-del-puesto-de-trabajo-diferencias-vdi-sdi/.
- https://www.nakivo.com/blog/es/aprovisionamiento-thick-y-thin-cual-es-la-diferencia/
- https://www.powerdata.es/cloud
- https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube#Software_como_servicio_(S aaS) 
- https://skyone.solutions/es/hub/conocer-la-computacion-en-la-nube/
- https://www.masvoz.es/blog/comunicaciones-en-la-nube/blogla-evolucion-del-cloud-
computing/ 
- https://es.wikipedia.org/wiki/Seguridad_como_servicio
- https://www.redhat.com/es/topics/cloud-computing/public-cloud-vs-private-cloud-and-
hybrid-cloud 
- https://www.arsys.es/
- https://es.wikipedia.org/wiki/Single_Sign-On

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|Ficha Resumen del Tema 02]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque4-tema02|Nota Fuente Oficial del Tema 02]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema02-windows-server|Test Tema 02]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema01|⬅️ Tema Completo 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema03|Tema Completo 03 ➡️]]
