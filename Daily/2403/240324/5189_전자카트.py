import sys
sys.stdin = open("5189_input (1).txt", "r")

def perm(level):
    global minv
    if level == N:
        arr_sum = 0
        for i in range(N-1):
            s = path[i]
            e = path[i+1]
            arr_sum += arr[s][e]
        arr_sum += arr[path[-1]][0]
        minv = min(minv, arr_sum)
        return

    for i in range(N):
        if not visited[i]:
            path[level] = i
            visited[i] = 1
            perm(level+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    visited = [0] * N
    path = [0] * N
    visited[0] = 1

    minv = float('inf')
    # 1에서 시작
    perm(1)
    print(minv)