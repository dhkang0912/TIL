package ch08;

public class Animal {
    // 필드
    String name = "동물";
    int age;

    public void printName(){
        System.out.println("부모 클래스의 name: " + name);
    }

    // 생성자
//    public Animal(String name, int age){
//        this.name = name;
//        this.age = age;
//        System.out.printf("이름 : %S%n나이: %d%n", this.name, this.age);
//    }

    // 메서드
    public void eat(){
        System.out.println(name + "가 밥을 먹습니다.");
    }

}
