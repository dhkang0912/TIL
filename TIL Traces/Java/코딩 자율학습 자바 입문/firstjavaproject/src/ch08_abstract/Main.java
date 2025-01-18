package ch08_abstract;

public class Main {
    public static void main(String[] args){
        // 입출금 계좌 객체 생성
        CheckingAccount myChecking = new CheckingAccount("123-4567890", 100000);
        myChecking.displayAccountInfo(); // 계좌 정보 출력

        myChecking.withdraw(100000); // 출금
        myChecking.deposit(50000); // 입금
    }
}
