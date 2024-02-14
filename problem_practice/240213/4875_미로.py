def dfs(stR, stC):
    st = []
    visited = [[False] * N for _ in range(N)]
    st.append((stR, stC))
    visited[stR][stC] = True
    while st:
        vR, vC = st.pop()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newR = vR + dr
            newC = vC + dc
            if 0 <= newR < N and 0 <= newC < N and not visited[newR][newC] and arr[newR][newC] != 1:
                if arr[newR][newC] == 3:
                    return 1
                st.append((newR, newC))
                visited[newR][newC] = True
    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2 :
                stR = row
                stC = col
                break
    if dfs(stR,stC) :
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     Map = [list(map(int, input().strip())) for _ in range(N)]
#     check = [[0]*N for _ in range(N)]
#
#     sx = 0
#     sy = 0
#
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
#     for i in range(N):
#         for j in range(N):
#             if Map[i][j] == 2:
#                 sx = i
#                 sy = j
#
#     stack = [(sx, sy)]
#     check[sx][sy] = 1
#
#     result = 0
#     while stack:
#         x, y = stack.pop()
#         check[x][y] = 1
#         if Map[x][y] == 3:
#             result = 1
#             break
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and (Map[nx][ny] == 0 or Map[nx][ny] == 3) and check[nx][ny] == 0:
#                 stack.append((nx, ny))
#
#     print(f'#{tc+1} {result}')