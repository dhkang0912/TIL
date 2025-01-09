import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("학년을 입력하세요.");
        Scanner scanGrade = new Scanner(System.in);
        int grade = scanGrade.nextInt(); // 학년을 입력받기

        if (grade == 4){
            System.out.println("점수를 입력하세요.");
            Scanner scanScore = new Scanner(System.in);
            int score = scanScore.nextInt(); // 점수 입력받기

            if (score >= 90){
                System.out.println("장학금 지급 대상입니다.");
            } else {
                System.out.println("장학금 지급 대상이 아닙니다.");
            }
        } else {
            System.out.println("장학금 지급 학년이 아닙니다.");
        }

    }
}