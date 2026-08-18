---
title: "Tema Completo Extendido 01 (Bloque 4): Administración de Sistemas Operativos Servidor (Linux SysAdmin, Windows Server)"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-4
  - tema-01
  - oposiciones-tai\nestado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque4-tema01.md]]"
  - "[[wiki/sources/bloque4-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---
> [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Portada Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema02|Tema Completo 02 ➡️]]

# 🔴 Tema Completo Extendido 01 (Bloque 4): Administración de Sistemas Operativos Servidor (Linux SysAdmin, Windows Server)

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 01 correspondiente al Bloque 4 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

---

Administración del Sistema 
Operativo y software de Base 

---

ÍNDICE 
1. Software 
5 
1.1. Software de sistemas 
5 
1.1.1. Sistemas Operativos 
7 
1.1.1.1. Funciones 
7 
1.1.1.2. Evolución 
8 
1.1.1.3. Principales Sistemas Operativos 
9 
1.2. Software de aplicación 
9 
2. Servicio de directorio 
9 
2.1. Estándares y protocolos 
12 
2.1.1. X.500 
12 
2.1.2. Protocolo LDAP 
13 
2.2. eDirectory de Novell 
15 
2.3. Directorio activo de Microsoft 
18 
2.3.1. Dominio en Active Directory 
21 
2.3.2. Direccionamientos a recursos 
24 
2.3.3. Diferencias entre Windows NT y Active Directory 
24 
2.3.4. Conclusión sobre Active Directory 
24 
2.3.5. Introducción a Active Directory Domain Services (AD DS) 
25 
2.3.6. Herramientas de gestión de Active Directory 
26 
2.3.6.1. Servidor SolarWinds y Monitor de aplicaciones 
27 
2.3.6.2. ENow Compass 
28 
2.3.6.3. Monitor de Active Directory de Anturis 
29 
2.3.6.4. Quest Active Administrator 
29 
2.3.6.5. Kit Herramientas gratuitas de ManageEngine Active Directory 
30 
3. Administrador de sistemas. Funciones 
32 
3.1. Realizar copias de seguridad 
34 
3.1.1. Configuración de Copias de Seguridad automáticas 
35 
3.2. Preparar los equipos nuevos 
37 
3.3. Cambiar la configuración hardware de los equipos 
37

---

3.4. Actualización del sistema operativo 
37 
3.4.1. Actualización de servidores 
38 
3.4.2. Actualización de S.O. desde el puesto de usuario 
42 
3.5. Actualización o instalación de nuevo software de aplicación 
50 
3.6. Configurar y mantener acceso a internet 
52 
3.7. Gestión de cuentas de usuarios 
53 
3.8. Monitorizar el rendimiento del sistema 
53 
3.8.1. Monitorización del rendimiento y uso de recursos 
54 
3.9. Seguridad 
54 
3.9.1. Configuración de Directivas de Seguridad y Controles de acceso 
55 
3.10. Relación con usuarios y dirección 
56 
3.11. Informar a la dirección 
56 
3.12. Documentación del sistema 
56 
4. Herramientas para la administracion del sistema 
57 
4.1. Comandos de Windows 
57 
4.2. Herramienta Netsh 
63 
4.3. Herramienta Netcat 
67 
4.4. Herramienta Net User 
68 
4.5. Bash 
69 
4.5.1. Historia 
71 
4.5.2. Seguridad 
71 
4.5.2.1. Shellshock 
72 
4.5.2.2. Sintaxis de Bash 
73 
4.6. Scripting en entornos Windows 
76 
4.6.1. PowerShell 
76 
4.6.1.1. Algunos de los comandos CMDLETS 
78 
4.6.2. Batch 
80 
4.7. Otras herramientas 
82 
4.7.1. Predominante en Windows 
82

---

4.7.2. Predominante en Linux 
83 
4.7.3. Multiplataforma 
84 
5. Configuración optima del sistema en Windows 
85 
5.1. Uso de cuenta de administrador 
85 
5.2. Configurar actualizaciones automáticas 
86 
5.3. Uso del registro de eventos 
87 
5.3.1. Uso del Visor de eventos en Windows Server 
87 
5.4. Uso de unidades SSD en servidores 
88 
5.5. Configuración de permisos de acceso de roles en Windows Server 
88 
6. Mantenimiento y reparación 
89 
6.1. Pasos a seguir para mantener/reparar el Sistema Operativo 
93 
6.2. Otras herramientas administrativas de configuracion 
98 
7. Supervisión del sistema mediante logs y mensajes de consola en Linux 
99 
7.1. Archivos de log 
99 
7.2. Comandos básicos para consultar logs 
100 
7.3. Uso de journalctl 
101 
7.4. Rotación y mantenimiento de logs 
101 
7.5. Buenas prácticas de supervisión 
102 
8. Tendencias: Bring Your Own Device 
103 
9. Gestión de dispositivos móviles 
104 
9.1. Actualización de terminales móviles 
104 
9.2. Enrolamiento de móviles 
108 
10. Bibliografía 
109

---

Administración del Sistema Operativo y software de Base 
5 
1. Software 
Podemos clasificar el software en 2 categorías, dependiendo de su función en el uso de un ordenador: 
• De sistemas: 
Controla las operaciones propias de ordenador, por lo tanto, es el más importante. (Si no 
disponemos de él, no podemos instalar ningún tipo de software de aplicación). 
• De aplicación: 
Es el software encargado de realizar tareas concretas para resolver problemas específicos del 
usuario. 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
1.1. Software de sistemas 
Denominado también software de Base. 
El software de sistemas, es el conjunto de instrucciones que permiten el manejo del ordenador, sirve de 
soporte o base para controlar e interactuar con el hardware y permitir la instalación de otros programas. 
El software de base lo podemos clasificar por orden de necesidad de la siguiente forma: 
• El programa BIOS (Basic Input/Output System), o su sucesor UEFI. 
Se trata de un Firmware, (soporte lógico inalterable), es el software de más bajo nivel, una 
porción de código, que se encarga de controlar lo que debe hacer cada dispositivo de hardware, 
y además debe asegurarse de que su funcionamiento básico sea correcto.

---

Administración del Sistema Operativo y software de Base 
6 
Su propósito es activar una máquina desde su encendido, y preparar el entorno para cargar un 
sistema operativo. 
El firmware es un programa informático que establece la lógica de más bajo nivel que controla 
los circuitos electrónicos de un dispositivo de cualquier tipo. Está fuertemente integrado con la \nelectrónica del dispositivo, es el software que tiene directa interacción con el hardware, siendo 
así el encargado de controlarlo para ejecutar correctamente las instrucciones externas. 
Se almacena en un tipo de memoria especifica que actualmente es reescribible, (aunque se 
conoce como soporte lógico inalterable por sus inicios) la traducción sea para poder realizar 
instalaciones del fabricante, que pueden ser necesarias para que la placa base reconozca \nelementos nuevos de hardware (fabricados con posterioridad de la placa base). Una 
actualización errónea (por ejemplo, de otro modelo de placa base) puede hacer que la placa 
base deje de funcionar. 
El Firmware sucesor de BIOS es UEFI, siglas de EFI-Unified Extensible Firmware Interface, 
traducido como la interfaz Unificada de firmware extensible. 
UEFI es el firmware sucesor de BIOS, escrito en C, para ofrecer más recursos, (como menús 
gráficos, diagnósticos más detallados, abrir software compatible con EFI desde otras 
ubicaciones de almacenamiento, como una unidad de disco duro o un dispositivo de 
almacenamiento USB) y permite que el BIOS contenga recursos más sofisticados, como el 
Arranque seguro. 
Es necesario para poder utilizar opciones de acceso remoto, (que el ordenador pueda ser \nencendido remotamente a través de la conexión de red). 
La Interfaz Unificada de firmware extensible (EFI-Unified Extensible Firmware Interface) es una \nespecificación que define una interfaz entre el sistema operativo y el firmware. 
UEFI reemplaza la antigua interfaz del Sistema Básico de Entrada y Salida (BIOS) estándar 
presentado en las computadoras personales IBM PC como IBM PC ROM BIOS. 
• El sistema Operativo. 
Es la base del funcionamiento de un ordenador, realizan diversas tareas, como la transferencia 
de datos entre la memoria RAM y los dispositivos de almacenamiento, etc. 
 
 
 
 
+ Info 
Algunos autores también consideran los lenguajes de 
programación (intérpretes, compiladores, etcétera) como 
software de sistemas. 
Pero no lo son, ya que es necesario que para su uso haya instalado 
primero un sistema operativo.

---

Administración del Sistema Operativo y software de Base 
7 
1.1.1. Sistemas Operativos 
Ya estudiaste en la unidad 4 del Bloque II, "El Sistema Operativo". 
Recordemos que es un software, que se encarga de arrancar el equipo y gestionar los recursos del 
mismo, controlando los elementos de hardware (mediante los drivers), para proporcionar un entorno 
de trabajo al usuario. 
Actúa como intermediario entre el hardware y el usuario. 
Además de realizar sus funciones propias, también incluye programas utilitarios, para que el usuario 
pueda realizar tareas en general y de mantenimiento, y diversas funciones para resolver problemas \nespecíficos. Estos programas, varían según el sistema operativo y su versión. por ejemplo, son: 
• Herramientas de programación: compiladores, ensambladores, enlazadores, etc. 
• Entorno de escritorio / Interfaz gráfica de usuario (que pueden incluir un gestor de ventanas). 
• Línea de comandos. 
• Hipervisores. 
• Bootloaders (gestores de arranque). 
1.1.1.1. Funciones 
La función principal del S.O. es gestionar y optimizar el uso de los recursos del sistema, utilizando el 
Gestor de Recursos. 
Las funciones u objetivos del S.O. son los siguientes: 
• Aceptar y procesar todos los trabajos solicitados y mantenerlos hasta su finalización. 
• Interpretar los comandos que permiten al usuario interactuar con el ordenador. 
• Controlar los recursos, coordinar y gestionar la parte física del ordenador (hardware), tanto 
interna (memoria, procesador, HD…) como externa (teclado, monitor…). 
• Manejo de errores que provoquen la perdida de información o del flujo del proceso. 
• Secuenciador de tareas, debe administrar la prioridad de los procesos necesarios para el buen fin 
de las tareas encomendadas. 
• Protección del proceso de trabajo, de forma que las acciones de otros usuarios o periféricos no 
detenga o perjudique su continuidad.

---

Administración del Sistema Operativo y software de Base 
8 
1.1.1.2. Evolución 
En un principio, los sistemas operativos tenían una estructura monolítica. Estaba todo al mismo nivel, 
como el MS-DOS, es decir todos los comandos estaban al mismo nivel de ejecución. 
Las rutinas y funcionalidades (de drivers, sistemas de archivos, gestión de memoria, etc.), se agrupaban \nen un solo programa (el S.O.), descrito como un conjunto de procedimientos o rutinas entrelazadas de 
tal forma que cada una tiene la posibilidad de llamar a las otras rutinas cada vez que así lo requiera. 
Todo el sistema, se ejecuta todo en el mismo nivel del núcleo (kernel). 
La consecuencia de esta estructura monolítica pura, es que si falla un programa se produce un error en 
todo el sistema, por lo que no nos ofrece confiabilidad. 
Esto no era suficiente para los requisitos de los usuarios, por tanto, comenzaron a aparecer los niveles 
jerárquicos y la abstracción de la información. 
Vamos a repasar algunos conceptos que han ido apareciendo a lo largo de la historia de los sistemas 
operativos, y que muchos de ellos ya estudiaste con mayor detenimiento en el Bloque II: 
• Kernel. 
El kernel es el núcleo del sistema operativo. Se carga en memoria al arrancar el ordenador y 
permanece aquí hasta que se apaga. 
• Gestor del sistema de E/S. 
• Gestión de procesos. Gestor de recursos (Gestión y planificación de los recursos). 
Un proceso es, básicamente, un programa en ejecución. Está formado por el programa \nejecutable, los datos que utilizará y el contexto en que se ejecuta. 
• Gestión de la memoria. 
• Gestor de Sistema de archivos. (almacenamiento secundario). 
• Llamadas al sistema. 
El sistema operativo debe gestionar los recursos que hay en el sistema (procesadores, memoria, 
periféricos, etcétera) y planificar la utilización de los recursos de manera justa y eficiente. 
Todos los procesos que compiten por un determinado recurso deben disponer de él de una 
forma planificada, basándose en los requerimientos de cada proceso. 
• Sistema de protección y seguridad de la información. 
Se deben aplicar políticas de seguridad e implementar mecanismos de protección para evitar 
que personas o aplicaciones realicen ataques al sistema informático. 
• Sistema de comunicación. 
• Intérprete de comandos.

---

Administración del Sistema Operativo y software de Base 
9 
1.1.1.3. Principales Sistemas Operativos 
Existen muchos sistemas Operativos, algunos muy conocidos y otros todo lo contrario. 
Vamos a hacer un resumen: 
• El software de sistema por antonomasia es Microsoft Windows, que acumula cerca de un 90% 
de la cuota de mercado. 
• También hay que destacar el proyecto GNU, cuyas herramientas de programación permitieron 
combinarse con el núcleo informático basado en Unix denominado Linux, formando entre ambos 
las conocidas como distribuciones GNU/Linux. Además, en este caso se trata de software libre. 
• Destacamos también Mac OS. 
• Otros más desconocidos (aunque puedan derivar de Linux) son: 
Theos, DexOS, Debian, Solaris, Syllable, FreeBSD, ReactOS, Aros, FreeDOS, Haiku, Illumos, 
MenuetOS, Visopsys… 
1.2. Software de aplicación 
Dependiendo de las necesidades del usuario, es decir de para que vamos a utilizar un software, 
tendremos infinidad de tipos de aplicaciones como: 
• Diseñadas gestionar diferentes oficios: peluquerías, venta de ropa, talleres… 
• Diseñadas para hacer una gestión concreta como las máquinas que recargan las tarjetas del 
autobús, o nos dan un número de orden de atención en un organismo como el registro civil, 
dependiendo la gestión que queremos realizar. 
• La gestión de maquinaría de empresas, como las maquinas que recortan tableros de madera 
siguiendo un patrón dibujado en el software. 
• Diseñados para proteger el ordenador como los antivirus. 
• Y otras muchas… 
2. Servicio de directorio 
Para gestionar un sistema informático, es necesario conocer qué es un servicio de directorio (SD) y las 
herramientas disponibles para facilitar el trabajo del administrador de sistemas. 
Un servicio de directorio (SD) es una aplicación o un conjunto de aplicaciones que almacena y organiza 
la información sobre: 
• Los usuarios de una red de ordenadores. 
• Sobre los recursos de red que permite a los administradores gestionar el acceso de usuarios a los 
recursos sobre dicha red.

---

Administración del Sistema Operativo y software de Base 
10 
Además, los servicios de directorio actúan como una capa de abstracción entre los usuarios y los 
recursos compartidos. 
 
 
 
 
Aviso 
Un servicio de directorio no debería confundirse con el repositorio 
de directorio, que es la base de datos la que contiene la 
información sobre los objetos de nombrado gestionada por el 
servicio de directorio. 
 
 
En el caso del modelo de servicio de directorio distribuido en X.500, se usa uno o más espacios de 
nombre (árbol de objetos) para formar el servicio de directorio. 
El servicio de directorio proporciona la interfaz de acceso a los datos que se contienen en unos o más \nespacios de nombre de directorio. 
La interfaz del servicio de directorio es la encargada de gestionar la autenticación de los accesos al 
servicio de forma segura, actuando como autoridad central para el acceso a los recursos de sistema que 
manejan los datos del directorio. 
Como base de datos, un servicio del directorio está altamente optimizado para lecturas y proporciona 
alternativas avanzadas de búsqueda en los diferentes atributos que se puedan asociar a los objetos de 
un directorio. Los datos que se almacenan en el directorio son definidos por un esquema extensible y 
modificable. Los servicios de directorio utilizan un modelo distribuido para almacenar su información y \nesa información generalmente está replicada entre los servidores que forman el directorio. 
Un servicio del directorio define el espacio de nombres de una red. Un espacio de nombres, en este 
contexto, es el término que se utiliza para llevar a cabo unos o más objetos como entradas nombradas. 
El proceso del diseño del directorio tiene normalmente un conjunto de las reglas que determinan cómo 
se nombran y se identifican los recursos de la red. Las reglas especifican que los nombres sean únicos e 
inequívocos. 
En X.500 (los estándares de servicio de directorio) y en LDAP el nombre se denomina distinguished 
name (DN) y se utiliza para referirse al nombre único de una entrada. 
Un servicio del directorio es una infraestructura compartida de la información para localizar, manejar, 
administrar, y organizar los componentes y recursos comunes de una red, que pueden incluir 
volúmenes, carpetas, archivos, impresoras, usuarios, grupos, dispositivos, números de teléfono y otros 
objetos.

---

Administración del Sistema Operativo y software de Base 
11 
Un servicio del directorio es un componente importante del sistema operativo de red NOS, en inglés, 
Network Operating System: 
• Es un software que permite la interconexión de ordenadores para poder acceder a los servicios y 
recursos, hardware y software, creando redes de computadoras. 
• Al igual que un equipo no puede trabajar sin un sistema operativo, una red de equipos no puede 
funcionar sin un sistema operativo de red. 
• Consiste en un software que posibilita la comunicación de un sistema informático con otros \nequipos en el ámbito de una red). 
En los casos más complejos, un servicio de directorio es el repositorio central de la información para una 
Plataforma de Entrega de Servicios. 
Por ejemplo, explorando "computadoras" usando un servicio de directorio, se puede obtener una lista 
de computadoras disponibles y la información necesaria para tener acceso. 
La réplica y la distribución tienen significados muy distintos en el diseño y la gestión de un servicio del 
directorio. 
• La réplica se utiliza para indicar que el mismo espacio de nombres de un directorio (los mismos 
objetos) está copiado en otro servidor de directorio por razones de redundancia y de 
rendimiento de procesamiento. 
El espacio de nombres replicado es gobernado por la misma autoridad. 
• La distribución de un servicio de directorio tiene por fin la mejora de la disponibilidad, \nescalabilidad y distribución de la carga de trabajo del servicio entre varios servidores. 
• La distribución implica que el servicio de directorio se organiza en una red de servidores 
interconectados que trabajan juntos para proporcionar un servicio de directorio coherente y \nescalable. Cada servidor puede contener una parte de los datos del directorio y puede ser 
responsable de un subconjunto específico de operaciones. 
Ejemplo 
Un servicio de directorio sencillo es, por ejemplo, un servicio de nombres para corresponder los 
nombres de los recursos de la red con sus respectivas direcciones de red. 
Con este tipo de servicio de directorio, un usuario no tiene que recordar la dirección física de los 
diferentes recursos de la red, pues con saber simplemente su nombre estará accediendo a tal recurso 
demandado. 
Cada recurso de la red se considera como un objeto en el servidor de directorio, donde la información 
de un recurso en particular se almacena como atributos de ese objeto.

---

Administración del Sistema Operativo y software de Base 
12 
La información que representa un objeto se establece de forma segura, accediendo a tales objetos 
usuarios con los permisos adecuados para poder manipular dicha información. 
Directorios más sofisticados son diseñados con multitud de características y preferencias para poder 
manipular la información del directorio, según la dificultad de gestión que su administrador pretenda 
manejar. 
2.1. Estándares y protocolos 
2.1.1. X.500 
X.500 es un conjunto de estándares de redes de ordenadores de la UIT-T, ITU-T en inglés (Sector de 
Normalización de las Telecomunicaciones), sobre servicios de directorio. 
 
 
 
 
+ Info 
El UIT-T de la Unión Internacional de Telecomunicaciones (UIT, 
ITU en inglés), con sede en Ginebra (Suiza), es el órgano 
permanente de esta organización encargado de estudiar los 
aspectos técnicos, de explotación y tarifarios, y de publicar 
normativas al respecto, con el fin de promover la normalización de 
las telecomunicaciones a nivel mundial. 
Fue conocido hasta 1992 como Comité Consultivo Internacional 
Telefónico y Telegráfico (CCITT). 
 
 
El estándar X.500 se desarrolló conjuntamente con la ISO como parte del Modelo de interconexión de 
sistemas abiertos, para usarlo como soporte del correo electrónico X.400. 
X.500 es un protocolo de la capa de Aplicación. No es fiable. 
Los protocolos definidos por X.500 incluyen: 
• Protocolo de acceso al directorio (DAP). 
El protocolo LDAP fue creado como una versión liviana de X.500 y terminó por reemplazarlo. 
Por esta razón algunos de los conceptos y estándares que utiliza LDAP provienen de la serie de 
protocolos X.500.

---

Administración del Sistema Operativo y software de Base 
13 
• El protocolo de sistema de directorio. 
• El protocolo de ocultación de información de directorio. 
• El protocolo de gestión de enlaces operativos de directorio. 
 
 
 
 
+ Info 
Dentro de la serie X.500, la especificación que ha resultado ser la 
más difundida no trata de protocolos de directorio, sino de 
certificados de clave pública: X.509. 
 
2.1.2. Protocolo LDAP 
El Lightweight Directory Access Protocol, LDAP, en español protocolo ligero de acceso a directorios, \nes un protocolo a nivel de aplicación que permite el acceso a un servicio de directorio ordenado y 
distribuido para buscar diversa información en un entorno de red. 
El protocolo LDAP es un estándar de la industria, independiente del proveedor, utilizado para el 
acceso y el mantenimiento distribuido de servicios de información de directorio sobre un Protocolo 
de Internet (IP). 
Un árbol de directorio LDAP puede reflejar límites políticos, geográficos u organizacionales, 
dependiendo del modelo elegido. 
Los despliegues actuales de LDAP tienden a usar nombres de Sistema de Nombres de Dominio (DNS) 
para estructurar los niveles más altos de la jerarquía, y conforme se desciende en el directorio pueden 
aparecer entradas que representan personas, unidades organizacionales, impresoras, documentos, 
grupos de personas o cualquier cosa que representa una entrada dada en el árbol (o múltiples \nentradas). 
Se almacena la información de autenticación (usuario y contraseña) y es utilizado para autenticarse, 
aunque es posible almacenar otra información (datos de contacto del usuario, ubicación de diversos 
recursos de la red, permisos, certificados, etc). 
La versión actual es LDAPv3, y se encuentra definido en el RFC 4511(una hoja de ruta de las \nespecificaciones técnicas está suministrada por la RFC 4510).

---

Administración del Sistema Operativo y software de Base 
14 
 
 
 
Resumiendo 
LDAP es un protocolo de acceso unificado a un conjunto de 
información sobre una red. 
 
 
Los servicios de directorio desempeñan un papel importante en el desarrollo de aplicaciones de intranet \ne Internet al permitir compartir información sobre usuarios, sistemas, redes, servicios y aplicaciones en 
toda la red. 
Los servicios de directorio pueden proporcionar cualquier conjunto organizado de registros con una \nestructura jerárquica, como por ejemplo un directorio de correo electrónico corporativo, como lo hace 
una guía telefónica es una lista de suscriptores con un número de teléfono. 
LDAP se especifica en una serie de publicaciones de seguimiento estándar del Grupo de trabajo de 
ingeniería de Internet (IETF) llamadas Solicitud de comentarios (RFC), utilizando el lenguaje de 
descripción ASN.1. 
La notación de sintaxis abstracta uno (ASN.1) es un lenguaje de descripción de interfaz estándar para 
definir estructuras de datos que se pueden serializar y deserializar de una manera multiplataforma. Se 
utiliza ampliamente en telecomunicaciones y redes informáticas, y especialmente en criptografía). 
La última especificación es la Versión 3, publicada como RFC 4511 (RFC4510 proporciona una hoja de 
ruta para las especificaciones técnicas). 
Un uso común de LDAP es proporcionar un lugar central para almacenar nombres de usuario y 
contraseñas. Esto permite que muchas aplicaciones y servicios diferentes se conecten al servidor LDAP 
para validar usuarios. 
LDAP se basa en un subconjunto más simple de los estándares contenidos en el estándar X.500. Debido 
a esta relación, LDAP a veces se denomina X.500-lite. 
La descripción general del funcionamiento del protocolo es la siguiente: 
• Un cliente inicia una sesión LDAP conectándose a un servidor LDAP, llamado Directory System 
Agent (DSA). 
De forma predeterminada en el puerto TCP y UDP 389, o en el puerto 636 para LDAPS (LDAP 
sobre SSL, ver más abajo). 
• El cliente luego envía una solicitud de operación al servidor, y un servidor envía respuestas a 
cambio. 
Con algunas excepciones, el cliente no necesita esperar una respuesta antes de enviar la 
siguiente solicitud, y el servidor puede enviar las respuestas en cualquier orden. Toda la 
información se transmite mediante las reglas de codificación básicas (BER).

---

Administración del Sistema Operativo y software de Base 
15 
El cliente puede solicitar las siguientes operaciones, que veremos más adelante con mayor detalle: 
• StartTLS: use la extensión LDAPv3 Transport Layer Security (TLS) para una conexión segura. 
• Vincular: autenticar y especificar la versión del protocolo LDAP. 
• Buscar: buscar y / o recuperar entradas del directorio. 
• Comparar: prueba si una entrada con nombre contiene un valor de atributo determinado. 
• Agregar, eliminar o modificar una entrada. 
• Modificar nombre distinguido (DN): mover o cambiar el nombre de una entrada. 
• Abandonar: cancelar una solicitud anterior. 
• Operación extendida: operación genérica utilizada para definir otras operaciones. 
• Desvincular: cierre la conexión (no a la inversa de Bind). 
• El servidor también puede enviar "Notificaciones no solicitadas" que no son respuestas a 
ninguna solicitud, por ejemplo, antes de que se agote el tiempo de espera de la conexión. 
 
 
 
 
+ Info 
Un método alternativo común para proteger la comunicación 
LDAP es utilizar un túnel SSL. 
El puerto predeterminado para LDAP sobre SSL es 636. 
El uso de LDAP sobre SSL era común en LDAP Versión 2 (LDAPv2) 
pero nunca se estandarizó en ninguna especificación formal. Este 
uso ha quedado obsoleto junto con LDAPv2, que se retiró 
oficialmente en 2003. 
 
2.2. eDirectory de Novell \neDirectory es un producto de software de servicio de directorio compatible con X.500 de NetIQ. 
Anteriormente propiedad de Novell, el producto también se conocía como Novell Directory Services ( 
NDS ) y, en ocasiones, se denominaba NetWare Directory Services.

---

Administración del Sistema Operativo y software de Base 
16 
NDS fue lanzado inicialmente por Novell en 1993 para Netware 4, reemplazando el mecanismo de \nenlace de Netware utilizado en versiones anteriores, para administrar de manera centralizada el acceso 
a los recursos en múltiples servidores y computadoras dentro de una red determinada. \neDirectory es una base de datos jerárquica y orientada a objetos que se utiliza para representar 
ciertos activos en una organización en un árbol lógico, incluidas organizaciones, unidades 
organizativas, personas, puestos, servidores, volúmenes, estaciones de trabajo, aplicaciones, 
impresoras, servicios y grupos, por nombrar solo algunos. 
Funciones \neDirectory utiliza la herencia dinámica de derechos, que permite controles de acceso tanto globales 
como específicos. 
Los derechos de acceso a los objetos en el árbol se determinan en el momento de la solicitud y están 
determinados por los derechos asignados a los objetos en virtud de su ubicación en el árbol, las \nequivalencias de seguridad y las asignaciones individuales. 
El software admite la creación de particiones en cualquier punto del árbol, así como la replicación de 
cualquier partición en cualquier número de servidores, esta replicación entre servidores se produce 
periódicamente utilizando deltas de los objetos. Cada servidor puede actuar como maestro de la 
información que contiene (siempre que la réplica no sea de solo lectura), y las réplicas se pueden filtrar 
para incluir solo atributos definidos para aumentar la velocidad (por ejemplo, una réplica se puede 
configurar para incluir solo un nombre y número de teléfono para su uso en una libreta de direcciones 
corporativa. 
El software: 
• Admite integridad referencial. 
Propiedad de los datos que afirman que todas sus referencias son válidas. 
En el contexto de las bases de datos relacionales, requiere que si un valor de un atributo 
(columna) de una relación (tabla) hace referencia a un valor de otro atributo, entonces el valor 
referenciado debe existir. 
• Admite replicación multimaestro. 
Método de replicación de la base de datos que permite que los datos sean almacenados por un 
grupo de computadoras y actualizados por cualquier miembro del grupo. 
Todos los miembros responden a las consultas de datos de los clientes. 
El sistema de replicación multimaestro es responsable de propagar las modificaciones de datos 
realizadas por cada miembro al resto del grupo y resolver los conflictos que puedan surgir entre 
cambios simultáneos realizados por diferentes miembros.

---

Administración del Sistema Operativo y software de Base 
17 
• Arquitectura de autenticación modular. 
Cuando hablamos de eDirectory, hemos de mencionar su arquitectura distribuida, que juega un 
rol específico. El sistema está diseñado para que su base de datos de directorio y sus servicios se 
puedan ejecutar y gestionar en múltiples servidores o ubicaciones de red de manera eficiente y 
colaborativa. 
Por otro lado, podemos hablar de la arquitectura modular de autenticación de eDirectory, \nespecialmente cuando se emplea NMAS (Novell Modular Authentication Service), que permite 
una integración profunda con diversas tecnologías, ofreciendo una solución de autenticación 
flexible y escalable. 
NMAS (Novell Modular Authentication Service) implementa una solución flexible y escalable 
para la autenticación en eDirectory, facilitando la utilización de múltiples métodos como 
contraseñas, autenticación biométrica, y tarjetas inteligentes. Por otro lado, facilita la 
autenticación multinivel, donde se pueden combinar diversos factores para mejorar la 
seguridad. Asimismo, permite la personalización de políticas de autenticación según las 
necesidades de usuarios o grupos específicos, integrándose con tecnologías existentes como 
Active Directory y OpenLDAP. 
Gracias a su diseño modular, NMAS soporta la federación de identidades, lo que facilita la 
autenticación entre diferentes dominios y sistemas de confianza. Interfaces de programación o 
APIs como ADSI, JDBC, ODBC, interfaces de directorio como JNDI, protocolos como SOAP o \nestándares como DSML, pueden servir para iniciar el proceso de autenticación. 
• LDAP es el protocolo subyacente que permite a NMAS comunicarse con eDirectory. A 
través de LDAP, NMAS obtiene información de usuarios, esquemas de autenticación y 
políticas configuradas. LDAP facilita que NMAS se integre con otros servicios de directorio 
como Active Directory, OpenLDAP, etc., facilitando la federación de identidades. 
• JDBC/ODBC: Si NMAS necesita verificar información almacenada en una base de datos (por \nejemplo, credenciales adicionales o atributos biométricos), puede utilizar JDBC (para 
aplicaciones Java) u ODBC (para otras aplicaciones) para conectarse a la base de datos y \nejecutar consultas. Las bases de datos pueden servir como repositorios para datos de 
autenticación que no encajan dentro del esquema estándar de eDirectory. 
• ADSI: Aunque no hay una integración directa con ADSI, NMAS puede trabajar con 
conectores y puentes que mapean los esquemas de eDirectory y Active Directory, 
permitiendo la sincronización de usuarios y grupos. NMAS puede extender las políticas de 
autenticación a usuarios y grupos provenientes de Active Directory. 
• SOAP y DSML permiten a NMAS comunicarse con sistemas que no soportan LDAP de 
forma nativa. Esto es útil para integrar sistemas legados o aplicaciones personalizadas en la 
arquitectura de autenticación. SOAP puede utilizarse para exponer servicios de 
autenticación de eDirectory como servicios web, permitiendo su consumo por parte de 
otras aplicaciones. 
• JNDI (Java Naming and Directory Interface) proporciona un mecanismo estándar para 
acceder a diversos servicios de nombres y directorios, incluyendo LDAP. NMAS puede 
utilizar JNDI para buscar y localizar los recursos necesarios para la autenticación, como 
módulos de autenticación específicos o fuentes de datos.

---

Administración del Sistema Operativo y software de Base 
18 
2.3. Directorio activo de Microsoft 
Active Directory (AD) es el servicio de directorio desarrollado por Microsoft para gestionar de manera 
centralizada los recursos de red en entornos Windows. Su propósito principal es permitir que usuarios, \nequipos y servicios trabajen de forma coordinada bajo una única estructura jerárquica de autenticación, 
autorización y políticas. 
Evolución histórica y versiones 
Active Directory fue introducido por primera vez en Windows 2000 Server, marcando un salto frente al 
modelo anterior basado en dominios NT. En versiones como Windows Server 2003, se mantuvo como 
pilar central de la infraestructura de red, y a partir de Windows Server 2008 y 2008 R2, pasó a 
denominarse formalmente Servicios de dominio de Active Directory (AD DS). 
Durante años, herramientas como dcpromo eran fundamentales para instalar un controlador de 
dominio, aunque en versiones modernas como Windows Server 2016 o 2019, el proceso se gestiona a 
través del Administrador del servidor. 
También cambió la forma de administración: antiguamente se usaba la consola dsa.msc, y hoy en día se 
integra con PowerShell, Server Manager y portales híbridos como Azure AD Connect. 
Estructura jerárquica en profundidad 
La estructura de Active Directory es jerárquica y escalable: 
• Dominios: son el núcleo de la administración. Agrupan objetos (usuarios, equipos, impresoras, \netc.) que comparten políticas y una base común de autenticación. 
• Árboles: agrupan dominios que comparten un espacio de nombres contiguo, como \nempresa.local y ventas.empresa.local. 
• Bosques: conjunto de árboles, aunque sus dominios no compartan espacio de nombres. Entre \nellos se establecen relaciones de confianza, permitiendo autenticaciones cruzadas sin duplicar 
identidades. 
Esta estructura permite centralizar el control, aunque la red esté distribuida geográficamente. 
Componentes críticos del sistema 
• Controlador de Dominio (Domain Controller o DC): servidor que almacena y replica la base de 
datos de AD, autentica usuarios y aplica políticas mediante Kerberos. 
• DNS: crítico para resolver nombres de dominio dentro de la red; sin él, los clientes no podrían \nencontrar el controlador de dominio.

---

Administración del Sistema Operativo y software de Base 
19 
• LDAP (Lightweight Directory Access Protocol): permite consultar/modificar la base de datos 
de objetos. 
• DHCP: aunque no es parte directa de AD, se suele usar conjuntamente para asignar IPs, con 
integración mediante políticas de asignación por nombre de host. 
• SYSVOL y NTDS: carpetas internas en el DC donde se almacenan scripts, políticas y la propia 
base de datos del directorio. 
Gestión de políticas y administración 
Las Políticas de Grupo (GPOs) permiten aplicar configuraciones masivas a través de Unidades 
Organizativas (OUs). Por ejemplo, en una empresa: 
• Se puede restringir el acceso a puertos USB solo en el departamento financiero. 
• Se puede forzar el cambio de contraseña cada 60 días para todo el dominio. 
Estas políticas son heredables, aunque pueden bloquearse o sobreescribirse por niveles inferiores. 
Herramientas como gpresult o rsop.msc ayudan a diagnosticar qué políticas se aplican realmente a un \nequipo. 
Integración con servicios Microsoft y nube 
AD se integra con: 
• Exchange Server: las cuentas de usuario pueden vincularse directamente a buzones de correo. 
• System Center: permite administración centralizada de equipos, actualizaciones y software. 
• Azure Active Directory (Azure AD): para sincronización con la nube y habilitación de inicio de 
sesión único (SSO) en entornos híbridos. 
• PowerShell: mediante módulos como ActiveDirectory, se pueden automatizar tareas (por \nejemplo, crear usuarios en masa, deshabilitar cuentas inactivas o mover objetos entre OUs). 
Aplicaciones prácticas en entornos reales 
• Universidades: los estudiantes acceden a laboratorios con restricciones; los profesores tienen 
privilegios elevados para instalar software docente. 
• Pymes: un único dominio con OUs por departamentos, control de permisos básicos y mapeo 
automático de carpetas compartidas. 
• Corporaciones: múltiples dominios y bosques, con políticas adaptadas a cada región, integración 
con Office 365 y autenticación multifactor.

---

Administración del Sistema Operativo y software de Base 
20 
Requisitos técnicos y configuración 
Para implementar un dominio AD se requiere: 
• Un sistema operativo Windows Server (2000, 2003, 2008, 2012, 2016 o superior). 
• Protocolo TCP/IP configurado manualmente con IP fija (no por DHCP). 
• Un servidor DNS funcional y correctamente configurado. 
• Al menos 250 MB de espacio libre en disco con formato NTFS. 
• Conexión estable en redes LAN o WAN según el caso. 
 
 
 
 
+Info 
Windows 11, al igual que Windows 10, no incluye Active Directory 
como servicio de servidor, pero sus ediciones Pro, Enterprise y 
Education pueden formar parte de un dominio corporativo, lo que 
permite a empresas usarlo como cliente dentro de una 
infraestructura de red centralizada. 
 
Interfaces de desarrollo y compatibilidad 
Mediante las ADSI (Active Directory Service Interfaces) es posible crear aplicaciones y scripts en 
lenguajes como C++, VBScript o PowerShell que consulten, modifiquen o sincronicen objetos del 
directorio sin preocuparse por el protocolo subyacente. 
También existen extensiones como MAPI o LDAP SDKs que permiten conectar aplicaciones de terceros 
o clientes ligeros. 
En resumen 
Active Directory es mucho más que una base de datos: es una plataforma completa para el control de 
acceso, la administración de recursos y la seguridad a gran escala. Su arquitectura jerárquica, sus 
capacidades de integración y su soporte para infraestructuras híbridas lo convierten en una solución 
indispensable para la gestión de redes en el ecosistema Microsoft, desde una pequeña empresa hasta un \nentorno multinacional.

---

Administración del Sistema Operativo y software de Base 
21 
 
 
 
+Info 
Active Directory es un servicio de directorio que centraliza la 
administración de una red, permitiendo gestionar y controlar todos 
sus componentes lógicos como usuarios, equipos y recursos 
compartidos de manera unificada. 
 
2.3.1. Dominio en Active Directory 
Un dominio en Active Directory es un conjunto de ordenadores conectados a una red los cuales cuentan 
con un equipo servidor para administrar las cuentas de usuario y credenciales de la red. 
Veamos diferentes conceptos en relación con los dominios: 
• Relación de confianza o trust entre dominios. 
Es la relación entre los diferentes dominios que podemos tener en una red y que tienen 
contacto. 
En una red no solamente podremos tener un dominio, sino varios de ellos, que pueden o no \nestar en contacto unos con otros, por tanto, Active Directory actúa también como un 
controlador de dominio, ya que se pueden crear distintos dominios y gestionar los permisos e 
interacción en cada uno de ellos. 
• Objeto. 
Un objeto es el nombre genérico que utilizamos para referirnos cualquier componente dentro 
de un directorio. 
Los objetos se dividen en tres tipos distintos: 
• Usuarios: 
Las credenciales de acceso a estaciones de trabajo. 
• Recursos: 
Los elementos disponibles para un usuario en función de sus permisos (carpetas 
compartidas, impresoras, etc.). 
• Servicios: 
Las funcionalidades a las puede acceder un usuario, como acceso a Internet, correo \nelectrónico, informes estadísticos etc.

---

Administración del Sistema Operativo y software de Base 
22 
• Unidad organizativa. 
Es un contenedor de objetos como impresoras, usuarios, grupos etc., organizados mediante 
subconjuntos estableciendo así una jerarquía, así se puede ver fácilmente de un vistazo la 
jerarquía de nuestro dominio y se realiza la asignación de permisos fácilmente según los objetos 
contenidos. 
• Árbol. 
Mediante la estructura de árbol, podemos dividir en partes un directorio Activo, se identifica 
mejor un dominio de otro y por tanto se facilita su gestión. Un usuario que pertenezca a un 
dominio también será reconocido por los dominios que pertenezcan al dominio principal. 
Es un conjunto de dominios que dependen de una raíz común y están organizados en una 
determinada jerarquía, también llamada DNS común. 
• Bosque. 
En un bosque nos encontramos con todos los dominios existentes contenidos en él. 
Estamos subiendo un escalón (nivel) en la jerarquía. 
Cada dominio dentro de un bosque tendrá unas relaciones de confianza transitivas o 
intransitivas determinadas, que están construidas automáticamente, pero que podremos 
modificar adaptándolas a nuestras necesidades. 
En un bosque existirán distintos árboles de dominio con imprescindiblemente diferentes 
nombres. 
Al instalar el primer dominio, estamos creando la raíz de un árbol, y encima de este, en un nivel 
superior, la raíz de un bosque. (Un bosque, siempre tiene como mínimo un dominio raíz dentro 
de él). 
Confianza entre dominios 
En una red no solamente podremos tener un dominio, sino varios de ellos, que pueden o no estar en 
contacto unos con otros, por tanto, Active Directory actúa también como un controlador de dominio, 
ya que se pueden crear distintos dominios y gestionar los permisos e interacción en cada uno de ellos. 
Active Directory usa el protocolo V5 de Kerberos, aunque también soporta NTLM y usuarios webs 
mediante autentificación SSL/TLS. 
Relación de confianza o trust entre dominios, es la relación entre los diferentes dominios que podemos 
tener en una red y que tienen contacto.

---

Administración del Sistema Operativo y software de Base 
23 
Para permitir que los usuarios de un dominio accedan a recursos de otro dominio, Active Directory usa 
una relación de confianza, llamada también trust. 
Esta relación trust: 
• Es creada automáticamente cuando se crean nuevos dominios. 
• La confianza es la relación existente entre dos dominios, dos árboles o dos bosques. 
• Los límites de la relación de confianza no son marcados por dominio, sino por el bosque al cual 
pertenece. 
• Hay dos tipos: 
• Confianza transitiva: 
Se extienden de forma automática, en ambos sentidos, en dominios de AD que tienen 
relación (de dos vías que existen entre dominios en Active Directory). 
• Confianza de acceso directo: 
Se define de forma explícita (confianza explícita) para dos dominios, de forma que 
podamos acceder directamente de uno a otro. 
Crea accesos directos entre dos dominios en la estructura de dominios. Este tipo de 
relaciones permite incrementar la conectividad entre dos dominios, reduciendo las 
consultas y los tiempos de espera para la autenticación. 
• Confianza entre bosques: 
La Confianza entre bosques permite la interconexión entre bosques de dominios, creando 
relaciones transitivas de doble vía. 
Depende de cada versión (por ejemplo, en Windows 2000, las confianzas entre bosques son de 
tipo explícito, al contrario de Windows Server 2003). 
 
 
 
 
Resumiendo 
Existen relaciones de confianza transitivas, donde las relaciones de 
confianza de Active Directory pueden ser un acceso directo (une 
dos dominios en árboles diferentes, transitivo, una o dos vías), 
bosque (transitivo, una o dos vías), reino (transitivo o no 
transitivo, una o dos vías), o externo (no transitivo, una o dos 
vías), para conectarse a otros bosques o dominios que no son de 
Active Directory.

---

Administración del Sistema Operativo y software de Base 
24 
2.3.2. Direccionamientos a recursos 
Los direccionamientos a recursos de Active Directory son estándares con la Convención Universal de 
Nombres (UNC), Localizador Uniforme de Recursos (URL) y Nombres de LDAP. 
Cada objeto de la red posee un nombre de distinción (en inglés, Distinguished name (DN)), así una 
impresora llamada Imprime en una Unidad Organizativa (en inglés, Organizational Units, OU) llamada 
Ventas y un dominio foo.org, puede escribirse de las siguientes formas para ser direccionado: 
• En DN sería CN=Imprime,OU=Ventas,DC=foo,DC=org, donde: 
• CN es el nombre común (en inglés, Common Name). 
• DC es clase de objeto de dominio (en inglés, Domain object Class). 
• En forma canónica sería foo.org/Ventas/Imprime. 
Los otros métodos de direccionamiento constituyen una forma local de localizar un recurso. 
• Distinción de Nombre Relativo (en inglés, Relative Distinguised Name (RDN)), que busca un 
recurso sólo con el Nombre Común (CN). 
• Globally Unique Identifier (GUID), que genera una cadena de 128 bits que es usado por Active 
Directory para buscar y replicar información. 
Ciertos tipos de objetos poseen un Nombre de Usuario Principal (en inglés, User Principal Name 
(UPN)) que permite el ingreso abreviado a un recurso o un directorio de la red. Su forma es 
objetodered@dominio. 
2.3.3. Diferencias entre Windows NT y Active Directory 
A diferencia del anterior sistema de administración de dominios de Windows NT Server, que proveía 
únicamente el dominio de administración, Active Directory permite también crear estructuras 
jerárquicas de dominios y subdominios, facilitando la estructuración de los recursos según su 
localización o función dentro de la organización a la que sirven. 
Otra diferencia importante es el uso de estándares como X.500 y LDAP para el acceso a la información. 
2.3.4. Conclusión sobre Active Directory 
Active Directory es una herramienta muy importante de cara a la centralización de recursos en un \nentorno de trabajo basado en equipos informáticos. Gracias a él, no tendremos la necesidad de realizar \nel mantenimiento individualizado en las estaciones de trabajo, ya que todo será gestionable desde un 
servidor central o varios. Además, la estructura es muy intuitiva para así facilitar la asignación de 
permisos y recursos.

---

Administración del Sistema Operativo y software de Base 
25 
Por otro lado, debemos tener presente que Active directorio es un sistema de dominio con licencia de 
pago perteneciente a Microsoft. Existen aplicaciones gratuitas que también ofrecen este tipo 
funcionalidades como por ejemplo Open LDAP, Mandriva Directory Server o incluso Samba. Y es por \nesto que las empresas cada vez más están optando por estas soluciones para no tener la necesidad de 
pagar licencias de software. 
 
 
 
 
Importante 
Si el equipo donde un usuario trabaja se rompe, únicamente el 
usuario tiene que utilizar cualquier otro ordenador conectado a la 
red, y al autentificarse dispondrá de la misma configuración y 
servicios que en su ordenador habitual. 
Únicamente no tendrá acceso a los datos que haya podido guardar \nen el disco duro propio del ordenador, por ello no se recomienda 
hacer el almacenamiento de esta forma, si no en los discos duros 
de los servidores. 
 
2.3.5. Introducción a Active Directory Domain Services (AD DS) 
Si bien el apellido 'Domain Services' ya empieza a asomar en el 2003 para hablar de los distintos 
componentes de Active Directory, se acaba formalizando su uso terminológico con la versión de 
Windows Server del 2008. El término Active Directory Domain Services (AD DS) fue acuñado en 
Windows Server 2008, anteriormente se conocía como Active Directory desde febrero del año 2000. 
Hoy, AD DS, continúa siendo un componente esencial en las últimas versiones de Windows Server, 
incluyendo Windows Server 2016, 2019 y 2022. 
Ya sabemos que un directorio es una estructura jerárquica que almacena información acerca de los 
objetos de la red. Un servicio de directorio, como Active Directory Domain Services (AD DS), 
proporciona los métodos para almacenar los datos de directorio y hacer que estos datos estén 
disponibles para los usuarios y administradores de la red. Por ejemplo, AD DS almacena información 
acerca de las cuentas de usuario, como nombres, contraseñas, números de teléfono, etc., y permite que 
otros usuarios autorizados de la misma red tengan acceso a dicha información. 
Se almacena información acerca de los objetos de una red y facilita su búsqueda y uso por parte de los 
usuarios y administradores, usando un almacén de datos estructurado como base para una organización 
jerárquica lógica de la información del directorio. 
Este almacén de datos, (conocido como directorio), contiene información sobre los objetos de Active 
Directory. Estos objetos suelen incluir recursos compartidos como servidores, volúmenes, impresoras y 
las cuentas de equipo y usuario de red.

---

Administración del Sistema Operativo y software de Base 
26 
La seguridad se integra a través de la autenticación de inicio de sesión y el control de acceso a los 
objetos del directorio. Con un único inicio de sesión de red, los administradores pueden administrar los 
datos del directorio y la organización a través de su red, y los usuarios de red autorizados pueden tener 
acceso a los recursos en cualquier parte de la red. La administración basada en directiva facilita la 
administración de incluso las redes más complejas. Para obtener más información sobre la seguridad de 
Active Directory, consulte información general sobre seguridad. 
También incluye: 
• Conjunto de reglas, el esquema, que define las clases de objetos y atributos incluidos en el 
directorio, las restricciones y los límites de las instancias de estos objetos y el formato de sus 
nombres. 
• Catálogo global que contiene información sobre todos los objetos del directorio. Esto permite a 
los usuarios y administradores buscar información de directorio independientemente del 
dominio del directorio que contenga realmente los datos. 
• Un mecanismo de consulta e índice, de modo que los usuarios o las aplicaciones de red puedan 
publicar y encontrar los objetos y sus propiedades. 
• Un servicio de replicación que distribuye los datos de directorio a través de una red. Todos los 
controladores de dominio de un dominio participan en la replicación y contienen una copia 
completa de toda la información de directorio de su dominio. Cualquier cambio en los datos del 
directorio se replica en todos los controladores de dominio del dominio. 
 
 
 
 
+ Info 
Consulta más información en la página web oficial de Microsoft. 
https://docs.microsoft.com/es-es/windows-server/identity/ad-
ds/get-started/virtual-dc/active-directory-domain-services-
overview 
 
2.3.6. Herramientas de gestión de Active Directory 
Active Directory resulta muy complejo, por lo que se han desarrollado diferentes (por terceros) para 
facilitar las funciones administrativas de AD. 
Existen muchas herramientas, algunas de ellas las nombramos a continuación.

---

Administración del Sistema Operativo y software de Base 
27 
2.3.6.1. Servidor SolarWinds y Monitor de aplicaciones 
SolarWinds es una de las mejores herramientas de administración de redes y sistemas. 
Disponible de una versión de prueba gratuita de 30 días. 
Su amplia gama de funcionalidades la convierten en una gran herramienta para monitorear y 
administrar Active Directory, ayuda con la administración de AD de las siguientes formas: 
• Primero, la herramienta cuenta con monitoreo de controlador de dominio que monitorea varios 
parámetros operativos, como: 
• Indicará cuándo el uso de la CPU es demasiado alto. 
• Indicará cuando una cuenta de usuario está bloqueada. 
• Indicará cuando hay un problema de inicio de sesión. 
• También monitoreará los contadores de objetos NTDS, ayudando a reducir la sobrecarga del 
servidor. 
• Ofrece información sobre varias estadísticas de LDAP, incluidos los subprocesos activos de 
LDAP, el tiempo de enlace, las sesiones de cliente y los enlaces y búsquedas exitosos por 
segundo. 
• Pueden enviar notificaciones cuando fallan los servidores de directorios para replicar, un suceso 
que puede evitar que los usuarios accedan a las carpetas y archivos. 
• Proporciona estadísticas de rendimiento detalladas relacionadas con los servicios de directorio, 
como: 
• El sistema de archivos distribuido. 
• La replicación dfs. 
• La mensajería entre sitios. 
• El cliente dns. 
• La hora de Windows. 
• Rpc. 
• Los servicios de servidor y estación de trabajo. 
• Los servicios de dominio de active directory. 
• Etc.

---

Administración del Sistema Operativo y software de Base 
28 
Esta herramienta no solo supervisará los servicios de Active Directory sino también los servidores en 
sí y las aplicaciones que se ejecutan en ellos. 
Este paquete completo puede escalar desde las redes más pequeñas a redes grandes de sitios múltiples 
con cientos de servidores físicos y virtuales, y monitorear servidores en entornos de nube como los de 
Amazon Web Services y Microsoft Azure. 
El monitor SolarWinds Server & Application detectará inicialmente de forma automática hosts y 
dispositivos en su red, y después en un segundo análisis de detección detectará las aplicaciones que se \nejecutan en cada servidor. 
Una vez que está en funcionamiento, usar esta herramienta es muy sencillo, gracias a su interfaz de 
usuario muy intuitiva, por ejemplo, simplemente haciendo clic en Detalles del nodo, se muestra el 
rendimiento del nodo y la información de estado. 
2.3.6.2. ENow Compass 
Monitorea la replicación DFS / FRS, los problemas de resolución de nombres de DNS y ayuda a 
solucionar problemas de aplicaciones (costosas consultas LDAP) para ayudarlo a mantener su AD 
funcionando sin problemas. 
Compass proporciona más de 50 informes que incluyen una auditoría del grupo de administradores de 
dominio, una identificación y eliminación de cuentas de usuario inactivas y una identificación de roles 
FSMO, entre otras cosas. 
Es una herramienta única y concisa que proporciona un panel intuitivo y fácil de usar que ayuda a 
identificar problemas antes de que se conviertan en interrupciones. 
Se puede obtener una prueba gratuita de 14 días. 
 
 
 
 
+ Info 
La brújula de ENow Software lo ayuda a identificar problemas 
ocultos en su entorno antes de que se vea comprometido. 
Puede consultar más información en su web: 
https://www.enowsoftware.com/products/active-directory-
monitoring-and-reporting-free-trial

---

Administración del Sistema Operativo y software de Base 
29 
2.3.6.3. Monitor de Active Directory de Anturis 
Active Directory Monitor de Anturis ayuda a garantizar que todos los servicios funcionen sin problemas, 
lo cual es una parte importante del uso de administrar Active Directory. 
Esta herramienta puede: 
• Alertarlo sobre situaciones anormales por correo electrónico, SMS o notificaciones de llamadas 
de voz. 
• Establecer líneas de base de rendimiento para sus servidores de Active Directory y su estructura 
de replicación. 
Lo que le permite reconocer las tendencias de rendimiento y ayudar a reducir el riesgo de 
cuellos de botella antes de que tengan un impacto negativo en su rendimiento de AD. 
• Mostrar las sesiones de servidor y LDAP y establecer umbrales de alerta. 
• Mostrar las autenticaciones Kerberos y NTLM por segundo. 
Lo que le dará una idea de la carga general del servidor. 
• En cuanto a la replicación, supervisa: 
• Las métricas de rendimiento de la replicación. 
• Las sincronizaciones de replicación pendientes de dra. 
• Las operaciones de replicación pendientes de dra. 
Active Directory Monitor es un servicio basado en la nube y hay varios planes de suscripción disponibles 
con una prueba gratuita de 30 días. 
También está disponible una versión gratuita limitada a 5 monitores. 
2.3.6.4. Quest Active Administrator 
Esta es una solución de software de administración de Active Directory completa e integrada., que 
facilita cumplir con los requisitos de auditoría y las necesidades de seguridad. 
Entre las características principales de la herramienta: 
• Ofrece una administración integrada y proactiva. 
• Tiene informes y alertas intuitivos, lo que le permite monitorear e informar rápidamente sobre 
los cambios filtrando el tipo de evento, el usuario y la fecha, así como el inicio de sesión del 
usuario y la actividad de bloqueo. 
• Puede configurar alertas de eventos y automatizar acciones basadas en alertas.

---

Administración del Sistema Operativo y software de Base 
30 
El precio para Active Administrator es por cuenta de usuario habilitada en su AD con soporte por un 
año. Se debe comprar una licencia mínima para 20 cuentas de usuario. Se puede descargar una versión 
de prueba gratuita de 30 días. 
2.3.6.5. Kit Herramientas gratuitas de ManageEngine Active Directory 
ManageEngine es otro nombre común entre los administradores de sistemas y redes. 
Convierte a OpManager en una de las mejores herramientas de monitoreo de infraestructura de TI, y 
dispone de más de quince herramientas gratuitas de Active Directory que pueden ayudarlo a 
monitorear y administrar su infraestructura de AD. 
Algunos son programas independientes, mientras que otros son cmdlets de Powershell. 
Este kit de herramientas se incluye en una sola descarga, y algunas de las herramientas que incorpora 
son: 
• Herramienta de consulta AD. 
Permite leer cualquier dato de atributo que requiera del Directorio Activo (nombre de un 
usuario, apellido, teléfono, dirección, etc.) 
También puede ayudar a consultar objetos de grupo y computadora de Active Directory. 
• Herramienta CSV Generator. 
Genera un archivo CSV, que contiene una matriz personalizada de atributos de Active Directory \nespecificados por el usuario y sus valores correspondientes. 
El archivo resultante se puede usar para la administración masiva de Active Directory. 
• Último buscador de inicio de sesión. 
Enumera la última hora de inicio de sesión de todos los usuarios seleccionados en todos los 
controladores de dominio seleccionados en el dominio. 
Suele ser utilizado para actividades de auditoría y limpieza. 
• Administrador de sesión de terminal. 
Es un Powershell cmdlet que se puede utilizar para identificar y gestionar múltiples sesiones de 
terminal en un dominio desde un único punto. 
Con él, las sesiones de terminal para múltiples usuarios en un dominio se pueden administrar, 
desconectar o cerrar sesión.

---

Administración del Sistema Operativo y software de Base 
31 
• Directorio Activo de replicación. 
Permite a los administradores, por ejemplo: 
• Forzar la replicación de los datos en un dominio o todo el bosque. 
• La replicación de datos entre dos controladores de dominio. 
• Enumerar informes completos sobre la última replicación. 
• Puerto DMZ analizador. 
Permite a los administradores comprobar el estado de los puertos requeridos por cualquier 
aplicación de terceros para trabajar con Active Directory. 
Se puede usar para abrir puertos apropiados en firewalls. 
• Reportero de Roles de Controlador de Dominio. 
Enumera todos los controladores de dominio y sus respectivos roles en el Dominio. 
Puede ayudar a los administradores a identificar cualquier rol asociado de un controlador de 
dominio. 
• Local User Manager. 
Ayuda a los administradores a administrar cuentas de usuario dentro del dominio. 
Proporciona información sobre cuentas de usuarios locales y también permite la administración 
de estas cuentas mediante una interfaz de usuario conveniente. 
• Herramienta de monitoreo de controlador de dominio. 
Es una herramienta sencilla que descubre automáticamente los dominios y los muestra, 
indicando varios parámetros de los controladores de dominio, como: 
• La utilización de la CPU. 
• La utilización del disco. 
• La utilización de la memoria. 
• Otros parametros destacadas como: 
» Lecturas de página por segundo. 
» Escrituras de página por segundo. 
» Lecturas de archivos. 
» Escrituras de archivos. 
» Etc.

---

Administración del Sistema Operativo y software de Base 
32 
• Contraseña Policy Manager. 
Permite a cualquier usuario recuperar y visualizar la política de contraseñas de dominio y 
también permite a los usuarios con derechos administrativos editar la política de contraseña de 
dominio. 
Se utiliza para encontrar las cuentas de usuario con campos de contraseña establecidos en nulo, 
ayudando así a los administradores a evitar cualquier problema relacionado con la seguridad. 
• Buscador de duplicados de Active Directory. 
Esta utilidad de Powershell permite a los administradores identificar entradas duplicadas para 
los atributos de Active Directory en un dominio. 
Las entradas duplicadas se enumeran convenientemente, lo que ayuda a los administradores a 
garantizar un Active Directory libre de duplicados. 
• Reportero DNS. 
Ayuda a obtener información relacionada con la infraestructura DNS de la red. 
Puede mostrar los detalles de los registros DNS disponibles, sus tipos de registros 
correspondientes, las direcciones IP y los detalles del servicio simplemente ingresando un 
nombre de dominio. 
• Gestión de cuentas de servicio. 
Está diseñada para ayudarlo a crear, editar y eliminar fácilmente cuentas de servicio gestionadas 
con solo unos pocos clics. 
Esta herramienta no requiere conocimiento de PowerShell, la herramienta habitual utilizada 
para realizar estas tareas. 
• Informe de usuarios de contraseña débil. 
Ayuda a encontrar contraseñas débiles en Active Directory comparando las contraseñas de los 
usuarios con una lista de más de 100,000 contraseñas débiles de uso común. 
A continuación, puede obligar a los usuarios con contraseñas débiles a cambiar sus contraseñas 
la próxima vez que inicien sesión. 
3. Administrador de sistemas. Funciones 
Somos conscientes de que, en la actualidad, los sistemas informáticos son esenciales en cualquier 
organismo o empresa, de hecho, en muchos casos dependen totalmente del sistema informático para 
poder trabajar (farmacias, organismos oficiales, registro civil…), incluso e esencial para los usuarios 
domésticos.

---

Administración del Sistema Operativo y software de Base 
33 
El éxito y funcionamiento de muchas empresas depende de los servicios informatizados que tiene u 
ofrece. Es un elemento clave que aporta competitividad. Por ello, es muy importante la figura del 
administrador de sistema, un puesto de gran responsabilidad. 
El administrador del sistema debe encargarse de que todo el sistema informático funcione 
correctamente en todo momento, y que lo haga de manera óptima, (instalarlo y mantenerlo). 
Vamos a ver esta figura con mayor detalle. 
Cuando el tamaño y complejidad del sistema son muy grandes, las funciones del administrador de 
sistemas se pueden dividir en varios roles, siendo necesarios varios administradores que asuman dichos 
roles. 
Algunos de estos roles podrían ser: 
• Administrador de servidores. 
• Administrador de bases de datos. 
• Administrador de redes. 
• Administrador de seguridad. 
• Administrador de software de sistemas (Windows. / GNU/Linux / etc…), y/o de software de 
aplicación. 
 
 
 
 
Ejemplo 
En Debian GNU/Linux, para obtener la versión de Linux que 
tenemos instalada, ejecutamos: 
• lsb_release -a. 
 
Funciones y responsabilidades del administrador 
Un administrador de sistemas realiza gran cantidad de tareas. Nos vamos a centrar en las tareas diarias 
o cotidianas y no a las de gran envergadura, las cuales recaerían en un equipo dirigido por un director de 
sistemas.

---

Administración del Sistema Operativo y software de Base 
34 
Con respecto al administrador de sistemas, nos centraremos en un rol general (que asumirá los 
distintos roles). En definitiva, sus tareas más habituales son: 
• Realizar copias de seguridad. 
• Preparar los equipos nuevos. (Levantar servidores nuevos o puestos de usuario). 
• Cambiar la configuración hardware de los equipos. 
• Actualización del Sistema Operativo. 
• Actualización o instalación de nuevo Software de aplicación. 
• Configurar y mantener el acceso correcto a Internet. 
• Gestión de cuentas de usuarios. 
• Monitorizar el rendimiento del sistema. 
• Seguridad. 
• Recuperación ante fallos y caídas del sistema. 
• Atención a usuarios. 
• Información a dirección/organización. 
• Documentación del sistema. 
Vas a ver una explicación más detallada de cada una de estas funciones. 
3.1. Realizar copias de seguridad 
Es una tarea fundamental. En la medida de lo posible se debe automatizar. 
La labor del administrador consiste en: 
• Diseñar la política de seguridad: 
• Periodicidad de las copias. 
• Tipos de copia (total, parcial, incremental, etcétera). 
• Soportes que se utilizarán.

---

Administración del Sistema Operativo y software de Base 
35 
• Dónde se almacenarán. Es aconsejable: 
» Tener una copia fuera del centro de trabajo por si roban. 
» Guardar las copias en armarios ignífugos. 
» Si poseen información sensible, cerrar con llave los armarios. 
• Etcétera. 
• Determinar qué información se va a guardar. 
• Concienciar a los usuarios de que deben guardar los documentos en las carpetas habilitadas para \nello. Se realizarán copias de seguridad de estas carpetas. 
• Programar una ejecución automatizada y supervisarla. 
• Realizar pruebas de recuperación para asegurar que las copias se están realizando 
correctamente. 
• Recuperar información ante fallos o cuando un usuario lo requiera. 
3.1.1. Configuración de Copias de Seguridad automáticas 
Otro aspecto importante es la configuración de copias de seguridad automáticas. Automatizar este 
proceso garantiza que los datos estén protegidos de forma constante, sin depender de la intervención 
manual. 
En sistemas Windows, existen herramientas integradas como Historial de archivos y Copia de seguridad 
de Windows que permiten configurar este tipo de copias. Su configuración básica es sencilla y puede 
realizarse desde el panel de configuración del sistema. 
Historial de archivos: 
Esta herramienta realiza copias automáticas de las carpetas personales del usuario (Documentos, 
Imágenes, Escritorio, etc.). Para activarla: 
• Acceder a Configuración > Actualización y seguridad > Copia de seguridad (en Windows 10) o 
Configuración > Cuentas > Copia de seguridad de Windows (en Windows 11). 
• Seleccionar Agregar una unidad y elegir el disco externo o ubicación en red. 
• Activar la opción "Hacer copia de seguridad de mis archivos" (Windows 10) o "Hacer copia de 
seguridad automática de mis archivos" (Windows 11). 
Una vez activado, Windows guardará versiones de los archivos, permitiendo restaurar versiones 
anteriores o archivos eliminados accidentalmente. Estas copias se almacenan en la unidad externa o en 
red que hayas seleccionado.

---

Administración del Sistema Operativo y software de Base 
36 
Copia de seguridad de Windows (imagen del sistema): 
Permite crear una copia completa del sistema operativo, programas instalados y datos. Es \nespecialmente útil en caso de fallos graves del sistema, ya que permite restaurar todo el entorno 
operativo. 
1. Acceder a Panel de control > Sistema y seguridad > Historial de archivos. 
2. Seleccionar Crear una imagen del sistema en el menú lateral. 
3. Elegir la ubicación de destino (unidad externa, red o DVD) y seguir los pasos del asistente. 
Estas copias pueden almacenarse en un disco local, una unidad externa o en un servicio en la nube (una 
vez realizada), lo que facilita la recuperación de información en caso de fallo del sistema o pérdida de 
datos. 
Además de las herramientas nativas, existen aplicaciones de terceros como Acronis, Cobian Backup o 
Veeam, que ofrecen funcionalidades avanzadas: cifrado, compresión, notificaciones por correo, 
múltiples destinos y planificación más detallada. 
Tipos de copias 
Existen varios tipos de copias de seguridad que se utilizan para proteger los datos, cada uno con 
características y ventajas específicas. La elección del tipo de copia depende de las necesidades de 
recuperación, el tiempo disponible y la capacidad de almacenamiento. 
• Copia completa: realiza una copia exacta de todos los archivos y datos seleccionados en ese 
momento. Aunque permite una restauración rápida y sencilla, requiere más espacio de 
almacenamiento y más tiempo para su ejecución. 
• Copia incremental: tras una copia completa inicial, guarda solo los archivos que han cambiado 
desde la última copia (ya sea completa o incremental). Es más eficiente en tiempo y espacio, 
pero más compleja de restaurar, ya que requiere todas las copias anteriores. 
• Copia diferencial: también parte de una copia completa inicial, pero guarda todos los archivos 
que han cambiado desde esa copia completa. Ocupa más espacio que la incremental, pero su 
restauración es más rápida (solo se necesita la copia completa y la última diferencial). 
• Copia espejo: crea una duplicación exacta de los archivos seleccionados, sin compresión ni 
versiones anteriores. Es útil para una recuperación rápida, pero no protege frente a errores 
humanos como el borrado accidental. 
Una estrategia eficaz suele combinar varios tipos de copias de seguridad para equilibrar la velocidad, la \neficiencia de almacenamiento y la fiabilidad en la restauración. Asimismo, es recomendable programar 
las copias durante horarios de baja actividad y realizar pruebas periódicas de recuperación para verificar 
su eficacia.

---

Administración del Sistema Operativo y software de Base 
37 
3.2. Preparar los equipos nuevos 
Cuando se compra un nuevo equipo, ya sea para uso de servidor o para usuario, el administrador debe 
instalarle todo el software, tanto de base como las aplicaciones por defecto que usan en la empresa, 
teniendo en cuenta que tendrá que realizar también las actualizaciones necesarias. 
Es necesario configurar los distintos servicios, la red, recursos compartidos (ficheros, impresoras…) y 
hacerlo de forma que tengamos un rendimiento óptimo. 
3.3. Cambiar la configuración hardware de los equipos 
Cuando se añade un nuevo hardware de red (sistema de almacenamiento, impresora compartida, \netcétera), este debe ser reconocido por el sistema y los equipos que necesiten utilizarlo. 
Puede ser necesario: 
• Buscar incompatibilidades y buscar soluciones como: 
• Actualizar firmware del dispositivo. 
• Actualizar software de los equipos que lo utilizarán. 
• Buscar nuevos controladores del hardware nuevo. 
3.4. Actualización del sistema operativo 
La actualización del sistema operativo puede referirse a dos operaciones: 
• Actualizar a una versión superior del sistema operativo. Esto suele hacerse de forma guiada por 
un asistente, por lo que no vemos necesario entrar en ello. 
• Actualizar el sistema operativo. Añadiendo parches y actualizaciones que mejoran su 
rendimiento, eliminan vulnerabilidades o añaden nuevas funcionalidades. Nos vamos a centrar \nen este tipo de actualización. 
Dentro de la actualización del sistema operativo, vamos a ver los siguientes tipos: 
• Actualización de sistema operativo desde un servidor: 
» Sistemas Windows Server. 
» Sistemas Linux (no lo veremos en esta unidad). 
• Actualización de sistema operativo desde el puesto de usuario: 
» Sistemas Windows. 
» Sistemas Linux. 
» Sistemas MAC OS.

---

Administración del Sistema Operativo y software de Base 
38 
• Actualización de terminales móviles: 
» Android. 
» iOS. 
3.4.1. Actualización de servidores 
Resulta de vital importancia tener correctamente actualizados los equipos clientes y los servidores de 
la red. 
Cuando tenemos pocos equipos resulta fácil mantenerlos actualizados manualmente o de forma 
automática mediante Windows Update. 
Sin embargo, cuando disponemos de cientos o miles de equipos, este método no es viable. En estos 
casos, estas tareas las debe gestionar un servidor. 
Windows Server 
 
Fuente: https://es.m.wikipedia.org/wiki/Archivo:Windows-
server-2016.png 
El servicio Windows Server Update Services (WSUS) permite a los administradores implementar las 
actualizaciones de Microsoft más recientes, que se deben instalar en los diferentes equipos. 
Configuración en servidor 
Lo primero que debemos hacer es instalar WSUS en el servidor. Simplemente debemos seguir los pasos 
del asistente de instalación. 
A continuación, aparecerá el asistente de configuración. Debemos configurar los siguientes elementos: 
• Servidor de sincronización de contenido. 
Aquí le indicamos el servidor desde el que se van a obtener las actualizaciones. Lo más sencillo \nes obtenerlas directamente de Windows Update. 
• Seleccionamos el idioma. 
• Seleccionamos los productos de Microsoft que queremos sincronizar. Por ejemplo, para 
descargar actualizaciones de Microsoft Office. 
• Indicamos cuándo queremos que se realice la actualización. Lo ideal es que se haga de forma 
automática diariamente, a una determinada hora en la que no suela haber mucha carga de red.

---

Administración del Sistema Operativo y software de Base 
39 
 
Fuente: Fabiorahamim (https://commons.wikimedia.org/wiki/File:Wsus.png) 
Configuración en cliente 
La manera más adecuada de configurar las actualizaciones automáticas depende del entorno de red. 
En un entorno de Active Directory, se puede utilizar el objeto "Directiva de grupo" (GPO) de Active 
Directory. 
 
 
 
 
+ Info 
Active Directory es una implementación de servicio de directorio \nen una red distribuida de computadores. 
Utiliza distintos protocolos, principalmente LDAP, DNS, DHCP y 
Kerberos. 
Es un servicio establecido en uno o varios servidores donde se 
crean objetos tales como usuarios, equipos o grupos, con el 
objetivo de administrar los inicios de sesión en los equipos 
conectados a la red, así como la administración de políticas. 
 
 
En un entorno que no sea un dominio hay que utilizar las directivas de grupo local. Tanto si utilizamos 
un método u otro, debemos configurar las actualizaciones automáticas de los equipos cliente para que 
utilicen el servidor WSUS.

---

Administración del Sistema Operativo y software de Base 
40 
Para configurar un equipo cliente para que utilice el servidor WSUS debes realizar los siguientes pasos: 
 
• Ejecuta el comando gpedit.msc y, en la ventana que aparece, accede a "Configuración del \nequipo" → "Plantillas administrativas" → "Componentes de Windows" → "Windows Update".

---

Administración del Sistema Operativo y software de Base 
41 
• Habilita, al menos, los siguientes elementos: 
• Especificar la ubicación del servicio Windows Update de la Intranet. Aquí debes indicar la 
dirección del servidor de actualización. 
 
• Configurar actualizaciones automáticas. Aquí estableces cómo y cuándo se van a descargar \ne instalar las actualizaciones.

---

Administración del Sistema Operativo y software de Base 
42 
Administración 
Una vez configurados los equipos clientes, para que obtengan las actualizaciones del servidor interno es 
necesario realizar las siguientes tareas: 
• Debemos tener un control de las actualizaciones. 
• Aprobaremos las actualizaciones que queramos utilizar. 
• Podemos aprobarlas para ejecutarse en un equipo específico o en un grupo de ellos. 
• Para aprobar una actualización pulsamos con el botón derecho y seleccionamos "Aprobar". 
3.4.2. Actualización de S.O. desde el puesto de usuario 
Vamos a ver las actualizaciones de los diferentes S.O. y las herramientas que hay para ello. 
Sistemas Windows 
Vamos a ver cómo funcionan las actualizaciones automáticas en Windows 10. Al contrario que en 
versiones anteriores, en Windows 10 las actualizaciones automáticas están habilitadas por defecto. Es 
más, en algunas versiones ni siquiera se permite desactivarlas. 
Las ediciones Pro, Enterprise y Education permiten aplazar la instalación de las actualizaciones hasta un 
máximo de 35 días. 
Estas versiones también tienen (de momento) dos formas de configurar las actualizaciones para que el 
sistema avise antes de descargarlas: 
• A través de las directivas de grupo. 
• A través del registro de Windows. 
 
 
 
 
+ Info 
Hay algunos trucos e incluso existen herramientas que 
supuestamente te permiten deshabilitarlas. 
Nosotros desaconsejamos el uso de ese tipo de herramientas. Es 
más, recomendamos que las actualizaciones automáticas estén 
siempre activas. 
Por lo tanto, no entraremos en el tema de cómo aplazarlas o 
desactivarlas.

---

Administración del Sistema Operativo y software de Base 
43 
Para configurar las actualizaciones automáticas debemos seguir los siguientes pasos: 
• Botón "Inicio" → "Configuración". 
• Se abrirá la pantalla "Configuración de Windows". 
• Aquí, pulsa "Actualización y seguridad". 
 
Windows Update en Windows 10 Education 
Sistemas Linux 
Para actualizar Linux en Ubuntu (una "distribucion" de Linux), en primer lugar obtenemos la lista de 
actualizaciones con el siguiente comando: 
Sudo apt-get update

---

Administración del Sistema Operativo y software de Base 
44 
 
A continuación, instalamos los paquetes de la lista que acabamos de actualizar. 
Sudo apt-get upgrade 
Nos preguntará si queremos instalarlos y tendremos que responder "y" (yes). 
 
 
 
 
+ Info 
Advanced Package Tool (APT) es un sistema de gestión de paquetes 
creado por "Proyecto Debian" que simplifica en gran medida la 
instalación y eliminación de programas en los sistemas GNU/Linux.

---

Administración del Sistema Operativo y software de Base 
45 
 
 
 
 
 
+ Info 
En las últimas versiones de Ubuntu se puede usar "apt" en lugar de 
"apt-get". Puede realizar lo mismo, pero es algo más agradable de 
usar. 
 
 
Si queremos que las actualizaciones se realicen de forma automática, debemos seguir los siguientes 
pasos: 
• Primero: instalamos el paquete "unattended-upgrades".

---

Administración del Sistema Operativo y software de Base 
46 
Sudo apt install unattended-upgrades 
 
• Segundo: habilitamos las actualizaciones automáticas. 
Para ello debemos modificar el fichero "20archive", que se encuentra en la carpeta 
/etc/apt/apt.conf.d/. 
Por ejemplo, podemos utilizar el editor vi. 
Para abrirlo utilizamos el siguiente comando: 
sudo vi /etc/apt/apt.conf.d/20archive 
 
Añadimos "sudo" para tener permisos para editar este archivo (con "sudo" lo ejecutamos como 
si fuésemos el administrador). 
Añadimos las siguientes líneas al fichero: 
APT::Periodic::Update-Package-Lists "1"; 
                APT::Periodic::Download-Upgradeable-Packages "1"; 
                APT::Periodic::AutocleanInterval "3"; 
                APT::Periodic::Unattended-Upgrade "1";

---

Administración del Sistema Operativo y software de Base 
47 
Explicación: 
• Update-Package-Lists. Actualiza la lista de paquetes disponibles y sus versiones: 
• "1" para habilitar. 
• "0" para deshabilitar. 
• Download-Upgradeable-Packages. Descarga los paquetes de la lista anterior: 
• "1" para habilitar. 
• "0" para deshabilitar. 
• AutocleanInterval. Habilita la autolimpieza de los paquetes descargados cada X días (tres en 
nuestro ejemplo). 
• Unattended-Upgrade. Instala los paquetes descargados: 
• "1" para habilitar. 
• "0" para deshabilitar. 
 
Sistemas macOS 
Las actualizaciones automáticas del sistema están habilitadas por defecto en los sistemas operativos 
macOS. 
Se puede configurar varias opciones de descarga. A continuación, te contamos como llegar a la pantalla 
de configuración. 
En la barra de herramientas, pulsa la manzana y a continuación "Preferencias del sistema".

---

Administración del Sistema Operativo y software de Base 
48 
 
En la siguiente pantalla pulsa "App Store".

---

Administración del Sistema Operativo y software de Base 
49 
Aparecerá la siguiente pantalla, donde podrás configurar las actualizaciones automáticas. 
 
Desde aquí puedes configurar la descarga automática de actualizaciones de aplicaciones. En caso de no 
tenerlo activo, se puede acceder a través de la App Store para actualizar las aplicaciones que queramos. 
Para ello debemos abrir la App Store desde el lanzador de aplicaciones. Se abrirá la página de 
aplicaciones disponibles:

---

Administración del Sistema Operativo y software de Base 
50 
Aquí pulsamos sobre "App Store" y se abrirá la aplicación. En la barra superior de la aplicación \nencontramos el botón "Actualizaciones". Lo pulsamos. 
 
Se abrirá una pantalla con todas las actualizaciones disponibles (tanto de sistema como de aplicaciones). 
 
3.5. Actualización o instalación de nuevo software 
de aplicación 
Cuando se necesite instalar un nuevo software, (de desarrollo propio o a medida), se debería probar en 
un entorno de prueba antes de entrar en producción.

---

Administración del Sistema Operativo y software de Base 
51 
Actualizar software existente 
Esta tarea requiere dedicación constante. Las tareas principales son: 
• Mantener el software actualizado (salvo en el caso de que se deba funcionar con versiones más 
antiguas por temas de compatibilidad). 
• Aplicar los parches de seguridad de las vulnerabilidades que el fabricante vaya identificando. 
• Mantenerse informado de las nuevas versiones y parches de seguridad del software que se 
utiliza. 
Mantenimiento de los periféricos 
El administrador debe comprobar que todos los periféricos (impresoras, escáneres, etcétera) funcionan 
correctamente. 
En caso de fallo de hardware, debe anotar la tarea, establecer prioridad y ser responsable. 
Automatización de tareas rutinarias 
Mediante la programación de scripts se deben automatizar tareas rutinarias, ya sea en servidor o en los 
propios puestos de usuarios. 
Algunos ejemplos de estas tareas son: 
• Comprobar que los equipos de usuario tienen las últimas actualizaciones del sistema operativo y 
actualizar en caso necesario. 
• Comprobar que los equipos de usuario tienen las últimas actualizaciones del software antivirus y 
actualizar en caso necesario. 
• Conectar con sistemas de ficheros de servidores. 
• Etcétera. 
 
 
 
 
+ Info 
Hay que dejar bien claro que un administrador de sistemas no es un 
ingeniero de software. 
No es responsable del diseño de nuevas aplicaciones ni de añadir 
nuevas funcionalidades al software existente.

---

Administración del Sistema Operativo y software de Base 
52 
 
 
 
Sin embargo, si debe tener conocimientos de programación para: 
• Comprender cómo funciona el software que debe 
mantener. 
• Realización de scripts para la realización de tareas 
automáticamente. 
Por ejemplo, sería interesante que tuviera conocimientos de: 
• Distintos tipos de shell. 
• Perl. 
 
3.6. Configurar y mantener acceso a internet 
El administrador de sistemas debe aplicar una política de asignación de direcciones IP y configuración de 
red para proporcionar el acceso a Internet a los usuarios. 
También debe aplicar políticas de seguridad de control de contenidos, estableciendo qué páginas puede 
visitar y cuáles no. 
 
 
 
 
+ Info 
En caso de que los usuarios no necesiten una IP fija, se puede 
utilizar DHCP para asignarle direcciones disponibles. 
En el caso de los servidores y periféricos es mejor utilizar una 
dirección fija. 
DHCP (Dynamic Host Configuration Protocol) es un protocolo de 
red mediante el cual un servidor DHCP asigna dinámicamente una 
dirección IP y otros parámetros de configuración de red a cada 
dispositivo.

---

Administración del Sistema Operativo y software de Base 
53 
3.7. Gestión de cuentas de usuarios 
Las tareas a realizar respecto a las cuentas de usuario son: 
• Altas. 
• Bajas. 
• Modificaciones de usuarios existentes. 
• Configurar los privilegios de acceso. 
• Restaurar contraseñas. 
Estas tareas requieren la realización de varias subtareas. 
Se deben automatizar en la medida de lo posible. 
En todos los lenguajes existen comandos determinados para mostrar y gestionar la información de 
cuentas de usuario. 
 
 
 
 
Ejemplo 
En el Sistema Linux, el comando getfacl, muestra en pantalla por 
dada archivo, la información entre otras, de nombre de archivo, 
propietario y grupo. 
 
3.8. Monitorizar el rendimiento del sistema 
El administrador debe intentar prevenir los fallos. Para ello, debe monitorizar el sistema. En caso de 
degradación del rendimiento o la aparición de algún problema, se debe actuar lo más pronto posible, ya 
que, si esto se consigue solucionar antes de que lo reporte algún usuario, no tendrán la sensación de que \nel sistema ha fallado. 
Algunas de estas tareas preventivas pueden ser: 
• Realizar una correcta configuración del sistema. 
• Vigilancia de los logs del sistema.

---

Administración del Sistema Operativo y software de Base 
54 
• Estar atentos a las alertas del sistema. 
• Automatizar estos procesos mediante scripts o aplicaciones específicas que nos envíen un 
correo electrónico cuando hay una actividad anormal. 
Este tipo de seguimiento proactivo es fundamental en entornos donde la disponibilidad y el rendimiento 
son esenciales. 
3.8.1. Monitorización del rendimiento y uso de recursos 
Además del seguimiento general del sistema, es importante monitorizar de forma específica el uso de 
los recursos para detectar sobrecargas o cuellos de botella. La supervisión de CPU, memoria RAM, 
almacenamiento y red permite actuar ante consumos excesivos o ineficiencias. 
Windows proporciona herramientas integradas como: 
• Administrador de tareas: muestra en tiempo real qué procesos están consumiendo más 
recursos, lo que permite cerrar aplicaciones innecesarias o problemáticas. 
• Monitor de rendimiento: ofrece una vista más detallada, permite configurar contadores de 
rendimiento, generar informes y establecer alertas para detectar tendencias anómalas o 
degradaciones progresivas. 
Estas herramientas permiten al administrador tomar decisiones informadas y realizar ajustes para 
mantener un rendimiento óptimo del sistema. 
La monitorización de recursos no solo mejora la respuesta inmediata ante incidencias, sino que también 
ayuda a planificar mejoras futuras y a garantizar una mayor estabilidad del sistema a medio y largo 
plazo. 
3.9. Seguridad 
Este es sin duda uno de los aspectos críticos que requieren atención continua. No existe un sistema 
infalible ante: 
• Un ataque. 
• Acceso no autorizado. 
• Software dañino (virus, malware, spyware, troyanos, etcétera). 
Sin embargo, con las políticas de seguridad adecuadas se pueden adoptar: 
• Medidas preventivas. Con ellas minimizamos el riesgo a sufrir algún tipo de ataque. Algunas 
medidas son: 
• Concienciación de los usuarios. 
• Utilización de software antivirus. 
• Correcta arquitectura de red y utilización de cortafuegos.

---

Administración del Sistema Operativo y software de Base 
55 
• Instalación de parches de seguridad del software. 
• Establecer una política de cambio de contraseñas de usuario cada cierto tiempo. 
• Etcétera. 
• Medidas paliativas. Son aquellas que se aplican una vez que se ha producido el ataque. Algunas 
medidas son: 
• Política de actuación. 
• Restauración de copias de seguridad. 
• Tracking del problema. 
• Etcétera. 
Recuperación ante fallos y caídas del sistema 
Si no hemos podido detectar o parar el fallo, se puede producir una caída del sistema. Para ello es 
necesaria una intervención rápida para restaurar el sistema a su funcionamiento normal. En algunos 
casos puede ser necesario contratar un mantenimiento externo. 
Estos son los momentos más críticos en la labor de un administrador de sistemas. En estos casos es muy 
posible la necesidad de realizar horas extras. 
3.9.1. Configuración de Directivas de Seguridad y Controles 
de acceso 
Configurar bien las directivas de seguridad y control de acceso son fundamentales para proteger un 
sistema y sus recursos. Estas directivas aseguran que solo los usuarios autorizados puedan acceder al 
sistema y a los recursos compartidos, evitando accesos no deseados y riesgos de seguridad. Las políticas 
de grupo (GPO) permiten a los administradores establecer restricciones de acceso, políticas de 
contraseñas y controlar aspectos importantes de la red y los dispositivos, como las conexiones remotas 
o el uso de hardware externo. 
Las políticas de grupo también ayudan a gestionar la seguridad para cada usuario y equipo, controlando 
las aplicaciones que pueden usarse, qué configuraciones pueden cambiarse y qué permisos tiene cada 
usuario. Además, pueden automatizar tareas, como realizar actualizaciones de seguridad, mejorar la \neficiencia y consistencia en la gestión de la red. 
Al implementar directivas claras, se protege la red de accesos no autorizados y se definen bien los 
permisos de los usuarios, evitando errores y vulnerabilidades. Así, las políticas de grupo aumentan la 
seguridad, aseguran el cumplimiento de normativas y reducen los riesgos de ataques, protegiendo los 
datos y recursos de la organización.

---

Administración del Sistema Operativo y software de Base 
56 
3.10. Relación con usuarios y dirección 
La atención a los usuarios es quizás una de las labores que menos gusta a muchos administradores y 
ocupa gran parte de su tiempo. 
El administrador no debería confundirse con un help-desk o persona encargada de dar soporte al 
usuario. 
Se debería implantar un sistema de soporte por tickets y las tareas deberían ser resueltas por el personal 
apropiado (aunque en empresas pequeñas esta persona podría ser el administrador de sistemas). 
Otra medida que puede reducir la carga es dar a los usuarios una formación adecuada de los sistemas y 
programas que manejan. 
Un administrador de sistemas debe ser diplomático y empatizar con los usuarios, pero eso no es algo 
que se enseñe en la formación típica de un administrador. 
3.11. Informar a la dirección 
Debe realizarse una gestión de forma que se proporcione una visión global a la dirección del trabajo 
continuo que se realiza, y que no vean únicamente un fallo puntual. 
El correcto funcionamiento de los sistemas es algo que se presupone, pero un fallo puede tener una 
gran notoriedad. 
Hay que llevar un diario de las tareas que se realizan para poder justificar todo lo que se está haciendo 
bien. 
3.12. Documentación del sistema 
Esto es algo que no suele gustar, pero es muy importante. Todo lo que se hace debe estar 
documentado. Esto es vital porque el administrador de sistemas podría: 
• Irse de vacaciones. 
• Estar de baja por enfermedad. 
• Cambiar de trabajo. 
En ese caso, todo el conocimiento que tiene de los sistemas de la empresa debe recogerlos un nuevo 
administrador. La mejor forma es mediante la documentación. 
También sirve incorporar nuevos administradores para tener mayor capacidad de trabajo. Con una 
buena documentación no requerirán ser formados por parte de sus compañeros.

---

Administración del Sistema Operativo y software de Base 
57 
4. Herramientas para la administracion del sistema 
Los administradores de sistemas pueden utilizar diferentes herramientas de software concretas para 
cada necesidad y función que tengan que realizar, ahorrando tiempo y mejorando también los 
resultados de sus funciones. 
Existen muchas herramientas, vamos a ver algunas de las más destacadas. 
4.1. Comandos de Windows 
La información de este apartado se ha extraído de la web de Microsoft: 
https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/ windows-
commands. 
Todas las versiones compatibles de Windows y Windows Server tienen integrados un conjunto de 
comandos para ejecutar desde símbolo de sistema (consola), que es el shell de comandos. 
A través de ellos se puede gestionar el sistema y automatizar tareas mediante scripts o herramientas de 
scripting. Los scripts aceptan todos los comandos disponibles en la línea de comandos. 
Cada shell es un programa de software que comunica al usuario con el sistema operativo o la aplicación, 
facilitando un entorno para automatizar operaciones. 
Windows tiene dos shells de línea de comandos: 
• El shell de comandos: fue el primer shell integrado en Windows para automatizar tareas básicas, 
como la administración de cuentas de usuario o copias de seguridad, mediante archivos por 
lotes (.bat) 
No se pueden ejecutar los cmdlets de PowerShell. 
• PowerShell: fue diseñado para ampliar las posibilidades del Shell de comandos. 
Los comandos que se ejecutan con PowerShell se denominan cmdlets, estos son parecidos a los 
comandos de Windows, pero proporcionan un lenguaje de scripting más extensible. 
En PowerShell pueden ejecutar tanto los comandos de Windows como los cmdlets. 
La automatización de tareas es mejor con el uso de PowerShell que con el uso de comandos de 
Windows, archivos batch o por lotes o Windows Script Host. 
A continuación, abordaremos varios comandos del shell de Windows que, como hemos mencionado, 
también pueden ejecutarse en PowerShell. 
Si desde la línea de comandos se ejecuta (se teclea y se pulsa intro) help, se muestra por pantalla un 
listado con los comandos disponibles. Y para saber más información sobre cada comando, se ejecuta 
help seguido del nombre del comando.

---

Administración del Sistema Operativo y software de Base 
58 
Algunos de estos comandos destacan por su importancia en la gestión de red, como son, por ejemplo: 
• gpresult 
Es una herramienta vital para los administradores de red pues con ella pueden visualizar la 
configuración de directiva aplicada a equipos y usuarios de la organización. El RSoP (Resultant 
Set of Policy o Conjunto Resultante de Directivas) es un informe o listado de la directiva 
aplicada que puede ser obtenida desde la interfaz de comandos gracias a la ejecución de la 
herramienta RSoP.msc o bien a la ejecución del comando gpresult desde la línea de comandos. 
Sintaxis: 
gpresult [/R][/V][/H][/S][/U][/P][/USER][/SCOPE][/X][/F] 
• ipconfig  
Proporciona la configuración TCP-IP de un equipo. 
Muestra todos los valores de configuración de red TCP/IP actuales y actualiza la configuración 
del Protocolo de configuración dinámica de host (DHCP) y del Sistema de nombres de dominio 
(DNS). 
Si se usa sin parámetros, ipconfig muestra la versión 4 (IPv4) del protocolo de Internet y las 
direcciones IPv6, la máscara de subred y la puerta de enlace predeterminada para todos los 
adaptadores. 
Si se utiliza con la opción /all, se obtiene un informe detallado de la configuración de todas las 
interfaces de red presentes en el equipo, incluyendo los puertos serie configurados en el sistema 
(RAS).  
Las opciones /release [adaptador] y /renew [adaptador] liberan y renuevan respectivamente la 
dirección IP del adaptador especificado. Si no se especifica adaptador, el comando afectará a 
todas las direcciones de adaptadores enlazados a TCP/IP.  
Sintaxis: 
ipconfig [/allcompartments] [/all] [/renew [<adapter>]] [/release [<adap-ter>]] 
[/renew6[<adapter>]] [/release6 [<adapter>]] [/flushdns] [/displaydns] 
[/registerdns] [/showclassid <adapter>] [/setclassid <adap-ter> [<classID>]]

---

Administración del Sistema Operativo y software de Base 
59 
• ping 
Ayuda a comprobar la conectividad del equipo a nivel IP cuando hay errores en la conexión 
TCP/IP. Envía a un nombre DNS destino o a una dirección IP una petición ICMP de eco.  
Sintaxis: 
ping [/t] [/a] [/n <count>] [/l <size>] [/f] [/I <TTL>] [/v <TOS>] [/r <count>] 
[/s <count>] [{/j <hostlist> | /k <hostlist>}] [/w <timeout>] [/R] [/S <Srcaddr>] 
[/4] [/6] <targetname> 
• arp  
Es útil para visualizar la caché de resolución de direcciones, ya que muestra y modifica las tablas 
de traducción de direcciones IP a direcciones físicas usadas por el protocolo de resolución de 
direcciones ARP.  
La memoria caché de ARP contiene una o varias tablas que se usan para almacenar direcciones 
IP y sus direcciones físicas de Ethernet o Token Ring resueltas.  
Hay una tabla independiente para cada adaptador de red Ethernet o Token Ring instalado en el \nequipo.  
Si se utiliza sin parámetros, arp muestra información de ayuda. 
Sintaxis: 
arp [/a [<inetaddr>] [/n <ifaceaddr>]] [/g [<inetaddr>] [-n <ifaceaddr>]] [/d 
<inetaddr> [<ifaceaddr>]] [/s <inetaddr> <etheraddr> [<ifaceaddr>]] 
• tracert (trace route) 
Es una utilidad que permite visualizar trazas. Determina la ruta de acceso a un destino mediante \nel envío de mensajes de solicitud de eco del Protocolo de mensajes de control de Internet 
(ICMP) o ICMPv6 al destino con valores de campo de período de vida (TTL) cada vez mayores.  
Cada enrutador a lo largo de la ruta de acceso debe disminuir el TTL (contador máximo de 
vínculos) de un paquete IP en al menos 1 antes de reenviarlo.  
Cuando el TTL de un paquete alcanza 0, el enrutador devuelve un mensaje ICMP time Exceeded 
al equipo de origen.

---

Administración del Sistema Operativo y software de Base 
60 
Este comando determina la ruta de acceso enviando el primer mensaje de solicitud de eco con 
un TTL de 1, e incrementando el TTL en 1 en cada transmisión posterior, hasta que el destino 
responde o se alcanza el número máximo de saltos (que se puede especificar). 
La ruta de acceso se determina examinando los mensajes de ICMP time Exceeded devueltos por 
los enrutadores intermedios y el mensaje de eco de respuesta devuelto por el destino.  
Hay algunos enrutadores que no devuelven mensajes time Exceeded para paquetes con valores 
TTL caducados y son invisibles para el comando tracert, en cuyo caso, se muestra una fila de 
asteriscos (*) para ese salto.  
Sintaxis: 
tracert [/d] [/h <maximumhops>] [/j <hostlist>] [/w <timeout>] [/R] [/S <srcaddr>] 
[/4][/6] <targetname> 
Donde:  
• /d 
Detiene los intentos de resolver las direcciones IP, haciendo que se pueda acelerar la 
devolución de los resultados. 
• /h <maximumhops> 
Especifica el número máximo de saltos (siendo 30 el valor predeterminado) en la ruta de 
acceso para buscar el destino. 
• /j <hostlist> 
Especifica que los mensajes de solicitud de eco utilizan la opción Ruta de origen flexible en 
la cabecera IP, con el conjunto de destinos intermedios especificados en <hostlist>.  
<hostlist> se utiliza únicamente en seguimiento de direcciones IPv4, y es una serie de 
direcciones IP (en notación decimal con puntos) separadas por espacios. 
Con el uso del enrutamiento de origen flexible, los destinos intermedios sucesivos se 
pueden separar por uno o varios enrutadores, siendo 9 el número máximo de direcciones o 
nombres de la lista. 
• /w <timeout> 
Especifica la cantidad de tiempo en milisegundos (4000 predeterminado), que se debe \nesperar a que se reciba el mensaje ICMP time Exceeded o de respuesta de eco 
correspondiente a un mensaje de solicitud de eco dado.  
Si no se recibe dentro del tiempo de espera, se muestra un asterisco (*).

---

Administración del Sistema Operativo y software de Base 
61 
• /R 
Especifica que el encabezado de extensión de enrutamiento IPv6 se usa para enviar un 
mensaje de solicitud de eco al host local, usando el destino como destino intermedio y 
probando la ruta inversa. 
• /S <srcaddr> 
Se utiliza únicamente para el seguimiento de direcciones IPv6, y especifica la dirección de 
origen que se va a utilizar en los mensajes de solicitud de eco. 
• /4 
Especifica que tracert.exe solo puede usar IPv4 para realizar el seguimiento. 
• /6 
Especifica que tracert.exe solo puede usar IPv6 para realizar el seguimiento. 
• <targetname> 
Especifica el destino, identificado por la dirección IP o por el nombre de host. 
• route  
Se utiliza para visualizar y modificar la tabla de rutas: 
• route print muestra una lista con las rutas actuales conocidas por IP para el host.  
• route add se utiliza para añadir rutas a la tabla.  
• route delete se utiliza para borrar rutas de la tabla.  
Sintaxis: 
route [/f] [/p] [<command> [<destination>] [mask <netmask>] [<gate-way>] [metric 
<metric>]] [if <interface>]] 
• netstat 
Muestra: 
• Las conexiones TCP activas. 
• Los puertos en los que escucha el equipo. 
• Las estadísticas de Ethernet.

---

Administración del Sistema Operativo y software de Base 
62 
• La tabla de enrutamiento IP. 
• Las estadísticas IPv4 (para los protocolos IP, ICMP, TCP y UDP). 
• Las estadísticas de IPv6 (para los protocolos IPv6, ICMPv6, TCP a través de IPv6 y UDP a 
través de IPv6).  
Usado sin parámetros, muestra las conexiones TCP activas. 
Sintaxis: 
netstat [-a] [-b] [-e] [-n] [-o] [-p <Protocol>] [-r] [-s] [<interval>] 
• nbtstat 
Solo se puede utilizar si el protocolo TCP/IP está instalado como componente en las 
propiedades de un adaptador de red en conexiones de red. 
Muestra: 
• Estadísticas del protocolo NetBIOS a través de TCP/IP (NetBT). 
• Tablas de nombres NetBIOS para el equipo local y equipos remotos. 
• La caché de nombres NetBIOS. 
Permite actualizar la caché de nombres NetBIOS y los nombres registrados con el Servicio de 
nombres Internet de Windows (WINS). 
Sintaxis: 
nbtstat [/a <remotename>] [/A <IPaddress>] [/c] [/n] [/r] [/R] [/RR] [/s] [/S] 
[<interval>] 
• nslookup 
Solo está disponible si está instalado el protocolo TCP/IP. 
Nslookup se añadió a Windows NT 4. y es una herramienta muy útil para resolver problemas con \nel Servicio de Nombres de Dominio (DNS), tales como la resolución del nombre de un equipo. 
Tiene dos modos: 
• Interactivo: recomendado si es necesario buscar solo un fragmento de datos. 
• No interactivo.

---

Administración del Sistema Operativo y software de Base 
63 
Sintaxis: 
nslookup [exit | finger | help | ls | lserver | root | server | set | view] 
[options] 
 
 
 
 
Importante 
Puedes consultar las opciones de estos comandos, así como el 
resto de comando en la web de Microsoft: 
https://learn.microsoft.com/es-es/windows-
server/administration/windows-commands/windows-commands 
 
4.2. Herramienta Netsh 
Netsh es una herramienta para Windows, de la línea de comandos que ofrece varias opciones para 
consultar, modificar y diagnosticar la configuración de una red. También, es capaz de crear un script 
con la configuración actual de la red que nos permita configurar otros equipos de manera sencilla, o 
restaurarla después de realizar cambios. 
Netsh está disponible en las versiones Windows 2000, Windows Server 2003, Windows XP Profesional, 
Windows 7, Windows Server 2008, Windows 8, Windows 10, Windows 11 y Windows Server 2012. 
 
 
 
 
+ Info 
Netsh es una herramienta que se adapta a múltiples contextos y 
aporta muchas opciones, ya que se apoya en archivos dll que le 
aportan diferentes capacidades. 
Por ejemplo, el archivo dhcpmon.dll le ofrece el conjunto de 
características que le permiten administrar servidores DHCP.

---

Administración del Sistema Operativo y software de Base 
64 
Para utilizarla debemos entrar en símbolo del sistema ejecutando el comando cmd, una vez en la 
ventana de símbolo del sistema ejecutamos netsh, y entraremos al comando, por lo que el prompt 
cambiara a netsh >. 
El prompt es el carácter (o conjunto de caracteres) que se muestran en una línea de comandos para 
indicar que está a la espera de órdenes. 
Podemos obtener ayuda sobre el comando ejecutando ? si estamos dentro de nets (netsh>?) o si no lo \nestamos, ejecutando netsh /? 
Vamos a ver diferentes opciones del comando netsh, ejecutados desde netsh>, (si lo ejecutamos desde 
otro prompt, deberemos incluir la palabra netsh delante de cada opción indicada). 
Mostrar la configuración de red actual 
• Interface ip show config 
Muestra información sobre la configuración de red que está activa en esos momentos (es 
menos detallada que la que indica el comando ipconfig /all). 
• Interface ip show ipstats 
Muestra las estadísticas del protocolo IP. 
• Interface ip show ipnet 
Envía un paquete ARP a toda la red, usando broadcast, y muestra relación de direcciones MAC 
que se corresponden con las direcciones IP de todos los interfaces de red, indicando si son \nestáticas o dinámicas. 
• Interface ip show tcpconn 
Proporciona información sobre las conexiones TCP, muestra las direcciones establecidas, la 
dirección IP remota y el puerto que estamos utilizando. 
Guardar la configuración de la red 
• dump > C:MiConfigRed.cmp 
Se guarda la configuración de la red actual en el archivo MiConfigRed.cmp 
Podemos utilizar el archivo para configurar fácilmente otra red, o bien para restaurarla, si hemos 
realizado cambios. 
• exec C: MiConfigRed.cmp 
Cargamos la configurancion de la red guardada en el archivo MiConfigRed.cmp

---

Administración del Sistema Operativo y software de Base 
65 
Cambiar la configuración de la red 
Para cambiar la configuración de la red, utilizamos la orden netsh interface ip, añadiendo el comando 
set address, lo que nos obliga a indicar unos argumentos concretos que queremos establecer. 
Puesto que vamos a realizar cambios, debemos ejecutar cmd para entrar en la ventana Símbolo del 
sistema con privilegios de administrador. 
La sintaxis, con datos de ejemplo, será: 
netsh interface ip set address name="Ethernet" source=static 
addr=192.168.1.10 mask=255.255.255.0 gateway=192.168.1.1 
Donde: 
• Name= 
Indica el nombre de la red. 
• Source= 
Indica si la dirección será estática o dinámica: 
• source=static 
Será una dirección estática. 
• source= dhcp 
Será una dirección dinámica, la asignación de la dirección IP se realiza de forma 
automática,por lo que no tendremos que indicar el resto de parámetros, únicamente el 
comando será: netsh interface ip set address name="Ethernet" source=dhcp 
• addr= 
Indicamos el valor que queremos asignar a la dirección IP (en caso de definirla como static). 
• mask= 
Indicamos el valor para la máscara de red. 
• gateway= 
Indicamos el valor para la puerta de enlace.

---

Administración del Sistema Operativo y software de Base 
66 
• Para indicar el tipo de DNS que queremos utilizar tenemos: 
• interface ip set dnsserver "Ethernet" static 8.8.8.8 primary 
Asignamos un DNS estático. 
• interface ip set dnsserver "Ethernet" dhcp 
Lo asignamos mediante DHCP. 
Activar o Desactivar firewall windows XP 
• firewall set opmode enable 
Activado. 
• firewall set opmode disable 
Desactivado. 
 
 
 
 
Atención 
Te aconsejamos que consultes en siguiente enlace para gestión de 
firewall con Windows Server 
Uso del contexto de firewall de netsh advfirewall - Windows Server 
 
Otras opciones de comandos 
Para cambiar el DNS primario y secundario se usa las siguientes líneas de comando: 
• interface ip add dns name="Conexión de área local" addr=10.0.0.1 
• interface ip add dns name="Conexión de área local" addr=10.0.0.2 index=2 
Para ver los BSSID de las redes wifi a tu alcance se usa el comando "wlan": 
• wlan show networks mode=Bssid 
Solo funciona a partir de las versiones Windows Server 2008 y Windows Vista.

---

Administración del Sistema Operativo y software de Base 
67 
BSSID, (Basic Service Set Identifier), o identificador básico de conjunto de servicios, es un nombre de 
identificación único de todos los paquetes de una red inalámbrica para identificarlos como parte de \nesa red. 
 
 
 
 
+ Info 
Te aconsejamos que consultes en siguiente enlace para gestión de 
red con Windows Server 
Instalación y configuración de ip versión 6 - Windows Server 
También puedes consultar en la página oficial de Microsoft. 
https://docs.microsoft.com/es-es/ 
 
4.3. Herramienta Netcat 
Comando Netcat (nc de forma abreviada), es una herramienta de fácil uso para gestión de redes, 
conocida como la "Navaja suiza" de los hackers. 
La herramienta, fue desarrollada por Hobbit en 1996 y liberada bajo una licencia de software libre 
permisiva (no copyleft) para UNIX, y posteriormente fue portada a otras aplicaciones como Windows y 
Mac OS X. 
Permite analizar conexiones de red, buscar puertos abiertos, transferir datos, etc. Permite a través de 
intérprete de comandos: 
• Abrir puertos TCP/UDP en un HOST (quedando netcat a la escucha). 
• Utilizada también a menudo para abrir puertas traseras en un sistema. 
• Asociar una shell a un puerto en concreto (para conectarse por ejemplo a MS-DOS o al 
intérprete bash de Linux remotamente). 
• Forzar conexiones UDP/TCP (útil por ejemplo para realizar rastreos de puertos o realizar 
transferencias de archivos bit a bit entre dos equipos). 
• También se puede realizar la depuración de aplicaciones de red.

---

Administración del Sistema Operativo y software de Base 
68 
Algunas de las opciones básicas del comando nc son: 
• -l: Netcat abre un puerto y se mantiene a la escucha. Se aceptará una única conexión de un 
único cliente antes de cerrarse. 
• -k: Se usa junto con la opción -l con el objetivo de que el puerto se mantenga abierto tras recibir 
una conexión, a la espera de más conexiones. 
• -u: abre puertos con el protocolo UDP en vez de abrirlos mediante el protocolo TCP. 
• -p: permite especificar el puerto al que conectarse. 
• -v: muestra información acerca de la conexión. 
• -t: Respuestas compatibles con sesiones de Telnet. 
• -q segundos: después leer los datos de entrada, se esperarán los segundos especificados antes 
de enviar una respuesta. 
• -i segundos: se agregará un retraso, según los segundos especificados, tanto para el envío como 
para la recepción de líneas de texto. 
 
 
 
 
+ Info 
Crytpcat es una herramienta un poco más segura que el clásico 
Netcat, aunque es menos conocida. 
 
4.4. Herramienta Net User 
Es una herramienta de control de usuarios de Windows, que permite a los administradores de sistemas 
(que disponen de privilegios) poder administrar cuentas de usuario en PCs con Windows, a través de la 
línea de comandos. 
Desde la línea de comandos se pueden ejecutar diferentes instrucciones (o comandos), para mostrar 
información de las cuentas de usuario o hacer cambios en las mismas. 
• Ejemplos en Windows 10: 
• Net User/Help: 
Muestra la ayuda para el comando.

---

Administración del Sistema Operativo y software de Base 
69 
• Net User: 
Devuelve una lista con todas las cuentas de usuario en el sistema. 
• net user nombreusuario *: 
Cambia la contraseña de un usuario, gracias al uso del símbolo "asterisco". 
 
 
 
 
+ Info 
Si deseas conocer más opciones y comandos puedes consultar la 
página oficial de Microsoft. 
 
4.5. Bash 
GNU Bash o simplemente Bash (Bourne-again shell) es un lenguaje de órdenes y shell de Unix escrito 
por Brian Fox para el Proyecto GNU como un reemplazo de software libre para el shell Bourne. 
 
 
 
+ Info 
Bourne Shell es un programa informático cuya función consiste en 
interpretar órdenes. 
Incorpora características tales como control de procesos, 
redirección de entrada/salida, listado y lectura de ficheros, 
protección, comunicaciones y un lenguaje de órdenes para escribir 
programas por lotes o "scripts". 
Fue el intérprete usado en las primeras versiones de Unix y se 
convirtió en un estándar de facto.

---

Administración del Sistema Operativo y software de Base 
70 
Bash es un intérprete de órdenes que generalmente se ejecuta en una ventana de texto donde el 
usuario escribe órdenes en modo texto. 
Algunas características de Bash: 
• Puede leer y ejecutar órdenes desde un archivo, llamado guion o 'script'. 
• Compatibilidad: 
Como todos los intérpretes de Unix, es compatible con: 
• El agrupamiento de nombres de archivo (coincidencia de comodines). 
• Tuberías. 
• Here documents. 
• Sustitución de comandos. 
• Variables. 
• Estructuras de control para pruebas de condición e iteración. 
• Las palabras reservadas, la sintaxis, las variables de ámbito dinámico y otras características 
básicas del lenguaje se copian de sh. 
• Otras características: 
• El historial, se copian de csh y ksh. 
• Bash es un intérprete de órdenes compatible con POSIX, pero con varias extensiones. 
 
 
 
 
Anécdota 
El nombre del intérprete es un acrónimo de 'Bourne-again shell' 
(intérprete de órdenes Bourne, de nuevo), un juego de palabras 
con el nombre del intérprete Bourne que reemplaza y la noción de 
"nacer de nuevo".

---

Administración del Sistema Operativo y software de Base 
71 
4.5.1. Historia 
Brian Fox comenzó a codificar Bash el 10 de enero de 1988 después de que Richard Stallman se sintiera 
insatisfecho con la falta de progreso de un desarrollador anterior. 
Stallman y la Free Software Foundation (FSF) consideraron un intérprete libre que podría ejecutar 
scripts de shell existentes tan estratégicos para un sistema completamente libre construido a partir de 
código BSD y GNU que este fue uno de los pocos proyectos que financiaron ellos mismos, con Fox \nemprendiendo el trabajo como un empleado de FSF. 
Fox lanzó Bash como beta, versión .99, el 8 de junio de 1989 y se mantuvo como el colaborador 
principal hasta mediados de 1992 y mediados de 1994, []?cuando fue despedido de la FSF y su 
responsabilidad fue transferida a otro colaborador temprano, Chet Ramey. 
Desde entonces, Bash se ha convertido en el shell más popular entre los usuarios de las distribuciones 
GNU/Linux, convirtiéndose en el shell interactivo predeterminado en las diversas distribuciones 
GNU/Linux(con distribuciones se refiere a todo sistema operativo que como kernel tenga el kernel de 
linux) (aunque el intérprete Almquist puede ser el intérprete de secuencias de órdenes 
predeterminado) y en las versiones de MacOS de Apple antes de Catalina en octubre de 2019. 
Bash también ha sido importado a Microsoft Windows y distribuido con Cygwin y MinGW, a DOS por el 
proyecto DJGPP, a Novell NetWare y a Android a través de varias aplicaciones de emulación de terminal. 
 
 
 
 
Resumiendo 
Lanzado por primera vez en 1989, se ha utilizado ampliamente 
como el intérprete de inicio de sesión (login) predeterminado para 
la mayoría de las distribuciones de GNU/Linux y Mac OS X de 
Apple hasta la versión 10.15. 
Una versión también está disponible para Windows 10 y Android. 
También es el intérprete de órdenes de usuario predeterminado en 
Solaris 11. 
 
4.5.2. Seguridad 
Un agujero de seguridad en Bash que data de la versión 1.03 (agosto de 1989), denominado Shellshock, 
fue descubierto a principios de septiembre de 2014 y rápidamente provocó una serie de ataques en 
Internet. Los parches para corregir los errores se pusieron a disposición poco después de que se 
identificaron los errores. 
El error de seguridad fue descubierto por Stéphane Chazelas, especialista en Unix / Linux.

---

Administración del Sistema Operativo y software de Base 
72 
El error, se llamó Shellshock (inicialmente fue llamado fue llamado "Bashdoor") y se le asignaron los 
números CVE-2014-6271, CVE-2014-6277 y CVE-2014-7169. 
El error se consideró grave, ya que los scripts CGI que usan Bash podrían ser vulnerables, lo que permite 
la ejecución de código arbitrario. 
El error estaba relacionado con la forma en que Bash pasa las definiciones de funciones a subcapas a 
través de variables de entorno. 
4.5.2.1. Shellshock 
Shellshock, también conocida como Bashdoor, es una familia de bugs de seguridad en la ampliamente 
usada Bash de Shell de Unix. 
El primero de estos bugs fue divulgado el 24 de septiembre de 2014. 
Varios servicios de internet tal como algunas implementaciones de servidores web usan Bash para 
ciertos pedidos y procesos, esto le permitía al atacante ejecutar comandos arbitrarios en versiones 
vulnerables de Bash, de esta forma el atacante podía ganar acceso no autorizado al sistema atacado. 
El 12 de septiembre Stéphane Chazelas contactó al encargado del mantenimiento de Bash, Chet Ramey 
mencionándole acerca de su descubrimiento del error original el cual fue llamado "Bashdoor". 
Trabajando en conjunto con expertos en seguridad se obtuvo en poco tiempo un parche que 
solucionaría el problema. 
El primer error ocasionaba que Bash sin previa autorización ejecutara comandos cuando los comandos están 
concatenados al final de una definición de función guardada en los valores de las variables de ambiente. 
A días de la publicación del error, el intenso escrutinio de los defectos de diseño subyacentes, 
descubrieron vulnerabilidades que se encontraban relacionadas, (CVE-2014-6277, CVE-2014-6278, 
CVE-2014-7169, CVE-2014-7186 y CVE-2014-7187), para las cuales Ramey creó nuevos parches al 
software de Bash. 
Atacantes explotaron Shellshock apenas habían pasado unas horas de la revelación inicial mediante la 
creación de botnets de computadoras previamente comprometidas para ejecutar ataques de 
denegación de servicio distribuido y escaneo de vulnerabilidades. 
 
 
 
 
+ Info 
El término Botnet hace referencia a un conjunto o red de robots 
informáticos o bots, que se ejecutan de manera autónoma y 
automática. 
El artífice de la botnet puede controlar todos los ordenadores / 
servidores infectados de forma remota.

---

Administración del Sistema Operativo y software de Base 
73 
Las compañías de seguridad identificaron millones de ataques y pruebas relacionadas con el error en los 
días siguientes a su descubrimiento. 
El error fue anunciado al público el 24 de septiembre del 2014 cuando las actualizaciones de Bash ya 
incluían los parches hechos para la versión que se distribuiría en la actualización correspondiente. 
Shellshock pudo comprometer millones de servidores que no tuvieran el parche desarrollado por 
Ramey. Debido a su gran impacto ha sido comparada con el error Heartbleed debido a la severidad de la 
falla ocasionada. 
 
 
 
 
+ Info 
Heartbleed (traducido como "hemorragia de corazón") es un 
agujero de seguridad de software en la biblioteca de código abierto 
OpenSSL, solo vulnerable en su versión 1.0.1f, que permite a un 
atacante leer la memoria de un servidor o un cliente, 
permitiéndole, por ejemplo, conseguir las claves privadas SSL de un 
servidor. 
Investigaciones de auditorías indican que algunos atacantes \nexplotaron este error desde al menos cinco meses antes de que 
fuera descubierto y publicado. 
 
 
Apple Inc. indica que los sistemas OS X están a salvo por default, a menos que los usuarios configuraran 
servicios avanzados de UNIX. Estos usuarios avanzados pueden apagar los servicios hasta que un parche 
oficial de OS X esté disponible, de igual forma podrían usar Xcode para reemplazar el Bash provisto por 
default por sistema con una versión personalizada y compilada de Bash que incorporara parches no 
oficiales. A pesar de ser notificada de la vulnerabilidad antes de ser publicada, la compañía no sacó una 
actualización correspondiente de OS X hasta el 29 de septiembre de 2014, al tiempo que la 
actualización de Bash OS X 1.0 fue publicada. 
4.5.2.2. Sintaxis de Bash 
La sintaxis de órdenes de Bash es un superconjunto de instrucciones basadas en la sintaxis del 
intérprete Bourne.

---

Administración del Sistema Operativo y software de Base 
74 
 
 
 
+ Info 
La especificación definitiva de la sintaxis de órdenes de Bash, 
puede encontrarse en el Bash Reference Manual distribuido por el 
proyecto GNU. 
http://www.gnu.org/software/bash/manual/bashref.html 
 
 
La mayoría de los guiones de intérprete de órdenes Bourne ('shell scripts) pueden ejecutarse por Bash 
sin ningún cambio, con la excepción de aquellos guiones del intérprete de órdenes, o consola, Bourne 
que hacen referencia a variables especiales de Bourne o que utilizan una orden interna de Bourne. 
La sintaxis de órdenes de Bash incluye ideas tomadas desde: 
• Los intérpretes Korn shell (ksh) y C shell (csh). 
• La edición de la línea de órdenes. 
• El historial de órdenes. 
• La pila de directorios. 
• Las variables $RANDOM y $PPID. 
• La sintaxis de substitución de órdenes POSIX: $(...). 
Cuando se utiliza como un intérprete de órdenes interactivo, Bash proporciona autocompletado de 
nombres de programas, nombres de archivos, nombres de variables, etc., cuando el usuario pulsa la 
tecla TAB. 
La sintaxis de Bash tiene muchas extensiones que no proporciona el intérprete Bourne, y que 
mencionamos algunas de ellas a continuación. 
• Acceso a los argumentos. 
Los guiones de Bash reciben los argumentos que le pasa al intérprete como $1, $2, …, $n. 
Se puede obtener el número total de argumentos con el símbolo $#. 
La condición If se termina con fi.

---

Administración del Sistema Operativo y software de Base 
75 
Usando $# es posible comprobar el número de argumentos entregados al guion antes de 
realizar alguna acción con ellos: 
if [ $# -lt 2 ]; then 
                echo "Necesitas pasar dos argumentos." 
                exit 1 
             fi 
Otra forma de acceder a los argumentos es a través del array $@, por medio del cual se puede 
iterar sobre todos los argumentos dados: 
for arg in "$@" 
             do 
                echo "$arg" 
             done 
• Operaciones matemáticas con enteros. 
Una gran limitación del intérprete Bourne es que no puede realizar cálculos con enteros sin 
lanzar un proceso externo. 
En cambio, un proceso Bash puede realizar cálculos con enteros. 
Soporta los siguientes operadores relacionales: '==', '!=', ' > ', ' < ', ' > =', y ' < ='. 
Un proceso Bash no puede realizar cálculos en coma flotante. Los únicos intérpretes Unix 
capaces de esto son Korn Shell (versión de 1993) y zsh (a partir de la versión 4.0). 
Se llama bashismo al uso de características de Bash que no están contempladas en las \nespecificaciones POSIX para los intérpretes de órdenes. En general, se recomienda evitarlas, para 
permitir la portabilidad de guiones a otros sistemas operativos.

---

Administración del Sistema Operativo y software de Base 
76 
 
 
 
+ Info 
Puede consultar más información en la web oficial 
(Tienes el enlace en el Campus virtual). 
http://www.gnu.org/software/bash/bash.html 
 
4.6. Scripting en entornos Windows 
La automatización de tareas mediante scripting es una herramienta fundamental para los 
administradores de sistemas en entornos Windows: 
Existen varias opciones para ello, siendo PowerShell el entorno más potente y flexible actualmente. 
PowerShell permite escribir scripts avanzados utilizando cmdlets (comandos especializados diseñados 
para administrar el sistema) y un lenguaje orientado a objetos que facilita el acceso a servicios, 
configuración de red, gestión de usuarios, procesos y mucho más. Junto a PowerShell, los archivos por 
lotes con extensión .bat, basados en el antiguo intérprete de comandos (CMD), siguen siendo útiles 
para automatizaciones sencillas y tareas repetitivas como copiar archivos, lanzar programas o modificar 
variables de entorno. 
La combinación de estas herramientas permite adaptar la automatización a distintos niveles de 
complejidad, desde scripts básicos hasta soluciones completas de gestión del sistema. 
4.6.1. PowerShell 
PowerShell es un lenguaje de scripting avanzado y una interfaz de línea de comandos (CLI) desarrollada 
por Microsoft, diseñada para automatizar tareas, configurar sistemas y administrar entornos Windows 
de forma potente y flexible. Su primera versión fue lanzada en noviembre de 2006 para Windows XP 
SP2, Vista y Windows Server 2003, y requería .NET Framework 2.0 o superior. Actualmente, PowerShell 
ha evolucionado hacia una versión multiplataforma (PowerShell 7.x), basada en .NET Core y disponible 
para Windows, Linux y macOS. 
Desde 2016, PowerShell es de código abierto y está disponible en GitHub bajo licencia MIT, lo que ha 
impulsado su adopción y evolución en entornos heterogéneos. Su principal fortaleza radica en que no 
trabaja solo con texto, como otros intérpretes de comandos, sino con objetos. Los comandos de 
PowerShell, denominados cmdlets (command-lets), no devuelven texto plano, sino instancias de 
objetos .NET, lo que permite manipular directamente sus propiedades y métodos. Esto habilita flujos de 
trabajo complejos mediante canalizaciones (pipeline) entre comandos sin necesidad de programación 
adicional.

---

Administración del Sistema Operativo y software de Base 
77 
Además, PowerShell incluye cuatro tipos de comandos: 
• Cmdlets: comandos nativos del entorno. 
• Funciones: bloques reutilizables definidos por el usuario. 
• Scripts: archivos .ps1 que agrupan múltiples instrucciones. 
• Comandos nativos de Windows: compatibles con CMD o archivos .bat. 
PowerShell permite gestionar remotamente sistemas, ejecutar scripts en varios equipos 
simultáneamente, controlar configuraciones, instalar software o realizar tareas administrativas en 
servidores y estaciones de trabajo sin intervención manual directa. Su sintaxis admite condicionales, 
bucles, funciones personalizadas, alias para simplificar comandos y acceso completo a las bibliotecas del 
.NET Framework, lo que lo convierte también en un entorno de programación poderoso. 
Por ejemplo, un administrador puede automatizar la actualización del software antivirus en múltiples \nequipos remotos con un único script. A continuación, se muestra un ejemplo práctico de uso remoto: 
$computers = @("Equipo1", "Equipo2", "Equipo3", "Equipo4") 
$command = { 
    $antivirus = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like 
"*Antivirus*" } 
    if ($antivirus) {  
         Write-Host "Actualizando Antivirus en $env:COMPUTERNAME..." 
         Start-Process "C:\Program Files\Antivirus\update.exe" -ArgumentList 
"/silent" 
     } else { 
         Write-Host "Antivirus no encontrado en $env:COMPUTERNAME." 
     } 
} 
foreach ($computer in $computers) {  
    Invoke-Command -ComputerName $computer -ScriptBlock $command -Credential (Get-
Credential) 
} 
Este script define una lista de equipos, prepara un bloque de comandos ($command) que se ejecuta en 
cada uno, y luego lo lanza remotamente mediante Invoke-Command, solicitando credenciales 
administrativas. Gracias a la arquitectura basada en objetos y la capacidad de ejecución remota, 
PowerShell se ha convertido en la herramienta de referencia para la administración moderna de 
sistemas Windows.

---

Administración del Sistema Operativo y software de Base 
78 
4.6.1.1. Algunos de los comandos CMDLETS 
• Get-Command 
Muestra todos los comandos disponibles para tu sesión actual en PowerShell. 
• Get-Help 
Proporciona ayuda fundamental para saber exactamente qué es lo que estamos haciendo o con 
qué otras opciones podemos trabajar en nuesta línea de comandos. 
Una forma habitual de utilizar este cmdlet es la siguiente: 
Get-Help [[-Name] ] [-Path ] [-Category <String[]>] [-Component <String[]>] 
• Set-ExecutionPoliciy 
Como medida de seguridad y para evitar la inyección de código malicioso, Microsoft deshabilita 
por defecto, la posibilidad de ejecutar scripts en el entorno PowerShell. 
A la mayoría de los desarrolladores en cambio, les interesa (y mucho), poder disponer de esta 
funcionalidad. 
Para conseguirlo, el comando Set-ExecutionPolicy establece distintos niveles de control, 
alrededor de los cuales pueden ejecutarse distintos scripts, que son los siguientes: 
• Restricted 
No carga archivos de configuración, ni ejecuta scripts. Esta es la configuración 
predeterminada. 
• Allsigned 
Requiere que todos los scripts y archivos de configuración estén firmados por un editor de 
confianza. 
• Remotesigned 
Requiere que todos los scripts y archivos de configuración descargados de Internet estén 
firmados por un editor de confianza. 
• Unrestricted 
Carga todos los archivos de configuración y ejecuta todos los scripts. 
Como en el caso de get-command, si no sabemos en qué entorno «nos estamos moviendo» 
podemos averiguarlo fácilmente ejecutando el comando Get-ExecutionPolicy.

---

Administración del Sistema Operativo y software de Base 
79 
• Get-Service 
Es útil saber con qué servicios podemos contar en el sistema, y podemos averiguarlo 
sencillamente con el comando Get-Service. 
Si necesitamos conocer el estado de un servicio concreto, escribiremos el nombre del mismo 
tras el sufijo -Name. 
• ConvertTo-HTML 
Si necesitamos extraer los datos de PowerShell para compartirlos con una tercera persona, el 
comando ConvertTo-HTML es una forma muy recomendable de hacerlo. 
Para utilizarlo hay que incluirlo como sufijo de cualquier otro comando cuyo output queramos 
guardar. 
Además, deberemos determinar el nombre de un archivo HTML. 
• Get-EventLog 
Permite la utilidad de analizar los registros de eventos de nuestro equipo. 
Para hacerlo, utilizaremos el parámetro -Log seguido del nombre del archivo de registro para 
ver un registro específico. 
Una forma de utilizarlo es la siguiente: Get-EventLog -Log "Application". 
• Get-Process 
Sirve para entender qué procesos se están ejecutando en un momento determinado. 
Además de para saber qué es lo que se está ejecutando, este cmdlet nos sirve como primer paso 
para terminar un proceso que no está funcionando como debería o qué se ha bloqueado. 
Para ello utilizaremos la orden Stop-Process. 
Una forma de realizar ambas acciones podría ser la siguiente: 
• Get-Process 
• Stop-Process -processname notepad 
• Clear-History 
Se utiliza para borrar el histórico de comandos que hemos empleado hasta ese momento. 
Para borrar el histórico de un comando en concreto, le añadiremos el apendice -Command. Por \nejemplo, de esta forma: 
Clear-History -Command *help*

---

Administración del Sistema Operativo y software de Base 
80 
• Where-Object 
Crea un filtro que controla los objetos que se van a pasar con una canalizacion de comandos. 
Filtra los objetos que recibe, bien como entrada canalizada o a traves del parametro "- 
inputobject". 
Determina que objetos se van a pasar a través de la canalización mediante la evaluación de un 
bloque de script que puede incluir una referencia a un objeto que se va a filtrar. 
Si el resultado de la ejecución es verdadero, el objeto que se va a procesar se pasa a través de la 
canalización, en caso contrario, el objeto queda descartado. 
• Set-AuthenticodeSignature 
Para añadir una firma Authenticode a un script o archivo, para mantener nuestro trabajo seguro 
y evitar posibles modificaciones. 
 
 
 
 
+ Info 
Puedes consultar más información en la web oficial de Microsoft. 
https://docs.microsoft.com/en-us/powershell/ 
 
4.6.2. Batch 
Los scripts batch o archivos .bat (archivos de procesamiento por lotes) son la forma más simple de 
scripting en comparación con PowerShell. Estos archivos contienen una serie de comandos que se \nejecutan en secuencia, lo que permite automatizar tareas en el sistema operativo. 
A diferencia de PowerShell, los scripts .bat no tienen la capacidad de manejar objetos o interactuar con \nestructuras de datos complejas, lo que los hace menos potentes. Sin embargo, su simplicidad es una 
ventaja en muchos casos, ya que son más fáciles de escribir, entender y ejecutar, especialmente para 
tareas sencillas. 
Un script .bat se ejecuta utilizando el símbolo del sistema (CMD), y su sintaxis está basada en 
comandos de línea tradicionales de DOS, como echo, copy, del, mkdir, entre otros. 
Esto hace que los scripts .bat sean ideales para tareas rutinarias y repetitivas, como ejecutar programas 
de manera secuencial, copiar o mover archivos de una carpeta a otra, renombrar archivos, borrar 
archivos temporales, o configurar opciones del sistema como la red o los servicios.

---

Administración del Sistema Operativo y software de Base 
81 
Dado que no requieren un conocimiento avanzado de programación o administración, los scripts .bat 
son fáciles de crear incluso para usuarios con conocimientos limitados de scripting. A pesar de su 
simplicidad, los scripts .bat son útiles para automatizar procesos en entornos de TI, donde tareas como 
la instalación de software, la copia de archivos de respaldo, la configuración de ciertos parámetros de 
red o la eliminación de archivos innecesarios pueden ser realizadas de manera eficiente sin intervención 
manual. 
Si bien no ofrecen las capacidades avanzadas de PowerShell, como la manipulación de objetos o el 
acceso a recursos remotos, los scripts .bat siguen siendo una herramienta esencial para la 
automatización de tareas en sistemas Windows, especialmente en escenarios en los que no se requiere 
una lógica compleja o integración con otras aplicaciones. 
Ejemplo 
Imaginemos en este caso, que un usuario necesita hacer una limpieza en su ordenador de manera 
regular. Una tarea común es eliminar los archivos temporales para liberar espacio en el disco duro y 
mejorar el rendimiento del sistema. Se puede automatizar esa tarea utilizando un script .bat sencillo. 
@echo off \necho Eliminando archivos temporales... 
:: Eliminar archivos temporales de la carpeta Temp 
del /q /f %temp%\* 
:: Eliminar archivos temporales de la carpeta Prefetch del /q /f 
C:\Windows\Prefetch\* 
:: Vaciar la papelera de reciclaje \necho Vaciar la papelera de reciclaje... 
rf /s /q C:\$Recycle.Bin \necho Tareas completadas 
pause 
• @echo off: Evita que me muestren los comandos en la consola mientras se ejecutan permitiendo 
que la salida de los datos sea más limpia. 
• del/q/f%temp%\*: elimina todos los archivos de la carpeta temporal del sistema del usuario 
actual. El parámetro /q cancela la confirmación de eliminación y el parámetro /fuerza la \neliminación de los archivos de solo lectura. 
• del /q/f C:\Windows\Prefetch\*: elimina todos los archivos de la carpeta Prefetch que 
contienen información sobre los programas que se inician para mejorar el rendimiento del 
sistema.

---

Administración del Sistema Operativo y software de Base 
82 
• rd/s/q C:$Recycle.Bin: vacía la papelera de reciclaje del sistema. El parámetro /s elimina todos 
los subdirectorios y archivos de la papelera, y el parámetro /q evita las confirmaciones de \neliminación lo que permite que se elimine automáticamente. 
• pause: detiene la ejecución del script y le muestra un mensaje en la consola, permitiendo al 
usuario ver los resultados antes de cerrar la ventana de la consola. 
Cuando se ejecute el script, la consola mostrará los mensajes informando de la eliminación de archivos 
temporales y de que se ha vaciado la papelera de reciclaje. Al final el script se pausará y permitirá al 
usuario verificar que todo se ha realizado correctamente antes de cerrar la ventana de la consola. 
4.7. Otras herramientas 
4.7.1. Predominante en Windows 
SysInternals Suite 
Es un conjunto de herramientas gratuitas, de administración y monitorización de sistemas para 
Windows. Incluye más de 67 aplicaciones, entre las que se encuentran algunas tan populares como: 
ProcessExplorer, BgInfo, Autoruns, Dbgview, Procmon y TCPView. muy útiles. 
Anti-Twin 
Permite encontrar archivos similares y duplicados. Estos archivos de texto e imágenes se analizan 
fácilmente. Compara el contenido de los archivos, incluso si tienen diferente nombre. 
TreeSize 
Muestra el espacio utilizado, el tamaño de los archivos, directorios y subdirectorios, de forma clara y 
gráfica, para poder gestionar los discos duro, SSD o partición, cuando el espacio de almacenamiento 
libre es escaso. 
NetScan 
Permite obtener una visión general de los dispositivos conectados en la red en cuestión de segundos, 
muestra los puertos abiertos en cada dispositivo y su dirección IP. 
AOMEI Partition Assistant 
Es un programa de particionamiento de discos duros. (un disco duro, se puede formatear definiendo un \nespacio menor al total del disco, de forma que podemos crear diferentes particiones dentro de un 
mismo disco físico, que aparecerán visiblemente como si fueran diferentes discos, por ejemplo, en 
Windows, aparecerán en Mi equipo, distintas letras de unidades de discos.

---

Administración del Sistema Operativo y software de Base 
83 
Malwarebytes 
Es una solución profesional para evitar malware, ransomware, exploits y sitios web maliciosos, 
Malwarebytes. Se puede instalar en un ordenador después de haber sido infectada e incluso entonces 
logra identificar la mayoría de programas malintencionados que ya están activos. 
SumatraPDF 
SumatraPDF es una alternativa rápida y de alto rendimiento a los lectores PDF tradicionales. Los menús 
tienen un diseño minimalista y el software se centra en lo esencial. 
Ninite 
Se puede seleccionar todo el software básico y esencial necesario e instalarlo en un solo clic. Todos los 
programas se instalan automáticamente. 
PDFCreator 
Nos permite crear documentos PDF desde cualquier aplicación, aparece como si fuera una impresora, 
generando un documento .pdf que podremos enviar por correo electrónico, sin que se modifique su 
formato, o guardarlo para imprimirlo posteriormente en caso de que no tengamos impresora disponible \nen ese momento (en compras por internet etc.). 
Trend Micro Ransomware File Decryptor 
Nos permite verificar si existe una forma de descifrar archivos que han sido infectados por ransomware. 
Un ransomware, o "secuestro de datos" en español, es un tipo de programa dañino que restringe el 
acceso a determinadas partes o archivos del sistema operativo infectado y pide un rescate a cambio de 
quitar esta restricción. 
4.7.2. Predominante en Linux 
Ansible 
Ansible es una herramienta de automatización que permite gestionar múltiples servidores de forma 
remota mediante SSH, sin necesidad de instalar agentes. Utiliza playbooks en YAML para definir tareas 
como instalar software o configurar servicios, aplicándolas automáticamente con el comando ansible-
playbook.

---

Administración del Sistema Operativo y software de Base 
84 
VNC 
VNC (Virtual Network Computing) permite acceder de forma remota al escritorio gráfico de un 
servidor Linux, útil para tareas que requieren entorno visual. Requiere instalar y configurar un servidor 
VNC (como TigerVNC) en el equipo remoto y conectarse desde un cliente VNC. 
Webmin 
Webmin es una herramienta de administración remota basada en navegador que permite gestionar 
servidores Linux desde una interfaz gráfica web. Facilita la configuración de servicios, usuarios, redes o 
bases de datos sin usar la línea de comandos, accediendo vía https://IP-del-servidor:10000. 
RDP 
RDP es un protocolo que permite acceder al escritorio gráfico de forma remota. En Linux se puede 
habilitar mediante xrdp, lo que permite conectarse desde cualquier cliente RDP, como el Escritorio 
Remoto de Windows, tras instalar y activar el servicio. 
SSHFS 
SSHFS permite montar sistemas de archivos remotos a través de SSH, accediendo a ellos como si fueran 
carpetas locales. Es una alternativa segura y sencilla al FTP, ideal para gestionar archivos en servidores 
remotos desde el sistema local. 
4.7.3. Multiplataforma 
Clonezilla 
Es una herramienta gratuita de código abierto, para clonar discos duros creando una imagen y para 
realizar copias de seguridad. 
FileZilla 
El acceso a los servidores FTP generalmente requiere un cliente FTP. De hecho, esto está integrado en \nel sistema operativo y en el navegador web, pero bastante limitado a nivel funcional. FileZilla está \nequipado con muchas funciones y está disponible para Linux, Windows y MacOS. Además del protocolo 
FTP clásico, también se admiten protocolos como SFTP, FTPS, SSH y SSL. 
PuTTY 
Este software es para acceder a los sistemas Linux y MacOS, se puede utilizar el protocolo SSH. Puede 
generar archivos clave utilizando PuTTYgen.

---

Administración del Sistema Operativo y software de Base 
85 
TeamViewer 
Es una herramienta extraordinaria para facilitar el trabajo a los administradores de sistemas, 
permitiendo controlar un ordenador sin estar físicamente en ese puesto de ese ordenador, sino que lo 
hace de forma remota (puede manejar el ratón etc. como si estuviera en el ordenador concreto). 
Hay que instalar el software en el ordenador del administrador y en el ordenador que hay que mantener 
remotamente. 
TeamViewer es una solución de software que funciona en Windows, en MacOS y otros sistemas 
operativos. 
Herramientas de monitoreo de red (según el software específico) 
Son muy necesarias para analizar los problemas de red y transmisión. 
Con la ayuda de herramientas de monitoreo es posible registrar y analizar mensajes y advertencias en el 
sistema operativo y obtener una orientación para solucionarlos. Ejemplos de estas herramientas son: 
• Para Windows: PRTG, Orion, Whatsup, Nagios, Omnipeek, Netbrain, Netcrunch… 
• Para Linux: Nagios, Omnipeek, NetBrain 
5. Configuración optima del sistema en Windows 
Una configuración adecuada del sistema es esencial para garantizar su estabilidad, seguridad y eficiencia 
a largo plazo. En el contexto de la administración de sistemas, optimizar la configuración no solo implica 
ajustar parámetros técnicos, sino también establecer prácticas operativas que reduzcan riesgos, 
mejoren el rendimiento y faciliten la gestión. 
Este bloque recoge un conjunto de recomendaciones clave orientadas a reforzar la seguridad (como el 
uso de cuentas con privilegios diferenciados y la configuración de permisos por roles), asegurar la 
disponibilidad del sistema (mediante actualizaciones automáticas y uso de hardware adecuado), y 
mejorar la capacidad de diagnóstico y mantenimiento (gracias al uso del registro de eventos). La 
correcta aplicación de estas medidas contribuye a un entorno más robusto, eficiente y controlado, \nespecialmente en sistemas Windows tanto a nivel personal como corporativo. 
5.1. Uso de cuenta de administrador 
El uso de una cuenta de administrador exclusiva para la gestión del sistema y una cuenta estándar para 
las tareas diarias es una práctica necesaria para poder garantizar la seguridad y estabilidad de un 
sistema operativo, ya sea en Windows Server o en Windows 10/11.

---

Administración del Sistema Operativo y software de Base 
86 
Esta separación ayuda a prevenir cambios no autorizados o accidentalmente peligrosos en la 
configuración del sistema, ya que las cuentas de administrador tienen permisos completos para 
modificar configuraciones críticas, instalar o desinstalar programas y cambiar políticas de seguridad. 
Al utilizar una cuenta estándar para las actividades diarias, se limita el acceso a funciones importantes 
del sistema, reduciendo el riesgo de infecciones por malware o configuraciones erróneas. 
Además, usar una cuenta estándar para navegar por Internet o realizar tareas cotidianas disminuye el 
riesgo de que el malware pueda afectar el sistema, ya que no tendría acceso completo para realizar 
cambios perjudiciales. 
Esta separación también facilita un control más estricto sobre quién tiene acceso a configuraciones del 
sistema y permite aplicar el principio de mínimos privilegios, lo que asegura que solo se otorguen 
permisos necesarios para cada tarea. 
En general, esta práctica no solo mejora la seguridad, sino que también reduce la probabilidad de \nerrores accidentales que puedan dañar el sistema, asegurando que solo los administradores puedan 
realizar modificaciones importantes. 
5.2. Configurar actualizaciones automáticas 
Como ya hemos visto, el mantener el sistema operativo y las aplicaciones actualizadas es fundamental 
para proteger el sistema contra vulnerabilidades conocidas. Configurar las actualizaciones automáticas 
asegura que el sistema reciba las últimas actualizaciones de seguridad. 
Para configurar las actualizaciones automáticas hay que: 
• Hacer clic en el botón de Inicio y selecciona Configuración. 
• Acceder desde allí a la sección de Actualización y seguridad. 
• Dentro de esta sección, se verá la opción de Windows Update, donde puedes comprobar si hay 
actualizaciones disponibles y configurarlas según tus necesidades. 
• Para asegurarnos de que las actualizaciones se realicen automáticamente, simplemente 
activamos la opción "Actualizar automáticamente". Así asegurando que el sistema reciba las 
últimas actualizaciones de seguridad, correcciones de errores y mejoras de rendimiento de 
manera continua. 
También se pueden personalizar las horas activas en las que el sistema puede reiniciarse para aplicar 
actualizaciones, asegurando que el reinicio del sistema no interrumpa el uso diario y para los usuarios de 
Windows 10 Pro o Enterprise, también existe la opción de configurar las políticas de actualización a 
través de Editor de directivas de grupo o Windows Update for Business, lo que permite un control aún 
más detallado sobre cuándo y cómo se instalan las actualizaciones, correcciones de errores y mejoras 
de rendimiento, sin que el usuario tenga que intervenir. 
Esta práctica minimiza los riesgos de ciberataques y mejora la estabilidad del sistema.

---

Administración del Sistema Operativo y software de Base 
87 
5.3. Uso del registro de eventos 
El registro de eventos es una herramienta esencial para la administración de sistemas, ya que permite a 
los administradores realizar un seguimiento detallado de las actividades del sistema. 
Mediante el registro de eventos, se pueden identificar rápidamente problemas de hardware, software o 
seguridad, lo que facilita la solución de problemas antes de que se conviertan en incidentes críticos. 
Es recomendable revisar y configurar los registros para capturar eventos clave que podrían indicar fallos 
inminentes o comportamientos anómalos del sistema. 
Por ejemplo, si un servidor experimenta una desaceleración en su rendimiento, el administrador puede 
consultar el registro de eventos para identificar errores recurrentes relacionados con el uso de la 
memoria o fallos en un disco duro. 
Si el registro muestra múltiples errores de lectura en el disco, esto podría indicar un problema con el 
hardware, lo que permitiría al administrador tomar medidas preventivas, como realizar un respaldo de 
los datos y reemplazar el hardware defectuoso antes de que el problema cause una falla total del 
sistema. 
5.3.1. Uso del Visor de eventos en Windows Server 
En el contexto de Windows Server, la herramienta que permite consultar y gestionar los registros del 
sistema de forma estructurada es el Visor de eventos. A través de esta utilidad, el administrador puede \nexaminar en detalle los sucesos generados por el sistema operativo, los servicios instalados y los 
componentes de seguridad, con una organización clara y accesible. 
El visor presenta una interfaz jerárquica en la que los eventos se agrupan en categorías como 
Aplicación, Sistema, Seguridad, Instalación y Eventos reenviados. Cada entrada incluye datos como la 
hora del suceso, el origen, el nivel de gravedad (informativo, advertencia, error o crítico), y una 
descripción del evento. Esta información resulta especialmente útil para identificar con precisión la 
causa de un fallo, comprobar la actividad reciente o verificar la correcta ejecución de procesos clave. 
Los registros de la categoría Aplicación permiten supervisar el comportamiento de programas y 
servicios concretos, como servidores web, bases de datos o herramientas personalizadas. En cambio, la 
categoría Sistema recoge eventos generados por el propio sistema operativo, incluyendo la gestión de 
controladores, red, impresión o almacenamiento. Ambos tipos de eventos son claves para el 
diagnóstico técnico en entornos productivos. 
Dentro de los eventos de Seguridad se agrupan los intentos de inicio de sesión, los cambios de permisos 
y las acciones relacionadas con el control de accesos. Este registro es fundamental en tareas de 
auditoría y en la prevención de accesos no autorizados, sobre todo en entornos donde se gestionan 
múltiples usuarios o datos sensibles. 
El Visor de eventos permite aplicar filtros para localizar rápidamente eventos específicos por fecha, 
tipo, servicio o nivel de severidad. Además, se puede vincular su funcionamiento con otras herramientas 
del sistema, como el Programador de tareas o las políticas de grupo, para que determinadas condiciones 
generen alertas automáticas o desencadenen respuestas específicas.

---

Administración del Sistema Operativo y software de Base 
88 
En redes corporativas, es común complementar esta supervisión con herramientas que permiten 
centralizar y correlacionar eventos desde distintos equipos. Windows Event Forwarding, Splunk, 
Microsoft Sentinel o soluciones SIEM equivalentes permiten integrar los registros en plataformas de 
análisis más avanzadas, mejorando la capacidad de respuesta ante incidentes y facilitando el 
cumplimiento normativo. 
Dominar el uso del Visor de eventos en Windows Server forma parte de la práctica habitual en la 
administración de sistemas. No solo permite resolver errores con mayor eficacia, sino que también 
contribuye a reforzar la seguridad y estabilidad del entorno de trabajo, anticipándose a fallos antes de 
que afecten a la disponibilidad o al rendimiento del sistema. 
5.4. Uso de unidades SSD en servidores 
Los discos SSD (Solid State Drive) son significativamente más rápidos que los discos duros tradicionales 
(HDD), lo que mejora el tiempo de acceso a los datos y el rendimiento general del sistema. En 
servidores, donde el procesamiento de datos y la disponibilidad de servicios es crítica, usar SSDs puede 
reducir los tiempos de arranque, optimizar la velocidad de lectura/escritura y mejorar la eficiencia 
operativa, lo que es fundamental para entornos que requieren alta disponibilidad y velocidad. 
Puedes consultar en el temario general, unidad segunda del bloque II, "Periféricos: conectividad y 
administración..." para mayor información sobre estos dispositivos. 
5.5. Configuración de permisos de acceso de roles \nen Windows Server 
En un entorno de servidor corporativo, resulta fundamental establecer un sistema de control de acceso 
que garantice que cada usuario pueda acceder únicamente a los recursos y funcionalidades necesarias 
para el desarrollo de sus funciones. Esta gestión precisa se articula a través de la correcta configuración 
de roles de usuario, la asignación de permisos específicos y la aplicación de políticas de grupo, todo ello 
gestionado de manera centralizada mediante Active Directory. 
Definir grupos de usuarios 
El primer paso para organizar eficazmente el acceso a los recursos consiste en definir grupos de 
usuarios que representen los distintos perfiles funcionales o áreas de trabajo de la organización, como 
recursos humanos, contabilidad o soporte técnico. 
La creación y gestión de estos grupos se realiza desde la consola "Usuarios y Equipos de Active 
Directory". Una vez definidos, los grupos se utilizan para asignar los permisos correspondientes sobre 
los diferentes recursos del sistema, como el acceso a carpetas compartidas, aplicaciones específicas o 
configuraciones de red. Este enfoque basado en roles simplifica enormemente la administración: al 
incorporar un usuario a su grupo correspondiente, este hereda automáticamente las configuraciones y 
restricciones ya establecidas.

---

Administración del Sistema Operativo y software de Base 
89 
Aplicar politicas de configuración y seguridad 
Además de la gestión por grupos, Windows Server permite aplicar políticas de configuración y 
seguridad mediante las Políticas de Grupo, conocidas como GPO (Group Policy Objects). Estas políticas 
se gestionan a través de la Consola de Administración de Directivas de Grupo, una herramienta que 
permite aplicar de forma centralizada un conjunto amplio de directrices tanto a usuarios como a \nequipos. Las GPO permiten, entre otras funciones, establecer requisitos de contraseñas seguras, 
restringir el acceso a ciertas aplicaciones, definir la configuración del entorno de escritorio, limitar el uso 
de dispositivos externos o controlar la instalación de actualizaciones del sistema. 
Niveles de aplicación 
Una de las grandes ventajas de las GPO es su flexibilidad para aplicarse en distintos niveles de la 
jerarquía de Active Directory. Es posible aplicar políticas a todo el dominio, afectando a todos los 
usuarios y equipos que lo componen; también pueden dirigirse a unidades organizativas concretas, 
permitiendo un control más granular y adaptado a las necesidades de departamentos específicos. 
Incluso es posible filtrar su aplicación a través de grupos de seguridad, de modo que solo determinados 
usuarios dentro de una misma unidad organizativa se vean afectados por ciertas configuraciones. 
Ventajas 
La implementación coordinada de grupos de usuarios y políticas de grupo en Active Directory ofrece 
múltiples beneficios: permite controlar el acceso a recursos de manera estructurada y coherente, 
reduce los errores derivados de la configuración manual, mejora la seguridad al aplicar restricciones 
precisas y contribuye al cumplimiento de normativas internas y externas relacionadas con la gestión de 
la información. 
Esta centralización facilita considerablemente las tareas del administrador del sistema, optimizando el 
mantenimiento y la consistencia en la configuración de todos los equipos y usuarios de la red. 
6. Mantenimiento y reparación 
En este punto vamos a hablar sobre el mantenimiento y reparación de sistemas operativos, 
centrándonos especialmente en los sistemas Windows. Normalmente, el mantenimiento y la reparación 
van de la mano. 
El mantenimiento del sistema operativo suele prevenir su mal funcionamiento o perdida de velocidad. 
En caso de avería, si el sistema es estable, muchas veces se puede reparar aplicándole las mismas 
acciones que se realizan en el mantenimiento.

---

Administración del Sistema Operativo y software de Base 
90 
 
 
 
+ Info 
También el mantenimiento de hardware, como es la limpieza del 
polvo que se acumula en los ventiladores, previene fallos o roturas 
del hardware, qué lógicamente se transforman en fallos en el 
funcionamiento del software. (Incluso llegando a la rotura física en 
casos de sobrecalentamiento). 
 
 
Sin embargo, cuando el sistema no es estable, debemos recurrir a otras medidas, dependiendo del 
sistema operativo. Algunas de ellas pueden ser: 
Creación de un disco de arranque 
Desde este disco podemos intentar solucionar los problemas. Los más importantes son: 
• Disco de arranque del propio sistema operativo. Normalmente permite realizar acciones 
correctivas para intentar solucionar el problema. Incluso permite la reinstalación del sistema 
operativo, lo cual soluciona cualquier fallo del mismo. 
• Disco de arranque de antivirus. Este es el más aconsejable cuando se intuye que el problema lo 
ha ocasionado un virus. 
• Disco de arranque de utilidades. Estas suelen contar con muchas herramientas, como: 
• Antivirus, antimalware, etcétera. 
• Explorador de ficheros. 
• Programas para copias de seguridad. 
• Restauración de ficheros. 
• Creación y restauración de particiones. 
• Limpiadores. 
• Herramientas de recuperación. 
• Etcétera.

---

Administración del Sistema Operativo y software de Base 
91 
 
 
 
El experto opina 
Posiblemente, el mejor de ellos es el Hiren´s Boot CD. 
Se puede instalar en un CD o en un pendrive. 
Tiene una gran cantidad de herramientas muy útiles para 
mantener y reparar un ordenador. 
Aunque antiguamente contenía programas sin licencia, estos se 
han ido sustituyendo por software libre y ahora parece ser 
totalmente legal. 
 
Arrancar en modo línea de comandos 
Es un entorno con menos funcionalidades aún que el anterior. Desde aquí se pueden intentar muchas 
cosas, como buscar errores en disco, reparar el MBR, reparar archivos de sistema que hayan sido 
dañados, etcétera. 
Opciones avanzadas de inicio de Windows 10 
Permite realizar distintas tareas, como arrancar con inicio avanzado desde donde podrás intentar 
reparar el sistema.

---

Administración del Sistema Operativo y software de Base 
92 
Restaurar sistema 
En Windows 10 y 11, la función Restaurar sistema permite recuperar el estado del equipo ante fallos o 
problemas recientes, sin necesidad de formatear ni perder archivos personales. Esta herramienta resulta \nespecialmente valiosa cuando el sistema presenta malfuncionamientos tras instalar aplicaciones 
conflictivas, controladores incompatibles o actualizaciones problemáticas del sistema operativo. 
El mecanismo de restauración trabaja con puntos previamente creados, que son capturas del estado de 
Windows en momentos clave. Estos puntos se generan automáticamente antes de actualizaciones 
importantes, aunque también pueden crearse manualmente desde la configuración de protección del 
sistema. 
Cabe destacar que este proceso afecta directamente a la instalación de software: todos los programas 
añadidos después del punto de restauración seleccionado serán desinstalados automáticamente, 
mientras que las aplicaciones eliminadas posteriormente a ese punto reaparecerán. 
Para ejecutar una restauración, existen dos vías principales: mediante el acceso desde Panel de control 
> Sistema > Protección del sistema > Restaurar sistema cuando Windows funciona normalmente, o a 
través del entorno de recuperación si el sistema no inicia correctamente. 
Es importante comprender que, aunque este método preserva documentos personales, la 
desinstalación masiva de programas posteriores al punto de restauración puede requerir reinstalaciones 
manuales de software válido que se quiera conservar. 
Esta solución resulta particularmente eficaz contra errores sistémicos, cuelgues recurrentes o 
inestabilidad general del sistema. Sin embargo, su eficacia depende completamente de la existencia de 
puntos de restauración previos. 
Por ello, se recomienda mantener activada la protección del sistema y complementar esta función con 
prácticas de mantenimiento periódico, incluyendo la desinstalación adecuada de programas no \nesenciales mediante los métodos estándar (Panel de Control o Configuración de Windows), para 
reducir la necesidad de restauraciones drásticas del sistema. 
 
 
 
 
+ Info 
La recuperación de un estado anterior solo es posible si se han 
creado puntos de restauración. 
Windows suele crearlos ante eventos tales como la instalación de 
nuevo software.

---

Administración del Sistema Operativo y software de Base 
93 
 
Reinstala el sistema operativo 
Si se tiene una copia de seguridad de la información importante, la solución (cuando todo lo demás 
falla) es reinstalar el sistema operativo. Se puede hacer directamente sobre el que tenemos y podría 
funcionar. 
Sin embargo, lo que nunca falla y va a dar mejor rendimiento en cuanto a resultado es formatear e 
instalar desde cero. 
6.1. Pasos a seguir para mantener/reparar el Sistema 
Operativo 
Podemos realizar procesos rutinarios, para tener el sistema en un estado óptimo, evitando que se 
ralentice, previniendo entrada de virus etc. 
Estos pasos a seguir dependerán de la versión de Windows instalada, ya que algunas versiones ofrecen 
diferentes herramientas y opciones de recuperación.

---

Administración del Sistema Operativo y software de Base 
94 
Paso 1. Arrancar el sistema y hacer una copia de seguridad 
Si el sistema no arranca correctamente, o da fallos continuos, lo primero en hacer será intentar crear 
una copia de seguridad con los últimos cambios que hayamos podido realizar. 
• En caso de que no pueda arrancar de forma adecuada o no se tenga acceso a Internet, intentar 
arrancar en modo a prueba de fallos con conexión a red. (y si no es posible, intentar sin 
conexión a la red) 
• Si aun así sigue fallando, prueba a arrancar en modo a prueba de fallos normal. 
• Si esto no funciona tendremos que recurrir a regenerar el S.O. (opción de algunas versiones de 
reinstalar, manteniendo datos y configuraciones) o volverlo a instalarlo de nuevo. 
Paso 2. Verificar y reparar archivos del sistema con SFC 
Si el sistema sigue dando errores después de iniciar en modo seguro o experimenta fallos continuos, es 
recomendable verificar la integridad de los archivos del sistema con la herramienta System File Checker 
(SFC). 
1. Abrir Símbolo del sistema como Administrador: 
• Pulsa Windows + X, selecciona Símbolo del sistema (Administrador) o PowerShell 
(Administrador). 
• También puedes buscar "cmd" en el menú de inicio, hacer clic derecho y seleccionar 
Ejecutar como administrador. 
2. Ejecutar el comando SFC. 
El comando sfc /scannow es una herramienta de Windows que permite examinar todos los 
archivos de sistema protegidos y reemplazar aquellos dañados o corruptos con una copia 
almacenada en caché. Se ejecuta desde la línea de comandos y es útil para la resolución de 
problemas relacionados con la integridad del sistema operativo. Cuando se ejecuta este 
comando, Windows inicia un escaneo de los archivos de sistema protegidos y verifica la 
integridad de cada archivo, si encuentra archivos dañados o modificados, los reemplaza con una 
copia correcta de la carpeta de caché de Windows ubicada en %WinDir%\System32\dllcache. 
Puede requerir reiniciar el equipo para completar la reparación. Este comando es especialmente 
útil cuando el sistema experimenta errores inesperados, bloqueos o fallos en el funcionamiento 
de aplicaciones del sistema. 
Es recomendable utilizarlo cuando hay problemas con archivos del sistema después de una 
actualización o instalación de software, cuando se encuentrar errores frecuentes o bloqueos en 
aplicaciones del sistema, cuando hay pantallazos azules (BSOD) relacionadas con archivos de 
sistema, cuando hay problemas de estabilidad en el Explorador de Windows o cuando Windows 
no arranca correctamente. 
El comando sfc /scannow es una herramienta poderosa para la reparación de archivos de 
sistema en Windows, permitiendo corregir errores y restaurar la estabilidad del sistema 
operativo. Se recomienda ejecutarlo cuando se sospeche que hay archivos de sistema dañados o 
faltantes.

---

Administración del Sistema Operativo y software de Base 
95 
Uso SFC /SCANNOW 
• Abrir el Símbolo del sistema como administrador: Presiona Win + R, escribe cmd, y presiona 
Ctrl + Shift + Enter para abrir la consola con privilegios elevados. 
• También puedes buscar "Símbolo del sistema" en el menú Inicio, hacer clic derecho y 
seleccionar "Ejecutar como administrador". 
sfc /scannow 
Este proceso puede tardar varios minutos en completarse. Si encuentra archivos corruptos, 
intentará repararlos automáticamente. Si el sistema no encuentra problemas, se mostrará el 
mensaje: Protección de recursos de Windows no encontró ninguna infracción de integridad. Si 
se encontraron y repararon archivos corruptos, el mensaje indicará Protección de recursos de 
Windows encontró archivos dañados y los reparó correctamente. Si no pudo repararlos, se 
recomienda analizar el archivo de registro ubicado en %WinDir%\Logs\CBS\CBS.log para 
identificar los archivos problemáticos. 
Opciones adicionales: 
• sfc /verifyonly: Realiza una verificación sin hacer reparaciones. 
• sfc /scanfile=<ruta>: Escanea y repara un archivo específico. 
• sfc /offwindir=<ruta>: Especifica la ubicación del sistema operativo si se ejecuta desde un \nentorno de recuperación. 
Paso 3. Disponer de software de mantenimiento 
Existen programas que debemos tener instalados obligatoriamente como en un antivirus, y otros que 
nos facilitan el buen mantenimiento de nuestros sistemas: 
• Software antivirus: 
Hay muchos tipos de programas antivirus, dependiendo del nivel de seguridad y opciones de 
configuración que deseemos. Algunas versiones permiten dar permiso especifico a cada 
programa ejecutable (.exe) y otras muchas opciones de puertos etc. 
Lo básico es que haga la función de antivirus y firewall (cortafuegos), como mínimo. 
Las versiones actuales de programas antivirus son sumamente completas en su versión de pago 
y no es necesario ralentizar más nuestro ordenador con otras utilidades anti espías, etc. 
No aconsejamos el uso de antivirus gratuitos. 
Es desaconsejable siempre, tener instalado más de un programa antivirus, se reduce muchísimo 
la velocidad del equipo e incluso en ocasiones se producen fallos. Si se tiene activado el firewall 
del software antivirus, es mejor desactivar el que incorpora Windows.

---

Administración del Sistema Operativo y software de Base 
96 
 
 
 
El experto opina 
Nuestro consejo es instalar Panda Dome (el mejor en nuestra 
opinión). 
Otras opciones válidas podrían ser: Avira Free, AVG Free, Avast 
FREE, Bitdefender Free Edition y Karpesky Free. 
 
 
• Herramienta de limpieza y optimización: descargar CCleaner. CCleaner es, posiblemente, la 
mejor herramienta para la limpieza y optimización de un ordenador.

---

Administración del Sistema Operativo y software de Base 
97 
Paso 4. Actualizar el software descargado 
Tienes que actualizar todo el software que acabas de descargar. Seguramente ya tendrás las últimas 
versiones si acabas de descargarlo, pero si ya lo tenías descargado, deberías actualizarlo. 
Además, las herramientas tipo antivirus necesitarán actualizar sus bases de datos de amenazas. 
En caso de que falle Internet y no puedas hacer ni el paso anterior ni este, puedes descargarlo desde 
otro equipo. Los ficheros de actualización de las bases de datos de amenazas también suelen estar 
disponibles para descargar. 
Paso 5. Desinstalar todo lo que no sea necesario 
• Programas que no utilices, que no conozcas o que parezcan sospechosos. 
• Elimina las barras que se añaden a los navegadores. 
• Revisa los addons (también llamados "extensiones") instalados en los navegadores y elimina los 
que no utilices. 
Una vez terminado sería aconsejable limpiar el sistema con CCleaner y también limpiar el registro de 
Windows con este programa. 
Paso 6. Modificar el inicio de Windows (solo para expertos) 
Muchos programas se configuran para arrancar cuando se inicia el sistema operativo. Así lo hace 
también gran parte del software malintencionado. 
En Windows 10 puedes ejecutar el administrador de tareas para ver qué programas se cargan al inicio. 
Para versiones anteriores puedes usar msconfig. 
Desde aquí puedes habilitarlos o deshabilitarlos:

---

Administración del Sistema Operativo y software de Base 
98 
Desde aquí también puedes: 
• Eliminar tareas y procesos (en esta sesión, no para el próximo arranque). 
• Deshabilitar servicios. 
• Ver el historial de aplicaciones, su consumo y si han usado la red. 
• Etcétera. 
Paso 7. Arranca el equipo en modo seguro sin conexión a red 
Es aconsejable desconectar el cable de red. En este momento el sistema operativo estará funcionando 
con lo mínimo. 
Puedes abrir el administrador de tareas y eliminar las que te puedan parecer sospechosas, pero no suele 
hacer falta. 
Paso 8. Pasar software antivirus 
Analizar el equipo con los antivirus, malware, etcétera. Es posible que requieran reiniciar el equipo si \nencuentran algo. Si fuera necesario, volver a arrancar en modo seguro sin red. 
Paso 9. Volver a limpiar con CCleaner 
Para asegurarnos de que el trabajo del antivirus queda bien hecho es aconsejable volver a limpiar el 
sistema y el registro. 
Paso 10. Reiniciar con conexión a red 
Reiniciar en modo seguro con el cable de red enchufado y con las funciones de red habilitadas. 
Paso 11. Instalar actualizaciones del sistema operativo 
Utilizar Windows Update para instalar las actualizaciones que no tengas instaladas. Si no pudieras en \neste modo, arranca en modo normal e instala las actualizaciones. 
6.2. Otras herramientas administrativas de configuracion 
Hasta ahora hemos visto las herramientas de los Sistemas operativos más comunes. Pero existen otro 
muchos S.O. en el Mercado y hay empresas que han desarrollado herramientas para la configuración de \nesos sistemas operativos.

---

Administración del Sistema Operativo y software de Base 
99 
Un ejemplo de ello sería PUPPET, es una herramienta de gestión de la configuración de código abierto. 
Es una herramienta diseñada para administrar la configuración de sistemas similares a Unix y a Microsoft 
Windows de forma declarativa, y didpone de una interfaz gráfica para la gestión. El usuario describe los 
recursos del sistema y sus estados utilizando el lenguaje declarativo que proporciona Puppet. 
Esta información es almacenada en archivos denominados manifiestos Puppet. Puppet descubre la 
información del sistema a través de una utilidad llamada Facter, y compila los manifiestos en un 
catálogo específico del sistema que contiene los recursos y la dependencia de dichos recursos. Estos 
catálogos son ejecutados en los sistemas de destino. 
Puppet funciona en las distribuciones de Linux, incluyendo Red Hat Enterprise Linux (y sus clones como 
CentOS y Oracle Linux), Fedora, Debian, Mandriva, Ubuntu, y SUSE, así como en múltiples sistemas 
Unix (Solaris, BSD, Mac OS X, AIX, HP-UX), y cuenta con apoyo para Microsoft Windows. 
7. Supervisión del sistema mediante logs y mensajes 
de consola en Linux 
Una parte fundamental de la administración de sistemas operativos es la supervisión del comportamiento 
del sistema. Para ello, Linux dispone de un sistema completo de registro de eventos (logs) y mensajes que 
se pueden visualizar directamente desde consola. Estos registros son esenciales para el diagnóstico de \nerrores, la detección de actividades sospechosas y el mantenimiento general del sistema. 
7.1. Archivos de log 
Linux registra de forma constante los eventos que ocurren en el sistema mediante archivos de texto 
denominados logs. Estos archivos son generados tanto por el propio núcleo del sistema como por los 
distintos servicios y aplicaciones que se ejecutan, y permiten al administrador disponer de un historial 
detallado del comportamiento del sistema. La mayoría de estos archivos se encuentran en el directorio 
"/var/log", que actúa como contenedor centralizado de los registros. 
Uno de los archivos más importantes es "syslog", o en otras distribuciones "messages", que recoge 
información general sobre el funcionamiento del sistema. Incluye notificaciones de servicios, fallos, 
advertencias, procesos que se inician o detienen, y otros mensajes del sistema operativo. Su consulta es 
habitual para obtener una visión global del estado del equipo. 
Otro archivo esencial es "auth.log", donde se registran todos los eventos relacionados con la 
autenticación. Esto incluye los inicios y cierres de sesión, el uso de comandos con privilegios de 
superusuario, los intentos fallidos de acceso y los cambios de contraseña. Su revisión periódica permite 
detectar posibles accesos no autorizados o intentos de intrusión. 
El núcleo del sistema también genera su propio registro, que se guarda en "kern.log". Este archivo 
contiene información emitida directamente por el kernel y resulta de gran utilidad para identificar \nerrores de hardware, fallos en la carga de módulos, o problemas con controladores. A su vez, el 
comando "dmesg" permite consultar en tiempo real los mensajes más recientes del kernel, \nespecialmente útiles durante el arranque o cuando se conectan o desconectan dispositivos.

---

Administración del Sistema Operativo y software de Base 
100 
El proceso de arranque queda reflejado en archivos como "boot.log", que resume el estado de los 
servicios y módulos al iniciar el sistema. Revisar este archivo puede ayudar a identificar si algún servicio 
ha fallado o si el sistema ha arrancado correctamente. 
Además de estos registros generales, existen muchos otros archivos especializados. Por ejemplo, los 
relacionados con el sistema de actualizaciones e instalación de software (/var/log/apt), con las tareas 
programadas (/var/log/cron) o con la interfaz gráfica (/var/log/Xorg.0.log). Cada uno de ellos 
permite profundizar en el comportamiento de un componente concreto del sistema. 
La lectura y comprensión de estos registros es una de las herramientas más potentes que tiene el 
administrador para conocer el estado real del sistema. Es recomendable revisarlos periódicamente, \nespecialmente cuando se produce un fallo, un reinicio inesperado o un comportamiento anómalo. 
Dominar su consulta, entender su estructura y filtrar adecuadamente los mensajes permite actuar con 
rapidez y eficacia ante cualquier incidencia. 
7.2. Comandos básicos para consultar logs 
Para que los archivos de log cumplan su función, es necesario que el administrador sepa cómo acceder a \nellos y extraer la información que necesita. Linux ofrece una serie de comandos muy potentes y 
versátiles que permiten visualizar y analizar el contenido de estos registros directamente desde la 
consola. 
El comando más simple para consultar un archivo de log es "cat", que muestra en pantalla todo el 
contenido del archivo de una vez. Aunque útil para archivos pequeños, en registros más extensos puede 
resultar poco práctico. Por ello, es habitual recurrir a "less" o "more", que permiten navegar 
cómodamente por el contenido, desplazándose hacia arriba y hacia abajo para localizar información 
relevante sin necesidad de cargar todo el archivo de golpe. 
En situaciones en las que se quiere observar en tiempo real lo que está ocurriendo en el sistema, se 
utiliza el comando "tail" con el modificador "-f". Esta instrucción muestra las últimas líneas del archivo y 
actualiza automáticamente la salida a medida que se añaden nuevos registros. Es especialmente útil 
cuando se está supervisando el comportamiento de un servicio recién iniciado o se está esperando la 
aparición de un error determinado. 
Para buscar información específica dentro de un archivo de log, el comando más utilizado es "grep". 
Con él se puede localizar una palabra o cadena concreta dentro del archivo, como por ejemplo el 
término "error" o "failed". Esta búsqueda permite filtrar rápidamente los mensajes que contienen 
información relevante sin necesidad de revisar manualmente todo el contenido. 
Además, estos comandos pueden combinarse entre sí para mejorar la precisión de las búsquedas. Por \nejemplo, es posible encadenar "tail -f" con "grep" para observar en tiempo real únicamente los eventos 
que incluyan una palabra clave determinada. Este tipo de combinaciones es muy utilizado en entornos 
donde se requiere una supervisión constante de servicios críticos. 
Dominar estas herramientas básicas es fundamental para todo administrador, ya que permiten 
identificar problemas de forma rápida, comprobar el estado de los servicios, verificar la ejecución de 
tareas automatizadas o investigar incidentes de seguridad. El conocimiento práctico de su uso agiliza el 
diagnóstico y la resolución de fallos, especialmente cuando se trabaja en sistemas en producción donde 
la rapidez en la respuesta es esencial.

---

Administración del Sistema Operativo y software de Base 
101 
7.3. Uso de journalctl 
En las distribuciones de Linux que utilizan "systemd" como sistema de inicialización entre ellas Debian, 
Ubuntu, Fedora, CentOS o Arch Linux, la gestión de los registros del sistema no se limita a archivos de 
texto en "/var/log". En su lugar, o de forma complementaria, se emplea un sistema de registro binario 
centralizado conocido como journal. Este sistema recoge todos los mensajes del sistema y de los 
servicios y los almacena en un formato estructurado, lo que permite una consulta más flexible y potente 
mediante el comando "journalctl". 
El uso básico de journalctl sin argumentos muestra de forma cronológica todos los registros disponibles 
desde el arranque del sistema. Esto puede incluir desde mensajes del kernel hasta eventos de servicios, 
pasando por errores de aplicaciones. Para facilitar la navegación por esta salida, el comando presenta el 
resultado en modo paginado, permitiendo desplazarse cómodamente por los eventos registrados. 
Uno de los usos más comunes es consultar únicamente los eventos generados desde el último arranque. 
Esto se consigue con la opción "-b", muy útil cuando se quiere revisar lo que ha ocurrido en el sistema 
desde que fue encendido. Si se desea obtener únicamente los mensajes de error recientes, la combinación 
"-xe" proporciona una salida extendida centrada en los eventos con niveles de severidad elevados, \nespecialmente útil cuando un servicio falla y se quiere obtener información precisa del motivo. 
Journalctl permite también filtrar por servicio, lo que facilita enormemente la supervisión de procesos 
concretos. Por ejemplo, si se quiere revisar únicamente los mensajes relacionados con el servidor SSH o 
con el demonio de red, basta con especificar el nombre de la unidad correspondiente con el parámetro 
"-u", seguido del nombre del servicio. Esto evita tener que recorrer manualmente todo el log general del 
sistema. 
Otra característica avanzada de journalctl es la posibilidad de filtrar por fecha y hora. Utilizando 
opciones como "--since" y "--until", se pueden obtener únicamente los registros comprendidos entre 
dos momentos concretos. Esta funcionalidad es especialmente útil cuando se quiere investigar un \nevento que se sabe que ocurrió en una franja horaria determinada, como un reinicio inesperado o un 
fallo durante una actualización. 
A diferencia de los logs tradicionales basados en texto plano, el journal permite organizar, clasificar y 
filtrar la información con mayor precisión, lo que convierte a journalctl en una herramienta de primer 
orden para el análisis de problemas, la supervisión en tiempo real y la recopilación de información 
detallada sobre el estado del sistema. 
7.4. Rotación y mantenimiento de logs 
A medida que el sistema opera y sus servicios generan eventos, los archivos de log van creciendo 
progresivamente. En sistemas que están en funcionamiento de forma continua, especialmente aquellos 
que actúan como servidores, este crecimiento puede llegar a ocupar una cantidad considerable de \nespacio en disco. Para evitar que los logs antiguos saturen el sistema, Linux cuenta con un mecanismo 
automático de gestión llamado logrotate. 
El propósito principal de logrotate es controlar el tamaño de los archivos de log mediante un proceso de 
rotación. Esta rotación consiste en renombrar el archivo actual, comprimirlo o archivarlo, y crear uno 
nuevo en su lugar. De este modo, se conserva un historial limitado de registros, pero se impide que un 
solo archivo crezca indefinidamente. Este mecanismo puede aplicarse de forma diaria, semanal o 
mensual, según la configuración establecida para cada servicio.

---

Administración del Sistema Operativo y software de Base 
102 
La configuración global de logrotate se encuentra en el archivo "/etc/logrotate.conf", aunque es más 
habitual que los servicios individuales tengan configuraciones específicas en el directorio 
"/etc/logrotate.d/". Estas configuraciones determinan cuándo se debe rotar un archivo, cuántas 
copias antiguas se deben conservar, si deben comprimirse y si es necesario reiniciar el servicio 
correspondiente tras la rotación para que comience a escribir en el nuevo archivo. 
Durante su ejecución, logrotate puede operar de forma completamente automática, generalmente a 
través de una tarea programada mediante "cron". Sin embargo, también puede forzarse manualmente 
para aplicar las reglas de rotación en un momento concreto, lo que resulta útil al depurar servicios o tras 
aplicar cambios en la configuración. 
La rotación de logs es esencial no solo por razones de espacio, sino también desde el punto de vista del 
rendimiento y la organización. Un archivo de log demasiado grande puede dificultar su análisis, 
ralentizar comandos como "less" o "grep", y complicar la búsqueda de eventos recientes. Además, 
mantener archivos antiguos comprimidos y con nombres estructurados por fecha facilita las tareas de 
auditoría o revisión de incidencias pasadas. 
El correcto mantenimiento de los logs pasa por encontrar un equilibrio entre la conservación de la 
información histórica y el uso eficiente de los recursos del sistema. Configurar adecuadamente la 
rotación, adaptándola al tipo de servicio y a la criticidad del entorno, es una de las responsabilidades 
habituales del administrador de sistemas. 
7.5. Buenas prácticas de supervisión 
El simple hecho de contar con archivos de log y herramientas de consulta no garantiza una buena 
administración del sistema. Para que la supervisión sea realmente eficaz, es necesario aplicar una serie 
de prácticas que permitan aprovechar al máximo la información registrada y responder de forma ágil 
ante cualquier problema. 
Una de las costumbres más recomendables es revisar con frecuencia los logs más relevantes del 
sistema, como los relacionados con la autenticación, el núcleo o los eventos generales. Esta supervisión 
periódica ayuda a detectar patrones anómalos, intentos de acceso indebido o errores que podrían pasar 
desapercibidos si no se realiza una observación continuada. 
En entornos más exigentes, esta tarea puede automatizarse mediante herramientas específicas como 
Logwatch, que genera resúmenes diarios con lo más destacado de los registros del sistema, o Fail2ban, 
que analiza intentos fallidos de inicio de sesión y aplica medidas automáticas como el bloqueo de 
direcciones IP sospechosas. Para contextos más complejos o distribuidos, soluciones como Rsyslog, 
Graylog o pilas completas como ELK (Elasticsearch, Logstash y Kibana) permiten centralizar, indexar y 
visualizar los registros de múltiples sistemas de forma unificada y eficiente. 
La capacidad para filtrar adecuadamente la información es otro aspecto clave. Los logs suelen contener 
miles de líneas de texto, muchas de ellas poco significativas. Saber utilizar comandos como "grep", o \nexplotar las funciones avanzadas de herramientas como journalctl, permite centrarse únicamente en los 
mensajes relevantes y ahorrar tiempo de análisis. La personalización de filtros según el servicio o el tipo 
de error permite construir una supervisión mucho más precisa y útil.

---

Administración del Sistema Operativo y software de Base 
103 
Es igualmente importante aplicar una política de conservación de logs que se adapte a las necesidades 
del entorno. En algunos casos, basta con conservar los registros de las últimas semanas. En otros, \nespecialmente cuando se trata de sistemas críticos o sujetos a requisitos legales, es necesario mantener 
un historial más extenso y asegurarse de que los archivos no se eliminan prematuramente. El uso 
correcto de herramientas como logrotate permite cumplir estos objetivos sin comprometer el espacio 
de almacenamiento ni el rendimiento del sistema. 
Otro aspecto a considerar es la seguridad de los propios archivos de log. Almacenar información 
sensible o indicios de un incidente en archivos fácilmente manipulables puede suponer un riesgo. Por \neso, es aconsejable establecer permisos restrictivos sobre los logs, protegerlos frente a modificaciones 
y, en entornos distribuidos, centralizar su almacenamiento en servidores remotos para evitar 
manipulaciones locales. Esta centralización también facilita su análisis conjunto, especialmente cuando 
se administran múltiples máquinas. 
Finalmente, conviene tener presente que los logs no deben verse únicamente como una herramienta de 
diagnóstico ante fallos. También son una fuente valiosa de información para evaluar el rendimiento del 
sistema, verificar el cumplimiento de políticas internas o anticipar posibles problemas antes de que se 
manifiesten de forma visible. En este sentido, supervisar los logs es una tarea preventiva que 
complementa otras labores del administrador y contribuye a mantener un sistema más robusto, seguro 
y eficiente. 
8. Tendencias: Bring Your Own Device 
BYOD, siglas de Bring Your Own Device (traducido al castellano: "trae tu propio dispositivo", es una 
política empresarial consistente en que los empleados lleven sus propios dispositivos personales 
(portátiles, tabletas, móviles…) a su lugar de trabajo y utilizarlos para realizar sus tareas y tener acceso 
a los recursos de la empresa (aplicaciones, bases de datos y archivos en servidores, email…). 
También se le llama BYOT, siglas de "bring your own technology" (traducido al castellano: "trae tu 
propia tecnología"), incluyendo así al equipo (hardware) y también al software, convirtiéndolo en una 
forma de expresar un fenómeno más amplio. 
 
 
 
 
+ Info 
BYOD también ha llegado al ámbito educativo con la incorporación 
de las tecnologías. 
Alberta Education (Ministerio de Albertan, provincia en el oeste de 
Canadá, responsable de la educación de la primera infancia, la \neducación primaria y la educación secundaria en Alberta), lo define 
así: "BYOD es un modelo tecnológico en el cual los estudiantes 
llevan su dispositivo personal a la escuela con objeto de aprender".

---

Administración del Sistema Operativo y software de Base 
104 
9. Gestión de dispositivos móviles 
Normalmente denominado MDM, siglas de Mobile Device Management, es el software de gestión de 
dispositivos móviles o de administración de dispositivos móviles. 
MDM, es un tipo de software que permite asegurar, monitorizar y administrar dispositivos móviles 
sin importar el operador de telefonía o proveedor de servicios. 
La mayoría de las MDM permiten instalar aplicaciones, localizar y rastrear equipos, sincronizar archivos, 
reportar datos y acceder a dispositivos, todo esto de manera remota. 
Este tipo de aplicaciones ha tenido una gran aceptación por parte de las empresas y su crecimiento ha 
sido realmente vertiginoso, debido en gran medida a la popularidad que han tenido los smartphones 
dentro de las corporaciones. 
La arquitectura básica de un MDM consiste en un agente, el cual es una aplicación que se instala en cada 
uno de los dispositivos que se desean administrar, un servidor de implementación desde donde corre el 
MDM y una base de datos donde se guardan todos los datos recabados. Los agentes mantienen una 
conexión con el servidor a través de USB, Wi-Fi, GPRS, 3G o cualquier otro medio de transmisión de 
datos, lo cual le permite al MDM tomar control del dispositivo. 
9.1. Actualización de terminales móviles 
Android 
 
Fuente: 
https://es.m.wikiped
ia.org/wiki/Archivo:
Android_robot.svg 
Por defecto, las actualizaciones automáticas del sistema operativo Android están activadas. Cuando 
aparezca una nueva versión, te preguntará si quieres instalarla. Puedes aplazarlo o instalarla. 
Se pueden eliminar las notificaciones eliminando la aplicación que se encarga de actualizar el software, 
pero no es aconsejable.

---

Administración del Sistema Operativo y software de Base 
105 
Los pasos para realizar una actualización manual son: 
• Primero: pulsa "Ajustes" (el círculo rojo indica que hay una actualización pendiente). 
 
• Segundo: pulsa "Actualizar software".

---

Administración del Sistema Operativo y software de Base 
106 
Aquí te mostrará la versión que tienes y si hay alguna actualización nueva. En este caso podemos ver 
que sí la hay. Para instalarla, haz clic sobre ella. 
 
Si pulsamos sobre "Versión nueva" nos llevará a la pantalla desde donde podremos instalarla. En esta 
pantalla nos mostrará información de todos los cambios que hay en la nueva versión.

---

Administración del Sistema Operativo y software de Base 
107 
 
 
 
+ Info 
Debes tener en cuenta que esto puede variar dependiendo del 
fabricante y de la versión de Android, pero básicamente suelen 
seguir un patrón similar. 
 
iOS 
 
Fuente: 
https://commons.wikimedia.
org/wiki/File:IOS_logo.svg 
Antes de la versión 12, la única manera de actualizar de forma automática era mediante el uso de App 
Store e ITunes Store. 
   
 
Iconos App Store e ITunes Store (fuentes: 
https://commons.wikimedia.org/wiki/File:Apple_App_Store_icon.jpg 
y https://commons.wikimedia.org/wiki/File:ITunes_Store_icon.svg) 
Para activarlas teníamos que seguir los siguientes pasos: 
1. Pulsa sobre el icono "Ajustes". 
2. Busca la opción "iTunes Store y App Store" y pulsa sobre ella. 
3. En el apartado "Descargas automáticas" activa el interruptor "Actualizaciones".

---

Administración del Sistema Operativo y software de Base 
108 
A partir de la versión 12 de iOS se ha añadido la opción para actualizar el sistema de forma automática. 
Para ello hay que seguir los siguientes pasos: 
1. Abre "Ajustes". 
2. Pulsa "General". 
3. Pulsa "Actualización de software". 
4. Activa "Actualizaciones automáticas". 
9.2. Enrolamiento de móviles 
El enrolamiento de móviles es el proceso mediante el cual un dispositivo móvil se registra y configura en 
un sistema de gestión centralizado, permitiendo su administración remota, aplicación de políticas de 
seguridad y control de acceso a los recursos de la organización. El enrolamiento de móviles es un 
componente esencial en la administración de dispositivos dentro de las organizaciones, permitiendo un 
control efectivo, seguridad de datos y gestión eficiente de los dispositivos en entornos empresariales y \neducativos. 
El enrolamiento de móviles reporta numerosos beneficios al funcionamiento de la empresa en 
seguridad, eficiencia operativa, gestión y cumplimiento normativo (asegura el cumplimiento de 
regulaciones como GDPR, ISO 27001, HIPAA). 
Objetivos del Enrolamiento de Móviles 
• Gestión Centralizada: Facilita la administración remota de los dispositivos. 
• Seguridad y Cumplimiento: Aplicación de políticas de seguridad corporativas. 
• Control de Aplicaciones: Instalación, actualización y restricción de aplicaciones. 
• Monitorización y Soporte: Supervisión del estado del dispositivo y soporte técnico. 
• Protección de Datos: Implementación de cifrado y prevención de pérdida de datos. 
Tipos de Enrolamiento 
Enrolamiento Manual: 
• El usuario registra manualmente el dispositivo en el sistema de gestión. 
• Requiere la instalación de una aplicación de administración. 
• Suele usarse en dispositivos personales o BYOD (Bring Your Own Device).

---

Administración del Sistema Operativo y software de Base 
109 
Enrolamiento Automático: 
• Utilizado en dispositivos corporativos adquiridos a través de proveedores aprobados. 
• Permite la configuración sin intervención del usuario final. 
• Se integra con programas como Apple Business Manager (ABM) o Android Enterprise. 
Enrolamiento por Código QR o NFC: 
• Escaneo de un código QR para descargar la configuración automáticamente. 
• Utilizado en escenarios de implementación masiva de dispositivos. 
Enrolamiento Basado en Cuenta: 
• El usuario inicia sesión con una cuenta corporativa y el dispositivo se configura 
automáticamente. 
• Común en entornos de Microsoft Intune y Google Workspace. 
Métodos de Implementación 
Uso de MDM (Mobile Device Management): 
• Herramientas como Microsoft Intune, VMware Workspace ONE, IBM MaaS360, MobileIron. 
• Aplicación de políticas de seguridad y gestión remota. 
Zero-Touch Enrollment: 
• Dispositivos Android registrados previamente para su configuración automática sin intervención 
manual. 
• Ideal para grandes organizaciones. 
Apple Device Enrollment Program (DEP): 
• Integración con Apple Business Manager para la configuración automática de dispositivos iOS y 
macOS. 
10. Bibliografía 
• GÓMEZ LÓPEZ, J. y GÓMEZ LÓPEZ, O. D. Administración de sistemas operativos. Editorial 
RA-MA. 
• http://www.adminso.es/index.php/Administraci%C3%B3n_de_Sistemas_Operativos. 
• https://www.digitallearning.es/blog/tareas-administrador-sistemas-linux/. 
• http://ing.unne.edu.ar/pub/informatica/U3.pdf.

---

Administración del Sistema Operativo y software de Base 
110 
• https://es.wikipedia.org/wiki/Gestión_de_dispositivos_móviles. 
• https://okhosting.com/blog/tipos-de-software-su-clasificacion/#Software_de_Sistema. 
• https://proyectoova.webcindario.com/software_de_sistema.html. 
• https://es.slideshare.net/anahir_segovia/tareas-y-responsabilidades-del-administrador-del-
sistema?next_slideshow=1. 
• https://computerhoy.com/noticias/hardware/cuales-son-funciones-administrador-sistemas-
34953. 
• https://www.howtoforge.com/tutorial/how-to-setup-automatic-security-updates-on-ubuntu-
1604/. 
• https://www.cambiatealinux.com/actualizar-el-sistema-en-linux-desde-la-linea-de-comandos. 
• https://answers.microsoft.com/es-es/windows/forum/windows_10-update/c%C3%B3mo-
impedir-las-actualizaciones/df023892-ac7b-4647-b49c-84d5cbd108d7?auth=1. 
• https://www.pcworld.es/tutoriales/software/configurar-actualizaciones-automticas-
windows-10-3675705/. 
• http://www.idownloadblog.com/2018/06/11/how-to-have-your-iphone-and-ipad-
automatically-download-new-ios-updates/. 
• https://www.applesfera.com/tutoriales/ios-desde-cero-actualizaciones-automaticas. 
• https://es.wikihow.com/realizar-el-mantenimiento-de-una-computadora. 
• https://www.hirensbootcd.org/faq-items/is-windows-pe-legal-to-use/ 
• https://www.hirensbootcd.org/hbcd-v152/ 
• https://www.infospyware.com 
• http://respag.net/new-page-2.aspx 
• https://es.wikipedia.org/wiki/Puppet_(software) 
• https://es.wikipedia.org/wiki/Virtualización 
• https://es.wikipedia.org/wiki/Máquina_virtual 
• https://en.wikipedia.org/wiki/PowerVM 
• https://www.ibm.com/es-es/marketplace/ibm-powervm 
• https://puntinformatic.com/que-es-el-vdi/ 
• https://es.wikipedia.org/wiki/Virtualización_de_escritorio 
• https://www.muycomputerpro.com/2019/03/21/diez-comandos-imprescindibles-para-
iniciarse-en-microsoft-powershell 
• https://docs.microsoft.com/en-us/powershell/

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema01|Ficha Resumen del Tema 01]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque4-tema01|Nota Fuente Oficial del Tema 01]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema01-conceptos-so-virtualizacion|Test Tema 01]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Portada Bloque 4]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema02|Tema Completo 02 ➡️]]
