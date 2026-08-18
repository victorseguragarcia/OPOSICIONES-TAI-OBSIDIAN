---
title: "Resumen Completo Tema 03 (Bloque 4): Virtualización, Contenedores (Docker, Kubernetes) y Cloud Computing"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-4
  - tema-03
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque4-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|⬅️ Tema 02]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|Tema 04 ➡️]]

# 🔴 Resumen Completo Tema 03 (Bloque 4): Virtualización, Contenedores (Docker, Kubernetes) y Cloud Computing

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 03**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema cubre la arquitectura de mensajería electrónica corporativa y la administración moderna de aplicaciones mediante contenedores y microservicios. Se detalla el funcionamiento de los agentes de correo (MUA, MTA, MDA, MS), el diálogo de comandos y códigos de estado de SMTP (RFC 5321), POP3 (RFC 1939), IMAP4 (RFC 3501), las extensiones MIME y S/MIME, y los mecanismos de autenticación y reputación de correo (SPF, DKIM, DMARC, RFC 2142). En la segunda parte, se analiza la arquitectura de microservicios frente al monolito, la contenedorización con Docker (namespaces, cgroups, imágenes OCI, Dockerfile) y la orquestación distribuida con Kubernetes (Pods, Deployments, Services, Ingress, arquitectura Master/Worker).

---

## 🧩 Estructura y Desglose Temático

### 1. Arquitectura y Protocolos de Correo Electrónico
- **Agentes del Ecosistema de Correo**:
  - **MUA (Mail User Agent)**: Cliente de correo del usuario (Thunderbird, Outlook, Webmail).
  - **MTA (Mail Transfer Agent)**: Servidor que enruta y transfiere correos entre dominios mediante SMTP (Postfix, Sendmail, Exim, Exchange).
  - **MDA (Mail Delivery Agent)**: Deposita el correo en el buzón local del destinatario (Dovecot, Procmail).
  - **MS (Mail Store)**: Almacén de buzones en formatos `mbox` (un solo fichero por buzón) o `Maildir` (un fichero por mensaje).
- **El Rol de DNS en el Correo**:
  - Registros **MX (Mail Exchanger)**: Indican los servidores MTA de un dominio con valor de prioridad (menor número = mayor prioridad).
  - Registros **A / AAAA**: Resuelven las FQDN de los MTAs a direcciones IP.
  - Registro **PTR**: Resolución inversa utilizada por los MTAs receptores para verificar la legitimidad de la IP del remitente.

#### 1.1 Protocolo SMTP (Simple Mail Transfer Protocol)
- Definido originalmente en RFC 821, actualizado en **RFC 5321** (ESMTP).
- Puertos estándar:
  - **25 TCP**: Transferencia entre MTAs (relay servidor-servidor).
  - **587 TCP**: Envío (*Submission*) cliente-a-servidor con autenticación (RFC 6409, `STARTTLS`).
  - **465 TCP**: SMTPS legado (SMTP encapsulado en SSL/TLS directo).
- **Comandos Principales SMTP**:
  - `HELO` / `EHLO` (identificación del cliente, EHLO habilita ESMTP).
  - `MAIL FROM:<origen>` (inicia transacción y define remitente del envelope).
  - `RCPT TO:<destino>` (especifica destinatario; puede repetirse).
  - `DATA` (inicia cuerpo del mensaje; finaliza con `<CRLF>.<CRLF>`).
  - `RSET` (cancela transacción actual), `NOOP` (no-operación), `QUIT` (cierra sesión), `VRFY` (verifica usuario), `STARTTLS` (negocia cifrado TLS).
- **Códigos de Respuesta SMTP**:
  - `2xx`: Éxito definitivo (ej. `220` Servicio listo, `250` Acción completada OK).
  - `3xx`: Éxito intermedio (ej. `354` Envíe datos de correo finalizando con `.`).
  - `4xx`: Fallo temporal (el cliente debe reintentar más tarde; ej. `421` Servicio no disponible).
  - `5xx`: Fallo permanente (rechazo definitivo; ej. `550` Buzón no encontrado).

#### 1.2 Protocolos de Recuperación: POP3 e IMAP4
- **POP3 (Post Office Protocol v3 - RFC 1939)**:
  - Puertos: **110 TCP** (plano) y **995 TCP** (POP3S con SSL/TLS).
  - Modelo *descarga y borra*: Descarga mensajes al cliente local y los elimina del servidor (o los deja temporalmente según configuración).
  - Estados: *Autorización* (`USER`, `PASS`, `APOP`), *Transacción* (`STAT`, `LIST`, `RETR`, `DELE`, `NOOP`, `RSET`), *Actualización* (`QUIT`).
- **IMAP4 (Internet Message Access Protocol v4 - RFC 3501)**:
  - Puertos: **143 TCP** (plano / STARTTLS) y **993 TCP** (IMAPS con SSL/TLS).
  - Modelo *sincronización bidireccional*: Los mensajes y carpetas residen permanentemente en el servidor.
  - Soporta descarga parcial (cabeceras antes del cuerpo/adjuntos), flags de estado (`\Seen`, `\Draft`, `\Deleted`) y múltiples clientes simultáneos.
- **Extensiones y Formatos**:
  - **MIME (Multipurpose Internet Mail Extensions - RFC 2045-2049)**: Permite adjuntos binarios (imágenes, PDFs) codificados en Base64, caracteres no ASCII y texto multipart/HTML.
  - **S/MIME**: Cifrado y firma digital de mensajes mediante certificados X.509.

#### 1.3 Seguridad y Reputación de Correo
- **SPF (Sender Policy Framework - RFC 7208)**: Registro DNS `TXT` que especifica qué IPs están autorizadas a enviar correo en nombre de un dominio.
- **DKIM (DomainKeys Identified Mail - RFC 6376)**: Firma criptográfica asimétrica añadida a la cabecera; el receptor valida la firma usando la clave pública publicada en DNS `TXT`.
- **DMARC (RFC 7489)**: Política unificada basada en SPF y DKIM que indica al receptor qué hacer ante correos no alineados (`none`, `quarantine`, `reject`) y genera reportes.
- **RFC 2142**: Nombres de buzón estándar obligatorios (`postmaster@`, `abuse@`, `webmaster@`, `hostmaster@`).

### 2. Arquitectura de Microservicios
- **Monolito vs. Microservicios**:
  - Monolito: Base de código única, despliegue todo-o-nada, acoplamiento alto, dificultad para escalar componentes individuales.
  - Microservicios: Servicios autónomos, desacoplados, desplegables independientemente, comunicados mediante APIs REST/gRPC o colas de mensajes (Kafka, RabbitMQ).
- **Patrones de Microservicios**: API Gateway, Service Mesh (Istio), Circuit Breaker (Netflix Hystrix), Service Discovery (Consul, Eureka).

### 3. Docker y Contenedores
- **Fundamentos del Kernel de Linux**:
  - **Namespaces**: Aislamiento de recursos (`pid`, `net`, `ipc`, `mnt`, `uts`, `user`).
  - **Control Groups (cgroups)**: Límite y monitorización de consumo de hardware (CPU, memoria, I/O, red).
  - **Union File Systems (Overlay2)**: Sistema de capas de solo lectura apiladas con una capa superior de lectura/escritura efímera.
- **Ecosistema Docker**:
  - Docker Engine (demonio `dockerd`), Docker CLI, Dockerfile (`FROM`, `RUN`, `COPY`, `CMD`, `ENTRYPOINT`, `EXPOSE`, `VOLUME`).
  - Registro de imágenes (Docker Hub, Harbor).
  - Estándar OCI (Open Container Initiative): `runc` y `containerd`.

### 4. Kubernetes (K8s) y Orquestación
- Plataforma de orquestación de contenedores desarrollada originalmente por Google.
- **Arquitectura del Clúster**:
  - **Control Plane (Master)**: `kube-apiserver` (punto central de API), `etcd` (almacén clave-valor distribuido), `kube-scheduler` (asigna pods a nodos), `kube-controller-manager` (controladores de estado deseado).
  - **Nodos Worker**: `kubelet` (agente de nodo que comunica con el runtime de contenedores), `kube-proxy` (gestión de reglas iptables/IPVS de red), Container Runtime (`containerd`, `CRI-O`).
- **Objetos Principales de Kubernetes**:
  - **Pod**: Unidad mínima de despliegue (uno o más contenedores estrechamente acoplados que comparten red y almacenamiento).
  - **Deployment / ReplicaSet**: Gestión declarativa de réplicas, actualizaciones progresivas (*rolling updates*) y rollbacks.
  - **Service**: Abstracción de red que expone un conjunto de pods bajo una IP/DNS estable (`ClusterIP`, `NodePort`, `LoadBalancer`).
  - **Ingress**: Enrutamiento HTTP/HTTPS perimetral hacia servicios internos con balanceo y terminación SSL.
  - **ConfigMaps y Secrets**: Inyección desacoplada de configuraciones y credenciales sensibles.

---

## 🎯 Datos Clave para Oposiciones TAI

| Protocolo / Herramienta | Puertos y Especificaciones |
|-------------------------|---------------------------|
| SMTP Transfer (Relay) | **25 TCP** (RFC 5321) |
| SMTP Submission | **587 TCP** (RFC 6409 con STARTTLS) |
| SMTPS (Legado SSL) | **465 TCP** |
| POP3 / POP3S | **110 TCP** / **995 TCP** (RFC 1939) |
| IMAP4 / IMAPS | **143 TCP** / **993 TCP** (RFC 3501) |
| Seguridad Anti-Spoofing | **SPF** (TXT), **DKIM** (Firma clave pública en TXT), **DMARC** (Alineación) |
| Buzones RFC 2142 | `postmaster@`, `abuse@`, `hostmaster@`, `webmaster@` |
| Primitivas Kernel Docker | **Namespaces** (aislamiento) + **cgroups** (límites de recursos) |
| Almacén Estado K8s | **etcd** (base de datos clave-valor distribuida en Raft, puertos 2379/2380) |
| Unidad Mínima K8s | **Pod** (comparte espacio de red `localhost` y volúmenes) |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/smtp-imap-pop3|Protocolos de Correo: SMTP, IMAP y POP3]]
- [[wiki/entities/docker-and-containers|Docker y Motores de Contenedores]]
- [[wiki/entities/kubernetes|Kubernetes y Orquestación de Contenedores]]
- [[wiki/entities/dns-protocol|Protocolo DNS y Registros MX]]

### Conceptos Teóricos:
- [[wiki/concepts/microservices-and-middleware|Microservicios, APIs y Middleware]]
- [[wiki/concepts/virtualization-and-cloud-computing|Virtualización y Computación Cloud]]
- [[wiki/concepts/network-security-and-perimeter-defense|Seguridad en Redes y Defensa Perimetral]]

### Síntesis de Estudio:
- [[wiki/synthesis/email-protocols-smtp-pop-imap-guide|Guía Completa de Protocolos de Correo y Seguridad SPF/DKIM/DMARC]]
- [[wiki/synthesis/virtualization-vs-containerization-comparison|Comparativa: Máquinas Virtuales vs Contenedores]]
- [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Cheatsheet de Puertos y Protocolos de Red]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque4-tema03|Nota Fuente del Tema 03]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema03-linux-administracion|Test Tema 03]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema02|⬅️ Tema 02]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema04|Tema 04 ➡️]]
