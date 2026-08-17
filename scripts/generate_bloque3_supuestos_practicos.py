# -*- coding: utf-8 -*-
r"""
Script generador de la sección de Supuestos Prácticos del Bloque 3 (Desarrollo de Sistemas)
con autoevaluación interactiva, soluciones explicadas paso a paso y trampas de examen.
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

SUPUESTOS = {
    "wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md": """---
title: "Supuesto Práctico Resuelto: Normalización de Bases de Datos (1FN a 5FN) y SQL DDL"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-3
  - normalizacion
  - sql
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Supuesto Práctico Normalización"
  - "Casos Prácticos BBDD Bloque 3"
---

# 🔴 Supuesto Práctico Resuelto: Normalización de Bases de Datos (1FN a 5FN) y SQL DDL

Guía práctica de resolución de supuestos de examen sobre normalización relacional, dependencias funcionales y definición de esquemas en SQL ANSI.

---

## 📋 Caso 1: Identificación de Formas Normales en Tablas Reales

### Enunciado 1.1: Atomicidad de Atributos (1FN)
Dada la siguiente tabla `PERSONAS`:
| id | nombre | fecha_nacimiento | pais |
|---|---|---|---|
| 1 | José Pérez Fernández | 21/10/1970 | España |
| 2 | María López Ruiz | 01/01/1974 | Perú |

> [!question]- ❓ ¿Cumple la tabla la Primera Forma Normal (1FN)?
> **Respuesta Correcta**: **b) Sí, pues cada campo contiene un valor atómico dentro del dominio definido.**
>
> **Justificación Técnica**: 
> En el modelo relacional, un atributo es atómico si no contiene listas, conjuntos repetitivos o subtablas anidadas. A nivel de diseño, guardar `nombre y apellidos` en un campo de texto no viola formalmente 1FN salvo que el modelo exija explícitamente la descomposición por requisitos de negocio.

---

### Enunciado 1.2: Dependencias Parciales (2FN)
Dada la tabla `MATRICULAS` con clave primaria compuesta `(dni, curso, modulo)`:
| dni | nombre | apellidos | direccion | curso | modulo | nota |
|---|---|---|---|---|---|---|
| 12345678A | Almudena | Cantero Leal | Calle Sur | AD | DAM1 | 5.1 |
| 23456789B | Luis | López Ruiz | Calle Norte | PSP | DAM1 | 5.5 |

> [!question]- ❓ ¿Cumple la tabla la Segunda Forma Normal (2FN)?
> **Respuesta Correcta**: **a) No, existen dependencias funcionales parciales.**
>
> **Justificación Técnica**: 
> La clave primaria es `(dni, curso, modulo)`. Los atributos `nombre`, `apellidos` y `direccion` dependen únicamente de una parte de la clave (`dni`), es decir: `dni -> {nombre, apellidos, direccion}`. Para cumplir 2FN, todo atributo no principal debe tener **dependencia funcional completa** de toda la clave.

---

### Enunciado 1.3: Dependencias Transitivas (3FN) y Descomposición
Partiendo de las tablas resultantes:
- `USUARIOS(dni, nombre, apellidos, direccion)`
- `CURSOS(idcurso, curso, modulo)`
- `USUARIO_CURSOS(dni, idcurso, nota)`

> [!question]- ❓ ¿En qué forma normal se encuentra el esquema descompuesto?
> **Respuesta Correcta**: **3FN y BCNF**.
>
> **Justificación Técnica**:
> - Cada tabla representa una única entidad o relación.
> - No existen atributos multivaluados (1FN).
> - No existen dependencias parciales (2FN).
> - No existen dependencias transitivas entre atributos no clave ($X \rightarrow Y \rightarrow Z$) (3FN).

---

## 📋 Caso 2: Esquema Comercial Completo y 4FN

Dadas las siguientes tablas:
```sql
Cliente (idCliente, nombre, direccion)
Vendedor (idVendedor, nombre)
Venta (idVenta, Fecha, idCliente, idVendedor)
Articulos (idArticulo, nombre, precio)
ArticulosVendidos (idVenta, idArticulo, cantidad)
```

> [!question]- ❓ ¿En qué Forma Normal se encuentra este esquema? ¿Requiere 4FN?
> **Respuesta Correcta**: Se encuentra en **3FN / BCNF**. No requiere transformaciones para 4FN porque **no existen dependencias multivaluadas independientes** ($X \twoheadrightarrow Y$).

---

## 💻 Caso 3: Sintaxis SQL DDL para Creación de Esquema

> [!question]- ❓ Escribe la sentencia SQL ANSI para crear la tabla `Estudiante` con clave primaria autoincremental:
> ```sql
> CREATE TABLE Estudiante (
>     CodEstudiante INT AUTO_INCREMENT,
>     nombre VARCHAR(120) NOT NULL,
>     CONSTRAINT pk_estudiante PRIMARY KEY (CodEstudiante)
> );
> ```

> [!warning] ⚠️ Trampas Típicas de Examen en Normalización
> 1. **Confundir 2FN con 3FN**: 2FN solo aplica a tablas con **claves primarias compuestas** (si la PK es de un solo atributo y está en 1FN, automáticamente está en 2FN).
> 2. **BCNF vs 3FN**: La 3FN permite $X \rightarrow A$ si $A$ es atributo primo; la BCNF exige estrictamente que $X$ sea superclave sin excepciones.
> 3. **4FN**: Se aplica exclusivamente cuando existen **dos o más atributos multivaluados independientes** en la misma relación.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado Relacional y Normalización]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
""",

    "wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion.md": """---
title: "Supuesto Práctico Resuelto: Trazas de Código Java y PHP (Bucles, Herencia y Operadores)"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-3
  - java
  - php
  - programacion
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Supuesto Práctico Programación Java y PHP"
  - "Trazas de Código Bloque 3"
---

# 🔴 Supuesto Práctico Resuelto: Trazas de Código Java y PHP

Ejercicios prácticos de seguimiento de ejecución, bucles infinitos, operadores ternarios, sobrecarga y estructuras de control.

---

## ☕ 1. Trazas de Bucles en Java

### Ejercicio 1.1: Bucle con Condición Inicial Falsa
```java
int contador = 1; 
while (contador < 0) { 
    System.out.println(contador); 
    contador--; 
}
```
> [!question]- ❓ ¿Cuál es la salida del programa?
> **Respuesta**: **Nunca entra en el bucle**. La condición `1 < 0` se evalúa a `false` antes de la primera iteración.

---

### Ejercicio 1.2: Bucle Infinito por Incremento de Paso
```java
int contador = 3; 
while (contador != 10) { 
    System.out.println(contador); 
    contador += 2; 
}
```
> [!question]- ❓ ¿Qué ocurre durante la ejecución?
> **Respuesta**: **Bucle Infinito**. La variable `contador` toma la secuencia de valores impares: `3, 5, 7, 9, 11, 13...` saltándose el valor `10`, por lo que `contador != 10` nunca será falso.

---

### Ejercicio 1.3: Bucle con `continue` y `break`
```java
int a = 5; 
for (int i = 1; i <= 10; i++) { 
    if (i % 2 == 0) continue;  
    a = a + i; 
    System.out.print(i++ + "," + a + " "); 
    if (a > 20) break; 
}
```
> [!question]- ❓ ¿Qué imprime por pantalla este fragmento?
> **Traza paso a paso**:
> 1. $i=1$: Impar $\rightarrow a = 5 + 1 = 6$. Imprime `1,6 `. En la misma línea $i$ se incrementa con `i++` pasando a valer $2$. El `for` hace `i++`, pasando a $3$.
> 2. $i=3$: Impar $\rightarrow a = 6 + 3 = 9$. Imprime `3,9 `. $i$ pasa a $4$ con `i++`, y a $5$ con el `for`.
> 3. $i=5$: Impar $\rightarrow a = 9 + 5 = 14$. Imprime `5,14 `. $i$ pasa a $6$, y a $7$ con el `for`.
> 4. $i=7$: Impar $\rightarrow a = 14 + 7 = 21$. Imprime `7,21 `. Como $a > 20$ ($21 > 20$), ejecuta `break` y sale.
> **Salida final**: `1,6 3,9 5,14 7,21 `

---

## 🐘 2. Estructuras Condicionales en PHP y Operadores

### Ejercicio 2.1: Evaluación de `elseif` en PHP
```php
<?php 
$a = 10; 
if ($a < 10 && $a > 1)  
    echo 'el valor es menor que 10'; 
elseif ($a > 10) 
    echo 'el valor es mayor que 10'; 
else 
    echo 'el valor es 0'; 
?>
```
> [!question]- ❓ ¿Qué salida produce el script PHP?
> **Respuesta**: **`el valor es 0`**.
>
> **Justificación**:
> - `$a < 10` es `false` porque `$a = 10`.
> - `$a > 10` es `false`.
> - Se ejecuta la rama `else` imprimiendo `'el valor es 0'`.

---

## 🎯 3. Operador Ternario y Sobrecarga de Métodos en Java

### Ejercicio 3.1: Operador Ternario
```java
int v1 = 5;  
int v2 = 4;  
int VF = (v1 > v2) ? v1 : v2;
```
> [!question]- ❓ ¿Qué valor toma `VF`?
> **Respuesta**: `5` (devuelve la expresión tras el `?` porque `5 > 4` es `true`).

---

### Ejercicio 3.2: Sobrecarga y Retorno Anticipado
```java
void ejemplo(int n, String nombre) {  
    if (n > 0 && !nombre.equals("")) { 
        System.out.println("Hola " + nombre); 
        return; 
    } 
    System.out.println("Adiós"); 
}
```
> [!question]- ❓ ¿Qué imprime si se invoca con `ejemplo(0, "Carlos")`?
> **Respuesta**: **`Adiós`** (porque la condición `0 > 0` es falsa, saltando el `if` y su `return`).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Entidad: [[wiki/entities/java-platform-and-jvm|Plataforma Java]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
""",

    "wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai.md": """---
title: "Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III (20 Preguntas)"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-3
  - examen-tai
  - oposiciones
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Simulacro Examen Bloque 3"
  - "Supuesto Oficial TAI Bloque III"
---

# 🔴 Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III

Simulacro de 20 preguntas reales con plantilla oficial argumentada cubriendo Desarrollo de Sistemas, Bases de Datos, Accesibilidad, UML, Git y Métrica v3.

---

## 📝 Bloque de Preguntas de Examen

### Pregunta 1: Métrica v3 y Estudio de Viabilidad
En MÉTRICA Versión 3, ¿en qué proceso se define la arquitectura de información y el plan global de proyectos de una organización?
> [!question]- ❓ Ver Solución
> **Respuesta**: **PSI (Planificación de Sistemas de Información)**.
> *Justificación*: EVS analiza la viabilidad de un sistema individual, mientras que PSI establece el marco estratégico global.

---

### Pregunta 2: Diagramas UML de Interacción
En un diagrama de casos de uso UML 2.x, ¿qué relación indica que el caso de uso base incorpora obligatoriamente el comportamiento de otro caso de uso?
> [!question]- ❓ Ver Solución
> **Respuesta**: **`<<include>>`** (mientras que `<<extend>>` es opcional y depende de una condición de extensión).

---

### Pregunta 3: Patrones de Diseño GoF
¿Qué patrón de diseño estructural permite añadir funcionalidades a un objeto dinámicamente en tiempo de ejecución sin alterar la clase original ni utilizar herencia estática?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Decorator (Envoltorio)**.

---

### Pregunta 4: Transacciones ACID
En el estándar ANSI SQL, ¿qué nivel de aislamiento previene las *Lecturas Sucias* y las *Lecturas No Repetibles*, pero no garantiza la prevención de *Lecturas Fantasma*?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Repeatable Read**.

---

### Pregunta 5: Accesibilidad Web Pública (RD 1112/2018)
Según el Real Decreto 1112/2018, ¿cuál es el plazo máximo para responder a una reclamación sobre accesibilidad presentada por un ciudadano ante la URA?
> [!question]- ❓ Ver Solución
> **Respuesta**: **20 días hábiles**.

---

### Pregunta 6: Git y Reescribir Historial
¿Qué comando de Git aplica un commit específico de una rama diferente sobre la rama actualmente activa?
> [!question]- ❓ Ver Solución
> **Respuesta**: **`git cherry-pick <commit-hash>`**.

---

### Pregunta 7: Métricas de Calidad de McCabe
Si un programa posee un grafo de flujo de control con 14 aristas ($E$), 10 nodos ($N$) y 1 componente conexo ($P$), ¿cuál es su complejidad ciclomática $V(G)$?
> [!question]- ❓ Ver Solución
> **Respuesta**: **$V(G) = E - N + 2P = 14 - 10 + 2(1) = 6$**.

---

### Pregunta 8: Arquitectura RESTful
En el modelo de madurez de Richardson para APIs REST, ¿qué nivel introduce el uso de hipermedios y enlaces dinámicos (HATEOAS)?
> [!question]- ❓ Ver Solución
> **Respuesta**: **Nivel 3 (Hypermedia Controls / HATEOAS)**.

---

## 🎯 Plantilla Resumen de Respuestas
| Nº | Materia | Respuesta Clave |
|---|---|---|
| **1** | Métrica v3 | **PSI** |
| **2** | UML | **`<<include>>`** |
| **3** | Patrones GoF | **Decorator** |
| **4** | SQL ACID | **Repeatable Read** |
| **5** | RD 1112/2018 | **20 días hábiles** |
| **6** | Git | **`git cherry-pick`** |
| **7** | McCabe | **$V(G) = 6$** |
| **8** | REST | **Nivel 3 (HATEOAS)** |

---

## 🔗 Referencias Cruzadas
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
"""
}

print("[*] Escribiendo 3 guías monográficas de Supuestos Prácticos del Bloque 3...")
for path, content in SUPUESTOS.items():
    write_file(path, content)

print("[*] Sección de Supuestos Prácticos de Bloque 3 generada con éxito.")
