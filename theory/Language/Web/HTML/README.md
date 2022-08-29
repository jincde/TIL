# <i>HTML</i>

### 1. 개념

- Hypertext Markup Language
  - Hypertext : 다른 페이지로 연결하는 링크
- 웹을 이루는 가장 기초적인 구성 요소
- 웹 컨텐츠의 의미와 구조를 정의할 때 사용
- 컨텐츠의 서로 다른 부분들을 씌우거나`wrap`, 감싸서`enclose` 다른 형식으로 동작하도록 하는 요소`elements`로 이루어져 있다

<br>

### 2. 요소

- 여는 태그(opening tag) : 요소가 시작되는 곳, 효과를 시작하는 곳
- 닫는 태그(closing tag) : 요소 이름 앞에 `/`가 포함, 요소의 끝
- 컨텐츠(content) : 요소의 내용
- 요소(element) : 여는 태그, 닫는 태그, 컨텐츠로 이루어져 있다
- 요소는 속성을 가질 수 있다
  - 요소 이름과 속성 사이에 공백이 있어야 한다
  - 속성 이름 뒤에는 `=`
  - 속성 값의 앞 뒤에 열고 닫는 `""` 또는 `''`

#### 2-1 요소 중첩

- 요소 안에 다른 요소를 추가할 수 있다 `nesting`

  ```html
  <p>
    내 강아지는 <strong>아주</strong> 귀여워.
  </p>
  ```

  > 내 강아지는 **아주** 귀여워.

#### 2-2 빈 요소

- 내용을 갖지 않는 요소 `empty elements`

  ```html
  <img src="link" alt='test'>
  ```

  > 두 개의 속성을 포함하지만, 닫는 태그가 없다.
  >
  > 이미지 요소는 효과를 주기 위해 컨텐츠를 감싸지 않기 때문.

<br>

### 3. 사용법

- 웹 브라우저에 표시되는 컨텐츠를 위해 `마크업`을 사용
- 태그를 사용해 문서의 다른 텍스트와 구분 `<태그이름>`
- 다양한 요소를 사용
  - `<head>`, `<title>`, `<body>`, `<header>`등이 있다
- 대소문자를 구분하지 않기 때문에 혼합 사용 가능
- 주석 `<!-- 주석내용 -->`

<br>

### 4. 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- `<!DOCTYPE html>` : 역사적 유물, HTML 페이지가 따라야 할 일련의 규칙, 연결통로로써 작동
- `<html></html>` : 페이지 전체 컨텐츠를 감싸며, `루트`요소라고도 한다
- `<head></head>` : 페이지에 포함된 모든 것들의 컨테이너 역할
  - 브라우저 화면에 직접적으로 보이진 않으며, 숨은 데이터를 정의하는 태그들이 들어간다
- `<body></body>` : 사용자들에게 나타낼 컨텐츠들을 담고 있다
  - `<body>`태그 내부에 들어가는 대표적인 태그 목록
    - `<br>`
    - `<p>`
    - `<b>`
    - `<i>`
    - `<h1>`
    - `<a>`
    - `<img>`
    - `<table>`
    - `<div>`
    - `<span>`
    - `<ul>`, `<li>`
    - `<form>`
- `<img>` : `src`속성을 통해 이미지 파일 경로, `alt` 이미지 대체 텍스트
- `<meta charset = "utf-8">` : 문서가 사용할 문자 집합을 utf-8로 설정
- `<title></title>` : 페이지 제목을 설정, 브라우저 탭에 표시

<br>

### 5. 문자 표현

- 제목

  - `<h1>` ~ `<h6>`

    ```html
    <h1>main title</h1>
    <h2>top level</h2>
    <h3>sub heading</h3>
    ```

- 문단

  - `<p>`

    ```html
    <p>This is text area</p>
    ```

    > 일반적인 문자 내용을 나타낼 때 많이 사용

- 목록

  - `<ul>` - Unorderd list

    ```html
    <ul>
      <li>apple</li>
      <li>banana</li>
      <li>grape</li>
    </ul>
    ```

    > - apple
    > - banana
    > - grape

  - `<ol>` - ordered list

    ```html
    <ol>
      <li>제목</li>
      <li>본문</li>
      <li>마무리</li>
      <li>레퍼런스</li>
    </ol>
    ```

    > 1. 제목
    > 2. 본문
    > 3. 마무리
    > 4. 레퍼런스

- 연결

  - `<a>` - anchor

    ```html
    <a href="https://www.google.com">google</a>
    ```

    > 문장 안의 어떤 단어를 링크로 만들어 준다

<br>

### 6. 레퍼런스

- [MDN web docs](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [ofcourse](https://ofcourse.kr/html-course/HTML-%EC%9E%85%EB%AC%B8)