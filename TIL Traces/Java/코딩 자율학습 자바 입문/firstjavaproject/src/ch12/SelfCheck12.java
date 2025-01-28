package ch12;

import java.util.ArrayList;
import java.util.function.Predicate;

public class SelfCheck12 {
    public static void main(String[] args) {
        // 리스트를 생성하고 1~6 추가
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);

        // Predicate 인터페이스로 짝수인지 판별하는 람다식 정의
        Predicate<Integer> isEven = (n) -> n % 2 == 0;
        // 짝수만 필터링한 결과를 담을 리스트 생성
        ArrayList<Integer> evenNumbers = filterList(numbers, isEven);
        // 결과 출력
        System.out.println("짝수만 필터링한 결과: " + evenNumbers);
    }

    // 리스트를 받아 조건에 맞는 요소들만 반환하는 메서드
    public static ArrayList<Integer> filterList(ArrayList<Integer> list, Predicate<Integer> predicate) {
        ArrayList<Integer> filteredList = new ArrayList<>();
        for (Integer num : list) {
            if (predicate.test(num)) { // 조건에 맞는 검사
                filteredList.add(num); // 필터링한 결과 리스트에 담기
            }
        }

        return filteredList; // 필터링 결과 리스트 반환
    }
}
