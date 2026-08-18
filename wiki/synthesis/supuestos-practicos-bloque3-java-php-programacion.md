---
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
> 1. $i=1$: Impar $\rightarrow$ a = 5 + 1 = 6$. Imprime `1,6 `. En la misma línea $i$ se incrementa con `i++` pasando a valer $2$. El `for` hace `i++`, pasando a $3$.
> 2. $i=3$: Impar $\rightarrow$ a = 6 + 3 = 9$. Imprime `3,9 `. $i$ pasa a $4$ con `i++`, y a $5$ con el `for`.
> 3. $i=5$: Impar $\rightarrow$ a = 9 + 5 = 14$. Imprime `5,14 `. $i$ pasa a $6$, y a $7$ con el `for`.
> 4. $i=7$: Impar $\rightarrow$ a = 14 + 7 = 21$. Imprime `7,21 `. Como $a > 20$ ($21 > 20$), ejecuta `break` y sale.
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
