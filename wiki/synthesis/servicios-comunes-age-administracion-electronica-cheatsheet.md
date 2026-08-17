---
title: "Cheatsheet de Servicios Comunes, Plataformas e Infraestructuras Digitales de la AGE"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-1
  - administracion-electronica
  - red-sara
  - clave
  - face
  - geiser
  - inside
sources:
  - "raw/sources/bloque1-tema09.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Servicios Comunes AGE Cheatsheet"
  - "Catálogo Servicios Digitales AGE"
---

# 🔴 Cheatsheet de Servicios Comunes, Plataformas e Infraestructuras Digitales de la AGE

Tabla de memorización de las plataformas tecnológicas del Catálogo de Servicios de Administración Digital de la Secretaría General de Administración Digital (SGAD).

---

## 🏛️ Matriz Maestra de Servicios Comunes de la AGE

| Servicio / Plataforma | Nombre Completo / Acrónimo | Función Técnica Principal |
|-----------------------|----------------------------|---------------------------|
| **Red SARA** | **S**istema de **A**plicaciones y **R**edes para las **A**dministraciones | Red privada de alta velocidad y seguridad que interconecta todos los Ministerios, CCAA, EE.LL. y la Unión Europea (mediante sTESTA / EuroDomain). |
| **Cl@ve** | Plataforma de Identidad Digital | Sistema unificado de autenticación ciudadana: Cl@ve PIN (código temporal por SMS/App) y Cl@ve Permanente (usuario/contraseña + OTP). |
| **Cl@ve Firma** | Firma Centralizada en la Nube | Firma electrónica avanzada con certificados cualificados almacenados en servidores seguros (HSM) de la AGE. |
| **Autofirm@** | Cliente de Firma Local | Aplicación de escritorio desarrollada por el Ministerio para realizar firmas electrónicas avanzadas en navegadores web (sin applets Java). |
| **@Firma (VALIDe)** | Plataforma de Validación de Firma | Servicio horizontal de validación de certificados y firmas electrónicas multi-PKI y sede de validación para ciudadanos (**VALIDe**). |
| **SIR** | **S**istema de **I**nterconexión de **R**egistros | Plataforma troncal que permite el intercambio electrónico seguro de asientos registrales entre todas las Administraciones (conforme a norma SICRES 3.0). |
| **GEISER** | Gestión Integrada de Servicios de Registro | Solución integral en la nube para oficinas de registro de la AGE conectada a SIR. |
| **ORVE** | Oficina de Registro Virtual | Aplicación web para digitalizar y enviar documentos desde oficinas de registro de entidades locales hacia cualquier administración a través de SIR. |
| **Notific@** | Plataforma de Notificaciones | Plataforma centralizada para emisión y gestión de notificaciones telemáticas y papel (conecta con la **Dirección Electrónica Habilitada única - DEHú**). |
| **FACe** | Punto General de Entrada de Facturas Electrónicas | Ventanilla única estatal para la remisión de facturas electrónicas (**Facturae 3.2.x**) a cualquier organismo público. |
| **INSIDE** | Infraestructura y Servicios de Documentos Electrónicos | Sistema para la gestión, foliado y remisión de expedientes electrónicos entre administraciones y con la Administración de Justicia. |
| **ARCHIVE** | Archivo Electrónico Único | Solución modular para la conservación y preservación a largo plazo de documentos y expedientes electrónicos (conforme al modelo OAIS). |
| **PAGe** | Punto de Acceso General electrónico | Portal ciudadano estatal (`administracion.gob.es`) con sede electrónica, buscador de trámites y acceso a **Mi Carpeta Ciudadana**. |
| **SIA** | **S**istema de **I**nformación **A**dministrativa | Inventario oficial y normalizado de todos los procedimientos administrativos de la AGE y otras AAPP. |
| **PID (SCSP)** | Plataforma de Intermediación de Datos | Servicio para evitar que el ciudadano aporte certificados en papel (consulta telemática de títulos, padrón, IRPF, TGSS mediante protocolo SCSP). |

---

## ⚠️ Trampas Típicas en Test sobre Servicios Comunes
- **SIR vs GEISER/ORVE**: **SIR** es la *red de intercambio/interconexión*, mientras que **GEISER** y **ORVE** son las *aplicaciones cliente de registro* que se conectan a SIR.
- **INSIDE vs ARCHIVE**: **INSIDE** gestiona el expediente durante su *tramitación activa e intercambio*; **ARCHIVE** gestiona la *custodia y preservación a largo plazo*.
- **FACe**: Exige el uso del formato estándar **Facturae** (XML firmado con XAdES).

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/servicios-comunes-administracion-electronica|Servicios Comunes de Administración Electrónica]]
- Guía: [[wiki/synthesis/bloque1-informatica-y-administracion-digital-master-guide|Guía Maestra Informática Bloque 1]]
