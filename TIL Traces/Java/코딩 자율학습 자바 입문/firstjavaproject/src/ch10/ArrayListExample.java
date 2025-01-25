package ch10;

import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<>();

        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        System.out.println(list.get(1));
        list.set(1, "Durian");
        System.out.println(list.get(1));
        list.remove(0);

        System.out.printf("리스트 크기: %d%n", list.size());
        System.out.printf("리스트가 비었는가? %b%n", list.isEmpty());
        System.out.println(list);

    }
}
