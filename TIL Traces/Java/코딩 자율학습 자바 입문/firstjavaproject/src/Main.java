import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("정수를 입력하세요. --> ");
        int intNum = scan.nextInt();

        System.out.print("실수를 입력하세요. --> ");
        double doubleNum = scan.nextDouble();

        int add = intNum + (int)doubleNum;
        double sub = intNum - doubleNum;
        double mul = intNum * doubleNum;
        int div = intNum / (int)doubleNum;
        System.out.println("덧셈 결과(정수): "+ add);
        System.out.println("뺄셈 결과(실수): "+ sub);
        System.out.println("곱셈 결과(실수): "+ mul);
        System.out.println("나눗셈 결과(정수): "+ div);

    }
}