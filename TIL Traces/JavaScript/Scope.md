# 스코프
- [스코프](#스코프)
  - [1. 스코프란?](#1-스코프란)
  - [2. 스코프의 구분](#2-스코프의-구분)
    - [자바스크립트에서 스코프 구분](#자바스크립트에서-스코프-구분)
    - [변수의 관점에서 스코프](#변수의-관점에서-스코프)
  - [3. 자바스크립트 스코프의 특징](#3-자바스크립트-스코프의-특징)
  - [4. 전역 스코프](#4-전역-스코프)
  - [5.  비 블록 레벨 스코프 (Non block-level scope)](#5--비-블록-레벨-스코프-non-block-level-scope)
  - [6. 함수 레벨 스코프 (Function-level scope)](#6-함수-레벨-스코프-function-level-scope)
  - [7.  내부 함수](#7--내부-함수)
  - [7. 렉시컬 스코프](#7-렉시컬-스코프)
  - [8. 암묵적 전역](#8-암묵적-전역)
  - [9. 최소한의 전역 변수 사용](#9-최소한의-전역-변수-사용)
  - [10. 즉시 실행 함수를 이용한 전역변수 사용 억제](#10-즉시-실행-함수를-이용한-전역변수-사용-억제)
  - [참고 자료](#참고-자료)


## 1. 스코프란?

- 스코프(Scope, 유효범위) : 참조 대상 식별자를 찾아내기 위한 규칙
    - 참조 대상 식별자(identifier) : 변수, 함수의 이름과 같이 어떤 대상을 다른 대상과 구분하여 식별할 수 있는 유일한 이름
- 변수는 전역 또는 코드 블록이나 함수 내에 선언하며, 코드 블록이나 함수는 중첩될 수 있음
- 식별자는 자신이 어디에서 선언됐는지에 의해 다른 코드가 자신을 참조할 수 있는 유효한 범위를 갖는다.

```jsx
var x = 'global';

function foo () {
  var x = 'function scope';
  console.log(x);
}

foo(); // ?
console.log(x); // ?
```

- 이름이 같은 변수 x가 중복 선언됨
- 전역에서 변수 x를 참조할 때, 함수 foo 내부에서 변수 x를 참조할 때 이름이 중복된 2개의 변수 중 어떤 변수를 참조해야할까?
    - 정답
        
        ```jsx
        var x = 'global';
        
        function foo () {
          var x = 'function scope';
          console.log(x);
        }
        
        foo(); // function scope
        console.log(x); // global
        ```
        
    - 전역에 선언된 변수 x는 어디에든 참조할 수 있음
    - 함수 foo 내에서 선언된 변수 x는 함수 foo 내부에서만 참조할 수 있음
    - 스코프가 없다면 같은 식별자 이름끼리 충돌을 일으켜 프로그램 전체에서 같은 이름은 하나밖에 사용할 수 없음
        - 디렉토리가 없는 컴퓨터와 비슷 ⇒ 디렉토리가 없다면 같은 이름을 갖는 파일은 하나밖에 만들 수 없음
    - 스코프도 식별자 이름의 충돌을 방지함

## 2. 스코프의 구분

### 자바스크립트에서 스코프 구분

1. 전역 스코프(Global scope) : 코드 어디에서든지 참조할 수 있음
2. 지역 스코프(Local scope or Function-level scope) : 함수 코드 블록이 만든 스코프로 함수 자신과 하위 함수에서만 참조할 수 있음

### 변수의 관점에서 스코프

1. 전역 변수 (Global variable) : 전역에서 선언된 변수이며 어디에든 참조할 수 있음
2. 지역 변수 (Local variable) : 지역 내에서 선언된 변수이며 그 지역과 그 지역 하부 지역에서만 참조할 수 있음

## 3. 자바스크립트 스코프의 특징

자바스크립트의 스코프는 타 언어와는 다른 특징을 가지고 있음

- block-level scope : 코드 블록 내에서 유효한 스코프, 대부분의 C-family language가 이에 속함
- function-level scope : 함수 레벨 스코프, 함수 코드 블록 내에서 선언된 변수는 함수 코드 블록 내에서만 유효하고 함수 외부에서는 유효하지 않음, 자바스크립트가 이에 속함
    - ECMAScript 6에서 도입된 `let` 을 사용하면 블록 레벨 스코프를 사용할 수 있음

```jsx
var x = 0;
{
  var x = 1;
  console.log(x); // 
}
console.log(x);   // 

let y = 0;
{
  let y = 1;
  console.log(y); // 
}
console.log(y);   // 
```

- 정답
    
    ```jsx
    var x = 0;
    {
      var x = 1;
      console.log(x); // 1
    }
    console.log(x);   // 1
    
    let y = 0;
    {
      let y = 1;
      console.log(y); // 1
    }
    console.log(y);   // 0
    ```
    

## 4. 전역 스코프

- 전역에 변수를 선언하면 어디서든지 참조할 수 있는 전역 스코프를 갖는 전역 변수가 됨
- var 키워드로 선언한 전역 변수는 전역 객체(Global Object) window의 프로퍼티임

```python
var global = 'global';

function foo() {
  var local = 'local';
  console.log(global);
  console.log(local);
}
foo();

console.log(global); //?
console.log(local); //?
```

- 정답
    
    ```jsx
    var global = 'global';
    
    function foo() {
      var local = 'local';
      console.log(global);
      console.log(local);
    }
    foo();
    
    console.log(global);
    console.log(local); // Uncaught ReferenceError: local is not defined
    ```
    
- 자바스크립트는 타 언어와는 달리 특별한 시작점(Entry Point)가 없어서 위 코드와 같이 전역에 변수나 함수를 선언하기 쉬움

## 5.  비 블록 레벨 스코프 (Non block-level scope)

```python
if (true) {
  var x = 5;
}
console.log(x);
```

- 자바스크립트는 블록 레벨 스코프를 사용하지 않으므로 함수 밖에서 선언된 변수는 코드 블록 내에서 선언되어있을지라도 모두 전역 스코프를 갖게 됨

## 6. 함수 레벨 스코프 (Function-level scope)

```jsx
var a = 10;     // 전역변수

(function () {
  var b = 20;   // 지역변수
})();

console.log(a); // ?
console.log(b); // ?
```

- 자바스크립트는 함수 레벨 스코프를 사용하여 함수 내에서 선언된 매개변수와 변수는 함수 외부에서 유효하지 않음
- 함수 내 지역 영역에서는 전역과 지역 변수 모두 참조 가능
    - 중복된 경우 지역 변수 우선
- 정답
    
    ```jsx
    var a = 10;     // 전역변수
    
    (function () {
      var b = 20;   // 지역변수
    })();
    
    console.log(a); // 10
    console.log(b); // "b" is not defined
    ```
    

## 7.  내부 함수

- 함수 내 존재하는 함수
- 내부 함수는 자신을 포함하고 있는 외부함수의 변수에 접근할 수 있음
- 함수 영역에서 전역변수를 참조할 수 있으므로 전역 변수의 값도 변경할 수 있음
- 내부 함수의 경우 전역변수와 상위 함수에서 선언한 변수에 접근, 변경이 가능
- 중첩 스코프는 가장 인접한 지역을 우선하여 참조

```jsx
var x = 'global';

function foo() {
  var x = 'local';
  console.log(x);

  function bar() {  // 내부함수
    console.log(x); // ?
  }

  bar();
}
foo();
console.log(x); // ?
```

- 정답
    
    ```jsx
    var x = 'global';
    
    function foo() {
      var x = 'local';
      console.log(x);
    
      function bar() {  // 내부함수
        console.log(x); // local
      }
    
      bar();
    }
    foo();
    console.log(x); // global
    ```
    

```jsx
var foo = function ( ) {

  var a = 3, b = 5;

  var bar = function ( ) {
    var b = 7, c = 11;

// 이 시점에서 a는 3, b는 7, c는 11

    a += b + c;

// 이 시점에서 a는 21, b는 7, c는 11

  };

// 이 시점에서 a는 3, b는 5, c는 not defined

  bar( );

// 이 시점에서 a는 21, b는 5

};
```

## 7. 렉시컬 스코프

- 함수를 어디서 호출하였는지(동적 스코프)와 어디서 선언하였는지(렉시컬, 정적 스코프 : Lexical or static scope)에 따라 상위 스코프가 결정됨
- 자바스크립트는 렉시컬 스코프를 따름
    - 함수를 어디에 선언하였는지에 따라 결정

```jsx
var x = 1;

function foo() {
  var x = 10;
  bar();
}

function bar() {
  console.log(x);
}

foo(); // ?
bar(); // ?
```

- 정답
    
    ```jsx
    var x = 1;
    
    function foo() {
      var x = 10;
      bar();
    }
    
    function bar() {
      console.log(x);
    }
    
    foo(); // 1
    bar(); // 1
    ```
    

## 8. 암묵적 전역

- 선언하지 않은 식별자에 값을 할당하는 경우 전역 객체의 프로퍼티가 됨
- 이 현상을 암묵적 전역이라고 함

```jsx
var x = 10; // 전역 변수

function foo () {
  // 선언하지 않은 식별자
  y = 20;
  console.log(x + y);
}

foo(); // 30
```

- y는 window.y = 20으로 해석
- 변수 선언 없이 전역 객체의 프로퍼티로 추가되었을 뿐 변수가 아님
- 따라서 호이스팅이 발생하지 않음
- 이 경우 `delete y` 로 삭제할 수 있음
- 전역 변수는 프로퍼티지만 delete 연산자로 삭제할 수 없음

```jsx
var x = 10; // 전역 변수

function foo () {
  // 선언하지 않은 변수
  y = 20;
  console.log(x + y);
}

foo(); // 30

console.log(window.x); // 10
console.log(window.y); // 20

delete x; // 전역 변수는 삭제되지 않는다.
delete y; // 프로퍼티는 삭제된다.

console.log(window.x); // 10
console.log(window.y); // undefined
```

## 9. 최소한의 전역 변수 사용

- 전역 변수 사용을 최소화하는 방법 중 하나는 전역 변수 객체 하나를 만들어 사용하는 것 (더글라스 크락포드의 제안)

```jsx
var MYAPP = {};

MYAPP.student = {
  name: 'Lee',
  gender: 'male'
};

console.log(MYAPP.student.name);
```

## 10. 즉시 실행 함수를 이용한 전역변수 사용 억제

- 즉시 실행 함수(IIFE, Immediately-Invoked Function Expression)를 사용할 수 있음
- 이 경우 전역변수를 만들지 않아 라이브러리 등에 자주 사용됨
- 즉시 실행 함수는 즉시 실행되고 그 후 전역에서 바로 사라짐

```jsx
(function () {
  var MYAPP = {};

  MYAPP.student = {
    name: 'Lee',
    gender: 'male'
  };

  console.log(MYAPP.student.name);
}());

console.log(MYAPP.student.name);
```

https://developer.mozilla.org/ko/docs/Glossary/IIFE

## 참고 자료

https://poiemaweb.com/js-scope