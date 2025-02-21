'''
토마토 3차원 배열
인접한 위, 아래, 왼쪽, 오른쪽, 앞 뒤 6방향 토마토
최소 일수를 확인하기

M : 가로 칸수, 열
N : 세로 칸수, 행 * 2배로 이차원 배열을 하는 것과 동일
H : 쌓인 상자의 수

3차원은 어떻게 생각해야하지? 방향이?
우, 좌, 하, 상, 앞, 뒤
directions = [(0,1),(0,-1),(1,0),(-1,0),(N,0),(-N,0)]
   0 1 2 3 4
0  0 0 0 0 0
1  0 0 0 0 0
2  0 0 0 0 0
3  0 0 0 0 0
4  0 0 1 0 0
5  0 0 0 0 0

'''
import sys
input = sys.stdin.readline

from collections import deque

def tomato_check(q, H, N, M):
    directions = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
    while q:
        z, r, c = q.popleft()
        for dz, dx, dy in directions:
            nz = z + dz
            nr = r + dx
            nc = c + dy
            if 0 <= nz < H and 0 <= nr < N and 0 <= nc < M and tomatos[nz][nr][nc] == 0:
                tomatos[nz][nr][nc] = tomatos[z][r][c] + 1
                q.append((nz, nr, nc))
    max_days = 0
    for z in range(H):
        for r in tomatos[z]:
            if 0 in r:
                return -1
            else:
                max_days = max(max(r), max_days)
    return max_days-1



# x : c, y : r, z : (r*c)*H, 
M, N, H = map(int, input().split())
# 3차원 배열 생성
q = deque()
tomatos = [[[0]*M for _ in range(N)] for _ in range(H)]
# print(tomatos)

for z in range(H):
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            tomatos[z][r][c] = row[c]
            if row[c] == 1:
                q.append((z,r,c))

if all(tomatos[z][r][c] != 0 for z in range(H) for r in range(N) for c in range(M)): # 행을 순회하며 행에 0이 없다면 True => 처음부터 다 익은 토마토인 경우
    print(0)
else:
    print(tomato_check(q, H, N, M))

