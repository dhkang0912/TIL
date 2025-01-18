package ch08_interface;

public class Main {
    public static void main(String[] args){
        // 입출금 계좌 객체 생성
        CheckingAccount myChecking = new CheckingAccount("123-4567890", 100000, 0.02);
        myChecking.displayAccountInfo();
        myChecking.withdraw(100000);
        myChecking.deposit(50000);
        myChecking.addInterest();// 이자 계산 및 추가
        myChecking.displayAccountInfo();
    }
}
