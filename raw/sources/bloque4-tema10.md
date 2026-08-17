---
title: "Bloque 4 - Tema 10: Redes Locales: Tipología, Técnicas de Transmisión, Métodos de Acceso"
type: "source"
tags:
  - oposiciones
  - tai
  - bloque-4
  - tema-10
  - raw-source-extracted
sources:
  - "raw/bloque 4/bloque4,tema10.pdf"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Bloque 4 Tema 10"
  - "bloque4,tema10.pdf"
---

# Bloque 4 - Tema 10: Redes Locales: Tipología, Técnicas de Transmisión, Métodos de Acceso

> **Fuente Original**: `raw/bloque 4/bloque4,tema10.pdf`  
> **Tipo**: Extracción completa de documento PDF  
> **Fecha de Ingesta**: 2026-08-17

---

## Contenido Extraído

### Página 1

Redes Locales. Tipología. 
Técnicas de transmisión. 
Métodos de acceso. Dispositivos 
de interconexión 
DV.TextoHTML(01).Esp.dot     |     UD012126_V07_T01

---

### Página 2

ÍNDICE 
1. Redes locales 
5 
1.1. LAN (alámbrica) 
6 
1.1.1. VLAN 
7 
1.2. WLAN (inalámbrica: wifi) 
8 
1.3. Asignación del canal 
8 
1.4. Tipos de red 
9 
2. Estándar IEEE 802 
9 
3. Topología de red 
12 
3.1. Punto a punto 
13 
3.1.1. Simplex 
14 
3.1.2. Semi-dúplex o Half-duplex 
14 
3.1.3. Full-dúplex o Dúplex 
15 
3.2. Bus 
16 
3.3. Estrella 
18 
3.4. Estrella extendida 
20 
3.5. Anillo 
21 
3.6. Anillo doble 
22 
3.7. Malla 
23 
3.8. Árbol 
25 
3.9. Red celular 
26 
4. Técnicas de transmisión 
27 
4.1. Clasificación según el número de bits transmitidos por ciclo de reloj 
28 
4.1.1. Transmisión Paralela 
28 
4.1.2. Transmisión Serie 
29 
4.1.2.1. Transmisión Asíncrona 
30 
4.1.2.2. Transmisión Síncrona 
31 
4.1.2.3. Transmisión Isócrona 
32

---

### Página 3

4.2. Multiplexación 
33 
4.2.1. FDM 
34 
4.2.2. Wdm 
34 
4.2.3. TDM (Multiplexión por División en el Tiempo) 
35 
4.3. Banda base 
35 
4.4. Modulación 
39 
4.4.1. Tipos de Modulación según el sistema de transmisión 
39 
4.4.2. Perturbaciones en una Transmisión 
40 
4.4.2.1. Ruido 
41 
4.4.2.2. Atenuación 
42 
4.4.2.3. Distorsión de retardo 
43 
4.5. Clasificación según el flujo de datos 
43 
4.5.1. UniCast 
43 
4.5.2. MultiCast 
44 
4.5.3. BroadCast 
45 
4.5.4. AnyCast 
45 
5. Métodos de acceso al medio 
46 
5.1. Clasificación 
47 
5.1.1. Repartición 
47 
5.1.2. Compartición 
48 
5.1.2.1. Contienda 
49 
5.1.2.1.1. Principales protocolos de Contienda dentro del método de compartición 
50 
5.1.2.2. Reserva 
52 
5.1.2.3. Selección 
53 
6. Dispositivos de interconexión 
56 
6.1. Repetidor 
57 
6.2. Concentrador (Hub) 
57 
6.3. Conmutador (Switch) 
59 
6.4. Puente (Bridge) 
60

---

### Página 4

6.5. Enrutador (Router) 
62 
6.5.1. Protocolos de Enrutamiento 
64 
6.6. Compuerta (Gateway) 
69 
7. Power Over Ethernet (POE), POE+ Y POE++ 
69 
8. La globalización 
70 
9. Bibliografía 
71

---

### Página 5

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
5 
1. Redes locales 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, 
y además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
 
Una red local (Local Area Network o LAN) puede incluir a dos o más (miles) dispositivos conectados 
entre sí, tanto en una vivienda privada como en una empresa, o instituciones públicas como 
administraciones, colegios o universidades. 
 
 
 
 
+ Info 
A las redes de campus también se les denomina CAN (Campus 
Area Network). 
 
 
Si se conectan más de dos ordenadores en una red LAN, se necesitan otros componentes de red como 
concentradores (hubs), puentes (bridges) y conmutadores (switches) los cuales funcionan como 
elementos de acoplamiento y nodos de distribución. 
También pueden utilizar un enrutador para la salida a internet. 
Las redes LAN permiten una transmisión rápida de grandes cantidades de datos. 
Además, las redes LAN permiten un intercambio de información cómodo entre los diversos dispositivos 
conectados a la red.

---

### Página 6

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
6 
Por ello, en el entorno empresarial es habitual que varios equipos de trabajo puedan acceder a 
servidores de archivos comunes, a impresoras de red o a aplicaciones por medio de la red LAN. 
Es posible dividir una gran LAN física en dos o más redes LAN lógicas más pequeñas denominadas LAN 
virtual o VLAN. 
Esto es útil cuando se quieren aislar dos segmentos de la red, por ejemplo, cuando la distribución del 
equipo de red no coincide con la estructura de la organización. 
De esta forma, los paquetes de difusión que se envíen por una red lógica no se reciben por los equipos 
del resto de redes lógicas (aunque estén en la misma red física). 
 
 
 
 
Ejemplo 
Los departamentos de informática y personal de una empresa 
podrían tener ordenadores en la misma LAN física debido a que se 
encuentran en la misma ala del edificio. 
Sería más sencillo administrar el sistema si cada departamento 
tuviera su propia red lógica. 
Si una persona de informática necesita enviar información a todo 
su departamento, podrá hacerlo sin tener que involucrar a los de 
personal, aun estando en la misma red física. 
 
 
Podemos diferenciar dos tipos de red, en función a cómo se transmite la información en el contexto 
físico: alámbrica o inalámbrica. 
1.1. LAN (alámbrica) 
La transmisión de datos tiene lugar o bien de manera electrónica a través de cables de cobre o mediante 
fibra óptica de vidrio. 
El estándar IEEE 802.3, comúnmente conocido como Ethernet, es hasta ahora el tipo más común de 
LAN alámbrica. (Otras opciones menos comunes, y ya obsoletas son: ARCNET, FDDI, y Token Ring).

---

### Página 7

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
7 
1.1.1. VLAN 
Una VLAN, o red local virtual, es un mecanismo de segmentación lógica que permite dividir una única 
red física en varios dominios de red independientes. Aunque todos los equipos estén conectados al 
mismo switch o a la misma infraestructura física, cada VLAN se comporta como una red distinta, de 
manera que el tráfico de difusión, de multidifusión y el tráfico interno de un grupo nunca alcanza a los 
equipos que pertenecen a otra VLAN. Este aislamiento mejora la seguridad, reduce el tráfico innecesario 
y permite organizar mejor la red según la estructura funcional de la organización. 
El funcionamiento de una VLAN se basa en la inserción de etiquetas (tags) en las tramas Ethernet, 
siguiendo el estándar IEEE 802.1Q. Esta etiqueta permite identificar a qué red virtual pertenece la 
trama, de manera que un mismo enlace físico puede transportar tráfico de múltiples VLAN. Los 
switches gestionan este etiquetado para garantizar que cada puerto solo reciba el tráfico 
correspondiente a su red lógica asignada. 
En un switch existen dos tipos de puertos en relación con las VLAN: 
• Los puertos de acceso son aquellos configurados para pertenecer únicamente a una VLAN 
concreta y se utilizan para conectar terminales como ordenadores, impresoras o teléfonos IP.  
• Los puertos de tipo trunk, en cambio, permiten transportar varias VLAN simultáneamente 
mediante el uso del etiquetado 802.1Q y se utilizan para interconectar switches entre sí o para 
enlazar un switch con un router o un firewall. 
Cuando se necesita comunicación entre VLAN diferentes, esta no se realiza de forma directa, ya que 
cada VLAN constituye un dominio lógico separado. Para permitir el intercambio de información entre 
ellas, se recurre a un dispositivo de capa superior, como un router o un switch de capa 3, que ejecuta lo 
que se conoce como enrutamiento inter-VLAN. Este mecanismo permite que las distintas VLAN 
mantengan aislamiento lógico, pero se comuniquen cuando las políticas de red lo permiten. 
Una de las principales ventajas de las VLAN es su capacidad para reorganizar la red sin modificar el 
cableado físico. La asignación de un dispositivo a una VLAN depende únicamente de la configuración 
del puerto del switch o del perfil de autenticación del dispositivo cuando se emplean sistemas 
dinámicos. Esto facilita la administración de la red, especialmente en organizaciones con varios 
departamentos distribuidos en la misma planta o edificio. Además, permite aplicar políticas de 
seguridad diferentes según el tipo de usuarios o servicios, como separar la red administrativa de la red 
de invitados, o segmentar sistemas críticos para evitar accesos no autorizados. 
Desde el punto de vista del rendimiento, las VLAN reducen el número de dispositivos que reciben 
tráfico de difusión, lo que contribuye a mejorar la eficiencia de la red y disminuir la congestión. 
También permiten implementar estrategias de calidad de servicio y priorización del tráfico según la 
importancia de cada segmento de red. 
En conjunto, las VLAN forman parte esencial del diseño moderno de redes locales, aportando 
flexibilidad, seguridad y un control granular del tráfico. Su utilización es especialmente relevante en 
entornos corporativos y administrativos, donde la segmentación lógica permite alinear la 
infraestructura de red con la estructura funcional de la organización

---

### Página 8

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
8 
1.2. WLAN (inalámbrica: wifi) 
WLAN (Wireless Local Area Network red de área local inalámbrica) es una LAN formada por conexiones 
inalámbricas. 
Los fundamentos básicos de las redes WLAN se definen en las normas IEEE 802.11. 
Las redes locales inalámbricas ofrecen la posibilidad de integrar terminales cómodamente en una red 
doméstica o empresarial y son compatibles con redes LAN Ethernet. 
El rendimiento es menor que el de una conexión Ethernet. 
El alcance de una Local Area Network depende del estándar usado como del medio de transmisión y se 
puede aumentar mediante el uso de repetidores. 
1.3. Asignación del canal 
Las redes inalámbricas y las alámbricas se pueden dividir en diseños estáticos y dinámicos, dependiendo 
de la forma en que se asigna el canal. 
• Estáticos. 
Consiste en dividir el tiempo en intervalos y utilizar un algoritmo por turnos (como Round-
Robin) para que cada máquina pueda difundir los datos en su turno durante un intervalo de 
tiempo. 
Su principal problema es que se desperdicia la capacidad del canal cuando una máquina que lo 
tiene asignado no necesita utilizarlo. 
• Dinámicos. 
Es el más utilizado. Hay dos métodos: 
• Centralizados: 
Existe una entidad central que determina el turno de cada dispositivo. 
Para ello acepta los paquetes a enviar y les asigna prioridades en base a algún algoritmo o 
función interna. 
• Descentralizados: 
No hay una entidad central. Cada máquina decide por su cuenta cuando transmitir. Hay que 
utilizar algoritmos para evitar colisiones.

---

### Página 9

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
9 
 
Ejemplo de red LAN. Fuente: SilverStar (https://en.wikipedia.org/w/index.php?curid=7654281) 
1.4. Tipos de red 
Hay muchos parámetros que conforman la arquitectura de una red de área local. 
En esta unidad veremos algunos de ellos: 
• Según la topología. 
• Según la técnica de transmisión. 
• Según método de acceso al medio. 
2. Estándar IEEE 802 
IEEE 802 es un proyecto del Institute of Electrical and Electronics Engineers (IEEE o instituto de 
ingenieros eléctricos y de electrónica). 
Su misión se centra en desarrollar estándares de redes de área local (LAN) y redes de área 
metropolitana (MAN), principalmente en las dos capas inferiores del modelo OSI (física y enlace de 
datos). 
Se desarrolló con el fin de crear estándares para que diferentes tipos de tecnologías pudieran integrarse 
y trabajar juntas. 
El proyecto 802 define aspectos relacionados con el cableado físico y la transmisión de datos. 
Se centra en definir los niveles más bajos (según el modelo de referencia OSI o sobre cualquier otro 
modelo).

---

### Página 10

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
10 
Concretamente subdivide el segundo nivel, el de enlace, en dos subniveles: el de Enlace Lógico (LLC), 
recogido en 802.2, y el de Control de Acceso al Medio (MAC), subcapa de la capa de Enlace Lógico. 
El resto de los estándares actúan tanto en el Nivel Físico, como en el subnivel de Control de Acceso al 
Medio. 
A continuación, te mostramos la lista de los grupos de trabajo que están trabajando en las distintas 
categorías. 
Nombre 
Descripción 
Nota 
IEEE 802.1 
Normalización de interfaz 
 
802.1d 
Spanning Tree Protocol 
Previene la formación de bucles en la red 
 
802.1p 
Asignación de Prioridades de tráfico 
 
802.1q 
Virtual Local Area Networks (VLAN) 
 
802.1x 
Autenticación en redes LAN (Controla equipos invitados, no autorizados 
o no administrados) 
 
802.1aq 
Shortest Path Bridging (SPB) 
 
IEEE 802.2 
Control de enlace lógico (LLC) 
Activo 
IEEE 802.3 
CSMA / CD (ETHERNET) 
 
IEEE 
802.3a 
Ethernet delgada 10Base2 
 
IEEE 
802.3c 
Especificaciones de Repetidor en Ethernet a 10 Mbps 
 
IEEE 
802.3i 
Ethernet de par trenzado 10BaseT 
 
IEEE 
802.3j 
Ethernet de fibra óptica 10BaseF 
 
IEEE 
802.3u 
Fast Ethernet 100BaseT 
 
IEEE 
802.3z 
Gigabit Ethernet parámetros para 1000 Mbps 
 
IEEE 
802.3ab 
Gigabit Ethernet sobre 4 pares de cable UTP Cat5e o superior

---

### Página 11

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
11 
Nombre 
Descripción 
Nota 
IEEE 
802.3ae 
10 Gigabit Ethernet 
 
IEEE 802.4 
Token bus LAN (Topología logia anillo física bus) 
Disuelto 
IEEE 802.5 
Token ring LAN (topología en anillo) 
Inactivo 
IEEE 802.6 
Redes de Área Metropolitana (MAN) (ciudad) (fibra óptica) 
(Bus dual de cola distribuida-DQDB) 
Disuelto 
IEEE 802.7 
Grupo Asesor en Banda ancha 
Disuelto 
IEEE 802.8 
Grupo Asesor en Fibras Ópticas 
Disuelto 
IEEE 802.9 
Servicios Integrados de red de Área Local (redes con voz y datos 
integrados) 
Disuelto 
IEEE 
802.10 
Seguridad de red 
Disuelto 
IEEE 
802.11 
Redes inalámbricas WLAN. (Wi-Fi) 
 
IEEE 
802.12 
Acceso de Prioridad por demanda 100 Base VG-Any Lan 
Disuelto 
IEEE 
802.13 
Se ha evitado su uso por superstición 
Sin uso 
IEEE 
802.14 
Módems de cable 
Disuelto 
IEEE 
802.15 
WPAN (Bluetooth) 
 
IEEE 
802.16 
Redes de acceso metropolitanas sin hilos de banda ancha (WIMAX). 
(Para acceso inalámbrico desde casa) 
 
IEEE 
802.17 
Anillo de paquete elástico script (Anillos de paquetes con recuperación) 
 
IEEE 
802.18 
Grupo de Asesoría Técnica sobre Normativas de Radio 
En desarrollo 
actualmente 
IEEE 
802.19 
Grupo de Asesoría Técnica sobre Coexistencia

---

### Página 12

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
12 
Nombre 
Descripción 
Nota 
IEEE 
802.20 
Mobile Broadband Wireless Access (Acceso inalámbrico de Banda ancha 
móvil). Similar al 16 pero en movimiento) 
 
IEEE 
802.21 
Media Independent Handoff (Interoperabilidad independiente del medio) 
 
IEEE 
802.22 
Wireless Regional Area Network (Red inalámbrica de área regional) 
 
3. Topología de red 
La topología de una red define su estructura. 
Se puede establecer desde dos puntos de vista básicos: 
• Topología física: 
Es la forma en que se conectan los terminales, dispositivos y recursos de la red. 
• Topología lógica: 
Es la forma de acceso a la información de la red. 
La elección de una topología u otra influye en gran medida en el funcionamiento y configuración de la red. 
La topología de red la determina únicamente la configuración de las conexiones entre nodos. 
Otros factores que no pertenecen a la topología de red, aunque pueden verse afectados por la misma son: 
• La distancia entre los nodos. 
• Las interconexiones físicas. 
• Las tasas de transmisión. 
• Los tipos de señales. 
Los principales tipos de topologías son: 
• Punto a Punto. 
• Bus. 
• Estrella.

---

### Página 13

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
13 
• Estrella extendida. 
• Anillo. 
• Anillo doble. 
• Malla. 
• Árbol o jerárquica. 
• Red celular. 
• Mixtas (unión de varias de las anteriores). 
Vas a estudiar cada una de ellas con detenimiento. 
3.1. Punto a punto 
 
Topología punto a punto 
Las redes punto a punto es una arquitectura de red en las que cada canal de datos se usa para 
comunicar dos nodos. 
En una red punto a punto, los dispositivos en red actúan como iguales, o pares entre sí. 
Cada dispositivo puede tomar el rol de emisor o de receptor. 
Las redes punto a punto son relativamente fáciles de instalar y operar. 
A medida que las redes crecen, las relaciones punto a punto se vuelven más difíciles de coordinar y 
operar. 
Su eficiencia decrece rápidamente a medida que la cantidad de dispositivos en la red aumenta. 
Los enlaces que interconectan los nodos de una red punto a punto se pueden clasificar en tres tipos 
según el sentido de las comunicaciones que transportan: 
• Símplex. 
• Semidúplex o Half-duplex. 
• Dúplex o Full-duplex.

---

### Página 14

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
14 
3.1.1. Simplex 
La comunicación es unidireccional. 
Solamente una de las dos estaciones de enlace puede transmitir; la otra sólo puede recibir. 
(Ejemplo: Impresora: recibir y Escáner: transmitir). 
El modo simplex puede usar toda la capacidad del canal para enviar datos en una dirección. 
 
Comunicación Simplex 
3.1.2. Semi-dúplex o Half-duplex 
Cada estación puede enviar y recibir, pero no al mismo tiempo. 
Cuando un dispositivo está enviando, el otro sólo puede recibir, y viceversa. 
En la transmisión semi-dúplex, la capacidad total del canal es usada por el dispositivo que está 
transmitiendo. 
Ejemplos: 
• Walkie-talkies. 
• Radios de banda civil o policiaca. 
• Cajero automático. 
Toda la capacidad del canal la usa el emisor.

---

### Página 15

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
15 
 
Comunicación Semi-Dúplex 
3.1.3. Full-dúplex o Dúplex 
En el modo dúplex ambas estaciones pueden enviar y recibir simultáneamente. 
Esto se puede conseguir de dos formas: 
• Usar dos caminos separados físicamente (por ejemplo, dos cables). 
• Utilizando distintas frecuencias (multiplexación de frecuencias). 
Se divide la capacidad del canal. 
Ejemplos: 
• Teléfono. 
• Dispositivo Bluetooth. 
• Dos ordenadores conectados en red. 
 
Comunicación Full-Dúplex o Dúplex 
Características 
• Los algoritmos de encaminamiento suelen ser complejos. 
• El control de errores se realiza en los nodos intermedios además de los extremos. 
• Las estaciones reciben sólo los mensajes que van dirigidos a él. 
• La conexión entre los nodos se puede realizar con uno o varios sistemas de transmisión de 
diferente velocidad, trabajando en paralelo. 
• Los retardos se deben al tránsito de los mensajes a través de los nodos intermedios.

---

### Página 16

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
16 
Ventajas 
• Fáciles de configurar. 
• Menor complejidad. 
• Menor costo dado que no se necesita dispositivos de red ni servidores dedicados. 
Desventajas 
• Administración no centralizada. 
• No son muy seguras. 
• Todos los dispositivos pueden actuar como cliente y como servidor, lo que puede ralentizar su 
funcionamiento. 
• No son escalables. 
• Reducen su rendimiento. 
3.2. Bus 
 
Topología en bus 
 
 
 
+ Info 
"La topología de bus es una configuración donde un único enlace 
conecta todos los dispositivos de la red constituyendo una red en 
forma de tronco". Gil, Pomares y Candelas (2010).

---

### Página 17

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
17 
La topología de bus tiene todos sus nodos conectados directamente a un enlace y no tiene ninguna otra 
conexión entre nodos. 
Físicamente cada dispositivo está conectado a un cable común, por lo que se pueden comunicar a 
través de él. 
La ruptura del cable hace que los hosts queden desconectados. 
La topología de bus permite que todos los dispositivos de la red puedan ver todas las señales de todos 
los demás dispositivos. 
Esto puede ser ventajoso si desea que todos los dispositivos obtengan esta información. 
También puede ser una desventaja ya que es común que se produzcan problemas de tráfico y 
colisiones, que se pueden paliar segmentando la red en varias partes. 
Ventajas 
• La principal ventaja es la facilidad de instalación. 
• Es muy económica. 
• No necesita la implementación de dispositivos adicionales para lograr la interconexión. 
Desventajas 
• Hay un límite de equipos dependiendo de la calidad de la señal. 
• Puede producirse degradación de la señal. 
• Complejidad de reconfiguración y aislamiento de fallos. 
• Limitación de las longitudes físicas del canal. 
• Un problema en el canal usualmente degrada toda la red. 
• El desempeño se disminuye a medida que la red crece. 
• El canal requiere ser correctamente cerrado (caminos cerrados). 
• Altas pérdidas en la transmisión debido a colisiones entre mensajes.

---

### Página 18

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
18 
 
 
 
+ Info 
A pesar de las desventajas de la topología en bus, esta sigue siendo 
una topología utilizada en redes organizacionales para los enlaces 
troncales. 
 
3.3. Estrella 
 
Topología en estrella 
 
 
 
+ Info 
El elemento distintivo de esta red es la incorporación de un 
dispositivo que funciona como un nodo central. 
Este nodo central se encarga de la gestión de forma directa con 
todos los demás nodos de la red, manteniendo un enlace punto a 
punto con cada uno. 
 
 
Algunas de las principales funciones que debe realizar el nodo central son la recepción y reenvío de 
datos a su nodo receptor correcto.

---

### Página 19

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
19 
Cuando un nodo requiera comunicarse con otro en la red, o enviar datos, lo hará por medio del nodo 
central al que le envía los datos, así como la solicitud de envío, indicándole a qué nodo debe reenviarlos. 
Otras características: 
• Otra de sus funciones principales consiste en controlar el tráfico en la red. 
• El nodo central es lo más importante en esta tecnología. 
• El envío de información está centralizado en el nodo central. 
• El nodo central puede ser un concentrador (hub) o un conmutador (switch). 
• El uso de un conmutador es más eficiente. 
Ventajas 
• Posee un sistema que permite agregar nuevos equipos fácilmente. 
• Reconfiguración rápida. 
• Fácil de prevenir daños y/o conflictos, ya que no afecta a los demás equipos si ocurre algún fallo. 
• Centralización de la red. 
• Fácil de encontrar fallos. 
Desventajas 
• Si el concentrador (hub) o conmutador (switch) central falla, toda la red deja de transmitir. 
• Es costosa, ya que requiere más cables que las topologías en bus o anillo. 
• Debe haber un cable desde el concentrador hasta cada dispositivo. 
 
 
 
 
+ Info 
Es la topología más popular y más utilizada, sobre todo en redes 
locales. 
En redes organizacionales de mayor tamaño, es frecuente utilizar 
múltiples estrellas interconectadas entre sí por medio de enlaces 
troncales.

---

### Página 20

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
20 
3.4. Estrella extendida 
 
Topología en estrella extendida 
La topología en estrella extendida es igual a la topología en estrella, con la diferencia de que cada nodo 
que se conecta con el nodo central también es el centro de otra estrella. 
Generalmente el nodo central está ocupado por un switch y los nodos secundarios por hubs o switch (se 
aconseja switch). 
La topología en estrella extendida es sumamente jerárquica, y busca que la información se mantenga 
local. 
 
 
 
 
+ Info 
Esta es la forma de conexión utilizada actualmente por el sistema 
telefónico. 
 
Ventajas 
• El cableado es más corto. 
• Limita la cantidad de dispositivos que se deben interconectar con cualquier nodo central.

---

### Página 21

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
21 
Desventajas 
• Si el nodo central falla, toda la red deja de transmitir. 
• Es costosa, ya que requiere más cable que las topologías bus o anillo. 
3.5. Anillo 
 
Topología en anillo 
 
 
 
+ Info 
"La topología de anillo es una topología de red donde cada 
dispositivo tiene una línea de conexión con todos los dispositivos 
de la red constituyendo una red en forma de anillo". Gil, Pomares y 
Candelas (2010). 
 
 
En una topología en anillo (Token Ring), los equipos están conectados con un cable de forma circular. 
En esta no hay extremos con terminaciones. 
Las señales viajan alrededor del bucle en una dirección y pasan a través de cada nodo, que actúa como 
repetidor para amplificarla señal y enviarla al siguiente nodo.

---

### Página 22

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
22 
Ventajas 
• El sistema provee un acceso equitativo para todas las computadoras. 
• El rendimiento no decae cuando muchos usuarios utilizan la red. 
• Arquitectura muy sólida. 
• Facilidad para la fluidez de datos. 
Desventajas 
• La información debe pasar por todas las estaciones intermedias antes de llegar al destino por lo 
que: 
• La transmisión de datos es más lenta. 
• La longitud de los canales es mayor. 
• Un archivo enviado podrá ser visto por todas las estaciones intermedias. 
• El canal usualmente se degradará a medida que la red crece. 
• Difícil de diagnosticar y reparar los problemas. 
3.6. Anillo doble 
 
Tipología en anillo doble

---

### Página 23

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
23 
En un anillo doble (Double Token Ring), dos anillos permiten que los datos se envíen en ambas 
direcciones (Token passing). 
Una topología en anillo doble consta de dos anillos concéntricos, donde cada dispositivo de la red está 
conectado a ambos anillos. 
Los dos anillos no están conectados directamente entre sí. 
Es análoga a la topología de anillo, con la diferencia de que, para incrementar la confiabilidad y 
flexibilidad de la red, hay un segundo anillo redundante que conecta los mismos dispositivos. 
Ventajas sobre la topología de anillo 
• Tolerancia a fallos (redundancia). 
• Se puede llegar a un nodo en dos sentidos (por el más rápido). 
3.7. Malla 
 
Topología en malla totalmente conectada 
 
 
 
+ Info 
"La topología de malla es una configuración en la que cada 
dispositivo tiene un enlace punto a punto dedicado con cualquier 
otro dispositivo.

---

### Página 24

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
24 
 
 
 
El término dedicado indica que el enlace sólo conduce al flujo de 
datos entre los dispositivos que interconecta". Gil, Pomares y 
Candelas (2010). 
 
 
La topología de red malla es una topología de red en la que cada nodo está conectado a todos los nodos. 
De esta manera es posible llevar los mensajes de un nodo a otro por distintos caminos. 
Si la red de malla está completamente conectada, no puede existir absolutamente ninguna interrupción 
en las comunicaciones. 
Cada dispositivo tiene sus propias conexiones con todos los demás dispositivos. 
Funcionamiento 
Esta topología no requiere de un nodo central. Si falla un nodo no implica la caída de la red. 
Las redes en malla pueden prescindir de enrutamiento manual, o apenas requerir atención para el 
mantenimiento de éste. 
La comunicación entre dos nodos cualesquiera de una red en malla puede llevarse a cabo incluso si uno 
o más nodos se desconectan de ésta de forma imprevista, o si alguno de los enlaces entre dos nodos 
adyacentes falla, ya que el resto evitarán el paso por ese punto. 
Los nodos adyacentes a un nodo o enlace fallido propagarán un cambio en la tabla de rutas, notificando 
a nodos contiguos del cambio en la red, y así sucesivamente. 
Ventajas 
• Una red en malla resulta muy confiable. 
• Ofrece total redundancia y por tanto una fiabilidad y tolerancia a fallos superiores. 
• Facilidad de solución de problemas. 
Desventajas 
• Resultan caras de instalar.

---

### Página 25

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
25 
3.8. Árbol 
 
Topología en árbol 
 
 
 
+ Info 
"La topología de árbol se ve como una estructura jerárquica, 
resultado de la combinación de varias topologías en estrella, en 
donde se puede observar que los nodos, en este caso switch o 
concentradores, están conectados a su vez en una topología de 
bus.". Romero, Barbancho, Benjumea, Rivera, Ropero, Sánchez y 
Sivianes (2010). 
 
 
La red en árbol es una topología de red en la que los nodos están colocados en forma de árbol. 
Desde una visión topológica, es parecida a una serie de redes en estrella interconectadas salvo en que 
no tiene un nodo central. 
En cambio, tiene un nodo de enlace troncal, generalmente ocupado por un concentrador desde el que 
se ramifican los demás nodos. 
Se comparte el mismo canal de comunicaciones.

---

### Página 26

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
26 
Ventajas 
• Su diseño permite colocar los dispositivos más importantes en los primeros niveles de jerarquía, 
para mejorar el desempeño y prevenir fallos. 
• Proporciona un control eficiente para la detección de errores y solución de problemas, ya que 
no se necesita controlar toda la red de forma centralizada, sino que se pueden crear diferentes 
zonas de control. 
• Cableado punto a punto para segmentos individuales. 
Desventajas 
• Puede presentar diversos problemas de cuello de botella, sobre todo en caso de fallo del nodo 
principal encargado del control de la red. 
• Es una red que presenta problemas de fiabilidad, sobre todo al saturar los canales o vías de 
comunicación hacia el nodo principal. 
• Es más difícil su configuración. 
• Si se desconecta un nodo, todos los que están conectados a él se desconectan también. 
3.9. Red celular 
 
Topología de red celular por áreas circulares

---

### Página 27

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
27 
 
Red de celdas con antenas de transmisión 
La topología celular está compuesta por áreas circulares o hexagonales, cada una de las cuales tiene un 
nodo individual en el centro. 
La topología celular es un área geográfica dividida en regiones (celdas) que se usa en las tecnologías 
inalámbricas. 
En esta tecnología no existen enlaces físicos. 
Sólo hay ondas electromagnéticas. 
Ventajas 
• No existe ningún medio tangible aparte de la atmósfera terrestre o el del vacío del espacio 
exterior (y los satélites). 
Desventajas 
• Las señales se encuentran presentes en cualquier lugar de la celda y, de ese modo, pueden sufrir 
disturbios y violaciones de seguridad. 
4. Técnicas de transmisión 
La transmisión de datos, transmisión digital o comunicaciones digitales es la transferencia física de 
datos (un flujo digital de bits) por un canal de comunicación punto a punto o punto a multipunto. 
Ejemplos de estos canales son cables de par trenzado, fibra óptica, los canales de comunicación 
inalámbrica y medios de almacenamiento.

---

### Página 28

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
28 
Los datos se representan como una señal electromagnética, una señal de tensión eléctrica, ondas 
radioeléctricas, microondas o infrarrojos. 
Existen dos tipos de transmisión: analógica y digital (la utilizada en informática). Y dos modos de 
transmisión: paralela y en serie. 
4.1. Clasificación según el número de bits transmitidos 
por ciclo de reloj 
La transmisión de datos binarios por un enlace se puede llevar a cabo en dos modos: 
• Modo paralelo: 
Se envían varios bits por cada pulso de reloj. 
• Modo serie: 
Solamente se envía un bit con cada pulso de reloj. Hay tres tipos de transmisiones serie: 
• Síncrona. 
• Asíncrona. 
• Isócrona. 
4.1.1. Transmisión Paralela 
Los datos binarios (formados por unos y ceros) se organizan en grupos de n bits. 
 
 
 
 
+ Info 
Los ordenadores producen y consumen datos en grupos de bits. 
 
 
Agrupando los datos podemos enviar n bits al mismo tiempo en lugar de 1.

---

### Página 29

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
29 
El mecanismo es sencillo: 
• Consiste en usar n hilos para enviar n bits cada vez. 
• Cada bit tiene su propio hilo y los n bits de un grupo se pueden transmitir en un pulso de reloj de 
un dispositivo a otro. 
• Normalmente, los n hilos están agrupados en un cable con un conector a cada extremo. 
Ventaja: 
• Aumenta la velocidad de transferencia n veces frente a la transmisión en serie. 
Desventaja: 
• Coste superior ya que requiere n líneas de comunicación. 
• Debido al alto coste se utiliza solo en distancias cortas. 
 
Transmisión paralela de 8 bits 
4.1.2. Transmisión Serie 
En este tipo de transmisión, un bit sigue a otro, por lo que solo necesita un canal de comunicación (en 
lugar de n) para transmitir datos entre dispositivos. 
 
Transmisión serie

---

### Página 30

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
30 
Ventaja: 
• Al tener un único canal de comunicación, el coste es n veces inferior a las paralelas. 
Desventaja: 
Dado que los equipos producen y consumen datos en grupos de bits, necesitaremos dispositivos de 
conversión: 
• Paralelo a serie en la interfaz entre emisor y la línea de comunicación. 
• Serie a paralelo en la interfaz entre la línea de comunicación y el receptor. 
La transmisión serie puede llevase a cabo de tres maneras: 
• Asíncrona. 
• Síncrona. 
• Isócrona. 
4.1.2.1. Transmisión Asíncrona 
En la transmisión asíncrona, la temporización de la señal no es importante. 
 
Transmisión asíncrona 
Funcionamiento: 
• La información se recibe y se traduce usando unos patrones acordados basados en la agrupación 
el flujo de bits en bytes. 
• Cada grupo (habitualmente 8 bits) se envía como una unidad.

---

### Página 31

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
31 
• El sistema que lo envía gestiona cada grupo independientemente, entregándolo al enlace en 
cuanto está listo. 
• El receptor no sabe cuándo va a llegar el grupo siguiente. 
• Para avisar al receptor de la llegada de un nuevo grupo se añade un bit extra al principio de cada 
byte (habitualmente un cero) denominado bit de inicio. 
• Para avisar al receptor de que grupo de bits ha terminado, se añaden uno o varios bits 
adicionales (normalmente unos) al final denominados bits de parada. 
• Usando este método estamos aumentando el tamaño del grupo de bits al menos en dos 
unidades. 
• Además, la transmisión de cada grupo de bits puede ir seguida de un intervalo de duración 
variable. 
• Este modo es asíncrono a nivel de grupo de n bits, pero la recepción de bits de un grupo debe 
tener algún tipo de temporizador que permita recibir los bits de forma sincronizada. 
• Cuando el dispositivo receptor detecta un bit de inicio, activa un temporizador y comienza a 
contar los bits a medida que llegan. 
• Después de contar n bits, el receptor busca un bit de parada. Al detectarlo, ignora cualquier 
pulso recibido hasta que vuelve a detectar un nuevo bit de inicio. 
Desventaja: 
Se debe añadir información extra (bit de inicio, bits de parada y un intervalo entre grupos de bits). Por 
lo tanto, la comunicación es más lenta. 
Ventajas: 
• Es más barata. 
• Es más efectiva. 
• Ideal para comunicaciones de baja velocidad. 
Ejemplo: Conexión entre un ordenador y el teclado. 
4.1.2.2. Transmisión Síncrona 
En la transmisión síncrona, se envía un bit detrás de otro (sin bits de inicio / parada o intervalos). 
Es responsabilidad del receptor agrupar los bits.

---

### Página 32

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
32 
 
Transmisión síncrona 
Aunque en la figura se han incluido divisiones entre los bytes, en realidad estas divisiones no existen. 
El emisor puede enviar los datos en ráfagas separadas. Los intervalos entre ráfagas se deben rellenar 
con una secuencia especial que indican vacío. 
El receptor cuenta los bits a medida que llega y los agrupa en unidades de n bits. 
En este caso la temporización es muy importante, ya que la exactitud de la información recibida 
depende de la habilidad del recepto de llevar exactamente la cuenta de los bits a medida que llegan. 
Ventaja: 
Mayor velocidad al no haber bits extra ni intervalos. 
La transmisión síncrona es útil para aplicaciones de alta velocidad como la transmisión de datos entre 
dos ordenadores. 
 
 
 
 
+ Info 
Debemos tener en cuenta que, aunque no hay intervalos entre 
grupos de bits, sí que puede haber intervalos desiguales entre 
tramas. 
 
4.1.2.3. Transmisión Isócrona 
En vídeo y audio en tiempo real no podemos utilizar transmisión síncrona dado que lo importante es no 
tener retardos desiguales entre tramas.

---

### Página 33

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
33 
 
 
 
Ejemplo 
Si las imágenes de TV se difunden a una tasa de 50 imágenes por 
segundo, estas imágenes deben ser visualizadas en la misma tasa. 
 
 
La transmisión isócrona garantiza que los datos llegan a una tasa fija sincronizando el flujo entero de 
bits. 
 
Transmisión isócrona 
4.2. Multiplexación 
Es el conjunto de técnicas que permite la transmisión simultánea de múltiples señales (canales) a través 
de un único enlace de datos. 
En toda transmisión multiplexada se necesita: 
• Un multiplexor en el transmisor. 
• Un demultiplexor en el receptor. 
Hay tres técnicas de multiplexación: 
• FDM (Multiplexación por División en Frecuencias). 
• WDM (Multiplexación por División de Onda). 
• TDM (Multiplexación por División en el Tiempo).

---

### Página 34

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
34 
4.2.1. FDM 
Multiplexación por División en Frecuencias. 
Características: 
• Normalmente se usa para señales analógicas. 
• Se puede aplicar cuando el ancho de banda de un enlace es mayor que los anchos de banda 
combinados de la señal a transmitir. 
• Se usan distintas frecuencias portadoras para transmitir (que no deben interferir con las 
frecuencias de los datos originales). 
• Se usan bandas de seguridad. 
 
4.2.2. Wdm 
Multiplexación por División de Onda. 
Características: 
• Conceptualmente igual que FDM, pero la multiplexación y demultiplexación se aplica a señales 
luminosas a través de fibra óptica.

---

### Página 35

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
35 
4.2.3. TDM (Multiplexión por División en el Tiempo) 
Características: 
• Se utiliza normalmente para señales digitales. 
• Se puede aplicar cuando la capacidad de tasa de datos de la transmisión es mayor que la tasa de 
datos necesaria requerida por los dispositivos transmisores y receptores. 
• Se divide el enlace en el tiempo y no en frecuencia. 
Tipos: 
• Síncrona. 
• El multiplexor siempre asigna exactamente la misma ranura de tiempo para cada 
dispositivo, independientemente de que los dispositivos tengan o no que transmitir. 
• Asíncrona o estadística. 
• El multiplexor usa reserva dinámica bajo demanda de las ranuras. 
• Puede dar más servicios que la síncrona. 
 
4.3. Banda base 
Se denomina banda base al conjunto de señales que no sufren ningún proceso de modulación a la salida 
de la fuente que las origina, es decir, son señales que son transmitidas en su frecuencia original. Dichas 
señales se pueden codificar y ello da lugar a los códigos de banda base. 
Las señales empleadas en banda base se pueden clasificar de la siguiente forma: 
• Unipolares: 
En este caso, un 1 siempre toma una polaridad, positiva o negativa, mientras que un 0 vale 
siempre 0.

---

### Página 36

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
36 
 
• Polares. 
En este caso la señal tomará valores positivos para un 1 lógico y negativos para un 0 lógico, pero 
nunca toma el valor 0. 
 
• Bipolares. 
En este caso un dígito toma valor con polaridad alternada, mientras que el otro permanece 
siempre en 0.

---

### Página 37

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
37 
Transmisión en banda base 
Es utilizada para cortas distancias debido a su bajo costo. El MODEM no efectúa modulación alguna, 
sino que solo las codifica. 
Los datos se codifican para solucionar los siguientes aspectos inherentes a la banda base: 
• Disminuir la componente continua. 
• Proveer sincronismo entre transmisor y receptor. 
• Permitir detectar la presencia de la señal en la línea. 
Como se está trabajando con pulsos, de acuerdo al desarrollo de Fourier, se puede tener un valor 
importante de la componente continua. Al codificar se trata de disminuir dicho valor, pues el sistema de 
transmisión puede poseer amplificadores y/o transformadores que no tendrían en cuenta la 
componente continua y ello provocaría una deformación de la señal. 
Es posible utilizar banda base en redes LAN y en otro tipo de redes siempre y cuando no se emplee la 
red pública de comunicaciones. 
Características de la transmisión en banda base. 
• La señal más simple que se emplea es la NRZL (NonReturn to Zero Level). 
• La señal no retorna a 0 y el pulso de tensión tiene la duración de 1 bit. 
• Generalmente un 1 lógico es un pulso de tensión mientras que un 0 lógico es la ausencia de 
dicho pulso de tensión. 
• Técnicamente se las conoce como señales on/off y las mismas tienen un alto valor de 
componente continua. 
• La mayor parte de la potencia transmitida se encuentra en las primeras armónicas, puesto que el 
desarrollo de la serie de Fourier da un espectro de la forma sen(x)/x. 
• En esta transmisión está limitado el uso de transformadores, puesto que los mismos no 
permiten el paso de la corriente continua, únicamente funcionan con corriente alterna. 
• No es posible enviar junto con los datos una señal de sincronismo. El receptor se sincroniza por 
medio de las transiciones de pulsos recibidos. Pero si se tiene una larga secuencia de ceros o de 
unos, la señal permanece constante durante un tiempo bastante largo en la línea y el receptor 
no puede identificar el principio y fin de cada bit. Este inconveniente se resuelve con la 
codificación. 
• En transmisiones en banda base puede producirse una deformación por interferencia entre 
símbolos (intersímbolos), la cual es debida a la superposición parcial de señales que corresponde 
a cada bit.

---

### Página 38

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
38 
 
Sistemas de codificación en banda base 
Hay diversos sistemas de codificación en banda base, entre otros. 
• Codificación Manchester. 
La codificación Manchester, también denominada codificación bifase-L, es un método de 
codificación eléctrica de una señal binaria en el que en cada tiempo de bit hay una transición 
entre dos niveles de señal. 
• Códigos NRZ. 
Se denomina NRZ porque el voltaje no vuelve a cero entre bits consecutivos de valor uno. 
Mediante la asignación de un nivel de tensión a cada símbolo se simplifica la tarea de decodificar 
un mensaje. Esta es la teoría que desarrolla el código NRZ (non return to zero). La 
decodificación en banda base se considera como una disposición diferente de los bits de la señal 
on/off, de este modo se adapta la señal al sistema de transmisión utilizado. Para ello se emplean 
los códigos tipo NRZ. 
• AMI ("Alternate Mark Inversion"). 
Dependen de un tipo de codificación que representa a los "unos" con impulsos de polaridad 
alternativa, y a los "ceros" mediante ausencia de pulsos. El código AMI genera señales ternarias 
(+V -V 0), bipolares( + - ), y del tipo RZ o NRZ (con o sin vuelta a cero). La señal AMI carece de 
componente continua y permite la detección de errores con base en la ley de formación de los 
"unos" alternados. En efecto, la recepción de los "unos" consecutivos con igual polaridad se 
deberá a un error de transmisión. 
La señal eléctrica resultante no tiene componente continua porque las marcas correspondientes 
al "1" lógico se representan alternativamente con amplitud positiva y negativa. Cada impulso es 
neutralizado por el del impulso siguiente al ser de polaridad opuesta. 
Los códigos AMI (inversión de marcas alternadas) se han desarrollado para paliar los 
inconvenientes que presentan los códigos binarios NRZ y RZ (el sincronismo y la corriente 
continua).

---

### Página 39

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
39 
• Pseudoternario. 
El pseudoternario codificaría de manera inversa a la "AMI". Codificando los "ceros" con impulsos 
de polaridad alternativa y los "unos" mediante ausencia de impulsos, el código resultante se 
denomina codificación pseudoternaria o pseudoternario. 
• Polar RZ-L. 
La sincronía se resuelve con transiciones a cero en la mitad del bit, tanto para los 0 y 1. 
• HDB3. 
HDB3 es un código binario de telecomunicaciones principalmente usado en Japón, Europa y 
Australia y está basado en el código AMI, usando una de sus características principales que es 
invertir la polaridad de los unos para eliminar la componente continua. 
• 2B1Q. 
Se trata de un mecanismo multinivel. Su nombre indica que codifica patrones de m=2 elementos 
de datos en un patrón de n=1 elemento de señal. Se emplea en las líneas xDSL. 
4.4. Modulación 
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
4.4.1. Tipos de Modulación según el sistema de transmisión 
• Señal portadora y moduladora son analógicas: 
• Modulación de amplitud, AM. 
• Modulación de frecuencia, FM. 
• Modulación de fase, PM.

---

### Página 40

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
40 
• Señal portadora analógica y moduladora digital: 
• Desplazamiento de amplitud, ASK. 
• Desplazamiento de frecuencia, FSK. 
• Desplazamiento de fase, PSK. 
• Señal portadora digital y moduladora analógica: 
• Modulación por amplitud de pulsos PAM. 
• Modulación de pulsos en duración (PDM). 
• Modulación de pulsos en posición (PPM). 
• Modulación por codificación de pulsos PCM. 
• Modulación por anchura de pulso (PWM). 
• Modulación Delta. 
• Señal portadora digital y moduladora digital: 
• En este caso no es necesaria la modulación. 
4.4.2. Perturbaciones en una Transmisión 
Consisten en pérdidas de información ocurridas en el transporte de la señal desde el emisor hasta el 
receptor. Estas perturbaciones son inevitables, pues existen una serie de factores que afectan a la 
calidad de las señales transmitidas los cuales provocan que estas nunca sean iguales a las señales 
recibidas. 
El efecto de las perturbaciones varía según la naturaleza analógica o digital de las señales. 
En las señales digitales se reduce la velocidad de transmisión al aumentar la tasa de errores de bits. 
 
 
 
 
+ Info 
El efecto en una señal analógica consiste en que esta línea de 
transmisión introduce variaciones de amplitud y frecuencia, lo que 
degrada la calidad de la señal.

---

### Página 41

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
41 
Las principales perturbaciones son: 
• Ruido: 
• Ruido Térmico o Blanco. 
• Ruido de Intermodulación. 
• Diafonía. 
• Ruido Impulsivo o Electromagnético (EMI). 
• Atenuación. 
• Distorsión de retardo. 
4.4.2.1. Ruido 
Es el conjunto de señales extrañas a la transmisión que se introducen en el medio de transmisión 
provocando alteraciones de amplitud del voltaje y variaciones de frecuencia. 
Está clasificado por: 
• Ruido Térmico o Blanco. 
Llamado también Ruido de Johnson-Nyquist, es provocado por la excitación de electrones 
debido a las oscilaciones térmicas del medio y se mantiene uniforme en el rango de frecuencias 
a la cual se transmite la señal mensaje. 
Se puede calcular mediante la fórmula: 
N=KTB (W) 
Donde: 
• B = El ancho de banda (Hz). 
• K = 1,3803 x 10-23 J/K. (Cte. de Boltzmann). 
• T = Temperatura (absoluta), en Kelvin. 
• La fórmula para W es N(W)=KTB y para dB es N(dB)= 10 log(KTB).

---

### Página 42

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
42 
• Ruido de Intermodulación. 
El ruido de intermodulación se produce en sistemas de transmisión no lineales produciéndose la 
inserción de nuevas frecuencias las cuales se adicionan o se restan con las frecuencias de la señal 
mensaje degenerándola. 
• Diafonía. 
También llamado Crosstalk, se produce cuando las señales se transmiten en medios adyacentes 
donde parte de las señales de uno, producto del acoplamiento magnético que produce la 
corriente de la señal mensaje, perturba la señal en el otro. 
(Por ejemplo, el cruce de conversaciones en la telefonía analógica). 
• Ruido Impulsivo o Electromagnético (EMI). 
Este tipo de ruido es impredecible puesto que siempre está presente en forma de sobresaltos o 
picos de tensión en el suministro de energía. Este tipo de ruido no es muy notable en la 
transmisión de señales analógicas, pero en la transmisión de señales digitales podría provocar 
perdida de datos. 
4.4.2.2. Atenuación 
Es la pérdida de potencia que se produce en el medio de transmisión por la longitud que este presenta, 
pues la potencia de la señal recibida es inversamente proporcional a la distancia entre el transmisor y el 
receptor. 
En medios guiados esta atenuación es representada por la proporción de la potencia transmitida y la 
potencia recibida: 
A= log(Pt/Pr) 
Donde: 
• A= atenuación. 
• Pt=Potencia transmitida. 
• Pr= potencia recibida.

---

### Página 43

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
43 
4.4.2.3. Distorsión de retardo 
Si la señal se transmite mediante guías de ondas la velocidad de propagación varía con la frecuencia, por 
lo que los distintos armónicos o componentes del espectro de frecuencias de la señal no viajen todas a 
la misma velocidad y las frecuencias centrales aumenten su velocidad. Como consecuencia, unos datos 
pueden solaparse con los anteriores. El efecto resultante es la distorsión de retraso y para contrarrestar 
esto se requiere el uso de técnicas de ecualización. 
4.5. Clasificación según el flujo de datos 
En la transmisión de datos en redes, hay diferentes métodos para enviar un mensaje desde un emisor 
hasta uno o varios receptores. 
Vas a estudiar los métodos: 
• UniCast. 
• MultiCast. 
• BroadCast. 
• AnyCast. 
4.5.1. UniCast 
 
Fuente: (https://es.m.wikipedia.org/wiki/Archivo:Unicast.svg) 
La comunicación UniCast es una comunicación uno a uno o punto a punto. 
Se puede utilizar para aplicaciones cliente/servidor en las que hay un solo emisor y un solo receptor.

---

### Página 44

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
44 
Estas comunicaciones están principalmente dirigidas por el emisor de datos, el cual conoce la dirección 
IP del receptor. 
Por lo tanto, los paquetes unicast usan la dirección del dispositivo de destino para la entrega de los 
datos. 
Estos datos pueden pasar por una interconexión de redes (no tienen por qué estar conectados 
directamente por un único cable). 
Este tipo de comunicación es la forma más común y eficiente de la comunicación entre dos nodos. 
Dependiendo de la dirección de la comunicación, existen 3 tipos de comunicación entre dos 
dispositivos: 
• Simplex. 
• Semi-Dúplex. 
• Dúplex. 
4.5.2. MultiCast 
 
Fuente: (https://es.m.wikipedia.org/wiki/Archivo:Multicast.svg) 
Las comunicaciones multicast permiten el envío de datos desde un emisor a muchos receptores (uno-a-
muchos), o desde muchos emisores a muchos receptores (muchos-a-muchos) si la gestión de los 
grupos se realiza de forma adecuada. 
En la actualidad los conmutadores que conectan los nodos de una red tienen soporte para administrar 
los grupos multicast. 
Estos grupos multicast pueden crecer o disminuir dinámicamente. 
Los nodos se unen (join) a un grupo multicast si están interesados en recibir tráfico dirigido a la 
dirección multicast de dicho grupo y lo deja (leave) cuando dejan de estar interesados. 
El Internet Group Management Protocol (IGMP) permite llevar a cabo la comunicación entre los nodos 
y los conmutadores de la red.

---

### Página 45

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
45 
4.5.3. BroadCast 
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:Broadcast.svg) 
La comunicación broadcast es comparable con la comunicación multicast ya que existe un solo emisor. 
En cambio, con broadcast un solo mensaje se entrega a todos los potenciales receptores (por ejemplo, 
en una subred), mientras que con multicast solo lo reciben los nodos interesados en el tráfico. 
La manera más común de lograr la comunicación broadcast es utilizar una dirección de difusión especial, 
en la cual se indica al mecanismo de comunicación que el mensaje debe ser entregado a todos los nodos 
de la subred. 
Al enviar un mensaje broadcast, el emisor no necesita conocer el número de receptores. 
Broadcast es menos eficiente porque ocupa más infraestructura de la red al enviarlo a todos los nodos 
quieran o no quieran los datos. 
Un claro ejemplo del uso de broadcast se puede encontrar en el protocolo de resolución de direcciones 
o Address Resolution Protocol (ARP). 
4.5.4. AnyCast 
 
Fuente: (https://commons.wikimedia.org/wiki/File:Anycast.svg)

---

### Página 46

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
46 
Anycast es una forma de direccionamiento o enrutamiento en la que la información es encaminada al 
mejor destino desde el punto de vista de la topología de la red. 
Está compuesta por un emisor, un receptor y un grupo de posibles receptores. 
En la red internet, una dirección IP se puede anunciar desde varios puntos diferentes. 
Los enrutadores intermedios encaminan el paquete hasta el destino más cercano. 
Un paquete enviado a una dirección anycast es entregado a la máquina más próxima desde el punto de 
vista del tiempo de latencia. 
En anycast, el paquete solo lo recibe un nodo. 
5. Métodos de acceso al medio 
Los métodos de acceso al medio, en inglés MAC (Media Access Control), son un conjunto de 
mecanismos y protocolos de comunicaciones a través de los cuales varios "interlocutores" (dispositivos 
en una red, como computadoras, teléfonos móviles, etcétera) se ponen de acuerdo para compartir un 
medio de transmisión común. 
Se realiza en la capa de enlace de datos del modelo OSI. 
Se denomina método de acceso al conjunto de reglas que definen la forma en que un equipo coloca 
los datos en la red y toma los datos de esta. 
Propiedades: 
• Una vez que los datos se están moviendo en la red, los métodos de acceso ayudan a regular el 
flujo del tráfico de la red. 
• Controlan la forma de acceder al medio de transmisión en redes de difusión evitando conflictos 
y errores. 
• Caracteriza el funcionamiento de la red y condiciona el rendimiento, fiabilidad y gestión de esta. 
• Los protocolos de acceso al medio son aquellos que definen la forma a través de la cual se 
producirá la comunicación. 
El protocolo MAC, se creó a partir de que en redes LAN y MAN todas las estaciones están conectadas a 
un mismo medio de transmisión, lo cual ocasiona 2 problemas: 
• La transmisión de una estación es escuchada por las demás estaciones. 
• Colisión. Una colisión se produce cuando dos estaciones transmiten simultáneamente 
dañándose las tramas de ambas estaciones.

---

### Página 47

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
47 
Por ello, para solucionar estos problemas el protocolo MAC tiene la misión, entre otras, de: 
• Evitar que una estación se apodere del medio durante mucho tiempo. 
• Aplicar métodos para evitar o resolver colisiones. 
5.1. Clasificación 
Podemos clasificar las técnicas de control de acceso al medio en: 
• Repartición (control estático): 
• FDM. 
• TDM. 
• Compartición (control dinámico): 
• Control centralizado. 
Existe un controlador con autoridad para conceder acceso a red. 
Las estaciones que deseen transmitir deben esperar que les dé permiso. 
• Control distribuido. 
Las estaciones realizan conjuntamente la función MAC para determinar dinámicamente el 
orden de transmisión. 
5.1.1. Repartición 
Se reparte el medio entre los N usuarios que acceden al mismo. 
Se puede repartir de dos formas: 
• FDM o Multiplexación por división de frecuencia. 
El ancho de banda total disponible en un medio de comunicación se divide en una serie de sub-
bandas de frecuencia que no se superponen, cada una de las cuales se utiliza para transportar 
una señal separada. 
• TDM o Multiplexación por división de tiempo. 
El ancho de banda total del medio de transmisión es asignado a cada canal durante una fracción 
del tiempo total (intervalo de tiempo).

---

### Página 48

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
48 
Características 
• No existen interferencias entre usuarios. 
• Es simple. 
• Es eficiente si el número de usuarios es pequeño y el tráfico es alto. 
• Ineficiente para muchos usuarios. 
• No están optimizadas (por ejemplo, en la división de tiempo, el canal está reservado para un 
dispositivo, aunque este no esté transmitiendo). 
5.1.2. Compartición 
Se aplican métodos para compartir el canal. 
Se clasifican en: 
• Contienda. 
• Reserva. 
• Selección (controlado). 
• Métodos híbridos: 
Obtienen los beneficios de los métodos que combinan Contienda-Reserva, Contienda-Selección, 
Reserva-Selección. 
Los métodos híbridos se consideran de compartición porque pese a tener características de los 
métodos de repartición, tienen características propias a la compartición, en los dos primeros 
casos contienda-reserva y contienda-selección la contienda las hace claramente pertenecer a 
los métodos de compartición, donde generalmente no hay ni tiempos ni canales establecidos 
previamente. 
• Contienda-reserva. 
» En la contienda-reserva las estaciones compiten por el medio, y el ganador reservará 
un tiempo para poder transmitir. 
» Mejores para cargas bajas (Retardo mínimo). 
» Peor para cargas altas (Baja eficiencia por colisión).

---

### Página 49

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
49 
• Contienda-selección. 
» En la contienda-selección se erige en árbitro un controlador central que determina de 
manera dinámica cuál de los dispositivos en contienda puede transmitir en un 
momento dado, en función de criterios de prioridad y calidad del servicio. 
» Peores para cargas bajas (gran retardo). 
» Mejores para cargas altas (mejor eficiencia). 
• Reserva-selección. 
» En el método de reserva-selección las estaciones reservan un intervalo de tiempo o 
canal para uso exclusivo y será un controlador central quien ajuste las asignaciones en 
función de las necesidades de red. 
5.1.2.1. Contienda 
Se conocen también como métodos de acceso aleatorio porque la transmisión no es planificada, o 
como métodos de contención pues existe competencia a la hora de acceder al medio. 
Son métodos que carecen de una jerarquía superior que dirija al tráfico, sino que será el dispositivo en 
disposición de transmitir quien decida transmitir según el protocolo que lo regule y generalmente en 
base a la ocupación del medio. 
En entornos de baja carga, son apropiados para el tráfico a ráfagas, la toma de decisiones de 
transmisión tiene naturaleza distribuida, y son sencillos de implementar. 
Si más de una estación trata de transmitir a la vez se producirá una colisión, y las tramas involucradas en 
la misma serán modifcadas o destruidas. 
La evolución de estos protocolos que se inicia con los Métodos Aloha propuestos a principios de los 70, 
seguiría este orden histórico: 
• Aloha puro (universidad de Hawai) que se clasifica como método sordo pues no posee 
información del estado del canal. 
• Aloha ranurado, cuenta ya con capacidad de escucha,  
• Familia CSMA (Carrier Sense Multiple Access) utilizada generalmente en redes de tipo BUS: 
• CSMA 
• CSMA Persistente 
• CSMA/CD

---

### Página 50

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
50 
5.1.2.1.1. Principales protocolos de Contienda dentro del método 
de compartición 
Vas a profundizar un poco en los protocolos más destacados. 
ALOHA PURO 
Es originario de la Universidad de Hawai. 
Detecta colisiones. Sigue los siguientes pasos: 
1. La estación transmite. 
2. Escucha el medio durante un tiempo. 
3. Si recibe confirmación, asume que la trama se ha recibido. 
4. Si no recibe información, espera un intervalo de tiempo aleatorio y vuelve a trasmitir la trama, 
volviendo al paso 2. 
5. Si el número de intentos supera un límite, desiste. 
ALOHA RANURADO 
El tiempo del canal se divide en ranuras de duración igual al tiempo de transmisión de la trama. 
Se requiere un método de sincronización de las estaciones. 
Una estación sólo puede transmitir al inicio de una ranura de tiempo. 
CSMA 
CSMA (Acceso múltiple por detección de portadora) también es conocido como CSMA no persistente. 
Sigue los siguientes pasos: 
1. Una estación debe escuchar el medio antes de transmitir. 
2. Si el medio está ocupado, debe esperar un tiempo aleatorio y volver al paso 1. 
3. Si el medio está libre, puede transmitir. 
4. La estación transmisora debe esperar una confirmación, si no la recibe, retransmitirá. 
Debido al retardo de propagación, una estación puede no escuchar una transmisión que acaba de 
empezar y se producirá una colisión. 
El medio permanece libre justo después de terminar una transmisión de una estación.

---

### Página 51

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
51 
CSMA persistente 
En CSMA persistente, una estación que detecta ocupado el canal, se queda escuchando hasta que 
detecte que queda libre, momento en el cual inicia la transmisión. 
En CSMA persistente, las estaciones son más egoístas que en CSMA no persistente. 
Aumenta la probabilidad de colisión (dos estaciones podrían estar esperando para transmitir). 
Solución: CSMA p-persistente. 
Si el medio se encuentra libre, se transmite con una probabilidad p, o se espera una unidad de tiempo 
con una probabilidad (1-p). 
CSMA/CD 
El protocolo CSMA/CD (Carrier Sense Multiple Access/Collision Detect) es uno de los métodos MAC 
más utilizados. 
Se emplea en la norma 802.3 y el protocolo Ethernet. 
Es un acceso múltiple por detección de portadora con detección de colisiones. 
Las estaciones que desean transmitir escuchan el medio identificando si se está usando en ese 
momento por otra estación: 
• Si el medio está libre transmite. 
• Si el medio está ocupado sigue escuchando y cuando esté libre transmite. 
Pueden existir colisiones debido a retardos. 
Si las hay las detecta, dado que sigue escuchando mientras transmite. 
Si detecta una colisión deja de transmitir, manda unas señales de consenso, espera un tiempo aleatorio 
y lo intenta de nuevo. 
Las colisiones se detectan por existir una tensión mayor de lo normal, para evitar malentendidos por 
atenuaciones se deben limitar distancias. 
Características: 
• A mayor carga de la red, los dispositivos disminuyen la utilización del medio. 
• Cuando la carga disminuye, las estaciones vuelven a utilizar el medio con mayor frecuencia. 
• La capacidad desaprovechada se reduce al tiempo que se tarda en detectar la colisión.

---

### Página 52

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
52 
• Sirve para LAN en Bus, pero no para redes inalámbricas (no se puede escuchar el eco). 
• La trama debe ser lo suficientemente larga como para detectar la colisión antes de finalizar la 
transmisión (longitud mínima). 
5.1.2.2. Reserva 
Las estaciones que quieren usar el medio solicitan una reserva y no inician la transmisión de información 
hasta que se le concede. 
Son métodos libres de colisiones en la transmisión de datos, pero puede haberla en la solicitud de 
reservas. 
Son adecuadas para tráfico continuo. 
Las técnicas de repartición (control estático, modulación por tiempo o por frecuencia) se pueden 
considerar también técnicas de reserva. 
Estos métodos se pueden dividir en: 
• Métodos Centralizados. 
Existe un controlador que gestiona (recibe y concede) las demandas de reserva del canal. Se 
puede disponer de dos canales distintos, uno para efectuar las reservas y otro para transmitir los 
datos. 
El modelo SRMA (Split Chanel Reservation Multiple Access) multiplexa los dos canales en 
frecuencia, pero se puede producir colisión en el canal de las reservas. 
EL método GSMA (Global Scheduling Multiple Access) multiplexa en el tiempo el canal, 
asignando durante un tiempo el canal para la transmisión de datos, a su vez, multiplexa el canal 
de reservas entre todas las estaciones, evitando colisiones. 
Se puede hacer una "reserva de conexión" o una "reserva de mensaje". 
• Métodos Distribuidos. 
El sistema de reserva se lleva a cabo entre todas las estaciones sin que exista ninguna especial. 
Algunos de estos protocolos son: 
• Bit Map (mapa de bits). 
• BRAP (Reconocimiento de difusión con prioridades alternas). 
• Slotted Ring (Anillo ranurado). 
Se usa principalmente en redes en anillo.

---

### Página 53

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
53 
Sus características principales son: 
• Un nodo especial (monitor) inicia el anillo conteniendo un número fijo de bits que circula 
continuamente por el anillo de una estación a otra. 
• El anillo está dividido en un número fijo de ranuras de un determinado número de bits capaz 
de transportar una única trama MAC (cada una). 
• Cuando una estación desea transmitir espera una ranura vacía y la marca como ocupada 
insertando su trama en la misma. 
• El anillo ranurado plantea dos problemas importantes: 
• Requiere un nodo monitor especial (vulnerable) para mantener la estructura básica del 
anillo. 
• La transmisión de cada trama completa del nivel de enlace suele requerir varias ranuras 
(tramas MAC). 
5.1.2.3. Selección 
Es una técnica controlada por rotación. 
Cada estación, por turno, recibe permiso para transmitir. 
En su tiempo puede transmitir o no, pasado el mismo pasa el turno a la siguiente. 
Las estaciones deben almacenar sus mensajes hasta recibir su turno, en principio desconocen cuándo se 
producirá. 
El problema de las técnicas controladas es que la espera de turnos depende del número de estaciones. A 
mayor número de estaciones, mayor tiempo de espera. 
Sin embargo, tiene un buen comportamiento en condiciones de carga alta (su rendimiento no baja). 
El control de turnos puede ser: 
• Centralizado. 
Hay una estación dedicada denominada "maestro". 
El problema es que falle esta estación. 
• Distribuido. 
La tarea se reparte entre las estaciones que quieren transmitir.

---

### Página 54

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
54 
Algunos de los protocolos más importantes son: 
• Sondeo, Polling o Lista. 
• Hub-Polling. 
• Daisy Chain. 
• Token Pass (Paso de testigo): 
(Protocolo de acceso al medio). 
Todas las estaciones participantes intervienen en la circulación de un paquete especial 
(denominado testigo o token), que indica a la estación que lo posee que puede disponer del 
medio de transmisión. 
Puede implementarse de forma distribuida o centralizada. 
Según sea la topología de la red en la que se implementa recibe el nombre de: 
• Protocolo Token-ring para topologías de anillo. 
Precisa la formación de un anillo lógico, y precisa labores de gestión del anillo: 
» Inicializar el anillo. 
» Adición de estaciones al anillo. 
» Eliminación de estaciones del anillo. 
» Recuperación de errores. 
Características: 
» En una red con topología en anillo, los dispositivos pueden conectarse al anillo 
directamente o a través de concentradores. 
» En esta topología es más eficaz y da mayor rendimiento. 
» Proporciona reparto equitativo y gestión de red fácil. 
» El orden de selección es fijo, según la conexión física al anillo. 
» El testigo o trama circula por el anillo constantemente, un bit indica si está ocupado (T 
= 1) o libre (T = 0). 
» Con tráfico alto las demandas se resuelven por mecanismos de rotación (conexión al 
anillo).

---

### Página 55

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
55 
» Se pueden establecer prioridades a nivel MAC. 
» Puede existir anillo redundante en sentido opuesto (seguridad). 
» Una vez conseguido el testigo se pueden transmitir todas las tramas que se deseen 
mientras que no expire el tiempo de retención. 
» Si no hay tráfico sólo se transmite el testigo. 
» Es necesario que exista una estación destacada, monitor, que realiza funciones 
especiales de gestión. 
» Es uno de los métodos MAC más utilizados. 
» Se emplea en la norma IEEE 802.5. 
• Protocolo Token-bus para topologías tipo bus. 
Es un protocolo de acceso al medio en el cual los nodos están conectados a un bus o canal 
para comunicarse con el resto. En todo momento hay un testigo (token) que los nodos de 
la red se van pasando, y únicamente el nodo que tiene el testigo tiene permiso para 
transmitir. El bus principal consiste en un cable coaxial. 
Características: 
» Tiene una topografía en bus (configuración en bus física), pero una topología en anillo. 
Las estaciones están conectadas a un bus común, pero funcionan como si estuvieran 
conectadas en anillo. 
» Todas las estaciones o nodos conocen la identidad de los nodos siguiente y anterior. El 
último nodo conoce la dirección del primero y de su anterior, así como el primer nodo 
conoce la dirección del último y de su sucesor. 
» La estación que tiene el testigo o token tiene el control sobre el medio y puede 
transmitir información a otro nodo. 
» Cada estación tiene un receptor y un transmisor que hace las funciones de repetidor de 
la señal para la siguiente estación del anillo lógico. 
» No existen colisiones. 
» Todas las estaciones tienen igual probabilidad de envío. 
» Es un protocolo eficaz en la producción en serie.

---

### Página 56

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
56 
6. Dispositivos de interconexión 
El objetivo de la interconexión de redes es dar un servicio de comunicación de datos que involucre 
diversas redes con diferentes tecnologías de forma transparente para el usuario. 
Este concepto hace que las cuestiones técnicas particulares de cada red puedan ser ignoradas al diseñar 
las aplicaciones que utilizarán los usuarios de los servicios. 
Los dispositivos de interconexión de redes sirven para superar las limitaciones físicas de los elementos 
básicos de una red. 
Vamos a estudiar los siguientes dispositivos: 
• Repetidor. 
• Concentrador (Hub). 
• Conmutador (Switch). 
• Puente (Bridge). 
• Enrutador (Router). 
• Compuerta (Gateway) Repetidor. 
Estos dispositivos de red operan en las siguientes capas de los modelos ISO/OSI y TCP/IP: 
Dispositivo de red 
Capa OSI 
Capa TCP/IP 
Repetidor 
Física 
Hardware (no capa) 
Concentrador (Hub) 
Física 
Hardware (no capa) 
Conmutador (Switch) 
Enlace de Datos 
Acceso a la Red 
Puente (Bridge) 
Enlace de Datos 
Acceso a la Red 
Enrutador (Router) 
Red 
Internet 
Compuerta (Gateway) 
Transporte y/o Sesión 
Transporte

---

### Página 57

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
57 
6.1. Repetidor 
 
Fuente: 
(https://de.m.wikipedia.org/wiki/Datei:Repea
ter_netz.png) 
Un repetidor es un dispositivo que une dos segmentos del mismo tipo de red. 
Características: 
• Los cables que unen pueden ser de tipos diferentes (por ejemplo, coaxial y fibra óptica). 
• Se encarga de amplificar, regenerar y re-temporizar la señal. 
• Permite que los bits viajen a mayor distancia a través de los medios. 
• No entiende de formatos, simplemente copia cualquier señal eléctrica (incluido ruido e 
interferencias). 
• No filtra tráfico de Red. 
6.2. Concentrador (Hub) 
 
Un hub es un dispositivo que actúa como punto de conexión central entre los nodos que componen 
una red. 
Posee una topología física en estrella, pero lógica de bus.

---

### Página 58

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
58 
Los equipos conectados al hub son miembros de un mismo segmento de red y comparten el ancho de 
banda del hub para sus comunicaciones. 
Son repetidores multi-puertos, interconectando varios dispositivos de forma económica y sencilla. 
Ventaja: 
Aumenta la confiabilidad de la red, ya que si cualquier cable falla no afecta a la red. 
Desventaja: 
Transmite por difusión, por lo que se producen colisiones. 
Tipos 
Existen dos tipos de hub: 
• Activos. 
Realizan la regeneración de la señal que reciben antes de ser enviada. 
• Pasivos. 
No regeneran la señal. Simplemente interconectan los dispositivos. 
Funcionamiento 
Cuando un equipo envía un mensaje, los datos llegan al hub y éste los regenera (si es activo) y los 
retransmite a todos sus puertos, excepto al puerto que emite el mensaje. 
El hub no divide dominios de colisión, ni dominios de broadcast. 
 
 
 
 
+ Info 
Dominio de colisión. 
Son segmentos de la red que comparten el mismo ancho de banda. 
Cuando dos o más dispositivos, que comparten el mismo 
segmento, intentan comunicarse al mismo tiempo pueden ocurrir 
colisiones.

---

### Página 59

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
59 
 
 
 
Dominio de broadcast. 
Contiene todos los dispositivos que pueden ser alcanzados por un 
broadcast (mensaje para todos los miembros de la red). 
 
6.3. Conmutador (Switch) 
 
Es un dispositivo que permite la interconexión de dispositivos entre sí. 
Características 
• Permite segmentar una red para aumentar su rendimiento a nivel de enlace. 
• A diferencia de los puentes, los switch sólo permiten conectar redes que utilicen los mismos 
protocolos a nivel físico y de enlace. 
• Filtran y dirigen tramas entre los segmentos de la red de área local proporcionando un ancho de 
banda dedicado. 
• Conoce los dispositivos que tiene conectados a cada uno de sus puertos. 
• Cuando se enchufa no conoce las direcciones de los dispositivos de sus puertos, las aprende a 
medida que circula información a través de él. 
• Un switch divide el dominio de colisiones. 
• Tiene tantos dominios de colisión como bocas posea. 
• Un switch no divide el dominio de broadcast, ya que la red segmentada se ve como una sola. 
• Cuando un switch no conoce la dirección MAC de destino envía la trama por todos sus puertos, 
al igual que un HUB.

---

### Página 60

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
60 
• Cuando hay más de un ordenador conectado a un puerto de un switch este aprende sus 
direcciones MAC y cuando se envían información entre ellos no la propaga al resto de la red (a 
esto se llama filtrado). 
• Operan a velocidades mucho más altas que los puentes. 
• Los datos pueden conducirse por rutas separadas, mientras que, en el hub, las tramas son 
conducidas por todos los puertos. 
6.4. Puente (Bridge) 
 
Los puentes son dispositivos que pueden conectar a varias LAN entre sí. 
Características 
• Generalmente conectan LAN con idénticos protocolos de capa física y de acceso al medio 
(MAC). 
• Deben tener una memoria temporal para albergar las tramas a intercambiar de LAN. 
• Mantienen una tabla de direcciones físicas MAC para saber qué tramas van a una LAN o a otra. 
• Desde el punto de vista de cada estación, todas las demás estaciones están en su misma LAN y 
es el puente el encargado de encaminar las tramas.

---

### Página 61

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
61 
Funciones 
Las funciones de un puente son: 
• Dividir una red de área local en dos redes de menor tamaño. 
Cuando una red de área local se hace demasiado grande en cuanto a número de nodos, debe ser 
dividida para mejorar su rendimiento. 
• Interconectar redes de área local. 
Pueden tener protocolos de nivel de enlace o medios de transmisión distintos. 
Ejemplo: Interconexión de una red inalámbrica a una de cable. 
• Controlar las tramas defectuosas. 
Funcionamiento 
El puente entrará en funcionamiento, pasando la información, sólo cuando el nodo de un segmento 
envíe información al nodo del segmento al otro lado del puente. 
Cada puente va almacenando en memoria una tabla de direcciones MAC asignada a cada uno de sus 
puertos. 
De esta manera, cuando llega una trama, comprueba la dirección MAC, la compara con el "mapa" que 
posee en memoria y la envía por el puerto adecuado. 
Ventajas 
• Cuando se conectan varias LAN con puentes, el fallo en una LAN no implica el fallo en la otra. 
• Varias LAN pequeñas tienen mayores prestaciones que una grande. 
• Reduce el dominio de colisión. 
• Las longitudes de cableado son menores. 
• Cuando hay dos LAN separadas geográficamente, es más sencillo y barato conectarlas con un 
puente que usar cable coaxial. 
• Divide el dominio de colisión, pero no el dominio de broadcast.

---

### Página 62

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
62 
6.5. Enrutador (Router) 
 
Fuente: (https://es.wikipedia.org/wiki/Archivo:Linksys-Wireless-G-
Router.jpg) 
Es un dispositivo hardware o producto software que permite interconectar redes entre sí. 
Características 
• Como funciona a nivel de red, los protocolos de comunicación en los niveles superiores a ambos 
lados del enrutador deben ser iguales. 
• Toma decisiones lógicas con respecto a la mejor ruta para el envío de datos a través de una red 
interconectada. 
• Comparte información con otros enrutadores. 
• Divide el dominio de colisión y de broadcast. 
Funcionamiento 
Al recibir un paquete, debe extraer de éste la dirección del destinatario y decidir cuál es la mejor ruta. 
Para ello utiliza: 
• Un algoritmo de enrutamiento. 
• Una tabla de enrutamiento. 
• Sus propias direcciones a nivel de red.

---

### Página 63

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
63 
Un enrutador necesita de una serie de parámetros básicos para que pueda funcionar correctamente: 
• Direcciones de los puertos y redes a las que está conectado. 
• Algoritmos de enrutamiento que va a utilizar. 
• Una tabla de enrutamiento. 
El enrutador, para determinar la mejor ruta, utiliza la tabla de rutas y evalúa una métrica. 
La ruta escogida es aquella que tiene el menor valor de la métrica utilizada. 
 
 
 
 
+ Info 
La métrica es un valor generado por el enrutador o asignador por 
el administrador para cada ruta en base a una función que depende 
de diversos factores a los cuales se le asignan pesos para indicar 
que unos son más importantes que otros. 
Algunos factores pueden ser: 
• Ancho de banda. 
• Retardo. 
• Carga. 
• Confiabilidad. 
• Número de saltos. 
• Coste. 
 
Algoritmos de las tablas de enrutamiento 
• No adaptativos o estáticos. 
No tienen en cuenta los cambios. 
Las rutas se calculan manualmente y luego se introducen en la tabla de rutas (inundación). 
• Adaptativos o dinámicos.

---

### Página 64

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
64 
6.5.1. Protocolos de Enrutamiento 
Especifican cómo los enrutadores se comunican entre sí para distribuir información que les permite 
seleccionar rutas entre nodos en una red informática. 
Los algoritmos de enrutamiento determinan la elección específica de la ruta. 
Un protocolo de enrutamiento comparte la información de que dispone un router (conocimiento previo 
solo de las redes conectadas a él directamente) primero entre los vecinos inmediatos y luego en toda la 
red, así los routers adquieren conocimiento de la topología de la red. 
La capacidad de los protocolos de enrutamiento para ajustarse dinámicamente a condiciones 
cambiantes, como conexiones y componentes deshabilitados y enrutar datos alrededor de 
obstrucciones, es lo que le da a Internet su tolerancia a fallas y alta disponibilidad. 
Las características específicas de los protocolos de enrutamiento incluyen cosas tales como: 
• La forma en que evitan los bucles de enrutamiento. 
• La forma en que seleccionan las rutas preferidas. 
• El uso de información sobre los costos de salto. 
• El tiempo que requieren para alcanzar la convergencia de enrutamiento, su escalabilidad. 
• Factores como la multiplexación de relés y los parámetros del marco de acceso a la nube. 
Ciertas características adicionales, como la interfaz multicapa, también pueden emplearse como medio 
para distribuir puertas de enlace de red sin compromisos a puertos autorizados., lo que permite 
prevenir problemas con los bucles del protocolo de enrutamiento. 
Veamos brevemente algunos protocolos: 
• Protocolo BGP. 
Siglas de Border Gateway Protocol, es un protocolo de puerta de enlace exterior estandarizado 
diseñado para intercambiar información de enrutamiento y accesibilidad entre sistemas 
autónomos (AS) en Internet. 
Se clasifica como un protocolo de enrutamiento de vector de ruta, y toma decisiones de 
enrutamiento basadas en rutas, políticas de red o conjuntos de reglas configurados por un 
administrador de red. 
• El BGP utilizado para el enrutamiento dentro de un sistema autónomo se denomina 
Protocolo de puerta de enlace de borde interior, BGP interno (iBGP). 
• La aplicación de Internet del protocolo se denomina Protocolo de puerta de enlace de 
borde exterior, BGP externo (eBGP).

---

### Página 65

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
65 
 
 
 
+ Info 
EGP, Exterior Gateway Protocol fue un protocolo estándar usado 
para intercambiar información de encaminamiento entre sistemas 
autónomos en los primeros años de Internet, hasta que fue 
completamente reemplazado por BGP a mediados de los 90. 
Las puertas de enlace o pasarelas EGP solamente podían 
retransmitir información de accesibilidad para las redes de su 
sistema autónomo (AS). 
La pasarela debía recoger esta información, habitualmente por 
medio de un Interior Gateway Protocol (IGP), usado para 
intercambiar información entre pasarelas del mismo AS. 
 
 
• Protocolo IS-IS. 
Siglas del inglés Intermediate System to intermediate System) es un protocolo de enrutamiento 
(IGP), que se ejecuta en la capa de enlace de datos (capa 2). 
Utiliza el Algoritmo de Dijkstra y está descrito por el RFC 1142. 
• Protocolo RIP. 
El protocolo RIP (Protocolo de información de encaminamiento) es un protocolo de puerta de 
enlace interna o IGP (Internal Gateway Protocol) utilizado por los routers, derivado del 
protocolo GWINFO de XEROX y que se ha convertido en el protocolo de mayor compatibilidad 
para las redes Internet, fundamentalmente por su capacidad para interoperar con cualquier 
equipo de encaminamiento, aun cuando no es considerado el más eficiente. 
• RIP es un protocolo de enrutamiento por vector de distancia. 
• RIP utiliza el conteo de saltos como su única métrica para la selección de rutas. 
• Las rutas publicadas con conteo de saltos mayores que 15 son inalcanzables. 
• Se transmiten mensajes cada 30 segundos. 
Versiones de RIP: 
• RIP v1: No soporta subredes ni CIDR (Encaminamiento Inter-Dominios sin Clases, estándar 
para la interpretación de direcciones IP). Tampoco incluye ningún mecanismo de 
autentificación de los mensajes. Actualmente en desuso. Se rige por la RFC 1058.

---

### Página 66

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
66 
• RIP v2: Soporta subredes, CIDR y VLSM. Soporta autenticación utilizando uno de los 
siguientes mecanismos: no autentificación, autentificación mediante contraseña, 
autentificación mediante contraseña codificada mediante MD5 (desarrollado por Ronald 
Rivest). Se rige por la RFC 1723-2453. 
• RIPng: RIP para IPv6. Se rige por la RFC 2080. 
Ventajas: 
• RIP es más fácil de configurar (comparativamente a otros protocolos). 
• Es un protocolo abierto (admite versiones derivadas aunque no necesariamente 
compatibles). 
• Es soportado por la mayoría de los fabricantes. 
Desventajas: 
• Su principal desventaja, consiste en que, para determinar la mejor métrica, únicamente 
toma en el número de saltos, descartando otros criterios (AB, congestión, etc.). 
• RIP tampoco está diseñado para resolver cualquier posible problema de encaminamiento. El 
RFC 1720 (STD 1) describe estas limitaciones técnicas de RIP como graves y el IETF está 
evaluando candidatos para reemplazarlo en que OSPF es el favorito. Este cambio, está 
dificultado por la amplia expansión de RIP y necesidad de acuerdos adecuados. 
• IGRP y EGRP. 
IGRP es un protocolo propietario de CISCO de enrutamiento basado en la tecnología vector-
distancia, aunque tiene también en cuenta el estado del enlace. 
Para determinar la mejor ruta Utiliza una métrica compuesta basándose en: 
• El ancho de banda. 
• La confiabilidad. 
• El retardo. 
• La carga del enlace. 
El concepto es que publica destinos con una distancia correspondiente, no necesita saber todas 
las relaciones de ruta/enlace para la red entera. Cada enrutador que recibe la información, 
ajusta la distancia para alcanzar las trayectorias óptimas y la propaga a los routers vecinos. IGRP 
envía, por defecto, las actualizaciones de tablas de encaminamiento de un sistema autónomo en 
particular a intervalos de 90 segundos. 
Al igual que RIP v.1, es un protocolo de encaminamiento classfull o con clase; es decir, no 
permite la utilización de máscaras de red diferentes a las de la propia clase (utiliza las máscaras 
por defecto de cada Clase) y, por tanto, no puede trabajar con máscaras de subred. Por ello 
IGRP ya no se soporta en el sistema operativo de Cisco, que saco una versión mejorada para 
corregir este problema, la versión EIGRP (Enhanced IGRP).

---

### Página 67

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
67 
EIGRP mejora el IGRP utilizando una combinación de los algoritmos de vector-distancia y de 
estado-enlace, además: 
• Incorpora balanceo de carga asimétrico. 
• Utiliza el algoritmo de actualización difusa (dual) para el cálculo de la ruta más corta. 
• Permite operar con redes de gran tamaño. 
• Los cambios en la topología de la red son notificados mediante mensajes de multidifusión. 
 
 
 
 
+ Info 
GRP (Interior Gateway Routing Protocol, o Protocolo de 
enrutamiento de gateway interior) es un protocolo propietario 
patentado y desarrollado por la empresa Cisco Systems que se 
emplea conjuntamente con el protocolo TCP/IP según el modelo 
(OSI) Internet. 
La versión original del IP fue diseñada y desplegada con éxito en 
1986. Utilizado como el Interior Gateway Protocol (IGP) para 
intercambiar datos dentro de un Sistema Autónomo, pero también 
se ha utilizado extensivamente como Exterior Gateway Protocol 
(EGP) para el enrutamiento interdominio. 
 
Protocolos de enrutamiento en el marco OSI 
De acuerdo con el marco de enrutamiento OSI, los protocolos de enrutamiento, son protocolos de 
administración de capas para la capa de red, independientemente de su mecanismo de transporte: 
• IS-IS se ejecuta en la capa de enlace de datos (capa 2). 
• Open Shortest Path First (OSPF) está encapsulado en IP. 
• Solo se ejecuta en la subred IPv4, mientras que la versión IPv6 se ejecuta en el vínculo utilizando 
solo el direccionamiento local de vínculo. 
• IGRP y EIGRP están directamente encapsulados en IP. 
• El EIGRP utiliza su propio mecanismo de transmisión fiable, mientras que el IGRP asume un 
transporte poco fiable.

---

### Página 68

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
68 
• El Protocolo de información de enrutamiento (RIP) se ejecuta sobre el Protocolo de datagramas 
de usuario (UDP). 
• La versión 1 funciona en modo de difusión, mientras que la versión 2 utiliza el direccionamiento 
multidifusión. 
• BGP se ejecuta sobre el Protocolo de control de transmisión (TCP). 
Protocolos de puerta de enlace pueden ser de intercambio interior y exterior: 
• Interior. 
Los protocolos de puerta de enlace interior (IGP) intercambian información de enrutamiento 
dentro de un único dominio de enrutamiento. Ejemplos de IGP incluyen: 
• Abra primero la ruta más corta (OSPF). 
• Protocolo de información de enrutamiento (RIP). 
• Sistema Intermedio a Sistema Intermedio (IS-IS). 
• Protocolo de enrutamiento de puerta de enlace interior mejorada (EIGRP). 
• Exterior. 
Los protocolos de pasarela exterior intercambian información de enrutamiento entre sistemas 
autónomos. Algunos ejemplos son: 
• Protocolo de puerta de enlace exterior (eBPG). 
• Protocolo de puerta de enlace fronteriza (BGP). 
 
 
 
 
+ Info 
Los protocolos de enrutamiento se definen en normas técnicas 
RFC. 
Existen implementaciones de software para la mayoría de los 
protocolos de enrutamiento comunes. 
Algunos ejemplos de aplicaciones de código abierto son: Bird 
Internet routing daemon, Quagga, GNU Zebra, OpenBGPD, 
OpenOSPFDy XORP.

---

### Página 69

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
69 
6.6. Compuerta (Gateway) 
 
Una compuerta que une una red SNA de IBM con una red NetWare de Novell 
Una compuerta actúa como traductor entre sistemas que no utilizan los mismos protocolos de 
comunicaciones, formatos de estructuras de datos, lenguajes y/o arquitecturas. 
Se utilizan cuando las redes son completamente distintas. 
Funcionamiento: 
• Cuando una compuerta recibe un paquete de una red, ésta traduce el paquete del formato 
usado en la red a un formato común entre compuertas. 
• A continuación, lo envía a otra compuerta que lo traduce del formato común al formato usado 
en la red destino y lo envía. 
Normalmente una compuerta se diseña utilizando un ordenador personal dedicado, con varias tarjetas 
de red y programas de conversión y comunicación. 
Debe tener la capacidad suficiente para acoplar velocidades entre las líneas, realizar conversiones de 
protocolo y optimizar la ocupación de las redes. 
7. Power Over Ethernet (POE), POE+ Y POE++ 
Familia de estándares POE 
PoE es una familia de estándares IEEE 802.3 que se utiliza para la transmisión de energía eléctrica junto 
con datos a través de cables Ethernet. Un estándar se aplica a dispositivos de red conectados por cable, 
como cámaras de seguridad, teléfonos IP, puntos de acceso inalámbrico, etc.

---

### Página 70

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
70 
IEEE 802.3af (PoE), IEEE 802.3at (PoE+), IEEE 802.3bt (PoE++) 
El estándar POE original está definido en IEEE 802.3af, y POE+ se define en IEEE 802.3at. 
PoE y sus variantes se centran en la CAPA FÍSICA y en la capa de ENLACE DE DATOS del modelo OSI. 
Estos estándares definen cómo se suministra energía eléctrica a través de los cables Ethernet junto con 
la transmisión de datos. 
Más recientemente, se ha introducido POE++ (también conocido como IEEE 802.3bt), que permite 
suministrar aún más potencia a dispositivos conectados, adecuado para equipos que requieren niveles 
más altos de energía, como cámaras PTZ (Pan-Tilt-Zoom) y otros dispositivos avanzados. 
 La diferencia fundamental entre los estándares PoE es la potencia que son capaces de sumisitrar: 
• PoE(IEEE 802.3af): Hasta 15.4 vatios. 
• PoE+(IEEE 802.3at): Hasta 30 vatios. 
• PoE++(IEEE 802.3bt): Hasta 60 vatios (Tipo 3) y hasta 90 vatios (Tipo 4). 
Beneficios de la entrega de energía a través de cables Ethernet 
Simplificación del Cableado, al transmitirse energía y datos por el mismo cableado se reduce la 
necesidad de cables. Asimismo permite instalar dispositivos donde el acceso a la corriente eléctrica es 
complicado o inexistente. Por ambos motivos el costo de las instalaciones se reduce, pues se ahorran 
fuentes de alimentación y cableado. Se facilitan control y monitorización de la energía pues stán 
centralizadas, hasta el punto de poder regular la potencia o incluso apagar dispositivos abundando en la 
eficiencia energética, pues se pueden llegar a apagar dispositivos que no están en uso. 
8. La globalización 
Todo en las tecnologías de la información avanza rápidamente y está siendo sometida a procesos de 
estandarización globales. 
Un ejemplo de esto es el proyecto oneM2M. 
Es una iniciativa de asociación global para las comunicaciones M2M (Machine to Machine) y la IoT 
(Internet of Things) fundado en 2012 y constituido por 8 de las principales organizaciones mundiales 
de desarrollo de estándares de TIC, en particular: ARIB (Japón), ATIS (Estados Unidos), CCSA (China), 
ETSI (Europa), TIA (EE. UU.), TSDSI (India), TTA (Corea) y TTC (Japón). 
El objetivo de la organización es crear un estándar técnico global para la interoperabilidad con respecto 
a la arquitectura, las especificaciones API, las soluciones de seguridad e inscripción para las tecnologías 
de máquina a máquina e IoT basadas en los requisitos aportados por sus miembros.

---

### Página 71

Redes Locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión 
71 
Las especificaciones estandarizadas producidas permiten que un sistema ecológico sea compatible con 
una amplia gama de aplicaciones y servicios, como ciudades inteligentes, redes inteligentes, 
automóviles conectados, domótica, seguridad pública y salud. 
La tecnología oneM2M está eliminando la fragmentación en el mundo de IoT. Debido a que es 
independiente de la tecnología de conectividad o protocolo que se utiliza para el transporte, está 
diseñada para ser una solución a largo plazo para la implementación de IoT. 
9. Bibliografía 
• Redes de computadoras 5ª edición. Tanenbaum, Wetherall. Editorial Pearson. 
• Transmisión de datos y redes de comunicaciones. Forouzan, B. Editorial MC Graw Hill. 
• https://docplayer.es/3757416-3-topologias-de-red-ist-la-recoleta.html. 
• http://roa.uveg.edu.mx/repositorio/licenciatura/210/Topologasdered.pdf. 
• https://apuntesjulio.com/topologias-de-red/. 
• https://es.slideshare.net/AllanBertran/topologias-de-red-13053210. 
• http://ing.unne.edu.ar/pub/local.pdf. 
• https://es.slideshare.net/LarryRuiz/estndar-ieee-802-15502942. 
• http://www4.ujaen.es/~mdmolina/rrcc/Tema3MAC.pdf. 
• http://jpadilla.docentes.upbbga.edu.co/programa%20redes/Redes%20Datos%205.pdf. 
• https://www.ecured.cu/Protocolo_RIP. 
• https://es.wikipedia.org/wiki/Exterior_Gateway_Protocol 
• https://es.wikipedia.org/wiki/IS-IS 
• https://en.wikipedia.org/wiki/Routing_protocol
