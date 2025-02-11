'''
트리의 부모 찾기

# 문제
트리의 루트 = 1, 각 노드의 부모를 구하는 프로그램을 작성

# 입력
1. N = 노드의 개수
2. N-1개의 줄에 트리 상에서 연결된 두 정점

# 출력
2번 노드부터 부모 노드 출력

'''

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


N = int(input())
nodes = [[] for _ in range(N+1)] # 1번부터 시작함, 1번부터 N번까지
parent = [0] * (N+1)
parent[1] = -1 # 1번은 부모 노드가 없음, 1번이 부모 노드

# print(nodes)

for _ in range(N-1):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)

# def dfs(node):
#     for neighbor in nodes[node]: # 현재 node와 연결되어 있는 모든 노드를 순회
#         if parent[neighbor] == 0 : # 만약 자식 노드의 부모 노드가 안 나왔으면 현재 노드가 부모 노드 (부모 노드부터 하향하기 때문)
#             parent[neighbor] = node
#             dfs(neighbor) # 자식 노드의 부모 노드를 찾으러 감

def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in nodes[node]:
            if parent[neighbor] == 0:
                parent[neighbor] = node
                stack.append(neighbor)

dfs(1) # 1번부터 시작함

for p in parent[2:]:
    print(p)