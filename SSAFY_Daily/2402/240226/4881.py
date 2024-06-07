def perm(k):
    global minV
    if k == N:
        # print(col_lst)
        sum = 0
        for i in range(N):
            sum += arr[i][col_lst[i]]
        # print(sum, minV)
        if minV > sum:
            minV = sum
        return
    for col in range(N):
        if visited[col] == 0:
            col_lst[k] = col
            visited[col] = 1
            perm(k+1)
            visited[col] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col_lst = [-1] * N
    visited = [0] * N
    minV = 10*N
    # print(arr)
    perm(0)
    print(f'#{tc}', minV)
