'''
인접행렬
bfs, dfs 문제

입력
1. T 입력
2. M, N, K
M= 가로, N=세로, K=배추 위치

로직
bfs로 좌표 값으로 시작 0,0으로 시작
해당 좌표를 Q에 넣고 상하좌우 좌표 값이 1인 경우 해당 좌표를 Q에 넣음
들린 좌표를 0으로 바꿈 -> 이미 들린 곳, 다시 가지 않기 위해
count는 어떻게 하지? 한 bfs를 돌면 다른 곳으로 가기
시작점을 새로 넣을 때마다 cnt +1?

'''
def bfs(row, col):
    Q = [(row, col)]
    arr[row][col] = 0

    while Q:
        row, col = Q.pop(0)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row <= N-1 and 0 <= new_col <= M-1:
                if arr[new_row][new_col] == 1:
                    Q.append((new_row, new_col))
                    arr[new_row][new_col] = 0

T = int(input())

for tc in range(1, T+1):
    # M= 열, N=행, K=배추 위치
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    # print(arr)

    for _ in range(K):
        col, row = map(int, input().split())
        # 배추 있는 곳의 좌표를 1로 바꿈
        arr[row][col] = 1

    # print(arr)

    cnt = 0
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1:
                cnt += 1
                bfs(row, col)

    print(cnt)



