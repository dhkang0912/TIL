package ch11;

public class StdOutputStreamExample {
    public static void main(String[] args){
        System.out.println("Hello java");
        int a = 10;
        int b = 20;
        System.out.printf("%d와 %d의 합: %d%n", a, b, a+b); // 서식을 지정해 출력
    }
}
