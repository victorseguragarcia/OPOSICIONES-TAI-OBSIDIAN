# 🏛️ LLM Wiki: Preparación Integral Oposiciones TAI (AGE)

> **Base de Conocimiento Persistente, Grafo de Estudio y Banco de Autoevaluación**  
> Diseñado según la arquitectura **LLM Wiki Pattern** para el Cuerpo de **Técnicos Auxiliares de Informática (TAI)** de la Administración General del Estado.

---

## 📌 Descripción del Proyecto

Este repositorio constituye un **ecosistema de estudio interactivo y estructurado** que transforma el temario oficial de las oposiciones TAI en un grafo de conocimiento hiperconectado en formato Markdown, optimizado para su visualización y navegación en **Obsidian** y entornos IDE.

El proyecto sigue el **patrón LLM Wiki** (inspirado en la arquitectura de Andrej Karpathy), donde la IA actúa como compilador/mantenedor continuo del conocimiento, Obsidian como IDE visual de estudio, y el repositorio Markdown como la base de conocimiento incremental y persistente.

---

## 📊 Métricas y Estado del Repositorio

- **Archivos Markdown Analizados e Interconectados**: `213+ notas`
- **Fuentes Oficiales Ingeridas y Resumidas**: `35 temas oficiales`
- **Fichas Técnicas de Entidades y Conceptos**: `113 fichas`
- **Guías Maestras de Síntesis y Cheatsheets**: `50 guías monográficas`
- **Supuestos Prácticos y Simulacros de Examen**: `3 cuadernos de supuestos + banco de tests`
- **Lienzos Visuales Interactivos (Obsidian Canvas)**: `5 mapas Canvas`
- **Integridad del Grafo**: `100% verificado (0 enlaces rotos, 0 notas huérfanas)`

---

## 🗺️ Mapa de los 4 Bloques Temáticos

```
                                TEMARIO OFICIAL TAI (AGE)
                                            │
       ┌────────────────────┬───────────────┴───────────────┬────────────────────┐
       ▼                    ▼                               ▼                    ▼
   🔴 BLOQUE 1          🔴 BLOQUE 2                     🔴 BLOQUE 3          🔴 BLOQUE 4
Organización del     Tecnología Básica               Desarrollo de       Sistemas y Redes
Estado y Normativa   Hardware, SO y SGBD             Sistemas y Web      Comunicaciones y ENS
 • CE 1978 y AGE      • C2, IEEE 754, Unicode         • Normalización     • Pila OSI y TCP/IP
 • LPACAP y LRJSP     • PCIe, NVMe, USB4              • UML 2.x y GoF     • Subnetting IPv4/IPv6
 • TREBEP y Personal  • Algoritmos Big-O              • Java / .NET       • Windows Server / AD
 • Red SARA y eIDAS   • Planificación CPU y Memoria   • REST vs SOAP      • Linux y SysAdmin
 • RGPD / LOPDGDD     • NoSQL y Teorema CAP           • MÉTRICA v3 y QA   • Seguridad y ENS RD 311
```

---

## 🎨 Jerarquía Cromática de Estudio (`tai-colors.css`)

Para maximizar la memoria visual y la retención activa, todo el repositorio sigue un sistema de diseño visual con colores pastel y callouts pedagógicos personalizados:

| Nivel / Elemento | Color / Tonalidad | Significado y Uso en las Notas |
|:---|:---|:---|
| 🔴 **Nivel 1 (H1 / Bloques)** | **Coral Pastel** (`#EF5350`) | Títulos de bloques, leyes principales y portadas maestras. |
| 🟣 **Nivel 2 (H2 / Subtemas)** | **Orquídea Pastel** (`#BA68C8`) | Entidades técnicas, normas específicas y clasificaciones. |
| 🔵 **Nivel 3 (H3 / Tablas)** | **Azul Cielo** (`#64B5F6`) | Datos concretos de examen: puertos, RFCs, artículos, plazos y fórmulas. |
| ⚠️ **`> [!trampa]`** | **Ámbar** (`#FFB74D`) | **Trampas típicas de examen** y distractores habituales en preguntas test. |
| 🧠 **`> [!mnemo]`** | **Menta** (`#81C784`) | **Reglas mnemotécnicas** de memorización rápida. |
| ❓ **`> [!question]-`** | **Lavanda** (`#9575CD`) | **Preguntas test desplegables** (Active Recall con solución oculta). |
| ⚡ **`> [!repaso]`** | **Cian** (`#4DD0E1`) | **Resumen en 30 segundos** de puntos clave. |

---

## 📁 Estructura del Repositorio

```
.
├── raw/                         # Fuentes brutas originales e inmutables (PDFs oficiales)
│   ├── bloque 1/                # 9 PDFs oficiales Bloque 1 (Constitución, AGE, eIDAS, RGPD)
│   ├── bloque 2/                # 5 PDFs oficiales Bloque 2 (Hardware, SO, SGBD, Algoritmos)
│   ├── bloque 3/                # 9 PDFs oficiales Bloque 3 (MÉTRICA v3, UML, Java, Web, QA)
│   ├── bloque 3 SUPUESTOS/      # 6 PDFs oficiales de Supuestos Prácticos de Examen
│   ├── bloque 4/                # 10 PDFs oficiales Bloque 4 (Redes, Sistemas, Seguridad)
│   └── sources/                 # Texto extraído y estructurado de los PDFs
│
├── wiki/                        # Base de conocimiento persistente mantenida por el agente
│   ├── sources/                 # Resúmenes analíticos estructurados de cada tema (35 temas)
│   ├── entities/                # Fichas de herramientas, leyes, hardware y estándares (72)
│   ├── concepts/                # Fundamentos teóricos, modelos y arquitecturas (41)
│   ├── synthesis/               # Guías maestras, tablas comparativas y supuestos resueltos (50)
│   └── tests/                   # Banco de autoevaluación interactivo
│       ├── bloques/             # Simulacros globales de examen por bloques completos
│       └── temas/               # Tests temáticos unitarios con soluciones argumentadas
│
├── templates/                   # Plantillas oficiales para la generación de nuevos contenidos
│   ├── test-tema.md             # Plantilla de tests unitarios de autoevaluación
│   └── test-bloque.md           # Plantilla de simulacros de bloque
│
├── tutorials/                   # Guías paso a paso del flujo de trabajo LLM Wiki (01 a 07)
├── scripts/                     # Automatización, linter, indexación y motor de búsqueda
│   ├── query.py                 # Buscador de alta precisión por relevancia en consola
│   ├── lint.py                  # Linter de integridad de grafo, enlaces rotos y frontmatter
│   ├── rebuild_catalog.py       # Reconstructor automático de index.md y log.md
│   ├── deep_filesystem_audit.py # Auditoría integral del sistema de archivos
│   └── test_tutorials.py        # Suite de pruebas automatizadas del wiki
│
├── .obsidian/                   # Configuración del espacio de trabajo en Obsidian
│   ├── snippets/tai-colors.css  # Snippet CSS de estilos y callouts de oposición
│   └── graph.json               # Configuración cromática de la Vista Gráfica
│
├── index.md                     # Catálogo maestro categorizado de toda la base de conocimiento
├── log.md                       # Registro cronológico inmutable de operaciones
├── AGENTS.md                    # Esquema de reglas y directivas del agente LLM
└── README.md                    # Este documento
```

---

## 🗺️ Lienzos Interactivos (Obsidian Canvas)

El repositorio incluye 5 lienzos gráficos para explorar el temario de forma visual:

1. 🌐 [**`temario-tai-visual-map.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-tai-visual-map.canvas): Mapa global con los 4 bloques interconectados.
2. 🏛️ [**`temario-bloque1-administracion.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque1-administracion.canvas): Bloque 1 (CE, AGE, LPACAP, LRJSP, Red SARA, Cl@ve, eIDAS, LOPDGDD).
3. 💻 [**`temario-bloque2-tecnologia.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque2-tecnologia.canvas): Bloque 2 (Hardware, C2, IEEE 754, Algoritmos Big-O, SO, Paginación, NoSQL).
4. ⚙️ [**`temario-bloque3-desarrollo.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque3-desarrollo.canvas): Bloque 3 (MÉTRICA v3, Scrum, Normalización BBDD, SQL, UML, Java/.NET, QA).
5. 🌐 [**`temario-bloque4-sistemas.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque4-sistemas.canvas): Bloque 4 (Redes OSI/TCP-IP, Subnetting IPv4/IPv6, Windows Server, Linux, ENS).

---

## 🚀 Guía de Uso y Comandos CLI

### 1. Consultar la Base de Conocimiento (Búsqueda Rápida)
```bash
python scripts/query.py "Red SARA SIR GEISER Cl@ve"
python scripts/query.py "Teorema CAP Brewer MongoDB"
python scripts/query.py "Complejidad Ciclomatica McCabe"
```

### 2. Ejecutar el Linter y Validación de Integridad
```bash
python scripts/lint.py
```

### 3. Reconstruir el Catálogo Maestro (`index.md`)
```bash
python scripts/rebuild_catalog.py
```

### 4. Auditoría Completa del Sistema de Archivos
```bash
python scripts/deep_filesystem_audit.py
```

### 5. Ejecutar la Suite de Pruebas Automatizadas
```bash
python scripts/test_tutorials.py
```

---

## 🎓 Metodología de Estudio Recomendada

1. **Visión Global**: Abrir [`index.md`](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/index.md) o el lienzo Canvas del bloque correspondiente.
2. **Estudio Teórico**: Leer el resumen del tema en `wiki/sources/` y profundizar en las entidades y conceptos enlazados (`[[...]]`).
3. **Consolidación**: Repasar las Guías Maestras de Síntesis y Cheatsheets en `wiki/synthesis/` para memorizar tablas, plazos, puertos y artículos.
4. **Casos Prácticos**: Resolver los cuadernos de supuestos resueltos (Normalización de BBDD, Trazas de Código Java/PHP y Simulacros Oficiales).
5. **Autoevaluación**: Realizar los cuestionarios de preguntas test en `wiki/tests/temas/` y `wiki/tests/bloques/` con verificación de soluciones ocultas.

---

## 📜 Licencia y Autoría
Proyecto de preparación técnica y sistematización de conocimientos para el **Cuerpo de Técnicos Auxiliares de Informática (TAI) de la Administración General del Estado (AGE)**.
