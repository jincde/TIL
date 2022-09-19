// 초기값
let countNumber = 0

// ID가 btn인 요소를 선택
const btn = document.querySelector('#btn')
console.log(btn)
// btn이 클릭 되었을 때마다 함수가 실행됨
btn.addEventListener('click', function() {
  console.log('버튼 클릭!')
  // countNumber를 증가시키고
  countNumber += 1
  // id가 counter인의 내용을 변경 시킨다. 
  const counter = document.querySelector('#counter')
  counter.innerText = countNumber
})