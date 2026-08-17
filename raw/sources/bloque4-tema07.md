---
title: "Bloque 4 - Tema 07: Modelo ISO-OSI, Modelo TCP-IP, Protocolo IP (IPv4 e IPv6)"
type: "source"
tags:
  - oposiciones
  - tai
  - bloque-4
  - tema-07
  - raw-source-extracted
sources:
  - "raw/bloque 4/bloque4,tema7.pdf"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Bloque 4 Tema 07"
  - "bloque4,tema7.pdf"
---

# Bloque 4 - Tema 07: Modelo ISO-OSI, Modelo TCP-IP, Protocolo IP (IPv4 e IPv6)

> **Fuente Original**: `raw/bloque 4/bloque4,tema7.pdf`  
> **Tipo**: Extracción completa de documento PDF  
> **Fecha de Ingesta**: 2026-08-17

---

## Contenido Extraído

### Página 1

Modelo ISO/OSI, TCP/IP. 
Protocolos 
DV.TextoHTML(01).Esp.dot     |     UD012123_V07_T01

---

### Página 2

ÍNDICE 
1. Modelo ISO/OSI 
4 
1.1. Niveles o capas 
5 
1.1.1. Funciones de los distintos niveles o capas 
6 
1.1.1.1. Capa Física (Nivel 1) 
7 
1.1.1.2. Capa de enlace de datos (Nivel 2) 
7 
1.1.1.2.1. Protocolo STP 
8 
1.1.1.2.2. Características avanzadas de Ethernet en la Capa de Enlace de Datos 
12 
1.1.1.3. Capa de red (Nivel 3) 
13 
1.1.1.4. Capa de transporte (Nivel 4) 
14 
1.1.1.5. Capa de sesión (Nivel 5) 
15 
1.1.1.6. Capa de presentación (Nivel 6) 
16 
1.1.1.7. Capa de aplicación (Nivel 7) 
17 
1.1.2. Primitivas de Comunicación en el Modelo OSI 
17 
2. Protocolo IP 
19 
2.1. Versión IPv4 
19 
2.1.1. Partes de una dirección IP 
19 
2.1.2. Direcciones especiales 
20 
2.1.3. Clases de redes en el IPv4 
21 
2.1.4. Direcciones IP reservadas en IPv4 
23 
2.1.5. Creación de subredes en IPv4 
24 
2.1.6. Cabecera IPv4 
30 
2.2. Versión IPv6 
36 
2.2.1. Ámbito de direcciones IPv6 
39 
2.2.2. Configuración automática sin estado 
45 
2.2.3. EUI-64 Modificado 
45 
2.2.4. Detección de direcciones duplicadas 
47 
2.2.5. Tiempo de vida de la dirección 
47 
2.2.6. Selección automática de dirección 
48 
2.2.7. Direcciones de enlace-local e índice de zonas 
49 
2.2.8. Direcciones IPv6 en el DNS 
50

---

### Página 3

2.2.9. Cabecera IPV6 
51 
2.3. Comparación de cabeceras IPv4 y IPv6 
52 
2.3.1. Las cabeceras de extensión (extension headers) 
52 
2.3.1.1. Tipos de cabecera 
54 
2.4. Asignaciones geográficas de direcciones IP (RIR) 
56 
3. Modelo TCP/IP 
57 
3.1. Funciones de las capas del modelo TCP/IP 
58 
3.1.1. Capa de interfaz de Red (Nivel 1) 
58 
3.1.2. Capa de Internet (Nivel 2) 
58 
3.1.3. Capa de Transporte (Nivel 3) 
59 
3.1.4. Capa de Aplicación (Nivel 4) 
60 
3.2. Protocolos TCP/IP 
60 
3.2.1. Capa de Interfaz de red 
61 
3.2.2. Capa de Internet 
61 
3.2.2.1. Protocolo ICMP 
62 
3.2.2.2. Protocolo IPSEC 
62 
3.2.2.2.1. Modos de IPsec 
63 
3.2.2.2.2. Los 3 Protocolos que forman IPsec 
63 
3.2.2.3. Protocolo IGMP 
67 
3.2.3. Capa de transporte 
67 
3.2.4. Capa de aplicación 
69 
3.3. Funcionamiento del modelo TCP/IP 
72 
3.3.1. Proceso de Comunicación en la Pila TCP/IP 
72 
4. Comparación de los modelos OSI y TCP/IP (ventajas y desventajas) 
75 
5. Correspondencia ISO/OSI con TCP/IP 
76 
6. Bibliografía 
77

---

### Página 4

Modelo ISO/OSI, TCP/IP. Protocolos 
4 
1. Modelo ISO/OSI 
En la década de 1970 dos proyectos iniciaron con la misma meta: "Definir un estándar unificado para 
la arquitectura de sistemas de redes". 
Uno estaba siendo desarrollado por ISO (International Organization for Standardization) y la otra por la 
CCITT (International Telegraph and Telephone Consultative Committee). 
Finalmente, ambos se fusionaron dando lugar al Modelo OSI (Open System Interconnection o 
interconexión de sistemas abiertos). 
El modelo OSI es el modelo de protocolos más citado en la industria actual. La norma ISO/IEC 7498-
1:1994 es la versión estándar más reciente y el Modelo OSI no ha experimentado cambios 
fundamentales a nivel de norma, pese a ello ha evolucionado de manera implícita a través de nuevas 
tecnologías, estándares y prácticas de la industria. 
Sin embargo, ninguno de los protocolos de redes más utilizados lo siguen, aunque pueden tener cierta 
correspondencia parcial. 
El modelo OSI es un conjunto de operaciones que una capa proporcionara a la capa que esta sobre ella. 
Describe las funciones y el comportamiento de cada uno de los niveles (o capas), pero no su 
implementación. 
Los niveles se crean donde se requiere un nivel de abstracción distinto. 
Por lo tanto, OSI es un modelo de referencia. 
Un modelo de referencia es una visión que define el alcance, estructura, y mecanismos de un sistema. 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional.  
ACCEDE DIRECTAMENTE DESDE AQUÍ

---

### Página 5

Modelo ISO/OSI, TCP/IP. Protocolos 
5 
1.1. Niveles o capas 
Hay 7 niveles en el modelo OSI. 
 
El comportamiento y utilidad de cada nivel se define mediante: 
• Los servicios que ofrece al nivel superior (comunicación vertical). 
• El protocolo utilizado para ofrecer servicios para la comunicación entre dos entidades que 
trabajan en un mismo nivel (ya sea hardware o software) sirve para permitir la comunicación 
horizontal. 
• Los servicios del protocolo se apoyan en los servicios que le ofrece el nivel inmediatamente 
inferior. 
• En la comunicación vertical se utiliza la encapsulación/desencapsulación. 
Esta es la comunicación horizontal a través de protocolos:

---

### Página 6

Modelo ISO/OSI, TCP/IP. Protocolos 
6 
 
Comunicación horizontal a través de protocolos 
Las comunicaciones horizontales son lógicas excepto en la capa física. 
1.1.1. Funciones de los distintos niveles o capas 
A modo de resumen, presentaremos la siguiente tabla. 
Capa 
Funciones 
Aplicación 
Funciones de usuario final como navegación web, correo electrónico, transferencia de 
archivos, etc. 
Presentación 
Representación de los datos (formato, codificación, comprensión y cifrado). 
Sesión 
Comunicación entre dispositivos de la red. Permite establecer, mantener y finalizar una 
sesión. 
Transporte 
Conexión extremo a extremo y fiabilidad de los datos (detección y corrección de errores). 
Red 
Direccionamiento y enrutamiento de los paquetes en la red. Direccionamiento lógico. 
Enlace de 
datos 
Método de acceso o estrategia para compartir el medio físico de transmisión. 
Direccionamiento físico en tu red (MAC y LLC). 
Física 
Características eléctricas y mecánicas de la red (cables, conectores, señales eléctricas, etc.) y 
transmisión binaria. 
** En la capa Transporte, es fiable dependiendo del protocolo usado (UDP no es fiable) **

---

### Página 7

Modelo ISO/OSI, TCP/IP. Protocolos 
7 
1.1.1.1. Capa Física (Nivel 1) 
Se encarga de la interfaz física entre los dispositivos. 
Define las reglas que rigen la transmisión de bits. 
Tiene 4 características importantes: 
• Mecánicas: 
Relacionadas con las propiedades físicas de la interfaz con el medio de transmisión. 
Incluye la especificación del conector que transmite las señales a través de conductores o 
medios físicos. 
• Eléctricas: 
Especifican cómo se representan los bits (Por ejemplo, en términos de niveles de tensión). 
Especifican la velocidad de transmisión. 
• Funcionales: 
Especifican las funciones que realiza cada uno de los circuitos de la interfaz física entre el 
sistema y el medio de transmisión. 
• De procedimiento: 
Especifican la secuencia de eventos que se llevan a cabo en el intercambio del flujo de bits a 
través del medio físico. 
La unidad de información que transmiten son los bits. 
1.1.1.2. Capa de enlace de datos (Nivel 2) 
Ensambla los bits de la capa física en grupos de tramas (protocolos de red) y asegura su correcto envío. 
Proporciona un tráfico de datos libre de errores a través de un enlace físico. 
Utiliza: 
• Direccionamiento físico. 
• Topologías lógicas de red. 
• Métodos de acceso al medio. 
• Detección y notificación de errores. 
• Etc.

---

### Página 8

Modelo ISO/OSI, TCP/IP. Protocolos 
8 
El transmisor numera las tramas y les añade los bits necesarios para la detección de errores a nivel de enlace. 
Asimismo, puede intercambiar tramas de reconocimiento entre los extremos de la comunicación. 
La capa de enlace de datos también incluye protocolos destinados a la gestión de la topología lógica de 
la red, como el protocolo Spanning Tree Protocol (STP), cuyo objetivo es evitar bucles en redes 
conmutadas mediante la activación o bloqueo lógico de enlaces redundantes. 
1.1.1.2.1. Protocolo STP 
STP es un protocolo de red de capa 2 del modelo OSI (capa de enlace de datos). 
Su función es la de gestionar la presencia de bucles en topologías de red debido a la existencia de 
enlaces redundantes (necesarios en muchos casos para garantizar la disponibilidad de las conexiones). 
El protocolo permite a los dispositivos de interconexión activar o desactivar automáticamente los 
enlaces de conexión, de forma que se garantice la eliminación de bucles. 
STP es transparente a las estaciones de usuario. 
Está basado en un algoritmo diseñado por Radia Perlman, creadora de software e ingeniera de redes, 
experta en seguridad, más conocida como la Madre de Internet. (Trabajo para Intel, para la cual 
consiguió más de 47 patentes, y después paso a trabajar para Dell EMC en Seattle). 
El algoritmo de Spanning Tree fue desarrollado originalmente por Radia Perlman en Digital Equipment 
Corporation (DEC) y posteriormente estandarizado por el IEEE como IEEE 802.1D. 
Se recomienda utilizar la versión estandarizada por el IEEE 802.1D. 
El algoritmo transforma una red física con forma de malla, en la que existen bucles, por una red lógica 
en forma de árbol (libre de bucles). 
Los puentes se comunican mediante mensajes de configuración llamados Bridge Protocol Data Units 
(BPDU). 
El protocolo establece identificadores por puente y elige el que tiene la prioridad más alta (el número 
más bajo de prioridad numérica), como el puente raíz (Root Bridge). 
Este puente raíz establecerá el camino de menor coste para todas las redes: 
• Cada puerto tiene un parámetro configurable denominado coste del camino (Path Cost o Root 
Path Cost). 
• Después, entre todos los puentes que conectan un segmento de red, se elige un puente 
designado, el de menor coste (en el caso que haya el mismo coste en dos puentes, se elige el 
que tenga el menor identificador "dirección MAC"), para transmitir las tramas hacia la raíz. 
» En cada segmento de red se elige un puerto designado, que será el puerto del switch 
que ofrezca el menor coste hacia el puente raíz. Por otro lado, en cada switch que no 
es raíz se selecciona un único puerto raíz, que es el puerto que proporciona el camino 
de menor coste hacia el puente raíz. 
Todos los demás puertos y caminos son bloqueados, esto es en un estado ya estacionario de 
funcionamiento.

---

### Página 9

Modelo ISO/OSI, TCP/IP. Protocolos 
9 
La primera decisión que toman todos los switches de la red es identificar el puente raíz ya que esto 
afectará al flujo de tráfico: 
• Cuando un switch se enciende, supone que es el switch raíz y envía las BPDUs que contienen la 
dirección MAC de sí mismo tanto en el BID raíz como emisor. 
• El BID es el Bridge IDentifier: Bridge Priority + Bridge Mac Address. 
• El Bridge Priority es un valor configurable que por defecto está asignado en 32768. 
• El Bridge Mac Address es la dirección MAC (única) del Puente. 
Cada switch actualiza la información del puente raíz cuando recibe BPDUs con un identificador de raíz 
menor y propaga dicha información en las BPDUs que envía. 
Todos los switches reciben las BPDU y determinan que el switch que cuyo valor de BID raíz es el más 
bajo será el puente raíz. En caso de empate, el switch root sería el que menor MAC tuviera. El 
administrador de red puede establecer la prioridad de switch en un valor más pequeño que el del valor 
por defecto (32768), el nuevo valor debe ser múltiplo de 4096, lo que hace que el BID sea más 
pequeño. Esto sólo se debe implementar cuando se tiene un conocimiento profundo del flujo de tráfico 
en la red. 
Una vez elegido el puente raíz hay que calcular el puerto raíz para los otros puentes que no son raíz. El 
procedimiento a seguir para cada puente es el mismo: 
• Entre todos los puertos del puente, se escoge como puerto raíz el puerto que tenga el menor 
costo hasta el puente raíz. 
En el caso de que haya dos o más puertos con el mismo coste hacia el puente raíz, se utilizan 
criterios de desempate adicionales, como el Bridge ID y el identificador del puerto, para 
establecer el puerto raíz. 
Cuando se ha elegido el puente raíz y los puertos raíz de los otros puentes pasamos a calcular los 
puertos designados de cada segmento de red. 
• En cada enlace que exista entre dos switches habrá un puerto designado, el cual será el puerto 
del switch que tenga un menor coste para llegar al puente raíz, este coste administrativo será un 
valor que estará relacionado al tipo de enlace que exista en el puerto (Ethernet, FastEthernet, 
GigabitEthernet). 
Cada tipo de enlace tendrá un coste administrativo distinto, siendo de un coste menor el puerto 
con una mayor velocidad. Si hubiese empate entre los costes administrativos que tienen los dos 
switches para llegar al root bridge, entonces se elegirá como Designated Port, el puerto del 
switch que tenga un menor Bridge ID (BID). 
Aquellos puertos que no sean elegidos como raíz ni como designados deben bloquearse. Estos puertos 
evitan los lazos.

---

### Página 10

Modelo ISO/OSI, TCP/IP. Protocolos 
10 
En el mantenimiento del Spanning Tree, El cambio en la topología puede ocurrir de dos formas: 
• El puerto se desactiva o se bloquea. 
• El puerto pasa de estar bloqueado o desactivado a activado. 
Cuando se detecta un cambio el switch notifica al puente raíz dicho cambio y entonces el puente raíz 
envía por broadcast dicho cambio. Para ello, se introduce una BPDU especial denominada notificación 
de cambio en la topología (TCN). Cuando un switch necesita avisar acerca de un cambio en la 
topología, comienza a enviar TCN en su puerto raíz. 
La TCN es una BPDU muy simple que no contiene información y se envía durante el intervalo de tiempo 
de saludo. 
El switch que recibe la TCN se denomina puente designado y realiza el acuse de recibo mediante el 
envío inmediato de una BPDU normal con el bit de acuse de recibo de cambio en la topología (TCA). 
Este intercambio continúa hasta que el puente raíz responde. 
La unidad de información que transmite es la trama. 
Ejemplo del STP:

---

### Página 11

Modelo ISO/OSI, TCP/IP. Protocolos 
11 
 
 
 
Imprescindible 
IEEE 802.1D es el estándar del IEEE para bridges MAC (puentes 
MAC) e incluye el funcionamiento del bridging y del protocolo 
Spanning Tree. 
También impide que los bucles se forman cuando los puentes o los 
interruptores están interconectados a través de varias rutas. 
El algoritmo BPDU logra mediante el intercambio de mensajes con 
otros switches para detectar bucles y, a continuación, elimina el 
bucle por el cierre de puente seleccionado interfaces. Este 
algoritmo garantiza que hay una y sólo una ruta activa entre dos 
dispositivos de red. 
Las VLANs (redes virtuales) no son parte de 802.1D, sino de IEEE 
802.1Q. 
 
 
El estándar de IEEE 802.1Q se encarga de marcar las directrices para implementar las VLANS en una red 
Ethernet. Es un estándar que agrega una etiqueta identificativa que incluye un identificador VLAN 
(VLAN ID) de 12 bits al principio de las tramas Ethernet. Las tramas etiquetadas se denominan 
"tagged", las que no lo son no portarán ninguna etiqueta y no existe la etiqueta "untagged". 
Rapid Spanning Tree Protocol 
El Rapid Spanning Tree Protocol (RSTP), definido en el estándar IEEE 802.1w, es una evolución del 
Spanning Tree Protocol (STP) tradicional (IEEE 802.1D). Su principal mejora radica en la reducción 
drástica de los tiempos de convergencia de la red, permitiendo una adaptación más rápida ante fallos en 
enlaces o incorporación de nuevos dispositivos. 
Multiple Spanning Tree Protocol 
Es definido por la norma 802.1s. Es un protocolo que extiende las capacidades de su predecesor, el 
RSTP, soportando múltiples instancias de spanning tree en la misma red. Es una solución robusta y 
eficiente para redes con VLANs múltiples ya que proporciona una redundancia optimizada para 
gestionar más eficientemente el tráfico. Y pese a ser más compleja que los modelos anteriores, son las 
idóneas en términos de escalabilidad para las redes de alta disponibilidad.

---

### Página 12

Modelo ISO/OSI, TCP/IP. Protocolos 
12 
1.1.1.2.2. Características avanzadas de Ethernet en la Capa de Enlace 
de Datos 
La capa de Enlace de Datos en el modelo OSI permite diversas configuraciones avanzadas que 
optimizan el rendimiento, la seguridad y la eficiencia en redes Ethernet. Estos ajustes permiten adaptar 
la red a necesidades específicas, mejorando la fiabilidad en distintos entornos. La configuración 
adecuada depende de los requisitos de la red y del hardware disponible. 
A continuación, se describen algunos de los ajustes más relevantes en Ethernet: 
Jumbo Frames 
Permiten aumentar el tamaño máximo de las tramas Ethernet más allá del valor estándar de 1.500 
bytes, alcanzando hasta 9.000 bytes o más. Se trata de una extensión no estandarizada por IEEE, 
dependiente del fabricante y del hardware utilizado. Esto reduce la sobrecarga en la transmisión de 
datos y disminuye el número de paquetes transmitidos, reduciendo así la carga en la CPU. Es ideal para 
aplicaciones de alto rendimiento como almacenamiento en red (NAS/SAN) y Big Data. Es importante 
que todos los dispositivos de la red estén configurados para soportar el mismo tamaño de trama. 
Control de Flujo (Flow Control) 
Mecanismo que permite a los dispositivos Ethernet gestionar la congestión en la red regulando el tráfico 
entre ellos. Su implementación evita la pérdida de paquetes en situaciones de alta carga y mejora la 
estabilidad en redes con aplicaciones sensibles al tiempo. 
Protocolo relevante: LACP (Link Aggregation Control Protocol), estandarizado actualmente por IEEE 
802.1AX (anteriormente IEEE 802.3ad). 
EtherChannel (Agregación de enlaces) 
Permite combinar múltiples enlaces físicos Ethernet en un único enlace lógico, incrementando el ancho 
de banda disponible y proporcionando redundancia para mejorar la disponibilidad de la red. 
Protocolo relevante: LACP (Link Aggregation Control Protocol, IEEE 802.3ad). 
Calidad de Servicio (QoS) 
Prioriza ciertos tipos de tráfico, como voz o video, para garantizar un rendimiento óptimo en 
aplicaciones críticas. Su implementación ayuda a reducir la latencia para tráfico de alta prioridad y a 
gestionar eficientemente los recursos en redes congestionadas. 
Protocolo relevante: IEEE 802.1p.

---

### Página 13

Modelo ISO/OSI, TCP/IP. Protocolos 
13 
VLANs (Redes de Área Local Virtual) 
Permiten segmentar una red física en múltiples redes lógicas independientes, mejorando la seguridad al 
aislar segmentos de red. También facilitan la gestión de grandes infraestructuras y optimizan la 
eficiencia al reducir el tráfico de broadcast. 
Protocolo relevante: IEEE 802.1Q. 
Descubrimiento del Tamaño Máximo de Unidad (MTU Discovery) 
Aunque el tamaño máximo de trama afecta a la capa de enlace de datos, el descubrimiento automático 
del MTU es un mecanismo propio de la capa de red (IP), basado en mensajes ICMP. Su función es evitar 
la fragmentación de paquetes y optimizar el rendimiento en redes con configuraciones heterogéneas. 
Port Security 
Controla el acceso a los puertos del switch basándose en direcciones MAC específicas. Esta 
funcionalidad, implementada habitualmente por los fabricantes, evita conexiones no autorizadas y 
mejora la seguridad en entornos corporativos y redes sensibles. 
Rapid Spanning Tree Protocol (RSTP) 
Protocolo de capa de enlace de datos para la gestión de topologías Ethernet con enlaces 
redundantes. Para una descripción detallada de su funcionamiento, véase el epígrafe anterior 
dedicado al protocolo STP. 
Data Center Bridging (DCB) 
Conjunto de extensiones Ethernet diseñadas para mejorar el rendimiento en centros de datos. Su 
implementación optimiza la calidad de servicio en redes de almacenamiento y virtualización, además de 
prevenir la pérdida de paquetes en entornos de alto tráfico. Incluye estándares como IEEE 802.1Qbb 
(Priority Flow Control), IEEE 802.1Qaz (Enhanced Transmission Selection) y IEEE 802.1Qau 
(Congestion Notification). 
1.1.1.3. Capa de red (Nivel 3) 
Proporciona: 
• Conectividad. 
• Selección de caminos entre dos sistemas (enrutamiento) dependiente de criterios como el 
coste, la capacidad y la calidad del servicio.

---

### Página 14

Modelo ISO/OSI, TCP/IP. Protocolos 
14 
El direccionamiento físico de la capa de enlace de datos manipula el problema de las direcciones 
localmente. 
Sin embargo, si un paquete pasa de la frontera de la red, se necesita otro sistema de direccionamiento 
para ayudar a distinguir los sistemas fuente y destino (Direccionamiento lógico). 
Realiza el enrutamiento a través de tablas estáticas o dinámicas, gestión de prioridades, reenvío de 
paquetes, etc. 
También resuelve el problema de la interconexión entre redes heterogéneas. 
La unidad de información que transmite es el paquete. 
Libera a las capas superiores de la necesidad de conocer: 
• La transmisión de datos subyacente. 
• Las tecnologías de conmutación utilizadas. 
En enlaces punto a punto simples y directos entre dos estaciones, sin necesidad de encaminamiento, 
la capa de red no resulta estrictamente necesaria, ya que la capa de enlace de datos puede 
proporcionar las funciones básicas de gestión del enlace. 
1.1.1.4. Capa de transporte (Nivel 4) 
Es la responsable de la comunicación extremo a extremo (desde la fuente hasta el destino) entre 
sistemas finales. 
El servicio de transporte orientado a conexión (TCP) asegura que los datos se entregan: 
• Libres de errores. 
• En orden. 
• Sin pérdidas ni duplicaciones. 
Algunas funciones de la capa de transporte son: 
• La optimización del uso de los servicios de red. 
• Proporcionar servicios de comunicación confiable de extremo a extremo (TCP) o servicios de 
comunicación rápida sin garantía de orden ni entrega (UDP). 
• Proporcionar servicios orientados a la conexión y no orientados a la conexión. 
• Segmentar y ordenar datos.

---

### Página 15

Modelo ISO/OSI, TCP/IP. Protocolos 
15 
• Multiplexar conexiones simultáneas de transporte en una única de red. 
• Fragmentar datos de la capa superior en unidades menores cuando es necesario. 
• Proporcionar la calidad del servicio solicitada. 
• Tasa máxima de error y Retardo máximo. 
• Prioridades. 
• Nivel de seguridad. 
El tamaño y la complejidad de un protocolo de transporte dependen de cuán fiables sean los servicios 
de red y las redes subyacentes. 
La unidad de información que transmite es el segmento. 
1.1.1.5. Capa de sesión (Nivel 5) 
Para muchas aplicaciones, no es suficiente el servicio básico de intercambio de datos que proporcionan 
las 4 capas inferiores del modelo OSI. 
Algunas de sus funciones son: 
• Establece, administra y finaliza las sesiones entre dos extremos. 
• Control de diálogo. Puede ser: 
• Full Dúplex. Simultáneo en los 2 sentidos. 
• Half Dúplex. Alternado en ambos sentidos. 
• Sincronización. 
• Administra el control de diálogo en conexiones de tráfico alternante. 
• Suministra el diálogo entre dos computadores. 
• Actúa como interfaz entre procesos remotos, gestionando el establecimiento, mantenimiento y 
finalización de sesiones de comunicación. 
• Coordina el intercambio de datos dentro de una sesión establecida. 
• Recuperar datos: 
• Se pueden establecer puntos de comprobación. 
• En caso de fallo se puede retransmitir los datos desde el último punto de comprobación.

---

### Página 16

Modelo ISO/OSI, TCP/IP. Protocolos 
16 
En muchos casos, los servicios de la capa de sesión son parcialmente o totalmente prescindibles y 
podrían incorporarse directamente en la capa de aplicación. 
En otras ocasiones son imprescindibles. 
Vamos a ver los Protocolos de la capa de sesión (Nivel 5): 
• Protocolo RPC (llamada a procedimiento remoto): 
RPC (Remote Procedure Call) es un mecanismo de comunicación de alto nivel utilizado en 
arquitecturas cliente-servidor para invocar procedimientos remotos. Aunque conceptualmente 
utiliza servicios de sesión, se implementa en la práctica en la capa de aplicación. 
El protocolo es un gran avance sobre los sockets usados hasta el momento. 
Las RPC son muy utilizadas dentro del paradigma cliente-servidor. Siendo el cliente el que inicia 
el proceso solicitando al servidor que ejecute cierto procedimiento o función y enviando éste de 
vuelta el resultado de dicha operación al cliente. Hoy en día se está utilizando el XML como 
lenguaje para definir el IDL y el HTTP como protocolo de red, dando lugar a lo que se conoce 
como servicios web. 
• SCP (Secure Copy): 
SCP (Secure Copy) es un protocolo de transferencia de archivos que funciona sobre SSH y 
pertenece a la capa de aplicación. A diferencia de RCP los datos son cifrados durante su 
transferencia, para evitar que potenciales packet sniffers extraigan información útil de los 
paquetes de datos. 
Sin embargo, el protocolo mismo no provee autenticación y seguridad; sino que espera que el 
protocolo subyacente, SSH, lo asegure. 
• ASP (Protocolo de sesión APPLE TALK): 
Fue desarrollado por Apple Computers, ofrece establecimiento de la sesión, mantenimiento y 
desmontaje, así como la secuencia petición. 
ASP es un protocolo intermedio que se basa en la parte superior de AppleTalk Protocolo de 
transacciones (ATP), que es el original fiable de nivel de sesión protocolo de AppleTalk. 
Proporciona servicios básicos para solicitar respuestas a las arbitrarias órdenes y llevar a cabo 
fuera de la banda de consultas de estado. También permite al servidor enviar mensajes 
asíncronos de atención al cliente. 
1.1.1.6. Capa de presentación (Nivel 6) 
Asegura que la información enviada a la capa de presentación del sistema remoto pueda ser 
interpretada correctamente. 
Para ello, se encarga de verificar el formato de los datos que se van a intercambiar realizando una 
verificación de sintaxis y semántica de dichos datos.

---

### Página 17

Modelo ISO/OSI, TCP/IP. Protocolos 
17 
También puede realizar otras funciones como: 
• Define el formato de los datos que se van a intercambiar entre las aplicaciones. 
• Ofrece a los programas de aplicación un conjunto de servicios de transformación de datos: 
• Conversión de formatos. 
• Cifrado. 
• Compresión. 
• Etc. 
1.1.1.7. Capa de aplicación (Nivel 7) 
La capa de aplicación es usada por aplicaciones que utilizan los usuarios. 
Algunas de sus funciones son: 
• Define protocolos a nivel de aplicaciones. 
• Lleva los servicios de red al usuario final. 
• Proporcionar servicios como: 
• Comprobación de contraseñas. 
• Bases de datos distribuidas. 
• Transferencia de archivos. 
• Conexión remota. 
• Correo electrónico. 
1.1.2. Primitivas de Comunicación en el Modelo OSI 
Las capas OSI proveen de servicios a sus capas adyacentes superiores. La capa usuaria (adyacente 
superior) solicitará el servicio por medio de las primitivas de servicio, que son mecanismos u 
operaciones que comunicarán con la capa proveedora, a través de los SAP (Service Access Point o 
Puntos de Acceso al Servicio), que se encontrarán agrupados en la interfaz que separa ambas capas. 
Como decíamos, la interfaz se compone de un grupo de reglas de comunicación que engloban estos 
servicios y las operaciones primitivas que los permiten.

---

### Página 18

Modelo ISO/OSI, TCP/IP. Protocolos 
18 
La capa superior puede acceder a los servicios a través del SAP (service access point) que se identificará 
a través de una dirección única. 
Los servicios que cada capa brinda a su capa superior pueden ser de dos tipos: orientados o no a 
conexión -conectivos o no conectivos, confirmados y no confirmados. 
Un servicio orientado a conexión requiere del establecimiento, el mantenimiento y el final de la 
conexión, el ejemplo claro sería el de la telefonía. 
Por otro lado, el servicio no orientado a conexión no necesita de conexión explícita y puede enviar la 
información sin ese establecimiento explícito, en este caso el ejemplo perfecto sería el correo postal. 
Las postales llegarán a destino, pero el orden de llegada puede variar. 
 
 
 
 
Info 
Para entender las primitivas pasamos a definir algunos términos 
que se han de enmarcar en el modelo OSI. 
• SERVICIO: operación que una capa proveedora ofrece a su 
capa usuaria. 
• SAP: Service Access Point o Punto de Acceso al Servicio. 
Este punto se identifica con una dirección única y es el 
punto por el que accede la capa usuaria a un servicio 
determinado. 
• INTERFAZ: agrupación de SAPs que se encuentra entre 
capas. 
• PRIMITIVA: Mecanismo que invoca un determinado 
servicio. 
 
Operaciones primitivas 
Entre las operaciones primitivas básicas encontramos: 
• Request o solicitud: la entidad usuaria solicita un servicio a su capa adyacente. 
• Indication o indicación: la entidad par es informada de una solicitud. 
• Response o respuesta: la entidad usuaria par comunica su respuesta. 
• Confirmation o confirmación: la confirmación se enviará a la capa usuaria del modelo emisor y 
puede indicar si la operación se completó con éxito. 
En los servicio confirmados y orientados a conexión se usarán las cuatro primitivas, en un servicio NO 
orientado a conexión o no confirmado solo se requerirán las primitivas request e indication.

---

### Página 19

Modelo ISO/OSI, TCP/IP. Protocolos 
19 
2. Protocolo IP 
El Internet Protocol o IP (Protocolo de Internet) es un protocolo NO orientado a la conexión, para la 
comunicación de datos a través de una red de paquetes conmutados. 
El IP proporciona los medios necesarios para la transmisión de bloques de datos, llamados datagramas, 
desde el origen al destino, donde origen y destino son hosts identificados por direcciones de longitud fija. 
Sus principales versiones son: IPv4 y IPv6. 
2.1. Versión IPv4 
Los equipos se comunican a través de Internet mediante el protocolo IP (Internet Protocol). 
Este protocolo utiliza direcciones numéricas denominadas direcciones IP compuestas por cuatro 
números enteros de un byte cada uno, por lo que pueden tomar valores desde 0 a 255. 
Están escritos en el formato byte.byte.byte.byte (xxx.xxx.xxx.xxx) 
Este sistema de paquetes no es fiable, porque no garantiza la entrega de paquetes, ni la entrega en 
secuencia. 
Ejemplos de direcciones IP: 172.16.12.116, 192.168.15.23 
Los equipos de una red utilizan estas direcciones para comunicarse, de manera que cada equipo de la 
red tiene una dirección IP exclusiva. 
El organismo a cargo de asignar direcciones públicas IP, es decir, direcciones IP para los equipos conectados 
directamente a Internet, es el ICANN (Internet Corporation for Assigned Names and Numbers). 
2.1.1. Partes de una dirección IP 
Una dirección IP tiene dos partes diferenciadas: 
• Net ID o identificador de red: 
Son los números de la izquierda e indican la red. 
• Host-ID (identificador de host): 
Son los números de la derecha e indican los equipos dentro de esta red. 
Se pueden usar uno, dos o tres bytes para el identificador de red (igual que para el de host), teniendo 
en cuenta que siempre tienen que haber 4.

---

### Página 20

Modelo ISO/OSI, TCP/IP. Protocolos 
20 
 
 
 
Ejemplo 
Si utilizamos 1 byte para red, podríamos tener la red 
10.xxx.xxx.xxx. 
El rango de IPs para host será desde 10.0.0.1 hasta la 
10.255.255.254. 
Si utilizamos 3 bytes para la red, podríamos tener la red 
192.168.13.0. 
El rango de IPs para host será desde 192.168.13.1 hasta 
192.168.13.254. 
 
2.1.2. Direcciones especiales 
Algunas de las direcciones de red tienen significados especiales, ahora vamos a ver las más 
significativas. 
• Dirección de Red: 
La dirección de red es aquella en la que todos los bits correspondientes al identificador de host 
están a cero. Esta dirección identifica a la propia red y no puede asignarse a ningún equipo. 
Ejemplo con la dirección 10.0.0.0: 
Si se utiliza un byte para el identificador de red, una posible dirección de red sería 10.0.0.0, 
donde todos los bits del identificador de host están a cero. 
La dirección 0.0.0.0 se denomina dirección no especificada y es utilizada por un host cuando 
todavía no conoce su dirección IP, por ejemplo durante el proceso de arranque. No identifica a 
un host concreto ni a una red específica. 
• Dirección de Difusión (o Broadcast): 
Cuando todos los bits del identificador de host están en 1 (es decir, todos los bytes están a 
255), la dirección que se obtiene es la denominada dirección de difusión. 
Es una dirección específica que permite enviar un mensaje a todos los equipos de la red 
especificados por el netID. 
Ejemplo: 
Si utilizamos 2 bytes para red, la dirección de difusión o broadcast sería 172.16.255.255 (Si 
enviamos un mensaje a esta dirección, les llegará a todos los equipos de la red 172.16.0.0).

---

### Página 21

Modelo ISO/OSI, TCP/IP. Protocolos 
21 
• HOST LOCAL: 
La dirección de host local es 127.0.0.1, se conoce como loopback o localhost e identifica a la 
propia máquina. Es una IP reservada para que una máquina se comunique consigo misma a 
través de la red TCP/IP. 
Cuando un protocolo de nivel superior envía un datagrama dirigido a la dirección de loopback, se 
le devuelve al remitente sin que llegue a los niveles inferiores de la capa OSI, no llegará a la red. 
2.1.3. Clases de redes en el IPv4 
Las direcciones IP se clasifican en clases dependiendo del número de bytes que se utilicen para la red. 
Existen cinco tipos básicos: 
• Clase A: 
• Utiliza un byte para la red. 
• El primer bit es 0. 
• 128 redes. 
• En estas, el primer bit estará a cero, lo que permite un total de 27 redes posibles (o 128 
redes), de las cuales se utilizan 126 (se excluyen 0 y 127) 
• El rango de direcciones de clase A va desde 1.0.0.0 hasta 126.255.255.255. El bloque 
127.0.0.0/8 está reservado para loopback, siendo 127.0.0.1 la dirección más utilizada para 
este fin. 
• Utiliza 3 bytes para hosts, por lo que puede tener 2²⁴ &minus; 2 direcciones utilizables, es 
decir, 16.777.214 equipos por red. 
0 
XXXXXXX 
XXXXXXXX 
XXXXXXXX 
XXXXXXXX 
Red 
Equipos 
• Clase B: 
• Utiliza dos bytes para la red. 
• Los dos primeros bits son 10. 
• 214 redes (16.384). 
• El rango de redes de clase B va desde 128.0.0.0 hasta 191.255.255.255. 
• Utiliza 2 bytes para hosts, por lo que puede tener 216-2 reservadas = 65.534 equipos.

---

### Página 22

Modelo ISO/OSI, TCP/IP. Protocolos 
22 
10 
XXXXXX 
XXXXXXXX 
XXXXXXXX 
XXXXXXXX 
Red 
Equipos 
• Clase C: 
• Utiliza tres bytes para la red. 
• Los tres primeros bits son 110. 
• 221 redes (2.097.152). 
• El rango de redes de clase C va desde 192.0.0.0 hasta 223.255.255.255. 
• Utiliza 1 byte para hosts, por lo que puede tener 28-2 reservadas = 254 equipos. 
110 
XXXXXX 
XXXXXXXX 
XXXXXXXX 
XXXXXXXX 
Red 
Equipos 
• Clase D: 
• No utiliza identificador de red ni de host, ya que está reservada para direcciones de 
multidifusión (multicast). 
• Los cuatro primeros bits son 1110. 
• Red reservada para multidifusión. 
• El rango de redes de clase D va desde 224.0.0.0 hasta 239.255.255.255. 
• Toda la red está reservada. 
111 
XXXXX 
XXXXXXXX 
XXXXXXXX 
XXXXXXXX 
Red 
Equipos 
• Clase E: 
• No utiliza identificador de red ni de host, ya que está reservada para usos experimentales e 
investigación. 
• Los cuatro primeros bits son 1111.

---

### Página 23

Modelo ISO/OSI, TCP/IP. Protocolos 
23 
• Red reservada para investigación. 
• El rango de redes de clase E va desde 240.0.0.0 hasta 255.255.255.255. 
• La clase E está reservada para usos experimentales y no se utiliza en el direccionamiento 
convencional. La dirección 255.255.255.255 es una dirección de broadcast limitado y no 
forma parte funcional de la clase E. 
1111 
XXXX 
XXXXXXXX 
XXXXXXXX 
XXXXXXXX 
Red 
Equipos 
2.1.4. Direcciones IP reservadas en IPv4 
Es habitual que en una empresa u organización un solo equipo tenga conexión a Internet y los otros 
equipos de la red acceden a Internet a través de él (proxy o pasarela). 
Como veremos más adelante, la ICANN (Internet Corporation for Assigned Names and Numbers) como 
coordinadora de la asignación de identificadores únicos en Internet, gestiona las IPs a través de la IANA 
(Internet Assigned Numbers Authority) que a su vez asigna bloques de IPs a los RIR (Registros 
Regionales de Internet) quienes suministrarán en última instancia IPs públicas a los ISP para que estos 
las proporcionen a los usuarios finales. 
La organización u empresa solicitará a su ISP una conexión a Internet recibiendo una IP pública que le 
servirá de puerta de enlace y por la que compartirá acceso a Internet con el resto de dispositivos. 
Sin embargo, los otros equipos necesitarán también direcciones IP para comunicarse entre ellos. 
Estas direcciones IP privadas se reservan para uso en redes locales, no son accesibles desde Internet y 
por ello no entran en conflicto con las direcciones IP de Internet. Las direcciones IP privadas no son 
visibles fuera de la red local. 
Estas direcciones son las siguientes: 
• Direcciones IP privadas de clase A: de 10.0.0.0 a 10.255.255.255 permiten la creación de 
grandes redes privadas que incluyen miles de equipos. 
• Direcciones IP privadas de clase B: de 172.16.0.0 a 172.31.255.255 permiten la creación de 
redes privadas de tamaño medio. 
• Direcciones IP privadas de clase C: de 192.168.0.0 a 192.168.255.255 permiten la 
implementación de pequeñas redes privadas.

---

### Página 24

Modelo ISO/OSI, TCP/IP. Protocolos 
24 
Máscara de subred en IPv4 
La máscara de subred sirve para saber cuántos bits corresponden a la red y cuantos a los equipos. 
Por lo tanto, las máscaras de subred son: 
Tipo de red 
Bytes de red 
Bytes de hosts 
Máscara de subred 
A 
1 
3 
255.0.0.0 
B 
2 
2 
255.255.0.0 
C 
3 
1 
255.255.255.0 
Para que los equipos con direcciones IP privadas puedan acceder a Internet, es necesario un mecanismo 
de traducción de direcciones de red (NAT), que permita utilizar la dirección IP pública asignada por el 
proveedor. 
2.1.5. Creación de subredes en IPv4 
Una dirección de red, o net ID, tiene asociada por defecto una máscara de red que define la capacidad 
de hosts del sistema. Esta máscara de red puede ser modificada según los requisitos del diseño de la red. 
Si es necesario crear subredes, se puede aumentar el número de bits destinados a las direcciones de red 
o subred, sustrayéndolos de la parte de direccionamiento destinada a los hosts. 
 
 
 
 
Ejemplo 
Imaginemos que tenemos la red 12.0.0.0. 
Si nuestra máscara de red por defecto es 255.0.0.0 
(11111111.00000000.00000000.00000000) y añadimos dos bits 
sustraídos de la parte correspondiente al rango de los hosts (se 
usan siempre los bits más significativos), obtendremos la máscara 
de red 255.192.0.0 (11111111.11000000.00000000.00000000). 
Fijaos como los dos primeros bits del segundo octeto se han 
puesto a 1.

---

### Página 25

Modelo ISO/OSI, TCP/IP. Protocolos 
25 
La máscara de red original 255.0.0.0, pasará a ser 255.192.0.0. 
Con esta nueva configuración tendremos a disposición 4 subredes. 
• 12.0.0.0 - 12.63.255.255 
• 12.64.0.0 - 12.127.255.255 
• 12.128.0.0 - 12.191.255.255 
• 12.192.0.0 - 12.255.255.255 
Dependiendo del número de bits que utilicemos para la subred podemos tener: 
Número de bits 
Número de subredes 
1 
2 
2 
4 
3 
8 
4 
16 
5 
32 
6 
64 
7 
128 
8 (no se puede en clase C) 
256 
En la clase C no se pueden usar 8 bits para la subred, porque solo se tienen 8 bits para equipos, por lo 
que no quedaría ningún bit para equipos. 
La máscara de subred será quien indique qué rango de bits es asignado a la red y cuál a los hosts. 
La máscara de red se puede presentar en dos formatos distintos, en formato decimal punteado como el 
que hemos visto en nuestro ejemplo 255.192.0.0, o bien en formato CIDR (Classless Inter-Domain 
Routing), que indica el número de bits destinados a la parte de red en este caso "/10", pues hemos 
pasado de usar 8 bits para la máscara de red (11111111.00000000.00000000.00000000) a 10 
(11111111.11000000.00000000). 
Ejemplos de subredes: 
Caso 1: 
Imaginemos que tenemos una red de clase B 172.16.0.0 con máscara de red por defecto 255.255.0.0 o 
bien /16. Nos piden que tenemos que sacar 3 subredes para tres departamentos diferentes.

---

### Página 26

Modelo ISO/OSI, TCP/IP. Protocolos 
26 
• Necesitaríamos entonces "robar" 2 bits de la parte de los hosts: 
Si solo robáramos 1 bit 2^1 = 2 No nos vale (necesitamos 3 subredes). 
Robamos 2 bits 2^2 = 4 Ya nos vale, pues solo necesitamos tres subredes. 
Con lo que la máscara de red se quedaría como 255.255.192.0 o bien /18. 
• Procedemos, por lo tanto, hacer la división de las 4 subredes que nos han salido: 
1ºSubred: 172.16.0.0 – 172.16.63.255 /18 
2ºSubred: 172.16.64.0 – 172.16.127.255 /18 
3ºSubred: 172.16.128.0 – 172.16.191.255 /18 
4ºSubred: 172.16.192.0 – 172.16.255.255 /18 
Caso 2: 
Partimos como antes de una red de clase B con máscara de red por defecto, 172.16.0.0/16 o bien 
172.16.0.0 255.255.0.0. 
En este supuesto se trata de hallar el número máximo de subredes posibles, siempre y cuando tengamos 
en cada una de ellas un MÍNIMO de 10 equipos. 
Conociendo nuestra configuración inicial, 2 octetos para la identificación de red y los dos restantes para 
el direccionamiento de hosts, buscaremos cuantos bits mínimos necesitamos para tener el mínimo de 
hosts exigido. Sabiendo que cada subred necesita de una dirección para la red y otra dirección para el 
broadcast, tendremos que tener presente que hay que restar esas 2 direcciones. 
En esta ocasión la restricción de bits para asignar a la red depende del número de hosts requerido, 
hallaremos pues cuantos bits necesitamos para poder direccionar 10 equipos. En este caso y al tratarse 
del rango de hosts comenzaremos a buscar cuantos bits de entre los de menor peso (los del último 
octeto), nos hacen falta. 
• 2^1 - 2 = 0  
No nos sirve 
• 2^2 - 2 = 2  
No nos sirve 
• 2^3 – 2 = 6  
No nos sirve 
• 2^4 – 2 = 14  
Con 4 bits se obtienen 16 direcciones totales, de las cuales 14 son utilizables para hosts, una vez 
descontadas las direcciones de red y de broadcast, cumpliéndose así el mínimo de 10 equipos 
exigido.

---

### Página 27

Modelo ISO/OSI, TCP/IP. Protocolos 
27 
Sabiendo que nuestra configuración inicial reserva 2 octetos a los hosts, esto es, 16 bits, y que 
finalmente solo necesitaremos 4 de ellos para contar con un mínimo de 10 equipos, se reasignan los 12 
(16 - 4) bits restantes a la creación de subredes, incorporándolos a la identificación de red que pasaría a 
contar con 28 bits, esto es una máscara 255.255.255.240 o bien /28. 
Los 12 bits robados a los hosts en favor de la Red permiten obtener un total de 212 = 4096 subredes. 
• 1º Subred = 172.16.0.0 – 172.16.15.255 /20 
• 2º Subred = 172.16.16.0 – 172.16.31.255 /20 
• 3º Subred = 172.16.32.0 – 172.16.47.255 /20 
• 4º Subred = 172.16.48.0 – 172.16.63.255 /20 
• Etc. 
Conclusiones: A mayores subredes menos host por subred, a menores subredes más hosts por subred 
 
 
 
Imprescindible 
Cómo saber cuántos ordenadores puedes conectar a una red tipo C. 
Si recordamos que la última dirección 255 es para broadcast, 
cuando la submáscara afecta únicamente al último octeto, basta 
con restar a 254 el valor del último octeto de la máscara de subred. 
Para 255.255.255.128 254-128=126 ordenadores. 
Para 255.255.255.240 254-240=14 ordenadores. 
("Este truco solo sirve para más de 2 ordenadores"). 
 
Máscara WildCard 
Hay que destacar wildcard, que es una máscara de bits que indica qué partes de una dirección de IP son 
relevantes para la ejecución de una determinada acción. 
En Cisco IOS, tiene varios usos, por ejemplo: 
• Indicar el tamaño de una red o subred para algunos protocolos de encaminamiento, como OSPF. 
• Indicar qué direcciones IP tendrían que ser permitidas o denegadas en las listas de control del 
acceso (ACLs).

---

### Página 28

Modelo ISO/OSI, TCP/IP. Protocolos 
28 
 
 
 
+ Info 
Cisco IOS es el software utilizado en la gran mayoría de routers y 
switches de Cisco Systems. 
IOS es un paquete de funciones de enrutamiento, conmutamiento, 
trabajo de internet y telecomunicaciones que se integra 
estrechamente con un sistema operativo multitarea. 
 
 
En un nivel simple, una máscara wildcard puede ser pensada como una máscara de subred. 
 
 
 
 
Ejemplo 
La máscara de subred 255.255.255.0. 
(Equivalente en binario a = 
11111111.11111111.11111111.00000000). 
Se invierte a una máscara wildcard de 0.0.0.255. 
 
 
Una máscara wildcard es una regla de correspondencia. La regla para la máscara es: 
• El 0 significa que se debe comprobar el bit equivalente. 
• El 1 significa que el bit equivalente no importa. 
Cualquier wildcard puede ser enmascarada para su examen.

---

### Página 29

Modelo ISO/OSI, TCP/IP. Protocolos 
29 
 
 
 
Ejemplo 
Una máscara wildcard de 0.0.0.254. 
(Equivalente binario = 
00000000.00000000.00000000.11111110). 
Aplica a la IP 10.10.10.2 
(00001010.00001010.00001010.00000010). 
Que emparejará con las direcciones IP pares. 
10.10.10.0, 10.10.10.2, 10.10.10.4, 10.10.10.6 etc. 
 
 
 
 
 
Ejemplo 
La misma máscara de 0.0.0.254 
Aplica a la IP 10.10.10.1 
(00001010.00001010.00001010.00000001). 
Que emparejará con las direcciones IP impares. 
10.10.10.1, 10.10.10.3, 10.10.10.5 etc. 
 
 
Una combinación de la red y la máscara wildcard 1.1.1.1 0.0.0.0 emparejaría con la interfaz configurada 
exactamente con 1.1.1.1, y ninguna otra. 
Esto es realmente útil si se quiere activar OSPF en una interfaz concreta en una manera muy clara y 
sencilla. 
Si se trata de emparejar un rango de redes, la combinación la red y de la máscara wildcard 1.1.0.0 
0.0.255.255 emparejaría con cualquier interfaz en la gama de 1.1.0.0 a 1.1.255.255. 
Debido a esto, es más sencillo y más seguro utilizar la máscara wildcard 0.0.0.0 e identificar cada 
interfaz OSPF individualmente, pero una vez configurado, funcionan exactamente igual (una manera no 
es mejor que la otra).

---

### Página 30

Modelo ISO/OSI, TCP/IP. Protocolos 
30 
Las máscaras wildcard se utilizan en situaciones donde es necesario realizar coincidencias flexibles de 
direcciones IP, y no para definir límites de red como hacen las máscaras de subred. 
Por ejemplo, cuándo dos hosts están en diferentes subredes, el uso de la máscara wildcard los agruparía. 
Lista de Máscaras Wildcard: 
CIDR 
Netmask 
Máscara wildcard 
/16 
255.255.0.0 
0.0.255.255 
/15 
255.254.0.0 
0.1.255.255 
/14 
255.252.0.0 
0.3.255.255 
/13 
255.248.0.0 
0.7.255.255 
/12 
255.240.0.0 
0.15.255.255 
/11 
255.224.0.0 
0.31.255.255 
/10 
255.192.0.0 
0.63.255.255 
/9 
255.128.0.0 
0.127.255.255 
/8 
255.0.0.0 
0.255.255.255 
/7 
254.0.0.0 
1.255.255.255 
/6 
252.0.0.0 
3.255.255.255 
/5 
248.0.0.0 
7.255.255.255 
/4 
240.0.0.0 
15.255.255.255 
/3 
224.0.0.0 
31.255.255.255 
/2 
192.0.0.0 
63.255.255.255 
/1 
128.0.0.0 
127.255.255.255 
2.1.6. Cabecera IPv4 
Vamos a ver en una tabla, cómo es una cabecera IPv4. 
A continuación, describiremos cada uno de sus campos.

---

### Página 31

Modelo ISO/OSI, TCP/IP. Protocolos 
31 
 
El tamaño mínimo de la cabecera (IP_PCI) es de 20 Bytes mientras que el máximo es 60 bytes. 
Descripción de cada uno de los campos: 
• Versión: 4 bits. 
El campo versión indica el formato de la cabecera IP utilizada. Para IPv4 su valor es siempre 
0100 (4 en decimal). El valor 0110 corresponde a IPv6 y no aparece en cabeceras IPv4. Este 
campo describe el formato de la cabecera utilizada. En la tabla se describe la versión 4. 
• Tamaño Cabecera (IHL): 4 bits. 
Longitud de la cabecera, en palabras de 32 bits. Su valor mínimo es de 5 palabras (5x32 = 160 
bits, 20 bytes) para una cabecera correcta, y el máximo de 15 palabras (15x32 = 480 bits, 60 
bytes). 
• Tipo de Servicio (ToS): 8 bits. 
Antes de 2001, el campo ToS, de 8 bits, estaba destinado a definir cómo los enrutadores debían 
manejar los paquetes según características como retraso, rendimiento o fiabilidad, a partir de 
esta fecha el campo se dividió en dos: 
• DSCP (Differentiated Services Code Point) de 6 bits para para clasificar el tráfico y QoS. 
• ECN (Explicit Congestion Notification) de 2 bits, para notificación si el paquete había 
atravesado una sección congestionada de la red.

---

### Página 32

Modelo ISO/OSI, TCP/IP. Protocolos 
32 
• Longitud Total: 16 bits. 
Es el tamaño total, en octetos, del datagrama, incluyendo el tamaño de la cabecera y el de los 
datos. El campo Longitud Total indica el tamaño total del datagrama IP, incluyendo cabecera y 
datos. Aunque el tamaño máximo teórico es de 65.535 octetos, históricamente se estableció 
que los hosts debían ser capaces de manejar datagramas de al menos 576 octetos. No obstante, 
IP permite el envío de datagramas de distintos tamaños, dependiendo de la MTU de la red. 
En caso de fragmentación este campo contendrá el tamaño del fragmento, no el del datagrama 
original. 
• Identificador: 16 bits. 
Identificador utilizado para distinguir los fragmentos de un mismo datagrama en caso de 
fragmentación. Se utilizará, en caso de que el datagrama deba ser fragmentado, para poder 
distinguir los fragmentos de un datagrama de los de otro. El originador del datagrama debe 
asegurar un valor único para la pareja origen-destino y el tipo de protocolo durante el tiempo 
que el datagrama pueda estar activo en la red. El valor asignado en este campo debe ir en 
formato de red. 
• Flags: 3 bits. 
Actualmente utilizado sólo para especificar valores relativos a la fragmentación de paquetes. 
Los 3 bits (por orden de mayor a menor peso) son: 
• bit 0: Reservado; debe ser 0. 
• bit 1: 0 = Divisible, 1 = No Divisible (DF). 
• bit 2 (MF, More Fragments): cuando vale 1 indica que existen más fragmentos; cuando vale 
0 indica que este es el último fragmento o que el paquete no ha sido fragmentado. 
La indicación de que un paquete es indivisible debe ser tenida en cuenta bajo cualquier 
circunstancia. Si el paquete necesitara ser fragmentado, no se enviará. 
• Posición de Fragmento: 13 bits. 
Indica en qué parte del datagrama actual va este fragmento. El desplazamiento del fragmento 
se expresa en unidades de 8 bytes, por lo que todos los fragmentos, excepto el último, deben 
tener un tamaño múltiplo de 8 bytes. 
• Tiempo de Vida (TTL): 8 bits. 
Indica el máximo número de enrutadores que un paquete puede atravesar. 
Cada vez que algún nodo procesa este paquete disminuye su valor en, como mínimo, una 
unidad. Cuando llegue a ser 0, el paquete será descartado. 
Típicamente toma el valor 64 o 128 en los datagramas. Básicamente impide que un mensaje 
este dando vueltas indefinidamente.

---

### Página 33

Modelo ISO/OSI, TCP/IP. Protocolos 
33 
• Protocolo: 8 bits. 
Indica el protocolo de las capas superiores al que debe entregarse el paquete Vea Números de 
protocolo IP para comprender como interpretar este campo. 
• Suma de Control de Cabecera: 16 bits. 
Suma de control de cabecera. Se recalcula cada vez que algún nodo cambia alguno de sus 
campos (por ejemplo, el Tiempo de Vida). El método de cálculo -intencionadamente simple- 
consiste en sumar en complemento a 1 cada palabra de 16 bits de la cabecera (considerando 
valor 0 para el campo de suma de control de cabecera) y hacer el complemento a 1 del valor 
resultante. 
• Dirección IP de origen: 32 bits. 
Debe ser dada en formato de red. 
• Dirección IP de destino: 32 bits. 
Debe ser dada en formato de red. 
• Opciones: Variable. 
Aunque no es obligatoria la utilización de este campo, cualquier nodo que procese un paquete 
IPv4 debe ser capaz de reconocer y procesar correctamente las opciones, o bien descartarlo si 
no las soporta. 
Puede contener un número indeterminado de opciones, que tendrán dos posibles formatos: 
• Formato de opciones simple. 
Se determina con un solo octeto indicando el 'Tipo de opción', el cual está dividido en 3 
campos. 
» Indicador de copia: 
1 bit. En caso de fragmentación, la opción se copiará o no a cada nuevo fragmento 
según el valor de este campo: 
» 0 = no se copia. 
» 1 = se copia. 
» Clase de opción: 
2 bits. Las posibles clases son: 
» 0 = control. 
» 1 = reservada.

---

### Página 34

Modelo ISO/OSI, TCP/IP. Protocolos 
34 
» 2 = depuración y mediciones. 
» 3 = reservada. 
» Número de opción: 
5 bits. Identificador de la opción. 
• Formato de opciones compuesto. 
Un octeto para el 'Tipo de opción', otro para el 'Tamaño de opción', y uno o más octetos 
conformando los 'Datos de opción'. 
El 'Tamaño de opción' incluye el octeto de 'Tipo de opción', el de 'Tamaño de opción' y la 
suma de los octetos de datos. 
La siguiente tabla muestra el formato de opciones compuesto actualmente definidas: 
Clase 
Número 
Tamaño 
Descripción 
0 
0 
- 
Final de lista de opciones. Formato simple 
0 
1 
- 
Ninguna operación (NOP). Formato simple 
0 
2 
11 
Seguridad 
0 
3 
variable 
Enrutado desde el Origen, abierto (Loose Source Routing) 
0 
9 
variable 
Enrutado desde el Origen, estricto (Strict Source Routing) 
0 
7 
variable 
Registro de Ruta (Record Route) 
0 
8 
4 
Identificador de flujo (Stream ID) 
2 
4 
variable 
Marca de tiempo (Internet Timestamping) 
» 'Final de Lista de Opciones': Se usa al final de la lista de opciones, si ésta no coincide 
con el final de la cabecera IP. 
» 'Ninguna Operación (NOP)': Se puede usar para forzar la alineación de las opciones en 
palabras de 32 bits. 
» "Seguridad": Especifica niveles de seguridad que van desde "No Clasificado" hasta 
"Máximo Secreto", definidos por la Agencia de Seguridad Nacional de la Defensa de 
EE. UU.

---

### Página 35

Modelo ISO/OSI, TCP/IP. Protocolos 
35 
» "Enrutado desde el Origen (abierto) y Registro de Ruta (LSSR)": Esta opción provee el 
mecanismo para que el originador de un datagrama pueda indicar el itinerario que ha 
de seguir a través de la red y para registrar el camino seguido. 
» Los Datos de Opción consisten en un puntero (un octeto) y una lista de 
direcciones IP (4 octetos cada una) que se han de alcanzar ("procesar"). 
» El puntero indica la posición de la siguiente dirección de la ruta, dentro de la 
Opción; así, su valor mínimo es de 4. 
» Cuando un nodo de Internet procesa la dirección de la lista apuntada por el 
puntero (es decir, se alcanza esa dirección) incrementa el puntero en 4, y redirige 
el paquete a la siguiente dirección. Si el puntero llega a ser mayor que el Tamaño 
de Opción significa que la información de ruta se ha procesado y registrado 
completamente y se redirigirá el paquete a su dirección de destino. 
» Si se alcanza la dirección de destino antes de haber procesado la lista de 
direcciones completa (el puntero es menor que el Tamaño de Opción) la siguiente 
dirección de la lista reemplaza a la dirección de destino del paquete y es a su vez 
reemplazada por la dirección del nodo que está procesando el datagrama ("Ruta 
Registrada"), incrementando, además, el puntero en 4. 
» Utilizando este método de sustituir la dirección especificada en origen por la Ruta 
Registrada se asegura que el tamaño de la Opción (y de la cabecera IP) no varía 
durante su recorrido por la red. 
» Se considera que la ruta especificada por el originador es "abierta" porque 
cualquier nodo que procesa el paquete es libre de dirigirlo a la siguiente dirección 
siguiendo cualquier otra ruta intermedia. 
» Sólo puede usarse una vez en un datagrama, y, en caso de fragmentación, la 
opción se copiará a los paquetes resultantes. 
» "Enrutado desde el Origen (estricto) y Registro de Ruta (SSRR)": Exactamente igual 
que LSSR, excepto en el tratamiento que los nodos harán de este datagrama. Al ser la 
ruta especificada "estricta", un nodo debe reenviar el paquete directamente a la 
siguiente dirección, es decir, no podrá redireccionarlo por otra red. 
» "Registro de Ruta': Mediante el uso de esta Opción se puede registrar el itinerario de un 
datagrama. Los Datos de Opción consisten en un puntero (un octeto) y un espacio 
relleno de ceros que contendrá la Ruta Registrada para el paquete. 
» Cuando un nodo recibe un paquete en el que está presente esta opción, escribirá 
su dirección IP en la posición indicada por el puntero, siempre que ésta sea menor 
que el Tamaño de Opción, e incrementará el puntero en 4. 
» Es preciso que el espacio reservado para la Ruta Registrada tenga una longitud 
múltiplo de 4; si al intentar grabar su dirección un nodo detecta que existe espacio 
libre, pero es menor de 4 octetos, el paquete no se reenvía (se pierde) y se 
notifica el error, mediante ICMP, al originador del datagrama.

---

### Página 36

Modelo ISO/OSI, TCP/IP. Protocolos 
36 
» Esta Opción no se copia en caso de fragmentación, y sólo puede aparecer una vez 
en un paquete. 
» Identificador de flujo: Esta opción proporciona una manera para Identificador de flujo 
SATNET de 16 bits para ser transportado a través de redes que no admiten el 
concepto de flujo. 
» Marca de tiempo: Permite registrar marcas temporales a lo largo del recorrido del 
datagrama, con fines de diagnóstico y medición de retardos. 
2.2. Versión IPv6 
Para que los dispositivos se conecten a la red, necesitan una dirección IP. 
Cuando se diseñó IPv4, casi como un experimento, no se pensó que pudiera tener tanto éxito 
comercial, y dado que sólo dispone de 2^32 direcciones (direcciones con una longitud de 32 bits, es 
decir, 4.294.967.296 direcciones), junto con el imparable crecimiento de usuarios y dispositivos, 
implicó que pronto se agotaran las direcciones. 
Por este motivo, y previendo la situación, el organismo que se encarga de la estandarización de los 
protocolos de Internet (IETF, Internet Engineering Task Force), trabajó durante los años noventa en el 
desarrollo de una nueva versión del Protocolo de Internet (IPv6). 
Posee direcciones con una longitud de 128 bits, es decir 2^128 posibles direcciones 
(340.282.366.920.938.463.463.374.607.431.768.211.456), o, dicho de otro modo, 340 sextillones. 
El despliegue de IPv6 se irá realizando gradualmente, en una coexistencia ordenada con IPv4, al que irá 
desplazando a medida que dispositivos de cliente, equipos de red, aplicaciones, contenidos y servicios 
se vayan adaptando a la nueva versión del protocolo de Internet. 
El uso de IPv6 va a ser cada vez más generalizado, por lo que vamos a profundizar en el 
conocimiento de este protocolo. 
Una dirección IPv6 tiene un tamaño de 128 bits y se compone de ocho campos de 16 bits, cada uno de 
ellos unido por dos puntos. 
Cada campo debe contener un número hexadecimal, a diferencia de la notación decimal con puntos de 
las direcciones IPv4. 
En la figura siguiente, las equis representan números hexadecimales.

---

### Página 37

Modelo ISO/OSI, TCP/IP. Protocolos 
37 
Formato básico de las direcciones IPv6: 
 
Fuente: Wikipedia 
• Ejemplo de los dígitos, que muestran los 128 bits completos de una dirección IPv6: 
2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b 
• Los tres primeros campos, de la dirección IPv6 (48 bits), 2001:0db8:3c4d, corresponden al 
prefijo global, que describe la topología pública asignada por el ISP o el RIR (Regional 
Internet Registry, Registro Regional de Internet). 
• El siguiente campo de 16 bits, 0015, corresponde al identificador de subred, que es 
asignado por el administrador del sitio y describe la topología privada interna. 
• Los últimos 4 campos, 64 bits, que están más a la derecha, 0000:0000:1a2f:1a2b, 
contienen el ID de interfaz. 
• El ID de interfaz puede configurarse automáticamente o manualmente. Inicialmente se 
utilizó el formato EUI-64 derivado de la dirección MAC, aunque en la actualidad es habitual 
el uso de identificadores aleatorios por motivos de privacidad. 
El protocolo IPv6 define un conjunto de encabezados, que se dividen en básicos y de extensión. 
Descripción de la función de cada campo de encabezados básicos 
• Versión: 
Número de versión de 4 bits del protocolo de Internet = 6. 
• Clase de tráfico: 
Campo de clase de tráfico de 8 bits.

---

### Página 38

Modelo ISO/OSI, TCP/IP. Protocolos 
38 
• Etiqueta de flujo: 
Campo de 20 bits. 
• Tamaño de carga útil: 
Entero sin signo de 16 bits, que representa el tamaño de la carga útil, es decir, el conjunto de 
encabezados de extensión y los datos que siguen al encabezado IPv6. 
• Encabezado siguiente: 
Selector de 8 bits. Identifica el tipo de encabezado que va inmediatamente después del 
encabezado de IPv6. Emplea los mismos valores que el campo de protocolo IPv4. 
• Límite de salto: 
Entero sin signo de 8 bits. Disminuye en uno cada nodo que reenvía el paquete. El paquete se 
desecha si el límite de salto se reduce a cero. 
• Dirección de origen: 
128 bits. Dirección del remitente inicial del paquete. 
• Dirección de destino: 
128 bits. Dirección del destinatario previsto del paquete. El destinatario previsto no es 
necesariamente el destinatario si existe un encabezado de enrutamiento opcional. 
Descripción de la función de encabezados de extensión de IPv6 
• Encaminamiento: 
Enrutamiento extendido, por ejemplo, ruta holgada fijada en origen de IPv4. 
• Fragmentación: 
Fragmentación y reensamblado, realizada únicamente por el nodo origen y el nodo destino. 
• Autenticación: 
Integridad y autenticación, y seguridad. 
• Encapsulado de carga útil: 
Confidencialidad.

---

### Página 39

Modelo ISO/OSI, TCP/IP. Protocolos 
39 
• Opciones de salto a salto: 
Opciones especiales que necesitan procesamiento salto a salto. 
• Opciones de destino: 
Información opcional que el nodo de destino debe examinar. 
2.2.1. Ámbito de direcciones IPv6 
Toda dirección IPv6, excepto la (::), pertenece a un "ámbito" de red, ya que la dirección indefinida 
no se asigna a ningún interfaz ni se utiliza para comunicaciones reales. 
Dentro de este ámbito diferenciaremos 2 tipos de direcciones: 
• En una dirección UNICAST: 
Cada dirección de destino corresponde a un UNICO destino. 
• En MULTICAST: 
También hay una asociación de una dirección destino, pero a varias máquinas. 
En este entorno hay unas direcciones con significado especial. Vamos a verlo en la siguiente tabla, 
algunas asignada al UNICAST y otras a MULTICAST. 
Bloques de direccionamiento especiales 
Bloque de 
direcciones 
(CIDR) 
Primera 
dirección 
Última dirección 
N° de 
direcciones 
Alcance 
Propósito 
::/0 
:: 
ffff:ffff:ffff:ffff:ffff 
:ffff:ffff:ffff 
2128 
Enrutamiento 
Ruta por defecto 
::/128 
:: 
 
1 
Software 
Dirección sin 
especificar 
::1/128 
::1 
 
1 
Host 
Dirección de 
loopback 
::ffff:0:0/96 
::ffff:0.0.0.0 
::ffff:255.255.255.255 
232 
Software 
Dirección IPv4 
mapeada 
::ffff:0:0:0/96 
::ffff:0.0.0.0 
::ffff:0:255.255.255.255 
232 
Software 
Dirección IPv4 
traducida

---

### Página 40

Modelo ISO/OSI, TCP/IP. Protocolos 
40 
Bloques de direccionamiento especiales 
Bloque de 
direcciones 
(CIDR) 
Primera 
dirección 
Última dirección 
N° de 
direcciones 
Alcance 
Propósito 
64:ff9b::/96 
64:ff9b::0.0.0.0 
64:ff9b::255.255 
.255.255 
232 
Internet 
Traducción 
IPv4/IPv6 
100::/64 
100:: 
100::ffff:ffff:ffff:ffff 
264 
Enrutamiento 
Prefijo 
2001::/32 
2001:: 
2001::ffff:ffff:ffff 
:ffff:ffff:ffff 
296 
Internet 
Túnel Teredo 
2001:20::/28 
2001:20:: 
2001:2f:ffff:ffff 
:ffff:ffff:ffff:ffff 
2100 
Software 
ORCHIDv2 
2001:db8::/32 
2001:db8:: 
2001:db8:ffff:ffff 
:ffff:ffff:ffff:ffff 
296 
Documentación 
Direcciones 
utilizadas en 
documentación y 
código fuente de 
ejemplo 
2002::/16 
2002:: 
2002:ffff:ffff:ffff 
:ffff:ffff:ffff:ffff 
2112 
Internet 
Esquema de 
direccionamiento 
6to4 (ahora en 
desuso) 
fc00::/7 
fc00:: 
fdff:ffff:ffff:ffff 
:ffff:ffff:ffff:ffff 
2121 
Red privada 
Dirección local 
única 
fe80::/10 
fe80:: 
febf:ffff:ffff:ffff 
:ffff:ffff:ffff:ffff 
2118 
Enlace 
Dirección de 
Enlace-Local 
ff00::/8 
ff00:: 
ffff:ffff:ffff:ffff 
:ffff:ffff:ffff:ffff 
2120 
Internet 
Dirección 
multidifusión 
(multicast) 
Direcciones Unicast 
Vamos a explicar con mayor detalle las direcciones Unicast: 
• Dirección indefinida. 
::/128 
La dirección con todos sus bits a 0 se llama dirección indefinida (similar a la dirección 0.0.0.0 en 
IPv4).

---

### Página 41

Modelo ISO/OSI, TCP/IP. Protocolos 
41 
Esta dirección no puede nunca ser asignada a ningún interface, pues se utiliza únicamente por el 
software de una aplicación antes de conocer la dirección origen de una conexión. Los routers no 
deben encaminar paquetes con la dirección indefinida. 
Las aplicaciones pueden escuchar (listen) en uno o más interfaces por nuevas conexiones. Esto 
puede verse en un listado de conexiones activas con una dupla dirección IP y número de puerto 
separados por dos puntos. Cuando la aplicación está escuchando (listening) en todos los 
interfaces disponibles, aparece la dirección indefinida en dicho listado. 
• Ruta por defecto. 
::/0 
La ruta por defecto para tráfico unicast (correspondiente a la ruta a 0.0.0.0 con máscara 0.0.0.0 
en IPv4). 
• Direcciones locales. 
• ::1/128 
La dirección de loopback es una dirección unicast del localhost. Si una aplicación en un host 
envía paquetes a esta dirección, la pila IPv6 enviará de vuelta los paquetes al mismo 
interface virtual (correspondiente a 127.0.0.1 en IPv4). 
• fe80::/10 
Las direcciones de prefijo enlace-local (link-local) son válidas (utilizables) y únicas (no 
repetidas) solo en la red local. Dentro de este rango de enlace local (fe80::/10), en la 
práctica se utiliza el prefijo fe80::/64 para la asignación de direcciones a interfaces. Los 64 
bits menos significativos suelen construirse a partir de la dirección hardware del interface 
en formato EUI-64 modificado. 
Las direcciones de enlace local son requeridas en todos los interfaces con IPv6 habilitado; 
por ello, las aplicaciones pueden aprovechar la existencia de direcciones de enlace local aun 
cuando no haya encaminamiento IPv6. Estas direcciones son comparables a las direcciones 
de auto-configuración 169.254.0.0/16 en IPv4. 
• Dirección local única. 
fc00::/7 
Las direcciones locales únicas (ULA's por sus siglas en inglés) se utilizan para comunicaciones 
locales. Son enrutables solo dentro de un ámbito cooperativo (similar a los rangos de 
direcciones privadas 10/8, 172.16/12, y 192.168/16 en IPv4). Las direcciones incluyen una 
secuencia pseudoaleatoria en el prefijo de encaminamiento (routing prefix) para minimizar el 
riesgo de conflictos en la interconexión de plataformas diferentes o si los paquetes se desvían a 
Internet. A pesar del uso restringido y local de estas direcciones, su ámbito es global, es decir, se 
esperan sean únicas (no repetidas) en todo el mundo.

---

### Página 42

Modelo ISO/OSI, TCP/IP. Protocolos 
42 
• Transición de IPv4. 
• ::ffff:0:0/96 
Este prefijo designa una dirección IPv6 IPv4-mapeada. Salvo pocas excepciones, este tipo 
de dirección permite el funcionamiento de protocolos de capa de transporte IPv4 en 
software (APIs) IPv6. Las aplicaciones servidoras solo tienen que abrir un socket en 
listening para aceptar conexiones de clientes usando protocolos IPv6 o IPv4. Los clientes 
IPv6 serán gestionados de modo nativo, mientras que los clientes IPv4 aparecerán como 
clientes IPv6 cuya dirección es una dirección IPv6 IPv4-mapeada. La transmisión se 
gestiona de modo similar; los sockets pueden transmitir datagramas IPv4 o IPv6, mediante 
la conexión a una dirección IPv6 nativa o a una dirección IPv4-mapeada. (Vea también 
Mecanismos de transición a IPv6). 
• ::ffff:0:0:0/96 
Un prefijo reservado para direcciones IPv4-traducidas, utilizadas por el protocolo Stateless 
IP/ICMP Translation (SIIT). 
• 64:ff9b::/96 
El prefijo "Well-Known" (ya conocido). Este prefijo se utiliza para traducciones automáticas 
IPv4/IPv6.19. 
• 2002::/16 
Esta red se utiliza para el direccionamiento 6to4. Se utiliza también una dirección de la red 
IPv4 192.88.99.0/24. 
• Direcciones de uso especial. 
IANA ha reservado un bloque de direcciones llamado 'Sub-TLA ID' que consisten en 64 prefijos 
de red desde 2001:0000::/29 hasta 2001:01f8 ::/29. Se han realizado tres asignaciones en este 
bloque: 
• 2001::/32 
Usado por el protocolo de túneles Teredo (que también cae dentro de la categoría 
mecanismo de transición IPv6). 
• 2001:2::/48 
Asignado a Benchmarking Methodology Working Group (BMWG) para comparativas 
(benchmarking) en IPv6 (similar a la red 198.18.0.0/15 para comparativas en IPv4). 
• 2001:10::/28 
ORCHID (Overlay Routable Cryptographic Hash Identifiers). Son direcciones IPv6 no-
enrutables usadas para identificadores criptográficos Hash.

---

### Página 43

Modelo ISO/OSI, TCP/IP. Protocolos 
43 
• Documentación. 
2001:db8::/32 
Este prefijo está reservado para documentación.22. Estas direcciones deben usarse siempre que 
alguien quiera escribir un ejemplo de dirección IPv6, o se plasmen modelos de red (similar a las 
redes 192.0.2.0/24, 198.51.100.0/24, y 203.0.113.0/24 en IPv4). 
• Direcciones obsoletas (historia). 
El prefijo site-local fec0::/10 especifica que la dirección es válida únicamente dentro de la red de 
una organización. Formaba parte de la arquitectura de direccionamiento original en diciembre 
de 1995, pero su uso fue desaconsejado en septiembre de 2004, pues la definición del término 
inglés site era ambigua provocando reglas de routing confusas. Las nuevas redes no debían 
soportar este tipo especial de direcciones. En octubre de 2005, una nueva especificación24 
sustituyó este tipo de direcciones por las direcciones locales únicas. 
El bloque de direcciones 0200::/7 fue definido como un prefijo OSI NSAP-mapped en agosto de 
1996, pero fue eliminado en diciembre de 2004. 
El prefijo de 96-bits a cero ::/96, conocido originalmente como direcciones IPv4-compatibles, 
fue mencionado en 1995 pero descrito por primera vez en 1998. 
Esta clase de direcciones se usaba para representar direcciones IPv4 dentro de tecnología IPv6, 
facilitando la transición. 
Era una dirección IPv6 con sus primeros (más significativos) 96 bits a cero, mientras que los 
últimos 32 bits eran la dirección IPv4 que representaban. 
En febrero de 2006 la Internet Engineering Task Force (IETF) ha desaconsejado la utilización de 
direcciones IPv4-compatibles. El único uso que se mantiene de este formato de dirección es al 
representar una dirección IPv4 en una tabla o base de datos con campos de tamaño fijos, que 
también deben ser capaces de almacenar direcciones IPv6. 
La resolución inversa de direcciones IPv6 se configuraba originalmente en el Domain name 
system (DNS) en la zona ip6, bajo el dominio principal .int. 
La intención inicial era que el dominio .arpa fuese movido dentro de .int, pero se desechó en el 
año 2000 por la Internet Architecture Board (IAB). 
Por ello, el registro inicial bajo ip6.int debía moverse a ip6.arpa. La IAB lo formalizó en agosto de 
2001. La zona ip6.int fue oficialmente eliminada el 6 de junio de 2006. 
Se reservó el bloque de direcciones 3ffe::/16 para pruebas de la red 6bone en diciembre de 
1998. Antes de eso se utilizaba el rango de direcciones 5F00::/8. 
Ambos rangos fueron liberados en junio de 2006, con la defunción del proyecto 6bone.

---

### Página 44

Modelo ISO/OSI, TCP/IP. Protocolos 
44 
Direcciones Multicast 
ff00::/8 es el rango general para direcciones multicast en IPv6. 
Las direcciones Multicast ff00::/12 están reservadas y no deberían utilizarse para ningún grupo 
multicast. Para ver una lista completa de direcciones IPv6 Multicast reservadas se debe visitar a Internet 
Assigned Numbers Authority (IANA). 
A continuación, se muestran algunas de las más usuales: 
Dirección 
Descripción 
Ámbitos disponibles 
ff0X::1 
Dirección all-nodes (todos los 
nodos). 
Identifica al grupo de todos los 
nodos IPv6. 
Disponible en el ámbito (scope) 1 (interface-
local) y 2 (link-local): 
ff01::1 → Todos los nodos en el interface local 
ff02::1 → Todos los nodos en el enlace local 
ff0X::2 
Dirección all-routers (todos los 
routers). 
Identifica al grupo de todos los 
routers IPv6. 
Disponible en el ámbito (scope) 1 (interface-
local), 2 (link-local) y 5 (site-local): 
ff01::2 → Todos los routers en el interface 
local 
ff02::2 → Todos los routers en el enlace local 
ff05::2 → Todos los routers en el site-local 
ff02::5 
OSPFIGP 
2 (enlace-local) 
ff02::6 
OSPFIGP Designated Routers 
2 (enlace-local) 
ff02::9 
Routers RIP 
2 (enlace-local) 
ff02::a 
Routers EIGRP 
2 (enlace-local) 
ff02::d 
Todos los routers PIM 
2 (enlace-local) 
ff0X::fb 
mDNSv6 
Disponible en todos los ámbitos 
ff0X::101 
Todos los servidores de NTP 
(Network Time Protocol) 
Disponible en todos los ámbitos 
ff02::1:1 
Link Name 
2 (enlace-local) 
ff02::1:2 
All-dhcp-agents 
2 (enlace-local) 
ff02::1:3 
Link-local Multicast Name 
Resolution 
2 (enlace-local)

---

### Página 45

Modelo ISO/OSI, TCP/IP. Protocolos 
45 
Dirección 
Descripción 
Ámbitos disponibles 
ff05::1:3 
All-dhcp-servers 
5 (site-local) 
FF02::1:FF00:0000/104 
Dirección Solicited-Node. Véase 
explicación más abajo 
2 (enlace-local) 
FF02:0:0:0:0:2:FF00::/104 
Node Information Queries 
2 (enlace-local) 
• Dirección multicast Solicited-node. 
Los 24 bits menos significativos del group ID de una dirección Solicited-Node se rellenan con los 
24 bits menos significativos de la dirección unicast o anycast. Estas direcciones permiten la 
resolución de la dirección de red vía Neighbor Discovery (NDP) en la red sin molestar a todos 
los hosts conectados (como ocurría con ARP en IPv4). Un host debe unirse (join) a un grupo 
multicast Solicited-Node para cada una de sus direcciones Unicast o Anycast. 
2.2.2. Configuración automática sin estado 
Tras el arranque del sistema, un nodo crea automáticamente una dirección de enlace-local en cada 
interface con IPv6 habilitado, aunque se hayan configurado manualmente u obtenido por DHCPv6 
direcciones globales. 
Esto se realiza de modo automático, y sin ningún tipo de configuración previa gracias a la configuración 
automática sin estado (SLAAC, stateless address autoconfiguration), usando un componente del 
Neighbor Discovery Protocol. Esta dirección tendrá el prefijo fe80::/64. 
Además, el host puede crear una dirección unicast encaminable cuando un router responde a su 
solicitud de router con una asignación de subred. 
Los 64 bits menos significativos de estas direcciones se rellenan con un identificador de interfaz de 64 
bits. Inicialmente se utilizaba el formato EUI-64 modificado derivado de la dirección MAC, aunque 
actualmente es habitual el uso de identificadores aleatorios por motivos de privacidad. Este 
identificador se utiliza para las direcciones automáticas de ese interfaz, de modo que el host se une a un 
grupo multicast Solicited-Node específico por cada dirección IPv6 configurada, utilizado por el 
Neighbor Discovery Protocol. 
Para ello se utiliza una dirección multicast formada a partir del prefijo ff02::1:ff00:0/104 y los 24 bits 
menos significativos de la dirección IPv6 unicast. 
2.2.3. EUI-64 Modificado 
El identificador de interfaz de 64 bits deriva comúnmente de los 48 bits de la dirección MAC. Una 
dirección MAC 00:1D:BA:06:37:64 se convierte en una dirección EUI-64 de 64 bits insertando FF:FE en 
el medio.

---

### Página 46

Modelo ISO/OSI, TCP/IP. Protocolos 
46 
Lo primero es separar la dirección MAC en dos bloques iguales, 3 octetos a cada lado, para insertar el 
octeto FFFE tras los 24 primeros bits o 3 primeros octetos: 00:1D:BA:FF:FE:06:37:64 
Cuando usamos EUI-64 para formar una dirección IPv6, invertimos el bit Universal/Local (U/L), que es 
el segundo bit menos significativo del primer octeto del identificador EUI-64, de manera que un 0 en 
dicho bit del EUI-64 resultará un 1 o a la inversa en el EUI-64 modificado. 
Para que quede claro, y partiendo de la dirección señalada, 00:1D:BA:FF:FE:06:37:64 
1. Nuestro primer octeto hexadecimal 00 corresponde a 00000000 en binario. 
2. Se invierte el bit U/L (segundo bit menos significativo), obteniendo 00000010. 
3. Pasamos nuestro binario 00000010 de nuevo a hexadecimal: 02 
Y ya tenemos nuestra dirección EUI-64 MODIFICADA. 
Enumeramos los pasos desde el principio a continuación: 
1. 00:1D:BA:06:37:64 (partimos de la dirección MAC de 48 bits). 
2. 00:1D:BA:FF:FE:06:37:64 (se añaden los octetos FF:FE en el medio). 
3. 02:1D:BA:FF:FE:06:37:64 (se invierte el bit U/L, segundo bit menos significativo del primer 
octeto). 
Para identificar la interfaz anterior en la red IPv6 2001:db8:1:2::/64, añadimos el identificador EUI-64 
modificado completo 02:1D:BA:FF:FE:06:37:64, resultando la dirección IPv6: 
2001:db8:1:2:021d:baff:fe06:3764/64 
La razón de modificar el bit U/L: 
• Es debido a que cuando asignamos direcciones de modo manual a un interfaz, es probable que 
asignemos una del tipo 2001:db8:1:2::1/64 en lugar de la menos atractiva e intuitiva 
2001:db8:1:2:0200::1/64. 
• Cuando asignamos manualmente direcciones de enlace-local, la necesidad de esta modificación 
es más evidente: configuraremos manualmente una dirección corta fe80::1 en lugar de una larga 
fe80:0:0:0:0200::1. 
En resumen, la modificación del bit U/L en EUI-64 reduce la probabilidad de colisiones entre 
direcciones generadas automáticamente y direcciones configuradas manualmente, facilitando 
además la diferenciación entre identificadores globales y locales.

---

### Página 47

Modelo ISO/OSI, TCP/IP. Protocolos 
47 
2.2.4. Detección de direcciones duplicadas 
La asignación de una dirección IPv6 unicast a un interface necesita de una prueba interna de su 
disponibilidad, utilizando los mensajes ICMPv6 tipo 135 (Neighbor Solicitation) y 136 (Neighbor 
Advertisement). 
Durante el proceso de verificación de disponibilidad, la dirección tiene un estado de dirección 
tentativa. 
("Tentativa", significa que todavía no tenemos una dirección definitiva) 
El nodo se une a la dirección multicast solicited-node para la dirección tentativa (si no lo ha hecho ya), y 
envía neighbor solicitations utilizando como dirección origen la dirección indefinida (::/128) y como 
dirección destino la dirección multicast solicited-node correspondiente a la dirección tentativa. 
El nodo también se une a la dirección de multicast all-nodes (todos los equipos) ff02::1, por lo que 
recibirá los anuncios del resto de equipos (Neighbor Advertisements). 
Si un nodo recibe una solicitud (neighbor solicitation) con su dirección tentativa como dirección 
destino, la dirección no es única. 
Tampoco podrá ser única si el nodo recibe un anuncio (neighbor advertisement) con la dirección 
tentativa como origen. 
Tan sólo después de haber verificado que la dirección es única, puede ser usada y asignada a un 
interface. 
2.2.5. Tiempo de vida de la dirección 
Cada dirección IPv6 vinculada a una interfaz tiene un tiempo de vida preestablecido. 
El tiempo de vida puede ser infinito o limitado, dependiendo de los valores configurados. Hay dos 
valores que rigen el tiempo de vida de una dirección: 
• Preferred lifetime (tiempo preferido). 
• Valid lifetime (tiempo de validez). 
Estos tiempos de vida pueden configurarse en los routers que proveen los valores para autoconfiguración, 
o especificar durante la configuración manual de las direcciones en las interfaces. 
Cuando se asigna una dirección a un interface tiene el estado preferred (preferido), que mantiene 
durante su preferred-lifetime.

---

### Página 48

Modelo ISO/OSI, TCP/IP. Protocolos 
48 
Tras expirar dicho tiempo de vida, el estado pasa a deprecated (obsoleto) y la dirección no podrá 
usarse para nuevas conexiones. La dirección pasa a invalid (inválida) cuando expira también su valid-
lifetime; la dirección se elimina del interfaz y deja de ser válida y utilizable. 
Direcciones temporales 
Las estáticas y mundialmente únicas direcciones MAC, usadas por la configuración automática sin 
estado para crear identificadores de interface, ofrecen una oportunidad para hacer un seguimiento de 
los equipos y usuarios a través del tiempo y de las distintas redes IPv6. 
Para reducir la atadura de la identidad del usuario a una porción de dirección IPv6, un host puede crear 
direcciones temporales con identificadores de interfaces basados en números aleatorios y tiempos de 
vida relativamente cortos (de horas o días), tras los cuales se reemplazan con nuevas direcciones. 
Un host puede utilizar direcciones temporales como direcciones origen para conexiones salientes; 
mientras, el resto de hosts utilizará la dirección pública para acceder a él tras preguntar a DNS. 
Los sistemas configurados en IPv6 en Windows Vista, Windows Server 2008 o versiones posteriores 
utilizan direcciones temporales por defecto. 
2.2.6. Selección automática de dirección 
Las interfaces de red habilitados para IPv6 tienen normalmente más de una dirección IPv6. 
Por ejemplo, una dirección de enlace-local y una dirección global, o direcciones permanentes versus 
temporales. 
IPv6 introduce los conceptos de alcance y políticas de prefijos, dando múltiples opciones para 
seleccionar la dirección origen y destino en comunicaciones con otros hosts. 
El algoritmo de selección de direcciones, que elige la dirección más apropiada para la comunicación con 
un destino concreto (incluyendo el uso de direcciones IPv4-mapeadas en implementaciones de doble 
pila), está basado en una tabla de políticas de prefijos, que asocia cada prefijo con un nivel de prioridad. 
La tabla de Políticas de Prefijos por defecto sería como la siguiente: 
Prefijo 
Prioridad 
Etiqueta 
::1/128 
50 
0 
::/0 
40 
1 
2002::/16 
30 
2

---

### Página 49

Modelo ISO/OSI, TCP/IP. Protocolos 
49 
Prefijo 
Prioridad 
Etiqueta 
::/96 
20 
3 
::ffff:0:0/96 
10 
4 
En una configuración por defecto, IPv6 tendrá mayor prioridad que IPv4, y también utilizará direcciones 
destino con el ámbito más pequeño posible, de modo que las comunicaciones de enlace-local son 
preferidas a caminos globales cuando ambos sean igualmente adecuados. 
La tabla de políticas de prefijos es conceptualmente similar a una tabla de rutas, en la que la prioridad se 
utiliza para decidir qué prefijo se utilizará para las conexiones; una mayor prioridad es indicada por un 
valor numérico mayor. 
Las direcciones origen candidatas se obtienen del Sistema Operativo, y las direcciones destino 
candidatas pueden ser consultadas vía Domain Name System (DNS). 
Después se cruzan con la tabla de políticas de prefijos, seleccionando el prefijo más largo que coincida 
con la dirección IPv6, de acuerdo con la prioridad del prefijo y la longitud del mismo. 
2.2.7. Direcciones de enlace-local e índice de zonas 
Debido a que todas las direcciones de enlace-local en un host tienen un prefijo común, no se pueden 
utilizar los procedimientos normales de encaminamiento basados en direcciones de red para elegir el 
interface de salida en el envío de paquetes a un destino de enlace-local. 
Se necesita de un identificador especial, conocido como zone index o scope ID (índice de zona o 
identificador de ámbito), para proveer información de encaminamiento adicional; en el caso de 
direcciones de enlace-local, los índices de zona corresponden a identificadores de interface. 
Al escribir textualmente una dirección, añadimos el índice de zona a la dirección separado por un signo 
de porcentaje (%). 
La sintaxis actual de los índices de zona depende del sistema operativo: 
• La pila IPv6 en Microsoft Windows utiliza índices de zona numéricos, p.ej. fe80::3%1. El índice se 
establece por el número de interface. 
• La mayoría de sistemas Unix (p.ej. BSD, Linux, Mac OS X) usa el nombre de interface como 
índice de zona: fe80::3%eth0. 
La notación de índice de zona causa conflictos de sintaxis al usar la dirección para URIs o URLs, ya que el 
carácter '%' tiene un significado especial y debe codificarse como '%25' según las reglas de escape de URI.

---

### Página 50

Modelo ISO/OSI, TCP/IP. Protocolos 
50 
2.2.8. Direcciones IPv6 en el DNS 
Mediante el Domain Name System, los hostnames se mapean a direcciones IPv6 por registros AAAA, 
también llamados registros cuádruple-A. La IANA (Internet Assigned Numbers Authority), siguiendo las 
especificaciones definidas por la IETF, ha reservado el dominio ip6.arpa para la resolución inversa de DNS, 
dividiendo el espacio de nombres jerárquicamente por cada dígito hexadecimal de la dirección IPv6. 
(Esta traducción se define en el RFC 3596.) 
De igual modo que en IPv4, cada host puede estar representado en el DNS por dos registros, un registro 
directo (address record) y un registro de resolución inversa. 
Por ejemplo, un equipo llamado servidor en la zona 'ejemplo.es' tiene la dirección local única 
fdda:5cc1:23:4::1f. 
Su registro cuádruple-A es: 
servidor.ejemplo.es. IN   AAAA   fdda:5cc1:23:4::1f 
Y su resolución inversa es: 
f.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.0.0.0.3.2.0.0.1.c.c.5.a.d.d.f.ip6.arpa. IN   PTR   
servidor.ejemplo.es. 
Este registro inverso puede definirse en varias zonas, dependiendo de la cadena de delegación en la 
zona d.f.ip6.arpa. 
El DNS es independiente del protocolo de transporte. Las peticiones y respuestas pueden ser 
transmitidas sobre IPv6 o IPv4, independientemente del tipo de información transportada. 
Campos registro AAAA 
NAME 
Nombre de Dominio 
TYPE 
AAAA (28) 
CLASS 
Internet (1) 
TTL 
Tiempo de vida en segundos 
RDLENGTH 
Longitud del campo RDATA 
RDATA 
Dirección IPv6 en formato texto

---

### Página 51

Modelo ISO/OSI, TCP/IP. Protocolos 
51 
El campo RDATA almacena la dirección IPv6 en formato binario de 128 bits, aunque en los ficheros de 
zona DNS se representa en formato textual hexadecimal. 
Transición 
Históricamente, muchos dispositivos NAT y routers en los hogares han gestionado incorrectamente los 
registros AAAA. 
Algunos de ellos simplemente desechan las peticiones DNS a estos registros, en lugar de devolver una 
respuesta negativa apropiada. Debido a que la petición es desechada, el host debe esperar el timeout de 
esa petición. 
Esto, a menudo, causa una percepción de lentitud en la conexión de hosts IPv6. 
2.2.9. Cabecera IPV6 
Los primeros 40 bytes (320 bits) son la cabecera del paquete y contiene los siguientes campos: 
 
Fuente: Wikipedia 
• Versión del protocolo IP (4 bits). 
• Clase de tráfico (8 bits, Prioridad del Paquete). 
• Etiqueta de flujo (20 bits, manejo de la Calidad de Servicio). 
• Longitud de la carga útil(16 bits). 
• Cabecera siguiente (8 bits). 
• Límite de saltos (8 bits). 
• Direcciones de origen (128 bits). 
• Direcciones de destino (128 bits).

---

### Página 52

Modelo ISO/OSI, TCP/IP. Protocolos 
52 
Hay dos versiones de IPv6 levemente diferentes. La ahora obsoleta versión inicial, descrita en el RFC 
1883, difiere de la versión actualmente estandarizada, descrita originalmente en el RFC 2460, en dos 
campos: hay 4 bits que han sido reasignados desde "etiqueta de flujo" (flow label) a "clase de tráfico" 
(traffic class). El resto de diferencias son menores. 
En IPv6 la fragmentación se realiza solamente en el nodo origen del paquete, al contrario que en IPv4 
en donde los routers pueden fragmentar un paquete. 
En IPv6, las opciones también desaparecen de la cabecera estándar y son especificadas por el campo 
"Cabecera Siguiente" (Next Header), similar en funcionalidad en IPv4 al campo Protocolo. Un ejemplo: 
en IPv4 uno añadiría la opción "ruta fijada desde origen" (Strict Source and Record Routing) a la 
cabecera IPv4 si quiere forzar una cierta ruta para el paquete, pero en IPv6 uno modificaría el campo 
"Cabecera Siguiente" indicando que viene una cabecera de encaminamiento. 
La cabecera de encaminamiento podrá entonces especificar la información adicional de 
encaminamiento para el paquete, e indicar que, por ejemplo, la cabecera TCP será la siguiente. Este 
procedimiento es análogo al uso de AH y ESP en IPsec, que se implementa mediante cabeceras de 
extensión en IPv6. 
2.3. Comparación de cabeceras IPv4 y IPv6 
Entender la estructura de la cabecera de un protocolo y el tipo de información que se puede transportar 
con la misma es el mejor camino para aprender a trabajar con un protocolo. 
Este conocimiento ayuda a identificar cómo se puede configurar el protocolo de la mejor manera 
posible y qué opciones ofrece. 
También ayuda a identificar posibles fuentes de problemas y soluciones de problemas. 
La estructura de la cabecera de un paquete IPv6 está especificada en el RFC 8200 (que reemplaza al 
RFC 2460). 
Durante el diseño de IPv6 se ha analizado la cabecera IPv4, simplificándola y eliminando aquello que era 
superfluo. 
La cabecera IPv6 es mucho más simple que la de IPv4 y esto acelera el procesamiento de los datos. 
La cabecera IPv6 tiene una longitud fija de 40 bytes, de los cuales 32 bytes corresponden a las 
direcciones de origen y destino (16 bytes cada una) y 8 bytes al resto de campos de control. 
Por último, nos centraremos en el funcionamiento de las nuevas cabeceras de extensión. 
2.3.1. Las cabeceras de extensión (extension headers) 
En la cabecera de IPv4, dentro de la propia cabecera IPv4, después de los campos fijos y antes del 
campo de datos, se coloca el campo de 'Opciones'.

---

### Página 53

Modelo ISO/OSI, TCP/IP. Protocolos 
53 
Estas "Opciones" pueden ocupar hasta 40 bytes, ya que la cabecera IPv4 tiene un tamaño máximo de 60 
bytes y dan indicaciones a los nodos que se encuentran en el camino (o path) que va del equipo origen 
al destino, acerca de cuestiones relacionadas con seguridad, enrutamiento, timestamping, etc. 
Concretamente, las opciones disponibles en IPv4 son: 
• Crear un registro de la ruta. 
En el datagrama se van guardando las direcciones IP de los routers visitados. Cada router 
intenta poner su dirección al final de la lista existente. Si la lista está llena y no puede hacerlo, 
simplemente reenvía el datagrama sin añadir su dirección. 
• Marcas de tiempo (Timestamp). 
• Seguridad básica del Departamento de Defensa. 
Permite asegurar que el origen del datagrama tiene autorización para ser transmitido. Son 
opciones históricas definidas para entornos del Departamento de Defensa de EE. UU., hoy en 
desuso. 
• Seguridad extendida del Departamento de Defensa. 
Es una opción que permite a los departamentos antes mencionados hacer configuraciones de 
seguridad específicas según sus necesidades. 
• Sin operación (No Operation). 
Se usa como relleno entre opciones, para alinear la siguiente opción en un marco de 32 bits. 
En este caso se pretende rellenar el final del campo de opción para que el tamaño total sea 
múltiplo de 32 bits. 
En IPv4 no suelen utilizarse estas opciones porque ralentizan la transmisión. 
En IPv6 las opciones se manejan por medio de las llamadas Cabeceras de Extensión (Extension 
Headers). Estas cabeceras se insertan en el paquete solo si las opciones son necesarias. 
En un primer ejemplo de paquete IPv6, hay una única cabecera IPv6 que precede a los datos de la capa 
superior de transporte. 
En un segundo ejemplo, se ha insertado una tercera cabecera entre las dos anteriores. Ahora, la 
cabecera IPv6 indica que la siguiente cabecera es una cabecera de Extensión del tipo Routing, cuyo 
código identificativo es el 43 y que se utiliza para especificar información de encaminamiento, como 
listas de nodos, aunque su uso está actualmente muy restringido por razones de seguridad. 
En el campo Next Header de esa cabecera de Routing se indica ya que a continuación van los datos de 
TCP.

---

### Página 54

Modelo ISO/OSI, TCP/IP. Protocolos 
54 
En un tercer ejemplo se ha insertado una cabecera más. En este caso es una cabecera de Extensión de 
Fragmento, cuyo código es el 44. 
Como se puede ver los campos Next Header de las distintas cabeceras mantienen la lógica explicada. 
Podemos enumerar ya algunas cuestiones generales relativas a las cabeceras de Extensión: 
• En un paquete IPv6 puede haber cero, una o más cabeceras de Extensión. 
• Estas cabeceras se sitúan entre la cabecera IPv6 y la cabecera del protocolo de la capa superior 
(capa de transporte). 
• Las cabeceras existentes deben ser procesadas en el orden exacto en que aparecen en la 
cabecera del paquete. 
• Cada cabecera de Extensión es identificada por el campo "Next Header" de la cabecera 
precedente. 
• Las cabeceras de Extensión son examinadas o procesadas únicamente por los nodos a los que 
están destinadas, normalmente el nodo destino de la cabecera IPv6... 
.. con una única excepción: 
Si la cabecera de Extensión es del tipo Opciones Hop-by-Hop, la información que lleva debe ser 
examinada y procesada por cada uno de los nodos que se encuentran en la ruta del paquete. 
• Este tipo de cabecera debe seguir inmediatamente a la cabecera IPv6 y su valor de "Next 
Header" es 0. 
• Si en el campo "Dirección de destino" hay una dirección multicast, las cabeceras de Extensión 
que así lo requieran serán examinadas y procesadas por los nodos que pertenezcan al grupo 
multicast. 
• La longitud de cada cabecera de Extensión es un múltiplo de 8 bytes de forma que, 
independientemente del número de ellas que se utilicen, siempre quedan alineadas. 
2.3.1.1. Tipos de cabecera 
Los 6 tipos de cabeceras de Extensión que se definen en la RFC 8200 (que sustituye y deja obsoleta a la 
RFC 2460) son: 
• De opción Hop-by-Hop (RFC 2460). 
La información de esta cabecera debe ser examinada Salto-a-Salto, es decir, en cada uno de los 
nodos de la ruta que ha de seguir el paquete. 
• De enrutado (RFC 2460). 
Se utiliza para incluir información de enrutamiento. El Routing Header de tipo 0 (RH0) fue 
declarado obsoleto por motivos de seguridad, y su uso está actualmente restringido

---

### Página 55

Modelo ISO/OSI, TCP/IP. Protocolos 
55 
• De fragmento (RFC 2460). 
Un host IPv6 que quiere enviar un paquete a un destino IPv6 utiliza el llamado "Path MTU 
discovery" para determinar el tamaño máximo de paquete que se puede utilizar en el path hasta 
ese destino. Si el paquete que hay que enviar es más grande que el MTU soportado, el host 
origen fragmenta el paquete. Gracias a esta forma de actuar, la fragmentación se gestiona de 
extremo a extremo, liberando a los routers del path de este trabajo. 
En caso de que el "Path MTU discovery" falle, se usará el valor mínimo de "Path MTU" en IPv6, 
1280 bytes. El tamaño máximo de un paquete IPv6 es de 65.535 bytes, y el campo Payload 
Length no incluye los 40 bytes de la cabecera IPv6. 
• De opciones de destino (RFC 2460). 
Estas cabeceras llevan información que será procesada, exclusivamente, por el nodo de destino. 
• De autenticación (AH) (RFC 4302). 
Proporciona integridad y autenticación (que no confidencialidad) para todos los paquetes de 
datos IP. Soporta distintos mecanismos de autenticación. 
• De carga útil de seguridad encapsulada(Encapsulating Security Payload –ESP) (RFC 4303) 
Proporciona confidencialidad, integridad y autenticación de origen de los datos, además de 
otras funciones de seguridad para los paquetes IP. 
La flexibilidad de esta arquitectura permitirá el desarrollo de nuevas cabeceras de Extensión en el 
futuro, a medida que sean necesarias. Lo bueno de este sistema es que las nuevas cabeceras de 
Extensión se pueden definir y usar sin cambiar la cabecera IPv6. 
Orden de ejecución de los tipos de cabecera 
Si se le pide a un nodo que procese la siguiente cabecera, pero no identifica el valor del campo "Next 
Header", descartará el paquete y enviará un mensaje "ICMPv6 Parameter Problem" al equipo origen del 
paquete. 
Según la RFC 8200, si en un paquete se usa más de una cabecera de Extensión, se debería respetar el 
siguiente orden: 
• Cabecera IPv6. 
• Cabecera de Opciones Hop-by-Hop. 
• Cabecera de opciones de destino (para opciones que tienen que ser procesadas por el primer 
destino que aparece en el campo de dirección de destino, además de los destinos posteriores 
enumerados en la cabecera de Routing). 
• Cabecera de enrutamiento (Routing). 
• Cabecera de Fragmento.

---

### Página 56

Modelo ISO/OSI, TCP/IP. Protocolos 
56 
• Cabecera de autenticación (Authentication header). 
• Cabecera de carga útil de seguridad encapsulada (Encapsulating Security Payload). 
• Cabecera de Opciones de Destino (para opciones a ser procesadas solo por el destino final del 
paquete). 
• Cabecera de capa superior. 
Cuando se encapsula IPv6 en IPv4, la cabecera de capa superior puede ser otra cabecera IPv6 y puede 
contener cabeceras de Extensión que tienen que seguir las reglas mencionadas. 
2.4. Asignaciones geográficas de direcciones IP (RIR) 
Los Registros Regionales de Internet (RIR, por sus siglas en inglés Regional Internet Registry) son 
organizaciones internacionales, sin fines de lucro, que se encargan de asignar el espacio de direcciones 
de Protocolo de Internet (IP), tanto IPv4 como IPv6, y los Números de Sistema Autónomo dentro de 
una región geográfica. 
 
 
 
 
Conclusiones 
Los RIR son organizaciones que asignan direcciones por zonas 
geográficas. 
 
 
El vertiginoso crecimiento de Internet y la consiguiente demanda de direcciones IP durante la década de 
los 90, provocó la aparición de los Registros Regionales de Internet. La creación de los RIR fue 
impulsada por la necesidad de descentralizar la administración de estos recursos de direcciones IP, que 
inicialmente eran gestionados de forma centralizada por la IANA (Internet Assigned Numbers 
Authority: Autoridad de Números Asignados para Internet), función que actualmente coordina en 
colaboración con los RIR bajo el marco de la ICANN (Corporación de Internet para la Asignación de 
Nombres y Números). 
Hoy en día, administrar el espacio para las direcciones de Internet implica la cooperación y 
comunicación entre los cinco RIR, los cuales comparten una responsabilidad global por medio de IANA. 
Durante la última década, la gestión del espacio de direcciones de Internet se ha mantenido como un 
sistema distribuido y coordinado, basado en la cooperación entre IANA y los cinco RIR. 
Existen cinco RIR que representan diferentes regiones, los cuales son: 
• ARIN, se estableció en 1997 y es la RIR responsable de asignar las direcciones IP para la región 
de Norteamérica, Canadá, Estados Unidos y también para una parte del Caribe.

---

### Página 57

Modelo ISO/OSI, TCP/IP. Protocolos 
57 
• RIPE NCC, establecido en 1992, es el Registro Regional de Internet responsable de la asignación 
y gestión de direcciones IP (IPv4 e IPv6) y Números de Sistema Autónomo para las regiones de 
Europa, Oriente Medio y Asia Central. 
Su denominación proviene del acrónimo Réseaux IP Européens Network Coordination Centre, 
reflejo de su origen histórico vinculado inicialmente al ámbito europeo. 
• APNIC, se estableció en 1993 y es el RIR responsable de asignar las direcciones IP para la región 
de Asia-Pacífico, incluyendo Asia, Oceanía y Australia. 
• LACNIC, se estableció en 2001 y es el RIR responsable de asignar las direcciones IP para la 
región de Latinoamérica y para las áreas del Caribe que ARIN no cubre. 
• AFRINIC entró en funcionamiento en el 2005 y es el RIR responsable de asignar las direcciones 
IP para el continente africano. 
3. Modelo TCP/IP 
TCP/IP lo desarrolló la Agencia de Defensa de Proyectos Avanzados de Investigación (DARPA) a 
petición del Departamento de Defensa de Estados Unidos. 
Dicho departamento necesitaba un conjunto de protocolos que pudieran utilizarse en cualquier sistema 
operativo, ya que no existía uniformidad alguna entre los sistemas informáticos de sus oficinas. 
Evolucionó de ARPANET, la cual fue la primera red de área amplia. 
El modelo TCP/IP se denomina a veces como Modelo Internet, Modelo DoD o Modelo Darpa. 
TCP/IP se ha convertido en el estándar rápidamente para la conexión en red corporativa. 
Las redes TCP/IP son ampliamente escalables, por lo que TCP/IP puede utilizarse tanto para redes 
pequeñas como grandes. 
TCP/IP es un conjunto de protocolos que pueden ejecutarse en distintas plataformas de software y casi 
todos los sistemas operativos de red lo soportan como protocolo de red predeterminado. 
TCP/IP consta de una serie de protocolos que componen la pila TCP/IP. 
Puesto que el conjunto de protocolos TCP/IP se desarrolló antes de que terminara de desarrollarse el 
modelo de referencia OSI, los protocolos que lo conforman no se corresponden perfectamente con las 
distintas capas del modelo. 
Protocolos de usuario y de soporte 
Los protocolos del modelo TCP/IP se distribuyen en distintas capas, cada una de las cuales cumple una 
función específica dentro del proceso de comunicación.

---

### Página 58

Modelo ISO/OSI, TCP/IP. Protocolos 
58 
Los protocolos de la capa de aplicación, como HTTP, FTP, SMTP o Telnet (a menudo denominados en 
manuales como protocolos de usuario), son los únicos directamente visibles e interactivos para el 
usuario. 
Por el contrario, los protocolos de las capas inferiores actúan de forma transparente. Estos protocolos 
de soporte -como TCP y UDP en la capa de transporte, IP e ICMP en la capa de Internet, y ARP en la 
capa de acceso a la red- son esenciales para el transporte confiable o no confiable de los datos, el 
direccionamiento lógico, la resolución de direcciones físicas y el control de la comunicación a través de 
la red. 
Esta distinción es clave para entender cómo se comunican los sistemas en una red y cómo se organiza el 
modelo TCP/IP por capas. 
3.1. Funciones de las capas del modelo TCP/IP 
Cada una de las capas del modelo TCP/IP cumple unas funciones. 
Cada una de las cuatro capas cumple una determinada función. 
3.1.1. Capa de interfaz de Red (Nivel 1) 
También conocida como CAPA FISICA o CAPA DE ACCESO AL MEDIO, (Estaría relacionada con las 
capas 1 y 2 del modelo OSI). 
Es el punto de interacción o interfaz entre la red local y los protocolos TCP/IP. 
Es la responsable de aceptar paquetes IP y realizar su transmisión sobre una red específica. 
El emisor debe proporcionar a la red la dirección del destino para que pueda encaminar (enrutar) los 
datos hasta el destino apropiado. 
El emisor puede requerir ciertos servicios que pueden ser proporcionados por el nivel de red (como 
solicitar una determinada prioridad). 
El software de comunicaciones situado por encima de la capa de acceso a la red no tendrá que 
preocuparse de los detalles específicos de la red a utilizar. Funcionará con independencia de la red. 
3.1.2. Capa de Internet (Nivel 2) 
También conocida como CAPA de RED al estar directamente relacionada con la capa 3 (capa de red) 
del modelo OSI.

---

### Página 59

Modelo ISO/OSI, TCP/IP. Protocolos 
59 
Para sistemas finales conectados a la misma red, la capa de acceso a la red se encarga del acceso y 
encaminamiento de los datos. 
Si los dos dispositivos están conectados a redes diferentes se necesitarán una serie de procedimientos 
que permitan que los datos atraviesen redes distintas interconectadas. Esta es la función que desarrolla 
la capa de internet. 
Se encarga de ofrecer servicios de: 
• Direccionamiento lógico. 
• Enrutamiento. 
• Fragmentación. 
• Reenvío. 
• Etc. 
Al igual que la capa 3 del modelo OSI, recibe la petición de enviar un segmento de la capa de transporte 
y una dirección de destino para el paquete. 
3.1.3. Capa de Transporte (Nivel 3) 
Está relacionada con la capa 4 del modelo OSI. 
La capa de transporte realiza las siguientes funciones: 
• Proporciona los siguientes servicios: 
• Comunicación confiable de extremo a extremo. 
• Comunicación sin garantía de entrega. 
• Segmentación y ordenación de datos. 
• Multiplexación de conexiones simultáneas. 
• Define como dos entidades de aplicación realizan una conversación sobre el protocolo IP. 
• Realiza detección/corrección de errores. 
• Realiza control de flujo. 
• Identifica la aplicación específica de origen y destino. 
Define 2 protocolos principales: 
• TCP (Transmission Control Protocol): 
• Es un protocolo confiable. 
• Orientado a la conexión.

---

### Página 60

Modelo ISO/OSI, TCP/IP. Protocolos 
60 
• Permite que un flujo de bytes sea entregado a la máquina destino sin errores y en correcto 
orden. 
• Realiza fragmentación de los mensajes. 
• Realiza control de flujo. 
• UDP (User datagram protocol): 
• Protocolo no confiable. 
• No orientado a la conexión. 
• Permite mejores tiempos de respuesta. 
3.1.4. Capa de Aplicación (Nivel 4) 
Representa la consolidación de las capas 5 (Sesión), 6 (Presentación) y 7 (Aplicación) del modelo OSI 
en una única capa. Esto elimina los límites difusos entre ellas y contiene la lógica específica necesaria 
para cada aplicación de usuario. 
3.2. Protocolos TCP/IP 
Se llama familia de protocolos TCP/IP a la amplia colección de protocolos que se han especificado como 
estándares de internet por parte del I.A.B. (Internet Architecture Board). 
A continuación, vemos un gráfico con los principales protocolos del modelo TCP/IP.

---

### Página 61

Modelo ISO/OSI, TCP/IP. Protocolos 
61 
3.2.1. Capa de Interfaz de red 
Comprende a la Capa de acceso a datos y a la capa física. 
Los principales protocolos son: 
• Protocolo ARP. 
El Address Resolution Protocol o Protocolo de Resolución de Direcciones hace corresponder las 
direcciones IP con las direcciones MAC de hardware. 
• Protocolo NDP. 
Neighbor Discovery Protocol (NDP) es un protocolo de IPv6, y es equivalente al protocolo 
Address Resolution Protocol (ARP) en IPv4, aunque se distingue porque también incorpora 
funcionalidades de ICMP. 
Utiliza mensajes especiales de ICMPv6 construyendo así una manera simple para que los 
terminales aprendan las direcciones IPv6 de los vecinos de la capa de enlace. 
Consiste en un mecanismo con el cual un nodo que se acaba de conectar a la red descubre la 
presencia de otros nodos en el mismo enlace, además de ver sus direcciones IP. 
• Protocolo Ethernet. 
Es un estándar de redes de área local para computadores con acceso al medio por detección de 
la onda portadora y con detección de colisiones (CSMA/CD). 
Define las características de cableado y señalización de nivel físico y los formatos de tramas de 
datos del nivel de enlace de datos del modelo OSI. 
Ethernet se tomó como base para la redacción del estándar internacional IEEE 802.3, siendo 
usualmente tomados como sinónimos. 
Se diferencian en uno de los campos de la trama de datos. Sin embargo, las tramas Ethernet y 
IEEE 802.3 pueden coexistir en la misma red. 
3.2.2. Capa de Internet 
Los principales protocolos son: 
• ICMP. 
• IPSEC. 
• IGM.

---

### Página 62

Modelo ISO/OSI, TCP/IP. Protocolos 
62 
3.2.2.1. Protocolo ICMP 
El 'Protocolo de Mensajes de Control de Internet' o ICMP es el sub-protocolo de control y notificación 
de errores del Protocolo de Internet. 
Como tal, se usa para enviar mensajes de error, indicando por ejemplo que un enrutador o host no 
puede ser localizado. 
3.2.2.2. Protocolo IPSEC 
IPsec (Internet Protocol security) es un conjunto de protocolos cuya función es asegurar las 
comunicaciones sobre el Protocolo de Internet (IP) autenticando y/o cifrando cada paquete IP en un 
flujo de datos. 
Los protocolos de IPsec actúan en la capa de red, la capa 3 del modelo OSI. Otros protocolos de 
seguridad para Internet de uso extendido, como SSL, TLS y SSH operan de la capa de aplicación (capa 7 
del modelo OSI). 
Esto hace que IPsec sea más flexible, ya que puede ser utilizado para proteger protocolos de la capa 4, 
incluyendo TCP y UDP. 
Vamos a ver características de IPsec: 
• Propósito de diseño: fue proyectado para proporcionar seguridad en modo transporte 
(extremo a extremo) del tráfico de paquetes, en el que los ordenadores de los extremos finales 
realizan el procesado de seguridad, o en modo túnel (puerta a puerta) en el que la seguridad del 
tráfico de paquetes es proporcionada a varias máquinas (incluso a toda la red de área local) por 
un único nodo. 
• Puede utilizarse para crear VPNs en los dos modos, y este es su uso principal. Hay que tener en 
cuenta, sin embargo, que las implicaciones de seguridad son bastante diferentes entre los dos 
modos de operación. 
• La seguridad de comunicaciones extremo a extremo a escala Internet se ha desarrollado más 
lentamente de lo esperado. Parte de la razón a esto es que no ha surgido infraestructura de 
clave pública universal o universalmente de confianza (DNSSEC fue originalmente previsto para 
esto); otra parte es que muchos usuarios no comprenden lo suficientemente bien ni sus 
necesidades ni las opciones disponibles como para promover su inclusión en los productos de los 
vendedores. 
• Como el Protocolo de Internet no provee intrínsecamente de ninguna capacidad de seguridad, 
IPsec se introdujo para proporcionar servicios de seguridad tales como: 
• Cifrar el tráfico (de forma que no pueda ser leído por nadie más que las partes a las que está 
dirigido). 
• Validación de integridad (asegurar que el tráfico no ha sido modificado a lo largo de su 
trayecto).

---

### Página 63

Modelo ISO/OSI, TCP/IP. Protocolos 
63 
• Autenticar a los extremos (asegurar que el tráfico proviene de un extremo de confianza). 
• Anti-repetición (proteger contra la repetición de la sesión segura). 
3.2.2.2.1. Modos de IPsec 
Así pues y dependiendo del nivel sobre el que se actúe, podemos establecer dos modos básicos de 
operación de IPsec: modo transporte y modo túnel. 
• Modo transporte. 
En modo transporte, sólo la carga útil (los datos que se transfieren) del paquete IP es cifrada o 
autenticada. El enrutamiento permanece intacto, ya que no se modifica ni se cifra la cabecera IP; 
sin embargo, cuando se utiliza la cabecera de autenticación (AH), las direcciones IP no pueden 
ser traducidas, ya que eso invalidaría el hash. Las capas de transporte y aplicación están siempre 
aseguradas por un hash, de forma que no pueden ser modificadas de ninguna manera (por 
ejemplo, traduciendo los números de puerto TCP y UDP). El modo transporte se utiliza para 
comunicaciones ordenador a ordenador. 
Una forma de encapsular mensajes IPsec para atravesar NAT ha sido definido por RFCs que 
describen el mecanismo de NAT transversal. 
• Modo túnel. 
En el modo túnel, todo el paquete IP (datos más cabeceras del mensaje) es cifrado o 
autenticado. Debe ser entonces encapsulado en un nuevo paquete IP para que funcione el 
enrutamiento. El modo túnel se utiliza para comunicaciones red a red (túneles seguros entre 
routers, p.e. para VPNs) o comunicaciones ordenador a red u ordenador a ordenador sobre 
Internet. 
3.2.2.2.2. Los 3 Protocolos que forman IPsec 
IPsec consta de 3 protocolos, que han sido desarrollados para proporcionar seguridad a nivel de 
paquete, tanto para IPv4 como para IPv6: 
1. Authentication Header (AH) proporciona integridad, autenticación y no repudio si se eligen los 
algoritmos criptográficos apropiados. 
2. Encapsulating Security Payload (ESP) proporciona confidencialidad y la opción -altamente 
recomendable- de autenticación y protección de integridad. 
3. Internet key exchange (IKE) emplea un intercambio secreto de claves de tipo Diffie-Hellman 
para establecer el secreto compartido de la sesión. Se suelen usar sistemas de Criptografía de 
clave pública o clave pre-compartida. 
Los algoritmos criptográficos definidos para usar con IPsec incluyen HMAC- SHA-1 para 
protección de integridad, y Triple DES-CBC y AES-CBC para confidencialidad. Más detalles en la 
RFC 4305.

---

### Página 64

Modelo ISO/OSI, TCP/IP. Protocolos 
64 
1. Authentication Header (AH) 
AH está dirigido a garantizar integridad, sin conexión y autenticación de los datos de origen de los 
datagramas IP. 
Para ello, calcula un Hash Message Authentication Code (HMAC) a través de algún algoritmo hash 
operando sobre una clave secreta, el contenido del paquete IP y las partes inmutables del datagrama. 
Este proceso restringe la posibilidad de emplear NAT, que puede ser implementada con NAT transversal. 
Por otro lado, AH puede proteger opcionalmente contra ataques de repetición utilizando la técnica de 
ventana deslizante y descartando paquetes viejos. 
AH protege la carga útil IP y todos los campos de la cabecera de un datagrama IP excepto los campos 
mutantes, es decir, aquellos que pueden ser alterados en el tránsito. 
En IPv4, los campos de la cabecera IP mutantes (y por lo tanto no autenticados) incluyen TOS, Flags, 
Offset de fragmentos, TTL y suma de verificación de la cabecera. AH opera directamente por encima 
de IP, utilizando el protocolo IP número 51. 
Una cabecera AH mide 32 bits, se organiza de la siguiente forma: 
0 - 7 bit 
8 - 15 bit 
16 - 23 bit 
24 - 31 bit 
Next header 
Payload length 
RESERVED 
Security parameters index (SPI) 
Sequence number 
Hash Message Authentication Code (variable) 
Vamos a explicar el significado de los campos (de esta cabecera AH). 
• Next header. 
Identifica el protocolo de los datos transferidos. 
• Payload length. 
Tamaño del paquete AH. 
• RESERVED. 
Reservado para uso futuro (hasta entonces todo ceros).

---

### Página 65

Modelo ISO/OSI, TCP/IP. Protocolos 
65 
• Security parameters index (SPI). 
Indica los parámetros de seguridad que, en combinación con la dirección IP, identifican la 
asociación de seguridad implementada con este paquete. 
• Sequence number. 
Un número siempre creciente, utilizado para evitar ataques de repetición. 
• HMAC. 
Contiene el valor de verificación de integridad (ICV) necesario para autenticar el paquete; 
puede contener relleno. 
2. Los Encapsulating Security Payload (ESP) 
El protocolo ESP proporciona autenticidad de origen, integridad y protección de confidencialidad de un 
paquete. 
ESP también soporta configuraciones de sólo cifrado y sólo autenticación, pero utilizar cifrado sin 
autenticación está altamente desaconsejado porque es inseguro. 
Al contrario que con AH, la cabecera del paquete IP no está protegida por ESP (aunque en ESP en modo 
túnel, la protección es proporcionada a todo el paquete IP interno, incluyendo la cabecera interna; la 
cabecera externa permanece sin proteger). 
ESP opera directamente sobre IP, utilizando el protocolo IP número 50. 
Un diagrama de paquete ESP: 
 
Fuente: Wilkipedia

---

### Página 66

Modelo ISO/OSI, TCP/IP. Protocolos 
66 
Significado de los campos: 
• Security parameters index (SPI). 
Identifica los parámetros de seguridad en combinación con la dirección IP. 
• Sequence number. 
Un número siempre creciente, utilizado para evitar ataques de repetición. 
• Payload data. 
Los datos a transferir. 
• Padding. 
Usado por algunos algoritmos criptográficos para rellenar por completo los bloques. 
• Pad length. 
Tamaño del relleno en bytes. 
• Next header. 
Identifica el protocolo de los datos transferidos. 
• Authentication data. 
Contiene los datos utilizados para autenticar el paquete. 
3. Internet key exchange (IKE) 
Los IPsec también incluye protocolos para el establecimiento de claves de cifrado. 
• IKE Internet Key Exchange, es un protocolo usado para establecer una Asociación de Seguridad 
(SA). IKE emplea un intercambio secreto de claves de tipo Diffie-Hellman para establecer el 
secreto compartido de la sesión. Se suelen usar sistemas de clave pública o clave pre-
compartida. 
Supone una alternativa al intercambio manual de claves. Su objetivo es la negociación de una 
Asociación de Seguridad para IPSEC. Permite, además, especificar el tiempo de vida de la sesión 
IPSEC, autenticación dinámica de otras máquinas, etc.

---

### Página 67

Modelo ISO/OSI, TCP/IP. Protocolos 
67 
• IKEv2 Internet Key Exchange versión 2, es la siguiente versión del protocolo Internet Key 
Exchange que se utiliza para negociar una Asociación de Seguridad al principio de una sesión. 
IKEv2 utiliza mecanismos para proteger criptográficamente sus propios paquetes muy similares 
a los que se emplean para proteger el contenido de los paquetes IP en la pila IPsec 
(Encapsulating Security Payload - ESP). 
Esto conduce a implementaciones más simples y también probablemente certificaciones más 
sencillas. 
3.2.2.3. Protocolo IGMP 
El protocolo de red IGMP (Internet Group Management Protocol) se utiliza para intercambiar 
información acerca del estado de pertenencia entre enrutadores IP que admiten la multidifusión y 
miembros de grupos de multidifusión. 
3.2.3. Capa de transporte 
Proporciona comunicación directa entre aplicaciones que se ejecutan en hosts diferentes, manejando la 
segmentación, el control de flujo, la fiabilidad y el control de congestión. Los principales protocolos son: 
Los principales protocolos son: 
• TCP. 
El Protocolo de Control de Transmisión (Transmission Control Protocol, TCP) es un estándar 
esencial en las redes de computadoras y forma parte de la capa de transporte del modelo 
TCP/IP. Se caracteriza por ser un protocolo orientado a la conexión, lo que implica que, antes 
de intercambiar datos, establece un canal de comunicación fiable mediante el mecanismo 
conocido como three-way handshake (SYN → SYN-ACK → ACK). Este proceso garantiza que 
tanto el emisor como el receptor estén sincronizados y preparados para la transmisión de datos. 
TCP está diseñado para ofrecer una entrega fiable, ordenada y libre de errores. Para lograrlo, 
emplea mecanismos como las confirmaciones de recepción (ACK), la retransmisión automática 
en caso de pérdida de paquetes y la numeración de secuencia, que asegura que los datos lleguen 
en el orden correcto. Además, incorpora control de flujo, que evita la saturación del receptor, y 
control de congestión, que adapta la velocidad de transmisión en función de las condiciones de 
la red. 
Gracias a su robustez y a su capacidad para garantizar la integridad de la información, TCP es 
ampliamente utilizado en aplicaciones críticas como la navegación web (HTTP/HTTPS), el 
envío de correos electrónicos (SMTP, IMAP, POP3) o la transferencia de archivos (FTP). Su 
diseño lo convierte en la opción preferida cuando la fiabilidad y la precisión de los datos son más 
importantes que la velocidad.

---

### Página 68

Modelo ISO/OSI, TCP/IP. Protocolos 
68 
• UDP. 
El Protocolo de Datagramas de Usuario (UDP) es un protocolo de transporte del modelo 
TCP/IP diseñado para transmisiones rápidas y ligeras. A diferencia de TCP, no establece 
conexiones previas (es no orientado a la conexión), lo que elimina la sobrecarga del handshake 
inicial y reduce la latencia. 
Cada datagrama UDP incluye en su cabecera las direcciones IP y puertos necesarios para el 
enrutamiento, junto con una suma de verificación básica. Sin embargo, no garantiza la entrega, 
el orden ni la integridad de los datos, ya que carece de: 
• Confirmaciones de recepción (ACKs). 
• Retransmisiones automáticas. 
• Control de flujo o congestión. 
Esta simplicidad lo hace ideal para aplicaciones donde la velocidad prima sobre la fiabilidad, 
como: 
• Streaming (YouTube, Twitch). 
• Videollamadas (Zoom, Skype). 
• Juegos online. 
• Consultas DNS. 
Al ser un protocolo "best-effort", delega el manejo de errores en las aplicaciones, siendo 
perfecto para escenarios donde una pérdida ocasional de paquetes es preferible a los retrasos. 
• DCCP (Datagram Congestion Control Protocol). 
Protocolo de nivel de transporte orientado a mensajes, diseñado para aplicaciones que 
necesitan control de congestión (como el streaming multimedia) pero no requieren la fiabilidad 
estricta de TCP. Proporciona un servicio de datagramas con negociación de características y 
control de congestión, siendo útil para tráfico en tiempo real que puede tolerar cierta pérdida de 
paquetes. 
• uTP (Micro Transport Protocol o µTP). 
Micro Transport Protocol (uTP) es un protocolo libre multiplataforma diseñado para ser usado 
en las conexiones P2P del protocolo BitTorrent. 
Está implementado sobre el protocolo UDP, como alternativa a TCP para la transferencia de 
datos. 
Se encuentra bajo la licencia MIT.

---

### Página 69

Modelo ISO/OSI, TCP/IP. Protocolos 
69 
uTP fue diseñado para evitar latencias, pero aprovechando el ancho de banda cuando la latencia 
no es excesiva. 
Esto significa que BitTorrent no saturaría la conexión a Internet, aunque no exista un límite de 
descarga. 
3.2.4. Capa de aplicación 
Los principales protocolos son: 
• SSH. 
SSH o Secure SHell es un protocolo que facilita las comunicaciones seguras entre dos sistemas 
usando una arquitectura cliente/servidor y que permite a los usuarios conectarse a un host 
remotamente. 
A diferencia de otros protocolos de comunicación remota tales como FTP o Telnet, SSH 
encripta la sesión de conexión, haciendo imposible que alguien pueda obtener contraseñas no 
encriptadas. 
• FTP. 
El Protocolo de transferencia de archivos (File Transfer Protocol o FTP) es un protocolo de red 
para la transferencia de archivos entre sistemas conectados a una red TCP, basado en la 
arquitectura cliente-servidor. 
Desde un equipo cliente se puede conectar a un servidor para descargar archivos desde él o para 
e9nviarle archivos, independientemente del sistema operativo utilizado en cada equipo. 
• FTPS. 
Es una extensión de FTP que añade el cifrado de comunicaciones gracias a SSL/TLS. 
Implementa asimismo el uso de certificado digital, autenticación con usuario y contraseña o 
ambas cosas. 
Puede trabajar de manera implícita con el uso del cifrado desde el inicio de la conexión, en el 
puerto por defecto 990, o por lo contrario usar modo explícito que se servirá del puerto 21 y 
negociará el cifrado tras la conexión. Existen en FTPS más puertos suplementarios para la 
transferencia de datos. Pese a tener un alto grado de compatibilidad gran variedad de 
herramientas FTP no tiene comandos estandarizados para listar atributos avanzados o 
manipular directorios. 
• SFTP. 
No es una extensión, como en el caso anterior de FTP sino que se basa en SSH, protocolo de 
comunicación segura que suele usar el puerto 22. A diferencia FTPS usa un solo puerto para 
todas sus comunicaciones facilitando su uso en entornos de red más restringidos. Usa el cifrado 
implícito desde el principio de la comunicación. En lo que sí coincide con FTPS admite la

---

### Página 70

Modelo ISO/OSI, TCP/IP. Protocolos 
70 
autenticación basada en contraseñas, claves públicas o la combinación de ambas. Garantiza 
integridad y confidencialidad de los datos gracias a SSH. Tiene comandos de manipulación de 
sistemas de archivos, mover, eliminar o cambiar permisos de estos. 
• SMTP. 
El protocolo para transferencia simple de correo (SMTP o Simple Mail Transfer Protocol) es un 
protocolo de red utilizado para el intercambio de mensajes de correo electrónico entre 
computadoras u otros dispositivos. 
Su tarea principal es enviar correo (tiene limitaciones para la recepción). 
• DHCP. 
El protocolo de configuración dinámica de host (Dynamic Host Configuration Protocol o DHCP) 
es un protocolo de red de tipo cliente/servidor mediante el cual un servidor DHCP asigna 
dinámicamente una dirección IP y otros parámetros de configuración de red a cada dispositivo 
en una red para que puedan comunicarse con otras redes IP. 
Este servidor posee una lista de direcciones IP dinámicas y las va asignando a los clientes 
conforme éstas van quedando libres, sabiendo en todo momento quién ha estado en posesión 
de esa IP, cuánto tiempo la ha tenido y a quién se la ha asignado después. 
De esta forma, los clientes de una red IP pueden conseguir sus parámetros de configuración 
automáticamente. 
• DNS. 
Las DNS (Domain Name System o Sistema de Nombres de Dominio) se utiliza para traducir la 
dirección real (IP) en el nombre del dominio y viceversa. 
• RIP. 
El Protocolo de Información de Encaminamiento (Routing Information Protocol o RIP) es un 
protocolo de puerta de enlace interna (Interior Gateway Protocol, IGP) utilizado por los 
enrutadores para intercambiar información acerca de redes IP a las que se encuentran 
conectados. 
Su algoritmo de encaminamiento está basado en el vector de distancia, ya que calcula la métrica 
o ruta más corta posible hasta el destino a partir del número de "saltos" o equipos intermedios 
que los paquetes IP deben atravesar. 
Este algoritmo usa el método Split Horizon (Horizonte dividido) para evitar los loops de 
enrutamiento, prohíbe a un router publicar una ruta por la misma interfaz por la que se aprendió 
en primer lugar.

---

### Página 71

Modelo ISO/OSI, TCP/IP. Protocolos 
71 
• SNMP. 
El Protocolo simple de administración de red (SNMP o Simple Network Management Protocol) 
es un protocolo de la capa de aplicación que facilita el intercambio de información de 
administración entre dispositivos de red. 
• HTTP. 
El Protocolo de transferencia de hipertexto (HTTP o Hypertext Transfer Protocol) es el protocolo 
de comunicación que permite las transferencias de información en la World Wide Web. 
Define la sintaxis y la semántica que utilizan los elementos de software de la arquitectura web 
(clientes, servidores, proxis) para comunicarse. 
HTTP es un protocolo sin estado, es decir, no guarda ninguna información sobre conexiones 
anteriores. 
El desarrollo de aplicaciones web necesita frecuentemente mantener estado. Para esto se usan 
las cookies, que es información que un servidor puede almacenar en el sistema cliente. 
• TELNET. 
Telnet (Teletype Network) es el nombre de un protocolo de red que nos permite acceder a otra 
máquina para manejarla remotamente como si estuviéramos sentados delante de ella. 
También es el nombre del programa informático que implementa el cliente. 
Para que la conexión funcione, como en todos los servicios de Internet, la máquina a la que se 
acceda debe tener un programa especial que reciba y gestione las conexiones. El puerto que se 
utiliza generalmente es el 23. 
• L2TP 
Es un protocolo de túnel utilizado por redes privadas virtuales (VPN), diseñado por un grupo de 
trabajo del IETF para corregir las deficiencias de los protocolos PPTP y L2F. Se ha establecido 
como un estándar aprobado por el IETF (RFC 2661). 
Funcionamiento: L2TP utiliza PPP para emular un enlace de acceso de capa 2, el cual es dirigido 
a través de un túnel sobre una red IP (como Internet) hasta un punto determinado. Define su 
propio protocolo para el establecimiento y gestión de túneles. 
Ubicación en el modelo TCP/IP: Aunque su función es transportar tramas de nivel de enlace 
(capa 2), en la arquitectura del modelo TCP/IP de 4 capas, L2TP se implementa en la capa de 
aplicación. Esto se debe a que se encapsula sobre el protocolo de transporte UDP (puerto 1701) 
para su transmisión a través de la red. Es, por tanto, una aplicación que proporciona servicios de 
tunelización a otros componentes del sistema. 
Transporte: El diseño de L2TP permite su transporte sobre una gran variedad de tecnologías de 
red de paquetes, incluyendo IP, X.25, Frame Relay y ATM.

---

### Página 72

Modelo ISO/OSI, TCP/IP. Protocolos 
72 
3.3. Funcionamiento del modelo TCP/IP 
 
PDUs (Protocol Data Unit o unidades de datos de protocolo) del modelo TCP/IP 
El funcionamiento es bastante complejo, pero vamos a definirlo someramente para darte una idea 
general. 
IP no está orientado a la conexión. Está basado en la idea de transportar datagramas por internet de 
forma transparente, pero sin seguridad. 
Puede viajar por varias redes hasta llegar al receptor. Incluso puede que los datagramas viajen por redes 
distintas. 
3.3.1. Proceso de Comunicación en la Pila TCP/IP 
En el Host Emisor: 
1. Capa de Aplicación: La aplicación genera los datos (por ejemplo, un archivo o un mensaje de 
correo) y los entrega a la capa de transporte. 
2. Capa de Transporte (TCP): 
• TCP toma el bloque de datos de la aplicación. Si es muy grande, lo divide en unidades más 
pequeñas llamadas segmentos.

---

### Página 73

Modelo ISO/OSI, TCP/IP. Protocolos 
73 
• A cada segmento se le añade una cabecera TCP, que contiene información de control 
fundamental como: 
» Puerto de origen y puerto de destino (para identificar la aplicación). 
» Número de secuencia (para ordenar los segmentos). 
» Número de acuse de recibo (ACK) y ventana (para control de flujo y fiabilidad). 
» Suma de verificación (checksum) para detectar errores. 
• TCP pasa cada segmento a la capa de Internet (IP) con las instrucciones para entregarlo. 
3. Capa de Internet (IP): 
• IP toma el segmento TCP y le añade su propia cabecera IP, formando así un paquete IP 
(también llamado datagrama IP). 
• La cabecera IP contiene, entre otros, el campo crítico: la dirección IP lógica del destino final. 
• IP determina, consultando su tabla de enrutamiento, cuál es el siguiente dispositivo al que 
debe enviar el paquete (el "próximo salto" o next-hop), que puede ser el destino final o un 
enrutador en la misma red local. 
• El paquete IP se pasa a la capa de acceso a la red. 
4. Capa de Acceso a la Red (Capa de Enlace + Física): 
• Esta capa encapsula el paquete IP dentro de una trama de red (por ejemplo, una trama 
Ethernet). 
• Añade una cabecera de enlace de datos que contiene la dirección física (MAC) del próximo 
salto (obtenida mediante un protocolo como ARP) y la dirección MAC de la interfaz de 
salida. 
• La trama resultante se transmite a través del medio físico (cable, aire) hacia el dispositivo 
del próximo salto. 
En el Enrutador Intermedio 
5. El enrutador recibe la trama por una de sus interfaces. 
6. Su capa de acceso a la red: 
• Verifica la integridad de la trama (usando la secuencia de verificación, FCS). 
• Elimina la cabecera y terminación de la trama, extrayendo el paquete IP en su interior. 
• Pasa el paquete IP a su capa de Internet (IP).

---

### Página 74

Modelo ISO/OSI, TCP/IP. Protocolos 
74 
7. La capa IP del enrutador: 
• Verifica el checksum de la cabecera IP y decrementa el campo TTL (Tiempo de Vida). Si el 
TTL llega a cero, el paquete se descarta. 
• Examina la dirección IP de destino en la cabecera. 
• Consulta su tabla de enrutamiento para decidir por qué interfaz de salida y hacia qué 
"próximo salto" debe reenviar el paquete para que se acerque a su destino final. 
8. Para el reenvío, el proceso de encapsulación se repite: 
• El paquete IP (con su cabecera original modificada solo en TTL) se pasa a la capa de acceso 
a la red de la interfaz de salida. 
• Esta capa construye una nueva trama con una nueva cabecera de enlace, que ahora 
contendrá las direcciones MAC correspondientes al nuevo segmento de red (la MAC del 
próximo enrutador o del host destino final si está en la misma red). 
• La nueva trama se transmite. 
En el Host Receptor final: 
9. El host destino recibe la trama. 
10. Su capa de acceso a la red verifica la trama, la desencapsula y pasa el paquete IP a la capa IP. 
11. La capa IP verifica el paquete, lo desencapsula y pasa el segmento TCP a la capa de transporte. 
12. La capa de transporte (TCP): 
• Utiliza la información de su cabecera (números de secuencia y puertos) para reensamblar 
los segmentos en el orden correcto. 
• Realiza el control de errores. Si un segmento se pierde o está corrupto (detectado 
mediante el checksum o por falta de ACK), TCP en el receptor solicita su retransmisión al 
emisor. 
• Una vez que todos los segmentos están correctos y en orden, TCP entrega el flujo de datos 
original a la aplicación destino indicada por el puerto de destino. 
Este proceso sería más largo si tuviera que pasar por más de dos subredes, y, por lo tanto, más de 
dos enrutadores. Se repetirían los pasos de 5 al 8 por cada enrutador intermedio a atravesar hasta 
el destino.

---

### Página 75

Modelo ISO/OSI, TCP/IP. Protocolos 
75 
4. Comparación de los modelos OSI y TCP/IP 
(ventajas y desventajas) 
El modelo OSI es un modelo conceptual que no se aplica en la práctica. 
En este se definen: 
• Las funciones de cada capa. 
• Como una capa accede a los servicios de la capa inmediatamente inferior. 
Sin embargo, el modelo TCP/IP es una tecnología muy utilizada, pero conceptualmente fue definida a 
posteriori, es decir, primero se crearon los protocolos y luego el modelo. 
Ventajas de OSI 
• Facilita la comprensión al dividir un problema complejo en partes más simples. 
• Normaliza los componentes de red y permite el desarrollo por parte de diferentes fabricantes. 
• Los cambios en una capa no afectan a las demás, por lo que pueden evolucionar. 
• El aprendizaje es sencillo. 
Ventajas de TCP/IP 
• Fácil de implementar, es decir, cualquier fabricante puede utilizar una pila de protocolos de 
manera que su equipo se comunique con el de cualquier otro fabricante. 
• Fácil de extender, es decir, se le pueden añadir funcionalidades agregando servicios nuevos en la 
capa de aplicación. 
Desventajas de OSI 
• Muchas capas. Se produce reiteración de funciones. 
• No se puede implementar bien. 
• Mala sincronización. Cuando se estableció el estándar los protocolos TCP/IP ya se utilizaban 
ampliamente.

---

### Página 76

Modelo ISO/OSI, TCP/IP. Protocolos 
76 
Desventajas TCP/IP 
• Faltan conceptos. 
• No se define la capa física. 
• Cuando se estandarizó OSI ya llevaban tiempo utilizando los protocolos TCP/IP en el entorno 
académico, por lo que no se pudo crear con respecto al estándar. 
• No distingue con claridad conceptos de servicio, interfaz y protocolo, por lo que el modelo no es 
una buena guía para diseñar redes nuevas con nuevas tecnologías. 
5. Correspondencia ISO/OSI con TCP/IP 
A continuación, vamos a ver de manera gráfica la correlación entre las capas TCP/IP y las capas OSI. 
TCP/IP 
OSI 
4. Aplicación 
7. Aplicación 
6. Presentación 
5. Sesión 
3. Transporte 
4. Transporte 
2. Internet 
3. Red 
1. Acceso a la red 
2. Enlace de datos 
Hardware (TCP/IP no contempla esta capa) 
1. Física 
Correspondencia entre los modelos ISO/OSI y TCP/IP 
Se usan 4 capas que se relacionan con las 6 capas superiores del modelo OSI. El modelo TCP/IP no toma 
en cuenta las funciones de la capa física del modelo OSI. 
La capa "Acceso a la red" es considerada el punto de interfaz entre el conjunto de protocolos TCP/IP y 
el hardware de red. 
 
 
 
 
+ Info 
Algunos autores no establecen una relación exacta entre las capas 
de transporte.

---

### Página 77

Modelo ISO/OSI, TCP/IP. Protocolos 
77 
 
 
 
Indican que algunas de las funciones de la capa de sesión del 
modelo OSI se corresponden con la capa de transporte y otras con 
la de aplicación. 
 
 
Correspondencia entre los modelos ISO/OSI y TCP/IP según algunos autores 
TCP/IP 
OSI 
4. Aplicación 
7. Aplicación 
6. Presentación 
5. Sesión 
3. Transporte 
4. Transporte 
2. Internet 
3. Red 
1. Acceso a la red 
2. Enlace de datos 
Hardware (TCP/IP no contempla esta capa) 
1. Física 
6. Bibliografía 
• Redes de computadoras 5ª edición. Tanenbaum, Wetherall. Editorial Pearson. 
• Forouzan, B. Transmisión de datos y redes de comunicaciones. Editorial MC Graw Hill. 
• http://es.wikipedia.com. 
• http://en.wikipedia.com. 
• https://campusvirtual.univalle.edu.co/moodle/pluginfile.php/56106/mod_resource/content/
0/03_-_Arquitectura_Modelo_de_Referencia _OSI_TCP_IP.pdf. 
• https://docs.oracle.com/cd/E19957-01/820-2981/ipov-10/. 
• https://blyx.com/public/docs/pila_OSI.pdf. 
• https://docplayer.es/11614287-Modelos-tcp-ip-y-osi.html.

---

### Página 78

Modelo ISO/OSI, TCP/IP. Protocolos 
78 
• http://exa.unne.edu.ar/depar/areas/informatica/teleproc/Comunicaciones/Presentaciones_
Proyector/ModeloOSIyTCPIP.pdf. 
• http://www.exa.unicen.edu.ar/catedras/comdat1/material/ElmodeloOSI.pdf. 
• http://5cp1ok2012g5.blogspot.com/2012/06/encapsulacion.html. 
• http://www.tech-faq.com/understanding-data-encapsulation.html. 
• http://exa.unne.edu.ar/depar/areas/informatica/teleproc/Comunicaciones/Presentaciones_
Proyector/ModeloOSIyTCPIP.pdf. 
• https://blyx.com/public/docs/pila_OSI.pdf. 
• http://monicagross.tripod.com/backup/caracterf.html. 
• https://es.ccm.net/contents/267-direccion-ip. 
• http://www.ipv6.es/es-ES/introduccion/Paginas/QueesIPv6.aspx. 
• https://es.wikipedia.org/wiki/M%C3%A1scara_wildcard. 
• https://docs.oracle.com/cd/E19957-01/820-2981/ipv6-overview-7/index.html. 
• https://sites.google.com/site/tknikaipv6/2-direccionamiento/2-1-la-nueva-cabecera. 
• https://docs.oracle.com/cd/E19957-01/820-2981/ipv6-ref-
2/index.html#:~:text=Clase%20de%20tr%C3%A1fico%3A%20campo%20de,encabezado%20de
%20IPv6%2C%20en%20octetos.&text=Direcci%C3%B3n%20de%20origen%3A%20128%20bits. 
• https://es.wikipedia.org/wiki/Cabecera_IP#cite_ref-1. 
• https://es.wikipedia.org/wiki/IPsec#Encapsulating_Security_Payload_(ESP).
