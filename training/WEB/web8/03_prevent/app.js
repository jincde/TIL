const h1 = document.querySelector('h1')
    h1.addEventListener('copy', function(event) {
      // event의 기본 동작을 막고,
      event.preventDefault()
      console.log('삐빅 복사를 할 수 없습니다.')
    })
    
    h1.addEventListener('click', function(event) {
      event.preventDefault()
      console.log(event.button)
    })