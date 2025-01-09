'''
쉬운 최단 거리

지도의 모든 지점에서 목표 지점까지의 거리
가로와 세로로만 움직임 => 상하좌우로만 움직임

# 인풋
1. n*m이 주어진다
2. n개의 줄, m개의 숫자
n 행, m 열
이차원 배열로 인풋을 받는다
3. 0은 갈 수 없고 1은 갈 수 있고, 2는 목표지점

# 풀이
이렇게 어딘가로 가고 안 가고는 bfs, dfs를 통해서 했던 것 같긴 하다
그 지점을 연결해서 갈 수 있고 못 가고의 차이니까
목표 지점까지 거리니까 visited를 +1 해나갔던 것 같다
arr을 한개씩 돌면서 지금이 1이면 더 나아가서 확인하고
그 외 숫자면 0을 출력함

arr을 탐색할 때
1인 경우 상하좌우로 움직여서 쭉쭉 확인하기 => 재귀인가...?
그리고 만약 목표지점에 도달 못한다면 -1 찍기

우선 한번 쭉 돌아서 목표지점의 좌표를 알고 있어야 하는건가?

'''
# import sys
# sys.stdin = open("BOJ_14940_input.txt", "r", encoding="utf-8")
from collections import deque

n, m = map(int,input().split())

# input 한 줄 받은 걸 split으로 나눠서 넣고 그 걸 n행 반복
# 맞다 이렇게 해서 이차원 배열을 인풋 받았지
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

# 방문 여부를 표시할 visited 배열 생성
# m열의 세트를 n번 반복하여 생성
visited = [[0]*m for _ in range(n)]
# print(visited)

aim_x, aim_y = 0,0
# 목표 지점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            # 목표 지점 찾기
            aim_x, aim_y = i,j
        elif arr[i][j] == 0:
            # 갈 수 없는 곳 표현
            visited[i][j] = -1


# bfs 함수 만들기
def bfs(x, y):
    q = deque([(x,y)])
    visited[aim_x][aim_y] = 0

    while q:
        x, y = q.popleft()

        for i in [(0,1),(1,0),(0,-1),(-1,0)]:
            # 상하좌우로 움직여서 확인하기
            dx = x + i[0]
            dy = y + i[1]

            # 인덱스가 좌표 범위 안에 있고 갈 수 없는 -1이 아닌 가본 적 없는 곳인 0일때,
            # 그리고 목표 지점을 다시 가지 않기 위해 arr[dx][dy]가 1일때로 조건을 건다
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and arr[dx][dy] == 1 :
                q.append((dx, dy))
                # 지금 좌표의 거리보다 더 가서 확인한 거니 거리는 +1
                visited[dx][dy] = visited[x][y]+1
bfs(aim_x, aim_y)


# visited[aim_x][aim_y] = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            print(0, end=' ')
        elif visited[i][j] == 0 and arr[i][j] == 1:
            print(-1, end=' ')
        else :
            print(visited[i][j], end=' ')
    print()

