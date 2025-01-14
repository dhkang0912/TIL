import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
       int [][] scoreArray = {
               {85, 70, 90, 95},
               {80, 95, 90, 75},
               {75, 85,90, 80}
       };
        System.out.println("학생들의 성적은 다음과 같습니다.");
       for (int i=0; i<scoreArray.length; i++){
           int sum = 0;
           System.out.print("학생" + (i+1)+ " ");
           for (int j=0; j<scoreArray[0].length; j++){
               sum+=scoreArray[i][j];
           }
           double average = (double) sum / scoreArray[i].length;
           System.out.print("| 평균: " + average+ "\n");
       }
    }
}