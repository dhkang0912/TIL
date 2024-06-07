## [JAVA][Udemy 초보자를 위한 자바 프로그래밍 과정부터 자바 객체 지향 프로그래밍까지] - 자바 소개
> 원래 듣던 강의가 기존에 아는 것을 전제로 스킵하는 내용들이 많아서 udemy에 있는 다른 강의로 넘어가게 됐다. 
udmey에서 기존 듣고 있는 리액트 강의가 있는데 만족하며 듣고 있는 중이고 영어 강의에 익숙해지면 좋을 것 같아서 한국어 자막이 있는 영어 강의로 결제했다.
udemy에서 자바 기초 강의로 제일 유명한 인도 분이 하시는 강의인데 인도 억양이 좀 낯설고 어렵지만 언젠가 글로벌한 환경에서 일할 수 있으니 미리 익숙해져보는 계기로 삼으려고 한다.

### 강의 자료
[Java Course Guide, Course Presentation](https://github.com/in28minutes/course-material/blob/main/11-java-programming-for-beginners/downloads.md)
<br>

### 자바 설치하기
#### installing on Windows
- java jdk downloads
    - 설치 위치 저장해놓기
    - 윈도우 검색창에 환경 변수 설정하기 들어가기
    - 환경 변수에 들어가서 path를 설정하기
    - path를 선택 후 편집으로 들어가서 새로 만들기
    - 설치 위치에 들어가서 java 위치 > jdk-version > bin의 경로를 복사해서 추가하기
    - 해당 경로를 최상단으로 옮기고 저장하기
    - cmd 창에서 java -version 입력하면 설치한 자바 버전을 확인할 수 있음
    - jshell -version을 검색했을 때 error 없이 jshell 버전이 나온다면 제대로 설치 된 것

#### installing on Mac
- java jdk downloads
  - dmg 파일 다운로드
  - path 편집할 필요 없이 mac에서는 설치 후 바로 java -version과 jshell -version을 확인하면 됨
  - 종종 이전 버전으로 자바가 나올 때가 있는데 그럴 때는 공식 사이트의[installation instructions](https://docs.oracle.com/en/java/javase/22/install/overview-jdk-installation.html)를 확인하면 됨
  
<br>

### 프로그래밍을 통한 단계별 문제 해결
#### 1. Undestand the problem
#### 2. Design
  - Break the problem down
#### 3. Write your program (and test)
  - Express your solution : Language Specifics (syntax)

> 결국 큰 문제도 작게 쪼개서 단계별로 문제를 해결하는 게 중요하구나

<br>

### Jshell
- Java 9부터 사용 가능하게 바뀜
- Java REPL(Read Eval Print Loop) : 읽기, 분석, 출력, 반복
- 코드를 한줄 입력하면 그에 대한 결과가 바로 나옴
- 오류를 즉각적으로 알 수 있음
```
//jshell 들어가기 => terminal에서 명령어 입력
jshell

//jshell에서 빠져나오기 => terminal에서 명령어 입력
/exit
```
<br>

### 구구단표 과제
#### 구구단을 프로그래밍하는데 필요한 게 뭐가 있을가?
- jshell
- statements, 구문
- expression, 표현식
- variables, 변수
- literals 
- if statment
- for loop
- method/function

#### 문제를 해결하기 위해서는 어떻게 나눌 수 있을까?
- 5*5를 계산하는 것
- 이를 출력하는 것
- 이것을 변수로 숫자를 바꿔서 10번 반복하는 것

<br>

### 자바 표현식(expression)
- 표현식은 값을 계산하거나 결과를 반환하는 코드 조각, 값으로 평가됨
- 자바는 미리 정해진 연산자가 있음
- literal : 변하지 않는 값, 상수
- 프로그램 언어에는 precedence(우선순위)가 있음
  - \* / % 
  - \+ -
  
### 자바 구문(statement)
- 구문은 프로그램의 실행 단위로, 특정 작업을 수행하며 세미콜론(;)으로 끝남
- System.out.println() : 콘솔 창에 프린트 하는 메서드









