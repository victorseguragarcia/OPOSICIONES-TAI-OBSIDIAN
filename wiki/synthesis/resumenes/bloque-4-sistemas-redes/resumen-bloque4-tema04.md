---
title: "Resumen Completo y Profundo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID"
type: "synthesis"
tags:
  - resumen
  - resumen-profundo
  - temario-completo
  - bloque-4
  - tema-04
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema04.md]]"
  - "[[wiki/sources/bloque4-tema04]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]

# 🔴 Resumen Completo y Profundo Tema 04 (Bloque 4): Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 04**
> Guía completa y exhaustiva que recopila todo el temario oficial, marco legal/normativo, detalles de arquitectura, tablas de datos críticos, protocolos, comandos de consola y casos prácticos.

---

## 🟣 1. Desarrollo Temático Completo e Íntegro

---

Administración de Redes 
de Área Local 

---

1. Administración de Redes de Área Local 
5 
1.1. Esquemas básicos de red 
7 
1.1.1. Esquema básico 
8 
1.1.2. Esquema con zona neutra o desmilitarizada 
8 
1.1.3. Esquema con zona neutra, red interna y un solo enrutador 
10 
1.1.4. Esquema con una zona neutra y varias redes internas 
11 
1.1.5. Esquema con varias zonas neutras 
12 
1.2. Intranets y extranets 
13 
1.2.1. Intranet 
13 
1.2.2. Extranet 
14 
1.2.3. Comparativa 
15 
1.2.4. Tecnologías comunes 
15 
1.2.5. Ventajas y desafíos 
15 
1.3. Integración de sistemas 
16 
1.3.1. Red 
18 
1.3.1.1. Dirección MAC 
18 
1.3.1.2. Dirección IP 
20 
1.3.1.2.1. Conocer la IP en Windows. IPCONFIG 
20 
1.3.1.2.2. Conocer la IP en Linux. IFCONFIG 
24 
1.3.2. Datos 
27 
1.3.3. Servicios 
27 
1.3.3.1. Servicios funcionales para el usuario 
28 
1.3.3.2. Servicios de infraestructura básica 
31 
1.3.3.2.1. DHCP 
31 
1.3.3.2.2. DNS 
35 
2. Gestión de usuarios en sistemas Windows 
38 
3. Gestión de usuarios en sistemas Linux 
41 
4. Gestión de dispositivos 
44 
4.1. Administrador de discos en Windows 
44 
4.2. Administrador de discos en Linux 
50 
4.3. Gestión de impresoras/escaneres 
52

---

5. Monitorización y control de tráfico de red 
55 
5.1. Balanceo de carga 
56 
5.1.1. Algoritmos del balanceador de carga 
58 
5.1.2. Generaciones de sistemas de balanceo de carga 
61 
5.1.3. Persistencia de la sesión 
61 
5.1.4. Configuración dinámica de grupos de servidores 
62 
5.1.5. Formas de Balanceo de Carga 
62 
5.1.5.1. Por Destino 
63 
5.1.5.2. Por paquete 
63 
5.1.6. Métodos 
64 
5.1.6.1. NAT (Network Address Translation) 
64 
5.1.6.2. Balanceo de carga a nivel de enlace (capa 2) 
64 
5.1.6.3. Puerta de enlace TCP 
65 
5.1.7. El balanceo de carga dentro del ecosistema de clústeres 
65 
5.1.7.1. Clasificación general de clústeres 
67 
5.1.7.2. Funcionamiento 
67 
5.1.7.3. Ventajas y desventajas 
68 
5.1.8. Herramientas para "EC" en Windows 
69 
5.1.8.1. Configuración del Balanceo de Carga en NICs 
69 
5.1.8.2. Softwares 
70 
5.2. Herramientas de monitorización y control de trafico/red 
72 
5.3. Protocolos de gestión de red 
77 
5.3.1. CMIP 
77 
5.3.2. LDAP 
78 
5.3.3. SNMP 
79 
5.3.3.1. Funcionamiento 
80 
5.3.3.2. Desarrollo y uso 
87 
5.3.3.2.1. Versión 1 
87 
5.3.3.2.2. Versión 2 
88 
5.3.3.2.3. Versión 3 
90

---

5.3.3.3. Dificultades de implementación 
92 
5.3.3.4. Implicaciones de Seguridad SNMP 
93 
6. Gestión de red 
95 
6.1. Nmap 
96 
6.2. Tracert y Traceroute 
99 
7. Bibliografía 
100

---

Administración de Redes de Área Local 
5 
1. Administración de Redes de Área Local 
Existen muchas funciones o tareas relacionadas con la administración de red. 
En función del tamaño de la empresa u organización, y también de la planificación deseada de personal, 
existirán diversos perfiles o bien todos los roles los realizará una misma persona. 
Por tanto, pueden ser funciones del Administrador de Red o recaer en el administrador de sistemas. 
Cada empresa decidirá su organización de personal y tareas a realizar por cada cargo. 
Algunas de las tareas que son necesarias realizar son: 
• Selección e implementación del esquema básico de red. 
• Integración de sistemas. 
• Gestión usuarios. 
• Gestión de dispositivos. 
• Gestión recursos. 
• Direccionamiento. 
• Gestión de servicios. 
• Gestión de red. 
• Gestión de seguridad. 
• Monitorización y control del tráfico de red. 
• Documentación. 
• Informar a los usuarios de los cambios en las políticas de uso de la red. 
A lo largo de esta unidad vamos a profundizar en algunas de estas tareas. 
 
 
 
 
Recuerda ver las clases emitidas en Temario 
Audiovisual 
Las clases impartidas en directo y disponibles en Campus, en 
Temario Audiovisual, te ayudarán al entendimiento de la unidad, y 
además pueden tener información adicional. 
ACCEDE DIRECTAMENTE DESDE AQUÍ

---

Administración de Redes de Área Local 
6 
Para ayudar en las tareas del administrador de red, se utiliza un NMS, Network Management System. 
Un NMS, traducido como Sistema de gestión de red, es un software que permite a los administradores 
de red supervisar y administrar los diversos componentes de una red informática. 
Un NMS puede: 
• Gestionar e indicar el volumen de recursos de procesamiento y memoria requeridos para la 
administración de la red. 
• Monitorizar los componentes de software y hardware de la red. 
Permite a los usuarios monitorizar o administrar todas sus operaciones en la red. 
• Registrar los datos de los puntos remotos de una red y analizarlos para crear informes que 
facilitan el trabajo al administrador. 
Para que un NMS realice un seguimiento correcto de la red necesita: 
• Saber cuántos dispositivos están conectados. 
• Realizar una recopilación de datos de qué hacen esos dispositivos. 
Los elementos de la red transmiten a la NMS datos de telemetría con la información de gestión 
y control. 
(La telemetría se compone de dos palabras, Tele (distancia) y Metry (medir), por tanto, 
Telemetría, recopilar datos de sistemas remotos). 
Hay plataformas NMS para administrar los servicios alojados en la nube. 
 
 
 
+ Info 
Existen diversas soluciones NMS en el mercado, tanto OpenSource 
como de pago. Algunas OpenSource son:  
• Zenoss. 
• OpenNMS. 
• Zabbix.

---

Administración de Redes de Área Local 
7 
 
 
 
• Nagios. 
• Cacti. 
• PandoraFMS. 
 
1.1. Esquemas básicos de red 
Diseñar y configurar una red requiere una planificación cuidadosa de su arquitectura. Esta define cómo 
se interconectan los dispositivos y qué mecanismos regulan el flujo de información. Aunque el objetivo 
principal es facilitar la comunicación mediante protocolos y medios de transmisión, también es crucial 
proteger los recursos internos frente a amenazas externas. Para ello, se emplean elementos como 
cortafuegos, segmentación de red o zonas de aislamiento controlado. 
La arquitectura de red segura se compone de cuatro elementos esenciales que trabajan de forma 
integrada: el enrutador perimetral, la red interna, la red perimetral y la zona desmilitarizada (DMZ). 
Cada componente cumple funciones específicas en la protección de los sistemas corporativos. 
• El enrutador actúa como puerta de enlace entre la red local e Internet. Su configuración 
determina qué tráfico puede entrar o salir, funcionando como la primera línea de defensa. En 
esquemas básicos, es el único dispositivo que separa los equipos internos de las amenazas 
externas, por lo que su correcta configuración es crítica. 
• La red interna alberga los sistemas y datos sensibles de la organización, como servidores de 
bases de datos, estaciones de trabajo y recursos corporativos. Su acceso debe estar restringido 
únicamente a usuarios autorizados, evitando cualquier exposición innecesaria a Internet. Para 
aumentar su seguridad, puede segmentarse en subredes con políticas de acceso diferenciadas. 
• La red perimetral engloba todos los mecanismos que protegen la red interna desde su frontera 
con Internet. Aquí se ubican los cortafuegos, sistemas de detección de intrusiones (IDS/IPS) y, 
en muchos casos, una zona desmilitarizada (DMZ). 
• La DMZ es una subred aislada, perteneciente a una red perimetral, donde se alojan servidores 
accesibles desde el exterior, como servidores web, de correo o DNS. Su propósito es evitar que 
un ataque a estos servicios comprometa la red interna. 
A continuación, vamos a ver algunos ejemplos de esquemas de red sencillos. La elección de uno u otro 
dependerá de las necesidades de la organización.

---

Administración de Redes de Área Local 
8 
1.1.1. Esquema básico 
Utilizamos un enrutador para conectar nuestra red interna con internet. 
 
Esquema de red con una red interna y un enrutador 
Este modelo, aunque simple, es el más vulnerable. El enrutador gestiona todo el tráfico entre la red 
interna e Internet, por lo que un fallo en su configuración o seguridad podría dejar expuestos todos los 
sistemas internos. Si se aloja un servidor accesible desde fuera (como un sitio web), un atacante que lo 
comprometa podría moverse lateralmente hacia el resto de la red. 
La solución es añadir una nueva red: Una zona neutra o desmilitarizada. 
1.1.2. Esquema con zona neutra o desmilitarizada 
Este diseño de red representa la solución óptima para organizaciones que requieren ofrecer servicios a 
Internet manteniendo protegidos sus sistemas internos. La zona neutra, también conocida 
técnicamente como DMZ (DeMilitarized Zone), establece un área intermedia entre la red corporativa 
privada y las redes externas. Aunque el término "zona neutra" se utiliza coloquialmente en algunos 
entornos, es importante destacar que "DMZ" es la denominación técnica correcta y estandarizada.

---

Administración de Redes de Área Local 
9 
El funcionamiento de esta zona se basa en un principio fundamental: los servidores públicos (como 
web, correo o DNS) se ubican en este segmento especial, mientras que los sistemas críticos 
permanecen en la red interna protegida. Esto crea una barrera de seguridad que impide el acceso 
directo desde Internet a los recursos sensibles. 
Para implementar correctamente esta arquitectura, se utilizan cortafuegos profesionales configurados 
con reglas estrictas. La configuración más común utiliza un cortafuegos en trípode (three-legged 
firewall), que dispone de tres interfaces de red conectadas respectivamente a: 
• Interfaz hacia Internet: Filtra el tráfico entrante, permitiendo solo conexiones a los puertos y 
servicios específicos expuestos en la DMZ. 
• Interfaz hacia la DMZ: Aísla los servidores públicos, impidiendo que inicien conexiones hacia la 
red interna. 
• Interfaz hacia la red interna: Restringe severamente el acceso, permitiendo solo tráfico 
autorizado y conexiones iniciadas desde dentro. 
Existen dos enfoques principales para implementar esta solución. 
• Dos cortafuegos independientes (configuración "sandwich"), ideal para entornos de alta 
seguridad. 
• Un único cortafuegos en trípode, más económico, pero igualmente seguro si está bien 
configurado. 
Es importante comprender que la función "DMZ host" en routers domésticos difiere completamente del 
concepto profesional de zona desmilitarizada. Mientras que la versión doméstica simplemente redirige 
todo el tráfico a un dispositivo, la DMZ empresarial (o zona neutra correctamente implementada) 
aplica filtrado granular y políticas de seguridad estrictas para cada servicio expuesto. 
La correcta implementación de esta arquitectura sigue estándares internacionales de seguridad y 
cumple con principios fundamentales como el mínimo privilegio y la defensa en profundidad. Esto 
garantiza que, incluso si un atacante compromete un servidor en la zona neutra/DMZ, el cortafuegos 
en trípode actuará como última barrera para proteger los sistemas críticos de la organización. 
 
 
 
 
Atención 
Los enrutadores domésticos son llamados incorrectamente en 
muchas ocasiones DMZ host, pero no es una definición correcta de 
zona desmilitarizada.

---

Administración de Redes de Área Local 
10 
 
Esquema de red con una zona neutra, una red interna y dos enrutadores 
A partir de este esquema se pueden proponer algunas modificaciones según las necesidades de la 
organización. Vamos a ver algunas de las configuraciones más utilizadas. 
1.1.3. Esquema con zona neutra, red interna y un solo enrutador 
Esta configuración representa una solución intermedia entre el esquema básico (sin DMZ) y la 
implementación óptima con doble cortafuegos. Aunque menos segura que el diseño con dos 
dispositivos independientes, ofrece mejores protecciones que una red sin segmentación. 
• Interfaz WAN: Conectada a Internet, con filtrado básico de tráfico entrante. 
• Interfaz DMZ: Para servidores accesibles desde el exterior (web, correo). 
• Interfaz LAN: Protege la red interna con políticas estrictas.

---

Administración de Redes de Área Local 
11 
 
Esquema de red con una zona neutra, una red interna y un solo enrutador 
El principal valor de este diseño radica en su equilibrio entre coste y seguridad básica. Permite aislar los 
servidores públicos en la zona neutra mientras protege la red interna, todo con un solo equipo. Sin 
embargo, esta simplicidad implica limitaciones importantes, ya que concentra toda la seguridad en un 
único punto que, si falla, comprometería toda la infraestructura. 
1.1.4. Esquema con una zona neutra y varias redes internas 
Este diseño avanzado se recomienda cuando la organización maneja distintos niveles de sensibilidad en 
sus sistemas o requiere segregación interna adicional. La arquitectura combina la protección perimetral 
de una DMZ tradicional con una segmentación interna estricta, creando múltiples redes aisladas dentro 
de la infraestructura corporativa.

---

Administración de Redes de Área Local 
12 
 
Esquema de red con una zona neutra, dos redes internas y dos enrutadores 
1.1.5. Esquema con varias zonas neutras 
Si necesitamos ofrecer servicios bien diferenciados al exterior, podemos optar por tener varias zonas 
neutras. 
También podemos tener varias salidas diferentes a internet diferenciados por el exterior puede optar 
por tener dos zonas neutras O incluso dos salidas diferentes a Internet. 
De esta forma aislamos los servicios entre sí.

---

Administración de Redes de Área Local 
13 
 
Esquema de red con dos zonas neutras, una red interna y tres enrutadores 
1.2. Intranets y extranets 
Las intranets y extranets son tipos de redes privadas utilizadas por las organizaciones para gestionar el 
acceso a sus recursos digitales. Aunque ambas emplean tecnologías propias de Internet, su diferencia 
fundamental radica en quién puede acceder a ellas y con qué nivel de permisos. 
1.2.1. Intranet 
Una intranet es una red interna privada utilizada exclusivamente por los miembros de una organización. 
Se basa en los mismos protocolos y servicios que Internet (HTTP/HTTPS, navegadores web y 
servidores), pero con acceso restringido mediante sistemas de autenticación robustos. Su principal 
objetivo es centralizar la información corporativa y facilitar la comunicación y colaboración entre 
departamentos, funcionando como una plataforma unificada para los recursos digitales de la empresa. 
Entre sus funciones más habituales destacan el acceso al portal del empleado -donde se gestionan 
nóminas, solicitudes de vacaciones y beneficios-, sistemas de gestión documental compartida como 
SharePoint o Nextcloud, y herramientas colaborativas que incluyen desde agendas grupales hasta chats 
corporativos. Muchas organizaciones también integran sus sistemas ERP (Enterprise Resource Planning: 
software que centraliza y automatiza los procesos internos) y CRM (Customer Relationship 
Management: sistema para gestionar relaciones e interacciones con usuarios o ciudadanos) internos en 
la intranet para optimizar los procesos empresariales.

---

Administración de Redes de Área Local 
14 
A nivel de infraestructura, las intranets suelen implementarse en servidores locales o entornos de nube 
privada, nunca expuestos directamente a Internet para garantizar máxima seguridad. Esta arquitectura 
se protege mediante firewalls perimetrales, segmentación de red a través de VLANs (Virtual LANs: 
redes locales virtuales que separan lógicamente el tráfico), y estrictos controles de acceso basados en 
roles. Los mecanismos de autenticación más comunes incluyen integración con LDAP, Active Directory 
o sistemas SSO (Single Sign-On) empresariales. 
Algunos ejemplos prácticos de uso son los portales de recursos humanos para autogestión de 
empleados, repositorios de documentos corporativos con control de versiones, y plataformas de 
formación interna con cursos e-learning. En empresas distribuidas geográficamente, la intranet suele 
complementarse con acceso VPN para teletrabajadores, manteniendo siempre los máximos estándares 
de seguridad. 
1.2.2. Extranet 
La extranet es una extensión segura de la intranet que permite el acceso controlado desde fuera de la 
organización. Está diseñada específicamente para compartir información y recursos de forma selectiva 
con agentes externos autorizados, como clientes prioritarios, proveedores certificados o socios 
estratégicos. A diferencia de una página web pública convencional, la extranet mantiene su carácter de 
red privada, donde cada acceso está estrictamente regulado mediante sistemas de identificación 
robustos que pueden incluir credenciales personalizadas, certificados digitales, autenticación 
multifactor o conexiones mediante redes privadas virtuales (VPN). 
Esta solución tecnológica facilita la colaboración empresarial avanzada, permitiendo casos de uso como 
el seguimiento en tiempo real de pedidos por parte de proveedores, la descarga de documentación 
técnica confidencial para clientes autorizados, o la gestión compartida de proyectos con partners 
estratégicos. Para garantizar la máxima seguridad, las extranets implementan arquitecturas 
especializadas que combinan zonas desmilitarizadas (DMZ) para aislar los servidores expuestos, 
firewalls de última generación con inspección profunda de paquetes, y segmentación estricta de 
servicios mediante VLANs. 
Un aspecto clave de las extranets modernas es su integración con tecnologías empresariales como APIs 
REST seguras para interoperabilidad entre sistemas, portales B2B personalizables, y plataformas de 
gestión documental con control granular de permisos. Todo ello sin perder las ventajas de accesibilidad 
remota que ofrece la nube, pero manteniendo los más altos estándares de ciberseguridad corporativa 
mediante protocolos como TLS 1.3 para el cifrado de comunicaciones y sistemas SIEM para la 
monitorización continua de accesos. 
Ejemplos prácticos incluyen plataformas de facturación electrónica para proveedores, entornos 
colaborativos para desarrollo conjunto de productos con partners tecnológicos, o portales de 
autoservicio para clientes premium con acceso a informes personalizados y herramientas de análisis 
exclusivas. Estas implementaciones demuestran cómo la extranet se ha convertido en un elemento 
estratégico para la transformación digital de las relaciones empresariales, siempre equilibrando 
funcionalidad con seguridad.

---

Administración de Redes de Área Local 
15 
1.2.3. Comparativa 
Aspecto 
Intranet 
Extranet 
Acceso 
Solo usuarios internos (empleados) 
Usuarios internos y externos autorizados 
Seguridad 
Alta, controlada internamente 
Requiere medidas de seguridad adicionales 
Alcance 
Red interna de la organización 
Parte controlada y compartida de la red interna 
Ejemplos de uso 
Portal del empleado, recursos internos 
Portal de proveedores, seguimiento de pedidos 
1.2.4. Tecnologías comunes 
Las intranets y extranets comparten una base tecnológica común que integra servidores web, sistemas 
avanzados de autenticación y arquitecturas de red seguras. Los usuarios acceden habitualmente 
mediante navegadores web estándar, mientras que, en el backend, sistemas como LDAP o Active 
Directory gestionan de forma centralizada los permisos y el control de acceso a los recursos. Estas 
soluciones implementan protocolos universales como HTTP y HTTPS, utilizando cifrado TLS/SSL para 
asegurar la confidencialidad e integridad de todas las comunicaciones. 
En el caso específico de las extranets, se incorporan medidas de seguridad adicionales para proteger los 
accesos externos. Las conexiones VPN cifradas permiten a usuarios autorizados conectarse de forma 
remota con los mismos niveles de seguridad que tendrían dentro de la red corporativa. Además, es 
práctica común implementar zonas desmilitarizadas (DMZ) que aíslan estratégicamente los servidores 
accesibles desde el exterior, creando una barrera de protección adicional para la red interna. Estas DMZ 
suelen incluir firewalls de última generación con inspección profunda de paquetes y sistemas de 
prevención de intrusiones. 
La evolución tecnológica ha permitido que ambas plataformas incorporen funcionalidades avanzadas 
como APIs REST seguras para la integración con otros sistemas empresariales, soluciones SSO (Single 
Sign-On) para una experiencia de usuario más fluida, y arquitecturas escalables basadas en 
microservicios. Estas mejoras mantienen los principios de seguridad mientras ofrecen mayor flexibilidad 
y capacidad de adaptación a las necesidades cambiantes de las organizaciones modernas. 
1.2.5. Ventajas y desafíos 
Estos sistemas de red ofrecen ventajas estratégicas clave para las organizaciones modernas. Al 
centralizar la información crítica en plataformas unificadas, las empresas logran optimizar sus 
operaciones, reducir costes operativos y mejorar sustancialmente la colaboración tanto interna como 
con socios externos. La automatización de procesos administrativos y la disponibilidad inmediata de 
datos actualizados generan ganancias significativas en eficiencia operativa, permitiendo una toma de 
decisiones más ágil e informada.

---

Administración de Redes de Área Local 
16 
No obstante, su implementación conlleva retos técnicos y de seguridad considerables. Las extranets, en 
particular, introducen complejidades adicionales al requerir una exposición controlada de recursos a 
usuarios externos. Esto exige protocolos de seguridad avanzados que incluyen: 
• Sistemas de autenticación multifactorial. 
• Cifrado extremo a extremo de las comunicaciones. 
• Estricta segmentación de redes mediante VLANs y zonas DMZ. 
• Monitorización continua con herramientas SIEM. 
• Auditorías periódicas de seguridad. 
La gestión de identidades y accesos se convierte en un componente crítico, requiriendo soluciones IAM 
(Identity and Access Management) capaces de administrar permisos granulares mientras mantienen la 
usabilidad. Estos desafíos técnicos, aunque significativos, pueden mitigarse mediante arquitecturas bien 
planificadas y el cumplimiento de estándares de ciberseguridad como ISO 27001 o el Esquema Nacional 
de Seguridad. 
El equilibrio entre accesibilidad y protección representa el principal reto en la administración de estas 
redes, donde cada conexión externa debe evaluarse en términos de valor empresarial versus riesgo 
potencial. Las organizaciones que logran implementar estos controles sin comprometer la experiencia 
del usuario obtienen una ventaja competitiva sustancial en el entorno digital actual. 
1.3. Integración de sistemas 
En la actualidad es muy frecuente tener redes heterogéneas en las que conviven diferentes sistemas 
operativos, tanto a nivel de diente como de servidor. 
A nivel de servidor lo normal es encontrar: 
• Sistemas basados en Windows Server. 
• Sistemas basados en Linux. 
A nivel de cliente nos encontramos una mayor variedad de sistemas operativos y un mayor número de 
sus respectivas versiones. Algunos de ellos son: 
• Windows. 
• Linux. 
• MAC OS. 
• Sistemas operativos para dispositivos móviles: 
• Android. 
• iOS.

---

Administración de Redes de Área Local 
17 
No existe el sistema ideal. Cada uno tiene ventajas y desventajas. 
Una tarea importante es permitir la comunicación entre los diferentes dispositivos, 
independientemente del sistema operativo, hardware y software de red que utilicen. 
 
Esquema básico de red con múltiples sistemas operativos 
Para que esto pueda funcionar debemos trabajar en tres niveles de integración: 
• Red. 
Para que los equipos puedan comunicarse entre sí. 
• Datos. 
Debemos garantizar la seguridad de la información, la disponibilidad y el acceso por los distintos 
equipos. Además, debemos permitir que puedan intercambiar datos. 
• Servicios. 
Todos los equipos deben poder acceder a los servicios indistintamente de su sistema operativo y 
del sistema operativo del equipo que ofrece los servicios.

---

Administración de Redes de Área Local 
18 
1.3.1. Red 
Para que una red funcione correctamente como mínimo debe disponer de los siguientes servicios: 
• Enrutamiento. 
Se deben utilizar enrutadores o servidores configurados como enrutadores para permitir la 
comunicación entre redes. 
• Servidor DHCP. 
Permite asignar automáticamente la configuración IP a los equipos clientes de la red. 
Este servicio es muy importante ya que facilita la conexión de los equipos a la red. 
Por otro lado, aprovecha mejor las direcciones IPs (especialmente útil cuando hay más 
dispositivos que direcciones IP). 
Los ordenadores apagados o desconectados liberan la IP que se les había asignado para que 
pueda usarla otro equipo. 
• Servidor DNS. 
Permite mantener una equivalencia entre un nombre de servidor y su dirección IP. 
 
 
 
 
El experto opina 
Estos tres servicios se pueden implementar en un servidor 
Windows, pero nosotros aconsejamos utilizar un servidor basado 
en Linux, ya que es gratis y tiene mejor rendimiento y seguridad. 
 
1.3.1.1. Dirección MAC 
MAC (siglas en inglés de Media Access Control). 
Es un identificador (único) que corresponde de forma única a una tarjeta o dispositivo de red. 
Está formado por 48 bits; 6 bloques de dos caracteres hexadecimales (8 bits).

---

Administración de Redes de Área Local 
19 
Se la conoce también como dirección física (única para cada dispositivo). 
Está determinada y configurada por el IEEE (los últimos 24 bits) y el fabricante (primeros 24 bits) 
utilizando el Organizationally Unique Identifier. 
 
 
 
 
+ Info 
La mayoría de los protocolos que trabajan en la capa 2 del modelo 
OSI usan una de las tres numeraciones manejadas por el IEEE: 
MAC-48, EUI-48, y EUI-64, las cuales han sido diseñadas para ser 
identificadores globalmente únicos. 
No todos los protocolos de comunicación usan direcciones MAC, y 
no todos los protocolos requieren identificadores globalmente 
únicos. 
 
 
Para conocer la dirección IP de una MAC, existe el protocolo RARP (Reverse Address Resolution 
Protocol) o Protocolo de Resolución de Direcciones Inverso (inverso del ARP) que nos dará la IP que 
necesitamos. 
El RARP está descrito en RFC 903 y el ARP en el RFC 826. 
Posteriormente, el uso del protocolo Bootstrap (BOOTP) dejó obsoleto el RARP porque funciona con 
paquetes del User Datagram Protocol (UDP), que se reenvían a través de los routers (eliminando la 
necesidad de disponer de un servidor RARP en cada subred) y, además, BOOTP ya tiene un conjunto de 
funciones mayor, que permite obtener más información y no solamente la dirección IP. 
Si solo conocemos la dirección del recurso de red, en Windows disponemos del comando "getmac". 
Comando "getmac": 
• Devuelve la dirección Media Access Control (MAC) y la lista de protocolos de red asociados a 
cada dirección de todas las tarjetas de red de cada equipo, ya sea de forma local o a través de 
una red. 
• Este comando es especialmente útil si desea escribir la dirección MAC en un analizador de red o 
si necesita saber qué protocolos se están usando actualmente en cada adaptador de red de un 
equipo.

---

Administración de Redes de Área Local 
20 
Cambiar una dirección Mac: 
• Aunque, en principio, la MAC de un dispositivo no se puede cambiar (como hemos dicho antes, 
la MAC esta físicamente fijada en el dispositivo), en algunas ocasiones es necesario hacerlo. (Lo 
más conveniente es no hacerlo). 
• Existen herramientas que pueden hacer al sistema operativo creer que el NIC tiene la dirección 
MAC de la elección de un usuario. Estas herramientas son conocidas como MAC spoofing o 
suplantación de dirección MAC. 
• El cambio de la dirección MAC asignada puede permitir que se incumplan las listas de control de 
acceso en los servidores o routers, o bien ocultar un ordenador en una red o permitir que se 
haga pasar por otro dispositivo de red. 
1.3.1.2. Dirección IP 
La IP de tu equipo te permite identificarlo dentro de una red. Por lo tanto, será necesario conocerla para 
realizar determinadas configuraciones de red y permitir que otros equipos y servicios se conecten con 
tu equipo. 
Existen dos tipos de dirección IP: 
• IP privada. 
Es la que utiliza cada ordenador dentro de su red local y permite identificar a los distintos 
equipos que están conectados a ella. 
• IP pública. 
Es la que se muestra al resto de dispositivos que están fuera de esa red. 
En este caso todos los equipos conectados a un mismo router comparten la misma IP pública, ya 
que es el router el que hace las funciones de puerta de entrada/salida. 
1.3.1.2.1. Conocer la IP en Windows. IPCONFIG 
Para conocer la IP en Windows, desde "cmd" (símbolo del sistema), escribimos "ipconfig" y nos 
mostrara en pantalla la información de nuestra red. 
El comando ipconfig es importantísimo en la gestión de la red. 
IPCONFIG muestra la configuración actual de red TCP/IP y actualiza la configuración de DHCP y los 
servidores DNS del sistema de nombres de dominio

---

Administración de Redes de Área Local 
21 
Si no se indica ningún parámetro, ipconfig muestra: 
• Las direcciones IPv4 (Protocolo de Internet versión 4) e IPv6. 
• La máscara de subred. 
• Y la puerta de enlace predeterminada para todos los adaptadores. 
Sintaxis: 
ipconfig [/allcompartments] [/all] [/renew [<adapter>]] [/release [<adapter>]] 
[/renew6[<adapter>]] [/release6 [<adapter>]] [/flushdns] [/displaydns] 
[/registerdns] [/showclassid <adapter>] [/setclassid <adapter> [<classID>]] 
Parámetros: 
• /all 
Muestra la configuración TCP/IP completa de todos los adaptadores. Los adaptadores pueden 
representar interfaces físicas, como adaptadores de red instalados o interfaces lógicas como 
conexiones de acceso telefónico. 
• /displaydns 
Muestra el contenido de la memoria caché de la resolución del cliente DNS, que incluye las 
entradas cargadas previamente desde el archivo de hosts local y los registros de recursos que se 
han obtenido recientemente para las consultas de nombres resueltas por el equipo. 
El servicio cliente DNS usa esta información para resolver rápidamente los nombres consultados 
con frecuencia, antes de consultar sus servidores DNS configurados. 
• /flushdns 
Vacía y restablece el contenido de la memoria caché de la resolución del cliente DNS. 
Durante la solución de problemas de DNS, puede usar este procedimiento para descartar las 
entradas de caché negativas de la memoria caché, así como cualquier otra entrada que se haya 
agregado dinámicamente. 
• /registerdns 
Inicia el registro dinámico manual de los nombres DNS y las direcciones IP que se configuran en 
un equipo.

---

Administración de Redes de Área Local 
22 
Se utiliza este parámetro para solucionar un error de registro de nombres DNS o resolver un 
problema de actualización dinámica entre un cliente y el servidor DNS sin reiniciar el equipo 
cliente. 
La configuración de DNS en las propiedades avanzadas del protocolo TCP/IP determina los 
nombres que se registran en DNS. 
• /Release[<adapter>] 
Envía un mensaje DHCPRELEASE al servidor DHCP para liberar la configuración actual de DHCP 
y descartar la configuración de la dirección IP para todos los adaptadores (si no se especifica un 
adaptador) o para un adaptador específico, si se incluye el parámetro adaptador. 
Este parámetro deshabilita TCP/IP para los adaptadores configurados para obtener una 
dirección IP automáticamente. 
Para especificar un nombre de adaptador, escribimos el nombre que nos muestra (del 
adaptador) cuando ejecutamos ipconfig sin parámetros. 
• /release6[<adapter>] 
Envía un mensaje DHCPRELEASE al servidor DHCPv6 para liberar la configuración actual de 
DHCP y descartar la configuración de la dirección IPv6 para todos los adaptadores (si no se 
especifica un adaptador) o para un adaptador específico, si se incluye el parámetro Adapter. 
Este parámetro deshabilita TCP/IP para los adaptadores configurados para obtener una 
dirección IP automáticamente. 
Para especificar un nombre de adaptador, escribimos el nombre que nos muestra (del 
adaptador) cuando ejecutamos ipconfig sin parámetros. 
• /Renew[<adapter>] 
Renueva la configuración de DHCP para todos los adaptadores (si no se especifica un 
adaptador) o para un adaptador específico si se incluye el parámetro de adaptador. 
Este parámetro solo está disponible en equipos con adaptadores que estén configurados para 
obtener una dirección IP automáticamente. 
• /renew6[<adapter>] 
Renueva la configuración de DHCPv6 para todos los adaptadores (si no se especifica un 
adaptador) o para un adaptador específico si se incluye el parámetro de adaptador. 
Este parámetro solo está disponible en equipos con adaptadores que estén configurados para 
obtener una dirección IPv6 automáticamente. Para especificar un nombre de adaptador, escriba 
el nombre del adaptador que aparece cuando se usa ipconfig sin parámetros.

---

Administración de Redes de Área Local 
23 
• /setclassid<adapter> [<classID>] 
Configura el identificador de clase DHCP para un adaptador especificado. 
Para establecer el identificador de clase de DHCP para todos los adaptadores, se utiliza el 
carácter comodín de asterisco (*) en lugar del adaptador. 
Este parámetro solo está disponible en equipos con adaptadores que estén configurados para 
obtener una dirección IP automáticamente. Si no se especifica un identificador de clase DHCP, 
se quita el ID. de clase actual. 
• /showclassid<adapter> 
Muestra el identificador de clase DHCP de un adaptador especificado. 
Para ver el identificador de clase de DHCP para todos los adaptadores, se utiliza el carácter 
comodín de asterisco (*) en lugar del adaptador. 
Este parámetro solo está disponible en equipos con adaptadores que estén configurados para 
obtener una dirección IP automáticamente. 
• /? 
Muestra la Ayuda en el símbolo del sistema. 
Observaciones para el comando ipconfig: 
• Este comando es muy útil en los equipos que están configurados para obtener una dirección IP 
automáticamente, ya que permite a los usuarios determinar qué valores de configuración de 
TCP/IP han sido configurados por DHCP, el direccionamiento IP privado automático (APIPA) o 
una configuración alternativa. 
• Si el nombre proporcionado para el adaptador contiene espacios, hay que escribir el nombre 
entre comillas. 
• Ipconfig admite el uso del carácter comodín de asterisco (*). Nos permite así, especificar los 
adaptadores con nombres que comienzan por una cadena o adaptadores especificados con 
nombres que contienen una cadena especificada. 
Por ejemplo, Local* coincide con todos los adaptadores que comienzan con la cadena local y 
*Con* coincide con todos los adaptadores que contienen la cadena con. 
Ejemplos: 
• Para mostrar la configuración básica de TCP/IP de todos los adaptadores, se utiliza: 
ipconfig 
• Para mostrar la configuración TCP/IP completa de todos los adaptadores, se utiliza: 
ipconfig /all

---

Administración de Redes de Área Local 
24 
• Para renovar una configuración de dirección IP asignada por DHCP solo para el adaptador de 
conexión de área local, se utiliza: 
ipconfig /renew Local Area Connection 
• Para vaciar la memoria caché de la resolución DNS al solucionar problemas de resolución de 
nombres DNS, se utiliza: 
ipconfig /flushdns 
• Para mostrar el ID. de clase de DHCP para todos los adaptadores cuyos nombres empiecen por 
local, se utiliza: 
ipconfig /showclassid Local* 
• Para establecer el identificador de clase DHCP del adaptador de conexión de área local que se va 
a probar, se utiliza: 
ipconfig /setclassid Local Area Connection TEST 
1.3.1.2.2. Conocer la IP en Linux. IFCONFIG 
En GNU/Linux utilizamos el comando ifconfig (equivalente a ipconfig de Windows) 
Ifconfig («configuración de interfaz») permite configurar o desplegar numerosos parámetros de las 
interfaces de red residentes en el núcleo, como la dirección IP (dinámica o estática), o la máscara de 
red. 
Si se llama sin argumentos suele mostrar la configuración vigente de las interfaces de red activas, con 
detalles como la dirección MAC o el tráfico que ha circulado por las mismas hasta el momento. Las 
interfaces de red en Linux se suelen denominar eth (eth0, eth1, etc.). 
Sintaxis: 
ifconfig interfaz [dirección [parámetros]] 
Usamos simplemente «ifconfig» sin comillas en el terminal, el resultado se mostrará en pantalla. 
El comando ifconfig, al igual que Windows, también admite parámetros. 
Parámetros para ifconfig: (Las opciones que simplemente activan alguna característica pueden usarse 
para desactivarla).

---

Administración de Redes de Área Local 
25 
• up. 
Marca la interfaz como disponible para que sea usada por la capa IP. Esta opción va implícita 
cuando lo que se da en la línea de órdenes es una dirección. 
También permite reactivar una interfaz que se ha desactivado temporalmente mediante la 
opción down. 
Esta opción corresponde a los indicadores UP y RUNNING. 
IP: 46.6.184.82. 
• down. 
Marca la interfaz como inaccesible a la capa IP. Esto inhabilita cualquier tráfico IP a través de la 
interfaz. Es importante darse cuenta de que esto también borra los registros de la tabla de 
encaminamiento correspondientes a esa interfaz de forma automática. 
• netmask (máscara). 
Asigna una máscara de subred a una interfaz. Se puede dar como un valor de 32 bits en 
hexadecimal precedido del prefijo 0x, o en notación de cuaterna usando números decimales 
separados por puntos. 
Aunque la notación en forma de cuaterna es más común, la representación hexadecimal es 
muchas veces más fácil de usar. 
Las máscaras de red son esencialmente binarias, y es más fácil hacer una conversión de binario a 
hexadecimal que una binario a decimal. 
• pointopoint (dirección). 
Se usa para enlaces IP punto-a-punto en los que intervienen únicamente dos máquinas. Esta 
opción es necesaria para, por ejemplo, configurar las interfaces SLIP o PLIP. Si se ha definido una 
dirección punto a punto, ifconfig muestra el indicador POINTOPOINT. 
• broadcast (dirección). 
La dirección de difusión se obtiene, generalmente, usando la parte de red de la dirección y 
activando todos los bits de la parte correspondiente a la máquina. Algunas implementaciones de 
los protocolos IP, esta opción proporciona un método para adaptarse a esos entornos más raros. 
ifconfig confirma el establecimiento de una dirección de difusión incluyendo el indicador 
BROADCAST. 
• Irq. 
Permite establecer la línea de IRQ usado por ciertos dispositivos. Esto es especialmente útil para 
PLIP, pero también puede ser de utilidad para algunas tarjetas Ethernet.

---

Administración de Redes de Área Local 
26 
• metric (número). 
Puede ser usada para asignar un valor de métrica a la tabla de encaminamiento creada para la 
interfaz. Esta métrica es usada por el Protocolo de Información de Encaminamiento (RIP) para 
construir las tablas de encaminamiento para la red. 
El valor usado por omisión por ifconfig es cero. Si no está ejecutando un demonio RIP, no 
necesita usar esta opción para nada; si por el contrario lo usa, sólo tendrá que modificar este 
valor en contadas ocasiones. 
• mtu (bytes). 
Esto fija la unidad máxima de transferencia, o lo que es lo mismo, el máximo número de octetos 
que la interfaz es capaz de manejar en una única transacción. 
Para Ethernets, la MTU toma el valor 1500 por omisión (que es el tamaño máximo permitido 
para un paquete Ethernet); para interfaces tipo SLIP, el valor por defecto es 296. No hay 
tamaño límite para el MTU en enlaces SLIP, pero este valor es una buena garantía. 
• arp. 
Esta opción es específica de redes de difusión como las Ethernet o las de radio-paquetes. 
Permite el uso de ARP, el Protocolo de Resolución de Direcciones, para detectar la dirección 
física de las máquinas conectadas a la red. Para redes de difusión, esta opción es habilitada por 
omisión. Si ARP está desactivado, ifconfig muestra el indicador NOARP. 
-arp inhabilita el uso de ARP para esta interfaz. 
• promisc. 
Pone la interfaz en modo promiscuo. En una red de difusión, esto hace que la interfaz reciba 
todos los paquetes, independientemente de si eran para ella o no. Esto permite el análisis del 
tráfico de red utilizando utilidades como filtros de paquetes, también llamado fisgoneo de 
Ethernet. Se trata de una buena técnica para localizar problemas de red que de otra forma 
resultan difíciles de detectar. 
Herramientas como tcpdump se basan en esto. 
Esta opción también permite a los atacantes hacer cosas como filtrar el tráfico de su red en 
busca de contraseñas. Para evitarlo, se pueden usar protocolos de autentificación segura, como 
Kerberos o SS (Secure Shell). 
–promisc desactiva el modo promiscuo. 
• Allmulti. 
Las direcciones de envío múltiple (multicast) son como las direcciones de difusión de Ethernet, 
excepto que, en lugar de incluir automáticamente a todo el mundo, los únicos que reciben 
paquetes enviados a una dirección de envío múltiple son aquellos programados para escucharla.

---

Administración de Redes de Área Local 
27 
Esto es útil para aplicaciones como videoconferencia basada en Ethernet o audio para red, en los 
que sólo los interesados pueden escuchar. 
Las direcciones de envío múltiple están soportadas por casi todas las controladoras Ethernet 
(pero no todas). 
Cuando esta opción está activa, la interfaz recibe y envía paquetes de envío múltiple para su 
proceso. 
–allmulti deshabilitar el modo allmulti. 
1.3.2. Datos 
Los datos son, junto al personal, el activo más importante de una empresa. 
Se debe garantizar la integración entre distintos sistemas operativos para que los equipos puedan 
compartir información entre sí. 
Los servicios más utilizados para compartir datos son: 
• Samba. 
Permite compartir archivos e impresoras entre sistemas Windows y Linux. 
• NFS (Network File System). 
Está especialmente diseñado para compartir archivos entre sistemas Linux, pero las últimas 
versiones de Windows Server pueden utilizarlo. 
En la actualidad, en lugar de servidores de archivos se usan sistemas de almacenamiento en red 
dedicados como las unidades NAS (Network Attached Storage). 
Otra forma de compartir datos es utilizar los sistemas de ficheros distribuidos. 
Los sistemas de ficheros distribuidos permiten acceder de forma transparente a los datos que se 
almacena en varios servidores (se percibe como un único sistema de archivos). 
1.3.3. Servicios 
En el ámbito de la administración de redes, los servicios son procesos fundamentales que posibilitan la 
comunicación entre dispositivos, el intercambio de recursos y el mantenimiento del sistema. Estos se 
dividen principalmente en: 
• servicios generales, orientados a facilitar tareas directas para los usuarios como el acceso a 
archivos compartidos o la impresión en red

---

Administración de Redes de Área Local 
28 
• servicios de infraestructura básica, indispensables para el funcionamiento dinámico de la red, 
como DHCP para la asignación automática de direcciones IP o DNS para la resolución de 
nombres de dominio.  
Mientras los primeros optimizan la experiencia del usuario final, los segundos constituyen la base 
técnica que sostiene toda la operatividad de la red. 
1.3.3.1. Servicios funcionales para el usuario 
Los servicios de red otorgan funcionalidades a la red. 
Algunos de los servicios más utilizados son: 
• Acceso remoto: 
• En modo terminal. 
• En modo gráfico. 
• Directorio activo. 
• Servidores de impresión. 
• Actualización centralizada de sistemas. 
• Monitorización centralizada de sistemas. 
Acceso remoto 
Son los servicios que nos permiten conectarnos de forma remota a otros equipos. 
Podemos acceder de dos formas: 
• En modo terminal. 
Podemos abrir una terminal en un equipo remoto a través de servicios como Telnet 
(Telecommunication Network) o SSH (Secure Shell). 
SSH permite ejecutar comandos en nuestra consola de comandos que, por ejemplo, copie 
ficheros a otro equipo de la red. 
SSH es el más utilizado actualmente ya que garantiza la seguridad de las comunicaciones (lo que 
no ocurre con Telnet). 
• En modo gráfico. 
Permite conectarnos a otro equipo de la red de forma que podemos ver su pantalla e interactuar 
con ella como si fuera nuestro propio ordenador. Por otra parte, también podemos ver las 
acciones que realiza el usuario de dicho equipo.

---

Administración de Redes de Área Local 
29 
Para ello se suelen utilizar determinados servicios o aplicaciones. Las más utilizadas son: 
• VNC. 
VNC es un programa de software libre basado en una estructura cliente-servidor. 
Se puede utilizar en cualquier sistema operativo, incluso si el cliente y el servidor tienen 
distintos sistemas operativos. 
• Team Viewer. 
Es un software privado que ofrece licencia gratuita a los usuarios y de pago a las empresas. 
También se puede usar independientemente del sistema operativo de los equipos 
conectados. 
Su principal función es el control remoto, pero tiene otras funcionalidades de trabajo en 
equipo y presentación (reuniones en línea, videoconferencias, etc.). 
Directorio Activo 
Cuando existe un único servidor y pocos usuarios podemos implementar un inicio de sesión en base a un 
nombre de usuario y contraseña. 
De esta forma, puede acceder a un equipo donde se haya configurado este usuario y acceder a sus 
ficheros y servicios. 
Sin embargo, si tenemos muchos servidores y estaciones cliente, este sistema es inviable, ya que las 
modificaciones tendrían que hacerse en todos los equipos cliente. 
Para ello es mejor usar los servicios de directorio activo (dominio). Un dominio consiste en una 
agrupación de máquinas y usuarios. 
Cuando un usuario se conecta a la red, debe seleccionar el dominio al que quiere entrar e introducir su 
usuario y contraseña. 
Al ser autenticado en un dominio, el usuario tiene disponibles todos los recursos dados de alta en dicho 
dominio sin tener que autenticarse en cada uno de los servidores que formen parte de dicho dominio. 
La gestión de un dominio se realiza de forma centralizada, ya que toda la información se encuentra en 
una base de datos almacenada en el Controlador de Dominio (OC). 
Por ejemplo, si queremos modificar una contraseña lo hacemos en el OC y no en cada equipo. 
Ya has estudiado "Active Directory" en la unidad 1 Administración del Sistema Operativo y Software de 
base.

---

Administración de Redes de Área Local 
30 
 
 
 
+ Info 
Active Directory es una implementación de servicio de directorio 
en una red distribuida de computadores. 
Utiliza distintos protocolos, principalmente LDAP, DNS, DHCP y 
Kerberos. 
Es un servicio establecido en uno o varios servidores en donde se 
crean objetos tales como usuarios, equipos o grupos, con el 
objetivo de administrar los inicios de sesión en los equipos 
conectados a la red, así como la administración de políticas. 
https://docs.microsoft.com/es-es/windows-server/identity/ad-
ds/active-directory-domain-services 
 
Servidores de impresión 
Permiten compartir impresoras y monitorizar su estado, cola de impresión, administrar trabajos, etc. 
En la actualidad la mayoría de las impresoras lo tienen integrado y se administra desde un navegador web. 
Actualización centralizada de sistemas 
Es muy importante mantener actualizados los programas y sistemas operativos de los equipos de la 
empresa, especialmente los parches de seguridad (muy común en sistemas Windows). 
El servicio Windows Server Update Services (WSUS) permite a los administradores de red especificar las 
actualizaciones de Microsoft que se deben instalar en los diferentes equipos de la red. 
Monitorización centralizada de sistemas 
La monitorización de servidores consiste en la vigilancia de los servicios activos que un servidor nos 
ofrece. Con ello pretendemos controlar su nivel de disponibilidad y rendimiento para poder prevenir 
posibles fallos. Existen gran variedad de herramientas para monitorizar redes. Las veremos más 
adelante en esta unidad.

---

Administración de Redes de Área Local 
31 
1.3.3.2. Servicios de infraestructura básica 
Los servicios de infraestructura básica constituyen los cimientos operativos de cualquier red, 
encargándose de funciones esenciales que garantizan su correcto funcionamiento. A diferencia de los 
servicios orientados al usuario, operan de forma transparente automatizando procesos críticos como la 
asignación dinámica de direcciones IP (mediante DHCP) y la traducción de nombres a direcciones 
numéricas (a través de DNS). Estos mecanismos, fundamentales tanto en redes corporativas como 
domésticas, permiten establecer conectividad básica y acceder a recursos de red sin necesidad de 
configuración manual, optimizando así la gestión y escalabilidad de la infraestructura. 
1.3.3.2.1. DHCP 
El protocolo DHCP (Dynamic Host Configuration Protocol) es un servicio esencial en redes modernas 
que automatiza la configuración de dispositivos. Opera en la capa de aplicación del modelo TCP/IP y 
está definido en el RFC 2131. Su principal función es asignar automáticamente direcciones IP y otros 
parámetros de red a los dispositivos que se conectan, eliminando la necesidad de configuración manual 
y reduciendo errores humanos. 
El proceso de asignación sigue un esquema conocido como DORA, formado por cuatro pasos clave. 
Primero, el cliente envía un paquete DHCPDISCOVER por broadcast para localizar servidores 
disponibles. Luego, el servidor responde con un DHCPOFFER que contiene una dirección IP propuesta. 
En tercer lugar, el cliente confirma la aceptación con un DHCPREQUEST. Finalmente, el servidor 
completa la transacción con un DHCPACK, confirmando la asignación, o un DHCPNAK si la dirección ya 
no está disponible. 
Entre los parámetros que DHCP puede configurar se incluyen no solo la dirección IP y máscara de 
subred, sino también la puerta de enlace predeterminada, servidores DNS, nombre de dominio y otros 
valores opcionales. Esta capacidad lo hace especialmente útil en redes de todo tamaño, desde pequeños 
routers domésticos hasta grandes infraestructuras corporativas. El protocolo incluye mecanismos como 
el tiempo de concesión (lease time) que permite reutilizar direcciones IP cuando los dispositivos se 
desconectan, optimizando así el espacio de direcciones disponible. 
En entornos profesionales, los administradores pueden crear múltiples ámbitos (scopes) para diferentes 
segmentos de red, establecer reservas para dispositivos específicos que siempre necesiten la misma IP, 
e incluso implementar agentes de retransmisión (relay agents) para servir a múltiples subredes desde 
un único servidor DHCP. Estas características avanzadas permiten una gestión escalable y eficiente de 
redes complejas. 
Ejemplo práctico: Configuración de un servidor DHCP en Windows Server 
Este servicio automatiza la asignación de direcciones IP a los dispositivos conectados a la red. Gracias a 
DHCP, los administradores pueden evitar conflictos de direcciones IP y gestionar dinámicamente la 
configuración de red, asegurando que cada dispositivo obtenga una dirección IP válida y única dentro 
de la red.

---

Administración de Redes de Área Local 
32 
Para instalar este servicio se deben seguir estos pasos: 
• Abrir el Administrador del servidor: al iniciar sesión en el servidor, el Administrador del servidor 
se abre automáticamente. Si no se abre, se puede acceder a él manualmente desde el Menú de 
inicio. 
• Agregar Roles y Características. 
Dentro del Administrador del servidor, dirigirse a la esquina superior derecha y hacer clic en 
Administrar. A continuación, seleccionar Agregar roles y características. 
• Iniciar el Asistente de Roles y Características. 
Se abrirá un asistente. En la primera pantalla, simplemente hacer clic en Siguiente para 
continuar. 
• Seleccionar el Servidor Local. 
A continuación, seleccionar el Servidor local desde la lista disponible y hacer clic en Siguiente. 
• Seleccionar Tipo de Instalación. En la sección de tipo de instalación, elegir la opción Instalación 
basada en roles o características. 
• Seleccionar el Rol de Servidor DHCP 
En la lista de roles, marcar la casilla correspondiente a Servidor DHCP. Asegurarse de tener una 
IP estática antes de instalar DHCP. Luego, hacer clic en Siguiente.

---

Administración de Redes de Área Local 
33 
• Agregar Características Necesarias. 
Aparecerá una ventana emergente preguntando si se desea agregar las características 
necesarias. Hacer clic en Agregar características para proceder. 
• Continuar con la Instalación. 
Hacer clic en Siguiente hasta llegar a la pantalla final, donde podrás presionar el botón Instalar 
para comenzar la instalación. 
• Finalizar la Instalación. 
Esperar a que la instalación se complete. Una vez finalizada, hacer clic en Cerrar para salir del 
asistente. 
Si bien el servidor DHCP ya está instalado, es necesario realizar una configuración inicial. 
Se deben seguir estos pasos a continuación: 
 
• Notificación de Configuración Posterior a la Instalación. 
En el Administrador del servidor, aparecerá un aviso amarillo en la parte superior que indica que 
se requiere una configuración posterior a la instalación. Hacer clic en este aviso y seleccionar 
Completar configuración de DHCP. 
• Confirmación de Datos. 
Se abrirá un asistente de configuración. Verificar el nombre del servidor y las credenciales de 
administrador. Después de confirmarlos, hacer clic en Confirmar y luego en Cerrar. 
Con estos pasos, el servicio DHCP estará instalado y registrado correctamente en el sistema, listo para 
su configuración. El siguiente paso deberá ser la creación de un ámbito DHCP. Un conjunto de 
direcciones IP que el servidor podrá asignar automáticamente a los dispositivos de red.

---

Administración de Redes de Área Local 
34 
Para ello se deben de seguir estos pasos: 
• Abrir la Consola DHCP. 
En el Administrador del servidor, ve al menú Herramientas y selecciona DHCP. Esto abrirá la 
consola DHCP. 
• Desplegar el Servidor y IPv4. 
En la consola DHCP, despliega el nombre de tu servidor y luego IPv4. 
• Crear un Nuevo Ámbito. 
Hacer clic derecho sobre IPv4 y seleccionar Nuevo ámbito…. Se abrirá un asistente para crear el 
nuevo ámbito. 
• Configurar el Ámbito. 
En las pantallas del asistente, completar los siguientes datos: 
• Nombre del ámbito: Asignar un nombre al ámbito, por ejemplo, "Red local". 
• Rango de direcciones IP: Define el rango de direcciones IP que el servidor asignará, por 
ejemplo, de 192.168.1.100 a 192.168.1.200. 
• Máscara de subred: Si la máscara es 255.255.255.0, la longitud será 24. 
• Exclusiones: Si se desean reservar algunas IPs para dispositivos específicos (como 
impresoras o servidores), se puede agregar estas exclusiones. 
• Duración de la concesión: se puede dejar el valor por defecto (8 días). 
• Configurar las Opciones del DHCP. 
El asistente preguntará si se desean configurar las opciones del DHCP. Hacer clic en Sí para 
continuar. 
Especificar Opciones de Red. 
En la siguiente pantalla, ingresar la siguiente información: 
Puerta de enlace: La dirección IP del router, por ejemplo, 192.168.1.254. 
Servidor DNS: Se puede usar un servidor DNS público como 8.8.8.8 o configurar el del propio 
servidor si ya tienes un servicio DNS. 
Servidor WINS (Windows Internet Name Service): Si no se usa WINS, dejar este campo en 
blanco. 
• Activar el Ámbito. 
Al finalizar, asegurarse de activar el ámbito de inmediato. Esto permitirá que el servidor DHCP 
comience a asignar direcciones IP a los dispositivos de la red.

---

Administración de Redes de Área Local 
35 
1.3.3.2.2. DNS 
El servicio DNS (Domain Name System) traduce los nombres de dominio (como "administracion.gob.es") en 
direcciones IP, permitiendo que los dispositivos localicen y se comuniquen con otros equipos o servicios 
en la red. Esto simplifica la configuración y el acceso a los recursos de red, ya que los usuarios solo 
necesitan recordar el nombre del dominio en lugar de las direcciones IP. 
Ejemplo práctico: Configuración de un servidor DNS en Windows Server 
Para instalar y configurar un servidor DNS hay que seguir estos pasos relatados a continuación, en una 
típica instalación en Windows Server, desde el Administrador de Servidor. 
• Abrir el Administrador del Servidor. 
• Iniciar sesión en el servidor con una cuenta de administrador. 
• Si el Administrador de Servidor no se abre automáticamente se puede acceder 
manualmente desde el Inicio> herramientas administrativas > Administrador del Servidor. 
• Iniciar el asistente "Agregar roles y características", en el Administrador del Servidor, haga clic 
en Administrar > Agregar roles y características. 
• Pantalla de bienvenida del asistente, hacer clic en Siguiente para continuar. 
• Seleccionar tipo de instalación, elegir instalación basada en roles o características, pulsar sobre 
Siguiente. 
• Seleccionar el Servidor de Destino. Seleccionar el servidor local de la lista disponible y hace clic 
en Siguiente. 
• Seleccionar el Rol de Servidor DNS. En la lista de roles, marcar la casilla correspondiente a 
Servidor DNS. Aparecerá una ventana emergente para agregar características necesarias. Hacer 
clic en Agregar Características y luego en Siguiente.

---

Administración de Redes de Área Local 
36 
• Confirmar características adicionales, no es necesario marcar Características adicionales para 
DNS. Hacer clic en Siguiente. 
• Confirmar e instalar. Revisar la información de resumen y hacer clic en Instalar. Esperar a que 
finalice la instalación (puede tardar varios minutos). 
• Finalizar la Instalación. Espera a que la instalación se complete. Una vez completada, hacer clic 
en Cerrar para salir del asistente. 
Una vez realizada la instalación propiamente dicha se habrá de completar una configuración, narrada a 
continuación: 
• Notificación de Configuración Posterior a la Instalación. En el Administrador del servidor, verás 
un aviso amarillo en la parte superior que indica que se requiere una configuración posterior a la 
instalación. Haz clic en este aviso y selecciona Completar configuración de DNS. 
• Confirmación de Datos. Se abrirá un asistente de configuración. Verifica el nombre del servidor 
y las credenciales de administrador. Después de confirmarlos, haz clic en Confirmar y luego en 
Cerrar. 
Con estos pasos, el servicio DNS estará instalado y registrado correctamente en el sistema, listo para su 
configuración. 
 
El siguiente paso es crear una zona DNS. Una zona es una sección del espacio de nombres DNS que se 
maneja de manera independiente. Para crear una nueva zona, se deben seguir los pasos relatados a 
continuación: 
• Abrir el Administrador del Servidor. Iniciar sesión en el servidor con una cuenta de 
administrador. Si el Administrador de Servidor no se abre automáticamente se puede acceder 
manualmente desde el Inicio> herramientas administrativas > Administrador del Servidor.

---

Administración de Redes de Área Local 
37 
• Agregar Rol del Servidor DNS. Hacer clic en clic en Administrar > Agregar roles y características. 
En el asistente seleccionar: 
• Tipo de instalación: Instalación basada en roles o características. 
• Servidor de destino: Elegir el servidor local. 
• Roles: Marcar Servidor DNS y confirmar instalación. 
• Configurar una zona DNS primaria: 
• Abrir la consola DNS (Herramientas > DNS). 
• Hacer clic derecho en Zonas de búsqueda directa > Nueva zona. 
• Especificar: nombre de zona (midominio.es), tipo de zona (primaria), archivo de zona 
(aceptar el nombre predeterminado (midomino.com.dns). 
• Agregar los Registros DNS: 
Una vez creada la zona, puedes agregar registros DNS. Los más comunes son: 
• A (Address Record): Asocia un nombre de dominio con una dirección IP. 
• MX (Mail Exchange): Configura los servidores de correo para tu dominio. 
• CNAME (Canonical Name): Redirige un subdominio a otro nombre de dominio. 
• Verificar la Configuración. Asegurarse de verificar que la zona y los registros DNS estén 
correctamente configurados, realizando una prueba de resolución de nombres desde otro 
dispositivo en la misma red.

---

Administración de Redes de Área Local 
38 
Si por ejemplo se agregara un registro A: 
• Clic derecho en zona > Nuevo registro A 
• Nombre: servidor1 
• Dirección IP: 192.168.1.10 
nslookup servidor1.midominio.com 
El comando debería devolver la dirección ip del registro, 192.168.1.10 
Con estos pasos, se habrá instalado y configurado correctamente un servidor DNS, y creado la primera 
zona DNS, asegurando que las solicitudes de nombres de dominio se resuelvan adecuadamente en la red. 
2. Gestión de usuarios en sistemas Windows 
Las cuentas de usuario son una parte muy importante de la seguridad de Windows ya que controlan el 
acceso a los equipos informáticos. 
Con ellas concedemos a los usuarios autorizaciones de acceso a distintos componentes y servicios. 
Hay dos formas de gestionarlas utilizando el administrador de usuarios (dependiendo de si estamos 
usando o no dominios): 
• Sin dominios. Se administra la seguridad de cada equipo informático (servidores, estaciones de 
trabajo, etc.). 
• Con dominios. Se administra la seguridad en los controladores de dominio. 
Las medidas de seguridad proporcionadas por el administrador de usuarios consisten en: 
• La creación de cuentas de usuarios y de grupo. 
• La asignación de derechos de usuario. 
• El establecimiento de relaciones de confianza entre dominios. 
Usuarios 
Una cuenta de usuario contiene un nombre único de usuario, una contraseña y los permisos que tiene el 
usuario sobre el uso de los recursos y servicios del sistema. 
A esto se le llama Seguridad de usuario y cada cuenta de usuario tienen asociado un identificador de 
seguridad de usuario (SID).

---

Administración de Redes de Área Local 
39 
Las cuentas de usuario pueden definirse en: 
• Una máquina local. 
Solo podrán utilizarse en esa máquina. 
• En un dominio. 
Podrán utilizarse en las máquinas que pertenezcan a ese dominio o a otro dominio que tenga 
una relación de confianza con este. 
Por norma general hay dos cuentas de usuario predefinidas: 
• Administrador. 
Tiene todos los permisos. 
La cuenta Administrador debería gestionarla el administrador de sistemas. 
• Invitado. 
Está pensada para un acceso ocasional al sistema por parte de alguien que no tiene cuenta de 
usuario. 
 
 
 
 
El experto opina 
Recomendamos no utilizar nunca este tipo de cuenta de usuario. 
En su lugar es mejor crear cuentas temporales con permisos que 
definamos nosotros. 
De esta forma podemos saber lo que hace cada usuario ocasional 
(tracking). 
 
El administrador de usuarios 
El administrador de usuarios es una herramienta que nos permite gestionar de manera sencilla los 
usuarios y grupos de usuarios en Windows Server. 
Si utilizas un Directorio Activo, para administrar los usuarios deberás utilizar la herramienta 
Administración de usuarios y equipos de directorio activo.

---

Administración de Redes de Área Local 
40 
Con esta herramienta podemos: 
• Crear usuarios nuevos. 
• Modificar las propiedades. 
• Agregar o quitar grupos de usuarios a los que pertenece. 
• Establecer el directorio particular del usuario (debería ser una carpeta de red). 
• Cambiar la contraseña. 
• Borrar o editar un usuario. 
Gestión de contraseñas 
 
Fuente: (https://pixabay.com/es/internet-de-seguridad-
contrase%C3%B1a-1952019/) 
La gestión de usuarios y contraseñas es la primera línea de defensa frente al acceso no autorizado. 
Debemos determinar una serie de condiciones de seguridad mínimas en cuanto a las características de 
las contraseñas, así como periodos de renovación de estas. 
Todas estas condiciones y medidas de seguridad deberían estar definidas en la política de seguridad de 
la organización. 
Las contraseñas deben ser robustas y secretas. Para ello: 
• Deben tener una longitud adecuada. (A mayor número de caracteres, mayor dificultad de 
obtenerla con algoritmos de fuerza bruta). 
• Longitud mínima de ocho caracteres.

---

Administración de Redes de Área Local 
41 
• No deben utilizarse palabras conocidas: 
• Palabras del diccionario. 
• Nombres propios. 
• Lugares. 
Las contraseñas con estas palabras son más fáciles de romper con ataques de diccionario. 
• Las contraseñas deben incluir variedad de caracteres: 
• Mayúsculas. 
• Minúsculas. 
• Números. 
• Signos de puntuación. 
• No se deben reutilizar claves. Cada servicio que usemos debe tener una clave diferente. 
Se deberían establecer políticas de seguridad que obliguen a los usuarios a cambiar la contraseña 
periódicamente, evitando la reutilización de estas. 
En Windows, esto se puede definir mediante las directivas de contraseña. 
3. Gestión de usuarios en sistemas Linux 
En Linux hay tres tipos de usuarios: 
• Root. 
Es el administrador del sistema. 
Se debe usar solo para las tareas específicas de administración y debería tenerla el administrador 
de red o de sistemas. 
• Usuarios. 
Son los usuarios que pueden iniciar sesión en el sistema. 
Tienen una funcionalidad limitada tanto en los comandos que pueden ejecutar como en los 
ficheros a los que tiene acceso.

---

Administración de Redes de Área Local 
42 
• Usuarios asociados a servicios. 
Estos usuarios no pueden iniciar sesión en el sistema. 
Se aplican a servicios. 
 
 
 
 
Ejemplo 
Por ejemplo, un servidor de páginas web puede tener asociado un 
usuario para poder especificar a qué ficheros tiene acceso. 
De esta forma, solo esos ficheros serán accesibles desde internet. 
 
 
Todos los usuarios del sistema tienen un identificador de usuario (UID) y un identificador de grupo 
(GID). 
El administrador del sistema (root) tiene los identificadores de usuario y grupo 0:0. 
La gestión de usuarios se puede hacer desde el intérprete de comandos. 
Vamos a ver los principales comandos: 
Comandos de usuarios 
COMANDO 
DESCRIPCIÓN 
adduser <usuario> 
Da de alta a un usuario. El sistema socilita datos como 
nombre completo, dirección, contraseña, etc. 
addgroup 
No es un comando estándar POSIX sino un script no 
disponible en todas las distribuciones Linux. Al ser un 
script permite hacer mayor cantidad de cosas por 
ejemplo especificar opciones como la descripción del 
grupo (especificar el nombre es obligatorio en ambos 
comandos), el GID y los usuarios que han de 
agregarse en el mismo comando.

---

Administración de Redes de Área Local 
43 
COMANDO 
DESCRIPCIÓN 
chage 
Permite esteblecer los períodos de vigencia de las 
contraseñas. 
id 
Muestra el usuario que se está usando 
passwd 
Si ejecuta "passwd" cambia la contraseña del usuario 
actual y si ejecuta "passwd nombre_usuario" cambia la 
contraseña del usuario indicado. 
su 
Cambio de usuario. 
sudo 
Ejecuta un comando como root 
userdel 
Borra un usuario 
usermod 
Modifica las propiedades de usuario 
Comandos de grupos 
COMANDO 
DESCRIPCIÓN 
groups 
Muestra los grupos a los que pertenece el usuario 
groupadd 
Comando POSIX que permite dar de alta un grupo. 
groupdel 
Borra un grupo de usuarios (el grupo, no a los 
usuarios) 
groupmod 
Modifica las propiedades de un grupo 
La información de las cuentas de usuario y grupos se encuentran en los siguientes ficheros: 
• /etc/passwd. 
Contiene el listado de las cuentas de usuario que están dados de alta en el sistema. 
• /etc/shadow. 
Contiene las contraseñas cifradas y sus periodos de vigencia. 
• /etc/group. 
Contiene el listado de grupos activos en el sistema y usuarios que pertenecen a cada grupo.

---

Administración de Redes de Área Local 
44 
Asistentes 
La administración de usuarios se puede realizar en modo gráfico con una herramienta o con webmin. 
Seguridad de las contraseñas 
Se deben aplicar las mismas políticas que hemos definido en Windows. 
4. Gestión de dispositivos 
En una red, tenemos diferentes tipos de dispositivos conectados, como ordenadores, impresoras, 
escáneres o actualmente impresoras multifunción. 
Todos estos dispositivos se puedes compartir a través de la red, para que diferentes usuarios accedan a 
ellos. 
Es necesario gestionar correctamente todos los dispositivos de hardware que pueden ser compartidos 
y/o usados en red. 
 
 
 
 
Atención 
Recuerda la importancia de los Sistemas RAID y los Tipos de 
Almacenamiento DAS, NAS y SAN, que estudiaste en el Bloque II 
Tecnología Básica, Unidad: 2. Periféricos: conectividad y 
administración. 
 
4.1. Administrador de discos en Windows 
La herramienta Administración de discos se utiliza para administrar el subsistema de discos. 
Esto incluye los discos duros y las unidades extraíbles. 
Se puede utilizar para administrar particiones o volúmenes, para asignar letras de unidad, formatear, etc.

---

Administración de Redes de Área Local 
45 
 
Administrador de discos 
Si pulsamos botón derecho sobre un disco duro y seleccionamos propiedades, accedemos a una ventana 
desde donde podremos realizar distintas tareas.

---

Administración de Redes de Área Local 
46 
 
Propiedades del disco. Pestaña "General" 
En esta pestaña podemos realizar dos tareas de mantenimiento: 
• Comprimir la unidad para ahorrar espacio de disco. 
Esto se consigue a costa de velocidad. 
• Liberar espacio. 
Abre el asistente para liberar espacio eliminando ficheros temporales o no utilizados. 
En la pestaña herramientas encontramos otras dos tareas de mantenimiento: 
• Desfragmentar y optimizar. 
Reorganiza la estructura de los ficheros almacenados en el disco para que el acceso sea más 
rápido. 
• Comprobación de errores. 
Comprueba si hay errores en el sistema de archivos.

---

Administración de Redes de Área Local 
47 
 
Desde esta ventana también podemos modificar: 
• Seguridad. Permite establecer permisos de usuarios sobre la unidad. 
• Cuota. Establecer límites de espacio a utilizar para los usuarios. 
• Compartir: Permite que otros usuarios puedan acceder a esta unidad. 
Existen muchas herramientas que podemos usar en lugar del administrador de discos de Windows. 
A continuación, mostramos algunas de ellas:

---

Administración de Redes de Área Local 
48 
EaseUS Partition Master 
 
EaseUS Partition Master 
EaseUS es uno de los mejores programas de partición. 
Algunas de sus funciones son: 
• Crear, formatear, cambiar el tamaño, mover, dividir, combinar, copiar, limpiar, comprobar y 
explorar particiones. 
• Recuperar particiones pérdidas o eliminadas. 
• Convertir de FAT a NTFS, primaria a lógica y viceversa. 
• Interfaz gráfica de usuario para ser extremadamente intuitivo.

---

Administración de Redes de Área Local 
49 
Características PRO (de pago): 
 
Diferencias entre la versión Free y Pro 
MiniTool Partition Wizard 
 
MiniTool Partition Wizard

---

Administración de Redes de Área Local 
50 
Este programa de pago también está disponible de forma gratuita. 
Permite, entre otras cosas: 
• Crear partición. 
• Cambiar el tamaño. 
• Mover. 
• Eliminar. 
• Formatear. 
• Ocultar. 
• Mostrar. 
• Dividir. 
• Fusionar. 
• Copiar. 
• Clonar. 
• Recuperar particiones eliminadas. 
• Permite reconstruir la tabla MBR. 
• Convertir el sistema de archivos de FAT a NTFS y viceversa. 
• Soporta unidades RAID, unidades USB externas y discos FireWire. 
• Proteger los datos en las particiones en caso de fallo. 
4.2. Administrador de discos en Linux 
Existen muchas herramientas para gestionar las particiones de disco en Linux. Vamos a mostrar las más 
importantes: 
LÍNEA DE COMANDOS: 
• Fdisk. 
Es una potente herramienta con la que podrás gestionar tus particiones. 
No es fácil de manejar por lo que tendrás que acudir a la ayuda en más de una ocasión. 
• Parted. 
Su principal diferencia con la anterior es que todas las acciones de los comandos enviados se 
aplicarán de forma inmediata (lo cual es peligroso).

---

Administración de Redes de Área Local 
51 
 
 
 
+ Info 
Ten mucho cuidado si haces pruebas con estos comandos porque 
es una práctica de alto riesgo. 
 
 
GUI (INTERFAZ GRÁFICA DE USUARIO): 
• GParted. 
Posee una interfaz gráfica sencilla e intuitiva. 
Permite realizar la mayoría de las funciones básicas sobre particiones: 
• Reparar. 
• Crear una partición. 
• Formatear. 
• Redimensionar. 
• Etc. 
 
Fuente (https://es.m.wikipedia.org/wiki/Archivo:Gparted_es.png)

---

Administración de Redes de Área Local 
52 
• Integradas en entornos de escritorio. 
Tanto GNOME como KDE traen instaladas por defecto una herramienta de administración de 
discos (GNOME Disks y KDE Partition Manager). Son muy parecidas a GParted y ambas son 
buenas opciones. 
 
 
 
 
El experto opina 
Nuestro consejo es que utilices GParted y que evites utilizar 
Parted. 
 
4.3. Gestión de impresoras/escaneres 
Los servicios de impresión permiten compartir impresoras, escáneres o sistemas multifunción en una 
red y centralizar las tareas administrativas que se realizan en los servidores de impresión. 
Existen dos formas que permiten compartir una impresora para que puedan utilizarla en red: 
• Compartir una impresora. 
Es la forma más fácil y para ello hay que hacer uso del servicio Compartir archivos e impresoras. 
• Servidor de impresión. 
Permite supervisar las colas de impresión y recibir notificaciones cuando las colas de impresión 
dejan de procesar trabajos de impresión. 
También permiten migrar servidores de impresión e implementar conexiones de impresora 
mediante la directiva de grupo. 
Compartir impresora 
Para compartir una impresora tenemos que abrir el Panel de control, Pulsar en "Hardware y sonido" y a 
continuación en "Dispositivos e impresoras". 
Se abrirá la siguiente página.

---

Administración de Redes de Área Local 
53 
 
Dispositivos e impresoras 
Para compartir la impresora pulsamos el botón derecho y pulsamos "propiedades de impresora". Se 
abrirá una ventana con varias pestañas y seleccionamos la pestaña "Compartir". 
 
Ventana propiedades de impresora 
Aquí marcamos la casilla "Compartir esta impresora" y le damos un nombre (el que verán los clientes).

---

Administración de Redes de Área Local 
54 
Servidor de impresión 
Se puede configurar un equipo como servidor de impresión. 
Este compartirá una impresora conectada al equipo. 
Esto es algo que hoy en día no se utiliza porque muchas impresoras traen incorporado su propio 
servidor de impresión, los cuales son muy fáciles de configurar. 
Estos servidores tienen habilitados los servicios necesarios para utilizarla desde la mayoría de los 
sistemas operativos. 
La administración se hace a través de un navegador web. 
Para ello debe acceder a la dirección IP de la impresora o a su dirección MAC. 
 
 
 
 
+ Info 
Si tenemos activado un servidor DHCP, se le asignará una IP de 
forma automática, aunque es aconsejable asignarle una IP fija. 
 
 
Administrador de impresora a través de un navegador 
De esta forma, se puede acceder desde cualquier sistema operativo que soporte un navegador.

---

Administración de Redes de Área Local 
55 
5. Monitorización y control de tráfico de red 
Network Monitoring, o monitorización de red, consiste en el uso de un sistema que recopila datos 
sistemáticamente y los analiza, buscando componentes defectuosos o lentos para facilitar que en todo 
momento la infraestructura funcione sin problemas. 
Posteriormente informará a los administradores de redes (o de sistemas en su defecto) mediante 
distintos medios como correos electrónicos, avisos al móvil, alarmas, etc. Esto hace que la 
observabilidad del sistema facilite la mejor com-prensión de la arquitectura del sistema, viendo qué es 
más lento, que fallos hay, y así poder mejorar el rendimiento. 
 
 
 
 
Observabilidad 
El ingeniero sénior de Big Commerce, Shaun McCormick, explicó la 
idea de la observabilidad, como que no se trata de saber si el 
problema está ocurriendo, sino por qué está ocurriendo en primer 
lugar, y, después cómo alguien puede resolverlo. 
 
 
La monitorización y control de tráfico de red es una función de la administración de redes, por tanto, 
del administrador de red, si existe ese perfil, para lo que se utilizan herramientas de monitorización. 
Las principales características a tener en cuenta para seleccionar dichas herramientas son: 
• Comunicación de las alertas. 
• Integraciones con servidores externos. 
• Usabilidad y presentación de los datos en el panel. 
• Flexibilidad a la hora de adaptarse a herramientas o software particulares. 
• API de acceso desde sistemas externos. 
• Detección de dispositivos de forma automática. 
• Integraciones con Bases de Datos. 
• Multidispositivo. 
• Escalado.

---

Administración de Redes de Área Local 
56 
• Soporte del mayor número de protocolos de adquisición de datos posible. 
• Seguridad. 
• Integración con máquinas virtuales. 
• Integraciones hardware. 
• Control remoto. 
• Inventario de Hardware y Software. 
• Geolocalización. 
• Monitorización de la nube. 
5.1. Balanceo de carga 
El balance o balanceo de carga, en inglés load balance, es un concepto usado en informática para 
referirse a la técnica usada para compartir el trabajo a realizar entre varios procesos, ordenadores, 
discos y otros recursos compartidos en red. 
También se conoce como Load Balancing. 
El balanceo de carga se basa en un algoritmo que divide el trabajo a realizar de la forma más eficiente 
posible para evitar los llamados "Cuellos de botella", que son momentos en los que las peticiones de 
servicios exceden la capacidad del servidor para cumplirlas. 
Actualmente donde este problema se da de forma más repetida y donde se han volcado los esfuerzos 
de los desarrolladores, es en los servidores web, por tanto, vamos a tratar el balanceo de carga en el 
contexto de red. 
En un entorno de Red, el balanceo de carga, es la manera en que las peticiones de Internet son 
distribuidas sobre una fila de servidores. Es necesario que el tráfico de red entrante se distribuya a 
través de un grupo de servidores back-end, esta distribución es denominada también como Server 
Farm (conjunto de servidor o Server Pool (conjunto de servidores). 
Debemos tener en cuenta que actualmente los sitios web deben atender a un elevadísimo número de 
solicitudes concurrentes de usuarios o clientes, y proporcionar aquello que demandan (textos, 
imágenes, videos… y el uso cada vez mayor de comercio electrónico), y deben hacerlo de una forma 
rápida y confiable. Estos sitios web están alojados en servidores web que tienen una capacidad limitada, 
se origina un problema de escalabilidad debido al continuo crecimiento del número de usuarios activos 
en el sistema, por ello es imprescindible el uso de un balanceador de carga.

---

Administración de Redes de Área Local 
57 
Un balanceador de carga hace posible que el sitio web que administra esté siempre disponible, y sea 
capaz de servir todas las peticiones a la máxima velocidad posible, y lo hace de forma totalmente 
transparente para el usuario. 
Para ello: 
• Distribuye las solicitudes de los clientes o la carga de la red de manera eficiente en varios 
servidores. 
• Controla el tráfico entre sus servidores, enruta las solicitudes de los clientes en todos los 
servidores con el fin de satisfacer dichas solicitudes garantizando un rápido servicio al mismo 
tiempo que se logre que ningún servidor esté sobrecargado. 
• Si un servidor falla, el balanceador de carga redirige el tráfico al resto de los servidores. 
• Si se agrega un nuevo servidor al grupo de servidores, el balanceador de carga comienza a 
integrarlo y automáticamente a enviarle solicitudes. 
• Asegura alta disponibilidad y confiabilidad al enviar solicitudes solo a servidores que están en 
línea (que está conectado y funcionando). 
• Proporciona la flexibilidad de agregar o restar servidores según la demanda. 
 
 
 
 
Resumiendo 
Un balanceador de carga es una herramienta, que se encarga de 
direccionar a un cliente al servidor web que se encuentre con 
mayor disponibilidad (dentro del grupo de servidores que tienen el 
mismo contenido). 
 
Tipos de Balanceo de Carga 
Los balanceadores de carga generalmente vienen en dos formas: basados en hardware y basados en 
software: 
• Basados en hardware: 
Hay dos tipos principales. 
• Servidor dedicado: 
Consiste en un servidor dedicado con un sistema operativo en concreto, y un software para 
hacer el proceso de balanceador de carga. Este servidor integra los servidores web 
mediante las soluciones Plug and Play, lo que significa que tan pronto se conectan, 
funcionan con poco o nada de ajustes previos.

---

Administración de Redes de Área Local 
58 
• De tipo switch: 
Un balanceador de carga de este tipo necesita de un switch Layer 2 o Layer 3 para la 
integración del proceso de balanceo. No se necesita de ningún dispositivo intermediario 
entre el switch y el servidor web. 
• Basados en software: 
Para este caso no es necesario modificar ninguna característica de conectividad de red. 
Se puedes instalar el software para el propósito en los propios servidores web, o puedes optar 
por un servidor dedicado para cumplir el rol de balanceador de carga. 
En general los proveedores de soluciones Hardware utilizan software propietario y procesadores 
especializados, si aumenta el tráfico en la red, es necesario adquirir más dispositivos. 
Las soluciones Software suelen utilizar un hardware de libre elección o la propia nube, siendo, por tanto, 
más flexible. 
En Linux destaca Linux Virtual Server (LVS)que es el más conocido, y también otros, como el Red Hat 
Piranha, que ha sido sustituido por Keepalived. 
Y en la plataforma para Windows Server se tiene al ISA Server (Microsoft Internet Security and 
Acceleration Server). 
Existen softwares para el balance de carga, como "Wingate" en donde se pueden añadir dos redes. 
 
 
 
 
+ Info 
Puedes consultar la página del fabricante dlink (de routers y swich) 
para ampliar información. 
https://eu.dlink.com/es/es/support/faq/routers/wireless-
routers/dsr-series/uk_dsr_how_to_setup_load_balancing 
_with_multiple_wan_links_fw_2_x 
 
5.1.1. Algoritmos del balanceador de carga 
El balance de carga se mantiene gracias a un algoritmo que divide de la manera más equitativa posible el 
trabajo, para evitar los así denominados cuellos de botella, evitar que un servidor se sature. 
El equilibrio de carga se produce desde las capas 4 (capa de transporte) a 7 (capa de aplicación) del 
modelo OSI.

---

Administración de Redes de Área Local 
59 
La elección del algoritmo dependerá de las necesidades, ya que cada tipo ofrece diferentes beneficios 
para distribuir el tráfico de red en función de la distribución del tráfico, si se trata de tráfico de capa de 
red o tráfico de capa de aplicación. 
• El tráfico en la capa de red se enruta según las direcciones IP de destino. 
• El tráfico de la capa de aplicación se enruta teniendo en cuenta otros factores, como el 
encabezado HTTP, SSL. 
Algoritmos de capa de Red 
• Round Robin: las solicitudes se distribuyen equitativamente entre el grupo de servidores 
existentes. 
Este sistema no tiene en cuenta las condiciones de los servidores ni el tipo de solicitud. Esto 
puede ocasionar que un PC Pentium de bajas prestaciones este sirviendo un video en streaming, 
mientras que otro servidor mucho más potente, este suministrando un fichero PDF. Tampoco 
reconoce de forma rápida los problemas en los servidores, por lo que puede estar realizando 
peticiones a un servidor ya caído. 
Este algoritmo puede resultar eficaz cuando los servidores son idénticos y no hay conexiones 
persistentes. 
Hay dos tipos principales a destacar: 
• Round-robin con peso. 
Si los servidores no tienen la misma capacidad, este algoritmo se puede utilizar para 
distribuir la carga. Se pueden asignar algunos pesos o parámetros de eficiencia a todos los 
servidores de un grupo y, en base a eso, de manera cíclica similar, se distribuye la carga. 
• Round-robin dinámico. 
Los pesos que se asignan a un servidor para identificar su capacidad también se pueden 
calcular en tiempo de ejecución. El round robin dinámico ayuda a enviar las solicitudes a un 
servidor según el peso del tiempo de ejecución. 
• Least Connections (Conexiones mínimas). 
Dependiendo de las conexiones de los clientes en un determinado momento se envía una nueva 
solicitud al servidor, sin tener en cuenta la capacidad de cada uno de los servidores (que no 
tienen por qué ser iguales). Se dirige el tráfico entrante al servidor con la menor cantidad de 
conexiones. 
Utiliza un criterio de evaluación implícito (número de conexiones activas) que puede no ser del 
todo preciso en algunos escenarios. 
Es útil cuando se requiere una conexión persistente.

---

Administración de Redes de Área Local 
60 
• Weighted least-connection (Conexiones mínimas con peso). 
Tiene en cuenta el número de conexiones activas de cada servidor y aplica un peso predefinido 
basado en su capacidad (CPU, RAM, ancho de banda). Los servidores con mayor peso reciben 
más tráfico, incluso si ya tienen conexiones activas, lo que permite una distribución equilibrada 
según su capacidad real. Esto es ideal para entornos con servidores de hardware heterogéneo. 
• Least-response-time (menor tiempo de respuesta). 
Selecciona el servidor con el menor tiempo de respuesta en tiempo real, considerando latencia 
de red y carga actual. No utiliza pesos estáticos, sino métricas dinámicas para optimizar la 
entrega de solicitudes. Es ideal para aplicaciones sensibles a la latencia, como APIs o servicios en 
tiempo real, ya que adapta la distribución de carga constantemente según el rendimiento actual 
de cada servidor. 
• Algoritmo de Hashing (IP Hash). 
Se utiliza la dirección IP del cliente para determinar que servidor va a recibir la solicitud del 
mismo y prestarle el servicio solicitado. 
Hay dos tipos: 
• Hash de fuente/destino: Se combinan las direcciones IP de origen y destino para 
seleccionar que servidor atenderá la solicitud. Si se produce una interrupción en la 
conexión, la misma solicitud se puede redirigir al mismo servidor para recuperarla. 
• Hash de URL: Se utiliza la URL de solicitud para realizar un hash, y ayudar a reducir la 
duplicación de cachés del servidor, ya que se está evitando almacenar el mismo objeto de 
solicitud en muchas cachés. 
• Otros algoritmos: 
• Menor ancho de banda: se selecciona el servidor que haya tenido menor consumo de ancho 
de banda en los últimos 14 minutos. 
• Menor cantidad de paquetes: se elige el servidor que está transmitiendo la menor cantidad 
de paquetes para redirigir el tráfico. 
• Carga personalizada: se selecciona el servidor en función de la carga que tiene en ese 
determinado momento, que se determina por memoria, uso de la CPU, tiempo de 
respuesta, número de solicitudes, etc. 
Algoritmos de capa de Aplicación 
En esta capa, los LB disponen de mucha más información para decidir, ya que se puede rastrear la 
respuesta del servidor, y esto ayuda a determinar la carga del servidor de manera mucho más efectiva. 
Uno de los algoritmos más utilizados en el algoritmo Least Outstanding Re-quests (LOR, menos 
solicitudes pendientes) , que dirige el tráfico de solicitudes HTTP pendientes al servidor más disponible, 
por lo que resulta muy útil para ajustar un pico repentino en las solicitudes detectado al monitorear la 
carga del servidor.

---

Administración de Redes de Área Local 
61 
5.1.2. Generaciones de sistemas de balanceo de carga 
Se puede diferenciar entre dos generaciones de sistemas de balanceo de carga: 
• Primera Generación: 
Podía detectar el rendimiento de un servidor mediante el "passive polling". Con este sistema se 
puede medir el tiempo de respuesta de un servidor y por tanto tener una idea de su 
rendimiento, pero tampoco guardaba los distintos tipos servidor para optimizar peticiones, y 
solo es capaz de detectar los problemas a posteriori, es decir cuando ya ha bajado el 
rendimiento del servidor o este está caído. 
• Segunda Generación: 
Esta generación realiza un enrutamiento "PROACTIVO", es decir, conoce y considera el uso real 
de los servidores (incluso antes de que lleguen las peticiones de los clientes), lo que permite una 
optimización de recursos. 
Esto lo logra realizando continuas peticiones de servicios en los distintos servidores a su cargo, 
lo que le permite monitorizar sus condiciones. 
Normalmente los parámetros utilizados son: Utilización de CPU, uso de memoria (RAM) y 
número de conexiones abiertas. Esto nos permite direccionar las peticiones de los clientes hacia 
el servidor que se encuentre más disponible y en mejor estado para responder a dichas 
peticiones. 
Otra característica interesante de la segunda generación, son sus funciones de "mensajería". No 
solo nos informará de los servidores caídos, también puede comunicarnos cuando está previsto 
que vuelvan a estar operativos. Normalmente, estos servidores reactivados pasan por un 
periodo de prueba, donde reciben un número de solicitudes restringido para probar su 
funcionamiento. 
También tienen la capacidad de ir derivando las solicitudes de servidores a los que hay que 
realizar mantenimiento o sustitución, de forma que su ausencia no afecte de golpe al 
rendimiento del servicio. 
5.1.3. Persistencia de la sesión 
Este concepto, en inglés sessión persitence, se refiere a no cambiar el servidor que está prestando 
respuesta a las peticiones realizadas por un usuario durante un tiempo determinado, normalmente 
hasta que finalice un proceso o cierre la sesión o sitio web donde está enviando solicitudes. 
En muchas ocasiones, la información sobre el usuario se almacena de forma local en el navegador que 
esté utilizando, como es el caso de una web con carro de compra, donde los artículos en el carro del 
usuario pueden almacenarse en el navegador hasta que el usuario decida comprarlos o cierre la sesión 
(se desconecte).

---

Administración de Redes de Área Local 
62 
Cambiar el servidor que recibe las solicitudes en medio de la sesión de compra podría originar 
problemas de la transacción o de rendimiento, por tanto, es necesario que todas las solicitudes del 
cliente se envíen al mismo servidor durante la sesión. Por ello recibe el nombre de persistencia de 
sesión. 
5.1.4. Configuración dinámica de grupos de servidores 
En caso necesario, el balanceador de carga puede agregar o eliminar dinámicamente servidores del 
grupo sin que se interrumpan las conexiones existentes. 
Existen aplicaciones que cambian rápidamente, y por ello requieren que se agreguen o eliminen 
constantemente servidores, como es por ejemplo en el entorno de Amazon Elastic Compute Cloud 
(EC2), donde los usuarios pagan únicamente por la capacidad de cómputo que realmente usan, 
mientras que al mismo tiempo asegura que la capacidad se amplíe en picos de tráfico. 
 
 
 
 
+ Info 
Amazon Elastic Compute Cloud (Amazon EC2) es una parte 
central de la plataforma de cómputo en la nube de la empresa 
Amazon.com denominada Amazon Web Services (AWS). 
EC2 permite a los usuarios alquilar computadores virtuales en los 
cuales pueden ejecutar sus propias aplicaciones. Este tipo de 
servicio supone un cambio en el modelo informático al 
proporcionar capacidad informática con tamaño modificable en la 
nube, pagando por la capacidad utilizada. En lugar de comprar o 
alquilar un determinado procesador para utilizarlo varios meses o 
años, en EC2 se alquila la capacidad por horas. 
 
5.1.5. Formas de Balanceo de Carga 
Existen dos formas para el balanceo de carga que se usan principalmente en los dispositivos físicos (tipo 
Rourter, switch, etc…) 
• Por destino. 
• Por paquete.

---

Administración de Redes de Área Local 
63 
5.1.5.1. Por Destino 
El balanceo de carga por destino significa que el router distribuye los paquetes según la dirección de 
destino. 
Dadas dos trayectorias a la misma red: 
• Todos los paquetes para el destino 1 en esa red pasan a través de la primera trayectoria. 
• Todos los paquetes para el destino 2 en esa red pasan a través de la segunda trayectoria. 
• Así sucesivamente. 
Esto preserva el orden de los paquetes, con el posible uso desigual de los links. Si un host recibe la 
mayor parte del tráfico, todos los paquetes utilizan un link, de forma que deja el ancho de banda en los 
otros links sin utilizar. 
Una mayor cantidad de direcciones de destino hace que los links se utilicen de una manera más 
equitativa, para que esto suceda, se utiliza un software específico para generar una entrada de memoria 
caché de ruta para cada dirección de destino, en lugar de cada red de destino, al igual que en el caso 
cuando existe solamente una trayectoria. Por lo tanto, los tráficos de diferentes hosts en la misma red 
de destino pueden utilizar diferentes trayectorias. 
Hay que destacar una desventaja de este sistema Por Destino, que es que para los routers de backbone 
principales que transportan tráfico de miles de hosts de destino, los requisitos de procesamiento y 
memoria para mantener la memoria caché se vuelven muy exigentes. 
5.1.5.2. Por paquete 
El balanceo de carga por paquete significa que: 
• El router envía un paquete para el destino 1 a través de la primera trayectoria. 
• El segundo paquete para el (mismo) destino 1 a través de la segunda trayectoria. 
• Así sucesivamente. 
El balanceo de carga por paquete garantiza una carga equitativa en todos los links. 
Sin embargo, hay una posibilidad de que los paquetes lleguen fuera de servicio al destino porque puede 
haber una demora diferencial dentro de la red, esto es porque en algunos routers, el balanceo de carga 
por paquete inhabilita la aceleración de reenvío por una memoria caché de ruta porque la información 
de memoria caché de ruta incluye la interfaz saliente. 
Para el balanceo de carga por paquete, el proceso de reenvío determina la interfaz saliente para cada 
paquete al buscar la tabla de ruteo y seleccionar la interfaz menos utilizada, así se garantiza una 
utilización equitativa de los links, pero es una tarea intensiva del procesador y afecta el rendimiento 
general del reenvío. 
El balanceo de carga por paquete no es adecuado para interfaces con velocidades más altas.

---

Administración de Redes de Área Local 
64 
5.1.6. Métodos 
Existen varios métodos para que un balanceador de carga haga la redirección del tráfico del cliente 
hacia el servidor adecuado. 
• NAT (Network Address Translation). 
• Balanceo de carga a nivel de enlace 
• Puerta de enlace TCP. 
5.1.6.1. NAT (Network Address Translation) 
El método NAT (Network Address Translation) es una técnica de balanceo de carga que opera en la 
capa de red (capa 3 del modelo OSI). Su principal objetivo es ocultar las direcciones IP reales de los 
servidores backend a los clientes externos, protegiendo así la infraestructura interna. Este proceso, 
conocido comúnmente como "nateo", garantiza que los clientes solo interactúen con la IP pública del 
balanceador sin tener visibilidad directa de los servidores que procesan sus solicitudes. 
En la configuración inicial, los servidores backend disponen de direcciones IP privadas (por ejemplo, 
192.168.1.10 y 192.168.1.11), mientras que el balanceador posee una dirección IP pública (como 
203.0.113.1) que recibe todas las solicitudes entrantes de los clientes. Cuando un cliente envía una 
petición a la IP pública del balanceador, este selecciona automáticamente el servidor más adecuado 
según el algoritmo configurado, que puede ser round-robin, por menor carga u otros criterios. 
El proceso de traducción de direcciones se realiza de forma transparente. El balanceador modifica la 
dirección IP de destino en el paquete recibido, sustituyendo su propia IP pública por la IP privada del 
servidor seleccionado. Simultáneamente, crea una entrada en su tabla de traducción NAT para mantener 
el seguimiento de la conexión y poder gestionar correctamente la respuesta. El servidor backend recibe y 
procesa la solicitud, enviando su respuesta al balanceador, que se encarga de revertir la traducción 
reemplazando la IP origen privada por su IP pública antes de enviar la respuesta final al cliente. 
Entre las características clave de este método destacan su transparencia para los clientes, que nunca 
ven las IPs reales de los servidores, y el mantenimiento de una tabla de estado que permite gestionar 
correctamente todas las traducciones. Además, proporciona un nivel básico de seguridad al ocultar la 
infraestructura interna. Sin embargo, presenta algunas limitaciones importantes, como la posibilidad de 
convertirse en cuello de botella al procesar todo el tráfico en ambos sentidos, el consumo adicional de 
recursos para mantener la tabla de traducción NAT y la posible introducción de latencia adicional en las 
comunicaciones. Esta técnica resulta especialmente útil en entornos donde la ocultación de la 
infraestructura interna es un requisito de seguridad prioritario. 
5.1.6.2. Balanceo de carga a nivel de enlace (capa 2) 
El balanceo de carga a nivel 2 (capa de enlace de datos) se basa en modificar únicamente la dirección 
MAC de destino de las tramas, sin alterar las direcciones IP. Este enfoque, utilizado en soluciones como 
LVS-DR o DSR, permite distribuir el tráfico entre varios servidores backend con mínima carga para el 
balanceador, ya que evita el procesamiento de las cabeceras IP.

---

Administración de Redes de Área Local 
65 
Cada servidor backend configura la IP virtual del balanceador como una dirección de loopback (lo:0), lo 
que le permite aceptar tráfico dirigido a esa IP. El balanceador recibe la petición del cliente, elige un 
servidor según el algoritmo configurado y reescribe solo la MAC destino, enviando la trama 
directamente al backend seleccionado. 
El servidor responde directamente al cliente con su IP real, sin pasar por el balanceador. Si esto no es 
posible por restricciones de red, se puede recurrir al modo NAT, donde sí se reescriben las direcciones 
IP. Para que este modelo funcione, todos los servidores deben estar en la misma subred y deben 
desactivar ARP para la IP virtual. 
Entre sus ventajas destacan la eficiencia, al reducir la carga del balanceador, y la transparencia para el 
cliente. Para mantener la trazabilidad, se utilizan cabeceras HTTP como X-Forwarded-For. A diferencia 
del balanceo NAT, este método opera en capa 2 (MAC), manteniendo intactas las direcciones IP (capa 3). 
5.1.6.3. Puerta de enlace TCP 
En este método, se redirecciona el tráfico en la capa TCP y más arriba. 
El balanceador de carga y el cliente que realiza la solicitud de conexión, establecen una conexión TCP, el 
protocolo TCP actúa como un intermedio entre los potenciales servidores de destino, el balanceador de 
carga y el cliente. 
• El balanceador de carga recibe los datos de la solicitud ya antes de realizar la búsqueda del 
servidor más apropiado. 
• Después, el balanceador de carga establece una conexión TCP con el servidor ya designado para 
transmitir la solicitud del cliente. 
• Dicho balanceador de carga también pasa la respuesta del servidor al cliente mediante la 
conexión TCP. 
Así, vemos que el protocolo TCP actúa como un intermedio entre los potenciales servidores de destino, 
el balanceador de carga y el cliente. 
5.1.7. El balanceo de carga dentro del ecosistema de clústeres 
Un CLÚSTER es un conjunto, que se comporta como una única unidad. 
Un clúster de balanceo de carga o de cómputo adaptativo está compuesto por uno o más ordenadores 
(llamados nodos) que actúan como frontend (Interfaz de usuario) del clúster, y que se ocupan de 
repartir las peticiones de servicio que reciba el clúster, a otros ordenadores del clúster que forman el 
back-end (Servidor) de éste.

---

Administración de Redes de Área Local 
66 
El uso de los clústers, nació como consecuencia del desarrollo de varias tecnologías y nuevas 
necesidades. microprocesadores económicos de alto rendimiento y redes de alta velocidad, desarrollo 
de herramientas de software para cómputo distribuido de alto rendimiento y la creciente necesidad de 
potencia computacional para aplicaciones web. 
Un tipo concreto de clúster cuya función es repartir la carga de proceso entre los nodos en lugar de los 
servicios es el clúster openMosix, que es un sistema de clúster para Linux que permite a varias máquinas 
actuar como un único sistema multiprocesador, de esta forma no es necesario reprogramar nuestras 
aplicaciones para que aprovechen el clúster. Los procesos no saben en qué nodo del clúster se ejecutan, 
y es el propio openMosix el responsable de "engañarlos", y redirigir las llamadas al sistema al nodo del 
clúster en el que se lanzó el proceso. 
openMosix implementa un algoritmo balanceador que permite repartir de forma óptima la carga, si está 
el clúster bien calibrado. 
Resumen 
Las soluciones por medio de clústeres son: 
• Robustas y de igual desempeño a otras de gran envergadura. 
• Se usan para distribución, procesamiento o balanceo de procesos. 
• Son significativamente económicas respecto de la inversión requerida para su implementación. 
El conocimiento requerido para el desarrollo de un clúster es de igual valor frente al costo monetario 
para la adquisición de un mainframe. La opción de escoger de una de las dos soluciones radica en la 
necesidad y los recursos disponibles de la organización que la solicita. 
Los clústeres pueden ser aplicados en cualquier tipo de industria, dado su modo de trabajo grupal, 
distribuido, centralizado y balanceado, factores claves para el procesamiento adecuado y eficiente de la 
información. 
Los elementos típicos que forman un clúster son: 
• Un nodo activo, donde corren los servicios. 
• Un nodo pasivo que funciona como respaldo (Backup). 
• Servidores reales. 
• Software de administración. 
• Protocolos de comunicación y servicios. 
• Conexiones de red. 
• Ambientes de programación paralela. 
• Middleware.

---

Administración de Redes de Área Local 
67 
5.1.7.1. Clasificación general de clústeres 
Los clústers, en base a sus características, pueden clasificarse en 4: 
• Clústeres de alto rendimiento o High Performance Clúster (HPC): 
Son clústeres en los cuales se ejecutan tareas que requieren una gran capacidad computacional, 
cantidades enormes de memoria o ambas a la vez. 
Llevar a cabo estas tareas puede comprometer los recursos del clúster por largos periodos. 
• Clústeres de alta disponibilidad o High Availability (HA): 
Son clústeres cuyo objetivo es proveer disponibilidad y confiabilidad. Estos clústeres tratan de 
brindar la máxima disponibilidad de los servicios que ofrecen. La confiabilidad se provee 
mediante un software que detecta fallos y permite recuperarse frente a ellos, mientras que en 
hardware se evita tener un único punto de fallos. 
• Clústeres de alta eficiencia o High Throughput (HT): 
Son clústeres cuyo objetivo de diseño es ejecutar la mayor cantidad de tareas en el menor 
tiempo posible; existe independencia de datos entre las tareas individuales. El retardo entre los 
nodos del clúster no es considerado un gran problema. 
• Clústeres de balanceo de carga: 
Clúster que permite que un conjunto de servidores, compartan la carga de trabajo y de tráfico a 
sus clientes. Está compuesto por uno o más ordenadores (llamados nodos) que actúan como 
front-end del clúster y se ocupa de repartir las peticiones de servicio que reciba el clúster a otros 
ordenadores que forman su back-end. 
5.1.7.2. Funcionamiento 
Desde un punto de vista general, podemos dividir el funcionamiento de un clúster en dos partes: 
• El software: 
Se trata de un sistema operativo confeccionado especialmente para esta tarea (por ejemplo, un 
Kernel Linux modificado). 
También se necesitan compiladores y aplicaciones especiales que permiten que los programas 
que se ejecuten en el sistema utilicen todas las ventajas del clúster. 
En el entorno de GNU/Linux hay que destacar la PVM (Paralell Virtual Machine) y la MPI 
(Message Passing Interface), librerías que abstraen el componente hardware del componente 
software.

---

Administración de Redes de Área Local 
68 
• La interconexión: 
Hardware entre las máquinas (nodos) del clúster. 
Aunque se ha realizado un desarrollo de interfaces de interconexión especiales muy eficientes, 
es común realizar las interconexiones mediante una red Ethernet dedicada de alta velocidad, 
que permite que los nodos del clúster intercambian entre sí las tareas, actualizaciones de estado 
y los datos del programa. 
En un clúster abierto, existirá una interfaz de red que conecte al clúster con el mundo exterior 
(internet). 
Si hay que resolver un problema en paralelo, el software debe poder dividirlo en tareas más pequeñas, 
repartirlas entre los nodos y elaborar los resultados, por tanto, estas subtareas van a ejecutarse en 
paralelo consiguiendo un aumento de velocidad, aunque también se debe tener en cuenta el retardo en 
la división, el reparto y la transmisión de mensajes. 
En balanceo de carga, los clústeres deben funcionar con una actuación conjunta del hardware y el 
software, para que el tráfico se distribuya entre los nodos del clúster, y así ofrecer mayor velocidad. 
Los servidores de un clúster de alta disponibilidad no suelen compartir la carga de procesamiento que 
tiene un clúster de alto rendimiento ni tampoco la carga de tráfico, como lo hacen los clústeres de 
balanceo de carga, ya que su función es diferente, deben estar preparados para entrar inmediatamente 
en funcionamiento, en caso de que falle algún otro servidor. 
5.1.7.3. Ventajas y desventajas 
Las principales ventajas de los clústers de balanceo de carga son: 
• Disponibilidad. 
Capacidad para continuar operando ante la caída de alguno de los ordenadores del clúster. 
• Distribución en paralelo. 
• Flexibilidad. 
Los balanceadores de carga no están amarrados a ninguna arquitectura específica, en lo que 
respecta a hardware. 
• Costos. 
El diseño y montaje requiere de inversiones sumamente bajas comparadas con las alternativas 
de solución, las cuales son de un costo elevado. 
• Escalabilidad. 
Capacidad para hacer frente a volúmenes de trabajo cada vez mayores, prestando así un nivel 
de rendimiento óptimo.

---

Administración de Redes de Área Local 
69 
• Expansibilidad. 
Capacidad de aumentar sus capacidades a través de mejores técnicas. 
Transferencia de información y todo tipo de servicio por internet de forma rápida, a bajo costo 
e ininterrumpidamente. 
• Incremento: 
• Velocidad de respuesta: Mejora de los tiempos de respuesta al distribuir las solicitudes entre 
varios nodos, evitando la sobrecarga de un solo servidor. 
• Número de transacciones: Capacidad de manejar un mayor número de transacciones 
simultáneas gracias a la distribución equitativa de la carga entre los nodos. 
Las principales desventajas de los clústeres de balanceo de carga son: 
• Empresas y entidades prefieren seguir utilizando el modelo cliente/servidor tradicional debido al 
espacio físico o a nuevos problemas que no se daban en la arquitectura tradicional. 
• Espacio físico para el montaje de clústeres de balanceo de carga. 
5.1.8. Herramientas para "EC" en Windows 
Vamos a ver algunas de las mejores soluciones actuales para realizar balanceo de carga, o Equilibrador 
de Carga (EC) en Windows: 
5.1.8.1. Configuración del Balanceo de Carga en NICs 
El balanceo de carga permite dividir las cargas de red entre varias tarjetas de interfaz de red basadas en 
varios algoritmos. Cada una de las sesiones IP será tratada individualmente antes de decidir la ruta, lo 
que significa que una sola conexión IP no puede ser dividida durante el proceso. Sólo se pueden separar 
varias conexiones. 
A continuación, indicamos cómo configurar métricas de coste idénticas en las NICs Network Manager 
(NIC son las siglas de Network interface controller): 
• Hacer clic en el botón Panel de control del gadget. 
• Hacer clic en Herramientas y luego en Equilibrio de carga. 
• Hacer clic en la pestaña Windows. 
• Introduzca el valor de la métrica que desea utilizar; también puede dejar los valores 
predeterminados y, a continuación, hacer clic en Aplicar. 
• Espere a que el programa se actualice y ya está listo.

---

Administración de Redes de Área Local 
70 
Cada adaptador de red en Windows 7 y posteriores viene con dos valores métricos que el sistema 
operativo le asigna automáticamente, dependen del rendimiento de la conexión, de la métrica de la 
interfaz y también de la métrica predeterminada de la pasarela. 
El adaptador de red con la métrica de ruta más pequeña obtendrá todo el tráfico. 
Hay que tener en cuenta que, si se configuran manualmente varios adaptadores de red utilizando la 
misma métrica de ruta, las conexiones se realizarán a través de la que tenga menor carga de tráfico. 
5.1.8.2. Softwares 
Existen diversos softwares en el mercado, indicamos algunos de los más destacados. 
Software SafeKit 
Este software ofrece a los usuarios una de las soluciones más sencillas para la escalabilidad de 
aplicaciones críticas y la alta disponibilidad, y permite ahorrar el coste de las complicadas equilibradoras 
de carga. 
El clúster SafeKit farm puede implementar un clúster de balanceo de carga de red entre varios 
servidores. 
En una red, la misma aplicación se ejecuta en cada servidor, y la distribución de la actividad de la red 
equilibrará la carga. 
SafeKit no requiere ningún servidor específico por encima de la granja para implementar el clúster de 
balanceo de carga de la red. 
Características principales: 
• Ofrece un módulo de granja genérico sobre Windows y Linux para construir un clúster de 
balanceo de carga de red. 
• Permite escribir un módulo de granja propio para una aplicación a partir del módulo genérico de 
granja. 
También puede implementar un clúster de réplica que ofrezca replicación en tiempo real y 
conmutación por error. 
 
 
 
 
+ Info 
Puede obtener más información sobre el clúster de equilibrio de 
carga de la red en Windows y sobre cómo funciona el clúster de 
granja SafeKit, en la web oficial de Evidian.

---

Administración de Redes de Área Local 
71 
NGINX y NGINX Plus 
Permite escalar aplicaciones y distribuir la carga de trabajo uniformemente entre varios servidores. Si 
nos referimos a una aplicación web, las solicitudes HTTP se cargan de forma equilibrada en más 
servidores de aplicaciones. 
Ventajas principales: 
• Escalar y manejar más usuarios de los que sería posible con el uso de un solo servidor. 
• Si un servidor falla, habrá otros disponibles para asegurarse de que la aplicación permanezca en 
línea (redundancia). 
Otras características y beneficios del uso de NGINX/NGINX Plus: 
• Tanto NGINX de código abierto como NGINX Plus son capaces de equilibrar el tráfico HTTP, 
UDP y TCP. 
• NGINX Plus amplía el código abierto de NGINX con un equilibrio de carga de nivel empresarial 
que incluye comprobaciones de estado activas, persistencia de sesión, métricas adicionales y 
mucho más. 
Para la gestión de una red doméstica, es suficiente en utilizar el NGINX de código abierto. 
Con NGINX Plus, se puede aplicar automáticamente una amplia gama de mejoras a una transacción 
HTTP, y estas optimizaciones incluyen actualizaciones y transformaciones HTTP como el 
almacenamiento en caché de respuestas y la compresión de contenido. 
 
 
 
 
+ Info 
Puede obtener más información sobre el software NGINX, en el 
sitio web oficial. 
 
KEMPs Free LoadMaster 
Es un controlador de entrega de aplicaciones avanzado. KEMP ofrece este LoadMaster gratuito para 
ayudar también a las pequeñas empresas y a los desarrolladores, ofreciéndoles una atractiva opción de 
equilibrio de carga. 
Si las necesidades de equilibrio de carga crecen y se expanden, se puede actualizar a una versión 
comercial.

---

Administración de Redes de Área Local 
72 
Principales características: 
• Es un equilibrador de carga libre que es creado por una compañía bien establecida. 
• Permite que muchas empresas de nueva creación y equipos de control de calidad/desarrollo se 
centren en sus tareas sin tener que preocuparse por el compromiso entre la calidad, el coste y la 
capacidad de actualización que normalmente se asocian con otras soluciones de balanceo de 
carga de código abierto y aplicaciones que puede encontrar actualmente. 
 
 
 
 
+ Info 
En el sitio web oficial de KEMP, hay una comparación entre las 
características de Free LoadMaster y las de Commercial 
LoadMaster, para ver cuál es la más indicada según las necesidades. 
 
Snapt 
Es una de las mejores opciones de firewall de aplicaciones para DevOps, Cloud y también para 
despliegues virtualizados. 
Funciones que se incluyen en Snapt: 
• Acelerar su sitio web con el sólido acelerador web HTTP/S. 
• Puede descargar sus servidores y mejorar los tiempos de carga de las páginas. 
• Puede mantenerse en línea bajo presión utilizando el balanceador de carga y al mismo tiempo 
disfrutar de una alta visibilidad, informes, alertas y mucho más. 
• Puede utilizar Snapt GSLB para enrutar la inteligibilidad del tráfico en todo el mundo. 
• Con Snapt, estará protegido contra inyecciones de SQL, fugas y mucho más gracias a su función 
Snapt WAF. 
5.2. Herramientas de monitorización y control de trafico/red 
Existen herramientas de control propias de cada sistema operativo. 
Por ejemplo, en Linux el comando "IW" permite obtener una información variada sobre nuestra 
conexión inalámbrica (ejemplo: "iw dev <nombre dispositivo>, da la interfaz inalámbrica del 
dispositivo). Como la mayoría de los comandos de LINUX tiene la poción "help" para ver cómo trabaja 
más en profundidad.

---

Administración de Redes de Área Local 
73 
Un comando parecido, pero con menos información seria el "ipconfig" de Windows, que también 
dispone de un "help". 
Vamos a citar algunas de las herramientas externas para el control de la Red: 
• Nagios. 
• Pandora FMS. 
• SolarWinds. 
• Zabbix. 
• GroudWork. 
• Zenoss. 
• Monitis. 
• OpenView. 
• Icinga. 
• OpManager. 
• Op5 Monitor. 
• Wireshark (Ethereal). (Se puede usar con Windows, Linux y OS x). 
Nagios 
 
Fuente: 
(https://www.flickr.com/photos/xmodul
o/11700273965) 
Es un software de monitorización de equipos y servicios de red, creado para ayudar a los 
administradores a tener siempre el control de qué está pasando en la red y conocer los problemas que 
ocurren en la infraestructura antes de que los usuarios los perciban.

---

Administración de Redes de Área Local 
74 
Es un sistema complejo y completo en cuanto a sus características que además hace uso en algunos 
casos de diversos sistemas como por ejemplo sistemas gestores de bases de datos, servidores web, etc. 
Está implementado en lenguaje PHP. 
Nagios está licenciado bajo la GNU General Public License Version 2. 
Pandora FMS 
 
Fuente: 
(https://commons.wikimedia.org/wiki/File:L
ogo_Pandor_FMS_community_edition.png) 
Pandora FMS es un software de monitorización para gestión de infraestructura TI. 
Esto incluye: 
• Equipamiento de red. 
• Servidores Windows. 
• Servidores Unix. 
• Infraestructura virtualizada. 
• Aplicaciones. 
Pandora FMS tiene multitud de funcionalidades, lo cual lo convierte en un software de nueva 
generación que cubre todos los aspectos de monitorización necesarios. 
Es un software de código abierto. 
Solarwinds 
 
Fuente: (https://commons.wikimedia.org/wiki/File:Solarwinds.svg) 
Se desmarca del resto por su mapeo automático de redes y nodos sin necesidad de acciones manuales.

---

Administración de Redes de Área Local 
75 
Tiene un interfaz gráfico bastante potente en el que se puede ver fácilmente la topología de red y el 
estado de la misma. 
Nos permite integrar máquinas virtuales en su monitorización. 
Zabbix 
 
Fuente: (https://ca.m.wikipedia.org/wiki/Fitxer:Zabbix_logo.png) 
Nos ofrece una herramienta de fácil configuración y potente interfaz gráfico y se pueden monitorizar 
hasta 10,000 nodos sin problemas de rendimiento y sin necesidad de instalar agentes. 
GroundWork 
 
Reutiliza diferente software de Nagios, Icinga o Cacti para crear su solución global. 
Consigue entrar entre las mejores herramientas de monitorización de red gracias a su agrupación de 
otras herramientas. 
Zenoss 
 
Fuente: 
(https://commons.wikimedia.org/wiki/Fil
e:Zenoss-logo.png) 
Con Zenoss podremos monitorizar almacenamiento, redes, servidores, aplicaciones y servidores 
virtuales sin necesidad de instalar agentes. 
Dispone de una versión "Community" con funcionalidades muy reducidas y una versión comercial con 
todas las funcionalidades.

---

Administración de Redes de Área Local 
76 
Monitis 
Esta herramienta está enfocada a las PYMEs. 
Es de la empresa desarrolladora de Team Viewer lo que da garantías de ser un buen software. 
Sin embargo, es una herramienta de pago. 
OpenView 
HP OpenView es el nombre anterior de una familia de productos Hewlett-Packard que consistía en 
productos de administración de sistemas y redes. En 2007, HP OpenView fue renombrado como 
Software HP BTO cuando se convirtió en parte de la División de Software HP. 
Icinga 
 
Fuente: (https://en.m.wikipedia.org/wiki/File:Logo-icinga.png) 
Se integra con varias bases de datos. 
Destaca por su interfaz API REST. 
Está muy enfocada a redes complejas y monitorizaciones de protocolos, recursos de máquinas y 
servidores. 
Manage Engine/OPManager 
Está orientada específicamente a la gestión de redes. 
De forma predefinida, ofrece monitorización de redes de servidores físicos y virtuales, análisis de ancho 
de banda basado en flujo, análisis y almacenamiento de logs de firewall, gestión de cambios y 
configuraciones, y administración de direcciones IP y puertos de switch.

---

Administración de Redes de Área Local 
77 
Op5 Monitor 
Es capaz de monitorizar múltiples plataformas, sistemas en la nube y entornos virtuales. 
Esta herramienta de monitoreo está muy centrada en monitorización de hardware, tráfico de red y 
servicios y destaca su capacidad para grandes entornos. 
WiresShark 
 
Fuente: 
(https://commons.wi
kimedia.org/wiki/File
:Wireshark_icon.svg) 
Wireshark es un analizador de paquetes de código abierto y gratuito. 
Se utiliza para la resolución de problemas de red, análisis y desarrollo de protocolos de software y 
comunicaciones y también para fines educativos. 
Anteriormente se llamaba Ethereal. 
Wireshark es multiplataforma. 
5.3. Protocolos de gestión de red 
Vamos a ver 3 protocolos que se encargan de diferentes tareas en cuanto a la gestión de red, como son: 
administrar la red de información, el acceso ordenado y la consultas. 
5.3.1. CMIP 
CMIP: Common Management Information Protocol. 
El Protocolo de administración de red de información común (CMIP) define la comunicación entre 
las aplicaciones de administración de red y la gerencia de los agentes.

---

Administración de Redes de Área Local 
78 
CMIP se basa en el modelo OSI (Open Systems Interconnection) y es definido por la serie de 
recomendaciones ITU-T X.700. 
CMIP define la información de la gerencia en términos de objetos administrados y permite tanto la 
modificación como las acciones sobre objetos gestionados. Se describen usando GDMO y los objetos 
son identificados por un nombre distinguido (DN), similar en concepto al directorio X.500. 
Los NMS pueden realizar las operaciones siguientes: 
• CREATE: crear una instancia de un objeto gestionado. 
• DELETE: suprimir una instancia de un objeto gestionado. 
• GET: solicitar el valor de un atributo de una instancia de un objeto gestionado. 
• CANCEL_GET: cancelar una petición de GET en curso. 
• SET: fijar el valor de un atributo de una instancia de un objeto gestionado. 
• ACTION: solicitar una acción para ocurrir según lo definido por el objeto gestionado. 
El agente administrador puede realizar la siguiente operación: 
• EVENT_REPORT: enviar notificaciones o alarmar a los NMS. 
CMIP también proporciona buena seguridad (autorización de la ayuda, control de acceso y registros 
de la seguridad) y un reporte flexible de las condiciones inusuales de la red. 
5.3.2. LDAP 
LDAP siglas del inglés: Lightweight Directory Access Protocol. En castellano protocolo ligero de acceso 
a directorios. 
Hace referencia a un protocolo a nivel de aplicación que permite el acceso a un servicio de directorio 
ordenado y distribuido para buscar diversa información en un entorno de red. 
Un directorio es un conjunto de objetos con atributos organizados en una manera lógica y jerárquica.

---

Administración de Redes de Área Local 
79 
 
 
 
Ejemplo 
El ejemplo más común es el directorio telefónico, que consiste en 
una serie de nombres (personas u organizaciones) que están 
ordenados alfabéticamente, con cada nombre teniendo una 
dirección y un número de teléfono adjuntos. Es decir, es un libro o 
carpeta, en la cual se escriben nombres de personas, teléfonos y 
direcciones, y se ordena alfabéticamente. 
 
 
Un árbol de directorio LDAP a veces refleja varios límites políticos, geográficos u organizacionales, 
dependiendo del modelo elegido. Los despliegues actuales de LDAP tienden a usar nombres de Sistema 
de Nombres de Dominio (DNS por sus siglas en inglés) para estructurar los niveles más altos de la 
jerarquía. Conforme se desciende en el directorio pueden aparecer entradas que representan personas, 
unidades organizacionales, impresoras, documentos, grupos de personas o cualquier cosa que 
representa una entrada dada en el árbol (o múltiples entradas). 
Habitualmente, almacena la información de autenticación (usuario y contraseña) y es utilizado para 
autenticarse, aunque es posible almacenar otra información (datos de contacto del usuario, ubicación 
de diversos recursos de la red, permisos, certificados, etc). A manera de síntesis, LDAP es un protocolo 
de acceso unificado a un conjunto de información sobre una red. 
5.3.3. SNMP 
SNMP (Simple Network Management Protocol). 
SNMP es un protocolo de nivel de aplicación para realizar consultas a los diferentes elementos que 
forman una red. 
Estos elementos pueden ser: 
• Enrutadores. 
• Switches. 
• Hosts. 
• Modems. 
• Impresoras. 
• Etc.

---

Administración de Redes de Área Local 
80 
Cada equipo conectado a la red ejecuta unos procesos denominados agentes. 
Es un software residente en cada dispositivo, que permiten que se pueda realizar una administración 
tanto remota como local de la red. 
Dichos procesos van actualizando variables (manteniendo históricos) en una base de datos, que pueden 
ser consultadas remotamente. 
Por ejemplo, según el dispositivo, recogería los siguientes datos: 
• Enrutador: 
• Interfaces activos. 
• Velocidad de sus enlaces serie. 
• Número de errores. 
• Bytes emitidos. 
• Bytes recibidos. 
• Etc. 
• Impresora: 
• Falta de papel. 
• Atasco de papel. 
• Falta de tinta. 
• Modem: 
• Pérdida de conexión. 
5.3.3.1. Funcionamiento 
La forma normal de uso del SNMP es el sondeo (polling): 
1. Pregunta. 
La estación administradora envía una solicitud a un agente (proceso que atiende peticiones 
SNMP) pidiéndole información de estado o que realice una acción. 
2. Respuesta. 
El agente envía una respuesta a la estación administradora que puede ser la información de 
estado solicitada o la confirmación de la realización de la acción. 
El problema del sondeo es que, si hay muchos nodos administrativos, puede deteriorar el rendimiento 
de la red.

---

Administración de Redes de Área Local 
81 
Hay otra alternativa que produce menos carga. Es el método por interrupción (Trap), que es una 
comunicación asíncrona, en la que el agente pueda mandar la información al nodo administrador 
puntualmente, ante una situación predeterminada, por ejemplo, ante una anomalía detectada en la red. 
Una red administrada a través de SNMP consta de tres componentes clave: 
• Sistemas administradores de red (Network Management Systems, NMS). 
Un sistema administrador de red (NMS) ejecuta aplicaciones que supervisan y controlan a los 
dispositivos administrados. Los NMS's proporcionan el volumen de recursos de procesamiento y 
memoria requeridos para la administración de la red. Uno o más NMS's deben existir en 
cualquier red administrada. 
• Dispositivos administrados. 
Un dispositivo administrado es un dispositivo que contiene un agente SNMP y reside en una red 
administrada. Estos recogen y almacenan información de administración, la cual es puesta a 
disposición de los NMS's usando SNMP. 
Los dispositivos administrados, a veces llamados elementos de red, pueden ser routers, 
servidores de acceso, switches, bridges, hubs, computadores o impresoras. 
• Agentes. 
Un agente es un módulo de software de administración de red que reside en un dispositivo 
administrado. Un agente posee un conocimiento local de información de administración 
(memoria libre, número de paquetes IP recibidos, rutas, etcétera), la cual es traducida a un 
formato compatible con SNMP y organizada en jerarquías. 
Comandos básicos 
Los dispositivos administrados son supervisados y controlados usando cuatro comandos SNMP básicos: 
lectura, escritura, notificación y operaciones transversales. 
• GET: El comando de lectura es usado por un NMS para supervisar elementos de red. El NMS 
examina diferentes variables que son mantenidas por los dispositivos administrados. 
• SET: El comando de escritura es usado por un NMS para controlar elementos de red. El NMS 
cambia los valores de las variables almacenadas dentro de los dispositivos administrados. 
• TRAP: El comando de notificación es usado por los dispositivos administrados para reportar 
eventos en forma asíncrona a un NMS. Cuando cierto tipo de evento ocurre, un dispositivo 
administrado envía una notificación al NMS. 
• Las operaciones transversales son usadas por el NMS para determinar qué variables soporta un 
dispositivo administrado y para recoger secuencialmente información en tablas de variables, 
como, por ejemplo, una tabla de rutas. 
• GETNEXT: permite al NMS recuperar el siguiente objeto en la MIB, basado en el objeto 
actual. 
• GETBULK: permite al NMS solicitar bloques de datos en lugar de hacer múltiples solicitudes 
individuales, se usa para recoger múltiples entradas de la tabla de una sola vez.

---

Administración de Redes de Área Local 
82 
Base de información de administración SNMP (MIB) 
Una Base de Información de Administración (Management Information Base, MIB) es una colección de 
información que está organizada jerárquicamente. Las MIB's son accedidas usando un protocolo de 
administración de red, como, por ejemplo, SNMP. 
Un objeto administrado (algunas veces llamado objeto MIB, objeto, o MIB) es uno de cualquier número 
de características específicas de un dispositivo administrado. Los objetos administrados están 
compuestos de una o más instancias de objeto, que son esencialmente variables. 
Existen dos tipos de objetos administrados: 
• Tabulares. 
• Escalares. 
Los objetos escalares definen una simple instancia de objeto. Los objetos tabulares definen 
múltiples instancias de objeto relacionadas que están agrupadas conjuntamente en tablas MIB. 
Un ejemplo de un objeto administrado es atInput, que es un objeto escalar que contiene una simple 
instancia de objeto, el valor entero que indica el número total de paquetes AppleTalk de entrada sobre 
una interfaz de un router. 
Un identificador de objeto (object ID) identifica únicamente a un objeto administrado en la jerarquía 
MIB. La jerarquía MIB puede ser representada como un árbol con una raíz anónima y los niveles, que son 
asignados por diferentes organizaciones.

---

Administración de Redes de Área Local 
83 
El árbol MIB ilustra las variadas jerarquías asignadas por las diferentes organizaciones. 
Los identificadores de los objetos ubicados en la parte superior del árbol pertenecen a diferentes 
organizaciones estándares, mientras los identificadores de los objetos ubicados en la parte inferior del 
árbol son colocados por las organizaciones asociadas. 
Los fabricantes pueden definir ramas privadas que incluyen los objetos administrados para sus propios 
productos. Las MIB's que no han sido estandarizadas típicamente están localizadas en la rama 
experimental. 
El objeto administrado atInput podría ser identificado por el nombre de objeto iso.identified-
organization.dod.internet.private.enterprise.cisco.temporary.AppleTalk.atInput o por el descriptor de 
objeto equivalente 1.3.6.1.4.1.9.3.3.1. 
El corazón del árbol MIB se encuentra compuesto de varios grupos de objetos, los cuales en su conjunto 
son llamados mib-2. 
Los grupos son los siguientes: 
• System (1). 
• Interfaces (2). 
• AT (3). 
• IP (4). 
• ICMP (5). 
• TCP (6). 
• UDP (7). 
• EGP (8). 
• Transmission (10). 
• SNMP (11). 
Es importante destacar que la estructura de una MIB se describe mediante el estándar Notación 
Sintáctica Abstracta 1 (Abstract Syntax Notation One ó ASN.1). 
Detalles del Protocolo 
SNMP opera en la capa de aplicación del conjunto de protocolos de Internet (capa 7 del modelo OSI). 
El agente SNMP recibe solicitudes en el puerto UDP 161. 
El administrador puede enviar solicitudes de cualquier puerto de origen disponible para el puerto 161 en 
el agente.

---

Administración de Redes de Área Local 
84 
La respuesta del agente será enviada de vuelta al puerto de origen en el gestor. 
El administrador recibe notificaciones (Trampas e InformRequests) en el puerto 162. 
El agente puede generar notificaciones desde cualquier puerto disponible. Cuando se utiliza con 
Transport Layer Security las solicitudes se reciben en el puerto 10161 y trampas se envían al puerto 
10162. SNMPv1 especifica cinco unidades de datos de protocolo (PDU) centrales, (GetRequest, 
GetNextRequest, SetRequest, GetResponse y Trap) que se explican más adelante. 
Todas las PDU SNMP se construyen de la siguiente manera: 
• Cabecera IP. 
• Encabezado UDP versión comunidad. 
• Tipo de PDU. 
• Petición-ID. 
• Error de estado. 
• Índice de errores. 
• Enlaces de variables. 
Todos utilizan la siguiente estructura en el campo SNMP PDU: 
Tipo 
Identificador 
Estado de error 
Índice de error 
Enlazado de variables 
• Identificador: Es un número utilizado por el NMS y el agente para enviar solicitudes y respuesta 
diferentes en forma simultánea. 
• Estado e índice de error: Sólo se usan en los mensajes GetResponse (en las consultas siempre se 
utiliza cero). El campo "índice de error" sólo se usa cuando "estado de error" es distinto de 0 y 
posee el objetivo de proporcionar información adicional sobre la causa del problema. El campo 
"estado de error" puede tener los siguientes valores: 
• 0: No hay error. 
• 1: Demasiado grande. 
• 2: No existe esa variable. 
• 3: Valor incorrect. 
• 4: El valor es de solo lectura. 
• 5: Error genérico. 
• Enlazado de variables: Es una serie de nombres de variables con sus valores correspondientes 
(codificados en ASN.1).

---

Administración de Redes de Área Local 
85 
Mensajes SNMP 
Para realizar las operaciones básicas de administración anteriormente nombradas, el protocolo SNMP 
utiliza un servicio no orientado a la conexión (UDP) para enviar un pequeño grupo de mensajes (PDUs) 
entre los administradores y agentes. 
La utilización de un mecanismo de este tipo asegura que las tareas de administración de red no 
afectarán al rendimiento global de la misma, ya que se evita la utilización de mecanismos de control y 
recuperación como los de un servicio orientado a la conexión, por ejemplo, TCP. 
Los puertos comúnmente utilizados para SNMP son los siguientes: 
Número 
Descripción 
161 
SNMP 
162 
SNMP-trap 
Los paquetes utilizados para enviar consultas y respuestas SNMP poseen el siguiente formato: 
Versión 
Comunidad 
SNMP PDU 
• Versión: 
Número de versión de protocolo que se está utilizando (por ejemplo 0 para SNMPv1, 1 para 
SNMPv2c, 2 para SNMPv2p y SNMPv2u, 3 para SNMPv3, ...). 
• Comunidad: 
Nombre o palabra clave que se usa para la autenticación. Generalmente existe una comunidad 
de lectura llamada "public" y una comunidad de escritura llamada "private". 
• SNMP PDU: Contenido de la Unidad de Datos de Protocolo, el que depende de la operación que 
se ejecute. 
Los mensajes son: 
• GetRequest: 
A través de este mensaje el NMS solicita al agente retornar el valor de un objeto de interés 
mediante su nombre. En respuesta el agente envía una respuesta indicando el éxito o fracaso de 
la petición. Si la petición fue correcta, el mensaje resultante también contendrá el valor del 
objeto solicitado. Este mensaje puede ser usado para recoger un valor de un objeto, o varios 
valores de varios objetos, a través del uso de listas.

---

Administración de Redes de Área Local 
86 
• GetNextRequest: 
Este mensaje es usado para recorrer una tabla de objetos. Una vez que se ha usado un mensaje 
GetRequest para recoger el valor de un objeto, puede ser utilizado el mensaje GetNextRequest 
para repetir la operación con el siguiente objeto de la tabla. Siempre el resultado de la operación 
anterior será utilizado para la nueva consulta. De esta forma un NMS puede recorrer una tabla 
de longitud variable hasta que haya extraído toda la información para cada fila existente. 
• SetRequest: 
Este tipo de mensaje es utilizado por el NMS para solicitar a un agente modificar valores de 
objetos. Para realizar esta operación el NMS envía al agente una lista de nombres de objetos con 
sus correspondientes valores. 
• GetResponse: 
Este mensaje es usado por el agente para responder un mensaje GetRequest, GetNextRequest, 
o SetRequest. En el campo "Identificador de Request" lleva el mismo identificador que el 
"request" al que está respondiendo. 
• Trap: 
Una trap es generado por el agente para reportar ciertas condiciones y cambios de estado a un 
proceso de administración. El formato de la PDU es diferente: 
Tipo 
Enterprise 
Dirección del 
agente 
Tipo genérico 
de trap 
Tipo específico 
de trap 
Timestamp 
Enlazado de 
variables 
• Enterprise: Identificación del subsistema de gestión que ha emitido el trap. 
• Dirección del agente: Dirección IP del agente que ha emitido el trap. 
• Tipo genérico de trap: 
» Cold start (0): Indica que el agente ha sido inicializado o reinicializado. 
» Warm start (1): Indica que la configuración del agente ha cambiado. 
» Link down (2): Indica que una interfaz de comunicación se encuentra fuera de servicio 
(inactiva). 
» Link up (3): Indica que una interfaz de comunicación se encuentra en servicio (activa). 
» Authentication failure (4): Indica que el agente ha recibido un requerimiento de un 
NMS no autorizado (normalmente controlado por una comunidad). 
» EGP neighbor loss (5): Indica que en sistemas en que los routers están utilizando el 
protocolo EGP, un equipo colindante se encuentra fuera de servicio. 
» Enterprise (6): En esta categoría se encuentran todos los nuevos traps incluidos por los 
vendedores.

---

Administración de Redes de Área Local 
87 
• Tipo específico de trap: Es usado para traps privados (de fabricantes), así como para 
precisar la información de un determinado trap genérico. 
• Timestamp: Indica el tiempo que ha transcurrido entre la reinicialización del agente y la 
generación del trap. 
• Enlazado de variables: Se utiliza para proporcionar información adicional sobre la causa del 
mensaje. 
Otros dos PDU, GetBulkRequest e InformRequest se añadieron en SNMPv2 y prorrogados a SNMPv3. 
• GetBulkRequest: Este mensaje es usado por un NMS que utiliza el protocolo SNMP (V.2 donde 
aparece y v.3) típicamente cuando es requerida una larga transmisión de datos, tal como la 
recuperación de largas tablas. En este sentido es similar al mensaje GetNextRequest usado en la 
versión 1 del protocolo, sin embargo, GetBulkRequest es un mensaje que implica un método 
mucho más rápido y eficiente, ya que a través de un solo mensaje es posible solicitar la totalidad 
de la tabla. 
• InformRequest: Un NMS que utiliza la versión 2 o 3 del protocolo SNMP transmite un mensaje 
de este tipo a otro NMS con las mismas características, para notificar información sobre objetos 
administrados, utilizando el protocolo de nivel 4(OSI) TCP, y enviara el InformRequest hasta 
que tenga un acuse de recibo. 
5.3.3.2. Desarrollo y uso 
Existen diferentes versiones de este protocolo. Debemos tener en cuenta, que como todo lo referente a 
la informática, la tecnología de red sigue avanzando y modificándose continuamente. 
Vamos a ir viendo diferentes versiones y lo más destacado de cada una de ellas. 
5.3.3.2.1. Versión 1 
SNMP versión 1 (SNMPv1) fue la primera implementación del protocolo SNMP, publicada inicialmente 
en 1988. Funcionaba sobre múltiples protocolos de red como UDP, IP, CLNS, AppleTalk DDP y Novell 
IPX. A pesar de su sencillez, se convirtió rápidamente en el protocolo de gestión de red de facto en la 
comunidad de Internet. Las especificaciones originales se publicaron en tres RFCs, que fueron 
reemplazados por versiones revisadas en 1990. Más adelante, en 1991, se introdujo la MIB-II como 
evolución natural de la MIB-I. 
• RFC 1065 (1988): estructura e identificación de la información de gestión para redes basadas 
en TCP/IP. Se sustituye en 1990 por el RFC 1155. 
• RFC 1066 (1988): primera base de información de gestión (MIB-I) para la gestión de redes 
TCP/IP. Se sustituye en 1990 por el RFC 1156. 
• RFC 1067 (1988): define el protocolo simple de administración de red (SNMPv1). Se sustituye 
en 1990 por el RFC 1157.

---

Administración de Redes de Área Local 
88 
• RFC 1155 (1990): revisión de la estructura e identificación de la información de gestión. 
Sustituye al RFC 1065. 
• RFC 1156 (1990): revisión de la base de información de gestión (MIB-I). Sustituye al RFC 1066. 
Se sustituye en 1991 por el RFC 1213. 
• RFC 1157 (1990): revisión formal del protocolo SNMPv1. Sustituye al RFC 1067. 
• RFC 1213 (1991): introduce la MIB-II, ampliando y mejorando la MIB-I. Sustituye al RFC 1156 y 
se convierte en la base habitual de gestión de redes TCP/IP. 
La Versión 1 ha sido criticada por su falta de seguridad. 
El sistema de autenticación que utilizaba era una sistema basado únicamente en cadenas de comunidad 
transmitidas en texto claro, sin cifrado ni mecanismos de integridad o control de acceso. 
El diseño de SNMPv1 en los años 80 fue obra de un grupo de colaboradores que consideraron que las 
soluciones de gestión de red patrocinadas oficialmente en ese momento, como HEMS/CMIS/CMIP -
respaldadas por OSI, IETF y la NSF (National Science Foundation)- eran inaplicables en las plataformas 
informáticas disponibles y potencialmente inviables para una implementación práctica. Ante esta 
situación, SNMP fue aprobado como un protocolo provisional, con la idea de que ofrecía una solución 
práctica y suficiente para dar soporte a la expansión masiva de Internet y su posterior comercialización. 
Su sencillez y facilidad de implementación lo convirtieron rápidamente en el protocolo de gestión de 
red dominante, a pesar de sus limitaciones, como la falta de mecanismos de seguridad robustos. 
En los años 80, los estándares de seguridad y autenticación en Internet aún eran una aspiración lejana. 
Los grupos de diseño de protocolos priorizaban la simplicidad y el despliegue rápido, por lo que se 
desalentaba la incorporación de mecanismos de seguridad avanzados. 
5.3.3.2.2. Versión 2 
SNMPv2, definido en los RFC 1441 al 1452, fue una revisión de SNMPv1 que introdujo mejoras 
importantes en áreas como el rendimiento de las comunicaciones, la seguridad, la confidencialidad y la 
relación entre el gestor y los agentes. Una de sus principales novedades fue la operación 
GetBulkRequest, que permite recuperar grandes cantidades de datos de gestión con una sola solicitud, 
en lugar de realizar múltiples GetNextRequest consecutivos. Sin embargo, el nuevo sistema de 
seguridad basado en el concepto de "partidos" fue considerado excesivamente complejo por muchos 
implementadores, lo que limitó su adopción. Aunque esta versión alcanzó el nivel de madurez de 
estándar (Draft Standard), fue declarada obsoleta por versiones posteriores. 
En respuesta a la complejidad del modelo de seguridad original, se definió SNMPv2c (Community-based 
SNMPv2) en los RFC 1901 al 1908. Esta versión conserva las mejoras funcionales de SNMPv2, pero 
reemplaza su modelo de seguridad por el sistema basado en comunidades de SNMPv1, mucho más 
simple. Gracias a esta simplificación, SNMPv2c se convirtió en el estándar de facto de SNMPv2, aunque 
también quedó obsoleto más adelante con la llegada de SNMPv3.

---

Administración de Redes de Área Local 
89 
Otra variante fue SNMPv2u (User-based SNMPv2), especificada en los RFC 1909 y 1910, que intentó 
ofrecer un compromiso entre la simplicidad de SNMPv2c y la seguridad avanzada del modelo original de 
SNMPv2. Esta versión ofrecía mayores garantías de seguridad sin la complejidad total del modelo 
basado en partidos, y una de sus variantes, SNMPv2*, llegó a implementarse comercialmente. El 
mecanismo de seguridad de SNMPv2u fue finalmente adoptado como uno de los dos marcos de 
seguridad en SNMPv3, la versión más completa y segura del protocolo. 
SNMPv1 y SNMPv2c interoperabilidad 
Tal como está actualmente especificada, SNMPv2c es incompatible con SNMPv1 en dos áreas clave:  
• los formatos de mensajes. 
• las operaciones del protocolo. 
Por un lado, los mensajes SNMPv2c utilizan una cabecera y una estructura de unidad de datos de 
protocolo (PDU) distintas a las de SNMPv1, lo que impide la interoperabilidad directa. Por otro lado, 
SNMPv2c introduce dos operaciones de protocolo que no están definidas en SNMPv1. 
Para permitir la coexistencia de ambas versiones en una misma red, el RFC 2576 establece dos posibles 
estrategias: el uso de agentes proxy, que actúan como intermediarios entre dispositivos SNMPv1 y 
sistemas de gestión SNMPv2c, y los sistemas de gestión de red bilingües, capaces de comunicarse con 
agentes SNMPv1 y SNMPv2c seleccionando automáticamente el protocolo adecuado. 
Agentes de proxy 
Un agente proxy SNMPv2 permite que un sistema de gestión de red (NMS) que utiliza SNMP versión 2 
pueda comunicarse con dispositivos que solo soportan SNMPv1. Su función es traducir o reenviar los 
mensajes según sea necesario. 
• El NMS SNMPv2 emite una solicitud (como un comando Get, GetNext, Set o GetBulk) dirigida a 
un dispositivo SNMPv1. 
• El mensaje no se envía directamente al dispositivo SNMPv1, sino al agente proxy SNMPv2. 
• El agente proxy SNMPv2 actúa como intermediario: 
• Para comandos Get, GetNext y Set, el proxy los reenvía sin modificar al agente SNMPv1. 
• Para comandos GetBulk (que no existen en SNMPv1), el proxy los convierte en múltiples 
solicitudes GetNext, ya que SNMPv1 solo permite acceder a un valor cada vez. 
• Para traps o notificaciones, el proxy convierte los mensajes de captura (trap) del agente 
SNMPv1 en mensajes compatibles con SNMPv2 y los envía al NMS.

---

Administración de Redes de Área Local 
90 
Sistema de gestión de la red bilingüe 
Un sistema de gestión de red SNMPv2 bilingüe es capaz de comunicarse tanto con agentes SNMPv1 
como con agentes SNMPv2. 
Para facilitar este entorno de gestión dual, la aplicación del NMS bilingüe debe contactar con los 
agentes gestionados. 
El NMS consulta una base de datos local que indica qué versión de SNMP admite cada agente. 
En función de esta información, el NMS utiliza la versión apropiada del protocolo SNMP para 
comunicarse con el agente. 
5.3.3.2.3. Versión 3 
Aunque SNMPv3 no realiza cambios en el protocolo, aparte de la adición de seguridad criptográfica, 
da la impresión de ser muy diferente debido a las nuevas convenciones textuales, los conceptos y la 
terminología. 
SNMPv3 añadió principalmente mejoras en seguridad y configuración remota de SNMP. 
Debido a la falta de seguridad en las versiones anteriores del protocolo, los administradores de red 
recurrían a otros medios, como SSH, para tareas de configuración, contabilidad y gestión de fallos. 
SNMPv3 aborda aspectos críticos para el despliegue a gran escala, como la contabilidad y la gestión de 
fallos. En la actualidad, SNMP se emplea principalmente para el control y la gestión del rendimiento de 
los sistemas. 
SNMPv3 define una versión segura del protocolo y facilita la configuración remota de entidades SNMP. 
Proporciona un entorno protegido para la gestión de sistemas, incluyendo los siguientes aspectos: 
• Identificación de las entidades SNMP para permitir la comunicación solo entre entidades 
conocidas. Cada entidad SNMP tiene un identificador llamado snmpEngineID, y la comunicación 
solo es posible si ambas partes conocen sus identidades. Las trampas y notificaciones son la 
excepción a esta norma. 
• Soporte para modelos de seguridad: un modelo de seguridad define políticas dentro de un 
dominio administrativo o una intranet. SNMPv3 incluye las especificaciones para el USM (User-
based Security Model). 
SNMPv3 también define objetivos de seguridad, en los que los servicios de autenticación de mensajes 
están diseñados para proteger contra: 
• Modificación de la información: evita que una entidad altere los mensajes SNMP durante su 
tránsito. 
• Suplantación (Masquerade): impide que un gestor no autorizado realice operaciones simulando 
la identidad de un usuario con permisos válidos.

---

Administración de Redes de Área Local 
91 
• Modificación del flujo de mensajes: protege contra reordenamientos, retrasos o repeticiones 
maliciosas de mensajes legítimos. 
• Divulgación: evita la interceptación no autorizada de los mensajes entre motores SNMP. 
Especificación para USM (User-based Security Model): 
• Comunicación sin autenticación ni privacidad (noAuthNoPriv). 
• Comunicación con autenticación y sin privacidad (authNoPriv). 
• Comunicación con autenticación y privacidad (authPriv). 
USM permite el uso de diferentes protocolos de seguridad, incluyendo: 
• Autenticación: MD5 y SHA 
• Privacidad (cifrado): CBC_DES y CFB_AES_128 
También se definen procedimientos esenciales como: 
• Descubrimiento del snmpEngineID de una entidad para una dirección de transporte específica. 
• Sincronización horaria, necesaria para la comunicación autenticada. 
• Marco MIB SNMP, que permite la configuración remota y la gestión de entidades SNMP. 
• MIB USM, para administrar remotamente el módulo de seguridad. 
• MIB VACM, para configurar remotamente el módulo de control de acceso. 
SNMPv3 se centra en dos áreas principales: seguridad y administración. 
• En cuanto a seguridad, proporciona autenticación sólida y cifrado para garantizar la privacidad. 
• En cuanto a administración, destaca la gestión de originadores de notificaciones y agentes 
proxy. 
SNMPv3 incorpora varias capacidades de seguridad. Las especificaciones iniciales definieron los 
modelos USM y VACM, a los que se añadió posteriormente el TSM (Transport Security Model) para 
ofrecer soporte mediante SSH, TLS y DTLS. 
• USM (Modelo de Seguridad basado en Usuarios): proporciona autenticación y privacidad 
(cifrado) a nivel de mensaje. 
• VACM (Modelo de Control de Acceso basado en Vista): determina si un gestor puede acceder a 
un objeto MIB y realizar operaciones específicas. Opera a nivel de PDU. 
• TSM (Modelo de Seguridad de Transporte): permite la autenticación y cifrado a través de 
canales externos seguros como SSH, TLS y DTLS. 
La seguridad ha sido la mayor debilidad de SNMP desde su creación.

---

Administración de Redes de Área Local 
92 
Las versiones 1 y 2 solo ofrecían autenticación mediante una cadena de comunidad en texto claro, lo 
que representaba un riesgo elevado. 
En SNMPv3, cada mensaje incluye parámetros de seguridad codificados como una cadena de octetos. 
El significado de estos parámetros varía según el modelo de seguridad utilizado. SNMPv3 proporciona 
funciones de seguridad clave: 
• Confidencialidad: mediante el cifrado de paquetes, evita la interceptación por parte de 
entidades no autorizadas. 
• Integridad: asegura que los mensajes no han sido alterados durante el tránsito, e incluye 
protección opcional contra repeticiones. 
• Autenticación: verifica que el mensaje procede de una fuente válida. 
Desde 2004, el IETF reconoce SNMPv3 como la versión estándar actual del protocolo, tal como se 
define en los RFC 3411 al RFC 3418 (STD0062). 
El IETF ha designado SNMPv3 como estándar completo de Internet, el máximo nivel de madurez que 
puede alcanzar un RFC. Las versiones anteriores han sido declaradas obsoletas y designadas como 
"Históricas" o "Obsoletas". 
En la práctica, muchas implementaciones SNMP son mixtas, y soportan múltiples versiones 
simultáneamente: típicamente SNMPv1, SNMPv2c y SNMPv3. 
5.3.3.3. Dificultades de implementación 
Las implementaciones del protocolo SNMP pueden variar entre diferentes fabricantes. 
En algunos casos, SNMP es incorporado como característica adicional del sistema y no se considera 
seriamente como un elemento fundamental del diseño del mismo. 
Algunos de los principales fabricantes tienden a ampliar en exceso su interfaz de línea de comandos 
(siglas CLI en inglés) propietaria para configurar y controlar sus sistemas. 
En febrero de 2002 el Centro de Coordinación del Equipo de Respuesta de Emergencia de 
Computadores (CERT-CC) del Instituto de Ingeniería del Software Carnegie Mellon (CM-SEI) realizó un 
proceso consultivo sobre SNMPv1, el CA-2002-03, después, el Grupo de Programación Segura de la 
Universidad de Oulu dirigió un análisis sobre la gestión de mensajes SNMP. 
La mayoría de las implementaciones de SNMP, independientemente de la versión del protocolo, 
reutilizan el mismo código de programación para la decodificación de las unidades de datos de 
protocolo (PDU). 
Por este motivo, muchos fabricantes se han visto obligados a publicar parches, debido a 
vulnerabilidades detectadas en el proceso de decodificación, tanto de los mensajes de trampa SNMP 
recibidos por la estación de gestión, como de las solicitudes procesadas por los agentes SNMP en los 
dispositivos de red.

---

Administración de Redes de Área Local 
93 
Las potentes capacidades de escritura de SNMP -que permiten la configuración directa de dispositivos 
de red- no han sido ampliamente utilizadas por muchos fabricantes. Esto se debe, en parte, a la falta de 
seguridad en las versiones de SNMP anteriores a la v3, y en parte a que muchos dispositivos 
simplemente no están diseñados para ser configurados mediante modificaciones en los objetos MIB. 
Además, los requisitos de la operación Set de SNMP son complejos de implementar correctamente, lo 
que ha llevado a muchos fabricantes a omitir su soporte, con el objetivo de reducir costes, simplificar el 
desarrollo y disminuir el tamaño del código. 
Por otro lado, aunque SNMP utiliza una estructura de datos en forma de árbol con indexado lineal que 
puede parecer simple, este modelo no siempre se adapta bien a las estructuras de datos internas de los 
sistemas. Como resultado, el procesamiento de ciertas consultas SNMP puede generar una carga 
excesiva en la CPU, especialmente en conjuntos de datos grandes, como las tablas de enrutamiento 
BGP o IGP. 
Además, algunos valores SNMP -especialmente los tabulares- requieren conocimientos específicos 
sobre esquemas de indexación, los cuales no son consistentes entre plataformas. Esto puede provocar 
problemas de correlación al recopilar información de múltiples dispositivos, como ocurre al recolectar 
métricas de utilización de disco cuando un mismo identificador representa diferentes discos según la 
plataforma. 
5.3.3.4. Implicaciones de Seguridad SNMP 
Debido a que SNMP está diseñado para permitir a los administradores la configuración y monitorización 
de dispositivos de red de forma remota, puede utilizarse también para penetrar en una Red de Área 
Local, es decir, "se puede utilizar SNMP para atacar una red". 
 
 
 
 
+ Info 
Un número significativo de herramientas de software podrían 
escanear la red completa a través de SNMP, por lo que errores de 
configuración del modo de lectura-escritura podrían hacer que una 
red fuese susceptible a los ataques. 
 
 
Si SNMP no se va a utilizar en una red, debe deshabilitarse, puesto que además de crear una 
vulnerabilidad, consumirá ancho de banda disponible y ciclos de CPU innecesariamente. 
En el año 2001, Cisco publicó información que incluso en el modo de sólo lectura la implementación de 
Cisco IOS 11.0 y 12.0 (el sistema operativo utilizado por los conmutadores y enrutadores de red) es 
vulnerable a ciertos ataques de denegación de servicio.

---

Administración de Redes de Área Local 
94 
Estos problemas de seguridad pueden arreglarse con una actualización de IOS.2. 
Cuando se configura el modo de sólo lectura se debe prestar atención a la configuración del control de 
accesos y desde qué direcciones IP se aceptan mensajes SNMP. 
Si los servidores SNMP son identificados por su dirección IP, SNMP solo tiene permitido responder a 
estas IPs y deberán denegarse mensajes SNMP de otras direcciones. Sin embargo, la suplantación de 
identidad de direcciones IP sigue siendo una preocupación. 
Autenticación SNMP 
SNMP está disponible en varias versiones, 1, 2 y 3; cada una tiene sus problemas de seguridad. SNMP v1 
envía contraseñas en texto plano a través de la red. 
Por lo tanto, las contraseñas pueden leerse mediante detección de paquetes. SNMP v2 permite 
descomposición de contraseñas con MD5, pero esto hay que configurarlo. 
Virtualmente todas las aplicaciones de administración de redes soportan SNMP v1, pero no 
necesariamente SNMP v2 o v3. SNMP v2 fue desarrollado específicamente para proporcionar seguridad 
en la información, esto es autenticación, privacidad y autorización, pero solamente la versión SNMP 2c 
ganó la aprobación del Grupo de trabajo de Ingeniería de Internet (siglas IETF en inglés), mientras las 
versiones 2u y 2* no obtuvieron la aprobación de IETF debido a problemas de seguridad. SNMP v3 utiliza 
MD5, Algoritmo de Descomposición Seguro (siglas SHA en inglés) y algoritmos de claves para asegurar la 
protección contra la modificación de información no autorizada y ataques de enmascaramiento. 
Si se necesitara un nivel de seguridad superior, el algoritmo Estándar de Encriptación de Datos (siglas 
DES en inglés) podría utilizarse opcionalmente en modo de encadenamiento de bloques de cifras. SNMP 
v3 está implementado desde publicación de la versión 12.0(3)T de Cisco IOS. 
SNMPv3 es susceptible a ataques de fuerza bruta y ataques de diccionario para adivinar las claves de 
autenticación, o encriptación, si estas claves se generan mediante contraseñas cortas (o débiles), o 
contraseñas que se puedan encontrar en un diccionario. 
SNMPv3 permite claves de encriptación distribuidas de forma aleatoria, y también generación de 
contraseñas suministradas por el usuario. El riesgo de la adivinación de cadenas de autenticación 
mediante los valores descompuestos transmitidos por la red depende de la función de descomposición 
utilizada y de la longitud del valor descompuesto. 
SNMPv3 utiliza el Protocolo de Autenticación HMAC-SHA-2 para el Modelo de Seguridad del Usuario 
(siglas USM en inglés). El intercambio desafío-respuesta no fue utilizado para mejorar la seguridad. 
SNMPv3 (así como las otras versiones de SNMP) es un protocolo sin estado, y ha sido diseñado para 
minimizar la cantidad de interacciones entre el agente y el gestor. Por lo que la introducción de un 
intercambio desafío-respuesta para cada comando hubiera impuesto una carga sobre el agente (y 
probablemente sobre la red misma) que los diseñadores del protocolo consideraron excesivo e 
inaceptable. 
Las deficiencias de seguridad en todas las versiones de SNMP pueden mitigarse mediante mecanismos 
de confidencialidad y autenticación IPsec. 
La implementación de SNMP sobre la Seguridad de la Capa de Transporte de Datagramas (siglas DTLS 
en inglés) también está disponible.

---

Administración de Redes de Área Local 
95 
Descubrimiento automático SNMP 
Las aplicaciones de administración de redes basadas en SNMP envían las contraseñas repetidamente 
durante las operaciones habituales a través de la red. Por lo tanto, las contraseñas de texto plano son un 
riesgo de seguridad significativo. 
Si se utiliza SNMP v2, los administradores de redes deben habilitar la encriptación de contraseñas en los 
dispositivos de la red, que son los servidores SNMP sobre los que se ejecuta. (Esto puede hacerse con el 
comando snmp-server enable traps snmp authentication md5). 
Muchas implementaciones de SNMP incluyen un tipo de descubrimiento automático cuando un nuevo 
componente de la red, como un conmutador o un enrutador, es descubierto y agrupado 
automáticamente. 
En SNMPv1 y v2c esto se realiza a través de una cadena comunitaria que es retransmitida en texto-
plano a otros dispositivos. Es por este motivo que las cadenas comunitarias que están configuradas por 
defecto, son públicas para acceso de sólo lectura y privadas para acceso de lectura-escritura:1874SNMP 
era el primero en la lista de Problemas de Configuración por Defecto Más Comunes del Instituto SANS y 
el número diez en la lista de Amenazas de Seguridad de Internet Más Críticas del año 2000. 
Los administradores de redes y sistemas no cambian estas configuraciones frecuentemente:1874 La 
cadena comunitaria enviada por SNMP a través de la red no está encriptada. En cuanto se conociese la 
cadena de seguridad fuera de la organización podría convertirse en objetivo para un ataque. Para 
prevenir el descubrimiento de forma sencilla de la cadena comunitaria, SNMP debe configurarse para 
pasar las "trampas" de fallos de autenticación de nombres de comunidad y el dispositivo de gestión de 
SNMP necesita configurarse para reaccionar a la "trampa" de fallo de autenticación. 
SNMPv1 y v2 son vulnerables a los ataques de suplantación de identidad de direcciones IP, tanto si se 
ejecuta sobre TCP o UDP, y los sujetos de traspaso de la lista de acceso de dispositivos han sido 
implementados para restringir el acceso SNMP. 
Los mecanismos de seguridad SNMPv3 cómo USM o TSM previenen el éxito de los ataques. Sería inútil 
emplear SNMPv3 VACM (Control de acceso basado en Vistas) sin asegurar los mensajes con USM o TSM. 
6. Gestión de red 
Existen diferentes herramientas que permiten administrar las redes, algunas de ellas ya las has 
estudiado en la unidad 1 "Administración del Sistema Operativo y software de base". Te aconsejamos 
que las repases: 
• Herramienta NETSH. 
• Herramienta NETCAT. 
• Herramienta NET USER. 
• Etc. 
Vamos a ver a continuación otras dos herramientas de software.

---

Administración de Redes de Área Local 
96 
6.1. Nmap 
Nmap es un software escrito originalmente por Gordon Lyon (más conocido por su alias Fyodor 
Vaskovich) de código abierto, cuyo desarrollo se encuentra hoy a cargo de una comunidad. 
Nmap fue creado originalmente para Linux, aunque actualmente es multiplataforma, por lo que 
funciona en sistemas operativos basados en Unix (GNU/Linux, Solaris, BSD y Mac OS X), y también en 
otros Sistemas Operativos como Microsoft Windows y AmigaOS. 
Es una herramienta muy útil para un administrador de sistema, se usa para evaluar la seguridad de 
sistemas informáticos, efectuar rastreo de puertos, así como para descubrir servicios o servidores en 
una red informática, para ello Nmap envía unos paquetes definidos a otros equipos y analiza sus 
respuestas. 
Nmap apareció en septiembre de 1997, en un artículo de la revista Phrack Magazine, donde se incluía el 
código fuente, de forma que posteriormente, desarrollos incluyeron mejores algoritmos para 
determinar qué servicios estaban funcionando, reescritura de código de C a C++, y se agregaron tipos 
de scan adicionales y nuevos protocolos como IPv6. 
En febrero de 2004 apareció la versión Nmap 3.5, y la versión 4.0 en enero de 2006, con cientos de 
mejoras. 
 
 
 
 
+ Info 
Puedes obtener más información en las webs: 
https://nmap.org/ 
http://insecure.org/nmap/nmap_inthenews.html 
https://ayudalinux.com/comando-nmap/ 
 
 
Vamos a ver características de NMAP: 
• Posee varias funciones para sondear redes de computadores, incluyendo detección de equipos, 
servicios y sistemas operativos. 
Estas funciones son extensibles con el uso de scripts para proveer servicios de detección 
avanzados, (como vulnerabilidades y otras aplicaciones).

---

Administración de Redes de Área Local 
97 
• Descubrimiento de servidores: Identifica computadoras en una red, por ejemplo, listando 
aquellas que responden ping. 
• Identifica puertos abiertos en una computadora objetivo. 
• Determina qué servicios está ejecutando la misma. 
• Determina qué sistema operativo y versión utiliza dicha computadora, (esta técnica es también 
conocida como fingerprinting). 
• Obtiene algunas características del hardware de red de la máquina objeto de la prueba. 
• Durante un escaneo, es capaz de adaptarse a las condiciones de la red incluyendo latencia y 
congestión de la misma. 
• Es usado para pruebas de penetración y tareas de seguridad informática en general. 
• Permite hacer el inventario y el mantenimiento del inventario de computadores de una red. 
• Por tanto, se puede usar para auditar la seguridad de una red, mediante la identificación de todo 
nuevo servidor que se conecte. 
 
 
 
 
+ Info 
Nmap se confunde en ocasiones con herramientas para 
verificación de vulnerabilidades como Nessus. 
Nmap es difícilmente detectable, ha sido creado para evadir los 
Sistema de detección de intrusos (IDS) e interfiere lo menos 
posible con las operaciones normales de las redes y de las 
computadoras que son analizadas. 
 
La interfaz 
La interfaz de usuario oficial es nmapfe, escrita originalmente por Zach Smith, y Nmap lo integra desde 
la versión 2.2. Pero existen otras interfaces como son entre otras: 
• Basadas en navegadores Web: 
• LOCALSCAN. 
• nmap-web. 
• Nmap-CGI.

---

Administración de Redes de Área Local 
98 
• Interfaz sobre Microsoft Windows: 
• NmapW. 
• NmapWin. 
 
 
 
 
+ Info 
Una plataforma completa Nmap con capacidades para funcionar 
sobre distintos Sistemas Operativos se encuentra en UMIT. 
Zenmap es la interfaz oficial para sistemas operativos GNU/Linux, 
Windows, Mac OS X, etc. 
 
Seguridad o hacking 
Las herramientas usadas en el campo de la seguridad informática, también pueden utilizarse para 
hacking. Los crackers pueden usarlo para descubrir objetivos potenciales (puede usarse solo o para 
preparar otro ataque, con otra herramienta de intrusión). 
Los administradores de sistema pueden utilizarlo para verificar la presencia de posibles aplicaciones no 
autorizadas ejecutándose en el servidor, buscar fallas en sus propias redes, o detectar computadoras 
que no cumplen con los requisitos mínimos de seguridad de la organización. 
Nmap por sí solo sólo dará una indicación básica de la vulnerabilidad de una computadora, por lo que 
normalmente es usado en conjunto con otras herramientas y tests. 
 
 
 
 
Anécdota 
Nmap ha sido usado en la película The Matrix reloaded, donde el 
personaje Trinity penetra en el sistema de la central eléctrica, 
mediante la explotación de vulnerabilidades en el servidor SSH y en 
el Control de redundancia cíclica, (descubiertas en el 2001).

---

Administración de Redes de Área Local 
99 
 
 
 
La interfaz gráfica de Nmap en la película suscitó el interés de las 
discusiones en Internet, y fue comentado como una aparición 
bastante realista de las herramientas de hacking. 
Nmap y NmapFE fueron también usados en la película The 
Listening (2006), sobre un exfuncionario de la NSA 
estadounidense, que deserta y organiza una estación de 
contraespionaje en los Alpes italianos. 
Partes del código fuente de Nmap pueden verse en la película 
Battle Royale. 
 
6.2. Tracert y Traceroute 
Son comandos de diagnóstico de redes para mostrar las posibles rutas o caminos de los paquetes y 
medir las latencias de tránsito y los tiempos de ida y vuelta a través de redes de Protocolo de Internet. 
• Tracert se utiliza en Windows. 
• Tracertoute se utiliza en GNU/Linux o Mac. 
Estos comandos permiten: 
• Permite trazar la ruta que hace un paquete entrante que viene desde un host o punto de red 
hasta tu ordenador. 
• Sirve para encontrar y diagnosticar problemas que pueda haber en una red, o conexión con 
internet. 
• Se puede utilizar cuando no se consigue conectar con otro ordenador de la red, y se quiere 
saber en qué punto del trazado está el problema. 
• Puede servir cuando hay problemas para conecta con una web, y para saber si el problema es del 
usuario, de esa web, o de algún punto intermedio. 
Tracert 
En realidad, Tracert es una aplicación nativa de Windows, sólo que, en vez de ejecutarse con una 
interfaz gráfica, se ejecuta directamente en cualquiera de las dos consolas del sistema, tanto en el 
Símbolo de sistema como en Windows PowerShell, por ello se suele hacer referencia a él como 
comando porque para ejecutar la aplicación hay que utilizar el comando tracert en la consola.

---

Administración de Redes de Área Local 
100 
Cuando se ejecuta este comando, se envía un paquete (utilizando ICMP, Protocolo de control de 
mensajes de Internet) a un nodo de destino, y por el camino que sigue, el ordenador le va solicitando a 
cada enrutador o nodo por el que pasa el tiempo de respuesta de cada uno cuando pasa por ahí el 
paquete. 
Con el envío de esos paquetes se obtienen estadísticas del RTT o la latencia de red, y la dirección IP de 
cada uno de los nodos por los que va pasando el paquete hasta llegar a su destino. 
Tracert utiliza el campo Time To Live (TTL) de la cabecera IP. Se trata de un número entero que va 
siendo disminuyendo en cada nodo por el que pasa el paquete que se envía, y que cuando llega al valor 
0 es descartado. 
El comando envía varios mensajes, cada uno a un nodo diferente para obtener su información: 
• El mensaje que se envía al primer nodo tiene un valor TTL=1 para que al llegar a él se le reste un 
número y quede en 0, siendo descartado. 
• Al segundo nodo se le envía un valor TLL=2 para que rebote en el primero restándole uno, y 
luego llegue al segundo hasta convertirse cero allí. 
• Cuando el mensaje se convierte en 0 en un nodo, al ser descartado el nodo devuelve el mensaje 
de control con la información. 
Así conseguimos enviarle a cada nodo del camino un mensaje que se vaya a agotar en él, para que cada 
uno devuelva un mensaje informando sobre su IP, su tiempo de conexión, la latencia o si ha pasado algo. 
De esta forma, si existe un problema en la conexión desde nuestro ordenador a otro ordenador de la red 
o a una web, sabremos dónde se pierde la conexión y dónde está ese problema. 
7. Bibliografía 
• GÓMEZ, J Y GÓMEZ, O.D. Administración de sistemas operativos. Editorial RA-MA. 
• https://docs.microsoft.com/en-us/windows-server/storage/nfs/nfs-overview. 
• http://es.wikipedia.org. 
• http://en.wikipedia.org. 
• https://docs.microsoft.com/es-es/windows-server/identity/ad-ds/active-directory-domain-
services. 
• https://www.linuxadictos.com/los-mejores-gestores-particiones-linux.html. 
• https://es.wikipedia.org/wiki/Ifconfig#Parámetros. 
• https://www.softzone.es/2014/11/25/3-herramientas-gratuitas-para-particionar-y-
gestionar-discos-duros/.

---

Administración de Redes de Área Local 
101 
• https://vivantic.org/mejor-gestor-particiones/. 
• https://anlorenro.wordpress.com/2016/04/18/das-nas-y-san/. 
• http://rm-rf.es/storage-diferencias-entre-nas-san-y-das/. 
• https://blog.pandorafms.org/es/monitoreo-de-red-que-debemos-saber/. 
• http://informatica.uv.es/it3guia/ARS/transparencias_1c/snmp-santi.ppt. 
• https://apen.es/2017/03/10/las-10-mejores-herramientas-de-monitoreo-de-redes-del-
2017/. 
• https://es.wikipedia.org/wiki/Protocolo_simple_de_administraci%C3%B3n_de_red. 
• https://es.wikipedia.org/wiki/Balance_de_carga 
• https://quanti.com.mx/2018/07/20/que-es-load-balance-o-balance-de-carga/ 
• https://www.computerworld.es/tendencias/que-es-el-balanceo-de-carga 
• https://www.redeszone.net/tutoriales/servidores/balanceador-carga-load-balancer-que-es-
funcionamiento/ 
• https://www.cisco.com/c/es_mx/support/docs/ip/border-gateway-protocol-bgp/5212-
46.html 
• https://mundowin.com/5-mejores-soluciones-de-balanceo-de-carga-para-una-distribucion-
estable-del-trafico-de-la-
red/#:~:text=El%20balanceo%20de%20carga%20permite,ser%20dividida%20durante%20el%2
0proceso. 
• https://es.wikipedia.org/wiki/Amazon_EC2 
• Clúster de balanceo de carga y alta disponibilidad para servicios web y mail / María Mercedes 
Sinisterra / Tania Marcela Díaz Henao / Erik Giancarlo Ruiz López 
• https://es.wikipedia.org/wiki/Nmap 
• https://ayudalinux.com/comando-nmap

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial**: [[wiki/sources/bloque4-tema04|Fuente Oficial del Tema 04]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema04-redes-lan-dhcp-dns|Test Tema 04]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Portada e Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|⬅️ Tema 03]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema05|Tema 05 ➡️]]
