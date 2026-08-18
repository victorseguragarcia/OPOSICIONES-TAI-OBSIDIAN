---
title: "Tema Completo Extendido 06 (Bloque 4): Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-4
  - tema-06
  - oposiciones-tai\nestado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque4-tema06.md]]"
  - "[[wiki/sources/bloque4-tema06]]"
created: "2026-08-18"
updated: "2026-08-18"
---
> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema05|⬅️ Tema Completo 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema07|Tema Completo 07 ➡️]]

# 🔴 Tema Completo Extendido 06 (Bloque 4): 

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 06 correspondiente al Bloque 4 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Comunicaciones
La comunicación consiste en el intercambio o compartición de información. 
 
 
 
 
 
 
Existen muchas clasificaciones de comunicación, pero quizás la más básica sea: 
- Comunicación local.
Se producen cara a cara. 
Ejemplo: dos personas hablando. 
- Comunicación remota.
Se producen a través de la distancia, y se denomina telecomunicación. 
Ejemplos: Teléfono, Telégrafo, Televisión. 
Para realizar una comunicación hay que realizar una transmisión de datos, que es el intercambio de 
datos entre dos dispositivos a través de algún medio de transmisión (Por ejemplo, cable). 
 
 
 
 
+ Info 
Para que la transmisión de datos sea posible, un sistema de 
comunicación debe estar formado por hardware (equipo físico) y 
software (programas).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 1.1. Efectividad de la comunicación
La efectividad del sistema de comunicación de datos depende de cuatro características fundamentales: 
1. Entrega. 
El sistema debe entregar los datos en el destino correcto. 
Los datos deben ser recibidos por el dispositivo o usuario adecuado y solamente por ese 
dispositivo o usuario. 
2. Exactitud. 
El sistema debe entregar los datos con exactitud. 
Los datos que se alteran en la transmisión son incorrectos y no se pueden utilizar. 
3. Puntualidad. 
El sistema debe entregar los datos con puntualidad. 
Los datos entregados tarde son inútiles. 
4. Jitter (retardo variable). 
No todos los datos tardan exactamente lo mismo en ser recibidos. 
Por ejemplo, uno podría llegar en 10ms y otro en 15ms. 
Un jitter alto repercutiría en una mala calidad de transmisión (por ejemplo, de video). 
 
 
 
 
+ Info 
La transmisión en tiempo real consiste en la entrega de datos de 
vídeo, audio y voz de forma puntual, entregando los datos a 
medida que se producen, en el orden que se producen y sin un 
retardo significativo.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 1.2. Componentes de la comunicación
Un sistema de transmisión de datos está formado por cinco componentes básicos: 
1. Mensaje. 
El mensaje es la información (datos) a comunicar. 
Los formatos más populares son texto, gráficos, audio y vídeo. 
2. Emisor. 
El emisor es la persona o dispositivo que envía el mensaje. 
Puede ser un ordenador, un teléfono, una persona, etc. 
3. Receptor. 
El receptor es la persona o dispositivo que recibe el mensaje. 
Puede ser un ordenador, una televisión, una persona, etc. 
4. Medio. 
El medio de transmisión es el camino físico por el cual viaja el mensaje desde el emisor hasta el 
receptor. 
Puede estar formado por un cable de par trenzado, un cable coaxial, un cable de fibra óptica o 
por ondas de radio. 
5. Protocolo. 
Un protocolo es un conjunto de reglas que gobiernan la transmisión de datos. Sin un protocolo, 
dos dispositivos pueden estar conectados, pero no pueden comunicarse. 
Representa un acuerdo entre los dispositivos que se comunican. 
Ejemplo: una persona que hable chino puede hablar con una persona que habla español, pero no 
se podrán comunicar, no se entenderán. 
 
Componentes de un sistema de transmisión de datos

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 1.3. Estándares y organizaciones de estandarización
Los estándares son esenciales para garantizar la interoperabilidad nacional e internacional de los datos, 
la tecnología y los procesos de telecomunicaciones. 
Proporcionan guías a los fabricantes, vendedores, agencias del gobierno y otros proveedores de 
servicios, para asegurar la interconectividad de sus productos o servicios. 
Los estándares son desarrollados mediante Organizadores de Estandarización, con la cooperación \nentre: 
- Comités de creación de estándares.
- Foros.
- Agencias reguladoras de los gobiernos.
### 🔵 Comités de creación de estándares 
Hay muchas organizaciones que se dedican a la definición y establecimiento de estándares para datos y 
comunicaciones. 
Sin embargo, se confía fundamentalmente en los siguientes: 
- The International Organization for Standardization (ISO).
El ISO es un organismo multinacional cuyos miembros provienen fundamentalmente de los 
comités de creación de estándares de varios gobiernos a lo largo del mundo. 
El ISO es activo en el desarrollo de la cooperación en los ámbitos científicos, tecnológicos y de 
las actividades económicas. 
- The International Telecommunications Union-Telecommunication Standards Sector (ITU-T).
Al principio, los países estaban definiendo estándares nacionales para telecomunicaciones, por 
lo que había problemas de compatibilidad internacional. 
Para solucionarlo, las Naciones Unidas el Comité Consultivo para la Telefonía y la Telegrafía 
Internacional (CCITT), el cual formaba parte de la Unión Internacional de Telecomunicaciones 
(ITU). 
Este comité estaba dedicado al desarrollo y establecimiento de estándares para 
telecomunicaciones (especialmente para telefonía y comunicación de datos). 
Posteriormente, el nombre de este comité se cambió a Unión Internacional de 
Telecomunicaciones-Sector de Estándares de Telecomunicaciones (ITU-T).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- The American National Standards Institute (ANSI).
El Instituto Nacional Americano para la Estandarización (ANSI) es una corporación privada sin 
ánimo de lucro que no tiene ninguna relación con el gobierno de Estados Unidos. 
- The Institute of Electrical and Electronics Engineers (IEEE).
El Instituto de Ingenieros Eléctricos y Electrónicos (IEEE, Institute of Electrical and Electronics 
Engineering) es la mayor sociedad profesional de ingeniería del mundo. 
De ámbito internacional, sus objetivos son el desarrollo de la teoría, la creatividad y la calidad de 
los productos en el campo de la ingeniería eléctrica, la electrónica y la radio, así como otras 
ramas relacionadas de la ingeniería. 
Como uno de sus objetivos principales, el IEEE prevé el desarrollo y adopción de estándares 
internacionales para computación y comunicación. 
- The Electronic Industries Association (EIA).
Es una organización sin ánimo de lucro dedicada a la promoción de aspectos de la fabricación \nelectrónica. 
En el campo de la tecnología de la información, la EIA ha hecho contribuciones significativas 
mediante la definición de interfaces de conexión física y de especificaciones de señalización \neléctrica para la comunicación de datos. 
### 🔵 Foros 
El desarrollo de la tecnología de las telecomunicaciones se está produciendo más rápidamente que lo 
que permite la habilidad de los comités de estandarización para ratificar los estándares. 
Los comités de estandarización son organizaciones procedimentales y actúan lentamente por 
naturaleza. 
Para acomodar la necesidad de tener modelos de trabajo y acuerdos y facilitar los procesos de \nestandarización, muchos grupos de interés especial han desarrollado foros compuestos por miembros 
que representan a las empresas interesadas. 
Los foros trabajan con las universidades y los usuarios para probar, evaluar y estandarizar nuevas 
tecnologías. 
Concentrando sus esfuerzos en una tecnología en particular, los foros son capaces de acelerar la 
aceptación y el uso de esa tecnología en la comunidad de las telecomunicaciones. 
Los foros presentan sus conclusiones a los organismos de estandarización.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Agencias reguladoras 
Toda la tecnología de comunicaciones está sujeta a regulación por las agencias del gobierno (por \nejemplo, la Comisión Federal de Comunicaciones (FCC) en Estados Unidos). 
El objetivo de estas agencias es proteger el interés público mediante la regulación de la radio, la 
televisión y las comunicaciones por cable. 
Tecnologías de Información y Comunicaciones (TIC). Normativas 
Las TICs, son todas las tecnologías que nos permiten acceder, producir, guardar, presentar y transferir 
información. Ellas están en todos los ámbitos de nuestras vidas, en nuestra vida social, familiar y escolar. 
Sus usos son ilimitados y pueden manejarse con facilidad, sin necesidad de ser un experto. 
 
 
 
 
### 🔵 Ejemplo 
Televisores, teléfonos celulares, computadores, radios, 
reproductores de audio y video, consolas de videojuegos, tabletas \ne Internet. 
 
 
Su utilización es diversa, para divertirnos, aprender, mantenernos en contacto, saber lo que está 
sucediendo en el mundo, dar nuestra opinión y conocer lo que los demás opinan, etc. 
Con ellas las distancias se disminuyen, la comunicación y el intercambio de información se hacen cada 
vez más rápidos y eficientes. 
Gracias a las TIC, infinidad de cosas diferentes están a una distancia tan solo de un clic de nuestro ratón, 
como videos y películas, música, videojuegos, los amigos, noticias, el conocimiento y el mundo entero. 
RD 1112/2018 
El 21 de diciembre de 2018, la Comisión Europea publicó la Decisión de Ejecución (UE) 2018/2048 de 
la Comisión, de 20 de diciembre de 2018, sobre la norma armonizada aplicable a los sitios web y a las 
aplicaciones para dispositivos móviles. Redactada en apoyo de la Directiva (UE) 2016/2102 del 
Parlamento Europeo y del Consejo. Esta decisión se aplica al contexto español a través del RD 
1112/2018.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Con la publicación de esta decisión se establece: 
- Que el estándar de aplicación para el cumplimiento de los requisitos es la norma "EN 301 549
V2.1.2 (2018-08): Requisitos de accesibilidad para productos y servicios TIC". 
En su versión española se materializa en la norma UNE-EN 301-549:2019, de Requisitos de 
accesibilidad de productos y servicios TIC. 
Con esta norma se pretende ayudar tanto a los desarrolladores y evaluadores de aplicaciones 
móviles y páginas web en materia de accesibilidad, como a las personas encargadas de realizar 
las evaluaciones de accesibilidad, normalmente auditores o consultores que velan por el 
cumplimiento de los requisitos de accesibilidad. 
### 🔵 Estándar de Internet 
Es una especificación concienzudamente probada a la que se adhieren aquellos que trabajan en 
Internet. 
Es una regulación formalizada que debe ser seguida. 
Para que una especificación obtenga el estatus de estándar de internet debe seguir un estricto 
procedimiento. 
Los estándares se pueden clasificar en dos categorías: de facto ("de hecho" o "por convención") y de 
jure ("por ley" o "por regulación"). 
- De facto.
Son estándares que no han sido aprobados por un cuerpo organizado, pero han sido adoptados 
como estándares por su gran difusión. 
- De jure.
Estándares que han sido legislados por un organismo oficialmente reconocido. 
## 🟣 2. Modos de comunicación
Dependiendo de cómo realicemos una comunicación, una transmisión de datos, podemos tener 
diferentes modos. 
### 🔵 2.1. Multiplexación
Es el conjunto de técnicas que permite la transmisión simultánea de múltiples señales (canales) a través 
de un único enlace de datos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
En toda transmisión multiplexada se necesita: 
- Un multiplexor en el transmisor.
- Un demultiplexor en el receptor.
Hay tres técnicas de multiplexación, por división en Frecuencias (FDM), de Onda (WDM), y en el 
tiempo (TDM): 
- FDM (Multiplexación por División en Frecuencias).
Normalmente se usa para señales analógicas. 
Se puede aplicar cuando el ancho de banda de un enlace es mayor que los anchos de banda 
combinados de la señal a transmitir. 
Se usan distintas frecuencias portadoras para transmitir (que no deben interferir con las 
frecuencias de los datos originales). 
Se usan bandas de seguridad. 
 
- WDM (Multiplexación por División de Onda).
Conceptualmente igual que FDM, pero la multiplexación y demultiplexación se aplica a señales 
luminosas a través de fibra óptica. 
 
- TDM (Multiplexación por División en el Tiempo).
Se utiliza normalmente para señales digitales. 
Se puede aplicar cuando la capacidad de tasa de datos de la transmisión es mayor que la tasa de 
datos necesaria requerida por los dispositivos transmisores y receptores.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Se divide el enlace en el tiempo y no en frecuencia. 
Tipos: 
- Síncrona.
» El multiplexor siempre asigna exactamente la misma ranura de tiempo para cada 
dispositivo, independientemente de que los dispositivos tengan o no que transmitir. 
- Asíncrona o estadística.
» El multiplexor usa reserva dinámica bajo demanda de las ranuras. 
» Puede dar más servicios que la síncrona. 
 
### 🔵 2.2. Modulación
Para las telecomunicaciones, la modulación son aquellas técnicas que se aplican en el transporte de 
datos sobre ondas portadoras. 
Gracias a estas técnicas, es posible aprovechar el canal comunicativo de la mejor manera para transmitir 
un mayor caudal de datos de manera simultánea. 
La modulación contribuye a proteger la señal de interferencias y ruidos. 
El proceso de modulación consiste en variar un parámetro que está en la onda portadora en función de 
las alteraciones de la señal moduladora. 
Se aprovecha mejor el espectro electromagnético, ya que permite la multiplexación por frecuencias. 
Demodulación es el proceso inverso a la modulación. 
Consiste en recuperar la señal de datos de una señal modulada. 
Según el sistema de transmisión tenemos diferentes tipos de modulación: 
Tipos de Modulación según el sistema de transmisión 
- Señal portadora y moduladora son analógicas:
- Modulación de amplitud, AM.
- Modulación de frecuencia, FM.
- Modulación de fase, PM.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Señal portadora analógica y moduladora digital:
- Desplazamiento de amplitud, ASK.
- Desplazamiento de frecuencia, FSK.
- Desplazamiento de fase, PSK.
- Señal portadora digital y moduladora analógica:
- Modulación por amplitud de pulsos PAM.
- Modulación de pulsos en duración (PDM).
- Modulación de pulsos en posición (PPM).
- Modulación por codificación de pulsos PCM.
- Modulación por anchura de pulso (PWM).
- Modulación Delta.
- Señal portadora digital y moduladora digital:
En este caso no es necesaria la modulación. 
### 🔵 2.3. Clasificación según el flujo de datos
Dependiendo del flujo de datos, tenemos: 
- Comunicación UniCast.
Puede ser: 
- Simplex.
- Semi-Dúplex.
- Dúplex o Full-Duplex.
- Comunicación MultiCast.
- Comunicación BroadCast.
- Comunicación AnyCast.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
#### 🔹 2.3.1. UniCast
 
Fuente: (https://es.m.wikipedia.org/wiki/Archivo:Unicast.svg) 
La comunicación unicast es una comunicación uno a uno o punto a punto. 
Se puede utilizar para aplicaciones cliente/servidor en las que hay un solo emisor y un solo receptor. 
Estas comunicaciones están principalmente dirigidas por el emisor de datos, el cual conoce la dirección 
IP del receptor. 
Por lo tanto, los paquetes unicast usan la dirección del dispositivo de destino para la entrega de los 
datos. 
Estos datos pueden pasar por una interconexión de redes (no tienen por qué estar conectados 
directamente por un único cable). 
Este tipo de comunicación es la forma más común y eficiente de la comunicación entre dos nodos. 
Dependiendo de la dirección de la comunicación, existen 3 tipos de comunicación entre dos 
dispositivos: Simplex, Semi-Dúplex y Dúplex. 
##### 2.3.1.1. Simplex
La comunicación es unidireccional. 
Solamente una de las dos estaciones de enlace puede transmitir; la otra sólo puede recibir. 
Ejemplos: 
- Emisor simplex:
- Teclado, y Ratón.
- Mando a distancia de un televisor.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Receptor simplex:
- Impresora.
- Escáner.
- Receptor de radio.
- Televisión común (sin smartTV).
El modo simplex puede usar toda la capacidad del canal para enviar datos en una dirección. 
 
Comunicación Simplex 
##### 2.3.1.2. Semi-dúplex
Cada estación puede enviar y recibir, pero no al mismo tiempo. 
Cuando un dispositivo está enviando, el otro sólo puede recibir, y viceversa. 
En la transmisión semi-dúplex, la capacidad total del canal es usada por el dispositivo que está 
transmitiendo. 
Ejemplos: 
- Walkie-talkies.
- Radios de banda civil o policiaca.
- Cajero automático.
Toda la capacidad del canal la usa el emisor. 
 
Comunicación Semi-Dúplex

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
##### 2.3.1.3. Dúplex o Full-dúplex
En el modo dúplex ambas estaciones pueden enviar y recibir simultáneamente. 
Esto se puede conseguir de dos formas: 
- Usar dos caminos separados físicamente (por ejemplo, dos cables).
- Utilizando distintas frecuencias (multiplexación de frecuencias).
Se divide la capacidad del canal. 
Ejemplos: 
- Teléfono.
- Dispositivo Bluetooth.
- Dos ordenadores conectados en red.
 
Comunicación Full-Dúplex o Dúplex 
#### 🔹 2.3.2. MultiCast
 
Fuente: (https://es.m.wikipedia.org/wiki/Archivo:Multicast.svg) 
Las comunicaciones multicast permiten el envío de datos desde un emisor a muchos receptores (uno-a-
muchos), o desde muchos emisores a muchos receptores (muchos-a-muchos) si la gestión de los 
grupos se realiza de forma adecuada. 
En la actualidad los conmutadores que conectan los nodos de una red tienen soporte para administrar 
los grupos multicast.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Estos grupos multicast pueden crecer o disminuir dinámicamente. 
Los nodos se unen (join) a un grupo multicast si están interesados en recibir tráfico dirigido a la 
dirección multicast de dicho grupo y lo deja (leave) cuando dejan de estar interesados. 
El Internet Group Management Protocol (IGMP) permite llevar a cabo la comunicación entre los nodos 
y los conmutadores de la red. 
#### 🔹 2.3.3. BroadCast
 
Fuente: (https://commons.wikimedia.org/wiki/File:Broadcast.svg) 
La comunicación broadcast es comparable con la comunicación multicast ya que existe un solo emisor. 
En cambio, con broadcast un solo mensaje se entrega a todos los potenciales receptores (por ejemplo, \nen una subred), mientras que con multicast solo lo reciben los nodos interesados en el tráfico. 
La manera más común de lograr la comunicación broadcast es utilizar una dirección de difusión \nespecial, en la cual se indica al mecanismo de comunicación que el mensaje debe ser entregado a todos 
los nodos de la subred. 
Al enviar un mensaje broadcast, el emisor no necesita conocer el número de receptores. 
Broadcast es menos eficiente porque ocupa más infraestructura de la red al enviarlo a todos los nodos 
quieran o no quieran los datos. 
Un claro ejemplo del uso de broadcast se puede encontrar en el protocolo de resolución de direcciones 
o Address Resolution Protocol (ARP).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
#### 🔹 2.3.4. AnyCast
 
Fuente: (https://commons.wikimedia.org/wiki/File:Anycast.svg) 
Anycast es una forma de direccionamiento o enrutamiento en la que la información es encaminada al 
mejor destino desde el punto de vista de la topología de la red. 
En la red internet, una dirección IP se puede anunciar desde varios puntos diferentes. 
Los enrutadores intermedios encaminan el paquete hasta el destino más cercano. 
Un paquete enviado a una dirección anycast es entregado a la máquina más próxima desde el punto de 
vista del tiempo de latencia. 
En Anycast, el paquete solo lo recibe un nodo. 
### 🔵 2.4. Clasificación según el número de bits transmitidos por ciclo de reloj 
La transmisión de datos binarios por un enlace se puede llevar a cabo en dos modos: 
- Modo paralelo.
Se envían varios bits por cada pulso de reloj. 
- Modo serie.
Solamente se envía un bit con cada pulso de reloj. Hay tres tipos de transmisiones serie: 
- Síncrona.
- Asíncrona.
- Isócrona.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
#### 🔹 2.4.1. Transmisión paralela
Los datos binarios (formados por unos y ceros) se organizan en grupos de n bits. 
- (Los ordenadores producen y consumen datos en grupos de bits.)
Agrupando los datos podemos enviar n bits al mismo tiempo en lugar de 1. 
El mecanismo es sencillo: 
- Consiste en usar n hilos para enviar n bits cada vez.
- Cada bit tiene su propio hilo y los n bits de un grupo se pueden transmitir en un pulso de reloj de un dispositivo a otro. 
- Normalmente, los n hilos están agrupados en un cable con un conector a cada extremo.
Ventaja: Aumenta la velocidad de transferencia n veces frente a la transmisión en serie. 
Desventaja: Coste superior ya que requiere n líneas de comunicación. 
Debido al alto coste se utiliza solo en distancias cortas. 
 
Transmisión paralela de 8 bits 
#### 🔹 2.4.2. Transmisión serie
En este tipo de transmisión, un bit sigue a otro, por lo que solo necesita un canal de comunicación (en 
lugar de n) para transmitir datos entre dispositivos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
### 🔵 Transmisión serie 
Ventaja: Al tener un único canal de comunicación, el coste es n veces inferior a las paralelas. 
Desventaja: Dado que los equipos producen y consumen datos en grupos de bits, necesitaremos 
dispositivos de conversión: 
- Paralelo a serie en la interfaz entre emisor y la línea de comunicación.
- Serie a paralelo en la interfaz entre la línea de comunicación y el receptor.
La transmisión serie puede llevase a cabo de tres maneras: Asíncrona, Síncrona e Isócrona. 
##### 2.4.2.1. Transmisión asíncrona
En la transmisión asíncrona, la temporización de la señal no es importante. 
La información se recibe y se traduce usando unos patrones acordados basados en la agrupación el flujo 
de bits en bytes. 
Cada grupo (habitualmente 8 bits) se envía como una unidad. 
El sistema que lo envía gestiona cada grupo independientemente, entregándolo al enlace en cuanto \nestá listo. 
El receptor no sabe cuándo va a llegar el grupo siguiente. 
Para avisar al receptor de la llegada de un nuevo grupo se añade un bit extra al principio de cada byte 
(habitualmente un cero) denominado bit de inicio. 
Para avisar al receptor de que grupo de bits ha terminado, se añaden uno o varios bits adicionales 
(normalmente unos) al final denominados bits de parada. 
Usando este método estamos aumentando el tamaño del grupo de bits al menos en dos unidades.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Además, la transmisión de cada grupo de bits puede ir seguida de un intervalo de duración variable. 
Este modo es asíncrono a nivel de grupo de n bits, pero la recepción de bits de un grupo debe tener 
algún tipo de temporizador que permita recibir los bits de forma sincronizada. 
Cuando el dispositivo receptor detecta un bit de inicio, activa un temporizador y comienza a contar los 
bits a medida que llegan. 
Después de contar n bits, el receptor busca un bit de parada. Al detectarlo, ignora cualquier pulso 
recibido hasta que vuelve a detectar un nuevo bit de inicio. 
Desventaja: Se debe añadir información extra (bit de inicio, bits de parada y un intervalo entre grupos 
de bits). Por lo tanto, la comunicación es más lenta. 
Ventajas: Es más barata y es más efectiva. Ideal para comunicaciones de baja velocidad. Ejemplo: 
conexión entre un ordenador y el teclado. 
 
Transmisión asíncrona 
##### 2.4.2.2. Transmisión síncrona
En la transmisión síncrona, se envía un bit detrás de otro (sin bits de inicio/parada o intervalos). 
Es responsabilidad del receptor agrupar los bits. 
 
Transmisión síncrona

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Aunque en la figura se han incluido divisiones entre los bytes, en realidad estas divisiones no existen. 
El emisor puede enviar los datos en ráfagas separadas. Los intervalos entre ráfagas se deben rellenar 
con una secuencia especial que indican vacío. 
El receptor cuenta los bits a medida que llega y los agrupa en unidades de n bits. 
En este caso la temporización es muy importante, ya que la exactitud de la información recibida 
depende de la habilidad del receptor de llevar exactamente la cuenta de los bits a medida que llegan. 
Ventaja: Mayor velocidad al no haber bits extra ni intervalos. 
La transmisión síncrona es útil para aplicaciones de alta velocidad como la transmisión de datos \nentre dos ordenadores. 
 
 
 
+ Info 
Debemos tener en cuenta que, aunque no hay intervalos entre 
grupos de bits, sí que puede haber intervalos desiguales entre 
tramas. 
 
##### 2.4.2.3. Transmisión isócrona
En vídeo y audio en tiempo real no podemos utilizar transmisión síncrona dado que lo importante es no 
tener retardos desiguales entre tramas. 
Ejemplo: Si las imágenes de TV se difunden a una tasa de 50 imágenes por segundo, estas imágenes 
deben ser visualizadas en la misma tasa. 
La transmisión isócrona garantiza que los datos llegan a una tasa fija sincronizando el flujo entero de 
bits. 
 
Transmisión isócrona

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
3. 
### 🔵 Los 
Un medio de transmisión es el medio físico a través del cual viaja la señal desde el Transmisor hasta el 
Receptor. 
### 🔵 3.1. Tipos de transmisión según el medio utilizado
Dependiendo de la vía de transmisión utilizada, se clasifican en 2 tipos: 
- Guiados o alámbricos.
- No Guiados o inalámbricos.
#### 🔹 3.1.1. Tecnología Ethernet
Ethernet es la tecnología de red más utilizada en la actualidad para la interconexión de dispositivos 
dentro de redes locales (LAN). Desde su creación en la década de 1970, ha evolucionado 
significativamente, aumentando su velocidad y eficiencia. 
Las tecnologías Ethernet se clasifican según su velocidad de transmisión y el tipo de medio de 
transmisión utilizado. La tecnología se ha ido adaptando a las necesidades de las redes modernas, desde 
implementaciones domésticas hasta infraestructuras de alta velocidad en centros de datos. 
La elección de la tecnología dependerá de la infraestructura disponible, el presupuesto y las necesidades 
de rendimiento, como la latencia, la velocidad de transmisión y la escalabilidad. El medio de transmisión 
se seleccionará en función de estos criterios, pudiendo ser cableado (cobre, fibra óptica) o inalámbrico 
(Wi-Fi, 5G, Bluetooth, LoRa). Los factores a evaluar incluirán la velocidad, la seguridad, la interferencia 
(ruido) y la distancia de transmisión. 
Ethernet (10Mbs) 
Primera versión de Ethernet, desarrollada en los años 70. 10 Mbps (megabits por segundo). Se utiliza \nen redes antiguas y conexiones básicas. 
Estándar: IEEE 802.3. 
Cableado: 
- Par trenzado (CAT 3 o superior).
- Cable Coaxial.
- Fibra óptica (en implementaciones específicas).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Fast Ethernet (100 Mbps) 
Evolución de Ethernet que permitió aumentar la velocidad a 100 Mbps. 100 Mbps. Se usa en redes 
locales empresariales y domésticas durante los años 90 y 2000. 
Estándar: IEEE 802.3u. 
Cableado: 
- Par trenzado (CAT 5 o superior).
- Fibra óptica (100BASE-FX).
Gigabit Ethernet (1 Gbps) 
Permite alcanzar 1 Gbps, siendo el estándar predominante en redes modernas. 1 Gbps (1.000 Mbps). 
Se usa en redes empresariales, centros de datos y conexiones domésticas avanzadas. 
Estándar: IEEE 802.3ab (cobre), IEEE 802.3z (fibra óptica). 
Cableado: 
- Par trenzado (Cat 5e, Cat 6 o superior) - 1000BASE-T.
- Fibra óptica multimodo (1000BASE-SX) - hasta 550 metros.
- Fibra óptica monomodo (1000BASE-LX) - hasta 5 km o más.
10 Gigabit Ethernet (10 Gbps) 
Multiplica por diez la velocidad de Gigabit Ethernet, mejorando el rendimiento en redes de alta 
demanda. 10 Gbps. Se usa en centros de datos, redes de almacenamiento (SAN) y conexiones de alta 
velocidad. 
Estándar: IEEE 802.3ae. 
Cableado: 
- Par trenzado (CAT 6A o superior) - 10GBASE-T (hasta 100 metros).
- Fibra óptica multimodo (10GBASE-SR) - hasta 300 metros.
- Fibra óptica monomodo (10GBASE-LR) - hasta 10 km.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
40 Gigabit Ethernet (40 Gbps) y 100 Gigabit Ethernet (100 Gbps) 
Tecnologías diseñadas para infraestructura de redes de alto rendimiento, como interconexiones en 
centros de datos. 40 Gbps (40.000 Mbps), 100 Gbps (100.000 Mbps). Se usa en redes troncales de alta 
velocidad en entornos empresariales y proveedores de servicios. 
Estándar: IEEE 802.3ba. 
Cableado: 
- Fibra óptica multimodo (40GBASE-SR4) - hasta 150 metros.
- Fibra óptica monomodo (40GBASE-LR4 y 100GBASE-LR4) - hasta 10 km.
Ethernet 400G y 800G 
Últimos avances en Ethernet para satisfacer las necesidades de redes masivas y computación en la 
nube. 400 Gbps (400.000 Mbps), 800 Gbps (800.000 Mbps). Se usa en grandes centros de datos, 
inteligencia artificial y redes de hiperescala. 
Estándar: IEEE 802.3bs, IEEE 802.3ck. 
Cableado: 
- Fibra óptica monomodo avanzada.
#### 🔹 3.1.2. Guiados o alámbricos
Es el que brinda un camino que conduce la señal de emisor a receptor. Normalmente son medios 
cableados. 
Los principales son: 
- Par trenzado.
- Coaxial.
- Fibra óptica.
##### 3.1.2.1. Par trenzado
El cable de par trenzado consiste en grupos de hilos de cobre entrelazados en pares en forma helicoidal. 
Esto se hace porque dos alambres paralelos constituyen una antena simple.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Cuando se entrelazan los alambres helicoidalmente, las ondas se cancelan, por lo que la interferencia 
producida por los mismos es reducida lo que permite una mejor transmisión de datos. 
Es actualmente el tipo de cable más común en redes de área local. 
Se originó como solución para conectar redes de comunicaciones reutilizando el cableado existente de 
redes telefónicas. 
 
 
 
 
+ Info 
- Los cables de telefonía tenían dos pares.
- En España, esos pares ni siquiera iban trenzados.
 
 
El cable típico en las redes de área local y en la conexión final de equipos es el de 4 pares. 
Los cables llamados multipar pueden tener 25, 50, 100, 200 y 300 pares. 
Las normativas de cableado estructurado clasifican los diferentes tipos de cable de pares trenzados en 
categorías de acuerdo con sus características para la transmisión de datos. 
Estas dependen fundamentalmente de dos factores: 
- La densidad de trenzado del cable (número de vueltas por metro).
- Los materiales utilizados en el recubrimiento aislante.
La característica principal de un cable desde el punto de vista de transmisión de datos es su atenuación. 
En la actualidad hay definidas 10 categorías (algunas aún en fase de desarrollo) y algunas más que son 
mejoras de una determinada categoría. Las más importantes actualmente son: 
- Categoría 5:
- Ancho de banda: 100 MHz Clase D.
- Aplicaciones: Ethernet 10BASE-T y 100BASE-TX.
- Tipo de cable: UTP/STP.
- Conector: RJ45/RJ49.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Categoría 5e:
- Ancho de banda: 100 MHz Clase D.
- Aplicaciones: Ethernet 100BASE-TX y 1000BASE-T.
- Tipo de cable: UTP/STP.
- Conector: RJ45/RJ49.
- Es una mejora del cable Categoría 5.
- Categoría 6:
- Ancho de banda: 250 MHz Clase E.
- Aplicaciones: Ethernet 1000BASE-T.
- Tipo de cable: UTP/STP.
- Conector: RJ45/RJ49.
- Categoría 6a:
- Ancho de banda: 500 MHz Clase E.
- Aplicaciones: Ethernet 10GBASE-T.
- Tipo de cable: UTP/STP.
- Conector: RJ45/RJ49.
- Categoría 7:
- Ancho de banda: 600 MHz Clase F.
- Aplicaciones: Servicios de telefonía, televisión por cable y Ethernet 1000BASE-T en el mismo cable. 
- Tipo de cable: U/FTP (sin blindaje).
- Conector: GG-45 (compatible con RJ45), TERA.
- Categoría 7a:
- Ancho de banda: 1000 MHz Clase F.
- Aplicaciones: Servicios de telefonía, televisión por cable y Ethernet 1000BASE-T en el mismo cable.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Cable S/FTP (pares blindados y cable blindado).
- Conector: GG-45 (compatible con RJ45), TERA.
(Siemon comercializa un cable categoría 7a a 1200 MHz.) 
- Categoría 8:
- Ancho de banda: Hasta 2 GHz.
- Aplicaciones: Centro de datos, Telefonía + televisión + 1000BASE-T Ethernet.
- Cable SFTP/SSTP (pares blindados y cable blindado).
- Conector: RJ-45 Y GG-45, TERA.
### 🔵 CATEGORÍA 
VELOCIDAD 
FRECUENCIA 
VELOCIDAD DE 
### 🔵 DESCARGA 
ETHERNET CAT 5 
100 Mbps 
100 MHz 
15,5 MB/s 
ETHERNET CAT 5E 
1.000 Mbps 
100 MHz 
150,5 MB/s 
ETHERNET CAT 6 
1.000 Mbps 
250 MHz 
150,5 MB/s 
ETHERNET CAT 6A 
10.000 Mbps 
500 MHz 
1.250 MB/s o 1,25 GB/s 
ETHERNET CAT 7 
10.000 Mbps 
600 MHz 
1,25 GB/s 
ETHERNET CAT 7A 
10.000 Mbps 
1000/1200 MHz 
1,25 GB/s 
ETHERNET CAT 8 
40.000 Mbps 
2000 MHz 
5 GB/s 
 
 
 
 
### 🔵 Atención 
Si se utilizan conectores RJ49, se debería conectar la masa a tierra \nen uno de los extremos para evitar daños a los equipos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
3.1.2.1.1. Tipos de cable par trenzado 
Para que todo quede más claro, vamos a mostrar unos gráficos. Los símbolos que vamos a utilizar son 
los siguientes: 
- U/UTP.
 
Par trenzado no apantallado (Unshielded Twisted Pair) 
Es el más utilizado en redes de área local en Europa. 
Ventajas: 
- Bajo costo.
- Facilidad en su manejo (gran flexibilidad).
Desventajas: 
- Mayor tasa de error.
- Más sensible a perturbaciones.
- Menor distancia (necesita más regeneración de señal).
- F/UTP.
 
Par trenzado con aluminio (Foiled Twisted Pair) 
El conjunto de pares se recubre con una lámina de aluminio.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Características: 
- Esta técnica permite tener un apantallamiento mejor que UTP (aunque menor que STP).
- El sobrecoste frente a UTP es pequeño (más barato de STP).
- Se debería conectar la masa a tierra en uno de los extremos, para evitar daños a los equipos
(usando conectores RJ49). 
- Mayor flexibilidad que STP, pero menor que UTP.
- U/FTP.
 
Par trenzado apantallado (Shielded 
Twisted Pair) 
Utiliza conectores RJ-45. 
Es el más utilizado en redes de área local en EE.UU. 
Cada par se cubre con una malla metálica. 
Ventajas: 
- El empleo de la malla reduce la tasa de error (menor exposición a perturbaciones).
Desventajas: 
- Mayor coste.
- Menos manejable (mayor peso y menor flexibilidad).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- SF/UTP.
 
Par trenzado laminado apantallado (Screened Foiled 
Twisted Pair) 
Utiliza conectores RJ-49 oRJ-45). 
El conjunto de pares se recubre con una lámina de aluminio y esta a su vez se le añade una malla 
metálica LSZH. 
Ventajas: 
- El empleo de la malla reduce la tasa de error (menor exposición a perturbaciones).
Desventajas: 
- Mayor coste.
- Estos mejoran las prestaciones de un cable FTP, aunque siguen siendo inferiores a los cables
SSTP. 
- Se debería conectar la masa a tierra en uno de los extremos, para evitar daños a los equipos
(usando conectores RJ49). 
- S/FTP.
 
Par trenzado apantallado ("Screened Shielded Twisted Pair") 
Utiliza conectores RJ-49 o RJ-45. 
Es el más utilizado en redes de área local en EE.UU.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Cada par se cubre con una lámina de aluminio y el conjunto de pares se recubre material LSZH. 
Ventajas: 
- El empleo de la malla reduce la tasa de error (menor exposición a perturbaciones).
Desventajas: 
- Mayor coste.
- Menos manejable (mayor peso y menor flexibilidad).
- Se debería conectar la masa a tierra en uno de los extremos, para evitar daños a los equipos
(usando conectores RJ49). 
### 🔵 Para recordar 
 
Para poder recordar esta nomenclatura, dos trucos, traduzcamos primero el significado de cada 
término: 
- Shileded / Unshielded: Apantallado / Sin pantalla.
- Foiled: con Lámina/Hoja.
- Twisted: trenzado.
- Pair: par.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Segundo, recordemos que lo que va a la izquierda del separador "/" alude a las características del 
blindaje global de los pares (en azul en la tabla), y a la derecha a las características de cada par (rojo y 
verde en la tabla). 
3.1.2.1.2. Tipos de cable par trenzado según la norma ISO / IEC 11801 
A continuación, vamos a ver otra clasificación de Tipos de cable par trenzado según la norma ISO / IEC 
11801. 
El estándar define varias clases de interconexiones de cable de par trenzado de cobre, que difieren en la 
máxima frecuencia por la cual un cierto desempeño de canal es: 
- Clase A: hasta 100 kHz.
- Clase B: hasta 1 MHz.
- Clase C: hasta 16 MHz.
- Clase D: hasta 100 MHz.
- Clase E: hasta 250 MHz.
- Clase EA: hasta 500 MHz.
- Clase F: hasta 600 MHz.
- Clase Fa: hasta 1,000 MHz.
La impedancia estándar del vínculo es de 100 Ω (Ohmios) (la versión anterior de 1995 del estándar 
también permitía 120 Ω y 150 Ω en clases A-C, pero esto fue eliminado en la edición de 2002. 
3.1.2.1.3. Estándar en las conexiones 
Para que todos los cables funcionen en cualquier red, se sigue un estándar a la hora de hacer las 
conexiones. (Un orden de colores en el conector). 
El cable directo de red sirve para conectar dispositivos desiguales, como un computador con un hub o 
switch. 
En este caso, ambos extremos del cable deben tener la misma distribución. No existe diferencia alguna \nen la conectividad entre la distribución 568B y la distribución 568A siempre y cuando en ambos \nextremos se use la misma, en caso contrario hablamos de un cable cruzado. 
Tipos de cable directo: 
- Cable Directo Norma 568a.
1. Blanco/verde. 
2. Verde. 
3. Blanco/Naranja.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
4. Azul. 
5. Blanco/Azul. 
6. Naranja. 
7. Blanco/Marrón. 
8. Marrón. 
- Cable Directo Norma 568B:
Es en la práctica, el esquema más utilizado. (se sigue el mismo orden en ambos extremos). 
1. Blanco/naranja. 
2. Naranja. 
3. Blanco/Verde. 
4. Azul. 
5. Blanco/azul. 
6. Verde. 
7. Blanco/Marrón. 
8. Marrón. 
- Conexión directa PC a PC.
Si sólo se quieren conectar dos PC, existe la posibilidad de colocar el orden de los colores de tal 
manera que no sea necesaria la presencia de un hub. 
Es lo que se conoce como un "cable cruzado". 
Simplemente se intercambiarán los pares TX con los RX. 
El estándar que se sigue es el siguiente: 
Un extremo (Norma B) 
El otro extremo (Norma A) 
### 🔵 Blanco Naranja 
Blanco Verde 
Naranja 
Verde 
### 🔵 Blanco Verde 
Blanco Naranja 
Azul 
Azul 
Blanco Azul 
### 🔵 Blanco Azul 
Verde 
Naranja

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
3.1.2.1.4. Tecnologías xDSL sobre par trenzado 
Las tecnologías de acceso xDSL (Digital Subscriber Line) son un conjunto de soluciones que permiten 
transmitir datos digitales a alta velocidad a través de las líneas telefónicas convencionales de cobre. 
Estas tecnologías se utilizan principalmente para ofrecer acceso a Internet de banda ancha, así como 
servicios de voz y vídeo. El término "xDSL" abarca varias variantes, cada una con sus propias 
características y capacidades. 
ADSL (Asymmetric Digital Subscriber Line) 
Se caracteriza por una velocidad de descarga mucho mayor que la de subida, lo que la hace ideal para 
usuarios domésticos que buscan una conexión rápida para navegar por Internet, ver vídeos en 
streaming o jugar en línea. En condiciones óptimas, ADSL puede ofrecer velocidades de descarga de 
hasta 24 Mbps y de subida hasta 1-3 Mbps. Por otro lado, SDSL (Symmetric Digital Subscriber Line) 
ofrece una velocidad simétrica, es decir, las velocidades de descarga y subida son iguales, lo que la hace 
más adecuada para empresas que requieren un acceso equilibrado en ambas direcciones, como la subida 
de archivos grandes, con velocidades que generalmente alcanzan hasta 2 Mbps en ambos sentidos. 
VDSL (Very-high-bit-rate Digital Subscriber Line) 
Ofrece velocidades mucho más altas que ADSL y SDSL, especialmente en distancias cortas. VDSL puede 
alcanzar hasta 100 Mbps en descarga y 20 Mbps en subida, lo que la convierte en una excelente opción 
para usuarios que necesitan altas velocidades para aplicaciones como vídeo en alta definición o 
videoconferencias. VDSL2 (Very-high-bit-rate Digital Subscriber Line 2) es una mejora de esta 
tecnología, que no solo ofrece velocidades superiores, sino que también tiene un alcance mayor, 
permitiendo velocidades de hasta 200 Mbps en descarga y 100 Mbps en subida en condiciones óptimas. 
G.fast 
Es una tecnología de acceso de muy alta velocidad que también utiliza líneas de cobre, pero con un 
alcance más limitado que otras tecnologías DSL. G.fast puede ofrecer velocidades de hasta 1 Gbps en 
distancias de unos pocos cientos de metros, lo que la convierte en una opción ideal para proporcionar 
conexiones de fibra a la última milla, alcanzando velocidades muy altas sin necesidad de un despliegue 
completo de fibra óptica. 
xDSL Ventajas e Inconvenientes 
- Ventajas: entre las principales ventajas de las tecnologías xDSL se incluyen el uso de la infraestructura existente, ya que aprovechan las líneas telefónicas de cobre, lo que reduce 
significativamente el costo de implementación. Además, permiten a los usuarios acceder a 
Internet de banda ancha con velocidades mucho mayores que las de las conexiones 
tradicionales por módem, y son especialmente útiles en áreas rurales donde la fibra óptica aún 
no ha llegado. 
- Inconvenientes: disminución de calidad y velocidad con la distancia entre el usuario y la central telefónica o el nodo de acceso, y la susceptibilidad a interferencias en las líneas de cobre, lo que 
puede afectar la calidad de la señal.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
##### 3.1.2.2. Coaxial
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:Coaxial_cable
_cutaway.svg) 
### 🔵 Estructura 
El cable coaxial contiene: 
- Un conductor de cobre en su interior.
- Un aislante dieléctrico que envuelve al conductor de cobre para aislarlo del apantallado metálico. 
- Un apantallado metálico en forma de malla entretejida que aísla el cable de perturbaciones \nexternas.
- Un envoltorio de plástico que protege el resto de los elementos.
Ventajas frente al par trenzado 
- Tiene un alto grado de resistencia a las interferencias.
- Es posible conectar distancias mayores que con los cables de par trenzado.
Aplicaciones del Cable Coaxial 
- Sistemas de televisión por cable.
- Sistemas de transmisión entre centrales telefónicas.
- Redes de área local.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Transmisión digital de corta distancia.
- Sistemas de Audio.
- Redes de topología BUS extensas.
### 🔵 Tipos de cable 
Existen dos tipos de cable coaxial básicos: 
- Fino (thin coaxial).
- También conocido en redes como 10Base2.
- El 2 se refiere a que el mayor segmento posible es de 200 metros (en realidad 185).
- Usa un conector BNC.
 
Conector BNC. Fuente: 
(https://es.wikibooks.org/wiki/Archivo:Connector_bnc.jpg) 
- Grueso (thick coaxial).
- También conocido como 10Base5.
- El 5 se refiere a que el mayor segmento posible es de 500 metros.
- Tiene una capa plástica adicional que protege de la humedad al conductor de cobre.
- Tiene menor flexibilidad.
- Utiliza un conector tipo N.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Conector tipo N. Fuente: 
(https://commons.wikimedia.org/wiki/File:M ale_type_N_connector.jpg) 
##### 3.1.2.3. Fibra óptica
 
Luz a través del núcleo de la fibra óptica 
Es un medio de transmisión constituido por un medio fino y flexible, capaz de confinar un haz luminoso 
para transportar información. 
Estructura 
- El núcleo (core).
Es la parte interior de la fibra. 
Está fabricado por un material dieléctrico. 
- El revestimiento (cladding).
Envuelve al núcleo. 
Fabricado con materiales similares al núcleo, pero con un índice de refracción menor (necesario 
para que se produzca el fenómeno de la reflexión total interna). 
Gracias a este fenómeno los rayos de luz que entran en la fibra con cierto ángulo quedan 
confinados en el núcleo, siendo guiados por la fibra hasta el otro extremo.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- La camisa o cubierta.
Normalmente de plástico. Protege al núcleo y al revestimiento. 
 
Fuente: (https://en.m.wikipedia.org/wiki/File:Fiber-optic-
construction.png) 
Beneficios 
- Gran capacidad.
- Poco tamaño y peso.
- Poca atenuación.
- No perturbada por los campos magnéticos.
- Grandes distancias entre repetidores.
- Alta velocidad.
### 🔵 Modos de transmisión 
Las diferentes trayectorias que puede seguir un haz de luz en el interior de una fibra se denominan 
modos de propagación. 
Según el modo de propagación tendremos dos tipos de fibra óptica: monomodo y multimodo: 
- Fibra monomodo.
Se propaga un único modo por lo que se evita la dispersión modal. 
La longitud de onda de fibra monomodo de uso común es 1310nm y 1550nm.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
 
 
+ Info 
La dispersión modal se produce debido a la diferencia de 
velocidades de propagación de los modos que se transmiten por la 
fibra óptica. 
 
 
- Fibras multimodo.
Una fibra multimodo es aquella en la que los haces de luz pueden circular por más de un modo o 
camino. 
Los haces de luz, dependiendo del modo, pueden tardar más o menos. 
Una fibra multimodo puede tener más de mil modos de propagación de luz. 
Las fibras multimodo se usan comúnmente en aplicaciones de corta distancia, menores a 2 km, \nes simple de diseñar y económico. 
El núcleo de una fibra multimodo es mayor que el de las monomodo. 
Dependiendo el tipo de índice de refracción del núcleo, tenemos dos tipos de fibra multimodo: 
- Índice escalonado:
» El núcleo tiene un índice de refracción constante en toda la sección cilíndrica. 
» Tiene alta dispersión modal. 
- Índice gradual:
» El índice de refracción no es constante. 
» Tiene menor dispersión modal. 
» El núcleo está formado por distintos materiales.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Fuente: (https://cs.m.wikipedia.org/wiki/Soubor:Optical_fiber_types.svg) 
El núcleo de una fibra multimodo es mayor que el de las monomodo. 
 
 
 
+ Info 
- La fibra óptica presenta una gran sensibilidad a la curvatura. 
- Al curvarse se produce una atenuación adicional, y ciertos modos se podrían escapar del núcleo. 
- Estas pérdidas varían exponencialmente con la curvatura.
 
Técnicas de transmisión de señales por fibra óptica 
Algunas de las principales son: 
- DWDM.
Acrónimo, en inglés, de Dense Wavelength Division Multiplexing, que significa multiplexado 
denso por división en longitudes de onda.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
DWDM es una técnica de transmisión de señales a través de fibra óptica usando la banda C 
(1550 nm (nanómetros)). 
Es un método de multiplexación muy similar a la multiplexación por división de frecuencia que 
se utiliza en 
Varias señales portadoras se transmiten por una única fibra óptica utilizando distintas longitudes 
de onda de un haz láser en cada una de ellas. 
Sistemas WDM con más de ocho longitudes de onda activas por fibra. 
- CWDM.
Acrónimo, en inglés, de Coarse wavelength Division Multiplexing, que significa Multiplexación 
por división aproximada de longitud de onda. 
CWDM es una técnica de transmisión de señales a través de fibra óptica que pertenece a la 
familia de multiplexion por división de longitud de onda (WDM). 
Sistemas WDM con menos de ocho longitudes de onda activas por fibra. 
- OFDM.
Acrónimo, en inglés, de Orthogonal Frequency Division Multiplexing, deriva de FDM, Frequency 
Division Multiplexing, que es una técnica de multiplexión por división en frecuencia. 
El sistema consistía en separar, con un ancho de guarda, las portadoras para que no hubiera 
solapamiento, y, por tanto, interferencia entre portadoras, (ICI) 
### 🔵 Clasificación según ancho de banda 
También se pueden clasificar según su ancho de banda. El estándar ISO 11801especifica los siguientes 
tres tipos: 
- OM1.
- Fibra 62.5/125 µ m (micras).
- Soporta hasta Gigabit Ethernet (1 Gbit/s).
- Utiliza emisores led.
- OM2.
- Fibra 50/125 µm.
- Soporta hasta Gigabit Ethernet (1 Gbit/s).
- Utiliza emisores led.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- OM3.
- Fibra 50/125 µm.
- Soporta hasta 10 Gigabit Ethernet.
- Utiliza emisores láser.
- OM4.
- Fibra 50/125 µm.
- Soporta hasta 100 Gigabit Ethernet.
- Utiliza emisores láser.
### 🔵 Conectores 
Hay muchos tipos de conectores. Algunos de los más utilizados son: 
- FC.
Se usa en la transmisión de datos. 
- FDDI.
Se usa para redes de fibra óptica. 
- LC y MT-Array.
Se utilizan en transmisiones de alta densidad de datos. 
- SC y SC-Dúplex.
Se utilizan para la transmisión de datos. 
- ST o BFOC.
Se usa en redes de edificios y en sistemas de seguridad.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:Tipos_conectores_
fibra_optica.jpg) 
3.1.2.3.1. Normas 1000BASE para fibra óptica 
- 1000BASE-SX.
- Fibra Multimodo (MMF).
- Láser 850 nm.
- Distancia < 550 m.
- 1000BASE-LX.
- Fibra Multimodo (MMF) y Fibra Monomodo (SMF).
- Láser 1310 nm.
- Distancia < 10 km.
- 1000BASE-EX.
- Fibra SMF.
- Láser 1310 nm.
- Distancia < 40 km.
- 1000BASE-ZX.
- Fibra SMF.
- Láser 1550 nm.
- Distancia < 80 km.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
3.1.2.3.2. Fibra Óptica Plástica 
La gran diferencia con respecto a la de vidrio es que está fabricada con plástico es más flexible y 
maleable (permitiendo su uso en instalaciones donde los tubos son antiguos) y resistente. El plástico \nempleado es uno de los plásticos de ingeniería, el polimetilmetacrilato envuelto en polímeros fluoruros. 
Su composición le permite aprovechar todo el ancho de banda sin pérdidas sensibles en distancias 
cortas. Cuenta con un núcleo conductor es entre 20 y 100 veces mayor que el de la fibra de vídrio, 
diseñado para instalaciones donde la distancia de transmisión no es un elemento crítico. Su uso suele 
restringirse a aplicaciones como resdes locales. 
##### 3.1.2.4. Fibra hasta la casa o hasta el hogar
Se conoce así, a la tecnología de telecomunicaciones FTTH (acrónimo del inglés Fiber To The Home), 
comprendida dentro de las tecnologías FTTx. 
Se basa en el uso de cables de fibra óptica y sus sistemas de distribución para el suministro, de servicios 
avanzados de telecomunicaciones, como el denominado Triple Play: telefonía, Internet de banda ancha 
y televisión, a los hogares y negocios de los abonados. 
Muchos operadores reducen la promoción de servicios ADSL en beneficio de la fibra óptica con el 
objetivo de proponer servicios muy veloces de banda ancha para el usuario. 
 
 
 
 
### 🔵 Nota 
Tecnología de telecomunicaciones FTTx (del inglés Fiber to the x). 
Es un término genérico para designar cualquier acceso de banda 
ancha sobre fibra óptica que sustituya total o parcialmente el 
cobre del bucle de acceso. 
 
 
La tecnología FTTH propone utilizar la fibra óptica hasta la vivienda del usuario o cliente de fibra 
llamado también "usuario final". La red de acceso entre el abonado y el último modo de distribución 
puede realizarse con una o dos fibras ópticas dedicadas a cada usuario (una conexión punto-punto que 
resulta en una topología en estrella) o una red óptica pasiva (del inglés Passive Optical Network, PON) 
que usa una estructura arborescente con una fibra en el lado de la red y varias fibras en el lado usuario. 
Una red óptica pasiva permite eliminar todos los componentes activos existentes entre el servidor y el 
cliente introduciendo en su lugar componentes ópticos pasivos para guiar el tráfico por la red, cuyo \nelemento principal es el dispositivo divisor óptico. La utilización de estos sistemas pasivos reduce 
considerablemente los costes y son utilizados en las redes FTTH.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Las arquitecturas basadas en divisores ópticos pasivos se definen como sistemas sin elementos \nelectrónicos activos en el bucle y cuyo elemento principal es el dispositivo splitter (divisor de haz: un 
divisor de haz es un instrumento óptico que divide un rayo de luz en dos). 
Dependiendo de la dirección del haz de luz, divide el haz entrante y lo distribuye hacia múltiples fibras o 
lo combina dentro de una misma fibra. La filosofía de esta arquitectura se basa en compartir los costes 
del segmento óptico entre los diferentes terminales, de forma que se pueda reducir el número de fibras 
ópticas. 
Así, por ejemplo, mediante un splitter óptico, una señal de vídeo se puede transmitir desde una fuente a 
múltiples usuarios. 
 
 
 
 
+ Info 
Los Splitters son elementos pasivos, ya que no requieren ninguna 
fuente de energía externa, más que la señal óptica de entrada. Son 
independientes de la longitud de onda y solamente incorporan una 
atenuación debido al hecho que divide la potencia de entrada. 
 
 
Los Splitters son elementos pasivos, ya que no requieren ninguna fuente de energía externa, más que la 
señal óptica de entrada. Son independientes de la longitud de onda y solamente incorporan una 
atenuación debido al hecho que divide la potencia de entrada. 
La topología en estrella provee de 1 o 2 fibras dedicadas a un mismo usuario. Proporciona el mayor 
ancho de banda, pero requiere cables con mayor número de fibras ópticas en la central de 
comunicaciones y un mayor número de emisores láser en los equipos de telecomunicaciones. 
Se recomienda que los elementos pasivos se distribuirán lo más cerca del cliente final, minimizando los 
gastos de fibra óptica, pero el principal objetivo no es minimizar los gastos de fibra, sino diseñar una red 
fácilmente escalable en el futuro, aprovechando los recursos del diseño inicial. Con la menor inversión 
posible, permitirá aumentar las zonas de cobertura en caso de crecimiento urbano de la localidad. 
También es aconsejable distinguir tres ramales, con las siguientes características en la distribución de la 
fibra óptica: 
- Feeder o troncal:
Es la ruta por cada par de fibra óptica desde el Central Switch Point, hasta el primer elemento 
pasivo o splitter. 
Es indispensable y obligatorio que la ruta de feeder permita múltiples fibras ópticas, para 
permitir que varios operadores puedan usar la red GPON.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
La GPON (Red Óptica Pasiva con Capacidad de Gigabit) es una tecnología de acceso de 
telecomunicaciones que utiliza cableado de fibra óptica para llegar hasta el usuario, es decir, la 
última milla se compone de fibra óptica. 
- Distribución:
Es la ruta entre el feeder y el último punto de distribución, a partir del cual parten las fibras 
ópticas individuales hacia cada ONT o cliente. 
Una ONT (del inglés Optical Network Terminal) es el equipo que convierte la señal óptica que 
transporta la Fibra, en una señal de banda ancha Gigabit Ethernet (1000/1000) que puede 
interpretar el router. 
Mientras las fibras de distribución se acerquen más a la zona que se pretende cubrir, se reducen 
las cantidades de fibra óptica con la que se llega al abonado final. 
Si es posible, se recomienda instalar un ODF (Distribuidor de fibra óptica, también conocido 
como ROM; Repartidor Óptico Modular) o cajas de distribución cuyas dimensiones se adapten a 
la infraestructura civil. 
Un ODF facilita la centralización, interconexión y derivaciones de cables de fibra óptica. 
Por ejemplo: ODF en forma de cajetín de pared o de suelo para accesos a edificios con alta 
densidad de clientes, o cajas de distribución pequeñas que puedan ubicarse sobre los postes, en 
manzanas con baja densidad de clientes finales. 
- Acceso al Abonado.
Corresponde a la ruta desde la ubicación del ONT del cliente hasta el empalme con el poste más 
cercano, o punto de conexión. 
En zonas con poca densidad de vivienda, el tramo final del abonado puede hacerse por cableado 
aéreo desde la casa del cliente hasta el poste más cercano que se conecta con la red de 
distribución GPON. 
En zonas con mayor densidad de vivienda como edificios, se recomienda instalar un cajetín u 
ODF, al pie del cual partirán las fibras de acceso al abonado. 
##### 3.1.2.5. Redes híbridas: HFC (Hybrid Fiber-Coaxial)
Las redes HFC (Hybrid Fiber-Coaxial) son una arquitectura de transmisión que combina el uso de fibra 
óptica y cable coaxial. Esta tecnología fue desarrollada originalmente para distribuir televisión por cable, 
pero con el tiempo ha evolucionado para ofrecer también internet de banda ancha y servicios de 
telefonía. 
En una red HFC, la señal se transmite desde el proveedor de servicios a través de fibra óptica hasta un 
nodo óptico situado cerca de los usuarios. A partir de ese nodo, la señal se convierte en eléctrica y se 
distribuye mediante cable coaxial hasta los hogares. Esta combinación permite aprovechar la alta 
capacidad de la fibra en el núcleo de la red y la infraestructura coaxial ya instalada en muchas zonas 
residenciales.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Desde el punto de vista técnico, las redes HFC utilizan el estándar DOCSIS (Data Over Cable Service 
Interface Specification) para la transmisión de datos sobre cable coaxial. DOCSIS 3.0 permite 
velocidades de hasta 1 Gbps de bajada y 200 Mbps de subida, mientras que DOCSIS 3.1 eleva esos 
valores teóricos por encima de los 10 Gbps de descarga. Estas redes funcionan con acceso compartido, 
lo que significa que varios usuarios conectados al mismo nodo dividen el ancho de banda disponible. La 
señal se transmite mediante modulación QAM, y la comunicación entre cliente y proveedor se realiza 
mediante duplexación por división de frecuencia (FDD). Además, la fibra óptica suele cubrir tramos de \nentre 10 y 30 km hasta el nodo, y el cable coaxial entre 100 y 500 metros hasta el usuario final. 
Aunque no ofrece las mismas prestaciones que una red de fibra óptica hasta el hogar (FTTH), HFC 
sigue siendo una solución ampliamente utilizada por operadores de telecomunicaciones, ya que reduce 
costes de despliegue y mantiene un buen nivel de servicio. 
##### 3.1.2.6. Sistema de cableado estructurado
Infraestructura estandarizada (normas TIA/EIA-568 e ISO/IEC 11801) que integra cables, conectores y 
dispositivos para distribuir voz, datos y vídeo en edificios. Combina par trenzado (categorías 5e/6/6A), 
fibra óptica (monomodo/multimodo) y coaxial en una red jerárquica en estrella, con: 
- Cuarto principal (MDF) como núcleo.
- Cableado horizontal (90m + 10m latiguillos).
- Backbone vertical (fibra/cobre) entre IDFs.
- Área de entrada (EF) para conexiones externas.
Los estándares fijan distancias máximas (100m en horizontal para fibra), conectores (RJ-45, SC/LC) y 
requisitos de documentación (TIA-606). Permite integrar tecnologías (cobre en puestos de trabajo, 
fibra en troncales) garantizando escalabilidad, compatibilidad y mantenimiento simplificado. 
Ventajas clave: flexibilidad para upgrades futuros, organización física optimizada y soporte para 
múltiples servicios sobre la misma infraestructura. 
#### 🔹 3.1.3. No guiados o inalámbricos
Son aquellos que utilizan el aire, el vacío, el agua o la tierra como medio de transmisión. 
La transmisión puede ser de dos tipos: 
- Direccional:
La antena emisora y receptora deben estar alineadas. 
- Omnidireccional:
La antena transmisora emite en todas las direcciones.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Los principales sistemas son: 
- Sistemas de ondas de radio.
- Sistemas de microondas:
- Terrestres.
- Por satélite.
- Sistemas de luz:
- Infrarrojos.
- VLC (LIFI).
##### 3.1.3.1. Sistemas de ondas por radio
 
Fuente: (https://pixabay.com/es/ondas-de-radio-
wifi-inal%C3%A1mbrica-303258/) 
Es un enlace de radio que provee conectividad entre un emisor y uno o más receptores. 
Sus principales características son: 
- Las señales de radio son omnidireccionales.
- Bandas de frecuencia: LF, MF, HF y VHF.
- Fáciles de generar.
- Pueden viajar largas distancias.
- Atraviesan paredes de edificios sin problemas.
- Son absorbidas por la lluvia.
- Pueden sufrir interferencias por equipos eléctricos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Dependen de la frecuencia:
- Bajas frecuencias:
Cruzan bien los obstáculos, pero la potencia baja drásticamente con la distancia. 
- Altas frecuencias:
Tienden a viajar en línea recta y rebotar en obstáculos. 
- Su alcance depende de:
- Potencia de emisión.
- Sensibilidad en el receptor.
- Condiciones atmosféricas.
- Relieve del terreno.
- No necesita permisos ni licencias de uso.
##### 3.1.3.2. Sistemas de microondas
Pueden ser a través de diferentes medios: 
- Medios terrestres.
- Por Satélite.
### 🔵 Terrestres 
 
Fuente: (https://pixabay.com/es/torre-
de-microondas-la-comunicaci%C3%B3n-
2069093/)

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Es un enlace de radio que provee conectividad entre dos sitios alineados. 
Sus principales características son: 
- La forma de onda emitida puede ser analógica (convencionalmente en FM) o digital.
- Utiliza frecuencias muy altas: 1 -100 GHz.
- Longitud de onda muy pequeña.
- Es absorbida por la lluvia.
- No atraviesa bien edificios.
- Las ondas son direccionales.
- Se utilizan antenas parabólicas.
- Transmisor y receptor se tienen que "ver" (estar alineados).
- Cuanto más altas son las antenas, más distancia puede cubrir.
- Ejemplo: Con torres a 100 m de altura, las repetidoras pueden estar espaciadas 80 Km.
### 🔵 Por satélite 
 
Fuente: (https://sq.wikipedia.org/wiki/GPS) 
Son transmisiones por microondas en las que las estaciones son satélites que están orbitando la Tierra. 
Sus principales características son: 
- Amplia cobertura.
- Opera en el rango de los GHz.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Para la comunicación se usan dos bandas de frecuencia:
- Canal ascendente: desde la Tierra al satélite.
- Canal descendente: desde el satélite a la Tierra.
- Los satélites utilizan transpondedores.
Un transpondedor es un dispositivo electrónico que realiza dos funciones: 
- Recepción, amplificación y reemisión de una señal en una banda distinta a la de la señal.
- Envía una respuesta automática cuando recibe una señal concreta.
 
 
 
 
+ Info 
En el caso de los satélites, un transpondedor recibe una señal 
microondas desde la Tierra, la amplifica y la retransmite de regreso 
a una frecuencia diferente. 
 
##### 3.1.3.3. Sistemas de luz
Transmiten la señal mediante luz. 
Los principales sistemas son: 
- Infrarrojos.
 
Fuente: 
(https://pixabay.com/es/control-
remoto-televisi%C3%B3n-28001/)

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Son transmisores y receptores que modulan luz infrarroja no coherente (no tiene una frecuencia 
única de luz, sino que posee cierto ancho en el espectro). 
Para que la comunicación se pueda establecer, el transmisor y el receptor deben estar alineados. 
Características: 
- No pueden atravesar paredes.
- Son de corto alcance.
- No necesita permisos o licencias de uso.
- VLC o (LIFI).
 
Fuente: 
(https://es.m.wikipedia.org/wiki/Archivo:Lifi-
image.jpg) 
La comunicación por luz visible está desarrollada sobre la base de una bombilla LED como 
transmisor. 
Normalmente se usan para iluminación utilizando un valor fijo de corriente. 
Sin embargo, variando la corriente, la salida óptica, es decir la intensidad de la iluminación, 
puede ser variada a velocidades extremadamente elevadas. 
Esta propiedad es la base de VLC. 
El procedimiento es simple: 
- Si el LED está encendido, se transmite un uno digital.
- Si está apagado, se emite un cero digital.
Los LEDs pueden ser encendidos y apagados a grandes velocidades, lo que brinda buenas 
oportunidades para transmitir datos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Óptica del espacio libre (FSO).
 
La óptica de espacio libre (FSO o free-space optical) es una tecnología de comunicación óptica 
que utiliza la propagación de la luz (visible o infrarroja) en la atmósfera para transmitir 
información entre dos puntos. 
Su principal inconveniente es alinear los dos puntos. 
##### 3.1.3.4. Transmisión de datos VSAT (Very Small Aperture Terminal)
La tecnología VSAT (Very Small Aperture Terminal) se basa en el uso de antenas parabólicas de 
pequeño tamaño, generalmente menores de 3 metros, que permiten establecer enlaces de 
comunicación vía satélite tanto para voz como para datos. Estas estaciones, que pueden instalarse en 
ubicaciones fijas o móviles, se comunican con satélites en órbita geoestacionaria mediante ondas de 
radio en frecuencias de microondas. Utilizan dos canales diferenciados: el canal ascendente (uplink), 
que va desde la Tierra al satélite, y el canal descendente (downlink), que realiza el camino inverso desde \nel satélite a la Tierra. 
VSAT opera principalmente en tres bandas de frecuencia: la banda C (4-8 GHz), menos afectada por las 
condiciones atmosféricas pero que requiere antenas más grandes; la banda Ku (12-18 GHz), la más 
utilizada en aplicaciones comerciales por su equilibrio entre tamaño de antena y rendimiento; y la banda 
Ka (26-40 GHz), que ofrece mayor capacidad pero es más sensible a la atenuación por lluvia. En todos 
los casos, los transpondedores del satélite se encargan de recibir las señales, amplificarlas y reemitirlas \nen una frecuencia diferente, permitiendo así la comunicación entre la estación central (hub) y las 
numerosas estaciones remotas distribuidas en tierra. 
Entre sus principales ventajas destaca su amplia cobertura geográfica, lo que la hace ideal para zonas 
rurales o remotas carentes de infraestructura terrestre, así como su capacidad para desplegarse 
rápidamente en situaciones de emergencia donde otras formas de comunicación no están disponibles. 
Es una tecnología especialmente útil para aplicaciones como cajeros automáticos, terminales de punto 
de venta, monitorización remota de instalaciones industriales, redes corporativas distribuidas y como 
respaldo de comunicaciones críticas. 
Sin embargo, la tecnología VSAT presenta algunas limitaciones, siendo la más notable su mayor latencia 
(aproximadamente 500-700 milisegundos) debido a la gran distancia que deben recorrer las señales 
hasta los satélites geoestacionarios, situados a unos 36.000 kilómetros de altitud. Además, su coste 
suele ser superior al de las redes terrestres en aquellas zonas donde estas últimas están disponibles, lo 
que limita su uso a casos donde no existen alternativas más económicas o cuando se requiere una 
solución de conectividad inmediata y fiable en entornos remotos o de difícil acceso.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 3.2. Tipos de transmisión según el tipo de señal
Hay 4 tipos de transmisión según el tipo de señal: 
- Señal analógica a señal analógica.
Analógica-Analógica. 
Hay dos alternativas: 
- El ancho de banda de ambos dispositivos coincide:
En este caso los datos se envían tal cual. 
- El ancho de banda de ambos dispositivos no coincide:
Se tendrán que modular los datos. 
- Señal analógica a señal digital.
Analógica-Digital. 
Los datos analógicos se codifican utilizando un código para generar una cadena de bits que se \nenvía al receptor. 
- Señal digital a señal analógica.
Digital-Analógica. 
Los datos digitales se codifican usando un dispositivo (como un modem) para generar señales 
analógicas. 
- Señal digital a señal digital.
Digital-Digital. 
Tenemos dos alternativas: 
- La señal consiste en dos niveles de tensión que representan los dos valores binarios.
- Los datos digitales se codifican para producir una señal digital con las propiedades deseadas.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 3.3. Perturbaciones en la transmisión
Durante la comunicación se pueden producir diferentes alteraciones. 
Cuando ocurren en el entorno de las comunicaciones de datos o redes, este tipo de alteraciones reciben \nel nombre de perturbaciones. 
### 🔵 Atenuación 
En telecomunicación, se denomina atenuación de una señal (acústica, eléctrica u óptica) a la pérdida de 
potencia sufrida por la misma al transitar por cualquier medio de transmisión. 
Así, si introducimos una señal eléctrica con una potencia P1 en un circuito pasivo, como puede ser un 
cable, esta sufrirá una atenuación y al final de dicho circuito obtendremos una potencia P2 (siendo 
P2<P1). 
La atenuación (α) será igual a la diferencia entre ambas potencias (P1-P2). 
No obstante, la atenuación no suele expresarse como diferencia de potencias sino en unidades 
logarítmicas como el decibelio. 
Para corregir la atenuación, se establece un límite a la longitud del cable que puede usarse, para así 
garantizar que los circuitos receptores podrán detectar e interpretar con confiabilidad la señal atenuada 
recibida. 
Si el cable es más largo, se inserta uno o más amplificadores de señal (repetidores) a intervalos a lo 
largo del cable a fin de restablecer la señal recibida a su nivel original. 
### 🔵 Ruido 
El ruido en telecomunicaciones son las perturbaciones eléctricas que interfieren sobre las señales 
transmitidas y/o procesadas. 
El ruido tiene un comportamiento impredecible. 
Puede ocultar la señal transmitida, eliminarla parcialmente e incluso eliminarla totalmente. 
Los orígenes del ruido son múltiples. 
Algunas fuentes de ruido son: 
- La energía en forma de ondas electromagnéticas que desprenden todos los objetos
(dependiendo de su temperatura) influyen en las comunicaciones por radio. 
- El ruido producido por fuentes tales como contactos defectuosos, y artefactos eléctricos.
- El ruido producido por fenómenos naturales tales como tormentas eléctricas con relámpagos y rayos, eclipses, etc.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Distorsión por retardo 
En los 
frecuencia. 
Hay frecuencias que llegan antes que otras dentro de la misma señal y por tanto las diferentes 
componentes en frecuencia de la señal llegan en instantes diferentes al receptor. 
Para atenuar este problema se usan técnicas de ecualización. 
### 🔵 Reflexión 
La reflexión es el cambio de dirección de un rayo o una onda que ocurre en la superficie de separación \nentre dos medios, de tal forma que regresa al medio inicial. 
Ejemplos comunes son la reflexión de la luz, el sonido y las ondas en el agua. 
### 🔵 Dispersión 
Es el fenómeno por el cual un conjunto de partículas que se mueve en una dirección determinada rebota 
sucesivamente con las partículas del medio, por el que se mueve hasta perder la dirección ideal de 
movimiento. 
### 🔵 Fluctuación de fase 
Distorsión de la línea de comunicación analógica provocada por la variación de una señal con respecto a 
un punto de referencia en el eje del tiempo. 
La fluctuación de fase puede provocar la pérdida de datos, especialmente a altas velocidades. 
### 🔵 Latencia 
En redes informáticas de datos se denomina latencia a la suma de retardos temporales dentro de una red. 
Un retardo es producido por la demora en la propagación y transmisión de paquetes dentro de la red. 
Otros factores que influyen en la latencia de una red son: 
- El tamaño de los paquetes transmitidos.
- El tamaño de los buffers dentro de los equipos de conectividad.
- Pueden producir un Retardo Medio de Encolado.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Diafonía 
En el campo de las telecomunicaciones, se dice que entre dos circuitos existe diafonía, cuando parte de 
las señales presentes en uno de ellos (perturbador) aparece en el otro (perturbado). 
## 🟣 4. Estructura de una red
La estructura de una red está formada por niveles que interactúan entre sí para conseguir la 
comunicación. 
Para ello, siempre hay que seguir unos protocolos establecidos. 
 
 
 
 
### 🔵 Recuerda 
Un protocolo es una convención o estándar que contiene un 
conjunto de reglas que establecen cómo se comunicarán dos o más 
dispositivos (lógicos o físicos). 
Un protocolo actúa sobre una capa, estableciendo la comunicación 
referente a dicha capa. A esto se le denomina comunicación 
horizontal. 
 
 
Vamos a resumir algunos conceptos que ya has aprendido, y a introducir nuevos como la 
Encapsulación-Desencapsulación. 
### 🔵 Interfaz 
Representa comunicaciones entre capas adyacentes dentro del mismo dispositivo. 
Un Interfaz permite una conexión funcional entre dos sistemas, programas, dispositivos o componentes 
de cualquier tipo, proporcionando una comunicación de distintos niveles permitiendo para que puedan 
intercambiar información. 
En nuestro caso, Las interfaces se utilizan para comunicar dos capas adyacentes dentro de un mismo 
dispositivo. 
Esto también es conocido como comunicación vertical.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Encapsulación y desencapsulación 
La transmisión de información en una red requiere de un proceso de conversión tanto para enviar como 
para recibir datos. 
Este proceso es conocido como el proceso de encapsulación (y desencapsulación) de los datos. 
En la encapsulación, cuando los datos pasan de una capa a otra, se les añade información que requiere 
cada protocolo. 
A medida que van bajando por los distintos niveles (desde la capa de aplicación hasta la física), se les va 
agregando un encabezado. 
En algunos casos también se le puede añadir un finalizador (terminal) detrás. 
Los encabezados contienen información de control para cada dispositivo de la red y aseguran el 
correcto envío de los datos para su recepción. 
 
### 🔵 Proceso de encapsulación 
El proceso de encapsulación consiste en los siguientes pasos: 
1. El usuario emisor envía unos datos. Estos pasan a la capa de aplicación (nivel 7). 
2. La capa de aplicación agrega el encabezado L7H (Layer 7 Head o cabecera de la capa 7) y los 
pasa a la capa de presentación (nivel 6). 
3. La capa de presentación agrega el encabezado L6H y lo pasa a la capa de sesión (nivel 5).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
4. La capa de sesión agrega el encabezado L5H y lo pasa a la capa de Transporte (nivel 4). 
5. La capa de transporte agrega el encabezado L4H y lo pasa a la capa de red (nivel 3). 
6. La capa de red agrega el encabezado L3H y lo pasa a la capa de enlace de datos (nivel 2). 
7. La capa de enlace de datos agrega el encabezado L2H y un finalizador L2F (Layer 2 Finalizer) 
que suele utilizarse para el control de la integridad de los datos. A este finalizador se le llama 
FCS (Frame Check Secuence) y se utiliza para detectar en el receptor si los datos han llegado 
bien o contienen algún error. 
A continuación, la capa física transmite los datos en forma de bits por la red física. 
La Desencapsulasión, es el proceso inverso. 
Cuando recibe la secuencia de bits de la capa física, los datos empiezan el proceso opuesto a la \nencapsulación, es decir, van subiendo de nivel. 
Los pasos son los siguientes: 
1. La capa de enlace de datos verifica la información contenida en el (FCS). 
- Si encuentra un error.
Los datos son descartados y solicita su reenvío. 
- Si no hay error.
La capa de enlace de datos lee e interpreta la información de control contenida en el \nencabezado L2H (encabezado de la capa 2). 
A continuación, retira el encabezado L2H y el finalizador L2F (FCS) y lo envía a la capa de 
red (nivel 3). 
2. La capa de red lee e interpreta la información de control contenida en el encabezado L3H, 
retira el encabezado y lo envía a la capa de transporte (nivel 4). 
3. La capa de transporte lee e interpreta la información de control contenida en el encabezado 
L4H, retira el encabezado y lo envía a la capa de sesión (nivel 5). 
4. La capa de sesión lee e interpreta la información de control contenida en el encabezado L5H, 
retira el encabezado y lo envía a la capa de presentación (nivel 6). 
5. La capa de presentación lee e interpreta la información de control contenida en el encabezado 
L6H, retira el encabezado y lo envía a la capa de aplicación (nivel 7). 
6. La capa de aplicación lee e interpreta la información de control contenida en el encabezado 
L7H, retira el encabezado y muestra los resultados al receptor.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Las unidades de protocolo de datos 
También llamadas PDU (del inglés Protocol Data Unit). 
Se utilizan para el intercambio de datos entre unidades disparejas, dentro de una capa n del 
modelo OSI. 
Por lo tanto: 
PDU (capa n) = Encabezado (capa n) + PDU (capa n+1) + Finalizador (capa n). 
Siendo el finalizador opcional. 
Estas son las transformaciones que acabamos de ver en la encapsulación y la desencapsulación. 
Los PDUs de cada capa son: 
### 🔵 CAPA 
PDU 
Aplicación 
APDU o PDU de aplicación 
### 🔵 Presentación 
PPDU o PDU de presentación 
Sesión 
### 🔵 SPDU o PDU de sesión 
Transporte 
Segmentos 
### 🔵 Red 
Paquetes o datagramas 
Enlace de datos 
### 🔵 Tramas 
Física 
Bits 
Arquitectura de una red 
Es un conjunto de capas (o niveles), protocolos e interfaces. 
Vamos a ver algunas características: 
- La red se divide en niveles, cada uno de los cuales tendrá unas funciones específicas y ofrecerán unos servicios. 
- Los niveles interactúan entre sí para producir la comunicación entre dos dispositivos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Los niveles inferiores prestarán servicios a las superiores a través de los puntos de acceso al servicio (SAP o Service Access Point). 
- La comunicación entre las distintas capas estará definida por interfaces que permiten la comunicación vertical. 
- Los servicios ofrecidos en una capa se definen mediante los protocolos.
- Al conjunto de protocolos utilizados en una arquitectura de red se le denomina pila de protocolos. 
- Los objetivos de la arquitectura de red son:
- Modularidad.
- Conectividad.
- Facilidad de uso e implantación.
- Confiabilidad.
- Poder ser modificado fácilmente.
A continuación, veremos una arquitectura básica de red mediante niveles o capas que ayudará a que \nentiendas los distintos conceptos: 
 
Modelo de capas de una red

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 4.1. Control de acceso a la red (NAC)
El control de acceso a la red, conocido por sus siglas en inglés NAC (Network Access Control), es una 
tecnología de seguridad que regula quién o qué puede conectarse a una red informática. Su objetivo 
principal es garantizar que solo los dispositivos que cumplen ciertos requisitos de seguridad puedan 
acceder a los recursos de red, protegiendo así la infraestructura frente a amenazas tanto internas como \nexternas. NAC actúa como una primera línea de defensa, evaluando a cada dispositivo antes de 
permitir su conexión y controlando su comportamiento una vez que ya está conectado. 
El funcionamiento de NAC se basa en dos fases fundamentales: 
- pre-admisión: en primer lugar, antes de que un dispositivo obtenga acceso a la red, el sistema realiza una evaluación previa, comprobando aspectos como la identidad del usuario, el estado 
del sistema operativo, la existencia de antivirus actualizado o la aplicación de los últimos 
parches de seguridad. En esta fase se puede solicitar una autenticación basada en credenciales, 
certificados o incluso características del propio dispositivo. Si el dispositivo no cumple con los 
requisitos establecidos por la política de seguridad, el sistema puede bloquear el acceso por 
completo, o bien permitir solo un acceso limitado, redirigiéndolo a una red de cuarentena donde 
podrá actualizarse o corregir su situación. 
- post-admisión: una vez superada la fase de admisión, el control de acceso continúa activo durante toda la sesión. Esta vigilancia permanente permite al sistema NAC monitorizar el 
comportamiento del dispositivo conectado y detectar posibles desviaciones, como intentos de \nescaneo de red o patrones de tráfico sospechosos. En estos casos, el acceso puede ser revocado 
o modificado de forma dinámica, reforzando así la protección de la red frente a ataques internos 
o dispositivos comprometidos después de la conexión inicial. 
Los sistemas NAC suelen integrarse con otros elementos de la red como switches, routers o puntos de 
acceso inalámbricos, y también con servidores que gestionan la autenticación centralizada, como los 
basados en RADIUS o Active Directory. Además, muchas soluciones NAC incorporan agentes 
instalados en los dispositivos que recogen y transmiten información sobre su estado al sistema de 
control. Esta integración permite aplicar políticas de seguridad adaptadas al tipo de usuario, al nivel de 
riesgo detectado o a la ubicación desde la que se realiza la conexión. 
El uso de NAC se ha extendido especialmente en entornos corporativos, educativos y sanitarios, donde 
la protección de la red es crítica y el número de dispositivos conectados es elevado. También resulta 
fundamental en escenarios con usuarios que trabajan en remoto o traen sus propios dispositivos (lo que 
se conoce como entornos BYOD). 
Gracias al NAC, las organizaciones pueden aplicar un control granular sobre el acceso a la red, 
diferenciando entre perfiles de usuario y garantizando que cada dispositivo cumple unos estándares 
mínimos de seguridad antes de permitir su uso. 
## 🟣 5. Redes de comunicaciones
Una red de comunicaciones es un conjunto de medios técnicos que permiten la comunicación a 
distancia entre equipos autónomos. 
Normalmente se trata de transmitir datos, audio y vídeo por ondas electromagnéticas a través de 
diversos medios (aire, vacío, cable de cobre, fibra óptica, etc.).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
La información se puede transmitir de forma analógica, digital o mixta, pero en cualquier caso las 
conversiones, si las hay, siempre se realizan de forma transparente al usuario, el cual maneja la 
información de forma analógica exclusivamente. 
Las redes más habituales son: 
- Redes de ordenadores.
- De teléfono.
- De transmisión de audio (sistemas de megafonía o radio ambiental).
- Transmisión de vídeo (televisión o vídeo vigilancia).
 
 
 
 
+ Info 
En los medios de comunicación no guiados, es necesario el uso de 
dispositivos que emitan o reciban la señal con la información. 
 
### 🔵 Capacidad de transmisión 
La capacidad de transmisión indica el número de bits por segundo que se pueden transmitir a través de 
una conexión. 
 
 
 
 
+ Info 
A menudo se confunde con la velocidad de transmisión (que 
depende de la capacidad y de otros factores) el ancho de banda 
(que es la amplitud de onda utilizable). 
El término ancho de banda se ha aceptado como sinónimo de 
capacidad de transmisión (excepto cuando se refiere a frecuencias 
de onda).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Control de flujo 
Capacidad del receptor de enviar un mensaje al emisor para indicarle que deje de enviar datos (al menos 
momentáneamente) porque no se puede garantizar la recepción correcta de ellos. 
Ejemplo: Esto se puede utilizar, por ejemplo, cuando el buffer está lleno. 
### 🔵 5.1. Clasificación
Podemos clasificar las redes de comunicación de dos formas, en función de su cobertura y en función de 
su arquitectura. 
#### 🔹 5.1.1. Según su cobertura
Según la cobertura de las redes (extensión cubierta) podemos encontrar los siguientes tipos de red: 
### 🔵 Distancia aproximada 
Ubicación típica 
Tipo de red 
### 🔵 Descripción 
Hasta 1 metro 
### 🔵 Dispositivos personales 
PAN 
Personal Area Network: 
red de un solo usuario 
Hasta 10 metros 
### 🔵 Habitación 
LAN 
Local Area Network: red 
local 
Hasta 100 metros 
### 🔵 Edificio 
LAN 
Red local en un solo \nedificio 
Hasta 1 km 
Campus / complejo 
### 🔵 LAN 
Red entre varios edificios 
cercanos 
Hasta 10 km 
### 🔵 Ciudad 
MAN 
Metropolitan Area 
Network: red 
metropolitana 
Hasta 1.000 km 
Región / país / 
continente 
### 🔵 WAN 
Wide Area Network: red 
de largo alcance 
Más de 1.000 km / 
mundial 
Varios continentes / 
planeta 
### 🔵 GAN 
Global Area Network: red 
global 
### 🔵 Escala planetaria real 
Todo el planeta 
Internet (GAN) 
Red de redes; ejemplo 
real y masivo de GAN

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
 
 
+ Info 
La tecnología actual permite conectar dispositivos a más de un 
metro de distancia (por ejemplo, con Bluetooth). 
Por lo tanto, consideraremos que los elementos que se 
interconectan dentro de una misma habitación forman una red 
PAN y no LAN. 
 
 
Por lo tanto, los principales tipos son: 
- PAN.
- LAN.
- MAN.
- WAN.
- GAN (Global Area Network) o Interredes.
 
Fuente: (https://es.wikipedia.org/wiki/Archivo:Tipos_de_redes.jpg) 
##### 5.1.1.1. Personal Area Network (PAN)
Las redes de área personal, generalmente llamadas PAN (Personal Area Network) permiten a los 
dispositivos comunicarse dentro del rango de una persona. 
Para llevar a cabo un intercambio de datos, los terminales modernos como smartphones, tablets, 
ordenadores portátiles o equipos de escritorio permiten asociarse ad hoc a una red.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Esto puede realizarse por cable, adoptando la forma de una red PAN. 
La variante inalámbrica se denomina WPAN (Wireless Personal Area Network) y se basa en \nespecificaciones como: 
- Bluetooth LE.
- Wireless USB.
- Insteon.
- IrDA.
- ZigBee.
- Z-Wave.
- Etc.
 
 
 
 
+ Info 
Piconet es una WLAN que utiliza conexiones Bluetooth. 
Puede constar de dos a siete dispositivos habilitados para 
Bluetooth, (electrodomésticos, etc.) 
Siempre debe haber un dispositivo "maestro", y el resto serán 
"esclavos". 
A un grupo de piconets se le llama scatternet (Dispersión, por ello 
se les llama también redes de dispersión). 
El periférico, como maestro, se encarga de escoger el hop 
adecuado para mantener el enlace y establece conexiones en las 
que un paquete de datos ocupa un slot para la emisión y otro para 
la recepción que pueden ser usados alternativamente, dando lugar 
a un esquema de tipo TDD (Time Division Dúplex). 
La secuencia única de salto de frecuencia del canal está 
determinada por la identidad del maestro de la piconet (un código 
único para cada equipo), y por su frecuencia de reloj. 
Para que una unidad esclava pueda sincronizarse con una unidad 
maestra, esta debe añadir un ajuste a su propio reloj nativo y así 
poder compartir la misma portadora de salto.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
El ámbito de acción de las redes PAN y WPAN es de unos pocos metros, y no son aptas para conectar 
dispositivos que se encuentran en habitaciones diferentes. 
Además de establecer la comunicación entre cada uno de los dispositivos entre sí, las redes de área 
personal (Personal Area Networks) permiten la conexión con otras redes de mayor tamaño. 
En este caso se puede hablar de un uplink o de un enlace o conexión de subida. 
Debido al alcance limitado y a una tasa de transmisión de datos relativamente baja, las PAN se utilizan 
principalmente para conectar periféricos. 
 
 
 
 
Ejemplo 
- Conectar un ratón y un teclado inalámbricos al ordenador.
- Conectar el móvil a la radio del coche.
- Conectar unos auriculares a un teléfono móvil.
- Mando a distancia de un televisor.
 
 
En el marco del Internet of Things (IoT), las redes WPAN se utilizan para la domótica y la 
automatización del hogar. 
Para ello utiliza protocolos diseñados especialmente para este fin como Insteon, Z-Wave y ZigBee. 
Las redes PAN también se pueden construir con otras tecnologías que se comunican dentro de rangos 
cortos, como: 
- Near-field communication (NFC) o comunicación de campo cercano es una tecnología de comunicación inalámbrica, de corto alcance y alta frecuencia que permite el intercambio de 
datos entre dispositivos. 
- RFID (identificación por radiofrecuencia) que se usa en tarjetas inteligentes o en los libros de las bibliotecas. 
- Redes infrarrojas.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Ejemplo de red PAN 
##### 5.1.1.2. Local Area Network (LAN)
Una red local puede incluir a dos o más dispositivos en una vivienda privada o a varios miles de 
dispositivos en una empresa. 
Asimismo, las redes en instituciones públicas como administraciones, colegios o universidades también 
son redes LAN. 
También se incluyen en este tipo las SOHO, acrónimo de Small Office-Home Office (Pequeña Oficina-
Oficina en Casa). Es un término que se aplica para denominar a los aparatos destinados a un uso 
profesional o semiprofesional pero que, a diferencia de otros modelos, no están pensados para asumir 
un gran volumen de trabajo. 
 
 
 
 
+ Info 
A las redes de campus también se les denomina CAN (Campus 
Area Network).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Una tecnología de red es la aplicación práctica de un estándar en el que se definirían formato de los 
datos, protocolos de comunicación, topología de red y velocidad de transmisión. Cuando hablamos de 
una red Ethernet, nos referimos a la tecnología de red de área local que cumple con las especificaciones 
del IEEE 802.3. A continuación citamos otras tecnologías LAN menos comunes y ya obsoletas que 
tienen sus propios estándares. 
- ARCNET.
- FDDI.
- Token Ring.
La transmisión de datos tiene lugar o bien de manera electrónica a través de cables de cobre o mediante 
fibra óptica de vidrio. 
Si se conectan más de dos ordenadores en una red LAN, se necesitan otros componentes de red como 
concentradores (hubs), puentes (bridges) y conmutadores (switches) los cuales funcionan como \nelementos de acoplamiento y nodos de distribución. 
También pueden utilizar un enrutador para la salida a internet. 
Las redes LAN permiten una transmisión rápida de grandes cantidades de datos. 
Además, las redes LAN permiten un intercambio de información cómodo entre los diversos dispositivos 
conectados a la red. 
Por ello, en el entorno empresarial es habitual que varios equipos de trabajo puedan acceder a 
servidores de archivos comunes, a impresoras de red o a aplicaciones por medio de la red LAN. 
WLAN (WIFI) 
WLAN (Wireless Local Area Network red de área local inalámbrica) es una LAN formada por conexiones 
inalámbricas. 
Los fundamentos básicos de las redes WLAN se definen en las normas IEEE 802.11. 
Las redes locales inalámbricas ofrecen la posibilidad de integrar terminales cómodamente en una red 
doméstica o empresarial y son compatibles con redes LAN Ethernet. 
El rendimiento es menor que el de una conexión Ethernet. 
El alcance de una Local Area Network depende del estándar usado como del medio de transmisión y se 
puede aumentar mediante el uso de repetidores.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 VLAN 
El estándar IEEE 802.3, comúnmente conocido como Ethernet, es hasta ahora el tipo más común de 
LAN alámbrica. 
Sin embargo, es posible dividir una gran LAN física en dos o más redes LAN lógicas más pequeñas 
denominadas LAN virtual o VLAN. 
Esto es útil cuando se quieren aislar dos segmentos de la red, por ejemplo, cuando la distribución del \nequipo de red no coincide con la estructura de la organización. 
De esta forma, los paquetes de difusión que se envíen por una red lógica no se reciben por los equipos 
del resto de redes lógicas (aunque estén en la misma red física). 
 
 
 
 
### 🔵 Ejemplo 
Los departamentos de informática y personal de una empresa 
podrían tener ordenadores en la misma LAN física debido a que se \nencuentran en la misma ala del edificio. 
Sería más sencillo administrar el sistema si cada departamento 
tuviera su propia red lógica. 
Si una persona de informática necesita enviar información a todo 
su departamento, podrá hacerlo sin tener que involucrar a los de 
personal, aun estando en la misma red física. 
 
### 🔵 Asignación del canal 
Las redes inalámbricas y las alámbricas se pueden dividir en diseños estáticos y dinámicos, dependiendo 
de la forma en que se asigna el canal. 
- Estáticos.
Consiste en dividir el tiempo en intervalos y utilizar un algoritmo por turnos (como Round-
Robin) para que cada máquina pueda difundir los datos en su turno durante un intervalo de 
tiempo. 
Su principal problema es que se desperdicia la capacidad del canal cuando una máquina que lo 
tiene asignado no necesita utilizarlo.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Dinámicos. Es el más utilizado. Hay dos métodos:
- Centralizados.
Existe una entidad central que determina el turno de cada dispositivo. 
Para ello acepta los paquetes a enviar y les asigna prioridades en base a algún algoritmo o 
función interna. 
- Descentralizados.
No hay una entidad central. Cada máquina decide por su cuenta cuando transmitir. 
Hay que utilizar algoritmos para evitar colisiones. 
 
Ejemplo de red LAN. Fuente: (https://en.wikipedia.org/w/index.php?curid=7654281) 
##### 5.1.1.3. Metropolitan Area Network (MAN)
Una red de área metropolitana (Metropolitan Area Network o MAN) es una red de telecomunicaciones 
de banda ancha que comunica varias redes LAN en una zona geográficamente cercana. 
 
 
 
 
### 🔵 Ejemplo 
El ejemplo más popular de una MAN es el de las redes de televisión 
por cable disponibles en muchos pueblos o ciudades.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Puede tratarse de cada una de las sedes de una empresa que se agrupan en una MAN por medio de 
líneas arrendadas. 
Para ello se utilizan enrutadores de alto rendimiento basados en fibra de vidrio (fibra óptica), los cuales 
permiten un rendimiento mayor al de Internet. 
La velocidad de transmisión entre dos puntos de unión distantes usando fibra de vidrio es comparable a 
la comunicación que tiene lugar en una red LAN. 
Para una red MAN, la red Metro Ethernet supone una técnica especial de transmisión con la que se 
pueden construir redes MEN (Metro Ethernet Network) sobre la base de Carrier Ethernet (CE 1.0) o 
Carrier Ethernet 2.0 (CE 2.0). 
### 🔵 MAN inalámbricas 
 
El estándar para redes inalámbricas regionales de mayor envergadura (Wireless Metropolitan Area 
Networks o WMAN) está regido por los estándares IEEE 802.16. 
Esta tecnología de WiMAX (Worldwide Interoperability for Microwave Access) permite crear las 
llamadas redes WLAN hotzones, que consisten en varios puntos de acceso WLAN interconectados en 
diferentes localizaciones. 
Las redes WMAN se utilizan para ofrecer a los usuarios una potente conexión a Internet en aquellas 
regiones que carecen de infraestructura para ello. 
### 🔵 WIMAX 
WiMAX (Worldwide Interoperability for Microwave Access o interoperabilidad mundial para acceso por 
microondas) es una norma de transmisión de datos que utiliza las ondas de radio en las frecuencias de 
2,5 a 5,8 GHz y puede tener una cobertura hasta de 70 km.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Permite la recepción de datos por microondas y retransmisión por ondas de radio. 
Esta tecnología está definida en el estándar IEEE 802.16. 
Una de sus ventajas es dar servicios de banda ancha en zonas donde el despliegue de cable o fibra por la 
baja densidad de población presenta unos costos por usuario muy elevados (zonas rurales). 
El único organismo habilitado para certificar el cumplimiento del estándar y la interoperabilidad entre \nequipamiento de distintos fabricantes es el Wimax Forum. 
 
Fuente: 
(https://sco.m.wikipedia.org/wiki/File:
WiMAX_Forum_logo.svg) 
##### 5.1.1.4. Wide Area Network (WAN)
 
Fuente: (https://commons.wikimedia.org/wiki/File:Lanwan.gif)

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Una red WAN (Wide Area Networks o redes de área extensa) se extiende por zonas geográficas como 
países o continentes. 
El número de redes locales o terminales individuales que forman parte de una WAN es, en principio, 
ilimitado. 
Las redes LAN y las MAN se pueden establecerse a causa de la cercanía geográfica del ordenador o red 
que se tiene que conectar usando Ethernet. 
Este no es el caso de las redes WAN, en el que se tienen que utilizar técnicas como: 
- IP/MPLS (Multiprotocol Label Switching).
- PDH (Plesiochronous Digital Hierarchy).
- SDH (Synchronous Digital Hierarchy).
- SONET (Synchronous Optical Network).
- ATM (Asynchronous Transfer Mode).
- X.25 (rara vez. Está obsoleto).
En la mayoría de los casos, las Wide Area Networks suelen pertenecer a una organización determinada 
o a una empresa y se gestionan o alquilan de manera privada. 
Los proveedores de servicios de Internet también hacen uso de este tipo de redes para conectar las 
redes corporativas locales y a los consumidores a Internet. 
Existen dos variedades de redes WAN que resultan interesantes: 
- Línea dedicada.
La empresa alquila una línea que se utilizará para conectar dos redes situadas en lugares 
geográficamente muy distantes. 
De esta forma se crea una WAN a partir de 2 redes de cualquier tipo (incluso WAN). 
- VPN (Red privada virtual). Realiza lo mismo, pero utilizando internet como medio.
Es más barato. 
Menos prestaciones que la línea dedicada. 
Suelen cifrarse para garantizar la confidencialidad de los datos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:Virtual_Private_Network_overview.svg) 
5.1.1.4.1. Low Power Wide Area Network 
LPWAN (Low Power Wide Area Network) es una tecnología de red diseñada para conectar dispositivos 
que necesitan enviar pequeñas cantidades de datos a largas distancias, con un consumo de energía \nextremadamente bajo. Es ideal para aplicaciones de IoT (Internet of Things), como sensores, 
rastreadores y dispositivos industriales. Las principales características incluyen bajo consumo \nenergético, larga cobertura (hasta 15 km o más), baja velocidad de transmisión de datos y escalabilidad 
para conectar una gran cantidad de dispositivos. Además, su bajo costo en infraestructura y hardware la 
hace especialmente atractiva para aplicaciones a gran escala. 
Principales tecnologías y aplicaciones: 
Entre las tecnologías más populares de LPWAN se encuentran LoRa/LoRaWAN, Sigfox, NB-IoT y LTE-
M, cada una con ventajas específicas. 
LoRaWAN es flexible y libre de licencias, ideal para redes privadas o públicas. 
Sigfox opera bajo una infraestructura centralizada y ofrece cobertura global. 
NB-IoT y LTE-M son variantes basadas en redes celulares con espectro licenciado, adecuadas para 
dispositivos que requieren mayor penetración y conectividad estable. Estas tecnologías se aplican en 
sectores como ciudades inteligentes (monitoreo ambiental, iluminación pública), agricultura (sensores 
de humedad, rastreo de ganado), IoT industrial (mantenimiento predictivo) y logística (rastreo de 
paquetes y contenedores).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Ventajas, desventajas y factores clave para elegir LPWAN: 
Entre las ventajas de LPWAN destacan la larga vida útil de las baterías, amplia cobertura y su coste 
reducido para implementaciones masivas. Sin embargo, presenta limitaciones en la velocidad de 
transmisión de datos y no es adecuada para aplicaciones con altos requisitos de ancho de banda. 
También puede requerir infraestructura específica, como antenas o gateways. Al seleccionar una 
tecnología LPWAN, es importante considerar la cobertura geográfica, el consumo energético, el 
volumen de datos necesario, los costos y la interoperabilidad con otros sistemas. 
##### 5.1.1.5. Global Area Network (GAN)
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:R%C3%A9pr%C3%A9senta tion_d%27internet.jpg) 
Una red global como Internet recibe el nombre de Global Area Network (GAN). 
Sin embargo, no es la única red de ordenadores de esta índole. 
Las empresas que también son activas a nivel internacional mantienen redes aisladas que comprenden 
varias redes WAN y que logran, así, la comunicación entre los ordenadores de las empresas a nivel 
mundial. 
Las redes GAN utilizan la infraestructura de fibra de vidrio de las redes de área amplia (Wide Area 
Networks) y las agrupan mediante cables submarinos internacionales o transmisión por satélite.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
#### 🔹 5.1.2. Según su arquitectura
Podemos clasificarlas en redes conmutadas y redes de difusión 
Lo estudiamos a continuación. 
##### 5.1.2.1. Tipo de red: conmutación
(Redes conmutadas o redes de conmutación). 
La Conmutación consiste en establecer un canal entre un emisor y un receptor a través de nodos o \nequipos de transmisión. 
La conmutación permite la entrega de la señal desde el origen hasta el destino. 
### 🔵 Encaminamiento 
En las redes de conmutación existe más de un camino entre dos estaciones dadas y hay que determinar 
cuál es la ruta de encaminamiento óptima para el intercambio de información. 
Los protocolos que proporcionan técnicas para encaminar la información y que además proporcionan 
mecanismos para compartir la información de encaminamiento son los denominados protocolos de \nencaminamiento. 
Los métodos de encaminamiento se pueden clasificar en función de la adaptabilidad a los cambios en: 
- No adaptativos (estáticos).
Las tablas de encaminamiento de los nodos se configuran manualmente y permanecen fijas 
hasta que se vuelve a actuar sobre ellas. 
- Adaptativos (dinámicos).
Se distinguen tres tipos de métodos: 
- Adaptativos centralizados.
Todos los nodos se consideran iguales excepto uno, el nodo central. 
El nodo central cuenta con información de todos los nodos y se encarga de formar la tabla 
de enrutamiento de cada uno de ellos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Adaptativos aislados.
En cada nodo sólo se cuenta con información local. 
Cada vez que un nodo recibe un paquete que no es para él lo reenvía por todos los enlaces \nexcepto por el que llegó. 
Los principales métodos de encaminamiento adaptativo aislado son los algoritmos de 
inundación y de estado de enlaces. 
- Adaptativos distribuidos.
Son los más utilizados. 
Todos los nodos envían y reciben información de control de sus vecinos y calculan su tabla 
de encaminamiento. 
El control de encaminamiento es distribuido. 
Entre los métodos de encaminamiento adaptativo distribuido se encuentran los algoritmos 
de vector de distancias. 
X.25 
Es un conjunto de protocolos que define una recomendación internacional de la ITU-T tanto para el 
intercambio de datos como para el control de la información entre un DTE (equipo terminal de datos) y 
un DCE (equipo terminal del circuito de datos) de una red de conmutación de paquetes. 
La velocidad típica de una red X.25 está entre 9,6-64 Kbps. 
La capacidad de transferencia de datos de la línea X.25 puede estar compartida entre un número de 
sesiones diferentes. 
Cada sesión constituye lo que se llama un circuito virtual que puede ser: 
- Circuito Virtual Conmutado (SVC o Switched Virtual Circuit).
Son conexiones temporales utilizadas para transferencias de datos esporádicas. 
Requieren que cada vez que dos dispositivos DTE necesitan comunicarse se establezca, 
mantenga y termine una conexión. 
- Circuito Virtual Permanente (PVC o Permanent Virtual Circuit).
Son conexiones establecidas de forma permanente utilizadas para transferencias de datos 
frecuentes. 
No necesitan que se establezca o termine la conexión porque estará siempre activa.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
X.25 tiene tres niveles que se corresponden con las tres primeras capas de la arquitectura de siete 
niveles del modelo de referencia OSI de ISO: 
- Nivel físico.
Especifica las características mecánicas, eléctricas, funcionales y de procedimiento que son 
necesarias para activar, mantener y terminar una conexión física entre un DTE y un DCE. 
Las recomendaciones especificadas más utilizadas son X.21 y X.21 bis. 
- Nivel de enlace.
Especifica el procedimiento de acceso al enlace para el intercambio de datos a través del enlace 
físico. 
El nivel de enlace garantiza una transferencia fiable de los datos entre el DTE y el DCE, 
transmitiendo los datos como una secuencia de tramas. 
El protocolo más utilizado es LAP-B. 
- Nivel de paquete.
Gobierna la comunicación extremo a extremo, entre los diferentes DTEs. 
Crea unidades de datos de red, denominados paquetes, que contienen información de control y 
datos de usuario. 
Proporciona los procedimientos para: 
- El manejo de los SVC (Circuitos Virtuales Conmutados) y PVC (Circuitos Virtuales
Permanentes). 
- El establecimiento y liberación de llamada.
- Control de flujo y tratamiento de errores.
Frame Relay (FR) 
Se diseñó originalmente para operar con las interfaces de RDSI, pero en la actualidad se usa también 
sobre otras interfaces de red. 
Frame Relay es un ejemplo de tecnología de conmutación de paquetes que se considera como una \nevolución de X.25 y un paso de transición hacia ATM. 
Consigue rendimientos superiores a los de X.25 entre otras razones porque elimina la mayoría de los 
controles de errores.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Soporta velocidades de transmisión de hasta 45 Mbps, aunque las implementaciones típicas no pasan de 
1.5/2 Mbps. 
Frame Relay es también un sistema orientado a conexión, que de manera similar a X.25 utiliza SVC o 
PVC (normalmente PVC). 
Los circuitos virtuales ofrecen una trayectoria de comunicación bidireccional de un dispositivo DTE a 
otro y se identifican de manera única por medio del DLCI (Data Link Connection Identifier o 
identificador de canal del circuito establecido). 
Además, se pueden multiplexar muchos circuitos virtuales en un único circuito físico. 
Tanto para PVC como para SVC se distinguen dos interfaces: 
- UNI (interfaz de usuario red).
Se establece entre el dispositivo de acceso a la red del usuario y un conmutador de la red. 
- NNI (interfaz red a red).
Se establece entre dos conmutadores que pueden ser de la misma o de diferentes redes Frame 
Relay. 
### 🔵 ATM 
ATM (Asyncronous Transfer Mode o modo de transferencia asíncrona) es también una tecnología de 
conmutación de paquetes orientada a conexión. 
Crea circuitos virtuales (denominados Canales Virtuales en ATM) entre los sistemas que desean 
intercambiar información. 
En ATM los circuitos virtuales (VC o Virtual Circuit) se agrupan entre dos nodos terminales en los 
denominados caminos o trayectos virtuales (VP o Virtual Path). 
Tanto los circuitos virtuales como los caminos virtuales se numeran para su identificación. 
Los paquetes de ATM se denominan celdas y tienen una longitud fija de 53 bytes: 
- 5 bytes de cabecera.
- 48 bytes de carga útil.
En ATM se han definido las llamadas categorías de servicio. 
Cada una de ellas proporciona un nivel de garantía diferente respecto a la disponibilidad de los recursos 
de red solicitados.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Se han definido cuatro categorías de servicio: 
- CBR (Constant Bit Rate).
- VBR (Variable Bit Rate).
- ABR (Available Bit Rate).
- UBR (Unspecified Bit Rate).
Una de las grandes virtudes de ATM es la posibilidad de establecer una Calidad de Servicio (QoS, Quality 
of Service) garantizada. 
En las redes ATM se pueden establecer una larga serie de parámetros que definen los niveles mínimos 
de calidad que el operador debe ofrecer al usuario para cada una de las categorías de servicio. 
Estos parámetros se pueden clasificar en dos grupos: 
- Parámetros de tráfico.
- Parámetros de QoS.
El modelo de capas de ATM está formado por tres capas 
- Capa física.
Controla la transmisión y recepción de bits en el medio físico y mantiene el rastro de los límites de 
las celdas y de los paquetes de celdas dentro del tipo de trama apropiado al medio físico utilizado. 
Está dividida en: 
- Subcapa dependiente del medio físico.
- Subcapa de convergencia de transmisión.
- Capa ATM.
Es responsable del establecimiento de las conexiones y del paso de las celdas a través de la red ATM. 
- Capa de adaptación ATM (AAL).
Adapta los distintos tipos de tráfico para su transporte por las redes ATM. 
Hay 5 protocolos ALL: 
- ALL1.
- ALL2.
- ALL3.
- ALL4.
- ALL5.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 MPLS 
La conmutación de etiquetas multiprotocolo (MPLS o Multiprotocol Label Switching) es un estándar de 
transporte de datos creado por la IETF y definido en el RFC 3031. 
Opera entre la capa de enlace de datos y la capa de red del modelo OSI. 
Fue diseñado para unificar el servicio de transporte de datos para las redes basadas en circuitos y las 
basadas en paquetes. 
MPLS reemplazó a Frame Relay y ATM como la tecnología preferida para llevar datos de alta velocidad 
y voz digital en una sola conexión. 
La conmutación de etiquetas multiprotocolo es una forma de asegurar conexiones fiables para 
aplicaciones en tiempo real. 
La conmutación de etiquetas de protocolo múltiple (MPLS) establece rutas predeterminadas y 
altamente eficientes. 
Con MPLS, la primera vez que un paquete ingresa a la red, se asigna a una clase de equivalencia de 
reenvío específica (FEC), que se indica al agregar una secuencia de bit corto (la etiqueta) al paquete. 
Cada enrutador de la red tiene una tabla que indica cómo manejar los paquetes de un tipo de FEC \nespecífico, por lo que una vez que el paquete ha ingresado a la red, los enrutadores no necesitan realizar 
un análisis de encabezado. 
En cambio, los enrutadores posteriores usan la etiqueta como un índice en una tabla que les 
proporciona un nuevo FEC para ese paquete. 
Esto le da a la red MPLS la capacidad de manejar paquetes con características particulares (tales como 
provenientes de puertos particulares o que transportan tráfico de tipos de aplicaciones particulares) de 
manera consistente. 
Los paquetes que transportan tráfico en tiempo real, como voz o video, se pueden asignar fácilmente a 
rutas de baja latencia en toda la red, algo que es difícil con el enrutamiento convencional. 
El punto clave de la arquitectura es que las etiquetas proporcionan una forma de adjuntar información 
adicional a cada paquete, información que va más allá de lo que los enrutadores tenían previamente. 
MPLS no está ligada a ninguna tecnología subyacente. 
Fue diseñado en los días de ATM y frame relay como una técnica de superposición diseñada para 
simplificar y mejorar el rendimiento mediante el protocolo múltiple. 
El ATM y el frame relay están obsoletos, pero MPLS sigue vivo en las redes troncales de los operadores 
y en las redes empresariales.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Elementos de MPLS: 
- LER (Label Edge Router o enrutador frontera de etiquetado): elemento que inicia o termina el túnel (extrae e introduce cabeceras). Es decir, el elemento de entrada/salida a la red MPLS. 
Existen tanto enrutadores de entrada como de salida de la red. Ambos suelen denominarse 
router frontera ya que se encuentran en los extremos de la red MPLS. 
- LSR (Label Switching Router o enrutador de conmutación de etiquetas).
- LSP (Label Switched Path o intercambio de rutas por etiqueta) nombre genérico de un camino
MPLS (para cierto tráfico o FEC), es decir, del túnel MPLS establecido entre los extremos. A 
tener en cuenta que un LSP es unidireccional. 
- LDP (Label Distribution Protocol o protocolo de distribución de etiquetas): un protocolo para la distribución de etiquetas MPLS entre los equipos de la red. 
- FEC (Forwarding Equivalence Class o clase de equivalencia de reenvío): nombre que se le da al tráfico que se encamina bajo una etiqueta. Subconjunto de paquetes tratados del mismo modo 
por el conmutador. 
Los casos de uso más comunes son: 
- Sucursales.
- Redes de campus.
- Servicios Ethernet metropolitanos.
- Empresas que necesitan calidad de servicio (QoS) para aplicaciones en tiempo real.
Existen tres tipos de tecnologías de conmutación 
- Conmutación de mensajes.
- Conmutación de circuitos.
- Conmutación de paquetes.
5.1.2.1.1. Conmutación de mensajes 
Es muy poco utilizada. 
Para transmitir un mensaje a un receptor se realizan los siguientes pasos: 
- El emisor debe enviar primero el mensaje completo a un nodo intermedio el cual lo encola en la cola donde almacena los mensajes que le son enviados por otros nodos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- A continuación, cuando llega su turno, lo reenviará a otro y éste a otro y así las veces que sean necesarias antes de llegar al receptor. 
- El mensaje deberá ser almacenado por completo y de forma temporal en el nodo intermedio antes de poder ser reenviado al siguiente, por lo que los nodos temporales deben tener una gran 
capacidad de almacenamiento. 
Características de la conmutación de mensajes: 
- La conmutación de mensaje presenta un mejor aprovechamiento del canal de transmisión comparado con la conmutación de circuito y por paquetes. 
- Se unen los mensajes de orígenes diferentes que van hacia un mismo destino, y viceversa, todos al mismo tiempo sin necesidad de esperar a que se libere el circuito, esto provoca que el canal se 
libere mucho antes que, en la conmutación de circuitos, lo que reduce el tiempo de espera 
necesario para que otro remitente envíe mensajes. 
- El tamaño del mensaje es mayor en la conmutación de mensaje ya que se añade información \nextra de encaminamiento lo que implica:
- Disminución del rendimiento del canal.
- Mayor complejidad en los nodos intermedios.
- Es necesario contar con capacidad de almacenamiento para poder verificar y retransmitir el mensaje completo. 
- En caso de que la capacidad de almacenamiento se agote y llegue un nuevo mensaje, no puede ser almacenado y se perderá definitivamente. 
5.1.2.1.2. Conmutación de circuitos 
Se establece un circuito para la comunicación entre dos usuarios que piden el intercambio de 
información. Este circuito es asignado durante todo el tiempo que dura la comunicación. 
No resulta muy eficiente para el intercambio de datos. 
Hay dos tipos básicos: 
- Conmutación por división en el espacio.
En un conmutador por división en el espacio las rutas que se establecen son físicamente 
independientes. 
Cada conexión requiere el establecimiento de un camino físico a través del conmutador. 
El bloque básico de un conmutador de este tipo consiste en una matriz de conexiones, puertas 
semiconductoras o puntos de cruce que son habilitadas o deshabilitadas por la unidad de control 
del conmutador.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Conmutación por división en el tiempo.
La conmutación por división en el tiempo implica la partición de la cadena de bits de menor 
velocidad en fragmentos que compartirán una cadena de mayor velocidad con otras líneas de \nentrada. 
Los fragmentos se manipulan por lógica de control para encaminar los datos desde la entrada 
hasta la salida. 
Una de las técnicas más utilizadas de conmutación por división en el tiempo es la conmutación 
mediante bus TDM. 
Esta técnica se basa en la en la utilización de la multiplexación por división en el tiempo (TDM) 
síncrona, la cual permite que varias cadenas de bits de baja velocidad compartan una línea de 
alta velocidad. 
5.1.2.1.3. Conmutación de paquetes 
Los mensajes que se quieren comunicar se dividen en partes denominados paquetes. Estos son 
transmitidos al conmutador y almacenados en una cola en espera para su envío (store and forward). 
En la conmutación de paquetes se distinguen dos modos: 
- Datagrama.
Cada paquete se trata como una entidad independiente y es encaminado individualmente a 
través de la red. 
La cabecera de cada paquete contiene información completa acerca de su destino. 
- Circuito virtual.
- La transmisión requiere una fase de configuración en cada nodo involucrado antes de que se transfiera cualquier paquete para establecer los parámetros de comunicación. 
- Los paquetes incluyen un identificador de conexión en lugar de información de dirección.
- Los paquetes se negocian entre puntos finales para que se entreguen en orden y con verificación de errores. 
- La información de dirección solo se transfiere a cada nodo durante la fase de configuración de la conexión, cuando se descubre la ruta al destino y se agrega una entrada a la tabla de 
conmutación en cada nodo de red por el que pasa la conexión. 
- Los protocolos de señalización utilizados permiten a la aplicación especificar sus requisitos y descubrir los parámetros del enlace. 
- Se pueden negociar valores aceptables para los parámetros del servicio.
- Enrutar un paquete requiere que el nodo busque el ID de conexión en una tabla.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- El encabezado del paquete puede ser pequeño, ya que solo necesita contener este código y cualquier información, como la longitud, la marca de tiempo o el número de secuencia, que \nes diferente para los distintos paquetes. 
- El protocolo utilizado para transporte es TCP.
- TCP garantiza que todos los datos lleguen correctamente y en orden.
- Ejemplos de tecnologías de conmutación de paquetes de circuito virtual son X.25, Frame
Relay y ATM. 
##### 5.1.2.2. Tipo de red: redes de difusión
Las redes de difusión tienen un solo canal de difusión compartido por todas las máquinas de la red. 
Los paquetes que envía una máquina son recibidos por todas las demás. 
Un campo de dirección dentro del paquete indica a quien se dirige (o si se dirige a todos). 
Al recibir un paquete, una máquina verifica el campo de dirección. Si el paquete está dirigido a ella, lo 
procesa; y si no lo ignora. 
En las redes de difusión, la comunicación se realiza siempre en un único sentido (de uno o varios \nemisores a uno o varios receptores) y no se espera respuesta. 
 
 
 
 
+ Info 
Un ejemplo de difusión sería una lista de correo de noticias que \nenvía a sus subscriptores correos con las nuevas noticias. 
Obviamente no esperan respuesta a dichos correos y si las hubiera, 
no se procesarían. 
 
## 🟣 6. Equipos terminales
Tenemos dos tipos de Equipos Terminales: 
- Equipo terminal de datos.
- Equipo terminal del circuito de datos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Un equipo terminal de datos (ETD) 
También llamado DTE, del inglés Data Terminal Equipment. 
Es cualquier equipo informático, independientemente de que sea receptor o emisor final de datos. 
Los ETD se encargan de transmitir y recibir bits uno a uno. 
Es aquel componente del circuito de datos que hace de fuente o destino de la información. Por ejemplo, 
una terminal de usuario, un ordenador o una impresora. 
En normas como la RS232C o X.25, el DTE es el lado de una interfaz que representa al usuario de los 
servicios de comunicación de datos. 
Podríamos definir dos tipos de DTE: 
- DTE fuente.
Emite datos contenidos, generalmente, en una unidad de almacenamiento. 
- DTE destino.
Recibe datos de forma directa o indirecta, sin alterar el contenido de los datos durante el 
proceso. 
Equipo terminal del circuito de datos (DCE) 
Un equipo terminal del circuito de datos (DCE o Data Circuit-Terminating Equipment) es un dispositivo 
que recibe información de un DTE y la convierte en la señal apropiada para, posteriormente, 
introducirla en el canal de comunicaciones. 
También realiza la operación inversa, es decir, recibe información del canal de telecomunicaciones y 
convierte la señal en información que traslada al DTE. 
Un ejemplo de dispositivo DCE es el módem. 
 
 
 
 
+ Info 
En ocasiones, los enrutadores y los hub pueden actuar como DTE o 
DCE. 
Incluso, en algunos casos, tienen un interruptor u opción a través 
de software para seleccionar si actúa como DTE o DCE.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Diversas organizaciones de referencia internacionales establecen, con el fin de lograr compatibilizar la 
operación de los equipos de diferentes fabricantes, normalizaciones funcionales y eléctricas de la 
interfaz existente entre el DTE y el DCE. 
Una norma para un interfaz define las siguientes especificaciones: 
- Mecánica/física.
Número de pines y tipo de conector. 
- Eléctrica.
Define los niveles de tensión de 0 y 1. 
- Funcional.
Diversas organizaciones de referencia internacionales establecen, con el fin de lograr compatibilizar la 
operación de los equipos de diferentes fabricantes, normalizaciones funcionales y eléctricas de la 
interfaz existente entre el DTE y el DCE. 
Las principales organizaciones de estandarización que participan en la normalización de estos interfaces 
son: 
- TIA (TelecommunicationsIndustryAssociation).
Desarrolla normas de cableado industrial para muchos productos de las telecomunicaciones y 
tiene más de 70 normas preestablecidas. 
- ANSI (American National Standards Institute).
Organización sin ánimo de lucro que supervisa el desarrollo de estándares para productos, 
servicios, procesos y sistemas en los Estados Unidos. 
ANSI es miembro de la Organización Internacional para la Estandarización (ISO) y de la 
Comisión Electrotécnica Internacional (International Electrotechnical Commission, IEC).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- EIA (Electronic Industries Alliance).
Es una organización formada por la asociación de las compañías electrónicas y de alta 
tecnología de los Estados Unidos. 
Su misión es promover el desarrollo de mercado y la competitividad de la industria de alta 
tecnología de los Estados Unidos. 
- ISO (International Standards Organization).
Es una organización para la creación de estándares internacionales compuesta por diversas 
organizaciones nacionales de estandarización. 
- IEEE (Instituto de Ingenieros Eléctricos y de Electrónica).
Su principal aportación son las normas IEEE 802 (Ej. 802.11 para el funcionamiento de una red 
de área local inalámbrica). 
 
 
 
 
### 🔵 Atención 
Las normativas y protocolos avanzan continuamente, haciendo 
que otras se queden obsoletas. 
 
## 🟣 7. Equipos de interconexión y conmutación
El objetivo de la interconexión de redes es dar un servicio de comunicación de datos que involucre 
diversas redes con diferentes tecnologías de forma transparente para el usuario. 
Este concepto hace que las cuestiones técnicas particulares de cada red puedan ser ignoradas al diseñar 
las aplicaciones que utilizarán los usuarios de los servicios. 
Los dispositivos de interconexión de redes sirven para superar las limitaciones físicas de los elementos 
básicos de una red. 
Vamos a estudiar los siguientes dispositivos: 
- Repetidor.
- Concentrador (Hub).
- Conmutador (Switch).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Puente (Bridge).
- Enrutador (Router).
- Compuerta (Gateway) Repetidor.
Estos dispositivos de red operan en las siguientes capas de los modelos ISO/OSI y TCP/IP: 
### 🔵 Dispositivo de red 
Capa OSI 
Capa TCP/IP 
### 🔵 Repetidor 
Física 
Hardware (no capa) 
Concentrador (Hub) 
### 🔵 Física 
Hardware (no capa) 
Conmutador (Switch) 
### 🔵 Enlace de Datos 
Acceso a la Red 
Puente (Bridge) 
### 🔵 Enlace de Datos 
Acceso a la Red 
Enrutador (Router) 
### 🔵 Red 
Internet 
Compuerta (Gateway) 
Transporte y/o Sesión 
Transporte 
### 🔵 7.1. Repetidor
 
Fuente: 
(https://de.m.wikipedia.org/wiki/Datei:Repea ter_netz.png) 
Un repetidor es un dispositivo que une dos segmentos del mismo tipo de red. 
Características: 
- Los cables que une pueden ser de tipos diferentes (por ejemplo, coaxial y fibra óptica).
- Se encarga de amplificar, regenerar y re-temporizar la señal.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Permite que los bits viajen a mayor distancia a través de los medios.
- No entiende de formatos, simplemente copia cualquier señal eléctrica (incluido ruido e interferencias). 
- No filtra tráfico de Red.
### 🔵 7.2. Concentrador (Hub)
 
Un hub es un dispositivo que actúa como punto de conexión central entre los nodos que componen 
una red. 
Posee una topología física en estrella, pero lógica de bus. 
Los equipos conectados al hub son miembros de un mismo segmento de red y comparten el ancho de 
banda del hub para sus comunicaciones. 
Son repetidores multi-puertos, interconectando varios dispositivos de forma económica y sencilla. 
Ventaja: aumenta la confiabilidad de la red, ya que si cualquier cable falla no afecta a la red. 
Desventaja: transmite por difusión, por lo que se producen colisiones. 
### 🔵 Tipos 
Existen dos tipos de hub: 
- Activos.
Realizan la regeneración de la señal que reciben antes de ser enviada. 
- Pasivos.
No regeneran la señal. Simplemente interconectan los dispositivos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Funcionamiento 
Cuando un equipo envía un mensaje, los datos llegan al hub y éste los regenera (si es activo) y los 
retransmite a todos sus puertos, excepto al puerto que emite el mensaje. 
El hub no divide dominios de colisión, ni dominios de broadcast. 
 
 
 
 
+ Info 
- Dominio de colisión.
Son segmentos de la red que comparten el mismo ancho de 
banda. 
Cuando dos o más dispositivos, que comparten el mismo 
segmento, intentan comunicarse al mismo tiempo pueden 
ocurrir colisiones. 
- Dominio de broadcast.
Contiene todos los dispositivos que pueden ser 
alcanzados por un broadcast (mensaje para todos los 
miembros de la red). 
 
### 🔵 7.3. Conmutador (Switch)
 
Es un dispositivo que permite la interconexión de dispositivos entre sí. 
Características 
- Permite segmentar una red para aumentar su rendimiento a nivel de enlace.
- A diferencia de los puentes, los switch sólo permiten conectar redes que utilicen los mismos protocolos a nivel físico y de enlace.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Filtran y dirigen tramas entre los segmentos de la red de área local proporcionando un ancho de banda dedicado. 
- Conoce los dispositivos que tiene conectados a cada uno de sus puertos.
- Cuando se enchufa no conoce las direcciones de los dispositivos de sus puertos, las aprende a medida que circula información a través de él. 
- Un switch divide el dominio de colisiones. Tiene tantos dominios de colisión como bocas posea.
- Un switch no divide el dominio de broadcast, ya que la red segmentada se ve como una sola.
- Cuando un switch no conoce la dirección MAC de destino envía la trama por todos sus puertos, al igual que un HUB. 
- Cuando hay más de un ordenador conectado a un puerto de un switch este aprende sus direcciones MAC y cuando se envían información entre ellos no la propaga al resto de la red (a \nesto se llama filtrado). 
- Operan a velocidades mucho más altas que los puentes.
- Los datos pueden conducirse por rutas separadas, mientras que, en el hub, las tramas son conducidas por todos los puertos. 
#### 🔹 7.3.1. Indicadores LED en switches y tarjetas de red
En redes implementadas con Gigabit Ethernet, las tarjetas de red y los switches suelen contar con 
indicadores LED que reflejan el estado de la conexión y la velocidad de transmisión. 
Uno de los indicadores más comunes es el piloto de estado, que puede iluminarse en diferentes colores 
para señalar distintos estados de la conexión: 
- Verde fijo o intermitente: Indica que la conexión está operando a la velocidad máxima permitida por la red. 
- Naranja o ámbar intermitente: Puede indicar diversas situaciones, tales como:
- La tarjeta de red está funcionando a una velocidad inferior a la máxima soportada por la red
(por ejemplo, 100 Mbps en lugar de 1 Gbps). 
- El dispositivo está negociando la velocidad de conexión con el switch y aún no ha \nestablecido la velocidad óptima.
- Existen perturbaciones en la transmisión, como cables de baja calidad, interferencias \nelectromagnéticas o configuraciones incorrectas en los dispositivos de red.
- Rojo o apagado: Puede indicar una conexión defectuosa o la ausencia de conexión.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Posibles causas de un piloto naranja en una tarjeta de red 
Un indicador LED naranja o ámbar en una tarjeta de red puede ser señal de diversas situaciones que 
afectan el rendimiento de la conexión. Una de las causas más comunes es la incompatibilidad de 
velocidad, que ocurre cuando la tarjeta de red del dispositivo solo soporta 100 Mbps, mientras que la 
red está configurada para operar a 1 Gbps, lo que genera una reducción en la velocidad de transmisión. 
También puede deberse al uso de un cable inadecuado, como emplear un cable de categoría Cat 5 en 
lugar de Cat 5e o superior, lo que limita la capacidad de transmisión de datos y afecta el desempeño de 
la red. 
Otra posible causa es una configuración incorrecta de autonegociación, que impide que el switch y la 
tarjeta de red acuerden automáticamente la mejor velocidad de conexión disponible, estableciendo así 
una velocidad inferior a la óptima. Además, las interferencias electromagnéticas generadas por 
dispositivos eléctricos cercanos pueden degradar la señal, afectando la estabilidad de la conexión. 
Finalmente, un fallo en el hardware, ya sea en la tarjeta de red, en el switch o en un puerto defectuoso, 
también puede ser responsable de la activación del indicador LED en color ámbar o naranja. Ante esta 
situación, es recomendable realizar un diagnóstico para identificar la causa y aplicar la solución adecuada. 
### 🔵 Soluciones recomendadas 
Ante la presencia de un piloto naranja, se recomienda realizar las siguientes verificaciones: 
- Comprobar la categoría del cable Ethernet y asegurarse de que sea Cat 5e o superior.
- Revisar la configuración de autonegociación en la tarjeta de red y en el switch para garantizar que ambos dispositivos operen a la máxima velocidad posible. 
- Probar otro puerto en el switch o enrutador para descartar un problema en el puerto actual.
- Detectar posibles interferencias electromagnéticas en el entorno y reubicar los cables si es necesario. 
### 🔵 7.4. Puente (Bridge)

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Los puentes son dispositivos que pueden conectar a varias LAN entre sí. 
Características 
- Generalmente conectan LAN con idénticos protocolos de capa física y de acceso al medio (MAC).
- Deben tener una memoria temporal para albergar las tramas a intercambiar de LAN.
- Mantienen una tabla de direcciones físicas MAC para saber qué tramas van a una LAN o a otra.
- Desde el punto de vista de cada estación, todas las demás estaciones están en su misma LAN y \nes el puente el encargado de encaminar las tramas.
### 🔵 Funciones 
Las funciones de un puente son: 
- Dividir una red de área local en dos redes de menor tamaño.
Cuando una red de área local se hace demasiado grande en cuanto a número de nodos, debe ser 
dividida para mejorar su rendimiento. 
- Interconectar redes de área local.
Pueden tener protocolos de nivel de enlace o 
Ejemplo: Interconexión de una red inalámbrica a una de cable. 
- Controlar las tramas defectuosas.
### 🔵 Funcionamiento 
El puente entrará en funcionamiento, pasando la información, sólo cuando el nodo de un segmento \nenvíe información al nodo del segmento al otro lado del puente. 
Cada puente va almacenando en memoria una tabla de direcciones MAC asignada a cada uno de sus 
puertos. 
De esta manera, cuando llega una trama, comprueba la dirección MAC, la compara con el "mapa" que 
posee en memoria y la envía por el puerto adecuado.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Ventajas 
- Cuando se conectan varias LAN con puentes, el fallo en una LAN no implica el fallo en la otra.
- Varias LAN pequeñas tienen mayores prestaciones que una grande.
- Reduce el dominio de colisión.
- Las longitudes de cableado son menores.
- Cuando hay dos LAN separadas geográficamente, es más sencillo y barato conectarlas con un puente que usar cable coaxial. 
- Divide el dominio de colisión, pero no el dominio de broadcast.
### 🔵 7.5. Enrutador (Router)
 
Fuente: 
(https://es.wikipedia.org/wiki/Archivo:Linksys-
Wireless-G-Router.jpg) 
Es un dispositivo hardware o producto software que permite interconectar redes entre sí. 
Características 
- Como funciona a nivel de red, los protocolos de comunicación en los niveles superiores a ambos lados del enrutador deben ser iguales. 
- Toma decisiones lógicas con respecto a la mejor ruta para el envío de datos a través de una red interconectada. 
- Comparte información con otros enrutadores.
- Divide el dominio de colisión y de broadcast.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Funcionamiento 
Al recibir un paquete, debe extraer de éste la dirección del destinatario y decidir cuál es la mejor ruta. 
Para ello utiliza: 
- Un algoritmo de enrutamiento.
- Una tabla de enrutamiento.
- Sus propias direcciones a nivel de red.
Un enrutador necesita de una serie de parámetros básicos para que pueda funcionar correctamente: 
- Direcciones de los puertos y redes a las que está conectado.
- Algoritmos de enrutamiento que va a utilizar.
- Una tabla de enrutamiento.
El enrutador, para determinar la mejor ruta, utiliza la tabla de rutas y evalúa una métrica. 
La ruta escogida es aquella que tiene el menor valor de la métrica utilizada. 
 
 
 
 
+ Info 
La métrica es un valor generado por el enrutador o asignador por \nel administrador para cada ruta en base a una función que depende 
de diversos factores a los cuales se le asignan pesos para indicar 
que unos son más importantes que otros. 
Algunos factores pueden ser: 
- Ancho de banda.
- Retardo.
- Carga.
- Confiabilidad.
- Número de saltos.
- Coste.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Algoritmos de las tablas de enrutamiento 
- No adaptativos o estáticos.
No tienen en cuenta los cambios. 
Las rutas se calculan manualmente y luego se introducen en la tabla de rutas (inundación). 
- Adaptativos o dinámicos.
Tienen en cuenta los cambios de la topología y otros factores (vector de distancia, estado del \nenlace, jerarquía, etc.). 
 
 
 
 
### 🔵 Atención 
Enrutador software. 
Es un software que realiza las funciones de un enrutador, un \nejemplo de ello es IP-Masquerade en Linux, con él es posible tener 
acceso a Internet en ordenadores conectados a una red local 
donde al menos uno de ellos sí que posea conexión al exterior (el 
ordenador pasarela). 
 
### 🔵 7.6. Compuerta (Gateway)
 
Una compuerta que une una red SNA de IBM con una red NetWare de Novell

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Una compuerta actúa como traductor entre sistemas que no utilizan los mismos protocolos de 
comunicaciones, formatos de estructuras de datos, lenguajes y/o arquitecturas. 
Se utilizan cuando las redes son completamente distintas. 
Cuando una compuerta recibe un paquete de una red, ésta traduce el paquete del formato usado en la 
red a un formato común entre compuertas. 
A continuación, lo envía a otra compuerta que lo traduce del formato común al formato usado en la red 
destino y lo envía. Normalmente una compuerta se diseña utilizando un ordenador personal dedicado, 
con varias tarjetas de red y programas de conversión y comunicación. 
Debe tener la capacidad suficiente para acoplar velocidades entre las líneas, realizar conversiones de 
protocolo y optimizar la ocupación de las redes. 
 
 
 
 
+ Info 
Para mantenerte al día sobre cables y componentes de 
comunicación, te aconsejamos ver el enlace a los boletines 
informativos de Cofitel. 
https://www.c3comunicaciones.es/documentacion-tecnica-
sobre-fibra-optica/boletines-informativos/ 
 
## 🟣 8. Comunicaciones móviles
La conectividad móvil o comunicaciones móviles se dan cuando tanto el emisor como el receptor están, 
o pueden estar, en movimiento. 
Los profesionales de hoy en día tienen cada vez más la necesidad de estar siempre conectados fuera de 
sus oficinas, por lo que las tecnologías de comunicación móviles han experimentado un gran 
crecimiento. 
La necesidad de no abandonar el ritmo de trabajo al viajar para seguir siendo productivo ha llevado al 
desarrollo de la conectividad móvil. 
Los profesionales necesitan disponer de toda la información necesaria en cualquier lugar en el que se \nencuentren.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 8.1. Generaciones
La conectividad móvil ha ido evolucionando y se habla de generaciones de comunicaciones móviles. 
 
 
 
 
### 🔵 Atención 
Sistemas de comunicaciones móviles: 
- Orden de la evolución:
GSM, GPRS, UMTS, HSDPA, LTE. 
- Ordenados por generaciones:
AMPS, GSM, GPRS, HSDPA. 
 
 
En la actualidad se conocen 5 generaciones. 
8.1.1. 1ª Generación (1G) 
 
Fuente: 
(https://es.m.wikipedia.org/
wiki/Archivo:DynaTAC8000
X.jpg)

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Fue en el año 1970 cuando un nuevo estándar de comunicación se hacía conocido y dentro de las 
principales características tenía que ya no era necesario una comunicación mediante sistema de cables, 
lo que dio lugar a los primeros teléfonos móviles. 
La señal 1G sólo permitía la realización de llamadas telefónicas y transferencia de datos entre las torres. 
8.1.2. 2ª Generación (2G) 
Ya a comienzos de los 90, el rápido crecimiento de las tecnologías referente a los teléfonos móviles y la 
penetración que éstos tuvieron en la población hicieron que las redes móviles no aprovecharan el 
potencial dichos dispositivos tenían. 
El estándar GSM (Global System for Mobile Communications), permitía la transferencia de datos a una 
velocidad mayor, permitiendo utilizar capacidades como el correo de voz y los mensajes de texto. 
Algunos de los teléfonos más avanzados en esta generación, tenían la opción incluso de acceder a 
portales web especialmente optimizados para su uso en estos dispositivos. 
Aparecen 2 mejoras: 
- 2.5G GPRS (General packet radio service).
- 2.75G E-GPRS (Enhanced GPRS). También conocida como EDGE (Enhanced Data Rates for
GMS Evolution). 
8.1.3. 3ª Generación (3G) 
Era una versión de la conectividad EDGE que permitía alcanzar velocidades de hasta 2Mbps, cientos de 
veces superior a lo que ya se había conseguido. 
Se podía acceder a la web y los smartphones empezaron a llegar a los consumidores. 
En Europa y Japón se utilizó el estándar denominado UMTS (Universal Mobile Telecommunication 
System). 
### 🔵 UMTS 
UMTS (Universal Mobile Telecommunications System o Sistema universal de telecomunicaciones 
móviles) es una de las tecnologías usadas por los móviles de tercera generación, sucesora de GPRS, 
debido a que la tecnología GPRS (evolución de GSM, (siglas de Global System for Mobile 
communications, sistema global para las comunicaciones móviles, y es un tipo de red que se utiliza para 
la transmisión móvil de voz y datos) propiamente dicha no podía evolucionar para prestar servicios 
considerados de tercera generación.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Sus principales características son: 
- Capacidades multimedia.
- Velocidad de acceso a Internet elevada (permite transmitir audio y video en tiempo real).
- Transmisión de voz con calidad equiparable a la de las redes fijas.
UMTS tiene tres elementos fundamentales: 
- UE (User Equipment o equipamiento de usuario).
Está formado por: 
- Terminal de usuario (teléfono móvil).
- USIM (Universal Subscriber Identity Module o Módulo de Identificación del Abonado).
Sería el equivalente a la tarjeta SIM. 
- Núcleo de red (core network).
Incorpora funciones de transporte y de inteligencia. 
Las primeras soportan el transporte de la información de tráfico y señalización, incluida la 
conmutación. 
El encaminamiento reside en las funciones de inteligencia, que comprenden prestaciones como 
la lógica y el control de ciertos servicios ofrecidos a través de una serie de interfaces bien 
definidas. 
También incluyen la gestión de la movilidad. 
A través del núcleo de red, el UMTS se conecta con otras redes de telecomunicaciones, de 
forma que resulte posible la comunicación no sólo entre usuarios móviles UMTS, sino también 
con los que se encuentran conectados a otras redes. 
- UTRAN (UMTS Terrestrial Radio Access Network o Acceso Universal Radioeléctrico
Terrestre). 
Desarrollada para obtener altas velocidades de transmisión. 
La red de acceso radio proporciona la conexión entre los terminales móviles y el Core Network. 
Se compone de una serie de subsistemas de redes de radio (RNS) que son el modo de 
comunicación de la red UMTS.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
W-CDMA 
W-CDMA (Wideband Code Division Multiple Access ol Acceso múltiple por división de código de banda 
ancha) es la tecnología de acceso móvil en la que se basan varios estándares de telefonía móvil de 
tercera generación (3G), entre ellos el estándar UMTS. 
En WCDMA existen dos modos de operación: 
- TDD.
En este método bidireccional, las transmisiones de los enlace subida y bajada son transportadas \nen la misma banda de frecuencia usando intervalos de tiempo (intervalos de trama) de forma 
síncrona. 
Así los intervalos de tiempo en un canal físico se asignan para los flujos de datos de transmisión 
y de recepción. 
- FDD.
Los enlaces de las transmisiones de subida y de bajada emplean dos bandas de frecuencia 
separadas. 
Un par de bandas de frecuencia con una separación especificada se asigna para cada enlace. 
HSDPA (3.5G) 
La tecnología HSDPA (High Speed Downlink Packet Access o 3.5G) es la optimización de la tecnología 
radio de UMTS. 
Consigue aumentar la velocidad de descarga hasta 14,4Mbps incorporando un nuevo canal compartido 
para descarga y mejorando la técnica de modulación de señal. 
HSUPA (3.75G) 
HSUPA (High-Speed Uplink Packet Access) es un protocolo de acceso de datos para redes de telefonía 
móvil con alta tasa de transferencia de subida. 
Es una mejora de HSDPA, en el que aplican las mismas mejoras que hicieron en el canal de bajada al 
canal de subida. 
HSPA+ (3.8G, 3.85G) 
HSPA+ (Evolved HSPA o HSPA Evolucionado), es un estándar de telefonía móvil para alcanzar 
velocidades de hasta 42 Mbps de bajada y 11,5 Mbps de subida. 
Para conseguirlo utiliza: 
- Modulación 64QAM.
- MIMO (técnica multi-antena).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
8.1.4. 4ª Generación (4G) 
la Unión Internacional de Telecomunicaciones (UIT) creó un comité (IMT-Advanced) que definió las \nespecificaciones de 4G los requisitos necesarios para que un estándar sea considerado de la 
generación 4G. 
El principal requisito es que las velocidades máximas de transmisión de datos deben estar entre 100 
Mbit/s (12,5 MB/s) para una movilidad alta y 1 Gbit/s (125 MB/s) para movilidad baja. 
El estándar LTE (long term evolution: 'evolución a largo plazo') de la norma 3GPP no es 4G porque no 
cumple los requisitos respecto a velocidades pico de transmisión y eficiencia espectral. Por esto, se 
desarrolló LTE-Advanced (LTE-A) como una ampliación de LTE y como paradigma de lo que debería 
ser el 4G. 
LTE-A, en teoría, debe ser capaz de ofrecer altas capacidades de transmisión con anchos de banda de 
más de 100 MHz obtenidos mediante agregación de canales de 20 MHz, tecnologías de antenas 
múltiples basadas en MIMO y transmisiones coordinadas multipunto. Utiliza tecnología W-CDMA. 
Aun así, la UIT declaró en 2010 que los candidatos a 4G (como LTE) podían publicitarse como 4G. 
La 4G está basada completamente en el protocolo IP. 
Su principal característica (coincidiendo con su principal requisito) es la capacidad para proveer 
velocidades de acceso mayores de 100 Mbit/s en movimiento y 1 Gbit/s en reposo, manteniendo una 
calidad de servicio (QoS) de punta a punta de alta seguridad que permitirá ofrecer servicios de 
cualquier clase en cualquier momento, en cualquier lugar, con el mínimo coste posible. 
8.1.5. 5ª Generación (5G) 
Es una tecnología cuyo gran despliegue comenzó en 2020. 
 
 
 
 
+ Info 
El gobierno ha subastado 200 MHz en la banda de frecuencias de 
3,6-3,8 GHz destinadas a cobertura urbana. 
Para las otras dos bandas identificadas para el 5G, la de 26 GHz y 
las 700 MHz

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Las características ventajosas más llamativas de esta tecnología son: 
Las mejoras de 5G son: 
- Incremento de la velocidad de transmisión respecto a 4G (con una velocidad teórica de hasta
20Gbps). 
- Reducción de la latencia.
Se pretende que la latencia en las conexiones pase de los 50 milisegundos a 1 milisegundo, por 
lo que la velocidad de respuesta a las instrucciones de sensores o dispositivos de control será 
prácticamente instantánea. 
- Posibilidad de ofrecer servicios como network slicing.
El Network Slicing (rebanado de red o corte de red) es una arquitectura que permite el 
fraccionamiento de redes lógicas virtualizadas e independientes utilizando la misma 
infraestructura de red física. 
El network slicing permite crear múltiples redes virtuales sobre una infraestructura física común 
compartida. 
- Penetran mejor en interiores y tienen mayor alcance.
- Las antenas soportan más conexiones simultáneas.
Puede haber muchos más dispositivos por unidad de área. 
- Son posibles conexiones directas entre dispositivos.
- El empleo de protocolos de comunicación de muy bajo consumo de energía y repartir los recursos entre los usuarios, priorizándolos. 
Para conseguirlo, 5G aumentará la frecuencia hasta el entorno de los 60 GHz, lo que va a reducir 
levemente el alcance… de manera que harán falta más antenas. 
 
 
 
 
### 🔵 Resumiendo 
En resumen, la tecnología 5G supone la reducción del retardo en 
las comunicaciones, el aumento del caudal de transferencia de la 
información, una mejora de la cobertura, y la posibilidad de que 
millones de dispositivos estén conectados a la vez.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
8.1.6. 6ª Generación (6G) 
Con la sexta generación de la conectividad móvil, se pretende mejorar las tres características principales 
de la 5G: mayor ancho de banda, baja latencia y conexiones más amplias. Estimándose que la 6G podrá 
multiplicar las tasas de transmisión hasta 10 veces, consiguiendo así velocidades de hasta un terabit por 
segundo. 
Se espera pasar por un estado intermedio denominado como 5G+ o 5G avanzado, en funcionamiento 
antes de 2024. 
El Ministerio de Industria y Tecnología de la Información chino confirmó a finales de 2018 que China 
llevaba desde marzo de ese año investigando el 6G. Según las previsiones de aquel momento, el 
desarrollo oficial de esta nueva conectividad en el país asiático comenzaría en 2020, pero habría que \nesperar hasta 2030 para su comercialización. 
Antes del despliegue de la tecnología 5G, China ya estaba desarrollando la 6G en marzo de 2018, 
(confirmado por El Ministerio de Industria y Tecnología de la Información chino) con intención de 
tenerlo a finales de esta década. 
También Corea aseguraba que el primer proyecto piloto sería en 2026 (alcanzando velocidades cinco 
veces superiores al máximo teórico del 5G, reduciendo la latencia a la décima parte, es decir, a 0,1 
milisegundos). 
Las ventajas de 6G, se esperan aplicar en diversos sectores, como la medicina y la automoción. 
Potenciando varios campos como la realidad extendida, (incluyendo las comunicaciones holográficas), 
la inteligencia artificial, automatizada e interconectada y la eficiencia energética, con niveles de 
consumo ultra bajos. 
 
 
 
 
+ Info 
OPPO (empresa global de consumo en tecnología y 
comunicaciones móviles) ha elaborado un primer informe técnico 
sobre el 6G donde asegura que la próxima generación de redes 
revolucionará el modo en que la Inteligencia Artificial aprende, 
interactúa y es aplicada. 
https://www.oppo.com/content/dam/oppo/ \nen/mkt/newsroom/press/oppo-unveils-6g-white-
paper/6G%20AI-Cube%20Intelligent%20Networking.pdf

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 8.2. Itinerancia o Roaming
La itinerancia (del inglés roaming) es un concepto utilizado en telecomunicaciones para referirse a la 
posibilidad de un dispositivo inalámbrico, de utilizar una cobertura de red distinta de la principal. Esto le 
permite conectarse a redes secundarias utilizando su identificador en la red principal. 
En telefonía móvil, el término se usa para indicar la posibilidad ofrecida a sus clientes por un operador de 
usar el servicio en una red móvil distinta de la suya, y normalmente fuera del territorio nacional. Esta 
identificación se hace a través de la tarjeta SIM, que permite conectar al cliente con su operador de otra 
red mediante acuerdos entre operadores. 
En el caso de redes wifi, significa que el dispositivo wifi del cliente puede desplazarse e ir registrándose \nen diferentes redes inalámbricas. En este caso la identificación normalmente se hace a través de un 
usuario y contraseña personal compartida por distintas redes. 
En el caso del arte, "itinerancia" hace referencia a las exposiciones temporales que rotan por diferentes 
instituciones. 
## 🟣 9. Comunicaciones inalámbricas
La comunicación inalámbrica (o sin cables), es aquella en la que la comunicación (emisor/receptor) no 
se encuentra unida por un medio de propagación físico, sino que se utiliza la modulación de ondas \nelectromagnéticas a través del espacio. 
Los dispositivos físicos solo están presentes en los emisores y receptores de la señal, entre los cuales \nencontramos: antenas, puntos de acceso etc. 
El término red inalámbrica se utiliza para designar la conexión de nodos sin necesidad de una conexión 
física (cables), ésta se da por medio de ondas electromagnéticas. La transmisión y la recepción se 
realizan a través de puertos. 
Una de sus principales ventajas es notable en los costos, ya que se elimina todo el cable Ethernet y 
conexiones físicas entre nodos, pero también tiene una desventaja considerable ya que para este tipo 
de red se debe tener una seguridad mucho más exigente y robusta para evitar a los intrusos. 
Arquitectura de antenas Mimo y Mu-Mimo 
La tecnología MIMO, es el acrónimo en inglés de Multiple-input Multiple-output (en español, Múltiple \nentrada múltiple salida). También se le denomina SU-MIMO. 
Se refiere específicamente a la forma como son manejadas las ondas de transmisión y recepción en 
antenas para dispositivos inalámbricos como enrutadores. 
En el formato de transmisión inalámbrica tradicional la señal se ve afectada por reflexiones, lo que 
ocasiona degradación o corrupción de la misma y por lo tanto pérdida de datos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
MIMO aprovecha fenómenos físicos como la propagación multicamino para incrementar la tasa de 
transmisión y reducir la tasa de error. En breves palabras MIMO aumenta la eficiencia espectral de un 
sistema de comunicación inalámbrica por medio de la utilización del dominio espacial. 
Durante los últimos años la tecnología MIMO ha sido aclamada en las comunicaciones inalámbricas ya 
que aumenta significativamente la tasa de transferencia de información utilizando diferentes canales en 
la transmisión de datos o la multiplexación espacial por tener las antenas físicamente separadas. 
La tecnología MU-MIMO, además de permitir el envío de datos de forma simultánea, aprovecha el 
ancho de banda al máximo para que los clientes consigan la máxima velocidad y por lo tanto se ha 
convertido en una tecnología ideal para servicios en tiempo real como videoconferencias o juegos 
online que requieren que los datos se transmitan rápidamente. 
MU-MIMO permite que múltiples dispositivos puedan recibir de manera simultánea diferentes flujos de 
datos para aumentar la velocidad y el rendimiento de toda la red. 
Se aplica únicamente a las conexiones de enlace descendente. 
Es importante saber que a diferencia de SU-MIMO, MU-MINO a día de hoy únicamente funciona con 
conexiones inalámbricas de enlace descendente. Sólo los routers inalámbricos y puntos de acceso pueden \nenviar de manera simultánea datos de varios usuarios, ya sea uno o más flujos de datos a cada uno. 
Por su parte, los dispositivos como smartphones, tablets u ordenadores portátiles tiene que esperar su 
turno para enviar datos al router o punto de acceso, aunque se pueden utilizar individualmente SU-
MIMO para enviar múltiples flujos de datos cuando les toca el turno. Por lo tanto, MU-MO es muy útil en 
las redes donde los usuarios conectados en su mayoría del tiempo descargan datos en lugar de subir. 
SU-MIMO y MU-MIMO tienen sus respectivos dominios de funcionamiento. La banda de 5 GHz 
realmente brilla en términos de capacidad y menos congestión, haciendo que tecnologías como MU-
MIMO sean mucho más efectivas. Además, con la llegada de WiFi 6 y 6E, estamos viendo mejoras 
considerables en ambas bandas, 2.4 GHz y 5 GHz, y el nuevo espectro de 6 GHz, lo que abre aún más 
oportunidades para una conectividad más rápida y eficiente. 
Vamos a ver sus características: 
- BeamForming.
MU-MIMO cuenta con una característica que permite que realizar un envío direccional de los 
datos en lugar de hacer de forma aleatoria hacia todas las direcciones. De esta manera, los 
datos van más directos hacia el dispositivo que los solicita por lo que la señal se utiliza de 
forma más eficiente y además no se ve afectada por ningún tipo de obstáculo como las 
paredes de nuestra casa. 
- No soporta un número ilimitado de dispositivos.
Lamentablemente, un router MU-MIMO no puede servir al mismo tiempo flujos de datos a un 
número de dispositivos ilimitado. Hoy en día, un router de estas características únicamente va a 
poder suministrar datos de esta manera a un máximo de 3 o 4 dispositivos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Los dispositivos no requieren múltiples antenas.
Sólo los dispositivos inalámbricos con soporte incorporado para MU-MIMO pueden recibir 
señales MU-MIMO. Pero a diferencia con la tecnología SU-MIMO, los dispositivos inalámbricos 
no necesitan tener varias antenas para recibir datos desde Routers inalámbricos MU-MIMO. No 
obstante, si el dispositivo cuenta con más de una antena va a hacer que el rendimiento WiFi del 
terminal sea mayor. 
- La carga del procesamiento no cae sobre el dispositivo.
A diferencia con SU-MIMO, MU-MIMO ha sido diseñado para que los router o puntos de acceso 
sean los que carguen con todo el procesamiento de la señal y de ahí que los dispositivos puedan 
ahorrar espacio y energía. 
- Activar con una actualización de software.
En la actualidad no hay un gran número de routers o dispositivos móviles que tengan soporte 
MU-MIMO, sin embargo, el fabricante de chips Qualcomm afirma que algunas compañías que se 
dedican a desarrollar este tipo de dispositivos han incluido el hardware necesario en su interior, 
aunque el propio usuario no lo sepa, para que con una simple actualización de software se les 
pueda añadir soporte para esta nueva tecnología. 
- Aumenta la capacidad de la red.
Al aumentar la velocidad WiFi también aumenta la capacidad de la red, ya que los dispositivos 
reciben sus datos con mayor rapidez y por lo tanto el router dispone de más tiempo libre para \nenviar flujos de datos a más dispositivos. De esta manera, se puede decir que MU-MIMO puede 
ayudar a aliviar la congestión en redes muy ocupadas. 
- Soporta cualquier ancho de canal.
Una manera de aumentar en rendimiento de un canal de conexión WiFi es realizando una unión 
de canales, de esta forma, al combinar dos canales para crear uno sólo de doble ancho, se 
consigue aumentar la velocidad de la WiFi. El estándar 802.11ac añadió soporte para canales de 
80 MHz y a día de hoy es compatible también con canales de 160 MHz. 
- Aumenta la seguridad.
Se trata de un efecto secundario de la tecnología MU-MIMO, ya que el router codifica los datos 
antes de enviarlos de tal forma que sólo el dispositivo receptor será el que pueda decodificar los 
datos recibidos. De esta forma, esta tecnología ayuda a aumentar la seguridad de nuestra red 
WiFi. 
ES importante saber que MU-MIMO no funciona bien con dispositivos que se mueven 
rápidamente puesto que el proceso de formación de haces para el envío de los datos se vuelve 
más complejo y menos eficaz. Esto hace que la tecnología no aporte los mismos beneficios.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Comparativa entre MIMO y MU-MIMO: 
Mientras que SU-MIMO funciona en las bandas de frecuencia WiFi de 2,4GHz y de 5 GHz, MU-MIMO 
forma parte del estándar WiFi AC y únicamente funciona en la banda de 5GHz. Por lo tanto, los routers 
inalámbricos y los puntos de acceso únicamente pueden enviar flujos de datos a varios usuarios de 
forma simultánea en la banda WiFi de 5GHz. 
 
 
 
 
### 🔵 Recuerda 
Para que lo recuerdes mejor: 
- SU: Single User.
- MU: Multiple Users.
- MIMO: Multiple-Input Multiple-Outp.ut.
 
Componentes físicos de una red inalámbrica: 
Existen diferentes componentes físicos necesarios en una red inalámbrica, son: antenas, puntos de 
acceso, Bridge Inalámbrico, Router Inalámbrico y adaptadores. 
- Antenas:
Es un dispositivo que permite transmitir y recibir ondas de radio. 
Una de las cosas que hace es convertir la onda guiada (señales digitales) por la línea de 
transmisión (cable o guía de onda) en ondas electromagnéticas que se pueden transmitir por el \nespacio libre. 
Tipos de Antenas: 
- Antenas Direccionales (Directivas):
Orientan la señal en una dirección muy determinada con un haz estrecho, pero de largo 
alcance. 
Actúa de forma parecida a un foco que emite un haz concreto y estrecho, pero de forma 
intensa (más alcance). 
Envían la información a una cierta zona de cobertura, a un ángulo determinado, por lo cual 
su alcance es mayor. 
Fuera de la zona de cobertura, la recepción es nula.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Antenas Omnidireccionales:
Son buenas para cubrir áreas grandes, ya que la radiación trata de ser pareja para todos 
lados es decir cubre 360º. 
Orientan la señal en todas direcciones con un haz amplio, pero de corto alcance. 
Envían la información teóricamente a los 360 grados por lo que es posible establecer 
comunicación independientemente del punto en el que se esté. En contrapartida el alcance 
de estas antenas es menor que el de las antenas direccionales. 
 
 
 
 
### 🔵 Conclusiones 
Si una antena direccional sería como un foco, una antena 
omnidireccional sería como una bombilla emitiendo luz en todas 
direcciones, pero con una intensidad menor que la de un foco (con 
menor alcance). 
 
 
- Punto de Acceso:
Es un dispositivo de capa 2, por medio de los cuales las estaciones Wireless pueden integrarse 
rápida y fácilmente a cualquier red cableada. 
Puede actuar como punto central de una red inalámbrica autónoma y además puede usarse 
como un punto de conexión entre redes inalámbricas y cableadas. 
- Bridge Inalámbrico:
Está diseñado para conectar dos o más redes ubicadas en general en diferentes edificios. 
Proporciona elevadas velocidades de datos y un throughput Rendimiento) superior para las 
aplicaciones intensivas en cuanto a los datos. 
Se utilizan para poder conectar sitios difíciles de cablear, pisos no contiguos, instalaciones de 
campus de escuelas o corporativas, etc. 
Throughput se refiere a la tasa de transferencia, (la velocidad real de transporte de datos a 
través de una red, la cual normalmente se mide en megabits por segundo y siempre será inferior 
al ancho de banda).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Router Inalámbrico:
Es un dispositivo utilizado en redes como guía que permite la conexión de redes inalámbricas, y 
guiar los paquetes de datos, para que fluya hacia la red correcta a determinado destino. 
Permite la conexión a la WLAN de dispositivos inalámbricos. 
La tecnología de comunicación con que cuenta es a base de ondas de radio, también permiten 
conexión ADSL, la cual permite el manejo de internet de banda ancha y ser distribuido hacia 
otras computadoras. 
- Adaptadores:
Son tarjetas para expansión de capacidades que sirve para enviar y recibir datos sin la necesidad 
de cables en las redes WLAN. 
Tienen una antena que permite la buena recepción de datos de la red, así como para su envío. 
Están diseñadas para ciertos tipos de estándares de redes inalámbricas, por lo que tienen una 
velocidad máxima de transmisión de datos en bits por segundo (bps) acorde al estándar. 
(Pueden ser Tarjetas PCI, conectadas a la placa base de un ordenador, dispositivos USB etc.). 
### 🔵 Topologías de una red inalámbrica 
Vas a estudiar las topologías AD-HOC, infraestructura, y malla. 
- AD-HOC:
Es un tipo de red inalámbrica descentralizada, porque no depende de una infraestructura 
preexistente, o de puntos de accesos en redes inalámbricas administradas. (O routers si fuera 
una red cableada) 
En lugar de ello, cada nodo participa en el encaminamiento mediante el reenvío de datos hacia 
otros nodos, de modo que la determinación de estos nodos hacia la información se hace 
dinámicamente sobre la base de conectividad de la red. Además del encaminamiento clásico, las 
redes ad hoc pueden usar un flooding (inundación de red) para el reenvío de datos. 
Una red ad hoc se refiere típicamente a cualquier conjunto de redes donde todos los nodos 
tienen el mismo estado dentro de la red y son libres de asociarse con cualquier otro dispositivo 
de red ad hoc en el rango de enlace. 
Una red inalámbrica tipo ad-hoc, consiste en un grupo de ordenadores que se comunican cada 
uno directamente con los otros a través de las señales de radio sin usar un punto de acceso. 
Las configuraciones "Ad-hoc" son comunicaciones de tipo punto a punto. Solamente los 
ordenadores dentro de un rango de transmisión definido pueden comunicarse entre ellos.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Cuando un adaptador WIRELESS es activado, primero pasa a un estado de escucha en el cual 
dura 6 segundos, busca una conversión activa y le avisa al usuario, en el supuesto que no pueda 
conectar a otro Host que ya tuviera activo pasa a crear una conversación. Para una determinada 
WLAN con topología ad-Hoc, todos los equipos conectados a ella (Host) deben ser 
configurados con el mismo identificador del servicio básico (Basic Service Set, BSSID). El Modo 
Ad-Hoc puede soportar 256 usuarios. 
- Infraestructura:
Al contrario que en una red ad hoc, en este tipo hay un elemento de "coordinación"; un punto 
de acceso o estación base. 
Si el punto de acceso se conecta a una red Ethernet cableado los clientes inalámbricos pueden 
acceder a la red fija a través del punto de acceso. 
Para interconectar muchos puntos de acceso y clientes inalámbricos, todos deben configurarse 
con el mismo SSID. • En redes IEEE 802.11 el modo de infraestructura es conocido como 
conjunto de servicios básicos (BSS) o maestro y cliente. 
- Malla:
Se denominan redes inalámbricas malladas, redes acopladas, o redes de malla inalámbricas de 
infraestructura. 
Son aquellas en las que se mezclan la topología Ad-hoc y la topología infraestructura. 
Básicamente son redes de infraestructura, pero que permiten unirse a la red a dispositivos que, a 
pesar de estar fuera del rango de cobertura de los puntos de acceso están dentro del rango de 
cobertura de alguna tarjeta de red (TR) que directamente o indirectamente está dentro del 
rango de cobertura de un punto de acceso (PA). 
### 🔵 9.1. WiFi. Estándares
Wi-Fi es un mecanismo de conexión de dispositivos electrónicos de forma inalámbrica. 
 
 
 
 
* Curiosidad 
Hedwig Eva Maria Kiesler, actriz austríaca nacida en 1914, 
inventaría, desarrollaría y patentaría (11 de agosto de 1942) junto 
al pianista George Antheil un sistema de guía por radio para 
torpedos aliados usando el espectro ensanchado por primera vez. 
Tecnología precursora de la comunicación inalámbrica que la 
armada de los Estados Unidos no adpotaría hasta la década de los 
60 del siglo pasado.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
 
 
 
### 🔵 Hedwig Eva Maria Kiesler 
 
 
Los dispositivos habilitados con wifi pueden conectarse a Internet a través de un punto de acceso de 
red inalámbrica. 
"Wi-Fi" es una marca de la Wi-Fi Alliance, que es organización comercial que adopta, prueba y certifica 
que los equipos cumplen los estándares IEEE 802.11 referentes a las redes de área local inalámbricas. 
Existen diversos tipos de wifi, basado cada uno de ellos en un estándar IEEE 802.11. Son los siguientes: 
- IEEE 802.11a:
La revisión 802.11a fue aprobada en 1999. Este estándar utiliza el mismo juego de protocolos 
de base que el estándar original, opera en la banda de 5 GHz y utiliza 52 subportadoras de 
acceso múltiple por división de frecuencias ortogonales (Orthogonal Frequency-Division 
Multiplexing, OFDM) con una velocidad máxima de 54 Mbit/s, lo que lo hace un estándar 
práctico para redes inalámbricas con velocidades reales de aproximadamente 20 Mbit/s. 
Dado que la banda de 2,4 GHz es muy utilizada hasta el punto de estar llena de gente, la 
utilización de la relativamente inusitada banda de 5 GHz da una ventaja significativa a 802.11a. 
Sin embargo, esta alta frecuencia portadora también presenta una desventaja: el intervalo 
global eficaz de 802.11a es menor que el de 802.11b / g. En teoría, las señales 802.11a son 
absorbidas más fácilmente por paredes y otros objetos sólidos en su trayectoria debido a su 
longitud de onda más pequeña, y, como resultado, no pueden penetrar hasta los de 802.11b. En 
la práctica, 802.11b normalmente tiene un rango más alto a bajas velocidades. 802.11a también 
sufre de interferencia, pero localmente puede haber menos señales para interferir, resultando \nen menos interferencia y mejor rendimiento.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
802.11a tiene 12 canales sin solapamiento, 8 para red inalámbrica y 4 para conexiones punto a 
punto. No puede interoperar con equipos del estándar 802.11b, excepto si se dispone de \nequipos que implementen ambos estándares. 
- IEEE 802.11ac:
Utiliza la banda de 5 GHz. Velocidad máxima 300Mbit/s. Conocido como WIFI 5. 
Esta banda no se utiliza por otras tecnologías como el bluetooth o las microondas. 
Tiene mayor frecuencia y, por lo tanto, menor cobertura. 
- 802.11ac y MU-MIMO.
Una de las características más complejas que forma parte de este estándar, es la incorporación 
de MU-MIMO. 
- IEEE 802.11ah.
Es un protocolo de red inalámbrica publicado en 2017 que se denominará Wi-Fi HaLow como 
una enmienda del estándar de red inalámbrica IEEE 802.11-2007. Utiliza bandas exentas de 
licencia de 900 MHz para proporcionar redes Wi-Fi de rango extendido, en comparación con las 
redes Wi-Fi convencionales que operan en las bandas de 2.4 GHz y 5 GHz. 
- IEEE 802.11b.
La revisión 802.11b del estándar original fue ratificada en 1999. 
802.11b tiene una velocidad máxima de transmisión de 11 Mbps y utiliza el mismo método de 
acceso definido en el estándar original CSMA/CA. El estándar 802.11b funciona en la banda de 
2,4 GHz. Debido al espacio ocupado por la codificación del protocolo CSMA/CA, en la práctica, 
la velocidad máxima de transmisión con este estándar es de aproximadamente 5,9 Mbit/s sobre 
TCP y 7,1 Mbit/s sobre UDP. 
Los productos que usan esta versión aparecieron en el mercado a principios del 2000, ya que 
802.11b es una extensión directa de la técnica de modulación definida en la norma original. El 
aumento dramático del rendimiento de 802.11b y su reducido precio llevó a la rápida 
aceptación de 802.11b como la tecnología de LAN inalámbrica definitiva. 
Los dispositivos que utilizan 802.11b pueden experimentar interferencias con otros productos 
que funcionan en la banda de 2,4 GHz. 
- IEEE 802.11c.
Es menos usado que los primeros dos, por la implementación que este protocolo refleja. El 
protocolo 'c' es utilizado para la comunicación de dos redes distintas o de diferentes tipos, así 
como puede ser tanto conectar dos edificios distantes el uno con el otro, así como conectar dos 
redes de diferente tipo a través de una conexión inalámbrica. El protocolo 'c' es más utilizado 
diariamente, debido al costo que implica las largas distancias de instalación con fibra óptica, que, 
aunque más fidedigna, resulta más costosa tanto en instrumentos monetarios como en tiempo 
de instalación.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
"El estándar combinado 802.11c no ofrece ningún interés para el público general. Es solamente 
una versión modificada del estándar 802.11d que permite combinar el 802.11d con dispositivos 
compatibles 802.11 (en el nivel de enlace de datos capa 2 del modelo OSI)". 
- IEEE 802.11d.
Publicado en el año 2001, define los requisitos de nivel físico necesarios para extender el uso de 
redes IEEE 802.11 a países con dominios regulatorios no incluidos en el estándar general. 
Permite a los puntos de acceso comunicar información sobre los canales radio admisibles con 
niveles de potencia aceptables para los dispositivos de los usuarios. Permite que distintos 
dispositivos intercambien información en rangos de frecuencia según lo que se permite en el 
país de origen del dispositivo móvil. 
- IEEE 802.11e.
Su objetivo es proporcionar QoS (Calidad de servicio) en redes WLAN. La finalidad es 
proporcionar clases de servicio con niveles gestionados en QoS para aplicaciones de datos, voz y 
vídeo. Ofrece un estándar inalámbrico que permite interoperar entre entornos públicos, de 
negocios y usuarios residenciales, con la capacidad añadida de resolver las necesidades de cada 
sector. A diferencia de otras iniciativas de conectividad sin cables, ésta puede considerarse 
como uno de los primeros estándares inalámbricos que permite trabajar en entornos 
domésticos y empresariales. La especificación añade, respecto de los estándares 802.11b y 
802.11a, características QoS y de soporte multimedia, a la vez que mantiene compatibilidad con \nellos. Estas prestaciones resultan fundamentales para las redes domésticas y para que los 
operadores y proveedores de servicios conformen ofertas avanzadas. El sistema de gestión 
centralizado integrado en QoS evita la colisión y cuellos de botella, mejorando la capacidad de \nentrega en tiempo crítico de las cargas. 
- IEEE 802.11f.
Nace con el objetivo de lograr la interoperabilidad de puntos de acceso IEEE 802.11b/g dentro 
de una red WLAN con puntos de acceso de diferentes fabricantes dentro de la misma red. El \nestándar define un protocolo para la comunicación entre puntos de acceso que permite la 
transferencia de usuarios entre puntos de acceso. El protocolo IAPP (Inter Access Points 
Protocol) es el encargado de transferir la información de contexto para permitir el traspaso de 
usuarios entre puntos de acceso. 
- IEEE 802.11g.
Este utiliza la banda de 2,4 Ghz (al igual que 802.11b) pero opera a una velocidad teórica 
máxima de 54 Mbit/s, que en promedio es de 22,0 Mbit/s de velocidad real de transferencia, 
similar a la del estándar 802.11a. Es compatible con el estándar b y utiliza las mismas 
frecuencias. Buena parte del proceso de diseño del nuevo estándar lo tomó el hacer compatibles 
ambos modelos. Sin embargo, en redes bajo el estándar g la presencia de nodos bajo el estándar 
b reduce significativamente la velocidad de transmisión. 
Los equipos que trabajan bajo el estándar 802.11g llegaron al mercado muy rápidamente, 
incluso antes de su ratificación que fue dada aprox. el 20 de junio de 2003. Esto se debió en 
parte a que para construir equipos bajo este nuevo estándar se podían adaptar los ya diseñados 
para el estándar b.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Actualmente se venden equipos con esta especificación, con potencias de hasta medio vatio, 
que permite hacer comunicaciones de más de 50 km con antenas parabólicas o equipos de radio 
apropiados. 
Existe una variante llamada 802.11g+ capaz de alcanzar los 108Mbps de tasa de transferencia. 
Generalmente sólo funciona en equipos del mismo fabricante ya que utiliza protocolos 
propietarios. 
- IEEE 802.11h.
El desarrollo del 802.11h sigue unas recomendaciones hechas por la Unión Internacional de 
Telecomunicaciones (ITU) que fueron motivadas principalmente a raíz de los requerimientos 
que la Oficina Europea de Radiocomunicaciones (ERO) estimó convenientes para minimizar el 
impacto de abrir la banda de 5 GHz, utilizada generalmente por sistemas militares, a 
aplicaciones ISM (ECC/DEC/(04)08). 
Con el fin de respetar estos requerimientos, 802.11h proporciona a las redes 802.11a la 
capacidad de gestionar dinámicamente tanto la frecuencia, como la potencia de transmisión. 
- Selección Dinámica de Frecuencias.
DFS (Dynamic Frequency Selection) es una funcionalidad requerida por las WLAN que 
operan en la banda de 5 GHz con el fin de evitar interferencias co-canal con sistemas de 
radar y para asegurar una utilización uniforme de los canales disponibles. 
- Control de Potencia del Transmisor.
TPC (Transmitter Power Control) es una funcionalidad requerida por las WLAN que operan \nen la banda de 5 GHz para asegurar que se respetan las limitaciones de potencia 
transmitida que puede haber para diferentes canales en una determinada región, de manera 
que se minimiza la interferencia con sistemas de satélite. 
- IEEE 802.11i.
Está dirigido a batir la vulnerabilidad actual en la seguridad para protocolos de autenticación y 
de codificación. Proporciona una alternativa al mecanismo WEP original disponible para ofrecer 
seguridad en este tipo de redes. ofreciendo nuevos métodos de cifrado y procedimientos de 
autenticación. Estándar ratificado. 
- IEEE 802.11j.
Fue diseñada especialmente para el mercado japonés y permite que la operación de LAN 
inalámbrica en la banda de 4,9 a 5 GHz se ajuste a las normas japonesas para la operación de 
radio para aplicaciones en interiores, exteriores y móviles. La enmienda se ha incorporado a la 
norma IEEE 802.11-2077 publicada.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- IEEE 802.11k.
Permite a los conmutadores y puntos de acceso inalámbricos calcular y valorar los recursos de 
radiofrecuencia de los clientes de una red WLAN, mejorando así su gestión. Está diseñado para 
ser implementado en software, para soportarlo el equipamiento WLAN sólo requiere ser 
actualizado. Y, como es lógico, para que el estándar sea efectivo, han de ser compatibles tanto 
los clientes (adaptadores y tarjetas WLAN) como la infraestructura (puntos de acceso y 
conmutadores WLAN). 
- IEE 802.11m.
Complemento de mantenimiento del estándar IEEE 802.11 para llevar a cabo correcciones 
técnicas y aclaraciones sobre los distintos estándares. El grupo de trabajo del mismo nombre se \nencarga del mantenimiento del estándar, respondiendo a las peticiones de información y 
definiendo las líneas de trabajo del mantenimiento futuro del estándar. Estándar en desarrollo. 
- IEEE 802.11n.
Su principal objetivo es ofrecer una mayor velocidad de transmisión en redes WLAN, con un 
objetivo inicial de alcanzar los 100mbps. En enero de 2004, el IEEE anunció la formación de un 
grupo de trabajo 802.11 (Tgn) para desarrollar una nueva revisión del estándar 802.11. La 
velocidad real de transmisión podría llegar a los 600 Mbps (lo que significa que las velocidades 
teóricas de transmisión serían aún mayores), y debería ser hasta diez veces más rápida que una 
red bajo los estándares 802.11a y 802.11g, y unas cuarenta veces más rápida que una red bajo \nel estándar 802.11b. También se espera que el alcance de operación de las redes sea mayor con \neste nuevo estándar gracias a la tecnología MIMO (Multiple Input – Multiple Output), que 
permite utilizar varios canales a la vez para enviar y recibir datos gracias a la incorporación de 
varias antenas y la utilización de bandas de uso común .La mayor parte de los fabricantes ya 
incorpora a sus líneas de producción equipos wifi 802.11n, por este motivo la oferta ADSL, ya 
suele venir acompañada de wifi 802.11n, como novedad en el mercado de usuario doméstico. 
Uno de sus problemas es la posibilidad de ser interferidas por las redes 802.11.a/b/g. 
- IEEE 802.11p.
Este estándar opera en el espectro de frecuencias de 5,90 GHz y de 6,20 GHz, especialmente 
indicado para automóviles. Será la base de las comunicaciones dedicadas de corto alcance 
(DSRC). La tecnología DSRC permitirá el intercambio de datos entre vehículos y entre 
automóviles e infraestructuras en carretera. Además, agrega el Wireless Access in vehicular 
Environments o WAVE (acceso inalámbrico en entornos vehiculares), un sistema de 
comunicación vehicular. Esta mejora es muy usada en la implementación de los Sistemas 
Inteligentes de Transporte (SIT). Esto incluye el intercambio de datos entre vehículos y entre 
vehículos y la infraestructura de las carreteras por las que circulan. 
- IEEE802.11r.
También se conoce como Fast Basic Service Set Transition, y su principal característica es 
permitir a la red que establezca los protocolos de seguridad que identifican a un dispositivo en el 
nuevo punto de acceso antes de que abandone el actual y se pase a él. Esta función, que una vez \nenunciada parece obvia e indispensable en un sistema de datos inalámbricos, permite que la 
transición entre nodos demore menos de 50 milisegundos. Un lapso de tiempo de esa magnitud \nes lo suficientemente corto como para mantener una comunicación vía VoIP sin que haya cortes 
perceptibles.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- IEEE 802.11s.
Es el estándar en desarrollo para redes Wi-Fi malladas, también conocidas como redes Mesh. La 
malla es una topología de red en la que cada nodo está conectado a uno o más nodos. De esta 
manera es posible llevar los mensajes de un nodo a otro por diferentes caminos. Según la 
normativa 802.11 actual, una infraestructura Wi-Fi compleja se interconecta usando LANs fijas 
de tipo Ethernet. 802.11s pretende responder a la fuerte demanda de infraestructuras WLAN 
móviles con un protocolo para la autoconfiguración de rutas entre puntos de acceso mediante 
topologías multisalto. 
Dicha topología constituirá un WDS (Wireless Distribution System) que deberá soportar tráfico 
Unicast, Multicast y Broadcast. Para ello se realizarán modificaciones en las capas PHY y MAC de 
802.11 y se sustituirá la especificación BSS (Basic Service Set) actual por una más compleja 
conocida como ESS (Extended Service Set). 
- IEEE 802.11v.
Fue publicada en 2011. Y servirá para permitir la configuración remota de los dispositivos 
cliente. Esto permitirá una gestión de las estaciones de forma centralizada (similar a una red 
celular) o distribuida, a través de un mecanismo de capa de enlace de datos (capa 2). Esto 
incluye, por ejemplo, la capacidad de la red para supervisar, configurar y actualizar las \nestaciones cliente. Además de la mejora de la gestión, las nuevas capacidades proporcionadas 
por el "11v" se desglosan en cuatro categorías: 
1. Mecanismos de ahorro de energía con dispositivos de mano VoIP Wi-Fi en mente. 
2. Posicionamiento, para proporcionar nuevos servicios dependientes de la ubicación. 
3. Temporización, para soportar aplicaciones que requieren un calibrado muy preciso. 
4. Coexistencia, que reúne mecanismos para reducir la interferencia entre diferentes 
tecnologías en un mismo dispositivo. 
- IEEE 802.11w.
Es un protocolo que hace parte de IEEE 802.11 basado en el protocolo 802.11i, sirve para 
proteger redes WLAN contra ataques sutiles en las tramas de gestión inalámbricas (WLAN). 
Todavía no concluido. TGw está trabajando en mejorar la capa del control de acceso del medio de 
IEEE 802.11 para aumentar la seguridad de los protocolos de autenticación y codificación. 
Las WLAN envían la información del sistema en tramas desprotegidas, que las hace vulnerables. Este \nestándar podrá proteger las redes contra la interrupción causada por los sistemas malévolos que crean 
peticiones desasociadas que parecen ser enviadas por el equipo válido. 
Se intenta extender la protección que aporta el estándar 802.11i más allá de los datos hasta las tramas 
de gestión, responsables de las principales operaciones de una red.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Algunos de los protocolos inalámbricos con sus velocidades: 
### 🔵 Nombre 
Banda 
Velocidad 
802.11a 
5 GHz 
54 Mbps 
802.11b 
2,4 GHz 
11 Mbps 
802.11g 
2,4 GHz 
54 Mbps 
802.11n (WiFi 4) 
2,4 GHz y 5 GHz 
600 Mbps 
802.11ac (WiFi 5) 
5 GHz 
7 Gbps 
802.11ax (WiFi 6) 
2,4 y 5 GHz 
10 Gbps 
Arquitectura Wi-Fi 
Las redes Wi-Fi funcionan comúnmente en lo que se denomina modo infraestructura, donde 
necesitamos un punto de acceso al que conectarnos. 
El identificador del punto de acceso es el BSSID (Basic Service Set Identifier). 
Una red inalámbrica se identifica por el SSID. 
Habrá un único SSID en una red inalámbrica. 
Puede haber varios BSSID en una red inalámbrica (uno por punto de acceso). 
### 🔵 Seguridad 
Una red inalámbrica puede tener un sistema de cifrado para su seguridad o no tener ninguno (lo cual no \nes muy recomendable, salvo que sea una red pública). 
A continuación, vamos a ver los sistemas de cifrado utilizados: 
- WEP.
El esquema de seguridad inicial de 802.11 se llamó WEP (Wired Equivalent Privacy). 
Se basaba en el algoritmo de cifrado de flujo RC4 y una clave pre-compartida (PSK: Pre-Shared 
Key). 
El esquema original (WEP-40) para generar la clave de flujo de RC4 (64 bits) utiliza una clave 
PSK de 40 bits que se concatena con una cadena de 24 bits que identifica la red (vector de 
inicialización).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Posteriormente se comenzó a usar una clave de 128 bits (WEP-104). 
Los problemas de WEP con RC4 tienen mucho que ver con el vector de inicialización y la 
obtención de la clave de flujo, por lo que el aumento de la clave no es útil ya que el sistema sigue 
siendo inseguro. 
- WPA (Wi-Fi Protected Access).
Esta especificación se basa también en RC4 con PSK. 
Sin embargo, utiliza TKIP (Temporal Key Integrity Protocol) para mejorar la seguridad. 
TKIP realiza las siguientes comprobaciones: 
- Un control de integridad de los paquetes (ya que en los ataques algunos paquetes se alteraban sin llegarlos a descifrar). 
- Un conteo de los mismos.
- Utiliza una función para obtener la clave de RC4 mezclando la clave de usuario con el vector de inicialización de la red (en lugar de realizar una simple concatenación). 
- WPA2.
El sistema 802.11i es conocido como WPA2. 
Permite utilizar nuevos mecanismos de distribución de la clave (como EAP), autenticación 
basada en PSK o en servidores (como servidores RADIUS) y CCMP (basado en AES) para 
cifrado. 
La configuración habitual recomendada es: 
- Para entornos domésticos o pequeñas empresas:
WPA2 con clave precompartida (AES PreShared Key). 
- En entornos corporativos:
WPA2 con servidores RADIUS (EAP-TLS). 
- WPS.
WPS es el acrónimo de Wi-Fi Protected Setup, introducido en 2006 con el fin de posibilitar la 
configuración segura de las redes wifi en domicilios y oficinas. Su propósito esencial es facilitar \nel proceso de conexión de los dispositivos Wi-Fi a la red sin comprometer la seguridad.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
WPS propone distintos procedimientos de conexión evitando la introducción manual de la 
contraseña de red. Pasamos amencionar los métodos más conocidos: 
- PIN (Personal Identification Number): Posibilita la conexión de dispositivos mediante un
PIN numérico de ocho dígitos. 
- PBC (Push Button Configuration): El añadido de un botón en el enrutador, permite pulsarlo para luego conectar el dispositivo que lo solicite. 
- NFC (Near Field Communication): La tecnología NFC posibilita que se conecten al entrar \nen contacto los dispositivos compatibles.
- USB (Universal Serial Bus): La simple conexión de un dispositivo USB al enrutador a través del puerto USB del mismo establecerá la conexión permitiendo que el enrutador acceda a la 
información de configuración. 
### 🔵 9.2. Bluetooth
Se denomina Bluetooth al protocolo de comunicaciones diseñado especialmente para dispositivos de 
bajo consumo, que requieren corto alcance de emisión y basados en transceptores de bajo coste. 
Bluetooth es una especificación industrial para redes inalámbricas de área personal (WPAN) creado por 
Bluetooth Special Interest Group, Inc. que posibilita la transmisión de voz y datos entre diferentes 
dispositivos mediante un enlace por radiofrecuencia en la banda ISM de los 2.4 GHz. Los principales 
objetivos que se pretenden conseguir con esta norma son: 
- Facilitar las comunicaciones entre equipos móviles.
- Eliminar los cables y conectores entre estos.
- Ofrecer la posibilidad de crear pequeñas redes inalámbricas y facilitar la sincronización de datos \nentre equipos personales.
Los dispositivos que incorporan este protocolo pueden comunicarse entre sí cuando se encuentran 
dentro de su alcance. Las comunicaciones se realizan por radiofrecuencia de forma que los dispositivos 
no tienen que estar alineados y pueden incluso estar en habitaciones separadas si la potencia de 
transmisión es suficiente. 
Para utilizar Bluetooth, un dispositivo debe implementar alguno de los perfiles Bluetooth. Los perfiles 
son descripciones de comportamientos generales que los dispositivos pueden utilizar para comunicarse, 
formalizados para favorecer un uso unificado. La forma de utilizar las capacidades de Bluetooth se basa, 
por tanto, en los perfiles que soporta cada dispositivo. Un perfil Bluetooth, es la especificación de una 
interfaz de alto nivel, define el uso del canal Bluetooth.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Arquitectura hardware 
El hardware que compone el dispositivo Bluetooth está compuesto por dos partes: 
- Un dispositivo de radio, encargado de modular y transmitir la señal.
- Un controlador digital, compuesto por una CPU, un procesador de señales digitales (DSP -
Digital Signal Processor) llamado Link Controller (o controlador de Enlace) y de las interfaces 
con el dispositivo anfitrión. 
El LC o Link Controller se encarga del procesamiento de la banda base y del manejo de los protocolos 
ARQ y FEC de la capa física; además, se encarga de las funciones de transferencia tanto asíncrona como 
síncrona, la codificación de audio y el cifrado de datos. 
La CPU del dispositivo se encarga de las instrucciones relacionadas con Bluetooth en el dispositivo 
anfitrión, para así simplificar su operación. 
Para ello, sobre la CPU corre un software denominado Link Manager cuya función es la de comunicarse 
con otros dispositivos por medio del protocolo LMP. 
En un dispositivo de Radio Bluetooth Genérico, entre las tareas realizadas por el LC y el Link, destacan 
las siguientes: 
- Envío y Recepción de Datos.
- Paginación y Peticiones.
- Establecimiento de conexiones.
- Autenticación.
- Negociación y establecimiento de tipos de enlace.
- Establecimiento del tipo de cuerpo de cada paquete.
- Establecer el dispositivo en modo sniff o hold: El primero, sniff, significa olfatear, pero en castellano y en informática se traduce por escuchar (el medio): en este caso es la frecuencia o 
frecuencias en la que está funcionando el dispositivo. Así, cualquier paquete de datos enviado en \nesa frecuencia será "leído" por el dispositivo, aunque no vaya dirigido a él. Leerá todos los datos 
que se envíen en esa frecuencia por cualquier otro dispositivo Bluetooth, es lo que se denomina 
rastreo de paquetes. 
- Una técnica parecida, pero a nivel de frecuencias es la que se utiliza para detectar redes Wi-Fi, generalmente para encontrar redes abiertas (sin contraseña), al escanear todas las frecuencias 
se obtiene información de cada frecuencia o canal de las redes Wi-Fi disponibles. 
- Hold por su parte significa mantener, retener; esto quiere decir que el dispositivo se mantendrá \nen esa frecuencia, aunque no emita ni reciba nada, manteniendo esa frecuencia siempre disponible, aunque otros dispositivos la utilicen.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Usos de Bluetooth 
Su uso es adecuado cuando puede haber dos o más dispositivos en un área reducida sin grandes 
necesidades de ancho de banda. Su uso más común está integrado en teléfonos y tabletas, bien por 
medio de unos auriculares Bluetooth o en transferencia de ficheros. Además, se puede realizar y 
confeccionar enlaces o vincular distintos dispositivos entre sí. 
Los dispositivos que con mayor frecuencia utilizan esta tecnología pertenecen a sectores de las 
telecomunicaciones y la informática personal, como teléfonos inteligentes, teléfonos móviles, 
ordenadores, portátiles, tabletas, impresoras, altavoces inalámbricos o auriculares y cámaras digitales. 
Bluetooth simplifica el descubrimiento y configuración de los dispositivos, ya que estos pueden indicar a 
otros los servicios que ofrecen, lo que permite establecer la conexión de forma rápida (sólo la conexión, 
no la velocidad de transmisión). 
Aplicaciones de Bluetooth: 
- Conexión sin cables vía OBEX.
- Transferencia de fichas de contactos, citas y recordatorios entre dispositivos vía OBEX.
- Reemplazo de la tradicional comunicación por cable entre equipos GPS y equipamiento médico.
- Controles remotos (tradicionalmente dominado por el infrarrojo).
- Enviar pequeñas publicidades desde anunciantes a dispositivos con Bluetooth. Un negocio podría enviar publicidad a teléfonos móviles cuyo Bluetooth (los que lo posean) estuviera 
activado al pasar cerca. 
- Las consolas Sony PlayStation 3, PlayStation 4, Microsoft Xbox 360, Xbox One, Wii U y
Nintendo Switch incorporan Bluetooth, lo que les permite utilizar mandos inalámbricos, aunque \nel Gamepad original de Wii U se conecta a la consola mediante Wi-Fi y los mandos de Wii 
utilizan tecnología infrarroja para la función de puntero. 
### 🔵 Etimología y logo 
Si traducimos Blue tooth del inglés, su significado en español, es "Diente azul". 
El nombre procede del rey danés y noruego Harald Blåtand, cuya traducción al inglés es Harald 
Bluetooth. El rey es conocido por unificar las tribus danesas y convertirlas al cristianismo. Este nombre 
fue propuesto por Jim Kardach, quien desarrolló un sistema que permitiría a los teléfonos móviles 
comunicarse con los ordenadores y unificar la comunicación inalámbrica.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
 
Fuente: Wikipedia 
 
 
 
### 🔵 Anécdota 
Los alfabetos rúnicos: 
Son un grupo de alfabetos que comparten el uso de unas letras 
llamadas runas, que se emplearon para escribir en las lenguas 
germánicas, principalmente en Escandinavia y las islas Británicas, 
aunque también se usaron en Europa central y oriental, durante la 
Antigüedad y la Edad Media, antes y también durante la 
cristianización de la región. 
 
 
El logo de Bluetooth combina las runas Hagall (Runic letter ior.svg) y Berkana (Runic letter 
berkanan.svg), que corresponden a las iniciales de Harald Blåtand. 
- Hagall: Runa que representa la letra H en futhark joven y futhorc. La variante de la H en las runas del futhark antiguo sería la llamada haglaz o hagalaz. Significa granizo. 
- Berkana: Runa que representa las letras B o P en futhark joven, y que se considera originaria para la letra B latina. Significa abedul. 
#### 🔹 9.2.1. Clasificación
Podemos clasificar los dispositivos Bluetooth según su potencia de transmisión y su capacidad de canal. 
Clasificación en función a su potencia de transmisión: 
Se clasifican como "Clase 1", "Clase 2", "Clase 3" o "Clase 4" en referencia a su potencia de transmisión, 
siendo totalmente compatibles los dispositivos de una caja de ordenador.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Clase 
Potencia máxima 
permitida (mW) 
Potencia máxima 
permitida (dBm) 
Alcance (aproximado) 
Clase 1 
100 mW 
20 dBm 
~100 metros 
Clase 2 
2,5 mW 
4 dBm 
~5-10 metros 
Clase 3 
1 mW 
0 dBm 
~1 metro 
Clase 4 
0,5 mW 
-3 dBm 
~0,5 metros 
En la mayoría de los casos, la cobertura efectiva de un dispositivo de clase 2 se extiende cuando se 
conecta a un transceptor de clase 1, esto es debido a que la mayor potencia de transmisión del 
dispositivo de clase 1 permite que la señal llegue con energía suficiente hasta el de clase 2. También la 
mayor sensibilidad del dispositivo de clase 1 permite recibir la señal del otro pese a ser más débil. 
Clasificación según su capacidad de canal: 
### 🔵 Versión 
Ancho de banda (BW) 
Versión 1.2 
1 Mbit/s 
Versión 2.0 + EDR 
3 Mbit/s 
Versión 3.0 + HS 
24 Mbit/s 
Versión 4.0 
32 Mbit/s 
Versión 5 
50 Mbit/s 
#### 🔹 9.2.2. Versiones. Especificaciones
La utilidad Bluetooth se desarrolló para reemplazar el cable, en 1994 por Jaap Haartsen y Mattisson 
Sven, que estaban trabajando para Ericsson en Lund, Suecia. 
La utilidad se basa en la tecnología de saltos de frecuencia de amplio espectro. 
En sus inicios, la tecnología Bluetooth podía transmitir datos a una velocidad de 720 kbs, una capacidad 
increíble para la década de los noventa pero que hoy ya es muy limitada. 
Tras más de dos décadas de mejoras, los diferentes tipos de Bluetooth han llegado a contar con 
velocidades de hasta 50Mbs, y también el rango de conexión ha mejorado mucho, pasando de funcionar \nen distancias menores a un metro, a los más de 100 metros que pueden alcanzar hoy en día.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Las prestaciones fueron publicadas formalmente por el Bluetooth Special Interest Group (SIG), el 20 de 
mayo de 1998. Fue creado por Ericsson, IBM, Intel, Toshiba y Nokia, y posteriormente se sumaron 
muchas otras compañías. 
Todas las versiones de los estándares de Bluetooth están diseñadas para la retro compatibilidad, que 
permite que el último estándar cubra todas las versiones anteriores. 
Las versiones de Bluetooth son: 
- Bluetooth v1.0 y v1.kb.
- Bluetooth v1.1 (2002).
- Bluetooth v1.2 (2003).
- Bluetooth v2.0 + EDR (2004).
- Bluetooth v2.1 + EDR (2007).
- Bluetooth v3.0 + HS xxx (2009).
- Bluetooth v4.0 (2010).
- Bluetooth v5.0 (2016-2017).
- Bluetooth v5.1 (2019).
- Bluetooth v5.2 (2020).
Bluetooth v1.0 y v1.kb 
Las versiones 1.0 y 1.kb han tenido muchos problemas, y los fabricantes tenían dificultades para hacer 
sus productos interoperables. 
Las versiones 1.0 y 1.0k incluyen de forma obligatoria en el hardware la dirección del dispositivo 
Bluetooth (BD_ADDR) en la transmisión (el anonimato se hace imposible a nivel de protocolo), lo que 
fue un gran revés para algunos servicios previstos para su uso en entornos Bluetooth. 
Bluetooth v1.1 (2002) 
Ratificado como estándar IEEE 802.15.1-2002. Se corrigieron muchos errores en las especificaciones 
1.0b. 
Añadido soporte para canales no cifrados, e indicador de señal recibida (RSSI).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Bluetooth v1.2 (2003) 
Esta versión es compatible con USB 1.1 y las principales mejoras son las siguientes: 
- Una conexión más rápida y Discovery (detección de otros dispositivos bluetooth).
- Salto de frecuencia adaptable de espectro ampliado (AFH o Adaptive Frequency-hopping en inglés), que mejora la resistencia a las interferencias de radio frecuencia, evitando el uso de las 
frecuencias de lleno en la secuencia de saltos. 
- Mayor velocidad de transmisión, en la práctica, que en v1.1, de hasta 721 kbit/s.
- Conexiones Sincrónicas extendidas (ESCO), que mejoran la calidad de la voz de los enlaces de audio al permitir la retransmisión de paquetes corruptos, y, opcionalmente, puede aumentar la 
latencia de audio para proporcionar un mejor soporte para la transferencia de datos simultánea. 
- Host Controller Interface (HCI), con el apoyo a tres hilos UART.
- Ratificado como estándar IEEE 802.15.1-2005.
- Introdujo el control de flujo y los modos de retransmisión de L2CAP.
Bluetooth v2.0 + EDR (2004) 
La principal diferencia está en la introducción de una tasa de datos mejorada (EDR: Enhanced Data 
Rate, en inglés) para acelerar la transferencia de datos. 
La tasa nominal de EDR es de 3 Mbit/s, aunque la tasa de transferencia de datos práctica sea de 2,1 
Mbit/s.7 EDR utiliza una combinación de modulación por desplazamiento de frecuencia gausiana o 
GFSK (en inglés Gaussian Frequency Shift Keying) y modulación por desplazamiento de fase o PSK (en 
inglés Phase Shift Keying) con dos variantes, π/4-DQPSK y 8DPSK. EDR puede proporcionar un menor 
consumo de energía a través de un ciclo de trabajo reducido. 
La especificación se publica como "Bluetooth v2.0 + EDR", lo que implica que EDR es una característica 
opcional. 
Bluetooth v2.1 + EDR (2007) 
Fue adoptada por el Bluetooth SIG (Bluetooth Special Interest Group) el 26 de julio de 2007. 
La función que incorpora, es Secure Simple Pairing (SSP): se mejora la experiencia de emparejamiento 
de dispositivos Bluetooth, mientras que aumenta el uso y la fuerza de seguridad. 
También se incluye la "respuesta amplia investigación" (EIR), que proporciona más información durante \nel procedimiento de investigación para permitir un mejor filtrado de los dispositivos antes de la 
conexión, y oler subrating, lo que reduce el consumo de energía en modo de bajo consumo.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Bluetooth v3.0 + HS xxx (2009) 
La especificación Core Bluetooth9 fue aprobada por el Bluetooth SIG el 21 de abril de 2009. 
El Bluetooth 3.0+HS soporta velocidades teóricas de transferencia de datos de hasta 24 Mbit/s entre sí, 
aunque no a través del enlace Bluetooth propiamente dicho. 
La conexión Bluetooth nativa se utiliza para la negociación y el establecimiento mientras que el tráfico 
de datos de alta velocidad se realiza mediante un enlace 802.11, lo que es su principal novedad: AMP 
(Alternate MAC/PHY), la adición de 802.11 como transporte de alta velocidad. 
(Inicialmente, estaban previstas dos tecnologías para incorporar en AMP: 802.11 y UWB, pero 
finalmente UWB no se encuentra en la especificación.) 
En la especificación, la incorporación de la transmisión a alta velocidad no es obligatoria, y, por lo tanto: 
- Los dispositivos marcados con "+ HS" incorporan el enlace 802.11 de alta velocidad de transferencia de datos. 
- Un dispositivo Bluetooth 3.0, sin el sufijo "+ HS" no soporta alta velocidad, sino que solo admite una característica introducida en Bluetooth 3.0 + HS (o en CSA1). 
La Alternativa MAC / PHY permite el uso de alternativas MAC y PHY para el transporte de datos de 
perfil Bluetooth. 
La radio Bluetooth está siendo utilizada para la detección de dispositivos, la conexión inicial y 
configuración del perfil, sin embargo, cuando deben enviarse grandes cantidades de datos, se utiliza 
PHY MAC 802.11 (por lo general asociados con Wi-Fi) para transportar los datos. 
Esto significa que el modo de baja energía de la conexión Bluetooth se utiliza cuando el sistema está 
inactivo, y la radio 802.11 cuando se necesitan enviar grandes cantidades de datos. 
Unicast de datos sin conexión: Datos de los permisos de servicio para ser enviado sin establecer un 
canal L2CAP explícito. Está diseñado para su uso en aplicaciones que requieren baja latencia entre la 
acción del usuario y la reconexión/transmisión de datos. Esto solo es adecuado para pequeñas 
cantidades de datos. Control de energía mejorada. 
Se actualiza la función de control de potencia para eliminar el control de lazo abierto de energía y 
también para aclarar las ambigüedades en el control de energía presentado por los esquemas de 
modulación nuevo añadido para EDR. Control de potencia mejorada elimina las ambigüedades mediante 
la especificación de la conducta que se espera. Esta característica también añade control de potencia de 
bucle cerrado, es decir, RSSI filtrado puede empezar como se recibe la respuesta. Además, un "ir 
directamente a la máxima potencia" solicitud ha sido introducido. Con ello se espera abordar el tema 
auriculares pérdida de enlace normalmente se observa cuando un usuario pone su teléfono en un 
bolsillo en el lado opuesto a los auriculares. 
La alta velocidad (AMP), característica de la versión 3.0 de Bluetooth se basa en 802.11, pero el 
mecanismo de AMP se diseñó para ser utilizado también con otros radios.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Originalmente, fue pensado para UWB, pero la WiMedia Alliance, el organismo responsable por el sabor de 
la UWB destinado a Bluetooth, anunciado en marzo de 2009 que fue la disolución. El 16 de marzo de 
2009, la WiMedia Alliance anunció que iba a firmar un acuerdo de transferencia de tecnología para la 
WiMedia Ultra-Wideband (UWB) especificaciones. WiMedia transfiere entonces todas las especificaciones 
actuales y futuras, incluido el trabajo sobre el futuro de alta velocidad y la optimización de las 
implementaciones de energía, el Bluetooth Special Interest Group (SIG), Wireless USB Promoter Group y \nel Foro de Implementadores USB. Después de la finalización con éxito de la transferencia de tecnología, 
marketing y relacionados con cuestiones administrativas, la WiMedia Alliance dejo de operar. 
En octubre de 2009, el Bluetooth Special Interest Group suspendió el desarrollo de UWB como parte de 
la alternativa MAC / PHY, Bluetooth 3.0 + HS solution. Un número pequeño, pero significativo, de 
antiguos miembros de WiMedia no tenían y no iban a firmar acuerdos necesarios para la transferencia 
de propiedad intelectual. El SIG de Bluetooth se encontraba en esos momentos en el proceso de evaluar 
otras opciones para su plan de acción a largo plazo. 
Bluetooth v4.0 (2010) 
El SIG de Bluetooth completa la especificación del Núcleo de Bluetooth en su versión 4.0, que incluye 
Bluetooth clásico (BR/EDR), Bluetooth de alta velocidad (HS) y Bluetooth de bajo consumo (Low 
Energy, BLE). 
El Bluetooth de baja energía (Bluetooth Low Energy o BLE) es un subconjunto de Bluetooth v4.0 con 
una pila de protocolo completamente nueva, diseñada para establecer enlaces simples y eficientes en 
consumo de energía. 
Es una tecnología que permite que los dispositivos funcionen con baterías pequeñas durante largos 
períodos, lo que la hace ideal para aplicaciones de Internet de las Cosas (IoT), como sensores, 
dispositivos portátiles (wearables), balizas de localización (beacons) y sistemas de automatización. 
El 17 de diciembre de 2009, el Bluetooth SIG adoptó oficialmente la tecnología Bluetooth de bajo 
consumo como una característica distintiva de Bluetooth v4.0. Los nombres provisionales Wibree y 
Bluetooth ULP (Ultra Low Power) fueron descartados, consolidándose finalmente el término 
Bluetooth LE. 
Esta versión se adopta el 30 de junio de 2010. 
A finales de 2011, se presentaron los nuevos logotipos "Smart Bluetooth Ready" para los dispositivos 
anfitriones (compatibles con Classic y BLE) y "Smart Bluetooth" para los sensores BLE, estableciendo 
su identidad comercial. 
Como alternativa a los protocolos estándar de Bluetooth introducidos en versiones anteriores (v1.0 a 
v4.0), BLE está dirigido a aplicaciones de muy baja potencia, permitiendo la conectividad en dispositivos 
alimentados por una pila de botón. 
Los diseños de chips permiten tres tipos de implementación: 
- Modo único: Solo soporta la pila de protocolo de baja energía (BLE).
- Modo dual: Dispositivos compatibles con Bluetooth clásico (BR/EDR) y BLE.
- Versiones anteriores mejoradas: Implementaciones que optimizan la compatibilidad con BLE.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
En implementaciones de modo único solo se incluye la pila de protocolo de baja energía. CSR, Nordic 
Semiconductor y Texas Instruments han dado a conocer solo las soluciones modo Bluetooth de baja \nenergía. 
Bluetooth LE soporta topologías como punto a punto, transmisión en difusión (broadcasting) y redes \nen malla (mesh), haciéndolo versátil para aplicaciones domésticas, industriales y de proximidad. 
Bluetooth v5.0 (2016-2017) 
A mediados de 2016, SIG anuncia la llegada de Bluetooth 5 para finales del año 2016 o principios de 
2017 en su página oficial www.bluetooth.com. Afirman que tendrá el doble de velocidad, mejor 
fiabilidad y rango de cobertura; además de que contará con 800% mayor capacidad que su versión 
anterior. 
Con Bluetooth 5.0 el Bluetooth LE ofrece velocidades de hasta 2 Mbps y un alcance que varía de 10 a 50 
metros en condiciones típicas, lo que lo convierte en una opción ideal para redes de área personal 
(PAN) con necesidades de conectividad eficientes y de bajo consumo energético. 
Bluetooth v5.1 (2019) 
En enero de 2019 se presentó la versión 5.1. Entre las principales novedades que presenta está el que se 
podrán saber la ubicación de otros dispositivos a los que estén conectados. 
Esta detección no será 100% precisa como el caso del GPS, pero sí podrá determinar una ubicación con 
un margen de unos cuantos centímetros. 
Bluetooth v5.2 (2020) 
El 6 de enero de 2020 SIG presentó la versión 5.2 del protocolo Bluetooth con mejoras importantes en \nel modo de radiofrecuencia Bluetooth LE (Low Energy). 
Mejoras: 
- Se presenta el nuevo perfil EATT (Enhanced Attribute Protocol) que mejora el rendimiento cuando hay varios dispositivos BLE conectados de forma simultánea. 
- Se aumenta la seguridad al hacer las conexiones cifradas por defecto bajo el perfil EATT.
- Se disminuye el consumo y se aumenta la estabilidad de la señal al permitir optimizar dinámicamente la potencia de la transmisión (LE Power Control). 
- Se permite enviar audio sincronizado a múltiples dispositivos de manera sincronizada (LE
Isochronous Channels).

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
#### 🔹 9.2.3. Información electrónica
La especificación de Bluetooth define un canal de comunicación a un máximo 720 kbit/s (1 Mbit/s de 
capacidad bruta) con rango óptimo de 10 m (opcionalmente 100 m con repetidores). 
Opera en la frecuencia de radio de 2,4 a 2,48 GHz con amplio espectro y saltos de frecuencia con 
posibilidad de transmitir en Full Duplex con un máximo de 1600 saltos por segundo. Los saltos de 
frecuencia se dan entre un total de 79 frecuencias con intervalos de 1 MHz; esto permite dar seguridad 
y robustez. 
La potencia de salida para transmitir a una distancia máxima de 10 metros es de 0 dBm (1 mW), 
mientras que la versión de largo alcance transmite entre 20 y 30 dBm (entre 100 mW y 1 W). 
Para lograr alcanzar el objetivo de bajo consumo y bajo costo se ideó una solución que se puede 
implementar en un solo chip utilizando circuitos CMOS. De esta manera, se logró crear una solución de 
9×9 mm y que consume aproximadamente 97% menos energía que un teléfono celular común. 
El protocolo de banda base (canales simples por línea) combina conmutación de circuitos y paquetes. 
Para asegurar que los paquetes no lleguen fuera de orden, los slots pueden ser reservados por paquetes 
síncronos, empleando un salto diferente de señal para cada paquete. 
La conmutación de circuitos puede ser asíncrona o síncrona. Cada canal permite soportar tres canales 
de datos síncronos (voz) o un canal de datos síncrono y otro asíncrono. 
Cada canal de voz puede soportar una tasa de transferencia de 64 kbit/s en cada sentido, la cual es 
suficiente para la transmisión de voz. 
Un canal asíncrono puede transmitir como mucho 721 kbit/s en una dirección y 56 kbit/s en la 
dirección opuesta. Sin embargo, una conexión síncrona puede soportar 432,6 kbit/s en ambas 
direcciones si el enlace es simétrico. 
#### 🔹 9.2.4. Pila de protocolos de bluetooth
Bluetooth está definido como un protocolo de arquitectura de capa que está formado por: 
- Unos protocolos centrales.
- Protocolos de reemplazo de cable.
- Protocolos de control de telefonía.
- Y protocolos adoptados.
Como mínimo, toda pila de protocolos de Bluetooth debe tener los siguientes protocolos: LMP, L2CAP 
y SDP. 
- LMP.
El protocolo de control de enlace (Link Management Protocol, LMP) se usa para el \nestablecimiento y control del enlace de radio entre dos dispositivos. Está implementado en el 
controlador.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- L2CAP.
El protocolo de control y adaptación del enlace lógico (Logical Link Control and Adaptation 
Protocol, L2CAP) es usado para multiplexar múltiple conexiones lógicas entre dos dispositivos 
que usan diferentes protocolos de nivel superior. Proporciona segmentación y reemsamblado de 
los paquetes. 
En su modo básico, L2CAP proporciona a los paquetes una carga útil que se puede configurar 
hasta 64 kB, y con una MTU por defecto de 672 bytes. 
En los modos de Retransmisión y control de flujo, L2CAP puede configurarse para datos 
isócronos o para un canal de datos fiables mediante la retransmisión y la comprobación de CRC. 
El apéndice 1 de la especificación de Bluetooth añade dos modos adicionales a L2CAP. Estos 
nuevos modos dejan obsoletos los anteriores modos de retransmisión y control de flujo: 
- Modo de retransmisión mejorado (Enhanced Retransmission Mode, ERTM): Este modo es una versión mejorada del modo original de retransmisión. Proporciona un canal L2CAP 
confiable. 
- Modo streaming (Streaming Mode, SM): Es un modo muy simple, sin retransmisión ni control de flujo. Proporciona un canal L2CAP no confiable. 
La confiabilidad en cualquiera de estos modos es opcionalmente garantizada por la capa inferior 
BDR/EDR mediante la configuración del número de retransmisiones y el tiempo de espera antes 
de descartar paquetes. La capa inferior garantiza que los paquetes lleguen en orden. 
- SDP.
El protocolo de descubrimiento de servicio (Service Discovery Protocol, SDP) permite a un 
dispositivo descubrir servicios que ofrecen otros dispositivos y sus parámetros asociados. 
Por ejemplo, cuando usas un teléfono móvil con unos auriculares Bluetooth, el teléfono usa SDP 
para determinar qué perfil de Bluetooth pueden usar los auriculares y los ajustes del protocolo 
de multiplexación necesarios para que el teléfono pueda conectarse con los auriculares. Cada 
servicio está identificado por un UUID (Universally Unique Identifier). 
Además, los dispositivos que se comunican por Bluetooth pueden usar casi siempre los protocolos 
HCIy RFCOMM. 
- Protocolo RFCOMM.
RFCOMM (Radio Frequency Communications) es un protocolo de reemplazo de cable usado 
para generar un flujo de datos virtual en serie. RFCOMM ofrece transporte de datos binarios y \nemula las señales de control de EIA-232 a través de la capa de banda base de Bluetooth.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
RFCOMM ofrece un flujo de datos confiable y sencillo para el usuario, similar a TCP. Es utilizado 
por muchos perfiles relacionados con la telefonía. 
Muchas aplicaciones Bluetooth utilizan RFCOMM debido a su amplio soporte y la posibilidad de \nencontrar API públicas en la mayoría de sistemas operativos. Además, las aplicaciones que usen \nel puerto serie para comunicarse, podrán ser portadas a RFCOMM fácilmente. 
Otros protocolos: 
- BNEP.
El protocolo de encapsulación de red de Bluetooth (Bluetooth Network Encapsulation Protocol, 
BNEP) se usa para transferir datos de otra pila de protocolos a través de un canal L2CAP. Su 
principal propósito es la transmisión de paquetes IP en un perfil de red de área personal. BNEP 
realiza una función parecida a la que hace SNAP en las redes inalámbricas de área local. 
- AVCTP.
El protocolo de control de transporte de audio y vídeo (Control Transport Protocol), es usado 
por el perfil de control remoto para transferir órdenes de control de audio/vídeo a través de un 
canal L2CAP. Los botones de control en unos auriculares estéreo usan este protocolo para 
controlar el reproductor de música. 
Se usa para el perfil de distribución avanzada de audio para transferir música a los auriculares \nestéreo a través de un canal L2CAP pensado para la distribución de video. 
- TCS.
El protocolo de control de telefonía binario (Telephony Control Protocol - Binary, TCS BIN) es \nel protocolo orientado a bits que define la señalización del control de llamadas para el \nestablecimiento de las llamadas de voz y datos entre dispositivos Bluetooth. 
- Protocolos adoptados.
Los protocolos adoptados son aquellos que han sido definidos por otras organizaciones de \nestandarización y han sido incorporados en la pila de protocolos de Bluetooth, permitiendo a 
Bluetooth codificar protocolos solamente cuando sea necesario. Los protocolos adoptados 
incluyen: 
- Protocolo punto a punto (PPP).
Protocolo estándar de Internet para transportar datagramas IP en un enlace punto a punto. 
- TCP/IP UDP.
Protocolo base de la suite de protocolos TCP/IP. 
- Protocolo de intercambio de objetos (OBEX).
Protocolo de la capa de sesión para el intercambio de objetos, proporcionando un modelo 
para la representación de los objetos y las operaciones.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Wireless Application Environment/Wireless Application Protocol (WAE/WAP).
WAE especifica un marco de aplicación para los dispositivos inalámbricos y WAP es un \nestándar abierto que permite a los usuarios móviles acceder a los servicios de información y 
telefonía. 
#### 🔹 9.2.5. Comparaciones de bluetooth con Wi-Fi
Puede compararse la efectividad de varios protocolos de transmisión inalámbrica, como Bluetooth y 
Wi-Fi, por medio de la capacidad espacial (bits por segundo y metro cuadrado). 
5.3 Bluetooth contra Wi-Fi 
Bluetooth y Wi-Fi cubren necesidades distintas en los entornos domésticos actuales: desde la 
creación de redes y las labores de impresión a la transferencia de ficheros entre tabletas, teléfonos 
inteligentes y ordenadores personales. Ambas tecnologías operan en las bandas de frecuencia no 
reguladas (banda ISM). 
Wi-Fi: 
- Es similar a la red Ethernet tradicional y como tal el establecimiento de comunicación necesita una configuración previa. 
- Utiliza el mismo espectro de frecuencia que Bluetooth con una potencia de salida mayor que lleva a conexiones más sólidas. 
- A veces se denomina al Wi-Fi la "Ethernet sin cables". Aunque esta descripción no es muy precisa, da una idea de sus ventajas e inconvenientes en comparación a otras alternativas. 
- Se adecua mejor para redes de propósito general: permite conexiones más rápidas, un rango de distancias mayor y mejores mecanismos de seguridad. 
Wi-Fi Direct. 
- Es un programa de certificación que permite que varios dispositivos Wi-Fi se conecten entre sí sin necesidad de un punto de acceso intermedio. 
- Cuando un dispositivo ingresa al rango del anfitrión Wi-Fi Direct, éste se puede conectar usando \nel protocolo ad hoc existente, y luego recolecta información de configuración usando una transferencia del mismo tipo de la de Protected Setup. 
- La conexión y configuración se simplifican de tal forma que algunos sugieren que esto podría reemplazar al Bluetooth en algunas situaciones. 
- Puesto que sus ventajas son una mayor velocidad de transferencia (11 Gbps de 802.11ax contra
50 Mbps de Bluetooth 5.0), cubre una distancia mayor (100 metros contra 10 metros de 
Bluetooth) y una mayor seguridad teórica al emplear un cifrado de 256 bits contra los 128 bits 
de Bluetooth.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Sin embargo, las ventajas que ofrece la tecnología Bluetooth en contrapartida son un menor 
consumo de energía, la posibilidad de usar más de un dispositivo a la vez y que la distancia reducida 
minimiza el riesgo de interferencias. 
#### 🔹 9.2.6. IEEE 802.15
El protocolo IEEE 802.15 está ampliamente relacionado con el BLUETOOTH por lo que vamos a verlo 
con un poco más de profundidad. 
IEEE 802.15 es un grupo de trabajo dentro de IEEE 802 especializado en redes inalámbricas de área 
personal (Wireless Personal Area Networks, WPAN). 
Los estándares que desarrolla definen redes tipo PAN o HAN, centradas en las cortas distancias. Al igual 
que Bluetooth o ZigBee, el grupo de estándares 802.15 permite que dispositivos portátiles como PC, 
PDAs, teléfonos, pagers, sensores y actuadores utilizados en domótica, entre otros, puedan 
comunicarse e interoperar. 
Debido a que Bluetooth no puede coexistir con una red inalámbrica 802.11.x, se definió este estándar 
para permitir la interoperabilidad de las redes inalámbricas LAN con las redes tipo PAN o HAN. 
Se divide en 10 áreas de trabajo, aunque no todas están activas actualmente. El número de grupos de 
trabajo varía dependiendo del número de proyectos activos. 
La lista completa de proyecto activos está disponible en la web de IEEE 802.15 
Áreas de trabajo: 
- Grupo de trabajo 1: WPAN/Bluetooth.
IEEE 802.15.1-2002 desarrolla un estándar basado en la especificación 1.1 de Bluetooth. Define 
la capa física (PHY) y de control de acceso al medio (MAC) para la conectividad inalámbrica 
tanto de dispositivos estacionarios como móviles dentro de un área personal. Se ha publicado 
una versión actualizada, IEEE 802.15.1-2005. 
- Grupo de trabajo 2: Coexistencia.
IEEE 802.15.2-2003 estudia los posibles la coexistencia de redes personales inalámbricas 
(WPAN) con otros dispositivos inalámbricos que utilicen las bandas de frecuencia no reguladas, 
tales como redes inalámbricas de área local (WLAN). El grupo de trabajo 2 quedó inactivo 
indefinidamente tras publicar el estándar IEEE 802.15.2-2003 en 2003.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Grupo de trabajo 3: WPAN de alta velocidad.
- 3.1 IEEE 802.15.3-2003 (WPAN de alta velocidad).
Es un estándar que define los niveles físicos y de enlace para WPANs de alta velocidad (11-
55 Mbit/s). El estándar puede ser descargado a través del IEEE Get Program, que fue 
fundado por voluntarios del IEEE 802. 
- 3.2 IEEE 802.15.3a (Capa física alternativa para WPAN de alta velocidad).
Intentó realizar mejoras al nivel físico de las redes Ultra-WideBand (UWB) para conseguir 
mayor velocidad y poder aplicarlo en aplicaciones que trabajen con elementos multimedia. 
Su aspecto más destacable fue la consolidación de veintitrés especificaciones de PHY para 
UWB en dos propuestas utilizando multiplexación por división de frecuencias ortogonal 
multibanda (Multi-Band Orthogonal Frequency Division Multiplexing, MB-OFDM) en UWB 
y UWB en secuencia directa (DS-UWB, soportada por el UWB Forum). 
El 19 de enero de 2006, los miembros del grupo votaron para anular la petición de proyecto 
que iniciaba el desarrollo de estándares de alta velocidad para UWB, pues el proceso se \nencontraba bloqueado por completo. Había dos propuestas distintas respaldadas por dos 
alianzas distintas, una de las cuales estaba dispuesta a aunar esfuerzos (mientras que la otra 
no lo estaba, pero poseía votos suficientes para vetar decisiones). 
Finalmente se acordó que el mercado decidiera. La tecnología presenta bastantes 
problemas con su regulación debido a que, desde el punto de vista del desarrollo de \nestándares, seguramente es aún demasiado pronto para estandarizar UWB dado el 
desconocimiento del mercado a nivel mundial. 
Los documentos relacionados con el desarrollo del IEEE 802.15.3a fueron archivados y se 
pueden consultar en el servidor de documentos del IEEE. 
- 3.3 IEEE 802.15.3b-2006 (Revisión MAC).
Fue publicado el 5 de mayo de 2006. Define mejoras para refinar la implementación e 
interoperabilidad de la capa MAC. Esto incluye optimizaciones menores que preservan la 
compatibilidad en todos los casos, además de corregir errores y ambigüedades, así como 
realizar aclaraciones, siempre manteniendo la compatibilidad con versiones anteriores. 
Entre otros cambios, define las siguientes características: 
» Un nuevo punto de acceso de servicio de la entidad manejadora de la capa MAC. 
» Una nueva política de reconocimientos que permiten el polling. 
» Cabeceras LLC/SNAP. 
» Asignación de direcciones de multidifusión. 
» Múltiples periodos de contención dentro de una supertrama.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
» Un método para ceder el tiempo del canal a otro dispositivo del área personal. 
» Recuperación de la red más rápida en el caso de que el coordinador de la red se 
desconecte abruptamente. 
» Un método por el cual un dispositivo puede devolver información acerca de la calidad 
de la señal en un paquete recibido. 
- 3.4 IEEE 802.15.3c-2009 (PHY alternativa de onda milimétrica).
El grupo de trabajo 3c (TG3c) se formó en marzo de 2005 y trabajó en el desarrollo de una 
capa física alternativa basada en ondas milimétricas para el estándar 802.15.3-2003. Fue 
publicado el 11 de septiembre de 2009. Estas ondas milimétricas operan en el rango 57-66 
GHz, aunque dependiendo de la región geográfica, estará disponible cualquier banda entre 
2 y 9 GHz. 
Este nuevo estándar permite una tasa de transferencia muy alta en cortas distancias. Esto 
incluye el acceso a Internet a alta velocidad, descarga de contenido en streaming 
(televisión digital, cine en casa, etc.), emisiones en directo y además proporciona un bus de 
datos inalámbrico como alternativa a los cables. Se definieron un total de tres modos para 
la capa física: 
» Modo de una sola portadora (Singler Carrier, SC): hasta 5.3 Gbit/s. 
» Modo de interfaz de alta velocidad (High Speed Interface, HSI): una sola portadora, 
hasta 5Gbit/s. 
» Modo de audio/video (AV): OFDM, hasta 3.8 Gbit/s. 
- Grupo de trabajo 4: WPAN de baja velocidad.
- IEEE 802.15.4 (WPAN de baja velocidad).
IEEE 802.15.4-2003 (WPAN's de baja velocidad, Low Rate WPAN) trata las necesidades de 
sistemas con poca transmisión de datos, pero vidas útiles muy altas con alimentación 
limitada (pilas, baterías...) y una complejidad muy baja. La primera revisión se aprobó en 
mayo de 2003. El estándar define la capa física y la de enlace de datos del modelo OSI. Tras 
la formación del grupo 4b en marzo de 2004 este grupo pasó a estado latente. Los 
protocolos ZigBee se basan en la especificación producida por este grupo de trabajo. 
El grupo de trabajo 6loWPAN del Internet Engineering Task Force (IETF) trabaja en 
métodos para trabajar con redes IPv6 sobre esta base. Ya está disponible el RFC 4919 que 
describe los supuestos, la descripción del problema y las metas para transmitir IP sobre 
redes 802.15.4. 
- IEEE 802.15.4a (PHY alternativa).
Es una mejora de IEEE 802.15.4 que añade capas físicas adicionales al estándar original. El 
principal interés de este grupo es permitir comunicaciones y facilidades de localización de 
alta precisión (de un metro y mejor), alta productividad agregada y necesidades \nenergéticas extremadamente reducidas.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
También busca la escalabilidad en las tasas de transferencia de datos, distancia de 
transmisión, coste y consumo. 
En marzo de 2005 se seleccionó una especificación de base, consistente en dos PHY 
opcionales que utilizan una radio de pulso UWB (opera en las bandas UWB no reguladas) y 
técnicas de espectro de dispersión Chirp (en la banda de 2,4 GHz). La radio de pulso UWB 
se basa en la tecnología UWB de pulso continuo (continuous pulsed UWB, C-UWB) que es 
capaz de dar las prestaciones requeridas. 
- IEEE 802.15.4b (Revisiones y mejoras).
Se aprobó en junio de 2006 y se publicó en septiembre del mismo año como IEEE 802.15.4-
2006. 
Este grupo se inició con un proyecto de realización de mejoras y aclaraciones específicas 
sobre IEEE 802.15.4-2003. Entre estos objetivos se encuentran la resolución de 
ambigüedades y reducción de complejidad innecesaria, el incremento de la flexibilidad en el 
uso de claves de seguridad, las consideraciones para el uso de nuevos rangos de frecuencias 
disponibles y otros aspectos. 
- IEEE 802.15.4c (Modificación de la capa física para China).
Fue aprobada en 2008 y publicada en enero de 2009. Esta modificación de las capas físicas 
añade nuevas especificaciones en el espectro de radiofrecuencia, para adaptarse a los 
cambios de normativas que hay en China que han abierto las bandas de 314-316 MHz, 430-
434 MHz, y 779-787 MHz para el uso de PAN inalámbricas dentro de China. 
- IEEE 802.15.4d (Modificación de la capa física y de control de acceso al medio para Japón).
Fue constituido para definir una modificación en el estándar existente 802.15.4 de 2006. La 
modificación contempla cambios tanto en la capa física como en la de control de acceso al 
medio que son necesarios para soportar la asignación de una nueva frecuencia (950 MHz -
956 MHz) en Japón, mientras coexisten con otros sistemas de protocolos en la frecuencia 
de banda. 
- IEEE 802.15.4e (Modificación de la capa MAC para aplicaciones industriales).
Fue constituido para definir una modificación en el estándar existente 802.15.4 de 2006. 
Las mejoras más específicas fueron realizadas para añadir saltos de canal y una opción de 
intervalos de tiempos variables compatibles con ISA100.11a. Estos cambios fueron 
aprobados en 2011. 
La intención de esta modificación era mejorar y agregar nuevas funcionalidades a la capa 
MAC, que básicamente consisten en: 
» Mejorar el apoyo a los mercados industriales. 
» Permitir la compatibilidad con las modificaciones que se propusieron en el WPAN de 
China.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- IEEE 802.15.4f (Modificación en la capa física y la identificación por radiofrecuencia o
RFID). 
Fue constituido para definir nuevas capas físicas inalámbricas y mejoras con respecto al \nestándar de la capa MAC 802.15.4 del 2006 necesarias en las nuevas capas físicas para la 
identificación por frecuencia o RFID bidireccional. 
- IEEE 802.15.4g Modificación de la capa física para Herramientas de Red Inteligentes
(SUN). 
Fue constituido para crear una nueva capa física que modifique 802.15.4 para proporcionar 
un estándar que facilite, a gran escala, aplicaciones de control de procesos como la utilidad 
de redes inteligentes capaces de soportar geográficamente diversas redes con una mínima 
infraestructura. Recientemente han surgido noticias sobre el estándar de radio 802.15.4g. 
- Grupo de trabajo 5: Redes en malla.
IEEE 802.15.5 proporciona la estructura del marco de trabajo que permite a los dispositivos de 
una WPAN promover una red inalámbrica en malla interoperable, estable y escalable. El \nestándar está dividido en dos partes: redes WPAN en malla de baja tasa y redes WPAN en malla 
de alta tasa. Las de baja tasa, utilizan la capa MAC de IEEE 802.15.4-2006 mientras que las de 
alta tasa usan la capa MAC de IEEE 802.15.3/3b. Las características comunes de ambas incluyen 
la inicialización de la red, el direccionamiento, y la unidifusión multisalto. Además, las de baja 
tasa soportan multidifusión, difusión fiable, portabilidad, seguimiento de los paquetes y función 
de ahorro de energía. Las de alta tasa soportan el servicio de multisalto con tiempo reservado. 
- Grupo de trabajo 6: Red de Área Corporal (Body Area Network, BAN).
En diciembre de 2011, el IEEE 802.15.6 aprobó un borrador del estándar BAN. El borrador fue 
aprobado el 22 de julio de 2011. El grupo de trabajo 6 se formó en noviembre de 2007 para 
trabajar en un estándar inalámbrico de baja potencia y corto rango que estuviera optimizado 
para su uso en o alrededor del cuerpo humano (aunque sin ser limitado a humanos). Este 
podía servir para una gran variedad de aplicaciones, que incluían aplicaciones médicas, de \nelectrónica de consumo o de entretenimiento personal. Optimiza el bajo consumo de energía. 
Este estándar define tanto las capas físicas como de enlace, las cuales pueden satisfacer las 
necesidades de las BAN. 
- Grupo de trabajo 7: Comunicación de Luz Visible (Visible Light Communication, VLG).
En diciembre de 2011, el grupo de trabajo IEEE 802.15.7 completó el borrador 5c de un \nestándar de capa física y de enlace para la comunicación a través de la luz visible. La conferencia 
de inauguración del grupo de trabajo 7 se realizó en enero de 2009, en donde decidieron escribir \nestándares para la comunicación óptica mediante luz visible a través del espacio libre. Este 
método se caracteriza por la comunicación inalámbrica de corto alcance por medio de \nespectros de luz. Su mayor ventaja es que permite altas velocidades de datos (hasta 96Mb/s). 
El espectro de luz visible se sitúa en longitudes de onda entre 380 - 789 nm.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Grupo de trabajo 8: Comunicación por pares (Peer Aware Communication, PAC).
El IEEE 802.15.8 recibió la aprobación para formar un grupo de trabajo, el 29 de marzo de 2012, 
con la intención de trabajar en el desarrollo de un estándar para la comunicación entre pares 
(PAC) optimizada para P2P y comunicaciones sin infraestructura con una total coordinación 
distribuida que opere en bandas por debajo de 11 GHz. Algunos de los elementos que incluye 
son los siguientes: 
- Descubrimiento de información del otro dispositivo sin necesidad de asociación.
- Tasa de señalización de descubrimiento, normalmente 100 kbps.
- Número de dispositivos escalable durante el descubrimiento.
- Tasa de transmisión de datos escalable, normalmente 10 Mbps.
- Comunicaciones multigrupo simultáneas, normalmente hasta 10.
- Posicionamiento relativo.
- Retransmisión multisalto.
- Seguridad.
El grupo de trabajo 8 sigue aún activo en 2017. La última actualización de su trabajo se realizó \nen noviembre de 2016. 
- Grupo de trabajo 9: Protocolo de Administración de Claves (Key Management Protocol, KMP).
El IEEE 802.15.9 recibió la aprobación para crear el grupo de trabajo 9 el 7 de diciembre de 2016 
según la IEEE. Su intención era desarrollar unas prácticas recomendadas para el transporte de 
los datagramas del protocolo de administración de claves (KMP). 
La práctica recomendada definirá un marco de trabajo del mensaje basado en elementos de la 
información, como pueden ser un método de transporte para los datagramas del protocolo de 
administración de claves y unas líneas generales para el uso de los ya existentes KMP con el IEEE 
802.15.4. La práctica recomendada no crea un nuevo KMP. 
Aunque el IEEE 802.15.4 siempre ha soportado la seguridad en los datagramas, no ha 
proporcionado un mecanismo para establecer las claves usadas por esta seguridad. 
La carencia de soporte para la administración de las claves en IEEE 802.15.4 puede resultar en 
claves poco seguras, que es un desencadenante muy común para el ataque al sistema de 
seguridad. Añadir soporte para KMP es imprescindible para un marco de trabajo con una 
seguridad apropiada. Algunos de los KMP existentes que se pueden utilizar son IETF's PANA, 
HIP, IKEv2, IEEE 802.1X y 4-Way-Handshake. 
El borrador de las prácticas recomendadas aún sigue en desarrollo. Se puede obtener más 
información acerca del estado del mismo en la web de IEEE 802.15.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Grupo de trabajo 10: Enrutamiento de capa 2.
El IEEE 802.15.10 recibió la aprobación para formar el grupo de trabajo 10 el 23 de agosto de 
2017 según la página oficial de IEEE. Su intención era desarrollar una práctica recomendada para \nel enrutamiento de los paquetes en la red inalámbrica dinámica cambiante de 802.15.4. Estas 
prácticas debían tener un impacto mínimo en el manejo del enrutamiento. El objetivo era \nextender el área de cobertura conforme fuera aumentando el número de nodos. 
Las características relacionadas con el enrutamiento que la práctica recomendada proporciona 
son las siguientes: 
- Establecimiento de la ruta.
- Reconfiguración dinámica de la ruta.
- Descubrimiento y adicción de nuevos nodos.
- Ruptura de las rutas establecidas.
- Pérdida y reaparición de rutas.
- Recolección en tiempo real del estado del enlace.
- Permitir la aparición de un solo salto en la capa de red.
- Soporte para difusión.
- Soporte para multidifusión.
- Reenvío eficiente de tramas.
El desarrollo de este borrador aún sigue en proceso. Se puede obtener más información del estado del 
mismo en la web de IEEE 802.15.10. 
### 🔵 9.3. RFID (Radio Frequency Identification)
RFID es una tecnología que utiliza ondas de radio para identificar y rastrear objetos de manera 
automática. Esta tecnología funciona mediante un sistema que consta de dos componentes principales: 
un lector y una etiqueta RFID. La etiqueta RFID es un pequeño dispositivo que contiene un chip para 
almacenar información y una antena que permite la transmisión y recepción de señales. El lector RFID \nemite una señal de radio a una frecuencia específica, que es recibida por la etiqueta, la cual, al activarse, 
transmite de vuelta al lector la información almacenada en su chip. 
Existen dos tipos de etiquetas RFID: 
- Las etiquetas pasivas, que no necesitan una fuente de alimentación propia y solo se activan cuando reciben la señal del lector. 
- Las etiquetas activas, que cuentan con su propia fuente de energía y pueden emitir señales de manera autónoma.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Las etiquetas pasivas suelen ser más baratas y tienen un alcance de lectura más corto, mientras que las \netiquetas activas, al tener batería propia, pueden tener un alcance más largo y enviar señales por su 
cuenta. 
El proceso de funcionamiento de RFID es el siguiente: el lector emite una señal de radio que activa la \netiqueta, la cual responde enviando la información almacenada en su chip al lector. Esta información 
puede ser un identificador único, que el sistema utiliza para registrar, rastrear o gestionar el objeto al 
que la etiqueta está adherida. Una vez recibida la información, el lector la transmite al sistema de 
gestión de datos, donde se procesa y se puede usar para tareas como seguimiento de inventarios, 
control de acceso o pago sin contacto. 
RFID es ampliamente utilizado en diversas aplicaciones, como la gestión de inventarios, el control de 
acceso a edificios, el seguimiento de productos en la cadena de suministro, la identificación de 
vehículos, el rastreo de bienes en almacenes y el pago sin contacto en sistemas de transporte público o \nen comercios. La ventaja principal de RFID es que no requiere contacto físico entre el lector y la \netiqueta, lo que facilita la identificación rápida y remota de objetos, además de permitir el seguimiento \nen tiempo real de los mismos. 
### 🔵 9.4. NFC (Near Field Communication)
NFC es una tecnología de comunicación inalámbrica de corto alcance que permite la interacción entre 
dispositivos cuando se encuentran muy cerca, generalmente a unos 10 cm o menos. NFC se basa en la 
tecnología RFID, pero con la principal diferencia de que permite la comunicación bidireccional entre los 
dispositivos, lo que significa que ambos pueden transmitir y recibir información de manera activa. Esto 
lo convierte en una opción más dinámica que RFID, que generalmente solo permite la lectura de datos 
desde una etiqueta pasiva a un lector. 
El funcionamiento de NFC involucra la transmisión de datos mediante ondas de radio en la frecuencia de 
13.56 MHz. Al igual que RFID, utiliza etiquetas y lectores, pero en el caso de NFC, ambos dispositivos 
pueden actuar como emisor y receptor. Un dispositivo NFC puede estar en modo activo (transmitiendo 
y recibiendo señales) o en modo pasivo (solo leyendo datos desde una etiqueta o dispositivo que esté \nemitiendo señales). Cuando un dispositivo NFC, como un teléfono móvil, se acerca a una etiqueta NFC 
o a otro dispositivo NFC, se establece una comunicación que permite el intercambio de información, 
como datos de pago, información de contacto o acceso a servicios. 
El proceso de interacción con NFC comienza cuando los dispositivos están lo suficientemente cerca uno 
del otro. El dispositivo que actúa como lector emite una señal de radio que es captada por el dispositivo 
pasivo (como una etiqueta NFC), que a su vez responde enviando la información que contiene. Si 
ambos dispositivos son activos, como en el caso de dos teléfonos móviles, ambos pueden intercambiar 
información de manera recíproca, lo que habilita una comunicación bidireccional. 
NFC se utiliza principalmente en aplicaciones donde la proximidad y la seguridad son cruciales. Entre sus 
principales aplicaciones están los pagos móviles (como Apple Pay, Google Pay o Samsung Pay), que 
permiten realizar transacciones financieras sin contacto físico, simplemente acercando el teléfono a un 
terminal de pago. Además, se usa en sistemas de acceso sin contacto, como tarjetas de transporte 
público o sistemas de control de acceso a edificios, y en la transferencia de información entre 
dispositivos, como el intercambio de archivos o el emparejamiento de dispositivos Bluetooth.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
Una de las principales ventajas de NFC es su capacidad para facilitar interacciones rápidas y seguras, 
debido a su corto alcance y su naturaleza bidireccional. Además, es fácil de implementar en dispositivos 
como teléfonos móviles, lo que ha hecho que esta tecnología sea cada vez más común en la vida 
cotidiana. Sin embargo, su principal limitación es que su alcance limitado restringe su uso en situaciones 
donde se necesita una comunicación de mayor distancia. 
### 🔵 9.5. ZigBee
Tecnología y estándar IEEE 802.15.4 
ZigBee es una tecnología de comunicación inalámbrica diseñada para redes de bajo consumo de \nenergía, bajo costo y aplicaciones de corto alcance. Está basada en el estándar IEEE 802.15.4, y está 
orientada a la creación de redes de dispositivos interconectados, principalmente en entornos de 
automatización del hogar y Internet de las Cosas (IoT). A diferencia de otras tecnologías de 
comunicación inalámbrica, como Wi-Fi o Bluetooth, ZigBee está específicamente optimizada para 
dispositivos pequeños y de bajo consumo energético que requieren una comunicación continua, pero 
sin la necesidad de gran ancho de banda. 
### 🔵 Funcionamiento y red en malla 
El funcionamiento de ZigBee se basa en una arquitectura de red en malla, lo que significa que los 
dispositivos dentro de la red pueden actuar como repetidores para reenviar señales entre otros 
dispositivos. Esta estructura de malla mejora la fiabilidad y cobertura de la red, ya que, si un dispositivo 
no puede comunicarse directamente con el coordinador de la red, puede hacerlo a través de otros 
dispositivos que estén dentro del alcance. Esta capacidad permite extender la cobertura de la red sin 
necesidad de añadir repetidores adicionales de manera costosa. 
### 🔵 Frecuencia y cobertura 
ZigBee utiliza la banda de 2.4 GHz para la transmisión de datos, que es una frecuencia comúnmente 
utilizada en muchas aplicaciones inalámbricas. A pesar de tener un rango limitado (aproximadamente 
10-100 metros en condiciones ideales), la capacidad de formar redes de malla permite que la cobertura 
de la red sea considerablemente mayor, ya que los dispositivos pueden retransmitir las señales entre sí. 
Esta característica la hace especialmente útil en aplicaciones de domótica, como el control de luces, 
termostatos, persianas automáticas, sistemas de alarma, cerraduras inteligentes y dispositivos de 
monitoreo de energía. 
### 🔵 Tipos de dispositivos en la red 
El proceso de funcionamiento de ZigBee incluye la creación de una red formada por tres tipos de 
dispositivos: coordinador, enlace y dispositivo final. El coordinador es el encargado de gestionar la red, \nestableciendo y manteniendo la conexión entre los dispositivos. Los enlaces ayudan a transmitir las 
señales entre los dispositivos, actuando como repetidores. Los dispositivos finales son aquellos que 
realizan la acción principal de la red, como sensores o interruptores. Estos dispositivos pueden enviar y 
recibir datos, pero no retransmiten señales.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
### 🔵 Ventajas principales 
Una de las grandes ventajas de ZigBee es su bajo consumo energético, lo que permite que los 
dispositivos funcionen durante largos períodos de tiempo con baterías pequeñas, lo que resulta ideal 
para aplicaciones donde los dispositivos no pueden o no deben ser recargados frecuentemente. 
Además, ZigBee es escalable, lo que significa que una red puede contener desde unos pocos hasta miles 
de dispositivos conectados, sin que el rendimiento se vea afectado. 
ZigBee también destaca por ser una tecnología económica en términos de hardware y de 
implementación, lo que la hace atractiva para aplicaciones de bajo costo, como la automatización de 
viviendas, gestión de energía o monitoreo ambiental. Su seguridad también es una de sus ventajas, ya 
que incluye características de encriptación y autenticación para garantizar la protección de los datos 
transmitidos en la red. 
## 🟣 10. TETRA
TETRA son las siglas del inglés del inglés Trans European Trunked Radio. También como Terrestrial 
Trunked Radio, es un estándar de radio digital definido por el Instituto Europeo de Normas de 
Telecomunicaciones (ETSI) para las comunicaciones críticas. 
Este patrón define un sistema móvil digital de radio y nace por decisión de la Unión Europea con el 
objeto de unificar diversas alternativas de interfaces de radio digitales para la comunicación entre los 
profesionales de diferentes sectores, como la Seguridad Pública y agencias gubernamentales de 
Seguridad y El segmento del Transporte, incluyendo el Transporte Público masivo y Aeropuertos. 
### 🔵 10.1. Características
Se diferencia de la telefonía GSM por las siguientes características: 
- Utilización de una banda de frecuencias mucho más baja.
Esto supone una menor necesidad de equipos repetidores para dar cobertura a una misma zona 
geográfica. 
- Infraestructura propia separada de las redes de telefonía móvil públicas.
Ya que las estaciones repetidoras trabajan a mayor distancia. 
- Puede trabajar en modo terminal a terminal, en caso de fallo en las comunicaciones.
- Es un sistema digital más moderno que GSM con calidad de sonido superior al implementar sistemas más modernos de compresión de datos. 
- Las capacidades de transmisión de datos están definidas en el propio estándar inicial y sólo son comparables al actual patrón GPRS.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Mejor aprovechamiento del canal, ya que permite comunicaciones semidúplex como la radio convencional o dúplex como el teléfono en casos necesarios, utilizando los canales 
desocupados. 
- Menor grado de saturación, ya que la norma garantiza una capacidad por defecto superior al doble de los canales convencionales en uso. Además, dispone de comunicaciones priorizadas, 
por lo que en caso de saturación se garantizan la disponibilidad de estas comunicaciones 
prioritarias. 
- Permite comunicaciones grupales lo que mejora la gestión para coordinación en las urgencias.
- Dispone de terminales específicos para cada necesidad. Así dispone de terminales portátiles
(equiparables a teléfonos móviles), terminales móviles (destinados a vehículos) y terminales 
para bases. 
Tetra es una versión mejorada de Radio Trunking 
Radio Trunking que son sistemas de radiocomunicaciones móviles para aplicaciones privadas, formando 
grupos y subgrupos de usuarios, con las siguientes características principales: 
- Estructura de red celular (independientes de las redes públicas de telefonía móvil).
- Los usuarios comparten los recursos del sistema de forma automática y organizada.
- Cuando se requiere, por el tipo de servicio, es posible el establecimiento de canales prioritarios de emergencia que predominarían sobre el resto de comunicaciones del grupo. 
- Es un sistema de radio en el que todas las comunicaciones van precedidas de un código de llamada similar a una telefónica; si nuestro equipo la recibe y no es el destinatario la emite de 
nuevo, actuando como repetidor, y si es el destinatario se establece un circuito para asegurar la 
comunicación. 
Por lo tanto, sólo oímos las comunicaciones destinadas a nosotros. Dependiendo del servicio 
instalado se puede implementar conexión a la red de telefonía pública. 
### 🔵 10.2. Inconvenientes
Los inconvenientes principales frente a GSM son: 
- Soporta una menor densidad de usuarios que los servicios de GSM debido al tipo de modulación realizada. 
- Los terminales tienen un precio mucho mayor al estar dirigido a sectores diferentes y no disponer de un mercado masivo de clientes.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- Las transferencias de datos son más lentas (max 19 Kbps), aunque se está mejorando en versiones más modernas de esta tecnología. 
- Debido a la baja modulación de frecuencia, los terminales pueden interferir con dispositivos \nelectrónicos sensibles, como marcapasos o desfibriladores, lo cual es contraproducente dándole ventaja a la radio analógico UHF/VHF. 
### 🔵 10.3. Frecuencias
La modulación usada en este protocolo es DQPSK, sigla de Dual-polarization quadrature phase shift 
keying (que puede traducirse como Modulación por desplazamiento de fase en cuadratura de 
polarización dual), esquema que implica la multiplexación de polarización de dos señales diferentes 
QPSK, lo que duplica la eficiencia espectral. El formato de acceso es TDMA, también utiliza TDD/FDD 
(División doble). 
En Europa, la tecnología TETRA utiliza las siguientes frecuencias: 
### 🔵 Servicios de emergencia 
Servicio Público 
### 🔵 Número 
Pareja de frecuencias (MHz) 
### 🔵 Número 
Pareja de frecuencias (MHz) 
 
Banda 1 
Banda 2 
 
Banda 1 
Banda 2 
380-383 
390-393 
410-420 
420-430 
383-385 
393-395 
870-876 
915-921 
 
450-460 
460-470 
385-390 
395-399,9 
### 🔵 10.4. Documentos oficiales
Las normativas sobre el Sistema TETRA se revisan y se publican. 
- Instituto Europeo de Normas de Telecomunicaciones (ETSI).
https://www.etsi.org/. 
En estándares, se pueden encontrar las publicaciones sobre Terrestrial Trunked Radio. 
- Documento BOE-A-2009-3110.
https://www.boe.es/diario_boe/txt.php?id=BOE-A-2009-3110.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
## 🟣 11. Bibliografía
- FOROUZAN, B., Transmisión de datos y redes de comunicaciones. Editorial MC Graw Hill.
- http://www.serbi.ula.ve/serbiula/libros-\nelectronicos/Libros/trasmisiondedatos/pdf/librocompleto.pdf.
- https://radiosyculturalibre.com.ar/compartir/biblioteca/REDES/redes-de-
comunicaciones.pdf. 
- https://www.uaeh.edu.mx/scige/boletin/huejutla/n9/r1.html.
- http://en.wikipedia.org.
- www.acm.org/sigcomm/sos.html.
- www.ietf.org/.
- https://www.monografias.com/docs110/transmision-datos-analogicos-y-
digitales/transmision-datos-analogicos-y-digitales.shtml. 
- http://neo.lcc.uma.es/evirtual/cdd/tutorial/fisico/Transda.html.
- http://flowersfour14.blogspot.com/.
- https://mediosdetransmisionyperturbaciones.wordpress.com/perturbaciones/.
- https://es.slideshare.net/marthasol/perturbaciones-en-la-transmisin-3431088.
- https://guimi.net/monograficos/G-Cableado_estructurado.
- https://www.siemon.com/la/category7/.
- http://mediosdetransmisionnoguiados.blogspot.com/.
- https://rodas5.us.es/file/46f96617-a8e3-4999-845c-816f4c95cbe6/1/Tema_3.pdf.
- http://www.dte.us.es/personal/mcromero/docs/arc1/tema3-arc1.pdf.
- http://www.scielo.org.bo/scielo.php?script=sci_arttext&pid=S2518-44312015000100002.
- https://definicion.de.
- https://www.ecured.cu/Modulación.
- https://es.slideshare.net/johnwlad18/interfaz-dte-dce.
- https://unitel-tc.com/normas-sobre-cableado-estructurado/.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- http://normcableestruc.blogspot.com/2017/.
- https://www.c3comunicaciones.es/.
- https://campusvirtual.univalle.edu.co/moodle/pluginfile.php/56106/mod_resource/content/
0/03_-_Arquitectura_Modelo_de_Referencia_OSI_TCP_IP.pdf. 
- https://es.slideshare.net/kcfariam/dispositivos-y-protocolo-de-interconexion.
- http://www.nmt.com.mx/blogposts/dominios-de-colision-y-broadcast.php.
- https://es.wikipedia.org/wiki/MIMO.
- TANENBAUM, W. Redes de computadoras 5ª edición. Editorial Pearson.
- FOROUZAN, B. Transmisión de datos y redes de comunicaciones. Editorial MC Graw Hill.
- https://radiosyculturalibre.com.ar/compartir/biblioteca/REDES/redes-de-
comunicaciones.pdf. 
- https://www.1and1.es/digitalguide/servidores/know-how/los-tipos-de-redes-mas-
conocidos/. 
- https://es.scribd.com/document/359443990/TICB4-Conmutacion-pdf.
- https://www.techopedia.com/definition/9593/switched-virtual-circuit-svc.
- http://www.networkworld.es/telecomunicaciones/como-funciona-mpls.
- https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-
mpls/mpls/4649-mpls-faq-4649.html. 
- https://www.ecured.cu/Conmutaci%C3%B3n_(Redes_de_comunicaci%C3%B3n).
- https://ldc.usb.ve/~rgonzalez/Cursos/redes/laminas/Tema8_Parte1.pdf.
- http://www.ac.uma.es/~nico/docencia/ar/redes.pdf.
- https://gsitic.wordpress.com/2018/03/26/biv12-redes-conmutadas-y-de-difusion-
conmutacion-de-circuitos-y-de-paquetes-integracion-voz-datos-protocolos-de-\nencaminamiento-ethernet-conmutada-mpls-calidad-de-servicios-qos/. 
- https://mastermoviles.gitbook.io/tecnologias2/.
- https://hipertextual.com/2017/12/5g-espana.
- http://www.abartiateam.com/conectividad-movil.
- https://www.inc.cl/blog/internet/evolucion-conectividad-movil.

---

Comunicaciones: Modos, Medios y Equipos. Redes de conmutación y de difusión. Comunicaciones móviles \ne inalámbricas 
- https://www.abc.es/economia/abci-espana-conecta-redes-201807280222_noticia.html.
- https://www.movilonia.com/noticias/calendario-5g-espana/.
- http://agamenon.tsc.uah.es/Asignaturas/ittst/rc1/download/Tema4ApuntesAlumnado.pdf.
- https://es.wikipedia.org/wiki/Itinerancia.
- https://es.wikipedia.org/wiki/Bluetooth#:~:text=LMP,Est%C3%A1%20implementado%20en%
20el%20controlador. 
- https://es.wikipedia.org/wiki/IEEE_802.15.
- https://www.etsi.org/.
- https://es.wikipedia.org/wiki/Terrestrial_Trunked_Radio.

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema06|Ficha Resumen del Tema 06]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque4-tema06|Nota Fuente Oficial del Tema 06]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema06-medios-transmision-fibra|Test Tema 06]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema05|⬅️ Tema Completo 05]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema07|Tema Completo 07 ➡️]]
