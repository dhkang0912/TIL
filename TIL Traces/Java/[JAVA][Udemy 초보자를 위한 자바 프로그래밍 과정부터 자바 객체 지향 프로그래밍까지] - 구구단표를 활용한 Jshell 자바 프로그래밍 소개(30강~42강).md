## [JAVA][Udemy 초보자를 위한 자바 프로그래밍 과정부터 자바 객체 지향 프로그래밍까지] - 구구단표를 활용한 Jshell 자바 프로그래밍 소개(30강~36강)
### 자바 대입 연산자
- 아래와 같이 선언 이후 특정 값을 할당하는 경우 =는 같다는 의미가 아닌 j의 값이 i라는 메모리 장소로 복사되는 것을 의미함
- 할당은 한 변수의 값을 다른 변수에 복사할 때 사용됨
- 왼쪽의 값은 무조건 변수여야 함
- 변수에 값을을 넣어야 함
- 오른쪽에 변수를 넣으면 그 변수의 값이 복사되어 할당되는 것

```
jshell> int i = 10
i ==> 10

jshell> int j = 15
j ==> 15

jshell> i = j
i ==> 15

jshell> i
i ==> 15

jshell> j
j ==> 15

jshell> i = j * 2
i ==> 30

jshell> j
j ==> 15

jshell> i
i ==> 30

jshell> i = i* 2
i ==> 60

```

### 자바 대입 연산자 - 증가, 감소, 복합에 관한 퍼즐
- 증감연산자
```
// 증가연산자
jshell> int number = 5
number ==> 5

jshell> number = number +1
number ==> 6
 
jshell> number++
$72 ==> 6

jshell> number
number ==> 7

// 감소연산자
jshell> number--
$74 ==> 7

jshell> number
number ==> 6

```

- 복합 할당연산자
=> 연산 후 변수에 바로 할당함
```
jshell> i = i + 2
i ==> 64

jshell> i += 2
$77 ==> 66

jshell> i -= 2
$78 ==> 64

jshell> i /= 4
$79 ==> 16

jshell> i %= 2
$80 ==> 0
```

### Jshell 단축키, 여러개의 코드줄 및 변수
- 18년도 전에는 Jshell 없이 자바를 처음 다룰 때 바로 확인하기에는 복잡했음
- Jshell은 히스토리 기능을 지원함, 위 아래 키로 이미 실행했던 명령어를 확인할 수 있음
- ctrl + A = 첫 부분
- ctrl + E = 끝 부분
- ctrl + R = 명령어 검색
- 명령어를 완전히 완성하지 않고 엔터를 치면 다음줄로 넘어가서 이어서 작성할 수 있음
- 자바는 완성할 때 ;을 항상 넣어줘야 하지만 Jshell에서는 넣지 않아도 알아서 인식함
- 여러 조건을 한 줄에 넣을 때는 ;을 넣어서 구분해줘야 함
- 종료할 때는 /exit
- Jshell을 킬 때는 jshell이라고 입력하면 됨
- 선언을 하지 않고 식만 적으면 jshell이 알아서 변수를 만들어서 넣어줌

```
jshell> 3*4
$84 ==> 12

jshell> $84
$84 ==> 12
```

### 33.5강 Quiz
Q1. Java에서 문자 변수에 단일 문자 기호를 저장하는 올바른 방법은 무엇인가요?
A1. Java에서 작은따옴표('')는 단일 문자 리터럴을 나타내는데 사용됩니다. 따라서 문자 변수에 단일 문자를 저장하려면 해당 문자를 작은 따옴표로 묶어야 합니다. 큰따옴표는("") 문자열을 나타냅니다. 괄호()는 메서드 정의 및 메서드 호출에 사용됩니다.


### 자바 조건문과 if문
- 자바에서 반복문을 사용하기 위해서는 초기값, 조건문, 업데이트 조건을 작성해야함
  - ```
  for (initialization; conditionl; update)
    satatement;```

- condition, 조건문이란?
  - 특정 조건을 참, 거짓(boolean)으로 나타내어 그 경우에만 특정 명령을 하도록 설정하는 것
  - ```
  if (condition)
      statement```
  - 조건문에 해당할 때만 아래 글이 프린트 됨  
  ``` 
  jshell> i = 4
  i ==> 4

  jshell> if (i<5)
     ...> System.out.println("i is less than 5")
  i is less than 5

  jshell> i = 10
  i ==> 10

  jshell> if (i<5)
     ...> System.out.println("i is less than 5")
 ```
 
 - 조건문으로 비교 할 때 할당 연산자가 아니라 비교 연산자를 사용해야함
   - 같은 지 비교하는 비교 연산자  : ==

  <br>
  
### 자바 구구단표 출력을 위한 반복문
- {} 블록 안에서 구문을 끝내기 위해서는 세미콜론을 넣어야 함
- 반목문에서는 초기 변수 설정, 반복 조건 설정, 한 구문을 돈 이후 증가 혹은 감소 업데이트를 작성해야 함
- 각 중간에는 ;으로 구분을 둬야 함
- 조건은 반복할 조건임, 조건에 맞아야만 반복문이 실행됨

```
jshell> for (int i = 0; i<=10; i++){
   ...>     System.out.printf("%d * %d = %d", 5, i, 5*i).println();
   ...> }
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```

### 반복문 연습하기
```
// 구구단 6단 출력하기
jshell> for (int i = 1; i<=10; i++){
   ...>     System.out.printf("%d * %d = %d", 6, i, 6*i).println();}
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60

// 구구단 10단 출력하기
jshell> for (int i = 1; i<=10; i++){
   ...>     System.out.printf("%d * %d = %d", 10, i, 10*i).println();}
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100

// table을 변수에 저장하여 구구단표 출력하기
jshell> int table = 7
table ==> 7

jshell> for (int i = 1; i<=10; i++){
   ...>     System.out.printf("%d * %d = %d", table, i, table*i).println();}
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70

jshell> table = 9
table ==> 9

jshell> for (int i = 1; i<=10; i++){
   ...>     System.out.printf("%d * %d = %d", table, i, table*i).println();}
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90

// 10부터 1까지 감소하기
jshell> for (int i=10; i>0; i--){
   ...>     System.out.println(i);}
10
9
8
7
6
5
4
3
2
1

// 1~10 중에 짝수인 것만 제곱값을 출력하기
jshell> for (int i=1; i<=10; i++){
   ...>     if (i%2==0){
   ...>         System.out.println(i*i);
   ...> }
   ...>     }
4
16
36
64
100

// 1~10 중에 홀수인 것만 제곱값을 출력하기
jshell> for (int i=1; i<=10; i++){
   ...>     if (i%2==1){
   ...>         System.out.println(i*i);
   ...> }
   ...>     }
1
9
25
49
81

```

 - 빈 문 : for문 안에 ;; 두개로 영역만 나눠도 실행 가능
 ```
 // 무한 루프를 돌게 됨 => ctrl + c로 빠져나올 수 있음
for(;;);
 ```
 ```
 // i를 증가시키기만 함
  for (;i<=10;i++);

  jshell> i
  i ==> 11
 ```

- 초기값, 업데이트 조건 여러개 걸기
```
jshell> for (i=1,j=2; i<=10; i++, j++);

jshell> i
i ==> 11

jshell> j
j ==> 12
```

- if, for문을 쓸 때는 실행 구문을 {} 블록으로 감싸는게 좋음, 가독성이 훨씬 좋아지고 그래야 의도대로 제대로 실행될 수 있음

<br>

### 복습 겸 보충
- 자바 리터럴이란?
Java 리터럴은 코드에서 상수로 지정하는 모든 값입니다. integer , float , double , long , String , char 또는 boolean 등 모든 유형이 될 수 있습니다 .
  - [참고자료](https://recordsoflife.tistory.com/902)
  

 


