import sys
sys.stdin = open("7465_input.txt", "r")

def bfs(node):
    Q = [node]
    if visited[node] == 0:
        visited[node] = node

    while Q:
        V = Q.pop(0)

        for W in G[V]:
            if visited[W] == 0:
                Q.append(W)
                visited[W] = node



T = int(input())
for tc in range(1, T+1):
    # N = 마을 사람의 수(노드), M = 간선의 수
    N, M = map(int, input().split())

    # 0번 제외 (1번~N번까지 있음)
    G = [[] for _ in range (N+1)]
    # 그래프 받기
    for _ in range(M):
        v1, v2 = map(int, input().split())
        # 안다 = 무방향
        G[v1].append(v2)
        G[v2].append(v1)

    # print(G)

    # 0 번 제외
    visited = [0] * (N+1)

    for node in range(1, N+1):
        bfs(node)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] > 0 and visited[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')
