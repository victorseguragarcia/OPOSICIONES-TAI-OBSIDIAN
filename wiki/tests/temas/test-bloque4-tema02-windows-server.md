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

# 🔴 Test de Autoevaluación: Bloque 4 - Tema 02 (Administración de Windows Server y Active Directory)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 4 - Tema 02 (Administración de Windows Server y Active Directory)",
  "questions": [
    {
      "question": "En Active Directory Domain Services (AD DS), ¿cuál es el orden exacto de procesamiento y aplicación de las Directivas de Grupo (GPOs)?",
      "options": [
        "Dominio $",
        "Local $",
        "OU $",
        "Sitio $"
      ],
      "answer": "b",
      "explanation": "Regla mnemotécnica **LSDOU**: Local, Sitio (*Site*), Dominio (*Domain*), Unidad Organizativa (*OU*)."
    },
    {
      "question": "¿Qué protocolo criptográfico de autenticación de red basado en tickets (TGT y TGS) es el protocolo predeterminado en Active Directory desde Windows 2000?",
      "options": [
        "NTLMv2.",
        "Kerberos v5 (Puerto 88).",
        "RADIUS (802.1X).",
        "TACACS+."
      ],
      "answer": "b",
      "explanation": "Kerberos v5 opera sobre el puerto TCP/UDP 88 con el Centro de Distribución de Claves (KDC)."
    },
    {
      "question": "¿Cuántos roles FSMO (*Flexible Single Master Operations*) existen en un bosque de Active Directory y cuáles son únicos a nivel de TODO el bosque?",
      "options": [
        "5 roles en total; Maestro de Esquema y Maestro de Nombres de Dominio son únicos para todo el bosque.",
        "3 roles en total; todos únicos por dominio.",
        "7 roles en total; RID y PDC son únicos de bosque.",
        "4 roles en total; Infraestructura es el único de bosque."
      ],
      "answer": "a",
      "explanation": "5 roles FSMO: 2 a nivel de Bosque (*Schema Master* y *Domain Naming Master*) y 3 a nivel de Dominio (*PDC Emulator*, *RID Master*, *Infrastructure Master*)."
    },
    {
      "question": "¿Qué herramienta de línea de comandos en Windows Server permite forzar la actualización inmediata de las directivas de grupo en un cliente sin esperar al intervalo de refresco periódico?",
      "options": [
        "`dcdiag /fix`",
        "`gpupdate /force`",
        "`gpresult /v`",
        "`netdom resetpwd`"
      ],
      "answer": "b",
      "explanation": "`gpupdate /force` actualiza directivas de usuario y equipo inmediatamente."
    },
    {
      "question": "¿Qué puerto TCP/UDP estándar utiliza el protocolo LDAP seguro (LDAPS con cifrado TLS/SSL)?",
      "options": [
        "Puerto 389.",
        "Puerto 636.",
        "Puerto 3268.",
        "Puerto 445."
      ],
      "answer": "b",
      "explanation": "LDAP usa puerto 389; LDAPS (seguro sobre SSL) usa puerto 636."
    }
  ]
}
```
