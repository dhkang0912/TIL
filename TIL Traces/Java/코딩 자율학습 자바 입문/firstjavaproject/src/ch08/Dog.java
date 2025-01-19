package ch08;

public class Dog extends Animal{
    String name = "강아지";
    String breed; // 견종

    public void displayNames(){
        // 자식 클래스의 name 필드 출력
        System.out.println("자식 클래스의 name:" + this.name);
        // 부모 클래스의 name 필드 출력
        System.out.println("부모 클래스의 name: " + super.name);
    }

//    public Dog(String name, int age, String breed) {
//        // 부모 클래스의 생성자 호출
//        super(name, age);
//        this.breed = breed;
//        System.out.println("품종: " + this.breed);
//    }

    public void roll(){
        System.out.println(name + "가 바닥을 구릅니다.");
    }

    public void roll(int times){
        System.out.printf("%S가 바닥을 %d번 구릅니다.%n", name, times);
    }
}
