'''
So sad...
연결되어있는 모든 컴퓨터는 웜 바이러스에 걸림 (bfs, dfs)

100 이하인 정수의 컴퓨터 수

인풋
1. 컴퓨터의 개수 T
2. 컴퓨터의 쌍 N열
-> 무방향

1번 컴퓨터가 바이러스에 걸렸을 때 그걸 통해서 바이러스가 걸리게 한 수를 출력
'''

def bfs(s):
    Q = [s]
    cnt = 0

    while Q:
        v = Q.pop(0)

        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w]=1
                cnt+=1
    return cnt



# 컴퓨터 개수
N = int(input())

# Node 개수
NodeN = int(input())

# for문 돌리면서 Graph 만들기
# 아 내가 생각하려고 하는 거 하려면 이차원 리스트로 만들어야 한다
G = [-1] + [[] for _ in range(N)]
visited = [1] + ([0] * N)
visited[1] = 1

for i in range(1, NodeN+1):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
# print(G)

print(bfs(1))
# print(visited)
# print(sum(visited[2:]))


