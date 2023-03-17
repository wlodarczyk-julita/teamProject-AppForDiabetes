/// Sample js file for demo purposes
/// Remember to always export your functions
/// so that they can be used in other files

export function setupCounter(element) {
  let counter = 0
  const setCounter = (count) => {
    counter = count
    element.innerHTML = `script test - count is ${counter}`
  }
  element.addEventListener('click', () => setCounter(counter + 1))
  setCounter(0)
}

const nextButton = document.getElementById('btn-nextQuestion')

const questionElement = document.getElementById('question')
const answearButtonsElement = document.getElementById('btn-answear')

nextButton.addEventListener('click', setNextQuestion)

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
