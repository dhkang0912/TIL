# 1226_미로
# 선생님이 짜준 코드
import sys
sys.stdin = open("1226_미로1_input.txt", "r")

# def bfs(s):
#     Q = []
#     visited = [False] * (N+1)
#
#     Q.append(s)
#     visited[s] = [True]
#     while Q:
#         v = Q.pop(0)
#         print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = True

# 10개 tc, 사이즈는 16
# def bfs(stR, stC):
#     Q = []
#     visited = [[0]*N for _ in range(N)]
#
#     Q.append((stR, stC))
#     visited[stR][stC] = 1
#
#     while Q:
#         vR, vC = Q.pop(0)
#         for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
#             wR = vR + dr
#             wC = vC + dc
#
#             if 0 <= wR < N and 0 <= wC < N:
#                 if arr[wR][wC] == 3:
#                     return 1
#                 if arr[wR][wC] == 0 and not visited[wR][wC]:
#                     Q.append((wR, wC))
#                     visited[wR][wC] = 1
#                     # visited[wR][wC] = visited[vR][vC] + 1
#
#     return 0
#
#
#
#
# T = 10
# for tc in range(1, T+1):
#     tc = int(input())
#     N = 16
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     # print(arr)
#
#     for row in range(N):
#         for col in range(N):
#             if arr[row][col] == 2
#                 stR = row
#                 stC = col
#                 break
#
#
#     print(bfs(stR, stC))


# 내가 짠 코드
def bfs(start_row, start_col):
    Q = []
    visited = [[0]*N for _ in range(N)]
    Q.append((start_row, start_col))
    visited[start_row][start_col] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        current_row, current_col = Q.pop(0)

        for i in range(4):
            next_row = current_row + dr[i]
            next_col = current_col + dc[i]
            if not visited[next_row][next_col]:
                if miro[next_row][next_col] == 0:
                    Q.append((next_row, next_col))
                    visited[next_row][next_col] = 1
                if miro[next_row][next_col] == 3:
                    return 1

    return 0


T = 10
for tc in range(1, T+1):
    tc = int(input())
    N = 16
    miro = [list(map(int, input())) for _ in range(16)]
    start_row = 0
    start_col = 0

    for row in range(N):
        for col in range(N):
            if miro[row][col] == 2:
                start_row = row
                start_col = col
                break

    print(f'#{tc}', bfs(start_row, start_col))

