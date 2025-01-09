import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("알파벳 소문자를 입력해주세요.");
        Scanner input = new Scanner(System.in);
        String alpabet = input.next();
        switch (alpabet){
            case ("a"):
                System.out.println("A");
                break;
            case ("b"):
                System.out.println("B");
                break;
            case ("c"):
                System.out.println("C");
                break;
            default:
                System.out.println("일치하는 알파벳이 없습니다.");
        }
        input.close();
    }
}