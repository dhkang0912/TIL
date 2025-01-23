public class ObjectType {
        private Object content;

        public void setContent(Object content) {
            this.content = content;
        }

        public Object getContent() {
            return content;

    }

    public static void main(String[] args) {
        ObjectType box = new ObjectType(); // 내부 클래스 인스턴스 생성
        box.setContent("Hello, World!");
        Integer number = (Integer) box.getContent(); // 잘못된 타입 캐스팅
        System.out.println(number);
    }
}
