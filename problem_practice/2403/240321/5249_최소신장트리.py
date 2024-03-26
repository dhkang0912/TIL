# import sys
# sys.stdin = open("5249_input (1).txt", "r")
from heapq import heappush, heappop

def prim(start):
    PQ = []
    visited = [0] * (V+1)

    heappush(PQ, (0, start))
    sum_weight = 0

    while PQ:
        weight, now = heappop(PQ)

        # 기존 이미 더 짧은 거리로 방문했다면 넘어
        if visited[now] :
            continue

        visited[now] = 1
        sum_weight += weight

        for to in range(V+1): # +1 빼먹어가지고 얼마나 시간이 걸린건지 으이구
            if not visited[to] and G[now][to]:
            # if G[now][to] == 0 or visited[to]:
            #     continue
                heappush(PQ, (G[now][to], to))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    # print(arr)

    for i in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w
        G[e][s] = w

    # print(arr)

    print(f'#{tc} {prim(0)}')


