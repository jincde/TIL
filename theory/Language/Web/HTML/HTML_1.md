emmet

ul>li*5

h2#kimbap+ul>li.blue*5

[emmet](https://docs.emmet.io/abbreviations/syntax/)

html 기본 글꼴 크기 16px



## CSS 기본 스타일

- 글자
  - `px`
    - 모니터 해상도 한 화소인 `pixel` 기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - `%`
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
  - `em`
    - (바로 위) 상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적 사이즈를 가진다
  - `rem`
    - (바로 위) 상속의 영향을 받지 않음
    - 최상위 요소`html`의 사이즈를 기준으로 배수 단위를 가진다

<br>

- 크기 단위(viewport)
  - 방문한 유저에게 바로 보이게 되는 웹 컨텐츠 영역 (디바이스 화면)
  - 디바이스 viewport를 기준으로 상대적 사이즈가 결정
  - `vw` `vh` `vmin` `vmax`

<br>

- 색상 단위

  - `키워드`

    ```css
    background-color: red;
    /* 대소문자를 구분하지 않는다. */
    ```

  - `RGB`

    ```css
    background-color: rgb(0, 255, 0);
    /* 16진수 표기법, 함수형 표기법 사용 */
    
    background-color: rgba(0, 255, 0, 0.5);
    /* a는 alpha, 투명도 */
    ```

  - `HSL`

    ```css
    background-color: hsl(0, 100%, 50%);
    /* 색상, 채도, 명도로 표현 */
    
    background-color: hsla(0, 100%, 50%, 0.5);
    /* a는 alpha, 투명도 */
    ```

<br>

---

<br>

## CSS 상속

- CSS는 상속을 통해 상위 요소의 속성을 하위 요소에게 상속한다
- 상속이 가능한, 가능하지 않은 속성이 있다
  - 상속 가능 : Text관련 요소(font, color...), opacity, visibility
  - 상속 불가능 : Box관련 요소(width, padding...), Position관련 요소(top, z-index...)

<br>

---

<br>

## CSS 원칙

- 모든 요소는 `box`모델
- 위에서부터 아래로`Block Direction`
- 왼쪽에서 오른쪽으로 쌓인다`Inline Direction`

![mdn-horizontal](HTML_1.assets/mdn-horizontal.png)

<br>

### 1. Box model

- 하나의 박스는 네 영역으로 이루어져 있다

  - `margin` : 테두리 바깥의 외부 여백, 배경색 지정 불가

  - `border` : 테두리 영역

  - `padding` : 테두리 안쪽의 내부 여백, 배경색, 이미지는 `padding`까지 적용

  - `content` : 요소의 실제 내용

    ![스크린샷 2022-08-30 오후 2.54.32](HTML_1.assets/스크린샷 2022-08-30 오후 2.54.32.png)

<br>

- 상하좌우 설정(margin/padding)

  - 상하좌우

    ```css
    margin: 10px;
    /* 10px = 상하좌우 */
    ```

  - 상하 / 좌우

    ```css
    margin: 10px 20px
    /* 10px = 상 하 */
    /* 20px = 좌 우 */
    ```

  - 상 / 좌우 / 하

    ```css  
    margin: 10px 20px 30px;
    /* 10px = 상 */
    /* 20px = 좌우 */
    /* 30px = 하 */
    ```

  - 상 / 우 / 하 / 좌 `시계방향`

    ```css
    margin: 10px 20px 30px 40px;
    /* 10px = 상 */
    /* 20px = 우 */
    /* 30px = 하 */
    /* 40px = 좌 */
    ```

<br>

#### 1-1. box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

  - padding을 제외한 순수 content 영역만을 box로 지정

- border까지의 너비를 보는 것을 원할 때?

  ```css
  box-sizing: border-box;
  /* box-sizing을 border-box로 변경
  ```

  ![스크린샷 2022-08-30 오후 3.26.34](HTML_1.assets/스크린샷 2022-08-30 오후 3.26.34.png)

<br>

### 2. display

- block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 `inline`요소가 들어갈 수 있다 
- inline
  - 줄 바꿈이 일어나지 않는 일부 요소
  - content 너비만큼 가로 폭 차지
  - width, height, margin-top, margin-bottom 지정 불가
  - 상하 여백은 `line-height`로 지정