package ch08_selfCheck;

public interface BankAccount {
    void withdraw(double amount); // 출금
    void deposit(double amount); // 입금
    void displayAccountInfo(); // 계좌 정보 출력 메서드
}
