---
title: "Resumen Completo y Profundo Tema 04 (Bloque 2): Sistemas Operativos: Gestión de Procesos, Memoria y Ficheros"
type: "synthesis"
tags:
  - resumen
  - resumen-profundo
  - temario-completo
  - bloque-2
  - tema-04
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md]]"
  - "[[wiki/sources/bloque2-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema05|Tema 05 ➡️]]

# 🔴 Resumen Completo y Profundo Tema 04 (Bloque 2): Sistemas Operativos: Gestión de Procesos, Memoria y Ficheros

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 04**
> Guía completa y exhaustiva que recopila todo el temario oficial, marco legal/normativo, detalles de arquitectura, tablas de datos críticos, protocolos, comandos de consola y casos prácticos.

---

## 🟣 1. Desarrollo Temático Completo e Íntegro

# Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Arquitectura, Gestión de Procesos, Memoria y Sistemas de Archivos

<!-- Page 1 -->

 
 
Sistemas Operativos. 
Características y elementos 
constitutivos. Sistemas 
Windows, Linux, y para 
dispositivos móviles 

<!-- Page 2 -->

1. Software 
6 
2. Sistema Operativo 
7 
2.1. Funciones del S.O. 
8 
2.2. Gestor de recursos 
8 
2.3. Kernel 
10 
2.4. Gestión de procesos 
10 
2.5. Gestión de memoria 
11 
2.6. Sistema de archivos 
11 
2.7. Llamadas al sistema 
12 
2.8. Protección y seguridad de la información 
13 
2.9. Scheduler 
13 
3. Estructura de los Sistemas Operativos 
14 
3.1. Clasificación de los Sistemas Operativos 
15 
3.1.1. Por servicios ofrecidos 
15 
3.1.2. Por la forma de ofrecer servicio 
16 
3.1.3. Según el soporte de arquitecturas 
18 
3.2. Gestión avanzada de memoria 
19 
4. Sistemas windows 
23 
4.1. Versiones 
24 
4.2. Elementos básicos del interfaz de Windows 
46 
4.3. Opciones de energia 
49 
4.3.1. Opciones de energía en Windows 10/11 Home 
49 
4.3.2. Opciones de energía en Windows 10/11 Pro 
50 
4.3.3. Opciones de energía en Windows Server 
50 
4.4. Variables de entorno 
50 
4.4.1. Variables de entorno en Windows 10/11 Home 
51 
4.4.2. Variables de entorno en Windows 10/11 Pro 
51 
4.4.3. Variables de entornos en Windows Server 
51 

<!-- Page 3 -->

 
 
4.5. Registros de Windows 
52 
4.5.1. Registros en Windows 10/11 Home 
52 
4.5.2. Registros en Windows 10/11 Pro 
52 
4.5.3. Registros en Windows Server 
52 
4.6. Microsoft Azure 
53 
4.7. Herramientas de Windows 
54 
4.7.1. ActiveSync 
54 
4.7.2. AppLocker 
54 
4.7.3. Interfaz de Consola CLI 
55 
4.7.4. Windows Script Host 
56 
4.7.5. PowerShell 
56 
5. Sistemas Unix y Linux 
57 
5.1. Características 
59 
5.2. Conceptos básicos 
61 
5.3. Gestor de arranque (Linux Boot Loaders) 
62 
5.4. Distribuciones 
64 
5.5. Entornos de escritorio 
70 
5.6. Directorios y sistemas de archivos 
71 
5.7. Permisos 
72 
5.8. Principales comandos 
75 
5.8.1. Gestión y control de Linux 
75 
5.8.1.1. Which 
75 
5.8.1.2. Modprobe 
75 
5.8.1.3. Paquete e2fsprogs 
76 
5.8.1.4. Who 
76 
5.8.1.5. Id 
77 
5.8.1.6. Uname 
78 

<!-- Page 4 -->

 
 
5.8.2. Comandos para ficheros y directorios 
78 
5.8.2.1. pwd 
79 
5.8.2.2. touch 
79 
5.8.2.3. WC 
79 
5.8.2.4. cat 
80 
5.8.2.5. less 
80 
5.8.2.6. more 
81 
5.8.2.7. tac 
82 
5.8.2.8. du 
82 
5.8.2.9. vi 
83 
5.8.2.10. mount, umount 
85 
5.8.2.11. tar 
86 
5.8.2.12. shell 
91 
5.8.2.13. Sort 
93 
5.8.2.14. fsck 
94 
5.8.3. Comandos de Procesos 
95 
5.8.3.1. fork 
95 
5.8.3.2. ps 
95 
5.8.3.3. renice y nice 
96 
5.8.3.4. top 
98 
5.8.3.5. kill 
98 
5.8.3.6. killall 
98 
5.8.4. Comandos de visualización y localización de archivos 
98 
5.8.5. Otros comandos: Información, redes, usuarios 
100 
5.8.6. Metacaracteres 
104 
5.9. Señales 
107 
5.10. Runlevels estándar en Linux 
110 
5.11. S.O. FreeBSD 
110 
6. macOS 
111 

<!-- Page 5 -->

 
 
7. Sistemas operativos para dispositivos móviles 
113 
7.1. Android 
115 
7.2. IOS 
119 
7.3. Notificaciones Push 
120 
8. Bibliografía 
121 

<!-- Page 6 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
6 
1. Software 
 
Fuente: Flickry 
Ya sabes que el software es la parte lógica, intangible de un sistema informático. 
Si los programas tuvieran que comunicarse directamente con el hardware, sería muy complicado, 
porque cada máquina (procesador, memoria, discos, impresoras) tiene sus particularidades técnicas. 
Por lo tanto, era necesario dividir esta gestión de hardware en dos tipos: 
• Sistemas Operativos: software de sistema: Se encargan de controlar los elementos de 
hardware, para proporcionar un entorno de trabajo al usuario. 
• Programas o Aplicaciones: Resuelven los problemas específicos del usuario. 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 

<!-- Page 7 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
7 
2. Sistema Operativo 
 
Fuente: Wilkipedia 
El Sistema Operativo, es un software, que se encarga de arrancar el equipo y gestionar los recursos del 
mismo, controlando los elementos de hardware (mediante los drivers), para proporcionar un entorno 
de trabajo al usuario. 
Actúa como intermediario entre el hardware y el usuario. 
El sistema operativo (S.O.) es el software más importante del ordenador. Todos los ordenadores 
necesitan tener instalado al menos uno. De lo contrario, el ordenador al encenderlo, sólo nos mostrara 
sus características de hardware (placa base, memoria…). No nos permitirá realizar ninguna función. 
El sistema operativo es una capa que está por encima del hardware y cuya función es ocultar las 
particularidades de éste a los usuarios y a los programas. Actúa como interfaz entre el usuario y el 
hardware del ordenador. 
El sistema operativo muestra al usuario una abstracción del hardware. 
Para definir lo que es un sistema operativo, vamos a exponer sus funciones y objetivos. 
Tiene dos objetivos fundamentales: 
• Servir de interfaz entre el usuario y el ordenador, para lograr que el sistema se use de manera 
cómoda para el usuario. 
• Ejercer como gestor de recursos, para que el hardware del ordenador se emplee de la manera 
más eficiente. 
 
 
 
 
Básico 
Existen unos programas de utilidades que se incluyen con el sistema 
operativo. Se suelen ver como parte del sistema operativo, pero en 
realidad se utilizan para realizar funciones distintas a las del sistema 
operativo. (Calculadora, editor de texto, recortes, etc.). 
 

<!-- Page 8 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
8 
2.1. Funciones del S.O. 
El sistema operativo debe proporcionar servicios para las siguientes funciones: 
• Utilización y creación de programas. Para ello utiliza programas que no forman parte del 
sistema operativo, pero a los cuales podemos acceder a través de él (editores de texto, 
plataformas de programación, compiladores, etc.). 
• Ejecución de programas. Realiza las operaciones que permiten la ejecución de programas como 
son: 
• Cargar código y datos en la memoria principal. 
• Inicializar los dispositivos de E/S. 
• Preparar los recursos que se utilizarán en la ejecución del programa. 
• Operaciones de entrada/salida. El sistema operativo se encarga de realizar las operaciones que 
permiten la lectura, escritura y comunicación con periféricos por parte de un programa a través 
de los controladores (drivers). De esta forma aísla al programa de las particularidades del 
dispositivo. 
• Manipulación y control del sistema de archivos. Debe conocer el formato de almacenamiento y 
proporcionar los mecanismos para su control y seguridad. 
• Detección de errores. Debe ser capaz de detectar errores, corrigiéndolos cuando sea posible o 
minimizando el impacto cuando no pueda corregirse. 
• Control de acceso al sistema. Debe proporcionar servicios de seguridad para que solo tenga 
acceso al sistema y a los distintos recursos los usuarios autorizados. 
• Informes. Debe poder facilitar informes de utilización de recursos, rendimiento, etc. 
2.2. Gestor de recursos 
El kernel, núcleo del sistema operativo, debe gestionar los recursos que hay en el sistema 
(procesadores, memoria, periféricos, etc.) y planificar la utilización de los recursos de manera justa y 
eficiente. 
Su función es proporcionar una asignación ordenada y controlada a los programas que compiten por los 
distintos recursos (procesadores, memoria, periféricos, etc.). 
Todos los procesos que compiten por un determinado recurso deben disponer de él de una forma 
equitativa. 
Por otro lado, se debe tener en cuenta la prioridad de cada trabajo y planificar la asignación de recursos 
en base a los requerimientos de cada proceso. 

<!-- Page 9 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
9 
Funciona de la misma manera que otro programa (se ejecuta en el procesador y utiliza la memoria). 
El sistema operativo, es uno más, de los programas de ordenador. El procesador no lo distingue del 
resto. El sistema operativo planifica los programas que se ejecutarán en la CPU y el acceso a los 
recursos, pero para ello debe ceder el control del procesador a otra tarea y posteriormente volver a 
recuperarlo. 
 
 
 
 
Atención 
Un Sistema Operativo NO es una máquina virtual. 
Una máquina virtual es un software que se instala sobre un sistema 
operativo, y que es capaz de cargar en su interior otro sistema 
operativo haciéndole creer que es un PC de verdad. Crea una 
máquina (PC, consola, móvil o lo que sea) que en vez de ser física 
es virtual o emulada. 
Su uso ofrece muchas ventajas para realizar pruebas etc., sin dañar 
el S.O. real instalado en el ordenador. 
 
Driver 
Es un término inglés, device driver, o simplemente driver. 
En español, también podemos llamarlo controlador, o manejador de dispositivo. 
Un driver, es un software propio de un concreto elemento de hardware, que permite que el sistema 
operativo, sepa cómo utilizarlo con todas las funcionalidades que ese elemento de hardware ofrezca. 
El driver permite una abstracción del hardware y proporciona la interfaz-software para que el sistema 
operativo los pueda utilizar correctamente ofreciendo todas sus funcionalidades al usuario. 
Los sistemas operativos incluyen unos determinados drivers de fabricantes y modelos de elementos de 
hardware, por ello, a veces, reconocen directamente dichos elementos de hardware sin necesidad de 
instalar el driver. Pero, aun así, seguramente si lo instalamos tendremos opciones nuevas sobre ese 
hardware, que en ocasiones no son realmente necesarias para un usuario. 
Ejemplo: 
Si tenemos una determinada tarjeta de vídeo, el sistema operativo la reconocerá como estándar o como 
un modelo estándar del fabricante, ofreciendo una determinada resolución de aspecto y color, de lo 
contrario no podríamos ver nada en el monitor. 

<!-- Page 10 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
10 
Pero si instalamos el driver correspondiente, podremos tener todas las ventajas y funcionalidades de esa 
tarjeta de vídeo, mayores resoluciones, color, rapidez de imágenes en movimiento, incluso algunas 
opciones como son la rotación de la imagen en pantalla). 
Es muy común que no funcione algún video juego si no tememos instalado el driver de la tarjeta gráfica. 
De hecho, debemos fijarnos en los requisitos mínimos de los videojuegos para saber si funcionaran en 
nuestro ordenador con nuestra tarjeta gráfica. 
También existen dispositivos de hardware (tarjetas de sonido, impresoras, webcam, escáner…), los 
cuales, si no se instala el driver, no funcionan, el sistema operativo no es capaz de reconocerlos y 
ofrecer sus funciones al usuario. 
Los drivers de cada dispositivo de hardware pueden ser diferentes dependiendo de la versión de sistema 
operativo que utilicemos. Normalmente están disponible en la página web del fabricante para su 
descarga e instalación. 
2.3. Kernel 
El Kernel es el núcleo del sistema operativo. Se carga en memoria al arrancar el ordenador y permanece 
aquí hasta que se apaga. 
Realiza, entre otras, las siguientes funciones básicas: 
• Manejo de la memoria. 
• Determinar qué proceso tiene el control de la CPU. 
• Comunicación entre procesos. 
• Manejo de errores. 
• Control de periféricos. 
• Control de interrupciones. 
2.4. Gestión de procesos 
Un proceso es, básicamente, un programa en ejecución. Está formado por el programa ejecutable, los 
datos que utilizará y el contexto en que se ejecuta. 
Podemos verlo como una entidad que puede ser asignada a un procesador y ejecutada por el mismo. 
El kernel gestiona el tiempo del procesador mediante la planificación de procesos. Para ello puede 
suspender (interrumpir) la ejecución de un proceso y dar paso a otro, siguiendo el orden y la política de 
planificación que tenga definida (por ejemplo, por prioridad, turno o tiempo de uso). De esta forma, a 
cada proceso se le va asignando tiempo de CPU. 

<!-- Page 11 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
11 
La información sobre cada proceso se almacena en una estructura llamada Bloque de Control de 
Proceso (PCB), que mantiene el sistema operativo. El conjunto de estos PCBs forma la tabla de 
procesos. Cada PCB contiene, entre otros datos, información de planificación, estado, identificadores, y 
punteros a las estructuras de memoria y recursos que el proceso utiliza. 
2.5. Gestión de memoria 
El kernel reserva y libera memoria continuamente, para poder ejecutar los procesos y gestionar 
convenientemente el intercambio de información entre la memoria principal y la secundaría 
dependiendo de los recursos necesarios del proceso. 
El sistema operativo debe responsabilizarse de: 
• Aislar los procesos. Un proceso no debe interferir en la ejecución o los datos de otro proceso. 
• Asignación de memoria automática. El sistema operativo deberá ubicar los procesos de forma 
transparente para el programador. 
• Seguridad de la memoria. Debe controlar el acceso para que, en una memoria compartida, un 
programa no pueda acceder al espacio de direcciones de otro. 
• Memoria virtual. Los programas pueden direccionar la memoria sin preocuparse de si es 
memoria principal o virtual. Para el programa aparece todo como una sola memoria. 
 
 
 
 
+ Info 
Con la memoria virtual, que es es una técnica que permite que un 
proceso vea un espacio de direcciones contiguo, los programas 
creen que tienen más memoria principal de la que realmente 
existe, porque el sistema operativo usa memoria secundaria como 
apoyo y gestiona de forma transparente la asignación y el 
movimiento de datos 
 
2.6. Sistema de archivos 
Define el sistema de archivos que va a ser utilizado para el almacenamiento de larga duración. 
La información se almacenará en archivos y estarán ubicados dentro de directorios que a su vez pueden 
estar dentro de otros directorios. Tiene una estructura de árbol. 

<!-- Page 12 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
12 
2.7. Llamadas al sistema 
Las llamadas al sistema (system calls) son la interfaz entre los programas en modo usuario y el kernel. A 
través de ellas, las aplicaciones pueden solicitar de forma controlada servicios del núcleo como gestión 
de procesos, memoria, archivos o dispositivos. 
Las llamadas a sistema tienen un nombre y pueden tener parámetros. 
Se pueden agrupar en cinco categorías: 
1. Control de procesos. 
2. Manipulación de archivos. 
3. Manipulación de periféricos. 
4. Mantenimiento de la información. 
5. Comunicaciones. 
 
 
 
 
Ejemplo 
Analicemos la siguiente llamada: 
Contador = read(nombreArchivo,buffer,numeroBytes) 
• read: es el nombre de la llamada, indica que se va a leer un 
archivo. 
• nombreArchivo: es el nombre del archivo del cual vamos a 
leer. 
• buffer: es el almacenamiento temporal donde se colocarán 
los datos leídos. 
• numeroBytes: es el número de bytes que vamos a leer. 
• contador recibirá el número de bytes leídos. 
Si este no coincide con numeroBytes significa que se ha producido 
un error. 
 

<!-- Page 13 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
13 
2.8. Protección y seguridad de la información 
Se deben aplicar políticas de seguridad e implementar mecanismos de protección para evitar que 
personas o aplicaciones realicen ataques al sistema informático. 
2.9. Scheduler 
 
Agenda, Planificador. Fuente: Needpix.com 
Scheduler, (planificador) es un componente funcional muy importante de los S.O. multitarea y 
multiproceso, y es esencial en los S.O. de tiempo real. 
Su función consiste en repartir el tiempo disponible de un microprocesador entre todos los procesos 
que están disponibles para su ejecución. 
Un sistema operativo en tiempo real se caracteriza por garantizar que todo programa se ejecutará en 
un límite máximo de tiempo. El planificador debe comportarse de manera que esto sea cierto para 
cualquier proceso. 
En estos casos, la finalidad del Scheduler es balancear o equilibrar la carga del procesador, impidiendo 
que un proceso monopolice el procesador o que sea privado de los recursos de la máquina. En entornos 
de tiempo real, como los dispositivos para el control automático en la industria (por ejemplo, robots), el 
Scheduler también impide que los procesos se paren o interrumpan a otros que esperan que se realicen 
ciertas acciones. Su labor resulta imprescindible para mantener el sistema estable y funcionando. 
Los niveles de planificación están basados en la frecuencia con la que se realiza cada uno. 
En los sistemas operativos de propósito general, existen tres tipos de planificadores. 
• Short term scheduler: a corto plazo, (también se denomina dispatcher) es el, más importante. 
Decide qué proceso entra al procesador para su ejecución. 
• Mid term scheduler: a mediano plazo, relacionado con aquellos procesos que no se encuentran 
en memoria principal. Su misión es mover procesos entre memoria principal y disco (swapping). 
• Long term scheduler: a largo plazo, es el encargado de ingresar nuevos procesos al sistema y de 
finalizarlos. 

<!-- Page 14 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
14 
3. Estructura de los Sistemas Operativos 
Al principio, los sistemas operativos eran muy básicos, pero con el tiempo han ido creciendo en tamaño 
y complejidad. 
Su construcción debe realizarse con mucho cuidado para que todo funcione correctamente y para 
facilitar su modificación o actualización. 
Para construir un sistema tan grande se divide en componentes más pequeños. 
Aunque no todos los sistemas operativos tienen la misma estructura, es bastante habitual dividirlo en 
los siguientes componentes básicos: 
• Gestor de procesos. 
• Gestor de la memoria principal. 
• Gestor del almacenamiento secundario y del sistema de archivos. 
• Gestor del sistema de E/S. 
• Sistema de protección. 
• Sistema de comunicación. 
• Intérprete de comandos. 
Algunos de estos componentes se incluyen como programas de utilidades más que como un 
componente propio del sistema operativo. 
 
 
 
 
Ejemplo 
• El intérprete de comandos de Linux (Shell) es un programa 
de utilidad que puede cambiarse por otro en la instalación. 
• Windows incorpora MS-DOS, con sus propios comandos. 
 
 
En un principio los sistemas operativos tenían una estructura monolítica (no tenían una estructura bien 
definida) como el MS-DOS. 

<!-- Page 15 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
15 
Tenían una estructura modular, de manera que el sistema operativo se construía compilando por 
separado distintos procedimientos para luego enlazarlos. 
Para los grandes sistemas operativos esto no era suficiente y tuvieron que entrar en juego conceptos 
como los niveles jerárquicos y la abstracción de la información. 
3.1. Clasificación de los Sistemas Operativos 
Según la perspectiva con la que se observen los sistemas operativos, pueden realizarse múltiples 
clasificaciones. Vamos a ver dos de ellas. 
• Por servicios ofrecidos. 
• Por la forma de ofrecer el Servicio. 
• Según el soporte de arquitecturas multiprocesador. 
3.1.1. Por servicios ofrecidos 
En esta clasificación se tiene en cuenta la visión del usuario final: 
• Por el número de usuarios. 
• Monousuario o Monopuesto: el sistema operativo soporta un único usuario a la vez, 
indistintamente de las características de la máquina sobre la que está montado. 
• Multiusuario o Multipuesto: pueden dar servicio a más de un usuario a la vez, 
independientemente de la máquina. 
• Por el número de tareas. 
• Monotarea: sólo permiten una tarea a la vez por usuario. Puede haber un sistema 
multiusuario y monotarea, se admiten varios usuarios que sólo pueden realizar una tarea a 
la vez. 
• Multitarea: permiten al usuario realizar varias tareas al mismo tiempo. Suelen tener 
interfaces gráficas que permiten un rápido intercambio entre las tareas para el usuario, 
mejorando su productividad. 
• Por el número de procesos. 
• Monoproceso: únicamente permiten realizar un proceso a la vez. 
• Multiproceso: los sistemas de multiprocesamiento tienen más de un procesador y pueden 
ejecutar múltiples procesos simultáneamente. Existen dos tipos de multiprocesamiento: 
» Simétricos: distribuyen la carga de procesamiento por igual entre todos los 
procesadores existentes. 

<!-- Page 16 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
16 
» Asimétricos: la gestión se realiza en base a la prioridad de los procesos. Todos los 
procesos de baja prioridad son asignados a un procesador y el resto de los procesos se 
reparten entre el resto de los procesadores. 
 
 
 
 
+ Info 
Los sistemas monoproceso pueden simular la multitarea haciendo 
que el sistema asigne pequeñas porciones de tiempo a varias tareas 
de forma rotatoria, de forma que el usuario lo perciba como si se 
ejecutaran al mismo tiempo (pero aumentando el tiempo que 
tarda en ejecutarse). 
Por ejemplo, si tenemos dos procesos (proc1 y proc2) ejecutaría 
una parte de proc1, luego una parte de proc2, luego otra de proc1, 
otra de proc2… 
 
3.1.2. Por la forma de ofrecer servicio 
En esta clasificación, también tenemos en cuenta la visión externa del usuario, cómo el usuario accede a 
los servicios. 
Se clasifican en tres tipos: 
• Sistemas centralizados. 
• Sistemas distribuidos. 
• Sistemas en red. 
Sistemas centralizados 
En un principio aún no habían aparecido los ordenadores personales o estos eran muy caros y tenían 
bajas prestaciones. 
Por este motivo, la mayoría de los sistemas de empresas, administraciones públicas, universidades, etc. 
utilizaban el modelo centralizado. 
Existía un ordenador principal (mainframe) de altas prestaciones que se encargaban de todo el 
procesamiento (incluso muchas veces también del almacenamiento) y los usuarios manejaban 
terminales que no disponían de memoria ni procesador (se les denominaba terminales tontas). 
Actualmente casi no se utilizan. 

<!-- Page 17 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
17 
 
 
 
Ejemplo 
Aún podemos encontrar sistemas centralizados como los Terminal 
Services de Microsoft. 
Sin embargo, ya no utilizan terminales tontos, sino ordenadores 
personales con capacidad de cómputo, los cuales pueden realizar 
muchas tareas por sí mismos. 
 
Sistemas distribuidos 
Los sistemas distribuidos son un paradigma clave en la computación moderna, donde múltiples nodos 
(computadoras, servidores o dispositivos) trabajan de manera coordinada para lograr un objetivo 
común, pero aparecen ante el usuario como un único sistema unificado. Vemos a continuación sus 
principales características: 
• Transparencia: el usuario percibe el sistema como una única entidad. 
• Concurrencia: varios nodos pueden ejecutar tareas en paralelo, compartiendo recursos 
(almacenamiento y capacidad de procesamiento). 
• Alta disponibilidad: si un nodo falla otros pueden asumir su función, permitiendo que el sistema 
siga trabajando. 
• Escalabilidad: se pueden agregar nodos sin comprometer el comportamiento global 
• Comunicación mediante mensajes: los nodos se comunican entre sí mediante mensajes, 
utilizando protocolos de red como HTTP/HTTPS, gRPC, MPI, entre otros. 
Sistemas en red 
Cada equipo mantiene su independencia (sistema operativo, almacenamiento, aplicaciones), pero están 
conectados para compartir recursos. La red permite la colaboración, pero el usuario puede distinguir los 
distintos sistemas. 
 

<!-- Page 18 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
18 
 
 
 
Ejemplo 
Los más utilizados son: 
• Linux y UNIX. 
• Windows Server. 
• Novell Netware. 
Otros sistemas son: 
• Personal Netware. 
• LAN Manager. 
• LANtastic. 
 
3.1.3. Según el soporte de arquitecturas 
Los sistemas operativos pueden estar diseñados para gestionar hardware con múltiples procesadores, y 
su diseño varía según el tipo de acoplamiento entre estos. A continuación, se detallan las dos categorías 
principales: 
Sistemas para Arquitecturas Fuertemente Acopladas 
• Memoria compartida: Todos los procesadores acceden a la misma memoria principal. 
• Reloj global: Sincronización temporal común para coordinación. 
• Baja latencia: Comunicación directa entre CPUs (sin pasar por red). 
• Tiempos de acceso uniformes o predecibles (en SMP, no necesariamente en NUMA). 
En SNP (Symmetric Multi-Processing) todos los procesadores son iguales y acceden a memoria 
uniformemente. 
EN NUMA, la memoria está distribuida físicamente, pero lógicamente compartida. 
Los sistemas operativos compatibles son (Linux con soporte para SNP o NUMA), Windows Server y 
Solaris. 

<!-- Page 19 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
19 
Sistemas para Arquitecturas Débilmente Acopladas 
• Memoria distribuida: cada nodo tiene su memoria local. 
• Comunicación por red: Ethernet, InfiniBand. 
• No existe reloj global: cada nodo opera de manera independiente. 
• Alta Escalabilidad: no hay restricciones de hardware compartido. 
Encontramos estos sistemas en: 
• Clústeres: nodos independientes conectados por red. 
• Grid Computing: recursos distribuidos geográficamente. 
• Cloud Computing: plataformas como AWS, Azure, Google Cloud... 
Sistemas operativos compatibles: Linux (para clústeres, kubernetes), Sistema especializados en 
balanceo de carga (p.e Mosix). 
3.2. Gestión avanzada de memoria 
Ya hemos nombrado esta función del S.O. en conceptos básicos, pero ahora que hemos visto la 
clasificación de los S.O. (multiusuario, multiproceso…) vamos a profundizar más. 
Recordamos que los procesos se cargan en la memoria RAM para su ejecución. 
En los sistemas monotarea, la gestión de memoria es simple, puesto que el proceso en ejecución 
dispone de toda la memoria para su uso. 
En cambio, en procesos multiusuario y multitarea, la gestión de memoria es fundamental, tiene que 
realizar el reparto de memoria para los procesos de la forma más eficiente. 
Vamos a ver los conceptos clave en la gestión de memoria en ordenadores modernos: 
Memoria Virtual 
La memoria virtual es el espacio de direcciones reservado por el sistema operativo para un proceso. Este 
espacio está definido por el memory map, que se compone de múltiples áreas de memoria virtual 
(VMAs, Virtual Memory Areas). Cada VMA representa una región lógica del programa (por ejemplo, 
.text, heap, stack o archivos mapeados), con atributos específicos como dirección de inicio y fin, y 
permisos de acceso (lectura, escritura, ejecución). 

<!-- Page 20 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
20 
Paginación 
La paginación es el subsistema que, apoyándose en las Virtual Memory Areas (VMAs) del kernel, 
materializa el espacio de direcciones virtuales de un proceso mediante entradas en la tabla de páginas. 
Los VMAs definen el qué (las regiones lógicas, sus límites y permisos), mientras que la tabla de páginas 
implementa el cómo (el mapeo de direcciones virtuales a memoria física o swap). 
Tabla de Páginas 
La tabla de páginas es una estructura del sistema operativo que mapea direcciones virtuales a 
direcciones físicas (o a swap/archivos mapeados). 
Se crea al iniciar el proceso, pero la mayoría de sus entradas se completan dinámicamente conforme se 
accede a las páginas y se producen fallos de página (page faults). 
Cada entrada contiene: 
• Dirección del marco físico (si está en RAM), índice en swap (si fue expulsada) u offset en 
archivo (para código/datos mapeados). 
• Bits de control: presencia, permisos (R/W/X), dirty, acceso, etc. 
Su construcción está guiada por los VMAs del proceso, que definen qué regiones deben existir y con qué 
características, pero los marcos físicos/swap solo se asignan al acceder a la página (via page fault). 
Bit de Presencia 
El bit de presencia (Present bit) es el indicador más crítico de cada entrada en la tabla de páginas. Su 
función principal es señalar si la página referida por una dirección virtual está actualmente cargada en 
memoria física (RAM) o no. 
Cuando este bit está a 1, la entrada contiene una dirección de marco válida y la MMU puede completar 
la traducción de direcciones sin intervención del sistema operativo. Si está a 0, se genera un page fault 
que fuerza al kernel a: 
• Cargar la página desde swap o el archivo ejecutable (si el acceso es válido según los VMAs). 
• O terminar el proceso por violación de acceso. 
Este bit es es esencial para la gestión eficiente de la paginación bajo demanda y del swapping. Permite al 
sistema operativo identificar si una página está actualmente cargada en memoria física o si debe traerse 
desde disco. De este modo, hace posible cargar solo las páginas necesarias cuando se acceden, 
reduciendo el uso de memoria. Además, funciona como primera barrera de protección, colaborando 
con los VMAs para detectar accesos no válidos y generar excepciones (como page faults o violaciones 
de segmento). 

<!-- Page 21 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
21 
Swapping 
El swapping (del inglés swap -intercambiar) es un mecanismo del sistema operativo que gestiona el 
movimiento de páginas de memoria entre RAM y disco. Cuando el sistema necesita liberar memoria 
física, el kernel selecciona páginas poco usadas y las escribe al área de swap en disco (swap-out). 
Posteriormente, si un proceso intenta acceder a una de estas páginas, se genera un page fault y el 
kernel la recupera desde el swap a RAM (swap-in). 
Su entrada en la tabla de páginas guarda un índice al swap que permite localizarla cuando se necesite. 
Este mecanismo actúa principalmente sobre páginas anónimas (como las del heap y stack) o páginas de 
archivos mapeados que han sido modificadas. Los VMAs definen qué regiones pueden ser swappeadas, 
pero la decisión final de qué páginas mover la toma el kernel dinámicamente, mediante algoritmos 
como LRU. El swapping se activa automáticamente cuando hay presión en la memoria física. 
Trashing 
En casos extremos, si el sistema pasa más tiempo intercambiando páginas que ejecutando instrucciones 
útiles, se produce un fenómeno llamado thrashing. Ocurre cuando los procesos activos necesitan más 
memoria de la disponible y el sistema entra en un bucle de swap constante, afectando gravemente al 
rendimiento global. Es un signo de saturación de la memoria. 
MMU (Memory Management Unit) 
La Unidad de Gestión de Memoria (MMU, por sus siglas en inglés) es el componente de hardware 
encargado de traducir, en tiempo real, las direcciones virtuales generadas por la CPU en direcciones 
físicas de RAM. Esta traducción se realiza mediante la tabla de páginas, una estructura mantenida por el 
sistema operativo pero consultada continuamente por la MMU durante la ejecución de un proceso. 
La MMU no interpreta el contenido de dicha tabla, simplemente la recorre siguiendo reglas predefinidas 
por la arquitectura del sistema (como x86 o ARM). Si encuentra una entrada inválida (por ejemplo, con 
el bit de presencia desactivado), genera una excepción de hardware (page fault) que transfiere el 
control al kernel. A partir de ahí, será el sistema operativo quien consulte el mapa de memoria (VMAs) 
o el área de swap para decidir cómo resolver la falta. 
En este sentido, la MMU y la paginación forman una unidad tecnológica inseparable: la paginación 
define la lógica con la que se organiza el espacio de memoria virtual en páginas y se gestiona su 
correspondencia con memoria física o swap; la MMU la ejecuta físicamente. Juntas, hacen posible una 
gestión de memoria segura, flexible y eficiente, habilitando características clave como la carga bajo 
demanda, la protección de regiones o el intercambio de páginas con disco. 
CR3 (Control Register 3) 
Registro interno de la MMU (en arquitecturas como x86) que almacena la dirección física de la tabla de 
páginas raíz del proceso activo. Cada vez que la MMU necesita traducir una dirección virtual, comienza 
consultando CR3 para localizar el punto de entrada de la tabla. El sistema operativo actualiza este 
registro en cada cambio de contexto, asegurando que la MMU traduzca direcciones según la memoria 
virtual del proceso en ejecución. 

<!-- Page 22 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
22 
Page Fault: 
El page fault es una excepción generada por la MMU cuando un proceso accede a una dirección virtual 
cuya página no está presente en RAM o se accede con permisos no válidos. Al producirse, la ejecución 
se interrumpe y el control pasa al kernel. 
El sistema operativo consulta los VMAs para comprobar si la dirección pertenece a una región válida y 
decide si debe cargar la página desde el archivo ejecutable o recuperarla del área de swap. Si no es 
válida o el acceso es incorrecto, se termina el proceso con una señal de error. 
No indica necesariamente un fallo del programa. Es un mecanismo normal del sistema de memoria 
virtual que permite la carga bajo demanda y el uso eficiente de la RAM. 
Fragmentación externa e interna 
Antes de la paginación, la memoria se asignaba de forma contigua, lo que generaba fragmentación 
externa: con el tiempo, al cargarse y descargarse procesos, quedaban huecos dispersos entre bloques 
ocupados que no podían aprovecharse si no eran lo bastante grandes y continuos. Así, aunque hubiese 
memoria libre suficiente en total, no se podía utilizar eficientemente. La paginación resolvió este 
problema dividiendo la memoria lógica de los procesos y la memoria física en bloques del mismo 
tamaño llamados páginas y marcos, permitiendo asignar marcos no contiguos a cada proceso. De este 
modo, cualquier marco libre puede utilizarse, eliminando completamente la fragmentación externa y 
simplificando la gestión de memoria. 
Sin embargo, la paginación introduce un nuevo problema: la fragmentación interna. Esta aparece 
cuando un proceso no llena completamente el último marco asignado; por ejemplo, si un proceso 
necesita 10,5 KB y las páginas son de 4 KB, se le asignan 3 páginas (12 KB en total), pero la última solo 
usará 0,5 KB, quedando 3,5 KB inutilizados dentro del marco. Este desperdicio interno no puede ser 
aprovechado por otros procesos mientras el actual esté activo. Aun así, la fragmentación interna es 
predecible y limitada (como máximo el tamaño de una página por proceso), por lo que el uso de la 
paginación mejora significativamente el aprovechamiento global de la memoria frente al sistema 
contiguo tradicional. 
Mapa de memoria y segmentación 
Cuando un programa se ejecuta, el sistema operativo construye lo que llamamos su mapa de memoria 
(memory map), que representa cómo está distribuido su espacio de direcciones. Este mapa se basa 
directamente en los segmentos definidos durante la compilación y el enlazado, pero en tiempo de 
ejecución estos segmentos se traducen en áreas de memoria virtual (VMAs), que el sistema operativo 
utiliza para representar regiones válidas con atributos como permisos, tamaño y tipo de acceso. Así, la 
segmentación define las regiones lógicas del programa, y el mapa de memoria las ubica en direcciones 
concretas, con sus respectivos permisos. 
Por ejemplo, un mapa típico en un proceso podría tener: 
• Un segmento de código (text): solo lectura y ejecución. 
• Un segmento de datos inicializados (data): lectura y escritura. 

<!-- Page 23 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
23 
• Un segmento BSS (datos no inicializados): también lectura y escritura. 
• Un segmento de pila (stack): crece hacia abajo. 
• Un segmento heap: se gestiona en tiempo de ejecución para malloc/new. 
Cada uno de estos segmentos es una región del mapa de memoria. La segmentación no es la única 
responsable de cómo se organiza todo el mapa (el sistema operativo y el enlazador también influyen), 
pero sí es la estructura lógica base sobre la que se construye. 
En sistemas modernos, aunque se usa paginación para la asignación física de memoria, el modelo de 
segmentación sigue vivo a nivel lógico y se refleja en el diseño del espacio de direcciones. 
4. Sistemas windows 
 
Fuente: windows-icon-28161_960_720 de 
Pixabay 
Historia de Microsoft Windows 
Microsoft Windows es el nombre de una familia de distribuciones de software para PC, Smartphone, 
servidores y sistemas empotrados desarrollados y comercializados por Microsoft. 
La palabra Windows, en español se traduce como ventana. Se llama así porque utiliza un interfaz basado 
en ventanas. Las "ventanas" es la forma en que el sistema presenta al usuario los recursos de su 
ordenador, facilitando su uso. 
Microsoft Windows es el sistema operativo más usado del mundo en ordenadores personales, con gran 
diferencia (alrededor del 90% de cuota de mercado). 
Sin embargo, en dispositivos móviles (Windows Mobile), ha dejado de utilizarse. 

<!-- Page 24 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
24 
Windows 1.0 se presentó en 1983 (y comercializó en 1985) como una extensión del sistema operativo 
MS-DOS y se beneficiaba de las utilidades de este y la facilidad de manejo a través de ventanas. 
Microsoft Windows ha ido presentado nuevas versiones para adaptarse a las nuevas necesidades de los 
usuarios. Las versiones Windows más conocidas son: Windows NT, 95, 98, 2000, XP, Vista, 7, 8 y 10. 
El éxito de Windows se debe principalmente a los siguientes puntos: 
• Facilidad de uso a través de las ventanas. 
• Facilidad de conexión con el hardware. 
• Buena campaña de marketing. 
• Acuerdos con fabricantes como IBM. 
Sin embargo, los sistemas Windows han recibido numerosas críticas por sus fallos y problemas de 
seguridad. 
Microsoft ha seguido dos rutas paralelas en sus Sistemas operativos: 
• Usuarios domésticos. Mayor soporte multimedia y menos funcionalidad en redes y seguridad. 
• Usuarios profesionales. Menor soporte multimedia y más funcionalidades en redes y seguridad. 
4.1. Versiones 
Windows ha tenido numerosas versiones, y casi todas han tenido diferentes ediciones o subversiones. 
Además de las versiones, Microsoft popularizo los Service Pack. (SP), son varias actualizaciones 
empaquetadas (agrupadas) llamadas parches, que mejoran o corrigen errores de Windows o 
aplicaciones. Con el avance de Internet y su velocidad, desaparecieron estos Service Pack, y se 
implementó en Windows la herramienta Windows Update, para descargas los "parches" o 
actualizaciones de los diferentes componentes de Windows. 
(Como rumor, siempre se ha comentado, que, supuestamente, Microsoft lanzaba sus versiones de 
Windows para que los propios usuarios detectarán los fallos y vulnerabilidades, que Microsoft iba 
corrigiendo). 
Vamos a indicar algunas de las versiones más importantes, centrándonos en Windows para usuarios 
domésticos. 
 

<!-- Page 25 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
25 
 
 
 
Anécdota 
Un dato curioso sobre las versiones domésticas de Windows es que 
alternan una versión buena (que suele asentarse) con otra mala 
(que suele retirarse anticipadamente). Hasta ahora se ha ido 
cumpliendo esta regla. 
• Windows 95 (mal). 
• Windows 98 SE (bien). 
• Windows Millenium (muy mal). 
• Windows XP (bien). 
• Windows Vista (mal). 
• Windows 7 (bien). 
• Windows 8 (mal). 
• Windows 10 (bien). 
 
Windows 1 (1985) 
 
Windows 1 

<!-- Page 26 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
26 
Características: 
• Fue la primera versión de Windows, aunque no era un sistema operativo como tal, sino un 
programa que funcionaba sobre MS-DOS. 
• El software era inestable, pero el sistema de apuntar y hacer click tuvo mucho éxito entre los 
usuarios inexpertos (que eran la mayoría). 
• Contenía características de interfaz gráfica como las barras de desplazamiento y botones 
"Aceptar". 
Versiones/Ediciones: 
• Windows 1. 
• Windows 1.01. 
Windows 2 (1987) 
 
Windows 2 
Características: 
• Windows 2.0 era más rápido y más estable. 
• El sistema presentó el panel de control y ejecutó las primeras versiones de Excel y Word. 

<!-- Page 27 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
27 
Versiones/Ediciones: 
• Windows 2.0. 
• Windows 2.10. 
• Windows 2.11. 
Windows 3 (1990) 
 
Windows 3 
Características: 
• Soportaba 16 colores. 
• Optimizado para el 386. 
• Sigue funcionando en la parte superior de DOS. 
• Versión Windows 3.1 incluía: 
• Compatibilidad con fuentes TrueType. 
• Redes peer-to-peer. 

<!-- Page 28 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
28 
Versiones/Ediciones: 
• Windows 3.0. 
• Windows 3.1. 
• Windows 3.11. 
Windows NT (1993) 
 
Microsoft Windows NT 3.1 
Este sistema estaba orientado a servidores, pero fue de gran importancia ya que en esta tecnología se 
basaron los futuros sistemas operativos para usuarios. 
• Fue un proyecto paralelo a la versión 3. 
• Sistema operativo avanzado para estaciones de trabajo y servidores. 
• 32 bits. 
• Capa de abstracción de hardware. 
• Primera aparición del botón de inicio. 
• Ofrece soporte multiproceso y multiusuario. 
• Sistema de ficheros NTFS. 
• NTVDN (NT Virtual DOS Machine). 

<!-- Page 29 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
29 
Versiones/Ediciones: 
• Windows NT 3.1. 
• Windows 3.5. 
• Windows NT 3.51. 
• Windows NT 4.0. 
 
 
 
 
El experto opina 
Windows NT 4.0, se utilizó durante mucho tiempo, incluso después 
de que Microsoft lo considerara obsoleto. 
Sus usuarios, aunque en muchas ocasiones no lo utilizaban como 
servidor, estaban muy satisfechos con él. 
Apenas era sensible a virus, ya que no se creaban para afectar a 
esta versión de Windows. 
 
Windows 95 (1995) 
 
Windows 95 
"Fue el gran momento de Windows, la versión que revolucionó el mundo con su lanzamiento el 20 de 
noviembre de 1995". 

<!-- Page 30 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
30 
Características: 
• Sistema híbrido 16 y 32 bits. 
• Botón de inicio (por primera vez para los usuarios domésticos). 
• Facilidad de instalación de hardware plug and play. 
• Soporte redes TCP/IP. 
• Direct X. 
• Más colores y mejores aplicaciones multimedia. 
• Incluye Internet Explorer 3.0 (a partir de la versión OSR2). 
Versiones/Ediciones: 
• Windows 95 SP1. 
• Windows 95 OSR1. 
• Windows 95 OSR2. 
• Windows 95 OSR2.1. 
• Windows 95 OSR2.5. 
DirectX: 
DirectX es un conjunto de interfaces de programación de aplicaciones (Apis) desarrolladas por 
Microsoft que facilita la interacción entre el software y el hardware de un ordenador, especialmente en 
lo que respecta a gráficos, sonido y entrada de datos. Su objetivo principal es proporcionar una 
plataforma común para las aplicaciones y juegos, asegurando que puedan ejecutarse en distintas 
configuraciones de hardware sin necesidad de adaptaciones específicas para cada dispositivo. 
DirectX incluye varias API específicas, como Direct3D para los gráficos 3D, DirectDraw para los gráficos 
2D, y DirectSound para el audio, entre otras. A través de DirectX, los desarrolladores pueden acceder a 
las capacidades avanzadas del hardware, como tarjetas gráficas y tarjetas de sonido, para ofrecer 
experiencias visuales y auditivas de alta calidad. Además, DirectX ayuda a mejorar el rendimiento y la 
eficiencia de los videojuegos y aplicaciones multimedia, ya que permite realizar una mejor utilización de 
los recursos del sistema, como la memoria y los procesadores gráficos. 

<!-- Page 31 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
31 
Windows 98 (1998) 
 
Windows 98 
Características: 
• Mejor soporte AGP. 
• Controladores USB. 
• Sistema de ficheros FAT32. 
• Soporte ACPI. 
• Mejor soporte hardware Plug&Play. 
• Se incorporó la utilidad msconfig (oficialmente llamado Configuración del Sistema en Windows 
Vista, Windows 7, Windows 8 y Windows 10). Es una utilidad de sistema para modificar las 
opciones de inicio del sistema Windows, solucionar problemas en el proceso de arranque de 
Microsoft Windows. Puede desactivar o volver a activar software y/o servicios de Windows que 
se ejecutan automáticamente al arrancar el ordenador, controladores de dispositivos (drivers). 
Se incluye con todas las versiones del sistema operativo Microsoft Windows, desde Windows 98 
a excepción de Windows 2000. Los usuarios de Windows 95 y Windows 2000 pueden 
descargarse la utilidad, a pesar de que no fue diseñado para ellos. 
 
 
 
 
+ Info 
ACPI (Advanced Configuration and Power Interface o Interfaz 
Avanzada de Configuración y Energía) es un estándar que 
proporciona mecanismos avanzados para la gestión y ahorro de la 
energía. 
 

<!-- Page 32 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
32 
Versiones/Ediciones: 
• Windows 98: inestable, se producían errores continuos, con pantallazos azules. 
 
BSOD (blue screen of death o pantallazo azul de la muerte) 
 
 
 
Anécdota 
Hay una anécdota curiosa sobre Windows 98. 
En su presentación en la feria Comdex de Windows 98, a Bill Gates 
le apareció la famosa pantalla azul GPF (fallo de protección 
general) que obliga a reiniciar el ordenador. 
Empezó a llamarse "pantallazo azul de la muerte". 
 
 
• Windows 98 SE (Segunda Edición): se convirtió en un sistema bastante estable y con pocos 
fallos, mejorando mucho la primera versión. 
 

<!-- Page 33 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
33 
 
 
 
El experto opina 
Estuvo mucho tiempo en uso, y la mayoría de usuarios se 
mostraban reacios a cambiar de versión. 
 
Windows Me (Millenium Edition) (2000) 
Casi no llegó a utilizarse debido a sus continuos fallos y unas funcionalidades deficientes. 
Tenía una gran cantidad de vulnerabilidades y fallos constantes. 
La característica más relevante fue la incorporación de la función para restaurar el sistema. 
Muchos usuarios optaron por volver a versiones anteriores (Windows 98 SE). 
 
 
 
 
El experto opina 
Aunque la mayoría de los técnicos no lo recomendaban, siempre 
hay usuarios que desean la última versión, aunque funcionen 
correctamente con la instalada en su equipo. 
Se convirtió en la pesadilla de los técnicos informáticos, incapaces 
en muchos casos de hacer que funcionaran correctamente. 
 
Windows 2000 (2000) 
 
Windows 2000 

<!-- Page 34 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
34 
Era una versión orientada a servidores, pero debido al fracaso de Windows Me, se añadieron funciones 
para que fuera utilizada también por los usuarios domésticos de forma sencilla (por ejemplo, añadiendo 
características plug & play). 
Características: 
• Soporte para FAT16, FAT32 y NTFS. 
• Cifrado de ficheros (EFS). 
• Sistema de archivos distribuido (DFS). 
• Nuevo sistema de backup (ASR). 
• Servicios de acceso remoto. 
• Servicios de instalación desatendida por red. 
Versiones/Ediciones: 
• Windows 2000 Professional (muy estable, seguro y poco sensible a virus). 
• Windows 2000 Server. 
• Windows 2000 Advanced. 
• Windows 2000 Datacenter Server. 
Windows XP (2001) 
 
Fondo predeterminado de Windows XP 

<!-- Page 35 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
35 
Características: 
• Interfaz Luna. 
• Primer sistema basado en NT destinado al usuario doméstico. 
• Soporte para computadoras de 64 bits. 
• Buena crítica. Plataforma estable. 
• Entorno gráfico más agradable (uso de temas). 
• Uso de varias cuentas de usuario. 
• Cleartype para mejorar visualización de texto en pantallas planas. 
• Escritorio remoto. 
Versiones/Ediciones: 
• Windows XP Starter Edition. 
• Windows XP Home Edition y Home Edition N. 
• Windows XP Professional, Professional N y Professional x64 Edition. 
• Windows XP Tablet PC Edition. 
• Windows XP Media Center Edition. 4 versiones:. 
• Windows XP Media Center Edition. 
• Windows XP Media Center Edition 2003. 
• Windows XP Media Center Edition 2004. 
• Windows XP Media Center Edition 2005. 
• Windows XP Embedded. 
 
 
 
 
El experto opina 
La versión Windows XP SP2, tenía un buen funcionamiento y era 
muy estable. Todavía en 2020, a pesar de Microsoft dejó de darle 
soporte el 8 de abril de 2014, hay usuarios que siguen utilizándolo. 
 

<!-- Page 36 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
36 
 
 
 
También hay usuarios que optan por instalar una máquina virtual e 
instalar en ella Windows XP, así siguen pudiendo utilizar 
determinados programas, juegos o periféricos, cómo escáner para 
los cuales no se han desarrollado drivers para las versiones más 
actuales de Windows. 
 
Windows Vista (2006) 
Su funcionamiento e interfaz no terminó de gustar a todo el público en general, tuvo muchos 
detractores. La versión home, era muy inestable, la versión profesional proporcionaba un uso 
medianamente aceptable. 
Pero introdujo el controlador WDDM (Windows Display Driver Model) que es una arquitectura de 
controlador gráfico utilizada en Windows que se sigue utilizando en las nuevas versiones de Windows y 
lo que hace es mejorar el rendimiento, la estabilidad y la compatibilidad de los gráficos. Lo que permite 
una interacción más eficiente entre el sistema operativo y el hardware gráfico, gestionando el 
renderizado en modo de usuario, esto significa que los controladores gráficos funcionan aislados del 
núcleo del SO lo que evita que los fallos gráficos afecten al sistema. 
Además, optimiza el uso de la memoria de la tarjeta gráfica y habilita funciones avanzadas como la 
aceleración de hardware, mejorando así el rendimiento en tareas gráficas y multimedia como 
videojuegos y edición de video. 
 
Windows Vista 

<!-- Page 37 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
37 
Características: 
• Interfaz Gráfica Aero. 
• Interfaz metro para pantalla táctil. 
• Efectos visuales nuevos. 
• Tienda de aplicaciones. 
• Windows To Go. 
• Integración de redes sociales. 
• Más lento que XP. 
• Consumía muchos recursos. 
• Muchos fallos. 
Versiones/Ediciones: 
• Windows Vista Starter. 
• Windows Vista Home Basic. 
• Windows Vista Home Premium. 
• Windows Vista Business. 
• Windows Vista Enterprise. 
• Windows Vista Ultimate. 
Windows 7 (2009) 
 
Windows 7 

<!-- Page 38 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
38 
Características: 
• Soporte de arquitecturas de 32 y 64 bits. 
• Interfaz Gráfica Aero. 
• Internet Explorer 8. 
• Soporte para discos duros virtuales. 
• Mejor rendimiento en procesadores multinúcleo. 
• Soporte para varias tarjetas gráficas de distintos fabricantes. 
• Solucionador de problemas. 
• Sensores (de ubicación entre otros). 
• Administración de credenciales. 
• Centro de seguridad pasa a ser Centro de actividades (seguridad y mantenimiento del equipo). 
• Bibliotecas (carpeta virtual que muestra varias carpetas en una sola vista). 
• Jump lists (archivos abiertos recientemente con una determinada aplicación). 
• Modo XP para compatibilidad con programas antiguos. 
• Algunas versiones soportan Bitlocker To Go. 
• KEY_LOCAL_MACHINE (abreviado como HKLM), almacena de todas las cuentas de usuario que 
haya en el ordenador, las configuraciones de software, hardware, etc. 
Versiones/Ediciones: 
• Windows 7 Starter. 
• Windows 7 Starter N. 
• Windows 7 Home Basic. 
• Windows 7 Home Premium. 
• Windows 7 Home Premium N. 
• Windows 7 Professional. 
• Windows 7 Professional N. 

<!-- Page 39 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
39 
• Windows 7 Enterprise. 
• Windows 7 Ultimate. 
• Windows 7 Ultimate N. 
 
 
 
 
Curiosidad 
Es con Windows 7 y Windows Server 2008 R2, ya con 
arquitecturas Windows de 64 bits, donde la capacidad de realizar 
llamadas a procedimientos remotos (RPC) entre procesos de 32 y 
64 bits de manera robusta, ya sea en el mismo equipo como de 
manera remota, y con un amplio conjunto de características se 
introduce efectivamente en el último trimestre del año 2009. 
 
Windows 8 (2012) 
 
Windows 8 
Características: 
• Soporte de arquitecturas de 32 y 64 bits. 
• Interfaz Gráfica Metro. 
• Puede utilizarse en modo pantalla táctil o modo escritorio. 
• Sincronización entre dispositivos. Acceso a la información del usuario desde cualquier 
dispositivo en el que tenga Windows 8. 

<!-- Page 40 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
40 
• Gestor de tareas mejorado. 
• Algunas versiones soportan Bitlocker To Go. 
• Se pueden montar imágenes de disco. 
• Explorador de Windows utiliza interfaz Ribbon (utilizada en Microsoft Office 2007 y 2010). 
• Retirado el modo Windows XP. 
• La interfaz de usuario se denomina Metro UI, y posteriormente paso a denominarse Modern UI. 
Versiones/Ediciones: 
• Windows 8. 
• Windows 8 Pro. 
• Windows 8 Media Center. 
• Windows 8 Enterprise. 
• Windows 8.1. 
Windows 10 (2015) 
 
Windows 10 
 
 
 
Ojo al dato 
En versiones anteriores (Windows 7) en caso de tener la 
herramienta de Windows Update configurada para instalar las 
actualizaciones automáticamente, se descargaba la nueva versión 
Windows 10, y se instalaba en unos de los reinicios del sistema. 
 

<!-- Page 41 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
41 
 
 
 
El usuario no podía interrumpir la instalación. 
En algunos casos esta actualización, causaba prejuicios al usuario, 
tanto por el tiempo en que tardaba en realizarse y el usuario no 
podía utilizar el ordenador como por los cambios que se producían 
al ser una nueva versión. 
 
 
Características: 
• Interfaz Gráfica Continuum. Sustituida por la interfaz Fluent Design (o Metro 2) desde la 
versión RS3. Tienen un modo "Escritorio de PC" y otro "tableta". 
• Se recupera el menú "inicio", eliminado en Windows 8. 
• Los archivos de configuración de inicialización de Windows son .ini. 
• Microsoft Edge es el nuevo navegador por defecto (aún se puede abrir Microsoft Internet 
Explorer para compatibilidad con determinadas páginas y aplicaciones). 
• Windows Hello. Inicio de sesión por huella digital o reconocimiento facial. 
• Vista de Tareas. 
• Escritorio virtual. 
• Integración de Xbox Live. 
• Cortana (Asistente virtual). Sustituye a la función de búsqueda integrada con Windows. 
• Windows Update instala las actualizaciones automáticamente. En Windows Pro y Enterprise se 
permite aplazarlas. 
• Cross-buy. Si compras una aplicación en un dispositivo, (por ejemplo, un PC) puedes usar la 
versión de móvil sin coste adicional. 
• Nearby sharing (sustituye a Grupo Hogar). 
• Se elimina Windows Media Center. 
• Soporta BitLocker To Go. 
• Hyper-V para la creación de máquinas virtuales. 

<!-- Page 42 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
42 
• Incluye, entre otras, las siguientes aplicaciones: 
• 3D Builder. 
• Centro d. 
• seguridad de Windows Defender. 
• Cortana. 
• Editor de películas (extensión de Fotos). 
• El Tiempo. 
• Fotos. 
• Grabadora de voz. 
• Groove Música (sustituye a Xbox Music). 
• Mapas. 
• Microsoft Edge. 
• Microsoft Solitaire Collection. 
• Microsoft Store. 
• OneDrive, en forma nativa. 
• OneNote. 
• Películas y TV (antes Microsoft Video). 
• Paint 3D. 
• Portal de realidad mixta. 
• Sticky Notes. 
• Surface. 
• Visor de realidad mixta. 
• Skype. 
• Xbox. 

<!-- Page 43 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
43 
Versiones/Ediciones: 
• Windows 10 Home. 
• Windows 10 Pro. 
• Windows 10 Enterprise. 
• Windows 10 Education. 
• Windows 10 Pro Education. 
• Windows 10 Enterprise LTSB (Long Term Support o soporte a largo plazo). 
• Windows 10 Mobile. 
• Windows 10 Mobile Enterprise. 
• Windows 10 IoT (Internet of Things). 
Internet of Things o internet de las cosas es un concepto que se refiere a la interconexión de 
todo tipo de objetos. Este concepto está más enfocado a la interconexión y gestión de unos 
objetos por otros, en lugar de por personas. 
• Windows 10 IoT Core. 
• Windows 10 IoT Enterprise. 
• Windows 10 IoT Mobile Enterprise. 
• Windows 10 S (en la nube). 
• Windows 10 Team. 
• Windows 10 Pro for Workstations. 
Windows 11 
Es la versión más reciente de Windows, fue lanzado oficialmente el 5 de octubre de 2021, como una 
actualización gratuita (a través de Windows Update) para los equipos con Windows 10 que cumplan 
con ciertas especificaciones técnicas compatibles del nuevo sistema operativo. 
Características: 
• Mejorado el rendimiento y la facilidad de uso sobre Windows 10. 
• Cuenta con cambios importantes en el Shell de Windows influenciados por el cancelado 
Windows 10X (versión que no llego a lanzarse al mercado), incluido: 
• Un menú Inicio rediseñado. 

<!-- Page 44 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
44 
• El reemplazo de sus iconos dinámicos (Live Tiles) con un panel separado llamado 
«Widgets» con noticias e intereses. 
• La capacidad de crear conjuntos de ventanas en mosaico que se pueden minimizar y 
restaurar desde la barra de tareas como grupo. 
• Nuevas tecnologías de juego heredadas de Xbox Series X y Series S, como Auto HDR y 
DirectStorage en hardware compatible. 
• Internet Explorer está completamente eliminado y reemplazado por el motor Blink en el que se 
basa Microsoft Edge. 
• Microsoft Teams está integrado en el Shell de Windows en la Barra de Tareas. 
• Microsoft también anunció futuros planes para ofrecer soporte para aplicaciones de Android 
que se ejecutarán en Windows 11, con soporte para Amazon Appstore y paquetes instalados 
manualmente. 
• Requiere el arranque seguro UEFI y chip TPM (compatibilidad con Trusted Platform Module 2.0). 
Existen métodos para instalar Windows 11 en equipos sin TPM, peroMicrosoft ha indicado que 
estos ordenadores tendrán más errores, y no recibirán actualizaciones de seguridad del Sistema 
Operativo, ni tampoco las actualizaciones periódicas que vayan lanzando con nuevas 
características. 
• Windows 11 ya no es compatible con la arquitectura x86 de 32 bits o los sistemas que usan 
firmware del BIOS. 
 
 
 
 
+ Info 
Puedes consultar más información en la web oficial de Microsoft. 
https://www.microsoft.com/es-es/windows/windows-11?r=1 
 
 
Requisitos mínimos que pide Windows 11: 
• Procesador: Windows 11 solo tiene versión de 64 bits, por lo que los procesadores con 32 bits 
no podrán actualizarse. 
Requiere 2 o más núcleos de 1 GHz o más, y tiene que ser un procesador de 64 bits compatible 
o sistema en un chip (SoC, del inglés system on a chip). 

<!-- Page 45 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
45 
SoC, describe la tendencia cada vez más frecuente de usar tecnologías de fabricación que 
integran todos o gran parte de los módulos que componen un computador o cualquier otro 
sistema informático o electrónico en un único circuito integrado o chip. 
• Memoria RAM: un mínimo de 4 GB de memoria RAM. 
• Almacenamiento: es necesario un mínimo de 64 GB de espacio libre en el disco duro donde se 
vaya a instalar. 
• Firmware del sistema: 
Como ya hemos indicado en las característica, es necesario un ordenador con UEFI, y 
compatible con Secure Boot. 
• TPM 2.0: 
Es necesario compatibilidad con el Módulo de plataforma segura 2.0 o TPM 2.0. 
Para saber si un ordenador con Windows tiene TPM hay que abrir el menú de inicio y escribir 
tpm.msc. 
Se abrirá una venta, un programa con ese nombre y el icono de una llave y un microchip, hay 
que pulsar en él para acceder. 
• Si el programa indica que No se encuentra TPM compatible significa que el ordenador no 
tiene el chip TPM, y que no podrá actualizar a Windows 11. 
Será necesario, instalar el chip en la placa base (si dispone de esa opción, o bien cambiar la 
placa base. 
• Si dentro de este programa sí te aparece información sobre TPM, entonces es que sí que 
esta esté chip instalado. 
Puede ser que ya esté activado o que sea necesario activarlo manualmente (en la opción 
Preparar TPM de la columna de la derecha, o desde UEFI). 
• Tarjeta gráfica: necesita ser compatible con DirectX 12 o posterior, y con el controlador 
WDDM 2.0. 
• Pantalla: de un mínimo de 9 pulgadas en diagonal, con 720p de alta definición, y canal de 8 bits 
por color. 
• Otros: es necesario tener una cuenta de Microsoft, y estar conectado a Internet para la 
configuración inicial. 
 

<!-- Page 46 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
46 
 
 
 
El experto opina 
Ante una nueva versión de Windows piénsatelo antes de 
instalártela… 
Nuestro consejo, es que no cambies inmediatamente a la nueva 
versión, espera siempre unos meses para que se realicen 
correcciones a los errores que detecten los usuarios y ver que 
aceptación tiene por los usuarios. 
 
4.2. Elementos básicos del interfaz de Windows 
Son muchos los elementos que componen el interfaz de Windows. Seguramente ya conoces los más 
importantes. 
 
 
 
 
Recomendación 
Si tienes tiempo, sería interesante que aprendas a usar bien 
Windows 10 (incluso uno de Windows 7), ya que aún se utiliza 
mucho en la administración. 
También puedes usar la opción utilizar una máquina virtual para 
instalar esas versiones de Windows y practicar. 
 
 
No es nuestro objetivo, ni necesario, profundizar en este tema, por lo que solo vamos a enumerar los 
más comunes. 

<!-- Page 47 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
47 
 
Escritorio 
Es el área de la pantalla inicial (la que vemos en la imagen anterior). Ejerce la función de escritorio o 
superficie de trabajo. Distintos elementos (como iconos) aparecen en el escritorio, y al abrir un 
programa, éste aparece en el escritorio (dentro de una ventana). 
Ventana 
Es un área de forma rectangular que muestra un interfaz con una aplicación. 
En Windows podemos abrir más de una ventana a la vez, incluso verlas (sobre el escritorio) al mismo 
tiempo. 
Si minimizamos una ventana, la aplicación permanecerá en la barra de tareas y podremos restaurar la 
ventana desde aquí. 
En una ventana podemos encontrar: 
• Los botones de control (para cerrar, minimizar y maximizar/restaurar la ventana). 
• La barra de título. 
• La barra de menús. 
• La barra de herramientas. 
• Las barras de desplazamiento. 
• La barra de estado. 

<!-- Page 48 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
48 
Los iconos 
Son pictogramas que se utilizan para representar aplicaciones, carpetas, archivos o accesos directos. 
En Windows, los iconos son ficheros binarios con extensión ".ico". 
Papelera de reciclaje 
Área donde se almacenan los elementos borrados antes de ser eliminados del medio de 
almacenamiento. Permite restaurarlos. 
La barra de tareas 
Muestra las ventanas abiertas (programas en ejecución). 
Menú Inicio 
Aparece al pulsar el botón inicio. 
Es una lista con accesos directos a las principales aplicaciones, carpetas y servicios y opciones comunes 
como los botones de apagar, reiniciar, panel de control (configuración), el cuadro de búsqueda, etc. 
Explorador de archivos 
Es una ventana que nos permite administrar los directorios del equipo. 
Desde aquí podemos crear, copiar o borrar archivos y carpetas, etc. 
 
 
 
 
Atención 
El explorador de Windows, NO es para administrar el equipo, para 
ello se utiliza el Panel de Control. 
 

<!-- Page 49 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
49 
 
Explorador de archivos 
El Explorador de Windows se puede abrir de diferentes formas, que dependerán también de la versión 
de Windows que tengamos instalada. Algunas de ellas son: 
• Presionar teclas: Win + E. 
• Presionar Win + R (Ejecutar…) y escribir "explorer". 
• Hacer click con el botón derecho del ratón (en caso de diestros), sobre el botón Inicio y 
seleccionar la opción "Explorador de Windows". 
4.3. Opciones de energia 
La configuración de energía permite ajustar el comportamiento del sistema en función de las 
necesidades de rendimiento, consumo eléctrico o autonomía. Tanto en equipos de usuario como en 
servidores, una correcta gestión de los planes de energía puede mejorar la eficiencia, prolongar la vida 
útil del hardware y reducir el gasto energético. A continuación, se analizan las opciones disponibles 
según la edición del sistema operativo: Home, Pro y Server. 
4.3.1. Opciones de energía en Windows 10/11 Home 
Las ediciones Home de Windows 10 y Windows 11 ofrecen los planes de energía básicos que permiten 
adaptar el comportamiento del equipo a distintos usos. Los tres planes principales son: Equilibrado, que 
ajusta el rendimiento y el consumo energético de forma dinámica; Alto rendimiento, que prioriza la 
potencia de procesamiento sacrificando la eficiencia energética; y Ahorro de energía, que reduce el uso 
de recursos del sistema para extender la duración de la batería. 

<!-- Page 50 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
50 
Estos planes están disponibles a través de la aplicación de Configuración en el apartado de Sistema > 
Energía y suspensión, o desde el clásico Panel de control > Opciones de energía. En estas versiones, los 
usuarios pueden modificar aspectos como el tiempo de suspensión de la pantalla o del sistema, pero no 
disponen de herramientas administrativas avanzadas para aplicar políticas centralizadas sobre la 
energía. 
4.3.2. Opciones de energía en Windows 10/11 Pro 
Las opciones de energía en Windows 10 y Windows 11 Pro son fundamentales para controlar el 
comportamiento del sistema en relación con el consumo energético y el rendimiento. Esto resulta 
especialmente relevante en dispositivos portátiles, como ordenadores portátiles y convertibles, donde 
la autonomía de la batería es un recurso clave. Ambas versiones del sistema ofrecen planes de energía 
predefinidos como "Equilibrado", "Alto rendimiento" y "Ahorro de energía". 
El plan Equilibrado ajusta automáticamente el uso de recursos del sistema según las tareas que se estén 
ejecutando, tratando de mantener un equilibrio entre rendimiento y eficiencia energética. El plan de 
Alto rendimiento maximiza el rendimiento del procesador y de los componentes, aunque a costa de un 
mayor consumo eléctrico, mientras que el plan de Ahorro de energía reduce la actividad de los 
componentes no esenciales para conservar batería, sacrificando rendimiento. 
En ambas versiones Pro, el usuario tiene la posibilidad de crear planes de energía personalizados. Esto 
permite definir aspectos como el tiempo de apagado de la pantalla, el tiempo de suspensión del equipo 
o la administración del disco duro cuando el sistema está inactivo. Estas configuraciones se gestionan 
desde el apartado "Configuración > Sistema > Energía y suspensión", o desde el Panel de control clásico 
a través de "Opciones de energía". 
4.3.3. Opciones de energía en Windows Server 
Windows Server incorpora igualmente las opciones de energía, aunque su enfoque es diferente. Dado 
que estos sistemas están diseñados para operar de forma continua y estable, el plan de energía por 
defecto suele ser Alto rendimiento, y muchas veces se desactivan funciones como la suspensión 
automática. La prioridad en estos equipos no es el ahorro energético, sino la disponibilidad constante 
del servicio. 
Además, la configuración energética puede integrarse con entornos de virtualización, como Hyper-V, y 
gestionarse a través de soluciones de administración centralizada. En servidores físicos, también puede 
complementarse con configuraciones de BIOS/UEFI, asegurando que los dispositivos estén siempre 
operativos en condiciones de carga variable. 
4.4. Variables de entorno 
Las variables del entorno son valores del sistema operativo que permiten definir configuraciones 
fundamentales que afectan al funcionamiento de programas, scripts y procesos del sistema. Aunque su 
propósito es el mismo en todas las versiones de Windows, su uso y nivel de acceso varían según la 
edición del sistema. 

<!-- Page 51 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
51 
4.4.1. Variables de entorno en Windows 10/11 Home 
En las versiones Home, las variables de entorno pueden visualizarse y configurarse desde Propiedades 
del sistema > Configuración avanzada del sistema > Variables de entorno. Desde esta interfaz, el usuario 
puede definir variables propias de su sesión (variables de usuario), como TEMP, USERNAME o PATH, y 
también, con permisos de administrador, modificar variables del sistema. 
Un uso habitual es el de añadir rutas de programas a la variable PATH, de manera que estos puedan 
ejecutarse desde cualquier ubicación en la línea de comandos sin necesidad de desplazarse hasta el 
directorio donde están instalados. 
Aunque los usuarios domésticos pueden configurar estas variables para facilitar el uso de ciertos 
programas o entornos de desarrollo, la funcionalidad se limita a configuraciones individuales, y no 
existen herramientas para distribuir o imponer configuraciones comunes en varios equipos desde una 
consola central. 
4.4.2. Variables de entorno en Windows 10/11 Pro 
En las ediciones Pro, el funcionamiento de las variables del entorno es el mismo que en la versión Home, 
pero con una importante diferencia: se pueden gestionar a través de directivas de grupo, lo que permite 
aplicar variables a múltiples usuarios o estaciones de trabajo desde una administración centralizada. 
Esto resulta especialmente útil en entornos corporativos o educativos donde se requiere coherencia en 
la configuración de entornos de desarrollo, rutas de herramientas, carpetas temporales o scripts. 
Además, muchos scripts administrativos (tanto en PowerShell como en Batch) utilizan variables del 
entorno para realizar tareas automatizadas. La existencia de variables de sistema como %SystemRoot%, 
%ProgramData% o %USERPROFILE% facilita la creación de scripts portables y adaptables a cualquier 
usuario o instalación. 
4.4.3. Variables de entornos en Windows Server 
En Windows Server, el uso de variables del entorno es intensivo y forma parte de la gestión 
automatizada de tareas, scripts de mantenimiento y políticas de red. Su funcionamiento es idéntico al 
de los sistemas cliente, pero en el contexto de servidores, se utilizan comúnmente en scripts de inicio 
de sesión, tareas programadas y procesos de configuración desatendida. 
Además, es habitual definir variables personalizadas como parte de entornos de ejecución controlados. 
A través de scripts distribuidos por GPO o mediante herramientas como System Center Configuration 
Manager (SCCM), se pueden definir rutas de red, claves de configuración o parámetros de conexión, 
todo ello utilizando variables de entorno como soporte de datos compartidos. 

<!-- Page 52 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
52 
4.5. Registros de Windows 
El Registro de Windows es una base de datos jerárquica donde se almacenan configuraciones críticas 
del sistema operativo, de los programas instalados y del perfil de usuario. Aunque todas las versiones de 
Windows incluyen esta funcionalidad, el uso y acceso al registro varía según el tipo de sistema. 
4.5.1. Registros en Windows 10/11 Home 
En las versiones Home, el acceso al registro está permitido a través de la herramienta regedit.exe 
(Editor del Registro). Los usuarios pueden explorar y modificar claves que controlan funciones del 
sistema, comportamiento de aplicaciones, configuración de hardware y parámetros visuales. 
La edición del registro permite ajustar configuraciones que no están disponibles a través de la interfaz 
gráfica. Por ejemplo, es posible modificar parámetros ocultos del explorador de archivos, desactivar 
funciones específicas del sistema o establecer restricciones en el comportamiento del usuario. 
Sin embargo, cualquier modificación en el registro debe hacerse con precaución, ya que errores pueden 
comprometer la estabilidad del sistema, impedir su arranque o afectar el funcionamiento de 
aplicaciones. Aunque las versiones Home no permiten aplicar políticas mediante GPO, muchos ajustes 
equivalentes pueden realizarse directamente mediante cambios en el registro, siguiendo guías 
avanzadas. 
4.5.2. Registros en Windows 10/11 Pro 
Las versiones Pro permiten las mismas ediciones que Home, pero además complementan la gestión del 
registro con herramientas de administración como el Editor de directivas de grupo. Muchas de las 
políticas aplicadas mediante GPO se traducen internamente en modificaciones en el registro, lo que 
permite a los administradores definir de forma centralizada valores de configuración para múltiples 
equipos sin tener que editar manualmente las claves en cada uno de ellos. 
Además, los administradores pueden exportar configuraciones del registro y distribuirlas como archivos 
.reg, que se pueden ejecutar en otros sistemas para replicar configuraciones personalizadas. 
4.5.3. Registros en Windows Server 
En los sistemas Windows Server, el registro es una herramienta fundamental para la administración 
avanzada. Al igual que en los sistemas cliente, se accede mediante regedit, pero su uso es más frecuente 
y está relacionado con la configuración de servicios, roles del servidor, políticas de seguridad, control de 
acceso y comportamiento del sistema en red. 
Es común que los administradores modifiquen el registro de forma remota a través de la red, 
accediendo al registro de otros servidores o estaciones de trabajo para realizar configuraciones sin 
intervención directa. También es habitual su uso dentro de scripts de automatización, procesos de 
despliegue o restauración de configuraciones. 

<!-- Page 53 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
53 
La modificación del registro en Windows Server debe realizarse con especial precaución, ya que los 
errores pueden tener un impacto en múltiples usuarios o afectar servicios críticos como controladores 
de dominio, servicios de archivos o aplicaciones empresariales. 
4.6. Microsoft Azure 
 
Fuente: Wikimedia commons 
(Anteriormente Windows Azure y Azure Services Platform). 
Es un servicio en la nube ofrecida como servicio y alojado en los Data Centers de Microsoft. 
Su versión beta fue anunciada en el Professional Developers Conference de Microsoft (PDC) del 2008 
con el nombre en clave "Project Red Dog" pasó a ser un producto comercial a principios de 2010 como 
Windows Azure. En marzo de 2014 se rebautizo como "Microsoft Azure". 
Anunciada en el Professional Developers Conference de Microsoft (PDC) del 2008 en su versión beta, 
pasó a ser un producto comercial el 1 de enero de 2010. 
Microsoft Azure es una plataforma general que tiene diferentes servicios para aplicaciones, desde 
servicios que alojan aplicaciones en alguno de los centros de procesamiento de datos de Microsoft para 
que se ejecute sobre su infraestructura (Cloud Computing) hasta servicios de comunicación segura y 
federación entre aplicaciones. 
El servicio de proceso de Microsoft Azure ejecuta aplicaciones basadas en Windows Server, que pueden 
ser creadas mediante .NET Framework, o sin él. 
Su infraestructura posibilita desplegar de una forma sencilla máquinas virtuales con Windows Server o 
con distribuciones de Linux. 
Microsoft Azure se ejecuta en un gran número de máquinas, y es posible combinar las máquinas en un 
solo centro de datos de Microsoft Azure formando un conjunto. 
 
 
 
 
+ Info 
Puedes consultar los servicios que ofrece y su funcionamiento en la 
web oficial. https://azure.microsoft.com/es-es/ 
 

<!-- Page 54 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
54 
4.7. Herramientas de Windows 
Microsoft ha ido desarrollando diferentes herramientas e incorporándolas a sus nuevas versiones de 
Windows, para poder realizar diferentes gestiones. 
Vamos a ver algunas de ellas. 
4.7.1. ActiveSync 
ActiveSync es un programa de sincronización de datos desarrollado por Microsoft para su uso con sus 
sistemas operativos Microsoft Windows. 
Originalmente lanzado con el nombre "Explorador de PC Móvil" en 1996, proporciona a los usuarios de 
Microsoft Windows una manera de transportar los documentos, calendarios, listas de contacto y correo 
electrónico entre la computadora de escritorio y un dispositivo móvil, como un PC de mano, teléfonos 
móviles o cualquier otro dispositivo portátil que soporte el protocolo de ActiveSync. 
ActiveSync está disponible como una descarga gratuita desde el sitio web de Microsoft. 
ActiveSync utiliza Exchange ActiveSync, un protocolo propietario que requiere de otros proveedores de 
la licencia del protocolo para lograr la compatibilidad. 
A partir de Windows Vista, ActiveSync se ha sustituido por el Windows Mobile Device Center, que se 
incluye como parte del sistema operativo. 
4.7.2. AppLocker 
Es una herramienta de Windows que mejora el control de las aplicaciones, pudiento especificar que 
usuarios o grupos pueden ejercutar o no una aplicación. 
Está disponible en Windows 10 y Windows Server. 
Con AppLocker puede: 
• Controlar los siguientes tipos de aplicaciones: 
• Archivos ejecutables (. exe y. com). 
• Scripts (. js,. ps1,. vbs,. cmd y. bat). 
• Archivos de Windows Installer (. MST,. msi y. msp). 
• Archivos DLL (. dll y. ocx). 
• Aplicaciones empaquetadas y los instaladores de aplicaciones empaquetadas (Appx). 

<!-- Page 55 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
55 
• Definir reglas basadas en atributos de archivo derivados de la firma digital, como el editor, el 
nombre de producto, el nombre de archivo y la versión de archivo. Por ejemplo, puede crear 
reglas basadas en el atributo Editor persistente a través de las actualizaciones, o bien puede 
crear reglas para una versión específica de un archivo. 
• Asignar una regla a un grupo de seguridad o a un usuario individual. 
• Crear excepciones a ciertas reglas. 
• Por ejemplo, puede crear una regla que permita que se ejecuten todos los procesos de Windows 
excepto el editor del registro (regedit. exe). 
• Usar el modo de solo auditoría para implementar la directiva y ver qué impacto tendría antes de 
aplicarla. 
• Importar y exportar reglas. La importación y la exportación afectan a toda la Directiva. Por 
ejemplo, si exporta una directiva, se exportan todas las reglas de todas las colecciones de reglas, 
incluida la configuración de aplicación de las colecciones de reglas. Si importa una directiva, se 
sobrescriben todos los criterios de la directiva existente. 
• Simplificar la creación y la administración de reglas de AppLocker mediante cmdlets de 
Windows PowerShell. 
AppLocker ayuda a reducir la sobrecarga administrativa y ayuda a reducir el costo de administrar los 
recursos de computación de la organización al disminuir la cantidad de llamadas al servicio de asistencia 
que resultan de los usuarios que ejecutan aplicaciones no aprobadas. 
4.7.3. Interfaz de Consola CLI 
La interfaz de línea de comandos o interfaz de línea de órdenes es un método que permite a los usuarios 
dar instrucciones a algún programa informático por medio de una línea de texto simple. 
Hay que tener en cuenta, que los conceptos de CLI, shell y emulador de terminal no son lo mismo 
(aunque suelen utilizarse como sinónimos): 
• CLI es un método. 
• shell es un programa informático que proporciona la interfaz de línea de comandos y puede 
interpretar y ejecutar comandos. 
• emulador: es un programa que emula una terminal física, permitiendo a los usuarios interactuar 
con el shell. 
Windows 95, Microsoft introdujo el Símbolo del Sistema (cmd.exe) como el shell de línea de comandos 
para Windows. Este shell se basó en los conceptos de MS-DOS, pero estaba integrado en el entorno de 
Windows y proporcionaba una interfaz para ejecutar comandos y scripts en el contexto de Windows. 

<!-- Page 56 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
56 
4.7.4. Windows Script Host 
Windows Script Host (WSH) es un motor y entorno de ejecución de scripts que permite utilizar 
lenguajes como VBScript y JScript. Ofrece una funcionalidad más avanzada que los archivos por lotes 
(batch), superándolos en cuanto a la variedad de lenguajes que admite y la sofisticación de los scripts 
que se pueden crear. 
WSH se utiliza para tareas que requieren una interacción más compleja con el sistema operativo que lo 
que permiten los archivos por lotes, como el control de aplicaciones, la manipulación del registro de 
Windows o el acceso a objetos COM (Component Object Model). 
Para ejecutar scripts de Windows Script Host (WSH), se puede hacer de varias maneras: haciendo doble 
clic en el archivo de script (.vbs o .js) desde el Explorador de Windows, lo que utilizará el intérprete 
predeterminado; o mediante la línea de comandos usando el Símbolo del Sistema o PowerShell, 
ejecutando el script con los comandos cscript o wscript. Simplemente abre el Símbolo del Sistema o 
PowerShell, navega al directorio que contiene el script y utiliza uno de estos comandos para ejecutarlo. 
Aunque se pueden ejecutar scripts más complejos en el símbolo del sistema utilizando WSH, no permite 
ejecutar cmdlets de PowerShell. La automatización de tareas es generalmente más eficiente y versátil 
con PowerShell, que proporciona un lenguaje de scripting mucho más potente y extensible que el 
disponible en el símbolo del sistema o Windows Script Host. 
4.7.5. PowerShell 
Originalmente llamada Windows PowerShell. 
Es una interfaz de consola (CLI) con posibilidad de escritura y unión de comandos por medio de 
instrucciones (scripts en inglés). 
Esta interfaz de consola está diseñada para su uso por parte de administradores de sistemas, con el 
propósito de automatizar tareas o realizarlas de forma más controlada. 
Se presentó junto con el sistema operativo Windows Vista y se incluye también en Windows 7, 
Windows 8 y Windows 10. 
 
 
 
 
+ Info 
Requiere de la instalación previa del framework .NET versión 2.0 
para su funcionamiento. Lo estudiaremos en posteriores unidades. 
También puede ser instalado en sistemas Linux y MacOS. 
 

<!-- Page 57 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
57 
La herramienta PowerShell es posible abrirla rápidamente accediendo a la función Ejecutar que se 
incluye en Windows, para ello: 
• Hay que presionar de manera simultánea las teclas Windows + R. 
Se mostrará el cuadro Ejecutar. 
• En el cuadro Ejecutar, escribimos PowerShell. 
• Hacer clic en Aceptar o presionar directamente la tecla Enter. 
 
 
 
 
Imprescindible 
Los comandos de PowerShell se llaman cmdlets. 
(cmdlet en singular). 
 
5. Sistemas Unix y Linux 
 
Fuente: UniX_Logo File de Wilkimedia Commons 
 
Fuente: Flickr 

<!-- Page 58 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
58 
Primero vamos a definir las similitudes y diferencias entre UNIX y Linux. 
UNIX es un sistema operativo completo, desarrollado por AT&T en colaboración con diversas 
universidades. Está pensado en la facilidad de instalación en distintos hardware y la robustez 
(seguridad) de sistema. 
Linux NO es un sistema operativo completo. Sería solo la parte del Kernel, se realizó basándose en el 
UNIX pero reescribiendo todo el software para poder generar una distribución libre también llamada de 
Código Abierto. Tiene la misma sistemática de trabajo que el UNIX, por tanto prácticamente la 
totalidad de lo que vamos a ver más adelante es aplicable tanto a UNIX como a Linux. 
Un S.O. sin escritorio y aplicaciones no está completo, por lo que el resto del entorno se ha desarrollado 
por diversos desarrolladores comerciales, el más conocido GNU (GNU's Not Unix -GNU no es Unix), por 
lo que muchas veces es conocido como GNU/Linux. 
Linux es un sistema robusto y seguro. No suele haber problemas de virus y es gratuito. 
El código está disponible y hay una legión de usuarios dispuestos a mejorar el sistema y ayudar a los 
principiantes. ¿Por qué no es el sistema operativo más usado? 
Linux ha sido siempre un sistema operativo más difícil de manejar (aunque actualmente es mucho más 
sencillo y se sigue trabajando en ello). 
 
 
 
 
El experto opina 
Windows se utiliza mucho más, pero eso no quiere decir que sea 
mejor. 
Windows está orientado a facilitar la vida del usuario, mientras que 
Linux estaba orientado a ser flexible y robusto. 
Instalar los drivers de hardware en Windows es mucho más 
sencillo, y Windows tiene Microsoft Office (la aplicación de 
ofimática más utilizada). 
Mac OS clásico, desarrollado íntegramente por Apple, con primera 
versión en 1985, extendió su desarrollo hasta la versión 9 del 
sistema, lanzada en 1999. A partir de la versión 10 (Mac OS X), el 
sistema cambió su arquitectura totalmente y pasó a basarse en 
Unix, aunque su interfaz gráfica mantiene muchos elementos de 
las versiones anteriores. 
 

<!-- Page 59 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
59 
UNIX 
El sistema operativo Unix bebe directamente de CTSS (Compatible Time-Sharing System) y Multics. 
CTSS, desarrollado en el MIT, fue uno de los primeros sistemas operativos que puso el foco en el tiempo 
compartido. Multics (Multiplexed Information and Computing Service) y su esquema de seguridad 
avanzado (modelo de anillos de protección), por su lado, fue desarrollado entre MIT, Bell Labs y 
General Electric. 
Con la idea clara de conseguir un sistema operativo simple y eficiente, Unix nace en 1969. Sus primeras 
versiones fueron desarrolladas en ensamblador. Dennis Ritchie, uno de sus creadores, traduce el código 
a lenguaje C en 1973, un hecho que facilitaría la portabilidad del software a otras máquinas distintas. 
La séptima versión de Unix (1979) será la base sobre la que la Universidad de California, Berkeley, 
comience a desarrollar su propia versión BSD (Berkeley Software Distribution). BSD orientaría su 
sistema de archivos y directorios jerárquicos a la distribución en red, permitiendo a los usuarios acceder 
a los archivos remotos como si fueran locales: el Network File System (NFS). 
Más tarde, AT&T desarrollará a principios de los 80 una versión llamada AT&T Unix System V, que 
multiplicará las implementaciones de este sistema operativo, convirtiéndolo en un éxito comercial. En 
las dos últimas décadas del siglo pasado se trató de conseguir un estándar. A principios de los 90, 
aparece Linux, que, si bien no puede ser considerado como un sistema Unix, sí tiene muchos puntos en 
común, pues está construido siguiendo los principios y características de Unix. 
Las características fundamentales de Unix son la multitarea y el multiusuario, la portabilidad, el sistema 
de archivos jerárquico en estructura de árbol, la interconexión de procesos (redirección de entrada y 
salida de comandos y tuberías), y un robusto conjunto de utilidades y herramientas de software. 
LINUX 
Linux es un sistema operativo gratuito y de libre distribución inspirado en el sistema Unix escrito por 
Linus Torvalds. 
Por lo tanto, al estar basado en Unix es más difícil de manejar que sistemas Microsoft Windows o MAC 
OS (de Apple), pero desde hace unos años se está trabajando para facilitar su uso. 
Linux es un sistema operativo flexible, estable y de bajo coste, por lo que muchas empresas y 
administraciones públicas están migrando sus sistemas a Linux (especialmente los servidores). 
5.1. Características 
Vamos a destacar las características más importantes que los diferencian de otros sistemas operativos. 
• Sistema operativo de código abierto. Podemos disponer de sus fuentes, modificarlas y crear 
nuevas versiones que poder compartir bajo la licencia GPL (lo cual lo convierte a su vez en 
software libre). 

<!-- Page 60 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
60 
• Portabilidad. Está pensado para no depender de la arquitectura de una máquina concreta. 
• Se puede portar a casi cualquier arquitectura que pueda compilar C. 
• GNU/Linux es uno de los sistemas que soporta mayor número de arquitecturas. 
• Kernel monolítico. Kernel unido en una sola pieza, pero conceptualmente modular en las 
diferentes tareas. 
• Mejor rendimiento a costa de menor escalabilidad. 
• Módulos dinámicamente cargables. Partes del sistema operativo (como los controladores de 
dispositivos) son externas al kernel y enlazan con este en tiempo de ejecución cuando son 
demandados. 
• Simplifica el kernel. 
• Se pueden programar por separado. 
• El kernel funciona como un kernel mixto: es monolítico, pero tiene módulos que lo 
complementan (parecido al concepto de microkernel). 
• Desarrollo del sistema por la comunidad. 
 
 
 
 
+ Info 
Es posible que te preguntes qué es software libre. 
• Software libre significa que los usuarios tienen la libertad de 
ejecutar, copiar, distribuir, estudiar, modificar y mejorar el 
software. 
• Para ello, los usuarios tienen las siguientes libertades: 
1. Libertad para ejecutar el programa como lo desee, con 
cualquier propósito. 
2. Libertad para estudiar el funcionamiento del programa 
y adaptarlo a sus necesidades (se puede acceder al 
código). 
3. Libertad para redistribuir copias para ayudar a los 
demás. 
4. Libertad para mejorar el programa y publicar sus 
mejoras para beneficio de la comunidad. 
 

<!-- Page 61 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
61 
5.2. Conceptos básicos 
Kernel 
El kernel Linux es el componente central de un sistema operativo GNU/Linux. Su función principal es 
gestionar los recursos del hardware -como el procesador, la memoria, los dispositivos de 
almacenamiento y periféricos- y proporcionar a las aplicaciones un conjunto de abstracciones que les 
permite acceder a esos recursos de forma uniforme, segura y eficiente. 
Shell 
Shell (intérprete de comandos) es el programa que provee una interfaz de usuario para acceder a los 
servicios del sistema operativo. 
Por lo tanto, la shell actúa como un intermediario entre el sistema operativo y el usuario. 
Su función es la de leer la línea de comandos, interpretar su significado, ejecutar el comando y mostrar 
el resultado. 
El usuario se comunica con el sistema operativo mediante las líneas de comando que introduce en la shell. 
La shell es un archivo ejecutable cuyo nombre de fichero suele coincidir con el nombre de Shell. 
Algunas de las más comunes son: sh (Borune Shell), bash (Bourne again Shell) y csh (C Shell). 
Repositorios 
Los repositorios en un sistema operativo Linux son servidores web que alojan una amplia compliación 
de aplicaciones que los administradores de sistema y usuarios pueden instalar en su ordenador. El 
administrador del sistema elegirá qué repositorios usar y qué aplicaciones serán necesarias en función 
de los requerimientos y características que necesite el sistema a implementar. Además de los 
repositorios existen otras fuentes de programas para Linux como sitios web de desarrolladores, tiendas 
de aplicaciones (ubuntu, gnome) o paquetes independientes (GIMP, Libreoffice, VLC, Firefox) y 
software de código cerrado. 
Inodo (Inode) 
Es una estructura de datos que contiene las características de un archivo regular, directorio, o cualquier 
otro objeto que pueda contener el sistema de ficheros. El tipo de archivo. 
El término se refiere generalmente a inodos en discos (dispositivos en modo bloque) que almacenan 
archivos regulares, directorios, y enlaces simbólicos. El concepto es particularmente importante para la 
recuperación de los sistemas de archivos dañados. 

<!-- Page 62 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
62 
Cada inodo queda identificado por un número entero, único dentro del sistema de ficheros, y los 
directorios recogen una lista de parejas formadas por un número de inodo y nombre identificativo que 
permite acceder al archivo en cuestión: cada archivo tiene un único inodo, pero puede tener más de un 
nombre en distintos o incluso en el mismo directorio para facilitar su localización. 
El estándar POSIX establece un modelo de sistema de archivos que se ajusta al empleado en los UNIX 
tradicionales. 
Un archivo ordinario tendrá las propiedades siguientes: 
• El identificador de dispositivo del dispositivo que alberga al sistema de archivos. 
• El número de inodo que identifica al archivo dentro del sistema de archivos. 
• La longitud del archivo en bytes. 
• El identificador de usuario del creador o un propietario del archivo con derechos diferenciados. 
• El identificador de grupo de un grupo de usuarios con derechos diferenciados. 
• Permisos de acceso: capacidad de leer, escribir, y ejecutar el archivo por parte del propietario, 
del grupo y de otros usuarios. 
• Las marcas de tiempo con las fechas de última modificación (mtime), acceso (atime) y de 
alteración del propio inodo (ctime). 
• El número de enlaces, esto es, el número de nombres (entradas de directorio) asociados con 
este inodo. El número de enlaces se emplea por el sistema operativo para eliminar el archivo del 
sistema de ficheros, tanto el inodo como el contenido, cuando se han borrado todos los enlaces 
y el contador queda a cero. 
• La estructura de punteros, para direccionar hacia los bloques de datos (contenido) del archivo. 
Daemon 
Es una expresión que se refiere a un tipo especial de proceso informático no interactivo, es decir, que se 
ejecuta en segundo plano (background) en vez de ser controlado directamente por el usuario. 
5.3. Gestor de arranque (Linux Boot Loaders) 
Su función es gestionar varios sistemas operativos en un mismo ordenador, y poder seleccionar cual 
arrancar al encender el ordenador, dependiendo de nuestras necesidades en ese momento. 
Es un programa pequeño, almacenado en la tabla de particiones MBR o GUID, necesario e 
imprescindible para que sistema se cargue en la memoria. 
Al instalar Linux, podemos instalar diversos cargadores de arranque. Vamos a ver 4 de los más 
destacados: GNU GRUB, LILO, BURG y Syslinux. 

<!-- Page 63 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
63 
GNU GRUB 
Es el más utilizado, está basado en el Grub original (Grand Unified Bootloader) creado por Stefan Eirch 
Broleyn. Pero con nuevas características, mejoras y correcciones de errores respecto al GRUB original. 
El nombre GRUB se cambió GRUB Legacy, y ya no se sigue desarrollando, ya que ha sido sustituido por 
GRUB2, pero se sigue usando para arrancar sistemas antiguos. 
 
 
 
 
+ Info 
Un sistema heredado (o sistema legacy) es un sistema informático 
(equipos informáticos o aplicaciones) que ha quedado anticuado 
pero que sigue siendo utilizado por el usuario (generalmente, una 
organización o empresa) y no se quiere o no se puede reemplazar 
o actualizar de forma sencilla. 
 
LILO 
Es menos popular que GRUB, aunque es simple y potente, actualmente está desfasado y en desuso. 
Mientras se carga, la palabra «LILO» se visualiza en pantalla cada letra aparece antes o después de que 
un evento en particular que se haya producido. El desarrollo de LILO se paró en el año 2015 con la 
versión 24.2. 
BURG 
Surge de GNU GRUB, pero, aunque su programación interna es totalmente basada en la segunda 
versión de GRUB, fue reescrita completamente por el equipo de desarrollo, pero imitando la 
configuración exacta de GRUB, de esta forma, su configuración es exactamente idéntica. Es usado 
principalmente en sistemas operativos GNU Linux. 
Aunque tiene algunas de las características principales de GRUB, ofrece nuevas características 
excelentes, soporta un menú de arranque de texto y modo gráfico muy configurable y también un 
nuevo formato de objeto para soportar múltiples plataformas (Windows, Mac OS, FreeBSD, etc.). 
La idea de BURG es proveer un cargador de arranque con aspecto visual, capaz de mostrar fondos de 
escritorio, iconos, y animaciones en lugar de solo texto como GRUB. 
Existen miles de temas y diseños creados por la comunidad, y que se pueden descargar desde diversas 
páginas web. 

<!-- Page 64 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
64 
SYSLINUX 
Sólo accede a los archivos de su propia partición, no puede realizar el inicio de varios sistemas de 
archivos. 
Permite el arranque desde red, CD-ROM etc. También soporta sistemas de archivos de ext2, ext3, ext4 
para Linux, y archivos como FAT para MS-DOS. 
5.4. Distribuciones 
Una distribución o distro Linux es una recopilación que contiene el núcleo de Linux y una serie de 
paquetes de software (normalmente software libre) para satisfacer las necesidades de un determinado 
grupo de usuarios. 
Existen distribuciones de uso doméstico, servidores, jugadores, investigación, empresas, niños, 
educación, etc. 
Además del núcleo, se suele incluir las bibliotecas y herramientas del proyecto GNU/Linux y el sistema 
de ventanas X Windows System. Si incluye paquetes de código del proyecto GNU, se denomina 
distribución GNU/Linux. 
 
 
 
 
+ Info 
GNU es un sistema operativo de software libre. 
El sistema operativo GNU contiene el kernel de Linux, paquetes de 
GNU (programas publicados específicamente por el proyecto GNU) 
y software libre publicado por terceros. 
 
 
A continuación, vamos a ver algunas de las más importantes: 
• UBUNTU. 
• Posiblemente sea la mejor en términos generales, y puede que la más usada en los últimos 
años. 
• Basado en la arquitectura de Debian, pero con un enfoque más actualizado y user-friendly. 
• Tiene soporte tanto de la comunidad como profesional (Canonical). 

<!-- Page 65 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
65 
• Muchas distribuciones están basadas en Ubuntu (Lubuntu, Xubuntu, Mint, PepperMint…). 
• Escritorio GNome desde versión 18.04. Anteriormente usaba Unity. 
• Actualmente usa GNOME 46, con la versión 24.04 LTS con mejoras en rendimiento y apps 
modernas. 
• TRISQUEL 11.0 
• Con nombre en clave Aramo, está basada en Ubuntu 22.04 LTS. 
• Escritorio MATE 1.26 (modo clásico y ligero, alternativo a GNOME). 
• Kernel Linux-libre 6.6 (sin blobs propietarios, con soporte para hardware moderno). 
• Disponible en formato ISO/USB, con soporte para más de 50 idiomas y herramientas libres 
preinstaladas (Abrowser, Gnumeric). 
• Enfoque en privacidad y software 100% libre (elimina firmware no libre). 
• MINT. 
• Para muchos la mejor distribución actualmente. Posiblemente la más completa. 
• Basada en Ubuntu LTS y compatible con sus repositorios. Versión LMDE disponible (basada 
en Debian). 
• Estable y con buena experiencia de usuario. 
• La instalación de software es muy sencilla. 
• Escritorio Cinnamon (antes pesado, ahora optimizado. Estilo similar a Windows 10/11). 
• DEBIAN. 
• El más estable y confiable. Base de Ubuntu, Mint y muchas otras distribuciones. 
• Soporte comunitario excepcional. Versiones probadas a fondo antes de lanzarse. 
• Cuenta con más de 60,000 paquetes gratuitos (uno de los ecosistemas más grandes). 
• Gran cantidad de escritorios disponibles(GNOME, KDE Plasma, Xfce, LXQt, MATE, 
Cinnamon, etc). 
• ARCH. 
• Distribución desarrollada de forma independiente. 
• Dirigida a usuarios avanzados. 

<!-- Page 66 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
66 
• Rolling Release: Siempre actualizado (sin versiones fijas). 
• Pacman. Gestor de paquetes de desarrollo propio (ultrarrápido y eficiente). 
• El Sistema de Construcción de Arch (Arch Build System, ABS) facilita la creación de nuevos 
paquetes, modificarlos y compartirlos a través de los repositorios "Arch User Repositories", 
hay más de 85.000 paquetes comunitarios. 
• RED HAT (Red Hat Enterprise Linux). 
En la versión 8.1, se agregan herramientas del desarrollador nuevas, certificaciones de seguridad 
adicionales y más funciones de automatización. 
• Mejora la lucha contra las intrusiones. Incluye Red Hat Insights, un servicio de análisis 
predictivo de TI que identifica posibles problemas antes de que realmente ocurran. 
• Simplifica la complejidad con la gestión integrada. Combina Red Hat Enterprise Linux y Red 
Hat Smart Management para controlar los entornos operativos estándares (en instalaciones 
y nubes). 
• Implementa contenedores en sus S.O. nativos. Para desarrollar aplicaciones con mayor 
rapidez, ejecute Red Hat OpenShift. Puede diseñar, gestionar y compartir los contenedores 
utilizando las herramientas open source que le permiten adaptar los sistemas junto con 
otras herramientas compatibles con los estándares de la Open Container Initiative. 
• MANJARO. 
• Arch Linux simplificado. 
• Ideal para principiantes. Fácil de instalar y usar. 
• Apariencia similar a Windows. 
• Utiliza los repositorios "Arch User Repositories". 
• FEDORA. 
• La distribución líder para desarrolladores y tecnología de vanguardia. 
• Tiene actualizaciones regulares. 
• Buena estabilidad y seguridad. 
• Desarrollada por la comunidad que apoya al proyecto Fedora (propiedad de Red Hat). 
• Enfocado a la innovación e integración de nuevas tecnologías. 
• Distribuye variantes (Fedora Spins) enfocado a distintos campos (juegos, diseño, 
computación científica, etc.). 

<!-- Page 67 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
67 
• OPENSUSE: en enero de 2004, la compañía multinacional estadounidense Novell compro SuSE 
LINUX. En 2005, en la LinuxWorld, Novell, siguiendo los pasos de RedHat Inc., anunció la 
liberación de la distribución SuSE Linux para que la comunidad fuera la encargada del desarrollo 
de esta distribución, pasando a llamarse openSUSE. 
• Programa comunitario patrocinado por Novell. 
• Es un sistema operativo muy versatil, pero su uso principal es entornos de servidor debido a 
su estabilidad en entornos de producción. 
• Herramienta AppArmor para garantizar una mayor seguridad. 
• YaST. Centro de administración para configuraciones del sistema, instalaciones, 
desinstalaciones y actualizaciones con un solo clic. 
• Antes se usaba Xen para la virtulización, ahora se recomienda KVM. 
• Múltiples escritorios (por defecto KDE Plasma o GNOME). 
• CENTOS. 
• Es una reconstrucción de Red Hat Enterprise Linux 100% compatible. 
• Estable, pero ahora con un modelo "rolling release" en CentOS Stream. 
• Orientado a servidores. 
• Entorno empresarial y profesional. 
• Sitios como Facebook, Twitter y Google utilizan distribuciones de este tipo, pero con el 
cambio hacia CentOS Stream en 2020, que ahora actúa como una versión más dinámica 
entre las versiones de RHEL, algunas organizaciones han migrado a alternativas como 
Rocky Linux y AlmaLinux para mantener una estabilidad similar a la de las versiones 
anteriores de CentOS. 
A continuación vamos a indicar algunas distribuciones que consumen pocos recursos y por tanto son 
adecuadas para equipos antiguos o poco potentes y también para instalar en máquinas virtuales y poder 
utilizar un sistema Linux en un ordenador con Windows instalado. 
• Tiny Core (http://tinycorelinux.net/): 
Al ser muy ligera resulta un sistema muy minimalista, casi un Linux básico sin apenas 
aplicaciones preinstaladas. 
• Linux lite (https://www.linuxliteos.com/): 
Basado en Ubuntu LTS incluye herramientas con la instalación listas para usarse. Con el entorno 
de escritorio XFCE, que recuerda a Windows XP. 

<!-- Page 68 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
68 
• Bodhi Linux (https://www.bodhilinux.com/): 
Basada en Ubuntu, dispone de muchas aplicaciones libres con el acceso a los repositorios de 
Ubuntu. Incluye el escritorio Moksha el cual permite añadir efectos Compiz, pero no dispone de 
compositor de ventanas. 
• Puppy Linux (http://puppylinux.com/): 
Ocupa tan solo unos 300 megas en nuestro disco, a pesar de que incluye bastantes paquetes y 
aplicaciones para utilizar tras la instalación. El manejo es muy sencillo. 
• Peppermint OS (https://peppermintos.com/): 
Está basado en Lubuntu, por lo que se puede acceder a sus repositorios, y, además, se trata de 
una combinación con un sistema basado en la nube con aplicaciones comunes de escritorio. 
• Ubuntu Budgie (https://ubuntubudgie.org/): 
Utiliza recursos muy limitados y es una distribución que recuerda a GNOME. 
• Lubuntu (https://lubuntu.net/): 
Se basa en Ubuntu, pero más ligera, cambiando el escritorio y algunas aplicaciones 
preinstaladas. 
• Xubuntu (https://xubuntu.org/): 
También basada en Ubuntu, es mantenido por una gran comunidad de usuarios, se utiliza el 
entorno de escritorio XFCE y lleva aplicaciones preinstaladas como por ejemplo reproductor 
multimedia para música, vídeos y fotografías, navegador web, cliente de correo electrónico, 
procesador de textos, hoja de cálculo. También se pueden instalar otras desde el repositorio de 
Ubuntu. 
• LXLE (https://www.lxle.net/): 
Basadas en Lubuntu, por tanto, también es posible acceder al repositorio de aplicaciones de 
Ubuntu. Dispone de aplicaciones reinstaladas como LibreOffice y GIM y utiliza el entorno de 
escritorio LXDE. 
• Antix (https://antixlinux.com/): 
Para usar con equipos con muy pocos recursos ya que requiere un mínimo de 128MB de RAM, 
perfecto también para usar en máquinas virtuales. Dispone de diversas utilidades como 
administrador de archivos, recuperador de archivos eliminados, suite de ofimática gratuita, 
navegador web, gestor de control parental. Permite instalar aplicaciones desde los repositorios 
Linux y automatizar las copias de seguridad. 

<!-- Page 69 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
69 
• Point Linux (http://pointlinux.org/): 
Basada en Debian. La versión sencilla, incluye herramientas y aplicaciones que permiten usar el 
sistema tras su instalación. La versión completa incluye Mozilla Firefox, ThunderBird, 
LibreOffice, VLC Media Player, códecs multimedia etc. 
• SliTaz (http://www.slitaz.org/es/): 
Es una distro en formato Live ISO (una copia exacta en una unidadextraible o CD), que ocupa 
100 megas se instala, y dispone de paquetes y aplicaciones para usar el equipo tras su 
instalación, pudiendo añadir más. 
• SparkyLinux (https://sparkylinux.org/download/): 
Es de origen polaco basada en Debian (en la versión testing de Debian). Permite elegir entre 
diferentes entornos de escritorio y gestores de ventanas. 
• Porteus (http://www.porteus.org/): 
Además de poder instalarla en disco duro, permite su uso como un CD Live (arrancar desde 
unidad de memoria o CD). Ocupa solo 300MB, es compatible con arquitecturas de 32 Bits y 64 
Bits y está disponible en diferentes idiomas. 
• Slax (https://www.slax.org/): 
Está basada en Debian, como requisito necesita 256 MB de memoria RAM y ocupa 210 MB. 
Ofrece dos versiones, para equipos con arquitectura de 32 bits y para 64 bits.  
• Dawn Small Linux (http://damnsmalllinux.org/): 
Funciona con tan solo 16 MB de RAM, y su interfaz es JWM. 
• Q4OS (https://q4os.org/index.html): 
Basada en Debian y su interfaz es una versión 3 de KDE (Trinity DE). Los requisitos son tan solo 
Pentium de 300 MHz, 128 MB de memoria RAM y disco duro de 3 GB). 
• Rocky Linux: 
Es una de las mejores distribuciones para VPS (servidor privado virtual), muy estable, y destaca 
por su compatibilidad total con RHEL, (Red Hat Enterprise Linux), por tanto, compatible con la 
gran parte del software de Red Hat. 
Muchos lo consideran el sustituto de CentOS, ya que es utilizable por empresas y 
organizaciones, disponiendo de una migración sencilla entre equipos y segura, mediante la 
ejecución de un script que hace que se instalen los paquetes de forma automática. Este script 
solo funciona en sistemas CentOS Stream, CentOS Linux, Oracle Linux, Alma Linex y Red Hat. 
 

<!-- Page 70 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
70 
 
 
 
Refuerzo 
Estas distribuciones son las más importantes, pero existen muchas 
más que te pueden resultar muy interesantes. 
Aunque no es necesario, puedes investigar por internet, para 
buscar alguna que se adapte a tus necesidades. 
 
5.5. Entornos de escritorio 
Un entorno de escritorio o GUI (Grafical User Interface o Interfaz Gráfica de Usuario) es un conjunto de 
productos software que ofrecen al usuario una interacción amigable y cómoda con el sistema operativo. 
Linux cuenta con muchos de ellos. Cada distribución puede llevar uno por defecto, pero, al ser 
personalizables, podemos instalar otro escritorio. 
A continuación, vamos a ver algunos de los mejores entornos de escritorio a fecha de edición de este 
libro. 
• KDE Plasma. 
• Realizado por la comunidad KDE. 
• Uno de los más personalizables. 
• Dolphin es el administrador de archivos predeterminado. 
• Se utiliza en OpenSUSE y Kubuntu. 
• GNOME. 
• Diseñado para proporcionar simplicidad, facilidad de acceso y confiabilidad a los usuarios. 
• Está basado en el kit de herramientas GTK+. 
• Se utiliza en Fedora, Ubuntu GNOME, Debian y Arch Linux. 
• CINNAMON. 
• Derivado de GNOME 2. 
• Fácil transición desde Windows. 
• Muchos efectos visuales. 
• Se utiliza en Linux Mint. 

<!-- Page 71 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
71 
• MATE. 
• Es una extensión de GNOME 2. 
• Es más liviano. 
• Xfce. 
• Muy liviano. No tiene animaciones ni efectos visuales. 
5.6. Directorios y sistemas de archivos 
En Linux y Unix todo es un fichero. Los directorios son ficheros, los ficheros son ficheros, y los 
dispositivos (como discos duros o pendrive) son ficheros. También los puertos de comunicación y las 
consolas o terminales son dispositivos asociados a un archivo. 
Los sistemas de ficheros de Linux se organizan en una estructura jerárquica, de tipo árbol. 
El nivel más alto del sistema de ficheros es / o directorio raíz. 
Por debajo del directorio raíz (/) hay un importante grupo de directorios común a la mayoría de las 
distribuciones de GNU/Linux. 
A continuación, te mostramos una lista de los directorios que aparecen normalmente bajo el directorio 
raíz (/): 
• /bin: Aplicaciones binarias importantes. Aquí se almacenan los ficheros ejecutables y algunas 
utilidades del sistema operativo. 
• /boot: Ficheros de configuración del arranque, núcleos y otros ficheros necesarios para el 
arranque (boot) del equipo. 
• /dev: Ficheros de dispositivo. 
• /etc: Se almacenan los archivos de configuración, a nivel del sistema operativo y también de las 
aplicaciones instaladas a posteriori. 
• /home: Directorios personales (home) para los diferentes usuarios. 
• /initrd: Usado cuando se crea un proceso de arranque initrd personalizado. 
• /lib: Librerías del sistema (libraries). 
• /lost+found: Proporciona un sistema de "perdido+encontrado" (lost+found) para los ficheros 
que existen debajo del directorio raíz (/). 
• /media: Particiones montadas (cargadas) automáticamente en el disco duro y medios (media) 
extraíbles como CDs, cámaras digitales, etc. 

<!-- Page 72 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
72 
• /mnt: Sistemas de archivos montados manualmente en el disco duro. 
• /opt: Proporciona una ubicación donde instalar aplicaciones opcionales (de terceros). 
• /proc: Directorio dinámico especial que mantiene información sobre el estado del sistema, 
incluyendo los procesos actualmente en ejecución. 
• /root: Directorio personal del usuario root (superusuario); también llamado "barra-root". 
• /sbin: Binarios importantes del sistema. 
• /srv: Puede contener archivos que se sirven a otros sistemas. 
• /sys: Archivos del sistema (system). 
• /tmp: Archivos temporales. 
• /usr: Aplicaciones y archivos a los que puede acceder la mayoría de los usuarios. 
• /var: Archivos variables como archivos de registros y bases de datos. 
5.7. Permisos 
Todos los archivos de un sistema Linux tienen permisos que permiten o impiden a otros verlos, 
modificarlos o ejecutarlos. 
El superusuario "root" tiene acceso a cualquier archivo del sistema. 
Cada archivo es asociado a un propietario y un grupo. 
Cada archivo está asegurado por las tres capas de permisos siguientes, en orden de importancia: 
• Usuario. Propietario del archivo. 
• Grupo. Usuarios dentro del grupo asociado al archivo. 
• Otros. Resto de usuarios. 
Hay 3 tipos de permisos: 
• Lectura. 
• Los archivos pueden ser visualizados/abiertos. 
• El contenido del directorio se puede visualizar. 

<!-- Page 73 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
73 
• Escritura. 
• Los archivos se pueden modificar o eliminar. 
• El contenido del directorio se puede modificar (lo que incluye crear, renombrar y eliminar 
archivos y subdirectorios dentro de él). 
• Ejecución. 
• Los archivos ejecutables se pueden arrancar como un programa. 
• Se puede entrar en los directorios. 
Cada capa podrá tener uno o más permisos (o no tener ninguno). 
Sticky bit 
Este permiso de acceso puede ser asignado a ficheros y directorios en sistemas UNIX y similares. 
Asignándolo a un directorio, significa que los elementos que hay en ese directorio solo pueden ser 
renombrados o borrados por su propietario o bien por root. 
El resto de usuarios, aunque tengan permisos de lectura y escritura, los podrán leer y modificar, pero no 
borrar. 
Modificar permisos 
Desde el Shell, podemos ejecutar la orden chmod para ver y modificar los permisos de un fichero 
(aunque en la actualidad, la mayoría de los entornos de escritorio permiten hacerlo a través de 
ventanas). 
Sintaxis: chmod[modificadores]permisos fichero/directorio 
Los permisos se pueden dar con un número octal o con letras. 
Cuando utilizamos un número octal, los valores son de este modo: 
• El primer dígito corresponde a los permisos del propietario(dueño) del fichero. 
• El segundo dígito corresponde a los usuarios del grupo. 
• El tercer dígito corresponde al resto de usuarios. 

<!-- Page 74 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
74 
También es posible añadir y quitar permisos utilizando las letras. La siguiente tabla muestra los 
permisos: 
Octal 
Binario 
Letras 
Lectura(r) 
Escritura(w) 
Ejecución(x) 
0 
000 
 
No 
No 
No 
1 
001 
x 
No 
No 
Si 
2 
010 
w 
No 
Si 
No 
3 
011 
wx 
No 
Si 
Si 
4 
100 
r 
Si 
No 
No 
5 
101 
rx 
Si 
No 
Si 
6 
110 
rw 
Si 
Si 
No 
7 
111 
rwx 
Si 
Si 
Si 
 
 
 
 
Ejemplo 
Ejemplo con números: 
chmod 720 
• El 7 indica permisos de lectura, escritura y ejecución para el 
usuario. 
• El 2 indica permiso de escritura para los usuarios del grupo. 
• El 0 indica que el resto no tiene permisos. 
Ejemplo con letras: 
chmod u+r o-w 
• u+r indica que añadimos permiso de lectura al usuario. 
• o-w indica que quitamos los permisos de escritura al resto 
(los que no son ni el usuario ni usuarios del grupo). 
 

<!-- Page 75 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
75 
5.8. Principales comandos 
Existen muchos comandos en Linux, con diferentes opciones, que pueden variar dependiendo de la 
versión que estemos utilizando. 
Vamos a ver algunos de los más principales. Linux nos proporciona un manual de cada comando y sus 
opciones: 
Podemos ver el manual completo de cualquier comando escribiendo: man nombredelcomando. 
Ahora vas a estudiar los principales Comandos: 
5.8.1. Gestión y control de Linux 
Son comandos muy útiles, para controlar tareas de administración, gestión o soporte para conocer en 
detalle múltiples parámetros tanto del sistema como de procesos, usuarios, servicios… 
5.8.1.1. Which 
Se utiliza para conocer la ruta de un comando. 
Si necesitamos saber en qué directorio de nuestro PATH se encuentra un comando (programa), en vez 
de usar find o locate, que nos tardarán más, podemos usar: which <programa> 
PATH es una variable de entorno que contiene los directorios donde el shell (intérprete de comandos) 
buscará los programas (y comandos) cuando los queramos ejecutar. 
5.8.1.2. Modprobe 
Para añadir o eliminar un módulo cargable del kernel. 
Es un programa de Linux escrito originalmente por Rusty Russell y utilizado para añadir un módulo 
cargable del kernel (LKM) al kernel de Linux o para eliminarlo. 
Por lo general, es utilizado indirectamente: udev se basa en modprobe para cargar controladores de 
hardware detectado automáticamente. 
A partir de 2014 modprobe se distribuye como parte del paquete de software "kmod". 
Si se llama sin parámetros, el programa agrega / inserta / instala por defecto el módulo designado en el 
kernel. Normalmente se requieren privilegios de superusuario para realizar estos cambios. 

<!-- Page 76 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
76 
Ofrece funciones muy completas: 
• La capacidad de tomar decisiones más intuitivas sobre qué módulos cargar. 
• Un conocimiento de las dependencias de los módulos, de modo que cuando se le solicita que 
cargue un módulo, modprobe agrega otros módulos que se requerían previamente. 
• La resolución de las recursivas dependencias de los módulos que sean necesarios. 
5.8.1.3. Paquete e2fsprogs 
Es un conjunto de utilidades para mantenimiento de los sistemas de ficheros ext2, ext3 y ext4. Debido a 
que estos son generalmente los sistemas de archivos por defecto en las distribuciones Linux, 
comúnmente se considera al paquete e2fsprogs software esencial. 
Este paquete incluye: 
• e2fsck: un programa fsck que busca y corrige inconsistencias. 
Se debe de usar e2fsck exclusivamente en particiones desmontadas, ya que esta herramienta 
opera a bajo nivel accediendo directamente al dispositivo de bloque (/dev/sdXN) sin necesidad 
de montaje. El sistema operativo reconoce las particiones como dispositivos de bloque mediante 
la tabla de particiones, aunque solo puede gestionar archivos cuando están montadas. Si se 
ejecuta e2fsck sobre una partición montada, se puede interferir con las operaciones de 
lectura/escritura que el kernel realiza constantemente (actualizaciones de metadatos, 
journaling, etc.), causando posibles inconsistencias o daños permanentes en el sistema de 
archivos. Regla de oro: desmontar antes de verificar o reparar. 
• mke2fs: usado para crear sistemas de archivos ext2, ext3, y ext4. 
• resize2fs: que puede expandir y contraer sistemas de archivos ext2, ext3, y ext4. 
• tune2fs: usado para modificar los parámetros en el sistema de archivos. 
• dumpe2fs: que muestra la información de bloques y superbloques. 
• debugfs: usado para visualizar o modificar estructuras internas del sistema de archivos 
manualmente. 
5.8.1.4. Who 
Si ejecutamos who sin ningún argumento, la consola nos mostrara la información de la cuenta, con 
nombre de usuario, terminal del usuario, hora de inicio de sesión y del host en el cual se ha iniciado 
sesión. 

<!-- Page 77 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
77 
Podemos usar las siguientes opciones: 
• who-H 
Imprimir el encabezado de las columnas generadas. 
• who –q 
Ver nombres y usuarios conectados; mostrar en la pantalla los nombres de inicio de sesión y la 
cantidad total de usuarios conectados. 
• who –m 
Desplegar nombre de host y usuario asociado con stdin. 
• who -b – 
Permite ver el último arranque del sistema operativo. 
Con -b muestra la hora del último arranque del sistema seleccionado, y si añadimos, la opción –
u, muestra los usuarios conectados. 
• who –r 
Nos permite verificar el nivel de ejecución actual. 
• who –a 
Genera información general, imprime el resultado predeterminado combinado con la 
información de algunas de las opciones anteriores. 
5.8.1.5. Id 
El comando id en Linux es una herramienta útil para obtener información sobre la identidad de un 
usuario o grupo en el sistema. 
Id sin opciones mostrará el UID (identificación de usuario) y el GID (Identificación de grupo) y los 
grupos secundarios a los que pertenece el usuario actual. 
• id <nombre_usuario>: si acompañamos al id de un nombre de usuario obtendremos la 
información mencionada del usuario al que hacemos referencia. 
• id -u <nombre_usuario>: mostrará solo el UID del usuario especificado. 
• id -g <nombre_usuario>: mostrará solo el GID del usuario referenciado. 
• id -G <nombre_usuario>: mostrará los grupos a los que pertenecce el usuario referenciado. 

<!-- Page 78 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
78 
5.8.1.6. Uname 
El comando uname es una utilidad de línea de comandos en Linux que permite obtener información 
sobre el sistema operativo y el núcleo. Es muy útil para conocer detalles sobre el entorno del sistema en 
el que estás trabajando. 
uname significa Unix Name. Este comando muestra información básica del sistema, como el nombre del 
kernel, la arquitectura del hardware y la versión del sistema operativo. Es especialmente útil para tareas 
de diagnóstico y desarrollo. 
Sintaxis 
uname [OPCIÓN] 
Por defecto, si se ejecuta uname sin ninguna opción, el sistema dará la opción -s por implícita y 
mostrará únicamente el nombre del kernel. 
• -a Muestra toda la información disponible: kernel, hostname, arquitectura, etc. 
• -s Muestra solo el nombre del kernel (por ejemplo, Linux). 
• -n Muestra el nombre del host del sistema (hostname). 
• -r Muestra la versión del kernel en ejecución. 
• -v Muestra la versión del kernel (incluyendo fecha y hora de compilación). 
• -m Muestra la arquitectura del hardware de la máquina (por ejemplo, x86_64). 
• -p Muestra el tipo de procesador (a veces puede mostrar unknown si no está disponible). 
• -i Muestra la plataforma del hardware (similar a -m). 
• -o Muestra el sistema operativo (normalmente GNU/Linux). 
• --help Muestra un resumen de las opciones disponibles. 
• --version Muestra la versión de uname. 
5.8.2. Comandos para ficheros y directorios 
Es imprescindible, para desenvolverse en el entorno, conocer los comandos de manipulación de ficheros 
y directorios que el sistema operativo. 

<!-- Page 79 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
79 
5.8.2.1. pwd 
(De las siglas en inglés print working directory, cuya traducción sería imprimir directorio de trabajo). 
Sirve para mostrar la ruta actual. 
El comando pwd en Linux te devuelve la ruta en la que estas situado, se suele utilizar para saber en qué 
parte de la estructura de directorios te encuentras. 
5.8.2.2. touch 
Crear archivos. Sin ninguna opción crea un nuevo archivo vacío. 
Sintaxis: touch [ruta/archivo.txt] 
Si el archivo existe, el comando actualizará el tiempo de acceso y de modificación a la hora actual sin 
cambiar su contenido. 
Opciones: 
• -a, cambia solo el tiempo de acceso al archivo (atime), dejando el de modificación (mtime) 
intacto. 
• -m, cambia el mtime dejando el atime intacto. 
• -t HHMMyy.ss: Permite establecer una fecha y hora específicas en lugar de la hora actua. 
• -r [archivo-referencia] [archivo-destino], cambiará todos los timestamps del archivo destino 
para poner los mismos que el de referencia. 
5.8.2.3. WC 
WC (word count) es un comando utilizado en el sistema operativo Unix que permite realizar diferentes 
conteos desde la entrada estándar, ya sea de palabras, caracteres o saltos de líneas. Se combina con el 
comando cat. 
El programa lee la entrada estándar o una lista concatenada y genera una o más de las estadísticas 
siguientes: conteo de líneas, conteo de palabras, y conteo de bytes. Si se le pasa como parámetro una 
lista de archivos, muestra estadísticas de cada archivo individual y luego las estadísticas generales. 
• wc -l <fichero> número de líneas que tiene el fichero. 
• wc -c <fichero> número de bytes. 

<!-- Page 80 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
80 
• wc -m <fichero> imprime el número de caracteres. 
• wc -L <fichero> imprime la longitud de la línea más larga. 
• wc -w <fichero> imprime el número de palabras. 
5.8.2.4. cat 
Se usa para concatenar y mostrar archivos. La Single Unix Specification, establece que cat, escribirá a la 
salida estándar el contenido de cada uno de los archivos dados como argumentos, en el mismo orden en 
el que fueron dados, y obliga el uso de una opción, -u, con la que cada byte se imprime en cuanto se lee. 
Si introducimos el símbolo menos "-" como nombre de archivo, cat leerá de la entrada estándar cuando 
llegue a él. Si no se especifica ningún archivo, cat leerá solo de la entrada estándar. Cuando hablamos de 
entrada estándar nos referimos a lo introducido en el prompt o intérprete de comandos del sistema 
operativo. 
5.8.2.5. less 
Mostrar contenido de un archivo. 
El comando less en Linux, nos muestra el contenido de un archivo, (en ocasiones es demasiada 
información como para que se pueda leer en la pantalla del monitor), less nos lo muestra de forma 
interactiva, pudiendo navegar en él; avanzar o retroceder en el texto con las flechas de cursor del 
teclado. También nos permite realizar búsquedas. 
Sintaxis: Less[opciones]nombre_de_archivo 
Desplazarnos por el archivo: si abrimos un archivo cuyo contenido no cabe en una página, por ser 
demasiado grande aparecerá ":" 
Opciones del comando less: 
• Avanzar o retroceder una sola línea: utilizamos las teclas flecha arriba o flecha abajo. 
• Avanzar a la página siguiente: pulsamos la tecla (f) o la barra espaciadora. También podemos 
desplazarnos hacia abajo un número determinado de líneas, hay que especificarlas: escribimos el 
número de líneas seguido de la tecla espacio o (f). 
• Volver a la página anterior: pulsamos la tecla (b), o también podemos especificar las líneas hacia 
arriba: escribimos el número de líneas seguido de la tecla (b). 

<!-- Page 81 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
81 
• Buscar un patrón: escribimos la barra diagonal (/ patrón). Pulsamos la tecla «Enter» para 
comenzar. Si queremos que busque hacía atrás (? patrón). 
• Repetir ultima búsqueda: (n). 
• Repetir ultima búsqueda en sentido inverso: (N). 
• Ir a la primera línea del archivo: (g). 
• Ir a la línea N-th del archivo: ([número de línea]+g). 
• Ir a la última línea del archivo: (G). 
• Avanzar N líneas ([número de líneas]+j). 
• Retroceder N líneas ([número de líneas]+k) 
• Al llegar al final del archivo aparecerá la cadena (END) en la parte inferior de la pantalla. Para 
salir de less y volver a la línea de comandos pulsamos la tecla (q). 
5.8.2.6. more 
El comando "more" en Linux también permite mostrar el contenido de un archivo de forma interactiva, 
similar a "less", pero con algunas diferencias, solo se permite la navegación hacia adelante (no se puede 
retroceder): 
more [opciones] nombre_de_archivo 
• Visualización por páginas: "more" muestra el contenido del archivo una página a la vez. 
• Navegación: Puede avanzar o retroceder una página con la barra espaciadora o la tecla "Enter". 
• Búsqueda: No tiene una función de búsqueda integrada como "less". 
• Salida: Al final del archivo, "more" indica "--More--" y espera a que presione una tecla para 
continuar o "q" para salir. 
Opciones más comunes: 
• -h: Muestra una breve ayuda (desde el shell). 
• -d: Muestra ayuda a pie de texto 

<!-- Page 82 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
82 
• -l: Cuando more encuentra un ^L en pantalla, normalmente pausa la visualización, pero con -l 
ignora esa pausa y sigue mostrando el contenido continuamente. 
• -f: fuerza a mostrar líneas completas sin dividirlas, pero solo se nota cuando las líneas son más 
anchas que la terminal. 
• -[n]: Muestra el texto desde el principio y las líneas especificadas por "n" en cada página. 
• +[n]: Comienza la visualización desde la línea "n" 
5.8.2.7. tac 
Mostrar ficheros. Acrónimo de "concatenate", pero al revés cat -> tac. 
Tac te muestra el contenido de un fichero en orden contrario. Muestra un archivo línea por línea, pero 
en orden inverso (la última línea primero y la primera última). Te permite concatenar ficheros y 
mostrarlos a la inversa. 
5.8.2.8. du 
Gestión de espacio en disco. 
du (abreviatura de disk usage, uso de disco) es un comando estándar de los sistemas operativos de la 
familia Unix. 
Se usa para estimar el uso de espacio en disco duro de un archivo, un directorio en particular o de 
archivos en un sistema de archivos. 
Muestra el espacio del archivo asignado a cada archivo y directorio contenido en el directorio actual. 
Los enlaces se muestran como el tamaño del archivo de enlace, no lo que está vinculado a; se muestra el 
tamaño del contenido de directorios, como se esperaba. 
Opciones más comunes: 
• -c lista cada archivo/directorio con su ruta y tamaño, más un total general al final. 
• -a muestra resultados listando ficheros, no sólo directorios. 
• -h muestra el peso de forma legible, le añade el formato (K, M, G, T). 
• -s muestra solamente el peso total por cada directorio. 
• -x se salta los directorios de otros sistemas de ficheros (fruto de otros puntos de montaje). 
 

<!-- Page 83 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
83 
 
 
 
Ejemplo 
Ejemplos: 
• Uso del disco para un directorio y sus subdirectorios: du 
/home 
• Uso del disco con tamaños de archivos y directorios en 
formato legible para humanos: 
du -ah /home 
• Tamaño total de un directorio: du -s /home. 
 
5.8.2.9. vi 
Es un comando para editor de texto. 
vi (Visual) fue originalmente escrito por Bill Joy en 1976. Es un programa editor de texto, pero a 
diferencia de un procesador de texto no ofrece herramientas para determinar visualmente cómo 
quedará el documento impreso. 
Permite mover, copiar, eliminar o insertar caracteres, pero no opciones como centrado o justificación 
de párrafos. 
Con frecuencia es utilizado por programadores para escribir código fuente de software. 
El editor vi tiene dos modos de operación: 
• Modo de comandos: comandos, podemos desplazarnos dentro de un archivo y efectuar 
operaciones de edición como buscar texto, eliminar texto, modificar texto, etc. Vi suele iniciarse 
en modo de comandos. 
• Modo insertar: podemos escribir texto nuevo en el punto de inserción de un archivo, editar, 
borrar, copiar y pegar. 
Normalmente vi se inicia en modo comandos, una vez realizado un comando y escrito el testo (estamos 
en modo insertar), volvemos al modo de comandos, presionando la tecla esc (escape). 
Para desplazarse sobre el archivo se emplean las teclas j (abajo), k (arriba), h (izquierda) y l (derecha). 

<!-- Page 84 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
84 
• INSERCIÓN de texto: 
• i, antes del cursor. 
• a, después del cursor. 
• I (i mayúscula), al principio de línea. 
• A, el final de la línea. 
• o, agregar nueva línea debajo. 
• O, agregar nueva línea arriba. 
• MODIFICAR texto: 
• r, reemplazar un crácter. 
• R, reemplazar múltiples caracteres. 
• cw, cambiar palabra. 
• cc, cambiar línea completa. 
• C, cambiar desde cursor hasta el fin de línea. 
• COPIAR y PEGAR: 
• yy, copiar línea actual. 
• yw, copiar palabra. 
• y$, copiar desde cursor hasta el fin de línea. 
• y^, copiar desde cursor hasta inicio de línea. 
• 3yy, copiar 3 líneas. 
• p, pegar después del cursor. 
• P, pegar antes del cursor. 
• ELIMINAR el texto: 
• x, borrar carácter bajo el cursor. 
• X, borrar carácter antes el cursor. 
• dd, borrar línea actual. 

<!-- Page 85 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
85 
• dw, borrar palabra. 
• d$, borrar desde cursor hasta el inicio de línea. 
• d^, borrar desde cursor hasta el fin de línea. 
• 3dd, borrar 3 líneas. 
• DESHACER y REHACER: 
• u, deshacer el último cambio. 
• U, restaurar línea actual (cambios en línea actual). 
• Ctrl + r, rehacer. 
• ABRIR, GUARDAR y SALIR: 
• :w, guardar. 
• :w [archivo], guardar con otro nombre. 
• :q, salir. 
• :q!, salir sin guardar (forzar). 
• :wq o :x, guardar y salir. 
• ZZ, guardar y salir (en modo comandos). 
• :e [archivo], abrir otro archivo. 
5.8.2.10. mount, umount 
Se utilizan para montar y desmontar sistemas de archivos. 
Montar es hacer accesible el contenido de un dispositivo (disco, USB, partición) a través de un 
directorio específico en el árbol del sistema. 
• mount. 
• Monta un dispositivo de almacenamiento (por ejemplo, un disco duro) en un directorio de 
Linux. 
• Formato: mount [opciones] dispositivo directorio. 
• Sin parámetros muestra todos los sistemas montados. 

<!-- Page 86 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
86 
• Con parámetros: 
» -t [tipo], especifica el sistema de archivos (ext4, ntfs, vfat, xfs). 
» -r, monta en solo lectura. 
» -o [opciones], opciones adicionales (rw, remount, etc.) 
» -l (letra ele), muestra etiquetas. 
• Umount. 
• Desmonta un dispositivo de almacenamiento. 
• Formato: umount [opciones] directorio/dispositivo. 
 
 
 
 
Nota 
Existen muchas más opciones específicas, pero éstas cubren el 
95% de los casos de uso comunes. 
 
5.8.2.11. tar 
Tar es una herramienta de línea de comandos que se utiliza para crear y manipular archivos de 
almacenamiento en sistemas Linux y Unix. Es uno de los comandos más utilizados en Linux. 
El nombre Tar es el acrónimo de "Tape Archive" en inglés, lo que en español se traduce como 
Archivador de cinta, también indicado como archivo de cinta de grabación, por su uso original de 
unificar múltiples archivos en uno solo para simplificar el almacenamiento de archivos en cintas 
magnéticas). Para realizar el proceso inverso y obtener individualmente los archivos unificados, 
también se utiliza el mismo comando Tar. 
El comando Tar no es un comando compresor-descompresor en sí mismo, de forma nativa, es un 
comando de unificación de archivos. La funcionalidad de comprimir se añadió posteriormente por la 
popularización de la descarga de archivos de Internet, por lo que Tar ha integrado motores de 
compresión para poder reducir el tamaño final del archivo de unión. 
El comando Tar crea un archivo .tar y luego lo comprime usando una librería externa (Gzpi, bzip2, o xz) 
Extensiones obtenidas son: .tar.gz, .tar.bz2, tar.xz, etc. 
 

<!-- Page 87 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
87 
 
 
 
+ Info 
Estos archivos .TAR compresos son conocidos como tarballs y 
pueden ser fácilmente identificados por utilizar "doble" extensión 
.tar.gz. (las extensiones .gz y .tgz son formas cortas de renombrar 
.tar.gz. 
 
 
Formato: 
tar [opciones] nombrePaquete archivos 
Vamos a ver usos del comando Tar: 
• Crear un archivo .TAR sin compresión: 
tar -cvf [nombre-del-archivo-contenedor].tar /path/del/archivo/a/comprimir 
[/otros] 
Donde: 
• c: Flag o bandera que representa la acción "create" e informa al comando principal que se 
desea crear un archivo .TAR con los archivos o carpetas señalados en el comando. 
• v: Flag o bandera que representa la acción "verbose" e informa al comando principal que se 
desea mostrar todo lo que sucede en la ejecución, mostrando los archivos agregados o 
extraídos según corresponda y al mismo tiempo mostrar el progreso de la operación. 
• f: Flag o bandera que representa la acción "file" e informa al comando principal que se desea 
definir un nombre específico al archivo resultante. 
• nombre-del-archivo.tar: Corresponde al nombre del archivo .TAR a crear. Este nombre 
puede ser establecido dado a que fue ejecutado el flag o bandera " f " en la ejecución del 
comando tar. 
• /path/del/archivo/a/comprimir: Corresponde a la ruta de la carpeta o archivo que desea 
ser añadido al .TAR. 

<!-- Page 88 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
88 
• [/otros]: Al estar entre Brakes o Corchetes " [ ] " se aplica a una parte del comando que 
puede ser opcional. Corresponde a la ruta de archivos o carpetas adicionales que pueden 
ser añadidas al .TAR. 
• Crear un archivo .TAR comprimido: 
tar -czvf [nombre-del-archivo-contenedor].tar /path/del/archivo/a/comprimir 
[/otros] 
A diferencia de los descrito en el comando anterior, este comando solo incluye la siguiente 
acción: 
• z: Flag o bandera que representa la acción "compress" e informa al comando principal que 
se desea comprimir el .TAR resultante con GZip para disminuir el peso del archivo .TAR. 
• Abrir un archivo .TAR: 
tar -xvf [nombre-del-archivo-contenedor].tar 
Donde: 
• f: Flag o bandera que representa la acción "file" e informa al comando principal el nombre 
específico del archivo a descomprimir. 
• v: Flag o bandera que representa la acción "verbose" e informa al comando principal que se 
desea mostrar todo lo que sucede en la ejecución, mostrando los archivos agregados o 
extraídos según corresponda y al mismo tiempo mostrar el progreso de la operación. 
• x: Flag o bandera que representa la acción "extraer" e informa al comando principal que se 
desea extraer el contenido de un archivo .TAR. 
• z: Flag o bandera que representa la acción "descomprimir con gzip" e informa al comando 
principal que se desea descomprimir el archivo .TAR.GZ antes de extraer su contenido. 
• nombre-del-archivo.tar: Corresponde al nombre del archivo .TAR a descomprimir. Este 
nombre puede ser definido dado a que fue ejecutado el flag o bandera " f " en la ejecución 
del comando .TAR. 
 

<!-- Page 89 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
89 
 
 
 
+ Info 
En ocasiones surge la necesidad de cambiar los formatos de 
archivos .TAR, .TAR.GZ, etc. a otros que permitan su uso o 
manipulación en otros sistemas operativos. Para ello existen 
aplicaciones que permiten la conversión de estos archivos a otros 
equivalentes. Algunas de ellas son: 
• Convertio (Online). 
• Zamzar (Online). 
• Online-Convert.com (Online). 
• ArcConvert (Aplicación). 
• AnyToISO (Aplicación). 
 
 
Hacemos a continuación un repaso de las opciones del comando TAR: 
• -r: Agrega archivos a un paquete existente. 
Se utiliza para agregar o actualizar un archivo existente con archivos o directorios. 
• -u: Agrega archivos al paquete si son más recientes que los existentes. 
Como -r, pero las nuevas entradas se agregan solo si tienen una fecha de modificación más 
reciente que la entrada correspondiente en el archivo. 
• -t: Muestra el contenido de un paquete. 
Se utiliza para ver el contenido del archivo de almacenamiento. 
• -x: Extrae los archivos de un paquete. 
• -z: Comprime con gzip el paquete generado. 
• -c: crea un nuevo archivo .tar que contiene los elementos (archivos) especificados. 
• -v: Muestra los nombres de los archivos procesados, una descripción detallada del progreso de la 
compresión. 
• -w: Modo interactivo (pregunta antes de cada acción). 
• -f: nombre del archivo. Especificar el nombre del archivo de almacenamiento. 
• -j: Se utiliza para filtrar el archivo a través de bzip2. 
• -J: Se utiliza para filtrar el archivo a través de xz. 

<!-- Page 90 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
90 
Ventajas de la compresión de archivos: 
• Tiene una relación de compresión del 50%, lo que significa que comprime eficientemente. 
• Reduce drásticamente el tamaño de las carpetas y archivos comprimidos. 
• No altera las características de los archivos y directorios. Los permisos y otras particularidades 
permanecen intactos mientras se comprime. 
• Está disponible en las versiones más comunes de Linux. También se encuentra disponible en el 
firmware de Android, así como en versiones compatibles de Linux más antiguas. 
• Comprime y descomprime rápidamente. 
• Es fácil de usar. 
• Conveniencia de su uso: 
• Para transferir una gran cantidad de archivos y carpetas de un servidor a otro. 
• Para realizar copias de seguridad, en web etc. 
• Para reducir el uso de espacio en tu sistema en caso necesario (al estar comprimidos 
ocuparan menos espacio). 
 
 
 
 
Ejemplo 
Ejemplos: 
Crear un archivo .tar en Linux: 
tar -cvf sampleArchive.tar /home/sampleArchive 
Aquí /home/sampleArchive es el directorio que necesita ser 
guardado en sampleArchive.tar. (Este comando usa las opciones -
c,-v,-f ). 
Listar los ficheros contenidos en un archivo llamado 
"miejemplo.tar". 
tar -tvf miejemplo.tar 
Extraer un archivo tar.gz comprimido: 
tar -xzvf [archivo-comprimido].tar.gz 
 

<!-- Page 91 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
91 
5.8.2.12. shell 
Es el intérprete de comandos que permite al usuario interactuar con el Kernel de Linux. Los comandos 
que se ejecutan en él son para el manejo de ficheros, procesos, y más. 
Los comandos que se ejecutan en él son para el manejo de ficheros, procesos, y más. Los comandos 
Shell tienen una sintaxis más o menos común. Si quieres añadir dos opciones a un comando, no 
necesitas poner 2 guiones, es decir, si quieres añadir -a y -l puedes sustituirlo por -al. Se puede utilizar & 
al final de un comando para ejecutarlo en segundo plano. Vamos a ver algunas de las más importantes: 
Comandos para el manejo de ficheros 
• ls. 
• Muestra una lista del contenido del directorio actual. 
• Formato: ls [opciones] [archivos o ruta] 
• Opciones: 
» -l: Lista detallada. 
» -a: Ver todos los archivos (incluidos los ocultos). 
• cp. 
• Crea una copia de un archivo. 
• Formato: cp [opciones] archivoOriginal archivoDestino 
• Opciones: 
» -i: Espera confirmación antes de sobreescribir. 
» -r: Copia recursiva. Incluye subdirectorios. 
• mv. 
• Mueve o renombra archivos y directorios 
• Formato: mv [opciones] archivoOriginal archivoDestino 
• Opciones: 
» -i: Espera confirmación antes de sobreescribir. 
» -b: Crea una copia de seguridad del archivo antes de moverlo. 

<!-- Page 92 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
92 
• rm. 
• Borra un fichero. 
• Formato: rm [opciones] archivo. 
• Opciones: 
» -i: Espera confirmación antes de borrar cada archivo. 
» -r: borra los directorios y contenido de forma recursiva. 
• ln. 
• Crea enlaces entre archivos. Por defecto crea hard links 
• Formato: ln [opciones] archivoOrigen archivoDestino 
• Opciones: 
» -s: Crea un enlace simbólico. 
• cd. 
• Cambia el directorio actual. 
• Formato: cd ruta. 
• Si se escribe solo cambia al directorio home del usuario. 
• mkdir. 
• Crea un directorio nuevo. 
• Formato: mkdir ruta. 
• rmdir. 
• Solo borra directorios vacíos. 
• Formato: rmdir ruta. 
• chown. 
• Cambia el dueño de uno o más archivos. 
• Formato:  
» chown [opciones] usuario archivos (cambia el dueño) 
» chown [opciones] usuario:grupo archivos (cambia dueño y grupo) 

<!-- Page 93 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
93 
• chgrp. 
• Cambia el grupo propietario de archivos o directorios. 
• Formato: chgrp [opciones)] nombreGrupo archivos. 
• gzip. 
• Comprime un archivo. Reemplaza el fichero original con la versión comprimida y la añade la 
extensión .gz (de texto.txt a texto.txt.gz). 
• Para comprimir un grupo de ficheros se debe agrupar primero con tar y luego aplicar gzip. 
• Formato: gzip [opciones] archivo. 
• Opciones: 
» -d: Descomprime. 
5.8.2.13. Sort 
El comando sort en Linux es una herramienta de la shell diseñada para reordenar las líneas de archivos 
de texto o de cualquier entrada de datos basándose en reglas específicas (alfabéticas por defecto, 
numéricas, o por claves). 
La utilidad lee el contenido línea por línea, aplica la ordenación y solamente imprime el resultado 
reordenado en la salida estándar (como la pantalla o una tubería), sin alterar en modo alguno la 
estructura ni el contenido del archivo de entrada original. 
Sintaxis: 
$ sort [opciones] [archivo] 
Parámetros: 
• -r. 
Invertirá el orden. 
• -n. 
Toma un valor alfabético y lo interpreta como un número. 

<!-- Page 94 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
94 
• -f. 
No discriminara entre mayúsculas y minúsculas. 
• -t. 
Se utiliza como separador de campo. 
• -k. 
Busca según número de columna y lo ordena. 
5.8.2.14. fsck 
El comando fsck (File System Consistency Check) es una herramienta utilizada en Linux y UNIX para 
comprobar y reparar sistemas de archivos en discos y particiones. Se usa comúnmente para detectar y 
corregir errores en el sistema de archivos que pueden ocurrir debido a apagones inesperados, 
corrupción de datos o fallos en el disco. 
Sintaxis: 
fsck [opciones] [dispositivo] 
Parámetros: 
• -A 
Comprueba todas las particiones especificadas en /etc/fstab. 
• -C 
• Muestra una barra de progreso durante la verificación. 
• -M 
• No comprueba sistemas de archivos montados, útil en scripts. 
• -N 
Muestra lo que haría fsck sin ejecutarlo realmente. 
• -P 
Comprueba particiones en paralelo (solo con -A). 

<!-- Page 95 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
95 
• -R 
No revisa la partición raíz (/) cuando se usa con -A. 
• -T 
No muestra la cabecera de fsck. 
• -V 
• Muestra información detallada sobre la operación en curso. 
• -y 
• Responde automáticamente "sí" a todas las preguntas de corrección. 
• -n 
• Responde automáticamente "no" a todas las preguntas (modo solo lectura). 
5.8.3. Comandos de Procesos 
Son los comandos que nos permiten realizar acciones sobre los procesos, como crearlos, visualizarlos o 
cambiar su prioridad. 
5.8.3.1. fork 
Llamada al sistema fork( ) 
Se emplea para crear un nuevo proceso. Se crea una copia casi idéntica del proceso padre (se copia 
todo el código) y continúan ejecutándose en paralelo. 
El proceso padre recibe de fork( ) el pid del hijo, mientras que al proceso hijo devuelve un 0. 
El proceso hijo hereda recursos del padre (ficheros, abiertos, estado de las variables, etc.), otros no se 
heredan, como las señales pendientes (devuelve -1 en caso de error). 
5.8.3.2. ps 
Visualizar procesos. 
Formato ps[opciones] 
Este comando nos permite visualizar los procesos que tiene abiertos un usuario en nuestro sistema, y 
obtener información de ellos. 

<!-- Page 96 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
96 
El comando ps sin modificadores nos mostraría una lista con las columnas PID, TTY, TIME y CMD. 
• PID: P(rocess) ID(entificator). El ID del proceso en ejecución. 
En particular este elemento es muy importante, porque es necesario para modificar o destruir el 
proceso. 
• TTY: El terminal asociado al proceso. No todos los procesos tienen número de TTY. 
• TIME: Tiempo de CPU usado por el proceso 
• CMD: comando que inició el proceso. 
Dependiendo de las opciones o modificadores que acompañen a ps, obtendremos columnas 
importantes como pueden ser: 
• USER: nombre del usuario que ejecuta el proceso. 
• UID: U(ser) ID(entificator), indica al identificador del usuario que ejecuta el proceso. 
• PPID: es el identificador del proceso padre. 
 
 
 
 
Ejemplo 
Vamos a ver algunos ejemplos: 
• ps: muestra todos los procesos en nuestro shell activo. 
• ps –ef: muestra todos los procesos en ejecución en el 
sistema independientemente del usuario o terminal que los 
haya iniciado. 
• ps –elf: muestra los procesos con sus respectivos threads 
(hilos). 
• ps aux: muestra los procesos en estilo BSD. 
 
5.8.3.3. renice y nice 
Se utilizan para cambiar la prioridad de los procesos. 
Un procesador va alternando su uso en diferentes procesos, dando la sensación al usuario de que todos 
se ejecutan al mismo tiempo. 

<!-- Page 97 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
97 
Al indicar la prioridad le estamos diciendo al sistema que procesos van a utilizar más tiempo de 
procesador y que procesos pasan a un segundo lugar. 
La prioridad definida de cada proceso que está corriendo en el sistema se llama "nice value". 
Si iniciamos un programa y no tiene una prioridad definida por el usuario, se iniciará con prioridad 0 
(cero). 
Los valores de prioridad que podemos dar son: Mayor prioridad -20 (menos veinte) y Menor prioridad 
+19 (más diecinueve). 
• Comando renice. Modificar la prioridad de un proceso ya ejecutado. 
Si uno o más procesos usan muchos recursos del sistema, Usted puede cambiar las prioridades 
de los mismos en vez de terminarlos. Para tales tareas se puede usar el comando renice. 
Las opciones soportadas son: 
• -g Forzar que los parámetros quién sean interpretados como ID's de grupo de proceso. 
• -u Forzar que los parámetros quién sean interpretados como nombres de usuario. 
• -p Reinicia la interpretación de quién para que sea la de ID de proceso (por defecto). 
• Sintaxis: 
renice prioridad [[-p] pid …] [[-g] pgrp …] [[-u] usuario … 
• Prioridad es el valor de la prioridad, pid (use la opción -p para múltiples procesos) es el ID 
del proceso, pgrp (precedido por la opción -g si son varios) es el ID de grupo del proceso, y 
usuario (-u para más de uno) es el nombre de usuario del dueño del proceso. 
• Comando nice. Se utiliza para ejecutar un proceso con una prioridad predefinida por nosotros. 
En este caso debe especificar su comando como una opción para nice. De manera 
predeterminada nice ajusta una prioridad de 10. El rango va desde -20 (prioridad mayor) a 19 
(menor) La opción -n se usa para ajustar el valor de la prioridad. 
 
 
 
 
+ Info 
Para cambiar la prioridad de un proceso también podemos usar 
top. Usaremos la tecla r dentro de la interfaz de top para cambiar 
la prioridad de cualquier proceso. 
 

<!-- Page 98 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
98 
5.8.3.4. top 
Formato: top [opciones]. 
Muestra una lista de los procesos que se están ejecutando (y otros datos como consumo de cpu), que 
se va actualizando en tiempo real. 
5.8.3.5. kill 
Formato: kill [opciones] IDProceso 
Elimina un proceso por ID de proceso. 
Opción -9: Indica al sistema operativo que lo cierre. Más potente que un kill normal. 
5.8.3.6. killall 
Formato: killall [opciones] nombreDelProceso 
Elimina uno o más procesos cuyo nombre coincida con el indicado. 
5.8.4. Comandos de visualización y localización de archivos 
• locate. 
• Muestra el directorio donde se encuentra un archivo. 
• Es muy rápido porque busca en una base de datos y no en el sistema de archivos. 
• Formato: locate archivo. 
• Updatedb. 
• Actualiza la base de datos utilizada por el comando locate. 
• Se recomienda ejecutarlo en segundo plano y con el usuario root. 
• find. 
• Busca archivos y carpetas que contengan una expresión. Se pueden utilizar expresiones 
regulares. 
• Formato: find [ruta] [expresiónDeBúsqueda] [acción]. 

<!-- Page 99 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
99 
• grep. 
• Busca dentro de archivos, líneas que concuerden con el patrón dado. Si tiene éxito devuelve 
el nombre del archivo y la línea donde se encuentra el término buscado, y también puede 
devolver el número de líneas donde ha encontrado el termino buscado. 
Puede usar expresiones regulares. Cualquier meta-carácter con un significado especial debe 
ser protegido precediéndolo con una barra inclinada inversa ( ). 
• Formato: grep [opciones] "términoBuscado" archivos. 
• Opciones: 
» grep "ejemplo" ? lista las líneas que concuerdan con la cadena "ejemplo" de todos los 
archivos del directorio actual. 
» grep –ri "bien" ? busca en todos los archivos del directorio actual y subdirectorios la 
cadena "bien". 
» grep –v "bien" nombrearchivo ? lista las líneas que no contengan la cadena "bien" en el 
archivo indicado. 
» grep –c "bien" nombrearchivo ? devuelve el número total de líneas que contengan la 
cadena "bien" en el archivo indicado. 
» grep –i ? no distingue mayúsculas y minúsculas en la cadena a buscar. 
» grep –l ? devuelve el nombre del archivo, pero no la línea. 
» grep –n ? las líneas donde se encontró el texto buscado, con el número de línea. 
» grep –L ? da una lista de los archivos que no contengan el término. 
• tail: permite ver las últimas líneas de un fichero. 
• cat. 
• Muestra el contenido de un archivo. 
• Formato: cat [opciones] archivo. 
• Opciones: 
» -n: muestra el número de las líneas de texto. 
• diff. 
• Compara dos archivos y muestra una lista de las líneas que difieren. 
• Formato: diff [opciones] archivo1 archivo2. 

<!-- Page 100 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
100 
5.8.5. Otros comandos: Información, redes, usuarios 
Veamos una descripción breve de otros comandos. 
Información 
• df. 
Muestra estadísticas sobre el espacio ocupado y libre de las unidades montadas. Si se especifica 
un directorio solo mostrará las estadísticas de esa unidad. 
Formato: df [opciones] [directorio] 
Opciones: 
-h: muestra la información de una forma más comprensible para el usuario. 
• Free. 
Muestra el tamaño y la parte utilizada de la memoria física y de intercambio. 
Formato: free [opciones] 
Redes 
• ping. 
Formato: ping [opciones] nombreOrdenadorODirecciónIP 
Envía paquetes de datos a otro ordenador de la red, ordenando que lo devuelva una vez 
recibido. Sirve para comprobar el estado de una red y los ordenadores conectados. 
• ifconfig. 
Muestra información de red como adaptadores de red presentes, dirección IP, puerta de 
enlace, etc. 
Disponible en varias versiones del sistema operativo UNIX. 
Permite configurar o desplegar numerosos parámetros de las interfaces de red. 
Si se llama sin argumentos suele mostrar la configuración vigente de las interfaces de red 
activas, con detalles como la dirección MAC o el tráfico que ha circulado por las mismas hasta el 
momento. Las interfaces de red en Linux se suelen denominar eth (eth0, eth1, etc.). 

<!-- Page 101 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
101 
ifconfig acepta muchos parámetros, y generalmente su sintaxis es: 
ifconfig interfaz [dirección [parámetros] ] 
Siendo "interfaz" el nombre de la interfaz y "dirección" la dirección IP que se asigna a dicha 
interfaz. 
La «dirección» puede estar en forma de IP o usando un nombre que ifconfig buscará en 
/etc/hosts. 
En algunas versiones (Debian 9) se ha sustituido por el comando ip para asemejarse a Windows. 
• Comando Netcat (nc de forma abreviada). 
Permite analizar conexiones de red, buscar puertos abiertos, transferir datos, etc. Permite a 
través de intérprete de comandos: 
• Abrir puertos TCP/UDP en un HOST (quedando netcat a la escucha). 
• Utilizada también a menudo para abrir puertas traseras en un sistema. 
• Asociar una shell a un puerto en concreto (para conectarse por ejemplo a MS-DOS o al 
intérprete bash de Linux remotamente). 
• Forzar conexiones UDP/TCP (útil por ejemplo para realizar rastreos de puertos o realizar 
transferencias de archivos bit a bit entre dos equipos). 
• También se puede realizar la depuración de aplicaciones de red. 
Algunas de las opciones básicas del comando nc son: 
• -l: Netcat abre un puerto y se mantiene a la escucha. Se aceptará una única conexión de un 
único cliente antes de cerrarse. 
• -k: Se usa junto con la opción -l con el objetivo de que el puerto se mantenga abierto tras 
recibir una conexión, a la espera de más conexiones. 
• -u: abre puertos con el protocolo UDP en vez de abrirlos mediante el protocolo TCP. 
• -p: permite especificar el puerto al que conectarse. 
• -v: muestra información acerca de la conexión. 
• -t: Respuestas compatibles con sesiones de Telnet. 

<!-- Page 102 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
102 
Netcat es comúnmente conocida como la "Navaja suiza" de los hackers. 
La herramienta fue desarrollada por Hobbit en 1996 y liberada bajo una licencia de software 
libre permisiva (no copyleft) para UNIX, y posteriormente fue portada a otras aplicaciones 
como Windows y Mac OS X. 
Se añaden características nuevas como GNU Netcat o Cryptcat (Crytpcat es un poco más 
segura que el clásico Netcat), ya que existen muchos forks de esta herramienta. Un fork, o 
bifurcación, es realizar un desarrollo tomando como base un código fuente que ya existe, o bien 
la ramificación de un proyecto madre en varios proyectos que son independientes entre sí y que 
cuentan con objetivos o desarrolladores diferentes. 
• Comando route/ip route. 
El comando route (o el más moderno ip route) se utiliza para mostrar y modificar la tabla de 
enrutamiento que gestiona el kernel para determinar cómo se enrutan los paquetes hacia redes 
y hosts. 
Sintaxis: 
//comando antiguo y ya obsoleto 
route [opciones] comando destino [netmask máscara] [gw puerta_de_enlace] [metric 
métrica] [dev interfaz] 
//comando actual 
ip route comando destino[/prefijo] via puerta_de_enlace dev interfaz metric 
métrica 
Destino 
El parámetro destino indica el objetivo de la ruta y puede ser: 
• Una dirección de red IP. 
» route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1 
» ip route add 192.168.1.0/24 via 192.168.1.1 
• Una dirección IP para una ruta de host. 
» route add -host 192.168.1.50 gw 192.168.1.1 
» ip route add 192.168.1.50/32 via 192.168.1.1 

<!-- Page 103 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
103 
• Una ruta predeterminada. 
» route add default gw 192.168.1.1 
» ip route add default via 192.168.1.1 
Máscara de Red 
La máscara de red se especifica con netmask en el comando route o con la notación CIDR en ip 
route. 
//con route 
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1 
//con ip route en notación CIDR 
ip route add 192.168.1.0/24 via 192.168.1.1 
Si no se especifica máscara en route, se usa por defecto la correspondiente a la clase de red; en 
ip route, siempre se debe indicar la longitud del prefijo. 
Puerta de enlace 
El parámetro gw en route o via en ip route define la puerta de enlace predeterminada para 
alcanzar el destino. Los nombres simbólicos se resuelven usando /etc/hosts y, si aplica, 
/etc/networks. 
//con el comando antiguo 
route add default gw 192.168.1.1 
//con el comando moderno 
ip route add default via 192.168.1.1 
Métrica 
La métrica también se puede definir para priorizar rutas según su coste o preferencia. 
//con el comando antiguo 
route add -net 192.168.2.0 netmask 255.255.255.0 gw 192.168.1.1 metric 5 
//con el comando moderno 
ip route add 192.168.2.0/24 via 192.168.1.1 metric 5 

<!-- Page 104 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
104 
Un valor de métrica más bajo tiene mayor prioridad. 
Índice de Interfaz 
En Linux no se usa un índice numérico de interfaz en los comandos; en su lugar, se especifica 
directamente el nombre de la interfaz de red con la opción dev. 
//con route 
route add -net 192.168.2.0 netmask 255.255.255.0 gw 192.168.1.1 dev eth0 
//con ip route 
ip route add 192.168.2.0/24 via 192.168.1.1 dev eth0 
Si no se especifica dev, el sistema intenta determinar automáticamente la interfaz más 
adecuada. 
• passwd. 
Formato: passwd [opciones] nombreUsuario. 
Cambia el password de un usuario. Los usuarios pueden cambiar el suyo y el superusuario los de 
todos. 
• su. 
Formato: su [opciones] nombreusuario. 
Cambia de usuario sin cerrar la sesión actual. Por ejemplo, podemos usar su para ejecutar algo 
como root estando en nuestra sesión de usuario. 
• man. 
Formato: man comando. 
Muestra ayuda de los distintos comandos. Si se pone solo man, muestra una lista de comandos. 
5.8.6. Metacaracteres 
• *: coincide con cualquier cadena de caracteres, incluyendo una cadena vacía. 
ls *.txt //lista todos los archivos con extensión .txt 

<!-- Page 105 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
105 
• ?: coinciden con cualquier carácter individual que esté dentro de los corchetes. 
ls ho?a.txt //coincide con hola.txt, hoja.txt, etc. no coincide con horas.txt 
• [ ]: coinciden con cualquier carácter individual que esté dentro de los corchetes. 
ls salou202[34].jpg //coincide con salou2023.jpg, salou2024.jpg, 
//no COINCIDE con salou2025.jpg 
• ~: representa el directorio de inicio del usuario actual. 
cd ~ //cambia al directorio de inicio del usuario 
• " ": preservan los espacios y permiten la expansión de variables. 
echo "Bienvenido, $USER" //mostrará Bienvenido, [usuario actual] 
• ' ': preservan los espacios y no permiten la expansión de variables. 
echo 'Bienvenido $USER' //imprimirá literalmente Bienvenido, [usuario actual] 
• \: escapan el carácter siguiente, permitiendo que caracteres especiales se traten como literales. 
echo \$USER //mostrará $USER 
• {}: se utilizan para la expansión de llaves, permitiendo generar una serie de cadenas. 
echo {A..J} //mostrará A B C D E F G H I J  
echo {1..9} //mostrará 1 2 3 4 5 6 7 8 9 

<!-- Page 106 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
106 
• >, <, >>, 2>: redirigen la entrada y salida estándar. 
comando > archivo //redirige la salida estándar a un archivo. 
 comando < archivo //toma la entrada estándar de un archivo. 
 comando >> archivo //añade la salida estándar al final de un archivo. 
 comando 2> archivo //redirige los errores estándar a un archivo. 
• |: pasa la salida de un comando como entrada a otro comando. 
ls | grep txt //lista archivos y filtra aquellos que contienen "txt" 
• &&: ejecuta el segundo comando solo si el primero NO falló. 
comando1 && comando2 
• ||: ejecuta el segundo comando solo si el primero falló. 
comando1 || comando2 
• ;: separa comandos para ser ejecutados secuencialmente. 
comando1;comando2 //ejecuta comando1 seguido de comando2 sin importar si command1 
tuvo éxito. 
• $: referencia a una variable. 
echo $HOME //mostrará el directorio personal del usuario actual: /home/[usuario] 

<!-- Page 107 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
107 
• (), agrupan comandos y crean un subshell. 
(cd /tmp; ls) //cambiará al directorio /tmp, listará los archivos de /tmp 
5.9. Señales 
Sirven como mecanismo de comunicación mínima entre: procesos, teclado-proceso, núcleo-proceso, 
por el cual se envía un número (señal). 
 
 
 
 
Nota 
Las señales son atendidas en modo usuario, si el proceso está en 
modo núcleo, la señal se añade al conjunto de señales pendientes y 
se atiende cuando se regresa a modo usuario, esto puede causar un 
pequeño retraso. 
 
 
Si un proceso recibe una señal, se interrumpe su ejecución y se almacena su estado para reanudar su 
ejecución posteriormente. Se pasa a ejecutar la función que atiende esa señal, definida en el proceso 
receptory cuando finaliza se reanuda la ejecución del primer proceso en el punto que se interrumpió. 
 
 
 
 
Resumiendo 
1. El estado del proceso en ejecución se guarda en su stack. 
2. Se ejecuta el manejador de la señal. 
3. Se recupera el proceso en el estado en que se detuvo, y se 
continúa. 
 
 

<!-- Page 108 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
108 
Si un proceso recibe una señal y no se ha preparado para recibirla, se produce como resultado la muerte 
del proceso. 
Cada señal tiene un nombre SIGxxx con un significado específico. La comunicación es rápida y 
unidireccional. 
Podemos clasificar las señales en dos tipos: 
• Señales no tiempo real: son las clásicas, son las primeras 31 señales, cuando se envían solo se 
envía su número de señal. 
• Señales tiempo real: son configurables por los procesos, se puede mandar información extra a 
través de la estructura info, y si se está atendiendo a la primera señal, y se reciben más señales, 
estas se encolan. Están Definidas por la norma POSIX 1003. 
Listado señales no tiempo real 
1 
SIGHUP 
El modem ha detectado línea telefónica rota o ha terminado el proceso líder de la 
sesión 
2 
SIGINT 
Las teclas Ctrl C han sido pulsadas para matar un proceso. Puede ser controlada o 
ignorada por un manejador de señales 
3 
SIGQUIT 
Las teclas Ctrl \ han sido pulsadas, terminación de terminal 
4 
SIGILL 
Instrucción ilegal 
5 
SIGTRAP 
Traza de los programas 
6 
SIGIOT / 
SIGABORT 
Instrucción IOT (I/O TRAP), Terminación anormal 
7 
SIGBUS 
Error de Bus 
8 
SIGFPE 
Rebosamiento de coma flotante, error aritmético 
9 
SIGKILL 
Matar un proceso, no puede ser desviada a una función. 
Esta señal provoca un apagado forzoso del proceso, no puede ser ignorada ni 
manejada por un controlador de señales. Es la manera más segura de matar un 
programa si no podemos hacerlo de el resto de formas 
10 
SIGUSR1 
Señal definida por el usuario 
11 
SIGSEGV 
Violación de segmentación 
12 
SIGUSR2 
Señal definida por el usuario 
13 
SIGPIPE 
Escritura en pipe sin lectores 

<!-- Page 109 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
109 
Listado señales no tiempo real 
14 
SIGALRM 
Para despertar a un proceso que estaba en pausa. 
Señal enviada por el núcleo cuando fin del reloj ITIMER_REAL 
15 
SIGTERM 
Es una señal de terminación. 
Señal que se envía el proceso para comunicarle un apagado “amable” (cerrando 
conexiones, ficheros y limpiando sus propios búfer). También puede ser controlada o 
ignorada por un manejador de señales del proceso. Es la señala que mandan por 
defecto: kill y killall desde la terminal 
16 
SIGSTKFLT 
Desbordamiento coprocesador matemático 
17 
SIGCHLD 
Señal enviada por el núcleo a un padre cuando este hace un wait, para avisarle que un 
hijo ha terminado con un exit. 
(Señal enviada a un proceso cuando uno de sus procesos hijos termina) 
18 
SIGCONT 
El proceso se lleva a primer o segundo plano 
19 
SIGSTOP 
Suspensión de un proceso, por ejemplo por el debugger 
20 
SIGTSTP 
Suspensión del proceso debido a Ctrl Z del terminal 
21 
SIGTTIN 
Suspensión de un proceso en segundo plano que trata de leer del terminal 
22 
SIGTTOU 
Suspensión de un proceso en segundo plano que trata de escribir en el Terminal 
23 
SIGURG 
Datos urgentes para los sockets 
24 
SIGXCPU 
Sobrepasado límite de tiempo de CPU 
25 
SIGXFSZ 
Sobrepasado tamaño de fichero 
26 
SIGVTALRM 
Fin del temporizador ITIMER_VIRTUAL 
27 
SIGPROF 
Fin del temporizador ITIMER_PROF 
28 
SIGWINCH 
Cambio del tamaño de una ventana, usado por X11 
29 
SIGIO / 
SIGPOLL / 
SIGSLOT 
Datos disponibles para una entrada salida 
30 
SIGPWR 
Fallo de alimentación 
31 
SIGUNUSED 
Argumento erróneo en una llamada 
32 
SIGRTMIN 
Marca el límite se señales en tiempo real, ≥ 32 no tiempo real 
Fuente: http://sopa.dis.ulpgc.es/ii-dso/leclinux/interrupciones/senales/lec4_senales.pdf 

<!-- Page 110 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
110 
5.10. Runlevels estándar en Linux 
Runlevels son niveles de ejecución. 
El sistema operativo GNU/Linux puede aprovechar los niveles de ejecución a través de los programas 
del proyecto sysvinit. 
Después de que el núcleo Linux ha arrancado, el programa init lee el archivo /etc/inittab para 
determinar el comportamiento para cada nivel de ejecución. 
A no ser que el usuario especifique otro valor como un parámetro de autoarranque del núcleo, el 
sistema intentará entrar (iniciar) al nivel de ejecución por defecto. 
La mayoría de las distribuciones Linux, definen los siguientes niveles de ejecución adicionales: 
Los 7 niveles de ejecución (runlevels) estándars 
Nivel de 
ejecución 
Nombre o 
denominación 
Descripción 
0 
Alto 
Alto o cierre del sistema (Apagado) 
1 
Modo de usuario 
único (Monousuario) 
No configura la interfaz de red o los demonios de inicio, ni permite que 
ingresen otros usuarios que no sean el usuario root, sin contraseña. 
Este nivel de ejecución permite reparar problemas, o hacer pruebas en 
el sistema 
2 
Multiusuario 
Multiusuario sin soporte de red 
3 
Multiusuario con 
soporte de red 
Inicia el sistema normalmente 
4 
Multiusuario con 
soporte de red 
Con esta opción el administrador puede personalizar el inicio para 
cargar algún servicio 
5 
Multiusuario gráfico 
(X11) 
Similar al nivel de ejecución 3 + display manager 
6 
Reinicio 
Se reinicia el sistema 
5.11. S.O. FreeBSD 
FreeBSD es un sistema operativo de código abierto, descendiente del sistema Berkeley Software 
Distribution o BSD (concretamente basado en BSD-Lite versión 4.4). 
BSD (en español, «distribución de software Berkeley») fue un sistema operativo, desarrollado por 
Berkeley, derivado de Unix que nace a partir de los aportes realizados a ese sistema por la Universidad 
de California en Berkeley. 

<!-- Page 111 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
111 
Resumimos algunas características: 
• Sistema operativo multiusuario, capaz de efectuar multitarea con apropiación y multiproceso en 
plataformas compatibles con múltiples procesadores. 
• Se ha ajustado para ofrecer las máximas prestaciones. 
• Ofrece opciones avanzadas que no se encuentran en algunos sistemas operativos comerciales. 
• Excelente servidor de internet y extranet. Servicios de red muy robustos. 
• Buenos tiempos de respuesta con miles de procesos simultáneos. 
• Netflix utiliza servidores FreeBSD. 
6. macOS 
En este apartado daremos unos breves apuntes sobre el Sistema Operativo de Mac, el macOs. 
La evolución de este sistema operativo ha sido notable a lo largo del tiempo y pivotando 
fundamentalmente sobre las mejoras de diseño, funcionalidad, seguridad y rendimiento. 
Una parte fundamental ha sido la integración del Ecosistema Apple con otros dispositivos de la misma 
marca como los iPad, iPhones, Apple Watch, etc. 
La funcionalidad Handoff que ha permitido alternar la misma tarea en distintos dispositivos Apple y 
AirDrop que ha facilitado la transferencia de ficheros asimismo entre dispositivos de la misma marca. 
Otros puntos destacables son el diseño cuidado y la llamativa e intuitiva interfaz gráfica que interpela a 
muchos usuarios. 
Otra característica clave es el software de calidad con la App Store de Apple que ofrece una amplia 
gama de aplicaciones. 
Privacidad y Seguridad han sido también parte esencial de su propuesta. La estabilidad y el rendimiento 
fruto del control de Hardware y Software le han permitido destacar. 
El soporte a largo plazo es una garantía debido a sus actualizaciones periódicas durante varios años. 
Otro de sus puntos fuertes es su presencia en la industria creativa y las herramientas de diseño gráfico. 
Características todas ellas que han fomentado la fidelidad de sectores específicos. 

<!-- Page 112 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
112 
Indicaremos a continuación del macOS a través del histórico de versiones desde su aparición: 
• Mac OS X 10.0 "Cheetah" (2001): Primera versión de Mac OS X. 
• Mac OS X 10.1 "Puma" (2001): Aparecen mejores sobre la versión anterior y nuevas 
características. 
• Mac OS X 10.2 "Jaguar" (2002): Aparecen nuevas particularidades y se trabaja sobre el 
rendimiento. 
• Mac OS X 10.3 "Panther" (2003): Aparece el "Exposé" y distintas mejoras. 
• Mac OS X 10.4 "Tiger" (2005): Se introduce el "Dashboard y Spotlight", entre otras 
particularidades. 
• Mac OS X 10.5 "Leopard" (2007): Se incorpora Time Machine y Boot Camp, y varias novedades. 
• Mac OS X 10.6 "Snow Leopard" (2009): la estabilidad y la mejora de rendimiento es lo esencial 
en esta versión. 
• OS X 10.7 "Lion" (2011): la nomenclatura cambia a "OS X". 
• OS X 10.8 "Mountain Lion" (2012): intensifica la integración con iCloud. 
• OS X 10.9 "Mavericks" (2013): Implementa Maps y iBooks. 
• OS X 10.10 "Yosemite" (2014): Nuevo diseño más moderno y mejoras en la integración con iOS. 
• OS X 10.11 "El Capitan" (2015): Trabaja en el rendimiento, la estabilidad y profundiza en la 
experiencia de usuario de la versión anterior. 
• macOS 10.12 "Sierra" (2016): Aparece Siri en la plataforma Mac. 
• macOS 10.13 "High Sierra" (2017): mejora la gestión de archivos, la seguridad del sistema, e 
introduce el soporte de videos de alta eficiencia HEVC. 
• macOS 10.14 "Mojave" (2018): Presentó el modo oscuro, la función Stacks encargada de 
organizar los archivos del escritorio. 
• macOS 10.15 "Catalina" (2019): Separa el iTunes en tres aplicaciones distintas Apple Music, TV 
y Podcasts, es la versión que da el paso a aplicaciones de 64 bits. 
• macOS 11 "Big Sur" (2020): Presenta un nuevo diseño, el centro de control que incluye el 
acceso directo a funciones básicas del sistema operativo (Wi-Fi, Sonido, Bluetooth...), la versión 
del navegador Safari, la catorce mejora su velocidad de navegación y privacidad. 
• macOS 12 "Monterey" (2021): presenta el Modo Focus que permite personalizar notificaciones 
y la disponiblidad de las aplicaciones según su actividad y ubicación. Se introducen atajos para 
que los usuarios puedan automatizar flujos de trabajo personalizados. 

<!-- Page 113 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
113 
• macOS 13: "Ventura" (2022): trae nuevas aplicaciones, mejoras en su gestor de correo 
electrónico Mail, una nueva versión de Safari, nuevas funciones para las videoconferencias... 
• macOS 14: "Sonoma" (2023): vigésima versión. Widgets en el escritorio: permite además de 
tener widgets en el centro de notificaciones, incluirlos directamente en el escritorio, mejora del 
sistema de videoconferencia, mejoras en la navegación privada, en el compartir pantalla... 
• macOS 15 Sequoia (2024): destacando funciones como iPhone Mirroring para controlar el 
iPhone desde el Mac, una nueva aplicación de Contraseñas, mejoras en la organización de 
ventanas y herramientas avanzadas para videoconferencias. Además, se anunció Apple 
Intelligence, su sistema de IA, aunque su lanzamiento se programó para finales de 2024 y solo 
en Macs con chips M1 o posteriores. Actualmente, la versión más reciente es macOS Sequoia 
15.3, lanzada en enero de 2025, con mejoras en rendimiento y seguridad, correcciones en 
AirPlay, FaceTime, iCloud y Safari, además de la función beta GenEmoji para crear emojis 
personalizados mediante texto. También se optimizó Apple Intelligence, se mejoró la 
navegación en Safari y se ajustaron notificaciones para mayor claridad. 
7. Sistemas operativos para dispositivos móviles 
Un dispositivo móvil tiene las siguientes características que lo definen: 
• Es un aparato de pequeño tamaño. 
• Tiene algunas capacidades de procesamiento. 
• Pueden conectarse a redes. 
• Tiene memoria limitada. 
• Ha sido diseñado específicamente para una función, aunque puede llevar a cabo otras funciones 
más generales. 
• Normalmente se asocian al uso individual de una persona, tanto en posesión como en operación. 
 

<!-- Page 114 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
114 
 
 
 
El experto opina 
Consideramos dispositivos móviles a los teléfonos móviles, tablets, 
pdas y similares. 
Los netbooks se consideran a menudo dispositivos móviles, pero 
dado que el tamaño del dispositivo impide un manejo cómodo (por 
ejemplo, sin la ayuda de una mesa) no lo consideraremos un 
dispositivo móvil en este documento. 
 
 
Los Sistemas Operativos para dispositivos móviles están orientados a: 
• La movilidad. 
• La conectividad inalámbrica. 
• La administración de forma óptima del procesamiento y almacenamiento. 
• El consumo de la energía. 
A continuación, vamos a listar algunos de los sistemas operativos para móviles más conocidos: 
• Google Android. 
• Apple iOS. 
• Windows 10 Mobile. 
• Symbian. 
• Ubuntu touch. 
• Firefox O.S. 
• Blackberry OS. 
• MeeGo (unión de los sistemas operativos Maemo de Nokia y Moblin de Intel, con los cuales 
pretendían competir con el sistema Android de Google). 
• Tizen: (basado en Linux). 
Estudiaremos Android e iOs, ya que son los más utilizados. 

<!-- Page 115 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
115 
7.1. Android 
 
El sistema operativo Android es sin duda el líder del mercado móvil en sistemas operativos. 
Android se utiliza para teléfonos inteligentes y tabletas, así como también algunas distribuciones 
enfocadas a su uso en ordenadores personales de escritorio y portátiles (Note y Netbook 
respectivamente) ejemplo: Remix OS. 
Características 
• Código abierto. 
• Núcleo basado en el Kernel de Linux. 
• Pertenece a Google. 
• Está diseñado para su uso en dispositivos móviles. 
• El Android SDK (Software Development Kit) es la plataforma principal para el desarrollo de 
aplicaciones Android. Proporciona bibliotecas, emuladores, herramientas de depuración y 
compiladores que permiten a los desarrolladores crear aplicaciones en Java y Kotlin, los dos 
lenguajes oficialmente soportados por Android. 
• Si bien Java se sigue utilizando, en los últimos años Kotlin se ha convertido en el lenguaje 
recomendado por Google (desde 2017). 
• Las aplicaciones Android se empaquetan con la extensión .apk (Android Application Package, en 
español: Paquete de Aplicación Android), que permite su instalación en dispositivos Android. 
• Android cuenta con su propia máquina virtual para ejecutar estas aplicaciones: 
• Dalvik hasta la versión 4.3 (Jelly Bean). 
• ART (Android Run Time) a partir de la versión 4.4 (Kit Kat). 
• Adaptable a muchas pantallas y resoluciones. 
• Utiliza SQLite para el almacenamiento de datos. 
• Ofrece diferentes formas de mensajería. 

<!-- Page 116 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
116 
• Navegador web basado en WebKit incluido. 
• Soporte de Java y muchos formatos multimedia. 
• Soporte de HTML, HTML5, Adobe Flash Player, etc. 
• Entorno de desarrollo oficial Android Studio (anteriormente se utilizaba Eclipse con el plugin 
ADT (Herramientas de Desarrollo de Android). 
• Emulador de dispositivos. 
• Herramientas de depuración. 
• Análisis de rendimiento. 
• Google Play. Catálogo de aplicaciones (gratuitas y de pago) que podemos descargar e instalar. 
• Bluetooth. 
• Multitáctil. Soporte nativo para pantallas capacitivas. 
• Videollamada a través de Hangouts (antes Google Talk) desde su versión HoneyComb (fue 
ideada en exclusiva para tablets). 
• Multitarea. 
• Tethering. Actúa como punto de acceso inalámbrico para otros dispositivos, permitiéndoles 
utilizar la conexión de datos del dispositivo móvil. 
 

<!-- Page 117 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
117 
 
 
 
 
 
Reto 
Busca en internet las innovaciones que se han ido incluyendo en 
cada versión de Android. 
 
 
 And roid y las capas de personalización: 
El sistema operativo Android es implementado por numerosos y muy distintos fabricantes y marcas de 
teléfonos móviles. El caracter de código abierto de las rutinas operativas permitirá a los desarrolladores 
de cada compañía personalizar la interfaz de usuario sobre la misma base Android, otorgando a cada 
uno de los dispositivos un caracter único y una apariencia característica en lo que se viene a denominar 
comunmente la "experiencia de usuario". El término más técnico es el de capa de personalización. 
La capa de personalización, con su nombre específico, suele contar con funcionalidades propias, una 
apariencia visual totalmente adaptada y una configuración a medida. 

<!-- Page 118 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
118 
A continuación pasamos a destacar algunas de las capas de personalización más extendidas: 
• Samsung Experience/One UI: Utilizada en dispositivos Samsung, como la serie Galaxy. 
• ZenUI: ASUS implementa ZenUI en sus smartphones. 
• Nubia UI: Utilizada en dispositivos Nubia. 
• ColorOS: Utilizada en dispositivos OPPO. 
• Funtouch OS: Utilizada en dispositivos Vivo. 
• MIUI: Desarrollada por Xiaomi para sus dispositivos. 
• EMUI: Desarrollada por Huawei para sus dispositivos. 
• OxygenOS: Utilizada en dispositivos OnePlus. 
• LG UX: Utilizada en dispositivos LG. 
• Moto: Personalización de Motorola para sus dispositivos. 
• OriginOS: Desarrollada por BBK Electronics, la misma empresa matriz de OPPO, Vivo y OnePlus. 
• TCL UI: Usada por los dispositivos TCL. 
• Realme UI: Utilizada en dispositivos Realme. 
Los dispositivos de Google no usarán una capa de personalización pesada, presentando una versión muy 
pura de un sistema operativo que al fin y al cabo es propio desde el año 2005. 
 
Google Pixel 8 Pro 

<!-- Page 119 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
119 
7.2. IOS 
Es un sistema operativo móvil desarrollado por Apple Inc. 
Inicialmente fue creado para el iPhone, pero con el tiempo fue adaptado para los demás dispositivos 
móviles de esta compañía (iPad y el iPod touch). 
El primer sistema operativo IOS fue lanzado en el año 2007 junto con el primer iPhone. 
Está basado en el concepto de manipulación directa, es decir, que está creado para la interpretación de 
gestos multitáctiles que permiten al usuario interactuar directamente con la pantalla del dispositivo por 
medio de toques, pellizcos y deslices y utilizar varios puntos para interactuar con la pantalla y no 
únicamente un punto. 
Una de las cosas que le faltaba a este sistema operativo, era la inclusión de un centro de notificaciones 
visible al usuario, cosa que se ha solucionado con las últimas actualizaciones implementadas por la 
compañía. 
Aunque sea un sistema operativo privado y exclusivo para sus dispositivos, Apple libero su SDK o kit de 
desarrollo de software, para poder ser implementado y mejorado por desarrolladores que así lo decidan. 
Características 
• Deriva de la familia Mac OS X, que está basado en Darwin BSD y, por tanto, está basado en Unix. 
• Sistema operativo privado y exclusivo para sus dispositivos. 
• Multitarea. 
• Multitouch. 
• Pantalla compuesta por: 
• Pantalla principal o «SpringBoard» donde se sitúan las aplicaciones. 
• Dock en la parte inferior de la pantalla principal donde se pueden anclar aplicaciones de uso 
frecuente. 
• Barra de estado en la parte superior para mostrar datos como la hora, el nivel de batería, y 
la intensidad de la señal. 
• Actualizaciones y aplicaciones a través de Itunes. 
• Safari es el navegador web por defecto. 
• Aplicaciones descargables desde APP Store (extensión .IPA). 
• No soporta Adobe Flash ni Java. 

<!-- Page 120 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
120 
• Organización de carpetas. Se puede mover una aplicación sobre otra y se creará una carpeta, y 
así se pueden agregar más aplicaciones a esta mediante el mismo procedimiento. 
• Tethering. Actúa como punto de acceso inalámbrico para otros dispositivos, permitiéndoles 
utilizar la conexión de datos del dispositivo móvil. 
• Seguridad mediante activación por iCloud, la cual solicita los datos de acceso de la cuenta del 
usuario original, lo que permite bloquear e inutilizar el equipo al perderlo o ser víctima de robo 
del dispositivo. 
• XCODE es el IDE (entorno de desarrollo integrado) utilizado. 
7.3. Notificaciones Push 
Las notificaciones push son mensajes instantáneos que son enviados a dispositivos móviles 
generalmente a través de redes inalámbricas (redes de datos celulares o conexiones WI-FI). La 
particularidad de estas notificaciones es que no necesitan que la aplicación esté activa. No tenemos 
por qué estar logueados, tener la aplicación abierta o incluso activa para recibir una notificación de este 
tipo, siempre que tenga permisos para hacerlo. A la hora de instalarala en nuestros dispositivos, nos 
solicitará los permisos necesarios para poder hacerlo.  
Los desarrolladores de las aplicaciones serán quienes implementen y gestionen las notificaciones push a 
través de servicios como Firebase Cloud Messaging (FCM) para Android o Apple Push Notification 
Service (APNs) para iOS. Servicios que serán accesibles a través de la API de Notificaciones del 
navegador o bien a nivel del código nativo del sistema operativo correspondiente, según se haya 
decidido. 
El flujo de trabajo de las notificaciones mobile push es el siguiente: 
• Permisos: el usuario ha de otorgar su consentimiento para recibir estas notificaciones y la 
aplicación una vez lo tenga podrá continuar con el proceso. 
• Registro: la aplicación o sitio web registrará al usuario (si éste ha dado su consentimiento) 
obteniendo un identificador único a modo de token de registro que será usado para dirigir las 
notificaciones al usuario del dispositivo. 
• Envío: envío de la notificación junto con el token de registro. 
• Recepción: dependiendo de si es una aplicación web o nativa se recibirá la notificación. 
• Presentación: puede ser en formato de texto, de iconos, imágenes, enlaces o acciones, sonido y 
vibración o formatos específicos de la plataforma implicada. 
• Interacción: la notificación presentada al usuario puede solicitar al usuario una interacción 
(enlace a un sitio web específico, apertura de la aplicación, etc.) que de existir cerraría aquí el 
ciclo de vida del flujo de trabajo de la notificación mobile push. 

<!-- Page 121 -->

 
 
Sistemas Operativos. Características y elementos constitutivos. Sistemas Windows, Linux, 
y para dispositivos móviles 
121 
8. Bibliografía 
• Sistemas Operativos. Teoría y problemas. J. Aranda, M.A. Canto, J.M. de la Cruz, S. Dormido, C. 
Mañoso. Editorial Sanz y Torres. 
• Sistemas Operativos Monopuesto 2ª edición. J.L. Rayas y L. Raya. Editorial RA-MA. 
• https://searchdatacenter.techtarget.com/es/definicion/Microsoft. 
• https://www.ecured.cu/Microsoft_Windows y https://www.ecured.cu/IOS. 
• https://www.softwaredoit.es/definicion/definicion-microsoft-windows.html. 
• http://es.windows.wikia.com/ y https://www.wikipedia.org/. 
• Aprenda Linux como si estuviera en primero. Universidad de Navarra. J García de Jalón, I. 
Aguinaga, A. Mora. 
• https://www.gnu.org. 
• https://computerhoy.com. 
• https://www.softzone.es. 
• https://es.ccm.net/. 
• http://maslinux.es/. 
• http://isa.uniovi.es/docencia/SIGC/pdf/telefonia_movil.pdf. 
• http://androidos.readthedocs.io/en/latest/data/caracteristicas/. 
• http://culturacion.com/ios-el-sistema-operativo-movil-de-apple/. 
• https://help.ubuntu.com. 
• https://edu.gcfglobal.org/es/ipad/sistema-operativo-movil-ios/1/. 
• http://sopa.dis.ulpgc.es/ii-dso/leclinux/interrupciones/senales/lec4_senales.pdf. 
• https://www.microsoft.com/es-es/windows/windows-11?r=1. 
 

<!-- Page 122 -->

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial**: [[wiki/sources/bloque2-tema04|Fuente Oficial del Tema 04]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema04-sistemas-operativos|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Portada e Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema05|Tema 05 ➡️]]
