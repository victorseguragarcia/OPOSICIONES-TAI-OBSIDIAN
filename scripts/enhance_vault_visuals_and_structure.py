# -*- coding: utf-8 -*-
r"""
Script para transformar la visualización y estructura pedagógica del baúl:
1. Amplía tai-colors.css con callouts especializados (Trampas, Mnemotecnias, Flashcards, Badges, Tablas Zebra).
2. Genera los Canvas individuales interactivos para los 4 Bloques.
3. Sincroniza ambos baúles de Obsidian.
"""
import os
import json
import uuid
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_VAULT_DIR = r"D:\Desktop\TAI OPOSICIONES"

def gen_id():
    return uuid.uuid4().hex[:16]

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

ENHANCED_CSS = """/* ==========================================================================
   TAI Oposiciones - Suite Visual y Estilística Pedagógica
   - 🔴 Nivel 1: Temas Principales / Bloques / Leyes (Coral Pastel: #EF5350 / #E57373)
   - 🟣 Nivel 2: Subtemas / Entidades / Conceptos (Orquídea Pastel: #BA68C8 / #CE93D8)
   - 🔵 Nivel 3: Conocimientos Concretos / Síntesis / Tablas (Azul Cielo: #64B5F6 / #90CAF9)
   - ⚠️ Trampas de Examen (Ámbar / Coral: #FFB74D / #EF5350)
   - 🧠 Mnemotecnias (Esmeralda / Menta: #81C784 / #A5D6A7)
   ========================================================================== */

:root {
  --tai-tema-red: #ef5350;
  --tai-tema-red-soft: #e57373;
  --tai-tema-red-bg: rgba(239, 83, 80, 0.08);
  --tai-tema-red-border: rgba(239, 83, 80, 0.28);

  --tai-subtema-purple: #ba68c8;
  --tai-subtema-purple-soft: #ce93d8;
  --tai-subtema-purple-bg: rgba(186, 104, 200, 0.08);
  --tai-subtema-purple-border: rgba(186, 104, 200, 0.28);

  --tai-concreto-blue: #64b5f6;
  --tai-concreto-blue-soft: #90caf9;
  --tai-concreto-blue-bg: rgba(100, 181, 246, 0.08);
  --tai-concreto-blue-border: rgba(100, 181, 246, 0.28);

  --tai-amber-trampa: #ffb74d;
  --tai-amber-trampa-bg: rgba(255, 183, 77, 0.09);
  --tai-amber-trampa-border: rgba(255, 183, 77, 0.35);

  --tai-green-mnemo: #81c784;
  --tai-green-mnemo-bg: rgba(129, 199, 132, 0.09);
  --tai-green-mnemo-border: rgba(129, 199, 132, 0.35);
}

/* ==========================================================================
   1. ENCABEZADOS Y TIPOGRAFÍA (OBSIDIAN + PREVIEW)
   ========================================================================== */

h1,
.markdown-rendered h1,
.markdown-preview-view h1,
.cm-header-1,
.theme-dark h1,
.theme-light h1,
.vscode-body h1 {
  color: var(--tai-tema-red) !important;
  font-weight: 750 !important;
  border-bottom: 1.5px solid var(--tai-tema-red-border) !important;
  padding-bottom: 6px !important;
  margin-top: 24px !important;
  margin-bottom: 14px !important;
  letter-spacing: -0.01em;
}

h2,
.markdown-rendered h2,
.markdown-preview-view h2,
.cm-header-2,
.theme-dark h2,
.theme-light h2,
.vscode-body h2 {
  color: var(--tai-subtema-purple) !important;
  font-weight: 650 !important;
  border-left: 3.5px solid var(--tai-subtema-purple-soft) !important;
  padding-left: 10px !important;
  margin-top: 20px !important;
  margin-bottom: 12px !important;
}

h3,
.markdown-rendered h3,
.markdown-preview-view h3,
.cm-header-3,
.theme-dark h3,
.theme-light h3,
.vscode-body h3 {
  color: var(--tai-concreto-blue) !important;
  font-weight: 600 !important;
  margin-top: 16px !important;
  margin-bottom: 8px !important;
}

h4,
.markdown-rendered h4,
.markdown-preview-view h4,
.cm-header-4,
.theme-dark h4,
.theme-light h4,
.vscode-body h4 {
  color: #81d4fa !important;
  font-weight: 600 !important;
}

/* ==========================================================================
   2. TABLAS PEDAGÓGICAS CON EFECTO CEBRA Y HOVER
   ========================================================================== */

.markdown-rendered table,
.markdown-preview-view table,
.vscode-body table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid rgba(100, 181, 246, 0.2) !important;
  margin: 16px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.markdown-rendered table th,
.markdown-preview-view table th,
.vscode-body table th {
  background-color: var(--tai-concreto-blue-bg) !important;
  color: var(--tai-concreto-blue) !important;
  border-bottom: 2px solid var(--tai-concreto-blue-border) !important;
  padding: 10px 14px !important;
  font-weight: 650 !important;
  text-align: left;
}

.markdown-rendered table td,
.markdown-preview-view table td,
.vscode-body table td {
  padding: 9px 14px !important;
  border-bottom: 1px solid rgba(120, 120, 120, 0.12) !important;
}

.markdown-rendered table tr:nth-child(even) td,
.markdown-preview-view table tr:nth-child(even) td {
  background-color: rgba(120, 120, 120, 0.035);
}

.markdown-rendered table tr:hover td,
.markdown-preview-view table tr:hover td {
  background-color: rgba(100, 181, 246, 0.06) !important;
  transition: background-color 0.15s ease-in-out;
}

/* ==========================================================================
   3. SUITE DE CALLOUTS ESPECIALIZADOS DE OPOSICIÓN
   ========================================================================== */

.callout[data-callout="tema"],
.callout[data-callout="danger"],
.callout[data-callout="important"] {
  --callout-color: 239, 83, 80;
  border-left: 4px solid var(--tai-tema-red-soft) !important;
  background-color: var(--tai-tema-red-bg) !important;
  border-radius: 6px;
}

.callout[data-callout="subtema"],
.callout[data-callout="example"] {
  --callout-color: 186, 104, 200;
  border-left: 4px solid var(--tai-subtema-purple-soft) !important;
  background-color: var(--tai-subtema-purple-bg) !important;
  border-radius: 6px;
}

.callout[data-callout="concreto"],
.callout[data-callout="note"],
.callout[data-callout="tip"],
.callout[data-callout="info"] {
  --callout-color: 100, 181, 246;
  border-left: 4px solid var(--tai-concreto-blue-soft) !important;
  background-color: var(--tai-concreto-blue-bg) !important;
  border-radius: 6px;
}

.callout[data-callout="trampa"],
.callout[data-callout="warning"] {
  --callout-color: 255, 183, 77;
  border-left: 4px solid var(--tai-amber-trampa) !important;
  background-color: var(--tai-amber-trampa-bg) !important;
  border-radius: 6px;
}

.callout[data-callout="mnemo"],
.callout[data-callout="success"] {
  --callout-color: 129, 199, 132;
  border-left: 4px solid var(--tai-green-mnemo) !important;
  background-color: var(--tai-green-mnemo-bg) !important;
  border-radius: 6px;
}

.callout[data-callout="question"],
.callout[data-callout="test"],
.callout[data-callout="faq"] {
  --callout-color: 149, 117, 205;
  border-left: 4px solid #9575cd !important;
  background-color: rgba(149, 117, 205, 0.08) !important;
  border-radius: 6px;
}

.callout[data-callout="repaso"],
.callout[data-callout="abstract"],
.callout[data-callout="summary"] {
  --callout-color: 77, 208, 225;
  border-left: 4px solid #4dd0e1 !important;
  background-color: rgba(77, 208, 225, 0.08) !important;
  border-radius: 6px;
}

/* ==========================================================================
   4. VISTA GRÁFICA INTERACTIVA (GRAPH VIEW)
   ========================================================================== */

.graph-view.color-fill-1,
.graph-view.color-circle-1 {
  color: var(--tai-tema-red-soft) !important;
  fill: var(--tai-tema-red-soft) !important;
}

.graph-view.color-fill-2,
.graph-view.color-circle-2 {
  color: var(--tai-subtema-purple-soft) !important;
  fill: var(--tai-subtema-purple-soft) !important;
}

.graph-view.color-fill-3,
.graph-view.color-circle-3 {
  color: var(--tai-concreto-blue-soft) !important;
  fill: var(--tai-concreto-blue-soft) !important;
}

/* ==========================================================================
   5. OBSIDIAN CANVAS (LIENZOS VISUALES)
   ========================================================================== */

.canvas-node[data-color="1"],
.canvas-node[data-color="#E53935"],
.canvas-node[data-color="#ef5350"],
.canvas-node[data-color="#e57373"] {
  border-color: var(--tai-tema-red-soft) !important;
  background-color: rgba(239, 83, 80, 0.06) !important;
  border-radius: 8px;
}

.canvas-node[data-color="6"],
.canvas-node[data-color="#8E24AA"],
.canvas-node[data-color="#ba68c8"],
.canvas-node[data-color="#ce93d8"] {
  border-color: var(--tai-subtema-purple-soft) !important;
  background-color: rgba(186, 104, 200, 0.06) !important;
  border-radius: 8px;
}

.canvas-node[data-color="5"],
.canvas-node[data-color="#1E88E5"],
.canvas-node[data-color="#64b5f6"],
.canvas-node[data-color="#90caf9"] {
  border-color: var(--tai-concreto-blue-soft) !important;
  background-color: rgba(100, 181, 246, 0.06) !important;
  border-radius: 8px;
}

/* ==========================================================================
   6. ETIQUETAS (TAGS / BADGES)
   ========================================================================== */

.tag[href*="bloque"],
.tag[href*="tema"] {
  background-color: var(--tai-tema-red-bg) !important;
  color: var(--tai-tema-red-soft) !important;
  border: 1px solid var(--tai-tema-red-border) !important;
  border-radius: 12px;
  padding: 2px 8px;
}

.tag[href*="entity"],
.tag[href*="concept"] {
  background-color: var(--tai-subtema-purple-bg) !important;
  color: var(--tai-subtema-purple-soft) !important;
  border: 1px solid var(--tai-subtema-purple-border) !important;
  border-radius: 12px;
  padding: 2px 8px;
}

.tag[href*="synthesis"],
.tag[href*="cheatsheet"],
.tag[href*="guide"] {
  background-color: var(--tai-concreto-blue-bg) !important;
  color: var(--tai-concreto-blue-soft) !important;
  border: 1px solid var(--tai-concreto-blue-border) !important;
  border-radius: 12px;
  padding: 2px 8px;
}
"""

write_file(".obsidian/snippets/tai-colors.css", ENHANCED_CSS)

parent_snippets_dir = os.path.join(PARENT_VAULT_DIR, ".obsidian", "snippets")
if os.path.exists(parent_snippets_dir):
    with open(os.path.join(parent_snippets_dir, "tai-colors.css"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENHANCED_CSS.strip() + "\n")
    print("    [OK] Sincronizado en D:\\Desktop\\TAI OPOSICIONES\\.obsidian\\snippets\\tai-colors.css")

CANVAS_BLOCKS = [
    {
        "file": "temario-bloque1-administracion.canvas",
        "title": "🏛️ Bloque 1: Administración Pública y Marco Digital (TAI)",
        "color": "#EF5350",
        "nodes": [
            {"title": "🔴 Bloque 1: Normativa General", "text": "## 🔴 Bloque 1: AGE, UE y TREBEP\n- CE 1978 y Derechos Fundamentales\n- Gobierno, AGE y CCAA\n- Instituciones de la UE\n- TREBEP (Situaciones y Régimen Disciplinario)\n- Igualdad y Violencia de Género", "x": -450, "y": -200, "w": 400, "h": 220, "c": "#EF5350"},
            {"title": "🔴 Bloque 1: Administración Digital", "text": "## 🔴 Administración Digital y Datos\n- Ley 39/2015 LPACAP y Ley 40/2015 LRJSP\n- eIDAS, Ley 6/2020 y DNIe\n- Red SARA, Cl@ve, SIR, FACe, INSIDE, ARCHIVE\n- RGPD y LOPDGDD 3/2018 (Derechos Digitales)", "x": 50, "y": -200, "w": 420, "h": 220, "c": "#EF5350"},
            {"file": "wiki/synthesis/bloque1-informatica-y-administracion-digital-master-guide.md", "x": 50, "y": 80, "w": 420, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/servicios-comunes-age-administracion-electronica-cheatsheet.md", "x": 520, "y": 80, "w": 400, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/bloque1-tai-oposiciones-master-guide.md", "x": -450, "y": 80, "w": 400, "h": 240, "c": "#64B5F6"}
        ]
    },
    {
        "file": "temario-bloque2-tecnologia.canvas",
        "title": "💻 Bloque 2: Tecnología Básica y Hardware (TAI)",
        "color": "#EF5350",
        "nodes": [
            {"title": "🔴 Arquitectura y Datos", "text": "## 🔴 Arquitectura, CPU y Datos\n- Von Neumann vs Harvard\n- C2, IEEE 754 (Simple/Doble)\n- ASCII, Latin-9, UTF-8\n- Buses: PCIe 3.0/4.0/5.0, NVMe", "x": -450, "y": -200, "w": 400, "h": 200, "c": "#EF5350"},
            {"title": "🔴 Sistemas Operativos y SGBD", "text": "## 🔴 Sistemas Operativos y BBDD\n- Procesos y Planificación CPU (RR, SJF)\n- Deadlocks (4 Condiciones Coffman)\n- Memoria Virtual (Paginación, TLB, LRU)\n- NoSQL y Teorema CAP (MongoDB, Redis)", "x": 50, "y": -200, "w": 420, "h": 200, "c": "#EF5350"},
            {"file": "wiki/synthesis/bloque2-tai-oposiciones-master-guide.md", "x": -450, "y": 60, "w": 400, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet.md", "x": 50, "y": 60, "w": 420, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/nosql-families-and-cap-theorem-guide.md", "x": 520, "y": 60, "w": 400, "h": 240, "c": "#64B5F6"}
        ]
    },
    {
        "file": "temario-bloque3-desarrollo.canvas",
        "title": "⚙️ Bloque 3: Desarrollo de Sistemas (TAI)",
        "color": "#EF5350",
        "nodes": [
            {"title": "🔴 Metodologías y BBDD", "text": "## 🔴 Metodologías, UML y BBDD\n- MÉTRICA v3 (PSI, EVS, ASI, DSI, CSI, IAS)\n- Scrum (PO/SM/Devs), Kanban (WIP), XP\n- Normalización Relacional (1FN a 5FN, BCNF)\n- ANSI SQL, Triggers, Stored Procedures", "x": -450, "y": -200, "w": 400, "h": 220, "c": "#EF5350"},
            {"title": "🔴 Lenguajes, Arquitectura y QA", "text": "## 🔴 Programación, Web y QA\n- Java EE / JVM vs Microsoft .NET CLR\n- RESTful (HATEOAS) vs SOAP (WSDL/XML)\n- Testing: Caja Blanca (McCabe), Caja Negra\n- Accesibilidad: WCAG 2.1 POUR y RD 1112/2018", "x": 50, "y": -200, "w": 420, "h": 220, "c": "#EF5350"},
            {"file": "wiki/synthesis/bloque3-tai-oposiciones-master-guide.md", "x": -450, "y": 80, "w": 400, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/metrica-v3-processes-and-artifacts-guide.md", "x": 50, "y": 80, "w": 420, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md", "x": 520, "y": 80, "w": 400, "h": 240, "c": "#64B5F6"}
        ]
    },
    {
        "file": "temario-bloque4-sistemas.canvas",
        "title": "🌐 Bloque 4: Sistemas y Comunicaciones (TAI)",
        "color": "#EF5350",
        "nodes": [
            {"title": "🔴 Redes y Protocolos", "text": "## 🔴 Redes, TCP/IP y Seguridad\n- Modelo OSI (7 capas) vs Pila TCP/IP (4 capas)\n- IPv4 Subnetting VLSM y Direccionamiento IPv6\n- Protocolos: DNS, DHCP, HTTP/3 QUIC, TLS 1.3, SNMP\n- Criptografía (RSA, AES, SHA-2/3, Curvas Elípticas)\n- Esquema Nacional de Seguridad (ENS RD 311/2022)", "x": -450, "y": -200, "w": 420, "h": 230, "c": "#EF5350"},
            {"title": "🔴 Administración de Sistemas", "text": "## 🔴 Windows Server, Linux y Cloud\n- Active Directory (Kerberos, FSMO, GPOs)\n- Linux SysAdmin (Systemd, LVM, Bash, SSH)\n- Virtualización (ESXi, KVM, Docker, Kubernetes)\n- Alta Disponibilidad y CPD (TIER I a IV, RAID)", "x": 30, "y": -200, "w": 420, "h": 230, "c": "#EF5350"},
            {"file": "wiki/synthesis/bloque4-tai-oposiciones-master-guide.md", "x": -450, "y": 90, "w": 420, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/network-ports-and-protocols-cheatsheet.md", "x": 30, "y": 90, "w": 420, "h": 240, "c": "#64B5F6"},
            {"file": "wiki/synthesis/windows-server-administration-guide.md", "x": 500, "y": 90, "w": 400, "h": 240, "c": "#64B5F6"}
        ]
    }
]

print("[*] Generando Canvas interactivos por bloque temático...")
for cb in CANVAS_BLOCKS:
    c_nodes = []
    c_edges = []
    
    hub_id = gen_id()
    c_nodes.append({
        "id": hub_id,
        "type": "text",
        "x": -150,
        "y": -380,
        "width": 550,
        "height": 130,
        "color": cb["color"],
        "text": f"# {cb['title']}\n\nMapa interactivo de navegación y estudio visual."
    })
    
    for nd in cb["nodes"]:
        n_id = gen_id()
        if "file" in nd:
            c_nodes.append({
                "id": n_id,
                "type": "file",
                "file": nd["file"],
                "x": nd["x"],
                "y": nd["y"],
                "width": nd["w"],
                "height": nd["h"],
                "color": nd["c"]
            })
        else:
            c_nodes.append({
                "id": n_id,
                "type": "text",
                "x": nd["x"],
                "y": nd["y"],
                "width": nd["w"],
                "height": nd["h"],
                "color": nd["c"],
                "text": nd["text"]
            })
        
        c_edges.append({
            "id": gen_id(),
            "fromNode": hub_id,
            "toNode": n_id,
            "color": nd["c"]
        })
        
    c_data = {"nodes": c_nodes, "edges": c_edges}
    
    out_path = os.path.join(BASE_DIR, cb["file"])
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(c_data, f, indent=2)
    print(f"    [OK] Generado {cb['file']}")
    
    parent_canvas_path = os.path.join(PARENT_VAULT_DIR, cb["file"])
    try:
        with open(parent_canvas_path, "w", encoding="utf-8") as f:
            json.dump(c_data, f, indent=2)
    except Exception:
        pass

print("[*] Visualizaciones y Canvas de Bloques completados exitosamente.")
