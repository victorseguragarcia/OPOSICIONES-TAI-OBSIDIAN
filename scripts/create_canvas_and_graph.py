# -*- coding: utf-8 -*-
"""
Genera el Canvas visual interactivo (temario-tai-visual-map.canvas)
y perfecciona la configuración del Grafo de Obsidian (.obsidian/graph.json).
"""
import os
import json
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def gen_id():
    return uuid.uuid4().hex[:16]

# ==============================================================================
# 1. ACTUALIZAR .obsidian/graph.json
# ==============================================================================
graph_config = {
    "collapse-filter": False,
    "search": "",
    "showTags": True,
    "showAttachments": False,
    "hideUnresolved": False,
    "showOrphans": True,
    "colorGroups": [
        {
            "query": "path:sources",
            "color": {
                "a": 1,
                "rgb": 15022389  # #E53935 Rojo (Temas / Fuentes)
            }
        },
        {
            "query": "path:entities OR path:concepts",
            "color": {
                "a": 1,
                "rgb": 9315498   # #8E24AA Morado (Subtemas / Entidades / Conceptos)
            }
        },
        {
            "query": "path:synthesis",
            "color": {
                "a": 1,
                "rgb": 2001125   # #1E88E5 Azul (Conocimientos Concretos / Síntesis)
            }
        }
    ],
    "linkStrength": 0.8,
    "linkDistance": 120,
    "nodeSizeMultiplier": 1.25,
    "lineSizeMultiplier": 1.0,
    "textFadeMultiplier": 0.5,
    "centerStrength": 0.55
}

os.makedirs(os.path.join(BASE_DIR, ".obsidian"), exist_ok=True)
with open(os.path.join(BASE_DIR, ".obsidian", "graph.json"), "w", encoding="utf-8") as f:
    json.dump(graph_config, f, indent=2)

print("[OK] .obsidian/graph.json actualizado con grupos cromáticos exactos (Rojo, Morado, Azul).")

# ==============================================================================
# 2. GENERAR CANVAS MAESTRO (temario-tai-visual-map.canvas)
# ==============================================================================
nodes = []
edges = []

# Tarjeta Central / Hub
hub_id = gen_id()
nodes.append({
    "id": hub_id,
    "type": "text",
    "x": 0,
    "y": 0,
    "width": 500,
    "height": 220,
    "color": "#E53935",
    "text": "# 🏛️ Temario Oficial TAI (AGE)\n\n**Mapa Mental Jerárquico de Estudio**\n- 🔴 **Temas Principales**: Rojo (`#E53935`)\n- 🟣 **Subtemas / Entidades**: Morado (`#8E24AA`)\n- 🔵 **Datos Concretos / Síntesis**: Azul (`#1E88E5`)"
})

bloques_info = [
    {
        "name": "Bloque 1: Administración Pública y Normativa",
        "color": "#E53935",
        "x": -1100,
        "y": -700,
        "source": "wiki/sources/bloque1-tema01.md",
        "entity": "wiki/entities/constitucion-espanola-1978.md",
        "synthesis": "wiki/synthesis/bloque1-tai-oposiciones-master-guide.md",
        "summary": "10 Temas oficiales: CE 1978, AGE, CCAA, UE, TREBEP, Igualdad, LPACAP 39/2015, LRJSP 40/2015, RGPD, Transparencia."
    },
    {
        "name": "Bloque 2: Tecnología Básica",
        "color": "#E53935",
        "x": 600,
        "y": -700,
        "source": "wiki/sources/bloque2-tema01.md",
        "entity": "wiki/entities/cpu-architecture-von-neumann.md",
        "synthesis": "wiki/synthesis/bloque2-tai-oposiciones-master-guide.md",
        "summary": "5 Temas oficiales: CPU Von Neumann, RAM/Caché, USB/PCIe/NVMe, C2, IEEE 754, Unicode, Algoritmos Big-O, Sistemas Archivos."
    },
    {
        "name": "Bloque 3: Desarrollo de Sistemas",
        "color": "#E53935",
        "x": -1100,
        "y": 450,
        "source": "wiki/sources/bloque3-tema01.md",
        "entity": "wiki/entities/metrica-v3-methodology.md",
        "synthesis": "wiki/synthesis/bloque3-tai-oposiciones-master-guide.md",
        "summary": "9 Temas oficiales: Normalización/SQL, Métrica v3, Scrum, UML 2.x, Patrones GoF, Java/JVM, .NET, REST/SOAP, Testing/McCabe, WCAG."
    },
    {
        "name": "Bloque 4: Sistemas y Comunicaciones",
        "color": "#E53935",
        "x": 600,
        "y": 450,
        "source": "wiki/sources/bloque4-tema01.md",
        "entity": "wiki/entities/windows-server.md",
        "synthesis": "wiki/synthesis/bloque4-tai-oposiciones-master-guide.md",
        "summary": "10 Temas oficiales: Windows Server, Linux, Virtualización, DBA, Redes OSI/TCP-IP, IPv4/IPv6, Protocolos, Criptografía, ENS/Magerit."
    }
]

for b in bloques_info:
    # 1. Nodo del Bloque (Rojo)
    b_id = gen_id()
    nodes.append({
        "id": b_id,
        "type": "text",
        "x": b["x"],
        "y": b["y"],
        "width": 420,
        "height": 180,
        "color": "#E53935",
        "text": f"## 🔴 {b['name']}\n\n{b['summary']}"
    })
    
    # Conexión Hub -> Bloque
    edges.append({
        "id": gen_id(),
        "fromNode": hub_id,
        "toNode": b_id,
        "color": "#E53935"
    })
    
    # 2. Nodo de Subtema / Entidad (Morado)
    e_id = gen_id()
    nodes.append({
        "id": e_id,
        "type": "file",
        "file": b["entity"],
        "x": b["x"] + 460,
        "y": b["y"] - 30,
        "width": 380,
        "height": 220,
        "color": "#8E24AA"
    })
    
    edges.append({
        "id": gen_id(),
        "fromNode": b_id,
        "toNode": e_id,
        "color": "#8E24AA",
        "label": "🟣 Subtemas / Entidades"
    })
    
    # 3. Nodo de Síntesis / Conocimientos Concretos (Azul)
    s_id = gen_id()
    nodes.append({
        "id": s_id,
        "type": "file",
        "file": b["synthesis"],
        "x": b["x"] + 460,
        "y": b["y"] + 210,
        "width": 380,
        "height": 220,
        "color": "#1E88E5"
    })
    
    edges.append({
        "id": gen_id(),
        "fromNode": b_id,
        "toNode": s_id,
        "color": "#1E88E5",
        "label": "🔵 Guías / Datos Concretos"
    })

canvas_data = {
    "nodes": nodes,
    "edges": edges
}

canvas_path = os.path.join(BASE_DIR, "temario-tai-visual-map.canvas")
with open(canvas_path, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, indent=2)

print(f"[OK] Canvas generado: temario-tai-visual-map.canvas ({len(nodes)} nodos, {len(edges)} conexiones).")
