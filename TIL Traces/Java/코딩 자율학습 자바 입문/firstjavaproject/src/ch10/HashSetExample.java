package ch10;

import java.util.HashSet;
import java.util.Iterator;

public class HashSetExample {
    public static void main(String[] args){
        HashSet<String> fruits = new HashSet<>(); // 객체 생성

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        System.out.println("집합 상태: " + fruits);
        fruits.add("Apple"); // 중복을 허용하지 않아 추가되지 않음
        System.out.println("집합 상태: " + fruits);
        System.out.println("집합 크기: " + fruits.size());

        System.out.println("Banana가 있는가? " + fruits.contains("Banana")); // 요소 여부 확인
        System.out.println("Banana가 삭제됐는가? " + fruits.remove("Banana")); // 요소 삭제 및 확인
        System.out.println("Banana가 있는가? " + fruits.contains("Banana")); // 요소 여부 확인
        System.out.println("집합 상태: " + fruits);
        System.out.println("집합이 비어 있는가? " + fruits.isEmpty());

        System.out.println("집합 요소: ");
        // Iterator 인터페이스를 통해 객체 생성 후 사용법
        Iterator<String> iterator = fruits.iterator();
        // hasNext() : 다음 요소가 있는지 확인하고 있으면 true
        while (iterator.hasNext()){
            // next() : 다음 요소를 반환
            System.out.println(iterator.next());
        }

        fruits.clear(); // 요소 전체 삭제
        System.out.println("최종 집합 크기: " + fruits.size());
        System.out.println("집합이 비어 있는가? " + fruits.isEmpty());

    }
}
