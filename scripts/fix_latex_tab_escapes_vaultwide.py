# -*- coding: utf-8 -*-
r"""
Script para escanear y corregir cualquier tabulador \t corrupto en fórmulas LaTeX
(\text, \times, \to, \theta, etc.) en todo el baúl Obsidian.
"""
import os
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

print("=" * 70)
print("🧹 CORRIGIENDO SECUENCIAS LATEX CORRUPTAS POR TABULADORES EN TODO EL BAÚL")
print("=" * 70)

fixed_files = 0

for root, dirs, files in os.walk(REPO_DIR / "wiki"):
    for file in files:
        if not file.endswith(".md"):
            continue
        fp = Path(root) / file
        content = fp.read_text(encoding="utf-8")
        original = content
        
        # Corregir tabuladores en comandos LaTeX comunes
        content = content.replace("\text", "\\text")
        content = content.replace("\times", "\\times")
        content = content.replace("\to", "\\to")
        content = content.replace("\theta", "\\theta")
        content = content.replace("\tau", "\\tau")
        content = content.replace("\top", "\\top")
        content = content.replace("\tilde", "\\tilde")
        content = content.replace("\tan", "\\tan")
        content = content.replace("\pmod", "\\pmod")
        content = content.replace("\mu", "\\mu")
        content = content.replace("\le", "\\le")
        content = content.replace("\ge", "\\ge")
        content = content.replace("\ne", "\\ne")
        content = content.replace("\in", "\\in")
        content = content.replace("\pm", "\\pm")
        content = content.replace("\infty", "\\infty")
        content = content.replace("\approx", "\\approx")
        content = content.replace("\log", "\\log")
        content = content.replace("\rightarrow", "\\rightarrow")
        content = content.replace("\twoheadrightarrow", "\\twoheadrightarrow")
        
        # Corregir tabuladores literales seguidos de 'ext{' o 'imes'
        content = re.sub(r"\text\{", r"\\text{", content)
        content = re.sub(r"\times\s*", r"\\times ", content)
        content = re.sub(r"\tExt\s+", r"\\text{ a } ", content)
        
        if content != original:
            fp.write_text(content, encoding="utf-8")
            fixed_files += 1
            print(f"  [Fixed LaTeX] {fp.relative_to(REPO_DIR)}")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki"
dst = PARENT_DIR / "wiki"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print(f"\n[*] Limpieza completada. Total archivos corregidos: {fixed_files}")
