'''
Dijkstra
다이스트

E개의 일방통행 도로 구간 => 간선으로 연결됨
0번~N번까지 번호 -> V의 개수 == V+1

최소 거리를 구하시오

시작 = 0
마지막 연결지점 = N
도로의 개수수 = E (간선의 개)
'''
import sys
sys.stdin = open("5251_input (1).txt", "r")
from heapq import heappush, heappop

def dijk(start):
    PQ = []
    heappush(PQ, (0, start)) #가중치와 시작 노드
    distance[start] = 0

    while PQ:
        dist, now = heappop(PQ) # 거리와 현재 노드를 지정

        if distance[now] < dist: # 현재 노드까지의 누적거리가 이미 더 짧은 경우 다음 노드 확
            continue

        for to in G[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_node] = new_dist
            heappush(PQ, (new_dist, next_node))






T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N = 마지막 연결지점 (도착지) E = 간선의 수
    # 0~N번까지 (0,1,2 -> 3개, N=2)
    n = N+1
    G = [[] for _ in range(n)]
    # print(G)

    for _ in range(E):
        v1, v2, w = map(int, input().split())
        # 일방통행이라 단방향
        G[v1].append([w, v2]) # v1번 인덱스와 연결된 v2와 그 가중치를 넣어줌, G[v1][0] = 가중치,G[v1][1] = 연결된 노드

    # print(G)
    # 누적 거리 저장
    distance = [float('inf')] * n

    dijk(0)
    print(f'#{tc} {distance[-1]}')
