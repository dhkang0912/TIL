package ch10;

import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class HashMapExample {
    public static void main(String[] args){
        HashMap<String, Integer> map = new HashMap<>();

        map.put("Apple", 10);
        map.put("Banana", 15);
        map.put("Cherry", 20);
        map.put("Durian", 25);
        System.out.println("Apple의 수량: " + map.get("Apple"));

        map.remove("Banana");
        System.out.println("맵 상태: " + map);
        System.out.println("Cherry가 있는가? " + map.containsKey("Cherry"));
        System.out.println("값이 10인 항목이 있는가? " + map.containsValue(10));

        Set<String> keys = map.keySet();
        System.out.println("모든 키: " + keys);

        Collection<Integer> values = map.values();
        System.out.println("모든 값: " + values);
    }
}
