package ch07;

public class Main {
    public static void main(String[] args){
        Car car = new Car(); // 기본 생성자로 객체 생성
        System.out.println(""); // 구분을 위해 추가
        Car myCar = new Car("Hyundai", 2025); // 인자 2개 전달
        System.out.println("");
        Car yourCar = new Car("Kia", 2025, "Black"); // 매개변수 3개인 생성자 호출
        yourCar.carInfo();
    }
}
