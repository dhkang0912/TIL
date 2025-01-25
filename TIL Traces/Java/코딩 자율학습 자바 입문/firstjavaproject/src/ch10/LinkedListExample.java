package ch10;

import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args){
        LinkedList<String> list = new LinkedList<>();
        list.addFirst("Apple"); // 맨 앞 Apple 삽입
        list.addLast("Banana"); // 맨 뒤 Banana 삽입
        list.push("Cherry"); // 맨 앞 Cherry 삽입
        System.out.println("1번 출력 - 리스트 상태: " + list); // 1번 출력 - 리스트
        System.out.println("2번 출력 - 첫번째 요소: " + list.getFirst()); // 2번 출력 - 첫번째 요소 출력
        list.pop(); // 맨 앞 요소 삭제 후 반환
        System.out.println("3번 출력 - 리스트 상태: " + list); //3번 출력 - 리스트
        list.removeLast(); // 맨 뒤 요소 삭제 후 반환
        System.out.println("4번 출력 - 리스트 상태: " + list); //4번 출력 - 리스트
        list.addLast("Durian"); // 맨 뒤 요소 추가
        System.out.println("5번 출력 - 리스트 상태: " + list); //5번 출력 - 리스트
        list.pop(); // 맨 앞 요소 삭제 후 반환
        System.out.println("6번 출력 - 리스트 상태: " + list); //6번 출력 - 리스트
        System.out.println("7번 출력 - 첫번째 요소: " + list.getFirst()); //7번 출력 - 첫번째 요소 출력
        System.out.println("8번 출력 - 최종 리스트: " + list); //8번 출력 - 리스트

    }
}
