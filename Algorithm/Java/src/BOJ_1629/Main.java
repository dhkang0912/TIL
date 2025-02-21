package BOJ_1629;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        sc.close();

        System.out.println(power(A,B,C));
    }

    public static long power (long A, long B, long C){
        if (B == 1){
            return A%C;
        }
        long half = power(A, B/2, C);

        if (B%2==0) { //B가 짝수인 경우
            return (half * half) % C;
        } else { // B가 홀수인 경우, 오버플로우 방지
            return (((half * half) % C) * A) % C;
        }
    }
}
