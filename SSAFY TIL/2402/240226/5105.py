def find_route(start_row, start_col):
    Q = []
    visited = [[0]*N for _ in range(N)]
    Q.append((start_row, start_col))
    visited[start_row][start_col] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        current_row, current_col = Q.pop(0)

        for d in range(4):
            new_row = current_row + dr[d]
            new_col = current_col + dc[d]
            if 0 <= new_row <= N-1 and 0 <= new_col <= N-1 and not visited[new_row][new_col]:
                if arr[new_row][new_col] == 3:
                    return visited[current_row][current_col] - 1
                if arr[new_row][new_col] == 0:
                    Q.append((new_row, new_col))
                    visited[new_row][new_col] = visited[current_row][current_col] + 1

    return 0





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int, input())) for _ in range(N)]
    # print(arr)
    start_row = 0
    start_col = 0
    # 시작지점 찾기
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                start_row = row
                start_col = col


    print(f'#{tc}', find_route(start_row, start_col))








