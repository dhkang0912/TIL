import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        int score = 80;
        if (score >= 90){
            System.out.println("A학점입니다.");
        } else if (score < 90 && score>=80 ){
            System.out.println("B학점입니다.");
        } else if (score < 80 && score>=70 ){
            System.out.println("C학점입니다.");
        } else {
            System.out.println("D학점입니다.");
        }
    }
}