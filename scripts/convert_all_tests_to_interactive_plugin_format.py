# -*- coding: utf-8 -*-
r"""
Script de conversión masiva de todos los tests de la Wiki TAI
a la estructura nativa interactiva del plugin 'obsidian-tai-quiz' (```tai-quiz JSON).
"""
import os
import re
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

def parse_markdown_test(md_text, file_title):
    # 1. Extraer frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", md_text, flags=re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = fm_match.group(2)
    else:
        frontmatter = ""
        body = md_text

    # 2. Extraer solucionario y explicaciones del final si existen
    answers_map = {}
    explanations_map = {}

    # Buscar plantilla de respuestas (ej: "1. b | 2. c" o "1: b" o tablas "| 1 | c |")
    table_answers = re.findall(r"\|\s*(\d+)\s*\|\s*(?:<span[^>]*>)?([a-dA-D])(?:</span>)?\s*\|", body)
    if table_answers:
        for q_num, ans in table_answers:
            answers_map[int(q_num)] = ans.lower()
    else:
        list_answers = re.findall(r"(?:^|\s|\*\*)(\d+)[\.\:\)]\s*\**([a-dA-D])\**", body)
        for q_num, ans in list_answers:
            answers_map[int(q_num)] = ans.lower()

    # Buscar explicaciones
    expl_blocks = re.findall(r"- \*\*Pregunta (\d+)[^\*]*\*\*:\s*([^\n\r]+)", body)
    for q_num, expl in expl_blocks:
        explanations_map[int(q_num)] = expl.strip()
    
    # También buscar justificaciones tipo "- **P1 (c)**: Explicación"
    p_expl = re.findall(r"- \*\*P(\d+)[^\*]*\*\*:\s*([^\n\r]+)", body)
    for q_num, expl in p_expl:
        explanations_map[int(q_num)] = expl.strip()

    # 3. Extraer preguntas y opciones
    # Las preguntas suelen empezar con "### 1. ¿..." o "### 1. Texto"
    questions = []
    q_chunks = re.split(r"###\s*(\d+)[\.\:]\s*", body)
    
    if len(q_chunks) > 1:
        # q_chunks[0] es texto previo, luego viene [num1, text1, num2, text2, ...]
        for i in range(1, len(q_chunks), 2):
            q_num = int(q_chunks[i])
            q_content = q_chunks[i+1]
            
            # La primera línea es el enunciado de la pregunta
            lines = [l.strip() for l in q_content.strip().split("\n") if l.strip()]
            if not lines:
                continue
            
            q_text = lines[0]
            # Extraer opciones tipo "- [ ] a) Opción" o "a) Opción"
            options = []
            for l in lines[1:]:
                if l.startswith("###") or l.startswith("> [!question]"):
                    break
                opt_match = re.match(r"^(?:-\s*\[\s*\]\s*)?[a-dA-D]\)\s*(.*)", l)
                if opt_match:
                    options.append(opt_match.group(1).strip())

            # Respuesta correcta y explicación
            correct_ans = answers_map.get(q_num, "a")
            explanation = explanations_map.get(q_num, f"Respuesta correcta: opción ({correct_ans.upper()}).")

            if options:
                questions.append({
                    "question": q_text,
                    "options": options,
                    "answer": correct_ans,
                    "explanation": explanation
                })

    return frontmatter, questions

print("=" * 70)
print("🔄 CONVIRTIENDO TODOS LOS TESTS AL FORMATO INTERACTIVO NATIVO (```tai-quiz)")
print("=" * 70)

TEST_DIRS = [REPO_DIR / "wiki" / "tests" / "temas", REPO_DIR / "wiki" / "tests" / "bloques"]
converted_count = 0

for t_dir in TEST_DIRS:
    if not t_dir.exists():
        continue
    for test_file in t_dir.glob("*.md"):
        if test_file.name in ["index-tests-bloques.md", "index-tests-temas.md", "simulador-interactivo-plugin-tai.md"]:
            continue
        
        raw_text = test_file.read_text(encoding="utf-8")
        title_match = re.search(r'title:\s*"(.*?)"', raw_text)
        file_title = title_match.group(1) if title_match else test_file.stem
        
        frontmatter, questions = parse_markdown_test(raw_text, file_title)
        
        if not questions:
            print(f"  [Skip / No questions parsed] {test_file.name}")
            continue

        quiz_json = {
            "title": file_title,
            "questions": questions
        }
        
        json_str = json.dumps(quiz_json, indent=2, ensure_ascii=False)
        
        new_content = f"""---
{frontmatter}
---

# 🔴 {file_title}

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{json_str}
```
"""
        test_file.write_text(new_content.strip() + "\n", encoding="utf-8")
        converted_count += 1
        print(f"  [OK Interactive] {test_file.relative_to(REPO_DIR)} ({len(questions)} preguntas)")

# Sincronizar directorio de tests con el baúl superior
for d in ["wiki/tests"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado directorio en baúl superior: {d}")

print(f"\n[*] Conversión masiva finalizada. {converted_count} tests convertidos a formato interactivo.")
