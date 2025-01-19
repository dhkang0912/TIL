package ch07;

public class Person {
    private String name;
    private int age;

//     생성자
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    public void displayInfo(){
        System.out.println("이름 : " + name);
        System.out.println("나이 : " + age);
    }

//    게터 메서드
    public String getName(){
        return name;
    }

    public int getAge(){
        return age;
    }

//    세터 메서드
    public void setName(String name){
        this.name = name;
    }

    public void setAge(int age){
        this.age = age;
    }



}
