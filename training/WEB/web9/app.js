const display = document.querySelector('.numbers');
const btn1 = document.querySelector('#draw');
const btn2 = document.querySelector('#reset');

const numbers = [];
const colors = ['yellow', 'blue', 'red', 'gray', 'green'];

function paintNumber(number) {
  const eachNumDiv = document.createElement('div')
  let colorsIndex = Math.floor(number / 10);
  
  eachNumDiv.classList.add('eachnum')
  eachNumDiv.style.backgroundColor = colors[colorsIndex]
  eachNumDiv.textContent = number
  display.appendChild(eachNumDiv)
}

btn1.addEventListener('click', function() {
  while(numbers.length < 6) {
    let randomNumber = Math.floor(Math.random() * 45) + 1
    if (numbers.indexOf(randomNumber) === -1) {
      numbers.push(randomNumber)
      paintNumber(randomNumber)
    }
  }
})

btn2.addEventListener('click', function() {
  numbers.splice(0, 6); // 0번 인덱스부터 6개를 지우겠다
  display.innerHTML = ""
})