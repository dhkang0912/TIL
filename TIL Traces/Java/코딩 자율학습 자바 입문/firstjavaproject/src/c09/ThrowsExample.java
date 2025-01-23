package c09;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class ThrowsExample {

    public static void main(String[] args){
        try {
            readFile("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/example.txt"); // 파일 읽기 메서드 호출
        } catch (IOException e){
            System.out.println(e);
        } finally {
            System.out.println("프로그램을 종료합니다.");
        }
    }

    // 예외 처리를 호출한 곳으로 넘김
    // readFile 메서드
    // IOException : FileNotFoundException와 같이 읽으려는 파일이 존재하지 않는 등의 오류가 발생할 수 있지만 상위 예외 클래스인 IOException만 적어도 모두 대응하게 됨
    public static void readFile(String fileName) throws IOException {
        // 파일을 읽기 위해 객체 생성
        File file = new File(fileName);
        // FileReader = 파일을 문자 단위로 읽는 클래스
        // BufferedReader = 버퍼(기본 8KB)를 사용해 한번에 많은 데이터를 읽어올 수 있는 클래스
        // file 객체를 FileReader로 읽어 FileReader를 객체를 생성하고 이를 BufferedReader 클래스에 전달
        // BufferedReader 클래스는 객체를 생성하고 FileReader 객체에 있는 데이터를 버퍼에 저장
        BufferedReader reader = new BufferedReader(new FileReader(file));
        // 버퍼에서 데이터를 한줄씩 가져와서 저장, 파일 끝에 도달하면 null을 반환
        String line = reader.readLine();

        // line에 저장된 주소가 null일 때까지 반복
        while (line != null){
            // 저장된 한줄을 출력하고
            System.out.println(line);
            // 다음줄을 다시 line에 저장
            line = reader.readLine();
        }
        // 다 읽었으면 버퍼를 닫아줌
        reader.close();
    }
}
