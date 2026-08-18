---
title: "Resumen Exhaustivo Tema 02 (Bloque 4): Servicios de Directorio, Active Directory DS y Kerberos v5"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-4
  - tema-02
  - sistemas
  - redes
  - seguridad
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque4-tema02.md]]"
  - "[[wiki/sources/bloque4-tema02]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|Tema 03 ➡️]]

# 🔴 Resumen Exhaustivo Tema 02 (Bloque 4): Servicios de Directorio, Active Directory DS y Kerberos v5

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 02**
> Serie X.500 de ITU-T, protocolo LDAPv3 (RFC 4511), Active Directory Domain Services (Bosques, Árboles, Dominios, OUs), base de datos NTDS.dit, SYSVOL, Catálogo Global (puerto 3268), protocolo de autenticación Kerberos v5 (KDC, AS, TGS, TGT) y Directivas de Grupo (GPOs con orden LSDOU).

---

## 🟣 1. Desarrollo Técnico, Redes y Seguridad Exhaustivo

### 1. Directorios Distribuidos y Protocolo LDAP
- **Estándar X.500 y Protocolo LDAPv3 (RFC 4511)**:
  - Optimizado para **altas tasas de lectura** y búsquedas jerárquicas rápidas en árbol (DIT - Directory Information Tree).
  - *Puertos Estándar*: **389 TCP/UDP** (LDAP en texto plano / StartTLS) y **636 TCP** (LDAPS sobre SSL/TLS).
  - *Formato DN (Distinguished Name)*: `CN=Victor Segura,OU=Informatica,DC=tai,DC=gob,DC=es`.

### 2. Active Directory Domain Services (AD DS)
- **Estructura Lógica**:
  - *Unidad Organizativa (OU)*: Contenedor más pequeño al que se pueden vincular Directivas de Grupo (GPO) o delegar administración.
  - *Dominio*: Límite de seguridad y replicación que comparte base de datos `NTDS.dit` y directivas.
  - *Árbol*: Conjunto de dominios con espacio de nombres DNS contiguo.
  - *Bosque (Forest)*: **Límite máximo de seguridad de Active Directory**. Comparte un único Catálogo Global y Esquema común.
- **Componentes Críticos**:
  - `NTDS.dit`: Base de datos de AD basada en el motor ESE (Extensible Storage Engine).
  - `SYSVOL`: Recurso compartido replicado vía DFS-R que almacena scripts de inicio y plantillas de GPOs.
  - **Catálogo Global (GC - Global Catalog)**: Puerto **TCP 3268** (SSL **3269**). Contiene réplica parcial de solo lectura de todos los objetos de todos los dominios del bosque (esencial para búsquedas y autenticación universal).
- **Directivas de Grupo (GPOs)**:
  - **Orden de Procesamiento y Aplicación**: **LSDOU** (1º Local $\rightarrow$ 2º Sitio $\rightarrow$ 3º Dominio $\rightarrow$ 4º Unidad Organizativa). En caso de conflicto prevalece la GPO de la OU más cercana al objeto (a menos que exista directiva con opción *No sustituir / Enforced*).
  - Comandos: `gpupdate /force` (fuerza actualización inmediata), `gpresult /r` (muestra políticas aplicadas al usuario/equipo).

### 3. Protocolo de Autenticación Kerberos v5 (RFC 4120)
- **Componentes del KDC (Key Distribution Center)**:
  - **AS (Authentication Server)**: Autentica al usuario contra la base de datos y emite el **TGT (Ticket Granting Ticket)** cifrado con la clave secreta del KDC.
  - **TGS (Ticket Granting Server)**: Recibe el TGT válido del cliente y emite el **Ticket de Servicio (ST / Service Ticket)** cifrado con la clave del servidor destino.
  - Puerto estándar de Kerberos: **Port 88 TCP/UDP**.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 02 (Bloque 4)**
> 1. **Orden de procesamiento de GPOs**: Es estrictamente **LSDOU** (Local, Sitio, Dominio, OU). La última política aplicada (OU) es la que manda.
> 2. **Puerto del Catálogo Global**: Es **TCP 3268** (para búsquedas rápidas en todo el bosque). El LDAP ordinario es puerto **389**.
> 3. **Límite Máximo de Seguridad de AD**: Es el **Bosque (Forest)**, no el dominio.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Orden GPOs**: **LSDOU** $\rightarrow$ **L**ocal $\rightarrow$ **S**itio $\rightarrow$ **D**ominio $\rightarrow$ **O**rganizational **U**nit.
> - **Puertos LDAP / GC**: **389 LDAP / 636 LDAPS / 3268 Catálogo Global**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque4-tema02|Fuente Oficial del Tema 02]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-4-sistemas-redes/tema-completo-bloque4-tema02|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque4-tema02-windows-server|Test Tema 02]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad|Mazo Flashcards Bloque 4]]
- 🏠 **Índice del Bloque 4**: [[wiki/synthesis/resumenes/resumen-maestro-bloque4|Resumen Maestro Bloque 4]]

---

> [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema01|⬅️ Tema 01]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque4|🏠 Índice Bloque 4]]  ·  [[wiki/synthesis/resumenes/bloque-4-sistemas-redes/resumen-bloque4-tema03|Tema 03 ➡️]]
