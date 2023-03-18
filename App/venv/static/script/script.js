const nextButton = document.getElementById('btn-nextQuestion')

const questionElement = document.getElementById('question')
const answearButtonsElement = document.getElementById('btn-answear')

let currentQuestionIndex=0

nextButton.addEventListener('click', () => {
    setNextQuestion()
    currentQuestionIndex++
  })

function setNextQuestion () {
    resetState()
    showQuestion(currentQuestionIndex)
}

function showQuestion (question) {
questionElement.innerText = question.question
question.answear.forEach(answear => {
    const button = document.createElement('button')
    button.innerText = answear.text
    button.classList.add('btn-answear')
    button.addEventListener('click', selectAnswear)
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