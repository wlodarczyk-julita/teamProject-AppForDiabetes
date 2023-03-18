/// Main JavaScript File
/// Here we import all the global JavaScript files we need for our project.

import '../global-styles/style.scss'

const nextButton = document.getElementById('btn-nextQuestion')

const questionElement = document.getElementById('question')
const answearButtonsElement = document.getElementById('btn-answear')

function setNextQuestion () {
    resetState()
    showQuestion(question)
}

function showQuestion (question) {
questionElement.innerText = question.question
question.answear.forEach(answear => {
    const button = document.createElement('button')
    button.innerText = answear.text
    button.classList.add('btn')
    button.addEventListener('click', selectAnsear)
    answearButtonsElement.appendChild(button)
});
}

function resetState() {
    nextButton.classList.add('hide')
    while(answearButtonsElement.firstChild) {
        answearButtonsElement.removeChild(answearButtonsElement.firstChild)
    }
}

const question = [
    {
        question: "Wybierz swoją płeć",
        answear: [
            {text: 'Kobieta'},
            {text: 'Mężczyzna'}
        ]
    }
]