# from heapq import heappush, heappop
#
# def prim(start):
#     PQ = []
#     visited = [0] * V
#
#     heappush(PQ, (start, 0))
#     visited[start] = 1
#
#     while PQ:
#         now, weight = heappop()

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    # print(arr)

    for i in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w
        arr[e][s] = w

    print(arr)

    # print(f'#{tc} {prim(0)}')
