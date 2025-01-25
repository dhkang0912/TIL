package ch11;

public class StdErrorStreamExample {
    public static void main(String[] args){
        try{
            int result = 10/0; // 오류 발생
        } catch (ArithmeticException e){
            // 오류 메시지는 표준 오류 스트림으로 출력
            System.err.println("Error: Division by zero!");
        }
        System.out.println("프로그램 실행 중");
    }
}
