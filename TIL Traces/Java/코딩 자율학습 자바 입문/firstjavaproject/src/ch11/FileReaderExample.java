package ch11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderExample {
    public static void main(String[] args){
        // FileReader 객체를 생성해 스트림을 열고 이를 인자로 받아 BufferedReader 객체를 생성
        // BufferedReader 객체는 스트림을 감싸서 FileReader 객체가 읽어온 데이터를 버퍼에 저장
        try(BufferedReader br = new BufferedReader(new FileReader("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/txt.txt"))){
            String line; // 읽어들인 텍스트 한 줄을 저장할 변수
            // BufferedReader 객체의 버퍼에서 텍스트 한줄씩 읽어와 line에 저장
            // 더 이상 줄이 없으면 null을 반환하기 때문에 null이 나올 때까지 반복
            while ((line = br.readLine())!=null){
                System.out.print(line);
            }
            // try-with-resources 문법에 의해 try 블록 완료 후 스트림이 자동으로 닫힘
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
