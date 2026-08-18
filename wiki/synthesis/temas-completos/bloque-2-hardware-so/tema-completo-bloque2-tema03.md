---
title: "Tema Completo Extendido 03 (Bloque 2): Estructuras de Datos, Árboles y Algoritmos (AVL, B+, Big-O)"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-2
  - tema-03
  - oposiciones-tai
estado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md]]"
  - "[[wiki/sources/bloque2-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema02|⬅️ Tema Completo 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema04|Tema Completo 04 ➡️]]

# 🔴 Tema Completo Extendido 03 (Bloque 2): Estructuras de Datos, Árboles y Algoritmos (AVL, B+, Big-O)

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 03 correspondiente al Bloque 2 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro

# Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Complejidad Algorítmica

<!-- Page 1 -->

 
 
Tipos de Datos y Estructuras. 
Tipos, Organización y Formato 
de Ficheros. Algoritmos  
DV.Texto HTML (01).Esp.dot     |     DOCUMENTO3  

<!-- Page 2 -->

ÍNDICE  
1. Datos. Tipos de datos  
5 
1.1. Tipos básicos de datos  
7 
1.2. Estructuras de datos  
8 
1.2.1. Array 
8 
1.2.2. Puntero 
10 
1.3. Tipos abstractos de datos (tad)
 
11 
1.3.1. Estructuras Tipos de datos abstractos  
13 
1.3.1.1. Listas  
14 
1.3.1.2. Árboles 
22 
1.3.1.3. Grafos 
28 
2. Sistemas de almacenamiento  
29 
3. Ficheros 
30 
3.1. Nombre y extensión de un fichero  
32 
3.2. Atributos de los ficheros  
34 
3.3. Tipos de ficheros  
36 
3.4. Principales formatos de ficheros  
39 
3.4.1. Documentos  
40 
3.4.2. Hojas de Cálculo  
42 
3.4.3. Compresores  
42 
3.4.4. Imágenes 
43 
3.4.5. Audio 
46 
3.4.6. Video 
47 
3.5. Operaciones sobre ficheros  
48 
3.6. De los sectores a los bloques  
50 
3.6.1. Dispositivos de almacenamiento y sectores físicos  
51 
3.6.2. Direccionamiento lineal de sectores (LBA)  
51 
3.6.3. Bloques lógicos del sistema operativo  
52 
3.6.4. Clusters y fragmentación interna  
52 
3.7. Implementación interna del sistema de ficheros  
53 

<!-- Page 3 -->

 
 
3.7.1. Estrategias de asignación de bloques  
54 
3.7.1.1. Asignación contigua  
54 
3.7.1.2. Asignación enlazada (ejemplo: tablas FAT)
 
54 
3.7.1.3. Asignación indexada (ejemplo: i -nodos)  
55 
3.7.2. Gestión del espacio libre  
55 
3.7.2.1. Mapas de bits 
55 
3.7.2.2. Listas de bloques libres  
55 
3.7.3. Metadatos y consistencia del sistema de ficheros  
56 
3.8. Abstracción del fichero y métodos de acceso (so / aplicación)
 
56 
3.8.1. El fichero como secuencia lógica de bytes  
57 
3.8.2. Acceso secuencial  
57 
3.8.3. Acceso directo por desplazamiento (offset)  
57 
3.8.4. Traducción del offset lógico a bloques físicos  
57 
3.9. Organización lógica del contenido (nivel aplicación)
 
58 
3.9.1. Ficheros secuenciales y secuenciales ordenados  
59 
3.9.2. Ficheros de registros de longitud fija  
60 
3.9.3. Índices simples gestionados por la aplicación  
61 
3.10. Organización de ficheros en sgbd  
61 
3.10.1. Ficheros de registros y páginas de datos  
62 
3.10.2. Organización primaria  
62 
3.10.2.1.  Montículo (heap)  
63 
3.10.2.2.  Secuencial ordenada  
63 
3.10.2.3.  Dispersión (hashing)  
64 
3.10.3. Organización secundaria  
66 
3.10.3.1.  Índices como acceso alternativo  
66 
3.10.3.2.  Estructura General de un Índice  
66 
3.10.3.3.  Búsqueda en índices ordenados: busqueda binaria  
67 
3.10.3.4.  Densidad del índice  
67 
3.10.3.5.  Relación entre índice y organización primaria  
67 
3.10.3.6.  Gestión de índices en los SGBD  
68 
3.10.3.7.  Índices multinivel y árboles B / B+  
69 

<!-- Page 4 -->

 
 
3.11. Directorios  
69 
4. Códecs  
71 
4.1. Códec de audio  
72 
4.2. Códec de vídeo  
74 
5. Algoritmos  
76 
5.1. Bondad, recursividad y optimización  
77 
5.2. Complejidad de los algoritmos  
78 
5.2.1. 
78 
5.2.2. Casos de uso  
79 
5.2.3. Órdenes de complejidad  
80 
5.3. Rendimiento y medición de los algoritmos  
81 
5.4. Clasificación: ordenamiento y búsqueda  
82 
5.4.1. De ordenamiento 
82 
5.4.1.1. Según la estabilidad del algoritmo  
84 
5.4.1.2. Según el método de resolver el problema  
84 
5.4.1.2.1.  Iterativos  
85 
5.4.1.2.2.  Recursivos  
88 
5.4.1.3. Estructuras cíclicas  
91 
5.4.2. Algoritmos de Búsqueda  
92 
5.4.2.1. Secuencial 
92 
5.4.2.2. Búsqueda Binaria o Dicotómica  
92 
5.4.2.3. Búsqueda basada en tablas Hash  
93 
5.4.3. Algoritmos Voraces  
94 
5.5. Representación de algoritmos  
95 
5.5.1. Lenguaje natural  
95 
5.5.2. Diagramas de Nassi -Shneideman 
96 
5.5.3. Pseudocódigo 
96 
5.5.4. Diagrama de flujo  
97 
6. Bibliografía  
99 
 

<!-- Page 5 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
5 
1. Datos. Tipos de datos  
 
Fuente: Pixnio 
Es un conjunto de símbolos (alfanuméricos o de cualquier otra índole) que representan un hecho o un 
valor, pero que carece de significado o valor por sí mismo. Están formateados de forma adecuada para 
poder ser procesados.  
En este momento, lo importante es que tengas en cuenta que un dato representa un hecho o un valor. 
(si/no, verdadero/falso, texto, número…).
 
Un dato es una representación simbólica (numérica, alfabética, algorítmica, espacial, etc.) de un 
atributo de una entidad. Son la información que recibe el ordenador por diferentes medios, y que es 
manipulada según las necesidades del usuario, por los algoritmos creados por el programador, en un 
determinado lenguaje de programación.  
Se agrupan, y estructuran convenientemente, formando estructuras de datos, a través de los Sistemas 
de Gestión de Bases de Datos, que gestionan también su uso, acceso, etc.
 
En programación, el tipo de dato, define los valores que puede tomar una determinada variable y las 
operaciones que podemos realizar sobre la misma. Los tipos de datos pueden variar de un lenguaje a 
otro. 
Los tipos de datos definidos dependerán del lenguaje de programación que estemos utilizando.
 
 
 
 

<!-- Page 6 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
6 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. ACCEDE 
DIRECTAMENTE DESDE AQUÍ 
 
 
Los tipos de datos constituyen un mecanismo de abstracción, ya que permiten al programador trabajar 
con enteros, cadenas de texto, caracteres o booleanos sin preocuparse por cómo se representan 
internamente en la máquina. Cada tipo de dato determina qué valores puede almacenar una variable y 
qué operaciones son válidas sobre esos valores.  
Gracias a este sistema, se evita que el usuario intente realizar operaciones incoherentes (por ejemplo, 
sumar un número y un texto) y se garantiza que el programa sea independiente de la máquina concreta 
en la que se ejecute. 
Abstracción  
Es una operación mental, en la que aislamos conceptualmente una parte del problema global, 
estudiándolo sin tener en consideración el resto de las características del problema global.
 
 
Fuente: PixaBay 
Ejemplo: Nos centramos en una sola pieza del puzle, no nos importa el resto.
 

<!-- Page 7 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
7 
En informática, este concepto es muy usado como una manera de ocultar los detalles de 
implementación de un objeto, de forma que lo utilizamos, porque sabemos qué puede hacer, pero no 
necesitamos saber cómo lo hace. (Convertimos un dato mediante la abstracción en un objeto).  
En la abstracción realizamos dos procesos:  
• Determinar los aspectos relevantes del problema en el nivel de abstracción que estamos 
estudiando. 
• Ignorar los aspectos irrelevantes.  
Muy importante, tener en cuenta que, un aspecto irrelevante en un determinado nivel de abstracción 
puede resultar relevante en otro nivel.  
Los programadores, utilizan la abstracción para hacer los algoritmos más sencillos, a través de top
-
down (de arriba abajo, o lo que es lo mismo, de lo más general a lo más específico).
 
1.1. Tipos básicos de datos  
Los principales tipos básicos de datos son:  
• Enteros. 
Representan números enteros (normalmente con signo). Ejemplo: 2, 
-2. 
No se pueden representar todos los valores. El rango que se puede representar depende del 
número de bits que se utilicen. Los números que se pueden representar corresponden al rango 
[2 n&minus;1&minus;1,2 n&minus;1], donde n es el número de bits utilizados.  
• Reales. 
Denominado float en muchos lenguajes (dado que se representa en coma flotante. Permite 
representar números enteros reales (con decimales).  
No se pueden representar todos los números reales entre dos enteros (ya que son infinitos), por 
lo que se debe realizar un redondeo (por ejemplo, el número 3.697863785938327 se 
almacenaría como 3.7 (el redondeo depende del número de decimales que podamos 
almacenar).  
En muchos lenguajes se utiliza el tipo double, que permite almacenar un mayor rango que el 
float (normalmente usa el doble de bits). También se pueden utilizar tipos para rangos aún 
mayores. 
• Lógicos.  
Representan valores lógicos o booleanos, es decir, pueden tomar dos posibles valores (0 y 1, 
verdadero y falso, etcétera).  

<!-- Page 8 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
8 
Las operaciones que se realizan sobre estas variables son los operadores lógicos básicos (AND, 
OR y NOT). Algunos lenguajes incluyen también otros operadores como NAND, NOR y XOR).
 
• Carácter.  
Representa elementos individuales del conjunto de caracteres utilizado (por ejemplo, código 
ASCII (acrónimo inglés de American Standard Code for Information Interchange: Código 
Estándar Estadounidense para el Intercambio de Información).
 
No suele haber operaciones sobre el mismo (salvo la asignación de valor y, en ocasiones, el 
cambio a otro tipo, por ejemplo, entero).  
En la mayoría de los lenguajes se utiliza una estructura denominada string o cadena como tipo 
básico. Contiene un número a determinar de caracteres y sobre ella se pueden hacer distintas 
operaciones (buscar un carácter, dar su posición, transponer la cadena, etcétera).
 
1.2. Estructuras de datos  
Cuando hablamos de este tipo de estructuras podemos distinguir entre otros:
 
• Array. 
• Puntero. 
1.2.1. Array 
Un array es una estructura de datos que permite almacenar una colección ordenada de elementos bajo 
un mismo nombre.  
En algunos lenguajes como C, C++, C# esta colección de elementos será homogénea (del mismo tipo) y 
estática (con número fijo de elementos), y en otros como PHP, Python o Javascript esta colección 
podrá ser heterogénea y dinámica.  
Cada elemento ocupa, en el array, una posición determinada que se conoce como índice y será 
necesario para acceder a un elemento en concreto. Dependiendo del lenguaje de programación el 
índice puede arrancar en el 0 o en el 1.  
Un array tiene una o más dimensiones y tendrá un índice por cada dimensión. Lo más común es utilizar 
una o dos dimensiones: Vector o Matriz.  
 
 
 

<!-- Page 9 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
9 
 
Info 
En el examen de la convocatoria de septiembre de 2023, dieron 
por correcta esta respuesta:  
a) Un array o vector es un tipo de dato estructurado que permite 
almacenar un conjunto de datos homogéneo donde cada elemento se 
almacena de forma consecutiva en memoria.  
 
 
Vector 
Un array de una sola dimensión se denomina array lineal o vector.  
Es un conjunto de elementos referenciados por números consecutivos (para n elementos se utilizan los 
números de 1 a n o bien de 0 a n -1).  
Son estructuras de datos contiguas.  
A los elementos de un array, se le asigna memoria de forma contigua.  
Un ejemplo de array unidimensional sería:  
 
Para referenciar a un elemento utilizamos el índice. Así, si el array se llamase "arrayEjemplo", el 
elemento de índice 3 (que es en realidad el elemento cuarto, ya que empieza desde cero) se referencia 
como arrayEjemplo[3] y su valor es 12.  
Matriz 
Un array de dos dimensiones se conoce por el nombre de matriz. Es un vector (array multidimensional) 
que contiene como decíamos vectores (que en algunos lenguajes serán del mismo tipo y tamaño).
 
En matrices multidimensionales, los elementos dentro de cada fila suelen estar en posiciones de 
memoria contiguas, pero las filas en sí pueden no estarlo, lo que puede afectar el rendimiento en el 
acceso a elementos de diferentes filas.  
Veamos un ejemplo.  

<!-- Page 10 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
10 
 
Supongamos que tenemos esta matriz con nombre mEjemplo cuyos índices comienza en 0.
 
Para acceder al literal "baile" tendremos que referenciar: mEjempo[2][1].
 
Referenciaremos pues la tercera fila de la matriz (si la primera posición es 0 será la 2) y el segundo 
elemento (si los índices comienzan en 0, será el número 1).
 
Recordemos que esto no es uniforme, en algunos lenguajes, en vectores y matrices los datos han de ser 
homogéneos (siempre del mismo tipo) y la primera posición de los índices puede ser la 1.
 
1.2.2. Puntero 
Es una variable que almacena la dirección de memoria de otra variable. Esta estructura nos será muy útil 
para implementar otras estructuras más complejas.  
Normalmente, con un puntero, podemos obtener la dirección de memoria a la que apunta o el 
contenido que hay en dicha dirección.  
Ejemplo en el lenguaje C  
Cuando hacemos por ejemplo,  
int x = 1; 
El compilador asigna una dirección de memoria a mi variable y almacena en la misma el valor 1.
 
El operador & permite obtener la dirección de memoria de una variable. Continuando con nuestro 
ejemplo, si queremos conocer la dirección de memoria de x, lo indicaremos como &x, lo que devolverá 
una dirección de memoria virtual expresada en notación hexadecimal tal que 0x7ffd7482fd20.
 
En Linux, macOS y Windows de 64 bits, las direcciones que comienzan por 0x7ff… suelen corresponder 
a direcciones ubicadas en la pila (stack), que es donde habitualmente se almacenan variables locales 
como int x.  
El operador * tiene una doble función, en una declaración le indica al compilador que el tipo de dato 
solicitado es un puntero, si se utiliza más adelante en nuestro código el compilador devolverá el 
contenido de la casilla de memoria contenida en la dirección a la que apunta ese puntero.
 

<!-- Page 11 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
11 
Así pues si lo que me interesa es almacenar una dirección de memoria, el tipo de dato que he de emplear 
es un puntero, que se especifica en C de esta manera:  
int *puntero = &amp;x; 
 
 
 
 
 
+Recuerda  
Un puntero es una variable de tipo puntero que almacena la 
dirección de memoria de un dato de un tipo determinado.  
 
 
Si quiero obtener el valor contenido en esa dirección de memoria (siempre fuera de la declaración de 
variables), haré, siguiendo con nuestro ejemplo en lenguaje C, *puntero, lo que me devolverá el valor 1.
 
1.3. Tipos abstractos de datos (tad)
 
Un tipo abstracto de datos es un modelo matemático compuesto por una colección de operaciones 
definidas sobre un conjunto de datos para el modelo.  
Se le denomina también TDA, siglas de Abstract Data Type.
 
Es un conjunto de valores y de operaciones definidos mediante una especificación independiente de 
cualquier representación.  
TAD = valores + operaciones 
Un TAD es una formalización de dato (definición de un dato), que crea el programador considerando lo 
que resulta más adecuado para el objetivo que debe cumplir su programa, utilizando la abstracción.
 
Se definirá con las siguientes características:  
• Tipo de dato (enteros, reales, lógicos), valores que puede tomar, y conjunto de operaciones que 
se pueden realizar.  
• Cumplir con los principios de abstracción y ocultación de la información. Se pueden manejar sin 
conocer su estructura interna.  

<!-- Page 12 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
12 
Por tanto, podemos decir que consta de tres partes:  
• Dominio del tipo. Elementos que pueden constituirlo. Se representan mediante estructuras de 
datos. 
• Operaciones. Conjunto de operaciones que pueden realizarse sobre estos elementos. Se 
representan mediante procedimientos.  
• Semántica. Definiciones que describen qué hace cada operación. No nos interesa cómo se hace.
 
Resumiendo: 
Es la formalización del concepto de dato que consideramos adecuado para resolver el problema.
 
 
 
 
 
Nota 
El concepto TDA, fue propuesto por primera vez por John Guttag y 
otros compañeros, hacia 1974.  
Pero fue en 1975 cuando Barbara Liskov, lo propuso por primera 
vez para el lenguaje de programación CLU, creado por ella y sus 
estudiantes, incluyendo en el código tipos de datos abstractos. Fue 
un gran paso para la programación orientada a objetos.  
 
 

<!-- Page 13 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
13 
1.3.1. Estructuras Tipos de datos abstractos
 
 
Fuente: Pixabay 
Las estructuras de datos están definidas por las relaciones entre los datos y la forma en que pueden 
agruparse. 
Una estructura de datos es un tipo de datos construido a partir de otros tipos de datos. Está compuesto 
por una serie de componentes (datos de uno de los tipos básicos u otra estructura de datos) y alguna 
relación existente entre ellos (por ejemplo, el orden puede ser una relación entre ellos).
 
Es un paso más en la abstracción. Una estructura de datos es una agrupación de datos (pueden ser de 
distinto tipo), relacionados entre sí, y las operaciones definidas sobre dicha agrupación.
 
 
 
 
 
+ Info 
¿Ves cómo vamos usando la abstracción?  
Empezamos por lo más específico (dato) hacia lo más general. Al 
hablar de cada nivel ignorábamos las características del nivel 
superior. 
 
 
Algunas de las operaciones básicas sobre estructuras de datos son: acceder a un elemento (leer), 
buscar, insertar o borrar.  
Aquí no nos es relevante las operaciones individuales de cada componente, sino las operaciones sobre la 
estructura de datos global.  

<!-- Page 14 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
14 
Según el tipo de datos de los componentes, una estructura puede ser de dos tipos:
 
• Homogénea. Todos sus componentes son del mismo tipo.  
• Heterogénea.  Sus componentes no son del mismo tipo.  
Según la forma en que se le asigna memoria, una estructura puede ser de dos tipos:
 
• Estática.  Cuando se sabe a priori el número de elementos que va a tener. Se asigna la memoria 
que va a necesitar en la declaración.  
La expresión declaración, es una reminiscencia de los lenguajes de programación Cobol y 
Fortran, en las que se "declaraban" las variables, sus tipos y tamaños. (En cobol había un 
apartado que era "Declarative" en donde se definían todas las variables).  
• Dinámicas.  No se sabe a priori el número de elementos que va a tener (puede aumentar o 
disminuir en tiempo de ejecución del programa).  
Se reserva la memoria mínima para un elemento en la declaración y se le va asignando 
dinámicamente más memoria según se van creando más elementos (por ejemplo, en las listas y 
grafos).  
A continuación, vamos a ver algunas de las estructuras de datos más utilizadas.
 
1.3.1.1. Listas  
Una lista es un conjunto ordenado de elementos que nos permite introducir un elemento en cualquier 
punto de la lista o eliminar cualquiera de ellos sin desperdiciar memoria (estructura dinámica).
 
Es necesario tener un puntero inicio que apunta al primer elemento de la lista.  
Cada elemento de la lista está formado, al menos, por:  
• Variable de un determinado tipo de dato o estructura que contiene la información.
 
• Puntero que señala al siguiente elemento de la lista.  
Algunas de las características  de las listas son: 
• Permiten realizar inserciones en cualquier punto de la lista.  
• Permite eliminar cualquier elemento.  
• El acceso a los elementos es secuencial (tenemos que ir pasando por cada uno de ellos, ya que 
cada elemento nos direcciona al siguiente).  

<!-- Page 15 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
15 
• Todos los elementos tienen un antecesor y un sucesor, excepto el primero (que solo tiene 
sucesor) y el último (que solo tiene antecesor).
 
• La asignación de memoria se hace en tiempo de ejecución.  
• Los elementos no se almacenan contiguamente en la memoria.  
• El enlace entre elementos se hace mediante punteros.  
A continuación, veremos los principales tipos de listas:  
• Listas enlazadas simples.  
• Listas enlazadas dobles.  
• Listas circulares.  
• Pilas. 
• Colas. 
Listas enlazadas simples  
Es la forma de lista más sencilla en donde cada nodo contiene un valor (tipo de dato o estructura de 
datos) y un puntero denominado "siguiente" que apunta al nodo siguiente.
 
Además, podremos tender dos punteros: 
• Inicio (Head):  El puntero  
•  apunta al primer elemento y sirve como entrada para recorrer la lista de forma secuencial. Esto 
mejora la eficiencia de las operaciones de inserción y eliminación del primer elemento. El 
puntero  
•  suele ser común en la mayoría de las implementaciones, aunque puede haber excepciones en 
listas circulares dobles debido a su naturaleza circular.  
• Fin/Cola (Tail):  El puntero  
•  es menos común, ya que la mayoría de las operaciones en las listas se realizan desde el inicio. 
Sin embargo, puede ser útil en determinadas situaciones dependiendo de la implementación que 
se necesite. 
Es importante tener en cuenta que la presencia y la configuración de estos punteros pueden variar 
según el lenguaje de programación y su manejo de estructuras de datos, como las listas.
 
Si no hay elementos, "inicio" y "fin", apuntan a NULL (valor nulo). De la misma forma, el puntero 
"siguiente". 

<!-- Page 16 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
16 
Listas enlazadas dobles  
Son iguales a las listas enlazadas simples, pero añaden en cada elemento un nuevo puntero
 denominado 
"anterior" que apunta al antecesor.  
El puntero anterior del primer elemento apunta a "NULL" (dado que no tiene antecesor).
 
Las listas enlazadas dobles pueden ser recorridas en ambos sentidos. Podemos empezar en "inicio" y 
seguir los punteros "siguiente" de cada elemento o bien empezar en "fin" (si está implementado)
 y 
seguir los punteros "anterior" de cada elemento.  
Listas circulares  
La lista circular es una lista enlazada simple o doble con las siguientes particularidades:
 
• No siempre tiene puntero "fin". 
• El puntero "siguiente" del último elemento apunta al primer elemento.  
 
Estas imágenes son orientativas, como hemos comentado las estructuras de datos y su implementación 
puede variar sustancialmente de un lenguaje de programación a otro.  
Pilas 
También denominada lista LIFO  (Last In First Out) ya que almacena datos en este orden, es decir, el 
último elemento que se incorpora a la pila es el primero que sale.  
Para entenderlo, imagina una pila de libros. Si quieres poner otro libro en la pila lo sitúas arriba del todo. 
Cuando quieres coger un libro tienes que empezar cogiendo el de arriba (el último que has puesto).
 
Por lo tanto, el puntero "inicio" apunta al último elemento que se ha añadido (cabeza de la pila). Al 
puntero "inicio" se le suele llamar "cabeza", "cima" o "tope".  
No necesita el puntero "fin".  

<!-- Page 17 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
17 
 
Overflow: Es un desbordamiento de pila. Al realizar un problema aritmético se produce un exceso de 
flujo de datos almacenados en la pila. La operación aritmética intenta crear un valor numérico que está 
fuera del rango que puede representarse con un número dado de dígitos, ya sea mayor que el máximo o 
menor que el mínimo valor representable.  
En seguridad informática y programación, un desbordamiento de búfer (del inglés buffer overflow o 
buffer overrun) es un error de software que se produce cuando un programa no controla 
adecuadamente la cantidad de datos que se copian sobre un área de memoria reservada a tal efecto 
(buffer): Si dicha cantidad es superior a la capacidad preasignada, los bytes sobrantes se almacenan en 
zonas de memoria adyacentes, sobrescribiendo su contenido original, que probablemente pertenecían a 
datos o código almacenados en memoria. Esto constituye un fallo de programación.
 
Colas 
También denominada lista FIFO  (First In First Out) ya que almacena datos en este orden, es decir, el 
primer elemento que se incorpora a la cola es el primero que sale.  
Para entenderlo, imagina la cola de un cine. El primero que llega es el primero que entra al cine, y si llega 
alguien nuevo se sitúa al final de la cola.  
Por lo tanto, el puntero "inicio" apunta al primer elemento que se añadió y el puntero "fin" al último 
elemento añadido. 

<!-- Page 18 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
18 
 
Bicola 
La bicola o doble cola es un tipo de cola especial que permiten la inserción y eliminación de elementos 
de ambos extremos de la cola.  
Puede representarse a partir de un vector y dos índices, siendo su representación más frecuente una 
lista circular doblemente enlazada.  
Todas las operaciones de este tipo de datos tienen coste constante.
 
El coste constante en el contexto de las listas bicola no se refiere al consumo de recursos, por lo menos 
de manera directa, sino al del algoritmo que lo caracteriza, la inserción y eliminación de los datos al 
principio y al final de la cola implica que siempre tarda el mismo tiempo, no recorrerá la estructura de 
datos a menos que la inserción o eliminación esté en medio de la lista. Para eliminar el primer o último 
elemento, se actualiza el puntero correspondiente al que se estaba apuntando liberando el elemento 
descartado.  
Operaciones sobre listas simples  
Existen diversas operaciones comúnmente aceptadas que se realizan sobre una lista. Vamos a ver 
algunas de ellas: 
• Inicializar:  se crea la lista creando el puntero "inicio" y el puntero "fin" (este es opcional) y se les 
asigna el valor NULL.  
• Calcular tamaño:  se recorre la lista y se va añadiendo (sumando) 1 en un contador por cada 
elemento. En algunas ocasiones es conveniente conocer el tamaño de la lista (evitar inserciones 
fuera de rango, saber si la lista está vacía, uso de algoritmos de búsqueda, información útil del 
número de elementos para el usuario).  
• Visualización:  recorre la lista y muestra uno a uno todos los valores de la lista.  
• Inserción: añade un nuevo elemento a la lista. Se gestiona de distinta forma según sea:  
• En una lista vacía:  

<!-- Page 19 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
19 
» El puntero "inicio" apunta al nuevo elemento.  
» El elemento "fin" apunta al nuevo elemento.  
» El puntero "siguiente" del nuevo elemento apunta a "NULL".  
 
• Al principio de la lista:  
» El puntero "siguiente" del nuevo elemento apunta al mismo elemento que el puntero 
"inicio" (es decir, al primer elemento de la lista).  
» El puntero "inicio" apuntará al nuevo elemento.  
 
• Al final de la lista: 
» El puntero "siguiente" del elemento apuntado por el puntero "fin" apuntará al nuevo 
elemento. 
» El puntero "siguiente" del nuevo elemento apuntará a NULL.  
» El puntero "fin" apuntará al elemento nuevo.  
 
• En un punto intermedio de la lista:  

<!-- Page 20 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
20 
» Se recorre el puntero hasta llegar al elemento que será su antecesor.  
» El puntero "siguiente" del antecesor apuntará al nuevo elemento.  
» El puntero "siguiente" del nuevo elemento apuntará al "sucesor".  
 
• Eliminación: elimina un elemento de la lista. Se gestiona de distinta manera según sea:  
• El primer elemento de la lista:  
» El puntero "inicio" apuntará al mismo sitio que el puntero "siguiente" del primer 
elemento. 
 
• Un elemento intermedio de la lista:  
» Se recorre el puntero hasta llegar al elemento llegar al antecesor del elemento que 
vamos a eliminar. 

<!-- Page 21 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
21 
» El puntero "siguiente" del antecesor apuntará al mismo punto que el puntero 
"siguiente" del elemento a eliminar (al sucesor).  
 
• El último elemento de la lista:  
» Se recorre el puntero hasta llegar al penúltimo elemento (el antecesor del que vamos a 
borrar).  
» El puntero "siguiente" del antecesor apuntará a NULL.  
» El puntero "fin" apuntará al antecesor.  
 
 
 
 
 
Reto 
Ahora que ya conoces los distintos tipos de lista y las operaciones 
que se pueden realizar.  
¿Por qué no realizas un esquema, y defines las operaciones sobre 
ellas? 
Utiliza dibujos, te resultará más fácil y claro.  
 
 

<!-- Page 22 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
22 
  
1.3.1.2. Árboles 
Existen muchas definiciones de árboles. Algunos autores afirman que son un tipo abstracto de datos 
(TAD), mientras que otros los definen como una estructura de dato.
 
Diremos que un árbol es un tipo de datos estructurados, dinámico y no lineal.  
No queremos entrar en definiciones complejas, por lo que resumiremos diciendo que un árbol es una 
lista enlazada simple en la que cada elemento puede tener más de un puntero "siguiente".  
Los árboles utilizan una estructura dinámica, ya que podemos borrar o añadir árboles en cualquier 
momento, dependiendo de las necesidades.  
 
 
 
 
Atención 
Los árboles utilizan una estructura jerárquica, mientras que las 
listas tienen una estructura lineal.  
 
 
Conceptos básicos  
Para empezar, debemos tener claros algunos conceptos/definiciones para entender los árboles:
 
• Nodo. Elementos de un árbol.  
• Nodo padre. Nodo que le apunta.  
• Nodo hijo. Nodo al que apunta un nodo padre.  
• Nodo raíz.  Primer nodo del árbol. Se caracteriza por no tener padres. Solo puede haber un nodo 
raíz por árbol.  
• Nodo hoja. Son todos aquellos nodos que no tienen hijos, los cuales, por tanto, siempre se 
encuentran en los extremos de la estructura . 
• Nodo rama. Son todos aquellos nodos que no son raíz y que además tienen al menos un hijo.
 

<!-- Page 23 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
23 
• Subárbol. Subconjunto de un árbol que es, a su vez, un árbol.  
• Nivel. Se refiere a la generación del árbol. El nodo raíz es el nivel 1, sus hijos el nivel 2 y así 
sucesivamente.  
• Altura. Es el mayor nivel de los nodos del árbol. En la figura siguiente, la altura sería 3.  
 
• Peso. Número total de nodos del árbol.  
• Grado de un nodo. Número de hijos que tiene.  
• Grado del árbol: El grado se refiere al mayor número de hijos que tiene alguno de los nodos del 
Árbol. Está limitado por el Orden, ya que este indica el número máximo de hijos que puede tener 
un nodo. 
• Hijos de un nodo: Nodos que dependen directamente de ese nodo, es decir, las raíces de sus 
subárboles. Padre de un nodo: Antecesor directo de un nodo, nodo del que depende 
directamente. Nodos hermanos: Nodos hijos del mismo nodo padre.  
 
El grado se calcula contando de forma recursiva el número de hijos de cada sub
-árbol hijo y el 
número de hijos del nodo actual para tomar el mayor, esta operación se hace de forma recursiva 
para recorrer todo el árbol.  
• Orden de un árbol. Grado máximo que pueden tener sus nodos.  
Número máximo de hijos que puede tener un Nodo.  
 

<!-- Page 24 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
24 
La diferencia entre el grado y el orden  está en que el orden es el nº máximo de hijos que puede tener 
un nodo, mientras que el grado es el nº máximo de hijos que tiene en ese momento el nodo. Un nodo 
puede tener un orden 4, aunque en ese momento su grado sea 3, pues no ha terminado de 
desarrollarse. 
 
Ejemplo 
• Profundidad o Camino.  Sucesión de nodos que hay que recorrer para llegar desde el nodo raíz a 
un determinado nodo.  
Longitud del camino (único) que comienza en la raíz y termina en el nodo. Se denomina 
también nivel. 
La profundidad de la raíz es 0 (no se comienza en 1), y la profundidad de un nodo es igual a la 
profundidad de su padre + 1  
 
Un árbol balanceado es aquel en el que entre el nodo hoja de menor nivel y el nodo hoja de mayor nivel 
hay una distancia máxima de 1.  
Un árbol n-ario es aquel donde el número máximo de hijos por nodo es igual a n.  
 
 
 

<!-- Page 25 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
25 
 
Reflexión 
La altura es el mayor nivel, por tanto, si el nivel de un árbol tiene 
como valor inicial 1, la altura será el número más alto de nivel 
(empezando por 1).  
La altura de un nodo en un árbol, es un concepto poco usado. Se 
define como la longitud del camino más largo que comienza en el 
nodo y termina en una hoja.  
La altura de un nodo hoja será de cero, y la altura de un nodo se 
puede calcular sumando uno a la mayor altura de sus hijos.  
 
 
Recorrido de un árbol  
Tenemos dos tipos fundamentales de formas de recorrer un árbol binario: búsqueda en profundidad (se 
divide a su vez en tres tipos: pre -orden, in-orden, pos-orden) y búsqueda en amplitud.  
 
• Búsqueda en profundidad: el recorrido de un árbol en profundidad se realiza mediante 
algoritmos recursivos.  
• Recorrido pre-orden: empezamos leyendo el nodo raíz y, a continuación, leemos en pre
-orden 
el subárbol a su izquierda y a continuación leemos en pre -orden el subárbol de la derecha. 
Podemos observar que es un algoritmo recursivo. Veamos una imagen para ver mejor cómo se 
recorre. 
 
 
 
 

<!-- Page 26 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
26 
 
+ Info 
Un algoritmo o función son recursivos cuando su proceso conlleva 
una llamada a sí mismos.  
Por ejemplo: el cálculo del factorial de n (n!) es n*n -1*n-2…*1 
4! =4*3*2*1 = 24 
Este proceso, se podría definir de forma recursiva diciendo que:  
n! = n*(n-1)! (estamos definiendo el proceso mediante una 
llamada a sí mismo).  
4! = 4*3! = 4*3*2! = 4*3*2*1! = 4*3*2*1 = 24 
Son de gran utilidad para problemas recursivos y los programas 
suelen ser más cortos.  
 
 
 
Recorrido en pre -orden 
• Recorrido in-orden: empezamos leyendo en in -orden el primer subárbol de la raíz (el de la 
izquierda); a continuación, leemos el nodo raíz; finalmente, leemos en in
-orden el subárbol 
de la derecha. De nuevo utilizamos un algoritmo recursivo. Veamos una imagen para 
entenderlo mejor.  

<!-- Page 27 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
27 
 
Recorrido en in -orden 
• Recorrido post -orden: se recorren en post -orden los subárboles izquierdo y derecho para 
finalizar leyendo el nodo raíz. Para no variar, también es recursivo. Vamos a ver la imagen.
 
 
Recorrido en post -orden 
• Búsqueda en amplitud:  empezamos leyendo el nodo raíz. A continuación, leemos los nodos del 
siguiente nivel de izquierda a derecha y seguimos nivel a nivel hasta el final. Este es un problema 
iterativo, por lo que no usaremos recursividad. Vamos con una imagen para verlo más claro.
 
 
Búsqueda en amplitud  

<!-- Page 28 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
28 
1.3.1.3. Grafos 
Un grafo es una estructura de datos (o un tipo abstracto de datos según algunos autores) consistente 
en un conjunto de nodos o vértices  y un conjunto de arcos (aristas)  que establecen relaciones (no 
jerárquicas) entre los nodos.  
Características  
Algunas características de un grafo son:  
• No hay restricciones para formar un grafo.  
• El grado de un nodo es el número de aristas que inciden a ese nodo.  
• Puede haber dos aristas entre dos vértices (una en cada sentido en el caso de grafos dirigidos).
 
• El vértice de partida de una arista puede ser el mismo que el de llegada (se relaciona con si 
mismo).  
• Las aristas pueden o no llevar flechas (pueden ser dirigidos o no dirigidos).
 
• Se pueden formar ciclos. Un ciclo es un camino que empieza en un nodo y termina en el mismo 
nodo. 
 
 
 
 
+ Info 
Los grafos tienen multitud de aplicaciones.  
• Por ejemplo, podríamos calcular el recorrido óptimo de un 
repartidor que tiene que pasar por varios puntos.  
• También es parte fundamental en el reconocimiento del 
lenguaje natural y un sinfín de problemas más.  
Los grafos son un tema amplio y complejo, y no necesitamos tener 
más conocimiento sobre ellos.  
 
 

<!-- Page 29 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
29 
2. Sistemas de almacenamiento  
Hay dos sistemas de almacenamiento:  
• Primario: 
Está constituido por la memoria del dispositivo (RAM, cache, etc.).
 
Es donde se almacenan los programas durante su ejecución y los datos que estos necesitan, por 
lo que solo está activa mientras el dispositivo está en funcionamiento.  
• Secundario: 
Está constituido por diversos tipos de dispositivos, tales como discos duros, Pendrives, 
dispositivos ópticos y memorias flash, etc.  
Su objetivo es proporcionar un sistema de almacenamiento permanente de la información, es 
decir, mantener la información, aunque el dispositivo no se encuentren en funcionamiento.
 
En estos sistemas de almacenamiento secundario hay una determinada organización, la 
información se organiza mediante un sistema de ficheros.  
La forma más básica de organización utiliza dos tipos de entidades, FICHEROS y DIRECTORIOS 
y la estructura organizativa de la información mediante el uso de las entidades anteriores, es 
conocida como sistema de ficheros  (S.F.). Algunos de los aspectos que debe controlar un 
sistema de ficheros  son: 
• Las reglas (por ejemplo, en cuanto a nº máximo de caracteres y tipo de estos que admitan 
los nombres) que deben cumplir los ficheros y directorios.  
• Tamaños máximos de ficheros, directorios y almacenamiento total.
 
• Sistema organizativo de los directorios (generalmente "en árbol").
 
• Método de localización y asignación de espacio a los ficheros en el dispositivo de 
almacenamientos.  
• Etc. 
 
 
 
 

<!-- Page 30 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
30 
 
+ Info 
En los sistemas operativos modernos (Linux, Windows, macOS, 
iOS y Android), los directorios se gestionan internamente como un 
tipo especial de archivo dentro del sistema de ficheros.  
No obstante, para facilitar su uso, al usuario se le presenta una 
estructura jerárquica claramente diferenciada entre directorios y 
archivos. 
 
 
Sobre este almacenamiento secundario gestionado por el sistema de ficheros, el sistema 
operativo define el concepto de fichero como unidad lógica de información.
 
3. Ficheros 
Todas las estructuras de datos que hemos visto hasta ahora utilizan memoria principal. Esto presenta 
dos limitaciones importantes:  
1. Los datos desaparecen cuando el programa termina.  
2. La cantidad de los datos no puede ser muy grande debido al tamaño de la memoria principal.
 
 
Un fichero, también llamado archivo,  es una estructura dinámica (su tamaño puede variar en tiempo de 
ejecución).  
Archivo o fichero informático  
Unidad lógica de información estructurada en bytes, almacenada de forma persistente (soporte 
electrónico hardware o unidad de almacenamiento) en un sistema de archivos y gestionada por el 
kernel del sistema operativo a través del sistema de ficheros.  
Tiene un nombre, que debe ser único dentro del directorio donde se almacena; la extensión es una 
convención, utilizada por algunos sistemas operativos y aplicaciones, pero no obligatoria
 
Los ficheros pueden tener atributos como las fechas (creación y última modificación) y el propietario, 
así como permisos de acceso que determinan las operaciones permitidas (lectura, escritura y 

<!-- Page 31 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
31 
ejecución); además, dependiendo del sistema operativo, pueden existir atributos adicionales como solo 
lectura, oculto o de sistema.  
Debe preservase su accesibilidad, legibilidad y disponibilidad a largo plazo, evitando su deterioro o 
corrupción que lo haga ilegible.  
En algunos tipos de ficheros de datos estructurados, la información contenida puede organizarse 
lógicamente en registros y campos.  
• Registro:  Un registro es una estructura de datos formada por un conjunto organizado de 
campos relacionados entre sí por la información que contienen.  
Pueden ser de longitud fija o variable.  
• Campo: Son los elementos que componen un registro.  
Cada campo es de un tipo determinado.  
Un campo puede estar dividido en subcampos.  
Tabla de Base de Datos:  
 
El concepto de fichero aísla al usuario de los problemas físicos de almacenamiento.
 
El sistema operativo realiza una segunda abstracción que consiste en agrupar ficheros en carpetas o 
directorios.  
La estructura global del sistema de archivos suele tener una organización jerárquica en forma de árbol. 
El nodo raíz se denomina directorio raíz. En Windows corresponde a "
\" dentro de cada unidad 
identificada por una letra (por ejemplo, C: \), mientras que en Linux/Unix el directorio raíz es "/", y los 
dispositivos se montan en directorios. El resto de los directorios y los archivos deben tener un nombre.
 
La estructura de almacenamiento de archivos es en forma de árbol jerárquico. Una carpeta (directorio) 
puede contener otras carpetas (subcarpetas o subdirectorios) y/o ficheros.
 
Dentro de una carpeta no puede haber dos entradas con el mismo nombre, ya sean ficheros o 
subdirectorios.  

<!-- Page 32 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
32 
 
Cada fichero viene determinado por:  
• Nombre del fichero. El nombre es el identificador del fichero dentro del sistema de archivos. La 
extensión es una convención utilizada por algunos sistemas operativos y aplicaciones para 
indicar el tipo de fichero.  
Dependiendo del sistema de archivos se podrá diferenciar o no entre mayúsculas y minúsculas.
 
• Ruta del fichero.  Es la sucesión de carpetas por las que debe pasar para llegar al fichero (el 
camino que se debe recorrer).  
Se suele utilizar un símbolo para separar el nombre de cada carpeta (barra normal "/" en 
sistemas Unix/Linux y " \" en Windows).  
Por ejemplo, la ruta "/carpeta1/carpeta2/mitexto.txt" indica, en sistemas Unix/Linux el 
recorrido desde el directorio raíz hasta el fichero "mitexto.txt". 
 
3.1. Nombre y extensión de un fichero  
Nombre de fichero. Extensión.  
La identificación o "nombre" de un fichero, se compone de 3 partes: el nombre, seguido de un punto, y 
la extensión: 
• Nombre: 
La longitud máxima de los nombres de fichero está limitada por el sistema operativo y el sistema 
de archivos, por ejemplo, en Windows -NTFS podemos tener hasta 255 caracteres en el nombre.
 

<!-- Page 33 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
33 
A la hora de nombrar los ficheros, debemos tener en cuenta ciertas normas:
 
• Nombre Único: es decir que no debe repetirse en la misma carpeta/directorio.
 
• Restricción de uso de caracteres: existen caracteres no permitidos a la hora de dar nombre 
a un fichero, son caracteres "no válidos" (como por ejemplo: / : * ? " < > |).
 
También hay caracteres "no habituales", o no recomendables, como por ejemplo la ñ o los 
acentos y signos especiales (aunque esta característica dependerá del S.O. y del Sistema de 
Ficheros que estemos usando).  
• Uso de Mayúsculas/minúsculas:  
Dependiendo del sistema operativo utilizado, diferenciará un carácter en mayúscula o 
minúscula. 
En Windows es indiferente que utilicemos mayúsculas o minúsculas en el nombre. por lo 
que Ejemplo.txt es el mismo nombre que ejemplo.txt.  
En Unix/Linux si se diferencian, por lo que Ejemplo.txt es un archivo distinto de ejemplo.txt 
o de ejeMplo.txt.  
• El punto: separa el nombre de la extensión.  
• La extensión  es una convención utilizada para asociar el fichero con una aplicación, pero no 
garantiza ni determina el contenido real del fichero (no tiene una longitud fija).
 
La extensión puede ser asignada automáticamente por una aplicación, pero el usuario puede 
modificarla manualmente.  
Si un usuario cambia o borra la extensión, el fichero puede dejar de estar asociado 
correctamente a una aplicación, aunque su contenido no se modifica.
 
En una misma carpeta no puede haber dos entradas con el mismo nombre completo.
 
En los sistemas Windows, si un fichero tiene una extensión determinada (por ejemplo: .ai, .psd, 
.pdf), el sistema operativo mantiene un registro de asociaciones entre las extensiones de 
archivo y los programas instalados. De este modo, cuando el usuario abre un fichero, Windows 
ejecuta automáticamente el software asociado a dicha extensión (Adobe Illustrator, Photoshop, 
Acrobat Reader u otro programa compatible).
 
Si la extensión no está asociada a ningún programa, el sistema operativo puede solicitar al 
usuario que indique con qué aplicación desea abrir el archivo. En cualquier caso, la apertura 
correcta del fichero solo estará garantizada si el programa seleccionado reconoce y entiende 
correctamente el formato y la codificación real del archivo.
 
Algunas de las extensiones más comunes son:  
• .exe = Fichero ejecutable.  

<!-- Page 34 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
34 
• .c = Programa fuente en lenguaje C.  
• .cpp = Programa fuente en lenguaje C++.  
• .asm = Programa fuente en lenguaje ensamblador.  
• .html = Documento escrito en lenguaje de hipertexto.
 
• .jpg = Imagen codificada según el estándar JPEG.  
• .mp3 = Sonido codificado según el estándar MPEG -1/2 Audio Layer III.  
• .pdf = Documento en formato PDF (Portable Document Format).
 
• .zip = Archivo comprimido.  
 
 
 
 
+ Info 
Aunque la extensión ayuda al sistema operativo y al usuario a 
asociar un fichero con una aplicación, no garantiza el tipo real de 
contenido. Dos ficheros con la misma extensión pueden tener 
formatos internos distintos, y un fichero puede funcionar 
correctamente aunque su extensión sea incorrecta si la aplicación 
interpreta adecuadamente su codificación.  
 
 
3.2. Atributos de los ficheros  
Son características concretas que se asocian a un fichero, y que ofrecen información adicional no 
relacionada con su contenido, como puede ser fecha de creación o modificación, autor, si es un fichero 
de sistema, de sólo lectura etc. No son datos de su contenido, son sus atributos.
 
Están estrictamente definidos por el sistema de archivos de cada sistema operativo.
 
Los permisos de acceso se utilizan para obtener o denegar derechos sobre un archivo o carpeta; los 
atributos son metadatos del sistema de archivos.  
Cuando se aplica un atributo a un archivo, esta modificación solo se aplica a este archivo, en los 
directorios, la aplicación a subdirectorios y archivos depende del comando y de las opciones utilizadas, 
no es automática.  

<!-- Page 35 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
35 
También existe la posibilidad de aplicar estas modificaciones utilizando nombres de ficheros con 
caracteres "comodín". Por ejemplo, clientes??.txt modificaría a todos los archivos que se llamen 
"clientes" seguidos de dos caracteres más (clientes01, clientesAA, etc…).
 
Atributos en Windows  
Los atributos básicos de Windows pueden modificarse a través de la interfaz gráfica o mediante 
consola. 
Mediante la consola de Windows, con el comando: ATTRIB y sus respectivos modificadores o 
propiedades que podremos ver si escribimos: attrib /?  
Con el símbolo + se activa el atributo y con el símbolo menos se desactiva.
 
ATTRIB [+R | -R] [+A | -A ] [+S | -S] [+H | -H] [[drive:] [path] filena
-me] [/S [/D]]
 
Las opciones son:  
• R: Atributo de sólo lectura.  
• A: Atributo de archivo.  
• S: Atributo de sistema.  
• H: Atributo de archivo oculto.  
• /S: Procesa todos los archivos en todos los directorios de una ruta especificada.
 
• /D:  Procesa los directorios también.  
Atributos en GNU/Linux  
Vamos a ver una lista de los atributos más extendidos en el sistema de archivos ext2/ext3/ext4 
(entenderás mejor estos conceptos a medida que avances con el estudio de las siguientes unidades).
 
• Atributo A.  
El valor de la fecha de acceso sobre un archivo no será cambiado en cada lectura, por tanto, la 
fecha del último acceso no es actualizada. Puede incrementar los tiempos de lectura al ahorrarse 
la actualización de esta información que forma parte de los metadatos de un archivo.
 
• Atributo a. 
El archivo sólo puede ser abierto en adición para escritura, es decir, los archivos con este 
atributo sólo pueden ser escritos por redireccionamiento (>>) y el archivo no puede ser 
eliminado. 

<!-- Page 36 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
36 
Sólo el usuario root o un programa que disponga de privilegios necesarios puede cambiar este 
atributo, de hecho, este atributo está pensado principalmente para usarlo con logs.
 
• Atributo i. 
Pone el fichero en modo solo lectura, por tanto, el archivo (o directorio) no puede ser 
modificado, borrado, o renombrado.  
Sólo root o un binario que posea los privilegios necesarios puede modificar este atributo.
 
Resulta interesante activarlo en ficheros que rara vez son escritos, como binarios, ficheros de un 
servidor web, repositorios de consulta, o incluso ficheros de BBDD que no son accedidos vía 
web para su modificación.  
3.3. Tipos de ficheros  
Todos los ficheros se pueden clasificar en uno de dos grandes tipos según su formato de 
almacenamiento: ficheros de texto y ficheros binarios.  
Además de esta clasificación principal, los ficheros pueden agruparse atendiendo a otros criterios, en 
función de distintos parámetros como su contenido, su permanencia o su licencia.
 
 
Contenido del fichero  
Existen dos tipos principales: de texto y binarios.  
Tanto los ficheros binarios como los de texto contienen datos almacenados como una serie de bits 
(valores binarios de 0 y 1). La diferencia entre ambos no reside en la forma física de almacenamiento, 
sino en la interpretación que se hace de esos bits.  
En los ficheros de texto, los bits representan caracteres según una determinada codificación, mientras 
que en los ficheros binarios los bits se almacenan según la estructura interna que haya decidido el 
programa que los genera, y no necesariamente como texto legible.
 
 

<!-- Page 37 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
37 
• Ficheros de texto : 
Los ficheros de texto contienen información codificada como caracteres y solo permiten un 
determinado rango de valores (letras, números, signos de puntuación y caracteres especiales).
 
Sus características principales son:  
• Contienen secuencias de caracteres, habitualmente organizadas mediante separadores 
como saltos de línea.  
• Al abrirlos con un editor de texto es posible visualizar y comprender su contenido
 
• Son más restrictivos que los ficheros binarios, ya que solo pueden almacenar información 
textual. 
• Están codificados según tablas de codificación de caracteres, como ASCII, EBCDIC o 
Unicode 
• Debido a su formato simple y estandarizado, muchos programas distintos pueden leer y 
editar ficheros de texto.  
Los ficheros de texto pueden almacenarse como texto sin formato o como texto enriquecido. En este 
último caso, además de los caracteres visibles, el fichero incluye códigos adicionales que indican cómo 
debe mostrarse el texto (negrita, cursiva, tamaño de fuente, formato de página, etc.).
 
• Ficheros binarios:  
Los ficheros binarios contienen secuencias de elementos organizados según un tipo o estructura 
de datos determinada.  
Sus características principales son:  
• Los datos se almacenan de forma similar a como residen en la memoria principal, por lo que 
su lectura o escritura no requiere conversiones intermedias.  
• Suelen estar formados por secuencias de bytes o agrupaciones ordenadas de ocho bits.
 
• Pueden contener distintos tipos de información en un mismo fichero, como datos de audio, 
imágenes, vídeo o estructuras complejas.  
• Al abrirse con un editor de texto, su contenido aparece como texto ilegible.
 
• Su interpretación correcta requiere programas específicos que conozcan el formato interno 
del fichero. 
Estos ficheros suelen incluir encabezados, que son bloques de datos situados al comienzo del fichero y 
que identifican su tipo y proporcionan información descriptiva adicional.
 

<!-- Page 38 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
38 
Longitud del fichero  
Esta clasificación se aplica principalmente a ficheros de datos estructurados y será desarrollada con 
mayor detalle en los apartados dedicados a la organización lógica del contenido.
 
Según la longitud de los registros que contienen, los ficheros pueden clasificarse en:
 
• De longitud variable.  Cada registro es de una longitud diferente.  
• De longitud fija.  Los datos se almacenan en registros de tamaño constante.
 
• Mixtos. Contiene registros variables y de longitud fija.  
Permanencia del fichero  
 
 
 
 
+ Info 
Aunque vamos a comentar ligeramente los distintos tipos según la 
permanencia para que los puedas conocer, lo importante es que 
sepas que hay dos tipos de ficheros: permanentes y temporales.  
 
 
Según el tiempo durante el cual la información debe conservarse, los ficheros pueden clasificarse en dos 
grandes categorías.  
• Ficheros permanentes.  Son aquellos que se almacenan durante largos periodos de tiempo, ya 
que contienen información relevante que no puede regenerarse de forma inmediata.
 
Dentro de esta categoría tenemos tres tipos diferentes:  
• Maestros, que contienen el estado actual de los datos y pueden ser modificados por la 
aplicación. 
• Constantes , que almacenan datos fijos sobre los que se realizan consultas.  
• Históricos , que conservan datos antiguos para permitir la reconstrucción de situaciones 
pasadas o la verificación de estados anteriores.  
• Ficheros temporales.  Contienen información necesaria únicamente durante un proceso o 
durante un periodo de tiempo limitado, tras el cual dejan de ser útiles.  

<!-- Page 39 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
39 
Dentro de esta categoría tenemos tres tipos diferentes según su uso:
 
• Intermedios, que almacenan resultados parciales utilizados por procesos posteriores.  
• De maniobras, empleados cuando los datos no caben en memoria principal.  
• De resultados,  que contienen información destinada a ser transferida a un dispositivo de 
salida, como una impresora.  
Clasificación Según Licencia  
Existen dos tipos:  
• Abiertos. Son estándares libres que pueden utilizarse sin ninguna restricción. Un ejemplo sería 
OpenDocument . 
• Cerrados. Son formatos propietarios. Los usuarios deben pagar una licencia, comprar el 
programa correspondiente para poder usarlos. Ejemplos son los ficheros .docx (en versiones 
antiguas .doc) de Microsoft Word, o ficheros.psd de Photoshop.  
 
 
 
 
+ Info 
En la actualidad existe una tendencia hacia el uso de formatos 
abiertos, debido a los problemas de incompatibilidad que pueden 
generar los formatos propietarios, incluso entre distintas versiones 
de una misma aplicación.  
 
 
3.4. Principales formatos de ficheros  
Un formato de fichero indica la forma de codificar la información que se almacenará en un fichero.
 
Existe una gran cantidad de formatos de ficheros. Vamos a ver algunos de los más importantes 
clasificados en distintas categorías.  

<!-- Page 40 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
40 
 
3.4.1. Documentos  
Vamos a ver una descripción sobre cada tipo de documento:  
• .TXT:  
Ficheros en los que se guarda texto plano (normalmente en código ASCII). Es un formato simple 
que puede utilizarse con muchos editores. Almacena caracteres alfanuméricos y algunos 
caracteres especiales (como el salto de línea).  
• .DOC, .DOCX:  
Es uno de los más utilizados. Es un formato cerrado propiedad de Microsoft. Se pueden insertar 
imágenes e incluso código Visual Basic. Lo utiliza el programa Microsoft Word.
 
• .ODT:  
Documento de texto del estándar abierto ODF (Open Document Format) denominado 
OpenDocument. Es el elegido como estándar para el intercambio de texto con formato por ISO 
(Organización Internacional de Normalización).
 
• .PDF: 
Portable Document Format  (formato de documento portable). En realidad, se puede usar para 
gráficos vectoriales, mapas de bits, texto o la combinación de varios de ellos. Es uno de los más 
extendidos en Internet para el intercambio de documentos. Las instituciones públicas de España 
lo utilizan para sus comunicaciones. El lector de ficheros .pdf es gratuito y muchos programas 
permiten guardar en este formato (como Microsoft Word y Writer de OpenOffice).
 

<!-- Page 41 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
41 
Tipos de PDF:  
• PDF 2.0 (ISO 32000 -2:2020)  es una actualización y perfeccionamiento de las 
especificaciones PDF anteriores. El objetivo fundamental de esta especificación es 
consolidar, aclarar y limpiar la especificación, por lo que se han depurado funciones 
heredadas ofreciendo indicaciones más claras para los desarrolladores y como consecuencia 
una mejor experiencia de usuario PDF, posibilitando que puedan añadirse innovaciones de 
manera más efectiva.  
• PDF/UA (ISO 14289 -1:2012)  La UA proviene de las siglas en inglés Universal Accessibility, 
accesibilidad Universal. Está orientado esencialmente en facilitar pautas y especificaciones a 
los desarrolladores de viso -res PDF y herramientas de creación PDF con el fin de que 
cumplan con los requisitos de accesibilidad y permitan a los usuarios con discapacidades 
interactuar y comprender el contenido de los documentos. Por ejemplo, la lectura en voz 
de un documento por parte de un ordenador.  
• PDF/A  (ISO 19005 ), está pensado para que el documento se conserve igual a largo plazo, 
sea totalmente autocontenido y cuente con un juego de caracteres sea Unicode. No incluye 
audio, vídeo, JavaScript o cifrado.  
• PDF/X (ISO 15930)
, 2001 es la fecha de su primera versión, hoy la actualización de esa 
ISO. Los archivos han de ser autosuficientes y contener todos los elementos necesarios 
para su correcta visualización e impresión: fuentes, imágenes, colores… eliminando los que 
sean inservibles para la impresión como música, vídeo o botones interactivos.
 
• PDF/E (ISO 24517)
: diseñado para las necesidades específicas de la ingeniería, facilitando la 
creación, el intercambio y la visualización de documentos técnicos, como planos, dibujos, 
especificaciones y documentación relacionada con proyectos de ingeniería.
 
• PDF/VT  (ISO 16612):  estándar diseñado para aplicaciones de impresión variable y 
transaccional. Se centra fundamentalmente en la creación de documentos que contienen 
datos variables y que están optimizados para la producción de impresión de alta calidad. 
Tecnología es ampliamente utilizada en aplicaciones de impresión masiva y personalizada: 
creación de facturas, estados de cuenta, documentos personalizados y otros materiales de 
impresión de alta calidad.  
• .RTF:  
Rich Text Format  o formato de texto enriquecido. Se utilizaba para el intercambio de datos 
entre Apple y Microsoft. Es el formato que utiliza Wordpad por defecto.
 
• .PS: PostScript:  
Utiliza un lenguaje de programación para describir una imagen de impresión. Se utiliza para 
impresión en alta calidad de imágenes. Para abrirlo podemos utilizar programas como 
GhostView y GhostScript.  

<!-- Page 42 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
42 
3.4.2. Hojas de Cálculo  
Vamos a ver una descripción sobre cada tipo de hoja de cálculo:  
• .XLS:  
Predeterminado de Excel 2010 y Excel 2007. No se pueden almacenar códigos de macros de 
Microsoft Visual Basic para Aplicaciones (VBA) ni hojas de macro de Office Excel 4.0 (.xlm).
 
• .XLSM: 
Basado en XML y habilitado para macros para Excel 2016, Excel 2013, Excel 2010 y Excel 2007. 
Almacena código de macros de VBA u hojas de macros de Excel 4.0 (.xlm).
 
• .XLSB:  
Formato de archivo binario (BIFF12) de Excel 2010 y Excel 2007.
 
• .XLTX:  
El formato predeterminado para una plantilla de Excel 2010 y Excel 2007. No puede almacenar 
código de macros de VBA ni hojas de macros de Excel 4.0 (.xlm).
 
• .ODS: 
Formato de archivo Hoja de cálculo en OpenDocument (.ods) que usan algunas aplicaciones de 
hojas de cálculo como OpenOffice.org Calc y Google Docs.
 
3.4.3. Compresores  
Vamos a ver los principales compresores que se usan actualmente:  
• .ZIP: 
Formato libre de compresión sin pérdida. Es el más popular para Windows.  
• .GZ, .TGZ:  
GNU Zip o GZip. Es el más utilizado en UNIX y Linux. GZip comprime, pero no archiva. Para ello 
se vale de Tar. Tgz es un fichero comprimido con GZip y archivamos con Tar.
 
• .RAR: 

<!-- Page 43 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
43 
Formato propietario de compresión sin pérdida. Suele comprimir más que ZIP, pero es algo más 
lento. 
• .7z: 
Es un formato de compresión de datos sin pérdida con tasas de compresión superiores a ZIP y 
RAR. Puede utilizar distintos algoritmos de compresión.
 
3.4.4. Imágenes  
Existen dos tipos de imágenes:  
• Los mapas de bits (bitmaps) son agrupaciones rectangulares de pequeños puntos (píxeles).
 
A diferencia de los gráficos vectoriales al ser recalados a un tamaño mayor, pierden calidad.
 
• Los gráficos vectoriales se construyen sobre figuras geométricas.
 
Su principal ventaja es que se pueden agrandar sin perder calidad.  
Mapas de bits 
• . BMP: 
Es un formato propio del S.O. Microsoft Windows, se utiliza con Microsoft Paint, (aunque 
actualmente todos los S.O. son compatibles con esta extensión pudiéndose trabajar con estos 
archivos desde prácticamente cualquier software).  
Es un archivo de imagen con formato del ITSL imagen de mapa de bits, es decir, un archivo de 
imagen de gráficos, con píxeles almacenados en forma de tabla de puntos que administra los 
colores como colores reales o usando una paleta indexada.  
Algunas características son:  
• Los ficheros que contienen pueden guardar imágenes de 64 bits o menos.
 
En un principio el máximo que se tenía eran 24bits, pero luego se amplió a 64, aunque las 
más típicas son de 24 bits por píxel (16,7 millones de colores), 8 bits (256 colores).
 
• Usan una técnica de compresión RLE que permite almacenar imágenes, aunque no sean 
demasiado grandes.  
• Las imágenes digitales conservadas en dicho formato están compuestas por píxeles 
ubicados en una cuadrícula rectangular.  

<!-- Page 44 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
44 
• Los archivos de mapas de bits se componen de direcciones asociadas a códigos de color, 
uno para cada cuadro en una matriz de píxeles (tal como se esquematizaría un dibujo de 
"colorea los cuadros" para niños pequeños).  
• Pueden mostrar un buen nivel de calidad.  
A pesar de dicho nivel de calidad, se caracterizan por ser muy poco eficientes en su uso de 
espacio en disco, por tanto, no se utilizan en páginas web (problema de tamaño en su 
relación con la resolución).  
En función del color de la imagen, (de la profundidad de color que tenga la imagen), cada 
píxel puede llegar a ocupar 1 o varios bytes, lo que sería una barbaridad al cargar cualquier 
sitio web que incluyese archivos de este tipo.  
Generalmente se suelen transformar en otros formatos, como JPEG (fotografías), GIF 
(animaciones) o PNG (dibujos y esquemas), los cuales utilizan otros algoritmos para conseguir 
una mayor compresión (menor tamaño del archivo).
 
• . JPG .JPEG: 
Joint Photographic Experts Group.  
Es el más extendido por su relación tamaño/calidad, y por ofrecer muchas técnicas de 
compresión. Esta compresión pierde información sobre el color de una imagen, ya que el ojo 
humano percibir mejor los cambios en el brillo que en el color.  
Con esta técnica se pueden conseguir tasas de compresión de 20 a 1 sin que apenas se note. Se 
puede controlar la tasa de compresión de una imagen especificando el valor de un parámetro Q. 
Si el valor de Q es grande la imagen tiene mayor calidad y ocupa mayor espacio que cuando el 
valor de Q es pequeño . 
La técnica JPEG básica (baseline JPEG) consta de 5 pasos:
 
1. Transformación  de la imagen RGB a una imagen en el espacio de colores.  
» YCr Cb.  
2. Reducción de las componentes de color (opcional).  
3. Partición de la imagen en bloques (ventanas) de nxn pixeles y determinación de la 
transformada del coseno discreta (TCD) para cada bloque.
 
4. Cuantificación de los coeficientes de la TCD  de cada bloque. Para ello, dichos coeficientes 
se dividen por su correspondiente coeficiente de cuantificación y se redondean al valor 
entero más próximo. Este paso reduce muchos elementos a cero favoreciendo la 
compresión. El valor de Q determina los coeficientes de cuantificación. Así, se dispone de 
varias tablas de coeficientes de cuantificación.  
5. Codificación  sin pérdidas de los coeficientes reducidos utilizando el algoritmo de Huffman 
modificado.  

<!-- Page 45 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
45 
• .GIF: 
Graphics Interchange Format.  
Formato gráfico muy extendido en Internet al permitir imágenes animadas y ser soportado por 
la mayoría de los navegadores. Es un formato comprimido sin pérdida de calidad.  
• .TIF: 
Tagged Image File Format.  
Imagen que puede contener etiquetas y más de una imagen por archivo. Tiene una versión sin 
comprimir (ocupa mucho espacio) y otra con compresión sin pérdida.
 
• .PNG: 
Portable Network Graphics.  
Formato comprimido sin pérdida de calidad. Desarrollado como alternativa a GIF con mejores 
colores. 
Gráficos vectoriales  
• .SVG: 
Scalable Vector Graphics.  
Es el formato abierto estándar de w3c (World Wide Web Consortium).  La mayoría de los 
navegadores pueden mostrarlas. Soporta imágenes en dos dimensiones estáticas y animadas.
 
• .EPS: 
PostScript  encapsulado. 
Es un formato de exportación muy compatible, pero complejo, lo que hace que algunos 
programas no sean compatibles con todas sus variantes.  
• .ODG: 
Open Document Graphics.  
Documento de gráficos del estándar abierto ODF (OpenDocument). Puede contener gráficos 
vectoriales, mapas de bits o ambos al mismo tiempo.  
• .SWF: 
Inicialmente abreviación de Shockwave Flash y posteriormente retroacrónimo de Small Web 
Format -formato web pequeño - para evitar confusiones con Shockwave del que deriva.  

<!-- Page 46 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
46 
Creado por la empresa Macromedia (actualmente Adobe Systems) Pueden ser generados por 
diversidad de aplicaciones, aunque el programa original Adobe Flash Professional utiliza un 
formato editable con extensión ".fla" con los que el usuario trabaja y que después compila y 
comprime en SWF. Están constituidos principalmente por dos elementos: objetos basados en 
vectores (gráficos vectoriales) e imágenes. Aunque también incorporan audio y vídeo (en 
diferentes formatos Flash Video) y multitud de formas diferentes de interacción con el usuario.
 
3.4.5. Audio 
Existen tres tipos de formato de audio:  
• Sin comprimir.  
• Con compresión sin pérdida.  
• Comprimidos con pérdida.  
Sin comprimir 
• .WAV: 
WAVeform audio format.  
No posee compresión, por lo que es de muy alta calidad. WAV es uno de los formatos más 
utilizados en el ámbito del sonido profesional. No se utiliza en Internet por su gran tamaño.  
• .AIF .AIFF: 
Audio Interchange File Format.  
Sin compresión y de alta calidad. Desarrollado por Apple. Es otro de los formatos utilizados en el 
ámbito del sonido profesional.  
Compresión sin pérdida  
• .FLAC:  
Free Lossless Audio Codec.  
Códec libre de compresión de audio sin pérdida. Reduce en un tercio el tamaño de un WAV 
eliminando residuos no útiles. Tiene una calidad muy alta.  
• .ALAC:  
Aple Lossless Audio Codec.  

<!-- Page 47 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
47 
Es el formato utilizado para las transmisiones de Apple Music.  
Compresión con pérdida  
• .MP3: 
MPEG-1 Audio Layer 3 (MP3).  
Es un formato de audio digital comprimido con pérdida desarrollado por el 
Moving Picture 
Experts Group (MPEG) para formar parte del formato de vídeo MPEG. Actualmente es el más 
utilizado en Internet.  
• .WMA: 
Windows Media Audio. 
Es un formato de compresión de audio con pérdida perteneciente a Microsoft. Es inferior a MP3.
 
• .AAC: 
Advanced Audio Coding.  
Ofrece la misma calidad que MP3, pero con menor tamaño. La plataforma iTunes de Apple lo 
utiliza. También se utiliza para comprimir audio de vídeo.  
• .OGG Media (OGM):  
OGG es un contenedor que puede almacenar diversos contenidos multimedia, audio, vídeo e 
incluso texto (subtítulos). En lo que al audio se refiere, es compatible con una ampila gama de 
codecs como Vorbis, Opus o FLAC.  
Da resultados ligeramente superiores al MP3 en calidad, pero no está tan difundido y no tiene 
tanta compatibilidad.  
3.4.6. Video 
• .AVI: 
Audio Video Interleave.  
Es un formato contenedor de audio y video lanzado por Microsoft.
 
• .MPG, .MPEG: 
Es un estándar de codificación de audio y video desarrollado por el Moving Picture Experts 
Group perteneciente a ISO.  

<!-- Page 48 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
48 
• .WMV: 
Windows Media Video. 
Utiliza un conjunto de algoritmos de compresión desarrollado por Microsoft.
 
• .ASF: 
Advanced Streaming Format.  
(Posteriormente renombrado como Advanced Systems Format ). 
Es un formato contenedor de audio y vídeo digital propiedad de Microsoft, diseñado 
especialmente para el streaming. 
• .MOV: 
Formato utilizado por QuickTime de Apple.  
Actualmente es compatible con el estándar MPEG -4. 
• .MP4 es un formato de archivo comúnmente utilizado para almacenar flujos de video y audio 
digital. Es ampliamente compatible con diversos dispositivos y plataformas, lo que lo convierte 
en una opción popular para compartir y distribuir contenido de video. La extensión ".mp4" 
significa MPEG -4 Parte 14, que es un estándar de compresión de video ampliamente utilizado.
 
• .MKV Un archivo con extensión .mkv es un contenedor multimedia que puede contener 
múltiples tipos de contenido, como video, audio, subtítulos y metadatos. MKV significa 
Matroska Video, y es un formato de archivo de código abierto que es popular por su capacidad 
para almacenar una variedad de tipos de datos multimedia en un solo archivo.  
3.5. Operaciones sobre ficheros  
Las operaciones relacionadas con el almacenamiento persistente pueden aplicarse directamente sobre 
los ficheros o, en el caso de ficheros de datos estructurados, sobre los registros que contienen.
 
• Operaciones con ficheros:  
• Crear fichero.  Se crea un fichero nuevo sin dato, asignándole un nombre y una ubicación en 
el sistema de archivos.  
• Borrar fichero. Elimina el fichero y libera el espacio que ocupaba en el almacenamiento 
secundario. 
• Abrir fichero. Es necesario abrir el fichero para poder realizar operaciones sobre él. No 
implica cargar todo el fichero en memoria, sino establecer un canal de acceso gestionado 
por el sistema operativo.  

<!-- Page 49 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
49 
• Cerrar fichero.  Una vez concluidas las operaciones sobre el fichero, se debe cerrar para 
liberar los recursos asociados, evitar posibles errores (fichero corrupto) y asegurar la 
correcta escritura de los datos.  
• Ordenar fichero. Consiste en modificar la disposición de los registros en base a uno o más 
campos. No es una operación propia del sistema operativo, sino de la aplicación, y solo 
tiene sentido en ficheros de datos estructurados.  
• Obtener atributos.  Permite consultar los atributos del fichero como fechas de creación y 
modificación, el propietario o tamaño.  
• Establecer atributos.  Algunos atributos de los archivos pueden modificarse. Los permisos 
de acceso suelen gestionarse mediante mecanismos específicos del sistema operativo, 
aunque en algunos entornos se presentan como atributos a nivel de usuario.  
• Comparación.  Permite comparar dos ficheros para determinar si son copias exactas.
 
• Concatenar.  Genera un nuevo fichero que es la unión de dos o más ficheros.  
• Renombrar. Cambia el nombre del fichero.  
 
 
 
 
 
+ Info 
Estas operaciones dependen del sistema operativo.  
Aunque los lenguajes de programación pueden ofrecer funciones 
para realizarlas, normalmente se implementan mediante llamadas 
al sistema. 
 
 
• Operaciones con registros:  estas operaciones no son propias del sistema operativo, sino de 
aplicaciones que interpretan el contenido del fichero como una colección de registros. Solo 
tienen sentido en ficheros de datos organizados en registros. Para realizarlas, el fichero debe 
abrirse previamente y cerrarse al finalizar.  
• Leer registros.  Se leen datos del archivo de la posición actual. Los datos se almacenan 
normalmente en un buffer temporal.  
(Buffer de datos: espacio de memoria reservado para el almacenamiento temporal de 
información mientras se procesa).  
• Escribir registros.  Se escriben datos en el archivo en la posición actual. Puede añadirse 
como datos nuevos o sobrescribir los datos existentes.  

<!-- Page 50 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
50 
• Búsqueda. Permite localizar uno o varios registros que cumplen una determinada 
condición. Es una operación propia de la aplicación, que se realiza sobre ficheros de datos 
organizados en registros.  
3.6. De los sectores a los bloques  
Para comprender el funcionamiento de los sistemas de ficheros es necesario partir del nivel físico del 
almacenamiento y analizar las sucesivas abstracciones que introduce el sistema operativo hasta ofrecer 
a las aplicaciones una visión lógica y uniforme.  
Dispositivos de almacenamiento persistente  
Los dispositivos de almacenamiento persistente, como discos duros, unidades SSD o memorias flash, 
gestionan la información mediante sectores físicos, que constituyen la unidad mínima real de lectura y 
escritura del dispositivo. Estos sectores son gestionados directamente por el firmware del dispositivo, 
que expone el almacenamiento como una secuencia lineal de posiciones numeradas. En este nivel no 
existe ningún conocimiento de ficheros, directorios ni estructuras lógicas.
 
Para facilitar el acceso a los sectores físicos, los dispositivos modernos utilizan el direccionamiento lineal 
de sectores (LBA, Logical Block Addressing), mediante el cual cada sector se identifica por un número 
lógico. Este mecanismo pertenece al ámbito del dispositivo y su firmware, y no debe confundirse con las 
abstracciones que introduce posteriormente el sistema operativo.
 
Capa de Bloques  
El sistema operativo no trabaja directamente con sectores físicos. Sobre ellos construye una primera 
abstracción lógica: los bloques lógicos, que son la unidad básica de trabajo de la capa de bloques del 
sistema operativo. Un bloque lógico puede coincidir con un sector físico o agrupar varios sectores, 
dependiendo del sistema y de la configuración. Esta capa se encarga de traducir las operaciones 
solicitadas por el sistema de ficheros en accesos reales a los sectores del dispositivo, gestionando 
además la bufferización y el caching de las operaciones de E/S.
 
Sistema de Ficheros  
Sobre esta capa se sitúa el sistema de ficheros, que introduce una nueva unidad de asignación de 
espacio: el cluster. El cluster es la unidad mínima que el sistema de ficheros asigna a un fichero y puede 
estar compuesto por uno o varios bloques lógicos. En algunos sistemas esta unidad recibe también el 
nombre de bloque del sistema de ficheros, lo que puede dar lugar a ambigüedad terminológica; por este 
motivo, se utiliza el término cluster para diferenciarla claramente de los bloques lógicos del sistema 
operativo. 
La existencia de estas sucesivas abstracciones permite separar la organización física del 
almacenamiento de la organización lógica de los datos. Gracias a ello, los datos de un fichero no 
necesitan almacenarse de forma contigua en el dispositivo, y el sistema operativo puede ofrecer a las 

<!-- Page 51 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
51 
aplicaciones una visión uniforme del almacenamiento, independiente del tipo de dispositivo utilizado y 
de su disposición física real.  
Este proceso de abstracción es la base sobre la que se construye la implementación interna del sistema 
de ficheros y los mecanismos que permiten localizar, gestionar y acceder a la información almacenada 
de forma eficiente y fiable.  
3.6.1. Dispositivos de almacenamiento y sectores físicos  
Los dispositivos de almacenamiento persistente son los encargados de conservar la información de 
forma permanente, incluso cuando el sistema se apaga. Entre ellos se encuentran los discos duros 
magnéticos, las unidades de estado sólido (SSD), las memorias flash y otros dispositivos similares.
 
Desde el punto de vista físico, estos dispositivos organizan la información en sectores, que constituyen 
la unidad mínima real de lectura y escritura que el dispositivo presenta al exterior. En discos duros 
magnéticos, el sector es efectivamente la unidad física de acceso. En SSDs y memorias flash, el sector 
constituye la unidad lógica mínima que el firmware presenta al sistema, pero internamente estas 
tecnologías gestionan páginas de mayor tamaño (típicamente 4 KB, 8 KB o 16 KB) mediante una capa 
de traducción (FTL). Tradicionalmente, el tamaño expuesto de un sector ha sido de 512 bytes, aunque 
en sistemas modernos es habitual encontrar sectores de 4 KB.  
La gestión de los sectores físicos no corresponde al sistema operativo, sino al firmware del propio 
dispositivo. Este firmware se encarga de controlar el acceso al soporte físico y de exponer el 
almacenamiento como una secuencia de sectores numerados que el sistema operativo puede 
direccionar. En este nivel no existe ningún concepto de fichero, directorio, bloque lógico ni offset; 
únicamente se trabaja con posiciones físicas del dispositivo.  
Los sectores físicos constituyen, por tanto, el nivel más bajo de la jerarquía de almacenamiento sobre el 
que se construyen todas las abstracciones superiores que permiten la gestión de ficheros en un sistema 
informático.  
3.6.2. Direccionamiento lineal de sectores (LBA)
 
El direccionamiento lineal de sectores, conocido como LBA (Logical Block Addressing), es el mecanismo 
estándar mediante el cual los dispositivos de almacenamiento exponen sus sectores al sistema 
operativo de forma secuencial y numérica.  
En los sistemas antiguos, el acceso se realizaba mediante direccionamiento físico basado en cilindros, 
cabezas y sectores (CHS). Este método dependía de la geometría interna del dispositivo, lo que lo hacía 
complejo y poco flexible. El direccionamiento LBA sustituye este esquema por una numeración lineal 
continua que oculta la organización física real del dispositivo.  
Mediante LBA, cada sector se identifica por un número entero consecutivo (dirección lógica). El 
sistema operativo utiliza estas direcciones para solicitar operaciones de lectura o escritura, y el 
firmware del dispositivo traduce internamente estas direcciones lógicas a la localización física 
correspondiente. Esto libera al sistema operativo de conocer la estructura interna o la tecnología 
específica del dispositivo.  

<!-- Page 52 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
52 
Es importante destacar que, aunque el término "logica" forma parte de su nombre, el direccionamiento 
LBA no define bloques lógicos del sistema operativo. LBA se refiere a sectores del dispositivo, 
simplemente numerados linealmente; los bloques lógicos se definen en una capa superior y constituyen 
una abstracción diferente.  
El uso de LBA facilita la compatibilidad entre dispositivos, permite gestionar discos de gran capacidad y 
simplifica el diseño de los sistemas operativos al ofrecer una interfaz uniforme de acceso al 
almacenamiento físico.  
3.6.3. Bloques lógicos del sistema operativo  
El sistema operativo gestiona el almacenamiento introduciendo una abstracción propia sobre los 
sectores físicos direccionables vía LBA: los bloques lógicos (o bloques del kernel).
 
Un bloque lógico es la unidad mínima de transferencia gestionada por la capa de E/S del sistema 
operativo. Su tamaño viene determinado por el kernel y típicamente coincide con la de un sector físico 
o representa un múltiplo de esta (por ejemplo, 1 KB, 2 KB o 4 KB). Esta agrupación permite optimizar 
las operaciones de entrada/salida y gestionar eficientemente la caché del sistema.
 
La capa de bloques actúa como intermediaria entre el sistema de ficheros y el hardware. Cuando recibe 
peticiones de lectura o escritura relativas a bloques lógicos específicos, calcula los correspondientes 
números de sector LBA y gestiona la transferencia efectiva de datos entre la memoria principal y el 
dispositivo de almacenamiento.  
En este nivel no existe conocimiento alguno sobre ficheros, directorios o significado de los datos. Para la 
capa de bloques, el almacenamiento es simplemente una secuencia numerada de unidades de tamaño 
fijo, independientemente de su contenido.  
Además de la correspondencia matemática entre bloques lógicos y sectores físicos (accesibles vía LBA), 
esta capa se encarga de la planificación de operaciones de E/S, la gestión de colas, la utilización de 
caché y la optimización del acceso, todo ello de forma transparente para los niveles superiores.
 
Los bloques lógicos constituyen, por tanto, el punto de enlace entre el sistema de ficheros y el 
almacenamiento físico, sirviendo de base para la organización lógica de la información que se realiza en 
niveles superiores. 
3.6.4. Clusters y fragmentación interna  
Sobre los bloques lógicos definidos por el sistema operativo se construye el sistema de ficheros, que 
introduce su propia unidad mínima de asignación de espacio: el cluster (también denominado unidad de 
asignación en algunos sistemas).  
El cluster es la unidad mínima que el sistema de ficheros asigna a un fichero. Un cluster está compuesto 
por uno o varios bloques lógicos contiguos, dependiendo del sistema de ficheros y de su configuración 
durante el formateo. En algunos sistemas esta unidad recibe también el nombre de bloque del sistema 
de ficheros, lo que puede generar confusión terminológica; por este motivo aquí utilizamos el término 
cluster para diferenciarla claramente de los bloques lógicos del sistema operativo.
 

<!-- Page 53 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
53 
Cuando un fichero se crea o se amplía, el sistema de ficheros le asigna espacio en forma de clusters 
completos. Esto implica que un fichero, independientemente de su tamaño real (incluso si es de un solo 
byte), ocupa siempre un número entero de clusters. El espacio no utilizado dentro de los clusters 
asignados -particularmente el sobrante del último cluster - constituye la fragmentación interna.  
Cuanto mayor sea el tamaño del cluster, mayor será el desperdicio potencial de espacio por fichero 
(hasta un máximo teórico de tamaño_cluster - 1 byte por fichero), aunque a cambio se reduce la 
sobrecarga en la gestión de metadatos y se mejora el rendimiento en operaciones secuenciales.
 
Los clusters pertenecen exclusivamente al ámbito del sistema de ficheros y no deben confundirse con 
los bloques lógicos del sistema operativo ni con los sectores físicos del dispositivo. Cada uno de estos 
conceptos corresponde a una capa distinta dentro de la jerarquía de almacenamiento.
 
El uso de clusters permite al sistema de ficheros gestionar grandes volúmenes de almacenamiento con 
menor sobrecarga administrativa (menos unidades que gestionar que si se trabajara directamente con 
bloques lógicos), sirviendo de base para la organización lógica de la información que se realiza en 
niveles superiores. 
3.7. Implementación interna del sistema de ficheros  
Una vez establecidas las unidades y abstracciones básicas del almacenamiento, el sistema de ficheros 
debe resolver el problema fundamental de cómo asignar espacio a los ficheros, localizar sus datos 
dispersos y mantener la coherencia del sistema ante operaciones y posibles fallos.
 
La implementación interna gestiona el almacenamiento sobre un soporte que no garantiza contigüidad 
física. Para ello, utiliza estrategias de asignación de bloques, estructuras de control y metadatos que 
establecen la correspondencia entre los ficheros lógicos y los bloques físicos que los componen.
 
El sistema debe ser capaz de: asignar nuevos bloques cuando un fichero crece; liberar bloques cuando se 
elimina o reduce; y localizar rápidamente todos los bloques pertenecientes a un fichero para reconstruir 
su contenido en el orden lógico correcto.  
Además, mantiene información descriptiva -los metadatos - sobre las características de cada fichero y 
del sistema. Estos metadatos garantizan la integridad de la información, gestionan permisos, permiten 
detectar inconsistencias y facilitan la recuperación.  
Toda esta complejidad permanece oculta a las aplicaciones. Desde el exterior, un fichero se presenta 
como una secuencia lógica continua, independientemente de que internamente esté almacenado en 
bloques físicamente dispersos y gestionado mediante estructuras complejas.
 
En los siguientes subepígrafes se analizan las estrategias de asignación de bloques, los mecanismos de 
gestión del espacio libre y las técnicas para mantener la consistencia del sistema.
 

<!-- Page 54 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
54 
3.7.1. Estrategias de asignación de bloques  
El sistema de ficheros debe decidir cómo distribuir los clusters de un fichero dentro del dispositivo. Esta 
decisión determina si los datos deben ocupar posiciones físicas consecutivas o pueden dispersarse, 
afectando directamente al rendimiento, la capacidad de crecimiento dinámico y la complejidad de 
localización.  
Existen tres estrategias clásicas -contigua, enlazada e indexada - que representan modelos conceptuales 
distintos para organizar los bloques en el almacenamiento. Cada una implica compromisos entre 
simplicidad de implementación, velocidad de acceso, eficiencia del espacio y robustez ante la 
fragmentación externa.  
Estos mecanismos pertenecen a la implementación interna del sistema de ficheros, no al nivel de 
aplicación. Su elección condiciona: la rapidez para localizar bloques, la posibilidad de ampliar un fichero 
sin moverlo físicamente, y el rendimiento de los accesos secuenciales frente a los directos.
 
A continuación se analizan estas estrategias y sus implementaciones representativas en sistemas de 
ficheros reales. 
3.7.1.1. Asignación contigua  
En la asignación contigua, los clusters de un fichero se almacenan en posiciones consecutivas del 
dispositivo. El sistema de ficheros reserva, en el momento de la creación, un área continua suficiente 
para el tamaño declarado o estimado del fichero.  
Esta estrategia ofrece rendimiento óptimo en accesos secuenciales y directos, ya que basta conocer la 
dirección del primer cluster y el desplazamiento para localizar cualquier dato sin indirecciones 
adicionales. 
Su principal limitación es la fragmentación externa del espacio libre: el tiempo de uso del disco divide el 
espacio disponible en pequeños fragmentos no contiguos, dificultando encontrar áreas amplias para 
nuevos ficheros. Además, el crecimiento dinámico resulta problemático cuando no existe espacio libre 
adyacente inmediato, obligando a reubicar el fichero completo.  
Por estos motivos, su uso se restringe hoy a contextos específicos (ficheros de tamaño fijo, sistemas de 
archivo en CD -ROM, o particiones con gestión muy controlada).
 
3.7.1.2. Asignación enlazada (ejemplo: tablas FAT)
 
En la asignación enlazada, los clusters de un fichero pueden estar dispersos por el dispositivo. Cada 
cluster de datos contiene, junto con la información del usuario, un puntero o referencia al siguiente 
cluster de la cadena, formando una lista enlazada.  
Esta estrategia elimina la fragmentación externa (cualquier cluster libre sirve) y facilita el crecimiento 
ilimitado del fichero mientras exista espacio disperso. Sin embargo, el acceso directo es ineficiente 
(requiere recorrer la cadena desde el inicio) y la corrupción de un enlace rompe la cadena, pudiendo 
provocar la pérdida de los clusters subsiguientes.  

<!-- Page 55 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
55 
El sistema FAT (File Allocation Table) representa una implementación optimizada donde los punteros 
se centralizan en una tabla en memoria (o caché de disco) en lugar de dispersarse en los propios 
bloques de datos, acelerando la navegación pero manteniendo la lógica enlazada.
 
3.7.1.3. Asignación indexada (ejemplo: i -nodos)  
La asignación indexada utiliza una estructura intermedia -el bloque índice- que almacena las direcciones 
de todos los clusters que componen el fichero. Los clusters de datos pueden estar físicamente 
dispersos, pero se localizan consultando directamente la entrada correspondiente del índice.
 
Permite acceso directo eficiente (tiempo constante tras obtener el índice) y crecimiento dinámico 
(ampliando el índice). Como contrapartida, consume espacio adicional para la estructura de índice y 
requiere mecanismos de índices multinivel (simple, doble, triple indirección) cuando el fichero excede la 
capacidad de referencias directas de un solo bloque índice.  
El modelo de i-nodos en sistemas Unix/Linux constituye el ejemplo paradigmático, donde cada fichero 
dispone de un i-nodo con metadatos y una lista de direcciones de bloques que incluye referencias 
directas e indirectas.  
3.7.2. Gestión del espacio libre  
Además de asignar clusters a los ficheros existentes, el sistema de ficheros debe mantener información 
actualizada sobre qué clusters del dispositivo están libres y cuáles ocupados. Esta gestión es 
imprescindible para crear nuevos ficheros, ampliar los existentes y liberar espacio cuando se eliminan.
 
El sistema utiliza estructuras internas que permiten localizar rápidamente clusters disponibles. Entre los 
métodos más habituales se encuentran los mapas de bits y las listas de clusters libres
 
3.7.2.1. Mapas de bits 
En los mapas de bits, cada cluster del dispositivo se representa mediante un bit (típicamente 0=libre, 
1=ocupado). Esta estructura reside en el volumen (metadatos del sistema de ficheros) y se carga 
parcialmente en memoria según necesidad.  
Permite localizar clusters libres de forma eficiente y facilita la detección de zonas contiguas de espacio 
disponible, útil para minimizar la fragmentación. Su inconveniente es el tamaño fijo: requiere espacio en 
disco proporcional al número total de clusters (por ejemplo, 1 TB con clusters de 4 KB requiere 32 MB 
de mapa).  
3.7.2.2. Listas de bloques libres  
Este método enlaza entre sí los clusters disponibles: cada cluster libre contiene una referencia al 
siguiente cluster libre, formando una lista encadenada.  

<!-- Page 56 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
56 
Es sencillo de implementar y no requiere espacio adicional en disco (reutiliza los propios clusters libres 
para almacenar los punteros). Sin embargo, resulta ineficiente para localizar áreas contiguas grandes, 
ya que obliga a recorrer la lista secuencialmente, y fragmenta la información de gestión por todo el 
volumen. 
3.7.3. Metadatos y consistencia del sistema de ficheros  
Los metadatos describen las características de cada fichero y su ubicación en el almacenamiento: 
nombre (registrado en estructuras de directorio), tamaño, permisos, fechas de acceso/modificación y 
las referencias a los clusters que contienen los datos. En sistemas Unix/Linux residen principalmente en 
los i-nodos; en FAT, se distribuyen entre entradas de directorio y la tabla de asignación.
 
Estas estructuras garantizan la integridad del sistema. Cualquier operación sobre un fichero (creación, 
modificación, eliminación) implica actualizar tanto los datos como sus metadatos de forma coherente. 
Si una operación se interrumpe por un fallo de energía o error del sistema, los metadatos pueden 
quedar inconsistentes (por ejemplo, clusters marcados como ocupados sin fichero asociado, o registros 
que apuntan a clusters libres).  
Para mitigar este riesgo, los sistemas modernos emplean el registro por diario (journaling): antes de 
modificar los metadatos definitivamente, se escribe la operación pendiente en un área especial del 
volumen. Si ocurre un fallo, el sistema utiliza este registro para completar o deshacer la operación 
interrumpida, recuperando la consistencia sin necesidad de verificar todo el sistema de ficheros.
 
La correcta gestión de estos metadatos y la garantía de consistencia ante fallos son aspectos 
fundamentales para la fiabilidad del almacenamiento y la recuperación segura de la información.
 
3.8. Abstracción del fichero y métodos de acceso (so / 
aplicación)  
El sistema de ficheros proporciona a las aplicaciones una abstracción lógica del almacenamiento, 
presentando cada fichero como una secuencia continua de bytes numerados desde el inicio hasta su 
tamaño actual.  
Toda operación de lectura o escritura se define, de forma implícita o explícita, mediante una posición de 
referencia dentro del fichero (habitualmente el inicio), un desplazamiento u offset respecto a dicha 
referencia y un número de bytes a operar.  
El offset es un valor entero que representa la distancia, en bytes, desde la posición de referencia 
mencionada en el párrafo anterior hasta la posición lógica a partir de la cual se realizará la operación de 
lectura o escritura. Este valor pertenece al ámbito lógico del fichero y no guarda relación directa con la 
ubicación física de los datos en el dispositivo.  
Estos parámetros determinan el rango lógico de datos sobre el que se realizará la operación. El sistema 
de ficheros utiliza esta información para localizar los clusters físicos correspondientes y efectuar la 
transferencia, ocultando completamente la disposición real de los datos en el dispositivo.
 

<!-- Page 57 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
57 
Cada fichero abierto tiene asociado, en una estructura del kernel, un puntero de posición que almacena 
el offset lógico actual. Este offset existe siempre y es utilizado por el sistema de ficheros como punto de 
partida para cualquier operación de entrada o salida.  
3.8.1. El fichero como secuencia lógica de bytes  
Desde la perspectiva de la aplicación, un fichero es una secuencia ordenada de bytes numerados desde 
0 hasta N -1, donde N representa su tamaño actual. Esta representación es independiente de la 
distribución física: los datos pueden estar dispersos en clusters no contiguos del dispositivo sin que la 
aplicación perciba discontinuidad alguna.  
La interfaz del sistema operativo oculta los detalles de almacenamiento. La aplicación realiza 
operaciones de lectura/escritura especificando un offset (o no) y una cantidad de bytes, sin necesidad 
de conocer en qué cluster específico reside esa información ni si estos son contiguos físicamente.
 
El sistema de ficheros mantiene internamente la correspondencia entre cada rango de bytes lógicos y 
sus clusters físicos mediante las estructuras de asignación estudiadas (contigua, enlazada o indexada). 
Esta traducción es transparente: la aplicación percibe únicamente un flujo continuo de datos.
 
Esta abstracción sirve de base para las distintas formas de utilización del fichero por parte de las 
aplicaciones, todas ellas fundamentadas en el manejo de posiciones lógicas dentro de la secuencia de 
bytes. 
3.8.2. Acceso secuencial  
La literatura clásica denomina acceso secuencial al acceso en el que la aplicación no solicita 
explícitamente cambios en el offset. Tras cada operación de lectura o escritura, el propio sistema 
operativo actualiza automáticamente el puntero de posición, avanzándolo en función del número de 
bytes procesados.  
3.8.3. Acceso directo por desplazamiento (offset)
 
Los mismos manuales, denominan acceso directo al acceso en el que la aplicación solicita 
explícitamente la actualización del offset lógico antes de realizar una operación, indicando una nueva 
posición dentro del fichero desde la que continuar el acceso. Esta solicitud no altera el mecanismo 
interno del sistema de ficheros, sino únicamente el valor del offset utilizado como referencia.
 
3.8.4. Traducción del offset lógico a bloques físicos  
Como decíamos el offset puede ser gestionado implícitamente por el sistema operativo o modificado 
explícitamente por la aplicación, pero en todos los casos es utilizado por el sistema de ficheros para 
localizar los datos solicitados.  

<!-- Page 58 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
58 
El sistema de ficheros debe resolver la correspondencia entre ese offset lógico y la ubicación física real 
de los datos en el dispositivo de almacenamiento. Para ello, el proceso de traducción sigue la jerarquía 
de abstracciones establecida:  
• En primer lugar, se calcula el número de cluster lógico que contiene el byte correspondiente al 
offset, dividiendo dicho offset por el tamaño del cluster, y se determina el desplazamiento 
relativo dentro de ese cluster.  
• A continuación, mediante las estructuras internas del sistema de ficheros 
-como tablas FAT, i -
nodos o bloques índice, según la estrategia de asignación utilizada
- se traduce el cluster lógico a 
su localización física real dentro del volumen.  
• Posteriormente, el cluster físico se descompone en los bloques lógicos gestionados por la capa 
de entrada/salida del sistema operativo, recordando que un cluster puede agrupar uno o varios 
bloques lógicos contiguos.  
• Finalmente, la capa de bloques traduce estos bloques lógicos a direcciones LBA de sectores 
físicos, que el firmware del dispositivo convierte en operaciones reales de lectura o escritura 
sobre el medio. 
Todo este mecanismo es completamente transparente para la aplicación. Desde su perspectiva, el 
fichero se presenta como una secuencia continua de bytes accesible mediante operaciones de lectura y 
escritura, mientras que el sistema de ficheros se encarga de ocultar la fragmentación física y reconstruir 
el flujo lógico de datos de forma coherente.  
3.9. Organización lógica del contenido (nivel aplicación)
 
Tras la abstracción del sistema operativo -que presenta el fichero como una mera secuencia de bytes 
accesibles por offset, corresponde a la aplicación interpretar y estructurar esos datos.
 
Esta organización lógica es responsabilidad exclusiva del software aplicativo. El SO proporciona 
mecanismos de lectura/escritura de bytes; la aplicación decide si esos bytes representan texto plano, 
registros de longitud fija o estructuras complejas. El sistema desconoce el significado semántico del 
contenido: unos bytes pueden ser caracteres ASCII para un programa o códigos de cliente para otro.
 
La organización elegida determina las operaciones posibles (búsqueda secuencial, acceso relativo por 
número de registro, indexación simple), pero no altera la gestión física de clusters realizada por el 
kernel. 
A continuación se analizan las organizaciones lógicas implementadas directamente por aplicaciones 
-sin 
utilizar sistemas gestores de bases de datos, diferenciándolas claramente de las estructuras propias de 
los SGBD anteriormente.  

<!-- Page 59 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
59 
3.9.1. Ficheros secuenciales y secuenciales ordenados  
En el nivel de aplicación, la organización más elemental interpreta el fichero como una secuencia de 
datos procesados en orden de escritura. Esta estructura define los ficheros secuenciales, utilizados en 
logs, ficheros de texto o exportaciones simples.  
En un fichero secuencial puro , los datos se almacenan uno tras otro según llegan, sin ordenación 
implícita más allá de la cronología de inserción. La aplicación accede al contenido mediante lecturas 
secuenciales desde el inicio, siendo este modelo adecuado cuando se procesan todos los datos o las 
búsquedas son esporádicas.  
El fichero secuencial ordenado  mantiene los registros ordenados lógicamente según un campo clave 
(por ejemplo, código de cliente o fecha). Este orden es puramente semántico: el sistema de ficheros 
gestiona los clusters físicos sin conocer la secuencia lógica; es responsabilidad de la aplicación 
garantizar que las escrituras respeten el criterio de ordenación, típicamente reescribiendo secciones del 
fichero o generando copias ordenadas.  
La ventaja de la ordenación  es permitir búsquedas más eficientes (por ejemplo, mediante búsqueda 
binaria si el fichero cabe en memoria o mediante recorridos parciales) frente al acceso puramente 
secuencial. Sin embargo, el coste de inserciones y eliminaciones aumenta considerablemente, ya que 
mantener el orden puede requerir desplazar registros existentes o reconstruir el fichero completo.
 
Desde el punto de vista operativo, los ficheros secuenciales no ordenados presentan inserciones simples 
y rápidas, al añadirse los datos al final del fichero, pero requieren recorridos completos para localizar un 
elemento concreto. En cambio, los ficheros secuenciales ordenados permiten búsquedas más eficientes 
sobre el campo de ordenación, a costa de penalizar las inserciones y eliminaciones, que pueden requerir 
desplazamientos de registros o reorganización periódica del fichero.
 
En ambos casos, el sistema operativo ignora la organización lógica. La interpretación de los bytes como 
registros ordenados o no es una construcción exclusiva del software aplicativo que gestiona el 
contenido.  
En ficheros multimedia como imágenes, audio o vídeo, la organización lógica del contenido es 
igualmente secuencial, ya que los datos se interpretan como una secuencia de bytes definida por el 
formato. No obstante, las aplicaciones que los gestionan suelen emplear acceso directo por 
desplazamiento para localizar y modificar partes concretas del fichero (por ejemplo, una zona de 
píxeles o un fragmento de audio) sin necesidad de procesarlo completamente desde el inicio.
 
Ficheros secuencial encadenados  
En el caso de ficheros de registros, la aplicación puede definir organizaciones lógicas adicionales. Una de 
ellas es la organización secuencial encadenada, en la que los registros mantienen un orden lógico 
mediante punteros entre ellos, independientemente de su ubicación física.  
La principal ventaja de esta técnica es la flexibilidad en inserciones y eliminaciones, ya que basta con 
ajustar los punteros sin necesidad de desplazar grandes volúmenes de datos. Como contrapartida, el 
acceso secuencial requiere seguir los enlaces uno a uno, y el acceso directo por posición lógica resulta 
ineficiente o inexistente.  

<!-- Page 60 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
60 
El sistema operativo es ajeno a esta organización: para él, el fichero sigue siendo una secuencia de 
bytes. La estructura encadenada es una convención mantenida exclusivamente por la lógica de la 
aplicación. 
3.9.2. Ficheros de registros de longitud fija  
En muchas aplicaciones, el contenido del fichero se estructura como una colección de registros 
(entidades con campos definidos) en lugar de un flujo de bytes amorfo. Cuando todos los registros 
comparten el mismo tamaño en bytes, se denomina organización de registros de longitud fija.
 
Cada registro ocupa R bytes, distribuidos en campos con posiciones y longitudes predefinidas (por 
ejemplo: bytes 0 -9 para el código, 10 -49 para el nombre, 50 -53 para el salario).  
Esta regularidad permite calcular la posición lógica de cualquier registro mediante aritmética simple, a 
partir de su número de orden: offset = n × R, donde n es el número de registro, comenzando 
típicamente en 0.  
Esta organización habilita el acceso relativo por número de registro (o acceso directo relativo), que 
permite a la aplicación acceder a un registro concreto sin recorrer los anteriores, posicionando el 
puntero del fichero en el offset correspondiente. El sistema operativo traduce dicho offset a los clusters 
físicos necesarios, sin que la aplicación intervenga en la gestión de la dispersión física.
 
Este acceso es eficiente y de tiempo constante respecto al tamaño del fichero, pero solo es aplicable 
cuando la longitud de los registros es constante. En ficheros con registros de longitud variable, el 
cálculo directo de la posición resulta imposible sin el uso de estructuras auxiliares, como tablas de 
índices. 
El sistema operativo ignora la estructura interna. Desde su perspectiva, el fichero es una secuencia de 
bytes. La segmentación en registros y su interpretación semántica son convenciones gestionadas 
exclusivamente por la aplicación. Esta organización es característica de aplicaciones COBOL clásicas, 
ficheros binarios con formatos rígidos y sistemas embebidos que requieren acceso predecible.
 
Es importante distinguir este acceso relativo por número de registro, basado en la posición física 
calculable dentro del fichero, de los mecanismos de acceso por clave o índices utilizados por los SGBD, 
donde el orden físico de los registros carece de significado semántico.
 
 
 
 

<!-- Page 61 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
61 
 
Nota 
La organización de longitud fija presenta el inconveniente del 
desperdicio de espacio cuando los datos varían en tamaño 
(campos parcialmente vacíos) y complica la gestión de registros 
eliminados, que suele resolverse mediante marcas de borrado o 
reorganizaciones periódicas del fichero.  
 
 
3.9.3. Índices simples gestionados por la aplicación  
Cuando los ficheros grandes impiden el recorrido secuencial eficiente, la aplicación puede implementar 
índices simples: estructuras auxiliares que asocian valores clave con posiciones de acceso directo 
(offsets o números de registro). Estos índices son responsabilidad exclusiva del software, no del sistema 
operativo ni de un SGBD.  
Un índice simple típico consiste en una tabla (frecuentemente cargada en memoria) donde cada 
entrada contiene un par (clave, dirección). Por ejemplo, para localizar el registro de un cliente por su 
DNI, el índice contiene el DNI como clave y el número de registro donde reside la ficha completa.
 
La aplicación debe garantizar la coherencia entre índice y datos: toda inserción, borrado o modificación 
requiere actualizar simultáneamente ambas estructuras. La corrupción del índice (por cierre inesperado 
o error lógico) deja el sistema inconsistente, sin mecanismos automáticos de recuperación.
 
Esta técnica mejora el rendimiento de búsquedas puntuales, pero presenta limitaciones: no soportan 
eficientemente rangos de búsqueda; requieren reorganización manual ante modificaciones extensivas; 
y carecen de optimizaciones de consulta, integridad referencial o gestión concurrente propias de los 
SGBD.  
Por estas razones, los índices simples se reservan para aplicaciones autocontenidas o sistemas legacy; 
para requisitos complejos se recurre a los mecanismos de organización secundaria de los SGBD vistos 
anteriormente.  
3.10. Organización de ficheros en sgbd  
Cuando los volúmenes de datos crecen y se exige flexibilidad en el acceso, integridad referencial y 
gestión concurrente, los mecanismos de ficheros planos resultan insuficientes. En su lugar, el Sistema 
Gestor de Bases de Datos (SGBD) asume el control total de la organización física y lógica de los datos.
 
El SGBD se apoya en el sistema de ficheros del SO (almacenando su información en uno o varios 
ficheros de clusters), pero define una capa de abstracción superior: la información se estructura 
internamente en páginas de datos (típicamente de 4 KB, 8 KB o 16 KB, múltiplos del tamaño de cluster 

<!-- Page 62 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
62 
del SO). Dentro de estas páginas, el gestor organiza los registros y los metadatos necesarios para su 
administración.  
Esta arquitectura permite al SGBD ofrecer servicios inalcanzables para una aplicación de ficheros 
tradicional: 
• Acceso mediante múltiples claves y criterios complejos,  
• Optimización automática de consultas,  
• Garantías de integridad y coherencia transaccional (ACID),
 
• Control de concurrencia y recuperación ante fallos.  
A continuación se analizan las estrategias de organización primaria (cómo se disponen físicamente los 
registros dentro de las páginas: montículo, secuencial o hash) y organización secundaria (estructuras 
auxiliares como índices para acceso alternativo).  
3.10.1. Ficheros de registros y páginas de datos  
En los SGBD, la unidad lógica es el registro (fila de una tabla), pero la unidad física de entrada/salida es 
la página de datos: un conjunto contiguo de bytes que el gestor transfiere como bloque entre 
almacenamiento secundario y memoria principal. El tamaño de página (típicamente 4 KB, 8 KB o 16 KB) 
es determinado por el SGBD y suele coincidir con múltiplos del tamaño de bloque del sistema de 
ficheros subyacente.  
Los ficheros de registros son, por tanto, colecciones de estas páginas. Dentro de cada una, el SGBD 
organiza los registros, gestiona el espacio libre mediante directorios internos de ranuras (slot 
directories) y mantiene los metadatos necesarios para localizar registros cuando la base de datos los 
solicita. 
El sistema operativo desconoce semánticamente estas estructuras: para él, el fichero de datos del SGBD 
es solo una secuencia de clusters (bytes). Es el motor del SGBD quien interpreta esos clusters como 
páginas con contenido estructurado, aplicando técnicas de gestión propias (control de concurrencia a 
nivel de página, buffering, etc.).  
Esta separación permite al SGBD optimizar el acceso independientemente del sistema de ficheros 
concreto (NTFS, ext4, etc.), garantizando rendimiento y portabilidad.
 
3.10.2. Organización primaria  
La organización primaria define cómo el SGBD distribuye físicamente los registros dentro de las páginas 
de un fichero de datos, determinando así su ubicación inicial en el almacenamiento y el método básico 
de recuperación.  

<!-- Page 63 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
63 
Esta decisión del diseñador o del motor del SGBD condiciona el rendimiento de operaciones 
fundamentales: inserción, búsqueda exacta, rangos de consulta y eliminación. A diferencia de los 
ficheros planos, aquí el gestor controla internamente la disposición física, no la aplicación.
 
Las tres estrategias principales son:  
• Montículo (heap): Registros almacenados sin orden implícito, típicamente en el siguiente 
espacio libre disponible.  
• Secuencial ordenada: Registros físicamente ordenados según el valor de una clave, facilitando 
búsquedas por rango.  
• Dispersión (hashing): Registros ubicados mediante función hash sobre una clave, optimizando 
búsquedas exactas.  
Cada estrategia implica compromisos distintos entre velocidad de inserción, eficiencia de consulta y 
consumo de espacio. Cuando la organización primaria resulta ineficiente para ciertos patrones de 
acceso, el SGBD recurre a estructuras adicionales: la organización secundaria o índices, que ofrecen 
rutas de acceso alternativas sin alterar la disposición física primaria de los registros.
 
3.10.2.1. Montículo (heap)  
En la organización heap, los registros se almacenan sin orden predefinido, típicamente en la próxima 
página con espacio libre disponible o en una nueva página añadida al final del fichero. Es la organización 
por defecto en la mayoría de los SGBD cuando no se especifica criterio de ordenación.
 
Esta estrategia maximiza la velocidad de inserción (no requiere reorganización física) y utiliza 
eficientemente el espacio de las páginas. Sin embargo, la recuperación de un registro específico sin 
índice requiere recorrido secuencial completo de todas las páginas (full table scan), siendo ineficiente 
para tablas grandes.  
Por ello, los montículos se emplean cuando:  
• Las inserciones son frecuentes y masivas (carga inicial de datos).
 
• El acceso predominante es a través de índices secundarios, no por rango de clave primaria.
 
• No existe requisito de orden físico.  
El SGBD gestiona internamente las páginas y sus ranuras libres; el sistema operativo solo percibe la 
asignación de clusters para contener esas páginas.  
3.10.2.2. Secuencial ordenada  
En la organización secuencial ordenada, los registros se almacenan físicamente ordenados según el 
valor de un campo clave (por ejemplo, código de cliente o fecha). Este orden es mantenido por el 
motor del SGBD, no por el sistema de ficheros: el SO desconoce el significado de los datos y gestiona 

<!-- Page 64 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
64 
únicamente clusters (bytes). El SGBD, por encima, interpreta esas páginas y aplica las políticas 
necesarias para preservar el orden lógico -físico de la estructura.  
Esta organización permite recorridos secuenciales por rango sin necesidad de ordenar los datos en 
tiempo de ejecución, lo que resulta eficiente para consultas ordenadas o búsquedas por intervalos. 
Conceptualmente, se corresponde con los ficheros ordenados estudiados en la organización clásica de 
ficheros y sirve de base para la definición de índices primarios en dicha terminología.
 
El principal coste de esta organización reside en las operaciones de mantenimiento: las inserciones y 
eliminaciones pueden requerir desplazar registros existentes o reconstruir parcial o totalmente el 
fichero para preservar el orden lógico, lo que penaliza el rendimiento cuando las actualizaciones son 
frecuentes. 
Es adecuada cuando predominan las lecturas secuenciales o por rango y las actualizaciones son poco 
frecuentes, ya que inserciones y eliminaciones pueden exigir reorganización. El sistema operativo 
permanece ajeno a esta organización: para él solo hay bytes; la ordenación la gestiona internamente el 
SGBD.  
3.10.2.3. Dispersión (hashing)  
En la organización por hashing, la ubicación de un registro se determina aplicando una función de 
dispersión sobre el valor de una clave específica. Esta función calcula una dirección lógica (número de 
bucket o página) donde el SGBD almacenará o buscará el registro.
 
El objetivo es proporcionar acceso directo de tiempo constante O(1) para búsquedas por igualdad 
sobre la clave de dispersión, típicamente en uno o dos accesos a páginas de datos.
 
Una búsqueda por igualdad  es aquella en la que se quiere localizar registros cuyo campo clave sea 
exactamente un valor concreto (por ejemplo, DNI = 12345678X). En este caso, el hashing es 
especialmente eficaz porque aplica la función de dispersión a ese valor y conduce directamente al 
bucket donde debería estar el registro. En cambio, para búsquedas por rango (por ejemplo, DNI entre A 
y B), el hashing no es adecuado porque la dispersión destruye el orden y obliga a recorrer múltiples 
buckets.  
Hashing estático  
El principal inconveniente de esta organización es la gestión de colisiones, que se producen cuando dos 
claves distintas generan la misma dirección lógica. En los esquemas más simples, el número de buckets 
es fijo y, cuando un bucket alcanza su capacidad, los registros adicionales deben almacenarse fuera de 
él. Esta situación da lugar al uso de estructuras de desbordamiento (overflow).
 
En el hashing con área de desbordamiento, cuando una página o bucket principal se llena, los nuevos 
registros se almacenan en una o varias páginas auxiliares de overflow, enlazadas mediante punteros 
desde el bucket original. De este modo, todos los registros asociados a una misma dirección hash 
pueden localizarse recorriendo dicha cadena de desbordamiento. Esta técnica es conceptualmente 
sencilla, pero presenta una degradación progresiva del rendimiento a medida que crecen las cadenas de 
overflow, ya que las búsquedas pueden requerir varios accesos adicionales al alamcenamiento 
persistente. 

<!-- Page 65 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
65 
Cuando las cadenas de desbordamiento crecen, el rendimiento se degrada progresivamente, pudiendo 
aproximarse al de un recorrido secuencial en el peor caso.  
Hashing dinámico  
Para mitigar este problema, se desarrollaron técnicas de hashing dinámico, cuyo objetivo es permitir el 
crecimiento controlado de la estructura sin necesidad de reorganizar completamente el fichero de 
datos. 
• En el hashing lineal , la estructura crece de forma incremental. Los buckets se dividen uno a uno 
siguiendo un puntero de división, utilizando progresivamente un mayor número de bits del valor 
hash. Este enfoque distribuye el coste de expansión a lo largo del tiempo y evita duplicaciones 
globales de la estructura, manteniendo un rendimiento estable incluso con inserciones 
continuas. 
• En el hashing extensible , el crecimiento se gestiona mediante un directorio que contiene 
referencias a los buckets. Este directorio utiliza un número variable de bits del valor hash y se 
duplica cuando es necesario. Cada bucket puede tener una profundidad local distinta, lo que 
permite dividir únicamente los buckets que lo requieren. Esta técnica reduce el número de 
accesos en búsquedas y ofrece un control más preciso del crecimiento, a costa de una mayor 
complejidad estructural.  
Todas estas variantes comparten el mismo principio básico: la localización directa de los registros 
mediante una función de dispersión. Las diferencias entre ellas radican exclusivamente en la forma de 
gestionar las colisiones y el crecimiento del espacio de almacenamiento.
 
El hashing es la organización idónea cuando predominan las búsquedas exactas por clave primaria o 
única y no se requieren recorridos ordenados ni consultas por rangos, ya que la función de dispersión 
destruye cualquier orden lógico de los registros.  
Como organización primaria, el hashing es implementado internamente por el SGBD sobre sus páginas 
lógicas, sin que el sistema operativo ni las aplicaciones de usuario intervengan en el cálculo de 
direcciones ni en la gestión de colisiones.  
 
 
 

<!-- Page 66 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
66 
 
Nota 
En estructuras de datos en memoria principal -como tablas hash 
implementadas mediante arrays, utilizadas en programación o en 
estructuras internas del sistema operativo - las colisiones pueden 
resolverse mediante técnicas de direccionamiento abierto, como el 
probing lineal, el probing cuadrático o el doble hashing. En el 
almacenamiento secundario y en los SGBD, la resolución de 
colisiones se basa preferentemente en páginas de desbordamiento 
y en técnicas de hashing dinámico.  
 
 
3.10.3. Organización secundaria  
La organización secundaria complementa a la primaria proporcionando acceso alternativo por campos 
distintos a la clave de ordenación física. Mientras la organización primaria determina la ubicación física 
del registro, la secundaria permite localizarlo rápidamente sin reordenar el fichero base.
 
3.10.3.1. Índices como acceso alternativo  
Un índice constituye una vía de acceso secundaria que complementa la organización primaria del 
fichero. Mientras la organización primaria (heap, ordenada o hash) determina la ubicación física de los 
registros, el índice ofrece rutas adicionales para localizarlos por otros campos.
 
Físicamente, es un conjunto de páginas propias (almacenadas en clusters del disco, separadas o dentro 
del mismo tablespace) que contienen entradas ordenadas del tipo (valor_campo, dirección_registro) 
-
donde la dirección especifica la página y posición exacta del registro en el fichero de datos. Esta 
ordenación permite búsquedas por igualdad o rango recorriendo únicamente el índice y accediendo 
selectivamente a las páginas de datos necesarias, evitando el escaneo completo de la tabla.
 
Pueden definirse sobre atributos clave o no clave, únicos o repetidos. Su existencia es transparente para 
la lógica de la aplicación (el optimizador de consultas decide automáticamente su uso), pero implica 
costes de mantenimiento: cada operación -inserción, modificación o eliminación - del lenguaje de 
manipulación de datos (DML) sobre la tabla debe replicarse sincrónicamente en el índice para 
garantizar la coherencia, aumentando el tiempo de respuesta y el consumo de E/S de dichas 
operaciones. 
3.10.3.2. Estructura General de un Índice  
Un índice es una estructura de datos (típicamente un árbol B+ en sistemas relacionales) que almacena 
entradas del tipo (valor_clave, dirección_registro), donde la dirección especifica la página y posición 
exacta del registro en el fichero de datos. Al consultar por el campo indexado, el SGBD recorre esta 

<!-- Page 67 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
67 
estructura auxiliar para obtener la dirección física directamente, evitando el recorrido secuencial 
completo del fichero de datos.  
3.10.3.3. Búsqueda en índices ordenados: busqueda binaria  
En los índices ordenados, las entradas se mantienen clasificadas según el valor del campo indexado. Esta 
propiedad permite realizar búsquedas eficientes mediante búsqueda binaria sobre el propio índice.
 
La búsqueda binaria  consiste en comparar la clave buscada con la entrada central del índice y, según el 
resultado, continuar únicamente por la mitad superior o inferior. Al repetir el proceso, el número de 
entradas candidatas se reduce exponencialmente. Por ello, si el índice ocupa b páginas, la búsqueda 
requiere aproximadamente log ₂(b) accesos a p áginas del índice. Una vez localizada la entrada, se utiliza 
su puntero para acceder a la p ágina de datos donde est á el registro.  
3.10.3.4. Densidad del índice  
Desde el punto de vista clásico, un índice denso contiene una entrada por cada registro del fichero de 
datos, mientras que un índice no denso contiene una entrada por cada bloque o página. Como 
consecuencia, los índices primarios son necesariamente no densos, mientras que los índices secundarios 
suelen ser densos para permitir la localización precisa de registros individuales.
 
Según su densidad, los índices pueden clasificarse en:  
• Índices densos , que contienen una entrada por cada registro del fichero de datos.  
• Índices no densos , que contienen una entrada por cada bloque o página del fichero de datos.  
Los índices densos proporcionan accesos más precisos, mientras que los no densos reducen el tamaño 
del índice a costa de requerir una lectura secuencial adicional dentro del bloque localizado.
 
3.10.3.5. Relación entre índice y organización primaria  
Atendiendo a la relación entre el índice y la organización primaria del fichero, se distinguen:
 
• Índice primario, se construye sobre el campo que determina el orden físico de los registros en el 
fichero de datos, normalmente una clave primaria. Dado que los registros están almacenados en 
el mismo orden que el índice, basta con una entrada por bloque o página del fichero, lo que hace 
que este índice sea necesariamente no denso.  
• Durante una búsqueda, el SGBD localiza en el índice el rango de valores correspondiente y 
accede directamente a la página de datos indicada, donde se encuentra el registro buscado o el 
conjunto reducido de registros candidatos.  
• Índice secundario , no determina la ubicación física de los registros, sino que proporciona una vía 
de acceso alternativa por un campo distinto del de ordenación. Dado que el campo indexado 

<!-- Page 68 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
68 
puede contener valores repetidos, una misma clave del índice secundario puede estar asociada a 
uno o varios registros del fichero de datos.  
• En la práctica, esto se implementa mediante entradas que contienen la clave secundaria y una o 
varias referencias a los registros correspondientes. Durante una búsqueda, el SGBD localiza 
primero la entrada del índice y, a continuación, accede a todos los registros asociados a ese 
valor. 
• Índice de agrupamiento , se construye sobre un campo no clave por el que los registros están 
físicamente ordenados, de modo que varios registros pueden compartir el mismo valor. El índice 
contiene una entrada por cada valor distinto del campo de agrupamiento, apuntando al primer 
bloque o página que contiene registros con dicho valor.  
• A partir de esa página inicial, el SGBD recorre secuencialmente las páginas contiguas que 
contienen los registros del grupo. Este tipo de índice es no denso y resulta adecuado para 
recuperar conjuntos completos de registros con un mismo valor, a costa de penalizar 
inserciones y eliminaciones.  
En un fichero de registros puede existir o bien un índice primario o bien un índice de agrupamiento, ya 
que ambos dependen del orden físico de los registros: el primario se construye sobre un campo clave 
con valores únicos y el de agrupamiento sobre un campo no clave con valores repetidos. En ambos 
casos pueden coexistir uno o varios índices secundarios, que no determinan el orden físico y se limitan a 
proporcionar accesos alternativos apuntando a las posiciones físicas definidas por la organización 
primaria. 
Estas categorías proceden de la organización clásica de ficheros y constituyen la base conceptual de los 
índices utilizados en los SGBD modernos.  
3.10.3.6. Gestión de índices en los SGBD  
A diferencia de los índices simples gestionados por aplicaciones, los índices del SGBD son:
 
• Automáticos: El gestor los mantiene consistentes ante inserciones, borrados y modificaciones 
sin intervención del programador.  
• Transaccionales: Sus actualizaciones forman parte de las transacciones ACID.
 
• Gestión interna: El optimizador de consultas decide automáticamente cuándo utilizarlos.
 
Permiten acelerar búsquedas por igualdad y rangos sobre campos no principales, pero implican coste de 
almacenamiento adicional (ocupan páginas propias sobre los clusters del disco) y de mantenimiento 
(actualizaciones sincrónicas con los datos).
 
El SGBD almacena estos índices en estructuras de páginas propias 
-físicamente dentro del mismo 
fichero de datos (tablespace) o en ficheros separados gestionados por el motor
- siendo transparente 
para el sistema operativo, que únicamente gestiona la asignación de clusters.
 

<!-- Page 69 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
69 
3.10.3.7. Índices multinivel y árboles B / B+  
En sistemas reales, los índices pueden ocupar múltiples páginas de almacenamiento, lo que hace 
ineficiente mantenerlos como una única estructura ordenada lineal. Para resolver este problema, los 
SGBD utilizan índices multinivel, en los que el índice se organiza jerárquicamente en varios niveles.
 
Conceptualmente, un índice multinivel es un índice construido sobre otro índice: los niveles superiores 
permiten descartar grandes rangos de claves con pocos accesos a disco, reduciendo progresivamente el 
espacio de búsqueda hasta localizar la página de datos correspondiente.  
En los SGBD modernos, estos índices multinivel se implementan mediante estructuras dinámicas 
equilibradas, principalmente árboles B y árboles B+.  
En un árbol B, los valores de búsqueda y los punteros a registros pueden aparecer en cualquier nodo del 
árbol. En un árbol B+, en cambio, todos los punteros a los registros de datos se encuentran 
exclusivamente en los nodos hoja, mientras que los nodos internos actúan únicamente como guía de 
búsqueda. 
La estructura B+ es la más utilizada en bases de datos relacionales, ya que permite recorridos eficientes 
por rango mediante el encadenamiento secuencial de las hojas, manteniendo el árbol equilibrado y 
garantizando un número reducido y predecible de accesos a disco.
 
3.11. Directorios  
Los directorios proporcionan un mecanismo que permita establecer una organización de los ficheros en 
el sistema, de forma que el usuario pueda encontrar y manejar los ficheros sin dificultad, puesto que un 
sistema de ficheros almacenado en un disco duro puede contener miles de ficheros.
 
Es un fichero especial que contiene información sobre otros ficheros y directorios, lo que hace es 
básicamente almacenar los nombres de otros ficheros (o directorios) y la posición que ocupan en el 
sistema de ficheros.  
Son índices que permiten localizar a otros ficheros o directorios, (aunque la percepción como usuarios 
es que los directorios como contenedores de ficheros o de otros directorios).
 
En Windows, cuando se especifica una ruta, cada directorio se separa mediante el carácter "
\", mientras 
que, en Linux, es el carácter "/".  
Los sistemas de archivos empleados en Windows y Linux, contienen en cada directorio, dos entradas 
especiales "." y "..", las cuales hacen referencia al propio directorio, y al padre, respectivamente.
 
Lo más común en los sistemas modernos es la organización en forma de árbol.
 

<!-- Page 70 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
70 
Operaciones con directorios  
Las operaciones comunes a la hora de manejar un directorio son:  
• Crear: se requiere nombre. Como normas, no puede llamarse igual que otro archivo ubicado en 
el mismo directorio. No debe incluir algunos caracteres especiales.  
• Ejecutar/desplazarse:  acceder al directorio (entrar)/recorrer el árbol de directorios.
 
• Copiar / Mover / Renombrar.  
• Eliminar: borrar un directorio y sus subdirectorios. Hay que prestar especial atención ya que la 
eliminación de un directorio supone la eliminación de todos los archivos contenidos en cada uno 
de los subdirectorios.  
Atributos de los directorios  
En cuanto a los atributos, también son similares a los archivos, y dependiendo del sistema de archivos 
empleado se tienen los siguientes:  
• H: oculto. 
• R: sólo lectura. 
• A: modificado. 
• Fecha: fecha de creación del directorio.  
• Hora: hora de creación del directorio.  
Algunos sistemas operativos como Linux utilizan también atributos para identificar la pertenencia del 
directorio a un usuario o grupo, así como los permisos correspondientes.
 
En Windows, sin embargo, al igual que ocurría con los archivos hay atributos que indican si el directorio 
está comprimido o cifrado.  
Las normas para nombrar los directorios coinciden con las correspondientes a los archivos.
 

<!-- Page 71 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
71 
 
Fuente 
https://wiki.vitalinux.educa.aragon.es/index.php/Curso_CPV_MIA/Ar
chivos 
Cuando el sistema de ficheros está organizado mediante un árbol de directorios, para especificar un 
fichero, no basta con indicar su nombre, también hay que indicar la posición que ocupa en el árbol de 
directorios, para que no haya ambigüedad posible.  
Hay dos mecanismos para indicar la posición que ocupa un fichero en el árbol de directorios.
 
• Sendas absolutas.  
Permiten especificar un archivo mediante la senda que hay que recorrer desde el directorio raíz 
hasta la posición que ocupa el archivo en el árbol.  
Para separar los directorios que integran la senda se utiliza un carácter de separación. En el caso 
de Windows, se utiliza el carácter " \". 
• Sendas relativas:  
Se define un directorio activo en el sistema. Entonces la senda que especifica un archivo es 
relativa a dicho directorio.  
Debe indicarse que las sendas relativas se diferencian claramente de las absolutas en que no 
empiezan con el nombre del directorio raíz, ("" en el caso de Windows).
 
4. Códecs  
Un códec es un programa que comprime y descomprime un archivo de audio o vídeo (codificador y 
decodificador), es el algoritmo, que decide cómo se comprimen los datos en el momento de guardarlos 
en una unidad de almacenamiento y cómo se descomprimen en el momento de su reproducción.
 
Este proceso conlleva que los archivos de audio y vídeo ocupen más o menos espacio de 
almacenamiento, y afecta también a la calidad de los mismos en la reproducción (se debe mantener una 
calidad óptima, o al menos suficiente).  

<!-- Page 72 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
72 
Son usados en videollamadas y emisiones en vivo para comprimir la señal antes de a la hora de 
transmitir por Internet y descomprimirla en los equipos de reproducción.
 
Cada códec comprime la información de una determinada manera que luego permitirá ofrecer mejor o 
peor calidad al realizar la reproducción. En la compresión, a mayor reducción del tamaño, el espacio de 
almacenamiento necesario es menor, por lo que lógicamente es mayor la rapidez de transmisión en la 
red o entre unidades de almacenamiento físicas.  
La pérdida de información no tiene por qué implicar pérdida de calidad en el mismo grado, por ello los 
mejores códecs son aquellos que limitan el tamaño de los archivos sin que se produzca una pérdida de 
calidad que sea percibida de forma notoria.  
No hay que confundir los términos códec y formato, el formato es la estructura donde se alberga toda 
la información para dar forma al archivo.  
4.1. Códec de audio  
En el caso de los códec de audio se pueden dividir entre sistemas con pérdidas o sin pérdidas.
 
• Las compresiones con pérdidas (lossy ). 
Se basan en la capacidad auditiva del ser humano. A la hora de comprimir un archivo de audio 
eliminan las frecuencias que el oído humano no puede percibir (inferiores a 20 Hz y superiores a 
20 KHz.  
También filtran la cantidad de ruido para ofrecer sólo lo que es perceptible para nosotros en 
cada rango de frecuencias. Suelen ser los más utilizados puesto que siguen ofreciendo una alta 
calidad de sonido ocupando mucho menos espacio (MP3, AAC, OGG Vorbis
). 
• Las compresiones sin perdidas (lossless ). 
El audio se comprime, pero al descomprimir recuperas exactamente los mismos datos que tenías 
al inicio. Ofrecen una mayor calidad de audio, y son por tanto las utilizadas en la edición de 
audio (FLAC, ALAC, WAV sin comprimir).
 
Dependiendo del servicio que se van a utilizar, se emplean mayores o menores niveles de reducción, por 
ejemplo, para transmisiones en vivo la compresión suele ser mayor, como por ejemplo en la telefonía, el 
podcasting, o las emisoras de radio por internet.  
Códec de audio más importantes  
• MP3: 
Usa un algoritmo con pérdida para conseguir un menor tamaño de archivo.
 

<!-- Page 73 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
73 
Es un formato de audio común, el códec por excelencia más popular, utilizado para música tanto 
en computadoras como en reproductores de audio portátil.  
Fue creado por ISO / IEC MPEG Audio Committe en 1993, y se considera el primer formato de 
audio comprimido popular mundialmente.  
Un MP3 creado usando una compresión de 128 kbit/s tendrá un tamaño de aproximadamente 
unas 11 veces menor que su homónimo en CD.  
Un MP3 puede comprimirse usando una mayor o menor tasa de bits por segundo (los KB por 
segundo que es capaz de reproducir), lo que afecta directamente a la calidad de audio como al 
tamaño del archivo resultante. Por ejemplo, creando un MP3 con una compresión de 128 kbit/s 
el archivo resultante tendrá un tamaño aproximado de unas 11 veces menor que su homónimo 
en CD.  
La limitación más conocida del MP3 es que no es multicanal.  
• WMA: 
Algoritmo diseñado por Microsoft, lanzado en 1999 para ser competencia de MP3, aunque con 
poco éxito.  
Puede realizar compresión con o sin perdida. El codificador Windows Media Audio puede 
reproducirse hasta en 8 canales en la versión Pro.  
• WAV: 
Fue desarrollado en 1991 conjuntamente por IBM y Microsoft, muy popular por ser en el 
comienzo de los archivos musicales, no admite compresión, por lo que ofrece gran calidad de 
sonido (comparable a la de un CD musical), pero ocupa demasiado tamaño, lo que hacía que su 
manipulación pudiera ser complicada en algunas ocasiones.  
Todos los efectos de sonido de Windows 95 venían codificados en WAV en archivos con 
formatos .WAV o .WAVE.  
• AIFF (Audio Interchange File Format):  
Desarrollado por Apple en 1998, no comprime la información y ofrece calidad de CD. (AIFF es 
para Mac como WAV es para Microsoft).  
Es muy cuando se necesite una alta calidad de reproducción, y al no estar comprimido puede 
tener las limitaciones típicas de transferencia de datos.  
La mayoría de los códec AIFF trabajan con el formato PCM, (es compatible con Windows).
 
• AAC (Advanced Audio Coding):  
Cuatro años después del lanzamiento del MP3, sus desarrolladores lanzaron el códec AAC, con 
una compresión mucho mayor, lo cual facilitaba la transmisión por la red con los anchos de 
banda limitados a 56 Kbps en esa época. Sin embargo, la calidad de audio esa poco aceptable.  

<!-- Page 74 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
74 
• FLAC (Free Lossless Audio Codec):
 
Codec de Audio Libre Sin Pérdidas, permite que el audio digital sea comprimido sin pérdidas de 
forma que el tamaño del archivo de audio se reduce sin que se pierda ningún tipo de 
información. El audio digital comprimido por el algoritmo de FLAC típicamente se puede reducir 
de 50 a 60% de su tamaño original,  y se descomprime en una copia id éntica de los datos de 
audio originales. Fue desarrollado por xiph.org Foundation en 2001.  
• OGG Vorbis:  
Desarrollado por xiph.org Foundation en 2000, de código abierto, comprime la información 
eliminando datos innecesarios de forma que facilita su transmisión, especialmente eficaz cuando 
se reproduce a través de dispositivos conectados por Bluetooth.
 
 
 
 
 
Info 
La transparencia auditiva definiría el punto en el que el audio 
comprimido se vuelve indistinguible del original (no comprimido) 
para la mayor parte de los oyentes. La eficiencia sería el equilibrio 
alcanzado entre calidad y compresión. MP3, OGG y AAC estarían 
ordenados en orden creciente, si los clasificáramos en términos de 
transparencia a una determinada tasa de transferencia de bits.  
 
 
4.2. Códec de vídeo  
El códec de vídeo es el programa que comprime la imagen con mayor o menor pérdida, siendo el 
responsable de la resolución que ofrece un vídeo al ser reproducido.  
Los archivos de vídeo también están comprimidos en el momento de editarlos y exportarlos en el 
formato elegido para que luego, cada reproductor o dispositivo, lo pueda descomprimir en la 
reproducción.  
Entre los años 1990 y 2000, fue de especial importancia la distribución de música por Internet, pero en 
las décadas siguientes, el vídeo se ha convertido en el formato rey del contenido audiovisual, por tanto, 
ha cobrado gran importancia el desarrollo de códec que ofrezcan altos niveles de compresión con 
calidades suficientes.  
 

<!-- Page 75 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
75 
 
 
 
 
Básico 
Los códec MPEG son muy utilizados desde la aparición de su 
primera versión, que ofrecía problemas a la hora de la 
reproducción al necesitar altos requisitos.  
MPEG-4 por el contrario también comprime el audio y la imagen 
ofreciendo una buena calidad de reproducción con un alto grado 
de compatibilidad.  
Actualmente, el H.264 o MPEG -4 AVC es el más popular por su 
elevado nivel de compresión con pérdidas mínimas de calidad, lo 
cual permite la transmisión de vídeo de manera fluida a una alta 
resolución. 
 
 
Códec de vídeo más importantes  
• MPEG-4: 
Este compresor de vídeo suele trabajar con el formato MP4 y es uno de los más populares ya 
que realiza una buena compresión sobre los formatos, ofreciendo una alta calidad en audio y 
resolución de imagen.  
Es similar al formato MOV de Quicktime pero ofrece mayores niveles de compresión que facilita 
la transmisión de datos en Internet.  
• DivX y Xvid:  
Estos formatos ofrecen una calidad muy alta, se utilizaban en la reproducción de películas en 
DVD.  
Los primeros DVD se editaron con DivX, que comprimía los datos para disponer de más 
contenido, solo se comprime el vídeo por lo que la calidad de audio es muy buena.  
DivX fue sustituido por el codificador Xvid, que se convirtió en uno de los sistemas preferidos 
por el usuario, ya que funciona muy bien con archivos grandes ofreciendo una mayor 
compresión con una calidad similar.  
 
 

<!-- Page 76 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
76 
• H.264: 
H.264 o MPEG -4 parte 10 es una norma que define un códec de vídeo de alta compresión, 
desarrollada conjuntamente por el ITU -T Video Coding Experts Group (VCEG) y el ISO/IEC 
Moving Picture Experts Group (MPEG).
 
Es uno de los estándares más utilizados en la actualidad por las ventajas y beneficios que ofrece, 
con un sistema de compresión que permite tasas de transmisión inferiores a anteriores (MPEG
-2 
o MPEG-4) pero manteniendo la calidad y sencillez en la edición.  
Desde el año 2003 que se creó actualmente es muy popular para transmitir vídeo en la red o 
subirlo a las plataformas de streaming como YouTube.  
• HEVC / H.265:  
El High Efficiency Video Coding, que también adopta la denominación técnica de H.265 se 
considera el sucesor del anterior H.264 y fue lanzado en 2014, ofrece la misma calidad y 
compatibilidad con un mayor grado de compresión que su antecesor.
 
Esta evolución, ha supuesto la aparición de resoluciones en 4K y 8K, que necesitan de una mayor 
calidad sin aumentar mucho el ancho de banda necesario para las transmisiones en vivo o las 
plataformas de streaming.  
• AV1 (AOMedia Video 1):  
Es un formato de compresión de video abierto y libre de derechos de autor diseñado para las 
transmisiones de video a través de Internet. compatible con infinidad de dispositivos y 
reproductores.  
El codificador AOMedia Video 1 se lanzó en 2017 como uno de los compresores de vídeo que 
reduce el tamaño de los datos en un 30% de media sin que la calidad se vea apenas afectada.
 
Es muy indicado para transmitir y publicar en redes sociales, ya que se puede transmitir y 
reproducir con anchos de banda menores manteniendo un alto nivel de calidad.
 
5. Algoritmos  
Algoritmo : 
Según la RAE en su primera acepción algoritmo es un conjunto ordenado y finito de operaciones que 
permite hallar la solución de un problema.  
Partiendo de la definición formal esencial del término "algoritmo", podemos ser más concretos 
añadiéndole el calificativo "informático".  

<!-- Page 77 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
77 
Algoritmo Informático:  
Un algoritmo informático es una secuencia de instrucciones finitas, ordenadas y precisas que reciben 
uno o más datos de entrada y cuya finalidad es resolver un problema o realizar una tarea mediante un 
proceso automatizado en una computadora, arrojando un resultado (uno o más datos de salida). 
 
Entre sus características, podemos mencionar:  
• La precisión.  
• La finitud.  
• La generalidad.  
• La búsqueda de la eficiencia.  
Las instrucciones deben ser claras, tener un número de pasos determinado y ser aplicables a cualquier 
conjunto de datos de entrada que cumpla con unas condiciones específicas, utilizando la menor 
cantidad posible de recursos.  
5.1. Bondad, recursividad y optimización  
Bondad del algoritmo  
Se puede crear más de un algoritmo para un determinado problema. Para determinar el algoritmo más 
adecuado se mide la bondad del algoritmo a través de los siguientes parámetros:
 
• Tiempo que tarda en ejecutarse.  
• Recursos que consume.  
Recursividad del algoritmo  
Para determinar si un problema es recursivo, se divide en partes. Si alguna de las partes tiene la misma 
forma que el problema principal, será recursivo.  
Es recursivo cuando se llama a sí mismo para resolver un problema o parte de este.
 
Al realizar un procedimiento recursivo se está haciendo uso de una pila.  

<!-- Page 78 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
78 
Optimización de algoritmos  
Consiste en realizar modificaciones en un algoritmo para reducir el tiempo que tarda en ejecutarse o los 
recursos que consume.  
5.2. Complejidad de los algoritmos  
La complejidad algorítmica, representa la cantidad de recursos que necesita un algoritmo para resolver 
un problema. 
Un algoritmo será más eficiente comparado con otro, siempre que consuma menos recursos, como el 
tiempo y espacio de memoria necesarios para ejecutarlo.  
Por tanto, se cuantifica la eficiencia de un algoritmo con las siguientes medidas de complejidad:
 
• Complejidad Espacial:  
La cantidad de memoria que utiliza un programa para su ejecución, es decir, el espacio en 
memoria que ocupan todas las variables propias al algoritmo.  
• Para calcular la memoria estática de un algoritmo se suma la memoria que ocupan las 
variables declaradas en dicho algoritmo.  
• En el caso de la memoria dinámica , el cálculo no es tan simple ya que, éste depende de cada 
ejecución del algoritmo.  
Para cada problema determinamos una medida N, que es el tamaño de la entrada o número de 
datos a procesar por el programa, intentaremos hallar respuestas en función de dicha N.
 
El concepto exacto que cuantifica N dependerá de la naturaleza del problema, (no se puede 
establecer una regla para N, pues cada problema acarrea su propia lógica y complejidad).
 
• En un array se puede ver a N como el rango del array.  
• En una matriz, el número de elementos que la componen.  
• En un grafo, podría ser el número de nodos o arcos que lo arman.  
• Complejidad Temporal o Tiempo de ejecución:  
Tiempo de cómputo necesario para la ejecución de un programa.
 
El tiempo de Ejecución de un programa se mide en función de N, lo que se designa como T(N).
 

<!-- Page 79 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
79 
5.2.1. Casos de uso  
Dependiendo de la casuísitica se elegirá un escenario u otro para analizar y elegir algoritmo.
 
Caso mejor, caso peor y caso medio de un algoritmo  
El comportamiento de un algoritmo puede cambiar notablemente para diferentes entradas pues para 
muchos programas el tiempo de ejecución es en realidad una función de la entrada específica, y no sólo 
del tamaño de ésta.  
Así suelen estudiarse tres casos para un mismo algoritmo: caso peor, caso mejor y caso medio.  
El caso mejor puede ser útil si buscamos optimizar un algoritmo sabiendo que los datos de entrada 
serán favorables, buscaremos pues el algoritmo más rápido.  
• Coste en caso mejor: Tmejor(n) = min{Tn
(a)|a Î An}  
Con esta fórmula tratamos de hallar el menor tiempo ( Tmejor ) que el algoritmo puede lograr 
para cualquier entrada de tamaño n.  Tn(a) será el tiempo de ejecución de una instancia 
determinada donde (|) a  es una instancia perteneciente (Î) al conjunto de todos las posibles 
entradas ( A) de tamaño ( n). 
El caso peor devolverá el resultado del tiempo máximo acontecido para resolver nuestro problema. 
Puede ser muy útil en el caso de que los datos de entrada no sean predecibles ni tengan filtro previo.
 
• Coste en caso peor: Tpeor(n) = max{Tn
(a)|&alpha; Î An}  
Misma fórmula que la anterior con la variante que tratamos de hallar el tiempo de ejecución 
máximo ( max) dada la totalidad de casos posibles. Es una manera de asegurar que en el peor de 
los casos nuestro algoritmo no sobrepasará un tiempo determinado.  
El caso promedio será útil para obtener una visión realista de rendimiento en situaciones típicas. Si la 
mayoría de entradas son típicas el caso promedio puede ser interesante pues nos ayudará a encontrar el 
tiempo promedio de ejecución del algoritmo . 
• Coste en caso promedio: Tprom (n) = &sum;(&alpha; &isin; An) Pr(&alpha;) * Tn (&alpha;), 
donde Pr es la probabilidad de ocurrencia de la instancia a y T es su tiempo de ejecución dado el 
tamaño de datos n.  
La fórmula aparentemente más compleja trata de hallar el tiempo promedio
 (Tprom ) de todas 
las posibles entradas de tamaño (n). La sumatoria &sum;(&alpha; &isin; An) recorre todas las 
posibles instancias &alpha; del conjunto An que representa el conjunto de todas las posibles 
instancias de tamaño n. Pr(&alpha;) * Tn(&alpha;) es el producto de la 
Probabilidad de 
ocurrencia de la instancia &alpha; por el Tiempo de ejecución de esa entrada de tamaño n.  
Por lo general estudiaremos el coste en caso peor de los algoritmos por dos razones:
 

<!-- Page 80 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
80 
1. Proporciona garantías sobre el coste del algoritmo ya que en ningún caso excederá el coste en 
caso peor. 
2. Es más fácil de calcular que el coste en el caso promedio.  
Como puede observarse los algoritmos cuya complejidad es descrita por una función polinomial pueden 
ser ejecutados para entradas grandes en una cantidad de tiempo razonable, mientras que los algoritmos 
exponenciales son de poca utilidad excepto para entradas pequeñas.  
5.2.2. Órdenes de complejidad  
El orden de complejidad es un concepto utilizado para analizar y describir cómo el rendimiento 
temporal de un algoritmo varía en relación con el tamaño de su entrada. Se representa mediante un 
conjunto de funciones que describen esta variación, y a la que se le suele denominar O.
 
Las órdenes de Complejidad más frecuentes son:  
• O (1) orden constante.  
El tiempo de ejecución del algoritmo no depende del tamaño de la entrada.  
• O (n) orden lineal.  
El tiempo de ejecución es directamente proporcional al nº de elementos (se suele dar en la 
búsqueda secuencial).  
• O (n log n) casi lineal.  
El tiempo de ejecución es directamente proporcional al número de elementos multiplicado por 
el logaritmo del número de elementos. Suele darse en algoritmos que utilizan la técnica divide y 
vencerás, seguida de un proceso de fusión de los resultados.  
• O (log n) orden logarítmico.  
El tiempo de ejecución es directamente proporcional al logaritmo del número de elementos. Se 
suele encontrar en algoritmos que utilizan la técnica de divide y vencerás (búsqueda binaria).
 
• O (n 2) orden cuadrático.  
El tiempo de ejecución es directamente proporcional al cuadrado del número de elementos. 
Suele darse en algoritmos que tienen que iterar por todos los elementos.  
• O (n a) orden polinomial (a > 2).  
• O (a  Ùn) orden exponencial (a > 1).  
• O (n!) orden factorial.  

<!-- Page 81 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
81 
5.3. Rendimiento y medición de los algoritmos  
El rendimiento o complejidad de un algoritmo indica su eficiencia, los costes que supone encontrar la 
solución a un problema mediante un algoritmo en comparación con otros, respecto al consumo de 2 
recursos: 
• El espacio: memoria que utiliza.  
• Tiempo: lo que tarda en ejecutarse.  
Estos parámetros nos sirven para comparar entre sí distintos algoritmos que resuelven el mismo 
problema. 
Análisis de la eficiencia temporal Algoritmo  
Consta de dos fases: análisis a priori y análisis a posteriori.  
• A posteriori: se mide el tiempo de ejecución para unos valores de entrada de datos y en un 
ordenador concreto. Se obtiene una medida real.  
• A priori: para unos valores de entrada dados, se obtiene una función que acota (por arriba o por 
abajo), el tiempo de ejecución.  
El resultado ofrece estimaciones de valor independiente del ordenador utilizado y sin tener que 
ejecutarlos. 
Este resultado es una medida de eficiencia temporal  que no puede ser expresada en una unidad 
concreta de tiempo (segundos…), Es un resultado que se define como una función del tamaño o 
talla de la entrada. 
Proporciona una medida teórica.  
Se denomina tamaño de la entrada  al número de componentes sobre los que se va a ejecutar el 
algoritmo.  
Denotaremos por T(n) el tiempo de ejecución de un algoritmo para una entrada de tamaño n, donde 
T(n) indica el número de instrucciones ejecutadas por un ordenador idealizado.
 
Resumen rendimiento de algoritmos de ordenación.  
 

<!-- Page 82 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
82 
5.4. Clasificación: ordenamiento y búsqueda  
La clasificación de los algoritmos es muy amplia y variada, ya que depende del campo donde se utilicen, 
enfoque y uso que se les vaya a dar.  
En el campo de la programación informática, podemos diferenciar principalmente los algoritmos en 2 
tipos, basándonos en el enfoque de cuál es el objetivo que van a cumplir: algoritmos de ordenamiento y 
algoritmos de búsqueda.  
Veremos también los conceptos más importantes de los Algoritmos Voraces.
 
5.4.1. De ordenamiento  
Estos algoritmos se utilizan para ordenar una determinada cantidad de datos almacenados en un vector.
 
En los algoritmos que se utilizan para realizar ordenamiento, podemos diferenciar varios conceptos:
 
• La memoria que utilizan:  
• Interna. 
• Externa  (memoria secundaria).  
• La estabilidad del algoritmo:  
• Estable: al ordenar varios elementos con el mismo valor, estos mantienen el mismo orden 
que tenían entre ellos en un principio.  
• Inestable: no tienen en cuenta el orden que tenían en el vector inicial.  
• El método de resolver el problema.  
• Iterativos: Utiliza bucles o estructuras iterativas (for, while, repeat…) para solucionar el 
problema. 
Se utilizan para resolver problemas donde sea necesario repetir un determinado número de 
veces un conjunto de instrucciones, bucle. Se repite un proceso una y otra vez. (Se les llama 
también estructuras repetitivas, un ciclo iterativo es la repetición de operaciones hasta que 
se cumple una condición).  
Ejemplo: While Do, Repeat -Until y For.  
• Recursivos:  Utilizan la recursividad para solucionar el problema.  
La recursividad es una técnica de programación en la que una función se llama a sí misma y 
termina en su forma más simple con un caso base. La recursividad permite dividir un 

<!-- Page 83 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
83 
problema en subproblemas más pequeños del mismo tipo, hasta llegar a una condición que 
detiene la recursividad proporcionando una solución al problema.  
 
 
 
 
 
+ Info 
Recuerda: 
• Un algoritmo rescursivo finaliza en su forma más simple al 
llegar a un caso base.  
• El caso base aparece en un algoritmo recursivo cuando una 
función deja de invocarse a si misma para devolver un 
valor. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

<!-- Page 84 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
84 
5.4.1.1. Según la estabilidad del algoritmo  
Entenderemos mejor cuando un algoritmo es estable o inestable con el siguiente ejemplo:
 
 
 
 
 
Ejemplo 
Para verlo más claro utilizaremos letras.  
• Imaginemos que tenemos un vector con los elementos {b, 
A, c, a}.  
• Si lo ordenamos por orden alfabético, los valores "A" y "a" 
tienen el mismo valor.  
• Un algoritmo estable siempre devolverá el orden:  
{A, a, b, c}.  
• Dado que "A" aparece antes que "a" en el vector original, 
este orden se debe mantener.  
• Los algoritmos inestables no tienen en cuenta el orden que 
tenían en el vector inicial y podrían devolver {A, a, b, c} o 
bien {a, A, b, c}.  
 
 
5.4.1.2. Según el método de resolver el problema  
Vamos a ver los siguientes tipos de algoritmos:  
• Iterativos: 
• Round-robin. 
• Selección.  
• Burbuja. 
• Inserción. (Directa o Binaria).  
• Shellsort. 

<!-- Page 85 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
85 
• Recursivos:  
• QuickSort.  
• MergeSort.  
• Binsort. 
• RadixSort.  
 
 
 
 
Atención 
"Un algoritmo recursivo puede expresarse como iterativo y 
viceversa." 
Es decir, para solucionar un mismo problema, podemos programar 
un código de algoritmo con métodos recursivos o iterativos. 
Dependiendo de las condiciones del problema a resolver, será 
mejor utilizar uno u otro.  
 
 
5.4.1.2.1. Iterativos  
Aquellos que llegan a un resultado a través de una iteración mediante un ciclo definido o indefinido.
 
Se caracterizan por que se ejecutan mediante ciclos, esto hace que sean muy útiles para realizar tareas 
repetitivas. La mayoría de los lenguajes de programación modernos tienen palabras reservadas para 
realizar iteraciones.  
Algoritmo Iterativos Round -robin 
Es uno de los algoritmos más antiguos, sencillos y equitativos en el reparto de la CPU entre los procesos, 
es un algoritmo de planificación de procesos, simple de implementar, y de manera equitativa y en un 
orden racional, lo que significa que evita la monopolización de uso de la CPU, y es muy válido para 
entornos de tiempo compartido.  
Normalmente se realiza comenzando por el primer elemento de la lista hasta llegar al último y 
empezando de nuevo desde el primer elemento.  

<!-- Page 86 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
86 
Dentro de un sistema operativo se asigna a cada proceso una porción de tiempo equitativa y ordenada. 
Para tener una utilización equitativa de los recursos del equipo, se limita cada proceso a un pequeño 
período, llamado quantum (Q) o time -slice, y luego se suspende este proceso para dar oportunidad a 
otro proceso y así sucesivamente. A esto se le denomina comúnmente como Planificación Round
-Robin. 
(La lista de procesos se planifica por FIFO). Es decir, si el proceso agota su quantum (Q) de tiempo, se 
elige a otro proceso para ocupar la CPU. Si el proceso se bloquea o termina antes de agotar su quantum 
también se alterna el uso de la CPU.  
 
 
 
 
+ Info 
Por esta planificación surge la necesidad de un reloj en el sistema, 
que genera periódicamente interrupciones, así se garantiza que el 
sistema operativo (en concreto la rutina de servicio de 
interrupción del reloj) coja el mando de la CPU periódicamente.
 
El quantum de un proceso equivale a un número fijo de pulsos o 
ciclos de reloj. Al ocurrir una interrupción de reloj que coincide con 
el agotamiento del quantum se llama al despachador, el cual le 
cede el control de la CPU al proceso seleccionado por el 
planificador. 
 
 
Un proceso puede abandonar la CPU por 2 criterios:  
• Libremente, si su tiempo de ejecución en la CPU es < Q (quantum).
 
• Después de una interrupción, si su tiempo de ejecución en la CPU es > Q (quantum) o si el 
proceso se bloquea.  
Existe una variante del algoritmo de planificación de Round -Robin, denominado SSR (Selfish Round 
Robin, y que emplea dos colas, una para los procesos nuevos y otra para los procesos antiguos, por lo 
que favorece a los procesos parcialmente ejecutados.  
Algoritmo Iterativo de Selección  
Vamos comparando uno a uno para encontrar el menor elemento del vector y lo intercambiamos por el 
que está en la primera posición. Repetimos el proceso usando el resto de los elementos (buscamos el 
menor y lo ponemos en la segunda posición). Y así sucesivamente hasta que quede ordenado.
 
Para n elementos, debemos llevar a cabo n*(n-1)/2  comprobaciones, ya que necesitaremos n-1 
pasadas para completarlo. El coste del algoritmo es O(n 2). 

<!-- Page 87 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
87 
Algoritmo Iterativo de Método de Burbuja (o Bubblesort)  
Es uno de los métodos más simples para ordenar una cantidad determinada de datos.
 
Podemos decir que es un algoritmo de ordenación de complejidad cuadrática.
 
Método de ordenación donde se recorre un vector de elementos y se intercambia en cada recorrido un 
elemento con su sucesor si no están en orden.  
Se basa en comparar los elementos adyacentes, comparando cada elemento con el siguiente. Si el par 
de elementos no está en orden, intercambiamos su posición.  
Se repetirá el proceso varias veces con el resto de los elementos hasta llegar a una vuelta en la que no se 
produzcan cambios. Esto significa que ya está ordenado.
 
En el primer proceso o iteración, se hará la comparación del penúltimo elemento con el último, 
quedando el último elemento ordenado, por lo que en la siguiente iteración (segunda) ya no será 
necesario esa comparación, acortando así el proceso.  
Del mismo modo, en la segunda iteración la última comparación es el antepenúltimo elemento con el 
penúltimo, quedando el penúltimo ya ordenado, por tanto, en la siguiente iteración no se realizará ya la 
comparación entre esos dos elementos (antepenúltimo y último), y así sucesivamente.
 
Al igual que en el anterior, debemos llevar a cabo n*(n-1)/2  comprobaciones, ya que necesitaremos n-1 
pasadas como máximo para completarlo. El coste del algoritmo también es 
O(n 2). 
 
Ejemplo de número máximo de iteraciones necesarias para el 
ordenamiento 
Análisis Iterativo de Inserción  
Hay 2 tipos, inserción directa y Binaria.  
• Directa: La inserción directa irá comparando de manera secuencial un elemento con el elemento 
anterior y colocándolos en la posición que les corresponde. Empezará en la segunda posición de 
la lista hasta llegar a la última posición de la misma.  
• Binaria: La inserción binaria es un algoritmo incremental que toma el siguiente elemento de la 
lista desordenada (elegido de manera secuencial) y utiliza búsqueda binaria en la sublista 
ordenada para encontrar la posición adecuada de inserción.  

<!-- Page 88 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
88 
En la búsqueda binaria, se divide la sublista ordenada en dos mitades comparando el nuevo 
elemento con el elemento central de la sublista. Si el nuevo elemento es menor que el elemento 
central, la búsqueda continúa en la mitad izquierda; si es mayor, se busca en la mitad derecha.
 
Este proceso se repite ajustando el rango de búsqueda (creando las sublistas necesarias y 
comparando con su parte central) hasta encontrar la posición correcta. Una vez encontrada la 
posición, se desplazan a la derecha todos los elementos en la sublista ordenada que son mayores 
que el nuevo elemento para hacer espacio. Luego, se inserta el nuevo elemento en la posición 
correspondiente.  
Se continuará hasta que todos los elementos hayan sido procesados y colocados en su posición 
correcta, obteniendo así la lista completa ordenada.  
Análisis Iterativo de ShellSort (Shell)  
Es una versión mejorada del ordenamiento por inserción directa. Funciona comparando elementos que 
están distantes, separados por cierta distancia o incremento y reorganizarlos entre sí. La distancia o 
incremento inicialmente grande se va reduciendo en cada iteración.  
Cuando llega a 1, el algoritmo realiza una última pasada con el método de inserción directa. Dado que la 
lista ya está parcialmente ordenada por las pasadas anteriores, esta fase final es más eficiente.
 
Donald Shell sugirió empezar por n/2 e ir dividiendo entre 2 hasta llegar a 1. Aunque este método 
mejora el método de inserción, es posible mejorarlo con otras secuencias de incrementos.
 
Un incremento de 3 significa que vamos comparando los elementos separados por esa distancia, es 
decir, si tenemos 10 elementos:  
• Comparamos el primer elemento, el cuarto, el séptimo y el décimo.  
• Comparamos el segundo, quinto y octavo.  
• Comparamos el tercero, el sexto y el noveno.  
5.4.1.2.2. Recursivos  
Aquellos que realizan llamadas recursivas (a sí mismos) para llegar al resultado.
 
 
 
 

<!-- Page 89 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
89 
 
+ Info 
Cuando una función se llama a sí misma (recursiva), se agregan 
nuevas instancias de esa función a la pila de llamadas.  
Cada instancia de la función en la pila se denomina "frame" o 
marco de pila. 
 
 
Utilizan la recursividad a sí mismos, a sus funciones. Suelen ser más sencillos de diseñar y entender, pero 
utilizan más recursos que los iterativos, ya que necesitan usar la pila del sistema para "apilar" cada 
función. A esta repetición, que nos permiten ejecutar varias veces un conjunto determinado de 
instrucciones, se le denomina ciclos. 
Uso de la pila en la recursividad  
Hemos indicado que un programa recursivo en ejecución tiene una pila asociada para este propósito.
 
En la pila se almacena la siguiente información por cada llamada:  
• La dirección de retorno  de la función: de modo que sea posible regresar al punto de ejecución 
inmediatamente posterior al de la llamada a la función.  
• Los argumentos de la función o rutina  de la llamada: la función llamada obtiene los argumentos 
parámetros (también llamados parámetros) de la pila. Por ejemplo, en una función para sumar 
dos números, los argumentos serían los números a sumar.  
• Espacio para las variables locales:  la cantidad de espacio que hay que reservar, es proporcional 
al número de variables locales que hayamos definido y al tamaño que requiere cada (entero, 
carácter, real…).  
• El resultado devuelto por la función:  esto es opcional, normalmente se devuelve el resultado en 
uno de los registros de la CPU.  
 
 
 
+ Info 
En los lenguajes de alto nivel (como C o Java) la gestión de la pila 
de llamadas la realiza de forma automática el compilador, y el 
programador no necesita preocuparse de su funcionamiento.  
 
 

<!-- Page 90 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
90 
Análisis recursivo de Quicksort (ordenación rápida)
 
También conocido como algoritmo de Hoare. Es un algoritmo recursivo basado en la 
"técnica de divide 
y vencerás".  Su funcionamiento es el siguiente:  
• Seleccionamos un elemento de la lista que denominaremos pivote. 
• Se crean 2 sublistas, (sublista1 y sublista2),  antes y después del pivote.  
• Colocaremos los elementos menores que el pivote en la sublista1 y los mayores en la sublista2. 
• Repetimos el proceso dividiendo esas 2 sublistas creadas en otras 2, eligiendo un pivote en cada 
una de esas divisiones.  
• El logaritmo se detendrá cuando el bloque que se desea ordenar está formado por un solo 
elemento. 
Análisis recursivo de MergeSort (ordenación por mezcla)
 
Al igual que el anterior, es un algoritmo recursivo basado en la técnica de divide y vencerás.
 
Su funcionamiento se divide en dos partes: División y Fusión:  
• División: 
• Partimos el vector en dos partes iguales o de tamaño aproximado si tiene un número impar 
de elementos. 
• Volvemos a partir en dos recursivamente cada una de las partes hasta tener listas de un solo 
elemento. 
• Fusión: 
• Vamos mezclando de dos en dos las sublistas (de un elemento). En cada mezcla vamos 
cogiendo el elemento más pequeño de las dos sublistas hasta obtener una sola sublista 
ordenada. 
• Repetimos el paso anterior con pares de las sublistas obtenidas hasta que tengamos una 
sola lista ordenada. 

<!-- Page 91 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
91 
 
Ejemplo ordenamiento MergeSort  
Análisis recursivo de Binsort (clasificación por urnas)
 
Es un algoritmo de ordenamiento que distribuye todos los elementos a ordenar entre un número finito 
de urnas (casilleros). Cada urna sólo puede contener los elementos que cumplan unas determinadas 
condiciones.  
Por ejemplo, un intervalo de números entre n y n+15. Las condiciones deben ser excluyentes entre sí, 
para evitar que un elemento pueda ser clasificado en dos urnas distintas. Después cada una de esas 
urnas se ordena individualmente con otro algoritmo de ordenación (que podría ser distinto según la 
urna), o se aplica recursivamente este algoritmo para obtener urnas con menos elementos.
 
Análisis recursivo de RadixSort  
También basa su funcionamiento en el uso de urnas. Es un algoritmo de ordenamiento que ordena 
enteros procesando sus dígitos de forma individual. Como los enteros pueden representar cadenas de 
caracteres (por ejemplo, nombres o fechas) y, especialmente, números en punto flotante 
especialmente formateados, RadixSort no está limitado sólo a los enteros.
 
5.4.1.3. Estructuras cíclicas  
Existen 3 tipos de estructuras cíclicas, que pueden utilizarse tanto en algoritmos recursivos como 
iterativos: 
• While Do (hacer mientras):  WHILE condición DO instrucción.  
Si en la primera ejecución de la instrucción el resultado de la condición es FALSA, se sale del 
ciclo y se continua con la siguiente instrucción, por lo que no se cumpliría la recursividad. Se 
debe tener un valor para la variable a evaluar antes de comenzar y se debe evitar un ciclo 
infinito. 

<!-- Page 92 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
92 
• REPEAT -UNTIL (repite mientras):  similar a la anterior, pero la sentencia se ejecutará al menos 
una vez. 
• FOR (para):  se repite una instrucción un número determinado de veces.  
Se incrementa una variable en 1 desde un valor inicial hasta un valor final.  
Su sintaxis es: FOR identificador:  = inicio TO fin DO instrucción:  
• Identificador:  es la variable que se incrementará.  
• Inicio: es el primer valor que tendrá dicha variable.  
• Fin: es el valor hasta el cual se incrementará la variable.  
5.4.2. Algoritmos de Búsqueda  
El objetivo es encontrar un elemento dentro de la lista.  
Existen varios tipos:  
• Secuencial. 
• Búsqueda Binaria o Dicotómica.  
• Búsqueda basada en tablas Hash.  
5.4.2.1. Secuencial 
Recorremos todos los elementos secuencialmente comparándolos con el que buscamos, hasta 
encontrarlo o acabar la lista, dando un resultado de "elemento no encontrado".  
5.4.2.2. Búsqueda Binaria o Dicotómica  
Se debe partir de una tabla o lista ordenada. Se divide en 2 trozos y se comprueba el elemento. Si 
coincide termina la búsqueda. Si es mayor debe estar en la parte que contiene los elementos 
mayores y 
si es menor, en la parte que contiene los elementos menores. Posteriormente ese trozo se vuelve a 
dividir y así sucesivamente hasta que lleguemos al elemento deseado.  
Se utiliza con vectores ordenados.  

<!-- Page 93 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
93 
Para realizar la búsqueda binaria, comparamos el elemento que buscamos con un elemento del vector 
(normalmente el elemento central).  
• Si es igual, lo hemos encontrado.  
• Si es menor, se repite la búsqueda con los elementos a la izquierda del elemento central.
 
• Si es mayor, se repite la búsqueda con los elementos a la derecha del elemento central.
 
Con este método, en cada paso vamos descartando la mitad de los elementos. Si no lo encontramos, 
llegará un momento en que tendremos un intervalo indivisible (un solo elemento). Si este no coincide 
con el elemento buscado podemos decir que no se encuentra en el vector.
 
5.4.2.3. Búsqueda basada en tablas Hash  
La organización de ficheros es direccionada dispersa, lo que puede provocar colisiones.
 
La búsqueda en tablas Hash, es un método que optimiza las búsquedas. Asignamos a cada elemento de 
la tabla/lista un índice obtenido a partir de una función denominada Hash. Esa función debe aportar un 
dato que permita identificar y ordenar el elemento convenientemente y debe ser simple para que la 
velocidad de búsqueda realmente mejore. Lo que haremos posteriormente es buscar en la tabla de esos 
índices creados en lugar de entre los datos, optimizando recursos. En este método debemos tener en 
cuenta que se puede crear el mismo índice asignado a diferentes elementos de la tabla/lista a causa de 
la función Hash utilizada, generando colisiones que debemos evitar.
 
Para solucionar estas posibles colisiones tenemos 2 métodos:  
• Encadenamiento separado o Hashing abierto:  se construye para cada clave que salga en una 
tabla. Se suele usar una LIFO para ir guardando los elementos correspondientes a las claves que 
coincidan. 
• Direccionamiento abierto o Hashing cerrado:  usamos un vector en el que ponemos una clave 
para cada casilla. Utilizamos una función denominada rehasing,  que determina el elemento 
exacto una vez que localiza la clave que estamos buscando.
 
 
 
 
 
 
Atención 
La función Hash, también es una herramienta para proteger la 
integridad. 
 

<!-- Page 94 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
94 
 
5.4.3. Algoritmos Voraces  
También conocido como goloso, ávido, devorador o greedy.
 
Un algoritmo voraz, es una estrategia de búsqueda por la cual se sigue una heurística consistente en 
elegir la opción óptima en cada paso local con la esperanza de llegar a una solución general óptima. Este 
esquema algorítmico es el que menos dificultades plantea a la hora de diseñar y comprobar su 
funcionamiento. Normalmente se aplica a los problemas de optimización.
 
No siempre se llega a una solución óptima, ya que solo tienen en cuenta la información de las decisiones 
que han tomado hasta el momento y no las posibles futuras.  
 
 
 
 
+ Info 
Ejemplo de uso de los algoritmos voraces para alcanzar soluciones 
óptimas: 
Problema de la mochila fraccional (KP): Disponemos de una 
colección de objetos (cada uno de ellos con un valor y un peso 
asociados) y debemos determinar cuáles colocar en la mochila 
para lograr transportar el valor máximo sin superar el peso que 
puede soportar.  
 
 
Ejemplos de algoritmos voraces:  
• Algoritmo de Kruskal:  el algoritmo de Kruskal es un algoritmo de la teoría de grafos para 
encontrar un árbol recubridor mínimo en un grafo conexo y ponderado. Es decir, busca un 
subconjunto de aristas que, formando un árbol, incluyen todos los vértices y donde el valor de la 
suma de todas las aristas del árbol es el mínimo. Si el grafo no es conexo, entonces busca un 
bosque expandido mínimo (un árbol expandido mínimo para cada componente conexa).
 
• Algoritmo de Dijkstra:  es utilizado para determinar el camino más corto desde un vértice origen 
hasta los demás vértices de un grafo, que tiene pesos en cada arista.  

<!-- Page 95 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
95 
• Codificación Huffman:  es un método de compresión de datos sin perder información, que 
analiza la frecuencia de aparición de caracteres de un mensaje y les asigna un código de longitud 
variable. Cuanto mayor sea la frecuencia le corresponderá un código más corto.
 
 
 
 
 
Nota 
Otros algoritmos que sirven para hallar el árbol de expansión 
mínima o árbol recubridor mínimo son: el algoritmo de Prim, el 
algoritmo del borrador inverso y el algoritmo de Boruvka.  
 
 
• Algoritmo de Prim.  
• Algoritmo de triangulación voraz.  
• Algoritmo para la ubicación óptima.  
5.5. Representación de algoritmos  
Existen muchas formas de representar algoritmos, escritas o gráficas. Las más usuales son:
 
• Lenguaje Natural:  (ya no se utiliza por permitir ambigüedades).  
• Diagramas Nassi -Shneideman. 
• Pseudocódigo. 
• Diagrama de flujo.  
5.5.1. Lenguaje natural  
No es suficientemente preciso. Los programadores pueden realizan un primer paso en lenguaje natural 
(español, inglés…) para ellos mismos, como anotaciones etc. Pero no lo utilizaran como una 
representación real del algoritmo.  

<!-- Page 96 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
96 
5.5.2. Diagramas de Nassi -Shneideman 
También conocidos como diagramas de Chapin.  
Es una diagramación estructurada con una determinada simbología.
 
 
5.5.3. Pseudocódigo  
Es un lenguaje de descripción de algoritmos parecido a un lenguaje de programación, pero sin reglas 
sintácticas estrictas, el programador utiliza su lenguaje natural (español, inglés…). Lo importante es la 
secuencia de instrucciones.  
El pseudocódigo es fácil de escribir y es sencillo traducirlo a un lenguaje de programación.
 
 
 
 
 
 
 
 
 
 
 

<!-- Page 97 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
97 
 
Suelen utilizarse verbos imperativos: iniciar, leer, sumar, ordenar, fin…  
 
 
 
Ejemplo 
Pseudocódigo que imprime números del 1 al 10.  
PROGRAMA nombreDelPrograma  
ENTORNO: numero - 0 
ALGORITMO:  
MIENTRAS número = 10 HACER  
• ESCRIBIR  numero 
• número  - numero + 1  
FIN MIENTRAS  
FIN PROGRAMA  
 
 
5.5.4. Diagrama de flujo  
Por su representación gráfica es la más adecuada y utilizada para representar algoritmos.
 
Existen técnicas concretas para realizar los diagramas, la mejor en nuestro caso en la top
-down y 
estructurada.  
Top-down: consiste en descomponer un problema en partes. Primero indicamos la dimensión total y 
luego lo dividimos en subpartes, hasta llegar a una expresión concreta y simple.
 
La diagramación nos indica que símbolos gráficos (que representan acciones) utilizan, para facilitar el 
entendimiento visualmente, pero podemos vincularlos entre sí, uniéndolos mediante flechas, según las 
necesidades que debe cumplir el algoritmo.  
Las flechas indican el orden de ejecución.  
Por ejemplo: 

<!-- Page 98 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
98 
 
Simbología en los diagramas de flujo.  
 
 

<!-- Page 99 -->

 
 
Tipos de Datos y Estructuras. Tipos, Organización y Formato de Ficheros. Algoritmos 
 
99 
6. Bibliografía 
• Prieto Espinosa, A. Introducción a la informática. 4.ª edición, 2006.
 
• GOODMAN, S. E. y HEDETNIEMI, S. T. Introduction to the clesing and analysis of algorithms. 
Pearson, 2012.  
• https://es.ccm.net/.  
• http://informatica.uv.es/iiguia/AED/oldwww/2001_02/Teoria/Tema_10.pdf.
 
• https://es.wikipedia.org.  
• https://es.wikipedia.org/wiki/Tipo_de_dato_abstracto.
 
• https://es.slideshare.net/CarlosAlbertoCuervoC/tipos
-de-listas-en-estructura -de-datos. 
• http://www.iuma.ulpgc.es/users/jmiranda/docencia/programacion/.
 
• https://www.oscarblancarteblog.com/2014/08/22/estructura
-de-datos-arboles/.  
• http://informatica.uv.es/iiguia/AED/material.html.
 
• http://disi.unal.edu.co/~lctorress/estructuras/estructuras.htm.
 
• https://si.ua.es/es/ayuda/formatos
-de-fichero/formatos -de-fichero-que-debes-conocer.html.  
• http://www.juntadeandalucia.es/averroes/centros
-
tic/29009272/helvia/sitio/upload/Estudio_de_los_distintos_formatos_de_ficheros.pdf.
 
• http://lsub.org/ls/export/pfc_pfs/.
 
• https://tecnologia -informatica.com.  
• http://lwh.free.fr/pages/algo/tri/tri_selection_es.html.
 
• https://www.campusmvp.es/recursos/post/Rendimiento
-de-algoritmos -y-notacion-Big-
O.aspx. 
• https://www.adslzone.net/reportajes/software/codecs
-audio-video/.

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|Ficha Resumen del Tema 03]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque2-tema03|Nota Fuente Oficial del Tema 03]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema03-estructuras-algoritmos|Test Tema 03]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Flashcards Bloque 2]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema02|⬅️ Tema Completo 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema04|Tema Completo 04 ➡️]]
