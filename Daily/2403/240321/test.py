'''
노드의 수 7개
간선의 수 11개

7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

'''
# # 우선순위 큐를 활용
# from heapq import heappush, heappop
#
#
# def prim(start):
#     pq = []
#     MST = [0] * V
#
#     # 최소 비용
#     sum_weight = 0
#
#     # 시작점 추가
#     # [기존 BFS] 노드 번호만 관리
#     # [PRIM] 우선 순위가 가중치에 따라 정렬
#     # -> 가중치가 낮으면 먼저 나와야 함
#     # -> 관리해야 할 데이터 : 가중치, 노드 번호 2가지
#     # -> 1. class로 만들기
#     # -> 2. 튜플로 관리
#     # 이차원 배열 + 가중치 + 높이처럼 데이터가 많아지면 클래스로 관리하는 게 좋음
#     heappush(pq, (0, start))
#
#     while pq:
#         weight, now = heappop(pq)
#
#         # 우선 순위 큐의 특성 상
#         # 더 먼거리로 가는 방법이 큐에 저장되어 있기 때문에
#         # 기존에 이미 더 짧은 거리로 방문했다면 continue
#         if MST[now]:
#             continue
#
#         # 방문 처리
#         MST[now] = 1
#         # 누적합 추가
#         sum_weight += weight
#
#         # 갈 수 있는 노드들을 보면서
#         for to in range(V):
#             # 갈 수 없거나 이미 방문했다면 pass
#             # 인접 행렬로 저장해서 이렇게 표현
#             if graph[now][to] == 0 or MST[to]:
#                 continue
#
#             heappush(pq, (graph[now][to], to))
#
#     print(f'최소비용 : {sum_weight}')
#
#
# V, E = map(int, input().split())
#
# graph = [[0] * V for _ in range(V)]
# for _ in range(E):
#     s, e, w = map(int, input().split())  # 가중치를 같이 저장해야함
#
#     # 가중치 그래프 3->4로 가는데 31일이라는 비용이 든다
#     # graph[3][4]
#     # 무방향 그래프
#     graph[s][e] = w
#     graph[e][s] = w
#
# prim(0)

# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)
#
#     # 같은 집합이면 pass
#     if x == y:
#         return
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y
#
#
# V, E = map(int, input().split())
# edges = []  # 간선 정보들을 모두 저장
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     edges.append([s, e, w])
# # x의 2번째 인덱스(가중치) 기준으로 정렬하라
# edges.sort(key=lambda x: x[2])
# parents = [i for i in range(V)]
#
# sum_weight = 0
#
# # 간선들을 모두 확인함
# for s, e, w in edges:
#     # 싸이클이 발생하면 pass
#     if find_set(s) == find_set(e):
#         print(s, e, w, ' / 싸이클 발생! 탈락!')
#         continue
#
#     print(s, e, w)
#     # 싸이클이 없다면, 방문 처리
#     union(s, e)
#     sum_weight += w
#
# print(f'최소 비용 = {sum_weight}')

'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2 
3 5 1
4 5 5
'''
# from heapq import heappush, heappop
#
# V, E = map(int, input().split())
# start = 0  # 시작 노드 번호
#
# INF = int(1e9)
#
# # 인접 리스트
# graph = [[] for _ in range(V)]
# # 누적 거리를 저장할 변수
# distance = [INF] * V
#
# # 간선 정보 저장
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     # graph[3] = [[4, 31]] 이런 식으로 저장, s에서 e로 가는데 w만큼 걸림
#     graph[s].append([w, e])
#
#
# def dijkstra(start):
#     pq = []
#
#     # 시작점의 weight, node 번호를 한번에 저장
#     heappush(pq, (0, start))
#     # 시작 노드 초기화 -> 왜 0으로 초기화하지?
#     distance[start] = 0
#
#     while pq:
#         # 최단 거리 노드에 대한 정보
#         dist, now = heappop(pq)
#
#         # now가 이미 더 짧은 거리로 온 적이 있다면 pass
#         if distance[now] < dist:
#             continue
#
#         # now에서 인접한 다른 노드 확인
#         for to in graph[now]:
#             next_dist = to[0]
#             next_node = to[1]
#
#             # 누적 거리 계산
#             new_dist = dist + next_dist
#
#             # 이미 더 짧은 거리로 간 경우 pass
#             if new_dist >= distance[next_node]:
#                 continue
#
#             distance[next_node] = new_dist  # 누적 거리를 최단 거리로 갱신
#             heappush(pq, (new_dist, next_node))  # next_node로부터 갈 수 있는 인접 노드들을 pq에 추가
#
#
# dijkstra(0)
# print(distance)
#
#
# INF = int(1e6)
#
# def prim(now):
#     U = []
#     # 거리 저장
#     D = [INF] * V
#
#     D[now] = 0
#
#     # 노드를 다 보고 끝내기
#     while len(U) < V:
#         # D에 저장된 것 중 제일 작은 값인 vertex를 고름
#         # 단, 아직 안 가본 것 중
#         minV = INF
#         for i in range(V):
#             if i in U: continue
#             if D[i] < minV:
#                 minV = D[i]
#                 now = i
#         U.append(now)
#
#         for i in range(V):
#             if i in U: continue
#             if G[now][i]:
#                 D[i] = min(D[i], G[now][i])
#
#     print(U, D)
#
#
# V, E = map(int, input().split())
# G = [[0] * V for _ in range(V)]
#
# for i in range(E):
#     v1, v2, w = map(int, input().split())
#     G[v1][v2] = w
#     G[v2][v1] = w
#
# prim(0)

INF = int(1e6)

def prim(now):
    U = []
    # 거리 저장
    D = [INF] * V

    D[now] = 0

    # 노드를 다 보고 끝내기
    while len(U) < V:
        # D에 저장된 것 중 제일 작은 값인 vertex를 고름
        # 단, 아직 안 가본 것 중
        minV = INF
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i
        U.append(now)

        for i in range(V):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], D[now]+G[now][i])

    print(U, D)


V, E = map(int, input().split())
G = [[0] * V for _ in range(V)]

for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

prim(0)