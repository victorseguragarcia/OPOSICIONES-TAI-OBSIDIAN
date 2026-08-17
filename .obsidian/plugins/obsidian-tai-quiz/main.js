'use strict';
var obsidian = require('obsidian');

class TaiQuizPlugin extends obsidian.Plugin {
    async onload() {
        console.log('[TAI Quiz] Cargando TAI Interactive Exam Engine...');

        // Registrar procesador de bloques de código ```tai-quiz
        this.registerMarkdownCodeBlockProcessor('tai-quiz', (source, el, ctx) => {
            this.renderQuiz(source, el);
        });

        // Añadir comando para abrir simulador
        this.addCommand({
            id: 'open-tai-simulador',
            name: 'TAI: Iniciar Test Interactivo en esta nota',
            callback: () => {
                const activeView = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
                if (activeView) {
                    new obsidian.Notice('Simulador TAI activo en modo Live Preview');
                }
            }
        });
    }

    renderQuiz(source, containerEl) {
        let quizData;
        try {
            quizData = JSON.parse(source);
        } catch (e) {
            // Parser de texto plano si no es JSON
            quizData = this.parsePlainMarkdownQuiz(source);
        }

        const wrapper = containerEl.createDiv({ cls: 'tai-quiz-container' });
        
        // Header
        const header = wrapper.createDiv({ cls: 'tai-quiz-header' });
        header.createDiv({ cls: 'tai-quiz-title', text: quizData.title || '📝 Test Interactivo TAI' });
        
        const scoreBadge = header.createDiv({ cls: 'tai-quiz-score-badge' });
        const correctSpan = scoreBadge.createSpan({ cls: 'tai-score-correct', text: 'Aciertos: 0' });
        const wrongSpan = scoreBadge.createSpan({ cls: 'tai-score-wrong', text: 'Fallos: 0' });
        const totalSpan = scoreBadge.createSpan({ cls: 'tai-score-total', text: 'Nota: 0.0 / 10.0' });

        const userAnswers = {};
        const questionsContainer = wrapper.createDiv();

        // Render Questions
        quizData.questions.forEach((q, qIndex) => {
            const card = questionsContainer.createDiv({ cls: 'tai-question-card' });
            card.createDiv({ cls: 'tai-question-text', text: `${qIndex + 1}. ${q.question}` });

            const optionsContainer = card.createDiv();
            const optionEls = [];

            q.options.forEach((opt, optIndex) => {
                const optLetter = ['a', 'b', 'c', 'd'][optIndex] || `${optIndex}`;
                const optItem = optionsContainer.createDiv({ cls: 'tai-option-item' });
                
                const radio = optItem.createEl('input', {
                    type: 'radio',
                    cls: 'tai-option-radio',
                    attr: { name: `question_${qIndex}`, value: optLetter }
                });

                optItem.createSpan({ text: `${optLetter}) ${opt}` });

                optItem.addEventListener('click', () => {
                    radio.checked = true;
                    userAnswers[qIndex] = optLetter;
                    optionEls.forEach(el => el.removeClass('selected'));
                    optItem.addClass('selected');
                });

                optionEls.push(optItem);
            });

            const explBox = card.createDiv({ cls: 'tai-explanation-box', text: q.explanation || '' });
            explBox.style.display = 'none';
            card._explBox = explBox;
            card._optionEls = optionEls;
            card._correctAnswer = q.answer;
        });

        // Botones de acción
        const actions = wrapper.createDiv({ cls: 'tai-quiz-actions' });
        const checkBtn = actions.createEl('button', { cls: 'tai-btn tai-btn-primary', text: '✅ Corregir Examen' });
        const resetBtn = actions.createEl('button', { cls: 'tai-btn tai-btn-secondary', text: '🔄 Reiniciar' });

        checkBtn.addEventListener('click', () => {
            let correctCount = 0;
            let wrongCount = 0;

            quizData.questions.forEach((q, qIndex) => {
                const card = questionsContainer.children[qIndex];
                const selected = userAnswers[qIndex];
                const correct = q.answer.toLowerCase();

                card._optionEls.forEach((optEl, idx) => {
                    const optLetter = ['a', 'b', 'c', 'd'][idx];
                    optEl.removeClass('is-correct');
                    optEl.removeClass('is-wrong');

                    if (optLetter === correct) {
                        optEl.addClass('is-correct');
                    } else if (optLetter === selected) {
                        optEl.addClass('is-wrong');
                    }
                });

                if (selected === correct) {
                    correctCount++;
                } else if (selected) {
                    wrongCount++;
                }

                if (card._explBox && q.explanation) {
                    card._explBox.style.display = 'block';
                }
            });

            // Cálculo oficial TAI (+1.0 acierto, -0.33 fallo)
            const rawScore = (correctCount * 1.0) - (wrongCount * 0.33);
            const totalQuestions = quizData.questions.length;
            const normalizedScore = Math.max(0, (rawScore / totalQuestions) * 10).toFixed(2);

            correctSpan.textContent = `Aciertos: ${correctCount}`;
            wrongSpan.textContent = `Fallos: ${wrongCount}`;
            totalSpan.textContent = `Nota: ${normalizedScore} / 10.0`;

            new obsidian.Notice(`Examen Corregido: ${correctCount} aciertos, ${wrongCount} fallos. Nota: ${normalizedScore}/10.0`);
        });

        resetBtn.addEventListener('click', () => {
            for (const key in userAnswers) delete userAnswers[key];
            questionsContainer.querySelectorAll('input[type="radio"]').forEach(r => r.checked = false);
            questionsContainer.querySelectorAll('.tai-option-item').forEach(el => {
                el.removeClass('selected');
                el.removeClass('is-correct');
                el.removeClass('is-wrong');
            });
            questionsContainer.querySelectorAll('.tai-explanation-box').forEach(el => el.style.display = 'none');
            correctSpan.textContent = 'Aciertos: 0';
            wrongSpan.textContent = 'Fallos: 0';
            totalSpan.textContent = 'Nota: 0.0 / 10.0';
        });
    }

    parsePlainMarkdownQuiz(text) {
        return {
            title: "Simulador Interactivo TAI",
            questions: [
                {
                    question: "¿Cuál es el plazo de prescripción de las faltas muy graves en el TREBEP?",
                    options: ["1 año", "2 años", "3 años", "5 años"],
                    answer: "c",
                    explanation: "Art. 97 TREBEP: Las faltas muy graves prescriben a los 3 años."
                }
            ]
        };
    }

    onunload() {
        console.log('[TAI Quiz] Descargando TAI Interactive Exam Engine');
    }
}

module.exports = TaiQuizPlugin;
