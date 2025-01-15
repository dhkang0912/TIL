package ch07;

import java.time.Year;

public class Car {
//    클래스 변수
    static int countOfCars = 0; // 자동차 수량
//    인스턴스 변수
    String brand; // 브랜드
    int year; // 연식
    String color; // 색
//    기본 생성자
    public Car(){
        System.out.println("새로운 자동차 객체가 생성됐습니다.");
        //    인스턴스 메서드 호출
        this.carInfo();
    }

//    매개변수 2개 있는 생성자
    public Car(String brand, int year){
        System.out.println("새로운 자동차 객체가 생성됐습니다.");
        this.brand = brand;
        this.year = year;
        this.color = "white";
        this.carInfo();
    }

//    매개변수가 3개 있는 생성장
    public Car(String brand, int year, String color){
        System.out.println("새로운 자동차 객체가 생성됐습니다.");
        this.brand = brand;
        this.year = year;
        this.color = color;
    }

//    인스턴스 메서드
    public void carInfo(){
        System.out.println("---자동차 정보---");
        System.out.println("브랜드: " + brand);
        System.out.println("연식: " + year);
        System.out.println("색: " + color);

    }
//    클래스 메서드
    public static void countOfCarsInfo(){
        System.out.println("자동차 수량: " + countOfCars);
    }
}
