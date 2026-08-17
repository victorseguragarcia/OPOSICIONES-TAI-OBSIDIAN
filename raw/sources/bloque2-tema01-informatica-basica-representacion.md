---
title: "Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores"
type: "raw-source"
topic: "informatica-basica-representacion"
source_pdf: "raw/bloque 2/624446.pdf"
pages: 88
date: "2026-08-17"
---

# Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores



<!-- Page 1 -->

 
 
Informática básica. 
Representación y comunicación 
de la información: elementos 
constitutivos de un sistema 
de información 
DV.TextoHTML(01).Esp.dot     |     UD011929_V07_T01 


<!-- Page 2 -->

ÍNDICE 
1. Informática 
4 
1.1. Dato, información y conocimiento 
7 
1.2. ¿Qué es un ordenador? 
11 
1.3. Unidades de medida de la información 
12 
1.4. Sistemas de numeración 
17 
1.4.1. Conversión indirecta mediante base decimal 
18 
1.4.2. Conversión directa entre bases potencia de 2 
21 
1.5. Conversión entre sistemas de numeración 
22 
1.6. Representación de la información 
22 
2. Sistemas de información 
30 
2.1. Funciones de un sistema de información 
32 
2.2. Características de un sistema de información 
33 
2.3. Características de la información útil 
33 
2.4. Elementos de un sistema informático 
34 
2.5. Distintas clasificaciones 
35 
2.5.1. Clasificación del Software 
36 
2.6. Jerarquía de niveles 
37 
3. Arquitectura de ordenadores 
39 
3.1. La arquitectura Von Neumann 
39 
3.1.1. Evolución de los ordenadores. Generaciones 
39 
3.2. Arquitectura Harvard 
44 
4. Hardware 
45 
4.1. Placa base 
49 
4.1.1. Chip TPM 
54 
4.2. CPU (procesador) 
57 
4.2.1. Unidad aritméticológica 
58 
4.2.1.1. Operaciones aritméticas 
59 
4.2.1.2. Operaciones lógicas 
59 
4.2.1.3. Operaciones de desplazamiento 
62 


<!-- Page 3 -->

 
 
4.2.2. Unidad de control 
62 
4.2.2.1. El contador de programa (Ingles: Program Counter) 
63 
4.2.2.2. Gestionar la comunicación con los periféricos 
63 
4.2.3. Reloj del Sistema 
64 
4.2.4. Arquitectura de procesadores 
64 
4.2.4.1. CISC y RISC 
64 
4.2.4.2. Arquitectura ARM 
66 
4.2.5. Núcleo físico y lógico 
68 
4.3. Memoria 
70 
4.3.1. Tecnologías 
71 
4.3.2. Clasificación 
72 
4.3.2.1. Memoria primaria 
73 
4.3.2.1.1. Memorias ROM (Read Only Memory) 
73 
4.3.2.1.2. Memorias RAM (Random Access Memory) 
74 
4.3.2.1.3. Cache (SRAM) 
76 
4.3.2.2. Memoria secundaria (almacenamiento permanente) 
76 
4.3.2.2.1. SWAP (Virtual Memory) 
78 
4.3.2.2.2. Memorias flash 
78 
4.3.3. Jerarquía 
78 
4.3.4. Thrashing (Hiperpaginación) 
79 
4.4. Sistemas de direccionamiento 
80 
4.5. El tiempo de ejecución de un programa 
84 
4.5.1. Procesador multinúcleo 
85 
4.5.2. Clasificación según paralelismo 
85 
4.5.3. Tipos de Instrucciones de la CPU 
86 
5. Bibliografía 
87 
 


<!-- Page 4 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
4 
1. Informática 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
 
La mayoría de las fuentes (incluido el diccionario de la Real Academia Española) coinciden en que es una 
palabra de origen francés. Es un acrónimo de las palabras information (INFORmación) y automatique 
(autoMÁTICA). 
En inglés: "Computer Science and Engineering" (ciencia e ingeniería de computadores). 
Por lo tanto, una primera definición simple de informática sería: 
"Tratamiento automatizado de la información" 
Hoy en día no se concibe el tratamiento automatizado de la información sin el uso de ordenadores, por 
lo que se podría ampliar la definición. 
"Tratamiento automatizado de la información por medio de computadoras" 
Finalmente, la informática es una disciplina que utiliza metodologías, tanto para desarrollos de tipo 
teórico y experimental, como para el diseño de sistemas, por lo que puede considerarse una ciencia y 
una ingeniería al mismo tiempo. La disciplina de informática es el cuerpo de conocimiento que trata del 
diseño, análisis, implementación, eficiencia y aplicación de procesos que transforman la información 
(Tuk,1994). 


<!-- Page 5 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
5 
A partir de esta definición y nuestra definición anterior, podemos resumir en la siguiente: 
"Conjunto de conocimientos científicos y técnicas que hacen posible el tratamiento automático de 
la información por medio de computadoras" (R.A.E., 2017) 
 
 
 
Resumiendo 
• Es una ciencia y una ingeniería. 
• Procesamiento automatizado de la información. 
• Uso de ordenadores. 
 
Ahora debes tener claros los siguientes conceptos para el entendimiento del "Universo Informático" 
Ordenador, computador o computadora 
Se pueden utilizar cualquiera de estos tres términos para referirnos al mismo concepto. 
Según la R.A.E., "Un ordenador es una máquina electrónica que, mediante determinados programas, 
permite almacenar y tratar información, y resolver problemas de diversa índole". 
 
 
 
 
Definición 
Una definición más completa es la propuesta por Prieto en 2006: 
"Un ordenador, computador o computadora es una máquina capaz 
de aceptar unos datos de entrada, efectuar con ellos operaciones 
lógicas y aritméticas, y proporcionar la información resultante a 
través de un medio de salida; todo ello sin intervención de un 
operador humano y bajo el control de un programa de instrucciones 
previamente almacenado en el propio computador". 
 


<!-- Page 6 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
6 
Esta definición tiene los siguientes puntos importantes: 
• Es una máquina. 
• Es un sistema (como veremos más adelante). Acepta datos de entrada, los procesa y devuelve, 
unos resultados a través de un dispositivo de salida. 
• En el sector informático, donde nosotros nos vamos a centrar, los resultados de salida serán 
información. Sin embargo, no siempre tienen que ser información; en ocasiones pueden ser 
impulsos eléctricos que generan una reacción específica en otros dispositivos (por ejemplo, en 
robots en las cadenas de montaje). 
• Automático (no interviene operador humano). 
• Controlado por un programa. 
Sistema informático 
Un sistema es un conjunto de elementos que se relacionan entre sí, que funcionan como un todo, y que 
hace posible el tratamiento automático de la información. 
Un ordenador es un sistema en sí mismo 
Las partes principales de un sistema informático son: 
• Hardware: componentes físicos. 
• Software: componentes lógicos. 
• Humanware: componente humano. (añadido en los últimos años). 
 
 
 
 
Ejemplo 
Un ejemplo de sistema informático sería un ordenador, varios 
periféricos (ratón, teclado, monitor e impresora), la persona que lo 
utiliza y los programas instalados en la computadora. 
 
 
Un sistema puede ser un subsistema de otro sistema. 
Un Subsistema informático, es un sistema que es parte de otro sistema mayor. 


<!-- Page 7 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
7 
Ejemplo: el procesador es un subsistema que forma parte de un nivel superior, y a la vez es un 
subsistema formado por un conjunto de elementos interrelacionados (unidad aritmético-lógica, unidad 
de control y los registros). 
Podríamos denominar subsistemas a: 
• Subsistema físico: asociado al hardware. Incluye elementos como CPU, memoria principal, placa 
base, periféricos de entrada y salida, etc. 
• Subsistema lógico: asociado al software y la arquitectura; incluye, sistema operativo, firmware, 
aplicaciones y bases de datos. 
Codificación de la información 
Diferentes conjuntos de datos tienen que interactuar entre sí, con un fin común 
Es una transformación mediante la cual, se representa los elementos de un conjunto mediante los de 
otro, consiguiendo que a cada elemento del primer conjunto le corresponda un elemento del segundo. 
 
 
 
 
Ejemplo 
Un ejemplo de código podría ser los números de teléfono. En este 
caso, los códigos tienen significado, como los prefijos que indican 
la ciudad o el país. 
España corresponde al 034 y Zaragoza al 976. 
 
1.1. Dato, información y conocimiento 
 


<!-- Page 8 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
8 
 
 
 
Definición 
Según la R.A.E. la palabra dato, en el ámbito de la informática, se 
define como: 
"Información dispuesta de manera adecuada para su tratamiento 
por una computadora". 
 
 
Esta definición en informática puede llevar a equívoco dado que la mayoría de los autores indican que la 
información es un conjunto de datos ya procesados. 
Vamos a ver otras definiciones, más adaptadas a la informática: 
• Dato: 
Carece de significado o valor por sí mismo, no dice nada sobre el porqué de las cosas. 
(En informática, se les da el formato adecuado para poder ser procesados). 
• Información: 
Es el conjunto de datos ya procesados, estructurados e interrelacionados que tienen significado, 
y de los cuales podemos extraer conocimiento. 
La palabra "informar" significa originalmente "dar forma a" y la información es capaz de formar 
a la persona que la recibe (receptor). 
Tiene que informar; son datos que marcan la diferencia. 
A diferencia de los datos, la información tiene significado, relevancia y está organizada para 
algún propósito. Los datos se convierten en información cuando su creador les añade 
significado. 
La información, es un mensaje para un receptor, depende de la percepción del receptor cómo 
influirá sobre sus juicios de valor y comportamientos. 
Es el receptor, el que decide si el mensaje que ha recibido es realmente información, es decir, si 
realmente le informa. 
Hay varios métodos de ver la transformación de datos en información añadiéndoles valor en 
varios sentidos. Vamos a verlo según Davenport y Prusak (1999). 


<!-- Page 9 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
9 
La transformación de dato a información se puede producir por: 
• Contextualización. 
• Categorización. 
• Cálculo. 
• Corrección. 
• Condensación. 
 
 
 
 
Ejemplo 
En las organizaciones, la información se envía continuamente, 
informes, email, etc. 
Es el receptor el que la considerará o no útil y la convertirá en 
conocimiento. 
 
 
• Conocimiento: 
"El conocimiento deriva de la información, que a su vez deriva de los datos". 
Para Davenport y Prusak (1999), el conocimiento, es una mezcla de experiencia, valores, 
información y saber hacer que sirve como marco para la incorporación de nuevas experiencias e 
información, y es útil para la acción. 
Se origina y aplica en la mente de los conocedores. 
En las organizaciones con frecuencia, no solo se encuentra dentro de documentos o almacenes 
de datos, sino que también está en rutinas organizativas, procesos, prácticas, y normas. 
La transformación de información a conocimiento se puede producir mediante: 
• Comparación. 
• Consecuencias. 
• Conexiones. 
• Conversación. 
• Predicción. 


<!-- Page 10 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
10 
Veamos un esquema para que quede más claro 
 
Transformación de datos en conocimiento 
Veamos un ejemplo. 
Tenemos un extracto de cuenta bancaria con los gastos del primer trimestre del año. 
Fecha 
Concepto 
Importe 
12-01-2018 
Gasolina 
35€ 
24-01-2018 
Supermercado 
150€ 
01-02-2018 
Gasolina 
40€ 
17-02-2018 
Supermercado 
65€ 
23-02-2018 
Luz 
130€ 
07-03-2018 
Gasolina 
25€ 
12-03-2018 
Supermercado 
175€ 
28-03-2018 
Gasolina 
20€ 
El número 35 de la primera fila sería un dato. 
Si lo contextualizamos, podremos decir que es un gasto en gasolina. También podemos categorizarlo 
diciendo que son euros. Tenemos 35€ de gasto en gasolina. Esto es información. 
También podemos sumarlo todas las cifras de € que corresponden a Gasolina, en el mismo mes, en 
marzo tenemos: 25 € + 20 € = 45 € que determina el total que en marzo gastamos en gasolina. 


<!-- Page 11 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
11 
Entonces, si hemos calculado el total de cada mes en gasolina, tenemos la siguiente información: 
Fecha 
Concepto 
Importe 
Enero 
Gasolina 
35€ 
Febrero 
Gasolina 
40€ 
Marzo 
Gasolina 
45€ 
Finalmente, mediante comparación, podemos saber que enero es el mes con menor gasto y marzo el 
mes de mayor gasto. Esto es conocimiento. 
1.2. ¿Qué es un ordenador? 
 
 
 
Vídeo 
Antes de continuar, tienes que ver… 
Video Clase: "Bienvenido al Universo Informático". 
Seguro que ya conoces casi todos los conceptos, pero te ayudara a 
sumergirte de lleno en la informática. 
(Tienes el material en el Campus Virtual). 
 
 
Los ordenadores, son elementos electrónicos que contienen millones de interruptores eléctricos, que 
sólo pueden tener 2 valores: 
• Sin corriente eléctrica: valor 0. 
 
(Circuito abierto-
apagado) 


<!-- Page 12 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
12 
• Con corriente eléctrica: valor 1. 
 
(Circuito 
cerrado-
encendido) 
A cada uno de estos valores se le denomina bit. 
El código que utiliza dos valores (0 y 1) se llama código binario. 
Es el idioma del ordenador, la única forma que podemos comunicarnos con él, se denomina Lenguaje 
Máquina. 
Lenguaje máquina 
Es el idioma del ordenador, la única forma que podemos comunicarnos con él, a través del código 
binario, para que el ordenador entienda el conjunto de instrucciones que debe ejecutar. 
Los datos de entrada se deben codificar a código binario para el ordenador entienda, y las salidas se 
descodifican para que sean comprensibles para el usuario. 
Funcionamiento del Sistema 
La CPU ejecuta una serie de instrucciones u órdenes elementales llamadas instrucciones máquina que 
deben estar almacenadas en la memoria principal para poder ser leídas y ejecutadas. 
1.3. Unidades de medida de la información 
Bit (BInary digiT) 
Como hemos visto, es la unidad más elemental de información, con 2 únicos valores, 0 y 1. 
Por tanto, la unidad mínima de almacenamiento y transmisión de un ordenador es el bit. 
Con un bit podemos representar dos estados. Algunos ejemplos serían: 
• Sí/No. 
• Verdadero/Falso. 


<!-- Page 13 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
13 
• Ocurre/No ocurre. 
• Contiene/No contiene. 
• Encendido/Apagado. 
Representamos nuestros caracteres, letras o números, mediante Byte, es decir un grupo de 8 
valores de 0s y 1s 
 
Byte 
Es un conjunto de ocho bits. 
Normalmente nos comunicamos con el ordenador a través del lenguaje escrito, por lo que debemos 
codificar los caracteres a bits. Para ello, cada letra se codificará con un número determinado de ellos. 
Esta es la unidad que se utiliza para medir el almacenamiento. 
Cómo el byte es una unidad muy pequeña, se utilizan múltiplos de este para referirnos a cantidad de 
información. 
Veamos la tabla de medidas: 
UNIDADES DE MEDIDA DE ALMACENAMIENTO 
1 bit = dígito binario (0 o 1) 
8 bits = 1 Byte 
1024 bytes = 1 Kilobyte 


<!-- Page 14 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
14 
UNIDADES DE MEDIDA DE ALMACENAMIENTO 
1024 kilobytes = 1 Megabyte 
1024 megabytes = 1 Gigabyte 
1024 gigabytes = 1 Terabyte 
1024 terabytes = 1 Petabyte 
1024 petabytes = 1 Exabyte 
1024 exabytes = 1 Zettabyte 
1024 zettabytes = 1 Yottabyte 
1024 yottabyte = 1 Brontobyte 
1024 brontobytes = 1 geopbyte 
Unidades de medida de almacenamiento 
 
 
 
Técnicas de estudio 
Para memorizar el orden de las unidades de medida podría ser 
interesante crear una regla mnemotécnica (como crear una frase 
sencilla con palabras que empiecen con las letras K-M-G-T-P-E-Z-
Y-B-G). 
Ejemplo: Kilómetro (KM), Gran Turismo (GT), PEZ Y Bulgaria (BG 
es su código ISO 3166). 
 
Esta forma de medición fue válida hasta 1998. En este año, la "Comisión Electrónica Internacional" 
publico el apéndice IEC 60027-2, donde se instauraban los prefijos binarios y nacía la unidad 
"Kibibyte" 
Esto fue necesario por la confusión generada entre los prefijos de las unidades en el sistema decimal y el 
análogo informático. 
 


<!-- Page 15 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
15 
 
 
 
Ejemplo 
"Kilo" en el decimal es sinónimo de 1000, mientras que en el 
informático son 1024. Un Kilo-gramo son 1000 gramos, pero un 
Kilo-byte son 1024 bytes. 
 
 
Por tanto, se tomó la decisión de dejar los prefijos habituales con sus valores tradicionales, Kilo = 1.000, 
mega =1.000.000, etc. 
Y generar una nueva unidad para los sistemas informáticos, el Kibibyte y sus derivados: 
Kibibyte (KiB) = 210 → 1.024 B 
Mebibyte (MiB) = 220 → 1.048.576 B 
Gibibyte (GiB) = 230 → 1.073.741.824 B 
Tebibyte (TiB) = 240 → 1.099.511.627.776 B 
ETC. 
Y comparando 
Sistema Internacional Decimal 
Unidades ISO/UEC 80000-13 
Múltiplo 
Símb. 
Bytes 
Valor 
Múltiplo 
Símb. 
Bytes 
Valor 
Kilobyte 
KB 
10^3 
1000 B 
Kibibyte 
KiB 
2^10 
1024 B 
Megabyte 
MB 
10^6 
1000 KB 
Mebibyte 
MiB 
2^20 
1024 KiB 
Gigabyte 
GB 
10^9 
1000 MB 
Gibibyte 
GiB 
2^30 
1024 MiB 
Terabyte 
TB 
10^12 
1000 GB 
Tebibyte 
TiB 
2^40 
1024 GiB 
Petabyte 
PB 
10^15 
1000 TB 
Pebibyte 
PiB 
2^50 
1024 TiB 
Exabyte 
EB 
10^18 
1000 PB 
Exibyte 
EiB 
2^60 
1024 PiB 


<!-- Page 16 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
16 
Sistema Internacional Decimal 
Unidades ISO/UEC 80000-13 
Múltiplo 
Símb. 
Bytes 
Valor 
Múltiplo 
Símb. 
Bytes 
Valor 
Zetabyte 
ZB 
10^21 
1000 EB 
Zebibyte 
ZiB 
2^70 
1024 EiB 
Yottabyte 
YB 
10^24 
1000 ZB 
Yobibyte 
YiB 
2^80 
1024 ZiB 
ETC. 
 
 
 
 
 
 
 
Aunque a fecha actual (principios de 2021) algunas casas como Microsoft, todavía utilizan la unidad 
Kilobyte como 1024 bytes en sus sistemas operativos. 
Nibble 
A veces se le denomina también semi-octeto, cuarteto o medio-byte. 
Es un conjunto de 4 bits (o medio octeto). 
Su interés se debe a que cada cifra en hexadecimal (0, 1, 2, ..., 9, A, B, C, D, E, F) se puede representar 
con un cuarteto, puesto que 24 = 16 (). También el cuarteto es la base del sistema de codificación BCD. 
Binary-Coded Decimal (BCD) 
O Decimal codificado en binario, es un estándar para representar números decimales en el sistema 
binario, en donde cada dígito decimal, es codificado con una secuencia de 4 bits. 
Con esta codificación especial de los dígitos decimales en el sistema binario, se pueden realizar 
operaciones aritméticas como suma, resta, multiplicación y división. 
Cada dígito decimal tiene una representación binaria codificada con 4 bits: 
Binary-Coded Decimal (BCD) 
Decimal 
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 
BCD 
0000 
0001 
0010 
0011 
0100 
0101 
0110 
0111 
1000 
1001 
Los números decimales, se codifican en BCD con los bits que representan sus dígitos. Por ejemplo, la 
codificación en BCD del número decimal 59237 es: 
Número Decimal 59237 representado en BCD 
Decimal 
5 
9 
2 
3 
7 
BCD 
0101 
1001 
0010 
0011 
0111 


<!-- Page 17 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
17 
La representación anterior (en BCD) es diferente de la representación del mismo número decimal en 
binario puro: 
• Número Decimal 59237 = BCD: 01011001001000110111. 
• Número Decimal 59237 = Binario: 1110011101100101. 
1.4. Sistemas de numeración 
 
Los sistemas de numeración utilizados en la actualidad están basados en sistemas posicionales de tipo 
polinomial. Un número es una cadena de dígitos afectado cada uno de ellos por un peso que depende de 
la posición que ocupa. 
 
 
 
 
+ Info 
Función polinomial: 
Es una función continua, cuya expresión es un polinomio, por 
ejemplo: f(x)=3x4-5x6+6. 
Un polinomio es una expresión algebraica constituida por una 
suma finita de productos entre variables y constantes, o bien una 
sola variable. Las variables pueden tener exponentes de valores 
definidos naturales incluido el cero. 
 


<!-- Page 18 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
18 
Vamos a estudiar 4 sistemas de numeración 
 
 
 
Nota 
El sistema decimal es el menos eficiente de los cuatro. Es el más 
utilizado porque el ser humano tiene 10 dedos en las manos. 
 
 
Sistema 
Base 
Valores que podemos usar 
Binario 
2 
0, 1 
Octal 
8 
0, 1, 2, 3, 4, 5, 6, 7 
Decimal 
10 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
Hexadecimal 
16 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F 
El binario es el utilizado por los ordenadores y el octal y hexadecimal tienen importancia porque son 
potencias de 2 y su conversión a binario es directa. 
 
 
 
 
Vídeo 
Para repasar tienes esta Vídeo Clase: 
"Sistemas de Numeración". 
(Tienes el material en el Campus Virtual). 
 
1.4.1. Conversión indirecta mediante base decimal 
La conversión entre dos bases cualesquiera puede realizarse de forma indirecta, utilizando la base 
decimal (base 10) como paso intermedio. 
Este procedimiento es el más habitual y el más sencillo de aplicar, ya que el sistema decimal es el que 
mejor comprendemos y utilizamos en la vida cotidiana. 


<!-- Page 19 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
19 
A continuación vamos a estudiar este sistema de conversión indirecto, usando siempre como sistema 
intermedio el decimal, ya que las operaciones son más sencillas. Permitiendo realizarlas incluso sin 
calculadora. 
Recuerda que, matemáticamente, cualquier número elevado a 0 es igual a 1: n0 = 1 
De Sistema Decimal(base 10) a cualquier Sistema(base 2, 8 o 16) 
 
Para pasar un número decimal (base 10) a cualquier otro sistema (cuya base será nuestro divisor, 
realizaremos los siguientes pasos: 
• Dividiremos el número decimal (dividendo) entre la base del sistema que queremos como 
resultado (divisor). 
• Guardaremos el resto. 
• El resultado de la división (cociente) lo volvemos a dividir el divisor, e iremos guardando los 
restos. 
Repetiremos la división hasta que el cociente sea menor que el divisor. 
• Tendremos todos los resultados de los restos, e invertiremos su orden. 
Dependiendo del sistema que queramos obtener realizaremos un cálculo u otro. 
• Si el resultado de la conversión es en base 2 (binario) ya tendremos el resultado. 
• Si el resultado de la conversión es en base 8 (octal) ya tendremos el resultado. 
• Si el resultado de la conversión es en base 16 (hexadecimal), el resultado lo debemos 
convertir en su correspondiente valor en Hexadecimal (15=F). 


<!-- Page 20 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
20 
 
De cualquier Sistema a Decimal 
Para la conversión del número, debemos tener en cuenta, los caracteres que lo componen y la posición 
de cada uno de ellos, comenzando desde la derecha hacia la izquierda, y teniendo en cuenta que las 
posiciones se cuentan desde el valor 0. 
Cada posición tiene un peso que va aumentando de derecha a izquierda según potencias sucesivas de la 
base específica, empezando por cero. 
Ejemplo: 247 ? 7: posición 0 4:posición 1 2:posición 2 
 


<!-- Page 21 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
21 
1.4.2. Conversión directa entre bases potencia de 2 
En el procedimiento anterior hemos visto el método general de conversión, que utiliza la base decimal 
como paso intermedio. Es un método válido para cualquier par de bases, especialmente cuando no 
existe una relación directa entre ellas. 
Sin embargo, existe un caso particular en el que no es necesario pasar por la base 10: cuando las bases 
implicadas son potencias de 2, como la base 4, la base 8 (octal) o la base 16 (hexadecimal). En estos 
casos, la conversión puede realizarse de forma directa, sin operaciones aritméticas, simplemente 
reagrupando o sustituyendo grupos de bits. 
Esto es posible porque las bases que son potencias de 2 mantienen una correspondencia exacta con el 
sistema binario. Si una base se expresa como B=2n, cada dígito de esa base equivale a un grupo fijo de 
n bits. 
• En base 4: cada dígito representa 2 bits. 
• En base 8: cada dígito representa 3 bits. 
• En base 16: cada dígito representa 4 bits. 
Por lo tanto, para convertir un número de una base potencia de 2 a binario, basta con sustituir cada 
dígito por su grupo binario correspondiente. 
El proceso inverso consiste en agrupar los bits de n en n según la base destino. 
Ejemplo: 
Convertimos el número hexadecimal 3A₁₆ a binario: 
• 3 → 0011 
• A → 1010 
Resultado: 3A16 = 001110102 
Si deseamos volver al sistema hexadecimal, bastará con agrupar los bits de cuatro en cuatro desde la 
derecha: 
001110102:0011 1010 → 3ª16 
Este tipo de equivalencia directa es posible porque, en las bases potencia de 2, el desbordamiento de 
una posición coincide exactamente con el completado de un grupo entero de bits. Es decir, cuando una 
posición alcanza su valor máximo, el siguiente incremento provoca el paso a la posición superior de 
forma perfectamente alineada con la estructura binaria. 


<!-- Page 22 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
22 
Gracias a esta correspondencia, las bases potencia de 2 se utilizan con frecuencia en informática para la 
representación y el almacenamiento interno de la información binaria, ya que permiten expresar los 
datos de forma más compacta y eficiente. 
• En programación y electrónica digital se emplea el hexadecimal (base 16) para representar 
bytes y direcciones de memoria. 
• En algunos sistemas y representaciones más antiguas se ha utilizado la base 8 (octal). 
En resumen, mientras que el método general de conversión entre bases pasa por el sistema decimal, 
cuando las bases son potencias de 2 la conversión se simplifica y se realiza directamente mediante la 
correspondencia bit a bit, sin necesidad de cálculos intermedios. 
1.5. Conversión entre sistemas de numeración 
Conversión entre dos bases distintas a la decimal 
Por comodidad, es más sencillo pasar primero a base 10, y luego desde base 10 a la que queramos como 
resultado final. 
 
 
 
 
Vídeo 
Es difícil de comprender mediante teoría, pero muy sencillo con 
ejemplos prácticos. Lo entenderás con esta Vídeo Clase: 
"Conversión entre Sistemas de Numeración". 
(Tienes el material en el Campus Virtual). 
 
1.6. Representación de la información 
Los ordenadores trabajan en el sistema binario (con ceros y unos), por lo que debemos representar la 
información codificándolo a binario. 
Existen cuatro tipos de información básicos: 
• Texto. 
• Números. 
• Sonidos. 
• Imágenes. 


<!-- Page 23 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
23 
Cada una de ellas se debe tratar de forma distinta. Vamos a ver los procesos para transformar la 
información externa en patrones de bits que pueda procesar el ordenador. 
La compresión de archivos es una técnica que consiste en representar (codificar) la información de 
manera que ocupe menos espacio. 
Cuando se transmite o almacena información pueden producirse errores. Enunciaremos las técnicas 
básicas de detección automática de errores. 
Representación de textos 
Es el método más usual de introducir información en un ordenador. Prieto (2006) propone la siguiente 
clasificación: 
• Caracteres alfabéticos: 
letras mayúsculas y minúsculas del alfabeto 
• Caracteres numéricos: 
0,1,2,3,4,5,6,7,8,9 
• Caracteres especiales: 
Símbolos ortográficos y matemáticos: 
) ( , * / ; : + Ñ ñ = ! ? . " & > # < ] Ç [ 
• Caracteres geométricos y gráficos: 
Símbolos con los que se representan formas geométricas o iconos elementales: 
 


<!-- Page 24 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
24 
• Caracteres de control: 
Representan órdenes de control, como salto de línea o comienzo de línea. 
Para la transformación de caracteres a patrones de bits se utilizan códigos de Entrada/Salida (E/S), 
normalizados en diferentes estándares predefinidos (ASCII...). 
Con n bits podemos representar 2n elementos. Realizaremos una correspondencia entre las 2n 
combinaciones (o parte de ellas) y los caracteres que queremos representar. Por lo tanto, para codificar 
m símbolos diferentes se necesitarán n bits, siendo: 
n = log2 m ≈ 3,32 log m 
Por lo tanto, para codificar 95 caracteres: 3,32 * log (95) = 6,566. Necesitaremos 7 bits. 
Algunos de los códigos más relevantes son: 
• EBCDIC (Extended Binary Coded Decimal Interchange Code). Utiliza 8 bits. 
• ASCII (American Standard Code for Information Interchange). Utiliza 7 bits. Es de los más 
usados. Existen versiones ampliadas de este código utilizando 8 bits que respetan los códigos de 
ASCII, aprovechando las combinaciones no usadas. 
• UNICODE. (Está reconocido como estándar ISO/IEC 10646). 
Se origina debido a los inconvenientes de los tipos anteriores: 
• Símbolos codificados insuficientes. 
• Símbolos de las versiones ampliadas a 8 bits no están normalizados. 
• Basados en caracteres latinos. No contemplan otras culturas. 
• Las culturas orientales utilizan ideogramas para representar palabras, por lo que no sirven 
estos sistemas de codificación. 
• UNICODE Ofrece: 
• Universalidad: Cubre la mayoría de lenguajes. 
• Unicidad: Cada carácter tiene un único código. 
• Uniformidad: Todos los símbolos se representan con 16 bits. 
• UNICODE no codifica caracteres de control. 


<!-- Page 25 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
25 
Teniendo en cuenta que los ordenadores funcionan en base 2 (0 y 1), Resumimos: 
Para representar caracteres tendremos que definir estos en función de secuencias de ceros y unos que 
previamente habremos definido. 
Ejemplo. En el código ASCII la "a" se decidió que sería "1100001" y la "b" = "1100010". 
Por tanto, ¿cuántos bits ("n") necesitamos para representar un número "x" de caracteres? 
Para hallar una aproximación al número de bits n que necesitamos para representar una serie de 
caracteres m, hemos de saber el número de caracteres m a representar y calcular su logaritmo en base 2. 
El logaritmo en base 2 es equivalente al logaritmo en base 10 del número de caracteres a representar 
dividido por el logaritmo en base 10 de 2. Como veíamos antes en la fórmula (n = log2 m) y log2(m) = 
log10(m) / log10(2). Cuando la base del logaritmo es 10, no hace falta especificarla, así que log10(m) es 
lo mismo que log(m). 
Sabiendo que log10(2) es 0,3010 (n ≈ log (m) / 0,3010) y que dividir un número es equivalente a 
multiplicar por su inverso (inverso de 0,3010: 1 / 0,3010 = 3,32). 
Entonces, si queremos controlar 95 caracteres n ≈ 3,32 * log10 (95) = 6,566. 
Una vez tengamos la aproximación buscaremos el entero superior más cercano y con ello obtendremos 
el número de bits necesarios. 
n = 6,566, pero "n" tiene que ser un numero entero (no existen las fracciones de bit) igual o el 
inmediatamente superior. En este caso la respuesta es 7 (no podemos usar 6,56 bits, se pueden usar 6 o 
7, pero un bit no se puede partir). 
Entonces, para poder definir 95 caracteres necesitamos 7 bits. 
¿Y para 255? n ≈ 3,32 log (255) = 7,989 es decir necesitamos 8 bits. 
Ya hemos llegado al final del desarrollo y resultado, no obstante, te voy a contar una manera más fácil 
de hacer los cálculos sin tanta matemática. Imagina, como es el caso en temario, que queremos hallar 
los bits necesarios para codificar 95 caracteres, como hemos visto, esto es n &asymp; log295. 
 
 
 
 
Hazlo fácil 
Vamos a multiplicar el número 2 por si mismo las veces que haga 
falta hasta que superemos el número buscado, en nuestro ejemplo, 
95. Buscamos de esta manera el exponente que nos hace falta. 
n = 2 x 2 x 2 x 2 x 2 x 2 x 2 = 128 
 


<!-- Page 26 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
26 
 
 
 
Contaremos las veces que aparece el número 2 en nuestras 
multiplicaciones y tendremos nuestro exponente, que es el número 
de bits que necesitamos. 
 
 
En nuestro caso 2^6 se quedaría corto y 2^7 se pasaría pues buscamos codificar 95 caracteres y no 128. 
Pero sabiendo que un bit es un número entero, es decir que no puede dividirse, y que en este caso 
queremos codificar 95 caracteres, habré de elegir el exponente más alto, ya que, si eligiéramos el 
inmediatamente inferior, 6, no podríamos codificar todos nuestros caracteres, por lo contrario, si 
cogemos 7 bits, aunque nos sobren recursos, sí podremos codificar la totalidad de nuestros símbolos. 
Representación de sonidos 
Las señales de sonido o audio (voz y música) son captadas por un sensor que transforma las señales de 
presión en señales eléctricas analógicas, que posteriormente serán digitalizadas. 
Representación de imágenes 
Las imágenes se capturan utilizando periféricos como cámaras y escáneres, los cuales generan un 
conjunto de bits. Existen muchos tipos de codificación y sistemas de compresión de imágenes que no 
estudiaremos en este tema. Las principales formas de representar imágenes son: 
• Mapa de bits. 
• Imagen vectorial. 
Representación de valores numéricos 
Para introducir números utilizamos códigos de E/S al igual que con el texto. Sin embargo, si queremos 
el valor del número y realizar operaciones con el mismo, debemos utilizar una representación 
fundamentada en el sistema numérico en base 2. 
• Datos de tipo entero: 
Se puede utilizar representación binaria o la representación de dígitos decimales codificados en 
binario (BCD). 
La representación binaria es la más utilizada y podemos trabajar con enteros sin signo y enteros 
con signo. 
Los enteros sin signo se representan con su número binario. 


<!-- Page 27 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
27 
Los enteros con signo tienen cuatro métodos diferentes que debemos considerar: 
• Enteros en signo y magnitud. 
El bit más significativo (el de la izquierda) se utiliza para el signo (0 positivo y 1 negativo). 
El resto de bits representan el valor en binario. 
• Enteros en complemento a 1. 
El signo se representa igual que en el caso anterior. Si el número es positivo, el resto de bits 
representan el valor absoluto del número en binario y si es negativo, representan su 
complemento a 1. El complemento a 1 se calcula cambiando los ceros por unos y los unos 
por ceros. Ej. 1001 su complemento a 1 es 0110. 
• Enteros en complemento a 2. 
Igual que los enteros en complemento a 1, pero utilizando el complemento a 2. Este se 
calcula realizando el complemento a 1 y sumándole 1 al resultado. Ej. 1001 su 
complemento a 2 es 0110 + 0001 = 0111. 
• Representación sesgada (o en exceso). 
Se le suma al número un sesgo S (normalmente 2n-1, siendo n el número de bits), de forma 
que el número resultante siempre será positivo. De esta forma ya no necesitamos reservar 
un bit para el signo. 
• Datos de tipo real: 
En computación, la notación en coma flotante se utiliza para trabajar con números reales. 
Dependiendo de la precisión requerida, se emplean formatos específicos, como la precisión 
simple (32 bits) o la doble precisión (64 bits). Los lenguajes de programación, como Java, C, 
C++ o Python, definen los nombres de estos tipos de datos. Por ejemplo, float y double son los 
nombres comunes para representar datos de tipo real con mayor o menor precisión. 
Vamos a ver el mecanismo interno de conversión de un número real, concretamente el 6,75 a 
coma flotante en 32 bits o precisión simple. 
1. Conversión a binario: 
» Convertimos la parte entera a binario: 6 -> 110 
» Convertimos la parte decimal a binario: 0,75 
Para convertir una parte decimal a binario, multiplicaremos la parte decimal por 2, 
guardaremos la parte entera del resultado como el siguiente dígito binario, y usaremos la 
parte fraccionaria del resultado para la siguiente multiplicación. Repetiremos este proceso 
hasta que la parte fraccionaria sea 0: 
1. 0,75 x 2 = 1,50. Nos guardamos la parte entera 1 y repetimos. 


<!-- Page 28 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
28 
2. 0,50 x 2 = 1. 
3. El resultado decimal será 0,11 que sumado a la parte entera ya convertida 
obtendremos en este caso 110,11 
2. Normalización: 
Para normalizar ajustaremos la forma convertida a la siguiente: 1,bits x 2n. En este caso 
110,11, moveremos el punto binario a la izquierda hasta que solo haya un dígito a la 
izquierda del punto. En nuestro ejemplo 2 posiciones, de ahí que la potencia sea 2. 
Fórmula normalizada: 1,1011 x 22 
3. Asignar parte: 
Es la descomposición del número en los componentes que formarán la representación 
estándar en coma flotante. 
» Signo 0 positivo 
» Exponente 2 + 127 = 129 (10000001 en binario) 
El 127 es el sesgo, un número estándar que se suma al exponente real, en nuestro caso 
2, para normalizar el valor de un exponente que se almacenará en 8 bits. 
» Mantisa: 1011 (completado a 23 bits: 10110000000000000000000) 
» La mantisa almacena los dígitos significativos después del punto binario (en forma 
normalizada, es decir que al almacenarlo suprime el primer 1) y lo completa a 23 bits. 
4. Combinar: 
Acometidas las partes se combinan todas para lograr el almacenamiento en 32 bits en 
formato IEE 754, así pues, el resultado en coma flotante es el siguiente: 
0 10000001 1011000000000000000000 
Signo 0, Exponente 10000001, Mantisa 1011000000000000000000 
 
 
 
 
Aclaración 
Más que conocer los pasos exactos para almacenar un número real 
en el sistema informático es útil conocer las distintas precisiones 
de las que disponemos para almacenar los números reales que nos 
interesan. 
 


<!-- Page 29 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
29 
Representación de instrucciones de programa 
Las instrucciones que nosotros creamos en un lenguaje de alto nivel, están el formato texto, usamos un 
código de E/S para representarlas, y a continuación se utiliza un intérprete o un compilador que 
trasforman estas instrucciones a lenguaje máquina (patrones de bits). 
Detección de errores en almacenamiento y transmisión 
Cuando se transmite o almacena información, es posible que se produzcan errores. 
Estos errores pueden ser producidos por múltiples causas, pero una de las más corrientes es una brusca 
alteración en el voltaje, que provoca errores o desplazamiento en la memoria RAM. 
Para detectarlo se utilizan diversas técnicas que consiste en la introducción de redundancias en el 
código (números que no representan ningún símbolo). 
Los algoritmos más utilizados son: 
• Bit de paridad. 
Este bit se introduce antes de transmitir o guardar la información. Hay dos tipos: 
• Paridad par. El número total de unos debe ser par. 
• Paridad impar. El número total de unos debe ser impar. 
De esta forma, si contamos el número de unos podemos saber si se ha producido un error. 
• Verificación de redundancia cíclica. 
La verificación por redundancia cíclica (CRC) es un código de detección de errores usado 
frecuentemente en redes digitales y en dispositivos de almacenamiento para detectar cambios 
accidentales en los datos. 
Los bloques de datos ingresados en estos sistemas contienen un valor de verificación adjunto, 
basado en el residuo de una división de polinomios; el cálculo es repetido, y la acción de 
corrección puede tomarse en contra de los datos presuntamente corruptos en caso de que el 
valor de verificación no concuerde. 
Es útil para detección de errores, pero, en condiciones de seguridad, no podemos confiar en que 
el CRC puede verificar plenamente que los datos son los correctos en caso de que se hayan 
producido cambios deliberados y no aleatorios. 
• Verificación de redundancia LONGITUDINAL. 
La verificación de la redundancia longitudinal (LRC, también denominada verificación de 
redundancia horizontal) no consiste en verificar la integridad de los datos mediante la 
representación de un carácter individual, sino en verificar la integridad del bit de paridad de un 
grupo de caracteres. 


<!-- Page 30 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
30 
Los campos LRC constan de un byte que contiene un valor binario de ocho bits. 
Los valores de LRC se calculan mediante dispositivos de transmisión, que añaden LRC a los 
mensajes. 
El dispositivo en el extremo receptor recalcula el LRC al recibir el mensaje y compara el valor 
calculado con el valor real recibido en el campo LRC. Si los valores son iguales, la transmisión se 
realizó correctamente; si los valores no son iguales, esto indica un error. 
Veamos un ejemplo de detección de errores: 
Cuando se transmite o almacena información, es posible que se produzcan errores, es decir, que, en un 
byte, alguno de sus dígitos se vea alterado. 
Ejemplo: transmitimos 00000011, y se recibe 00000010. 
Para detectarlo se utilizan diversas técnicas de detección, que consiste en la introducción de 
redundancias en el código (números que no representan ningún símbolo, sólo sirven para la 
comprobación). 
El algoritmo más típico es el Bit de paridad, que es un bit que se introduce antes de transmitir o guardar 
la información. Hay dos tipos: 
• Paridad par: El número total de unos debe ser par. 
• Paridad impar: El número total de unos debe ser impar. 
De esta forma, si contamos el número de unos podemos saber si se ha producido un error. 
En nuestro ejemplo: 
• Transmitimos 00000011. 
• Enviaríamos que el número total de unos es par. 
• Se recibiría 00000010, por tanto, al no cumplirse la condición de que el número total de unos es 
par, se detecta ERROR. 
2. Sistemas de información 
 
 
 
+ Info 
El contenido de este punto está basado en el libro "Principios de 
sistemas de Información" de Ralph Stair y George Reynolds. Es una 
lectura interesante si se desea profundizar en el tema. 
 


<!-- Page 31 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
31 
En primer lugar, vamos a definir unos conceptos que nos ayudarán a entender mejor un sistema de 
información. 
Sistema 
Un sistema es un conjunto de elementos o componentes que interaccionan con el fin de alcanzar un 
objetivo. 
Un sistema tiene cuatro componentes principales: 
• Entrada. 
• Procesamiento. 
• Salida. 
• Retroalimentación. 
Sistema de Información 
Basándonos en la definición de sistema, ampliamos para definir un sistema de información. 
Un sistema de información es un conjunto de elementos o componentes interrelacionados que recaban 
(entrada), manipulan (proceso), almacenan y distribuyen (salida) datos e información y proporciona 
una reacción correctiva (mecanismo de retroalimentación) si no se ha logrado cumplir un objetivo. 
 
Componentes de un sistema de información 
Los componentes de un sistema de información son: 
• Entrada: Actividad de recabar y capturar datos. 
• Procesamiento: Conversión o transformación de los datos en salidas útiles. 
• Salida: Producción de información útil, por lo general en forma de documentos e informes. 


<!-- Page 32 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
32 
• Retroalimentación: Salida que se utiliza para realizar cambios en la entrada o en el 
procesamiento para mejorar la eficacia de un sistema (el grado en que un sistema logra sus 
objetivos). 
• Opcionalmente el Almacenamiento también forma parte de un sistema de información, en 
función de si los datos de entrada y salida se almacenan en el ordenador. Dependerá del proceso 
a realizar. 
Sistema de Información basado en ordenador 
Es un conjunto único de elementos de hardware, software, bases de datos, telecomunicaciones, 
personas y procedimientos, que hacen posible el tratamiento de información. 
Este tratamiento de información es: recolectar, manipular, almacenar y procesar datos, con el fin de 
convertirlos en información útil, logrando un objetivo. 
2.1. Funciones de un sistema de información 
Diversos autores y organismos han definido las funciones fundamentales que debe cumplir un sistema 
de información. Aunque las denominaciones pueden variar ligeramente, todas coinciden en que el 
propósito esencial de un sistema de información es captar, procesar, almacenar y comunicar datos para 
transformarlos en información útil. 
Entre las funciones más comúnmente aceptadas se encuentran: 
• Recolección: Captura y registro de los datos procedentes de distintas fuentes. 
• Clasificación: Identificación y agrupación de los datos según su tipo y modo de recuperación. 
• Síntesis o compresión: Reducción de los datos sin pérdida de información significativa, 
eliminando redundancias. 
• Almacenamiento: Conservación organizada de los datos en soportes adecuados. 
• Recuperación: Acceso rápido y eficaz a los datos almacenados cuando son necesarios. 
• Procesamiento: Transformación de los datos en información útil mediante operaciones o 
cálculos. 
• Transmisión: Comunicación de datos o información entre distintos puntos o sistemas. 
• Presentación o exhibición: Visualización de la información en un formato comprensible y útil 
para los usuarios. 
Estas funciones, descritas en la literatura clásica de sistemas de información (Laudon & Laudon, 
O'Brien, Stair & Reynolds, entre otros), coinciden con la doctrina utilizada en manuales de 
universidades españolas y latinoamericanas. 


<!-- Page 33 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
33 
2.2. Características de un sistema de información 
Según el autor EMERY JAMES C, en uno de sus libros publicado en 1990, las principales características 
de un sistema de información son: 
• Formar parte de las actividades de la organización. Un sistema de información gerencial bien 
proyectado se vuelve parte integrante de las actividades de la organización en todos sus niveles. 
• Está basado en tecnología de computación. Un sistema de información es mucho más que un 
conjunto de procesos computarizados, por lo tanto, un sistema de información que no esté 
basado en parte por tecnología informática, o es relativamente simple o fue proyectado 
precariamente. 
• Ser un sistema hombre – máquina. Un sistema de información bien proyectado que 
interrelaciona tareas entre hombres y máquinas en forma eficiente. 
• Ser una colección de subsistemas. Un sistema de información está compuesto por una colección 
de subsistemas y el grado de conexión entre esos subsistemas es variado (puede ser más fuerte 
o más débil) según sea el nivel de integración, técnica y económica, más adecuado. 
• Ser adaptable a necesidades de cambios. Un sistema de información bien diseñado debe 
responder continuamente a las necesidades de cambios y avances tecnológicos. 
2.3. Características de la información útil 
Para que la información sea de utilidad a una organización o a las personas que la utilizan, debe tener las 
siguientes características: 
• Accesible. Los usuarios autorizados deben poder acceder a la información de una manera fácil y 
dicha información debe tener el formato correcto y ser recibida en el momento preciso. 
• Exacta. Debe estar libre de errores. 
• Completa. Contendrá todos los hechos relevantes. 
• Económica. El costo de la producción de la información debe ser inferior al valor del beneficio 
que aporta. 
• Flexible. Información flexible es aquella que puede utilizarse para varios propósitos. 
• Relevante. Cuando resulta de interés para la persona que la recibe. Por ejemplo, la fecha y lugar 
de realización del examen de oposición puede ser relevante para nosotros, pero no resulta de 
interés para las personas que no lo preparan. 
• Confiable. Probabilidad de que la información sea veraz. Por ejemplo, un rumor no es una 
información confiable. 


<!-- Page 34 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
34 
• Segura. Se debe proteger la integridad de la información (ante fallos o pérdidas) y ésta solo 
podrá ser accedida por los usuarios autorizados. 
• Simple. Debe presentarse de la forma más sencilla posible para evitar ambigüedades en el 
significado e información no útil. 
2.4. Elementos de un sistema informático 
Sistema de Información Basado en Ordenador 
Un sistema informático está formado por un gran número de elementos, desde un pequeño circuito 
eléctrico hasta una gran instalación de muchos equipos conectados entre sí, los programas que nos 
resuelven problemas y nosotros mismos, los seres humanos que los creamos, modificamos y utilizamos. 
Esta es la clasificación típica de las partes de la informática: 
• Hardware, componentes físicos: 
Son todas las partes físicas, tangibles, de un sistema informático: componentes electrónicos, 
cables, conectores y cualquier elemento físico involucrado, soportes físicos de almacenamiento 
(pendrive) etc. 
Todos los componentes necesarios para que sean posibles las telecomunicaciones, red, 
internet… 
• Software, componentes lógicos: 
Son los componentes intangibles, los sistemas operativos, aplicaciones, datos y ficheros, que 
son utilizados por los distintos componentes de hardware. 
Hay que destacar la importancia de las Bases de Datos, que almacenan de forma organizada 
datos en registros específicos y que deben ser identificables. 
Una Base de Datos, es el elemento más importante del sistema de información y, debe de estar 
sujeto a medidas de seguridad que garanticen su integridad y eviten el acceso por personal no 
autorizado. 
En las bases de datos se realizan diversos procesos, que son la conversión o transformación de 
los datos, como son, por ejemplo: 
• Transacciones: 
Permiten al usuario (o a un programa) consultar, agregar, modificar o eliminar un dato 
específico de la Información. 


<!-- Page 35 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
35 
• Informes: 
Mediante ellos, el usuario puede obtener uno o más registros y/o información de tipo 
estadístico (contar, sumar) de acuerdo a criterios de búsqueda y selección definidos. 
Dentro del software están también todos los protocolos que permiten Telecomunicaciones, 
para poder realizar transferencias de información. 
• Humanware, componente humano: 
Es un término introducido recientemente, que se utiliza para definir los recursos humanos, el 
trabajo del personal que participa en el diseño de los sistemas informáticos en cualquiera de sus 
fases. 
Se diferencian en diferentes roles según su interacción con los equipos informáticos 
(administrar, operar, programar, mantener los sistemas, y los usuarios finales). 
Todas las empresas u organizaciones deben tener un conjunto de reglas y políticas que controlen la 
seguridad y tratamiento de estos componentes; métodos y reglas sobre cómo administrar, operar, 
programar, mantener y/o utilizar el sistema. Incluyendo de forma muy destacada la seguridad 
(realización de copias de seguridad, permisos de acceso a los usuarios etc.) Pueden denominarse como 
Procedimientos administrativos. 
2.5. Distintas clasificaciones 
Los sistemas de información pueden clasificarse siguiendo diferentes criterios: 
• Según el propósito para el que se utilizará la información obtenida. 
Las aplicaciones pueden realizarse con diferentes fines: 
• Los sistemas transaccionales automatizan procesos operativos dentro de una organización. 
• Los Sistemas de Soporte a la Toma de Decisiones (DSS) asisten a distintos grupos de una 
organización. Entre ellos altos ejecutivos, gerentes intermedios, analistas de datos, 
departamentos de marketing, financieros y operaciones. Áreas que utilizan la información 
analítica proporcionada por los DSS para tomar decisiones informadas y estratégicas, 
optimizando la gestión de equipos, analizando tendencias, evaluando campañas y 
realizando proyecciones. 
• Sistemas Estratégicos, similar a los de toma de decisiones, ayudan a lograr ventajas 
competitivas. 
• Según su organización física. 
Vamos a ver una diferenciación y definición muy breve: 
• Sistemas centralizados: 
Básicamente, son sistemas donde los procesos se realizan en localización central, usando 
terminales conectados a un servidor, que puede controlar todos los periféricos directamente. 


<!-- Page 36 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
36 
• Sistemas distribuidos: 
Los ordenadores están separados físicamente y conectados entre sí por una red de 
comunicaciones. 
El usuario percibe como un solo sistema (no necesita saber qué cosas están en qué 
máquinas). El usuario accede a los recursos remotos de la misma manera en que accede a 
recursos locales. 
2.5.1. Clasificación del Software 
Merece la pena crear un epígrafe específico sobre la clasificación del software pues tiene un universo 
propio realmente consistente. 
En un primer nivel podemos distinguir tres grandes categorías: 
• Software de sistema: incluye el sistema operativo y las herramientas de gestión del sistema. 
• Software de programación: conjunto de herramientas usadas por los programadores para crear, 
editar, compilar, depurar y mantener otros programas informáticos. 
• Software de aplicación: programas diseñados para realizar tareas específicas del usuario. 
Dentro de este último nivel citaremos algunos de los distintos tipos que podemos encontrar: 
• Procesadores de texto: permiten la creacion, edición y aplicar formato a documento escritos 
(Word, LibreOffice, Documentos de Google). 
• Hojas de cálculo: sirven para realizar calculo, gestionar datos en tablas y generar gráficos (Excel, 
Google Sheets). 
• Navegadores web: permiten el acceso a navegar por paginas de internet (Google Chrome, 
Microsoft Edge, Opera, Brave). 
• Programas de presentación: se usan para la creación de diapositivas con texto, imágenes y 
efectos visuales (PowerPoint, Presentaciones de Google, Canva) 
• Bases de datos: pueden ser de tipo relacional o no y sirven para gestionar grandes cantidades de 
datos (MySQL, PostgreSQL, Oracle Database, Microsoft Access, MongoDB, Cassandra). 
• Software de diseño gráfico: se usa para crear y editar imágenes, ilustraciones o diseños 
(Photoshop, Gimp, Microsoft Paint). 
• Aplicaciones multimedia: reproducen o editan audio y vídeo (VLC Media Player, Audacity). 
• Software educativo: diseñado para el apoyo del aprendizaje en distintas áreas (Duolingo, 
Classroom). 
• Software de gestión empresarial: automatizan tareas contables, administrativas o de recursos 
humanos (SAP, Contaplus). 


<!-- Page 37 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
37 
Si nos atenemos a su modelo de distribución y uso permitido nos podemos encontrar con: 
• Software propietario: software de uso restringido y requieren una licencia pagada para su uso, 
además el usuario no puede modificar su código (Microsoft Office, Adobe Acrobat). 
• Software libre: distribuido con una licencia gratuita que permite al usuario usarlo, modificarlo y 
compartirlo libremente (LibreOffice, GIMP). 
• Software de codigo abierto: es similar al software libre, aunque en algunos casos puede tener 
restricciones comerciales (Firefox, Audacity). 
• Freeware: gratuito para el usuario, pero no permite modificaciones en su código ni redistribuirlo 
(Skype, PDF Creator). 
• Shareware: se ofrece de forma gratuita con las funciones reducidas o de forma temporal, tras lo 
cual se requiere pago (WinRAR, Avast). 
Por último, añadimos una última clasificación basada en el modo de creación del software: 
• Software a medida: desarrollados específicamente para una empresa o necesidad concreta, por 
lo que es más costoso, pero cumple con todos los requisitos del cliente. 
• Soluciones empaquetadas (software estándar): programas genéricos diseñados para un público 
amplio, son más económicos y reciben actualizaciones periódicas pero son menos 
personalizados. 
2.6. Jerarquía de niveles 
 


<!-- Page 38 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
38 
Entre distintas clasificaciones podemos encontrar la que se base en la jerarquía y se ordena por niveles. 
Pasamos a comentar los niveles de esta pirámide invertida: 
Hardware 
Nivel físico del sistema, compuesto por la CPU, memoria, dispositivos de entrada/salida, etc. Es la base 
sobre la que operan todos los demás niveles. Proporciona la capacidad de procesamiento y 
almacenamiento. Sin hardware, no existe soporte para los niveles superiores. 
Firmware 
Programas grabados en chips del hardware (por ejemplo, la BIOS o UEFI), encargados de iniciar el 
sistema y realizar tareas básicas de configuración. Inicializa el hardware (POST), configura dispositivos 
y actúa como puente entre el hardware y el sistema operativo. 
Sistema Operativo 
Es el cerebro del sistema. Gestiona recursos (CPU, memoria), controla dispositivos mediante drivers y 
ofrece interfaces para aplicaciones (API). Software que actúa como intermediario entre el hardware y 
los programas. Administra recursos, controla dispositivos y proporciona servicios esenciales. 
Middleware 
Software que permite la comunicación y gestión de datos entre el sistema operativo y las aplicaciones, 
especialmente en sistemas distribuidos o complejos. Facilita la comunicación entre aplicaciones o 
sistemas heterogéneos (ejemplo: bases de datos, servidores web, APIs de red). 
Software de aplicación 
Programas diseñados para que el usuario realice tareas concretas, como procesadores de texto, hojas 
de cálculo o navegadores web. Requieren el SO y, a veces, middleware para acceder a recursos. 
Usuario 
Aunque no es un nivel técnico del ordenador, representa el punto final de esta jerarquía, ya que todas 
las capas anteriores están diseñadas para servirle. 


<!-- Page 39 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
39 
3. Arquitectura de ordenadores 
Existen diferentes arquitecturas de ordenadores. 
3.1. La arquitectura Von Neumann 
También conocida como modelo de Von Neumann o arquitectura Princeton, ya que se basa en la 
arquitectura de computadoras descrita en 1945 por el matemático y físico John Von Neumann (y otros 
colaboradores), en el primer borrador de un informe sobre el EDVAC (considerado el primer). 
Esta arquitectura de diseño para un computador digital electrónico diferencia las siguientes partes: 
• Unidad de procesamiento: contiene la ALU y los registros del procesador. 
• Unidad de control: contiene el registro de instrucciones, el contador de programa y el 
decodificador de instrucciones. 
• Memoria: almacena tanto instrucciones como datos. 
• Mecanismos de entrada y salida: para la gestión de la entrada y salida de datos. 
El concepto ha evolucionado para convertirse en un computador de programa almacenado en el cual no 
pueden darse simultáneamente una búsqueda de instrucciones y una operación de datos, ya que 
comparten un bus en común. Esto se conoce como el cuello de botella Von Neumann, y muchas veces 
limita el rendimiento del sistema. 
Se puede decir que en la mayoría de los ordenadores actuales se utiliza la Arquitectura Von 
Neumann, o una arquitectura Von Neumann modificada, ya que a medida que los computadores han 
evolucionado se han añadido características procedentes de la arquitectura Harvard. 
3.1.1. Evolución de los ordenadores. Generaciones 
Los ordenadores han ido evolucionando. Cada vez que aparecía una nueva tecnología, la anterior 
quedaba en desuso y aparecía una nueva generación de ordenadores. 
Existen múltiples versiones de las generaciones de los ordenadores. Normalmente, casi todos los 
autores coinciden en las tres o cuatro primeras generaciones, pero hay mucha discrepancia entre la 
existencia o no de posteriores generaciones y las tecnologías que engloban. 
Luis Álvarez Munárriz, en su libro "Fundamentos de inteligencia artificial" propone 5 generaciones 


<!-- Page 40 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
40 
Primera Generación 
La primera generación de ordenadores digitales utiliza válvulas de vacío y relés. Eran lentos, caros, 
voluminosos y consumían mucha energía eléctrica. 
Se considera a EDVAC, diseñado por Von Neumann en el año 1945, el primer ordenador ya que 
funcionaba por programa de control almacenado. 
Al mismo tiempo, en Inglaterra, se construyó el ordenador EDSAC que funcionaba según estos 
principios. 
Características: 
• Tubos de vacío para procesar información. 
• Tarjetas perforadas para la introducción de datos. 
• Cilindros magnéticos para almacenamiento. 
• Grandes, lentas y de gran consumo. 
 
Válvulas de vacío 
Segunda Generación 
La segunda generación se hizo posible por la aparición del transistor que sustituye las válvulas de vacío. 
Esto produjo una mayor rapidez de conmutación, reducción del tamaño y mayor fiabilidad. En 1954 se 
construyó el ordenador TRADIC utilizando transistores. 


<!-- Page 41 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
41 
Características: 
• Transistores para procesar información. 
• Anillos magnéticos para almacenar información. 
• Se disminuye el consumo y el tamaño. 
 
TRADIC 
Tercera Generación 
La tercera generación surge con la introducción de los circuitos integrados (pastillas de silicio) en las 
cuales se colocan miles de componentes electrónicos, en una integración en miniatura. 
La investigación sobre el comportamiento de los semiconductores en el campo de la Física permitió 
conectar en una delgada capa de silicio transistores, resistencias, condensadores y diodos. Aunque se 
trata de una baja integración, sin embargo, se aumenta la velocidad del proceso y se reduce el tamaño 
de los ordenadores. 
Características: 
• Aparecen las memorias con chip de silicio (circuitos integrados en chip para procesar y 
almacenar información). 
• Aumenta la velocidad. 


<!-- Page 42 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
42 
• Disminuye el tamaño. 
• Disminuye el consumo (desprendían menos calor, siendo energéticamente más eficientes. 
 
IBM 360. Museo de historia de la computación 
Cuarta generación 
La cuarta generación surge con los avances en las técnicas de integración. 
Ello posibilita la creación y uso del microprocesador en el que se conectan todos los elementos de la 
Unidad Central de proceso. Se construyen y comercializan los ordenadores personales y al mismo 
tiempo se construye el primer Superordenador. 
Características: 
• Procesos de integración LSI y VLSI (Large Scale of Integration y Very Large Scale of 
Integration). 
• Desarrollo del microprocesador. 
• Ordenadores personales. 
 


<!-- Page 43 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
43 
Quinta generación 
En la quinta generación se intentan hacer realidad los proyectos surgidos ante las limitaciones de la 
arquitectura Von Neumann. 
El proyecto japonés de 5ª generación se consideró como prototipo del ordenador del futuro. 
Entretanto, se introducen mejoras fundamentales con respecto a la generación anterior. Se aspira a que 
estos ordenadores sean rápidos, fiables, inteligentes y afables con el usuario. Ello será posible en la 
medida que muchos aspectos de lo que hoy es software en los ordenadores actuales se implemente en 
su hardware. 
 
La inteligencia artificial está cambiando la forma de diseñar ordenadores 
Se pueden resaltar las siguientes líneas de investigación: 
• Semiconductores. 
Miniaturización y aumento de rapidez de los circuitos posibilitadas por las investigaciones sobre 
semiconductores promovidos por la investigación de los físicos. 
• Paralelismo masivo. 
Construcción de un tipo de ordenador que posea múltiples unidades de proceso. 
• Lógica difusa. 
Ordenadores que manejen conocimiento incierto cuyo manejo y procesamiento se realiza a 
través de sistemas de control difuso. (Lógica difusa es aquella en la que, en lugar de trabajar con 
valores numéricos, trabajamos con valores difusos. Por ejemplo, usar los valores mal, regular, 
normal, bueno y muy buen en lugar de valores del 1 al 10). 


<!-- Page 44 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
44 
• Facilidad de uso. 
Conseguir que las personas que no tengan conocimientos de informática puedan trabajar con 
un ordenador de forma sencilla. 
• Sistemas distribuidos. 
Conjunto de ordenadores separados físicamente e interconectados entre sí por una red de 
comunicaciones. Cada máquina tiene su propio hardware y software, pero el programador lo 
percibe como un solo sistema. Sus principales ventajas son el coste, la tolerancia a fallos y la 
escalabilidad. 
• Inteligencia artificial. 
Integración de sistemas inteligentes, que son aquellos que pueden resolver problemas 
complejos en distintos campos de una forma automática utilizando técnicas de inteligencia 
artificial y aprendizaje automático. 
 
 
 
 
El experto opina 
Cuando aparece una nueva tecnología, aparece una nueva 
generación que deja obsoleta a la anterior. Esto solo pasa hasta la 
4ª generación. 
No creemos que exista una 5ª generación como tal, sino que, 
conviven distintas tecnologías y se trabaja sobre distintas líneas de 
investigación, pero la aparición de una nueva tecnología o la 
mejora en la misma no supone un salto de generación ya que no 
dejan de utilizarse el resto de tecnologías. 
 
3.2. Arquitectura Harvard 
En este modelo de arquitectura, hay una división de la memoria en dos, una memoria de instrucciones y 
una memoria de datos, de manera que el procesador puede acceder separada y simultáneamente a las 
dos memorias, ya que el procesador dispone de un sistema de conexión independiente para acceder a 
cada una de ellas. 
La arquitectura Harvard es más moderna que la de Von Neumann, esta división de memoria la 
diferencia del modelo de Von Neumann. 


<!-- Page 45 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
45 
Cada memoria y cada conexión pueden tener características diferentes, como, por ejemplo, el tamaño 
de cada memoria, el tamaño de las palabras de memoria (número de bits de una palabra), y la 
tecnología usada para implementarlas. 
Debe haber separados un mapa de direcciones de instrucciones y un mapa de direcciones. 
En la arquitectura Harvard se utilizan dos tipos de computadores: los microcontroladores y el DSP 
(procesador de señales digitales o digital signal processor). 
La arquitectura Harvard no se utiliza habitualmente en computadores de propósito general, sino que se 
utiliza en computadores para aplicaciones específicas. 
4. Hardware 
 
Fuente: Pexels 
Ya hemos definido Hardware como la parte física, tangible, de un sistema informático. 
 
 
 
 
Vídeo 
He preparado un repaso audiovisual sobre el Hardware, con 
anécdotas para que te resulte más ameno. También incluye 
Periféricos, que es la siguiente unidad. 
Vídeo Clase: "El Hardware". 
(Tienes el material en el Campus Virtual). 
 
 


<!-- Page 46 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
46 
Ahora vamos a estudiar los elementos de hardware más importantes, los que hacen posible que un 
ordenador realice un proceso solicitado por el usuario. 
Para entender esos elementos de hardware vamos a ver unos conceptos básicos: 
• Microprocesador. 
Es un chip (circuito integrado) que incorpora los elementos necesarios para actuar como CPU. 
• Microcontrolador. 
Circuito integrado que contiene las tres unidades funcionales de un ordenador (CPU, Memoria y 
unidad de E/S). 
• Buses. 
Es el medio físico a través del cual se comunican la CPU, memoria y unidad de E/S, un conjunto 
de conexiones eléctricas en forma de cables, o circuitos impresos, que llevan información de un 
dispositivo a otro del ordenador. 
Existen 3 tipos de buses: 
• De datos. Para el intercambio de datos. 
• De direcciones. Direcciones de memoria o de dispositivos E/S. 
• De control. Señales enviadas por la unidad de control. 
• Memoria principal. 
La memoria principal almacena las instrucciones que van a ser ejecutadas, los datos que 
utilizarán dichas instrucciones y los resultados parciales y finales derivados de la ejecución de las 
instrucciones. 
• Ancho de palabra. 
Es el número de bits que maneja en paralelo el ordenador. Hoy en día el ancho más habitual es 
32 o 64 bits. 
Tanto los datos como las instrucciones del lenguaje máquina de un ordenador se organizan en 
palabras de n bits o múltiplos de n bits. 
A mayor ancho de banda palabra, mayor potencia de cálculo. 
• Unidad de entrada/salida. 
Proporciona un camino a través del cual se comunican los distintos elementos del ordenador y 
los periféricos (hardware de entrada y salida de información). 
En los ordenadores personales, normalmente es la placa base la que ejerce esta función 
proporcionando caminos entre los distintos componentes y periféricos, pero también pueden 
hacerlo las placas externas conectadas a los slots de ampliación. 


<!-- Page 47 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
47 
ARQUITECTURA DE ORDENADORES 
Cuando hablamos de arquitectura de ordenadores, nos referimos a cómo están organizados sus 
elementos. Conocerla es importante para programar y conseguir una buena optimización. 
En los inicios de la informática, se experimentaron diferentes modelos, cada uno con sus ventajas e 
inconvenientes. 
Pero se impuso el modelo basado en la arquitectura propuesta por Von Neumann en 1945, donde la 
memoria y el procesador se comunican por medio de un bus. Y fue el modelo a seguir por la gran 
mayoría de ordenadores. 
Al principio el modelo de arquitectura era de esta forma. 
 
Este tipo de arquitectura tiene gran influencia en el rendimiento de los programas, ya que, la cantidad 
de operaciones a realizar es lo que, principalmente, determina el tiempo de ejecución de un programa. 
El programa que tenga que realizar más operaciones que otro será el más lento. Esto se denomina 
complejidad algorítmica y lo estudiaremos más adelante, pero podemos decir que, en principio, un 
programa más complejo es el que realiza más operaciones, y se ejecuta más lentamente. 
Con el incremento de la velocidad de los procesadores, (que ya predecía la ley de Moore) sucede que 
frecuentemente, el procesador no recibe los datos que necesita al mismo ritmo puede realizar las 
operaciones. La CPU es forzada continuamente a esperar hasta que los datos necesarios son 
transferidos desde o hacia la memoria, esto se denomina "cuello de botella", y determinaba el tiempo de 
ejecución de un programa. 
Este problema forzó la investigación para mejorar la transferencia de información de la memoria al 
procesador, creándose buses cada vez más rápidos y añadiendo la memoria RAM. Por ello, las 
arquitecturas modernas se desvían del modelo de von Neumann, y utilizan más de una memoria, que se 
organizan jerárquicamente. 


<!-- Page 48 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
48 
 
Arquitectura de von Neumann con jerarquía de memorias (caché y memoria principal, aliviando el 
cuello de botella) 
Además de la memoria principal, se crea la memoria caché, que es más cercana al procesador, mucho 
más rápida que la memoria principal, y con un bus más ancho que puede transportar más datos que el 
bus normal. 
Como la caché es pequeña, suele estar siempre llena. Cuando el procesador necesita guardar un dato 
nuevo en la caché, los datos más antiguos se descartan. 
Esta característica de la caché puede usarse para optimizar métodos numéricos. 
Si antes, el programa que tenía que realizar más operaciones que otro sería el más lento, ahora con la 
memoria caché, el orden en el que se realizan las operaciones es más importante que la cantidad de 
operaciones. 
En algunos ordenadores, puede haber 2 niveles de caché, existiendo una jerarquía con tres niveles de 
memoria, donde cada nivel es más lento que el anterior: 
• 1º: Caché de nivel 1 (el más rápido). 
• 2ª: Caché de nivel 2. 
• 3ª: Memoria principal (el más lento). 
La memoria y el procesador son componentes aislados, ambos conectados a la placa base del 
ordenador, físicamente a unos centímetros de distancia. 
El tiempo que tardan las señales eléctricas en llegar desde uno a otro es muy pequeño, denominado 
"latencia", pero influye en la velocidad de ejecución de los procesadores. Por este motivo, la memoria 
caché es mucho más pequeña y se monta mucho más cercana al procesador. Actualmente forma parte 
del mismo procesador. 
Actualmente, lo general es que todos los ordenadores sigan este modelo, basado como hemos visto en 
la arquitectura propuesta por Von Neumann en 1945. 


<!-- Page 49 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
49 
Por tanto, según esta arquitectura, un ordenador consta, principalmente, de tres elementos: 
• CPU: (Central Proccessing Unit o Unidad Central de Proceso), constituido por una unidad de 
Control (CU o Control Unit) y una unidad Aritmético Lógica (ALU o Aritmetich Logical Unit). 
• Memoria. 
• Unidad de entrada/salida. 
 
Arquitectura de un ordenador 
4.1. Placa base 
También denominada motherboard, mainboard o placa madre. 
La placa base es una tarjeta de circuito impreso a la que se conectan las demás partes de la 
computadora. 
La placa base integra diversos componentes: 
• BIOS. 
• Zócalo para el microprocesador. 
• Chipset. 
• Pila. 
• Zócalos de memoria. 
• Ranuras de expansión. 
• Conectores Internos. 
• Conectores de dispositivos externos. 
Vamos a ver los principales elementos de la placa base, haciendo una diferenciación entre la BIOS y el 
resto de elementos: 


<!-- Page 50 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
50 
BIOS 
El firmware (soporte lógico inalterable), es el software de más bajo nivel, que controla los circuitos 
electrónicos, que maneja físicamente al hardware. 
BIOS (Basic Input/Output System) es un programa de firmware fundamental en los ordenadores cuyo 
cometido es iniciar y verificar el hardware del sistema cuando se enciende el equipo. La fuente de 
alimentación y, concretamente, el circuito de arranque inician el encendido y activación de este 
firmware (programa integrado en el hardware). Esta rutina está integrada en una memoria ROM (Read-
Only Memory), actualmente Flash ROM (que permite una reescritura más sencilla que su predecesora), 
y generalmente se encuentra ubicada en la placa base del ordenador. 
La primera tarea que realiza esta rutina es la ejecución del POST (Power-On Self-Test), una prueba de 
autoverificación del encendido, para verificar el estado de los componentes hardware principales: 
memoria RAM, CPU, tarjeta gráfica, discos duros y otros componentes. Luego, consulta la CMOS 
(Complementary Metal-Oxide-Semiconductor), que es una memoria de tipo RAM (alimentada por la 
pila de la placa base) que almacena la configuración del sistema, la elección de velocidad de buses, los 
tipos de discos duros instalados, secuencia de arranque, información de seguridad, la contraseña de 
modificación, overclock del procesador, activación de dispositivos, etc. 
Esta memoria es una RAM de entre 64 y 256 bytes de capacidad, que está vinculada con el reloj de 
tiempo real del sistema. La tecnología CMOS de bajo consumo de esta memoria permite que sea 
alimentada por la misma pila del reloj de tiempo real de la placa base. En los primeros PC se usaba una 
batería recargable, en la actualidad se usan baterías de litio desechables tipo botón (normalmente 
CR2032). 
Tras la ejecución del POST y la consulta a CMOS y antes de que se cargue el bootloader, el usuario 
puede acceder al BIOS Setup Utility (presionando una tecla específica como DEL, F2, F10, dependiendo 
del fabricante), lo que permite modificar parámetros como el orden de arranque, habilitar o deshabilitar 
dispositivos, o configurar otros aspectos del hardware. 
Si se detecta algún problema, la BIOS puede indicar el disfuncionamiento mediante pitidos o mensajes 
de error en pantalla. Si todo está en orden, localiza y carga el bootloader. 
Por último, la BIOS ejecuta el bootloader, un pequeño programa de arranque que se encarga de cargar 
el núcleo del sistema operativo (o kernel) en la RAM, eventualmente otros módulos, y finalmente 
transfiere el control al sistema operativo. El bootloader suele encontrarse almacenado en el sector de 
arranque (MBR, en sistemas BIOS, o como archivo .efi en la partición ESP en sistemas UEFI) del 
dispositivo de almacenamiento principal. Los bootloaders varían dependiendo del sistema: en los Linux 
antiguos se usaba LILO, en los modernos se usa GRUB; en Windows, el Windows Boot Manager; y en 
Apple, iBoot, todos ellos adaptados al entorno EFI cuando se utiliza UEFI. 
En los sistemas modernos, la BIOS ha sido reemplazada en muchos casos por la UEFI cuya interfaz, con 
capacidades avanzadas, es más amigable, soporta el manejo de discos duros grandes, superiores a dos 
terabytes y el uso del ratón. 
Actualmente las motherboards incorporan modelos de ROM que permiten su escritura, para 
actualizarse a nuevas versiones creadas por el fabricante de la motherboard, permitiendo mejorar su 
funcionamiento o reconocimiento de nuevos elementos de hardware, (este proceso debe hacerse con 
sumo cuidado, en caso de error la placa dejará de funcionar, y por tanto todo el ordenador). 
Esta ROM es configurable gracias a una memoria RAM-CMOS donde se guardan los parámetros de 
configuración. 


<!-- Page 51 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
51 
 
 
 
Atención 
La Bios es memoria no volátil, lo estudiaras en el apartado de 
memoria. 
 
UEFI, El sucesor de BIOS 
UEFI, Unified Extensible Firmware Interface, traducido como la Interfaz Unificada de Firmware 
Extensible. 
UEFI es el firmware sucesor de BIOS, escrito en C, para ofrecer más recursos, (como menús gráficos, 
diagnósticos más detallados, abrir software compatible con EFI desde otras ubicaciones de 
almacenamiento, como una unidad de disco duro o un dispositivo de almacenamiento USB) y permite 
que el BIOS contenga recursos más sofisticados, como el Arranque seguro (secure boot). 
UEFI utiliza NVRAM (Non-Volatile RAM) para almacenar la configuración del sistema de manera 
persistente, eliminando la dependencia de una batería, como ocurría con la CMOS en el estándar BIOS 
tradicional. 
UEFI también introduce el uso de discos con particionado GPT (GUID Partition Table), lo que permite 
soportar discos de más de 2 TB, más particiones primarias, y una estructura de arranque más robusta y 
segura. En lugar de usar el MBR para localizar el bootloader, UEFI busca un archivo .efi en la partición 
del sistema EFI (ESP), como por ejemplo bootx64.efi. 
La Interfaz Unificada de firmware extensible (EFI-Unified Extensible Firmware Interface) es una 
especificación que define una interfaz entre el sistema operativo y el firmware que reemplaza la antigua 
interfaz del Sistema Básico de Entrada y Salida (BIOS) estándar presentado en las computadoras 
personales IBM PC como IBM PC ROM BIOS. 
Otros elementos de la Placa Base 
• Zócalo para el microprocesador. 
Es el conector donde colocamos el microprocesador. Los tipos más utilizados son: 
• Socket PGA. Los pines van en el procesador. El modelo Socket ZIF (Zero Insertion Force) 
dispone de un mecanismo con una palanca que facilita la inserción del procesador sin 
ejercer presión. (Debía insertarse en una posición determinada, ya que en una de las 
esquinas no había pines, si se hacía de forma errónea se podían torcer los pines o incluso 
romperlos, dañándose el procesador). 
• LGA. Los pines están en la placa, por lo que los microprocesadores son menos delicados, 
son lisos. También debe insertarse en una determinada posición. 


<!-- Page 52 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
52 
• Chipset. 
Conjunto de chips que regulan la forma en que interaccionan (se comunican) los distintos 
componentes conectados a la placa base. 
Actualmente se integran en el procesador. 
Las placas base, en su origen, poseían dos chipsets, North Bridge y South Bridge, que se 
interconectaban entre sí a través de un bus de datos. Únicamente el North Bridge tenía 
comunicación directa con el procesador, a través del FSB (Front Side Bus) y controlaba la 
memoria RAM, y el South Bridge se encargaba de gestionar los puertos PCI, los dispositivos de 
almacenaje, etc. 
Como cada vez que el procesador quería acceder a alguna dirección de la memoria RAM para 
grabar o recuperar datos, tenía que mandar la información a través del FSB, para que luego 
fuera mandada a través del bus de memoria hacia la RAM, se introducían latencias en el sistema. 
Actualmente North Bridge y South Bridge se integran en el procesador desapareciendo por 
consiguiente el FSB. 
Indicamos características de cada uno de los dos chipsets: 
• Northbridge (puente norte). 
Conecta la CPU con la memoria principal, y controla las funciones de acceso hacia y entre el 
microprocesador, la memoria RAM, el puerto gráfico AGP (o GPU, acrónimo de Graphics 
Processing Unit, unidad de procesamiento de gráficos), y las comunicaciones con el 
southbrigde. 
Tradicionalmente estaba formado por un único chip que integraba funciones de control 
para la memoria RAM, el puerto AGP o PCI Express y el bus PCI. 
• Southbridge (puente sur). 
Conecta la CPU con los buses USB (Universal Serial Bus), serie, audio, IDE (Integrated Drive 
Electronics) e ISA (Industry Standard Architecture), PCI es decir, el almacenamiento 
secundario y los periféricos. Está formado por un único chip. 
El South bridge es un elemento de las placas base antiguas, (comunicaba el procesador con 
elementos que requieren de poco ancho de banda), pero desde 2012 aproximadamente ya 
no existen en las placas base, sino que se encuentra integrado entre el chipset y el mismo 
procesador. 
Las funciones siguen siendo las mismas pero un poco más ampliadas, y se encuentran 
distribuidas entre el chipset de las placas base y el procesador. 
Hoy en día, las funciones del Northbridge (como el controlador de memoria y gráfico) se 
integran en el procesador, reduciendo latencias. Las del Southbridge (USB, audio, red, etc.) 
se agrupan en el chipset moderno, llamado PCH en Intel. Ya no existen físicamente como 
chips separados, pero sus funciones se conservan. Así, el procesador y el PCH asumen su 
labor conjunta. 


<!-- Page 53 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
53 
• Pila. 
Alimenta la CMOS para que no se pierdan los datos de configuración de la BIOS. 
Un síntoma claro que nos indica que la pila está fallando es cuando la fecha del sistema no es 
correcta o se pierde al apagar el ordenador. 
• Zócalos de memoria. 
Ranuras para la conexión de módulos de memoria. Lo más común es presentar un número par 
de zócalos (2, 4, 6…), agrupados de dos en dos por un color que indica el canal en el que 
trabajan. (SIMM, DDR2, DDR3). 
• Ranuras de expansión. 
• AGP: utilizado sólo para los adaptadores de pantalla de gráficos, tarjetas gráficas VGA. 
• PCIex16: han sustituido las ranuras AGP, son para las tarjetas gráficas modernas. Puede 
haber más de uno (si la placa soporta varias tarjetas). (Existe un tipo de disco duro interno 
que puede conectarse a esta ranura). 
• PCI: Bus de 32 bits para conectar diversos tipos de tarjetas de expansión (red, sonido, 
captura de video, etc.) Cada vez se usa menos. Están siendo sustituidos por PCIe. 
• PCIe x1 y x4: Son las ranuras de expansión actuales. Se utilizan para tarjetas de red 
inalámbricas, sintonizadoras TDT, capturadoras de video, etc. 
PCIe es la interfaz utilizada para la conexión de los discos SSD (estudiarás los discos SSD un 
poco más adelante). 
 
Disco de Estado Sólido conexión PCI-E 
• ISA: es muy antigua y obsoleta. (Se conectaban tarjetas de red, de imagen, modem, tarjetas 
de sonido, ampliación de puertos…) Ya no se fabrican placas base con ranuras ISA. 
Desaparecieron a partir de los modelos del microprocesador Pentium III. 
• Alimentación ATX. 
Conector a través del cual se da corriente a la placa. Actualmente tiene dos conectores MOLEX, 
uno de 24 pines, el cual proporciona la mayoría de tensiones a la placa base, y un conector 
adicional de 4 u 8 pines que suministra corriente de 12V al microprocesador. 


<!-- Page 54 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
54 
• Conectores Internos: 
• Conectores IDE: se conectan los discos duros IDE, y lectores/ grabadores de CD y/o DVD. 
• USB y de audio internos: Se suele utilizar para llevar las salidas USB y audio al frontal de la 
caja o a otros lugares de la caja. 
• Conectores Serial ATA (SATA): Se usa para conectar discos duros SATA y unidades ópticas 
que tienen este tipo de conector. La velocidad de transferencia es 3 o 6 GB/s por canal. 
• Puertos de dispositivos externos. 
La ubicación de los puertos en las computadoras dependerá del diseño de las placas base y de las 
propias carcasas. Podemos encontrar en estas máquinas puertos como minijack de 3.5mm, 
Puerto Paralelo, Ethernet (red), VGA, PS2 (teclado y ratón), USB, Firewire (conexión de 
videocámaras), DVI, HDMI o eSATA. 
A continuación, mostramos en una imagen la cronología de estos puertos. 
 
4.1.1. Chip TPM 
TPM o módulo de plataforma de confianza (Trusted Platform Module por sus siglas en inglés) un 
pequeño chip, que es un criptoprocesador seguro, que sirve para almacenar las claves de cifrado de 
Windows y proteger así la privacidad de los archivos más sensibles. 


<!-- Page 55 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
55 
TPM es el nombre de: 
• Una especificación publicada, la cual detalla un criptoprocesador seguro que puede almacenar 
claves de cifrado para proteger información. 
• También se usa como el nombre general de las implementaciones de dicha especificación, 
frecuentemente llamadas el "chip TPM" o "dispositivo de seguridad TPM". 
La especificación fue publicada por el Trusted Computing Group y actualmente se encuentra en la 
versión 2.0, estandarizada en 2016. La especificación también está disponible como el estándar 
internacional ISO/IEC 11889. TCG lanzó la Especificación de biblioteca TPM 2.0. 
Su última edición y erratas se publicaron en 2019. 
Se trata de un chip que puede estar instalado en algunas placas base, en estado pasivo, lo que significa 
desactivado de fábrica, y que, por tanto, habrá que activar manualmente mediante el software de UEFI 
o el propio Sistema Operativo. 
 
 
 
 
+ Info 
El TPM es una función utilizada por el sistema de Secure Boot, o 
arranque seguro, que es un modo para UEFI que trae Windows 
desde Windows 8, y que impide la ejecución de cualquier software 
no firmado o certificado en el arranque del sistema, por lo que por 
lo que si has desactivado Secure Boot no te aparecerá la posibilidad 
de activar el TPM en tu ordenador, y será como si no lo tuvieras. 
 
 
Este chip, ayuda a mejorar la privacidad de un ordenador de varias formas diferentes, por lo que a partir 
de 2016 se solicitó a todos los fabricantes que incluyeran ese chip TPM en su versión 2.0 en sus 
ordenadores con Windows, ya que sería un requisito imprescindible para poder utilizar la versión 
Windows 11. (Aunque existen métodos para instalar Windows 11 en equipos sin TPM, Microsoft ha 
indicado que estos ordenadores tendrán más errores, y no recibirán actualizaciones). 
Existen varias versiones del chip TPM, y la última es la 2.0, (donde se implementó el almacenamiento de 
datos biométricos). 
No todos los ordenadores tienen este chip TPM. Algunas placas base lo traen integrado, pero la mayoría 
simplemente tienen un cabezal para instalarlo si quieres, de forma que si tu fabricante no lo puso 
puedas añadirlo de forma manual. 
Muchos de los términos que indicamos a continuación como características del chip, las estudiaras en el 
Bloque IV Sistemas y comunicaciones. 


<!-- Page 56 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
56 
Características del chip: 
• Sólo se comunica con el procesador de tu ordenador. 
Cuando está activado el TPM solo recibe comandos y datos de la CPU local, realiza su trabajo y 
devuelve los resultados, por tanto, ningún otro componente del equipo puede acceder a datos 
sin el permiso del propio procesador, lo que dificulta que un virus se instale en el disco duro y 
pueda acceder a claves criptográficas, ya que no tendrá contacto directo con el chip. 
• Permite almacenar contraseñas de administrador, las de los sistemas DRM de protección de 
datos, o permitir el cifrado de unidades de almacenamiento o carpetas y archivos. 
• Permite que los clientes con características de firma digital puedan enviar correos electrónicos 
de forma segura, o almacenar los datos biométricos de inicio de sesión. 
• Permite almacenar certificados digitales, lo que mejora la navegación segura con SSL, y puede 
también tener usos para las redes privadas virtuales o VPN. 
En cuanto a seguridad provee: 
• Memoria tanto volátil como no volátil. 
El almacenamiento no volátil es resistente a modificaciones, se usa por ejemplo para almacenar 
claves no migrables (Ej. Endorsement Key y Storage Root Key). 
Y el almacenamiento volátil se usa para almacenar de forma segura las mediciones de integridad 
realizadas para conseguir la computación confiable. 
• Generador de números aleatorios seguro. 
• Algoritmos de generación de claves. 
• Funciones criptográficas como cifrado/descifrado RSA y funciones hash. 
• Funcionalidades para permitir que la plataforma sea confiable: 
• Proporcionar mediciones e informes seguros de la integridad. 
Permite obtener mediciones de integridad y los resultados pueden ser almacenados de 
forma segura dentro del TPM, y basándose en estas medidas, un TPM puede ser usado para 
obtener un informe verificable que refleje la integridad del estado de la plataforma. 
• Sellado de datos. 
Los datos pueden ser almacenados de tal forma que solo sean accesibles si el usuario se 
autentifica satisfactoriamente y si la plataforma tiene cierto estado de integridad. 


<!-- Page 57 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
57 
4.2. CPU (procesador) 
Es uno de los componentes más importantes del ordenador, el procesador 
CPU, siglas de Central Processing Unit, en español Unidad Central de Proceso. 
Se encarga de gobernar el equipo y realizar todas las operaciones aritméticológicas. Un procesador está 
compuesto por millones de transistores dentro de un circuito integrado. 
 
Procesador Intel Core i9-10900X 
LGA2066 X299 
Está formada por dos unidades funcionales ALU y CU. Y cómo consecuencia de la CU, el Reloj: 
CPU 
ALU: La unidad aritmético-
lógica 
(ALU Arithmetic-Logical Unit) 
CU: La unidad de control 
(CU o Control Unit) 
RELOJ 
Efectúa operaciones lógicas y 
aritméticas sobre datos que 
provienen de la memoria 
principal, los operandos de 
entrada para la ALU. 
Estos datos se pueden almacenar 
de forma temporal en los 
registros de la ALU para 
aumentar la velocidad, dado que 
el acceso a los registros es 
mucho más rápido. 
Se encarga de supervisar la transferencia de 
información; de leer las instrucciones en 
código máquina que están en la memoria 
principal y de generar las señales de control 
para los elementos del computador que 
participarán en la ejecución de cada 
instrucción. 
Contiene el registro de instrucción (IR), que 
indica la instrucción a ejecutar (que se está 
ejecutando). 
Es un circuito síncrono, por lo que requiere 
de un reloj. 
Es un oscilador de 
frecuencia fija que se mide 
en megahercios. Marca la 
velocidad de ejecución de 
las instrucciones. 
A mayor índice de 
frecuencia, más rápido es 
el procesador. 


<!-- Page 58 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
58 
CPU 
ALU: La unidad aritmético-
lógica 
(ALU Arithmetic-Logical Unit) 
CU: La unidad de control 
(CU o Control Unit) 
RELOJ 
Sus principales componentes 
son: 
- Operador aritmético-lógico 
- Registros 
 
 
La gestión física de los periféricos la realiza la CU, que es la encargada de 
gestionar las “interrupciones”, pero en algunos casos, (como por ejemplo en la 
salida a pantalla de una imagen en alta resolución), también necesita la ALU, y en 
realidad, prácticamente en todos los periféricos de uso común. 
El mantener esa separación es porque en determinados dispositivos de hardware, 
ciertos periféricos de comunicaciones tienen buses especiales que no necesitan 
de la ALU. 
 
La velocidad de un procesador viene determinada, principalmente por la frecuencia del reloj, aunque 
también depende de otros factores, como el número de núcleos, la tecnología utilizada o la complejidad 
del juego de instrucciones (lenguaje máquina). 
La frecuencia se mide en hercios. En la actualidad se habla de Megahercios (106 hercios) y de 
Gigahercios (109 hercios). 
La capacidad de un procesador depende fuertemente de los componentes restantes del sistema, sobre 
todo del chipset, de la memoria RAM y del software. Pero obviando esas características puede tenerse 
una medida aproximada del rendimiento de un procesador por medio de indicadores como la cantidad 
de operaciones de coma flotante por unidad de tiempo FLOPS, o la cantidad de instrucciones por 
unidad de tiempo MIPS. 
Una medida exacta del rendimiento de un procesador o de un sistema, es muy complicada debido a los 
múltiples factores involucrados en la computación de un problema, por lo general las pruebas no son 
concluyentes entre sistemas de la misma generación. 
4.2.1. Unidad aritméticológica 
La unidad aritmética es el elemento encargado de procesar los datos, ejecutando las operaciones 
aritméticas y lógicas requeridas en función del programa que se está ejecutando. 
La unidad de control del computador se encargará de enviarle los datos correspondientes y de indicarle 
qué operación ha de realizar. Posteriormente recogerá los resultados de las operaciones de los registros 
destinados a este fin. 


<!-- Page 59 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
59 
La ALU realiza tres tipos de operaciones: 
• Aritméticas. 
• Lógicas. 
• De desplazamiento. 
4.2.1.1. Operaciones aritméticas 
Las operaciones más importantes que puede realizar la ALU son: 
• Sumar y restar. 
• Multiplicación y división. 
• Cambio de signo. 
• Extensión de signo. Consiste en aumentar el número de bits, manteniendo el mismo valor y 
signo. 
Para ejecutar dichas operaciones utiliza los siguientes dispositivos: 
• Dispositivo de adición: sirve para calcular las operaciones de suma, resta, multiplicación y 
división (estas tres últimas operaciones pueden realizarse por medio de múltiples operaciones 
de suma o cambiando el signo). 
• Registros: se utilizan para contener los operandos, los resultados parciales que se van 
obteniendo en las distintas operaciones y los resultados finales. 
• Dispositivo de control de cálculo: dirige y controla las operaciones de cálculo que se realizan en 
la ALU. 
• Comparador: Circuito que puede comprobar si dos datos son iguales o cuál es mayor o menor. 
4.2.1.2. Operaciones lógicas 
Pueden ser operaciones lógicas Directas y operaciones lógicas negadas 
Operaciones lógicas Directas 
• Igualdad. 
Puerta SI o buffer. 


<!-- Page 60 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
60 
ENTRADAS A 
SALIDAS A 
0 
0 
1 
1 
• Producto (AND). 
Dos entradas. Será uno si las dos entradas son uno. 
• Suma (OR). 
Dos entradas. Será uno si al menos una de las entradas vale uno. 
• Suma exclusiva (Puerta OR-exclusiva XOR). 
Dos entradas. Será uno si una de las entradas es uno (pero no las dos). 
Para entenderlo mejor, lo vemos en la siguiente tabla. 
Las dos primeras columnas (A y B) son las entradas y el resto las salidas resultantes de la operación. 
Gráfico Operaciones Lógicas Directas 
ENTRADAS 
SALIDAS 
A 
B 
A AND B 
A OR B 
A XOR B 
0 
0 
0 
0 
0 
0 
1 
0 
1 
1 
1 
0 
0 
1 
1 
1 
1 
1 
1 
0 
Operaciones lógicas negadas 
• NOT (Negación). 
Una sola entrada. Si la entrada es 0, la salida es 1 y viceversa. 
ENTRADAS A 
SALIDAS A 
0 
1 
1 
0 


<!-- Page 61 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
61 
• NAND (Puerta NO-Y). 
La puerta lógica NO-Y, más conocida por su nombre en inglés NAND, realiza la operación de 
producto lógico negado. En ocasiones es llamada también barra de Sheffer. 
• NOR (Puerta NO-O). 
Llamada también barra de Pierce. 
Dos entradas. 
• XNOR (No-exclusiva, Puerta NOR-exclusiva). 
Dos entradas. 
Será uno si una de las entradas es uno (pero no las dos). Puerta XNOR con Esta puerta al ser el 
complemento de la puerta OR exclusiva (XOR), sus resultados son uno (1) cuando sus entradas, 
para el caso de 2, son iguales, ya sean con valor 0 o valor 1 (0 y 0, o 1 y 1). Para más de 2 
entradas, si el número de unos de entradas es par, la salida es 1 y si es impar, la salida es 0. Si 
todas las entradas son 0, la salida es 1, como puede comprobarse en la tabla de verdad de tres 
entradas. La puerta lógica XNOR se identifica como función par, en tanto que la puerta lógica 
XOR se identifica como función impar. 
Gráfico Operaciones lógicas negadas 
ENTRADAS 
SALIDAS 
A 
B 
NO-Y (NAND) 
NO-O (NOR) 
NOR-exclusiva XNOR 
0 
0 
1 
1 
1 
0 
1 
1 
0 
0 
1 
0 
1 
0 
0 
1 
1 
0 
0 
1 
 
XNOR con tres entradas 
Entrada A 
Entrada B 
Entrada C 
Salida XNOR 
0 
0 
0 
1 
0 
0 
1 
0 
0 
1 
0 
0 


<!-- Page 62 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
62 
XNOR con tres entradas 
Entrada A 
Entrada B 
Entrada C 
Salida XNOR 
0 
1 
1 
1 
1 
0 
0 
0 
1 
0 
1 
1 
1 
1 
0 
1 
1 
1 
1 
0 
 
 
 
 
+ Info 
Si lo deseas, aunque no lo consideramos necesario, puedes ampliar 
tus conocimientos sobre este tema profundizando en dos puntos: 
• Álgebra de Boole. 
• Puertas lógicas. 
 
4.2.1.3. Operaciones de desplazamiento 
Las operaciones de desplazamiento de bits desplazan o rotan una palabra en un número específico de 
bits hacia la izquierda o la derecha, con o sin extensión de signo. 
Estos desplazamientos pueden ser interpretados como multiplicaciones o divisiones por dos. 
4.2.2. Unidad de control 
Sus funciones principales son controlar, coordinar e interpretar las instrucciones de los programas. 
La unidad de control extrae instrucciones de la memoria, las descifra y las ejecuta. En caso de ser 
necesario puede llamar a la ALU, encargándose también de proporcionarle operandos y transportar los 
resultados. 


<!-- Page 63 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
63 
Pasos para ejecutar la instrucción 
Los pasos para ejecutar una instrucción son los siguientes: 
• Ciclo de fetch. 
Extraer de la memoria la siguiente instrucción, indicada por el contador de programa. 
• Decodificar la instrucción leída. 
• Ciclo Execute. 
Ejecutar la instrucción. 
• Aumentar el contador de programa. 
Para que contenga la siguiente posición de memoria, la cual contiene la siguiente instrucción. 
Volver al primer paso. 
4.2.2.1. El contador de programa (Ingles: Program Counter) 
También se le llama contador de instrucción o puntero de instrucciones (Instruction Pointer), indica en 
qué posición está en procesador en la secuencia de instrucciones (la instrucción que es ejecutada, o la 
dirección de la próxima instrucción a ser ejecutada. 
Es incrementado automáticamente en cada ciclo de instrucción de forma que la dirección de la 
siguiente instrucción a ser ejecutada siempre se encuentra en el contador de instrucción. 
4.2.2.2. Gestionar la comunicación con los periféricos 
Otra función de la unidad de control es gestionar la comunicación con los periféricos, procesando la 
información transmitida desde o hacia los periféricos. 
Existen dos tipos de unidades de control: 
• Cableadas: los componentes principales son el circuito de lógica secuencial, el de control de 
estado, el de lógica combinacional y el de emisión de reconocimiento de señales de control. Son 
más sencillas pero difíciles de actualizar o modificar. 
• Microprogramadas: la microprogramación de la unidad de control se encuentra almacenada en 
una micromemoria, a la cual se accede de manera secuencial para posteriormente ir ejecutando 
cada una de las microinstrucciones. Son más complejas, pero se pueden modificar más 
fácilmente. 


<!-- Page 64 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
64 
4.2.3. Reloj del Sistema 
La Unidad de Control contiene el reloj de sistema, el cual oscila con una frecuencia de millones de veces 
por segundo. La velocidad a la que el procesador realiza las operaciones viene determinada por dicho 
reloj y se mide en gigahercios (GHz), es decir, 109 ciclos por segundo. 
Frecuencia 
La cantidad de operaciones por segundo que puede realizar un procesador se conoce como frecuencia. 
A finales de los años 90 del siglo pasado, un procesador doméstico podía tener una frecuencia de 400 o 
500 MHz en el mejor de los casos. Eso implica que era capaz de hacer entre 400 y 500 millones de 
operaciones por segundo. 
En la actualidad, es fácil encontrar procesadores domésticos de 3 GHz, es decir, que son capaces de 
hacer 3000 millones de operaciones por segundo. Además, los ordenadores modernos suelen 
incorporar más de un procesador, trabajando todos los procesadores a la vez. 
4.2.4. Arquitectura de procesadores 
Existen diferentes arquitecturas de procesadores que hacen que el funcionamiento y rendimiento del 
mismo sea diferente. 
Vamos a ver: 
• Arquitectura CISC. 
• Arquitectura RISC. 
• Arquitectura ARM. 
4.2.4.1. CISC y RISC 
La diferencia principal entre CISC Y RISC, es el número de instrucciones y su complejidad 
Ambos tipos se basan en la arquitectura de Von Neumann. 
Existen 2 tipos de procesadores, según la arquitectura que utilizan, que determina la complejidad de las 
intrusiones máquina a ejecutar. 
• CISC (Complex Instruction Set Computer). Ordenadores con un conjunto de instrucciones 
complejo. 
El objetivo de este Set de instrucciones es la de facilitar la programación reduciendo el número 
de instrucciones (que no de operaciones) para realizar una tarea. 


<!-- Page 65 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
65 
CISC trabaja con instrucciones complejas tal y como su nombre indica, suelen integrar múltiples 
operaciones en una sola (como direccionamiento de memoria, cálculos y almacenamiento) en 
cada instrucción. Por ello mismo necesitará de varios ciclos de reloj para completarla. 
La microprogramación es una característica esencial. 
Características: 
• Complejidad en instrucciones-decodificación. 
• Se necesita una instrucción para soportar múltiples modos de direccionamiento. 
• Teniendo en cuenta, la enorme cantidad de instrucciones que la CPU puede manejar, la 
construcción de una CPU con arquitectura CISC es muy compleja. 
• El hardware Intel está basado en CISC. 
• RISC (Reduced Instruction set computer). Ordenadores con un conjunto de instrucciones 
simples. 
Tiene mucho mayor rendimiento que el CISC. El procesador realiza una superposición en la 
ejecución de varias instrucciones en un pipeline. 
Un pipeline (tubería o cauce), consiste en una cadena de procesos conectados de tal forma que 
la salida de cada elemento de la cadena es la entrada del próximo. Es una técnica para 
implementar simultaneidad a nivel de instrucciones dentro de un solo procesador. Permiten la 
comunicación y sincronización entre procesos. 
Pipelining intenta mantener ocupada a cada parte del procesador, dividiendo las instrucciones 
entrantes en una serie de pasos secuenciales, que se realizan por diferentes unidades del 
procesador que trabajan de forma simultánea. 
Utiliza un conjunto de instrucciones altamente optimizado, reduciendo los ciclos por instrucción 
en el costo de la serie de instrucciones por pipeline de programa. 
Características: 
• El repertorio de instrucciones es sencillo y limitado. El objetivo principal es la optimización 
de instrucciones. 
• Reciben instrucciones simples, y tratan de ejecutarse dentro de un ciclo de reloj. 
• Tiene un gran número de registros de uso general. 
• Los diferentes dispositivos de Apple trabajan con arquitecturas RISC concretamente ARM 
para sus SoC (System on Chip) ya sea en sus iPhones, iPads o Macs. Tras abandonar los 
procesadores Intel, Apple y sus Macs incorporan procesadores de marca propia como M1, 
M1 Pro, M1 Max y M2. 


<!-- Page 66 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
66 
Comparativa entre CISC Y RISC 
Veamos algunas de las diferencias entre ambos: 
 
4.2.4.2. Arquitectura ARM 
ARM es una arquitectura RISC de 32 bits y recientemente con la llegada de su versión V8-A también 
de 64 Bits desarrollada por ARM Holdings 
Los procesadores ARM (Advanced RISC Machine: Máquina RISC Avanzada) surgen del auge de la 
informática móvil, que tiene unos determinados requisitos, como, por ejemplo, baterías y fuentes de 
energía más pequeñas, no disponer de espacio para sistemas de refrigeración, por tanto, el diseño de los 
procesadores debe ser diferente. 


<!-- Page 67 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
67 
El leitmotiv de ARM es tratar de obtener la máxima eficiencia con el menor consumo energético, para 
ello y continuando con la filosofía RISC su objetivo es proporcionar sets de instrucciones y procesadores 
que se lo permitan. 
Esto permite una reducción en el tamaño del código, el ancho de banda necesario y la cantidad de 
instrucciones que deben procesarse, lo cual se traduce en un menor consumo energético. 
Las evoluciones de ARM, con los procesadores Cortex (a partir de 2005), incorporan la arquitectura de 
64 bits, manteniendo la compatibilidad con la tecnología Thumb. Esto permite aceptar instrucciones 
más largas mientras se sigue beneficiando de una mayor eficiencia tecnológica. Manteniendo la 
compatibilidad con instrucciones de 16 bits (Thumb y Thumb2) y 32 bits, las arquitecturas ARMv8-A y 
ARMv9-A han ampliado significativamente su conjunto de instrucciones a 64 bits, ofreciendo un 
equilibrio entre la ejecución de código heredado y el aprovechamiento de las últimas innovaciones en 
procesamiento. 
Además, ARM desarrolla sistemas avanzados de gestión de energía que permiten a los procesadores 
entrar en estados de bajo consumo cuando no están activos. También optimiza su pipeline (reduciendo 
la latencia y mejorando la eficiencia) y su caché para mejorar el rendimiento general. 
ARM ha sido desarrollada por la multinacional ARM Holdings, y es una arquitectura licenciable, es decir 
que ARM Holdings no fabrica los procesadores por sí misma, diseña la tecnología y desarrolla el 
estándar y luego la licencia a otras empresas. 
Las empresas que son titulares de licencias ARM crean microcontroladores y CPUs basados en este 
núcleo, lo que hace que existan muchas variantes de este tipo de procesadores. 
Versiones del estándar: ARMv1, ARMv2, ARMv3, ARMv4, ARMv4T, ARMv5, ARMv6, ARMv7, ARMv8-A, 
ARMv8-R, ARMv9-A. 
En un inicio ARM se utilizaba en dispositivos móviles y Smart TV, pero los procesadores con 
arquitectura ARM pueden ser utilizados como CPU de un ordenador, y también en otros nichos de 
mercado, como el de los microcontroladores, los cuales son procesadores que incluyen la memoria RAM 
en el mismo chip y se utilizan por ejemplo para el control de electrodomésticos. 
AÑO 
Procesadores 
Tecnologías 
Clave 
Descripción General 
1985 
ARM1 
ARM 
Primer procesador ARM, 32 bits 
1986 
ARM2 
ARM 
Primera versión utilizada comercialmente 
1991 
ARM610 
ARM 
Ampliamente utilizado en sistemas embebidos 
1994 
ARM7TDMI 
ARM, Thumb 
Base para muchos dispositivos portátiles y PDA. 
Introducción de Thumb para reducir el tamaño del 
código. 
1996 
ARM9TDMI 
ARM, Thumb 
Utilizado en sistemas embebidos y dispositivos móviles 
de gama baja. 


<!-- Page 68 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
68 
AÑO 
Procesadores 
Tecnologías 
Clave 
Descripción General 
2005 
ARM11MPCore 
ARM, Thumb 
Base para muchos dispositivos móviles y embebidos. 
2011 
Cortex-A7, Cortex-M3, 
Cortex-M4, StrongARM 
SA1100 
ARM, Thumb, 
Thumb-2 
Ampliamente utilizada en dispositivos móviles, 
embebidos y microcontroladores. Buen equilibrio entre 
rendimiento y eficiencia energética. Introducción de 
Thumb-2 para mayor flexibilidad y rendimiento. 
2013 
Cortex-A53, Cortex-A57, 
Cortex-A72, Cortex-A73, 
Neoverse N1 
ARM, Thumb, 
Thumb-2 
Diseñada para aplicaciones de alto rendimiento. Soporta 
64 bits y ofrece alto rendimiento por vatio. 
2017 
Cortex-R52, Cortex-R5F 
ARM, Thumb, 
Thumb-2 
Optimizada para aplicaciones de tiempo real y seguridad. 
2021 
Cortex-X2, Cortex-A78, 
Cortex-A510, Neoverse 
V1 
ARM, Thumb, 
Thumb-2 
Última generación, diseñada para ofrecer mayor 
rendimiento y eficiencia energética. 
4.2.5. Núcleo físico y lógico 
Hay que diferenciar lo que es un núcleo físico de un núcleo lógico. 
• Un núcleo físico (o core) es un circuito integrado físico ubicado en el chip del procesador. 
• Un núcleo lógico no tiene su propia unidad de ejecución, sino que comparte la unidad de 
ejecución del núcleo físico en el que se ejecuta. Solo el sistema operativo entiende que existe. 
Un núcleo físico es una unidad de procesamiento que puede ejecutar un hilo a la vez, y se compone 
entre otros elementos de una ALU, UC, registros y memoria caché (L1, L2 y la L3 que puede ser 
compartida en algunos casos siempre que cuente con ella y existan más núcleos físicos). Aunque el flujo 
de ejecución es secuencial, un núcleo moderno puede ejecutar varias instrucciones de manera 
simultánea gracias a técnicas como el pipeline y la ejecución superescalar. 
Si se tiene más de un núcleo físico se pueden realizar varias operaciones de forma simultánea (una por 
núcleo) en cada ciclo de reloj, mejorando por tanto mucho el rendimiento. 
Los primeros procesadores únicamente tenían un núcleo físico, pero ahora tienen de media entre 4 a 18 
núcleos, incluso pueden tener 128 núcleos. 
En cuanto a un thread, es cada uno de los flujos de control de datos que el sistema operativo crea al 
subdividir los programas para su ejecución en memoria y poder repartirlas en los núcleos de procesador. 
Es necesario que el sistema operativo tenga que cargar en memoria los programas para poder ser 
ejecutados, y los subdivide en tareas o flujos de control de datos (thread). Cada uno de estos thread se 
irán gestionando u ordenando perfectamente para ser procesados, aunque el sistema operativo no 
siempre subdivide un programa en varios hilos; esto dependerá de si el propio programa está diseñado 
para ser multihilo. 


<!-- Page 69 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
69 
No todo procesador tendrá más de un núcleo lógico por núcleo, es necesario que disponga de una 
tecnología para ello: 
• Intel crea núcleos lógicos en sus procesadores mediante la tecnología Hyper Threading. 
• AMD crea núcleos lógicos en sus procesadores mediante la tecnología SMT en toda su gama 
Ryzen. 
Estas tecnologías permiten trabajar en cada uno de los núcleos lógicos reconocidos por el sistema 
operativo, pero los núcleos lógicos comparten recursos físicos, el núcleo (UC, ALU, cachés L1 y L2, 
etc.). La simultaneidad real entre hilos solo es posible cuando se cuenta con más de un núcleo físico, ya 
que los núcleos lógicos comparten los mismos recursos internos. Las múltiples ALU dentro de un núcleo 
permiten simultaneidad de instrucciones, pero no simultaneidad plena de hilos. 
Cada thread, unidad mínima de ejecución independiente, cuenta con una porción de instrucciones, un 
contador de programa que apuntará a la instrucción siguiente a ejecutar y una pila que almacenará 
variables y gestionará las funciones invocadas por esa porción (llamadas y resultados). Y como 
decíamos, un thread puede ejecutarse de manera singular (un hilo por núcleo) o puede coexistir de 
manera concurrente con otro hilo en el mismo núcleo si el procesador dispone de tecnologías como 
SMT o Hyper-Threading. 
Un procesador que no incorpora tecnologías como SMT o HyperThreading no dispone de núcleos 
lógicos; en ese caso, cada núcleo físico corresponde a un único hilo de ejecución. 
 
 
 
 
Info 
• Instrucción: Es la unidad más pequeña de trabajo en un 
programa de computadora. Las instrucciones son las 
operaciones elementales que realiza la CPU. 
• Programa: agrupación de instrucciones que, cuando se 
ejecutan por la computadora, realizan una tarea específica 
o resuelven un problema determinado. 
• Proceso: es la instancia en ejecución de un programa. Un 
proceso se crea cuando se ejecuta un programa y contiene 
su propio espacio de memoria, recursos del sistema, 
identificador de proceso (PID) y una o más unidades de 
ejecución llamadas hilos. 
 


<!-- Page 70 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
70 
 
 
 
• Hilo (Thread): Es una unidad básica de ejecución dentro de 
un proceso. Los hilos comparten recursos como memoria y 
archivos abiertos dentro del proceso y pueden ejecutar 
instrucciones de manera independiente sin necesitar 
necesariamente esperar a que otro hilo termine su 
ejecución para continuar con sus operaciones, a menos que 
estén compartiendo el mismo núcleo físico, en cuyo caso 
pueden llegar a competir por los recursos de ejecución y 
requerir esperas. 
 
4.3. Memoria 
 
Fuente: Public domain vectors 
Es uno de los elementos esencial para el funcionamiento del ordenador y su velocidad de proceso. 
Vamos a ver unos conceptos imprescindibles para entender los tipos y clasificación de memoria. 
Memoria Volátil o no volátil 
Es un término referido al almacenaje o no de la información: 
• Memoria Volátil: cuando se apaga el ordenador, se corta el suministro de corriente eléctrica, la 
información se pierde, no es almacenada. Es una memoria que se utiliza para llevar a cabo 
diferentes procesos mientras utilizamos el ordenador. 


<!-- Page 71 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
71 
• Memoria No volátil: cuando se apaga el ordenador, se corta el suministro de corriente eléctrica, 
la información no se pierde, se mantiene almacenada. 
Son memorias tipo NVRAM, y también los dispositivos de memoria secundaria o 
almacenamiento (discos duros, pen drive, CD, DVD etc.). 
 
 
 
 
Anécdota 
En ocasiones ante un apagado incorrecto del ordenador, por corte 
de luz o forma del usuario incorrecta de apagarlo, puede dañarse 
algún fichero que este en uso en ese momento, perdiendo los 
últimos cambios realizados o incluso volviéndose ilegibles. 
 
4.3.1. Tecnologías 
Tecnología NVRAM 
Es una tecnología que permite que las memorias sean no volátiles. 
Memoria de acceso aleatorio no volátil (Non-volatile random access memory). 
NVRAM es una memoria de acceso aleatorio que es capaz de almacenar información y no perderla al 
retirar la alimentación eléctrica del componente. Son: 
• EAROM. 
• EEPROM. 
• EPROM y flash EEPROM. 
Tecnología Flash NAND 
El término flash es debido a la alta velocidad que puede manejar y NAND a un tipo de conexión especial 
de sus elementos electrónicos (compuerta tipo NAND). 
Son memorias que permite almacenar datos y mantenerlos almacenados sin necesidad de alimentación 
eléctrica durante más de 10 años (cantidad que va aumentando con la rápida evolución del desarrollo 
de hardware). 
Se utiliza en las memorias USB, memorias SD, MemoryStick de Sony, unidades SSD, para BIOS, 
etcétera. 


<!-- Page 72 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
72 
Tecnología dual channel 
Es una tecnología que permite el incremento del rendimiento gracias al acceso simultáneo a dos 
módulos distintos de memoria RAM. Esto se consigue mediante un segundo controlador de memoria en 
el Northbridge. Para que el ordenador pueda funcionar en Dual Channel, se debe de tener dos módulos 
idénticos de memoria en los slots correspondientes de la placa base, y el chipset de la placa base debe 
soportar dicha tecnología. 
4.3.2. Clasificación 
Existen varias clasificaciones, en función de diferentes enfoques, pero la más utilizada, es la que divide la 
memoria en primaria y secundaria. Y la memoria Flash. 
• Memoria Primaria. 
• ROM (Read-Only Memory). 
» ROM. 
» Y ROM más modernas como: 
» PROM (Programmable ROM). 
» EPROM (Erasable Programmable ROM). 
» EEPROM (Electrically Erasable Programmable ROM). 
• RAM (Ramdom Access Memory). 
» RAM. 
» DRAM. 
» FPM DRAM. 
» EDO RAM. 
» BEDO RAM. 
» SDRAM. 
» RDRAM. 
» DDR. 
• Cache. 


<!-- Page 73 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
73 
• Memoria Secundaria. 
• Swap. 
• Disquettes. 
• Soportes ópticos. 
• Discos Duros. 
» Magnéticos. 
» IDE. 
» SATA. 
» SSD (solid-state disk). 
• La memoria flash. 
4.3.2.1. Memoria primaria 
Se divide en celdas identificadas mediante una dirección y que están formadas por bloques de circuitos 
integrados o chips. Estas celdas almacenan información binaria. 
Se comunica con el procesador mediante el bus de direcciones. 
Es mucho más rápida que la secundaria, pero tiene menor capacidad. 
Se puede clasificar en 3 tipos: 
• ROM. 
• RAM. 
• Cache. 
4.3.2.1.1. Memorias ROM (Read Only Memory) 
Son memorias no volátiles, de sólo lectura (no se puede escribir en ella). 
En la ROM, se almacena la BIOS, que contiene los programas necesarios para el arranque y las rutinas 
para las operaciones básicas de entrada y salida (se almacena cualquier contenido vital para el 
funcionamiento del equipo como el programa de arranque). 


<!-- Page 74 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
74 
Podemos clasificarlas en 4 tipos: 
• ROM (Read-Only Memory). 
• Y ROM más modernas como: 
• PROM (Programmable ROM). 
• EPROM (Erasable Programmable ROM). 
• EEPROM (Electrically Erasable Programmable ROM). 
Como indica su nombre, no son solo de lectura, pueden borrarse y volver a programarse un 
determinado número de veces, aunque este proceso es lento y poco frecuente. 
Estas han sustituido a las antiguas memorias ROM, las cuales no se utilizan en los 
ordenadores actuales. 
(La EEPROM sirve incluso como base para la memoria flash utilizada en las unidades SSD 
que ahora están disponibles en capacidades de datos de un terabyte o más). 
Vamos a ver un cuadro con diferentes memorias ROM 
Tipo ROM 
ROM 
Read Only Memory: memoria de 
solo lectura 
Memoria que permite leerse, pero no permite la escritura 
PROM 
Programmable Read Only Memory: 
memoria programable de solo 
lectura 
Memoria ROM que permite una programación y 
posteriormente un número indeterminado de lecturas, pero 
no puede ser modificada 
EPROM 
Erasable Programmable Read Only 
Memory: memoria programable y 
borrable de solo lectura 
Memoria PROM que permite reprogramación por medio de 
un dispositivo especial y borrado por medio de luz 
ultravioleta 
EEPROM 
"Electrically Erasable Programmable 
Read Only Memory", memoria 
eléctricamente programable y 
borrable de solo lectura 
Evolución de las memorias EPROM que permite alterar su 
contenido (borrar y grabar repetidas veces) por medio de 
señales eléctricas. Es la más utilizada en las computadoras 
actuales para albergar el programa de arranque del 
ordenador 
4.3.2.1.2. Memorias RAM (Random Access Memory) 
Es la memoria de donde el procesador obtiene las instrucciones que debe procesar y donde guarda los 
resultados. 
Es memoria volátil. 


<!-- Page 75 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
75 
Se le denomina memoria de acceso aleatorio (random access) porque el tiempo de espera en la lectura 
o escritura es el mismo para cualquier posición de la memoria, por lo que la información no tiene por 
qué estar ordenada para aumentar su rendimiento. 
Se usa como memoria de trabajo para el sistema operativo y los programas. 
Vamos a ver un cuadro con diferentes memorias RAM 
Tipo de 
Memoria 
Significado 
Descripción 
RAM 
Random Access Memory, 
memoria de acceso 
aleatorio 
Memoria primaria de la computadora, en la que puede leerse y 
escribirse información en cualquier momento, pero que pierde la 
información al no tener alimentación eléctrica. 
DRAM 
Dyamic Random Access 
Mrmory, memoria 
dinámica de acceso 
aleatorio. 
Memoria construida con capacitores que necesitan refrescar el 
dato que tienen almacenado ralentizando el proceso. 
FPM 
DRAM 
Fast Page Mode Dynamic 
Random Access memory, 
memoria dinámica de 
paginación de acceso 
aleatorio. 
Aumentan el rendimiento a las direcciones mediante páginas. Fue 
una de las primeras formas de DRAM que permite un acceso rápido 
a múltiples ubicaciones dentro de una fila de memoria sin tener que 
especificar la fila a cada vez. 
EDO RAM 
Extenden Data Out 
Random Access Memory, 
memoria de acceso 
aleatorio con salida de 
datos extendida 
Tecnología que permite acortar el camino de la transferencia de 
datos entre la memoria y el microprocesador. 
BEDO 
RAM 
Burst EDO Random Access 
Memory, memoria de 
acceso aleatorio con salida 
de datos extendida y 
acceso Burst. 
Se trata de una memoria EDO RAM que mejora su velocidad gracias 
al acceso sin latencias a direcciones contiguas de memoria. 
SDRAM 
Synchronous Dynamic 
Random Access Memory: 
memoria dinámica de 
acceso aleatorio. 
Tecnología DRAM que utiliza un reloj para sincronizar con el 
microprocesador la entrada y salida de datos en la memoria de un 
chip. Se ha utilizado en las memorias comerciales como SIMM, 
DIMM y actualmente en la familia de las memorias DDR. 
RDRAM 
Rambus DRAM, memoria 
dinámica de acceso 
aleatorio para tecnología 
Rambus. 
Memoria DRAM de alta velocidad desarrollada para procesadores 
con velocidad superior a 1 GHz. En esta clasificación se encuentra 
la familia de las memorias RIMM. 


<!-- Page 76 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
76 
Tipo de 
Memoria 
Significado 
Descripción 
DDR 
Double Data Rate SDRAM, 
SDRAM de doble velocidad 
de datos. 
Se introduce a finales de los años 90 y principios de siglo XXI, 
significa una mejora importante en la velocidad y la eficiencia con 
respecto a la tecnología SDRAM. Posibilita la transmisión de datos 
dos veces por ciclo de reloj. Las variantes de DDR han 
evolucionado con el tiempo, aumentando la velocidad y la 
eficiencia en comparación con sus predecesoras. 
 
 
 
 
Nota 
La memoria DDR fue introducida en el año 2000 con la DDR1 con 
velocidades de hasta 200 MHz, el bus de datos utilizado es de 64 
bits, posteriormente tenemos la DDR2 (2003), DDR3 (2007), 
DDR4 (2014) y DDR5 (2020). 
La generación DDR elegida dependerá de la compatibilidad con el 
hardware existente. 
 
4.3.2.1.3. Cache (SRAM) 
Static Random Access Memory: memoria estática de acceso aleatorio. 
Memoria RAM muy veloz y relativamente cara, construida con transistores, que no necesitan de 
proceso de refresco de datos. Anteriormente había módulos de memoria independientes, pero 
actualmente solo se encuentra integrada dentro de microprocesadores y discos duros para hacerlos 
más eficientes. 
4.3.2.2. Memoria secundaria (almacenamiento permanente) 
Es una memoria permanente (no se borra al apagar el ordenador) 
La memoria secundaria es un conjunto de dispositivos periféricos para el almacenamiento masivo de 
datos de un ordenador, con mayor capacidad que la memoria primaria, pero más lenta que ésta. 


<!-- Page 77 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
77 
Algunos tipos son: 
• Diskettes. 
Ya en desuso. 
• Soportes ópticos. 
Tienen tendencia a desaparecer (CD, DVD, Blu-Ray, etc.). 
• Disco duro. 
• Discos magnéticos IDE y SATA. 
Tienen partes móviles. Se han utilizado hasta hace unos años, que han empezado a 
utilizarse los discos SSD, o la combinación de ambos. 
Los discos magnéticos, al tener partes móviles, son más sensibles a golpes, más ruidosos y 
consumen más energía. 
Suelen ser más económicos en la misma capacidad de almacenamiento. 
• SSD o solid-state disk. 
Unidad de estado sólido, (llamado a veces incorrectamente disco de estado sólido, lo cual 
no es correcto puesto que carece de disco físico, y también se puede ver denominado como 
Solid State Drive). 
Son mucho más rápidos y al no tener partes móviles, menos sensibles a golpes, más 
silenciosos y consumen menos energía. 
Se elegirá el uso de uno u otro según las necesidades (aunque en ocasiones es una buena opción 
montar uno de cada, SSD para el sistema operativo, siendo mucho más rápido el arranque, y uno 
sólido de mayor capacidad para el almacenaje de datos). 
Se pueden conectar en el interior de la caja, conectándolo a la placa base, o en formato de disco 
duro externo conectándolo a los puertos externos del ordenador: SATA, Firewire y USB que es 
el más común. 
 
 
 
 
+ Info 
Estudiaremos los discos duros más detenidamente en la Unidad 2. 
 


<!-- Page 78 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
78 
4.3.2.2.1. SWAP (Virtual Memory) 
Espacio de intercambio en disco. 
Se trata de una simulación de RAM en un área de un disco duro con lo cual conseguimos que no se 
detengan servicios al escasear memoria RAM, pero ralentiza el ordenador al ser la memoria secundaria 
más lenta. 
 
 
 
 
Atención 
Swapping (del término inglés "swap": intercambiar): consiste en 
mover un proceso en ejecución o parte de él, temporalmente 
desde la memoria principal a la memoria secundaria (un dispositivo 
de almacenamiento), o viceversa. 
 
4.3.2.2.2. Memorias flash 
Es un tipo de memoria que únicamente permite la lectura programable y borrable electrónicamente, (lo 
que se conoce por sus siglas como EEPROM), por tanto, se puede utilizar como memoria ROM, o como 
dispositivos de almacenamiento de memoria independiente, como son los USB. 
El almacenamiento flash utiliza celdas de memoria para almacenar datos. Las celdas que tienen datos 
escritos anteriormente se tienen que borrar antes de poder escribir datos nuevos en ellas. 
Se le da el nombre de flash, por ser una tecnología de almacenamiento de datos que se programa 
eléctricamente a alta velocidad (escribe datos y realiza operaciones de I/O aleatorias a la velocidad del 
flash (puede traducirse como destello o Relámpago). 
Es un tipo de memoria no volátil. 
4.3.3. Jerarquía 
En la siguiente imagen se muestra la jerarquía de la memoria. 


<!-- Page 79 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
79 
 
Niveles de la jerarquía de memoria 
Como puedes observar, la punta de la pirámide muestra la memoria más rápida, cara y que más veces se 
usa, pero también la de menor capacidad. A medida que vamos bajando en la pirámide, aumenta la 
capacidad y disminuyen el resto de parámetros. 
Es imprescindible la realización periódica de copias de seguridad, para evitar la pérdida de información. 
Estas copias deben estar en un dispositivo diferente al de almacenamiento habitual, y además debe ser 
un dispositivo externo (no conectado a la placa base, ya que ante una subida de tensión, etc., podría 
dañarse tanto el dispositivo de uso normal como el de copia de seguridad). 
También es más conveniente, tener más de un dispositivo de copia, alternándolos. Si en el momento 
que estamos realizando la copia de datos hay un fallo eléctrico, se pueden dañar también los 2 
dispositivos, y perderíamos la información. 
4.3.4. Thrashing (Hiperpaginación) 
Se denomina thrashing, cuando un sistema operativo utiliza una creciente cantidad de recursos para 
hacer una cantidad de trabajo cada vez menor. 
A menudo, se refiere a cuando se cargan y descargan sucesiva y constantemente partes de la imagen de 
un proceso desde y hacia la memoria principal y la memoria virtual o espacio de intercambio. En un 
estado normal, esto permite que un proceso bloqueado y no listo para correr deje lugar en memoria 
principal a otro proceso listo. 


<!-- Page 80 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
80 
Cuando se produce hiperpaginación, los ciclos del procesador se utilizan en llevar y traer páginas (o 
segmentos, según sea el caso) y el rendimiento general del sistema se degrada notablemente. El 
sistema tarda más tiempo en paginar que en realizar procesos. 
Este término se utilizó por primera vez cuando los sistemas operativos funcionaban sobre cintas 
magnéticas para describir el sonido de que las cintas hacían cuando se leían y escribían datos a alta 
velocidad. 
Las formas de evitar la hiperpaginación, se investigaron mucho en los años 70, desarrollándose 
algoritmos efectivos, aunque complejos, con la idea de intentar adivinar qué páginas serán utilizadas 
próximamente, basándose en su historia reciente y utilizando como hipótesis el principio de cercanía de 
referencias. Estos son los denominados algoritmos de reemplazo de páginas. 
Resulta más práctico y sencillo evitar la hiperpaginación usando lo siguiente: 
• Aumentando la cantidad de memoria RAM (mejor solución a largo plazo). 
• Disminuyendo la cantidad de aplicaciones corriendo en la computadora. 
• Ajustando el tamaño de la partición de intercambio. 
4.4. Sistemas de direccionamiento 
Direccionamiento de la memoria por parte del procesador 
Los modos de direccionamiento de un procesador son las diferentes formas de transformación de 
determinada información de un operando contenida en una instrucción en la dirección de este 
operando. 
Tiene dos fines principales: 
• Permitir al programador manejar estructuras complejas como vectores y matrices. 
• Reducir el número de bits utilizado. 
Existen distintos modos de direccionamiento. No hay un estándar que los defina, por lo que existen 
múltiples clasificaciones. 
Modos de direccionamiento 
Existen muchos modos de direccionamiento, pero vamos a centrarnos en los principales: 
1. Implícito o inherente. 
2. Inmediato o literal. 
3. Directo por registro. 


<!-- Page 81 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
81 
4. Directo o absoluto. 
5. Indirecto. 
6. Relativo. 
7. Por base y desplazamiento. 
8. Indexado. 
9. Autoincremental. 
10. Autodecremental. 
Pasamos a verlos con más detalle 
1. IMPLÍCITO (O INHERENTE). 
El operando se especifica en la definición de la instrucción. 
Se utiliza para hacer referencia a dos tipos de operandos: 
• Registros. 
• Operandos de pila. La operación se realiza sobre la cima de la pila. 
2. INMEDIATO (O LITERAL). 
En la instrucción se encuentra incluido el operando, es decir, la información sobre la que se 
operará, por lo que no es necesario acceder a la memoria. 
3. DIRECTO POR REGISTRO. 
El campo de dirección de una instrucción especifica un registro del procesador. 
Este presenta dos ventajas: 
• El acceso a los registros es muy rápido. 
• El número de bits necesarios para especificar un registro es más pequeño que el necesario 
para especificar una dirección de memoria. 
4. DIRECTO (O ABSOLUTO). 
El campo de dirección obtenido no necesita ninguna transformación, es decir, es la dirección 
real del registro que buscamos, al que queremos acceder. 


<!-- Page 82 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
82 
5. INDIRECTO. 
Obtenemos una dirección del dato al que queremos acceder, que no es real, sino que es la 
dirección de dónde está. Por lo que necesitamos otro paso para llegar a acceder al dato. 
6. RELATIVO. 
La dirección del dato al que queremos acceder, la obtenemos sumando 2 valores, el indicado en 
la instrucción y una fija guardada en un registro. 
Las direcciones referenciadas por un programa suelen estar concentradas en una parte de 
memoria, no suelen alejarse mucho unas de otras. Así que no es necesario utilizar todos los bits 
de dirección de memoria, utilizaremos sólo los precisos para cubrir la parte la parte de memoria 
donde estén. 
Esto lo hacemos mediante la localidad de referencia: tomamos como referencia un punto de la 
memoria y como campo de operando la diferencia entre ese punto y la dirección efectiva del 
operando. 
La dirección que tomamos como referencia puede residir en un registro de la CPU, y la dirección 
efectiva se obtiene sumando el contenido del registro con el campo de operando. A estos se le 
llama relativos a un registro. 
7. POR BASE Y DESPLAZAMIENTO. 
Es una versión del direccionamiento relativo a registros donde la dirección que se toma como 
referencia de la zona de memoria en la que están localizados los datos se deposita en un registro 
denominado registro base y la dirección del operando se obtiene sumando el registro base y el 
campo de operando. 
Llamamos desplazamiento a la cantidad que hay que sumar al registro base para conseguir la 
dirección del operando (en este caso el campo de operando). 
8. INDEXADO. 
Es una versión del direccionamiento relativo a registros donde la dirección del operando 
también se calcula sumando un registro de la CPU al campo de operando. Este registro es un 
registro específico para este uso llamado registro índice. 
9. AUTOINCREMENTAL. 
Es una versión del direccionamiento relativo a registros donde la dirección del operando se 
encuentra en un registro y éste se va incrementando, después de acceder al operando, en el 
tamaño del mismo. 
10. AUTODECREMENTAL. 
Es una versión del direccionamiento relativo a registros donde la dirección del operando se 
encuentra en un registro y éste se va decrementando, después de acceder al operando, en el 
tamaño del mismo. 


<!-- Page 83 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
83 
Utilidades 
En la siguiente tabla te mostramos las utilidades de los principales modos de direccionamiento. 
MODOS 
UTILIDADES 
Implícito 
Organizaciones de un solo acumulador e instrucciones de los ordenadores con 
organización de pila 
Inmediato 
Operaciones con constantes 
Directo por registro 
Variables locales de procedimientos no recursivos 
Directo o absoluto 
Direcciones del sistema (que no dependen del programa) 
Indirecto 
Variables referenciadas a través de apuntadores 
Relativo 
Variables globales 
Por base y 
desplazamiento 
Varios programas en memoria 
Indexado 
Acceso a vectores, matrices y cadenas 
Autoincremental 
Desapilar parámetros de procedimientos. Recorrido de vectores y cadenas 
Autodecremental 
Apilar parámetros de procedimientos. Recorrido de vectores y cadenas hacia atrás 
 
 
 
 
Recomendación 
Sabemos que este punto es un poco complicado y denso. Consulta 
la Biblioteca Audiovisual. 
Te resultaría útil, que hicieras un resumen o tabla con los modos de 
direccionamiento y la forma en que calculan su dirección. 
Una visión global te puede ayudar a ver las diferencias. 
Es importante que la forma de calcularlo lo indiques con tus 
palabras y de la forma más reducida posible. 
 


<!-- Page 84 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
84 
4.5. El tiempo de ejecución de un programa 
 
Fuente: Public domain vectors 
Es el tiempo que tarda en ejecutar todas sus instrucciones 
El rendimiento de un ordenador en la ejecución de un programa es la inversa del tiempo de ejecución 
(cuanto menos tarde, mayor rendimiento). 
Al principio se utilizaban procesadores CISC porque se pensaba que el rendimiento era mayor si se tenía 
un pequeño conjunto de instrucciones complejas (algunas de las cuales tardaban varios ciclos de reloj). 
Estudios estadísticos demostraron que muchas de estas instrucciones no se utilizaban y surge la 
tendencia RISC que tiene las siguientes características: 
• El repertorio de instrucciones es muy reducido y contiene instrucciones muy básicas. 
• Estos procesadores disponen de muchos registros de propósito general. 
• Las instrucciones presentan un formato similar (longitud, tamaño, posición de los elementos, etc.). 
• El procesador contiene registros y las operaciones de la ALU se realizan con los datos de estos 
registros. El intercambio de información entre la memoria y los registros se efectúan mediante 
dos instrucciones específicas. 
• Load. Carga en registro. 
• Store. Guardado en memoria. 
• Por norma general, una instrucción se ejecuta en un ciclo de reloj. 
• El diseño y desarrollo de los procesadores es mucho más sencillo y menos costoso en términos 
de tiempo. 


<!-- Page 85 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
85 
Por lo tanto, para mejorar el rendimiento de un ordenador a la hora de ejecutar un programa tenemos 
dos enfoques: 
• Reduciendo el número de instrucciones (CISC). 
• Reduciendo el número de ciclos que utiliza una instrucción (RISC). 
Normalmente, al reducir un parámetro, aumentamos el otro. Para solucionar esto se utilizan técnicas de 
paralelismo para disminuir el número de ciclos utilizados sin variar el número de instrucciones. 
Hoy en día, la tendencia RISC es la más utilizada. 
4.5.1. Procesador multinúcleo 
Los procesadores fueron inicialmente desarrollados con un solo núcleo. 
Su evolución, fue a mediados de la década de 1980s Rockwell International fabricó versiones del 6502 
con dos núcleos en un solo chip (es decir, procesadores multinúcleo), compartiendo los pins del chip en 
fases alternativas del reloj. Otros procesadores multicore se desarrollaron a principios del siglo XXI por 
Intel, AMD y otros. 
Mientras que las tecnologías de fabricación de CMOS continúan mejorando, reduciendo el tamaño de 
las puertas sencillas, los límites físicos de los componentes microelectrónicos basados en 
semiconductores se han convertido en una importante preocupación. Algunos efectos de estas 
limitaciones físicas pueden ser la elevada disipación de calor y problemas de sincronización de la 
información. 
Un procesador multinúcleo es aquel que combina dos o más microprocesadores independientes en un 
solo paquete, a menudo un solo circuito integrado. 
Un microprocesador o procesador multinúcleo tiene varias unidades de procesamiento que comparten 
memoria caché, L3 y L2 en algunos modelos. 
4.5.2. Clasificación según paralelismo 
Para mejorar el rendimiento de los ordenadores se han desarrollado varios tipos que contienen 
múltiples procesadores. 
Flynn propone la siguiente clasificación de ordenadores atendiendo al paralelismo a nivel de 
procesadores: 
• SISD. 
Single Instruction Single Data. 
Son los ordenadores clásicos basados en la arquitectura Von Neumann. Un único procesador 
ejecuta un sólo flujo de instrucciones para operar datos en una única memoria. Se ejecuta una 
única instrucción y un dato en cada ciclo de reloj. 


<!-- Page 86 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
86 
• SIMD. 
Un flujo de instrucciones y múltiples flujos de datos. Todas las unidades de cómputo ejecutan 
simultáneamente la misma instrucción, pero con distintos datos. 
• MISD. 
Múltiples flujos de instrucciones y un solo flujo de datos. No se suele utilizar dado que no es 
eficiente. 
• MIMD. 
Múltiples flujos de instrucciones y múltiples flujos de datos. Varias unidades de cómputo 
ejecutan simultáneamente instrucciones distintas con distintos datos. 
 
Clasificación de ordenadores según paralelismo propuesta por Flynn 
4.5.3. Tipos de Instrucciones de la CPU 
1. Transferencia de datos. 
2. Instrucciones aritméticas. 
3. Instrucciones de comparación. 
4. Instrucciones lógicas. 
5. Instrucciones de desplazamiento. 


<!-- Page 87 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
87 
6. Instrucciones de bits. 
7. Instrucciones de control: 
a. Saltos. 
b. Llamadas a subrutinas. 
c. Gestión de interrupciones. 
8. Instrucciones de entrada y salida. 
9. Instrucciones de control y misceláneas. 
5. Bibliografía 
• PRIETO ESPINOSA, A. Introducción a la informática. 2006. 
• ÁLVAREZ MUNÁRRIZ, L. Fundamentos de inteligencia artificial. 
• STAIR, R. y REYNOLDS, G. Principios de sistemas de Información. 
• http://www.rae.es/. 
• https://www.definicionabc.com. 
• https://www.significados.com/. 
• Universidad Nacional Autónoma de México. Instituto de Investigaciones Bibliotecológicas y de la 
Información. http://iibi.unam.mx/. 
• Sistemas de información en la era digital. Fundación OSDE. 
• https://www.fundacionosde.com.ar/pdf/biblioteca/Sistemas_de_informacion_en_la_era_digi
tal-Modulo_I.pdf. 
• Apuntes UNED. Arquitectura de ordenadores. Grado en Informática. 
http://www.apuntesuned.es/informatica/arquitectura-de-ordenadores/apuntes-arquitectura-
de-ordenadores.html. 
• http://www.areatecnologia.com/. 
• https://whatis.techtarget.com/. 
• https://es.slideshare.net/Jomicast/componentes-internos-de-los-equipos-microinformaticos. 
• http://www.cad.com.mx/generaciones_de_las_computadoras.htm. 


<!-- Page 88 -->

 
 
Informática básica. Representación y comunicación de la información: elementos constitutivos de un sistema 
de información 
88 
• Departamento de Informática. Universidad de Valladolid. 
• https://www.infor.uva.es/~bastida/OC/modos.pdf. 
• PITTI, E. Imagen IBM 360. Museo de historia de la computación. Fuente: 
https://www.flickr.com/photos/24205142@N00/2370873167. 
• https://hardzone.es/tutoriales/componentes/procesador-arm/. 
• Arquitectura ARM – Wikipedia, la enciclopedia libre. 
• http://cv.uoc.edu/annotation/8255a8c320f60c2bfd6c9f2ce11b2e7f/619469/PID_00218274
/PID_00218274.html#w31aab5c11. 

