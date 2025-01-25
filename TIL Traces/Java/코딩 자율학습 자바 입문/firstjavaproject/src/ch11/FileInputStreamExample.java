package ch11;

import java.io.FileInputStream;
import java.io.IOException;

public class FileInputStreamExample {
    public static void main(String[] args){
        try (FileInputStream fis = new FileInputStream("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/txt.txt")){
            int data;
            while ((data = fis.read())!=-1){
                System.out.print((char) data);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
