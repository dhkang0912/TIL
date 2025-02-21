import sys
input = sys.stdin.readline

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = 1

    while Q:
        v = Q.popleft()
        for i in G[v]:
            if not visited[i]:
                visited[i]=1
                Q.append(i)


N, M = map(int, input().split())
# 1,1부터 시작할 수 있도록 처음은 비워놓고 정점보다 +1개의 이차원 리스트를 만든다.
G = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

# print(G)

# 1부터 시작하니 한개 더 많게 visited를 만들어주기
visited = [0]*(N+1)
# 0번은 확인한 것으로 만들어주기
visited[0]=1
cnt = 0

for i in range(1,N+1):
    if not visited[i]:
        cnt +=1
        bfs(i)
print(cnt)