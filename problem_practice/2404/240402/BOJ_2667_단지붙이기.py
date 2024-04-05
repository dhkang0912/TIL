'''
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

입력 > N => N*N

'''
from collections import deque
def bfs(row, col):
    global cnt
    Q = deque()
    Q.append((row, col))
    arr[row][col] = 0
    cnt += 1
    while Q:
        row, col = Q.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            New_row = row + dr
            New_col = col + dc
            if 0 <= New_row <= N-1 and 0 <= New_col <= N-1:
                if arr[New_row][New_col] == 1:
                    Q.append((New_row, New_col))
                    cnt += 1
                    arr[New_row][New_col] = 0


N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
# print(arr)
cnt_lst = []
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            cnt = 0
            bfs(row, col)
            cnt_lst.append(cnt)

print(len(cnt_lst))
cnt_lst.sort()
for cnt in cnt_lst:
    if cnt != 0:
        print(cnt)
