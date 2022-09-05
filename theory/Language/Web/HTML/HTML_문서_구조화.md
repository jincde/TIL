## 문서 구조화

`테이블`의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>`요소를 활용

- `tr`로 가로 줄 구성
- `th : header`, `td : data`로 셀을 구성

```html
<body>
  <table>
    
    <thead>
    	<tr>
      	<th>ID</th>
        <th>Name</th>
        <th>Major</th>
      </tr>
    </thead>
    
    <tbody>
    	<tr>
      	<td>1</td>
      	<td>홍길동</td>
      	<td>Computer Science</td>
      </tr>
    </tbody>
    
    <tfoot>
    	<tr>
      	<td>총계</td>
      	<td colspan="2">2명</td>
      </tr>
    </tfoot>
    
    <caption>1반 학생 명단</caption>
    
  </table>
</body>

/* colspan은 병합 */
```

<br>

## form

`<form>`은 **데이터를 서버에 제출**하기 위해 사용하는 태그

`action` : form을 처리할 서버의 URL(데이터를 보낼 곳)

`method` : form을 제출할 때 사용할 HTTP 메소드 (GET, POST)

`enctype` : method가 post인 경우 데이터의 유형

	- application/x-www-form-urlencoded : 기본값
	- multipart/form-data : 파일 전송시 (input type이 file인 경우)
	- text/plain : HTML5 디버깅 용도 

<br>

## input

다양한 타입을 갖는 입력 데이터 유형, 위젯이 제공

`name` : form control에 적용되는 이름(이름/값 페어로 전송)

`value` : form control에 적용되는 값(이름/값 페어로 전송)

`required`, `readonly`, `autofocus`, `autocomplete`, `disabled` 등

<br>

ex) google 검색창

```html
<form action="/search" method="GET">
  <input type="text" name="q">
</form>

https://www.google.com/search?q=HTML
```

```html
<form action="">
  username : <input type="text">
</form>
```

<br>

### input label

`label`을 클릭해 input 자체 초점을 맞추거나 활성화할 수 있다

- 유저는 선택할 수 있는 영역이 늘어나 웹/모바일 환경에서 편하게 사용 가능
- label과 input 입력의 관계가 화면리더기에서도 label을 읽어 쉽게 내용확인 가능

`<input>`에 id속성을, `<label>`에는 for 속성을 활용해 상호연관을 시킴

```html
<label for="agreement">개인정보 수집 동의</label>
<input type="checkbox" name="agreement" id="agreement">
```

<br>

### input type

타입별로 HTML 기본 검증 또는 추가 속성을 활용할 수 있다

`text` : 일반 텍스트 입력

`password` : 입력 시 값이 보이지 않고 문자를 `*`로 표현

`email` : 이메일 형식이 아닌 경우 form 제출 불가

`number` : min, max, step 속성을 활용해 숫자 범위 지정 가능

`file` : accept 속성을 활용해 파일 타입 지정 가능



### input type - select

일반적으로 label 태그와 함께 사용해 선택 항목 작성

동일 항목에 대해 name을 지정, 선택된 항목에 대한 value를 지정

`checkbox` : 다중 선택 가능

`radio` : 단일 선택만 가능

> name을 일치시켜줘야 한다



### input type - Etc.

다양한 input을 위한 picker 제공

`color` : color picker

`date` : date picker

<br>

`hidden input`을 활용해 사용자 입력을 받지 않고 서버에 전송되어야  할 값을 설정

`hidden` : 사용자에게 보이지 않는 input





