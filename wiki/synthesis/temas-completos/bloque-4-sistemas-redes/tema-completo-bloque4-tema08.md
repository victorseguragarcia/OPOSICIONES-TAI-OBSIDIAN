---
title: "Tema Completo Extendido 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-4
  - tema-08
  - oposiciones-tai
estado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/bloque4-tema08.md]]"
  - "[[wiki/sources/bloque4-tema08]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema07|⬅️ Tema Completo 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema09|Tema Completo 09 ➡️]]

# 🔴 Tema Completo Extendido 08 (Bloque 4): Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema 08 correspondiente al Bloque 4 de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro

---

Internet: Arquitectura de red. 
Origen, evolución y estado 
actual. Principales servicios. 
Protocolos HTTP, HTTPS 
y SSL/TLS 

---

ÍNDICE 
1. Internet 
4 
2. Arquitectura de red de internet 
5 
2.1. Tipos de conexiones entre operadores 
8 
2.2. Intercambiar tráfico entre ISP. IXP 
8 
2.3. DNS 
9 
2.3.1. Estructura de los dominios de Internet 
9 
2.3.2. Tipos de registros DNS 
10 
2.3.3. Funcionamiento del sistema DNS 
12 
3. Origen, evolución y estado actual 
13 
3.1. Origen 
13 
3.2. Evolución 
14 
3.3. Estado actual 
28 
3.3.1. Educación distribuida 
28 
3.3.2. Trabajo colaborativo y remoto 
28 
3.3.3. Servicios de red social 
29 
3.3.4. Búsqueda en Internet 
29 
3.3.5. Impacto social 
30 
3.3.6. Ocio 
32 
3.3.7. Trabajo 
32 
3.3.8. Censura 
33 
3.3.9. Efecto desinhibidor de Internet 
34 
4. Principales servicios de internet 
36 
4.1. Servicio web (WWW) 
36 
4.1.1. Estructura cliente servidor 
36 
4.1.2. Identificadores de recursos 
36 
4.1.3. Páginas web 
38 
4.1.4. Buscadores 
39 
4.1.5. Web 2.0. Herramientas de trabajo colaborativo 
40 
4.1.6. Web 3.0. Web semántica 
42

---

4.2. Webmail 
45 
4.3. Transferencia de ficheros 
46 
4.4. Servicio de acceso remoto 
46 
4.5. Telefonia IP 
47 
4.6. Mensajería instantánea 
51 
4.7. Otros servicios 
52 
5. Protocolo HTTP 
53 
5.1. Versiones 
54 
5.1.1. 0.9 (lanzada en 1991) 
54 
5.1.2. HTTP/1.0 (mayo de 1996) 
54 
5.1.3. HTTP/1.1 (junio de 1999) 
54 
5.1.4. HTTP/1.2 (febrero de 2000) 
55 
5.1.5. HTTP/2 (mayo de 2015) 
55 
5.1.6. HTTP/3 (Octubre de 2018) 
57 
5.2. Descripción de HTTP 
58 
5.2.1. Mensajes 
58 
5.2.2. Métodos de petición 
59 
5.2.3. Códigos de respuesta 
62 
5.2.4. Cabeceras 
63 
5.3. Solicitud HTTP 
65 
5.4. Respuesta HTTP 
69 
5.5. Herramientas 
74 
5.6. Conexiones Keep Alive en HTTP 
76 
6. Protocolo HTTPS 
76 
7. Protocolos (SSL y TLS) 
80 
7.1. Historia y desarrollo 
83 
7.2. Medidas de seguridad de TLS/SSL 
85 
7.3. Puertos en uso 
87 
8. Protocolo OSPF 
87 
9. Bibliografía 
89

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
4 
1. Internet 
El nombre Internet procede de las palabras en inglés Interconnected Networks, que significa "redes 
interconectadas". 
Internet es la unión de todas las redes y computadoras distribuidas por todo el mundo, por lo que se 
podría definir como una red global en la que se conjuntan todas las redes que utilizan protocolos 
TCP/IP y que son compatibles entre sí. 
En internet (también conocida como red de redes) participan dispositivos de todo tipo, desde grandes 
sistemas hasta ordenadores personales o teléfonos móviles. 
En la red se dan citas instituciones oficiales, gubernamentales, educativas, científicas y empresariales 
que ponen a disposición de millones de personas su información. 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ 
 
 
Muchas personas piensan que Internet y la World Wide Web es lo mismo. 
World Wide Web (www) es tan solo uno de los muchos servicios que se ofrecen en internet, 
seguramente el más importante. 
En ella podemos consultar páginas con texto, sonidos, imágenes, videos, etc.) a través de su URL. 
La navegación por las distintas páginas se consigue gracias a los enlaces o links (al pulsarlos te llevan a 
una determinada URL). 
En internet también se ofrecen otros servicios como: 
• FTP: Para descargar o subir archivos. 
• Telnet: Para acceso remoto a otro ordenador.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
5 
• Correo electrónico. 
• Grupos de discusión, foros, chat, etc. 
• Etc. 
El protocolo más utilizado es http, que nos permite la navegación por la World Wide Web. 
2. Arquitectura de red de internet 
Internet es la red de redes, es decir, es una red formada por muchas otras (millones de redes por todo el 
mundo). 
En sus primeros años de existencia, Internet creció en torno a una red llamada NSFNET (National 
Science Foundation NET), que hacía las funciones de red tronca. 
Todas las redes se unían entre sí a través de esta red. 
Si un organismo quería conectarse a Internet debía establecer un enlace con NSFNET. En 1995, NSF 
cedió la función de red troncal a cuatro grandes y comenzó el proceso de descentralización. 
La estructura actual de Internet es jerárquica con varios niveles, conocidos como tiers (tier en inglés 
signivica nivel). 
 
 
 
 
Atención 
Ya vimos el término TIER, con relación a los Centros de Datos. 
Un pequeño truco nemo-técnico: 
• En los Centros de Datos, el TIER con menor numeración es 
de menor categoría. 
• En las redes de INTERNET es al revés: 
Cuanto menor es el número mayor es la categoría de la red. 
 
 
Existen tres niveles en la arquitectura de red de Internet:

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
6 
Tier 1 (nivel 1) 
• Las redes Tier 1 son redes de grandes operadores globales que tienen tendidos de fibra óptica 
como mínimo en dos continentes. 
• Desde una red Tier 1 se puede acceder a cualquier punto de Internet. 
• Cada red Tier 1 está conectada de forma directa al resto de redes Tier 1. 
• Tienen cobertura internacional. 
• Pueden estar conectadas a muchas redes Tier 2. 
• Algunas de las compañías más importantes que poseen redes Tier 1 son: 
• AOL a través de ATDN (AOL Transit Data Network). 
• AT&T. 
• GTT Communications, Inc. 
• KPN International. 
• Verizon. 
• Inteliquent. 
• Deutsche Telekom. 
• NTT Communications. 
• Telefonica International Wholesale Services (TIWS). 
Tier 2 (nivel 2) 
• Las redes Tier 2 son operadores de ámbito regional o nacional. 
• Estas no pueden alcanzar todos los puntos de internet, por lo que necesitan conectarse a una 
Tier 1 para ello. 
• Su principal función es ofrecer servicios de conectividad a los operadores Tier 3. 
• Se conectan a uno o más Tier 1. Deben pagar por usar sus redes. 
• Las redes de Tier 2 se pueden conectar entre sí (mediante acuerdos de peering) de forma que el 
tráfico pueda fluir entre ambas redes sin necesidad de usar una red Tier 1.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
7 
• Ejemplos de operadores Tier 2: 
• China Telecom. 
• Vodafone. 
• British Telecom. 
• Easynet. 
• Fibrenoire. 
• FiberRing. 
Tier 3 (nivel 3) 
• Las redes Tier 3 son ISP (Internet Service Provider) o Proveedores de acceso a Internet para 
empresas y domicilios particulares. 
• No tienen ninguna red. Compran los servicios del Tier 2 pero no tienen infraestructura propia. 
• Ejemplos de operadores Tier 3: 
• MásMóvil. 
• Yoigo. 
• Tuenti.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
8 
2.1. Tipos de conexiones entre operadores 
La conexión entre las redes de diferentes operadores se puede hacer de dos formas: 
• Conexiones de tránsito. 
Conexión entre operadores de diferente jerarquía. 
El operador de mayor jerarquía (proveedor) vende una conexión de tránsito al operador de 
menor jerarquía (cliente). 
El proveedor le da acceso al cliente a todas sus rutas, es decir, el cliente recibirá tanto las rutas 
de la red del proveedor como a rutas con destino a otras redes. 
El cliente publica al proveedor sólo sus rutas y no otras que pueda tener con otros proveedores. 
• Conexión de peering. 
Conexión utilizada para el intercambio de tráfico sin coste entre dos operadores. 
Cada operador publica sólo sus rutas y no otras rutas que tenga con otros proveedores u otras 
rutas de peering. 
Por lo tanto, el peering sirve para acceder desde un operador al rango de direcciones IP del otro 
operador, pero no sirve para llegar a otros rangos de direcciones. 
Puede ser de dos tipos: 
• Públicos: utilizando un IXP. 
• Privados: conexión directa entre los dos proveedores. 
2.2. Intercambiar tráfico entre ISP. IXP 
IXP (Internet eXchange Point o Punto de intercambio de tráfico de Internet) es una infraestructura 
física que permite a diferentes ISP intercambiar tráfico de Internet entre sus redes. 
Este intercambio se lleva a cabo mediante conexiones peering. 
En realidad, cualquier empresa que quiera establecer una conexión pública de peering con un ISP puede 
utilizar un IXP. 
Habitualmente, los acuerdos de peering entre empresas facilitan el intercambio más eficiente de datos 
entre sus redes, es por ello, que los IXP han tenido un impacto muy beneficioso en el crecimiento de 
Internet.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
9 
2.3. DNS 
El Sistema de Nombres de Dominio (Domain Name System o DNS) es una tecnología fundamental en el 
funcionamiento de Internet. Actúa como una base de datos distribuida y jerárquica que traduce 
nombres de dominio legibles por humanos (como google.com) en direcciones IP numéricas (como 
*142.250.184.206*), esenciales para la localización de recursos en la red. Este sistema elimina la 
necesidad de memorizar direcciones IP y facilita la accesibilidad de servicios web. 
El DNS opera bajo un modelo descentralizado, donde los servidores se organizan en niveles para 
responder consultas recursivas o iterativas. Estas consultas utilizan el puerto 53 y pueden emplear tanto 
UDP (para respuestas rápidas y cortas) como TCP (en casos de respuestas extensas o transferencias de 
zona). Un aspecto crítico es el TTL (Time To Live), que define el tiempo de caché de una respuesta 
para evitar sobrecargas en el sistema. 
Entre sus funcionalidades clave destacan: 
• Resolución de registros MX (Mail Exchange): Permite el enrutamiento correcto del correo 
electrónico. Cuando un Mail Transfer Agent (MTA) envía un mensaje, consulta los registros MX 
del dominio destino, que indican los servidores de correo prioritarios y alternativos. 
• DNS Sinkhole: Técnica defensiva que redirige consultas hacia dominios maliciosos a direcciones 
IP controladas, bloqueando así amenazas como malware o botnets. Es común en redes 
corporativas y gubernamentales. 
La propagación de cambios en registros DNS no es inmediata debido a la caché distribuida. La 
actualización sigue un flujo jerárquico: servidores raíz → servidores TLD → servidores de ISPs → 
clientes finales. 
Para acelerar la actualización local, pueden limpiarse las cachés con comandos como ipconfig /flushdns 
(Windows) o sudo systemd-resolve --flush-caches (Linux). 
Puedes comprobar si se ha realizado correctamente, usando antes y después, el comando "sudo 
systemd-resolve –statistics" y comprobando si se han vaciado las estadísticas. 
2.3.1. Estructura de los dominios de Internet 
La arquitectura de los nombres de dominio se organiza en niveles jerárquicos separados por puntos, 
creando un sistema de identificación claro y ordenado para los recursos en Internet. Tomemos como 
ejemplo "www.google.com": aquí distinguimos tres componentes esenciales. El dominio de primer nivel 
(TLD: Top Level Domain) ".com" actúa como categorizador general, indicando la naturaleza comercial 
del sitio. Le sigue "google" como dominio de segundo nivel (SLD: Second Level Domain), el 
identificador único que representa la marca o entidad en la red. Finalmente, el subdominio "www" 
(aunque técnicamente opcional en la web moderna) tradicionalmente identifica el servicio web 
principal. Esta estructura escalable permite crear subdivisiones lógicas como "blog.ejemplo.com" para 
publicaciones o "tienda.ejemplo.com" para comercio electrónico, facilitando tanto la navegación como 
la gestión técnica de servicios diferenciados bajo un mismo dominio principal.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
10 
Clasificación de Dominios de Primer Nivel (TLD) 
Los dominios de primer nivel se clasifican en cuatro categorías principales según su alcance y 
regulación. Los dominios genéricos (gTLD: Generic TLD) como .com, .org y .net representan las 
extensiones más universales. Originalmente concebido para fines comerciales, ".com" se ha convertido 
en el estándar de facto para todo tipo de sitios, mientras ".org" mantiene su asociación tradicional con 
organizaciones sin ánimo de lucro. Estos dominios, al no estar vinculados a territorios específicos, son 
ideales para proyectos de alcance global. 
En contraste, los dominios patrocinados (sTLD: Sponsored TLD) como .edu (para instituciones 
educativas), .gov (entidades gubernamentales), .mil (ejército de Estados Unidos) o .cat (comunidad 
catalana) están gestionados por organizaciones específicas que imponen requisitos estrictos, aportando 
un sello de autenticidad y especialización. 
Dominios Geográficos y Especializados 
Los dominios de código de país (ccTLD: Country Code TLD) como .es (España), .mx (México) o .fr 
(Francia) ofrecen un valioso componente geográfico, siendo herramientas esenciales para el 
posicionamiento local. Algunos ccTLD como .co (Colombia) o .io (Territorio Británico del Índico) han 
trascendido su origen para convertirse en opciones globales, especialmente populares en sectores 
tecnológicos. 
Finalmente, los nuevos dominios genéricos (nTLD: New TDL) como .app, .tech o .blog representan la 
evolución más reciente del sistema, proporcionando extensiones especializadas que permiten nombres 
más descriptivos y memorables para proyectos innovadores. Estas opciones modernas cubren nichos 
específicos y necesidades emergentes, desde aplicaciones móviles (.app) hasta plataformas de 
contenido especializado (.blog), pasando por (.bio) para profesionales independientes. 
Ventajas del Sistema DNS Actual 
La combinación de esta estructura jerárquica con la diversidad de TLDs disponibles crea un sistema 
flexible y potente que satisface las necesidades de identificación digital tanto de grandes corporaciones 
como de pequeños proyectos. El SLD actúa como núcleo de la identidad digital, mientras los 
subdominios permiten una organización interna ilimitada. Paralelamente, la variedad de TLDs ofrece 
opciones para todo tipo de propósitos, desde la localización geográfica hasta la especialización 
temática, demostrando la adaptabilidad del sistema DNS a las cambiantes necesidades del mundo 
digital. Esta arquitectura, aparentemente simple pero extraordinariamente versátil, sigue siendo 
después de décadas la base técnica que hace posible navegar Internet de forma intuitiva. 
2.3.2. Tipos de registros DNS 
Los registros DNS son entradas en zonas de autoridad que definen las propiedades de un dominio. Los 
más relevantes incluyen:

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
11 
Registros A y AAAA: La Base de la Resolución DNS 
Los registros A (Address) constituyen el cimiento del sistema DNS, estableciendo la relación directa 
entre un nombre de dominio y su correspondiente dirección IPv4. Por ejemplo, el registro A para 
"ejemplo.com" podría apuntar a "192.0.2.1". Con el agotamiento de direcciones IPv4, los registros 
AAAA (quad-A) han ganado importancia al mapear dominios a direcciones IPv6, como "2001:db8::1". 
Estos registros son imprescindibles para cualquier servicio web, permitiendo que los navegadores 
encuentren los servidores correctos. Cuando se modifica la IP de un servidor, actualizar estos registros 
es crucial para mantener la accesibilidad del sitio. 
Registros CNAME: Aliases y Redirecciones Inteligentes 
Los registros de Nombre Canónico (CNAME) funcionan como alias que apuntan a otro nombre de 
dominio en lugar de a una dirección IP directa. Un caso típico sería "www.ejemplo.com" CNAME 
"ejemplo.com", centralizando las actualizaciones en un solo registro. Esta característica es 
particularmente útil para servicios en la nube, donde múltiples subdominios pueden apuntar a un mismo 
endpoint sin necesidad de conocer las IPs subyacentes. Sin embargo, es importante evitar cadenas 
largas de CNAMEs, ya que incrementan el tiempo de resolución y pueden afectar el rendimiento. 
Registros MX: El Corazón del Correo Electrónico 
Los registros Mail Exchange (MX) son esenciales para la entrega de correo electrónico, especificando 
los servidores responsables de gestionar los mensajes entrantes para un dominio. Cada registro MX 
incluye una prioridad numérica (preferencia), donde valores más bajos indican mayor prioridad. Por 
ejemplo, "10 mail1.ejemplo.com" y "20 mail2.ejemplo.com" crean un sistema redundante: si el servidor 
primario falla, los mensajes se enviarán al secundario. La correcta configuración de estos registros es 
vital para garantizar la entrega confiable de correos y prevenir pérdidas de mensajes. 
Registros PTR: Resolución Inversa y Reputación 
Mientras los registros A/AAAA resuelven nombres a IPs, los registros Pointer (PTR) realizan el proceso 
inverso: mapean direcciones IP a nombres de dominio. Esta funcionalidad es crítica para sistemas de 
autenticación de correo, donde muchos servidores verifican los registros PTR para combatir el spam. En 
entornos corporativos, los PTRs bien configurados mejoran la trazabilidad de la red y facilitan el 
diagnóstico de problemas. Por ejemplo, un servidor web con IP "203.0.113.45" debería tener un PTR 
que resuelva a un nombre de dominio válido, preferiblemente coincidente con su registro A 
correspondiente. 
Registros NS: La Autoridad DNS Delegada 
Los Name Server (NS) registran qué servidores DNS tienen autoridad sobre un dominio particular. 
Cuando se registra un dominio, estos registros apuntan típicamente a los DNS del proveedor de hosting 
o a servicios especializados como Cloudflare o Route 53. Una configuración típica incluye registros 
primarios y secundarios para redundancia, como "ns1.proveedor.com" y "ns2.proveedor.com". Es 
fundamental mantener estos registros actualizados durante migraciones de DNS, ya que errores aquí 
pueden hacer que un dominio deje de ser accesible completamente.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
12 
Registros TXT: Versatilidad y Seguridad 
Los registros de texto (TXT) ofrecen flexibilidad para múltiples propósitos, especialmente en seguridad 
y autenticación. Son esenciales para implementar políticas anti-spam como SPF (Sender Policy 
Framework), que especifica qué servidores pueden enviar correo para un dominio. Los registros DKIM 
(DomainKeys Identified Mail) usan TXT para almacenar claves públicas que verifican la autenticidad de 
los mensajes. Más recientemente, DMARC utiliza TXT para definir políticas de manejo de correos no 
autenticados. Estos registros también se emplean para verificación de propiedad de dominios con 
servicios como Google Workspace o Microsoft 365. 
2.3.3. Funcionamiento del sistema DNS 
El proceso de resolución DNS implica una cadena de consultas entre servidores jerárquicos: 
Consulta inicial (Cliente a Resolver recursivo) 
Cuando un usuario introduce un nombre de dominio como "ejemplo.com" en su navegador, su 
dispositivo envía una consulta al servidor DNS recursivo, que normalmente es proporcionado por el 
proveedor de servicios de Internet (ISP). Este servidor recursivo actúa como intermediario, verificando 
primero si tiene la respuesta almacenada en su caché. De ser así, devuelve inmediatamente la dirección 
IP correspondiente. Si no tiene la información en caché, inicia el proceso de resolución completo. 
Consulta a los servidores raíz (Resolver a Servidores raíz) 
El servidor recursivo, al no encontrar la respuesta en su caché, realiza una consulta a los servidores raíz 
DNS. Existen 13 grupos de estos servidores distribuidos globalmente, identificados desde a.root-
servers.net hasta m.root-servers.net. Estos servidores raíz no proporcionan directamente la dirección IP 
solicitada, pero indican al resolutor dónde puede encontrar la información para el dominio de primer 
nivel correspondiente (en este caso, .com). 
Consulta a los servidores TLD (Resolver a Servidores TLD) 
Con la información obtenida de los servidores raíz, el resolutor recursivo contacta entonces con los 
servidores responsables del dominio de primer nivel específico (.com en nuestro ejemplo). Estos 
servidores TLD tampoco almacenan la dirección IP final, pero pueden indicar cuáles son los servidores 
DNS autoritativos para el dominio "ejemplo.com". 
Consulta final al servidor autoritativo 
El resolutor recursivo se dirige entonces a los servidores DNS autoritativos del dominio "ejemplo.com". 
Estos servidores, que son los responsables últimos de la información sobre ese dominio específico, 
proporcionan finalmente la dirección IP asociada al nombre de dominio solicitado. Esta información 
incluye típicamente registros como el registro A (para IPv4) o AAAA (para IPv6).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
13 
Respuesta al cliente y almacenamiento en caché 
Una vez obtenida la dirección IP del servidor autoritativo, el resolutor recursivo la devuelve al cliente 
que originó la consulta. Además, almacena esta información en su caché durante un período 
determinado (conocido como TTL o Time To Live) para agilizar futuras consultas al mismo dominio. 
Este mecanismo de caché es fundamental para optimizar el rendimiento del sistema DNS y reducir la 
carga en los servidores. 
Este proceso de resolución distribuido ofrece importantes ventajas. La estructura jerárquica permite 
una gran escalabilidad, distribuyendo la carga entre múltiples servidores. El sistema es redundante, lo 
que significa que el fallo de un servidor no impide el funcionamiento general, ya que existen múltiples 
instancias de cada tipo de servidor. Además, el uso generalizado de cachés en los resolutores recursivos 
mejora significativamente la eficiencia del sistema, reduciendo los tiempos de respuesta para consultas 
frecuentes. 
3. Origen, evolución y estado actual 
Internet avanza a un ritmo imparable en su desarrollo, seguramente cuando termines la lectura de 
esta unidad, ya habrá alguna novedad al respecto. 
Vamos a ver, su origen, evolución y el estado actual que seguirá avanzando… 
3.1. Origen 
En 1958 se fundó la ARPA (Advanced Research Projects Agency o Agencia para los Proyectos de 
Investigación Avanzada) en los EE.UU. 
Compuesta por unos 200 científicos, su intención era conseguir la comunicación entre ordenadores. 
Así en 1967 nació ARPANET (Advanced Research Projects Agency Network o Red de la Agencia de 
Proyectos de Investigación Avanzada), que conectaba las universidades de Standford y UCLA. 
ARPA era un programa financiado por el PENTAGONO, por lo que al principio en la misma conexión se 
encontraban organizaciones militares y civiles, pero en 1983, por motivos de seguridad, se separan en 
ARPANET para uso civil y MILNET para uso militar. 
Por fin en 1972 aparece INTERNET con el nacimiento del InterNetworking Working Group, 
organización encargada de administrar Internet.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
14 
3.2. Evolución 
Vamos a ver de manera cronológica los acontecimientos que han influenciado en la creación y evolución 
de internet hasta su instauración en las casas de los usuarios. 
1958 
• El Departamento de Defensa de E.E.U.U. crea ARPA (Advanced Research Projects Agency) para 
conseguir el liderazgo americano en la ciencia y la tecnología aplicada al campo militar. 
• La compañía BELL crea el primer módem que permitía transmitir datos binarios sobre una línea 
telefónica simple. 
1961 
• Leonard Kleinrock, del MIT, publicó el primer paper sobre la teoría del "packet switching" (PS o 
conmutación de paquetes). 
La idea fundamental era que en las comunicaciones, era mucho más eficiente usando paquetes 
que enviando toda la conversación por un circuito virtual. 
1962 
• Inicio de investigaciones por parte de ARPA, una agencia del ministerio estadounidense de 
defensa. 
• Licklider (MIT), primer responsable de "computer research program", introduce el concepto de 
"Galactic Network" en que los ordenadores están interconectados y los usuarios podían acceder 
rápidamente a sus datos y/o programas. 
1964 
• Leonard Kleinrock publica un libro sobre la comunicación por conmutación de paquetes para 
implementar una red. 
• Paul Baran escribe un paper ("On distributed Communications Networks" donde se habla de 
cómo securizar las transmisiones de voz para el ejército. 
1965 
• Primera red WAN del mundo. 
Thomas Merrill y Lawrence G. Roberts conectan un TX-2 del MIT (Massachussets, Boston) con 
un AN/FSQ-32 en System Development Corporation (Santa Mónica, California) mediante una 
línea telefónica a 1200 bps (sin circuitos virtuales ni paquetes).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
15 
Demostraron: 
• Que los ordenadores podían trabajar conjuntamente. 
• Que los circuitos telefónicos no eran adecuados. Debía utilizarse la teoría del "packet 
switching". 
1966 
• Primer plan de ARPANET. 
Lawrence G. Roberts llega al MIT para desarrollar el concepto de red de ordenadores que se 
convierte en el primer Plan de ARPANET. 
 
 
 
 
+ Info 
Hay una leyenda urbana que dice que ARPANET se desarrolló para 
sobrevivir a un ataque nuclear. 
Prácticamente se puede asegurar que esto no es cierto. 
 
1967 
Lawrence Roberts expone en un simposio de la ACM el primer diseño formal de ARPANET. La 
conmutación de paquetes que adopta el proyecto se basa en investigaciones previas de Paul Baran 
(RAND) y Donald Davies (NPL), desarrolladas de forma independiente. 
1968 
• Se presentan oficialmente las redes paquetes a ARPA. 
• ARPA encarga a BBN (grupo liderado por Frank Heart en Bolt Beranek y Newman) el desarrollo 
de los IMPs (Interface Message Processors). 
• Network Análisis Corporation (NAC) se encarga del diseño de la topología y arquitectura de red 
(con Roberts y Frank Heart a la cabeza). 
• El equipo de Kleinrock se encargará, desde UCLA, de los equipos de medición y control de la red 
(Network Measurement Center).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
16 
1969 
• ARPANET pasa de ser un plan teórico a convertirse en un proyecto real y operativo. Se instalan 
los primeros IMP (Interface Message Processors) y se conectan los cuatro nodos iniciales en 
UCLA, SRI, UCSB y la Universidad de Utah. Desde UCLA se transmite el primer mensaje 
experimental ("LO"), marcando el inicio efectivo de la red. 
• Arranca MERIT. 
Comienza a funcionar la red MERIT, basada en X.25, destinada a dar servicio a la comunidad 
académica más allá de los proyectos financiados por ARPA. 
1970 
• Aparece el UNIX. 
• Crece el número de nodos y se hace necesario un protocolo de conexión. 
• Protocolo Host-to-Host. 
El Network Working Group (NWG), bajo dirección de S. Crocker, publica "Host-Host 
Comunication Protocol in the ARPA Network", conocido como NCP (Network Control 
Protocol), el antecesor del TCP/IP. 
• Desarrollo de ALOHA. 
En la Univ. De Hawai se desarrolla el protocolo ALOHA, que será el protocolo usado en 
ALOHAnet. 
Es el antecesor de las futuras redes locales y, por tanto, de ethernet. 
Protocolo entre islas, con detección de colisiones y teniendo a la radio como medio de 
transmisión. 
1971 
• 15 nodos conectados a ARPANET. 
1972 
• Correo electrónico. 
Ray Tomlinson (BBN) crea el correo electrónico en ARPANET. 
Surge por necesidad de comunicarse y como método de coordinación.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
17 
• Nacimiento del InterNetworking Working Group, grupo de trabajo internacional, no formal, 
dedicado al estudio y estandarización de protocolos para la interconexión de redes. 
• Primer chat entre ordenadores. 
• Aparece la idea de "open-architecture" para comunicar redes distintas. 
1973 
• TCP/IP. 
Kahn desarrolla el protocolo TCP/IP (Transmisión Control Protocol/ Internet Protocol): 
• Cada red es independiente y no debe necesitar cambios si otra se conecta/desconecta de 
ARPANET. 
• Basados en "best-effort". Si un paquete no llega al destino, debe ser revisado al poco 
tiempo. 
• Cajas negras que interconecten las redes, que no almacenen información sobre las 
conexiones que están fluyendo a través suyo. 
• No existirá un control central a nivel de operación. 
• Se asignan 32 bits para el direccionamiento (no pensaban la repercusión que tendría y que 
esto sería insuficiente en el futuro). 
• ETHERNET. 
Bob Metcalfe escribe un informe en el que describe una red Ethernet. 
Inicialmente esta red se llamaba "Alto Aloha Network". 
Ether proviene de la teoría de la época según la cual las ondas electromagnéticas viajaban por 
un fluido llamado éter. 
Esta ethernet experimental tenía las características fundamentales de la actual y funcionaba a 
2.94 Mbps. 
1974 
• Especificación / Implementación TCP/IP. 
Esto permite que se implemente el protocolo perfectamente pero sólo para grandes 
ordenadores. 
• BBN abre Telenet (versión comercial de ARPANET).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
18 
1975 
• Primera lista de correo. 
• MSG, primer programa completo de correo. 
• Enlaces de satélite. 
Se hacen las primeras pruebas de enlaces de satélite de larga distancia. 
• Pruebas TCP/IP. 
Se hacen pruebas entre Stanford, BBN y UCL. 
• Primer router. 
Creados por David Boggs en Xerox PARC. 
1976 
• AT&T desarrolla el UUCP (Unix-to-Unix Copy) para UNIX. 
• INTEL desarrolla el 8080. 
• Se publica en Comms de ACM "Ethernet: Distributed Packet Switching for Local Computer 
Networks". 
• Xerox crea SDD (Systems Development Division) para el desarrollo de PCs y de la red Ethernet. 
1977 
Xerox recibe patente de Ethernet. 
1978 
• TCP, IP y UDP. 
Se define: 
• UDP. 
Los paquetes se pueden perder. 
• IP. 
Permite el direccionamiento y envío de paquetes. 
• TCP. 
Se preocupa de la organización, flujo y recuperación de errores.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
19 
1979 
• Aparece USENET. 
• Uso de emoticones en MsgGroup. 
• Aparece 3COM (Computers, Communications and Compatibility). 
Metcalfe abandona Xerox para crear 3COM. 
1980 
• Ethernet v.1.0. 
Especificaciones desarrolladas por la alianza (DEC-Intel-Xerox). 
Velocidad 10 Mbps. 
• Explosión en el uso de redes locales. 
• El departamento de defensa de E.E.U.U. adopta el TCP/IP como estándar. 
1981 
• Aparece BITNET ("Because It's Time NETwork"). 
• Aparece CSNET (Computer Science NETwork). 
• Primer IBM PC con procesadores 8088. 
• Se establecen las redes IP clase A, B y C. 
• Se produce la transición de NCP a TCP. 
1982 
• TCP/IP se establece como protocolo base de Internet. 
• ARPA establece el TCP/IP como el protocolo base de ARPANET y, por tanto, se da una primera 
definición de qué es Internet: una red TCP/IP que conecta otras redes TCP/IP más pequeñas. 
• Ethernet v.2.0. 
• Xerox libera la marca Ethernet. 
• EGP. 
Se define EGP (Exterior Gateway Protocol) como el protocolo que utilizarán para comunicarse 
los gateways entre distintas redes.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
20 
1983 
• Nacimiento de Internet. 
• El 1 de enero de 1983 ARPANET adopta TCP/IP como protocolo obligatorio, lo que permite la 
interconexión de redes independientes y marca el nacimiento de Internet como red global. 
• MILNET. 
• ARPANET se divide en una red de uso civil (ARPANET) y otra militar (MILNET), manteniendo 
pasarelas de interconexión para garantizar la comunicación entre ambas. 
• Pasarela CSNET/ARPANET. Se establecen mecanismos de conexión entre ARPANET y CSNET, 
ampliando el acceso a universidades y centros de investigación. 
• Estaciones UNIX con TCP/IP. Aparecen estaciones de trabajo basadas en UNIX con soporte 
TCP/IP integrado, facilitando la expansión del nuevo protocolo. 
• Estándares IEEE. 
• El IEEE aprueba los estándares: 
• 802.3 (CSMA/CD para Ethernet). 
• 802.4 (Token Bus). 
• 802.5 (Token Ring). 
• DNS. Debido a la imposibilidad de mantener una tabla centralizada de nombres, Paul 
Mockapetris define el Domain Name System (DNS) en las RFC 882 y 883. DNS introduce el 
sistema jerárquico de nombres, servidores distribuidos, zonas y delegación de autoridad, 
reemplazando el archivo HOSTS y permitiendo una resolución distribuida, escalable y adecuada 
para el crecimiento de Internet. 
1984 
• 1000 máquinas conectadas. 
• Apple lanza el Macintosh. 
• Más redes académicas. 
• La URSS se conecta a USENET.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
21 
1985 
• Se crea el programa NSFNET. 
NSFNET nace con el propósito de dar servicio a la comunidad universitaria al completo. 
• Primeros dominios de Internet. 
sysmbolics.com es el primer dominio de internet. 
1986 
• NSFNET entra en funcionamiento. 
• Se financian infraestructuras y conexiones transoceánicas. 
• CSNET y ARPANET comparten infraestructura. 
• NNTP. 
Se desarrolla el protocolo NNTP (Network News Transfer Protocol) para mejorar/adaptar la 
transferencia de News a través de TCP/IP. 
• Registros MX. 
Se desarrollan los registros MX de forma que, aunque no se tuviese una dirección IP se pudiese 
recibir correo electrónico. 
1987 
• Primer ISP privado: UUNet. 
UUNet es el primer operador privado (ISP) y su propósito inicial es dar conectividad comercial 
(no académica) UUCP y a USENET. 
1988 
• Primer gusano de Internet. 
• Se crea el CERT (Computer Emergency Response Team). 
• DoD elige OSI. 
El Departamento de Defensa de E.E.U.U. especifica el modelo OSI. 
Aunque es un estándar teórico, no llegó a implantarse.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
22 
• Se crea IANA (Internet Assigned Numbers Authority). 
IANA se encarga de asignar y controlar el espacio de direccionamiento en internet. 
• Aparece el IRC. 
• Primer túnel multicast. 
1989 
• 100.000 hosts. 
• Se ponen un funcionamiento los primeros intercambiadores de correo electrónico entre 
Internet y las redes comerciales existentes. 
1990 
• Desaparece ARPANET. 
Ya solo se habla de internet. 
1991 
• Se crea Gopher. 
Primer servicio de internet para la navegación web a través de menús en forma de árbol. 
• WWW. Tim Berners-Lee, del CERN, presenta oficialmente el World Wide Web y consigue que 
CERN libere completamente el código y se comprometa a no cobrar por el uso de la tecnología. 
1992 
• 1.000.000 de hosts. 
• Se crea NCC (Network Coordination Center) para controlar la asignación de IPs en Europa. 
1993 
• NSF crea InterNIC para dar servicios de internet: 
• Base de datos y directorio, AT&T. 
• Registro, Network Solutions. 
• Información, CERFnet.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
23 
• Aparece Mosaic, el primer navegador gráfico multiplataforma con versiones para UNIX, Mac y 
Windows. 
• Primer buscador de la historia, Wandex servía como un índice de páginas web. 
1994 
• La Web -www, basada en HTTP y HTML, se populariza a partir de 1993 y, hacia 1994, llega a 
superar a FTP como principal forma de acceder y publicar información en Internet. 
• ARPANET/Internet cumple 25 años. 
• Aparecen las primeras tiendas en Internet. 
• Primer SPAM. 
• Aparece Netscape (será el sucesor de Mosaic). 
1995 
• SUN lanza JAVA. 
• Microsoft lanza Windows 95. 
• Real Audio lanza la tecnología streamming. 
• Internet para el usuario final. Empieza a llegar a las casas. 
• Desaparece la NSFNET. 
1996 
• 10 millones de ordenadores conectados. 
1998 
• Nace Google (indexación PageRank): revoluciona la búsqueda de información y el 
posicionamiento en la Web. 
2000 
• El NASDAQ alcanzó su máximo histórico el 10 de marzo de este año y en año y medio perdió el 
78 % de su valor, estallando la burbuja de las .com.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
24 
2001 
• Nace Wikipedia. 
2003 
• Se lanzan Safari, MySpace, LinkedIn, Skype, Wordpress e iTunes Store. 
• Wi-Fi 802.11g homologado: empieza la proliferación de redes domésticas y hotspots. 
2004 
• Nace Gmail, Facebook, Flickr y Vimeo. 
2005 
• Internet alcanza los MIL MILLONES de usuarios mundiales. 
• Nace YouTube. 
2007 
• Apple presenta el iPhone; la Web se rediseña para pantallas táctiles. 
2008 
• Se lanza CHROME (de Google). 
• App Store abre la vía a la economía de apps. 
2009 
• Se generaliza el diseño web adaptado a pantallas táctiles tras la expansión del iPhone y los 
smartphones. 
2010 
• Nace Instagram (solo para Apple). 
• Nace Pinterest.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
25 
2011 
• IANA entrega los últimos bloques de IPv4. 
• Cloudflare y otros proveedores populares de CDN extienden el uso de redes anycast para 
distribuir contenido y mitigar ataques. 
2012 
• Internet alcanza los 2,400 millones de usuarios mundiales. 
2013 
• Boom de los métodos de pago a través de internet. 
• Snowden revela el programa PRISM: se generaliza el cifrado HTTPS y nace el movimiento 
"Encrypt all the things". 
2014 
• Google anuncia que HTTPS será "ranking signal" (aún < 50 % de la Web). 
• Se anuncia Let's Encrypt, proyecto que en 2015 empezará a emitir certificados TLS gratuitos y 
automatizados. 
• Facebook compra WhatsApp, consolidando el dominio de las plataformas móviles. 
2015 
• Despliegue masivo del 4G LTE a nivel mundial. 
• Let's Encrypt entra en producción: los certificados TLS gratuitos se masifican. 
• Despliegue mundial de IPv6 por los grandes CDNs (Google, Facebook, LinkedIn); el tráfico IPv6 
supera el 10 %, aunque la escasez de IPv4 sigue presente. 
• Google presenta AMP (Accelerated Mobile Pages). 
• YouTube alcanza los mil millones de horas vistas al día.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
26 
2016 
• Se populariza el término "fake news" tras elecciones de EE.UU.; se crean los primeros 
observatorios de desinformación. 
• Lanzamiento de TikTok (Douyin en China). 
• Gran ataque DDoS mediante botnets IoT (Mirai), marcando un antes y un después en 
ciberseguridad. 
2017 
• Se popularizan masivamente los asistentes de voz (Alexa, Google Home). 
• Se implanta el protocolo HTTP/2 en la mayoría de navegadores. 
• Equifax sufre una de las mayores brechas de datos de la historia. 
2018 
• Entra en vigor el RGPD europeo, redefiniendo la protección de datos en Internet. 
• Escándalo Cambridge Analytica: uso indebido de datos de Facebook. 
• YouTube supera por primera vez a la TV en consumo entre jóvenes. 
• Se generaliza TLS 1.3 (RFC 8446) – 0-RTT, menos latencia, más privacidad; es la razón técnica 
real por la que HTTPS "va rápido". 
2019 
• Despliegue inicial del 5G en varios países. 
• WebAssembly se convierte en estándar, ampliando las capacidades del navegador. 
• Twitch domina el streaming en directo y supera récords de audiencia global. 
2020 
• La pandemia global dispara el uso de Internet: videoconferencias, teletrabajo y educación 
online. 
• Zoom multiplica su uso por 30 y se convierte en plataforma dominante. 
• Explosión del comercio electrónico y los servicios de streaming.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
27 
2021 
• Explosión del mercado NFT y auge de blockchain en plataformas de consumo. 
• Se publica QUIC (RFC 9000) → HTTP/3; Google, Cloudflare y Facebook lo tienen ya en 
producción. 
• Facebook anuncia su transición a Meta y populariza el término "metaverso". 
• Incremento de ataques ransomware a escala mundial. 
2022 
• Twitter es adquirido por Elon Musk, generando cambios masivos en la plataforma. 
• Se lanza ChatGPT, abriendo la era de la IA generativa de acceso masivo. 
• TikTok se convierte en la red social más descargada del mundo. 
• Se empieza a medir (APNIC/RIPE) que el 50 % del tráfico mundial ya circula por móvil, pero el 
80 % de ese tráfico acaba yendo por "fijo" (fibra o cable) en el tramo metro/core. 
2023 
• Google presenta Bard; Microsoft integra GPT-4 en Bing y en Office. 
• Por primera vez, más del 50 % de las páginas vistas y del tiempo de navegación proviene de 
dispositivos móviles; en volumen de datos el 'fijo' sigue siendo la mayoría. 
• Se generalizan los sistemas de verificación automática de identidad digital. 
2024 
• La IA generativa se integra nativamente en navegadores, sistemas operativos y móviles. 
• Aumentan las regulaciones globales de IA (UE: AI Act). 
• Las redes de fibra de 10 Gbps comienzan su despliegue doméstico en varios países. 
2025 
• La Web3 empieza a consolidarse con usos reales en identidad digital y trazabilidad. 
• La IA multimodal se vuelve estándar en herramientas de productividad y educación. 
• Continúa la expansión del 5G avanzado y comienzan pruebas de 6G en Asia y Europa.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
28 
3.3. Estado actual 
Internet ofrece muchas aplicaciones y servicios, sobre todo la World Wide Web, incluidas las redes 
sociales, el correo electrónico, las aplicaciones móviles, los juegos multijugador en línea, la telefonía por 
Internet, el intercambio de archivos y los servicios de transmisión de medios. 
La mayoría de los servidores que brindan estos servicios actualmente están alojados en centros de 
datos, y a menudo se accede al contenido a través de redes de distribución de contenido de alto 
rendimiento. 
3.3.1. Educación distribuida 
Se puede encontrar material didáctico a todos los niveles, desde preescolar hasta post-doctoral, todo 
ello está disponible en sitios web. 
Los métodos van desde CBeebies (canal de televisión abierta británico propiedad de la BBC dirigida a 
niños menores de 6 años que ofrece una mezcla de programación educativa y de entretenimiento), a 
recursos escolares y de secundaria, guías de revisión, universidades virtuales, hasta el acceso a la gama 
alta de literatura académica a través del programa de Google Académico. 
También se encuentran recursos para la educación a distancia, ayuda con las tareas y otras 
asignaciones, el autoaprendizaje guiado, entretenimiento o simplemente buscar más información sobre 
un hecho interesante. 
Nunca ha sido más fácil para cualquier persona de cualquier edad, acceder a la información educativa en 
cualquier nivel, desde cualquier lugar. El Internet en general es un importante facilitador de la educación 
tanto formal como informal. 
3.3.2. Trabajo colaborativo y remoto 
El bajo costo y el intercambio casi instantáneo de las ideas, conocimientos y habilidades han hecho el 
trabajo colaborativo definitivamente más fácil, con la ayuda del software de colaboración. 
El chat, ya sea en forma de una sala de chat IRC o del canal, a través de un sistema de mensajería 
instantánea, o un sitio web de redes sociales, permite a los colegas mantenerse en contacto de una 
manera muy conveniente cuando se trabaja en sus computadoras durante el día. 
Los mensajes pueden ser intercambiados de forma más rápida y cómodamente por medio del correo 
electrónico. Estos sistemas pueden permitir que los archivos se intercambien, que dibujos e imágenes 
puedan ser compartidos, y también que se puedan comunicar mediante la voz y por vídeo los miembros 
de un equipo. 
Los sistemas de gestión de contenido permiten la colaboración de los equipos, y trabajar 
conjuntamente en documentos compartidos al mismo tiempo, sin destruir accidentalmente el trabajo 
del otro.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
29 
Los equipos de negocio y el proyecto pueden compartir calendarios, así como documentos y otra 
información. 
Esta colaboración se produce en una amplia variedad de áreas, incluyendo la investigación científica, el 
desarrollo de software, la planificación de una conferencia, el activismo político y la escritura creativa. 
La colaboración en masa está cada vez más generalizada, así como el acceso a Internet y la difusión 
de conocimientos de informática 
Internet permite a los usuarios de computadoras acceder remotamente a otros equipos y almacenes de 
información fácilmente, donde quiera que estén. Pueden hacer esto con o sin la seguridad informática, 
es decir, la autenticación y el cifrado, dependiendo de los requerimientos. Esto es alentador, nuevas 
formas de trabajo, la colaboración y la información en muchas industrias. 
3.3.3. Servicios de red social 
Servicio de red social (en inglés Social Networking Services, SNS). 
SNS, es un medio social que permite establecer contacto con otras personas por medio de una 
plataforma web. 
Está conformado por un conjunto de equipos, servidores, programas, conductores, transmisores, 
receptores, y sobre todo por personas que comparten alguna relación, principalmente de amistad y 
estas mantienen intereses y actividades en común o se encuentran interesados en explorar los intereses 
y las actividades de otros usuarios. 
Genralmente, las redes sociales se usan para poder comunicarse con grupos de personas de diferentes 
países sin las limitaciones convencionales del correo electrónico o las llamadas telefónicas y 
Videoconferencia, en los cuales aunque existen servicios que permiten conversaciones grupales, no 
otorgan el tiempo, el espacio o determinadas herramientas que disponen los servicios de redes sociales. 
Los servicios de redes sociales son frecuentemente utilizados por medio de ordenadores, tabletas y 
teléfono móviles. 
3.3.4. Búsqueda en Internet 
Para buscar información no es suficiente tener un ordenador u otro dispositivo con acceso a 
internet, sino que se necesitan estrategias para encontrar lo que se está buscando y determinar si el 
resultado encontrado es pertinente y confiable.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
30 
Los usuarios debemos asumir un rol de guías, acompañando y asesorando ante una situación de 
búsqueda de información ya que a veces aun teniendo estrategias y recurriendo a sitios confiables los 
resultados pueden no ser los esperados. 
Así mismo, es necesario entender que cada buscador establece sus propios criterios de búsqueda, 
siendo en general el de colocar en primer lugar la página más buscada, que no es necesariamente la más 
precisa, sino que se trata de un criterio de popularidad, o también pueden aparecer destacadas aquellas 
que han pagado por ese lugar. 
No conocemos todos los criterios que los buscadores establecen; pero, entender que esos criterios son 
arbitrariamente definidos por las empresas propietarias de esos buscadores, le quita a los mismos el 
estatus de "todopoderoso", y provoca que quien realiza la búsqueda deba ser más crítico para decidir 
con qué resultado quedarse, o para redefinir las búsquedas intentando mejorarlas. 
 
 
 
 
Anécdota 
En un artículo publicado en 2007, analizan búsquedas de diferentes 
estudiantes y entre sus conclusiones manifiestan: "se torna 
imprescindible diseñar condiciones de enseñanza para que las 
interpretaciones que realizan en sus búsquedas y los criterios de 
selección que elaboran sean objeto de reflexión colectiva y de 
intervenciones precisas de los docentes." 
 
 
Internet, es un gran espacio de almacenamiento de información, se tiene la idea de que "todo está en 
Internet", pero hay que tener siempre muy en cuenta, que cada material disponible tiene uno o varios 
autores, que deben ser citados o consultados para poder utilizar sus materiales. Para facilitar esta, 
existen las licencias abiertas y/o libres para obras culturales, científicas y educativas (textos, imágenes, 
audios, videos, etc.). Dichas licencias no inhabilitan los derechos de autor, simplemente dejan 
predefinido los permisos de uso. 
3.3.5. Impacto social 
Internet tiene un impacto profundo en el mundo laboral, el ocio y el conocimiento a nivel mundial. 
Gracias a la web, millones de personas tienen acceso fácil e inmediato a una cantidad extensa y diversa 
de información en línea. Este nuevo medio de comunicación logró romper las barreras físicas entre 
regiones remotas. 
Sin embargo, el idioma continúa siendo una dificultad importante.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
31 
Si bien en un principio nació como un medio de comunicación unilateral destinado a las masas, su 
evolución en la llamada Web 2.0 permitió la participación de los ahora emisores-receptores, creándose 
así puntos de encuentro en el espacio digital. 
Comparado a las enciclopedias y a las bibliotecas tradicionales, la web ha permitido una 
descentralización repentina y extrema de la información y de los datos. 
Algunas compañías e individuos han adoptado el uso de los weblogs, que se utilizan en gran parte como 
diarios actualizables, ya en decadencia tras la llegada de las plataformas sociales. 
La automatización de las bases de datos y la posibilidad de convertir cualquier ordenador en una 
terminal para acceder a ellas, ha traído como consecuencia la digitalización de diversos trámites, 
transacciones bancarias o consultas de cualquier tipo, ahorrando costos administrativos y tiempo del 
usuario. 
Esto también ha permitido la creación de proyectos de colaboración mundial en la creación de software 
libre y de código abierto (FOSS), por ejemplo: 
• La Free Software Foundation con sus herramientas GNU y licencia de contenido libre. 
• El núcleo de sistema operativo Linux. 
• La Fundación Mozilla con su navegador web Firefox y su lector de correos Thunderbird. 
• La suite ofimática Apache OpenOffice. 
• Y la propia Fundación Wikimedia. 
Internet se extendió globalmente, pero, de manera desigual. 
Floreció en gran parte de los hogares y empresas de países ricos, mientras que países y sectores 
desfavorecidos cuentan con baja penetración y velocidad promedio de Internet. 
La inequidad del acceso a esta nueva tecnología se le conoce como brecha digital, lo que repercute 
menores oportunidades de conocimiento, comunicación y cultura. 
Esta "brecha digital", repercute en menores oportunidades de conocimiento, comunicación y cultura, 
aunque se observa un crecimiento sostenido tanto en la posibilidad de uso y velocidad de Internet, 
implementándose gradualmente en todas las naciones.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
32 
3.3.6. Ocio 
Muchos utilizan Internet para descargar música, películas y otros trabajos, y también para tener 
acceso a las noticias y el estado del tiempo. 
Hay fuentes que cobran por su uso y otras gratuitas, usando los servidores centralizados y distribuidos, 
las tecnologías de P2P. 
Actualmente el correo electrónico y la mensajería instantánea WhatsApp (que sustituyó casi 
totalmente a los mensajes y a los chat) son algunos de los servicios más utilizado. 
También Facebook, que ofrece a los usuarios la creación de espacios y perfiles dónde los usuarios 
pueden poner sus fotografías, historias y comentarios personales. Y otros como Twiter, YouTube 
(visionar vídeos y también publicar vídeos creando el usuario su propio canal), etc. 
Los sistemas multijugador constituyen también buena parte del ocio en Internet, tomando cada vez un 
mayor porcentaje del pastel de los juegos electrónicos. Con el riesgo de crear adicción y de que pueda 
usarse por menores de edad. 
Se especula a diario si todas estas opciones de ocio en internet fomentan o restringen el contacto de 
persona a persona entre los seres humanos. 
 
 
 
Nota 
Reflexionar… 
Desgraciadamente, también la pornografía, a la que, por supuesto, 
no consideramos ocio, sino delito, representa buena parte del 
tráfico en Internet, lo que provoca muchas veces el pensamiento 
de si Internet tiene más ventajas o desventajas, por este aspecto y 
otros como estafas, suplantación de identidad, acoso etc. 
 
3.3.7. Trabajo 
Con la aparición de Internet y de las conexiones de alta velocidad disponibles al público, Internet ha 
alterado de manera significativa la manera de trabajar de algunas personas al poder hacerlo 
telemáticamente (desde sus hogares), lo que permite mayor conciliación familiar, flexibilidad en 
términos de horarios y de localización, y ahorro de tiempo en el traslado, contrariamente a la jornada 
laboral tradicional, que suele ocupar la mañana y parte de la tarde, en la cual los empleados se desplazan 
al lugar de trabajo.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
33 
 
 
 
Ejemplo 
Un experto contable, desde cualquier lugar del mundo (1erpaís), 
puede realizar los libros contables de una empresa de un 
determinado un país, (2ºpaís), en un servidor situado otro país 
(3erpaís), diferente que será mantenido remotamente por los 
especialistas que también podrán estar en un 4ºpaís). 
 
 
Internet y sobre todo los blogs han dado a los trabajadores un foro en el cual expresar sus opiniones 
sobre sus empleos, jefes y compañeros, creando una cantidad masiva de información y de datos sobre el 
trabajo que está siendo recogido actualmente por el colegio de abogados de Harvard. 
Internet ha impulsado el fenómeno de la Globalización y junto con la llamada desmaterialización de la 
economía ha dado lugar al nacimiento de una Nueva Economía caracterizada por la utilización de la red 
en todos los procesos de incremento de valor de la empresa. 
3.3.8. Censura 
Es extremadamente difícil, (algunos opinan que imposible, establecer control centralizado y global 
de Internet. 
Algunos gobiernos, de naciones tales como Irán, Arabia Saudita, Corea del Norte, la República Popular 
de China y Estados Unidos restringen el que personas de sus países puedan ver ciertos contenidos de 
Internet, políticos y religiosos, considerados contrarios a sus criterios. 
La censura se hace, a veces, mediante filtros controlados por el gobierno, apoyados en leyes o motivos 
culturales, castigando la propagación de estos contenidos. Sin embargo, muchos usuarios de Internet 
pueden burlar estos filtros, pues la mayoría del contenido de Internet está disponible en todo el mundo, 
sin importar donde se esté, siempre y cuando se tengan la habilidad y los medios técnicos necesarios. 
Otra posibilidad, como en el caso de China, es que este tipo de medidas se combine con la autocensura 
de las propias empresas proveedoras de servicios de Internet, serían las empresas equivalentes a 
Telefónicas (proveedores de servicios de Internet), para así ajustarse a las demandas del gobierno del 
país receptor. 
Sin embargo, algunos buscadores como Google, supuestamente, han tomado la decisión de amenazar al 
gobierno de China con la retirada de sus servicios en dicho país si no se abole la censura en Internet, 
aunque posteriormente se haya negado que tomarian dichas medidas.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
34 
Para saltarse cualquier tipo de censura o coerción en el uso de internet, se han desarrollado múltiples 
tecnologías y herramientas. 
Entre estas herramientas resaltamos las técnicas y herramientas criptológicas y las tecnologías 
encuadradas en la llamada Darknet. 
La Darknet es una colección de redes y tecnologías que persiguen la consecución de un anonimato total 
de los comunicantes, creando de esta forma una zona de total libertad. Aunque actualmente no se suele 
considerar que consigan un anonimato total, sin embargo, sí consiguen una mejora sustancial en la 
privacidad de los usuarios. Este tipo de redes se han usado intensamente, por ejemplo, en los sucesos de 
la Primavera Árabe y en todo el entramado de wikileaks para la publicación de información confidencial. 
Las tecnologías de la Darknet están en fase de perfeccionamiento y mejora de sus prestaciones. 
Para luchar contra la censura en Internet, RSF ha decidido desbloquear nueve sitios web informativos 
censurados en once países, es decir, permitirá que se pueda acceder a ellos desde el territorio en el que 
actualmente se encuentran prohibidos: 
• Grani.ru, bloqueado en Rusia. 
• Fregananews, censurado en Kazajistán, Uzbekistán y Turkmenistán. 
• The Tíbet Post y Mingjing News, prohibidos en China. 
• Dan Lam Bao, bloqueado en Vietnam. 
• Hablemos Press, censurado en Cuba. 
• Gooya News, bloqueado en Irán. 
• El Gulf Center for Human Rights, censurado en los Emiratos Árabes Unidos y en Arabia Saudita. 
• Y Bahrain Mirror, prohibido en Baréin y en Arabia Saudita. 
3.3.9. Efecto desinhibidor de Internet 
La soltura con la que nos expresamos en las redes sociales fue descrita por el psicólogo John Suler, 
especializado en ciberdelincuencia, en su obra "The Online Dishinibition Effect". 
Este autor explica que la forma de comportamiento no es la misma en las redes sociales que cuando 
estamos frente a frente, lo que se debe al efecto desinhibidor del ciberespacio.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
35 
La ausencia de contacto físico, así como la no percepción de gestos y sensaciones hace que la forma de 
relacionarse sea muy diferente. John Suler explica este fenómeno mediante 6 factores. 
• Disociación por Anonimato. Los perfiles virtuales hacen que se pueda ocultar la verdadera 
identidad de las personas. 
• Invisibilidad del ciberespacio. No existe contacto físico en el ciberespacio. 
• Asincronía de la comunicación virtual. 
• Solipsismo. El cerebro crea una imagen de la persona por las características que ésta nos 
transmite, que muchas veces no se corresponde con las reales. 
• Disociación imaginativa. La justificación de los comportamientos a través de las redes resulta 
más fácil porque no tiene tanta conciencia sobre ellos. 
• Minimización del estado de autoridad. El miedo a ser rechazados por que nuestra opinión no sea 
compartido por el otro disminuye. 
Twitter, es una de las redes sociales en las que existe una mayor libertad de expresión, lo que provoca 
que muchos de los internautas publiquen contenido calificado de inadecuado que, en ocasiones, se 
incluiría dentro de los delitos de odio. 
El mal uso de las redes puede desembocar en la creación de una identidad paralela o en la comisión de 
delitos relacionados con el Sexting, la suplantación de identidad, Phishing, injurias y calumnias o 
Stalking. Existe una disminución de la responsabilidad cuando se cometen este tipo de actos, y lo cierto 
es que la mayoría de los delitos que se cometen a través de las redes no se condenan, ya que Internet es 
un espacio en el que es muy difícil perseguir al delincuente 
Los cambios comportamentales en las redes están directamente relacionados con el aumento del 
número de delitos que se cometen a través de Internet. La sensación de seguridad y privacidad que 
aporta este espacio hace que estos delitos sean de los que más se cometen en España. 
Según las estadísticas publicadas por el Ministerio del Interior, en el año 2011 se contabilizaron 21.075 
delitos a través de las redes, pasando a 88.859 en el año 2019, lo que supone un aumento muy 
significativo. 
Las fuerzas y cuerpos de seguridad registraron 287.963 ciberdelitos en 2020, un 32 por ciento más que 
en 2019. 
 
 
 
 
+ Info 
A modo de curiosidad, puedes consultar el informe del Ministerio 
del Interior sobre la Cibercriminalidad en España. 
http://www.interior.gob.es/documents/10180/11389243/ 
Estudio+sobre+la+Cibercriminalidad+en+Espa%C3%B1a 
+2020.pdf/ed85b525-e67d-4058-9957-ea99ca9813c3

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
36 
4. Principales servicios de internet 
A lo largo del estudio de las unidades del curso, has aprendido los servicios que nos ofrece Internet, pero 
vamos a recordarlo, para contextualizarlo en este punto y afianzar los conceptos. 
4.1. Servicio web (WWW) 
Posiblemente sea el servicio más popular. La Web está formada por una gran cantidad de recursos web 
(principalmente páginas web) que tienen una estructura de tela de araña. 
El hipertexto es la base funcional y estructural de la World Wide Web. 
Las páginas web se enlazan unas a otras mediante los enlaces de hipertexto. Un enlace de hipertexto 
puede dirigirse a otra página o a un fragmento dentro del mismo documento. 
4.1.1. Estructura cliente servidor 
La estructura cliente/servidor es una arquitectura en la que uno o varios clientes, que pueden estar 
distribuidos geográficamente, solicitan servicios a uno o más servidores (los cuales también pueden 
estar distribuidos geográficamente). 
La arquitectura cliente/servidor es una arquitectura distribuida. 
Las tareas se reparten entre distintos servidores de forma transparente al usuario. 
El Esquema de funcionamiento de un Sistema cliente/servidor es el siguiente: 
• El cliente solicita una información o un servicio al servidor. 
• El servidor (que está escuchando) recibe la petición del cliente. 
• El servidor procesa dicha solicitud. 
• El servidor envía el resultado obtenido al cliente. 
• El cliente recibe el resultado. 
4.1.2. Identificadores de recursos 
Se estudió en la unidad 8 del Bloque III. Repasémoslo. 
URL 
URL (Localizador Uniforme de Recursos o Uniform Resource Locator) es un identificador de recursos 
uniforme (Uniform Resource Identifier, URI) cuyos recursos referidos pueden cambiar, esto es, la 
dirección puede apuntar a recursos variables en el tiempo.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
37 
Están formados por una secuencia de caracteres de acuerdo con un formato modélico y estándar que 
designa recursos en una red (como internet o una intranet). 
Se creó para permitir a los autores de documentos establecer hiperenlaces en la World Wide Web 
(WWW). 
En los estándares de Internet, el concepto de LRU ha sido incorporado dentro del más general de URI, 
pero el término URL todavía se utiliza ampliamente. 
URN 
El URN (Nombre de Recurso Uniforme o Uniform Resource Name) funciona de manera similar al URL. 
Sin embargo, aunque identifican recursos en la web, no indica exactamente dónde se encuentra el 
objeto. 
URI 
Un identificador de recursos uniforme o URI (Uniform Resource Identifier) es una cadena de caracteres 
que identifica los recursos de una red de forma unívoca. 
La diferencia respecto a un localizador de recursos uniforme (URL) es que estos últimos hacen 
referencia a recursos que, de forma general, pueden variar en el tiempo. 
 
Fuente: David Torres 
(https://commons.wikimedia.org/wiki/Fi
le:URI_Euler_Diagram_no_lone_URIs.svg) 
Un identificador de recursos uniforme (URI) puede ser: 
• Una URL (localizador uniforme de recursos). 
• Un URN (nombre de recurso uniforme). 
• Ambos a la vez. 
Un URI consta de las siguientes partes: 
• Esquema. 
Nombre que se refiere a una especificación para asignar identificadores (por ejemplo, "tag:" o 
"cid:"). 
En algunos casos también identifica el protocolo de acceso al recurso, por ejemplo, "http:", 
"mailto:", "ftp:", etc.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
38 
• Autoridad. 
Elemento jerárquico que identifica la autoridad de nombres (por ejemplo //www.masterd.es). 
• Ruta. 
Información usualmente organizada en forma jerárquica, que identifica al recurso en el ámbito 
del esquema URI y la autoridad de nombres (por ejemplo: /dominio/ejemplo). 
• Consulta. 
Información con estructura no jerárquica (usualmente pares "clave=valor") que identifica al 
recurso en el ámbito del esquema URI y la autoridad de nombres. 
El comienzo de este componente se indica mediante el carácter '?'. 
• Fragmento. 
Permite identificar una parte del recurso principal, o vista de una representación de este. 
El comienzo de este componente se indica mediante el carácter '#'. 
Aunque se acostumbra a llamar URL a todas las direcciones web, URI es un identificador más completo 
y por eso es recomendado su uso en lugar de la expresión URL. 
Un URI se diferencia de un URL en que permite incluir en la dirección una subdirección, determinada por 
el "fragmento". 
4.1.3. Páginas web 
 
Ejemplo de página web

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
39 
Una Página Web es un documento electrónico que puede incluir texto, sonido, gráficos, videos, menús y 
otros materiales dinámicos o estáticos. 
Toda esta información se ha configurado para poder utilizarse en el servicio World Wide Web. 
Las páginas web se encuentran contenidas dentro de los sitios web o websites, que son mejor 
conocidos por los desarrolladores con el nombre de dominios. 
Los dominios almacenan o alojan los contenidos desarrollados para que los usuarios puedan verlos o 
usarlos. 
Las páginas web se almacenan físicamente en un servidor, y el lenguaje básico para generar páginas es 
el HTML. 
Para visualizar una página web se utiliza un navegador (Chrome, Firefox, Edge, etc.). 
4.1.4. Buscadores 
Para encontrar una página de algún tema concreto se utilizan los buscadores (como Google). 
Hay dos tipos principales de buscadores web: 
• Los Directorios o Índices temáticos. 
• Descubrimiento de recursos: 
Los buscan las personas. 
• Ordenación del contenido: 
Manual. 
• Resultados de la consulta: 
Página de resultados creada antes de realizar la consulta. 
Resultados muy precisos, pero poco exhaustivos. 
• Los Motores de búsqueda: 
• Descubrimiento de recursos: 
Descubrimiento automático mediante el uso de crawlers (arañas o webbots). 
• Ordenación del contenido. 
A través de una métrica que puntúa las páginas en función de sus contenidos, palabras 
clave, etc.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
40 
• Resultados de la consulta. 
Página de resultados se crea de forma dinámica después de la consulta. 
Resultados muy exhaustivos, pero poco precisos. 
Los directorios y los motores de búsqueda son las principales herramientas de búsqueda en la Web. 
Sin embargo, también existen otro tipo de herramientas que funcionan como intermediarios en la 
recuperación de información. 
Estas herramientas no buscan por sí mismas, sino que limitan a pedir a otros que busquen por ellos. 
Actúan como un interfaz único para utilizar varios buscadores. 
Hay dos tipos: 
• Multibuscadores. 
Simplemente ponen una lista de los buscadores más famosos y los puedes utilizar desde su 
página. Los resultados mostrados son los del buscador utilizado. 
• Metabuscadores. 
El metabuscador es un sistema que conoce los parámetros que utilizan los distintos buscadores. 
Cuando realizamos una consulta, la convierte al formato de cada buscador y realiza la búsqueda 
en todos ellos. 
A continuación, recoge los resultados, elimina resultados y los muestra por orden de 
importancia en base a criterios como el orden en que lo ha devuelto, cuantos buscadores la han 
devuelto, etc. 
4.1.5. Web 2.0. Herramientas de trabajo colaborativo 
 
No existe una definición consensuada de web 2.0 o web 3.0. 
Las páginas de la web 1.0 son: 
• Estáticas. 
• No tienen posibilidad de interactuar con ellas.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
41 
La web 2.0 se ve como una evolución en la que se permite: 
• La creación y publicación de contenido en internet. 
• Una comunicación abierta que posibilita compartir, modificar y crear contenidos entre todos 
(web colaborativa). 
La principal caracteristica de la web 2.0 es que gracias a páginas como Facebook, Twitter, Amazon, 
Ebay, Instagram, Wikipedia, etc., ahora los usuarios tienen la capacidad de crear, compartir y modificar 
informacion pudiendo así aportar sus opiniones 
 
Principal diferencia entre Web 1.0 y Web 2.0 
En la Web 1.0 las personas se conectan a la web. 
En la Web 2.0 las personas se conectan con otras personas a través de las redes sociales. Las páginas 
presentan algún tipo de interacción con ellas (un botón de "me gusta", una opción de hacer un 
comentario, posibilidad de añadir conocimiento o contenidos, etc.).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
42 
Espacios de colaboración 
Estas interacciones son posibles gracias a los espacios de colaboración que son una parte clave de la 
Web 2.0, que permite a los usuarios poder interactuar de manera activa en la creación y modificación 
de contenido. De plataformas como wikis, foros y herramientas de colaboración en línea (como Google 
Docs o Trello) permitiendo que las personas trabajen juntas en tiempo real, compartan ideas y 
construyan conocimientos de manera colectiva. 
Ademas estos espacios permiten una colaboración activa, donde los usuarios pueden modificar 
documentos, aportar ideas y realizar tareas compartidas sin necesidad de estar en el mismo lugar físico. 
Esta capacidad de trabajar juntos de manera simultánea y en tiempo real es uno de los pilares de la Web 
2.0, ya que fomenta la innovación, el aprendizaje colectivo y la creación de contenido de manera 
mucho más accesible y participativa. 
Además, los espacios de colaboración han impulsado la creación de comunidades en línea y redes 
sociales, donde las personas pueden conectar, compartir intereses y generar conocimiento de manera 
abierta y distribuida. 
4.1.6. Web 3.0. Web semántica

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
43 
Hay 4 conceptos básicos que ya han empezado a cambiar la forma de ver la web. 
• Contenidos Semánticos. 
Se mejorará las búsquedas en internet para que sea algo más usable y natural. 
Ya no solo debemos pensar en base a palabras clave y si contiene o no un texto. 
Podemos hablar de términos como calidad, opiniones, estados de ánimo, etc. 
Por lo tanto, las búsquedas serán mucho más afinadas, pudiendo dar una respuesta mucho más 
correcta, dado que le dotará al buscador de cierta capacidad para razonar. 
Ejemplo de consulta: 
Quiero comprar una camiseta de algún color claro en una tienda de Córdoba que tenga buen 
precio y que la mayoría de los clientes que la han comprado estén satisfechos. 
Aquí estamos metiendo conceptos como: 
• Variedad de colores sin especificar. 
• Satisfacción del cliente (calidad del artículo). 
• Un rango de precio (lógica difusa). Tiene que ser un buen precio, no necesariamente el más 
bajo. 
 
 
 
 
+ Info 
Esto es ya una realidad. 
Google lleva años trabajando en un buscador semántico y en 
muchas empresas ya se han desarrollado algunos básicos. 
 
 
Para conseguir este tipo de resultados hay que trabajar con técnicas de inteligencia artificial y ya 
se están consiguiendo cosas muy interesantes.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
44 
• Búsquedas de lenguaje natural. 
Está relacionado en parte con el concepto anterior y se complementan. 
En lugar de realizar preguntas con una cierta estructura, podremos preguntar en lenguaje 
natural como lo haríamos con otra persona. 
El buscador realizará un procesamiento del lenguaje natural (basado en inteligencia artificial) 
para determinar qué es exactamente lo que estás pidiendo. 
• Contenidos accesibles sin navegación. 
La tendencia es que cada vez podamos acceder a toda clase de servicios desde cualquier 
dispositivo, a cualquier hora y en cualquier lugar, de una forma inmediata (sin tener que navegar 
y buscar). 
• Tecnologías de inteligencia artificial. 
Se pueden utilizar técnicas de inteligencia artificial para muchas cosas en internet: 
• Desarrollo de asistentes virtuales que se comuniquen como si fueran una persona. 
• Extracción no trivial de la información que reside de manera implícita en los contenidos 
(minería de textos). 
• Modelos predictivos (minería de datos). 
• Reconocimiento facial. 
• Reconocimiento de estado de ánimo, de manera que tanto los asistentes virtuales como las 
propias páginas puedan variar en función de este.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
45 
4.2. Webmail 
 
Gmail 
Es un correo electrónico basado en web o correo web. 
Es un servicio que permite acceder a tu cuenta de correo electrónico a través de una página web 
utilizando un navegador y sin descargar los mensajes al propio ordenador. 
Este servicio es muy útil, ya que puedes leer, enviar y organizar tu correo electrónico desde cualquier 
ordenador, desde cualquier parte del mundo, con conexión a Internet. 
La privacidad de los usuarios de webmail se lleva a cabo mediante la utilización de nombres de usuario y 
contraseña únicos. 
Los principales servidores de webmail son: 
• Gmail. 
• Hotmail. 
• Yahoo. 
Ventajas de webmail 
• Los mensajes pueden leerse, escribirse y enviarse desde cualquier lugar con un navegador y 
conexión a Internet. 
• Los mensajes no tienen que descargarse al ordenador. 
• Las cuentas de correo pueden crearse fácilmente. 
• Al conservarse los mensajes en el servidor, puedes acceder desde cualquier dispositivo sin 
sincronizar. 
• Estos servidores suelen proporcionar una buena seguridad y una política anti-SPAM. 
• Unificación con otros servicios (Por ejemplo, Gmail con Google Drive).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
46 
Desventajas de webmail 
• El usuario tiene que estar conectado a Internet para leer y escribir los mensajes. 
• Los servidores de webmail comerciales ofrecen espacio limitado para el almacenamiento de los 
mensajes. 
• Pueden mostrar publicidad. 
4.3. Transferencia de ficheros 
La transferencia de ficheros se hace posible gracias al protocolo FTP. 
El Protocolo de transferencia de archivos (File Transfer Protocol o FTP) es un protocolo de red para la 
transferencia de archivos entre sistemas conectados a una red TCP, basado en la arquitectura cliente-
servidor. 
Desde un equipo cliente se puede conectar a un servidor para descargar archivos desde él o para 
enviarle archivos, independientemente del sistema operativo utilizado en cada equipo. 
 
 
 
 
Curiosidad 
En FTP existen dos modos principales de transmisión de archivos, 
el modo ASCII que se usa para transmitir archivos de texto, de 
formatos txt, html, o csv y el modo binario útil para transmitir el 
resto de formatos como imágenes, vídeos, ejecutables, etc. 
El propósito fundamental del modo ASCII es garantizar que un 
archivo de texto se pueda transferir entre distintos sistemas 
operativos asegurando la conversión, por ejemplo de los saltos de 
línea. 
 
4.4. Servicio de acceso remoto 
Cómo has estudiado en la unidad 5 de este bloque, existen servicios que nos permiten conectarnos de 
forma remota a otros equipos. 
Recordemos que podemos acceder de dos formas: 
• En modo terminal. 
Podemos abrir una terminal en un equipo remoto a través de determinados servicios (como 
Telnet).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
47 
• En modo gráfico. 
Permite conectarnos a otro equipo de la red de forma que podemos ver su pantalla e interactuar 
con ella como si fuera nuestro propio ordenador, y también ver las acciones que realiza el 
usuario de dicho equipo. 
Las aplicaciones más utilizadas son: 
• VNC. 
VNC es un programa de software libre basado en una estructura cliente-servidor. 
• Team Viewer. 
Es un software privado que ofrece licencia gratuita a los usuarios y de pago a las empresas. 
4.5. Telefonia IP 
La Telefonía IP (Protocolo de telefonía por Internet), es un término utilizado para describir las 
tecnologías que usan el protocolo IP para el intercambio de voz, fax, y otras formas de información, 
tradicionalmente transportada sobre la Red Telefónica Pública Conmutada (PSTN). La llamada viaja en 
forma de paquetes, sobre una red de área local (LAN) o Internet, evitando el cargo de la PSTN. 
En la segunda mitad del año 1990, Internet y el protocolo TCP / IP comenzaron a impulsar el cambio de 
la industria de la telefonía y las comunicaciones. 
El Protocolo de Internet se convirtió en el transporte para casi todas las comunicaciones de datos. 
En la actualidad, todos los proveedores de telecomunicaciones están utilizando una infraestructura IP 
para una parte o la totalidad de sus servicios de voz. 
La mayoría de las empresas ya hicieron el cambio de PSTN y están utilizando VoIP para sus 
comunicaciones de voz o ya tienen planes de implementarla como parte de su solución de 
Comunicaciones Unificadas. 
Protocolos VoIP 
Existen diversos protocolos que pueden ser por la telefonía IP incluyendo: 
• Protocolo de Inicio de Sesión (SIP). 
• H.323. 
• Protocolo de Transporte en Tiempo Real (RTP). 
• Protocolo de Control en Tiempo Real (RTCP). 
• Protocolo Seguro de Transporte en Tiempo Real (SRTP). 
• Protocolo de Descripción de Sesión (SDP).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
48 
La Telefonía IP en las Empresas 
Los beneficios de la telefonía IP en ambientes corporativos son numerosos, pero se pueden resumir a 
consideraciones en costo asociados con la infraestructura y facturas de teléfono mensuales. 
Las soluciones modernas de PBX VoIP, como 3CX, permiten que a las empresas puedan hacer funcionar 
el sistema en hardware existente no propietario, así como dispositivos de bajo costo tales como 
MiniPCs. 
Los sistemas telefónicos tradicionales y las soluciones VoIP propietarias, requieren de una 
implementación extensiva sobre arquitecturas cerradas, las cuales pueden llegar a costar cientos de 
miles de dólares y son mucho más difíciles de administrar, configurar y mantener. Los sistemas de 
telefonía IP de estándares abiertos son mucho más fáciles y económicos de escalar. 
El uso de VoIP y Troncales SIP permite que las facturas de teléfono se reduzcan, esto se debe a que las 
empresas pueden conectar oficinas remotas y sucursales en otras ciudades y países, de forma fácil, por 
lo que las llamadas dentro de la empresa son gratuitas. Los costos de larga distancia se eliminan y en 
promedio, las tarifas de llamadas son mucho más económicas. 
Los sistemas de telefonía empresariales ofrecen a las empresas mucho más que sólo llamadas 
telefónicas. 
La telefonía IP marcó el comienzo de del desarrollo de las soluciones de Comunicaciones Unificadas, las 
cuales pueden brindan un paquete de comunicaciones completo y todo en uno, funcionar en una sola 
red y una sola plataforma. 
Estas soluciones también han permitido a los usuarios hacer uso de llamadas telefónicas VoIP a través 
de sus smartphones y computadoras, ya sea con el uso de las apps o cliente web. 
Problemas comunes en VoIP 
• Llamadas Cortadas o Congeladas al Comunicarse con Usuarios Externos: 
• Posible Causa: La salida a Internet está usando NAT (Network Address Translation), lo que 
impide la correcta transmisión de paquetes RTP. 
• Solución: Configurar STUN, usar un SIP Proxy con soporte de NAT, habilitar ALG 
(Application Layer Gateway) en el router o establecer una VPN para evitar la traducción de 
direcciones. 
• Retrasos y Latencia Elevada: 
• Posible Causa: Congestión en la red o rutas ineficientes en el tráfico VoIP. 
• Solución: Implementar QoS (Quality of Service) para priorizar tráfico VoIP y reducir la 
carga de red.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
49 
• Voz Robotizada o Cortes en el Audio: 
• Posible Causa: Uso incorrecto de códecs de compresión o insuficiente ancho de banda. 
• Solución: Verificar que los códecs configurados sean adecuados, como G.711 para calidad 
alta y G.729 para entornos con ancho de banda limitado. 
• No se Recibe Audio en una de las Direcciones: 
• Posible Causa: Configuración incorrecta de NAT o firewall bloqueando paquetes RTP. 
• Solución: Habilitar ALG SIP, permitir puertos RTP en el firewall y configurar correctamente 
la opción NAT en el servidor SIP. 
• Llamadas que No se Conectan: 
• Posible Causa: Servidor SIP mal configurado o bloqueo en firewall. 
• Solución: Verificar las reglas del firewall y asegurarse de que los puertos SIP y RTP estén 
abiertos. 
• Eco en las Llamadas: 
• Posible Causa: Dispositivos con mala cancelación de eco o problemas en la ganancia de 
micrófono. 
• Solución: Reducir el volumen del micrófono y habilitar funciones de cancelación de eco en 
los dispositivos VoIP. 
• Registro SIP Fallido o Perdido: 
• Posible Causa: Interrupción en la conectividad con el servidor SIP. 
• Solución: Verificar la conectividad, latencia y ajustar el tiempo de reintento de registro SIP 
en el cliente. 
Servicios de telefonía fija en la nube 
Servicios de telefonía fija en la nube son una solución de comunicaciones empresariales que permite a 
las organizaciones utilizar sistemas telefónicos tradicionales, pero gestionados a través de internet en 
lugar de infraestructura física local. Estos servicios están basados en la tecnología VoIP (Voice over IP), 
que permite realizar llamadas de voz a través de redes de datos en lugar de líneas telefónicas 
convencionales. 
En lugar de depender de un sistema de telefonía fija tradicional que requiere servidores locales y 
equipos especializados (como PBX - Private Branch Exchange), los servicios de telefonía fija en la nube 
permiten a las empresas operar su sistema telefónico a través de plataformas basadas en la nube. Esto 
ofrece varios beneficios, como la escalabilidad, la flexibilidad y la reducción de costes, ya que elimina la 
necesidad de equipos y mantenimiento físico en las instalaciones.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
50 
El sistema de telefonía fija en la nube se basa en el uso de servidores remotos que gestionan las llamadas 
telefónicas a través de internet. Cuando un usuario realiza o recibe una llamada, los datos de la llamada 
se envían a través de internet, donde son gestionados por el sistema de telefonía en la nube. Los 
proveedores de este servicio generalmente ofrecen una interfaz de usuario web o aplicaciones para 
configurar las líneas, gestionar llamadas y supervisar el estado de la telefonía. 
Ventajas: 
• Escalabilidad: Las empresas pueden añadir o eliminar líneas telefónicas fácilmente sin necesidad 
de actualizar infraestructura física, lo que permite adaptar el sistema a las necesidades 
cambiantes del negocio. 
• Costos reducidos: Al no necesitar equipos costosos ni mantenimiento de hardware, los servicios 
en la nube suelen ser más económicos que los sistemas tradicionales. Además, las tarifas de las 
llamadas pueden ser más bajas, especialmente para llamadas internacionales. 
• Flexibilidad y movilidad: Los empleados pueden acceder al sistema telefónico desde cualquier 
lugar con acceso a internet, lo que es ideal para empresas con trabajadores remotos o con varias 
ubicaciones. 
• Funciones avanzadas: Muchas plataformas en la nube ofrecen características adicionales como 
correo de voz, desvío de llamadas, integración con otros sistemas (CRM, correo electrónico, 
etc.), grabación de llamadas y análisis en tiempo real. 
• Mantenimiento y actualizaciones automáticas: Al estar gestionados por el proveedor de 
servicios, las actualizaciones de software y el mantenimiento del sistema se realizan de manera 
automática, lo que garantiza que el sistema siempre esté actualizado sin esfuerzo por parte de la 
empresa. 
Inconvenientes: 
• Dependencia de internet: Dado que todo el sistema se basa en la conexión a internet, cualquier 
interrupción en la red podría afectar la calidad de las llamadas o incluso interrumpir el servicio. 
• Seguridad: Aunque los proveedores suelen implementar medidas de seguridad avanzadas, las 
empresas deben asegurarse de que los datos de las llamadas estén adecuadamente protegidos, 
especialmente cuando se manejan información sensible. 
• Calidad de servicio: La calidad de las llamadas puede verse afectada por la capacidad de la red de 
internet. Si la conexión es débil o inestable, las llamadas pueden tener interferencias o caídas. 
Los servicios de telefonía fija en la nube ofrecen a las empresas una solución moderna, flexible y 
económica para sus necesidades de comunicación. A medida que más empresas adoptan el trabajo 
remoto y la digitalización, este tipo de servicio se está convirtiendo en una opción popular por su 
facilidad de implementación, coste reducido y características avanzadas.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
51 
4.6. Mensajería instantánea 
La mensajería instantánea (Instant Messaging o IM) es una forma de comunicación en tiempo real entre 
dos o más personas basada en texto. 
El texto es enviado a través de dispositivos conectados a internet (PCs, móviles, tablets, etc.) sin 
importar la distancia que exista entre los dos (o más) dispositivos conectados. 
El término se usa principalmente para la generación de tecnología que funcionaba en computadoras, 
aunque muchas de estas plataformas tienen aplicación móvil. 
Actualmente, muchas de estas aplicaciones permiten otras opciones como videoconferencia, llamada 
de voz, envío de fotos, vídeos o audio, etc. 
Protocolo XMPP 
XMPP (Extensible Messaging and Presence Protocol o Protocolo extensible de mensajería y 
comunicación de presencia) es un protocolo abierto y extensible basado en XML. 
Con el protocolo XMPP queda establecida una plataforma para el intercambio de datos XML que puede 
ser usada en aplicaciones de mensajería instantánea. 
Las características en cuanto a adaptabilidad y sencillez del XML son heredadas de este modo por el 
protocolo XMPP. 
A diferencia de los protocolos propietarios, se encuentra documentado y se insta a utilizarlo en 
cualquier proyecto. 
Existen servidores y clientes libres que pueden ser usados sin coste alguno. 
Tras varios años de su existencia, ha sido adoptado por empresas como Facebook, WhatsApp 
Messenger y Nimbuzz, entre otras, para su servicio de chat. Google lo adoptó para su servicio de 
mensajería Google Talk, y en 2013 anunció que lo abandonaría en favor de su protocolo propietario 
Hangouts. 
Principales aplicaciones 
Hoy en día todo el mundo usa WhatsApp y parece que es la mejor aplicación para mensajería. Sin 
embargo, existen aplicaciones mejores pero que no han tenido el mismo éxito. 
Vamos a indicar de las principales aplicaciones de mensajería instantánea. La mayoría incluyen otros 
servicios añadidos (videoconferencia, etc.): 
• WhatsApp. 
• Line. 
• Spotbros.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
52 
• Telegram. 
• WeChat. 
• Wire. 
• BBM. 
• SnapChat. 
• Skype. 
• Hangouts. 
• Viber. 
• Facebook Messenger. 
4.7. Otros servicios 
Vamos a ver otros servicios útiles de Internet: 
• Network Time Protocol (NTP): 
Es un protocolo de Internet para sincronizar los relojes de los sistemas informáticos a través del 
enrutamiento de paquetes en redes con latencia variable. NTP utiliza UDP como su capa de 
transporte, usando el puerto 123. 
• La hora ROA. 
Es la establecida por Real Instituto y Observatorio de la Armada en San Fernando, Cádiz, siendo 
esta la hora oficial de España. 
El ROA difunde la hora oficial de España a través del protocolo Protocolo NTP (Network Time 
Protocol), a través de dos servidores de internet situados en San Fernando («hora.roa.es» y 
«minuto.roa.es», ambos alcanzables en «ntp.roa.es»). 
• EDUROAM (Education Roaming): 
Es un consorcio de roaming WiFi globlal para facilitar la conexión a internet de forma segura, en 
vistas principalmente a la movilidad de los estudiantes. 
Mediante esta iniciativa, tanto estudiantes, investigadores o profesorado pueden disfrutar de 
conectividad en su propio campus, así como en el resto de campus adheridos. Esta conexión 
será gratis utilizando las credenciales de su institución educativa. 
En el caso de España, eduroam ES, forma parte del proyecto RedIRIS, una red académica y de 
investigación española, encargada de proporcionar servicios de comunicación a la comunidad 
científica y universitaria, financiada por el Ministerio de Ciencia, Innovación y Universidades.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
53 
5. Protocolo HTTP 
 
El Protocolo de transferencia de hipertexto (HTTP o Hypertext Transfer Protocol es el protocolo de 
comunicación que permite las transferencias de información en la World Wide Web. 
HTTP usa los siguientes puertos: 
• 80/tcp. 
Se usa para la navegación web de forma no segura. 
• 591/tcp. 
FileMaker 6.0 (alternativa para HTTP, ver puerto 80). 
• 3128/tcp. 
HTTP usado por web caches y por defecto en Squid cache. 
• 8080/tcp. 
HTTP HTTP-ALTERNATIVO. 
HTTP define la sintaxis y la semántica que utilizan los elementos de software de la arquitectura web 
(clientes, servidores, proxis) para comunicarse. 
HTTP es un protocolo sin estado, es decir, no guarda ninguna información sobre conexiones anteriores. 
El desarrollo de aplicaciones web necesita frecuentemente mantener estado. Para esto se usan las 
cookies, que es información que un servidor puede almacenar en el sistema cliente.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
54 
5.1. Versiones 
HTTP ha pasado por múltiples versiones del protocolo, muchas de las cuales son compatibles con las 
anteriores. 
El RFC 2145 describe el uso de los números de versión de HTTP 
El cliente le dice al servidor al principio de la petición la versión que usa, y el servidor usa la misma o una 
anterior en su respuesta. 
5.1.1. 0.9 (lanzada en 1991) 
Está totalmente obsoleta, algunas de sus características son: 
• Soporta solo un comando, GET. 
• No especifica el número de versión HTTP. 
• No soporta cabeceras. 
Como esta versión no soporta POST, el cliente no puede enviarle mucha información al servidor. 
5.1.2. HTTP/1.0 (mayo de 1996) 
Esta es la primera revisión del protocolo que especifica su versión en las comunicaciones, y todavía se 
usa ampliamente, sobre todo en servidores proxy. 
Permite los métodos de petición GET, HEAD y POST. 
5.1.3. HTTP/1.1 (junio de 1999) 
Las conexiones persistentes están activadas por defecto y funcionan bien con los proxies. También 
permite al cliente enviar múltiples peticiones a la vez por la misma conexión (pipelining) lo que hace 
posible eliminar el tiempo de Round-Trip delay por cada petición. 
Es la más compatible.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
55 
5.1.4. HTTP/1.2 (febrero de 2000) 
Los primeros borradores de 1995 del documento PEP, an Extension Mechanism for HTTP (el cual 
propone el Protocolo de Extensión de Protocolo, abreviado PEP) los hizo el World Wide Web 
Consortium y se envió al Internet Engineering Task Force. 
El PEP inicialmente estaba destinado a convertirse en un rango distintivo de HTTP/1.2. 
En borradores posteriores, sin embargo, se eliminó la referencia a HTTP/1.2. 
El RFC 2774 (experimental), HTTP Extension Framework, incluye en gran medida a PEP. Se publicó en 
febrero de 2000. 
5.1.5. HTTP/2 (mayo de 2015) 
En el año 2012 aparecen los primeros borradores de la nueva versión de HTTP (HTTP/2). 
Esta nueva versión no modifica la semántica de aplicación de http (todos los conceptos básicos 
continúan sin cambios). 
Sus mejoras se enfocan en cómo se empaquetan los datos y en el transporte. 
Algunas de las características de esta versión son: 
• Es un protocolo binario. 
Esto facilita encontrar el comienzo y el final de cada frame, que es algo realmente complicado 
en cualquier protocolo de texto. 
Además, los protocolos binarios son mucho más simples y por lo tanto son menos propensos a 
tener errores que los protocolos de texto utilizados por las versiones anteriores a HTTP 2.0. 
• Una única conexión. 
Al contrario que en HTTP/1.x donde para cargar cualquier contenido web es necesario el uso de 
múltiples conexiones TCP simultáneas para poder descargar todos los elementos de dicha web, 
en HTTP 2.0 utiliza una única conexión para ofrecer múltiples solicitudes y respuestas en 
paralelo. Teniendo en cuenta que cada página web puede contener objetos HTML, CSS, 
JavaScript, imágenes, vídeo… la diferencia de trabajo entre utilizar una única conexión o utilizar 
varias es elevada. 
• Eliminación de información redundante. 
El objetivo es evitar el envío de datos repetidos durante una misma conexión, así conseguiremos 
que se consuman menos recursos, obteniendo una menor latencia.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
56 
• Multiplexación. 
Con HTTP/1.1 el navegador envía una petición y debe esperar la respuesta del servidor para 
poder enviar la siguiente solicitud, como en las webs modernas suelen tener más de 100 
objetos, supone que el retardo es grande. 
La solución que introduce HTTP 2.0 a este problema es la denominada Multiplexación. 
La multiplexación permite enviar y recibir varios mensajes al mismo tiempo optimizando la 
comunicación, se consigue reducir el número de conexiones mejorando considerablemente la 
velocidad de carga y disminuyendo la congestión de los servidores web. 
• Servicio 'server push'. 
El servicio "server push" también conocido como "cache push", se basa en estimaciones para 
que el servidor sea capaz de enviar información al usuario antes de que éste la solicite para que 
la información esté disponible de forma inmediata. 
La forma de actuar del servidor es enviar varias respuestas a una única solicitud del cliente, es 
decir, además de la respuesta a la solicitud original, el servidor puede enviar recursos 
adicionales. Esto es así porque una página web está formada por decenas de archivos 
referenciados que gracias al servicio "server push" el servidor envía tras recibir una única 
solicitud ahorrando mensajes innecesarios. 
HTTP 2.0 contiene un campo denominado 'Ajustes' con el que el cliente puede indicar si desea o 
no obtener los recursos que proporciona el servicio 'server push'. 
• Compresión de cabeceras para transmitir menos información. 
Con las versiones anteriores a HTTP 2.0, las cabeceras de los mensajes de solicitud eran de 
texto claro, sin ningún tipo de compresión. 
El problema aparece como consecuencia del incremento de tamaño que sufren estas cabeceras 
por los user-agent de los navegadores, al uso de cookies (también deben aparecer en los 
mensajes de solicitud), etc. 
Además, cuando HTTP/1.1 envía una petición, debe esperar la respuesta del servidor para 
poder enviar la siguiente solicitud, aumentado mucho el retardo sufrido. 
Asimismo, hay que tener en cuenta que cuando un cliente hace numerosas peticiones a un 
mismo servidor, los encabezamientos apenas cambian unos de otros, por lo que se envía mucha 
información redundante. 
Con HTTP 2.0 las cabeceras experimentan compresiones, con lo que se obtienen mejores 
tiempos de respuesta y también se mejora la eficiencia (sobre todo en terminales móviles). 
El algoritmo empleado para realizar la compresión de cabeceras es HPACK, que es un algoritmo 
simple y poco flexible que se basa en eliminar campos de cabecera redundantes, además de 
prevenir posibles vulnerabilidades.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
57 
• Priorización de flujos. 
Un mensaje HTTP se puede dividir en múltiples fragmentos en su recorrido desde el cliente 
hasta el servidor o desde servidor al cliente. 
El orden y el retardo con el que estas tramas llegan a su destino son fundamentales, dado que 
algunos objetos de las webs son más importantes que otros, nos interesará que los objetos más 
relevantes cuenten con algún tipo de prioridad. 
Para poder 'controlar' la prioridad que tienen las tramas, HTTP 2.0 permite asignar a cada flujo 
un peso (entre 1 y 256) y una dependencia. Debemos ser conscientes de que las prioridades 
pueden variar durante la ejecución. 
Con las prioridades y la dependencia se hace un árbol de prioridades. 
Ejemplo: 
• Si A tiene un peso de 12 y B tiene un peso de 4: A dispondrá del 75 % de los recursos y B se 
quedará con el 25 % restante. 
• No requiere cifrado TLS. 
En HTTP/2 el uso de cifrado TLS (Transport Layer Security) es opcional. 
De todos modos un gran número de fabricantes de software7 (Firefox, Internet Explorer o 
Google Chrome por ejemplo) ya han anunciado que sus implementaciones solo soportarán 
HTTP 2.0 sobre TLS usando la extensión ALPN que requiere TLSv1.2 o superior. 
Recordemos que TLS es un protocolo criptográfico de la capa de transporte (de criptografía 
asimétrica), que proporciona comunicaciones seguras por la red. 
El uso de TLS añade un retardo adicional. 
Los exploradores más importantes solo soportan HTTP 2.0 sobre TLS usando la extensión ALPN 
que requiere TLSv1.2 o superior. 
5.1.6. HTTP/3 (Octubre de 2018) 
HTTP/3 es el sucesor propuesto de HTTP/2,? que ya está en uso en la web, utilizando UDP en lugar de 
TCP para el protocolo de transporte subyacente. 
Al igual que el HTTP/2, no es obsoleto en las versiones principales anteriores del protocolo. 
El soporte para HTTP/3 fue agregado a Cloudflare y Google Chrome en septiembre de 2019, y puede 
ser habilitado en las versiones estables de Chrome y Firefox.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
58 
5.2. Descripción de HTTP 
Es un protocolo orientado a transacciones y sigue el esquema petición-respuesta entre un cliente y un 
servidor. 
• El cliente realiza una petición enviando un mensaje, con cierto formato al servidor. 
(El cliente se le suele llamar "agente de usuario", en inglés user agent). 
Ejemplos de cliente son los navegadores web y las arañas web (también conocidas por su 
término inglés, webcrawlers). 
• El servidor le envía un mensaje de respuesta. 
(El servidor se le suele llamar un servidor web). 
5.2.1. Mensajes 
Los mensajes HTTP son en texto plano lo que lo hace más legible y fácil de depurar. Esto tiene el 
inconveniente de hacer los mensajes más largos. 
Los mensajes tienen la siguiente estructura: 
• Línea inicial (termina con retorno de carro y un salto de línea). 
• Para las peticiones: la acción requerida por el servidor (método de petición) seguido de la 
URL del recurso y la versión HTTP que soporta el cliente. 
• Para respuestas: La versión del HTTP usado seguido del código de respuesta (que indica 
qué ha pasado con la petición seguido de la URL del recurso) y de la frase asociada a dicho 
retorno. 
• Las cabeceras del mensaje que terminan con una línea en blanco. 
Son metadatos. Estas cabeceras le dan gran flexibilidad al protocolo. 
• Cuerpo del mensaje. 
Es opcional. Su presencia depende de la línea anterior del mensaje y del tipo de recurso al que 
hace referencia la URL. 
Típicamente tiene los datos que se intercambian cliente y servidor, como, por ejemplo, para una 
petición podría contener ciertos datos que se quieren enviar al servidor para que los procese. 
Para una respuesta podría incluir los datos que el cliente ha solicitado.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
59 
5.2.2. Métodos de petición 
HTTP define una serie predefinida de métodos de petición (algunas veces referido como "verbos") que 
pueden utilizarse. 
El protocolo tiene flexibilidad para ir añadiendo nuevos métodos y para así añadir nuevas 
funcionalidades. 
 
 
 
 
Recuerda 
Un Identificador de Recursos Uniforme o UR (del inglés Uniform 
Resource Identifier) es una cadena de caracteres que identifica los 
recursos de una red de forma unívoca. La diferencia respecto a un 
localizador de recursos uniforme (URL) es que estos últimos hacen 
referencia a recursos que, de forma general, pueden variar en el 
tiempo. 
 
El número de métodos de petición se ha ido aumentando según se avanzaba en las versiones. 
Cada método indica la acción que desea que se efectúe sobre el recurso identificado. Lo que este 
recurso representa depende de la aplicación del servidor. Por ejemplo, el recurso puede corresponderse 
con un archivo que reside en el servidor. 
• GET. 
El método GET solicita una representación del recurso especificado. Las solicitudes que usan 
GET solo deben recuperar datos y no deben tener ningún otro efecto. (Esto también es cierto 
para algunos otros métodos HTTP.) 
• HEAD. 
Pide una respuesta idéntica a la que correspondería a una petición GET, pero en la respuesta no 
se devuelve el cuerpo. Esto es útil para poder recuperar los metadatos de los encabezados de 
respuesta, sin tener que transportar todo el contenido. Consultar el enlace RFC 2616. 
• POST. 
Envía datos para que sean procesados por el recurso identificado en la URI de la línea petición. 
Los datos se incluirán en el cuerpo de la petición. A nivel semántico está orientado a crear un 
nuevo recurso, cuya naturaleza vendrá especificada por la cabecera Content-Type.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
60 
Ejemplos: 
• Para datos formularios codificados como una URL (aunque viajan en el cuerpo de la 
petición, no en la URL): application/x-www-form-urlencoded. 
• Para bloques a subir, ej. ficheros: multipart/form-data. 
• Además de los anteriores, no hay un estándar obligatorio y también podría ser otros como: 
» text/plain. 
» application/json. 
» application/octet-stream. 
» etc. 
• PUT: 
Envía datos al servidor, pero a diferencia del método POST la URI de la línea de petición no hace 
referencia al recurso que los procesará, sino que identifica a los propios datos. 
Otra diferencia con POST es semántica (ver REST): 
• POST está orientado a la creación de nuevos contenidos. 
• PUT está más orientado a la actualización de los mismos (aunque también podría crearlos). 
Ejemplo: 
PUT /path/filename.html HTTP/1.1 
• DELETE. 
Borra el recurso especificado. 
• TRACE. 
Este método solicita al servidor que introduzca en la respuesta todos los datos que reciba en el 
mensaje de petición. 
Se utiliza con fines de depuración y diagnóstico ya que el cliente puede ver lo que llega al 
servidor y de esta forma ver todo lo que añaden al mensaje los servidores intermedios.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
61 
• OPTIONS. 
Devuelve los métodos HTTP que el servidor soporta para un URL específico. 
Esto puede ser utilizado para comprobar la funcionalidad de un servidor web mediante petición 
en lugar de un recurso específico. 
• CONNECT. 
Se utiliza para saber si se tiene acceso a un host, no necesariamente la petición llega al servidor, 
este método se utiliza principalmente para saber si un proxy nos da acceso a un host bajo 
condiciones especiales, como por ejemplo "corrientes" de datos bidireccionales encriptadas 
(como lo requiere SSL). 
(Establece un túnel hacia el servidor identificado por el recurso). 
• PATCH. 
Es utilizado para aplicar modificaciones parciales a un recurso (similar a PUT, el cual sobrescribe 
completamente un recurso). 
Se utiliza para actualizar, de manera parcial una o varias partes. Está orientado también para el 
uso con proxy.12. 
• MOVE. 
La operación MOVE es el equivalente lógico de una copia (COPY), seguida de un procesamiento 
de mantenimiento de coherencia, seguido de una eliminación del origen, donde las tres acciones 
se realizan en una sola operación. 
• MKCOL. 
Crea un nuevo recurso en la ubicación especificada por Request-URI. 
• PROPFIND. 
El método PROPFIND recupera propiedades definidas en el recurso identificado por Request-URI. 
• PROPPATCH. 
Procesa las instrucciones especificadas en el cuerpo de la solicitud para establecer y / o eliminar 
las propiedades definidas en el recurso identificado por el Request-URI.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
62 
 
 
 
+ Info 
También están los métodos MERGE, UPDATE Y LABEL. 
Puede consultar más de información en las webs oficiales: 
https://www.w3.org/Protocols/ 
https://www.w3.org/Protocols/rfc2616/rfc2616.html 
https://tools.ietf.org/html/rfc2616 
https://tools.ietf.org/html/rfc3253 
https://tools.ietf.org/html/rfc2518 
https://tools.ietf.org/html/rfc5789 
 
5.2.3. Códigos de respuesta 
El código de respuesta o retorno es un número que indica que ha pasado con la petición. El resto del 
contenido de la respuesta dependerá del valor de este código. El sistema es flexible y de hecho la lista 
de códigos ha ido aumentando para así adaptarse a los cambios e identificar nuevas situaciones. Cada 
código tiene un significado concreto. Sin embargo, el número de los códigos están elegidos de tal forma 
que según si pertenece a una centena u otra se pueda identificar el tipo de respuesta que ha dado el 
servidor: 
• Códigos con formato 1xx: 
Respuestas informativas. Indica que la petición ha sido recibida y se está procesando. 
• Códigos con formato 2xx: 
Respuestas correctas. Indica que la petición ha sido procesada correctamente. 
• Códigos con formato 3xx: 
Respuestas de redirección. Indica que el cliente necesita realizar más acciones para finalizar la 
petición.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
63 
• Códigos con formato 4xx: 
Errores causados por el cliente. Indica que ha habido un error en el procesado de la petición a 
causa de que el cliente ha hecho algo mal. 
• Códigos con formato 5xx: 
Errores causados por el servidor. Indica que ha habido un error en el procesado de la petición a 
causa de un fallo en el servidor. 
5.2.4. Cabeceras 
Son los metadatos que se envían en las peticiones o respuesta HTTP para proporcionar información 
esencial sobre la transacción en curso. 
Cada cabecera es especificada por un nombre de cabecera seguido por dos puntos, un espacio en 
blanco y el valor de dicha cabecera seguida por un retorno de carro seguido por un salto de línea. 
Se usa una línea en blanco para indicar el final de las cabeceras. 
Si no hay cabeceras la línea en blanco debe permanecer. 
Las cabeceras le dan gran flexibilidad al protocolo permitiendo añadir nuevas funcionalidades sin tener 
que cambiar la base. 
Por eso según han ido sucediendo las versiones de HTTP se han ido añadiendo más y más cabeceras 
permitidas. 
Las cabeceras pueden tener metadatos que tienen que ser procesados por el cliente (ej. en respuesta a 
petición se puede indicar el tipo del contenido que contiene), por el servidor (ej. tipos de 
representaciones aceptables por el cliente del contenido que pide) o por los intermediarios (ej. cómo 
gestionar el cacheo por parte de los proxys). 
Dependiendo del tipo de mensaje en el que puede ir una cabecera las podemos clasificar en cabeceras 
de petición, cabeceras de respuesta y cabeceras que pueden ir tanto en una petición como en una 
respuesta. 
Podemos clasificar las cabeceras según su función. Por ejemplo: 
• Cabeceras que indican las capacidades aceptadas por el que envía el mensaje: 
• Accept (indica el MIME aceptado). 
• Accept-Charset (indica el código de caracteres aceptado). 
• Accept-Encoding (indica el método de compresión aceptado). 
• Accept-Language (indica el idioma aceptado).

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
64 
• User-Agent (para describir al cliente). 
• Server (indica el tipo de servidor). 
• Allow (métodos permitidos para el recurso). 
• Cabeceras que describen el contenido: 
• Content-Type (indica el MIME del contenido). 
• Content-Length (longitud del mensaje). 
• Content-Range. 
• Content-Encoding. 
• Content-Language. 
• Content-Location. 
• Cabeceras que hacen referencias a URIs: 
• Location (indica donde está el contenido). 
• Referer (Indica el origen de la petición). 
• Cabeceras que permiten ahorrar transmisiones: 
• Date (fecha de creación). 
• If-Modified-Since. 
• If-Unmodified-Since. 
• If-Match. 
• If-None-Match. 
• If-Range. 
• Expires. 
• Last-Modified. 
• Cache-Control. 
• Via. 
• Pragma.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
65 
• Etag. 
• Age. 
• Retry-After. 
• Cabeceras para control de cookies: 
• Set-Cookie. 
• Cookie. 
• Cabeceras para autentificación: 
• Authorization. 
• WW-Authenticate. 
• Cabeceras para describir la comunicación: 
• Host (indica máquina destino del mensaje). 
• Connection (indica cómo establecer la conexión). 
• Otras: 
• Range (para descargar solo partes del recurso). 
• Max-Forward (límite de cabeceras añadidas en TRACE). 
5.3. Solicitud HTTP 
Una solicitud HTTP es un conjunto de líneas que el navegador envía al servidor. 
Tiene 3 partes: 
• Una línea de solicitud. 
Es una línea que especifica: 
• El tipo de documento solicitado. 
• El método que se aplicará. 
• La versión del protocolo utilizada.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
66 
La línea está formada por tres elementos que deben estar separados por un espacio: 
• El método. 
• La dirección URL. 
• La versión del protocolo utilizada por el cliente (por lo general, HTTP/1.0). 
• Los campos del encabezado de solicitud. 
Son un conjunto de líneas opcionales que permiten aportar información adicional sobre la 
solicitud y/o el cliente (navegador, sistema operativo, etc.). 
Cada una de estas líneas está formada por un nombre que describe el tipo de encabezado, 
seguido de dos puntos (:) y el valor del encabezado. 
• El cuerpo de la solicitud. 
Es un conjunto de líneas opcionales que deben estar separadas de las líneas precedentes por una 
línea en blanco. 
Por ejemplo, se puede utilizar para enviar datos por un comando POST durante la transmisión 
de datos al servidor utilizando un formulario. 
Por lo tanto, una solicitud HTTP posee la siguiente sintaxis: 
MÉTODO URL VERSIÓN <crlf> 
        ENCABEZADO: Valor <crlf> 
        . . . 
        ENCABEZADO: Valor <crlf> 
        Línea en blanco <crlf> 
        CUERPO DE LA SOLICITUD (opcional) 
 
 
 
 
+ Info 
<crlf> significa retorno de carro y avance de línea y equivale a un 
salto de línea.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
67 
Lista de comandos HTTP 
Comando 
Descripción 
GET 
Solicita el recurso ubicado en la URL especificada 
HEAD 
Solicita el encabezado del recurso ubicado en la URL especificada 
POST 
Envía datos al programa ubicado en la URL especificada 
PUT 
Envía datos a la URL especificada 
DELETE 
Borra el recurso ubicado en la URL especificada 
Lista de encabezados HTTP 
Cabecera 
Descripción 
Ejemplo 
Accept 
Content-Types (tipos de 
contenido) que se aceptan 
Accept: text/plain 
Accept-Charset 
Conjunto de caracteres que se 
aceptan 
Accept-Charset: utf-8 
Accept-Encoding 
Lista de codificaciones que se 
aceptan 
Accept-Encoding: gzip, deflate 
Accept-Language 
Idiomas que se aceptan 
Accept-Language: en-US 
Accept-Datetime 
Versión de la hora y fecha que se 
aceptan 
Accept-Datetime: Thu, 31 May 
2007 20:35:00 GMT 
Authorization 
Credenciales de autorización 
Authorization: Basic 
QWxhZGRpbjpvcGVulHNlc2FtZQ== 
Cache-Control 
Se controla las políticas de caché 
Cache-Control: no-cache 
Connection 
Se controla el tipo de conexión 
Connection: keep-alive 
Connection: Upgrade 
Cookie 
Una cookie enviada previamente 
por el servidor usando Set-Cookie 
Cookie: $Version=1; Skin=new; 
Content-Length 
El tamaño del contenido de la 
petición en bytes 
Content-Length: 348

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
68 
Cabecera 
Descripción 
Ejemplo 
Content-MD5 
Un checksum en MD5 sobre el 
contenido 
Content-MD5: 
Q2hlY2sgSW50ZwdyaXR5lQ== 
Content-Type 
El tipo de contenido de la petición 
en POST o PUT 
Content-Type: application/x-www-
form-urlencoded 
Date 
La fecha y la hora de la petición 
Date: Tue, 15 Nov 1994 08:12:31 
GMT 
Forwarded 
Indica la información original del 
cliente en caso de conexión por 
proxy 
Forwarded: 
for=192.0.2.60;proto=http;by= 
203.0.113.43 Forwarded: 
for=192.0.2.43, for=198.51.100.17 
From 
La dirección de correo electrónico 
de la petición 
From: user@example.com 
Host 
El nombre de dominio o dirección 
IP (puede incluir número de 
puerto). El uso de la cabecera es 
obligatorio a partir de HTTP 1.1 
Host: en.wikipedia.org:8080 
Host: en.wikipedia.org 
Max-Forwards 
Limita el número de veces que un 
mensaje viaja a través de los 
proxies 
Max-Forwards: 10 
Origin 
Inicia una petición para servidores 
con respuesta a Access-Control-
Allow-Origin 
Origin: http://www.example-social-
network.com 
Pragma 
Implementa cabeceras en donde 
múltiples efectos se aplica a todo 
Pragma: no-cache 
Proxy-Authorization 
Credenciales de autorización para 
conectarse a un proxy 
Proxy-Authorization: Basic 
QWxhZGRpbjpvcGVulHNlc2FtZQ== 
Range 
Pide sólo una parte del contenido 
Range: bytes=500-999 
Referer 
Indica la dirección URL de donde 
proviene, en otras palabras, es la 
dirección web del botón Atrás 
Referer: http://en.wikipedia.org/ 
wiki/Main_Page 
User-Agent 
Contiene la información de la 
petición, como el navegador, el 
sistema operativo, etc. 
User-Agent: Mozilla/5.0 (X11; 
Linux x86_64; rv:12.0) 
Gecko/20100101 Firefox/21.0 
Upgrade 
Pide al servidor que se actualice la 
versión de HTTP para funcionar 
Upgrade: HTTP/2.0, HTTPS/1.3, 
IRC/6.9, RTA/x11, websocket 
Warning 
Una advertencia general sobre 
problemas de la entidad 
Warning: 199 Miscellaneous 
warning 
Fuente: (https://es.wikipedia.org/wiki/Anexo:Cabeceras_HTTP)

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
69 
 
 
 
+ Info 
Échale un vistazo al artículo "HTTP headers". 
https://developer.mozilla.org/es/docs/Web/HTTP/Headers 
 
5.4. Respuesta HTTP 
Una respuesta HTTP es un conjunto de líneas que el servidor envía al navegador. 
Está constituida por: 
• Una línea de estado: 
Es una línea que especifica la versión del protocolo utilizada y el estado de la solicitud en 
proceso mediante un texto explicativo y un código. 
La línea está compuesta por tres elementos que deben estar separados por un espacio: 
• La versión del protocolo utilizada. 
• El código de estado. 
• El significado del código. 
• Los campos del encabezado de respuesta: 
Son un conjunto de líneas opcionales que permiten aportar información adicional sobre la 
respuesta y/o el servidor. 
Cada una de estas líneas está formada por un nombre que describe el tipo de encabezado, 
seguido de dos puntos (:) y el valor del encabezado. 
• El cuerpo de la respuesta: 
Contiene el documento solicitado.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
70 
Por lo tanto, una respuesta HTTP posee la siguiente sintaxis: 
VERSIÓN-HTTP CÓDIGO SIGNIFICADO <crlf> 
      ENCABEZADO: Valor<crlf> 
      . . . 
      ENCABEZADO: Valor<crlf> 
      Línea en blanco <crlf> 
      CUERPO DE LA RESPUESTA 
<crlf> significa retorno de carro y avance de línea y equivale a un salto de línea. 
Encabezados de la respuesta 
Encabezado 
Descripción 
Content-
Encoding 
Tipo de codificación para el cuerpo de la respuesta 
Content-
Language 
Tipo de idioma en el cuerpo de la respuesta 
Content-Length 
Extensión del cuerpo de la respuesta 
Content-Type 
Tipo de contenido del cuerpo de la respuesta (por ejemplo, texto/html). Consulta: Tipos 
de MIME 
Date 
Fecha en que comienza la transferencia de datos 
Expires 
Fecha límite de uso de los datos 
Forwarded 
Utilizado por equipos intermediarios entre el navegador y el servidor 
Location 
Redireccionamiento a una nueva dirección URL asociada con el documento 
Server 
Características del servidor que envió la respuesta 
Códigos de respuesta 
Son los códigos que se ven cuando el navegador no puede mostrar la página solicitada. El código de 
respuesta está formado por tres dígitos: el primero indica el estado y los dos siguientes explican la 
naturaleza exacta del error.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
71 
Código 
Respuesta 
100-102 
Respuestas informativas 
200-226 
Respuestas satisfactorias 
300-308 
Redirecciones 
400-451 
Errores de cliente 
500-511 
Errores de servidor 
Más concretamente sería: 
Código 
Respuesta 
100 
Continue 
101 
Switching Protocol 
102 
Processing (WebDAV) 
200 
OK 
201 
Created 
202 
Acepted 
203 
Non-Authoritative Information 
204 
No Content 
205 
Reset Content 
206 
Partial Content 
207 
Multi-Status (WebDAV) 
208 
Already Reported (WebDAV) 
226 
IM Used (HTTP Delta encoding) 
300 
Multiple Choice 
301 
Moved Permanently 
302 
Found

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
72 
Código 
Respuesta 
303 
See Other 
304 
Not Modified 
305 
Use Proxy 
306 
Unused 
307 
Temporary Redirect 
308 
Permanent Redirect 
400 
Bad Request 
401 
Unauthorized 
402 
Payment Required 
403 
Forbidden 
404 
Not Found 
405 
Method Not Allowed 
406 
Not Acceptable 
407 
Proxy Authentication Required 
408 
Request Timeout 
409 
Conflict 
410 
Gone 
411 
Length Required 
412 
Precondition Failed 
413 
Payload Too Large 
414 
URI Too Long 
415 
Unsupported Media Type 
416 
Requested Range Not Satisfiable 
417 
Expectation Failed 
418 
I'm a teapot

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
73 
Código 
Respuesta 
421 
Misdirected Request 
422 
Unprocessable Entity (WebDAV) 
423 
Locked (WebDAV) 
424 
Failed Dependency (WebDAV) 
426 
Upgrade Required 
428 
Precondition Required 
429 
Too Many Requests 
431 
Request Header Fields Too Large 
451 
Unavailable For Legal Reasons 
500 
Internal Server Error 
501 
Not Implemented 
502 
Bad Gateway 
503 
Service Unavailable 
504 
Gateway Timeout 
505 
HTTP Version Not Supported 
506 
Variant Also Negotiates 
507 
Insufficient Storage 
508 
Loop Detected (WebDAV) 
510 
Not Extended 
511 
Network Authentication Required 
 
 
 
 
+ Info 
Artículo "Códigos de estado de respuesta HTTP". 
https://developer.mozilla.org/es/docs/Web/HTTP/Status

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
74 
5.5. Herramientas 
Además de los protocolos específicamente diseñados para la transferencia de archivos hay utilidades 
basadas en HTTP que también realizan esta función. 
Por ejemplo, Wget es una pequeña aplicación que permite hacer descargas de archivos, de páginas web 
y hasta de sitios completos de internet, usando el protocolo HTTP mediante la línea de comandos. 
La única desventaja de Wget es la carencia de interface gráfica, pero permite la descarga de archivos 
grandes. 
Y una de sus grandes ventajas es la posibilidad de las descargas recursivas, Una descarga recursiva no 
es más que la descarga de forma automática de todos los archivos vinculados a la página indicada, para 
lograr que esta funcione totalmente al usarla offline. 
Comandos: 
Nombre 
corto 
Nombre largo 
Descripción 
-o archivo 
--output-file=archivo 
Guarda todo el informe de la operación en un archivo de texto. Si se 
vuelve a realizar, sobrescribe el archivo. Usando -a se agrega 
información al archivo ya creado. 
-S 
--server-response 
Muestra los encabezados o http headers enviados por la aplicación y 
las respuestas recibidas del servidor. 
-d 
--debug 
Modo desarrollador, muestra información más detallada. 
-nv 
--no-verbose 
Se muestra solo información resumida. 
-i archivo 
--input-file=archivo 
Lee las direcciones URL de un archivo de texto externo. 
-t numero 
--tries=numero 
Se especifica el número de reintentos a realizar. Usa 0 o inf para 
infinitos reintentos. La opción predeterminada es 20. 
-c 
--continue 
Continúa descargando un archivo descargado parcialmente al ocurrir 
un error en la conexión, o que esta se haya cancelado 
deliberadamente. 
-E 
--adjust-extension 
Agrega a las páginas web que no la posean la extensión .html para 
facilitar su ejecución offline. 
-p 
--page-requisites 
Al usar esta opción Wget descarga todos los archivos necesarios para 
que una página funcione offline, se descargarán imágenes, css, scripts, 
etc. 
-r 
--recursive 
Crea una descarga recursiva, es decir, se descargan todos los archivos 
a los que apunten los links en la página.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
75 
Nombre 
corto 
Nombre largo 
Descripción 
-m 
--mirror 
Crea un espejo o imagen de un sitio, similar a una descarga recursiva 
pero sin ninguna restricción, es lo mismo que utilizar las opciones: -r -l 
inf -N 
-l numero 
--level=numero 
Especifica el nivel de profundidad en las descargas recursivas, el 
predeterminado es 5. 
-k 
--convert-links 
Después de finalizar la descarga, Wget reescribe los links para que 
apunten directamente a los archivos descargados en el equipo y de esa 
forma estén funcionales las páginas descargadas. 
-nc 
--no-clobber 
Impide que se vuelvan a descargar archivos que están ya en el equipo. 
-nd 
--no-directories 
No crea directorios en las descargas recursivas. 
-P carpeta 
--directory-
prefix=carpeta 
Permite establecer un directorio o carpeta determinado para todas las 
descargas. 
-A archivos 
--accept archivos 
Permite especificar qué tipo de archivos solo se desean descargar, se 
relacionan separados por comas. 
-R archivos 
--reject archivos 
Permite especificar qué tipo de archivos se desean rechazar, se 
relacionan separados por comas. 
-I 
directorios 
--include directorios 
Restringir directorios de los que solo descargar archivos en el modo 
recursivo, relacionarlos separados por comas. 
-X 
directorios 
--exclude directorios 
Inversa a la opción anterior, restringir directorios. 
-np 
--no-parent 
Evita descargar los archivos de directorios superiores, aunque los links 
apunten a ellos en descargas recursivas. 
-N 
--timestamping 
Verifica la fecha de la última modificación del archivo solicitado, si 
existe una copia en nuestro equipo y solo lo descarga del servidor si 
existe una copia más reciente. 
-O nombre 
--output-
document=nombre 
Permite renombrar un archivo. 
 
--referer=url 
Permite incluir la dirección de la página de referencia, para poder 
descargar archivos que estén protegidos contra el hotlinking. 
 
--spider 
Hace que Wget funcione como la araña de un buscador web, 
comprueba y muestra información sin descargar nada. 
 
--limit-rate=cantidad 
Limita la velocidad de descarga a una determinada cantidad de bytes 
por segundo. Para expresarla en kilobytes usa el sufijo k, o m para 
megabytes.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
76 
Nombre 
corto 
Nombre largo 
Descripción 
 
--no-cache 
Deshabilita el caché, Wget enviará al servidor la directiva Pragma: no-
cache para obtener los archivos directamente del servidor remoto. 
5.6. Conexiones Keep Alive en HTTP 
Keep Alive (mecanismos de mantenimiento de conexiones) se refiere generalmente a las conexiones de 
comunicación en una red que no están terminadas, pero que se mantienen hasta que el cliente o 
servidor interrumpe la conexión. 
La característica clave de mantener las Keep Alive es el envío de un mensaje sin contenido entre un 
servidor y un cliente. Con este mensaje, uno de los usuarios de la red (cliente o servidor) puede 
controlar si la conexión se mantendrá y evitar que se cancele. Si la conexión todavía está disponible, se 
puede utilizar para el intercambio de datos. 
Las conexiones Keep Alive también se denominan HTTP Keep-Alive, conexiones HTTP persistentes y 
reutilización de conexiones HTTP. 
El protocolo HTTP 1.1 soporta Keep-Alive por defecto, y también utiliza la canalización HTTP para 
procesar peticiones en lotes. 
HTTP 2 amplía el proceso de conexiones persistentes con opciones adicionales (por ejemplo, 
multiplexación). 
6. Protocolo HTTPS 
 
HTTP funciona bien, pero carece de seguridad. 
Cualquier dato se transmite en texto plano sin cifrar. 
Si alguien se conecta a tu red WiFi podría ver los datos que recibes y envías.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
77 
La solución es encriptar los datos para que nadie pueda leerlos. 
HTTPS (Hyper Text Transfer Protocol Secure) nació para solucionar este problema. 
HTTPS es HTTP normal sobre SSL/TSL. 
Como vimos en el epígrafe anterior, el puerto 80 es el puerto por defecto utilizado por el protocolo 
HTTP. Aunque en la actualidad la mayoría de los sitios web modernos funcionan con el protocolo 
seguro HTTPS en el puerto 443, una de las principales Autoridades Certificadoras, Let's Encrypt, 
conserva en su sección de "Mejores Prácticas", actualizada en enero de 2019 la recomendación de 
mantener el puerto 80 abierto. Esto permite que los usuarios que intenten acceder a través del 
protocolo HTTP sean automáticamente redirigidos al puerto 443, utilizando el protocolo HTTPS 
seguro. 
 
 
 
 
TAI AGE 2024 
En la convocatoria de diciembre de 2024, una respuesta indicaba 
que es el CCN quien aconseja mantener el puerto 80 abierto y 
redireccionarlo al 443, el equipo docente, en la búsqueda de 
documentos que lo corroborasen, solo encontró dicha 
recomendación mencionada por Let's Encrypt referenciada en el 
párrafo anterior. 
 
 
HTTPS usa el siguiente puerto: 
• 443/tcp. 
HTTPS/SSL usado para páginas web seguras. 
Establecimiento de una conexión segura 
Para cifrar datos se necesita una clave. 
Esa clave tendrá que saberla tanto el navegador como el servidor para poder comunicarse. 
Se utiliza un sistema de clave pública/clave privada, cifrado asimétrico. 
Las claves pública y privada son un par de números relacionados de una forma especial, de tal forma que 
un mensaje cifrado con una clave sólo puede ser cifrado con su par correspondiente.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
78 
Por ejemplo, si quiero enviar un mensaje a un servidor, lo cifro con su clave pública para que sólo se 
pueda descifrar con su clave privada. 
Después de haber acordado detalles técnicos entre navegador y servidor (versión del protocolo, 
algoritmos de cifrado asimétrico y simétrico que se usarán...), el navegador cifra una preclave generada 
en el momento con la clave pública del servidor al que nos queremos conectar. 
Eso se envía al servidor, que descifra la preclave con su clave privada. 
Tanto el servidor como el navegador aplicarán un cierto algoritmo a la preclave y obtendrán la misma 
clave de cifrado. 
De esta forma hemos superado el primer problema que teníamos: intercambiar la clave. 
A partir de entonces, simplemente se cifran y descifran los datos con esa clave. 
Como nadie más sabe esa clave, nuestras comunicaciones serán seguras y nadie podrá verlas. 
Certificate Authority 
Man-in-the-middle es un tipo de ataque en el que alguien crea un servidor falso para que creamos que 
es el original. 
Con https esto no puede pasar, ya que los sitios seguros pueden solicitar un certificado de autoridad 
(Certificate Authority) que garantizan que es quien dice ser. 
 
 
 
 
Imprescindible 
Sistema de seguridad del protocolo HTTPS: HSTS. 
HSTS (HTTP Strict Transport Security) es un mecanismo de 
seguridad diseñado para asegurar las conexiones HTTPS contra 
ataques man in the middle y secuestros de sesión (Session 
Hijacking). 
La extensión HTTPS permite a los operadores web señalar, con 
información adicional en la cabecera de HTTP, que, por un periodo 
determinado de tiempo, una página web solo será accesible por 
SSL/TSL.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
79 
Pasos de acceso de un cliente a un servidor 
A continuación, vamos a detallar paso a paso como un cliente accede a un servidor a través de HTTPS. 
1. Un usuario se conecta a https://www.masterd.es/ mediante una petición segura. 
 
2. El servidor donde está alojado el sitio web envía (si lo tiene) el certificado que incluye la clave 
pública del servidor. 
En caso de no tener certificado SSL, se producirá un error. 
 
3. El navegador comprueba que la entidad emisora del certificado (CA) sea de confianza. 
En caso contrario, pedirá al usuario que acepte el certificado bajo su responsabilidad. 
4. El navegador generará una clave simétrica, que será cifrada mediante la clave pública del 
servidor para ser enviada de manera segura al mismo.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
80 
5. De esta forma, la comunicación ya se ha establecido de manera segura, y será cifrada en ambos 
sentidos mediante la clave generada en el punto anterior. 
 
7. Protocolos (SSL y TLS) 
El protocolo SSL (Secure Socket Layer) o capa de puertos seguros), es el predecesor del protocolo 
TLS (Transport Layer Security o Seguridad de la Capa de Transporte). 
Se trata de protocolos criptográficos que proporcionan privacidad e integridad en la comunicación 
entre dos puntos en una red de comunicación. 
Esto garantiza que la información transmitida por dicha red no pueda ser interceptada ni modificada 
por elementos no autorizados, garantizando de esta forma que sólo los emisores y los receptores 
legítimos sean los que tengan acceso a la comunicación de manera íntegra. 
Protocolo SSL (Secure Socket Layer) 
SSL proporciona autenticación y privacidad de la información entre extremos sobre Internet mediante 
el uso de criptografía. 
Habitualmente, solo el servidor es autenticado (es decir, se garantiza su identidad) mientras que el 
cliente se mantiene sin autenticar. 
Características: 
• En el modelo OSi, SSL estaría en la capa de aplicación y en la de transporte. 
• Su uso más extendido es unirse a HTTP para dar lugar a HTTPS. 
• En el protocolo SSL se utiliza tanto criptografía asimétrica como simétrica. 
• La primera se utiliza para realizar el intercambio de las claves, que a su vez serán usadas para 
cifrar la comunicación mediante un algoritmo simétrico.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
81 
• En el caso de los sitios web, para el funcionamiento de este protocolo, lo que se necesita utilizar 
es un certificado SSL. 
• El servidor web tendrá instalado uno y cuando un cliente intente acceder a él, le remitirá el 
mismo con la clave pública del servidor, para enviar de esta forma la clave que se usará para 
realizar la conexión de manera segura mediante un cifrado simétrico. 
Ventajas de SSL para nuestro sitio web: 
• Protección de la Información en Tránsito: 
Se garantiza el cifrado en todas las comunicaciones con el sitio, cuando el navegador de un 
cliente conecta con el sitio web, automáticamente se negocia cifrado y todas las 
comunicaciones realizadas entre ambos son seguras, siendo ininteligibles para un tercero. 
• Identificación del Sitio Web: 
El certificado digital de un sitio web se emite para un dominio concreto, por lo que es fácil 
comparar el dominio al que nos conectamos con el que se define en el certificado. 
• Integridad de la información en tránsito: 
Si se produjera alguna modificación malintencionada o pérdida en la información intercambiada 
entre cliente y servidor se podría identificar y así descartarla. 
• No Repudio: 
Si una transmisión de datos se considera válida no se puede rechazar, ya que el protocolo 
garantiza que ambos extremos son legítimos y que se mantiene la integridad de la misma. Este 
factor es consecuencia de los tres anteriores. 
SSL implica una serie de 3 fases básicas: 
1. Negociar entre las partes el algoritmo que se usará en la comunicación. 
Durante la primera fase, el cliente y el servidor negocian qué algoritmos criptográficos se van a 
usar. Las implementaciones actuales proporcionan las siguientes opciones: 
• Para criptografía de clave pública: RSA, Diffie-Hellman, DSA (Digital Signature Algorithm) o 
Fortezza. 
• Para cifrado simétrico: RC2, RC4, IDEA (International Data Encryption Algorithm), DES 
(Data Encryption Standard), Triple DES y AES (Advanced Encryption Standard). 
• Con funciones hash: MD5 o de la familia SHA. 
2. Intercambio de claves públicas y autenticación basada en certificados digitales. 
3. Cifrado del tráfico basado en cifrado simétrico.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
82 
Funcionamiento de SSL: 
El protocolo SSL intercambia registros; opcionalmente, cada registro puede ser comprimido, cifrado y 
empaquetado con un código de autenticación del mensaje (MAC). Cada registro tiene un campo de 
content_type que especifica el protocolo de nivel superior que se está usando. 
Cuando se inicia la conexión, el nivel de registro encapsula otro protocolo, el protocolo handshake (o 
protocolo de acuerdo), que tiene el content_type 22. 
El cliente envía y recibe varias estructuras handshake: 
• Envía un mensaje ClientHello especificando una lista de conjunto de cifrados, métodos de 
compresión y la versión del protocolo SSL más alta permitida. Este también envía bytes 
aleatorios que serán usados más tarde (llamados Challenge de Cliente o Reto). Además, puede 
incluir el identificador de la sesión. 
• Después, recibe un registro ServerHello, en el que el servidor elige los parámetros de conexión a 
partir de las opciones ofertadas con anterioridad por el cliente. 
• Cuando los parámetros de la conexión son conocidos, cliente y servidor intercambian 
certificados (dependiendo de las claves públicas de cifrado seleccionadas). Estos certificados 
son actualmente X.509, pero hay también un borrador especificando el uso de certificados 
basados en OpenPGP. 
• Cliente y servidor negocian una clave secreta (simétrica) común llamada master secret, 
posiblemente usando el resultado de un intercambio Diffie-Hellman, o simplemente cifrando 
una clave secreta con una clave pública que es descifrada con la clave privada de cada uno. 
Todos los datos de claves restantes son derivados a partir de este master secret (y los valores 
aleatorios generados en el cliente y el servidor), que son pasados a través una función 
pseudoaleatoria cuidadosamente elegida. 
Protocolo TLS (Transport Layer Security) 
Se usan certificados X.509 y por lo tanto criptografía asimétrica para autentificar a la contraparte con 
quien se están comunicando y para intercambiar una llave simétrica. Esta sesión es luego usada para 
cifrar el flujo de datos entre las partes. Esto permite la confidencialidad del dato/mensaje, códigos de 
autenticación de mensajes para integridad y como un producto lateral, autenticación del mensaje. 
Varias versiones del protocolo están en aplicaciones ampliamente utilizadas como navegación web, 
correo electrónico, fax por Internet, mensajería instantánea y voz-sobre-IP (VoIP). Una propiedad 
importante en este contexto es forward secrecy, para que la clave de corta vida de la sesión no pueda 
ser descubierta a partir de la clave asimétrica de largo plazo. 
TLS es un protocolo de Internet Engineering Task Force (IETF), definido por primera vez en 1999 y 
actualizado en el RFC 5246 (agosto de 2008) y en RFC 6176 (marzo de 2011). Se basa en las 
especificaciones previas de SSL (1994, 1995, 1996) desarrolladas por Netscape Communications para 
agregar el protocolo HTTPS a su navegador Netscape Navigator. Su última versión, TLS 1.3, fue 
definida en agosto de 2018.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
83 
7.1. Historia y desarrollo 
Los primeros esfuerzos de investigación hacia la seguridad de la capa de transporte incluyeron la 
interfaz de programación de aplicaciones (API, por su sigla en inglés) de Secure Network Programming 
(SNP), la que en 1993 exploró la posibilidad de tener una API de capa de transporte segura similar a los 
sockets. Berkeley, para facilitar la retroadaptación de las aplicaciones de red preexistentes con medidas 
de seguridad. 
API de Secure Network Programming: 
Protocolo 
Publicación 
SSL 1.0 
No publicado 
SSL 2.0 
1995 
SSL 3.0 
1996 
TLS 1.0 
1999 
TLS 1.1 
2006 
TLS 1.2 
2008 
TLS 1.3 
2018 
Fuente: Wikipedia 
SSL versiones: v1.0 v2.0 y v3.0 
El protocolo SSL fue desarrollado originalmente por Netscape. 
La versión 1.0 nunca se entregó públicamente. La versión 2.0 se presentó en febrero de 1995 pero 
"contenía una cantidad de fallas de seguridad que al final llevaron al diseño de la versión SSL 3.0". 
La versión 3.0, presentada en 1996, fue un rediseño completo del protocolo producido por Paul 
Kocher, quien trabajó con los ingenieros de Netscape Phil Karlton y Alan Freier. 
Las versiones más nuevas de SSL/TLS están basadas en SSL 3.0. 
El borrador de 1996 de SSL 3.0 fue publicado por la IETF como el histórico RFC 6101. 
En octubre de 2014, se detectó una nueva vulnerabilidad sobre el protocolo SSL en su versión 3.0, la 
Vulnerabilidad de Poodle.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
84 
TLS 1.0 
TLS 1.0 fue definido en el RFC 2246 en enero de 1999 y es una actualización de SSL versión 3.0. 
Como dice el RFC, "las diferencias entre este protocolo y SSL 3.0 no son dramáticas, pero son 
suficientemente significativas como para impedir la interoperabilidad entre TLS 1.0 y SSL 3.0". 
TLS 1.0 incluye una forma en la cual la implementación puede conectarse en SSL 3.0, debilitando la 
seguridad. 
TLS 1.1 
TLS 1.1 fue definido en el RFC 4346 en abril de 2006. Es una actualización de TLS 1.0. Las diferencias 
más significativas incluyen: 
• Agrega protección contra ataques de CBC. 
• El vector de inicialización (IV) implícito fue reemplazado por un IV explícito. 
• Cambio en el manejo de los errores de relleno. 
• Soporte para el registro de parámetros de IANA. 
TLS 1.2 
TLS 1.2 fue definido originalmente en el RFC 5246 en agosto del 2008. Se basa en una especificación 
posterior de TLS 1.1. Las mayores diferencias son: 
• La combinación MD5-SHA-1 en la función pseudoaleatoria (PRF) fue reemplazada por SHA-256 
(HMAC-SHA256), con la opción de usar las PRF especificadas en la cipher-suite. 
• La combinación MD5-SHA-1 en el mensaje terminado fue reemplazada por SHA-256, sin la 
opción de usar algoritmos de hash específicos para la cipher-suite. Sin embargo, el tamaño del 
hash en el mensaje terminado es truncado a 96 bits. 
• La combinación MD5-SHA-1 en el elemento digitalmente firmado fue reemplazada por un hash 
simple negociado durante el handshake, que por defecto es SHA-1. 
• Mejoras en la habilidad de clientes y servidores para especificar que algoritmos de hash y de 
firma van a aceptar. 
• Expansión del soporte de cifras de cifrado autenticadas, usadas mayormente para modo 
Galois/Counter (GCM) y modo CCM del cifrado con Advanced Encryption Standard (AES). 
• Se agregaron definición de Extensiones de TLS y de Ciphersuites de AES.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
85 
TLS 1.2 fue después redefinido en el RFC 6176 de marzo de 2011 redactando su retrocompatibilidad 
con SSL y TLS para que dichas sesiones jamás negocien el uso de SSL versión 2.0. 
TLS 1.2 Usa para su funcionamiento dos capas, la TLS Record Protocol y la TLS Handshake Protocol. 
TLS 1.3 
TLS 1.3 fue definido en el RFC 8446 en agosto de 2018. Está basado en la anterior especificación TLS 
1.2. Las principales diferencias con TLS 1.2 incluyen: 
• Un modo 0-RTT. 
• Retiro de la hora GMT. 
• Fusiona soporte de ECC del RFC 4492 pero sin curvas explícitas. 
• Retira el campo de longitud innecesaria de la entrada de AD a cifras AEAD. 
• Cambiar el nombre de {Cliente, Servidor} KeyExchange a {Cliente, Servidor} KeyShare. 
• Añade un HelloRetryRequest explícita para rechazar el del cliente. 
• Handshake revisado a fin de proporcionar el modo 1-RTT. 
• Retiro de grupos DHE personalizados. 
• Eliminado el soporte para la compresión. 
• Eliminado el soporte para el intercambio de claves RSA estática y DH. 
• Eliminado el soporte para sistemas de cifrado no AEAD. 
7.2. Medidas de seguridad de TLS/SSL 
TLS/SSL poseen una variedad de medidas de seguridad: 
• Numerando todos los registros y usando el número de secuencia en el MAC. 
• Usando un resumen de mensaje mejorado con una clave (de forma que solo con dicha clave se 
pueda comprobar el MAC). Esto se especifica en el RFC 2104). 
• Protección contra varios ataques conocidos (incluyendo ataques man-in-the-middle), como los 
que implican un degradado del protocolo a versiones previas (por tanto, menos seguras), o 
conjuntos de cifrados más débiles.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
86 
• El mensaje que finaliza el protocolo handshake (Finished) envía un hash de todos los datos 
intercambiados y vistos por ambas partes. 
• La función pseudo aleatoria divide los datos de entrada en 2 mitades y las procesa con 
algoritmos hash diferentes (MD5 y SHA), después realiza sobre ellos una operación XOR. De 
esta forma se protege a sí mismo de la eventualidad de que alguno de estos algoritmos se 
revelen vulnerables en el futuro. 
Intercambio de claves 
Antes de que un cliente y el servidor puedan empezar a intercambiar información protegida por TLS, 
deben intercambiar en forma segura o acordar una clave de cifrado y una clave para usar cuando se 
cifren los datos (ver Cifrado). 
Entre los métodos utilizados para el intercambio/acuerdo de claves son: 
• Las claves públicas y privadas generadas con RSA (denotado TLS_RSA en el protocolo de 
handshake TLS). 
• Diffie-Hellman (llamado TLS_DH). 
• TLS_DHE. 
• TLS_ECDH (Diffie-Hellman de Curva Elíptica). 
• TLS_ECDHE (Diffie-Hellman de Curva Elíptica efímero). 
• Diffie-Hellman anónimo (TLS_DH_anon) ,2 y PSK (TLS_PSK). 
El método de acuerdo de claves TLS_DH_anon, no verifica el servidor o el usuario y por lo tanto rara 
vez se utiliza puesto que es vulnerable a un ataque de suplantación de identidad. 
Solo TLS_DHE y TLS_ECDHE proporcionan secreto-perfecto-hacia-adelante. 
Los certificados de clave pública que se utilizan durante el intercambio/acuerdo también varían en el 
tamaño de las claves de cifrado públicas/privadas utilizadas durante el intercambio y, por tanto, en la 
solidez de la seguridad que proveen. 
 
 
 
 
+ Info 
En julio de 2013, Google anunció que dejaría de utilizar claves 
públicas 1024 bits y cambiaría a claves de 2048 bits para aumentar 
la seguridad del cifrado TLS que proporciona a sus usuarios.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
87 
7.3. Puertos en uso 
Si selecciona SSL o TLS para SMTP, POP3 o IMAP4, el valor Puerto cambiará para coincidir con el 
protocolo. 
Se debe configurar el método de comunicación POP3/IMAP4/SMTP del equipo de modo que se 
corresponda con el método utilizado por el servidor de correo electrónico. 
En la mayoría de casos, los servicios de correo web seguros requieren la siguiente configuración: 
SMTP 
SSL: 465 
TLS: 587 
POP3 
SSL: 995 
TLS: 995 
IMAP4 
SSL: 993 
TLS: 993 
8. Protocolo OSPF 
Al hablar de INTERNET, tenemos que hablar del protocolo OSPF, siglas de Open Shortest Path First, (en 
español traducido como "abrir el camino más corto primero"), es un "Protocolo De Estado De Enlace" 
para encaminamiento jerárquico de pasarela interior o Interior Gateway Protocol (IGP), que usa el 
algoritmo Dijkstra, para calcular la ruta más corta entre dos nodos. 
Su medida de métrica se denomina cost, y tiene en cuenta diversos parámetros tales como el ancho de 
banda y la congestión de los enlaces. OSPF construye además una base de datos enlace-estado (Link-
State Database, LSDB) idéntica en todos los routers de la zona. 
OSPF puede operar con seguridad usando MD5 para autenticar sus puntos antes de realizar nuevas 
rutas y antes de aceptar avisos de enlace-estado. 
OSPF es probablemente el protocolo IGP más utilizado en redes grandes; IS-IS, otro protocolo de 
encaminamiento dinámico de enlace-estado, es más común en grandes proveedores de servicios. 
 
 
 
 
+ Info 
Protocolo IS-IS (del inglés Intermediate System to intermediate 
System) es un protocolo de enrutamiento (protocolo de 
Gateway interior (IGP)), que se ejecuta en la capa de enlace de 
datos (capa 2). 
Utiliza el Algoritmo de Dijkstra y está descrito por el RFC 1142.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
88 
OSPF, como sucesor natural de RIP, acepta VLSM y CIDR desde su inicio. A lo largo del tiempo, se han 
ido creando nuevas versiones, como OSPFv3 que soporta IPv6 o las extensiones multidifusión para 
OSPF (MOSPF), aunque no están demasiado extendidas. OSPF puede "etiquetar" rutas y propagar esas 
etiquetas por otras rutas. 
Una red OSPF se puede descomponer en regiones (áreas) más pequeñas. 
Hay un área especial llamada área backbone que forma la parte central de la red a la que se encuentran 
conectadas el resto de áreas de la misma. Las rutas entre las diferentes áreas circulan siempre por el 
backbone, por lo tanto, todas las áreas deben conectar con el backbone. Si no es posible hacer una 
conexión directa con el backbone, se puede hacer un enlace virtual entre redes. 
Los routers (también conocidos como encaminadores) en el mismo dominio de multidifusión o en el 
extremo de un enlace punto-a-punto forman enlaces cuando se descubren los unos a los otros. 
En un segmento de red Ethernet los routers eligen a un router designado (Designated Router, DR) y un 
router designado secundario o de copia (Backup Designated Router, BDR) que actúan como hubs para 
reducir el tráfico entre los diferentes routers. 
OSPF puede usar tanto multidifusiones (multicast) como unidifusiones (unicast) para enviar paquetes 
de bienvenida y actualizaciones de enlace-estado. Las direcciones de multidifusión usadas son 224.0.0.5 
y 224.0.0.6. Al contrario que RIP o BGP, OSPF no usa ni TCP ni UDP, sino que se encapsula 
directamente sobre el protocolo IP poniendo "89" en el campo protocolo. 
Comparación entre OSPF e IS-IS 
Ambos son protocolos de estado de enlaces que utilizan el Algoritmo de Dijkstra para encontrar el 
mejor camino a través de la red y soportan máscaras de subred de diferente longitud, pueden usar 
multicast para encontrar routers vecinos mediante paquetes hello y pueden soportar autentificación de 
actualizaciones de encaminamiento. 
Pero existen diferencias entre de IS-IS y OSPF: 
• En el modo en que la dirección de área es asignada. 
• En IS-IS, la dirección de área y de host son asignados al router entero. 
• Mientras que en OSPF el direccionamiento es asignado al nivel de interfaz. 
Por lo tanto, un router IS-IS únicamente estará en un área (Todos los routers de Nivel 1 
necesitan un router de Nivel 1-2 para conectarles a otra área). El router de Nivel 1-2 puede ver 
el resto del SA y se ofrece como ruta por defecto al área de Nivel 1. 
• En el manejo de los paquetes hello. 
Este es el único método por el cual los routers pueden saber si un router vecino sigue estando 
disponible en la red.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
89 
A diferencia de OSPF, los routers IS-IS son capaces de enviar dos tipos diferentes de saludos 
(paquetes hello). 
Los routers IS-IS pueden ser de Nivel 1, Nivel2 o Nivel 1-2, los routers CISCO son routers L1-L2, 
por lo que cada interfaz IS-IS estará habilitada para enviar tanto mensajes hello L1 como L2. 
• Respecto a su encapsulación: 
• IS-IS opera en la parte superior de la capa 2 y OSPF opera en la capa 3. 
• IS-IS es un protocolo de capa 3 con su propio paquete de capa 3, mientras que OSPF utiliza 
paquete IP. 
• La fragmentación es responsabilidad de IS-IS, pero en OSPF la fragmentación es 
responsabilidad de IP. 
9. Bibliografía 
• https://conceptodefinicion.de/internet/. 
• http://www.elmundo.es/imasd/docs/cursos/masterperiodismo/2002/rivero-master01-
usa.html. 
• http://es.wikipedia.org. 
• http://en.wikipedia.org. 
• https://www.eltiempo.com/tecnosfera/novedades-tecnologia/estudio-de-mozila-revela-el-
estado-actual-de-internet-38471. 
• http://redestelematicas.com/arquitectura-de-internet/. 
• https://datapath.io/resources/blog/what-is-an-internet-service-provider/. 
• https://es.wikibooks.org/wiki/Planificaci%C3%B3n_y_Administraci%C3%B3n_de_Redes/Tem
a_10/Estructura_jer%C3%A1rquica_de_internet. 
• https://conceptodefinicion.de. 
• http://www.hipertexto.info. 
• https://comenzandodecero.com/definicion-de-web-2-0/. 
• http://www.masadelante.com/faqs/que-significa-webmail. 
• https://www.xatakamovil.com/espacio-sony/la-mensajeria-instantanea-va-mas-alla-de-
whatsapp-11-aplicaciones-alternativas.

---

Internet: Arquitectura de red. Origen, evolución y estado actual. Principales servicios. Protocolos HTTP, HTTPS 
y SSL/TLS 
90 
• https://es.ccm.net/contents/264-el-protocolo-http. 
• https://www.cisco.com/c/es_mx/support/docs/security-vpn/ipsec-negotiation-ike-
protocols/14106-how-vpn-works.html. 
• https://www.genbeta.com/web/https-asi-funciona. 
• https://norfipc.com/internet/wget.html. 
• https://www.incibe.es/protege-tu-empresa/blog/certificado-digital-ssl-sitio-web-seleccionar-
uno. 
• https://www.redalia.es/ssl/protocolo-ssl/. 
• https://es.wikipedia.org/wiki/Internet#Uso_actua. 
• https://es.wikipedia.org/wiki/IS-IS.

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema08|Ficha Resumen del Tema 08]]
- 📖 **Fuente Raw Original**: [[wiki/sources/bloque4-tema08|Nota Fuente Oficial del Tema 08]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema08-internet-web-correo|Test Tema 08]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema07|⬅️ Tema Completo 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema09|Tema Completo 09 ➡️]]
