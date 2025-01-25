package ch11;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args){
        // try-with-resources 문법으로 FileWriter와 BufferedWriter 객체 생성
        // FileWriter 객체 생성 시 파일 명과 함께 두번째 인자를 true로 하면 append 모드로 열림 => 파일 끝에 새로운 내용 추가
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/txt.txt", true))){
            // 줄 바꿈을 파일에 추가
            writer.newLine();
            // 문자 추가
            writer.write("Hello, java");
            // 줄 바꿈을 파일에 추가
            writer.newLine();
            // 문자 추가
            writer.write("This is another line.");
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
