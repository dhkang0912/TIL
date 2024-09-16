# use Strict

- use Strict을 통해 strict mode를 활성화할 수 있음
- 최상단에 작성하면 해당 파일이 strict mode가 됨 ⇒ 대개 스크립트 전체에 적용함
- 만약 함수 본문 맨 앞에 오면 해당 함수만 strict mode로 진행됨
- strict mode가 되면 취소할 방법은 없음

```jsx
"use strict";
```

# strict mode 시 변경 사항

1. 기존에는 조용히 무시되던 에러들을 보여줌
    - 선언 전 할당
        
        ```jsx
        "use strict";
        myFunction();
        
        function myFunction() {
          y = 3.14;   // This will also cause an error because y is not declared
        }
        ```
        
    - 변수(또는 개체)는 삭제할 수 없음
        
        ```jsx
        "use strict";
        let x = 3.14;
        delete x;                // This will cause an error
        ```
        
    - 같은 매개변수 이름을 사용할 수 없음
        
        ```jsx
        "use strict";
        function x(p1, p1) {};   // This will cause an error
        ```
        
    - 8진법의 숫자는 허용되지 않음
        
        ```jsx
        "use strict";
        let x = 010;  
        ```
        
    - 8진법 이스케이프 문자는 허용되지 않음
        
        ```jsx
        "use strict";
        let x = "\010";            // This will cause an error
        ```
        
    - 읽기 전용 속성에 값을 할당하려고 할 때 오류가 남
        
        ```jsx
        "use strict";
        const obj = {};
        Object.defineProperty(obj, "x", {value:0, writable:false});
        
        obj.x = 3.14;            // This will cause an error
        ```
        
    - 지울 수 없는 속성을 지우려고 할 때 오류가 남
        
        ```jsx
        "use strict";
        delete Object.prototype; // This will cause an error
        ```
        
    - eval(예약어)을 변수로 사용할 수 없음
        
        ```jsx
        "use strict"; // 엄격 모드 활성화
        
        let eval = 3.14; // 이 라인은 오류를 발생시킵니다.
        ```
        
    - arguments를 변수로 사용할 수 없음
        
        ```jsx
        "use strict";
        let arguments = 3.14; 
        ```
        
    - with문(객체의 모든 메서드를 접근 가능)을 허용하지 않음
        
        ```jsx
        "use strict";
        with (Math){x = cos(2)}; 
        ```
        
    - 보안적인 이유로 `eval()` 이 호출된 스코프에서 변수 생성이 허용되지 않음
        
        ```jsx
        "use strict";
        eval("x = 2");
        alert(x); // This will cause an error
        
        ```
        
        - `eval()`은 `var` 키워드로 변수를 선언할 수 없음
        
        ```jsx
        "use strict";
        eval("var x = 2");
        alert(x); // This will cause an error
        
        ```
        
        - `let` 키워드를 사용해 변수를 선언할 수 없음
        
        ```jsx
        eval("let x = 2");
        alert(x); // This will cause an error
        
        ```
        
2. 자바스크립트 엔진의 최적화 작업을 어렵게 만드는 실수들을 바로 잡음
    - 비 엄격 모드의 동일한 코드보다 더 빨리 작동하기도 함
3. ECMAScript의 차기 버전들에서 정의될 문법을 금지함

# use strict를 꼭 사용해야 하는가?

- 모던 자바스크립트는 `클래스`와 `모듈`  구조가 제공되어 자동적으로 `use strict` 가 적용됨
    - 이 경우 굳이 붙일 필요 없음

# 참고 자료

https://www.w3schools.com/js/js_strict.asp

https://codingeverybody.kr/자바스크립트-화살표-함수의-이해와-사용법/