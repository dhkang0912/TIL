package ch08;

public class Cat extends Animal{
    public void rub(){
        System.out.println(name + "가 몸을 비빕니다.");
    }

    // 생성자
//    public Cat(String name, int age){
//        super(name, age);
//    }

    public void eat(){
        super.eat(); // 부모 클래스의 eat() 메서드 호
        System.out.println(name + "가 닭고기를 먹습니다.");
    }
}
