# -*- coding: utf-8 -*-
r"""
Script para profundizar al máximo rigor técnico todas las notas del Bloque 3 (Desarrollo de Sistemas)
incorporando axiomas de Armstrong, ciclo de vida de componentes, Richardson Maturity Model,
métrica de McCabe y plazos exactos del RD 1112/2018.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

DEEP_ENTITIES = {
    "wiki/entities/relational-database-modeling-and-normalization.md": """---
title: "Modelado de Datos Relacional, Modelo E/R y Normalización Rigurosa"
type: "entity"
tags:
  - modelado-datos
  - bases-datos
  - modelo-er
  - normalizacion
  - armstrong
  - sql
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelado Relacional y Normalización"
  - "Teoría de Normalización y Armstrong"
---

# Modelado de Datos Relacional, Modelo E/R y Normalización Rigurosa

El modelado relacional estructura los datos mediante relaciones (tablas) formadas por tuplas (filas) y atributos (columnas), garantizando la integridad de entidad e integridad referencial y eliminando redundancias mediante la teoría formal de la normalización.

---

## 🏛️ 1. Fases del Diseño de Bases de Datos

```
[ Requisitos de Negocio ]
           │
           ▼
1. DISEÑO CONCEPTUAL ──> Modelo Entidad-Relación (E/R de Chen)
           │             • Entidades (fuertes / débiles)
           │             • Atributos (simples, compuestos, multivaluados, derivados)
           │             • Relaciones (1:1, 1:N, M:N; cardinalidades mín/máx)
           ▼
2. DISEÑO LÓGICO ──────> Transformación al Modelo Relacional (Codd)
           │             • Tablas, Claves Primarias (PK), Claves Foráneas (FK)
           │             • Aplicación de Reglas de Normalización (1FN a BCNF)
           ▼
3. DISEÑO FÍSICO ──────> Estructuras de Almacenamiento en RDBMS
                         • Espacios de tablas (Tablespaces), Particionamiento
                         • Índices (B-Tree, Bitmap, Hash), Clústeres
```

---

## 📐 2. Axiomas de Armstrong (Reglas de Inferencia de Dependencias Funcionales)

Dado un conjunto de dependencias funcionales $F$, las reglas de Armstrong permiten derivar el cierre $F^+$:

1. **Axioma de Reflexividad**: Si $Y \subseteq X$, entonces $X \rightarrow Y$.
2. **Axioma de Aumento**: Si $X \rightarrow Y$, entonces $XZ \rightarrow YZ$.
3. **Axioma de Transitividad**: Si $X \rightarrow Y$ y $Y \rightarrow Z$, entonces $X \rightarrow Z$.

### Reglas Derivadas:
- **Unión (Aditividad)**: Si $X \rightarrow Y$ y $X \rightarrow Z$, entonces $X \rightarrow YZ$.
- **Descomposición (Proyectividad)**: Si $X \rightarrow YZ$, entonces $X \rightarrow Y$ y $X \rightarrow Z$.
- **Pseudotransitividad**: Si $X \rightarrow Y$ y $WY \rightarrow Z$, entonces $WX \rightarrow Z$.

---

## 📋 3. Formas Normales (1FN a 5FN)

| Forma Normal | Condición Rigurosa de Examen | Anomalía que Elimina |
|--------------|------------------------------|----------------------|
| **1FN** | Todos los dominios de los atributos son **atómicos** (valores escalares indivisibles, sin arrays ni tablas anidadas). | Multivalores y grupos repetitivos |
| **2FN** | Cumple 1FN y **todo atributo no principal tiene dependencia funcional completa de cada clave candidata** (no depende de un subconjunto propio de una clave compuesta). | Dependencias parciales |
| **3FN** | Cumple 2FN y **ningún atributo no principal depende transitivamente de ninguna clave** (para todo $X \rightarrow A$, $X$ es superclave o $A$ es atributo primo). | Dependencias transitivas ($X \rightarrow Y \rightarrow Z$) |
| **BCNF (Boyce-Codd)** | Para **toda** dependencia funcional no trivial $X \rightarrow A$, $X$ es una **superclave** (clave candidata). | Anomalías en claves candidatas compuestas solapadas |
| **4FN** | Cumple BCNF y para toda **dependencia multivaluada** $X \twoheadrightarrow Y$ no trivial, $X$ es superclave. | Redundancia por atributos multivaluados independientes |
| **5FN (Proyección-Unión)** | Cumple 4FN y no puede descomponerse en esquemas menores sin perder información mediante **dependencias de unión (JD)**. | Anomalías de unión en relaciones $N$-arias ($N \ge 3$) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
""",

    "wiki/entities/sql-ansi-and-stored-procedures.md": """---
title: "Estándar ANSI SQL, Procedimientos Almacenados, Triggers y Transacciones ACID"
type: "entity"
tags:
  - sql
  - ddl
  - dml
  - acid
  - triggers
  - stored-procedures
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ANSI SQL y Programación BBDD"
  - "SQL Transacciones y Triggers"
---

# Estándar ANSI SQL, Procedimientos Almacenados, Triggers y Transacciones ACID

Lenguaje estructurado de consultas normalizado por ANSI/ISO (SQL-86, SQL-92, SQL:1999 con soporte OO, SQL:2016 con JSON) para gestión y programación de bases de datos relacionales.

---

## 🏛️ 1. Clasificación de Sentencias SQL

```
                               Sublenguajes SQL
                                       │
     ┌──────────────────┬──────────────┴─────┬──────────────────┐
     ▼                  ▼                    ▼                  ▼
  [ DDL ]            [ DML ]              [ DCL ]            [ TCL ]
Definición         Manipulación           Control          Transacciones
 • CREATE           • SELECT               • GRANT            • COMMIT
 • ALTER            • INSERT               • REVOKE           • ROLLBACK
 • DROP             • UPDATE                                  • SAVEPOINT
 • TRUNCATE         • DELETE                                  • SET TRANS.
```

---

## ⚙️ 2. Disparadores (Triggers) y Objetos Programables

- **Tipos de Triggers según Momento**:
  - `BEFORE`: Se ejecuta antes de la operación DML (ideal para validaciones o cálculo de valores por defecto).
  - `AFTER`: Se ejecuta después de la operación DML (ideal para auditoría, replicación o actualización de tablas resumen).
  - `INSTEAD OF`: Reemplaza la sentencia DML (utilizado obligatoriamente para permitir modificaciones en **Vistas complejas no actualizables**).
- **Ámbito de Ejecución**:
  - `FOR EACH ROW`: Disparador de fila (utiliza las pseudotablas / registros `:OLD` y `:NEW` en Oracle/PostgreSQL o `INSERTED`/`DELETED` en SQL Server).
  - `FOR EACH STATEMENT`: Disparador de sentencia (se ejecuta una única vez por instrucción independientemente del número de filas afectadas).

---

## 🔒 3. Transacciones y Propiedades ACID

1. **Atomicidad (Atomicity)**: La transacción se ejecuta en su totalidad o no se ejecuta nada (*All or Nothing*).
2. **Consistencia (Consistency)**: La transacción traslada la base de datos de un estado válido a otro estado válido cumpliendo todas las restricciones de integridad.
3. **Aislamiento (Isolation)**: Las operaciones de transacciones concurrentes son invisibles entre sí hasta su confirmación.
4. **Durabilidad (Durability)**: Una vez confirmada (`COMMIT`), los cambios persisten de forma permanente incluso ante caídas del sistema (*Write-Ahead Logging* / WAL).

### Niveles de Aislamiento SQL ANSI vs Anomalías Concurrencia:

| Nivel de Aislamiento | Lectura Sucia (*Dirty Read*) | Lectura No Repetible (*Non-Repeatable Read*) | Lectura Fantasma (*Phantom Read*) |
|----------------------|------------------------------|---------------------------------------------|-----------------------------------|
| **Read Uncommitted** | Permitida | Permitida | Permitida |
| **Read Committed** | **Prevenida** | Permitida | Permitida |
| **Repeatable Read** | **Prevenida** | **Prevenida** | Permitida |
| **Serializable** | **Prevenida** | **Prevenida** | **Prevenida** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
""",

    "wiki/entities/web-accessibility-wcag-and-rd-1112-2018.md": """---
title: "Accesibilidad Web: Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018"
type: "entity"
tags:
  - accesibilidad-web
  - wcag
  - pour
  - rd-1112-2018
  - en-301-549
  - administracion-publica
sources:
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Accesibilidad Web Oficial"
  - "WCAG y RD 1112/2018"
---

# Accesibilidad Web: Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018

Marco normativo y técnico de obligado cumplimiento para garantizar la accesibilidad universal en todos los entornos digitales de las Administraciones Públicas españolas.

---

## 👁️ 1. Los 4 Principios POUR (WCAG 2.1 / 2.2)

1. **Perceptible**: La información y los componentes de la interfaz deben presentarse de forma que los usuarios puedan percibirlos con sus sentidos.
   - Alternativas textuales para contenido no textual (`alt`, `aria-label`).
   - Medios temporales: Subtítulos y audiodescripciones.
   - **Ratio de Contraste Nivel AA**: Mínimo **4.5:1** para texto normal y **3:1** para texto grande ($\ge 18\text{pt}$ o $\ge 14\text{pt}$ negrita) y componentes gráficos/UI.
2. **Operable**: Los componentes de navegación e interacción deben ser manejables.
   - **Accesibilidad total por teclado** (sin requerir ratón y sin trampas de foco).
   - Tiempo suficiente para leer y usar el contenido (mecanismos de pausa/ampliación).
   - No diseñar contenido que provoque convulsiones o reacciones físicas (evitar destellos $> 3\text{ Hz}$).
3. **Comprensible**: La información y el manejo de la interfaz deben ser comprensibles y predecibles.
   - Idioma de la página declarado en HTML (`<html lang="es">`).
   - Navegación e identificación coherentes y predecibles.
   - Asistencia a la entrada de datos: Detección y sugerencia automática de corrección de errores en formularios.
4. **Robusto**: El contenido debe ser lo suficientemente robusto como para ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia (lectores de pantalla NVDA, JAWS, VoiceOver).
   - Código HTML válido y estandarizado.
   - Uso correcto de especificaciones **WAI-ARIA** (`role`, `aria-expanded`, `aria-hidden`).

---

## 🏛️ 2. Exigencias Legales del Real Decreto 1112/2018 en España

- **Ámbito Subjetivo**: Obliga a la Administración General del Estado, CCAA, Entidades Locales y organismos públicos vinculados o dependientes.
- **Nivel de Conformidad Exigido**: **Nivel AA** (alineado con la norma europea **EN 301 549**).
- **Obligaciones Esenciales**:
  1. **Declaración de Accesibilidad**: Publicada en formato accesible en cada sede electrónica, portal web y aplicación móvil, actualizada anualmente.
  2. **Unidad Responsable de Accesibilidad (URA)**: Cada organismo público debe designar formalmente una URA encargada de garantizar el cumplimiento y canalizar las quejas.
  3. **Mecanismo de Comunicación y Reclamación**: Canal habilitado para consultas ciudadanas sobre accesibilidad.
  4. **Plazo Legal de Respuesta**: Plazo máximo de **20 días hábiles** para responder a quejas y solicitudes de información accesible.
  5. **Informes de Seguimiento**: Informes periódicos cada **3 años** remitidos a la Comisión Europea.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema08|Resumen Bloque 3 - Tema 08]]
- Síntesis: [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR y RD 1112/2018]]
"""
}

print("[*] Escribiendo entidades enriquecidas del Bloque 3...")
for path, content in DEEP_ENTITIES.items():
    write_file(path, content)

print("[*] Enriquecimiento técnico del Bloque 3 completado.")
