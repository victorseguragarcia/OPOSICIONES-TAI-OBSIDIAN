# -*- coding: utf-8 -*-
r"""
Script de actualización del plugin 'obsidian-tai-quiz':
Implementa el modo de CORRECCIÓN INMEDIATA 1 A 1:
- Al hacer clic en cualquier opción, se corrige al instante:
  * Verde si es correcta
  * Rojo si es incorrecta (y resalta la correcta en verde)
  * Despliega la justificación inmediatamente
  * Actualiza la puntuación en vivo (+1.0 / -0.33) en tiempo real
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")
PLUGIN_DIR = REPO_DIR / ".obsidian" / "plugins" / "obsidian-tai-quiz"

MAIN_JS_CONTENT = """'use strict';
var obsidian = require('obsidian');

class TaiQuizPlugin extends obsidian.Plugin {
    async onload() {
        console.log('[TAI Quiz] Cargando motor de corrección inmediata 1 a 1...');

        // Registrar procesador de bloques ```tai-quiz
        this.registerMarkdownCodeBlockProcessor('tai-quiz', (source, el, ctx) => {
            this.renderInteractiveQuiz(source, el);
        });

        this.addCommand({
            id: 'reload-tai-quiz',
            name: 'TAI: Recargar Simulador de Examen',
            callback: () => {
                new obsidian.Notice('Simulador TAI recargado con corrección inmediata 1 a 1');
            }
        });
    }

    renderInteractiveQuiz(source, containerEl) {
        let quizData;
        try {
            quizData = JSON.parse(source);
        } catch (e) {
            quizData = {
                title: "Test TAI",
                questions: []
            };
        }

        const wrapper = containerEl.createDiv({ cls: 'tai-quiz-container' });
        
        // Cabecera con Marcador en Tiempo Real
        const header = wrapper.createDiv({ cls: 'tai-quiz-header' });
        const titleEl = header.createDiv({ cls: 'tai-quiz-title', text: quizData.title || '📝 Test de Autoevaluación TAI' });
        
        const scoreBadge = header.createDiv({ cls: 'tai-quiz-score-badge' });
        const correctSpan = scoreBadge.createSpan({ cls: 'tai-score-correct', text: 'Aciertos: 0' });
        const wrongSpan = scoreBadge.createSpan({ cls: 'tai-score-wrong', text: 'Fallos: 0' });
        const totalSpan = scoreBadge.createSpan({ cls: 'tai-score-total', text: 'Puntos: 0.0 / 10.0' });

        // Subtítulo explicativo de corrección inmediata
        const subheader = wrapper.createDiv({ cls: 'tai-quiz-mode-banner', text: '⚡ Modo Práctica Activa: Las preguntas se corrigen automáticamente al hacer clic en cada opción.' });

        let correctCount = 0;
        let wrongCount = 0;
        const totalQuestions = quizData.questions.length || 1;
        const answeredMap = {};

        function updateScoreboard() {
            const rawScore = (correctCount * 1.0) - (wrongCount * 0.33);
            const normalized = Math.max(0, (rawScore / totalQuestions) * 10).toFixed(2);
            correctSpan.textContent = `Aciertos: ${correctCount}`;
            wrongSpan.textContent = `Fallos: ${wrongCount}`;
            totalSpan.textContent = `Puntos: ${normalized} / 10.0`;
        }

        const questionsContainer = wrapper.createDiv({ cls: 'tai-questions-list' });

        // Renderizar cada tarjeta de pregunta
        quizData.questions.forEach((q, qIndex) => {
            const card = questionsContainer.createDiv({ cls: 'tai-question-card' });
            
            // Título de la pregunta con número
            const qHeader = card.createDiv({ cls: 'tai-question-header' });
            qHeader.createSpan({ cls: 'tai-q-num', text: `Pregunta ${qIndex + 1} de ${totalQuestions}` });
            
            const qText = card.createDiv({ cls: 'tai-question-text', text: q.question });

            const optionsContainer = card.createDiv({ cls: 'tai-options-container' });
            const optionEls = [];

            // Cuadro de explicación oculta por defecto
            const explBox = card.createDiv({ cls: 'tai-explanation-box' });
            explBox.innerHTML = `<strong>💡 Explicación Técnica/Jurídica:</strong><br>${q.explanation || 'Respuesta oficial contrastada con el temario.'}`;
            explBox.style.display = 'none';

            q.options.forEach((opt, optIndex) => {
                const optLetter = ['a', 'b', 'c', 'd'][optIndex] || `${optIndex}`;
                const optItem = optionsContainer.createDiv({ cls: 'tai-option-item' });
                
                const indicator = optItem.createSpan({ cls: 'tai-opt-letter', text: `${optLetter})` });
                const labelText = optItem.createSpan({ cls: 'tai-opt-text', text: opt });

                // Evento de clic: CORRECCIÓN INMEDIATA 1 A 1
                optItem.addEventListener('click', () => {
                    if (answeredMap[qIndex]) {
                        // Ya fue respondida esta pregunta, no permitir cambio
                        return;
                    }

                    answeredMap[qIndex] = true;
                    const correctLetter = (q.answer || 'a').toLowerCase().trim();
                    const isCorrect = (optLetter === correctLetter);

                    if (isCorrect) {
                        correctCount++;
                        optItem.addClass('is-correct');
                        optItem.createSpan({ cls: 'tai-feedback-badge-correct', text: ' ✔ Correcta (+1.0)' });
                    } else {
                        wrongCount++;
                        optItem.addClass('is-wrong');
                        optItem.createSpan({ cls: 'tai-feedback-badge-wrong', text: ' ✖ Incorrecta (-0.33)' });

                        // Marcar la respuesta verdadera en verde
                        optionEls.forEach((otherEl, otherIdx) => {
                            const otherLetter = ['a', 'b', 'c', 'd'][otherIdx];
                            if (otherLetter === correctLetter) {
                                otherEl.addClass('is-correct');
                                otherEl.createSpan({ cls: 'tai-feedback-badge-correct', text: ' ✔ Era la correcta' });
                            }
                        });
                    }

                    // Deshabilitar clics posteriores en esta tarjeta
                    card.addClass('answered');
                    explBox.style.display = 'block';
                    updateScoreboard();
                });

                optionEls.push(optItem);
            });
        });

        // Botón inferior para reiniciar el test
        const footer = wrapper.createDiv({ cls: 'tai-quiz-footer' });
        const resetBtn = footer.createEl('button', { cls: 'tai-btn tai-btn-secondary', text: '🔄 Reiniciar y Repetir Test' });
        
        resetBtn.addEventListener('click', () => {
            correctCount = 0;
            wrongCount = 0;
            for (const key in answeredMap) delete answeredMap[key];
            updateScoreboard();

            questionsContainer.querySelectorAll('.tai-question-card').forEach(card => {
                card.removeClass('answered');
            });
            questionsContainer.querySelectorAll('.tai-option-item').forEach(el => {
                el.removeClass('is-correct');
                el.removeClass('is-wrong');
                el.querySelectorAll('.tai-feedback-badge-correct, .tai-feedback-badge-wrong').forEach(b => b.remove());
            });
            questionsContainer.querySelectorAll('.tai-explanation-box').forEach(el => {
                el.style.display = 'none';
            });
            new obsidian.Notice('Test reiniciado');
        });
    }

    onunload() {
        console.log('[TAI Quiz] Descargando plugin');
    }
}

module.exports = TaiQuizPlugin;
"""

STYLES_CSS_CONTENT = """/* ==========================================================================
   TAI INTERACTIVE EXAM ENGINE - ESTILO CORRECCIÓN INMEDIATA 1 A 1
   ========================================================================== */

.tai-quiz-container {
  background: var(--background-secondary);
  border: 1px solid var(--background-modifier-border);
  border-radius: 14px;
  padding: 22px;
  margin: 18px 0;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.08);
}

.tai-quiz-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid rgba(239, 83, 80, 0.35);
  padding-bottom: 12px;
  margin-bottom: 10px;
}

.tai-quiz-title {
  font-size: 1.25em;
  font-weight: 700;
  color: #EF5350;
}

.tai-quiz-score-badge {
  background: var(--background-primary);
  border: 1px solid var(--background-modifier-border);
  border-radius: 20px;
  padding: 6px 16px;
  font-size: 0.95em;
  display: flex;
  gap: 14px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.tai-score-correct { color: #2E7D32; font-weight: 700; }
.tai-score-wrong { color: #C62828; font-weight: 700; }
.tai-score-total { color: #1976D2; font-weight: 700; }

.tai-quiz-mode-banner {
  font-size: 0.85em;
  color: var(--text-muted);
  margin-bottom: 18px;
  font-style: italic;
}

.tai-question-card {
  background: var(--background-primary);
  border: 1px solid var(--background-modifier-border);
  border-radius: 10px;
  padding: 16px 18px;
  margin-bottom: 18px;
  transition: border-color 0.2s;
}

.tai-question-card.answered {
  border-color: rgba(66, 165, 245, 0.4);
}

.tai-question-header {
  margin-bottom: 6px;
}

.tai-q-num {
  font-size: 0.8em;
  font-weight: 700;
  text-transform: uppercase;
  color: #42A5F5;
  background: rgba(66, 165, 245, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
}

.tai-question-text {
  font-weight: 600;
  font-size: 1.05em;
  margin: 8px 0 14px 0;
  color: var(--text-normal);
  line-height: 1.45;
}

.tai-options-container {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.tai-option-item {
  display: flex;
  align-items: center;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--background-modifier-border);
  background: var(--background-secondary-alt, var(--background-primary));
  cursor: pointer;
  transition: all 0.15s ease-in-out;
  user-select: none;
}

.tai-option-item:hover:not(.is-correct):not(.is-wrong) {
  background: rgba(66, 165, 245, 0.1);
  border-color: #42A5F5;
  transform: translateX(3px);
}

.tai-opt-letter {
  font-weight: 700;
  margin-right: 10px;
  color: var(--text-muted);
}

.tai-opt-text {
  flex-grow: 1;
}

/* --- Feedback Inmediato: Verde Acierto --- */
.tai-option-item.is-correct {
  background: rgba(76, 175, 80, 0.18) !important;
  border-color: #4CAF50 !important;
  color: #1B5E20 !important;
  font-weight: 600 !important;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.2);
}

/* --- Feedback Inmediato: Rojo Fallo --- */
.tai-option-item.is-wrong {
  background: rgba(239, 83, 80, 0.18) !important;
  border-color: #EF5350 !important;
  color: #B71C1C !important;
  text-decoration: line-through;
}

.tai-feedback-badge-correct {
  margin-left: auto;
  font-size: 0.85em;
  color: #2E7D32;
  font-weight: 700;
  background: rgba(76, 175, 80, 0.2);
  padding: 2px 8px;
  border-radius: 10px;
}

.tai-feedback-badge-wrong {
  margin-left: auto;
  font-size: 0.85em;
  color: #C62828;
  font-weight: 700;
  background: rgba(239, 83, 80, 0.2);
  padding: 2px 8px;
  border-radius: 10px;
}

.tai-explanation-box {
  margin-top: 14px;
  padding: 12px 16px;
  background: rgba(66, 165, 245, 0.08);
  border-left: 4px solid #42A5F5;
  border-radius: 6px;
  font-size: 0.92em;
  line-height: 1.5;
  color: var(--text-normal);
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

.tai-quiz-footer {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}

.tai-btn {
  padding: 9px 18px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid var(--background-modifier-border);
  background: var(--background-primary);
  color: var(--text-normal);
  transition: all 0.2s;
}

.tai-btn:hover {
  background: rgba(128, 128, 128, 0.15);
  border-color: var(--text-muted);
}
"""

(PLUGIN_DIR / "main.js").write_text(MAIN_JS_CONTENT, encoding="utf-8")
(PLUGIN_DIR / "styles.css").write_text(STYLES_CSS_CONTENT, encoding="utf-8")
print("  [OK] main.js y styles.css actualizados con corrección inmediata 1 a 1.")

# Sincronizar con baúl superior
for d in [".obsidian/plugins/obsidian-tai-quiz"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado plugin en baúl superior: {d}")

print("\n[*] Actualización de plugin completada.")
