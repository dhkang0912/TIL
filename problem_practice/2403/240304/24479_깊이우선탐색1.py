import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(R):
    global cnt
    visited[R] = cnt

    for w in sorted(G[R]):
        if not visited[w]:
            cnt += 1
            dfs(w)


N, M, R = map(int, input().split()) # N = 정점의 갯수, M = 간선의 수, S = 시작 정점
G = [[] for _ in range(N+1)] #1~N까지 정점
visited = [0] * (N+1)
# print(G)
cnt = 1

for i in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)


dfs(R)
print(visited)

for i in range(1, N+1):
    print(visited[i])