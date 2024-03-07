import sys
input = sys.stdin.readline

def dfs(R):
    global cnt
    stack = []
    stack.append(R)
    # visited[R] = cnt

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = cnt
            cnt += 1

        for w in G[v]:
            if not visited[w]:
                stack.append(w)




N, M, R = map(int, input().split()) # N = 정점의 갯수, M = 간선의 수, S = 시작 정점
G = [[] for _ in range(N+1)] #1~N까지 정점
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
    # G[v1].sort(reverse=True)
    # G[v2].sort(reverse=True)

for G_ele in G:
    G_ele.sort(reverse=True)

# print(G)

dfs(R)

for i in range(1, N+1):
    print(visited[i])