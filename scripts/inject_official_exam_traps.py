# -*- coding: utf-8 -*-
r"""
Script para inyectar Callouts de Trampas Oficiales del Tribunal (> [!trampa])
en todos los temas teóricos clave de los Bloques 1, 2, 3 y 4.
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

def enrich_note_with_trap(rel_path, trap_md):
    fp = REPO_DIR / rel_path
    if not fp.exists():
        print(f"  [Skip / Not found] {rel_path}")
        return
    content = fp.read_text(encoding="utf-8")
    # Arreglar posibles escapes \r en mnemotecnias
    content = content.replace("$\n\tightarrow$", " $\\rightarrow$ ").replace("$\n ightarrow$", " $\\rightarrow$ ")
    
    if trap_md.strip().split("\n")[0] in content:
        print(f"  [Already present] {rel_path}")
        return
    
    # Inyectar antes de la sección de Entidades y Conceptos Asociados o al final
    if "## 🔵 4. Entidades" in content:
        parts = content.split("## 🔵 4. Entidades")
        new_content = parts[0].rstrip() + "\n\n" + trap_md.strip() + "\n\n## 🔵 4. Entidades" + parts[1]
    elif "## 🔵 3. Entidades" in content:
        parts = content.split("## 🔵 3. Entidades")
        new_content = parts[0].rstrip() + "\n\n" + trap_md.strip() + "\n\n## 🔵 3. Entidades" + parts[1]
    else:
        new_content = content.rstrip() + "\n\n" + trap_md.strip() + "\n"
        
    fp.write_text(new_content, encoding="utf-8")
    print(f"  [OK Injected Trap Callout] {rel_path}")

print("=" * 70)
print("⚠️ INYECTANDO TRAMPAS OFICIALES DEL TRIBUNAL EN EL TEMARIO")
print("=" * 70)

# =============================================================================
# BLOQUE 1: TRAMPAS DE EXAMEN
# =============================================================================

enrich_note_with_trap(
    "wiki/sources/bloque1-tema01.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Constitución de 1978
> 1. **Entrada en vigor**: La CE **NO** entró en vigor el 6 de diciembre (referéndum) ni el 27 de diciembre (sanción real), sino el **29 de diciembre de 1978** (el mismo día de su publicación en el BOE).
> 2. **Refrendo de la investidura (Art. 64.1)**: La propuesta y el nombramiento del Presidente del Gobierno los refrenda el **Presidente del Congreso de los Diputados** (NUNCA el Presidente del Senado ni el saliente).
> 3. **Recurso de Amparo (Art. 53.2)**: Protege el **Art. 14**, la **Sección 1ª del Cap. II (Arts. 15 a 29)** y la **Objeción de Conciencia (Art. 30.2)**. Los derechos de la Sección 2ª (propiedad, trabajo, etc.) y los principios rectores (Cap. III) **NO** tienen recurso de amparo.
> 4. **Reforma Agravada (Art. 168)**: Requiere mayoría de **2/3 de cada Cámara**, disolución inmediata de Cortes, ratificación por las nuevas Cámaras elegidas por mayoría de 2/3 y **referéndum preceptivo obligatorio**.
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque1-tema02.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Gobierno y AGE
> 1. **Composición del Gobierno (Art. 1.2 Ley 50/1997)**: El Gobierno se compone del Presidente, Vicepresidentes y Ministros. Los **Secretarios de Estado NO forman parte del Gobierno**, aunque sí son altos cargos y asisten a la Comisión General de Secretarios de Estado y Subsecretarios.
> 2. **Secretario del Consejo de Ministros (Art. 5.2 Ley 50/1997)**: El Secretario es el **Ministro de la Presidencia** (no el Subsecretario de la Presidencia).
> 3. **Cuestión de Confianza vs Moción de Censura**: La moción de censura exige **Mayoría Absoluta** del Congreso (176); la cuestión de confianza se aprueba por **Mayoría Simple** (más votos a favor que en contra).
> 4. **Subdirector General (Art. 55 y 67 Ley 40/2015)**: Es el único órgano directivo que **NO es Alto Cargo** y se nombra por Orden Ministerial (no por Real Decreto).
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque1-tema05.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: TREBEP y Personal
> 1. **Diferencia de Plazo en Prescripciones Leves (Art. 97)**: La falta leve prescribe a los **6 meses**, pero la sanción leve prescribe al **1 año**. *(Muy graves: 3 años / 3 años; Graves: 2 años / 2 años)*.
> 2. **Límite Temporal del Funcionario Interino por Vacante (Art. 10.1.a)**: Las plazas vacantes ocupadas por interinos **no pueden superar los 3 años**; transcurrido este plazo debe producirse el cese del interino y la plaza debe salir a oferta de empleo público.
> 3. **Reserva de Potestades Públicas (Art. 9.2)**: El ejercicio de funciones que impliquen la participación directa o indirecta en el ejercicio de las potestades públicas o en la salvaguardia de los intereses generales del Estado corresponden **exclusivamente a los funcionarios públicos** (vetado al personal laboral).
> 4. **Excedencia por Interés Particular (Art. 89.2)**: Requiere haber prestado servicios efectivos en cualquiera de las AAPP durante un periodo mínimo de **5 años** inmediatamente anteriores.
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque1-tema07.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: LPACAP (Ley 39/2015)
> 1. **Días Hábiles vs Días Naturales**: En notificaciones electrónicas (Art. 43.2), se entiende rechazada a los **10 días naturales** sin acceder; pero el plazo para subsanar solicitudes (Art. 68.1) es de **10 días hábiles**.
> 2. **Cómputo de Sábados (Art. 30.2)**: Desde la entrada en vigor de la Ley 39/2015, los **sábados son días inhábiles** en vía administrativa.
> 3. **Plazos por Meses (Art. 30.4)**: Se computan de **fecha a fecha** a partir del día siguiente a la notificación. Si el mes de vencimiento no tiene día equivalente, expira el **último día del mes**.
> 4. **Doble Silencio Positivo (Art. 24.1)**: La falta de resolución de un Recurso de Alzada interpuesto contra la desestimación por silencio administrativo de una solicitud produce **silencio positivo** (salvo en las 4 materias tasadas: petición, dominio público, medio ambiente y responsabilidad patrimonial).
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque1-tema09.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Protección de Datos (RGPD y LOPDGDD)
> 1. **Edad de consentimiento del menor (Art. 7 LOPDGDD)**: En España es a partir de los **14 años** (el RGPD permitía entre 13 y 16, y España fijó 14).
> 2. **Plazo de Notificación de Brechas a la AEPD (Art. 33 RGPD)**: Plazo máximo de **72 horas** a más tardar desde que el responsable tenga constancia de ella.
> 3. **Sanciones a las Administraciones Públicas (Art. 77 LOPDGDD)**: La AEPD **NO impone multas económicas** al Sector Público; sanciona mediante apercibimiento e incoación de expediente disciplinario a los responsables.
> 4. **Plazo de respuesta derechos ARSOPOL (Art. 12.3 RGPD)**: **1 mes** con carácter general (prorrogable en otros 2 meses en casos de complejidad justificada).
"""
)

# =============================================================================
# BLOQUE 2: TRAMPAS DE EXAMEN
# =============================================================================

enrich_note_with_trap(
    "wiki/sources/bloque2-tema01.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Informática Básica y C2
> 1. **Rango de Complemento a 2**: En $n$ bits el rango es $[-2^{n-1}, +(2^{n-1}-1)]$. Para 8 bits: $[-128, +127]$. Ojo: el valor $-128$ se representa como `10000000` y **no tiene equivalente positivo en 8 bits** (desbordamiento / *overflow* si se intenta negar).
> 2. **Sesgo IEEE 754**: En simple precisión (32 bits), el sesgo es **127** ($2^{8-1}-1$). El exponente almacenado es $E = e + 127$. Los exponentes $E=0$ (números desnormalizados/cero) y $E=255$ (infinito/NaN) están reservados.
> 3. **Bit Implícito**: En números normalizados IEEE 754, la mantisa siempre comienza por `1.` que **NO se almacena** en los 23 bits de fracción, ganando 1 bit extra de precisión efectiva (24 bits totales).
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque2-tema04.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Sistemas Operativos y Memoria
> 1. **Anomalía de Bélády**: Aumentar el número de marcos de página en memoria física **PUEDE aumentar el número de fallos de página** en el algoritmo **FIFO**. Ojo: los algoritmos de pila como **LRU y Óptimo (OPT) son inmunes** a la anomalía de Bélády.
> 2. **Fragmentación Interna vs Externa**: La paginación sufre únicamente de **fragmentación interna** (en la última página asignada); la segmentación tradicional sufre de **fragmentación externa**.
> 3. **Inanición (*Starvation*)**: Ocurre en **SJF (Shortest Job First)** y en algoritmos por prioridades estrictas si llegan continuamente procesos cortos; se soluciona mediante la técnica de **envejecimiento (*aging*)**.
"""
)

# =============================================================================
# BLOQUE 3: TRAMPAS DE EXAMEN
# =============================================================================

enrich_note_with_trap(
    "wiki/sources/bloque3-tema01.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Normalización de Bases de Datos
> 1. **Diferencia Crítica entre 3FN y BCNF (Boyce-Codd)**: En 3FN se permite que para una dependencia funcional $X \rightarrow A$, si $X$ no es superclave, $A$ sea un **atributo primo** (parte de alguna clave candidata). En **BCNF NO HAY EXCEPCIONES**: **TODO determinante $X$ debe ser obligatoriamente una superclave**.
> 2. **2FN (Segunda Forma Normal)**: Exige estar en 1FN y que **no existan dependencias funcionales parciales** (los atributos no primos deben depender de la TOTALIDAD de la clave primaria, no de una parte). Ojo: Si la clave primaria es simple (de 1 solo atributo), la tabla en 1FN **está automáticamente en 2FN**.
> 3. **4FN (Cuarta Forma Normal)**: Elimina las **dependencias multivaluadas (DMV)** no triviales ($X \twoheadrightarrow Y$).
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque3-tema09.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: MÉTRICA v3 y QA
> 1. **Fórmula de Complejidad Ciclomática de McCabe**:
>    $$V(G) = E - N + 2P$$
>    Donde $E$ = Número de aristas, $N$ = Número de nodos, $P$ = Componentes conexos (para un programa simple $P=1 \implies V(G) = E - N + 2$).
>    También es igual a: $V(G) = \text{Regiones del grafo plano} = \text{Nodos predicado (condiciones simples)} + 1$.
> 2. **Procesos de MÉTRICA v3**:
>    - **EVS**: Estudio de Viabilidad del Sistema.
>    - **ASI**: Análisis del Sistema de Información.
>    - **DSI**: Diseño del Sistema de Información (incluye diseño de interfaz y arquitectura física).
>    - **CSI**: Construcción del Sistema de Información (codificación, pruebas unitarias y de integración).
>    - **IAS**: Implantación y Aceptación del Sistema (pruebas de aceptación y paso a producción).
>    - **MSI**: Mantenimiento del Sistema de Información.
"""
)

# =============================================================================
# BLOQUE 4: TRAMPAS DE EXAMEN
# =============================================================================

enrich_note_with_trap(
    "wiki/sources/bloque4-tema07.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: Redes y Subnetting
> 1. **Número de Hosts Útiles en IPv4**: Siempre es **$2^{h} - 2$** (se restan 2: la dirección de red donde todos los bits de host son `0` y la de broadcast donde todos son `1`).
>    *Ejemplo: En una máscara `/27` ($32 - 27 = 5$ bits de host), los hosts útiles son $2^5 - 2 = 30$ hosts*.
> 2. **Broadcast en IPv6**: **En IPv6 NO EXISTE EL BROADCAST**. Se sustituye por tráfico **Multicast** y **Anycast**.
> 3. **Cabecera IPv4 vs IPv6**: La cabecera IPv4 tiene longitud variable (20 a 60 bytes); la cabecera base de IPv6 tiene **longitud fija obligatoria de 40 bytes**, utilizando cabeceras de extensión encadenadas (*Next Header*).
> 4. **Dirección Loopback**: IPv4 es `127.0.0.1/8`; en IPv6 es estrictamente `::1/128`.
"""
)

enrich_note_with_trap(
    "wiki/sources/bloque4-tema09.md",
    """
> [!trampa] ⚠️ Trampas Frecuentes de Examen: ENS RD 311/2022 y Criptografía
> 1. **Las 5 Dimensiones de Seguridad del ENS (Regla DADIT)**: **D**isponibilidad, **A**utenticidad, **I**ntegridad, **C**onfidencialidad (o D), **T**razabilidad. Ojo: La 'C' es Confidencialidad y la 'T' es Trazabilidad.
> 2. **Categorización del Sistema en el ENS**: La categoría del sistema (BÁSICA, MEDIA, ALTA) se determina por la **regla del máximo**: la categoría global del sistema es la de la dimensión que haya obtenido el nivel MÁS ALTO.
> 3. **Firma Digital (Criptografía Asimétrica)**: La firma digital se genera cifrando el hash del mensaje con la **CLAVE PRIVADA del emisor** (garantiza autenticidad y no repudio); y se verifica descifrando con la **CLAVE PÚBLICA del emisor**.
> 4. **Diferencia entre Firma Avanzada y Firma Cualificada (eIDAS)**: La Firma Cualificada es una firma avanzada creada mediante un dispositivo cualificado de creación de firmas (QSCD / DNIe) y basada en un certificado cualificado. **Es la única que tiene efecto jurídico equivalente a la firma manuscrita en toda la UE**.
"""
)

print("\n[*] Inyección de trampas oficiales finalizada con éxito.")
