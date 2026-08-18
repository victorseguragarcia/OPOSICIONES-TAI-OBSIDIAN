# -*- coding: utf-8 -*-
r"""
Script para inyectar Tablas Comparativas Cara a Cara y Matrices de Decisión
en los temas teóricos de la Wiki TAI (wiki/sources/ y wiki/synthesis/).
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

def append_section_to_note(rel_path, section_md):
    fp = REPO_DIR / rel_path
    if not fp.exists():
        print(f"  [Skip / Not found] {rel_path}")
        return
    content = fp.read_text(encoding="utf-8")
    if section_md.strip().split("\n")[0] in content:
        print(f"  [Already present] {rel_path}")
        return
    new_content = content.rstrip() + "\n\n" + section_md.strip() + "\n"
    fp.write_text(new_content, encoding="utf-8")
    print(f"  [OK Enriched with Matrix] {rel_path}")

print("=" * 70)
print("📊 ENRIQUECIENDO TEMARIO CON TABLAS COMPARATIVAS CARA A CARA")
print("=" * 70)

# =============================================================================
# BLOQUE 1: MATRICES COMPARATIVAS
# =============================================================================

# Tema 02: Órganos Superiores vs Directivos de los Ministerios
append_section_to_note(
    "wiki/sources/bloque1-tema02.md",
    """
---

## 📊 Matriz Comparativa: Estructura Orgánica de los Departamentos Ministeriales (Ley 40/2015)

| Órgano Administrativo | Categoría Orgánica (Art. 55) | ¿Es Alto Cargo? (Ley 3/2015) | ¿Exige Funcionario A1? | Órgano de Nombramiento | Función Principal de Examen |
|:---|:---:|:---:|:---:|:---:|:---|
| **Ministro** | **Órgano Superior** | **SÍ** | **NO** | Real Decreto del Rey (a propuesta del Presidente del Gob.) | Miembro del Gobierno, dirige el Departamento y ejerce la potestad reglamentaria. |
| **Secretario de Estado** | **Órgano Superior** | **SÍ** | **NO** | Real Decreto de Consejo de Ministros (a propuesta del Ministro) | Dirige y coordina las Direcciones Generales del sector asignado. **NO es miembro del Gobierno**. |
| **Subsecretario** | **Órgano Directivo** | **SÍ** | **SÍ (A1 obligatorio)** | Real Decreto de Consejo de Ministros | Ostenta la **representación ordinaria**, jefatura superior de personal y dirige los servicios comunes. |
| **Secretario General** (asimilado a Subsecretario) | **Órgano Directivo** | **SÍ** | **NO** (salvo que el RD de estructura exija cualificación) | Real Decreto de Consejo de Ministros | Ejerce competencias sobre un sector de actividad específico cuando no hay Secretaría de Estado. |
| **Secretario General Técnico** (asimilado a Dir. Gral.) | **Órgano Directivo** | **SÍ** | **SÍ (A1 obligatorio + Lic. Derecho)** | Real Decreto de Consejo de Ministros | Asesoramiento jurídico, publicaciones, producción normativa y recursos administrativos. |
| **Director General** | **Órgano Directivo** | **SÍ** | **SÍ (A1)** *(Salvo excepción motivada por RD)* | Real Decreto de Consejo de Ministros | Gestión y ejecución de una o varias áreas homogéneas del Ministerio. |
| **Subdirector General** | **Órgano Directivo** | ❌ **NO (Empleado Público)** | **SÍ (A1 obligatorio)** | **Orden Ministerial** (a propuesta del Subsecretario/Director) | Ejecución directa de proyectos y gestión ordinaria de las unidades. |
"""
)

# Tema 05: Tipos de Empleados Públicos en el TREBEP
append_section_to_note(
    "wiki/sources/bloque1-tema05.md",
    """
---

## 📊 Matriz Comparativa: Clasificación de Empleados Públicos (Art. 8 a 12 TREBEP)

| Tipo de Empleado Público | Vínculo Jurídico | Causa / Supuesto de Nombramiento | Tipo de Selección | Reserva Exclusiva Potestades Públicas |
|:---|:---:|:---|:---:|:---:|
| **Funcionario de Carrera** (Art. 9) | Estatutario permanente | Servicio profesional retribuido con nombramiento legal | Oposición / Concurso-Oposición (Principios igualdad, mérito, capacidad) | **SÍ (Exclusivo Art. 9.2 TREBEP)** |
| **Funcionario Interino** (Art. 10) | Estatutario temporal | 1. Plazas vacantes (máx. 3 años).<br>2. Sustitución transitoria.<br>3. Programas temporales (máx. 3 años + 12 meses).<br>4. Exceso o acumulación de tareas (máx. 9 meses en 18 meses). | Procedimiento ágil respetando igualdad, mérito, capacidad y publicidad (Bolsas) | **SÍ** (mientras dure su nombramiento) |
| **Personal Laboral** (Fijo, Indefinido o Temporal) (Art. 11) | Contrato de trabajo (Derecho Laboral / Estatuto de los Trabajadores) | Puestos no reservados exclusivamente a funcionarios, oficios, mantenimiento, técnicos auxiliares | Oposición, Concurso-Oposición o Concurso de Méritos | ❌ **NO** (No pueden ejercer potestades públicas directas) |
| **Personal Eventual** (Art. 12) | No permanente (Cese libre) | Funciones de **confianza o asesoramiento especial** | Nombramiento y cese libre por los Ministros / Secretarios de Estado | ❌ **NO** (No pueden realizar tareas ordinarias de gestión) |
"""
)

# =============================================================================
# BLOQUE 2: MATRICES COMPARATIVAS
# =============================================================================

# Tema 01: Sistemas de Representación Numérica y Coma Flotante
append_section_to_note(
    "wiki/sources/bloque2-tema01.md",
    """
---

## 📊 Matriz Comparativa: Representación Entera y Coma Flotante IEEE 754

| Sistema de Representación | Rango para $n$ bits | ¿Tiene Doble Cero (+0 / -0)? | Ventaja Principal | Desventaja / Dificultad |
|:---|:---:|:---:|:---|:---|
| **Signo y Magnitud (SM)** | $[-(2^{n-1}-1), +(2^{n-1}-1)]$ | **SÍ** (`0000` y `1000`) | Intuitivo para humanos | Circuitos sumadores complejos |
| **Complemento a 1 (C1)** | $[-(2^{n-1}-1), +(2^{n-1}-1)]$ | **SÍ** (`0000` y `1111`) | Inversión bit a bit sencilla | Requiere suma de fin de vuelta (*End-around carry*) |
| **Complemento a 2 (C2)** | $[-2^{n-1}, +(2^{n-1}-1)]$ | ❌ **NO (Cero único)** | **Suma idéntica a enteros sin signo**. Estándar de la CPU | Rango asimétrico (un número negativo más) |
| **Exceso a $2^{n-1}$ (Sesgo)** | $[-2^{n-1}, +(2^{n-1}-1)]$ | ❌ **NO** | Facilita comparaciones de magnitud ordenadas | Requiere restar el sesgo |

### 📐 Formato Estándar IEEE 754

| Precisión | Tamaño Total | Bit de Signo | Bits de Exponente | Sesgo del Exponente | Bits de Mantisa (Fracción) | Bit Implícito |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Simple Precisión (Float32)** | **32 bits** (4 bytes) | 1 bit | 8 bits ($e$) | **127** ($2^{8-1}-1$) | 23 bits ($f$) | SÍ ($1.f$) |
| **Doble Precisión (Float64)** | **64 bits** (8 bytes) | 1 bit | 11 bits ($e$) | **1023** ($2^{11-1}-1$) | 52 bits ($f$) | SÍ ($1.f$) |
"""
)

# Tema 05: SQL Relacional vs NoSQL
append_section_to_note(
    "wiki/sources/bloque2-tema05.md",
    """
---

## 📊 Matriz Comparativa: Familias de Bases de Datos NoSQL y Teorema CAP

| Familia NoSQL | Estructura de Datos | Principales SGBD | Caso de Uso Ideal en Examen | Consistencia Típica |
|:---|:---|:---|:---|:---:|
| **Documental** | Documentos semiestructurados (JSON, BSON, XML) | **MongoDB, CouchDB, Amazon DocumentDB** | Catálogos web, CMS, aplicaciones móviles con esquemas dinámicos | CP o AP (Configurable) |
| **Clave-Valor** | Pares Clave $\rightarrow$ Valor binario/string | **Redis, Memcached, DynamoDB, Riak** | Caché de alta velocidad, sesiones de usuario, contadores | AP (Alta Disponibilidad) |
| **Columnares / Wide-Column** | Tablas con familias de columnas extensibles | **Apache Cassandra, HBase, ScyllaDB** | Big Data, series temporales, analítica distribuida de alto volumen | AP (Consistencia Eventual) |
| **Grafos** | Nodos, Relaciones (Aristas) y Propiedades | **Neo4j, Amazon Neptune, ArangoDB** | Redes sociales, detección de fraude, grafos de conocimiento | ACID (Consistente) |

### 🌐 Teorema CAP (Eric Brewer): En un sistema distribuido solo se pueden garantizar 2 de 3:
- **C (Consistencia)**: Todos los nodos ven los mismos datos al mismo tiempo.
- **A (Disponibilidad / Availability)**: Cada petición recibe una respuesta (sin garantía de ser la más reciente).
- **P (Tolerancia a Particiones)**: El sistema sigue funcionando a pesar de fallos de comunicación en la red.
*(En la práctica, al no poder evitar particiones de red en sistemas distribuidos, se elige **CP** o **AP**).*
"""
)

# =============================================================================
# BLOQUE 3: MATRICES COMPARATIVAS
# =============================================================================

# Tema 06: SOAP vs REST
append_section_to_note(
    "wiki/sources/bloque3-tema06.md",
    """
---

## 📊 Matriz Comparativa Cara a Cara: Servicios Web SOAP vs RESTful

| Característica | SOAP (Simple Object Access Protocol) | REST (Representational State Transfer) |
|:---|:---|:---|
| **Naturaleza** | **Protocolo formal estricto** (especificación W3C / OASIS) | **Estilo arquitectónico** basado en estándares web |
| **Formato de Mensaje** | **Exclusivamente XML** | **Múltiples formatos**: JSON (estándar de facto), XML, HTML, YAML |
| **Protocolo de Transporte** | Independiente (HTTP, HTTPS, SMTP, JMS, TCP) | **Exclusivamente HTTP / HTTPS** |
| **Definición de Interfaz** | **WSDL** (*Web Services Description Language*) | OpenAPI / Swagger, RAML (o enlaces HATEOAS) |
| **Estándar de Seguridad** | **WS-Security** (cifrado y firma XML a nivel de mensaje) | **HTTPS/TLS** (nivel transporte) + OAuth 2.0 / JWT |
| **Operaciones** | Definidas por funciones RPC en el Body (ej. `<getUser>`) | Verbos estándar HTTP: **GET, POST, PUT, DELETE, PATCH** |
| **Uso de Caché** | Difícil (la mayoría de peticiones usan POST) | **Nativo y transparente** (cabeceras Cache-Control en GET) |
| **Rendimiento y Sobrecarga** | Menor velocidad por *overhead* del envoltorio XML | **Alta velocidad, ligero y bajo consumo de ancho de banda** |
| **Caso de Uso Típico** | Banca, pasarelas de pago del Estado, interoperabilidad Red SARA | APIs móviles, microservicios, SPAs, servicios web modernos |
"""
)

# =============================================================================
# BLOQUE 4: MATRICES COMPARATIVAS
# =============================================================================

# Tema 05: Matriz RAID
append_section_to_note(
    "wiki/sources/bloque4-tema05.md",
    """
---

## 📊 Matriz Comparativa: Niveles RAID de Almacenamiento

| Nivel RAID | Técnica Utilizada | Discos Mínimos | Capacidad Útil (con $N$ discos de tamaño $S$) | Tolerancia a Fallos | Rendimiento Lectura | Rendimiento Escritura |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **RAID 0** | *Striping* (Fraccionamiento) | **2** | $N \times S$ (100%) | **0 discos** (Cero tolerancia) | Muy Alto ($N \times$) | Muy Alto ($N \times$) |
| **RAID 1** | *Mirroring* (Espejo) | **2** | $1 \times S$ (o $S/2$) (50%) | **$N-1$ discos** | Alto ($N \times$) | Normal (Igual a 1 disco) |
| **RAID 5** | Fraccionamiento con Paridad Distribuida | **3** | $(N - 1) \times S$ | **1 disco** | Muy Alto | Medio (*Overhead* cálculo paridad) |
| **RAID 6** | Fraccionamiento con Doble Paridad | **4** | $(N - 2) \times S$ | **2 discos simultáneos** | Muy Alto | Lento (Doble cálculo paridad) |
| **RAID 10 (1+0)** | Espejo de Fraccionamientos | **4** (pares) | $(N / 2) \times S$ (50%) | **Hasta 1 disco por sub-espejo** | Muy Alto | Muy Alto |
"""
)

# Tema 09: Criptografía Simétrica vs Asimétrica
append_section_to_note(
    "wiki/sources/bloque4-tema09.md",
    """
---

## 📊 Matriz Comparativa Cara a Cara: Criptografía Simétrica vs Asimétrica

| Característica | Criptografía Simétrica (Clave Secreta) | Criptografía Asimétrica (Clave Pública / Privada) |
|:---|:---|:---|
| **Número de Claves** | **1 sola clave compartida** (cifra y descifra) | **Par de claves matemáticas**: 1 Pública + 1 Privada |
| **Velocidad de Cómputo** | **Ultrarrápida** (operaciones a nivel de bit/bloque en hardware) | **Lenta** (operaciones matemáticas con números primos enormes) |
| **Tamaño de Claves Típico** | **128, 192 o 256 bits** (AES-256 es estándar gubernamental) | **2048 o 4096 bits** (RSA) \| **256 o 384 bits** (Curvas Elípticas ECC) |
| **Distribución de Claves** | Compleja (¿cómo enviar la clave secreta de forma segura?) | **Sencilla** (la clave pública se difunde abiertamente) |
| **Servicios de Seguridad** | **Confidencialidad** e Integridad (con HMAC) | **Confidencialidad, Autenticación, No Repudio y Firma Digital** |
| **Algoritmos Principales** | **AES (Rijndael), ChaCha20, 3DES, DES, Blowfish, RC4** | **RSA, ECC (ECDSA/Ed25519), Diffie-Hellman, DSA, ElGamal** |
| **Uso en Protocolos Híbridos (TLS)** | Cifrado masivo del flujo de datos de la sesión | Intercambio seguro de la clave de sesión y autenticación del servidor |
"""
)

print("\n[*] Inyección de matrices comparativas finalizada.")
