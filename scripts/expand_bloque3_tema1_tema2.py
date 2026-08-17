# -*- coding: utf-8 -*-
r"""
Script para profundizar exhaustivamente en el Bloque 3: Tema 01 y Tema 02
con todo el temario oficial (ANSI/SPARC, E/R, Normalización, Jerarquía de Chomsky, Compiladores, Parsers).
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

TEMA1_CONTENT = """---
title: "Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo E/R, Diseño Relacional y Normalización"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema01
  - modelado-datos
  - modelo-er
  - ansi-sparc
  - normalizacion
  - formas-normales
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Modelado de Datos y Normalización"
  - "bloque3-tema01"
---

# 🔴 Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo E/R, Diseño Relacional y Normalización

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque3-tema01-modelado-datos-bbdd.md|bloque3-tema01-modelado-datos-bbdd.md]] (90 páginas).

---

## 📖 1. Arquitectura ANSI/SPARC y Fases de Diseño de BBDD

### Arquitectura de 3 Niveles ANSI/SPARC:
1. **Nivel Externo**: Esquemas de usuario (vistas parciales y adaptadas a cada perfil o aplicación).
2. **Nivel Conceptual**: Esquema global lógico independiente del SGBD físico (entidades, relaciones y restricciones).
3. **Nivel Interno / Físico**: Estructuras de almacenamiento en disco, métodos de acceso, índices y organización de archivos.
- **Independencia Lógica**: Capacidad de modificar el esquema conceptual sin alterar los esquemas externos.
- **Independencia Física**: Capacidad de modificar el esquema interno (añadir índices, reorganizar ficheros) sin alterar el esquema conceptual.

---

## 🟣 2. Modelo Entidad-Relación Extendido (E/R de Peter Chen)

- **Entidades**:
  - **Fuertes (Regulares)**: Poseen existencia propia e identificación unívoca mediante su clave primaria.
  - **Débiles**: Dependen de otra entidad para existir (dependencia de existencia) o para identificarse (dependencia de identificación, representada con doble rectángulo).
- **Atributos**:
  - *Simples* (atómicos) vs *Compuestos* (ej. dirección compuesta por calle, número y CP).
  - *Monovaluados* vs *Multivaluados* (ej. varios teléfonos de un usuario, representados con doble elipse).
  - *Derivados / Calculados* (ej. edad calculada a partir de la fecha de nacimiento, elipse con trazo discontinuo).
- **Relaciones y Cardinalidad**:
  - Notación `(min, max)`: Participación obligatoria `(1, 1)` o `(1, N)` vs opcional `(0, 1)` o `(0, N)`.
- **Jerarquías de Generalización / Especialización**:
  - **Total**: Toda instancia de la superclase debe pertenecer obligatoriamente a alguna subclase.
  - **Parcial**: Pueden existir instancias de la superclase que no pertenezcan a ninguna subclase.
  - **Exclusiva (Disjunta)**: Una instancia puede pertenecer como máximo a una subclase.
  - **Solapada (Superpuesta)**: Una instancia puede pertenecer simultáneamente a varias subclases.

---

## 🔵 3. Reglas de Transformación del Modelo E/R al Modelo Relacional

| Elemento / Tipo de Relación | Regla Formal de Transformación Relacional |
|-----------------------------|-------------------------------------------|
| **Entidad Fuerte** | Se convierte en una **Tabla**, cuyos atributos son las columnas y la clave primaria (PK) es el identificador principal. |
| **Relación 1:N** | Se **propaga la clave primaria** del lado 1 como **clave foránea (FK)** en la tabla del lado N. |
| **Relación M:N** | Se genera una **nueva tabla** intermedia cuya clave primaria compuesta está formada por las claves foráneas de ambas entidades. |
| **Relación 1:1** | Se propaga la clave primaria de cualquiera de las entidades a la otra (preferentemente hacia la entidad con participación obligatoria `(1,1)`). |
| **Atributo Multivaluado** | Se crea una **tabla separada** que contiene el atributo multivaluado y la clave primaria de la entidad propietaria como clave foránea. |
| **Jerarquía (Opción A: Tabla Única)** | Una sola tabla con todos los atributos de la superclase y subclases, más un campo **discriminador** (genera nulos). |
| **Jerarquía (Opción B: Superclase + Subclases)** | Tabla para la superclase (con atributos comunes) y tablas para subclases (con atributos específicos y PK=FK apuntando a la superclase). |

---

## 🔵 4. Teoría de la Normalización y Formas Normales (1FN a 5FN)

### Definición de Dependencia Funcional (DF):
Dado un esquema $R$, existe una dependencia funcional $X \rightarrow Y$ si y solo si para cualquier par de tuplas $t_1, t_2 \in R$, si $t_1[X] = t_2[X]$ entonces $t_1[Y] = t_2[Y]$.

```
  1FN ──> 2FN ──> 3FN ──> BCNF (Boyce-Codd) ──> 4FN ──> 5FN
```

1. **Primera Forma Normal (1FN)**:
   - Todos los atributos son atómicos (valores indivisibles).
   - No existen grupos repetitivos ni atributos multivaluados.
2. **Segunda Forma Normal (2FN)**:
   - Cumple 1FN.
   - Todo atributo no principal posee **dependencia funcional completa** respecto a cada clave candidata (elimina dependencias parciales de claves compuestas).
3. **Tercera Forma Normal (3FN)**:
   - Cumple 2FN.
   - Ningún atributo no principal depende **transitivamente** de una clave candidata ($X \rightarrow Y \rightarrow Z$).
   - Condición formal: Para toda DF no trivial $X \rightarrow A$, $X$ es superclave o $A$ es un atributo primo (pertenece a alguna clave candidata).
4. **Forma Normal de Boyce-Codd (BCNF / FNBC)**:
   - Condición formal más estricta: Para **toda** dependencia funcional no trivial $X \rightarrow A$, $X$ debe ser **superclave**.
5. **Cuarta Forma Normal (4FN)**:
   - Cumple BCNF y no contiene **dependencias multivaluadas (MVD)** no triviales ($X \twoheadrightarrow Y$).
6. **Quinta Forma Normal (5FN / Proyección-Unión)**:
   - No puede descomponerse en esquemas menores sin pérdida mediante **dependencias de unión (Join Dependencies)**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Definición de Examen |
|----------|----------------------|
| **Clave Candidata** | Conjunto mínimo de atributos que identifica unívocamente a cada tupla en una relación. |
| **Clave Primaria (PK)** | Clave candidata elegida por el diseñador como identificador principal (no admite nulos). |
| **Clave Foránea (FK)** | Atributo en una relación que hace referencia a la clave primaria de otra (o de la misma) relación. |
| **Integridad de Entidad** | Ningún componente de la clave primaria puede tener valor nulo (`NOT NULL`). |
| **Integridad Referencial** | El valor de una clave foránea debe coincidir con un valor de clave primaria existente o ser nulo. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado de Datos Relacional y Normalización]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias Funcionales]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]
"""

TEMA2_CONTENT = """---
title: "Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema02
  - lenguajes-programacion
  - compiladores
  - interpretes
  - chomsky
  - gramaticas
  - parsers
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes de Programación y Compiladores"
  - "bloque3-tema02"
---

# 🔴 Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque3-tema02-lenguajes-programacion.md|bloque3-tema02-lenguajes-programacion.md]] (114 páginas).

---

## 📖 1. Clasificación y Paradigmas de Lenguajes de Programación

### Evolución por Generaciones:
- **1GL (Primera Generación)**: Lenguaje Máquina (código binario directo ejecutado por la CPU).
- **2GL (Segunda Generación)**: Lenguaje Ensamblador (mnemónicos traducidos por un ensamblador).
- **3GL (Tercera Generación)**: Lenguajes de Alto Nivel estructurados/imperativos (C, Pascal, Fortran, Java).
- **4GL (Cuarta Generación)**: Lenguajes declarativos orientados a bases de datos y gestión (SQL, ABAP, PL/SQL).
- **5GL (Quinta Generación)**: Lenguajes basados en restricciones, lógica e inteligencia artificial (Prolog, Lisp).

### Paradigmas de Programación:
- **Imperativo / Estructurado**: Secuencias de instrucciones que modifican el estado de la memoria (C, Pascal).
- **Orientado a Objetos (POO)**: Encapsulación de estado y comportamiento en objetos (Java, C++, C#, Python).
- **Funcional**: Basado en funciones puras sin efectos secundarios y evaluación de expresiones (Haskell, Scala, Clojure).
- **Lógico / Declarativo**: Basado en hechos, reglas y deducción matemática (Prolog).

---

## 🟣 2. Jerarquía de Chomsky de Gramáticas y Autómatas

La teoría de lenguajes formales de Noam Chomsky clasifica las gramáticas y sus reconocedores automáticos:

| Tipo | Tipo de Gramática | Reglas de Producción ($\alpha \rightarrow \beta$) | Autómata Reconocedor | Aplicación en Compilación |
|------|-------------------|---------------------------------------------------|----------------------|---------------------------|
| **Tipo 0** | **No Restringida** | Sin restricciones ($\alpha \rightarrow \beta$) | **Máquina de Turing** | Computabilidad universal |
| **Tipo 1** | **Sensible al Contexto** | $|\alpha| \le |\beta|$ ($uAv \rightarrow uwv$) | **Autómata Lineal Acotado (LBA)** | Análisis semántico complejo |
| **Tipo 2** | **Libre de Contexto (Incontextual)** | $A \rightarrow \gamma$ ($A \in V_N$, $\gamma \in (V_N \cup V_T)^*$) | **Autómata con Pila (PDA)** | **Análisis Sintáctico (Parser)** |
| **Tipo 3** | **Regular** | $A \rightarrow aB$ o $A \rightarrow a$ (Lineal) | **Autómata Finito (DFA / NFA)** | **Análisis Léxico (Scanner / Tokens)** |

---

## 🔵 3. Arquitectura y Fases de un Compilador

```
                   ESTRUCTURA DE UN COMPILADOR
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
FRONTEND (Depende del Lenguaje)              BACKEND (Depende de la CPU)
  1. Análisis Léxico (Scanner)                 4. Generación de Código Intermedio
     • Lee caracteres $\rightarrow$ Tokens        • Código 3 direcciones / Bytecode
  2. Análisis Sintáctico (Parser)              5. Optimización de Código
     • Gramática Tipo 2 $\rightarrow$ AST         • Eliminación de código muerto/bucles
  3. Análisis Semántico                        6. Generación de Código Máquina
     • Tipos y Tabla de Símbolos                  • Binario ejecutable objeto (.obj / .exe)
```

---

## 🔵 4. Analizadores Sintácticos (Parsers): Top-Down vs Bottom-Up

### A. Analizadores Descendentes (*Top-Down*):
- Construyen el árbol sintáctico desde la raíz (símbolo inicial) hacia las hojas.
- **LL(k)**: Lectura de **I**zquierda a derecha, derivación más a la **I**zquierda (*Leftmost*), con $k$ símbolos de anticipación (*lookahead*).
- Requieren gramáticas no ambiguas y sin recursividad por la izquierda.

### B. Analizadores Ascendentes (*Bottom-Up*):
- Construyen el árbol sintáctico desde las hojas (tokens) hacia la raíz mediante operaciones de desplazamiento (*Shift*) y reducción (*Reduce*).
- **LR(k)**: Lectura de **I**zquierda a derecha, derivación más a la **D**erecha invertida (*Rightmost*).
- Tipos de Parsers LR:
  - **LR(0)**: Sin símbolos de anticipación.
  - **SLR(1)** (*Simple LR*): Utiliza conjuntos *FOLLOW* para resolver conflictos desplazamiento/reducción.
  - **LALR(1)** (*Lookahead LR*): Combina estados equivalentes de LR(1) (base de herramientas como **Yacc** / **Bison**).
  - **LR(1)**: Máxima potencia sintáctica pero con tablas de gran tamaño.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| **Compilador** | Traduce todo el código fuente de una vez a código objeto ejecutable nativo antes de la ejecución. |
| **Intérprete** | Traduce y ejecuta las instrucciones línea por línea en tiempo real (mayor portabilidad, menor velocidad). |
| **JIT (Just-In-Time)** | Compilación híbrida en tiempo de ejecución (compila bytecode frecuentemente usado a código máquina nativo, ej. JVM y CLR). |
| **Gestión de Memoria** | **Stack** (registros de activación, variables locales) vs **Heap** (memoria dinámica gestionada por punteros o Garbage Collector). |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/programming-languages-and-compilers|Lenguajes de Programación, Paradigmas y Compiladores]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
"""

print("[*] Escribiendo resúmenes ampliados para Bloque 3: Tema 01 y Tema 02...")
write_file("wiki/sources/bloque3-tema01.md", TEMA1_CONTENT)
write_file("wiki/sources/bloque3-tema02.md", TEMA2_CONTENT)
print("[*] Temas 01 y 02 de Bloque 3 actualizados con éxito.")
