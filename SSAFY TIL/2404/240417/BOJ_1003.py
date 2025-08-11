'''
피보나치 함수

피보나치 수열을 재귀로 푸는 함수에 각각 fibo(1)과 fibo(0)이 몇번 사용되는지를 확인하는 함수가 필요하다

-> 재귀로 푸는 경우 무조건 시간초과가 나는 문제였다
사실 상 전형적인 DP문제로 점화식을 구해서 풀어야 한다
앞의 식과 앞앞 식이 계속 더해지는 것으로 당시 필요한 0, 1의 개수를 구하면 그것끼리 더하기만 하면 된다
'''

import sys
input = sys.stdin.readline

# def fibo(fibo_Num):
#     global fibo_0
#     global fibo_1
#
#     if fibo_Num == 0:
#         fibo_0 += 1
#         return memo[0]
#     elif fibo_Num == 1:
#         fibo_1 += 1
#         return memo[1]
#     else:
#         memo.append(memo[fibo_Num-1] + memo[fibo_Num-2])
#         return fibo(fibo_Num-1) + fibo(fibo_Num-2)
#
#
#
# N = int(input().strip())
# # 피보나치 함수를 N번 반복
# for tc in range(1, N+1):
#     fibo_0 = 0
#     fibo_1 = 0
#     memo = [0, 1]
#     fibo_Num = int(input().strip())
#     fibo(fibo_Num)
#
#     print(fibo_0, fibo_1)

T = int(input())
for tc in range(1, T+1):
    fibo_0_1 = [[1, 0], [0, 1], [1, 1]]
    fibo_num = int(input().strip())
    if fibo_num <= 2:
        print(*fibo_0_1[fibo_num])
    else:
        for i in range(3, fibo_num+1):
            fibo_0 = fibo_0_1[i-1][0] + fibo_0_1[i-2][0]
            fibo_1 = fibo_0_1[i-1][1] + fibo_0_1[i-2][1]
            fibo_0_1.append([fibo_0, fibo_1])
        print(*fibo_0_1[fibo_num])
