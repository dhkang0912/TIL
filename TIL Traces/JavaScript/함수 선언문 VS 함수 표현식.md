# 함수 선언문 vs 함수 표현

# 함수 표현식

- 자바스크립트는 함수를 **“특별한 종류의 값”**으로 취급함
- 다른 언어에서처럼 “특별한 동작을 하는 구조”로 취급하지 않음

## 함수 선언문 (Function Declaration)

```jsx
function sayHi() {
  alert( "Hello" );
}
```

## 함수 표현식 (Function Expression)

```jsx
let sayHi = function() {
  alert( "Hello" );
};
```

- 함수를 생성하고 변수에 값을 할당하는 것처럼 함수가 변수에 할당됨
- 함수가 어떤 방식으로 만들어졌는지에 관계없이 함수는 **값**이고 변수에 할당할 수 있음
- 위 코드의 의미는 함수를 만들고 그 함수를 변수 sayHi에 할당하는 것

```jsx
function sayHi() {
  alert( "Hello" );
}

alert( sayHi ); // 함수 코드가 보임
```

- 함수는 값이기 때문에 alert를 이용하여 함수 코드를 출력할 수도 있음
- 이렇게 하는 경우 sayHi 옆에 괄호가 없기 때문에 함수는 실행되지 않음
    - 자바스크립트에서 함수는 값이기 때문에 위 코드에서 함수 소스 코드가 문자형으로 바뀌어 출력됨
- 자바스크립트는 괄호가 있어야만 함수가 호출됨

```jsx
function sayHi() {   // (1) 함수 생성
  alert( "Hello" );
}

let func = sayHi;    // (2) 함수 복사

func(); // Hello     // (3) 복사한 함수를 실행(정상적으로 실행됩니다)!
sayHi(); // Hello    //     본래 함수도 정상적으로 실행됩니다.
```

- 기본적으로 값이기 때문에 변수를 복사해 다른 변수에 할당하는 것처럼 함수를 복사해 다른 변수에 할당할 수 있음
1. 함수 선언 방식을 이용해 함수를 생성, 생성한 함수는 sayHi라는 변수에 저장
2. sayHi를 새로운 변수 func에 복사함, 이 때 괄호가 없었기 때문에 값 복사
    1. 만약 괄호가 있었다면 함수 호출 결과값이 func에 저장됨
3. 이젠 sayHi()와 func() 함수를 호출할 수 있게 됨

# 함수 표현식 VS 함수 선언문

## 1. 함수 선언 방식의 차이

```jsx
// 함수 선언문
function sum(a, b) {
  return a + b;
}
```

- 함수 선언문: 함수가 주요 코드 흐름 중간에 독자적인 구문 형태로 존재함

```jsx
// 함수 표현식
let sum = function(a, b) {
  return a + b;
};
```

- 함수 표현식: 함수가 표현식이나 구문 구성(syntax construct) 내부에 생성됨
    - 위에서는 할당 연산자를 이용해 만든 “할당 표현식” 우측에서 생성

## 2. 자바스크립트 엔진의 함수 생성 타이밍 차이

- 함수 표현식은 실제 실행 흐름이 해당 함수에 도달했을 때 함수를 생성 ⇒ 호이스팅 되지 않음
- 함수 선언문은 함수 선언문이 정의되기 전에 호출할 수 있음
    - 전역 함수 선언문은 스크립트가 어디 있는지와 상관없이 어디서든 사용 가능
    - 자바스크립트는 스크립트 실행 전 준비 단계에서 전역에 선언된 함수 선언문을 찾고 함수를 생성함
    - 스크립트가 진짜 실행되기 전 “초기화 단계”에서 함수 선언 방식으로 정의한 함수가 생성됨
    - 스크립트는 함수 선언문이 모두 처리된 이후에 실행되어 스크립트는 어디서든 함수 선언문으로 선언한 함수에 접근 가능
    
    ⇒ 함수 호이스팅
    

### 예시

```jsx
sayHi("John"); // Hello, John

function sayHi(name) {
  alert( `Hello, ${name}` );
}
```

- 함수 선언문 sayHi는 스크립트 실행 준비 단계에서 생성되기 때문에 스크립트 내 어디서든 접근 가능

```jsx
sayHi("John"); // error! 레퍼런스 에러

let sayHi = function(name) {  // (*) 마술은 일어나지 않습니다.
  alert( `Hello, ${name}` );
};
```

- 함수 표현식은 함수가 선언되기 전에는 접근하는게 불가능함

## 3. 스코프 차이

- 함수 선언문이 코드 블록 내에 위치하면 블록 내 어디서든 접근 가능하지만 블록 밖에서는 접근 불가

```jsx
let age = prompt("나이를 알려주세요.", 18);

// 조건에 따라 함수를 선언함
if (age < 18) {

  function welcome() {
    alert("안녕!");
  }

} else {

  function welcome() {
    alert("안녕하세요!");
  }

}

// 함수를 나중에 호출합니다.
welcome(); // Error: welcome is not defined
```

- 함수 선언문은 함수가 선언된 코드 블록 안에서만 유효하기 때문에 에러가 남

```jsx
let age = prompt("나이를 알려주세요.", 18);

let welcome;

if (age < 18) {

  welcome = function() {
    alert("안녕!");
  };

} else {

  welcome = function() {
    alert("안녕하세요!");
  };

}

welcome(); // 제대로 동작합니다.
```

- if 문 밖에서 선언한 변수 welcome에 함수 표현식으로 만든 함수를 할당한 경우 코드 블록 밖에서도 유효

참고 자료

https://ko.javascript.info/function-expressions