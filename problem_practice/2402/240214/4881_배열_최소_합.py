# 4881 배열 최소 합
# N*N 배열
# N개의 숫자를 골라 합이 최소
# 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없음
# 최소 합을 출력하는 프로그램을 만드시오
'''
3
2 1 2
5 8 5
7 2 2
'''

import sys
sys.stdin = open("4881_input.txt", "r")
def perm(k, sumV):
    global minV
    if k == N:
        if minV > sumV:
            minV = sumV

    if sumV > minV:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            perm(k+1, sumV+arr[k][i])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minV = 123e12
    perm(0,0)
    print(f'#{tc}', minV )


