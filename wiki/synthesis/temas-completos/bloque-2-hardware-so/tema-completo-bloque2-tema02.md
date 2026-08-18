---
title: "Tema Completo Extendido 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-2
  - tema-02
  - oposiciones-tai
estado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md]]"
  - "[[wiki/sources/bloque2-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema01|⬅️ Tema Completo 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema03|Tema Completo 03 ➡️]]

# 🔴 Tema Completo Extendido 02 (Bloque 2): Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 02 correspondiente al Bloque 2 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro

# Bloque 2 - Tema 02 (UD012103): Periféricos, Conectividad, Puertos Físicos y Buses de Expansión

<!-- Page 1 -->

 
 
Periféricos: conectividad 
y administración 

<!-- Page 2 -->

ÍNDICE 
1. Hardware. Periféricos 
6 
1.1. Clasificación de los periféricos 
7 
1.2. Conexión de los periféricos al ordenador 
8 
1.2.1. Puertos físicos 
8 
1.2.1.1. Puerto Serie 
9 
1.2.1.2. Puerto Paralelo 
10 
1.2.1.3. Puerto PS/2 
11 
1.2.1.4. Puerto Firewire 
11 
1.2.1.5. Puerto USB 
12 
1.2.1.5.1. Conectores USB 
13 
1.2.1.5.2. Versiones USB 
16 
1.2.1.5.3. Otras especificaciones USB 
18 
1.2.1.5.4. Puertos Apple 
18 
1.2.1.6. SATA 
19 
1.2.1.7. Thunderbolt 
20 
1.2.1.8. Puertos y conectores TS/TRS/TRRS 
21 
1.2.2. Puertos virtuales 
22 
1.3. Administración del sistema de entrada/salida 
22 
1.3.1. Controlador de E/S 
23 
2. Hardware de entrada. Teclado y ratón 
24 
2.1. Teclado 
25 
2.2. Ratón 
28 
3. Hardware de almacenamiento 
29 
3.1. Cintas magnéticas 
29 
3.2. Discos duros 
30 
3.2.1. Magnéticos 
30 
3.2.2. Unidades de Estado Sólido (SSD) 
37 
3.2.3. Comparativa Discos HDD y SSD 
41 

<!-- Page 3 -->

 
 
3.2.4. Formatear Discos Duros (Sectorización) 
42 
3.2.4.1. FAT 
42 
3.2.4.2. NTFS 
44 
3.2.4.3. exFAT 
45 
3.3. Discos ópticos 
48 
3.4. Memorias flash 
48 
4. Sistemas de almacenamiento 
49 
4.1. Tipos de almacenamiento: DAS, NAS, SAN 
51 
4.1.1. DAS (Direct-Attached Storage) 
51 
4.1.2. NAS (Network-Attached Storage) 
52 
4.1.2.1. NFS 
52 
4.1.2.2. SMB 
53 
4.1.3. SAN (Storage Area Network) 
54 
4.1.3.1. FC (Fibre Channel) 
54 
4.1.3.2. FCoE 
54 
4.1.3.3. iSCSI 
55 
4.1.3.4. NVMeoF 
55 
4.2. Familias de controladoras 
56 
4.2.1. RAID 
56 
4.2.1.1. Sistemas RAID un solo nivel 
58 
4.2.1.2. Sistemas RAID multinivel 
67 
4.2.2. SCSI (interfaz de sistema de ordenador pequeño) 
69 
4.2.3. SATA 
72 
4.2.3.1. Conector sata de datos 
73 
4.2.3.2. Conector SATA de alimentación 
74 
4.2.3.3. SATA externo o Esata 
74 
4.2.3.4. Conector Mini SATA o mSATA 
75 
4.2.3.5. Conector SATA Express 
75 
4.3. Gestión de volúmenes 
75 

<!-- Page 4 -->

 
 
5. Hardware de impresión 
76 
5.1. Partes de la impresoras 
77 
5.2. Clasificación 
77 
5.2.1. Según el mecanismo de impresión 
77 
5.2.2. Según la forma de imprimir los caracteres 
77 
5.2.3. Según la tecnología utilizada 
77 
5.2.4. Trazadores o plotters 
78 
5.3. Descripción de los tipos de impresoras 
78 
5.3.1. Impresoras de impacto 
78 
5.3.2. Impresoras de tinta 
79 
5.3.3. Impresoras láser 
80 
5.3.4. Impresoras térmicas 
81 
5.3.5. Impresoras de sublimación 
81 
5.3.6. Impresoras electroestáticas 
82 
5.3.7. Tinta sólida 
82 
5.3.8. Multifunción 
82 
5.3.9. 3D 
82 
5.3.10. Plotters 
83 
6. Hardware de visualización 
84 
6.1. Tarjeta gráfica 
84 
6.2. Monitor 
87 
6.2.1. Resolución, ratio y refresco 
89 
6.2.2. Cronograma de Resoluciones 
90 
6.3. Pantalla táctil 
91 
7. Hardware de digitalización. Escáner 
93 
7.1. Conexión con el ordenador 
93 
7.2. Tipos de escáner 
95 

<!-- Page 5 -->

 
 
8. Equipos de control numérico computerizados (CNC) 
97 
8.1. Funcionamiento de una máquina CNC 
98 
8.1.1. Control de movimiento 
99 
8.1.2. Accesorios y funciones programables 
100 
8.1.3. Programa CNC 
100 
8.1.4. Controlador CNC 
101 
8.1.5. Programa CAM 
101 
8.1.6. Sistema DNC 
102 
9. Cortadora láser 
102 
9.1. Tipos de cortadoras láser 
104 
9.1.1. Láseres de gas 
104 
9.1.2. Láser de cristal 
104 
9.1.3. Láseres de fibra 
105 
9.2. Funcionamiento 
105 
9.3. Ventajas 
106 
9.4. Softwares de uso 
106 
10. Colorimetría 
107 
10.1. Resolución de imágenes 
108 
10.2. Modelos de color 
109 
10.2.1. RGB 
109 
10.2.2. CMYK 
110 
10.2.3. HSV (HSB) 
110 
10.3. Profundidad de color 
110 
11. Bibliografía 
111 
 

<!-- Page 6 -->

 
 
Periféricos: conectividad y administración 
6 
1. Hardware. Periféricos 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
 
Ya has aprendido los elementos de Hardware (parte física) más importantes de un ordenador: CPU, 
Memoria y Placa Base. 
Ahora vamos a continuar viendo otros elementos de hardware. 
Periféricos: proporcionan entrada y salida de información al ordenador. 
La definición más aceptada de periférico es la siguiente: 
Se denominan periféricos a los dispositivos de hardware que no pertenecen al núcleo fundamental 
del ordenador (la CPU), a través de los cuales el procesador realiza operaciones de entrada/salida 
(E/S). Se incluyendo por tanto los dispositivos de almacenamiento permanente. 
Si entiendes bien lo que es un periférico, entenderás distintas definiciones. 
Un periférico, es todo aquello que podemos conectar a un ordenador: webcam, pendrive, micrófono, 
lector de código de barras… 
En esta unidad vas a estudiar los siguientes periféricos: 
• Puertos de conexión. 
• De entrada (Teclado y Ratón). 
• De almacenamiento. 

<!-- Page 7 -->

 
 
Periféricos: conectividad y administración 
7 
• De impresión (Tipos de Impresoras). 
• De visualización (Pantallas). 
• De digitalización. 
Como complemento, estudiarás colorimetría (resolución, tipos de sistemas de color etc.) 
1.1. Clasificación de los periféricos 
Vamos a hacer una sencilla clasificación, basándonos en su función: 
• Periféricos de entrada: sirven para introducir datos en un ordenador desde el exterior. 
Transforman la información externa en señales eléctricas codificadas permitiendo su 
transmisión, detección, interpretación, procesamiento y almacenamiento. Ejemplo: teclado, 
ratón, lector de iris, lector de huella dactilar etc. 
• Periféricos de salida: hacen lo contrario que los de entrada, reciben las señales eléctricas del 
ordenador y las convierten en información en el formato adecuado para ser mostrada al usuario 
y entendible por este. Ejemplo: monitor, impresora, altavoces etc. 
• Periféricos de entrada/salida: permite las dos funciones anteriores. Ejemplo: pantalla táctil. 
• Periféricos de almacenamiento: almacenan la información en dispositivos no volátiles, para que 
pueda recuperarse y utilizarse cuando se requiera. Ejemplo: pendrive, disco duro externo etc. 
 
 
 
 
Ejemplo 
Si queremos escribir una carta con el ordenador, e imprimirla, se 
ejecutarán los siguientes pasos: 
1. Utilizamos un teclado para escribir el texto. (periférico de 
entrada). 
2. Esta entrada se codifica (utilizando un sistema de 
representación como ASCII o Unicode). Y será tratada por 
la memoria y procesador. 
3. La impresora (periférico de salida), recibirá la información 
y la transformará en caracteres inteligibles por el usuario. 
 

<!-- Page 8 -->

 
 
Periféricos: conectividad y administración 
8 
Toda clasificación se estructura de una determinada manera dependiendo del prisma desde el que se 
aborde. En este caso al igual que un disco duro externo se puede considerar periférico de entrada, se 
puede considerar asimismo de salida, pero también tanto de entrada y salida como de almacenamiento. 
En el examen hay que estar siempre atentos a entender un enunciado que deberá sacarnos de dudas si 
está planteado correctamente. 
Partes de un periférico 
Los periféricos suelen estar formados por dos partes: 
• Elementos mecánicos: constituidos por dispositivos electromecánicos (conmutadores 
manuales, relés, motores, electroimanes, servomecanismos, etcétera), controlados por los 
elementos electrónicos. 
• Elementos electrónicos: constituyen el controlador del periférico. Se encargan de interpretar las 
órdenes que le llegan del procesador para la recepción o emisión de datos y de generar las 
señales de control para la activación de los elementos electromecánicos del periférico que 
producen o captan los datos en el soporte de información correspondiente. 
1.2. Conexión de los periféricos al ordenador 
Los periféricos se conectan a la CPU a través de los buses. Los periféricos se conectan al bus del sistema 
directamente o bien a través de interfaces (puertos). 
Interfaz es una conexión entre dos sistemas de cualquier tipo (uno de los sistemas puede ser una 
persona), a los cuales les brinda un soporte para la comunicación a diferentes niveles. 
Existe una gran diversidad de periféricos con distintas características eléctricas y velocidades de 
funcionamiento. El objetivo de las interfaces es adaptar estas características al bus del sistema. 
A estas interfaces se les denomina puertos, permiten enviar y recibir datos digitales. 
Puede ser: 
• Puertos físicos. 
• Puertos virtuales. 
1.2.1. Puertos físicos 
Son entradas físicas en el ordenador para que se conecte un periférico. 
En un ordenador nos podemos encontrar numerosos tipos de conectores (como dispositivo 
electrónico) que nos permitirán la conexión de periféricos. 

<!-- Page 9 -->

 
 
Periféricos: conectividad y administración 
9 
Los conectores se insertan dentro de un puerto para hacer la conexión entre el ordenador y el 
dispositivo periférico. 
Vamos a ver algunos de los puertos/conectores más importantes: 
• Puerto serie. 
• Puerto paralelo. 
• PS/2. 
• Firewire. 
• USB. 
• SATA. 
• Thunderbolt. 
1.2.1.1. Puerto Serie 
 
La interfaz de datos en serie o puerto serial trabaja bajo el estándar que se realizó en 1962, con la 
norma EIA/TIA RS-232C, conocida popularmente como RS-232. 
 
 
 
 
+ Info 
Se creó también al mismo tiempo la recomendación V.24 que 
define los circuitos y señales de la interfaz, y la recomendación 
V.28 que define los aspectos eléctricos). 
 
 
En un puerto serie, la información se transmite de forma secuencial bit a bit (un solo bit a la vez), es 
decir, envía toda la información en un bit detrás de otro. (Un puerto paralelo enviaría varios bits de 
forma simultánea). 

<!-- Page 10 -->

 
 
Periféricos: conectividad y administración 
10 
El primer conector era el DB-25 (25 pines), que pasó a simplificarse al DB-9 (9 pines), que se denominó 
como RS-232. 
Actualmente está en desuso, se utilizaba antiguamente fundamentalmente para conectar el ratón, que 
paso a conectarse por puerto PS2 (aun en uso en algunos ordenadores), y conexión por USB. 
También se utilizaba para otros dispositivos, como impresoras de tickets, módems, lectores de códigos de 
barra por infrarrojos, y productos maquinaria industrial controlada mediante un ordenador, entre otros. 
Características: 
• Es un puerto lento. 
• También se le conoce como RS-232 (y como COM). 
• Es necesario reiniciar el equipo para que el sistema lo reconozca y funcione. 
Versiones: 
El modelo más común es el DB9, que contiene 9 pines. También existe un modelo con 25 pines. 
1.2.1.2. Puerto Paralelo 
 
El puerto paralelo permite el intercambio simultáneo de paquetes de bits a través de diferentes hilos. 
Cada puerto paralelo puede servir para enviar hasta 8 bits de forma simultánea, por 8 hilos distintos. Se 
conectaban impresoras etc. 
Es un conector de 25 pines, que no hay que confundir con el conector serie DB-25 (con 25 pines). 
 
 
 
 
+ Info 
Los puertos en paralelo han sido usados para impresoras, y 
conectores para discos duros bus PATA (IDE) y discos duros bus 
SCSI, en los cuales no se podía realizar la conexión en caliente, ni 
tampoco proporcionaba alimentación al periférico conectado. En la 
actualidad está prácticamente en desuso. (Pueden encontrarse en 
maquinarias industriales). 
 

<!-- Page 11 -->

 
 
Periféricos: conectividad y administración 
11 
Versiones: 
• Puerto paralelo: trabaja a una velocidad de 2,4 MB por segundo. 
• EPP (puerto paralelo mejorado): alcanza velocidades de 8 a 16 MB por segundo. 
• ECP (puerto de capacidad mejorada): desarrollado en común por HP y Microsoft. Misma 
velocidad que el anterior, pero permite reconocer un dispositivo al conectarlo. 
1.2.1.3. Puerto PS/2 
 
También denominado mini-DIM de 6 pines. Es un puerto que se utiliza para conectar el teclado y el 
ratón al ordenador. Están siendo sustituidos por el USB. 
Antiguamente el ordenador tenía 2 de estos puertos, uno para el teclado y otro para el ratón, que no 
eran compatibles entre sí (no se podían intercambiar). Eran de diferente color evitar que el usuario los 
conectará erróneamente (morado para el teclado y verde para el ratón, también los periféricos de 
teclado y ratón solían tener el conector del mismo color). 
Actualmente, los ordenadores ya no llevan este puerto o incorporan un único puerto que sí es 
intercambiable (se puede conectar tanto el ratón como el teclado). 
Características puerto PS/2: No se pueden conectar el dispositivo en caliente. Hay que conectarlo con 
el ordenador apagado para que al encenderlo lo reconozca. (En algunos ordenadores modernos sí que 
los reconoce en caliente). 
1.2.1.4. Puerto Firewire 
 
En desuso en la actualidad, sustituido por el USB versiones 2.0 y posteriores. 
También denominado IEEE 1394. Es un puerto serie de alta velocidad. Se suele usar para conectar 
cámaras de vídeo digitales, y también existen discos duros externos con este tipo de conexión. 

<!-- Page 12 -->

 
 
Periféricos: conectividad y administración 
12 
A diferencia de los puertos PS2, los puertos Firewire aceptan la conexión en caliente y el plug&play. 
Su forma física es similar al USB, pero con una esquina en forma de punta. Puede tener 4, 6, 9 y hasta 12 
pines según la versión. 
Versiones implementadas de Firewire: 
• Firewire 400 (IEEE 1394): 
Es la primera versión, con un conector de 6 pines, y velocidad de hasta 400 Mbits/s (50 MB/s), 
superando por tanto las velocidades de los USB 1.0 y 1.1. 
• Firewire 800 (IEEE 1394b): 
Conector de 9 pines en lugar de 6. Soporta trasferencias de 786 Mbits/s (100 MB/s) pudiendo 
alcanzar distancias de 100 metros de cable. 
• Firewire s1600: 
Continuando con 9 pines, amplió el ancho de banda hasta los 1,6 Gbps (200 MB/s), superando 
entonces a la versión USB 2.0 (solamente alcanzaba los 60 MB/s). 
• Firewire s3200 (IEEE 1394b): 
Amplió la velocidad hasta los 3,2 Gbps (400 MB/s). 
• Firewire s800T (IEEE 1394c): 
Es otra variante que implementa la tecnología Firewire a través del conector Ethernet RJ-45, 
para combinar las ventajas de uno y otro. 
1.2.1.5. Puerto USB 
 
USB (Bus Universal en Serie) es un estándar de comunicación que permite la conexión de periféricos a 
un ordenador. Aunque el USB transmite los datos bit a bit a nivel físico (se denomina 'serial'), la 
organización de estos bits en paquetes es fundamental para lograr una comunicación eficiente y 
confiable entre dispositivos. Fue diseñado para estandarizar la forma en que se conectan los periféricos, 
y es uno de los tipos de puertos más utilizados actualmente para conectar dispositivos como ratones, 
teclados, pendrives, impresoras, auriculares, entre otros. 

<!-- Page 13 -->

 
 
Periféricos: conectividad y administración 
13 
 
 
 
+Info 
Un cable USB típico está compuesto por cuatro conductores 
principales: VBUS (alimentación de 5V), D+ y D- (datos) y GND 
(tierra). Los datos se transmiten a través de los pines D+ y D- 
utilizando un protocolo de comunicación específico. Versiones más 
recientes como USB 3.0 y superiores incorporan pines adicionales 
para aumentar el ancho de banda y permitir velocidades de 
transferencia más altas. 
Los conectores USB, como Micro-A, Micro-B y USB-C, presentan 
diferentes configuraciones de pines para adaptarse a diversos 
dispositivos y aplicaciones. USB-C, por ejemplo, es un conector 
reversible que soporta una amplia gama de protocolos y 
velocidades, convirtiéndolo en un estándar cada vez más popular. 
 
 
Características de USB: 
• Plug and play: Conexión y configuración automáticas de dispositivos, sin necesidad de reiniciar 
el equipo en la mayoría de los casos. 
• Conexión en caliente: Permite conectar y desconectar dispositivos sin apagar el equipo ni 
afectar su funcionamiento. 
• Detección automática de controladores: El sistema operativo instala automáticamente los 
controladores necesarios, aunque en algunos casos puede requerirse instalación manual de 
software específico. 
• Los hubs USB permiten conectar múltiples dispositivos a un solo puerto, ampliando así las 
capacidades de conexión del equipo en cadena hasta 127 puertos. 
1.2.1.5.1. Conectores USB 
USB-A y USB-B 
En sus primeras versiones (USB 1.0 y 2.0), los conectores USB-A y USB-B constan de cuatro pines: 5V 
(alimentación), datos negativos, datos positivos y tierra. 
Su diseño asimétrico facilita la conexión correcta, impidiendo que se conecten al revés. Se distinguen 
fácilmente por su forma: 
• El USB-A es rectangular y plano. 
• El USB-B es más cuadrado. 

<!-- Page 14 -->

 
 
Periféricos: conectividad y administración 
14 
Los conectores USB 3.0 y 3.1, identificables por su color interior azul, incrementan el número de pines a 
nueve en los conectores USB-A, mientras que los conectores USB-B pueden llegar a tener hasta 11 
pines (USB 3.0 Powered-B). 
Estas versiones ofrecen velocidades de transferencia de datos mucho más altas, lo que las hace ideales 
para dispositivos como discos duros externos, escáneres, cámaras digitales, entre otros. 
 
USB-C 
Con un diseño simétrico y reversible, el USB-C cuenta con 24 pines y es compatible con una amplia 
gama de estándares, incluidos DisplayPort, Thunderbolt y versiones de USB que van desde USB 2.0 
hasta USB4. Su tamaño compacto y versatilidad lo han convertido en el estándar de la industria para 
dispositivos modernos. 
Permite la transmisión de datos, video, audio y energía de alta velocidad. Además, admite hasta 100W 
de potencia para la carga rápida de dispositivos, lo que lo convierte en una solución integral tanto para 
dispositivos móviles como para ordenadores y otros periféricos. 
Existen adaptadores que permiten conectar dispositivos con conectores USB-A o USB-B a puertos USB-C, 
aunque la funcionalidad y las velocidades pueden variar según el adaptador y los estándares involucrados. 
Mini A, Mini B y Mini AB 
También debemos mencionar unos conectores que estuvieron presentes desde la versión 1.1 hasta USB 
2.0. Estos conectores mini-USB eran comunes en dispositivos portátiles como cámaras digitales y 
algunos teléfonos móviles, pero su uso ha disminuido con la adopción de conectores más modernos 
como el micro-USB y el USB-C. 
 

<!-- Page 15 -->

 
 
Periféricos: conectividad y administración 
15 
Micro B, Micro AB 
Finalmente, hacemos referencia a los conectores micro-USB, ampliamente reconocidos por su uso en 
smartphones y otros dispositivos portátiles. Tanto Micro B como Micro AB en versiones USB 1.0 y 2.0 
tienen 5 contactos. 
Sin embargo, la evolución hacia el Micro B SuperSpeed en las versiones USB 3.0 y 3.1 añadió más pines, 
alcanzando 10 contactos, lo que permite velocidades de transferencia de datos significativamente 
superiores a las de los micro-USB tradicionales. 
Veamos unas imágenes para ver mejor la comparativa de conectores: 
 
 
Fuente: https://commons.wikimedia.org/wiki/File:USB_types_2.jpg 
De izquierda a derecha (Mostrado en una escala de 5 centímetros): 
• Micro-USB. 
• Mini-USB. 
• USB tipo B. 
• USB tipo A hembra. 
• USB tipo A macho. 

<!-- Page 16 -->

 
 
Periféricos: conectividad y administración 
16 
1.2.1.5.2. Versiones USB 
Existen varias versiones, la más actual es USB 4.0 
Para facilitar su comprensión vamos a ver las anteriores a 4.0 en una tabla, explicando a continuación 
con más detalle USB4. 
Versión 
Denominación 
alternativa 
Max. 
Transfer 
Rate 
(bits/s) 
Max. 
Transfer 
Rate 
(bytes/s) 
Max Power 
Out 
Power 
Direction 
Cable 
Configuration 
USB 1.x 
"Full Speed" 
12 Mbps 
1.5 MB/s 
5V/500mA 
(2.5W) 
Host to 
peripheral 
Type-A to 
Type-B 
USB 2.0 
"High Speed" 
480 Mbps 
60 MB/s 
5V/500mA 
(2.5W) 
Host to 
peripheral 
Type-A to 
Type-B 
USB 3.0 (3.1 
Gen1) 
"SuperSpeed 
USB" 
5 Gbps 
625 MB/s 
5V/900mA 
(4.5W) 
Host to 
peripheral 
Type-A to 
Type-B 
USB 3.1 
(USB 3.1 
Gen2) / 
USB-PD o 
USB Power 
Delivery 
"SuperSpeed 
USB 10 Gbps" 
10 Gbps 
1.25 GB/s 
20V/SA 
(100W) 
Bi-
directional 
Type-C both 
ends, reversible 
plug orientation 
USB 3.2 
"SuperSpeed 
USB 20 Gbps" 
Hasta 20 
Gbps 
 
Comparativa de las distintas versiones de USB 
Las distintas versiones son retro compatibles (compatibles con las versiones anteriores). El estándar 
USB 3.2, permite velocidades de 20 Gbps utilizando conectores tipo C. 
Generaciones USB 3.2 
USB 3.2 
Max. Transfer Rate (bits/s) 
Marketing name 
Generación 1 
5 Gbps 
SuperSpeed USB 
Generación. 2 
10 Gbps 
SuperSpeed USB 10 Gbps 
Generación. 2x2 
20 Gbps 
SuperSpeed USB 20 Gbps 

<!-- Page 17 -->

 
 
Periféricos: conectividad y administración 
17 
USB 4 
Aunque comúnmente sea llamado versión 4, el consorcio USB-IF que es el encargado de su desarrollo lo 
denomina tecnología USB4. 
USB4 Se anunció oficialmente en marzo de 2019, y se publicó el 29 de agosto de ese mismo año por 
USB Implementers Forum (IF). 
(En 2020 se anunció que este estándar sería compatible con DisplayPort 2.0 y que soportaría resoluciones 
superiores a 8K, como por ejemplo 16K (15.360 x 8.460) a 60Hz y 30 bpp 4:4:4 HDR con DSC). 
El motivo de su desarrollo fue: 
• El aumento del ancho de banda (permitiendo hasta 40 Gbit/s). 
• La convergencia del ecosistema USB-C. 
La especificación es compatible con USB 3.2 y USB 2.0. 
USB 4 se basa en Thunderbolt 3 (tecnología propietaria creada por Intel, que ha abierto el estándar, 
permitiendo así que sea utilizada y mejorada por USB), por lo que proporciona POWER DELIVERY (USB-
PD), que es de hecho un requisito de la especificación. 
USB Power Delivery permite alimentar dispositivos a través de puertos USB tipo C, esta cualidad 
posibilita universalizar cargadores para ordenadores y para smartphones. 
USB Power Delivery siempre funciona con unas determinadas condiciones en cuanto a potencia, 
dependiendo del dispositivo el USB Power Delivery podrá dar más o menos energía a los dispositivos 
que se le conecten con unos límites: 
• Mínimo de potencia de 7.5 vatios (específicamente 5V y 1.5 amperios por puerto). 
• Una potencia eléctrica máxima concreta. 
Máximo de 100W, a un voltaje máximo de 20V. (Concretamente, se puede llegar a los 20 voltios 
y 5 amperios de alimentación). 
Nunca más de la que acepta el que es cargado, ni más de la que puede dar el que proporciona la 
carga, por eso se dice que hay negociación. 
(Los dispositivos USB 2.0 pueden proporcionar 0.5A y los USB 3.0 0.9A, a 5V) 
USB 4 funciona con conectores USB tipo C 
Además de USB Power Delivery, la tecnología USB4 soporta distintos modos de transferencia de datos, 
aprovechando otros protocolos, como por ejemplo el USB 3.2, el DisplayPort (para conectar una 
pantalla por USB-C) y el PCI Express, o poder utilizar un SSD NVMe de forma externa. Esto dependerá 
del tipo de dispositivo, (no es lo mismo un ordenador que un hub), un ordenador debe soportar la 
conexión de una pantalla vía DisplayPort con ese conector USB4 USB-C, pero no es obligatorio el PCI 
Express. 

<!-- Page 18 -->

 
 
Periféricos: conectividad y administración 
18 
 
 
 
+ Info 
Wikipedia pública una tabla interesante en su web basándose en la 
especificación original. 
https://en.wikipedia.org/wiki/USB4 
 
 
Al igual que en versiones anteriores, en USB4 hay dos variantes: 
• USB4 Gen 2×2 con velocidad de transmisión a 20 Gbps.  
• USB4 Gen 3×2 con velocidad de transmisión a 40 Gbps. 
USB 4 es un protocolo que soporta dual-lane, es decir, en USB4 40 Gbps podremos tener una 
transferencia de entrada de hasta 20 Gbps y una de salida de hasta 20 Gbps a la vez. 
1.2.1.5.3. Otras especificaciones USB 
• USB On-The-Go (USB OTG): 
Es una especificación que permite a los dispositivos USB elegir el estado de cada puerto, es 
decir, actuar como servidor de datos o receptor de datos. 
De esta forma se puede transferir datos desde un puerto servidor hasta otro receptor sin usar 
un ordenador. 
• Wireless USB (WUSB): 
Wireless USB es un dispositivo para conectarnos a una red de forma que usamos transferencia 
inalámbrica. 
En USB 2.0. sus características son de una velocidad de 480 Mbps a menos de 3 metros de 
distancia, y 100 Mbps a menos de 10 metros. 
1.2.1.5.4. Puertos Apple 
Apple por su lado tiene un desarrollo y evolución del mismo propia. En 2003 aparece el iPod de tercera 
generación y con él el conector de 30 pines. Este conector fue utilizado en distintos modelos iPod, 
iPhone y iPad durante más de diez años. 

<!-- Page 19 -->

 
 
Periféricos: conectividad y administración 
19 
Sin embargo, el Lightning los sustituirá a partir de septiembre del 2012 con el iPhone 5. El conector de 
30 pines usado para transmitir audio, video, datos y energía tuvo que usar adaptadores que le 
permitieran seguir usándolo con la nueva tecnología. 
 
De la misma manera, pero esta vez obligado por la normativa europea, la tecnología Lightning será 
sustituida por el USB-tipo C, obligatorio a finales de 2024. 
Apple ya ha hecho la transición para su modelo iPhone 15 salido al mercado a fina-les de septiembre de 
2023. 
1.2.1.6. SATA 
Es un estándar basado en una comunicación en serie. 
Los discos duros magnéticos SATA (mayor velocidad) han sustituido a los de conexión IDE, se conectan 
a puertos SATA de la placa base. 
Con su aparición, las placas base pasaron a fabricarse con puertos IDE y SATA, y actualmente sólo se 
fabrican con puertos SATA. Los discos IDE ya no se fabrican, pero sigue habiendo ordenadores 
funcionado con este tipo de disco. 

<!-- Page 20 -->

 
 
Periféricos: conectividad y administración 
20 
1.2.1.7. Thunderbolt 
 
Thunderbolt es una conexión para periféricos basada en las arquitecturas PCI Express y DisplayPort 
desarrollada por Intel en colaboración con Apple. 
En sus primeras versiones tenía hasta 10 W de alimentación. 
Características de Thunderbolt: 
• Puede usarse como conector de datos o de transferencia de vídeo y sonido. 
• Es muy rápido. 
• Sus versiones son retro compatibles (aunque la última versión requiere un adaptador). 
Versiones de Thunderbolt: 
• Thunderbolt. Transferencia de 10Gb/s. (10 W). 
• Thunderbolt 2. Transferencia de 20Gb/s. (10 W). 
• Thunderbolt 3. 
• Transferencia de 40Gb/s. 
• Utiliza el conector USB tipo C. 
• Soporta dos monitores de 4 K o uno de 5 K de resolución. 
• 100 W de potencia para suministrar energía o recibirla. 
• Thunderbolt 4. 
• Ancho de banda bidireccional de 40 Gbps, al igual que en la versión 3. 
• Mayores longitudes de cable, hasta cables de 2 metros, (con pretensión de alcanzar hasta 
los 50 metros). 
• Doble de requisitos mínimos respecto a datos y vídeo que ofrecía Thunderbolt 3. 
» Datos: se duplica el ancho de banda de los puertos PCIe, pasando de 16 a 32 Gbps. 
» Vídeo: este aumento de datos permite soporte para dos pantallas de 4K o una de 8K. 

<!-- Page 21 -->

 
 
Periféricos: conectividad y administración 
21 
• Permite accesorios con hasta cuatro puertos. 
Soporte para docks con hasta cuatro puertos Thunderbolt 4, el PC se carga en, al menos, un 
puerto. 
• Se puede activar el ordenador tocando el teclado o ratón cuando esté conectado a una 
dock de Thunderbolt 4. 
Dock o docking station es una estación de acoplamiento o un replicador de puertos 
(concentrador). 
• 100 W de potencia para suministrar energía o recibirla. 
Puedes cargar un teléfono móvil, (que requiere menos de 100 W) y otros dispositivos USB 
compatibles rápidamente. 
• Redes. 
Permite conexión a una red Ethernet de 10 Gigabit de alta velocidad mediante un 
adaptador, y también utilizar un cable Thunderbolt para conectar dos ordenadores por 
medio de una red punto a punto, lo que permite transferir grandes volúmenes de datos de 
un ordenador a otro. 
1.2.1.8. Puertos y conectores TS/TRS/TRRS 
Los puertos y conectores TS sirven de entrada para micros, teclados, guitarras... o salida para altavoces 
o amplificadores. Los puertos y conectores TRS se usan para auriculares, micrófonos, smartphones y 
tablets y de salida para altavoces, auriculares, tarjetas de sonido e interfaces de audio. Su tamaño 
estándar es de 6.35mm pero existen tamaños de 3.5mm para ordenadores portátiles, tablets, 
smartphones, de 2.5mm para auriculares o micrófonos miniatura. 
 

<!-- Page 22 -->

 
 
Periféricos: conectividad y administración 
22 
La cantidad de anillos y su uso determinan el tipo de señal que el cable puede transmitir. 
TS, audio mono, TRS estéreo, TRRS estéreo y micro. Las siglas responden a cada parte del conector T -> 
Tip: punta, R-> Ring: anillo, S -> Sleeve: manga. 
Técnicamente, los conectores TR, TRS y TRRS no se consideran parte del hardware interno de un 
ordenador, sin embargo, sí juegan un papel crucial en la interfaz de hardware que permite la 
comunicación entre el ordenador y los dispositivos externos, como auriculares, micrófonos, 
instrumentos musicales, altavoces y otros equipos de audio. 
1.2.2. Puertos virtuales 
Son los utilizados en los protocolos de Internet como UDP (Protocolo de datagramas de usuario) o TCP 
(protocolo de control de transmisión, que es el protocolo más utilizado en Internet, orientado a la 
conexión, es decir, los datos pueden enviarse de forma bidireccional una vez establecida la conexión). 
Son como puntos de conexión para el intercambio de información y la transmisión de datos. Los datos 
viajan desde un puerto en el dispositivo inicial y se dirigen hacia e extremo receptor de la línea. 
 
 
 
 
+ Info 
Un número de puerto es un número entero de 16 bits, para 
identificar puertos de red específicos manteniendo la dirección IP 
relacionada y el protocolo aplicado para la conexión. 
 
1.3. Administración del sistema de entrada/salida 
El sistema de entrada/salida es la parte del sistema operativo encargada de la gestión de los dispositivos 
de E/S (periféricos), actuando como interfaz entre los dispositivos de E/S y el resto del sistema. 
Existe unas diferencias de velocidad entre la CPU y los periféricos de E/S, y además el tiempo de 
respuesta de dichos periféricos no es previsible, por lo que necesitamos un mecanismo que permita 
coordinar adecuadamente las transferencias de datos entre ambos. 
Objetivos 
Los objetivos de la administración del sistema de E/S son: 
• Facilitar el manejo de los dispositivos periféricos ofreciendo una interfaz entre los dispositivos y 
el resto del sistema. 
• Optimizar las operaciones de E/S. 

<!-- Page 23 -->

 
 
Periféricos: conectividad y administración 
23 
• Generar dispositivos virtuales que permitan conectar cualquier tipo de dispositivos físicos. 
• Facilitar la conexión de un nuevo dispositivo, instalando automáticamente los controladores 
necesarios (Plug&Play). 
1.3.1. Controlador de E/S 
Es el responsable de controlar los periféricos y el intercambio de datos entre estos y la memoria 
(principal o registros de la CPU). 
Tiene dos interfaces, una para conectarse con el ordenador y otra para conectarse con el periférico. 
Sus funciones principales son: 
• Gestionar la comunicación con la CPU y el periférico. 
• Servir de almacén temporal de datos. 
• Detectar errores. 
• Gestión de la memoria y el bus. 
Tipos de gestión de las E/S con la CPU 
Mecanismos básicos para sincronizar las operaciones de E/S con las de la CPU. Vas a estudiar 4 tipos: 
1. E/S controlada por programa: los datos se transfieren entre la CPU y el controlador de E/S. 
Esto está controlado por un programa que ejecuta la CPU. 
Cuando la CPU lanza una orden al controlador de E/S se queda esperando hasta que finaliza la 
operación de E/S, comprobando continuamente el estado del periférico. A esto se le llama bucle 
de espera activa. 
Con este método se pierde tiempo al tener que esperar la CPU a que el periférico esté 
preparado. Además, mientras está atendiendo a un periférico desatiende al resto. 
2. E/S controlada por interrupciones: la CPU envía la orden de E/S y prosigue con otras tareas en 
lugar de esperar. 
Cuando el periférico está preparado lanza una interrupción a la CPU solicitando que atienda a su 
petición de E/S. Esto lo hace activando una línea especial del bus de control denominada "línea 
de petición PI". 
La CPU transfiere los datos y continua con la ejecución del programa que había interrumpido. 

<!-- Page 24 -->

 
 
Periféricos: conectividad y administración 
24 
3. DMA (acceso directo a memoria): el problema de los dos métodos anteriores es que necesitan a 
la CPU para la transferencia de datos entre la memoria y el periférico, ocupando tiempo de CPU. 
Para solucionar este problema aparece DMA. 
Requiere un módulo adicional denominado "controlador de DMA", que va conectado al bus del 
sistema y que puede asumir las funciones que realizaba la CPU. La CPU solo participa al 
comienzo y al final de la transferencia. 
El controlador de DMA contiene: 
• Registro de datos. 
• Registro de dirección. Almacena la dirección de la siguiente palabra a trasmitir y, una vez 
transmitida, se autoincrementa. 
• Registro contador. Contiene el número de palabras que se tienen que quedan por 
transmitir. Cada vez que se transmite una palabra se autodecrementa. 
• Unidad de control. Comprueba el valor del registro contador y, si este vale cero, envía una 
interrupción a la CPU indicando el fin de la operación. 
4. Procesador de E/S (PE/S): es un controlador de E/S convertido en procesador. Contiene un 
conjunto de instrucciones de E/S que le dan el control completo de la operación. 
 
 
 
 
+ Info 
En realidad, la administración de los sistemas de E/S es mucho más 
compleja y extensa. 
No es necesario profundizar más en el tema. 
 
2. Hardware de entrada. Teclado y ratón 
Existen muchos periféricos de entrada: micrófonos, webcam etc. pero vamos a estudiar los más 
importantes que son el teclado y el ratón. 
 

<!-- Page 25 -->

 
 
Periféricos: conectividad y administración 
25 
 
 
 
Anécdota 
Muchos usuarios, acostumbrados a utilizar sistemas operativos 
como MS-DOS, o programas a medida donde la interfaz no hacía 
uso de ratón, utilizan las combinaciones de teclas para realizar 
acciones que se suelen hacer con el ratón. 
 
2.1. Teclado 
 
Fuente: pxhere. Foto libre de alta resolución de máquina de escribir. 
Museo criptológico. National Cryptologic Museum 
Los teclados están basados en la máquina de escribir en la que cada tecla corresponde a uno o más 
caracteres. En el teclado, las teclas también pueden corresponder a funciones y órdenes. En ocasiones 
puede ser necesario pulsar simultáneamente dos o más teclas. 
Al pulsar una tecla se cierra un conmutador que hay en el interior del teclado. Esto hace que unos 
circuitos codificadores generen el código de E/S correspondiente al carácter seleccionado (según el 
sistema de representación). Normalmente se replica este carácter para que aparezca en pantalla. 
Según las normas ANSI (American National Standars Institute) los teclados contienen los siguientes 
tipos de teclas: 
• Teclado principal: contiene los caracteres alfabéticos, numéricos y especiales. 
• Teclas de desplazamiento: permiten realizar diversas operaciones como mover el cursor, borrar 
un carácter o parte de una línea. 

<!-- Page 26 -->

 
 
Periféricos: conectividad y administración 
26 
• Teclas numéricas: en los teclados, las teclas correspondientes a los caracteres numéricos (cifras 
decimales), signos de operaciones básicas (+, -...) y punto decimal estén repetidas y 
posicionadas juntas a la derecha para facilitar la introducción de datos numéricos con la mano 
derecha. En los portátiles se suele omitir esta parte para reducir tamaño. 
• Teclas de funciones: son teclas cuyas funciones son definibles por el usuario o por un programa. 
• Teclas de funciones locales: controlan funciones propias del ordenador. Por ejemplo, imprimir 
pantalla. 
 
 
 
 
+ Info 
Los teclados que se utilizan principalmente en las regiones 
germano hablantes utilizan una distribución QWERTZ. 
 
 
Tipos según su funcionamiento 
Según el funcionamiento, en cuanto a la pulsación de las teclas, existen dos de teclado: 
• Mecánico. Cada tecla es un pulsador independiente. Un muelle la levanta al terminar de 
presionarla para que vuelva a su estado inicial. Son mucho más resistentes y duraderos. Son 
recomendables en entornos de trabajo con mayor suciedad ambiental (talleres, carpinterías con 
serrín…). 
• Membrana. Utilizan tres capas que, al pulsar, entran en contacto. 
 

<!-- Page 27 -->

 
 
Periféricos: conectividad y administración 
27 
 
 
 
El experto opina 
Nosotros preferimos el mecánico. Aunque a algunas personas les 
molesta el sonido, a nosotros nos encanta que suene cuando 
escribimos. 
Además, se adquiere mayor velocidad de escritura y los dedos se 
cansan menos (gracias al muelle de retorno). Si no tienes uno, 
¡deberías probarlos! 
 
Teclados de membrana 
Actualmente se utilizan teclados de membrana, y existen una gran cantidad de tipos, destacamos 
algunos de los principales: 
• Alfanumérico. Es el teclado estándar. Tiene las teclas especificadas por la ANSI que hemos visto 
anteriormente. 
• Teclado numérico. Contiene los números, operaciones, el punto para los decimales y la tecla 
"Intro". 
• Multimedia. Añade botones adicionales destinados al uso de programas multimedia (como 
control de volumen). 
• Inalámbrico. No requiere cables. La conexión al ordenador se hace por bluetooth o infrarrojos. 
• Flexible. Fabricado con silicona. Se puede doblar (o enrollar) y es resistente al agua. 
• Teclado virtual. Este nombre se utiliza para dos tipos de teclado: El teclado que aparece en las 
pantallas táctiles para simular uno real y el proyectado, el cual utiliza sensores para determinar 
las pulsaciones sobre una proyección de un teclado (parecido a los que puedes ver en las 
películas de ciencia ficción como Minority Report). 
• Braille. Teclado adaptado para el uso de invidentes. 
• Teclado touch. Es una pantalla que muestra un teclado que puedes configurar (añadir teclas, 
etcétera). 
• Ergonómico. Diseñado para las personas que hacen un uso extensivo del teclado. Buscan el 
mínimo esfuerzo y la máxima comodidad. 
 

<!-- Page 28 -->

 
 
Periféricos: conectividad y administración 
28 
 
 
 
El experto opina 
Nosotros no recomendamos el teclado ergonómico. No está 
demostrado que funcione realmente y, de todos modos, 
dependerá de la constitución física de la persona, de su postura, de 
sus hábitos, etcétera. 
Requiere de un periodo de aprendizaje y adaptación. 
 
2.2. Ratón 
 
Es un dispositivo que cuenta con un mecanismo que permite detectar el movimiento en dos 
dimensiones (izquierda, derecha, arriba y abajo). Al desplazar el ratón sobre una superficie plana, el 
movimiento se refleja en la pantalla a través del puntero (una flecha). 
Tiene dos o más botones que nos permiten realizar determinadas acciones: 
• Un clic. 
• Doble clic. 
• Arrastrar (mantener el botón pulsado mientras se mueve el ratón). 
• Scrolling: permite mover la barra de desplazamiento vertical (por ejemplo, para moverse arriba 
y abajo en un documento de Word). La mayoría de los ratones tienen una rueda en el centro 
para esta misión. 
Según la tecnología en que se basan, podemos definir los siguientes tipos de ratón: 
• Mecánicos: contienen una bola de plástico que, al desplazarlo por una superficie plana, mueve 
dos ruedas que envían las señales para reflejar este movimiento en la pantalla. 
• Ópticos: tienen un sensor que fotografía la superficie donde se encuentra y detecta las 
variaciones de posición del ratón. 
• Láser: el funcionamiento es similar al óptico, pero en lugar de un haz de luz utiliza un láser que lo 
hace más sensible y preciso. También le permite detectar movimiento en superficies irregulares. 

<!-- Page 29 -->

 
 
Periféricos: conectividad y administración 
29 
• Trackball: tiene una bola que se mueve con el dedo pulgar para indicar la dirección de 
movimiento. El dispositivo es estático (no se mueve, tan solo la bola). 
• TouchPad: presente en la mayoría de los portátiles, permite simular el movimiento del ratón 
mediante una pantalla táctil por donde se deslizan los dedos. 
 
 
 
 
+ Info 
Existe una línea de investigación para sustituir el mouse por otros 
dispositivos como, por ejemplo, el casco neuronal que te permite 
mover el puntero con la mente. 
Nosotros hemos probado el MindWave de NeuroSky y… ¡es 
impresionante! 
Recoge las ondas cerebrales y se asignan a distintas funciones. 
 
3. Hardware de almacenamiento 
Con periféricos de almacenamiento nos estamos refiriendo a la memoria secundaria, es decir la 
memoria permanente (no volátil). 
Vamos a ver algunos de los tipos de almacenamiento externo: 
• Cintas magnéticas. 
• Discos duros magnéticos. 
• Discos ópticos. 
• Memorias flash. 
• Discos de estado sólido (SSD). 
3.1. Cintas magnéticas 
Son dispositivos de entrada/salida de acceso secuencial, que permiten leer y escribir datos en un 
soporte magnético. Prácticamente no se utilizan por dos problemas principales: 
• Son muy lentas. 
• Al ser de acceso secuencial, no podemos intercalar información. Si se modifica parte de la 
información, se tiene que volver a escribir todo. 

<!-- Page 30 -->

 
 
Periféricos: conectividad y administración 
30 
Actualmente tan solo se usan para tareas de backup (copias de seguridad), dado que su coste es muy 
inferior al de los discos duros. 
Existen diversos tipos de cintas, pero la más importante es LTO (Linear Tape Open). Actualmente van 
por la octava generación (LTO-8), que permite almacenar 12 TB (TeraBytes) de forma nativa y 30 TB 
utilizando software de compresión. 
3.2. Discos duros 
Podemos hacer una clasificación de los discos duros basándonos en dos aspectos: 
• Según su ubicación respecto a la conexión: 
• Internos: conectados en el interior del ordenado, directamente a la placa base (conexión 
normalmente IDE o SATA). 
• Externos: conectados por el exterior del ordenador, normalmente a USB. 
• Según su arquitectura: 
• Discos Magnéticos (HDD). 
• Discos de estado sólido (SSD). 
3.2.1. Magnéticos 
 
Un disco duro magnético, está formado por uno o varios platos rígidos introducidos en una caja 
hermética y unidos por eje común que gira a gran velocidad. Sobre cada uno de los patos, que 
normalmente tienen sus dos caras destinadas al almacenamiento, se sitúan sendos cabezales de 
lectura/escritura. 

<!-- Page 31 -->

 
 
Periféricos: conectividad y administración 
31 
Componentes físicos que tienen un disco duro: 
• Componentes mecánicos: 
• Platos: 
Se guarda la información, dispuestos en forma horizontal y cada plato consta de dos caras o 
superficies magnetizadas, una cara superior y otra inferior. Normalmente son de metal, la 
información se guarda en celdas en donde es posible magnetizarlas de forma positiva o 
negativa (1 o 0). 
• Cabezal de lectura: 
Este elemento hace la función de lectura o escritura. Hay un cabezal por cada cara o 
superficie de plato, por tanto, si tenemos dos platos habrá cuatro cabezas lectoras, estas no 
deben hacer contacto con los platos, ya que la superficie quedaría rayada y se corromperían 
los datos. Se crea una fina capa de aire de unos 3mm de separación al girar los platos, 
impidiendo dicho contacto. 
• Brazo mecánico: 
Sujetan las cabezas lectoras, y las desplazan de forma lineal desde el interior al exterior de 
los platos de forma muy rápida para permitir el acceso a la información de los platos. 
• Motores: 
Hay dos motores dentro de un disco duro, uno para hacer girar los platos, (velocidad de 
entre 5000 y 7200 revoluciones por minuto (rpm)), y otro para el movimiento de los 
brazos mecánicos. 
• Otros componentes físicos: 
• Circuito electrónico: 
Se encarga de gestionar las funciones de posicionamiento del cabezal y la lectura y 
escritura de este, y también de comunicar el disco duro con el resto de componentes del 
ordenador, traduce las posiciones de las celdas de los platos a direcciones comprensibles 
por la memoria RAM y CPU. 
• Memoria caché: 
Tienen un chip de memoria integrada en el circuito electrónico que hace de "puente" de 
intercambio de información desde los platos físicos hasta la memoria RAM. 
• Puertos de conexiones: 
En la parte trasera del disco están los conectores, el de alimentación (12v), y el del bus para 
conectar con la placa base (si es un disco duro IDE también tiene las ranuras de jumpers 
para seleccionarlo como master, esclavo o cable select). 

<!-- Page 32 -->

 
 
Periféricos: conectividad y administración 
32 
Existe una estructura física y lógica en un disco duro, en cada plato del disco duro, no se trata 
simplemente de grabar la información aleatoriamente, tienen su propia estructura lógica que permiten 
el acceso a información concreta almacenada en ellos: 
• Pista (track): 
Cada una de las caras del disco se divide en anillos concéntricos, desde el interior hasta el 
exterior de cada cara. El borde exterior del disco duro es la pista 0. 
• Cilindro: 
Es un concepto que engloba un conjunto de varias pistas. Un cilindro lo forman todas las 
circunferencias que están alineadas en forma vertical de cada uno de los platos y caras, (como 
un cilindro imaginario). 
• Sector: 
Las pistas están divididas en trozos de arco llamados sectores. En estos tramos es donde se 
almacenan los bloques de datos. 
• Cluster (o unidad de asignación): 
Un archivo no puede ocupar menos de un cluster (que es la unidad mínima asignada por el 
Sistema Operativo), sin embargo, pueden perfectamante ocupar más, dependiendo de la 
información que contenga. 
 
 
 
 
+ Info 
Sector de arranque MBR (Master Boot Record): 
Es el 1er sector de todo el disco duro, es decir, pista 0, cilindro 0 
sector 1, y aquí se almacenan 2 cosas importantísimas: 
• La tabla de particiones que contienen toda la información 
acerca del inicio y el final de las particiones. 
• El programa Master Boot Code, que es el encargado de leer 
la tabla de particiones y proporcionar el control al sector de 
arranque de la partición activa. De esta forma el ordenador 
arrancará desde el sistema operativo de la partición activa. 
(Cuando tenemos varios sistemas operativos instalados en 
distintas particiones, será necesario la instalación de un gestor de 
arranque (bootloader) para que podamos elegir el sistema 
operativo que queremos arrancar). 
 

<!-- Page 33 -->

 
 
Periféricos: conectividad y administración 
33 
Este tipo de soporte de almacenamiento presenta estas características principales: 
• Es no volátil (lo guardado no se pierde al dejar de suministrar corriente). 
• Accede de forma directa a los datos (al contrario que la cinta). 
• Tienen gran capacidad. 
Su funcionamiento está basado en la grabación magnética de datos en las superficies de uno o más 
platos (discos) rígidos que giran sobre un eje metálico común. 
La grabación sobre el disco se realiza en circunferencias concéntricas denominadas pistas. Se numeran 
de fuera a dentro, empezando por 0. 
Cada pista se divide en sectores por unos ejes radiales, y estos se numeran en una secuencia única para 
todo el disco. Dependiendo del sistema de archivos o formato (NTFS, exFAT, FAT32), se pueden 
asignar los siguientes tamaños de bloque: 512, 1024, 2048, 4096 u 8192 bytes, o bien 16, 32 o 64 
kibibytes. 
Los sectores de las pistas exteriores tienen una longitud lineal son mayores que los de las interiores 
(dado que cada pista tiene el mismo número de sectores), por lo que la densidad de información (bits 
grabados por pulgada) es mayor en el interior. 
La cabeza de lectura/escritura se encarga de grabar y leer los datos en la superficie del disco. Hay dos 
tipos de cabezas: 
• Fija. No se mueve. Necesitaremos una por cada pista de cada disco. (Sistema abandonado). 
• Móvil. Posee un brazo metálico que le permite posicionarse sobre la pista que vamos a utilizar. 
Es la más usual. 
Vamos a ver cómo funcionaría un disco con brazo móvil. 
Cuando realizamos una operación de lectura o escritura, el brazo posiciona la cabeza en la pista donde 
se encuentra el sector que queremos leer y espera a que el sector en cuestión se posicione debajo de la 
cabeza (dado que los discos van girando). 
Por lo tanto, en la lectura o escritura de datos, debemos considerar tres tiempos distintos: 
• Tiempo de búsqueda: tiempo que tarda la cabeza en posicionarse sobre la pista o cilindro en 
cuestión. 
• Tiempo de espera (o latencia rotacional): tiempo que tarda el sector en posicionarse debajo de 
la cabeza debido al giro de los discos. 
• Tiempo de lectura o escritura: tiempo que tarda en leer o escribir un número determinado de 
bytes. 

<!-- Page 34 -->

 
 
Periféricos: conectividad y administración 
34 
De estos derivan el tiempo de acceso. Es el tiempo que tarda la cabeza en posicionarse sobre el sector y 
equivale a la suma del tiempo de búsqueda y el tiempo de espera. 
Hay que tener en cuenta los siguientes conceptos: 
• Sectorización hardware o física. 
Los platos de discos suelen tener una o varias referencias físicas (orificios o muescas) para 
poder identificar los sectores y pistas del plato. 
• Sectorización software o lógica. 
Antes de utilizar un disco debemos darle formato. Al formatear un disco se definen por software 
las pistas y sectores que pueden no coincidir con los sectores hardware. Detecta y elimina las 
zonas de disco dañadas. 
Hay distintas formas de formateas un disco, y distintos formatos: FAT32, NTFS, exFAT, que veremos un 
poco más adelante. 
Prestaciones de los discos duros 
Para medir las prestaciones de los discos duros se utilizan los siguientes parámetros: 
• Capacidad. 
Cantidad de información que se puede grabar. Hoy en día se mide en terabytes. 
• Tiempo medio de acceso (TMA). 
Es uno de los más importantes. Es el tiempo medio de búsqueda y posicionamiento de las 
cabezas del disco duro en un cilindro (o pista) determinado. Tenemos que medir el tiempo 
medio, ya que el acceso a cada pista tarda un tiempo diferente. 
• Velocidad de rotación. 
Es la velocidad a la que giran los platos. Se mide en r. p. m. (revoluciones por minuto). A mayor 
velocidad, mayor tasa de transferencia, pero también mayor ruido y calentamiento. 
• Velocidad de transferencia de datos (data transfer rate). 
Cantidad máxima de información que se transfiere por unidad de tiempo. 
• Posicionamiento pista a pista (TMB). 
Tiempo medio que tardan las cabezas en cambiar de un cilindro a otro contiguo. 
• Tiempo medio entre fallos (MTBF o Mean Time Between Failure). 
Es la medida del tiempo que transcurre desde que se produce un fallo hasta que se produce otro 
fallo. 

<!-- Page 35 -->

 
 
Periféricos: conectividad y administración 
35 
• Memoria caché (buffer). 
Es una memoria situada en la controladora del disco. Todos los datos que se leen y escriben a 
disco duro se almacenan primeramente en el buffer. 
• Tamaño. 
Hay dos tamaños principales: 3,5 pulgadas y 2,5 pulgadas. Los primeros se utilizan como discos 
internos mientras que los segundos se suelen utilizar como discos externos (aunque pueden 
utilizarse como discos internos en portátiles para ahorrar espacio). 
Interfaces del disco duro 
Los discos duros internos utilizan varios tipos de interfaces para conectarse al ordenador: 
• ATA (IDE): El estándar ATA (Advanced Technology Attachment) es una interfaz estándar que 
permite conectar distintos periféricos de almacenamiento al ordenador. Es más conocido por su 
término comercial IDE (Integrated Drive Electronics) o su versión mejorada E-IDE mejorado 
(Enhanced IDE). 
Se desarrolló una extensión llamada ATAPI (ATA Packet Interface) que permite conectar 
periféricos de almacenamiento como lectores/grabadores de CD o DVD. 
Para distinguirlo del posterior estándar Serial ATA (SATA), a veces se lo denomina P-ATA 
(Parallel ATA). Utiliza un cable plano de 40 u 80 hilos con tres conectores: uno para la placa 
base y dos para dispositivos. En cada canal, un dispositivo se configura como maestro y el otro 
como esclavo. Se soportan dos canales (primario y secundario), permitiendo hasta 4 
dispositivos en total. 
Evolución del estándar ATA: 
• ATA-4: Introdujo Ultra DMA/33 (33 MB/s). 
• ATA-6: Alcanzó 66 MB/s (Ultra DMA/66). 
• ATA-7: Llegó a 100 MB/s (Ultra DMA/100) y finalmente 133 MB/s (Ultra DMA/133). 
• SATA. 
Sustituye a la anterior para discos rígidos y dispositivos ópticos. 
El estándar Serial ATA pueden conseguir velocidades de: 
• 1,5 Gb/s (187,5 MB/s). Dato que cada octeto se envía con 1 bit de arranque y otro de 
parada, la velocidad efectiva sería 150 MB/s. 
• 3 Gb/s (375 MB/s). Velocidad efectiva de 300 MB/s. 
• 6 Gb/s (750 MB/s). Velocidad efectiva de 600 MB/s. 
Los cables SATA utilizan siete hilos y conectan un solo dispositivo por cable. Los dispositivos 
SATA permiten la conexión en caliente (sin apagar el equipo). 

<!-- Page 36 -->

 
 
Periféricos: conectividad y administración 
36 
 
 
 
+ Info 
ATA es una versión avanzada de la tecnología IDE. Pero 
tradicionalmente se le ha seguido llaman dos discos IDE a los 
discos ATA. 
Los discos ATA pueden ser P-ATA que son la versión que todo el 
mundo llama IDE. 
Y los S-ATA que es la última versión con la que estamos trabajando 
y que ha dejado obsoleta a la P-ATA (o IDE). 
 
 
Evolucion de Tecnología de discos duros 
• SCSI. 
El interfaz SCSI (Small Computers System Interface) permite la conexión de distintos tipos de 
periféricos a un ordenador mediante una tarjeta denominada adaptador o controladora SCSI o 
controlador SCSI. 
El número de periféricos que se pueden conectar depende del ancho del bus SCSI. El estándar 
SCSI-3 permite conectar 32 dispositivos (31 más la controladora SCSI) y tiene una velocidad 
máxima de 640 MB/s en modo Ultra-640. 
• SAS (Serial attached SCSI). 
Es la evolución de SCSI. Tiene velocidades similares a SATA, es compatible con este y permite 
conectar hasta 16.384 dispositivos SAS manteniendo el rendimiento y la fiabilidad. Además, al 
contrario que SCSI, permite la conexión en caliente. 
También tenemos los discos duros externos que normalmente se conectan a puerto USB, o Firewire. 

<!-- Page 37 -->

 
 
Periféricos: conectividad y administración 
37 
3.2.2. Unidades de Estado Sólido (SSD) 
Una unidad SSD es un sistema de almacenamiento de información que usa memoria de tipo flash. 
Al igual que los tradicionales discos magnéticos se componen de interfaz, controladora, memoria cache 
y otras partes. 
Quizás la parte que actualmente marca la diferencia, es el controlador, es la parte que los fabricantes 
personalizan con diferentes niveles de software para mejorar en velocidad, durabilidad y seguridad, 
frente a la competencia. 
Tipos de SSD según su conexión física 
Los dos tipos de SSD, más usadas a principios del 2022, según su conexión física, son la SATA y la PCIe: 
• SATA en su versión 3 nos permite un ancho de banda de 600 MB/s por canal. 
• PCIe Gen 4 admite hasta 2000 MB/s, siendo claramente más rápida y la que (a fecha actual) 
está imponiéndose en el mercado. 
Protocolos 
En Los discos SSD podemos encontrarnos con el veterano AHCI (Advanced Host Controller Interface) 
heredado de los discos duros clásicos y utilizado en la interface SATA. 
O con el NVMe, diseñado para las unidades SSD. 
El NVMe, que ha sido creado pensando en el modo de funcionamiento de una unidad SSD tiene una 
abismal diferencia de funcionamiento. 
Por ejemplo, admite IOPs de más de un millón frente al límite de 100.000 IOPs de las unidades AHCI. 
 
 
 
 
+ Info 
IOPS son las siglas de Inputs Outputs Per Second (Entradas Salidas 
Por Segundo). 
Es un método común para medir el rendimiento de los discos 
duros, como SATA, SAS y SSD. 
 

<!-- Page 38 -->

 
 
Periféricos: conectividad y administración 
38 
Formas y tamaños 
Podemos encontrar con interface SATA diversos tamaños, 3.5, 2.5 y 1.8 pulgadas, aunque en la 
actualidad la inmensa mayoría son de 2.5 y 7mm de ancho (Aunque también los hay de 9,5mm). 
También existe una versión mSATA, abandonada al salir el formato M.2. 
SSD M2 es un formato de las unidades de estado sólido (Solid State Drive), de un tamaño muy 
pequeño, que proporciona una unidad de almacenamiento ultrarrápida. 
Las unidades SSD M2 se conectan a un zócalo distinto, y que tan solo está incluido en las placas base 
más modernas. El formato más utilizado en el M2 2280 (22 mm de ancho y longitud de 80 mm), 
estando también el formato 2260 (22 mm de ancho y longitud de 60 mm), y el 2242 (22 mm de ancho 
y longitud de 42 mm). 
El formato M.2 está disponible para conexiones SATA y PCIe. 
• M2 SATA: velocidad de transferencia de datos de hasta 6 Gbps. 
Ofrecen menor rendimiento que los NVMe pero son más económicos. 
• M2 NVMe: es un protocolo que combinado con el bus PCIe 4.0 permite alcanzar velocidades de 
transferencia de hasta 16 Gbps. 
Es el uso de la tecnología NVM lo que permite un mayor rendimiento y no el factor de forma M2. 
Es solo compatible con placas base que cuentan con conectores PCIe de NVMe. 
 
 
 
 
 
+ Info 
Puedes utilizar SSD NVME como una unidad externa USB utilizando 
una carcasa compatible. Si deseas consultar más información sobre 
esto puedes visitar la web: 
https://www.profesionalreview.com/2020/12/22/convertir-ssd-
m2-nvme-en-externo-usb/ 
 

<!-- Page 39 -->

 
 
Periféricos: conectividad y administración 
39 
Tecnologías de fabricación 
La mayoría de unidades SSD basan su funcionamiento en una arquitectura construida con puertas NAND. 
La clasificación principal es en función de los bits que cada celda de esa memoria flash pueda almacenar. 
Actualmente los principales tipos son: 
• SLC (Single Level Cell): solo son capaces de almacenar un bit de información por celda, 
pudiendo escribir en ellos dos estados (0 o 1). Son las más rápidas debido a que solo hay que 
comprobar dos situaciones, además de las más duraderas (hay que comprobar menos veces 
cada celda), pero el precio del GB es el más alto al requerir más elementos para almacenar la 
misma información. 
• MLC (Multi-Level Cell): ya poseen dos bits por celda, por lo que podemos almacenar más 
información, perdiendo velocidad y vida útil. 
• TLC (Triple Level Cell): con tres bits por celda, admiten mucha capacidad de almacenamiento 
con menos requerimiento de componentes y por ello de espacio, perdiendo velocidad y vida útil. 
• QLC (Quad Level Cell): los más económicos de todos al usar cuatro bits de información por 
cada celda, lo que permite tener grandes capacidades de almacenamiento, pero a costa de ser 
los más lentos y con menor vida útil. 
Conforme aumenta la cantidad de bits que se pueden almacenar por celda, la corrupción de datos se 
incrementa y por ello los fabricantes deben integrar mejores y más precisos mecanismos de corrección 
de errores, los cuales se incluyen en el controlador. 
Esos mecanismos se encargan, entre otros menesteres, de detectar las celdas que por desgaste ya no 
son fiables a la hora de almacenar la información. Con el tiempo, si la unidad SSD es muy propensa a 
esos errores, esas celdas se irán perdiendo y con ello la capacidad de almacenamiento de la unidad SSD. 
Por tanto, dependiendo del uso al que vayamos a someter a la unidad SSD, deberemos elegir entre los 
diferentes tipos, lo que a su vez y junto con la calidad, nos marcara el precio de nuestra unidad. 
Evolución 
Para conseguir mejoras en el rendimiento de las memorias basadas en NAND, los fabricantes utilizan 
combinaciones y sistemas híbridos para diseñar las nuevas memorias. 
También hay avances en el diseño de las celdas, como ocurre con las unidades de tipo SSD 3D NAND y 
V-NAND. 
En su diseño más básico, una memoria NAND contiene una sola capa de celdas de memoria. 
Con avances en la fabricación se han ido reduciendo el tamaño de esas celdas y con ello aumentado la 
capacidad de almacenamiento en el mismo espacio. Pero esto conlleva mayores riesgos de 
interferencias eléctricas y una menor resistencia a procesos de escritura/lectura. 

<!-- Page 40 -->

 
 
Periféricos: conectividad y administración 
40 
Para solucionarlo, la industria construye unidades SSD con apilamiento de las celdas en múltiples capas. 
Ese diseño vertical admite más densidad de celdas al tiempo que hay una separación entre celdas 
mayor, aunando las ventajas de una alta densidad de celdas al tiempo que se minimizan los 
inconvenientes e incrementan prestaciones. 
• 3D NAND: 
Se trata de una tecnología donde las celdas se apilan también verticalmente (3D) y no solo a lo 
largo y ancho (2D), lo cual permite hacer las celdas más grandes y, por lo tanto, mejor aisladas. 
La primera memoria flash 3D NAND fue de Samsung y se llamaba V-NAND: 
• 3D V-NAND 
Las memorias V-NAND, o 3D V-NAND son la una evolución de la tecnología NAND donde 
se apilan verticalmente (de aquí la V de V-NAND) las celdas de memoria NAND. 
Debido al cambio en la disposición vertical de las células, estas unidades SSD son más 
densas, tienen un coste de producción más bajo y consumen la mitad de energía, también 
son el doble de rápidas y tienen una duración unas diez veces mayor que las memorias 
NAND normales. 
Funcionamiento 
La cantidad mínima de información que se puede leer o escribir no es la de una celda, ni la de la 
agrupación de éstas en palabras, sino que son las páginas, las cuales se agrupan a su vez en bloques. 
En el momento en que la información de una página debe cambiar, ésta se copia a otra del mismo 
bloque que esté vacía o libre, y a la primera el sistema le coloca un marcador para que pueda ser 
borrada. Cuando se necesita esa página de nuevo porque no queda ninguna sin usar, se procede a su 
borrado. 
La operación de borrado se realiza a nivel de bloque, lo que supone que, si necesitamos borrar alguna 
página de un bloque, previamente hay que mover todas las páginas en uso de ese bloque a uno vacío. 
Esta forma de gestionar la información provoca que con el tiempo y a mayor información almacenada, 
los SSD empeoren en su rendimiento, y para evitar que esto suceda y la velocidad de escritura/lectura 
siga siendo alta, los controladores son clave en todo el proceso. 
La denominada "recolección de elementos no utilizados o basura", es una especie de mantenimiento 
que se suele realizar cuando el SSD no está en uso intensivo, y en el que el controlador, de forma 
periódica, copia todos los datos válidos de una página en uso y los pasa a páginas vacías de otro bloque, 
de esta forma, ya se puede realizar el borrado de las celdas del bloque actual y dejarlo preparado para 
que cuando sea necesario, el SSD pueda escribir nuevos datos. 
Todo ese proceso de borrado conlleva un desgaste de los transistores, el cual puede llegar un momento 
en que el controlador los deje marcados como no válidos para almacenar información. Ese proceso se 
denomina P/E (Program/Erase) y es lo que marca la durabilidad de un SSD. 

<!-- Page 41 -->

 
 
Periféricos: conectividad y administración 
41 
El ciclo de vida de un disco SSD se puede indicar en ciclos de P/E o en información total que se puede 
escribir en el SSD antes de que comiencen a aparecer errores. 
La unidad es TW (TeraBytes Written). Otra medida de la fiabilidad de un disco SSD es MTBF (Mean 
Time Between Failures), que cambia el valor de fiabilidad a tiempo en vez de a cantidad de información 
que puede escribir. 
Firmware FTL (Flash Tranlation Layer) 
FTL (Flash Translation Layer) es una capa de software (firmware) situada entre el controlador y la 
unidad SSD. Se encargará de traducir las operaciones de entrada y salida (E/S) de la capa de 
abstracción de almacenamiento (ATA o SCSI) al protocolo de almacenamiento flash. 
• Wear Levelling: es una de las tecnologías usadas por el FTL se denomina Wear Levelling y 
básicamente consiste en hacer un reparto equitativo de la información en todas las celdas de las 
memorias flash, para evitar excesos de procesos de borrado/escritura en algunas celdas 
concretas. El Wear Levellin es un algoritmo del que se encarga el FLT y tiene por fin que la 
memoria flash sufra un desgaste homogéneo evitando sobreutilizar una área en concreto. 
• Caché: LBA (Logical Block Address) es un número identificador de un bloque de datos de la 
unidad. La memoria caché de las unidades SSD almacena los bloques de datos que se acceden 
con más frecuencia, lo que reduce el tiempo de acceso a los datos. Para no ralentizar el 
funcionamiento de un SSD, las peticiones de direcciones LBA del sistema operativo al SSD deben 
agilizarse, para lo que es necesario que el controlador del SSD conozca en todo momento qué 
información está en qué bloque. Reserva una parte de la memoria flash para tal fin (memoria 
caché), que debe ser accesible a mayor velocidad que a la memoria NAND de las celdas, es la 
caché de un SSD, en ocasiones cuenta así mismo con una memoria DRAM que sería un primer 
nivel de caché. 
Si un disco SSD carece de caché DRAM, será más económica pero su funcionamiento estará alejado de 
lo ideal. 
3.2.3. Comparativa Discos HDD y SSD 
Los HDD tienen un factor más alto de averías por desgaste de los motores de rotación o de los 
cabezales, cosa que no ocurre en los SSD que no tienen partes móviles, y al no tenerlas, la latencia se 
elimina, por lo que son más rápidos, el acceso a los datos es instantáneo. 
El riesgo de fallo de los SSD, es el propio uso de ellos, tienen un número limita-do de ciclos de escritura-
borrado de cada celda (la lectura no afecta), cuando se llega a ese límite, puede comenzar a fallar o 
volverse inservible. Sin embargo, hoy en día, ese número de ciclos es tan elevado que un usuario 
doméstico es muy difícil que lo alcance, en caso de que ocurriera, el tiempo transcurrido sería 
equiparable al desgaste físico de un disco HDD. 

<!-- Page 42 -->

 
 
Periféricos: conectividad y administración 
42 
3.2.4. Formatear Discos Duros (Sectorización) 
Para poder utilizar cualquier tipo de dispositivo de almacenamiento externo: discos duros magnéticos, 
Discos SSD, memoria USB, tarjeta SD, debemos "formatearlos", es decir, indicar un sistema de archivos. 
Si no están "formateados", no podemos utilizarlos. Su estructura lógica debe tener un formato para que 
el sistema operativo sea capaz de comprender su estructura y de trabajar con ella. El sistema operativo 
no nos indica las diferencias entre ellos. 
Un sistema de archivos es un método que almacena y organiza los datos contenidos en los archivos 
informáticos y mantiene la ubicación física para que fácilmente se puedan encontrar y acceder a los 
archivos en el futuro. 
Existen varios tipos de formato diferentes en Windows, concretamente, podemos elegir entre 3 tipos 
de formatos diferentes: FAT, NTFS y ExFAT, veamos cómo de elegir el formato adecuado. 
3.2.4.1. FAT 
FAT, del inglés File Allocation Table, traducido como Tabla de asignación de archivos, es un sistema de 
archivos desarrollado para MS-DOS, que paso a ser también el sistema de archivos principal de las 
ediciones de Microsoft Windows hasta Windows Me. 
Las implementaciones más extendidas de FAT tienen algunas desventajas., cono son: 
• Cuando se borran y se escriben nuevos archivos tiende a dejar fragmentos dispersos de estos 
por todo el soporte. 
Con el tiempo, esto hace que el proceso de lectura o escritura sea cada vez más lento. 
Para solucionar este problema, se realizaba el proceso denominado desfragmentación, pero que, 
al ser muy lento, hacía incomodo su uso regular para mantener el sistema de archivos en 
condiciones óptimas. 
• FAT no fue diseñado para ser redundante ante fallos. 
• Inicialmente solamente soportaba nombres cortos de archivo. 
Soportaba ocho caracteres para el nombre más tres para la extensión. 
Indicamos algunas características de las distintas implementaciones de FAT: 
FAT12 
Totalmente en desuso. 
Fue la versión inicial de FAT (ahora conocida como FAT12), sus limitaciones eran: 
• No soporta anidación de carpeta. 

<!-- Page 43 -->

 
 
Periféricos: conectividad y administración 
43 
• Las direcciones de bloque solamente contienen 12 bits. 
• El tamaño del disco se almacena como una cuenta de 16 bits expresada en sectores, lo que 
limita el espacio manejable a 32 megabytes. 
FAT16 
Totalmente en desuso. 
El límite era de 2 GigaBytes de almacenamiento. 
En FAT16, la tabla de asignación de archivos (FAT) utiliza 16 bits para identificar clústeres. Esto 
significa que FAT16 puede direccionar hasta 216 = 65.536216 = 65.536 clústeres. 
El tamaño máximo de una partición dependerá del tamaño del clúster, pues será resultado de la 
multiplicación de 65.536 clústeres por el tamaño del mismo. 
Con FAT16 podemos encontrar distintos tamaños de clústeres, indicamos a continuación el tamaño 
posible de las particiones en base al tamaño del clúster: 
• 512bytes => 32MB (aproximadamente). 
• 4KB => 256MB (aproximadamente) MS-DOS en su versión 6.22 soporta hasta 4KB. 
• 32KB => 2GB (aproximadamente) Windows 95/98/ME. 
• 64KB => Sistemas operativos y Controladores de disco no estaban preparados para trabajar con 
clústeres tan grandes. La gestión de clústeres grandes podría haber llevado a problemas de 
rendimiento y eficiencia, lo que hizo que los clústeres de 64 KB no se utilizaran en la práctica. 
 
 
 
 
+ Info 
Volúmenes FAT16 mayores de 2 GB no son accesibles desde 
equipos con otros sistemas operativos MS-DOS, Windows 95, 
Windows 98, Windows Millennium Edition (Me). 
Esta limitación se debe a que estos sistemas operativos no son 
compatibles con tamaños de cluster mayores de 32 KB, lo que 
resulta en límite de 2 GB. 
 

<!-- Page 44 -->

 
 
Periféricos: conectividad y administración 
44 
FAT32 
Es el sistema más antiguo compatible, pero tiene limitaciones, se incorporó en Windows 95 y sustituyo 
al formato FAT16, aunque con limitaciones. 
• Ventajas: prácticamente cualquier dispositivo va a ser compatible con él, este formato va a 
poder leerlo dispositivos como un televisor, un móvil o una videoconsola, que en cambio a lo 
mejor no reconocerían el formato NTFS. 
• Limitación: no puede almacenar archivos de más de 4 GB. Actualmente archivos de vídeo o 
proyectos de ediciones fotográficas como los álbumes fotográficos ocupan más de 4 Gb 
habitualmente. Tampoco podemos creas particiones en FAT32 mayores de 8 TB. 
 
 
 
 
El experto opina 
FAT32 es ideal para memorias externas donde no vamos a guardar 
archivos mayores de 4GB, y queramos que sean compatibles con la 
mayoría de todo tipo de dispositivos. 
 
3.2.4.2. NTFS 
NTFS es el sistema de archivos más avanzado desarrollado por Microsoft y se ha convertido en el 
estándar para las versiones modernas de Windows, desde Windows NT hasta las ediciones actuales. Fue 
diseñado específicamente para superar las limitaciones del antiguo sistema FAT32, ofreciendo 
importantes mejoras en capacidad, seguridad y funcionalidad. A diferencia de FAT32, NTFS permite 
trabajar con archivos de más de 4 GB y admite particiones de gran tamaño, con un límite teórico de 
hasta 256 terabytes. 
Ventajas 
Una de las principales ventajas de NTFS es su enfoque en la seguridad y la integridad de los datos. 
Incorpora un sistema avanzado de permisos granulares (ACLs) que permite controlar con precisión el 
acceso a archivos y carpetas, así como funciones de cifrado mediante EFS (Encrypting File System). 
Además, utiliza una técnica llamada journaling, que registra los cambios realizados en el sistema de 
archivos para facilitar la recuperación de datos en caso de fallos o cortes de energía. 
Otras características notables incluyen la compresión nativa de archivos, la capacidad de crear puntos 
de montaje para integrar diferentes unidades de almacenamiento sin necesidad de asignarles letras de 
unidad, y el soporte para enlaces simbólicos. Estas funcionalidades hacen de NTFS una opción ideal para 
entornos profesionales y corporativos donde se requieren altos niveles de seguridad y rendimiento. 

<!-- Page 45 -->

 
 
Periféricos: conectividad y administración 
45 
Limitaciones 
Sin embargo, NTFS presenta limitaciones en cuanto a compatibilidad con otros sistemas operativos. En 
macOS, por ejemplo, solo es posible leer unidades NTFS de forma nativa, mientras que para escribir en 
ellas es necesario instalar software adicional como Paragon NTFS o Tuxera. En sistemas Linux, el 
soporte es más amplio gracias al driver ntfs-3g, que permite tanto lectura como escritura, aunque con 
algunas restricciones en permisos avanzados. Por otro lado, dispositivos como televisores, consolas o 
reproductores multimedia generalmente no son compatibles con NTFS, ya que suelen utilizar sistemas 
más simples como FAT32 o exFAT. 
Alternativa 
Dada esta situación, NTFS resulta especialmente recomendable para discos internos en equipos con 
Windows, donde puede aprovecharse al máximo sus capacidades. No obstante, si se necesita compartir 
datos entre diferentes plataformas, como Windows, macOS y dispositivos externos, la mejor alternativa 
suele ser exFAT, un sistema de archivos moderno que combina buena compatibilidad con la capacidad 
de manejar archivos de gran tamaño. 
 
 
 
 
El experto opina 
NTFS, es el mejor formato para trabajar con discos duros internos 
dónde tengamos instalado el Sistema Operativo Windows, y/o 
como dispositivo de almacenamiento de información. 
 
3.2.4.3. exFAT 
exFAT, siglas de Extended File Allocation Table, tabla extendida de asignación de archivos), también 
conocido como FAT 64, es un sistema de archivos, patentado y privativo de Microsoft, especialmente 
optimizado para memorias flash presentado con Windows CE (Windows Embedded CE 6.0). 
exFAT apareció en 2006 y se introdujo en la mayoría de los sistemas operativos modernos, incluido 
Windows XP. Está pensado para unidades flash, no tiene las características de seguridad de NTFS, pero 
tampoco las limitaciones de FAT32 (4GB por archivo y 8 TB de tamaño máximo de partición). 
Todos los sistemas operativos de PC (Windows, Mac y Linux -aunque en este último es posible que 
tengamos que instalar algunas librerías) son compatibles de forma nativa con exFAT, a diferencia de 
NTFS. 
exFAT es compatible con un gran número de dispositivos tipo televisiones, reproductores multimedia, 
videoconsolas, etc., aunque es tan compatible como FAT32. 
El límite máximo de tamaño de archivo de exFAT es 16EiB (Exbibyte). 

<!-- Page 46 -->

 
 
Periféricos: conectividad y administración 
46 
 
 
 
+ Info 
Ventajas: 
• Mejoras en el rendimiento de la asignación de espacio libre 
(gracias a la introducción de un free space bitmap, 
utilizado para rastrear sectores asignados por algunos 
sistemas de archivo). 
• Soporte para listas de control de acceso. 
• Multiplataforma, tanto Mac OS X como Microsoft Windows 
soportan lectura y escritura de forma nativa. 
 
 
Al igual que NTFS, exFAT puede preasignar espacio en disco para un archivo simplemente marcando el 
espacio arbitrario en el disco como 'asignado'. 
exFAT y el resto de la familia de sistemas de archivos FAT no utiliza índices para nombres de archivos, a 
diferencia de NTFS y ext que utilizan árboles para la búsqueda de archivos. Cuando se accede a un 
archivo, el directorio debe buscarse secuencialmente hasta que se encuentre una coincidencia. 
 
 
 
 
El experto opina 
exFAT, lo recomendamos para unidades externas (USB o SD) 
donde vayamos a guardar archivos de más de 4 GB y que 
queramos que sea compatible con el mayor número de dispositivos 
posibles. 
Si no vamos a guardar archivos de más de 4 GB mejor utilizamos 
FAT32. 
 
 
Para que haya una Interoperabilidad, Microsoft provee medios para convertir particiones FAT32 a 
NTFS, pero no en sentido contrario, (NTFS a FAT32). 

<!-- Page 47 -->

 
 
Periféricos: conectividad y administración 
47 
• Partition Magic de Symantec y el proyecto de código abierto NTFSResize son ambos capaces de 
redimensionar particiones NTFS. 
• Con la herramienta convert incluida en los sistemas NT (Windows NT en adelante), se puede 
cambiar un disco con sistema de ficheros FAT32 a NTFS sin perder ningún dato con la 
instrucción "convert [unidad]:/fs:ntfs". 
• Por razones históricas, absolutamente todas las versiones de Windows que todavía no soportan 
NTFS almacenan internamente la fecha y hora como hora local, y consecuentemente los 
sistemas de ficheros correspondientes a esas versiones de Windows, también tratan la hora 
localmente. 
Sin embargo, Windows NT y sus sucesores almacenan la hora en formato GMT/UTC, y hacen 
las conversiones apropiadas en el momento de mostrar las fechas. De este modo, al copiar 
archivos entre un volumen NTFS y uno no NTFS, deben hacerse las conversiones "al vuelo", lo 
que puede originar ambigüedades si el horario de verano está activo en la copia de unos 
archivos y no en el de otros, pudiendo dar lugar a ficheros cuya marca de hora esté una hora 
desplazada. 
• MacOS X provee soporte de sólo lectura a particiones formateadas como NTFS. 
NTFS-3G es una utilidad de licencia GPL que permite lectura y escritura en particiones NTFS. 
Los desarrolladores de NTFS-3G también proveen una versión comercial y de alto rendimiento 
denominada Tuxera NTFS para Mac. 
 
 
 
 
+ Info 
Sistemas de archivos desarrollados por Apple son: MFS, HSF, HSF+, 
Mac OS Plus, APFS. 
El sistema de archivos diseñado específicamente para el kernel de 
Linux en 1992 se denomina Ext, acrónimo de Extended File 
System. Existen diferentes versiones según la distribución del 
sistema operativo. El sistema original ha sido sustituido por 
versiones posteriores ext2 (1993), ext3 (2001) y final mente el 
que es llamado fourth extended filesystem o "cuarto sistema de 
archivos extendido" ext4 (2008). 
 

<!-- Page 48 -->

 
 
Periféricos: conectividad y administración 
48 
3.3. Discos ópticos 
Un sistema de almacenamiento óptico utiliza un haz láser que explora las variaciones de dos estados de 
reflexión sobre una superficie especial. Existen distintas tecnologías que llevan a cabo estas 
operaciones. 
Los datos, con formato digital, se escriben en discos mediante creación de microsurcos en la superficie 
del disco. La información codificada en los surcos se puede leer detectando, mediante un fotodetector 
incorporado al haz láser, los cambios en la reflexión del elemento de superficie iluminado por el láser. La 
luz se dirige mediante una lente. 
Los principales formatos de los soportes ópticos son los discos compactos (CD), los discos versátiles 
digitales (DVD) y los discos Blu-ray (BD). Las diferencias entre estos formatos son la velocidad de 
transferencia y la capacidad (CD menor y BD mayor). También presentan variaciones en la tecnología 
utilizada para leer y escribir datos. 
Blu-ray se desarrolló para vídeo de alta definición, aunque en la actualidad, su uso más extendido es 
como soporte para los juegos de videoconsolas como PS4 y Xbox One. 
 
 
 
 
+ Info 
El HD DVD de Toshiba era el competidor de Blu-ray, pero este 
proyecto se abandonó. 
 
3.4. Memorias flash 
La memoria flash está basada en semiconductores. Es regrabable y no volátil. Por lo tanto, posee 
muchas de las características de la memoria RAM y tiene la ventaja de que sus datos no se eliminan al 
desenchufarlo. 
Debido a su alta velocidad, durabilidad y bajo consumo de energía, la memoria flash resulta ideal para 
muchos usos, como por ejemplo en cámaras digitales, tablets y teléfonos móviles. 
Al no tener partes móviles, son resistentes a golpes. 
Algunos ordenadores, especialmente los portátiles, incorporan lector para estos dispositivos, y también 
existen lectores externos que se conectan al ordenador mediante puerto USB. 

<!-- Page 49 -->

 
 
Periféricos: conectividad y administración 
49 
Según su formato físico y uso, podemos dividirlas en dos: 
• Pendrive. Son dispositivos pensados para ser usados como discos duros portátiles. Llevan una 
memoria flash en su interior y un conector USB que nos permite conectarlos directamente al 
ordenador. 
• Tarjetas de memoria. Son incompatibles entre sí. Algunos tipos son: 
• SD. Son las más utilizadas. Las tarjetas micro-SD han tenido una gran aceptación 
utilizándose como memoria en la mayoría de los teléfonos (Smartphone). Tienen buena 
relación capacidad-precio. 
• Compact Flash (CF). Era la memoria más común. 
• Multimedia Card (MMC). Son pequeñas, pero poco resistentes. 
• XD. Se emplean en cámaras fotográficas Fuji y Olimpus. 
• Memory Stick. Es de SONY y la utilizan en su consola PSP. 
Smart Media. También conocidas como Solid State Flash Digital Card (SSFDC). Parecidas a las 
tarjetas compact flash, pero más finas. 
4. Sistemas de almacenamiento 
Los sistemas de almacenamiento informático, son elementos, dispositivos, etc., capaces de almacenar 
información. Puesto que almacenan miles de datos con gran valor, una buena gestión de los mismos es 
esencial. 
Se estima que el incremento de la información guardada de año en año, crece entre un 50% y un 100%. 
En una primera división de los tipos de datos, podemos diferenciar estos entre "estructurados" y "no 
estructurados". 
• Estructurados: 
Cuando hablamos de datos estructurados nos referimos a la información que se suele encontrar 
en la mayoría de bases de datos. Son archivos de tipo texto que se suelen mostrar en filas y 
columnas con títulos. Son datos que pueden ser ordenados y procesados fácilmente por todas 
las herramientas de minería de datos. 
• No estructurados: 
Los datos no estructurados, generalmente son datos binarios que no tienen estructura interna 
identificable. Es un conglomerado masivo y desorganizado de varios objetos que no tienen valor 
hasta que se identifican y almacenan de manera organizada (correos, audio, documentos de 
texto, etc.). 

<!-- Page 50 -->

 
 
Periféricos: conectividad y administración 
50 
Gestión de Almacenamiento 
Todos los procesos informáticos generan datos que en muchos casos hay que guardar y garantizar su 
integridad. La "Gestión de almacenamiento" es la infraestructura necesaria para asegurar esta 
información, incluyendo las decisiones necesarias para la optimización de los recursos disponibles. 
A la hora de tomar las medidas adecuadas, debemos tener en cuenta: 
• La capacidad: 
Consiste en proporcionar el suficiente almacenamiento dentro de unos costes razonables. Se 
debe saber planificar no solo la capacidad necesaria actualmente sino tener en cuenta las 
expectativas de crecimiento. 
• El rendimiento: 
A la hora de planificar los sistemas de almacenamiento hay que tener en cuenta varios 
parámetros, por ejemplo: no usaremos los mismos dispositivos para almacenamiento de 
información histórica que para datos de uso inmediato. 
• La fiabilidad: 
El almacenamiento y sus datos deben estar disponibles cuando se necesiten. El sistema tiene 
que ser "tolerante al fallo", es decir, tiene que seguir suministrando la información solicitada, 
aunque alguno de sus componentes esté en "fallo". 
• La recuperabilidad: 
Los datos pueden ser alterados, dañados y borrados resultar inaccesibles. Se deben tener 
mecanismos para poder recuperarlos. Las copias de seguridad o backup pueden ser de los 
siguientes tipos: 
• Copia de seguridad física completa: 
Requieren la parada completa del sistema al cual se le quiera aplicar la copia de seguridad. 
• Copia de seguridad física incremental: 
Requieren la parada completa del sistema al cual se le quiera aplicar la copia de seguridad, 
pero durante un menor lapso de tiempo. 
• Copia de seguridad física online: 
Las bases de datos pueden permanecer abiertas a los usuarios durante el proceso de copia 
de seguridad y la recuperación se puede lograr de nuevo a la última transacción procesada. 
• Copia de seguridad lógica (exportado de archivos): 
Menos complicadas que las anteriores, pero consumen más tiempo. Permiten aplicaciones 
24/7 y las bases de datos pueden permanecer online. 
En este apartado vamos a estudiar distintos sistemas de almacenamiento. 

<!-- Page 51 -->

 
 
Periféricos: conectividad y administración 
51 
4.1. Tipos de almacenamiento: DAS, NAS, SAN 
NAS (Network Attached Storage), SAN (storage area network) y DAS (Direct Attached Storage) son 
tres modos de almacenamiento muy utilizados en la actualidad. 
Si bien el uso de la fibra y del protocolo FC (Fibre Channel) puede ser usado en los tres tipos de 
almacenamiento, es predominante en entornos SAN. 
Vamos a darles un repaso rápido para saber diferenciarlas y para qué debemos utilizar cada una. 
4.1.1. DAS (Direct-Attached Storage) 
Son dispositivos de almacenamiento conectados a las maquinas directamente (por ejemplo, discos 
duros). El almacenamiento es accesible solo desde la computadora o servidor al que está directamente 
conectado. No está disponible para otros dispositivos en la red. 
Un sistema DAS puede usar diversas tecnologías de conexión directa, como SCSI (Small Computer 
System Interface), FC (Fibre Channel), SATA, IDE, USB, y Thunderbolt. 
Tradicionalmente un sistema DAS habilita capacidad extra de almacenamiento a un servidor, mientras 
mantiene alto ancho de banda y tasas de acceso. 
Sin embargo hoy día un DAS se refiere a cualquier dispositivo de almacenamiento, como un disco duro o 
una unidad SSD, que está conectado directamente a una computadora o servidor sin pasar por una red. 
Esto significa que quien tiene un PC en casa tiene un DAS, pues en este caso el DAS haría referencia al 
disco duro o unidad de estado sólido conectado a esa máquina. 
Un típico sistema DAS está hecho de uno o más dispositivos de almacenamiento como discos rígidos, y 
uno o más controladores. 
Este tipo de Almacenamiento tiene los siguientes inconvenientes: 
• Dispersión del Almacenamiento que dificultad la gestión de copias de seguridad. 
• Mantenimiento complejo. 
• Incapacidad para compartir datos o recursos no usados con otros servidores. 

<!-- Page 52 -->

 
 
Periféricos: conectividad y administración 
52 
4.1.2. NAS (Network-Attached Storage) 
 
Fuente: 
(https://commons.wikimedia.org
/wiki/File:Gnome-dev-
network.svg) 
Es una tecnología de almacenamiento dedicada a compartir la capacidad de almacenamiento del 
dispositivo con ordenadores o servidores clientes a través de una red (normalmente TCP/IP). 
Conectado a través de una red local (LAN) mediante un puerto Ethernet. Los dispositivos NAS están 
diseñados para funcionar como un servidor de archivos accesible por varios usuarios en una red. 
La diferencia fundamental de un NAS con un servidor de archivos tradicional es la especialización y 
optimización. Un NAS suele tener un sistema operativo específico con herramientas orientadas al 
almacenamiento y una interfaz de administración de administración sencilla. 
Un servidor de archivos tradicional suele tener un sistema operativo Windows Server, Linux o Unix 
completo, con el que proporcionar múltipes servicios y puede implementar a su vez software para 
compartir almacenamiento y datos. 
Por su parte un sistema NAS está especializado y optimizado para una sola tarea, la gestión de archivos. 
Hace uso de un sistema operativo optimizado para dar acceso con los protocolos CIFS, NFS, FTP o 
TFTP. 
Los principales protocolos que vamos a ver son NFS y SMB. 
4.1.2.1. NFS 
NFS, siglas de Network File System 
Es un protocolo de red del sistema de archivos distribuidos que permite a la unidad NAS compartir 
directorios y archivos a través de una red. Como ocurre con los SMB, NFS da acceso en el nivel de los 
archivos a los usuarios y los programas. 

<!-- Page 53 -->

 
 
Periféricos: conectividad y administración 
53 
NFS tiene una amplia difusión para albergar los almacenes de datos de VMWare o compartir carpetas de 
red en un entorno de Linux/UNIX. 
Cuando se activa el servicio NFS en un recurso compartido, puede acceder a este mediante la ruta 
siguiente: 
[NOMBRE DE NAS o DIRECCIÓN IP]:/shares/SHARE_NAM 
4.1.2.2. SMB 
SMB, siglas de Server Message Block 
Es un protocolo de red cliente-servidor que controla el acceso a archivos y directorios enteros, así como 
a otros recursos de la red, como impresoras, routers o interfaces compartidas con la red. 
El protocolo SMB también sirve como base para el intercambio de información entre los diferentes 
procesos de un sistema. 
Permite al cliente comunicarse con otros participantes de la misma red para acceder a los archivos o 
servicios que se comparten en ella. 
Para que esto ocurra, el otro sistema también debe haber implementado el protocolo de red, para así 
recibir y procesar la solicitud del cliente respectivo utilizando una aplicación de servidor SMB. 
Sin embargo, ambas partes deben primero establecer una conexión, por lo que primero intercambian 
los mensajes con este fin. En las redes IP, SMB utiliza el Transmission Control Protocol (TCP) que 
emplea un triple apretón de manos (three-way handshake) entre cliente y servidor antes de establecer 
una conexión definitiva. 
 
 
 
 
+ Info 
En la implementación del protocolo SMB en Windows NT 4.0, 
Microsoft utilizó el nombre de Common Internet File System 
(CIFS), que a raíz de ello se utilizó inicialmente como sinónimo de 
la familia de protocolos SMB. Hoy en día, CIFS es como se suele 
llamar a la primera versión de SMB (SMB 1.0). 
 

<!-- Page 54 -->

 
 
Periféricos: conectividad y administración 
54 
4.1.3. SAN (Storage Area Network) 
Es un almacenamiento en el que los equipos cliente tienen la capacidad de leer y escribir directamente 
sobre el volumen compartido como si fuera un almacenamiento local. 
Protocolos utilizados en esta tecnología: 
• FC (Fibre Channel). 
• FCoE (Fibre Channel Over Ethernet). 
• iSCSI (Internet Small Computer System Interface -Internet SCSI). 
• NVMeoF (Non-Volatile Memory Express Over Fabrics). 
4.1.3.1. FC (Fibre Channel) 
Tiene las siguientes características: 
• Aporta mucha menor latencia y un mayor ancho de banda. 
• Se alcanzan velocidades de hasta 8 y 16 Gbit/s. (finales del 2020). 
• Se puede utilizar tanto con Fibra Óptica como con pares de cobre. 
• Tenemos tres topologías principales: 
• Punto a Punto: 
La topología punto a punto describe la conexión directa entre dos dipositivos, que, de no 
ser exclusiva, esto es dedicada, puede compartir la conexión con otros dispositivos de red. 
Anillo: 
Todos los dispositivos están en un bucle o anillo, similar a una red token ring. El añadir o 
quitar un elemento del anillo hace que se interrumpa la actividad en el mismo. El fallo de un 
dispositivo hace que se interrumpa el anillo. 
• Conmutada: 
Todos los dispositivos se conectan a conmutadores (switches) de Fibre Channel, 
conceptualmente similares a las modernas implementaciones Ethernet. Los conmutadores 
controlan el estado del medio físico, proporcionando interconexiones optimizadas. 
4.1.3.2. FCoE 
Se desarrolló como una forma alternativa de Fibre Channel llamada Fibre Channel sobre Ethernet (Fibre 
Channel over Ethernet). 
Su utilidad es reducir el costo de las soluciones de FC al eliminar la necesidad de comprar HBA 
(adaptador de bus de host). 

<!-- Page 55 -->

 
 
Periféricos: conectividad y administración 
55 
 
 
 
+ Info 
HBA es un componente que se conecta al bus (el PCIe) en el 
huésped. 
La descripción del trabajo de este componente es para conectar el 
anfitrión de una pieza externa de hardware, por lo general una 
SAN, a través de un switch o cualquier otro tipo de 
almacenamiento. 
 
4.1.3.3. iSCSI 
iSCSI es una extensión de SCSI, que es un protocolo para comunicación de dispositivos. 
SCSI suele usarse en dispositivos conectados físicamente a un host o servidor, tales como discos duros, 
lectoras de CD's o dispositivos de cinta. 
En iSCSI, los comandos SCSI que manejan el dispositivo, se envían a través de la red, de forma que en 
vez de tener un disco SCSI conectado físicamente a nuestro equipo, lo conectamos por medio de la red. 
iCSSI es bastante más económico que Fibre Channel. 
iSCSI no es multiconexión, es decir, dos equipos no pueden utilizar el mismo dispositivo ISCSI. 
4.1.3.4. NVMeoF 
NVMeoF: Non-Volatile Memory Express over Fabrics. 
Está diseñada para ofrecer la tecnología de alta velocidad y baja latencia de NVMe SSD por medio de 
una trama de red. Actualmente se encuentran disponibles tres implementaciones básicas de trama 
NVMe: 
• NVMe over Fibre Channel. 
• NVMe por medio de acceso remoto a la memoria directa. 
• NVMe over TCP. 

<!-- Page 56 -->

 
 
Periféricos: conectividad y administración 
56 
Es una forma de ejecutar el protocolo NVMe sobre una trama de "switches". 
 
 
 
+ Info 
NVMe (memoria no volátil rápida) es un protocolo de transporte y 
acceso al almacenamiento para unidades flash y de estado sólido 
(SSD) de última generación que ofrece el rendimiento más alto y 
los tiempos de respuesta más breves para todos los tipos de cargas 
de trabajo empresariales. 
 
4.2. Familias de controladoras 
Vamos a estudiar diferentes tipos de controladoras: 
• RAID. 
• SCSI. 
• SATA. 
4.2.1. RAID 
 
 
 
+ Info 
Este punto es muy importante, imprescindible para la seguridad de 
la información. 
Lo explicamos de un modo sencillo y gráfico para que te resulte 
más fácil comprenderlo y memorizarlo. 
También dispones de clases en Temario Audiovisual. ¡Ánimo! 
 
 

<!-- Page 57 -->

 
 
Periféricos: conectividad y administración 
57 
Hoy en día la información es el activo más importante de las empresas. Un fallo en un disco duro 
acarrea una pérdida de información y un tiempo en el que el sistema no está en explotación. 
RAID (Redundant Array of Independent Disks, aunque en principio se denominó Redundant Array of 
Inexpensive Disks) es un sistema de almacenamiento de datos en el que se utilizan dos o más discos 
para constituir una única unidad lógica (es decir, que el sistema operativo, y por lo tanto el usuario, ven 
como una sola unidad). 
En RAID se buscan dos objetivos: 
• Proteger el sistema ante fallos (mediante redundancia de datos). 
• Mejorar el rendimiento (accediendo a 2 o más discos al mismo tiempo). 
Existen distintas configuraciones de RAID o niveles de RAID. Cada uno proporciona distintas mejoras en 
la seguridad y/o rendimiento, sacrificando parte del almacenamiento. 
Te vamos a mostrar los niveles RAID estándar y algunos de los niveles RAID anidados. Omitiremos los 
RAID propietarios. 
Los niveles que vamos a ver son: 
• RAID de un solo nivel: 
• RAID 0 o fraccionamiento. 
• RAID 1 o espejo. 
• RAID 2. 
• RAID 3. 
• RAID 4. 
• RAID 5. 
• RAID 6. 
• RAID 5E y 6E. 
• RAID multinivel: 
• RAID 0 + 1. 
• RAID 1 + 0. 
• RAID 30. 
• RAID 50. 
• RAID 100. 
• RAID 101. 

<!-- Page 58 -->

 
 
Periféricos: conectividad y administración 
58 
4.2.1.1. Sistemas RAID un solo nivel 
RAID 0 (o nivel 0) 
También denominado striping o fragmentación. Los datos se desglosan en pequeños segmentos 
(denominados stripe o chunk) y se distribuyen entre varias unidades. 
 
Fragmentación de datos en dos discos 
Características: 
• Los discos están conectados en paralelo, permitiendo una transferencia simultánea de datos a 
todos ellos, lo cual implica una mayor velocidad en las operaciones de lectura y escritura. 
• No hay redundancia de datos, por lo que no estamos mejorando la tolerancia a fallos. Al 
contrario, la probabilidad de un fallo será mayor, ya que, para que el sistema falle, basta con que 
falle uno de los discos. Por lo tanto, a mayor cantidad de discos, mayor probabilidad de fallo. 
• No se pierde capacidad, salvo que se utilice con discos de distintos tamaños, en cuyo caso se 
aprovechará de cada uno un tamaño equivalente al tamaño del disco más pequeño. 
• Se necesita un mínimo de dos discos. 
• La capacidad de un sistema RAID 0 = NxS, donde N es el número total de unidades en la matriz y 
S es la capacidad de la unidad más pequeña de la matriz. 
 

<!-- Page 59 -->

 
 
Periféricos: conectividad y administración 
59 
 
 
 
+ Info 
Seguramente te estés preguntando por qué es un nivel RAID 
(array redundante de discos independientes) si no es redundante. 
Al principio no formaba parte de los niveles que se definieron 
(fueron del 1 al 5), pero el grupo de científicos que lo hizo pensó 
que era una forma interesante de incrementar el índice de 
transmisión del sistema y lo añadieron como RAID 0. 
 
Nivel 1 o RAID 1 
También denominado disk mirroring o en espejo. Se basa en la utilización de discos adicionales sobre 
los que se realiza una copia síncrona de los datos que se están modificando. 
Un RAID 1 crea una copia exacta (o espejo) de un conjunto de datos en dos o más discos, por ello su 
capacidad es equivalente a la del tamaño de almacenamiento de su disco más pequeño. 
La característica distintiva de un RAID 1 es la escritura simultánea en todos los discos. Esto significa que 
cuando se guardan datos, se escriben en todos los discos del conjunto de manera prácticamente 
instantánea. No existe un orden de prioridad o un disco "principal" que reciba los datos primero. 
Si bien al principio de RAID 1, cada disco podía tener su controladora, hoy día controladores RAID 
modernos, bien sea de hardware o de software, pueden gestionar múltiples discos distribuyendo la 
carga de trabajo de manera eficiente, incluso si los discos comparten la misma controladora. 
 
Copia síncrona de datos en dos discos 

<!-- Page 60 -->

 
 
Periféricos: conectividad y administración 
60 
Características: 
• Obtiene integridad de la información a cambio de una gran cantidad espacio. 
• La máxima capacidad de los discos viene determinada por el de menor tamaño, 
desperdiciándose el resto (en caso de que sean de distinto tamaño). 
• Se mejora el tiempo de lectura (se puede leer de varios discos a la vez), pero la escritura será 
más lenta pues si bien no deja de ser paralela, los protocolos de comunicación, la gestión de 
coherencia y verificación de datos pueden aumentar la latencia. 
• Para perder información tendrían que romperse todos los discos. 
• La capacidad de un sistema RAID 1 = S, donde S es la capacidad de la unidad más pequeña de la 
matriz. 
RAID 2 
Este nivel está obsoleto y no tiene aplicaciones comerciales. 
Distribuye los datos a nivel de bit y utiliza el código ECC para la corrección de errores. 
 
 
 
+ Info 
El código ECC o código Hamming es un código de detección y 
corrección de errores. Puede detectar fallos de hasta 2 bits y 
corregir fallos de 1 bit. 
 
 
Se crean dos grupos. En el primero se distribuye la información y en el segundo se guardan los códigos 
de corrección de errores. 
Para perder información debe fallar un disco de datos y el que contiene su código de corrección de 
errores. 

<!-- Page 61 -->

 
 
Periféricos: conectividad y administración 
61 
 
Diagrama de configuración RAID 2 de 7 discos 
RAID 3 
 
 
 
Atención 
Este nivel prácticamente ha dejado de utilizarse. 
 
 
Para entender este sistema de RAID 3, hay que conocer el concepto de PARIDAD: 
• Un bit de paridad es un dígito binario, que indica si el número de bits, con un valor de 1 en un 
conjunto de bits, es par o impar. 
Los bits de paridad conforman el método de detección de errores más simple. 
La idea básica es contar el nº de unos (1) que hay. 
• En el caso de la PARIDAD PAR: 
» Si el conteo de bits con valor 1 es impar, el bit de paridad se establece con valor 1, y así 
el valor de la suma ya es par. 
Ejemplo: 
1001001( ) hay 3 unos, por lo que es un valor impar, para cumplir la paridad PAR, 
debemos añadir otro uno 1001001(1), ahora hay 4 unos y se cumple la paridad par. 

<!-- Page 62 -->

 
 
Periféricos: conectividad y administración 
62 
» Si el conteo de bits con valor 1 es par, entonces el bit de paridad (par) se deja en 0, 
pues ya es par. 
Ejemplo: 
1000001( ) hay 2 unos, por lo que es un valor par, para cumplir la paridad PAR, no 
necesitamos añadir otro 1, ponemos un cero 1000001(0) y como sigue habiendo 2 
unos, se cumple la paridad par. 
• En el caso de la PARIDAD IMPAR: 
La situación es la contraria, por tanto: 
» Si el conteo de bits con valor 1 es impar, entonces ya se cumple la PARIDAD IMPAR y 
no es necesario añadir ningún 1 más, por lo que se pone el bit de paridad con valor 0. 
Ejemplo: 
1001001( ) hay 3 unos, por lo que es un valor impar, por lo que ya se cumple la paridad 
impar, no necesitamos añadir otro uno, ponemos un cero 1001001(0) y como hay 3 
unos, se cumple la paridad impar. 
» Si el conteo de bits con valor 1 es par, entonces no se cumple la PARIDAD IMPAR, por 
lo que el bit de paridad (impar) se pone con valor 1, haciendo impar la cuenta total de 
bits unos (cumpliéndose que sea impar la suma de los bits con valor 1). 
Ejemplo: 
1000001( ) hay 2 unos, por lo que es un valor par, para cumplir la paridad IMPAR, 
necesitamos añadir otro uno, 1000001(1), así ahora hay 3 unos y ya se cumple la 
paridad impar. 
RAID 3, Distribuye los datos a nivel de byte entre los discos y se añade un disco de paridad que 
contendrá los códigos de recuperación. Necesita un mínimo de tres discos (dos para fragmentación 
y uno para paridad). 
Esta configuración ya no se utilizada actualmente, consiste en dividir los datos a nivel de byte en las 
distintas unidades que forma el RAID excepto en una, que es donde se almacena información de paridad 
para poder unir estos datos al ser leídos. Con este método cada byte almacenado tiene un bit extra de 
paridad para identificar errores. 

<!-- Page 63 -->

 
 
Periféricos: conectividad y administración 
63 
 
Diagrama de configuración RAID 3 de 4 discos 
RAID 4 
Es igual que el anterior, solo que distribuye los datos a nivel de bloque en lugar de a nivel de byte, es 
decir, los datos se distribuyen a nivel de bloque entre los discos y se añade un disco de paridad. 
La diferencia fundamental respecto a RAID 3 es que, si perdemos una unidad, los datos pueden ser 
reconstruidos en tiempo real gracias a los bits de paridad calculados. 
 
Diagrama de configuración RAID 4 de 4 discos 

<!-- Page 64 -->

 
 
Periféricos: conectividad y administración 
64 
Características: 
• Para perder información deben fallar dos discos. 
• El rendimiento para leer es bueno, pero no en la escritura, ya que en todas las peticiones 
debemos acceder al disco de paridad. Por esta razón, este nivel no se usa prácticamente y ha 
sido sustituido por el nivel 5. 
RAID 5 
También llamado sistema distribuido con paridad, se sigue utilizando en la actualidad. 
A diferencia del nivel 4, la información de paridad no se distribuye en un solo disco. 
En este caso la información es almacenada de forma dividida en bloques que se reparten entre los discos 
duros que formen el RAID, y además se genera un bloque de paridad para asegurar de esta forma la 
redundancia y poder reconstruir la información en caso de que un disco duro se corrompa. 
Este bloque de paridad se almacenará en una unidad distinta a los bloques de datos que están 
implicados en el bloque calculado, así, de esta forma la información de paridad estará almacenada en un 
disco distinto a donde están los bloques de datos implicados, por lo que se permite la reconstrucción de 
la información. 
Existe una variante RAID 5E en donde se introduce un disco duro de reserva para minimizar el 
tiempo de reconstrucción de datos, si uno de los principales falla. 
 
Diagrama de configuración RAID 5 de 4 discos 

<!-- Page 65 -->

 
 
Periféricos: conectividad y administración 
65 
Características: 
• Se necesitan al menos tres unidades de almacenamiento para asegurad la redundancia de datos 
con paridad. 
En dos se distribuye un determinado dato y en el tercero se añade la información de paridad). 
• Se tolera únicamente que falle una unidad, ya que si fallan dos perderemos la información de 
paridad, y al menos uno de los bloques de datos implicados. 
Para perder la información deben fallar dos discos de forma simultánea, ya que la información 
de paridad contenida en un disco no corresponde a los datos de este disco y, por lo tanto, al 
romperse el disco, la información de paridad de los datos de este disco está distribuida en el 
resto (no están en el disco roto). 
• Desperdicia poco espacio de almacenamiento. 
• Tiene un buen rendimiento de lectura y escritura, ya que hace participar a todos los discos en 
cada operación. 
• El cálculo de la paridad añade una sobrecarga a la escritura de datos. 
Veamos cómo calcular el almacenamiento en un RAID 5: 
La tecnología RAID 5 (matriz redundante de discos independientes) proporciona tolerancia a fallos para 
un grupo (o matriz) de discos duros, permitiendo a la matriz soportar que falle un disco duro sin perder 
datos. 
La cantidad real de almacenamiento disponible en una matriz RAID 5 no es igual a la suma de todas las 
unidades de la matriz. 
Se necesitan como mínimo 3 discos (se puede romper un disco sin perder los datos). 
La capacidad utilizable de una matriz RAID 5 es (N-1) x S (min), donde N es el número total de 
unidades en la matriz y S (min) es la capacidad de la unidad más pequeña de la matriz. 
Si utilizamos 6 discos de 500 GB=0,5 TB tendremos: 6 discos – 1 = 5 discos -> 5x0,5 = 2,5 TB 
disponibles. 
RAID 6 
Igual que el RAID 5, pero utilizando doble paridad. Por lo tanto, necesita dos discos adicionales para la 
paridad en vez de uno. La paridad se sigue distribuyendo entre los discos. 

<!-- Page 66 -->

 
 
Periféricos: conectividad y administración 
66 
 
Diagrama de configuración RAID 6 de 5 discos 
Características: 
• Debe tener un mínimo de cuatro discos (dos para distribuir datos y dos para paridad). 
• Para perder la información deben fallar tres discos, ya que la doble paridad permite recuperar 
dos bits. 
• Se desperdicia espacio. 
• El cálculo de la doble paridad añade una sobrecarga importante. 
• La capacidad de un sistema RAID 6 = (N-2) x S, donde N es el número total de unidades en la 
matriz y S es la capacidad de la unidad más pequeña. 
RAID 5E y 6E 
Se puede decir que el RAID 5E y RAID 6E coinciden en el término 'Enhanced (mejorado)'. 
Las mejoras consisten en la gestión física y lógica de la reconstrucción ante el fallo de un disco, pueden 
abordarse de dos maneras distintas. 
• En el sistema Hot Spare, una unidad de almacenamiento permanece en espera hasta que falla 
una unidad del array, momento en el cual la controladora la utiliza para reemplazarla 
automáticamente. Durante la reconstrucción, los datos del disco dañado se recuperan ya sea 
mediante la información de paridad o a partir de la copia espejo, según el nivel de RAID 
configurado. 

<!-- Page 67 -->

 
 
Periféricos: conectividad y administración 
67 
• El sistema Distributed Spare no utiliza un disco físico de repuesto. En su lugar, crea espacios 
reservados distribuidos entre todos los discos sanos del array, que funcionan colectivamente 
como un 'disco virtual de emergencia'. Cuando ocurre un fallo, estos espacios almacenan 
temporalmente los datos reconstruidos (utilizando la información de paridad de los discos 
restantes). Posteriormente, al insertar un nuevo disco físico, los datos se vuelcan desde estos 
espacios distribuidos a la nueva unidad, liberando así la capacidad reservada y restaurando la 
configuración original del array. 
4.2.1.2. Sistemas RAID multinivel 
RAID 0+1 
Es un espejo de divisiones. Primero hacemos un RAID 0 con dos discos y, a continuación, lo duplicamos 
(RAID 1) en los otros dos discos (que también estarán en RAID 0). 
Seguro que lo ves más claro en la siguiente imagen: 
 
Diagrama de configuración RAID 0+1 de cuatro discos 
Características: 
• Es menos robusto que el RAID 1 + 0, ya que no pueden ocurrir dos fallos simultáneos de disco 
salvo que sean en la misma división. 
• Necesita al menos cuatro discos. 

<!-- Page 68 -->

 
 
Periféricos: conectividad y administración 
68 
RAID 1 + 0 
Es una división de espejos. Similar al anterior, salvo que primero hacemos dos conjuntos RAID 1 con dos 
o más discos cada grupo y, a continuación, segmentamos los datos entre los dos grupos. 
 
Diagrama de configuración RAID 1 + 0 de cuatro discos CAMBIAR 
RAID 30 
Primero se crean dos sistemas RAID 3, que se unen en un sistema RAID 0. 
El RAID 30 trocea los datos en bloques más pequeños y los divide en cada conjunto RAID 3, que a su vez 
lo divide en trozos aún menores, calcula la paridad aplicando un XOR a cada uno y los escriben en todos 
los discos del conjunto salvo en uno, donde se almacena la información de paridad. 
El RAID 30 permite que falle un disco de cada conjunto RAID 3. 
Proporciona tasas de transferencia elevadas combinadas con una alta fiabilidad a cambio de un coste de 
implementación muy alto. 
RAID 50 
Se trata de un nivel principal en RAID 0 que divide los datos de los subniveles configurados como RAID 
5, con sus respectivos tres discos duros. 
En cada bloque RAID 5 tendremos una serie de datos con su correspondiente paridad. En este caso, un 
disco duro puede fallar en cada RAID 5, y nos asegurará la integridad de los datos, pero si fallan más, 
perderemos los datos que haya ahí almacenados. 
Se consigue mayor redundancia, fiabilidad y velocidad. 

<!-- Page 69 -->

 
 
Periféricos: conectividad y administración 
69 
RAID 100 
En lugar de tener un árbol de dos niveles, lo tenemos de tres. 
En el caso del RAID 100 o 1+0+0, el sistema consiste en dos subniveles de RAID 1+0 divididos a su vez 
por un nivel principal también en RAID 0. 
Su velocidad de acceso y redundancia son muy buenos, y ofrecen buena tolerancia a fallos. 
Todos los discos menos uno, podrían fallar en cada RAID 1 sin perder datos. 
La cantidad de disco a utilizar es considerable frente a la disponibilidad de espacio. 
Puede ser la mejor elección para bases de datos muy grandes, donde el software limita la cantidad de 
discos físicos permitidos en cada conjunto estándar. 
RAID 101 
Es un sistema de tres niveles. 
Consiste en dos subniveles de RAID 1+0 divididos a su vez por un nivel principal también en RAID 1. 
Su velocidad de acceso y redundancia son muy buenos, y ofrecen buena tolerancia a fallos. 
Pueden fallar todos los discos de un subnivel 10 y algún otro de los RAID 1 SIN PERDER DATOS. 
La cantidad de discos a utilizar es TREMENDA frente a la disponibilidad de espacio. 
Es un sistema de alta disponibilidad por red, Se utiliza en la llamada Network RAID que aceptan algunas 
cabinas de datos. 
Las mejores aplicaciones para Network RAID-10+1 son aquellas que requieren disponibilidad de datos 
incluso si dos sistemas de almacenamiento en un clúster dejan de estar disponibles. 
4.2.2. SCSI (interfaz de sistema de ordenador pequeño) 
El término se refiere a los cables y puertos utilizados para conectar ciertos tipos de discos duros, 
unidades ópticas, escáneres y otros dispositivos periféricos a una computadora. 
SCSI es popular en estaciones de trabajo de alto rendimiento y servidores. Los sistemas RAID en 
servidores casi siempre usan discos duros SCSI, aunque varios fabricantes ofrecen sistemas RAID 
basados en SATA como una opción de menor coste. 
Características de SCSI: 
• Utilizan CCS (Command Common Set): 
Es un conjunto de comandos para acceder a los dispositivos que los hacen más o menos 
compatibles. 

<!-- Page 70 -->

 
 
Periféricos: conectividad y administración 
70 
• Hacen falta terminadores (jumperes o terminales físicos) en el inicio y fin de la cadena. 
• Número máximo de dispositivos: la controladora cuenta como un dispositivo (identificador 7, 15). 
• Bus: 
Puede ser de 8 bits o de 16 bits: 
• Bus de 8 bits; 7 dispositivos: identificados del 0 al 6; conector de 50 pines. 
• Bus de 16 bits: 15 dispositivos: identificados del 0 al 14; conector de 68 pines. 
• SCSI 1, SCSI 2 y SCSI 3.1 (SPI) conectan los dispositivos en paralelo. 
• SCSI 3.2 (FireWire), SCSI 3.3 (SSA) y SCSI 3.4 (FC-AL) conectan los dispositivos en serie. 
Tipos de SCSI 
Existen 3 generaciones de SCSI: 
• SCSI 1: 
Las características de SCSI 1 son: 
• Bus de 8 bits. 
• Velocidad de transmisión de datos a 5 MB/s. 
• Su conector genérico es de 50 pines (conector Centronics) y baja densidad. 
• La longitud máxima del cable es de seis metros. 
• Permite hasta 8 dispositivos (incluida la controladora), identificados por las direcciones 0 a 7. 
• SCSI 2: 
Hay dos tipos de SCSI 2: 
• Fast: 
» Con un bus de 8. 
» Dobla la velocidad de transmisión (de 5 MB/s a 10 MB/s). 
» Su conector genérico es de 50 pines y alta densidad. 
» La longitud máxima del cable es de tres metros. 
» Permite hasta 8 dispositivos (incluida la controladora), identificados por las 
direcciones 0 a 7. 

<!-- Page 71 -->

 
 
Periféricos: conectividad y administración 
71 
• Wide: 
» Dobla el bus (pasa de 8 a 16 bits). 
» Su conector genérico es de 68 pines y alta densidad. 
» La longitud máxima del cable es de tres metros. 
» Permite hasta 16 dispositivos (incluida la controladora), identificados por las 
direcciones 0 a 15. 
• SCSI 3 SPI: 
En la tercera generación de SCSI, aparecen las interfaces de conexión serie, como SSA, FC-AL y 
FireWire, pero continúan coexistiendo con las interfaces SCSI paralelas. Para diferenciar las 
interfaces serie de las paralelas, se introdujo el término SPI (SCSI Parallel Interface), que se 
refiere específicamente a las interfaces de conexión paralela. 
Dentro de las conexiones paralelas de tercera generación SCSI-3 SPI, se identifican varias 
versiones con diferentes velocidades de transferencia y características: 
• Ultra: con una velocidad de hasta 20 MB/s, utilizaba conectores de 50 o 68 pines y tenía una 
longitud máxima de cable de alrededor de 1.5 metros. También se conoce como Fast-20. 
• Ultra Wide: Ofrecía una velocidad de hasta 40 MB/s, utilizando conectores de 68 pines y 
manteniendo una longitud máxima de cable similar. También se conoce como Wide SCSI-3. 
• Ultra 2: alcanzaba velocidades de hasta 80 MB/s, también con conectores de 68 pines pero 
permitiendo una longitud de cable de hasta 12 metros.También se conoce como Fast 40. 
• Ultra320: con velocidad de hasta 320 MBps, conectores de 68 pines y alta densidad. La 
longitud máxima del cable es de 12 metros. 
• Ultra640: con velocidad de hasta 640 MBps, conectores de 68 pines y alta densidad. La 
longitud máxima del cable es de 12 metros. 
Todas estas versiones utilizaban la interfaz SCSI paralela, que fue ampliamente utilizada en 
sistemas informáticos durante muchos años. Sin embargo, debido a sus limitaciones en 
cuanto a velocidad y escalabilidad, ha sido reemplazada por tecnologías más modernas 
como SATA y SAS. 
Las principales diferencias radican en la forma en que se transmiten los datos, las 
velocidades alcanzables, las distancias y las topologías de conexión. 

<!-- Page 72 -->

 
 
Periféricos: conectividad y administración 
72 
• SCSI 3 Interfaces Serie: 
La decisión de conservar la denominación SCSI en tecnologías seriales como FireWire (SCSI 
3.2), SSA (SCSI 3.3) y FC-AL (SCSI 3.4) fue una estrategia que combinó la necesidad de 
mantener la compatibilidad, aprovechar la reputación de un estándar establecido y facilitar la 
transición hacia nuevas tecnologías. 
• FireWire (IEEE 1394). 
Es un estándar de conexión para la transferencia de datos a alta velocidad, utilizado 
principalmente en cámaras digitales, discos duros externos y otros dispositivos de 
almacenamiento. 
• SSA (Serial Storage Architecture), de IBM. 
Usa full-dúplex con canales separados. 
• FC-AL (Fibre Channel Arbitrated Loop). 
Usa cables de fibra óptica (hasta 10 km) o coaxial (hasta 24 m). Con una velocidad máxima 
de 100 MBps. 
4.2.3. SATA 
El conector SATA es actualmente la interfaz estándar para la conexión de discos duros. 
La interfaz o conector SATA es la evolución de la antigua interfaz IDE (Integrated Drive Electronics), 
también llamada PATA o Parallel Advanced Technologies Attachment. 
SATA es una interfaz de transferencia de datos entre un dispositivo de almacenamiento o lector de 
CD/DVD y la placa base de un ordenador. 
SATA proporciona mayores velocidades que las antiguas interfaces y asegura una mejor optimización 
del flujo de datos debido principalmente a que existe un cable exclusivamente dedicado a cada unidad a 
él conectado. 
Además proporciona otras ventanas como las siguientes: 
• Soporta mayores longitudes del cable, y además son mucho más pequeños. 
• Cuenta con la capacidad de conexión en caliente, tal y como ocurre con los puertos USB. 
• Es una interfaz estandarizada y que soportan todas las placas base del mercado. 
SATA ha ido evolucionando en diferentes versiones, que son: 
• SATA 1.0: 
Esta fue la primera versión que trabajaba a 1,5Gb/s de aquí la denominación de SATA 1,5 Gb/s. 
Con esta conexión podíamos alcanzar una velocidad real de 150 MB/s. 

<!-- Page 73 -->

 
 
Periféricos: conectividad y administración 
73 
• SATA 2.0: 
En esta segunda versión velocidad se duplicó, alcanzando los 3Gb/s y una velocidad de 
300MB/s. 
También se conoce como SATA 3Gb/s. 
• SATA 3.0: 
Este es el estándar actualmente que implementan todos los discos duros con esta interfaz. 
En este caso velocidad de transmisión es de 6Gb/s que resultan de una velocidad máxima de 
600 MB/s. se conoce como SATA 6Gb/s. 
La razón de esta merma de eficiencia en SATA 3.0 es debida a que de cada 8bits transmitidos 2 
se usan para la codificación, es codificación 8b/10b. 
Así pues, a los 750MB resultantes de la conversión de Gb a MB le restaremos un 20%, 
obteniendo la velocidad de 600MB/s mencionada. 
Conectores SATA 
SATA es una tecnología de conexión punto a punto, es decir, tendremos una conexión física entre dos 
dispositivos de forma directa y sin interferencias con otros dispositivos conectados, como ocurría en el 
caso de los conectores IDE en los que era necesario configurar un dispositivo como maestro y otro 
como esclavo para que la conexión fuera posible. 
Todos los dispositivos SATA usan la misma interfaz física de conexión. 
4.2.3.1. Conector sata de datos 
El conector tiene una anchura de 8 mm y en un extremo dispone de una terminación a 90 grados para 
identificar la posición correcta del conector macho y hembra. Este conector puede tener una longitud 
máxima de 1 m, frente al máximo de 45 cm que tenía los cables IDE. 
La función de los pines, empezando por los más alejados de la terminación a 90º: 
• Tierra. 
• A+ (transmisión). 
• A- (transmisión). 
• Tierra. 
• B+ (recepción). 
• B- (recepción). 
• Tierra. 

<!-- Page 74 -->

 
 
Periféricos: conectividad y administración 
74 
4.2.3.2. Conector SATA de alimentación 
Conector de 15 pines, solo le entran cinco cables, en este caso dos cables negros, uno amarillo, uno 
naranja y otro rojo. 
La función de los pines, empezando por los más cercanos de la terminación a 90º: 
• Naranja - Tensión (3,3V). 
• Naranja - Tensión (3,3V). 
• Naranja - Tensión (3,3V) Pre-carga. 
• Negro - Tierra. 
• Negro - Tierra. 
• Negro – Tierra. 
• Rojo - Tensión (5V) Pre-carga. 
• Rojo - Tensión (5V). 
• Rojo - Tensión (5V). 
• Negro – Tierra. 
• Negro – Tierra. 
• Negro – Tierra. 
• Amarillo - Tensión (12V) Pre-carga. 
• Amarillo - Tensión (12V). 
• Amarillo - Tensión (12V). 
4.2.3.3. SATA externo o Esata 
Es un conector destinado a unidades de almacenamiento externas que no trabajan mediante interfaz 
USB. Si bien esta interfaz no está demasiado utilizada, ya que la velocidad de transmisión es de 115 
MB/s muy inferior a las prestaciones de un USB 3.0. 
En cuanto a ventajas encontramos por ejemplo que las unidades no necesitarán la conversión entre 
SATA y USB y que cuenta con capacidad para discos RAID. 

<!-- Page 75 -->

 
 
Periféricos: conectividad y administración 
75 
4.2.3.4. Conector Mini SATA o mSATA 
Este conector utiliza una interfaz similar a la Mini-PCI pero no son conectores equivalentes ni pueden 
ser intercambiables. 
Esta interfaz tiene las mismas prestaciones que un SATA normal y está destinado a discos duros de 1,8 
pulgadas o SSD. 
4.2.3.5. Conector SATA Express 
Esta interfaz es una evolución de SATA capaz de trabajar tanto con discos duros SATA como con 
unidades PCI-Express. Cuenta con una interfaz propia y es capaz de alcanzar los 16 Gb/s o lo que es lo 
mismo, 1,97 GB/s. 
4.3. Gestión de volúmenes 
Un administrador de volúmenes permite agrupar dispositivos físicos (como discos o particiones) para 
obtener un volumen virtual que a ojos del SO será un solo dispositivo. 
En el almacenamiento informático, la gestión de volúmenes lógicos o LVM proporciona un método de 
asignación de espacio en dispositivos de almacenamiento masivo que es más flexible que los esquemas 
de partición convencionales para almacenar volúmenes. 
En particular, un gestor de volúmenes puede concatenar una "banda de datos" o de otro modo 
combinar particiones (o dispositivos de bloque en general) en particiones virtuales más grandes que los 
administradores pueden cambiar el tamaño o mover, potencialmente sin interrumpir el uso del sistema. 
La administración de volúmenes representa solo una de las muchas formas de virtualización de 
almacenamiento; su implementación tiene lugar en una capa en la pila de controladores de dispositivo 
de un sistema operativo (a diferencia de dentro de los dispositivos de almacenamiento o una red). 
 
 
 
 
+ Info 
En el almacenamiento de datos informáticos, la creación de bandas 
de datos es la técnica de segmentar datos secuenciales de forma 
lógica, como un archivo, de modo que los segmentos consecutivos 
se almacenen en diferentes dispositivos físicos de almacenamiento. 
 
 

<!-- Page 76 -->

 
 
Periféricos: conectividad y administración 
76 
Algunas posibilidades para la gestión de volúmenes son: 
Tipo 
Comentario 
RAID 
Permite unir varios dispositivos físicos en un volumen lógico 
Sus usos habituales son: lograr tolerancia a fallos y/o mejorar el rendimiento 
Está disponible en soluciones hardware o software para multitud de SOs 
LVM 
Administrador de volúmenes lógicos 
Permite crear dinámicamente volúmenes lógicos compuestos por diferentes dispositivos físicos, estos 
volúmenes lógicos pueden variar su tamaño mientras están en uso 
Disponible en varios SOs, entre ellos GNU/Linux 
EVMS 
Proporciona un mecanismo unificado para gestionar todas las opciones de almacenamiento en 
GNU/Linux 
ZFS 
El sistema de ficheros ZFS incorpora la administración de volúmenes 
Btrfs 
El sistema de ficheros Btrfs incorpora la administración de volúmenes 
5. Hardware de impresión 
Las impresoras son periféricos que escriben o dibujan la información de salida sobre el papel. 
Antiguamente, la conexión con el ordenador se hacía por el puerto paralelo. 
En la actualidad las impresoras se conectan a puerto USB. 
Aunque la tendencia es que las impresoras puedan conectarse directamente a la red (por cable RJ-45 o 
por wifi) para que sea accesible desde todos los dispositivos de la red (ordenadores, móviles, etcétera). 
Casi todas las impresoras contienen una memoria que actúa como buffer. 
En el buffer se almacena lo que hay que imprimir para que el ordenador quede liberado mientras la 
impresora realiza el trabajo de impresión. 
Cuando queremos comprar una impresora, dos de los factores a tener en cuenta son la memoria y la 
velocidad. 

<!-- Page 77 -->

 
 
Periféricos: conectividad y administración 
77 
5.1. Partes de la impresoras 
Las impresoras tienen dos partes: 
• Parte mecánica. Accionan los elementos que producen la impresión y se encarga de la 
alimentación y arrastre del papel. 
• Parte electrónica. Se encarga de convertir las señales procedentes del PC en estímulos 
eléctricos que producirán la impresión sobre el papel de las partes mecánicas. 
5.2. Clasificación 
Existen diversas formas de clasificar las impresoras. Algunas de ellas son: 
5.2.1. Según el mecanismo de impresión 
• De impacto. El mecanismo roza o golpea el papel. 
• Sin impacto. No existe contacto entre el cabezal de impresión y el papel. 
5.2.2. Según la forma de imprimir los caracteres 
• Impresoras de caracteres. 
• Impresoras de líneas. 
• Impresoras de páginas. 
5.2.3. Según la tecnología utilizada 
• De impacto. El mecanismo de impresión tiene contacto con el papel. Existen dos tipos: 
• De margarita. 
• Matriciales. 
• De tinta. Son económicas y dan buena calidad. Podemos distinguir 2 tipos: 
• De inyección de tinta. 
• De burbuja. 

<!-- Page 78 -->

 
 
Periféricos: conectividad y administración 
78 
• Láser. Rápidas y de gran calidad. 
• Térmicas. Podemos encontrar tres tipos: 
• Impresoras de papel térmico. 
• Impresoras de cera. 
• Impresoras de transferencia térmica con sublimación. 
• Sublimación. La tinta se utiliza en estado gaseoso y no líquido. 
• Electroestáticas. 
• Tinta sólida. 
5.2.4. Trazadores o plotters 
Otro tipo de dispositivos de impresión que hay que mencionar, son los trazadores o plotters. Estos 
pueden ser de cuatro tipos: 
• De tambor vertical. 
• De plataforma. 
• Electroestático. 
• De inyección. 
5.3. Descripción de los tipos de impresoras 
5.3.1. Impresoras de impacto 
Son difíciles de encontrar hoy en día, aunque aún se usan algunas matriciales porque, al golpear el papel, 
resultan de utilidad para imprimir en papel autocopiativo (para cuando se requieren dos o más copias de 
cada documento) y papel continúo, con marca de autocorte. Es un sistema que ha sido muy utilizado 
por las gestorías para la impresión de nóminas. Además, los recambios son baratos y duraderos (cintas 
de tinta). Sin embargo, tienen una baja resolución. 
Dado que golpean el papel, resultan muy ruidosas. Podemos encontrar dos tipos: margarita y matriz de 
puntos. 

<!-- Page 79 -->

 
 
Periféricos: conectividad y administración 
79 
Margarita (en desuso) 
La impresora tiene un tambor que contiene todas las letras del alfabeto (en mayúsculas y minúsculas) y 
los signos de puntuación. 
El tambor rota para posicionarse en el carácter que queremos imprimir y lo golpea con un pequeño 
martillo. Entre el papel y el rodillo se encuentra una cinta con tinta. 
No permiten imprimir gráficos y, para cambiar el tipo de letra, hay que reemplazar físicamente el rodillo 
de impresión. 
Matriciales 
También denominadas de matriz de puntos o de agujas. Su funcionamiento se basa en una matriz de 
agujas que golpean, de forma individual, sobre una cinta de tinta que marca el papel. 
Los modelos más comunes utilizaban 9 y 24 agujas. Permitían imprimir gráficos y utilizar distintos tipos 
de letra. 
5.3.2. Impresoras de tinta 
Podemos distinguir dos tipos, las impresoras de inyección de tinta y las de burbuja. 
Inyección de tinta 
Son las más utilizadas hoy en día por su relación calidad-precio. Consiguen resultados de gran calidad a 
bajo precio. 
Estas impresoras tienen unos inyectores que expulsan gotas de tinta líquida contra el papel formando, 
mediante puntos, los gráficos y textos que se quieren plasmar. 
La impresión se realiza aplicando una carga eléctrica mediante un cristal piezoeléctrico (normalmente 
cuarzo), el cual hace saltar una gota de tinta (del orden de micras) por cada inyector. 
 
 
 
 
+ Info 
Un material piezoeléctrico es aquel que produce una corriente 
eléctrica al aplicar presión sobre él. 
 
 

<!-- Page 80 -->

 
 
Periféricos: conectividad y administración 
80 
La tinta se encuentra en unos cartuchos reemplazables. Antiguamente se utilizaban dos cartuchos (uno 
negro y otro de color). Hoy en día se utiliza uno negro y tres o cuatro cartuchos de color. Algunos 
cartuchos incluyen también el cabezal de impresión. (El uso de cartuchos no originales, cuya tinta era 
más ácida dañaba el cabezal de impresión). 
La calidad de impresión depende de la resolución (puntos por pulgada o p. p. p.), la tinta y el papel 
utilizado. 
Burbuja 
Tiene un funcionamiento similar a las de tinta, pero la gota de tinta se controla mediante calor. 
El procedimiento es el siguiente: 
1. Un calentador en el tubo capilar del cabezal de impresión vaporiza un poco de tinta, generando 
una burbuja de gas. 
2. La presión que se produce al expandirse dentro del tubo empuja una gota de tinta hacia el papel. 
3. El vacío creado en el capilar se llena con una nueva gota de tinta. 
5.3.3. Impresoras láser 
La impresora láser es un dispositivo electrofotográfico que utiliza la misma tecnología que las 
fotocopiadoras. Son una buena opción de compra dada su calidad de impresión, velocidad, nivel de ruido y 
coste (aunque la inversión inicial es mayor el mantenimiento es menor que, por ejemplo, las de tinta). 
Utilizan uno o más tóneres. Un tóner es un cilindro relleno con tinta en polvo. 
 
 
 
 
Vídeo 
Antes de continuar, puedes hacer una pausa para ver un vídeo. Te 
llevará un par de minutos. 
"Funcionamiento de impresión Láser". 
El proceso de impresión es difícil y con imágenes es mucho más 
fácil entenderlo. 
https://www.youtube.com/watch?v=99CUorxtyAs 
 

<!-- Page 81 -->

 
 
Periféricos: conectividad y administración 
81 
El proceso de impresión sería el siguiente: 
• Un ordenador envía una orden de impresión, la cual es recibida y procesada por unos circuitos 
internos de la impresora. 
• Se almacenan los datos a imprimir en un buffer de memoria RAM que tiene la impresora. 
• Un mecanismo electromecánico acomoda la hoja dependiendo de lo que se vaya a imprimir. 
• El escáner emite un haz de luz láser que se refleja a través de un espejo sobre el tambor. Al 
incidir la luz sobre este, se carga electroestáticamente y atrae el polvo del tóner sobre su 
superficie para formar el carácter o figura sobre el tambor. 
• El tambor deposita el tóner en el papel, este pasa luego a través de un fusor, que es un rodillo 
giratorio que alcanza altas temperaturas. Por presión y temperatura funde el tóner sobre el 
papel. El polvo al enfriarse, se pega a la hoja y genera la impresión (el tambor y fusor, tienen una 
vida limitada de impresiones de hojas, cuando se alcanza ese número es necesario cambiarlos, 
aunque en el caso del fusor el número es tan alto que no es corriente). 
5.3.4. Impresoras térmicas 
Posee un mecanismo similar al de las impresoras matriciales. Utiliza papel termo sensible y agujas que 
imprimen por calentamiento o fricción (produciendo calentamiento. 
Son silenciosas y su mecánica es sencilla, pero no son recomendables porque el papel térmico no es 
estable, se borra con el tiempo. 
Otro tipo de impresoras térmicas utilizan una cinta con tinta térmica. Al aplicar calor sobre la cera de la 
tinta, esta se plasma sobre el papel. 
Antiguamente se utilizaban mucho en los aparatos de fax. En la actualidad se utilizan en comercios 
(para hacer tickets y etiquetas) y en cajeros automáticos. 
5.3.5. Impresoras de sublimación 
Con esta tecnología se consiguen imágenes en color con calidad fotográfica y de alta resolución. La 
sublimación es el paso del estado sólido a gaseoso de forma directa (sin pasar por el estado líquido). 
El funcionamiento de estas impresoras consiste en vaporizar y fundir tinta que es absorbida por un 
papel especial. Se aplica una fuente de calor a la cinta y los colores se difunden sobre la hoja. La 
densidad de color depende de la intensidad del calor aplicado. 
Se utilizan en arte gráfico y en aplicaciones fotográficas. La calidad es muy buena, pero son muy lentas 
y el papel que utilizan es muy caro. 

<!-- Page 82 -->

 
 
Periféricos: conectividad y administración 
82 
5.3.6. Impresoras electroestáticas 
Electroestáticas o de transferencia directa utilizan un papel dieléctrico sobre el que generan zonas 
cargadas negativamente mediante unas agujas. 
Una vez cargada una línea en el papel, se espolvorea con tóner líquido que contiene partículas de 
carbón mezclado con parafina cargadas positivamente. Estas se pegan a las áreas cargadas 
negativamente formando la imagen. 
No se utilizan mucho porque son caras y no tienen demasiada resolución. 
5.3.7. Tinta sólida 
Utilizan piezas sólidas de cera con tinta. Para imprimir licuan la cera en unos contenedores y luego 
ponen la tinta en un tambor de transferencia donde se fusiona en frío sobre el papel en un único paso. 
 
 
 
 
+ Info 
Las impresoras de tinta sólida son impresoras de página, es decir, 
imprimen toda la página al mismo tiempo. 
 
5.3.8. Multifunción 
En el mismo dispositivo, tenemos impresora y escáner, y por tanto función de copiadora. Algunos 
modelos también incorporan fax, aunque cada vez el fax se utiliza menos, sigue usándose en algunas 
empresas. 
Pueden ser de inyección de tinta o laser (sólo blanco/negro y color). 
5.3.9. 3D 
Producen una pieza volumétrica partiendo de un diseño tridimensional (desarrollado por un programa 
gráfico u obtenido mediante un escáner 3D). 
En la actualidad tiene usos como la generación de piezas en prototipos, pero el más interesante es la 
producción de prótesis médicas, ya que permite adaptar los elementos a las particularidades de cada 
individuo. 

<!-- Page 83 -->

 
 
Periféricos: conectividad y administración 
83 
 
 
 
Ejemplo 
En las operaciones para introducir una prótesis de rodilla en un 
paciente, el médico introducía la prótesis con una forma 
aproximada y luego, durante la operación, la iba moldeando, por lo 
que la operación era larga. 
En la actualidad, algunos centros médicos contratan los servicios 
de empresas externas que, mediante un escáner 3D, digitalizan una 
copia exacta de los huesos de la pierna del cliente. 
 
 
Las impresoras 3D utilizan distintos procesos para imprimir dependiendo de su tecnología. Destacamos 
algunas formas de realizar la impresión: 
• Acumulando capas de polvo de diversos metales, las cuales son fundidas entre sí por mediación 
de un láser. 
• Compactando los estratos de polvo. 
Mediante la inyección de polímeros (aglutinante). 
5.3.10. Plotters 
 
Fuente: PxHere 
Los plotters (o trazadores de gráficos) están destinados principalmente a la impresión de planos en 
proyectos de arquitectura e ingeniería, ya que permiten trabajar con grandes formatos de página (A1 y 
superior). 

<!-- Page 84 -->

 
 
Periféricos: conectividad y administración 
84 
Antiguamente consistían en una serie de plumillas móviles de diferentes grosores y colores que se 
movían por la hoja reproduciendo el plano. Eran imprecisos y requerían mantenimiento. 
En la actualidad, la mayoría de los plotters son de inyección de tinta. En realidad, son impresoras de tinta 
que utilizan un papel mucho más ancho y que vienen en rollos muy largos (muchos metros). 
Un tipo especial de plotter son los de corte. Además de imprimir, pueden cortar el papel utilizando unas 
cuchillas. Se utilizan mucho para la impresión de vinilos decorativos. 
6. Hardware de visualización 
Existen muchos tipos de elementos de visualización, desde pequeños displays hasta pantallas gigantes 
de vídeo. 
Este tipo de salidas son las más utilizadas para la interacción con el ordenador, por lo que tienen una 
gran importancia. 
Para procesar la salida de imagen se necesita una tarjeta gráfica y un monitor o pantalla. 
En este punto vamos a estudiar los principales tipos de tarjeta gráfica y de monitores, aunque también 
te vamos a mostrar un breve resumen de las pantallas táctiles. 
6.1. Tarjeta gráfica 
La tarjeta de vídeo o tarjeta gráfica se encarga de procesar los datos que le llegan del procesador para 
generar una salida que podrá representarse en un monitor. 
Evolución histórica 
La evolución histórica de los ordenadores personales está intrínsecamente ligada a la de las tarjetas 
gráficas. 
Hasta principios de los años 80, hablamos de adaptadores de imagen más que de tarjetas gráficas en el 
sentido moderno. El recorrido moderno de estas tarjetas comienza en 1981 con el MDA (Monochrome 
Display Adapter), diseñado principalmente para mostrar texto de alta calidad en blanco y negro. 
Ese mismo año, IBM introdujo el CGA (Color Graphics Adapter), que permitió la incorporación del color 
en las pantallas y es considerado uno de los primeros adaptadores gráficos con soporte para gráficos en 
color. 
En 1984, apareció el EGA (Enhanced Graphics Adapter), uno de los pioneros en incorporar la memoria y 
un chipset muy básico dedicado al procesamiento de gráficos. 

<!-- Page 85 -->

 
 
Periféricos: conectividad y administración 
85 
La contribución importante del VGA (Video Graphics Array), lanzado en 1987, fue la adopción de un 
conjunto de especificaciones (conector de 15 pines, controladores, compatibilidad con modos 
anteriores) que promovió la interoperabilidad entre múltiples fabricantes. 
A finales de los 80 y principios de los 90, las tarjetas gráficas comenzaron a adoptar el estándar SVGA 
(Super Video Graphics Array), que permitía resoluciones superiores a VGA, y el XGA (Extended 
Graphics Array), con una mayor capacidad gráfica. Durante este periodo, también se popularizó el uso 
de VRAM (Video RAM), memoria diseñada específicamente para mejorar el rendimiento en el 
procesamiento gráfico. 
La característica evolutiva esencial de las tarjetas, las resoluciones cada vez mayores continuó con 
SXGA, UXGA y posteriormente con los estándares HD, Full HD y Ultra HD. Con la evolución de estas 
tarjetas, los ventiladores se hicieron necesarios para disipar el calor generado por los componentes cada 
vez más potentes. 
En la actualidad, las resoluciones han alcanzado niveles asombrosos, con Ultra HD (3840x2160 píxeles) 
y 6K (7680x4320 píxeles) liderando el mercado. Esta evolución constante ha sido posible gracias a los 
avances tecnológicos en el diseño de las tarjetas gráficas y a la demanda de experiencias visuales cada 
vez más inmersivas. 
La VRAM y el desarrollo de los procesadores de gráficos en forma de GPUs han evolucionado con el 
tiempo hasta fundirse en la misma pieza de silicio, el mismo chipset. 
Los conectores también evolucionan del VGA al DVI, HDMI y Display Port. 
Cuando hablamos hoy día de una tarjeta gráfica contemplamos los siguientes elementos: 
• GPU (Graphics Processing Unit) procesa y renderiza gráficos. 
• VRAM permite el rápido acceso de la GPU a los datos. 
• VRM (Voltage Regulator Module) suministra voltaje adecuado a los demás componentes del 
adaptador. 
• VBIOS (Vídeo BIOS) almacena las configuraciones de los componentes del adaptador. 
• Refrigeración, mantiene entre disipadores y ventiladores una temperatura segura para los 
componentes. 
• Interfaces de conexión, externas (VGA, DVI, HDMI, DisplayPort) e internas (AGP, PCIe). 
Tipos 
Según donde se encuentran y qué recursos del ordenador utilizan, podemos encontrar dos tipos de 
tarjetas: 
• Integrada. Suele estar integrada en la placa base, aunque también puede estar en la CPU. Su 
coste es reducido, pero consume recursos de la CPU. 

<!-- Page 86 -->

 
 
Periféricos: conectividad y administración 
86 
• Dedicada (o discreta). Es una tarjeta no integrada en la placa base, se conecta a está 
normalmente en una ranura de expansión (como PCI-Express) y cuenta con una unidad de 
procesamiento (GPU o graphics processing unit) y una memoria (GRAM) propias e 
independientes de la memoria y del procesador del ordenador, son más potentes que las 
gráficas integradas y algunas incluyen su propio disipador. 
Interfaz con la placa base 
Han existido muchos sistemas de conexión entre la tarjeta gráfica y la placa base. Actualmente, el más 
utilizado es PCI-Express (PCIe), aunque aún se pueden encontrar algunos modelos antiguos con 
interfaz AGP (normalmente de segunda mano). 
Interfaz con el monitor 
Existen muchos tipos de interfaz con el monitor, pero los más habituales son: 
• VGA (Video Graphics Array). Se diseñó para trabajar con los monitores CRT. Convierte la señal 
digital que le envía la CPU en señal analógica que puede interpretar el monitor. Utiliza un 
conector de 15 pines. Todavía se puede encontrar en muchas tarjetas gráficas. 
• DVI (Digital Visual Interfaces). Utiliza una señal digital (no la convierte en analógica). 
• HDMI (High Definition Multimedia Interface). Transmite audio y vídeo de alta definición en 
formato digital. 
• DisplayPort. Rival de HDMI. Al igual que este, transmite audio y vídeo de alta definición en 
formato digital. Está libre de patentes. Su uso es mucho menor que el HDMI. Cuenta con una 
versión reducida (Mini DisplayPort) en la cual está basado el puerto Thunderbolt de Apple. 
 
Tarjeta de video. Se pueden observar, de izquierda a derecha, los siguientes conectores: 
VGA, HDMI y DVI 

<!-- Page 87 -->

 
 
Periféricos: conectividad y administración 
87 
 
 
 
El experto opina 
Actualmente, la industria del videojuego es importantísima y 
genera una gran cantidad de dinero. 
Por ello, las tarjetas gráficas han experimentado una gran 
evolución, presentando una tecnología más avanzada que el resto 
de los componentes. 
También resulta muy importante para programas de diseño, 
arquitectura, etc. 
Está diseñada para la generación de gráficos. Sin embargo, es tal su 
potencia, que se han generado lenguajes (o se han adaptado) para 
trabajar con los procesadores gráficos (GPU) en procesos tales 
como algoritmos de inteligencia artificial, simulación de la dinámica 
de fluidos o análisis sísmico. 
 
6.2. Monitor 
 
Es el dispositivo de salida más utilizado para interactuar con el usuario. Presenta visualmente la 
información procesada. Transforma la salida de la tarjeta gráfica en imágenes. 

<!-- Page 88 -->

 
 
Periféricos: conectividad y administración 
88 
Antiguamente los monitores utilizaban la tecnología CRT (tubo de rayos catódicos), pero hoy en día se 
ha dejado de comercializar y han sido superados con creces por las nuevas tecnologías, que nos 
permiten mayor definición con pantalla plana. Te vamos a mostrar las principales tecnologías utilizadas 
en la actualidad: 
• LCD: es la tecnología en que se basan la mayoría de los monitores. Utiliza cristal líquido, el cual 
produce color al ser retro iluminado por lámparas fluorescentes. Existen diversas variantes que 
se adaptan a diferentes necesidades: 
• IPS (In-Plane Switching): Proporciona amplios ángulos de visión y una excelente precisión 
en la reproducción de colores, ideal para trabajos gráficos y diseño. 
• TN (Twisted Nematic): Ofrece tiempos de respuesta rápidos y es común en monitores para 
videojuegos competitivos. Sin embargo, tiene colores menos vibrantes y ángulos de visión 
limitados. 
• VA (Vertical Alignment): Destaca por su alto contraste y buenos niveles de negros, siendo 
ideal para contenido multimedia y entornos oscuros. 
• Plasma: utiliza gases nobles en lugar de cristal líquido. Ofrece mejor contraste, colores y ángulo 
de visión que los monitores LCD, pero tiene una menor vida útil. Tiene altos niveles de brillo y 
contraste pero su consumo energético es elevado. Otra de sus desventajas es el mayor grosor si 
lo comparamos con otras tecnologías. 
• Led: es una evolución de la tecnología LCD. Ilumina la pantalla mediante lámparas led en lugar 
de utilizar lámparas fluorescentes. Mejora la calidad de imagen (brillo, contraste y ángulo de 
visión). La retroiluminación está compuesta por diodos emisores de luz en lugar de tubos 
fluorescentes, cuenta con algunas variantes: 
• Edge LED: Iluminación LED en los bordes de la pantalla, permitiendo diseños ultradelgados, 
aunque con menos uniformidad en la iluminación. 
• Full Array LED: LEDs distribuidos por toda la pantalla, ofreciendo un mejor control del brillo 
y un contraste superior. 
• Mini-LED: LEDs más pequeños y numerosos, que permiten una iluminación más precisa y 
acercan esta tecnología al rendimiento del OLED. 
• OLED (Organic Light Emitting Diode): utilizan materiales orgánicos que tienen la propiedad de 
iluminarse al pasar una corriente eléctrica a través de ellos. Representa un salto cualitativo al 
permitir que cada pixel emita su propia luz, eliminando la necesidad de retroalimentación por lo 
que son más delgados, consumen menos energía, negros puros y mayor eficiencia en la 
representación de colores. Variantes: 
• AMOLED (Active Matrix OLED): Utilizada principalmente en dispositivos móviles y 
wearables, mejora el control sobre cada píxel para una mayor precisión. 
• WOLED (White OLED): Usa una capa emisora blanca y filtros de color para televisores de 
gran tamaño, como los de LG. 
• MicroLED: Una tecnología emergente que combina las ventajas del OLED y LED, ofreciendo 
píxeles autoemisivos con una vida útil más larga y sin riesgo de quemado. 

<!-- Page 89 -->

 
 
Periféricos: conectividad y administración 
89 
6.2.1. Resolución, ratio y refresco 
Tanto en los monitores como en los televisores, existen unas características a la hora de visualizar las 
imágenes. Dependiendo de lo que visualicemos en la pantalla, estas características serán más o menos 
apreciable para el ojo humano (por ejemplo, en el flujo de movimiento en el futbol o deportes de 
rapidez, y en determinados videojuegos). 
Resolución 
Es el número de píxeles que un dispositivo de visualización es capaz de mostrar, expresada en función 
de su anchura y su altura. 
Por ejemplo, si un monitor tiene una resolución de 1920 x 1080 píxeles, significa que el monitor cuenta 
con 1920 píxeles de anchura y con 1080 píxeles de altura. 
Ratio de aspecto 
Este número se usa para describir la relación que hay entre la anchura y la altura de la pantalla. Es decir, 
y siguiendo con el ejemplo anterior, ese monitor tiene una relación de aspecto de 16:9. El hecho es que 
si dividís 1920/16 y 1080/9 siempre os saldrá un mismo número: 120. 
Los primeros monitores TFT eran de 4:3 Con la aparición de las pantallas panorámicas surgieron dos 
nuevas ratios, 16:10 y 16:9. Actualmente el formato 16:10 es usado en monitores profesionales, 
mientras que el formato 16:9 es menos profesional, para usuarios domésticos. 
Tasa de refresco 
Es la cantidad de imágenes que puede mostrar el dispositivo por segundo. Se mide en hercios (Hz) ya 
que se trata de una frecuencia de actualización. Una pantalla puede tener 60 Hz, y esto significaría que 
es capaz de actualizar la imagen mostrada hasta 60 veces por segundo. 
La tasa de refresco está directamente relacionada con las capacidades de la visión humana. 
Supuestamente, el ojo humano es capaz de captar hasta unas 220 imágenes diferentes por segundo. 
Cuantas más imágenes muestra una pantalla por segundo, más fluido es el movimiento en forma de 
vídeo (esto cobra valor en retransmisiones deportivas y video juegos). 
La tasa de refresco también puede suponer un cuello de botella para los dispositivos que procesan estas 
imágenes. Da igual tu hardware, tu pantalla puede estar haciendo un 'cuello de botella' por su tasa de 
refresco. 
Si la pantalla, solo soporta 60 Hz, y tienes una Tarjeta Gráfica está produciendo 200 imágenes 
diferentes por segundo (200 fps), que es lo que define al frame rate, pero la pantalla solo es capaz de 
actualizarse 60 veces en ese mismo segundo, se están perdiendo 140 imágenes que no se pueden 
mostrar por las capacidades máximas de la pantalla. Esto provoca una pérdida de frames, y en ocasiones 
efectos negativos sobre la imagen. 

<!-- Page 90 -->

 
 
Periféricos: conectividad y administración 
90 
Diferencia entre " p " y " i " 
La diferencia entre 1080p y 1080i estriba en la forma de desplegar las imágenes en cada segundo, pese 
a que ambos tienen la misma resolución de 1920 x 1080 píxeles. Pero no son iguales técnicamente y 
esto también es distinguible para el ojo humano en ciertas circunstancias. 
La resolución de 1920×1080 corresponde a 1080 líneas horizontales de 1920 píxeles cada una. Pero 
esta información se despliega de forma diferente en 1080p y en 1080i. 
La 'p' en el formato 1080p significa progresivo, los frames aparecen progresivamente, uno detrás de 
otro. Las líneas pares e impares se despliegan a la vez. En un segundo se muestran 60 frames, que 
coinciden con el número de actualizaciones de la imagen, cada una tiene 1080 líneas de 1920 píxeles. 
La 'i' en el formato 1080i quiere decir 'interlaced' (entrelazado) y significa que cada frame no aparece 
de forma completa en la pantalla, si no que primero se despliegan las líneas horizontales impares y en el 
siguiente cambio la imagen se completa con las líneas pares. El proceso es muy rápido por lo que el ojo 
humano rara vez es capaz de notarlo. Entonces cada actualización supone 540 líneas de 1920 píxeles, 
pues se renovarán las impares o las pares, según corresponda, pero nunca todas a la vez. Así que en este 
formato durante un segundo hay 60 actualizaciones, pero sólo se despliegan 30 frames o imágenes 
porque en cada actualización sólo aparece la mitad de un frame. 
6.2.2. Cronograma de Resoluciones 
 

<!-- Page 91 -->

 
 
Periféricos: conectividad y administración 
91 
Acrónimos 
• CGA, Color Graphics Adapter. 
• MDA, Monochrome Display Adapter. 
• EGA, Enhanced Graphics Adapter. 
• VGA, Video Graphics Array. 
• SVGA, Super VGA. 
• SXGA, Super Extended Graphics Array. 
• UXGA, Ultra Extended Graphics Array. 
• HD, High Definition. 
• WXGA, Widescreen Extended Graphics Array. 
• QHD, Quad HD. 
• UHD, Ultra High Definition. 
6.3. Pantalla táctil 
 
Pantalla táctil 80". Fuente: Vimeo 

<!-- Page 92 -->

 
 
Periféricos: conectividad y administración 
92 
 
 
Fuente: Pixabay y PxFuel 
La pantalla táctil es un dispositivo de entrada y salida al mismo tiempo, que permite al usuario introducir 
datos en el sistema mediante pulsaciones en la pantalla y recibir la información procesada en esta. 
Actualmente tienen un uso muy extendido, utilizándose en móviles, portátiles, cajeros automáticos, 
etcétera. 
Existen dos tipos básicos de pantallas táctiles: 
• Resistivas. Tiene varias capas entre las que destacan dos de material conductor, entre las cuales 
hay una pequeña separación. Al ejercer presión sobre un punto concreto, estas capas se unen, 
produciendo un cambio en la corriente eléctrica que permite detectar la posición. 
Ventajas: 
• Son más sensibles a la presión que las capacitativas. 
Desventajas: 
• Pierden aproximadamente un 25% del brillo debido a las capas necesarias. 
• Pueden ser dañadas por objetos afilados. 
• No permite multitouch. 

<!-- Page 93 -->

 
 
Periféricos: conectividad y administración 
93 
• Capacitivas. Están cubiertas de un material que conduce una corriente eléctrica a través del 
sensor, adquiriendo esté capacitancia. El cuerpo humano también tiene capacitancia. Al entrar 
en contacto el dedo con la pantalla se produce una distorsión que nos permite detectar la 
posición. 
Ventajas: 
• Es multitouch. 
• No pierde brillo. 
• La sensación es más fluida al no tener que ejercer presión. 
Desventajas: 
• Debe tocarse con el cuerpo. No sirve un lápiz y no se puede tocar con guantes. 
• El procesado de la señal es más complejo. 
 
 
 
 
+ Info 
Una pantalla multitouch es aquella que puede detectar varias 
pulsaciones simultáneas en múltiples puntos de la pantalla. 
 
7. Hardware de digitalización. Escáner 
El escáner es un dispositivo que explora un espacio o imagen y lo traduce en señales eléctricas para su 
procesamiento (lo traduce a formato digital). 
7.1. Conexión con el ordenador 
Con la mejora de la digitalización, los ficheros resultantes de escanear pueden ser muy grandes (una 
imagen con calidad de 24 bits, tamaño algo mayor que A4 y descomprimida, puede ocupar unos 100 
megabytes). Los escáneres de actuales, de alta calidad y rápidos en el escaneo, generan la información 
en pocos segundos, por hay que tener una conexión lo más rápida posible. 
Antes los escáneres usaban conexiones paralelas que no podían ir más rápido de los 70 
kilobytes/segundo, SCSI-II se adoptó para los modelos profesionales y aunque era algo más rápido 
(unos cuantos megabytes por segundo) era bastante más caro. 

<!-- Page 94 -->

 
 
Periféricos: conectividad y administración 
94 
Actualmente los que usan conexión USB, poseen una tasa de transferencia de hasta 12 megabits por 
segundo (Mbps) para los USB 1.1, de hasta 480 megabits por segundo para las conexiones USB 2.0, de 
hasta 5 gigabits (Gbps) por segundo para los USB 3.0, de hasta 10 Gbps para los USB 3.1 y de hasta 20 
Gbs para los USB 3.2, lo que elimina el cuello de botella que se tenía al principio. 
Existen 2 estándares para interfaces de PC con Windows o Macs, son: 
• TWAIN. Originalmente se utilizaba para uso doméstico o de bajo coste. Actualmente se usa 
también para el escaneado de gran volumen. 
• ISIS. Creado por Pixel Translations, que utiliza SCSI-II, se emplea en máquinas grandes 
destinadas a empresas. 
Windows Image Acquisition (WIA) 
Es un modelo de controlador e interfaz de programación de aplicaciones (API) para las versiones más 
modernas del sistema operativo Microsoft Windows que permite a las aplicaciones de gráficos 
comunicarse con dispositivos de imagen tales como escáneres, cámaras digitales y equipos de vídeo 
digital. 
Fue introducido por primera vez en el año 2000 como parte de Windows Me, y continúa siendo el 
estándar de dispositivos de imagen y modelo API a través de las sucesivas versiones de Windows. A 
partir de Windows XP, es implementado como un servicio bajo-demanda. 
WIA es un conjunto de utilidades significativo para el soporte de imágenes digitales proporcionado por 
Still Image Architecture (STI) en Windows 2000. Mientras que STI sólo proporciona una interfaz de 
bajo nivel para realizar transferencias de datos básicas desde y hacia el dispositivo (y la petición del 
proceso de escaneado de imagen en una máquina Windows a través de un dispositivo externo), WIA 
proporciona un entorno de trabajo a través del cual los dispositivos pueden presentar sus capacidades 
únicas al sistema operativo, y las aplicaciones pueden tomar ventaja de esas características. 
Según Microsoft, los controladores WIA están formados por un componente de interfaz de usuario (UI) 
y un componente núcleo del controlador, cargados en dos procesos diferentes: UI en el espacio de la 
aplicación y el núcleo del controlador en el servicio WIA. 
En comparación con TWAIN, se dice que WIA es más flexible, porque es una interfaz estandarizada que 
no requiere una unión fuerte entre el software del escáner y el controlador (los escáneres sólo-TWAIN a 
menudo están limitados a las funciones activadas en su unión controlador-aplicación). La mayoría de los 
escáneres recientes soportan WIA. 

<!-- Page 95 -->

 
 
Periféricos: conectividad y administración 
95 
7.2. Tipos de escáner 
 
Existen muchos tipos de escáneres. El escáner clásico de ordenador personal es aquel que permite 
digitalizar un documento (normalmente en papel). 
Hay diversos tipos: 
• De mano. Requiere que el usuario vaya pasando el escáner por la superficie del documento. 
Tienen poca resolución. 
• De mesa (o plano). Es el más utilizado. Posee una fuente de luz y un sensor de luz situados en 
un brazo móvil. Este va recorriendo un documento situado sobre una placa de vidrio. 
Hoy en día vienen integrados en las impresoras multifunción y pueden tener un alimentador de 
hojas para escanear varios documentos. 
También podemos encontrar adaptadores para diapositivas. 
• Cenital. Para escanear elementos frágiles como documentos o libros antiguos, evitando el 
contacto físico con ellos. 
• De tambor. Los documentos a escanear se colocan sobre un cilindro o tambor giratorio. Son los 
que tienen mayor calidad y se suele utilizar para diseño gráfico. 
Existen muchos otros tipos de escáner que se utilizan para realizar distintas funciones como los lectores 
de códigos de barras (de diversos tipos, de mano, integrados en las cajas de venta de los 
supermercados, etc.) y los sistemas de identificación que realizan un escáner de huellas digitales, 
actualmente muy de moda para desbloquear móviles, portátiles o para control de presencia en el 
trabajo ("fichar"). 
También se utilizan escáner de retina, especialmente para controles de seguridad. 

<!-- Page 96 -->

 
 
Periféricos: conectividad y administración 
96 
 
Especial importancia tienen los distintos tipos de escáner médico, que permiten, por medio de 
ultrasonidos, resonancia magnética, radiaciones ionizantes o rayos X, obtener una imagen de órganos o 
partes internas del cuerpo. Esta es, sin duda, una de las herramientas más importantes de diagnóstico. 
 
El móvil, al contar con una cámara, puede actuar como escáner. Algunos de los usos más habituales son: 
• Identificación. Por ejemplo, el reconocimiento de huella digital para desbloquear el móvil. 
• Escanear códigos de barras. Similar al lector de código de barras. 
• Escanear códigos QR. Para descargar aplicaciones. 
• Aplicaciones para escanear documentos. Existen aplicaciones que funcionan como un escáner 
de mano, resultando muy útiles para operaciones de OCR. 
 

<!-- Page 97 -->

 
 
Periféricos: conectividad y administración 
97 
 
 
 
+ Info 
OCR (Optical Character Recognition) es un proceso que permite 
extraer el texto contenido en una imagen a través del 
reconocimiento de los caracteres que aparecen en dicha imagen. El 
resultado se puede abrir con un editor de textos. 
 
 
Escaneo de código QR 
8. Equipos de control numérico computerizados 
(CNC) 
El mecanizado CNC, hace referencia a un proceso de fabricación sustractivo, que por lo general usan 
controles informáticos y máquinas que, eliminando capas de material de una pieza sin definir, producen 
una pieza personalizada. 
El CNC es un sistema que controla todos los movimientos de un elemento físico; una herramienta 
montada en una máquina. 
En la década de los 50 se introdujo en Estados Unidos el concepto de control numérico en una 
fresadora, que usaba tecnología de válvulas de vacío, en los 60 estas válvulas se sustituyeron por 
transistores y en la década de los 70 la introducción de las computadoras sentó las bases del CNC. 

<!-- Page 98 -->

 
 
Periféricos: conectividad y administración 
98 
Podemos clasificar las máquinas de CNC en tres tipos genéricos, basándonos en la trayectoria del 
mecanizado: 
• Máquinas de control punto a punto, como taladradoras o punteadoras. 
• Máquinas de control paraxial, por ejemplo, los tornos. 
• Máquinas de control interpolar, son polivalentes. 
Algunos ejemplos de máquinas CNC son: 
• Fresadora: 
Funciona arrancando viruta mediante el movimiento de una herramienta rotativa de varios filos 
de corte llamada fresa. 
• Torno de control numérico: 
El software de la computadora utiliza datos alfanuméricos, siguiendo los ejes cartesianos x e y. 
• Rectificadora: 
Realiza mecanizados por abrasión, usa discos abrasivos llamados muelas. 
Trabaja con mayor precisión dimensional y produce una pieza más fina que elmecanizado de 
arranque de viruta. 
• Máquina de corte por láser: 
Su fundamento es la concentración de luz en una superficie de trabajo. 
• Enrutadores. 
• Cortadores e plasma. 
• Impresoras 3 D. 
8.1. Funcionamiento de una máquina CNC 
Para ver el funcionamiento, vamos primero a indicar los elementos principales de una máquina CNC: 
• El mecanizado. 
• Dispositivo de entrada. 
• Un controlador. 

<!-- Page 99 -->

 
 
Periféricos: conectividad y administración 
99 
• Máquina herramienta. 
• Sistema de accionamiento. 
• Dispositivo de realimentación en sistemas con servomotores. 
• Monitor. 
 
Diagrama de bloques de una máquina CNC con servomotores 
Ahora vamos a examinar funciones específicas de su programación. 
8.1.1. Control de movimiento 
Tienen dos ejes o más programables, que pueden ser lineales o rotatorios, los nombres de los ejes 
lineales son X; Y y Z. Los ejes giratorios A, B y C. 
El control de movimiento se realiza mediante dos sistemas que pueden funcionar individualmente o 
combinados: 
• Valores absolutos. Las coordenadas del punto de destino son referidas al punto de origen de 
coordenadas. 
• Valores incrementables. Las coordenadas del punto de destino son referidas al punto actual. 

<!-- Page 100 -->

 
 
Periféricos: conectividad y administración 
100 
8.1.2. Accesorios y funciones programables 
Tenemos: 
• Cambiador automático de herramienta. 
• Velocidad y activación de herramienta. 
• Refrigerante. 
8.1.3. Programa CNC 
Es un listado secuencial de instrucciones que ejecutará la máquina. 
Está escrito en un lenguaje de bajo nivel, llamado G y M, estandarizado por las normas 6983 de ISO y 
RS274 de EIA y compuesto por instrucciones Generales (código G) y Misceláneas (código M). 
El programa presenta un formato de fases conformadas por bloques, encabezados por la letra N. 
Como vemos en la figura inferior, cada movimiento o acción se realiza secuencialmente y cada bloque 
está numerado y generalmente contiene un solo comando. 
 
• El código G describe las funciones de movimiento de la máquina. 
• Por ejemplo, movimientos rápidos, avances, avances radiales, pausas, ciclos. 
• El código M describe las funciones misceláneas que se requieren para el mecanizado de la pieza, 
pero que no corresponden a los movimientos de la máquina. 
• Por ejemplo, arranque y detención del husillo, cambio de herramienta, refrigerante, 
detención del programa. 

<!-- Page 101 -->

 
 
Periféricos: conectividad y administración 
101 
• A su vez, cada código contiene variables (direcciones), identificadas con otras letras y definidas 
por el programador para cada función específica. Por ejemplo: 
• F define la velocidad de avance. 
• S la velocidad del husillo. 
• T la herramienta seleccionada. 
• X, Y y Z el movimiento de los ejes. 
• I, J y K la localizción del centro de un arco. 
• Etc. 
8.1.4. Controlador CNC 
Es componente clave ya que interpreta un programa CNC y acciona la serie de comandos en orden 
secuencial. 
A medida que lee el programa, el controlador activa las funciones apropiadas de la máquina, impulsa el 
movimiento de los ejes, y en general, sigue las instrucciones dadas en el programa. 
Además de interpretar el programa CNC, el controlador tiene varios otros propósitos, por ejemplo: 
• Modificar (editar) los programas si se detectan errores. 
• Realizar funciones de verificación especial (como el funcionamiento en vacío) para confirmar la 
exactitud del programa CNC. 
• Especificar ciertas entradas importantes del operador, tales como los valores de longitud de las 
herramientas. 
8.1.5. Programa CAM 
El software CAM (Computer Aided Manufacturing), o programa de fabricación asistida por 
computadora, no solo incluye el control de máquinas, sino que también se encarga de combinar 
máquinas, software, procesos y personas para así crear piezas de alta calidad. 
Utiliza los modelos y los ensamblajes creados en el software CAD, para generar trayectorias con las que 
las herramientas de mecanizado convierten los diseños en piezas físicas (como por ejemplo en como 
Fusion 360). 
CAM ayuda a crear programas para diversas máquinas CNC que admiten diferentes procesos de 
fabricación (como el fresado, torneado, corte y la fabricación aditiva). 

<!-- Page 102 -->

 
 
Periféricos: conectividad y administración 
102 
 
 
 
+ Info 
CAD Y CAM: 
Ambos, aprovechan el software y la potencia computacional para 
ayudar a crear diseños más complejos y eficaces de los que se 
harían a mano.  
Diferencias: 
• CAD ayuda a los diseñadores a crear representaciones 
digitales denominadas modelos 3D. 
• CAM ayuda a escribir código para controlar las máquinas 
CNC que crean piezas físicas. 
 
8.1.6. Sistema DNC 
Un DNC es un sistema o una arquitectura (Distributed Numerical Control: Control Numérico 
Distribuido) que permite la comunicación y transferencia de programas (códigos G/M) entre una 
computadora central (que puede ser un servidor o una estación de trabajo) y múltiples máquinas 
CNC en red. 
Una vez que se ha desarrollado el programa CNC (ya sea manualmente o con un programa CAM), debe 
cargarse en el controlador y para ello se usa el sistema DNC. 
Tradicionalmente la transferencia de los programas se efectuaba mediante un protocolo rudimentario 
de comunicaciones serie (RS-232C), pero actualmente gracias al avance de la tecnología, se puede 
dotar a los controladores actuales (TCP/IP, Profinet, EtherNet/IP, Serial-to-Ethernet) con mayores 
capacidades de comunicación, de tal forma que puedan conectarse en red, por ejemplo, mediante 
Ethernet. 
9. Cortadora láser 
También conocida como máquina CNC (control numérico por computadora), o como máquina corte 
por láser. 
Una cortadora láser es una máquina de control numérico por computadora que permite cortar con 
gran precisión diferentes tipos de materiales utilizando un rayo láser de gran potencia. 

<!-- Page 103 -->

 
 
Periféricos: conectividad y administración 
103 
El uso del software tiene una gran importancia, ya que controla diversos parámetros con exactitud y 
permite guardar plantillas de corte. 
Los diseños realizados pueden enviarse a la cortadora láser para que se realice el corte o se grabe la 
chapa de metal, cuero o madera MDF con total precisión. 
Permite que artistas y creadores digitales puedan dar vida en el plano físico a sus diseños. Se crean 
rápidamente prototipos, de forma que los diseñadores pueden revisar de una forma rápida y con coste 
bajo sus trabajos antes de producirlos a gran escala. 
Han supuesto un gran avance en las empresas, facilitando el corte de grandes piezas de material en los 
talleres mecánicos y en la fabricación industrial. 
Algunos de los materiales que se pueden cortar con estos equipos son: 
• Madera simple, contrachapada o MDF. 
• Corcho. 
• Papel. 
• Cartón. 
• Cuero. 
• Fieltro. 
• Acrílico. 
• Polipropileno. 
• Cerámica. 
• Vidrio. 
• Metales. 
Historia 
Muchos autores atribuyen el descubrimiento del rayo láser a Einstein en 1917, pero ha fecha actual 
sigue habiendo polémica sobre ello. 
Su origen se remonta a 1965, cuando la Western Electric Engineering Research Center utilizó esta 
máquina por primera vez para perforar agujeros en los troqueles de diamantes. 
En el corte de metales por chorro de oxígeno asistido por láser, los británicos fueron pioneros en 1967 y 
en los 70, esta tecnología fue puesta en producción para cortar titanio en aplicaciones aeroespaciales. 
Simultáneamente para poder realizar cortes en materiales no metálicos como por ejemplo el textil, se 
adaptaron láseres de CO2. 

<!-- Page 104 -->

 
 
Periféricos: conectividad y administración 
104 
9.1. Tipos de cortadoras láser 
Existen diferentes tipos que se ajustan a necesidades específicas dentro de un amplio rango de 
industrias. 
Cada máquina permite realizar cortes y diseños personalizados con una precisión absoluta, que 
optimiza en gran manera la producción, puesto que se ha reducido muchísimo el trabajo humano. 
Hay tres tipos de máquinas de corte láser. 
9.1.1. Láseres de gas 
Este tipo de láser puede utilizar dos tipos de compuestos: 
• Una mezcla de dióxido de carbono (CO2). 
Se hace viable estimulando eléctricamente dicha mezcla de dióxido de carbono. 
Es más utilizado en materiales no metales. 
Se utiliza en muchos ámbitos médicos e industriales. 
• Nitrógeno. 
Debe ser puro, ya que de lo contrario se puede oxidar el metal con el que se trabaja. 
Funciona bien con metales como el acero y el aluminio. 
9.1.2. Láser de cristal 
Utiliza láseres fabricados con: 
• nd: YAG (granate de aluminio e itrio dopado con neodimio). 
• nd: YVO (ortovanadato de itrio dopado con neodimio). 
nd es el símbolo químico del neodimio. 
Estos cristales forman parte del grupo de los de estado sólido y permiten un corte de altísima potencia. 
Puede utilizarse tanto con metales como con no metales. 
Tiene gran variedad de aplicaciones, desde la medicina y la odontología hasta el ejército y la fabricación. 
El mayor inconveniente de una máquina láser de cristal es que se trata de un equipo caro, tienen menor 
durabilidad que otras máquinas del mercado. 

<!-- Page 105 -->

 
 
Periféricos: conectividad y administración 
105 
9.1.3. Láseres de fibra 
Tiene varias similitudes con el proceso de cristal, en el hecho de que la fibra óptica también pertenece al 
grupo de estado sólido. 
Tiene una vida útil mucho más larga que la de los dos tipos de corte anteriores, de unas 25.000 horas. 
También requiere muy poco mantenimiento y, en caso de necesitar piezas de repuesto, son muy 
baratas. 
9.2. Funcionamiento 
El corte láser es un tipo de proceso de separación térmica, donde el rayo láser incide en la superficie del 
material calentándolo con tanta fuerza que lo derrite y vaporiza por completo. 
Cuando el rayo ha penetrado completamente en el punto que se ha marcado por el software como 
punto inicial, comienza el proceso de corte del material siguiendo la geometría diseñada, cortando (o 
separando) el material. 
Para la separación del material sobrante, es necesario el uso de un gas a presión, que dependiendo del 
tipo de máquina y material a cortar podrá ser por ejemplo oxígeno, nitrógeno y argón. 
 
 
 
 
Básico 
Funcionamiento: 
1. El sistema envía un haz de luz intensa que se refleja a través 
de un conjunto de espejos hasta el cabezal de corte. 
2. Dentro del cabezal de corte, el láser se enfoca a través de 
una lente y se reduce a un haz extremadamente 
concentrado. 
3. A continuación, el haz se proyecta hacia el material y se 
utiliza para cortarlo. 
 

<!-- Page 106 -->

 
 
Periféricos: conectividad y administración 
106 
9.3. Ventajas 
Estas son las razones por las que se prefiere el corte por láser en comparación con otras tecnologías de 
corte: 
• Alta velocidad de producción. 
• Alta precisión y exactitud: 
Los cortes son limpios, con muy pocos rebordes. Se pueden trabajar perfiles complejos con 
pequeños radios de curvatura. 
Se produce poquísima distorsión o zonas afectadas por el calor. 
• Anchos de corte más estrechos: 
La gran variedad de grosores permitidos incluye los muy estrechos como son logotipos, código 
de barras o números de serie. 
• Sin riesgo de contaminación: 
No se emplean elementos químicos o que puedan resultar contaminantes. 
• Amplia compatibilidad de materiales: 
La longitud de onda permite una gran versatilidad, pudiendo cortar multitud de materiales 
(reflectantes como el aluminio, el cobre o el latón, acero tanto chapas como tubos, etc.). 
• Menores costes de producción: 
Normalmente se elimina la fase del tratamiento de lijado o sellado posterior. 
Además, hay que destacar que el cabezal no pierde propiedades con el uso continuado. 
9.4. Softwares de uso 
La importancia del software de control en esta tecnología es primordial, ya que se puede controlar 
diferentes parámetros, como la potencia, velocidad y frecuencia del haz de luz, hasta los movimientos 
del cabezal o la pieza a cortar. 
Los diseños de corte y grabado en los materiales a cortar (madera, metal…) se plasman por la 
programación el software, y se pueden almacenar los distintos diseños, para aplicarlos cada vez que sea 
necesario, o a partir de un diseño ya creado y guardado, realizar las modificaciones necesarias para 
tener el nuevo diseño requerido. 

<!-- Page 107 -->

 
 
Periféricos: conectividad y administración 
107 
Existen muchos softwares en el mercado, vamos a indicar brevemente los más destacados: 
• Autodesk Autocad: 
• Sobre todo, se utiliza en proyectos de arquitectura, electricistas y mecánica. 
• Compatible con muchos formatos, DWG, DXF, 3DS, WMF, PLT. 
• Destaca su gran precisión en las medidas. 
• Adobe Illustrator: 
• Permite crear gráficos vectoriales. 
• Cuenta con herramientas de dibujo de gran precisión. 
• Gran número de efectos para el diseño. 
• Cuenta con muchos formatos compatibles, AI, PDF, DXF, DWG, SVG,EPS. 
• Simplifica el proceso de corte por láser. 
• Corel Draw: 
• Comparte características con otros editores vectoriales. 
• Su interfaz es sencilla e intuitiva. 
• Inkscape: 
• Disponible para las principales plataformas: Linux, Windows y Mac OS. 
• Compatible con muchos formatos, SVG, PNG, ODD, DXF, SK1, PDF, EPS, POSTSCRIPT…. 
• Archicad de Graphisoft: 
• Software desarrollado para el modelado de edificios. 
• Compatible con PLN, DWG, DXF, EXPORT PDF, 3DS, OBJ… 
10. Colorimetría 
La colorimetría es la ciencia que estudia la medida de los colores y que desarrolla métodos para la 
cuantificación de la percepción del color. 
El matiz es el estado puro del color: rojo, amarillo, azul... 

<!-- Page 108 -->

 
 
Periféricos: conectividad y administración 
108 
La saturación de un color es su grado de pureza. Un color está más saturado cuanto menor sea su 
contenido de grises o de blancos. Los colores de la naturaleza siempre son más o menos saturados. 
La intensidad, o luminosidad de un color, es la característica que hace que este aparezca más claro, 
independientemente de su saturación. 
10.1. Resolución de imágenes 
La resolución de una imagen indica la cantidad de detalles que puede observarse en esta. 
También nos indica la cantidad de nitidez, (como antónimo de granular) en una imagen de fotografía 
convencional (o fotografía química). Es bueno señalar que, si la imagen aparece como granular, se le da 
el nombre de pixelada. 
Tener mayor resolución se traduce en obtener una imagen con más detalle o calidad visual. 
Para las imágenes digitales almacenadas como mapa de bits, la convención es describir la resolución de 
la imagen con dos números enteros, donde el primero es la cantidad de columnas de píxeles (cuántos 
píxeles tiene la imagen a lo ancho) y el segundo es la cantidad de filas de píxeles (cuántos píxeles tiene 
la imagen a lo alto). 
Popularmente se describir el número total de píxeles en la imagen (usualmente expresado como el 
múltiplo correspondiente a millón -mega-), que se calcula multiplicando la cantidad de columnas de 
píxeles en una imagen, por la cantidad de filas. 
Para saber cuál es la resolución de una cámara digital debemos conocer los píxeles de ancho x alto a los 
que es capaz de obtener una imagen. Así una cámara capaz de obtener una imagen de 1600 x 1200 
píxeles, tiene una resolución de 1600x1200=1.920.000 píxeles, es decir 1,92 megapíxeles. 
En cuanto a la resolución de impresión, es decir, los puntos por pulgada (ppp) a los que se puede 
imprimir una imagen digital de calidad. A partir de 200 ppp podemos decir que la resolución de 
impresión es buena, y si queremos asegurarnos, debemos alcanzar los 300 ppp, porque muchas veces la 
óptica de la cámara, la limpieza del objetivo o el procesador de imágenes de la cámara digital, 
disminuyen la calidad. 
Para saber cuál es la resolución de impresión máxima que permite una imagen digital, hay que dividir el 
ancho de esa imagen (por ejemplo, 1600), entre la resolución de impresión 200, 1600/200 = 8 l para 
una foto digital de 1600 píxeles de largo es de 8 pulgadas de largo (20,32 cm) en calidad 200 ppp 
(1600/300=5.33 pulgadas - 13,54 cm - en el caso de una resolución de 300 ppp). Una pulgada equivale 
a 2,54 cm. 

<!-- Page 109 -->

 
 
Periféricos: conectividad y administración 
109 
10.2. Modelos de color 
 
Archivo: Pixel geometry 01 Pengo.jpg - Wikipedia, la 
enciclopedia libre 
Existen diferentes modelos de color que podemos usar dependiendo de nuestras necesidades: RGB, 
CMYK, HSV (HSB). 
10.2.1. RGB 
RGB: sigla en inglés de red, green, blue, en español «rojo, verde y azul» 
(RVA: sigla preferida por la ASALE y la RAE) 
Definimos la composición del color en términos de la intensidad de los colores primarios de la luz: rojo, 
verde y azul. 
RGB está basado en la síntesis aditiva, es posible representar un color mediante la mezcla por adición de 
los tres colores de luz primarios. El modelo de color RGB no define por sí mismo lo que significa 
exactamente rojo, verde o azul, por lo que los mismos valores RGB pueden mostrar colores 
notablemente diferentes en distintos dispositivos que usen este modelo de color. Aunque utilicen un 
mismo modelo de color, sus espacios de color pueden variar considerablemente. 

<!-- Page 110 -->

 
 
Periféricos: conectividad y administración 
110 
10.2.2. CMYK 
CMYK: siglas de Cyan, Magenta, Yellow y Key. 
Es un modelo de color sustractivo que se utiliza en la impresión en colores. Es la versión moderna y más 
precisa del antiguo modelo tradicional de coloración (RYB), que se utiliza todavía en pintura y artes 
plásticas. Permite representar una gama de colores más amplia que este último, y tiene una mejor 
adaptación a los medios industriales. 
Este modelo se basa en la mezcla de pigmentos de los siguientes colores para crear otros más: 
La mezcla de colores CMY ideales es sustractiva (puesto que la mezcla de cian, magenta y amarillo en 
fondo blanco resulta en el color negro). El modelo CMYK se basa en la absorción de la luz. El color que 
presenta un objeto corresponde a la parte de la luz que incide sobre este y que no es absorbida por el 
objeto. 
El cian es el opuesto al rojo, lo que significa que actúa como un filtro que absorbe dicho color (-R +G +B). 
Magenta es el opuesto al verde (+R -G +B) y amarillo el opuesto al azul (+R +G -B). 
10.2.3. HSV (HSB) 
Define un color en base a los componentes; Matiz, Saturación y Brillo. 
HSV: del inglés Hue, Saturation, Value – Matiz, Saturación, Valor) 
HSB (Hue, Saturation, Brightness – Matiz, Saturación, Brillo) 
Para elegir un color adecuado en una aplicación, resulta muy útil usar la ruleta de color HSV. 
En ella el matiz se representa por una región circular; una región triangular separada, puede ser usada 
para representar la saturación y el valor del color. Normalmente, el eje horizontal del triángulo denota la 
saturación, mientras que el eje vertical corresponde al valor del color. De este modo, un color puede ser 
elegido al tomar primero el matiz de una región circular, y después seleccionar la saturación y el valor 
(brillo) del color deseado de la región triangular. 
10.3. Profundidad de color 
La profundidad de color o bits por píxel (bpp), se refiere a la cantidad de bits de información necesarios 
para representar el color de un píxel en una imagen digital (o en un framebuffer). 
Puesto que la informática utiliza el sistema binario de numeración, una profundidad de bits de n implica 
que cada píxel de la imagen puede tener 2n posibles valores y, por lo tanto, representar 2n colores 
distintos. 

<!-- Page 111 -->

 
 
Periféricos: conectividad y administración 
111 
Basándonos en los octetos de 8 bits, como unidades básicas de información, en los dispositivos de 
almacenamiento, los valores de profundidad de color suelen ser divisores o múltiplos de 8: 1, 2, 4, 8, 16, 
24 y 32, (con la excepción de la profundidad de color de 10 o 15, usada por ciertos dispositivos gráficos). 
En profundidades de color inferiores o iguales a 8, los valores de los píxeles hacen referencia a tonos 
RGB indexados en una tabla, (caja creadora de colorización o paleta; proceso mediante el cual un objeto 
o espacio es coloreado. Significará un proceso diferente de desgaste o de alteración de la superficie). 
Los tonos en dicha tabla pueden ser definidos por convención o bien ser configurables, en función de la 
aplicación que la defina. 
Vamos a ver algunas profundidades de color en la gama baja, la cantidad de tonos que pueden 
representar en cada pixel y el nombre que se les otorga a las imágenes o framebuffers que los soportan. 
• 1 bit por píxel: 21 = 2 colores, también llamado monocromo o blanco y negro. 
• 2 bits por píxel: 22 = 4 colores, o CGA. 
• 3 bits por píxel: 23 = 8 colores. (Primeros modelos de ordenador doméstico como el ZX 
Spectrum y el BBC Micro). 
• 4 bits por píxel: 24 = 16 colores, la cual es la mínima profundidad aceptada por el estándar EGA. 
Macintosh en color, Atari ST, Commodore 64, Amstrad CPC, MSX2. 
• 5 bits por píxel: 25 = 32 colores, como en el chipset original del Commodore Amiga. 
• 6 bits por píxel: 26 = 64 colores. 
• 8 bits por píxel: 28 = 256 colores, también llamado VGA. Super VGA. 
• 9 bits por píxel: 29 = 512 colores, también llamado Ultra VGA. 
• 10 bits por pixel: 210 = 1024 colores, usado en UHDTV. 
• 12 bits por pixel: 212 = 4096 colores, algunos modelos de Silicon Graphics, NeXTstation en color, 
modo HAM del Commodore Amiga. 
11. Bibliografía 
• PRIETO ESPINOSA, A. Introducción a la informática. 
• BEEKMAN, G. Introducción a la informática. 
• https://definicion.de/. 
• https://topbateriaexterna.com/usb-tipo-c/. 
• https://en.wikipedia.org/. 

<!-- Page 112 -->

 
 
Periféricos: conectividad y administración 
112 
• https://es.wikipedia.or. 
• https://www.apple.com/es/thunderbolt/. 
• https://www.tiposde.com. 
• http://www.mfbarcell.es/docencia_uned/so/tema_06/tema6.pdf. 
• https://www.uv.es/varnau/AEC_2011-12.htm. 
• http://www.informaticamoderna.com. 
• https://computerhoy.com. 
• https://es.ccm.net/. 
• http://knowledge.seagate.com. 
• https://blog.irontec.com/. 
• https://www.aboutespanol.com. 
• https://www.tecnonauta.com. 
• https://www.androidsis.com/. 
• https://es.wikiversity.org/wiki/Sistemas_de_almacenamiento. 
• https://www.ionos.es/digitalguide/servidores/know-how/server-message-block-smb/. 
• http://es.wikipedia.org/wiki/Canal_de_fibra. 
• http://es.wikipedia.org/wiki/Small_Computer_System_Interface. 
• https://www.profesionalreview.com/2018/11/26/conector-sata/. 
• https://elpuig.xeill.net/Members/vcarceler/c1/didactica/apuntes/ud4/na3. 
• https://en.wikipedia.org/wiki/Data_striping. 
• NTFS - Wikipedia, la enciclopedia libre. 
• Macintosh File System - Wikipedia, la enciclopedia libre. 
• Hierarchical File System - Wikipedia, la enciclopedia libre. 
• Formatos del sistema de archivos disponibles en Utilidad de Discos en el Mac - Soporte técnico 
de Apple.

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|Ficha Resumen del Tema 02]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque2-tema02|Nota Fuente Oficial del Tema 02]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema02-perifericos-interfaces|Test Tema 02]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Flashcards Bloque 2]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema01|⬅️ Tema Completo 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/temas-completos/bloque-2-hardware-so/tema-completo-bloque2-tema03|Tema Completo 03 ➡️]]
