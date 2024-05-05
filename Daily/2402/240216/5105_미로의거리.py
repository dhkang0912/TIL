# 5105_미로의거리
import sys
sys.stdin = open("5105_미로의거리_input.txt", "r")
'''
N*N 크기의 미로가 있음
출발지, 목적지가 주어짐
최소 몇칸을 지나야 알 수 있는지 확인

마지막 줄 2에서 출발,
0인 통로를 따라 이동
맨 윗줄의 3에 도착

1. 우선 출발할 수 있는 마지막줄에서 2를 찾아야 함
    for 문 써서 마지막 줄에 col만 바꿔서 찾으면 될 듯 -> 늘 마지막 줄에만 있는게 아니라서 이렇게 하면 안됨
    
2. 출발 row, 도착 col을 가지고 경로를 구하는 bfs 함수를 만듦
    2-1. visited도 이차원 리스트로 만들어서 각 위치에 갈 때까지 가야 하는 횟수를 저장, 처음 시작점에 1을 넣어줌
    2-2. 출발점에서 상하좌우에 갈 수 있는 곳이 어딘지 확인하고 갈 수 있고, 아직 안 갔으면 Q에 넣어주기
        그리고 visited[newR][newC] = visited[row][col] + 1
    2-3. 만약 새로운 visited[newR][newC] == 3이면 도착 -> return visited[newR][newC]에 담긴 횟수 -1
    2-4. 만약 도착을 할 수 없으면 0을 리턴
'''
def bfs(start_row, start_col):
    visited = [[0]*N for _ in range(N)]
    Q = []
    Q.append((start_row, start_col))
    visited[start_row][start_col] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        current_R, current_C = Q.pop(0)

        for i in range(4):
            next_R = current_R + dr[i]
            next_C = current_C + dc[i]
            if 0 <= next_R <= N-1 and 0 <= next_C <= N-1 and not visited[next_R][next_C]:
                if miro[next_R][next_C] == 0:
                    Q.append((next_R, next_C))
                    visited[next_R][next_C] = visited[current_R][current_C] + 1
                if miro[next_R][next_C] == 3:
                    return visited[current_R][current_C] - 1

    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    # print(miro)
    start_row = 0
    start_col = 0
    for row in range(N):
        for col in range(N):
            if miro[row][col] == 2:
                start_row = row
                start_col = col
                break

    print(f'#{tc}', bfs(start_row, start_col))


