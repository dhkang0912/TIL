# 10966_물놀이를 가자
import sys
sys.stdin = open("10966_물놀이를가자_input.txt", "r")

from collections import deque

'''
지도는 N*M 크기의 격자로 표현
물이면 W, 땅이면 L
-> 시작을 어디서 해...? 모든 땅에서 물로 가야함
    -> 이게 어려우니까 쌤이 힌트 준 게 모든 물에서 방문하지 않은 땅을 간다.
-> 상하좌우에 있는 칸으로 이동하여 다른 칸으로 이동할 수 있음
-> 격자 밖으로 나가는 것은 안됨
-> 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램

<입력>
테스트 케이스 수 T가 주어짐
N = 행, M = 열
'''
def bfs(Q):
    visited = [[0]*M for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    move_sum = 0

    while Q:
        current_R, current_C = Q.popleft()
        for i in range(4):
            next_R = current_R + dr[i]
            next_C = current_C + dc[i]
            if (0 <= next_R <= N-1) and (0 <= next_C <= M-1) and not visited[next_R][next_C]:
                if pool[next_R][next_C] == 'L':
                    Q.append((next_R,next_C))
                    visited[next_R][next_C] = visited[current_R][current_C] + 1

    for row in range(N):
        for col in range(M):
            move_sum += visited[row][col]

    return move_sum



T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N = 행, M = 열
    pool = [input() for _ in range(N)]
    start_RC = deque()
        # print(pool)
    for row in range(N):
        for col in range(M):
            if pool[row][col] == 'W':
                start_RC.append((row, col)) # 모든 W가 시작점

    print(f'#{tc}', bfs(start_RC))