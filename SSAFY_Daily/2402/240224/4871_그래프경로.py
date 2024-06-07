# import sys
# sys.stdin = open("4871_input (1).txt", "r")

def check(S, G):
    stack = []
    visited = [0] * (V+1)
    stack.append(S)
    visited[S] = 1

    while stack:
        v = stack.pop()
        if v == G:
            return 1

        for w in Graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = 1
    return 0




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V=노드의 수, E=간선의 수
    Graph = [[] for _ in range(V+1)]
    # print(Graph)
    for i in range(E):
        V1, V2 = map(int, input().split())
        Graph[V1].append(V2)
    # print(Graph)
    S, G = map(int, input().split()) #S = 시작노드, G = 끝노드
    # print(S, G)
    print(f'#{tc}', check(S, G))