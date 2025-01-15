'''
토마토

익은 토마토의 상하좌우 토마토가 영향을 받음
토마토가 익는 최소 날짜
1 = 익은 토마토
0 = 익지 않은 토마토
-1 = 빈 곳

처음부터 다 익었으면 0, 모두 익지 못하면 -1

# 입력
- 가로 M 세로 N <= 1000
N*M
tomatos = [list(map(int, input().split()) for _ in range (N)]
visited = [0]*1000

# 로직
1. 처음 배열에 0이 들어있는지 확인하기
없으면 처음부터 모두 익은 토마토 => 0 출력
2. bfs를 통해 다 방문하려면 얼마나 걸리는지 확인하기

'''
import sys
input = sys.stdin.readline
from collections import deque

def tomato_check(tomatos, N, M):
    q = deque()

    # 큐에 모든 익은 토마토의 위치를 넣어줘야 함
    for i in range(N):
        for j in range(M):
            if tomatos[i][j]==1:
                q.append((i,j))

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            new_x = x+dx
            new_y = y+dy
            if 0 <= new_x < N and 0 <= new_y < M : # 범위 내에 있고
                if visited[new_x][new_y]==0 and tomatos[new_x][new_y]==0: # 방문 하지 않았고 익지 않은 토마토일 때
                    q.append((new_x,new_y))
                    tomatos[new_x][new_y] = 1
                    visited[new_x][new_y] = visited[x][y]+1
    
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                return -1
    
    return max(max(row) for row in visited)


M, N = map(int, input().split()) # 가로, 세로 => N*M
tomatos = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

if not any(0 in row for row in tomatos): # 익지 않은 토마토가 없으면 0 출력
    print(0)
else :
    print(tomato_check(tomatos, N, M))