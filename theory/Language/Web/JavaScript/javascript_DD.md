### 변수는 하나의 값을 저장하기 위한 수단

```javascript
var userId = 1;
var userName = 'Lee';
var result = 10 + 20;
```

<br>

### 객체나 배열 같은 자료구조를 사용하면 여러 개의 값을 그룹화해서 하나의 값처럼 사용할 수 있다

```javascript
var user = {id: 1, name: 'Lee'};

var users = [
  {id: 1, name: 'Lee'},
  {id: 2, name: 'Kim'}
];
```

<br>

### 변수 선언

```javascript
var score;

console.log(score); // undefined
```

> var 키워드로 선언된 변수는 암묵적으로 undefined로 자동으로 초기화

<br>

### ReferenceError

```javascript
a
// Uncaught ReferenceError: a is not defined
```

> 식별자를 통해 값을 참조했지만 찾을 수 없을때 발생

<br>

### 호이스팅

```javascript
console.log(score);

var score;
```

> 호이스팅에 의해 변수선언이 인지되어 있다

<br>

```javascript
console.log(score); 

var score;
score = 80;

console.log(score); 

// undefined
// 80
// undefined
```

```javascript
console.log(score); 

score = 80;
var score;

console.log(score); 

// 80
// 80
// undefined
```

<br>

```javascript
var b = x = 5;

x // 5
b // 5
```



