package BOJ_1149;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); // 집 개수 입력 받기
        int[][] RGB = new int[N][3]; // 이차원 배열 받기

        // RGB 비용 입력 받기
        for (int i = 0; i < N; i++){
            RGB[i][0] = scan.nextInt(); // 빨강비용
            RGB[i][1] = scan.nextInt(); // 초록비용
            RGB[i][2] = scan.nextInt(); // 파랑비용
        }
        scan.close(); // Scanner 닫기

        int [][] dp = new int[N][3];
        // 첫번째 집 초기화
        dp[0][0] = RGB[0][0];
        dp[0][1] = RGB[0][1];
        dp[0][2] = RGB[0][2];

        for (int i=1; i < N ; i++){
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + RGB[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + RGB[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + RGB[i][2];
        }

        System.out.println(Math.min(dp[N-1][0], Math.min(dp[N-1][1], dp[N-1][2])));
    }
}

//package BOJ_1149;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.Scanner;
//import java.util.StringTokenizer;
//
//public class Main {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
//        int N = Integer.parseInt(br.readLine()); // 집 개수 입력 받기
//        int[][] RGB = new int[N][3]; // 이차원 배열 받기
//
//        // RGB 비용 입력 받기
//        for (int i = 0; i < N; i++){
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            RGB[i][0] = Integer.parseInt(st.nextToken()); // 빨강비용
//            RGB[i][1] = Integer.parseInt(st.nextToken()); // 초록비용
//            RGB[i][2] = Integer.parseInt(st.nextToken()); // 파랑비용
//        }
//
//        int [][] dp = new int[N][3];
//        // 첫번째 집 초기화
//        dp[0][0] = RGB[0][0];
//        dp[0][1] = RGB[0][1];
//        dp[0][2] = RGB[0][2];
//
//        for (int i=1; i < N ; i++){
//            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + RGB[i][0];
//            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + RGB[i][1];
//            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + RGB[i][2];
//        }
//
//        System.out.println(Math.min(dp[N-1][0], Math.min(dp[N-1][1], dp[N-1][2])));
//    }
//}
