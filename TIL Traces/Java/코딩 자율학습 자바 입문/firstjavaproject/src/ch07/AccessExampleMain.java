package ch07;

public class AccessExampleMain {
    public static void main(String[] args){
        AccessExample ae = new AccessExample();
        ae.publicMethod(); // 접근 가능
        ae.protectedMethod(); // 접근 가능
        ae.defaultMethod(); // 접근 가능
//        ae.privateMethod(); // 접근 불가능, 같은 클래스가 아님
    }
}
