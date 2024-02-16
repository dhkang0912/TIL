'''
V E : V = 1~V번까지 V개의 정점, E = E개의 간선
E개의 간선정보

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, N):  # 시작정점 s, 노드개수 N
    q = []  # 큐
    visited = [0] * (N + 1)  # visited
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐가 비워질 때까지... (남은 정점이 있으면)
        v = q.pop(0)
        # t에서 할일 ....
        print(v)
        for i in adjl[v]:  # t에 인접인 정점
            if visited[i] == 0:  # 방문하지 않은 정점이면
                q.append(i)  # 인큐
                visited[i] = i + visited[v]  # 방문 표시
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V + 1)] # vertax가 1번부터 있기 때문에 1개 더 생성

# 이렇게 2개씩 뽑아올 수도 있음
# for i in range(0, E*2, 2):
#     n1, n2 = arr[i], arr[i+1]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]  # 2개씩 묶어서 뽑아오는 방법
    adjl[n1].append(n2)
    adjl[n2].append(n1)  # 무방향 그래프, 양방향

bfs(1, V)