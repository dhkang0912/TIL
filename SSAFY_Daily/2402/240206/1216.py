# [S/W 문제해결 기본] 3일차 - 회문2
# 가장 긴 회문의 길이를 구하는 문제
# 100 * 100의 배열
# 회문 길이는 M이라고 했을 때 가장 짧은 회문이 2, 그 다음이 3...그 다음이 100
# 각 칸에 들어갈 단어는 A,B,C로 제한
# 글자 판은 무조건 N*N
# A도 한글자짜리 회문으로 인정
# 가로, 세로 직선만 회문으로 인정
import sys
sys.stdin = open("1216_input.txt","r")


def check(arr, N, M):
    for row in range(N):
        for start in range(N - M + 1):
            if arr[row][start:start + M] == arr[row][start:start + M][::-1]:
                return M

    for col in range(N):
        col_list = []
        for row in range(N):
            col_list.append(arr[row][col])
        for start in range(N - M + 1):
            if col_list[start:start + M] == col_list[start:start + M][::-1]:
                return M
    return -1


T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(str, input())) for _ in range(N)]

    for M in range(99,0,-1):
        if check(arr,N,M) > 0:
            print(f'#{tc} {check(arr, N, M)}')
            break




