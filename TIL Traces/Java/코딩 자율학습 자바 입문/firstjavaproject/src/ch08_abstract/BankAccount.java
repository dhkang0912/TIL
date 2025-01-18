package ch08_abstract;

public abstract class BankAccount {
    // 필드 선언
    String accountNumber; // 계좌번호
    double balance; // 잔액

    // 생성자 (객체를 초기화하는 메서드)
    public BankAccount(String accountNumber, double initialBalance){
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    // 추상 메서드 (입출금 메서드)
    public abstract void withdraw(double amount);
    public abstract void deposit(double amount);

    // 계좌 정보 출력 메서드
    public void displayAccountInfo(){
        System.out.println("계좌번호: " + accountNumber);
        System.out.println("잔액: " + balance + "원");
    }
}
