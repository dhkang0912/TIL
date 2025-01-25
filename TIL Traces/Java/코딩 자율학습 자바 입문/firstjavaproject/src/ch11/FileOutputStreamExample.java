package ch11;

import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamExample {
    public static void main(String[] args){
        String data = "Hello World!";
        // 예외처리를 위해 try-catch 블록을 사용
        try {
            // FileOutputStream 객체를 생성해 스트림을 연다
            FileOutputStream fos = new FileOutputStream("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/txt.txt");
                fos.write(data.getBytes());
                fos.close();
            System.out.println("Writing Completed.");
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
