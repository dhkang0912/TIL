# 5102_노드의_거리
'''
V = 노드 개수
E = 간선 정보
출발 노드에서 최소 몇개의 간선을 지나면 도착 노드에 갈 수 있을까?
-> 출발에서 도착 노드로 가는 길의 길이를 알아야 함
간선으로 연결되지 않을 수 있음 -> 이건 어떤 의미일까? 가는 길이 없을 수 있음

'''
import sys
sys.stdin = open("5102_노드의거리_input.txt", "r")

def bfs(S, G):
    Q = []
    visited = [0] * (V+1)
    Q.append(S)
    visited[S] = 1

    while Q:
        v = Q.pop(0)
        # if v == G:
        #     return visited[v] - 1

        for w in line_info[v]:
            if not visited[w]:
                # if w == G:
                #     return visited[v]
                Q.append(w)
                visited[w] = visited[v]+1
                if w  == G:
                    return visited[w]-1
    return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line_info = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        line_info[v1].append(v2)
        line_info[v2].append(v1)

    S, G = map(int, input().split())

    # print(line_info)

    print(f'#{tc}', bfs(S, G))