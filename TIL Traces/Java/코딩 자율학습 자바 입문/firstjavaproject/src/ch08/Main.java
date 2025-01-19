package ch08;

public class Main {
    public static void main(String[] args){
        Dog myDog = new Dog();
        // 자식 클래스와 부모 클래스의 필드 출력
        myDog.displayNames();
        // 부모 클래스의 메서드 호출 (부모 클래스의 name 필드 사용)
        myDog.printName();
    }
}
