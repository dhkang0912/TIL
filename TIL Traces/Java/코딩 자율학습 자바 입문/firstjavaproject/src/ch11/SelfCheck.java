package ch11;

import java.io.*;

public class SelfCheck {
    public static void main(String[] args){
        try (BufferedReader br = new BufferedReader(new FileReader("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/inputTest.txt"))){
            String line;
            BufferedWriter bw = new BufferedWriter(new BufferedWriter(new FileWriter("/Users/sarah/Desktop/Coding/SSAFY/SSAFY Data/SSAFY_study/TIL/TIL Traces/Java/코딩 자율학습 자바 입문/firstjavaproject/src/ch11/outputTest.txt")));
            while ((line = br.readLine()) != null){
                System.out.println(line);
                bw.write(line);
                bw.newLine();
            }
            System.out.println("Writing Completed");
            bw.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
