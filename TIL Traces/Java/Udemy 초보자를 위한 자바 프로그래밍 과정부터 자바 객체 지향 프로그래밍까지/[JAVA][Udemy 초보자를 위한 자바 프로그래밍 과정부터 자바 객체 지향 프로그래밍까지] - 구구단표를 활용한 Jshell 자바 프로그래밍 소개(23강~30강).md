## [JAVA][Udemy 초보자를 위한 자바 프로그래밍 과정부터 자바 객체 지향 프로그래밍까지] - 구구단표를 활용한 Jshell 자바 프로그래밍 소개(23강~30강)

### 변수 선언하기
- Declanation(선언)
- 선언을 하지 않으면 변수를 사용할 수 없음
- 할당하는 변수와 타입이 맞지 않다면 에러가 남
```
Type name = value
```

- Assignment(할당)
```
name = another value
```

### 피연산자 변수 활용
```
jshell> int i = 1
i ==> 1

jshell> System.out.printf("%d * %d = %d", 5,i , 5*i).println()
5 * 1 = 5

jshell> i = 2
i ==> 2

jshell> System.out.printf("%d * %d = %d", 5,i , 5*i).println()
5 * 2 = 10
```

### 24강 연습 문제
#### 변수 활용하여 식 작성해보기
```
jshell> int a = 12
a ==> 12

jshell> int b = 25
b ==> 25

jshell> int c = 45
c ==> 45

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
12 + 25 + 45 = 82

```

#### 다른 변수를 할당해보기
```
jshell> a = 90
a ==> 90

jshell> System.out.printf("%d + %d + %d = %d", a, b, c, a+b+c).println()
90 + 25 + 45 = 160

jshell> 
```
<br>

### 어떻게 변수가 메모리에 저장되는가?
- 메모리는 컴퓨터 용량에 따라 넣을 수 있는 용량이 다름
- 저장할 수 잇는 거대한 상자라고 생각하면 됨
- 이미 할당된 변수 a에 선언된 c를 할당하면 c의 메모리 주소 값이 a의 주소 값에 복사됨
- 각 변수마다 따로 메모리 위치를 가지고 있음
- 변수 유형은 프로그램 실행 중간에 변경할 수 없음
- 타입이 다른 값으로 변수를 할당할 수 없음 => 에러가 남


### 변수 이름 설정 방법
1. CamelCase : 첫 단어는 항상 소문자, 이어지는 단어는 항상 대문자
- ex : noOfGoals
- 다른 방식으로 변수명을 작성하는 것이 불가능한 것은 아니지만 이렇게 규칙을 정해서 CamelCase로 작성해야함
2. $, _, letters, numbers만 변수 이름으로 설정 가능
3. 변수 이름은 숫자로 시작할 수 없음
4. 변수 이름은 키워드(예약어)일 수 없음
5. 변수 이름의 길이는 제약이 없음
6. 설명이 없더라도 딱 봤을 때 이해할 수 있는 변수명을 짓는게 좋음
- 굳이 불필요하게 변수명을 줄이지 않아야 함

<br>

### 자바 기본 변수형 이해
- 자바에서 지원되는 정수형 데이터타입
1. byte 
- 8bit = 1byte
- -128 to 127
2. short 
- 16bit
- -32,768 to 32,767
3. int 
- 32bit
- -2,147,483 to 2,147,483,647
4. long 
- 64bit
- -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

<br>

- 그 외타입
1. float
- 32 bit
- decimal value (부동소수점)
- ±3.40282347E+38F. NOT precise
- ex : float f = 4.0f
- float로 쓸 거면 뒤에 f를 꼭 붙여야 함
- 정확한 숫자가 아니라서 financial에는 사용하면 안됨 (이 경우 Bigdecimal 사용)

<br>

2. double
- 64bit
- 소수점 표현
- ±1.79769313486231570E+308. NOT precise
- double d = 67.0
- 상수이자 double value
- 정확한 숫자가 아니라서 financial에는 사용하면 안됨 (이 경우 Bigdecimal 사용)

<br>

3. char
- 16bit
- 한 글자만 저장 가능
- '\u0000 to '\uffff
- ex : char c = 'A';

<br>

4. boolean
- 1bit
- true or false
- 기본값이 false

<br>

### 문자열 결합
- 더하기를 정수 사이에 넣으면 덧셈을 시행
- 더하기를 문자열과 함께 넣으면 결합해줌

```
jshell> "1" + 2 + 3
$52 ==> "123"

jshell> "1" + (2+3)
$53 ==> "15"
```
```
jshell> int i = 5
i ==> 5

jshell> System.out.println("value of i is " + i)
value of i is 5
```



