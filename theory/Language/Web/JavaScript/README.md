## JavaScript

웹 페이지 내용이 주기적으로 갱신되고, 사용자와 상호작용이 가능하거나, 애니메이션이 적용된다면 `JavasScript`가 관여하고 있다고 생각해도 된다

- 컨텐츠를 동적으로 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가

  ```javascript
  const para = document.querySelector('p');
  // 변수에 값을 저장
  
  para.addEventListener('click', updateName);
  // 발생하는 이벤트가 응답하도록 설정(click)
  
  function updateName() {
    const name = prompt('Enter a new name');
    para.textContent = `Player 1: ${name}`;
  }
  ```



## API

#### DOM (Document Object Model)

HTML 컨텐츠를 추가, 제거, 변경하고 페이지에 동적 스타일을 추가 `HTML` `CSS`를 조작

<br>

#### Geolocation API

지리정보를 가져올 수 있다. Google지도를 이용해 위치를 찾아 지도에 그리는 경우

<br>

#### Canvas, WebGL API

애니메이션을 적용한 2D, 3D 그래픽을 만들 수 있다

<br>

#### 오디오, 비디오

HTMLMediaElement, WebRTC를 포함하는 API로는 멀티미디어를 사용
오디오나 비디오를 웹페이지에서 바로 재생, 웹캠으로 비디오를 찍어 화면에 출력

<br>

<br>

## JavaScript는 인터프리터 언어

코드를 위에서 아래로 실행, 코드 구동 결과가 즉시 반환된다

브라우저에서 JavaScript 코드를 실행하기 전에 다른 형태로 변환할 필요가 없다

- 대부분 모던 JavaScript 인터프리터들은 `JIT(just-in-time)`이라는 기술을 사용해 성능을 향상
- 스크립트 실행과 동시에 소스 코드를 더 빠르게 실행할 수 있는 이진 형태로 변환해 높은 실행 속도를 얻음

<br>

<br>

## 클라이언트 사이드 코드

클라이언트 사이드 코드는 사용자 컴퓨터에서 동작하는 코드, 

웹을 방문하면 브라우저가 페이지 내 `클라이언트 사이드` 코드를 다운로드 후 실행. 

<br>

## 서버 사이드 코드

서버에서 동작하는 코드, 실행 결과를 브라우저가 다운로드해 화면에 띄움

유명한 서버 사이드 웹 언어로는 `PHP` `Python` `Ruby` `ASP.NET` `JavaScript`가 있다.

`JavaScript`는 브라우저 뿐 아니라, 많은 사람들이 사용하는 `Node.js`환경처럼 서버 사이드로 사용할 수 있다 

<br>

<br>

## addEventListener

`querySelectorAll()`함수를 사용해 페이지 내 모든 요소를 선택할 수 있다.

그 후 반복과 `addEventListener()`로 버튼 하나씩 처리기를 부착할 수 있다.

```javascript
const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}
```

<br>

## for...of

반복가능한 객체`Array` `Map` `Set` `String` `TypedArray` `arguments`에 대해 반복.

각 개별 속성값에 대해 실행되는 문이 있는 사용자 정의 반복 후크를 호출하는 루프 생성

```javascript
const array1 = ['a', 'b', 'c'];

for (const element of array1) {
  console.log(element);
}
```

<br>

<br>

## 스크립트 로딩

페이지의 모든 HTML은 순서대로 불러온다, JavaScript를 사용해 `DOM`을 조작하려고 할 때, HTML코드보다 JavaScript를 먼저 불러오면 코드가 올바르게 동작하지 않을 것

<br>

##### 파싱

해당 언어의 문법 검사기로 네트워크로 받은 HTML과 CSS파일을 토큰화 시켜 Parse Tree를 생성

이 Parse Tree를 DOM트리로 만들어 렌더한다

하지만 HTML을 화면에 보이기 위해 파싱하는 도중 파싱을 멈추는 경우가 발생

<br>

- 렌더링 엔진은 `HTML` `CSS`를 파싱한 결과물로 페이지를 화면에 표시
  - 사파리의 `webkit`, 크롬-오페라-edge의 `Blink`, IE의 `trident`, 파이어폭스의 `Gecko`
  - Blink는 webkit에서 파생됐다
- JavaScript는 해석기에서 해석
- script 태그의 파일은 두 개 과정을 거쳐 실행
  - 다운로드(fetching)
  - 실행(execution)
- HTML은 파싱 도중, script 태그를 마난게 되면 중간에 파싱이 멈춘다

<br>

##### 1. head 태그 내부에 script 태그

head 태그 내부에 불러온 script 태그를 느라 body내부 UI는 script태그를 읽은 후 출력될 것이다

만약 script 파일이 크고 무겁다면 HTML 파싱을 끝내지 못한 화면을 출력할 것

HTML 파싱 완료 전에 script 파일을 실행시키기 때문에 이 파일이 DOM요소를 조작한다면 존재하지 않는 DOM요소에 접근하려는 시도로 예상하지 못한 문제가 발생할 수 있다

<br>

##### 2. body 태그 마지막에 script 태그

1번 방법보다 빠르게 페이지 컨텐츠를 읽어볼 수 있다.

하지만 웹이 Javascript에 의존적이라면 HTML 파싱이 다 되어도 동작할 수 없다는 단점이 있다

<br>

##### 3. async

head 내부 script에 사용

HTML파일을 파싱하다 script태그를 만나면 파싱하는 동시에 script를 다운로드 한다

script를 실행시키는 동안엔 HTML 파싱이 멈춘다, javaScript에 의존적인 웹을 더 빨리 실행시킬 수 있다
하지만, HTML파싱이 멈추게 되기 때문에 1번과 같은 문제를 겪을 수 있다

script 파일 실행 순서에 영향을 받는다면 문제가 될 수 있다

<br>

##### 4. defer

HTML을 파싱하면서 script를 만나면 다운로드 완료만 한다.

즉, HTML 파싱이 완료된 후 script를 실행한다.

여러 개의 script파일을 미리 다운로드하고 HTML도 끝까지 파싱시킨 후 순서대로 실행

