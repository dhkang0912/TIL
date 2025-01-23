package ch10;

public class Generic<T> {
        private T content;

        public void setContent(T content){
            this.content = content;
        }

        public T getContent(){
            return content;
        }

    public static void main(String[] args) {
        Generic<String> box = new Generic<>() ; // String형의 Box 객체 생성
        box.setContent("Hello, World!"); // 문자열 저장
        String content = box.getContent(); // 형변환 불필요
        System.out.println(content);
    }
}
