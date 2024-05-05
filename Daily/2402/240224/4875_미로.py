# import sys
# sys.stdin = open("4875_input.txt", "r")

def find_route(start):
    stack = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0]*N for _ in range(N)]
    stack.append(start)
    visited[start[0]][start[1]] = 1

    while stack:
        row_x, col_y = stack.pop()
        if arr[row_x][col_y] == 3:
            return 1

        for d in range(4):
            new_row = row_x+dr[d]
            new_col = col_y+dc[d]
            if 0 <= new_row <= N-1 and 0 <= new_col <= N-1 and arr[new_row][new_col] != 1:
                if not visited[new_row][new_col]:
                    stack.append((new_row, new_col))
                    visited[new_row][new_col] = 1
    return 0





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    # print(arr)

    # 시작점 찾기
    start_row = 0
    start_col = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                start_row = row
                start_col = col

    print(f'#{tc}', find_route((start_row,start_col)))




