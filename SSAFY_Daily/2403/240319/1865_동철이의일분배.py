def perm(level, mutiple_percent):
    global max_percent

    if max_percent >= mutiple_percent:
        return

    if level == N:
        if max_percent < mutiple_percent:
            max_percent = mutiple_percent
        return

    for i in range(N): # N열 중 어떤 열을 뽑을지가 됨
        if not visited[i]:
            result[level] = i
            visited[i] = 1
            perm(level+1, mutiple_percent * arr[level][i]) # 다음 재귀로 넘어갈 때 꼭,,, +1 해주기, arr[index(행)][열, result에 추가할 열])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/100

    # print(arr)
    max_percent = 0
    result = [-1] * N
    visited = [0] * N
    perm(0, 1) # 시작 level과 mutiple_percent 초기값
    print(f'#{tc} {max_percent*100:6f}')