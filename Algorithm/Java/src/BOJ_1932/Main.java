//package BOJ_1932;
//
//import java.util.Scanner;
//
//public class Main {
//    public static void main(String[] args){
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        int[][] triangle = new int[n][n];
//
//        for (int i = 0; i<n; i++){
//            for (int j=0; j<=i;j++){
//                triangle[i][j] = sc.nextInt();
//            }
//        }
//        sc.close();
//        System.out.println(dp(n, triangle));
//    }
//
//    public static int dp(int n, int[][] triangle){
//        int [][] dp = new int[n][n];
//        dp[0][0] = triangle[0][0];
//        for (int i = 1; i<n; i++){
//            for (int j = 0; j<=i; j++){
//                if (j==0){
//                    dp[i][j] = dp[i-1][j] + triangle[i][j];
//                } else if (j==i) {
//                    dp[i][j] = dp[i-1][j-1] + triangle[i][j];
//                } else {
//                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];
//                }
//            }
//        }
//
//        int maxSum = 0;
//        for (int j = 0; j < n; j++){
//            maxSum = Math.max(maxSum, dp[n-1][j]);
//        }
//
//        return maxSum;
//
//    }
//
//}

package BOJ_1932;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] triangle = new int[n][n];

        for (int i = 0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<=i;j++){
                triangle[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        br.close();
        System.out.println(dp(n, triangle));
    }

    public static int dp(int n, int[][] triangle){
        int [][] dp = new int[n][n];
        dp[0][0] = triangle[0][0];
        for (int i = 1; i<n; i++){
            for (int j = 0; j<=i; j++){
                if (j==0){
                    dp[i][j] = dp[i-1][j] + triangle[i][j];
                } else if (j==i) {
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j];
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];
                }
            }
        }

        int maxSum = 0;
        for (int j = 0; j < n; j++){
            maxSum = Math.max(maxSum, dp[n-1][j]);
        }

        return maxSum;

    }

}

