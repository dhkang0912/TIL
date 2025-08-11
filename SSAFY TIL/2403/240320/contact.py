import sys
sys.stdin = open("contact_input.txt", "r")

# def bfs(s):
#     Q = []
#     visited = [False] * 101
#
#     Q.append((s, 0))
#     visited[s] = True
#
#     while Q:
#         v = Q.pop(0)
#         if maxC < cnt:
#             maxC = cnt
#             resV = v
#         elif maxC == cnt:
#             resV = max(resV, v)
#         for w in G[v]:
#             if not visited[w]:
#                 Q.append((w, cnt+1))
#                 visited[w] = True

def bfs(s):
    global resV
    maxC = 0
    Q = []
    visited = [False] * 101

    Q.append((s, 0))
    visited[s] = 1

    while Q:
        v, cnt = Q.pop(0)
        if maxC < cnt:
            maxC = cnt
            resV = v
        elif maxC == cnt:
            resV = max(resV, v)
        for w in G[v]:
            if not visited[w]:
                Q.append((w, cnt+1))
                visited[w] = 1


T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    G = [set() for _ in range(101)]
    resV = 0

    for i in range(0, N, 2):
        v1 = lst[i]
        v2 = lst[i+1]
        G[v1].add(v2)

    bfs(M) # 시작값을 넣어줌
    print(resV)