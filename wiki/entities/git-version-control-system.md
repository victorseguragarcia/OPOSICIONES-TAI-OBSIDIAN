---
title: "Sistema de Control de Versiones Distribuido Git"
type: "entity"
tags:
  - git
  - control-versiones
  - devops
  - repositorios
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Git"
  - "Control de Versiones"
---

# Sistema de Control de Versiones Distribuido Git

Sistema de control de versiones descentralizado creado por Linus Torvalds que registra instantáneas (*snapshots*) completas del árbol de archivos.

---

## 🏛️ Zonas de Trabajo y Comandos

```
      Working Directory ──────[ git add ]──────> Staging Area (Index)
             │                                         │
      [ git checkout ]                          [ git commit ]
             │                                         │
             ▼                                         ▼
      Archivos Modificados                     Local Repository (.git)
                                                       │
                                                [ git push / pull ]
                                                       │
                                                       ▼
                                                Remote Repository
```

- **`git merge` vs `git rebase`**: `merge` preserva el historial creando un commit de unión; `rebase` reescribe los commits linealmente sobre la rama destino.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Concepto: [[wiki/concepts/ci-cd-pipelines-and-devops|Pipelines CI/CD]]
