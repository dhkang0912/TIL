import java.io.IOException;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        System.out.println("*** 자판기 실행화면은 다음과 같습니다.");
        Scanner scan = new Scanner(System.in);
        int balance = 0;
        while (true){
            System.out.println("현재 투입된 금액: " + balance);
            System.out.println("1. 콜라 (1,500원)");
            System.out.println("2. 오렌지주스 (2,000원)");
            System.out.println("3. 생수 (1,000원)");
            System.out.println("4. 종료");
            System.out.println("음료를 고르세요. (번호 입력)");
            int canNum = scan.nextInt();
            switch (canNum){
                case 1:
                    if (balance>=1500){
                        balance-=1500;
                        System.out.println("콜라를 선택했습니다. 남은 금액: "+balance + "원");
                    } else {
                        System.out.println("금액이 부족합니다. 돈을 더 투입하세요.");
                    }
                    break;
                case 2:
                    if (balance>=2000){
                        balance-=2000;
                        System.out.println("오렌지 주스를 선택했습니다. 남은 금액: "+balance+"원");
                    } else {
                        System.out.println("금액이 부족합니다. 돈을 더 투입하세요.");
                    }
                    break;
                case 3:
                    if (balance>=1000){
                        balance-=1000;
                        System.out.println("생수를 선택했습니다. 남은 금액: "+balance + "원");
                    } else {
                        System.out.println("금액이 부족합니다. 돈을 더 투입하세요.");
                    }
                    break;
                case 4:
                    System.out.println("프로그램을 종료합니다.");
                    scan.close();
                    return;
                default:
                    System.out.println("잘못된 번호입니다. 다시 선택해주세요.");
            }
            System.out.println("돈을 투입하세요. (0원 입력하면 메뉴로 돌아갑니다.)");
            int money = scan.nextInt();
            if (money>0){
                balance+=money;
            } else {
                System.out.println("메뉴로 돌아갑니다.");
            }

        }
    }
}