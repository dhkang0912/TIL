package ch10;

public class Boxing {
    public static void main(String[] args){
        int a = 5;
        // 명시적 박싱
        Integer aObj = new Integer(a);

        // 오토 박싱
        int b = 10;
        Integer bObj = b;

        // 명시적 언박싱
        Integer numObj = new Integer(10);
        int num = numObj.intValue();

        // 오토 언박싱
        Integer numObj2 = 10;
        int num2 = numObj2;
    }
}
