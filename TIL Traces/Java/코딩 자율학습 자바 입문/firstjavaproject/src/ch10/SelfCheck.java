package ch10;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class SelfCheck {
    public static void main(String[] args){
        // 1. ArrayList
        ArrayList<String> students = new ArrayList<>();
        students.add("홍길동");
        students.add("김길벗");
        students.add("이코천");
        students.add("홍길동");

        System.out.println("1. ArrayList 출력: " + students);
        System.out.println("학생 명단 : ");
        for (String student:students) { // 향상된 for문으로 명단 출력
            System.out.println(student);
        }

        // 2. HashSet
        // HashSet을 ArrayList students로 초기화
        HashSet<String> students2 = new HashSet<>(students);
        students2.add("강남순");

        System.out.println("2. HashSet 출력: " + students2);
        System.out.println("학생 명단(중복 삭제) : ");
        for (String student:students2){
            System.out.println(student);
        }

        // HashSet으로 HashMap 만들기
        HashMap<String , Integer > studentsScore = new HashMap<>();
        studentsScore.put("홍길동", 85);
        studentsScore.put("김길벗", 92);
        studentsScore.put("이코천", 78);
        studentsScore.put("강남순", 90);
        System.out.println("3. HashMap 출력: " + studentsScore);
        System.out.println("4. 홍길동 확인: " + studentsScore.get("홍길동"));
        System.out.println("학생 명단과 점수 : ");
        for (String key: studentsScore.keySet()){
            System.out.println(key + "의 점수" + studentsScore.get(key) + "점");
        }





    }
}
