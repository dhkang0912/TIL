## [JAVA][Udemy 초보자를 위한 자바 프로그래밍 과정부터 자바 객체 지향 프로그래밍까지] - 구구단표를 활용한 Jshell 자바 프로그래밍 소개

### Escape character
```
System.out.println("hello \"world")
// 출력
hello "world

System.out.println("Hello\nWorld")
// 출력
Hello
World
```

### Method
```
// 랜덤 숫자를 뽑아주는 method
jshell> Math.random()
$7 ==> 0.556040817515667

// min number를 알려주는 method
Math.min(23, 45)
$9 ==> 23
```

#### printf
- 계산된 값을 출력할 수 있음
- %d는 정수값이 계산되는 걸 표현하는 문자
- printf만 사용하는 경우 printstream으로 나오게 됨, 이걸 문자로 변환해주기 위해서 println과 함께 사용됨
```
jshell> System.out.printf("5 * 2 = %d", 5*2).println()
5 * 2 = 10

jshell> System.out.printf("%d %d  %d", 5, 7, 5*7).println()
5 7  35

jshell> System.out.printf("%d *  %d =  %d", 5, 7, 5*7).println()
5 *  7 =  35

jshell> System.out.printf("%d + %d +%d = %d", 6, 7, 8, 6+7+8)
6 + 7 +8 = 21$23 ==> java.io.PrintStream@30dae81

jshell> System.out.printf("%d + %d +%d = %d", 6, 7, 8, 6+7+8).println()
6 + 7 +8 = 21

jshell> 

```