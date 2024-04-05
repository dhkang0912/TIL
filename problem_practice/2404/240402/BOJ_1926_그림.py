'''
그림의 개수, 그림의 넓이가 가장 넓은 것
단지 붙이기와 매우 유사

# 인풋
N*M 크기
arr
'''
from collections import deque

def bfs(row, col):
    global cnt
    Q = deque()
    Q.append((row, col))
    cnt += 1
    arr[row][col] = 0

    while Q:
        row, col = Q.popleft()
        for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            New_row = row + dr
            New_col = col + dc
            if 0 <= New_row <= N-1 and 0 <= New_col <= M-1:
                if arr[New_row][New_col] == 1:
                    cnt += 1
                    Q.append((New_row, New_col))
                    arr[New_row][New_col] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
cnt_lst = []

for row in range(N):
    for col in range(M):
        if arr[row][col] == 1:
            cnt = 0
            bfs(row, col)
            cnt_lst.append(cnt)

# print(cnt_lst)
print(len(cnt_lst))
if len(cnt_lst) == 0:
    print(0)
else:
    print(max(cnt_lst))