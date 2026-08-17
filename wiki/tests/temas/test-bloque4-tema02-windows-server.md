---
title: "Test de Autoevaluación: Bloque 4 - Tema 02 (Administración de Windows Server y Active Directory)"
type: "test"
target: "wiki/sources/bloque4-tema02.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-4
  - windows-server
  - active-directory
  - gpo
  - kerberos
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 02: Administración de Windows Server y Active Directory (AD DS)

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. En Active Directory Domain Services (AD DS), ¿cuál es el orden exacto de procesamiento y aplicación de las Directivas de Grupo (GPOs)?
- [ ] a) Dominio $
ightarrow$ Sitio $
ightarrow$ OU $
ightarrow$ Local
- [ ] b) Local $
ightarrow$ Sitio $
ightarrow$ Dominio $
ightarrow$ Unidad Organizativa (LSDOU)
- [ ] c) OU $
ightarrow$ Dominio $
ightarrow$ Sitio $
ightarrow$ Local
- [ ] d) Sitio $
ightarrow$ Dominio $
ightarrow$ OU $
ightarrow$ Equipo

### 2. ¿Qué protocolo criptográfico de autenticación de red basado en tickets (TGT y TGS) es el protocolo predeterminado en Active Directory desde Windows 2000?
- [ ] a) NTLMv2.
- [ ] b) Kerberos v5 (Puerto 88).
- [ ] c) RADIUS (802.1X).
- [ ] d) TACACS+.

### 3. ¿Cuántos roles FSMO (*Flexible Single Master Operations*) existen en un bosque de Active Directory y cuáles son únicos a nivel de TODO el bosque?
- [ ] a) 5 roles en total; Maestro de Esquema y Maestro de Nombres de Dominio son únicos para todo el bosque.
- [ ] b) 3 roles en total; todos únicos por dominio.
- [ ] c) 7 roles en total; RID y PDC son únicos de bosque.
- [ ] d) 4 roles en total; Infraestructura es el único de bosque.

### 4. ¿Qué herramienta de línea de comandos en Windows Server permite forzar la actualización inmediata de las directivas de grupo en un cliente sin esperar al intervalo de refresco periódico?
- [ ] a) `dcdiag /fix`
- [ ] b) `gpupdate /force`
- [ ] c) `gpresult /v`
- [ ] d) `netdom resetpwd`

### 5. ¿Qué puerto TCP/UDP estándar utiliza el protocolo LDAP seguro (LDAPS con cifrado TLS/SSL)?
- [ ] a) Puerto 389.
- [ ] b) Puerto 636.
- [ ] c) Puerto 3268.
- [ ] d) Puerto 445.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **a** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: Regla mnemotécnica **LSDOU**: Local, Sitio (*Site*), Dominio (*Domain*), Unidad Organizativa (*OU*).
> - **Pregunta 2 (b)**: Kerberos v5 opera sobre el puerto TCP/UDP 88 con el Centro de Distribución de Claves (KDC).
> - **Pregunta 3 (a)**: 5 roles FSMO: 2 a nivel de Bosque (*Schema Master* y *Domain Naming Master*) y 3 a nivel de Dominio (*PDC Emulator*, *RID Master*, *Infrastructure Master*).
> - **Pregunta 4 (b)**: `gpupdate /force` actualiza directivas de usuario y equipo inmediatamente.
> - **Pregunta 5 (b)**: LDAP usa puerto 389; LDAPS (seguro sobre SSL) usa puerto 636.
