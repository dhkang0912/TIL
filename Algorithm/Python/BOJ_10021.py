'''
Watering the Fields

FJ => N 필드를 연결해서 물을 최소 비용으로 끌어와야 함

i => xi, yi의 넓이의 비행기
0 <= xi, yi <= 1000

비용 = 유클리드 계산법
(xi - xj)^2 + (yi - yj)^2

모든 파이프는 연결되어있어야만 함 
필드에 닿기만 하면 물이 끌어와져서 최소 비용이 들어야 함
c = 비용 이상만 물 가져올 수 있음
1 <= c <= 1,000,000

결국 모든 노드를 최소 비용으로 연결해야 함
=> 트리 구조 (사이클 없음)

# input 
1. N, C / 필즈 크기, 최대 비용
2. xi, yi

# output
출력 못하면 -1
최소 비용으로 필즈에 연결할 수 있는 파이프 예산

'''
import heapq

# 유클리드 거리 제곱 계산으로 비용 계산
def cost_cal(node_1, node_2):
    x1, y1 = node_1
    x2, y2 = node_2
    return (x1-x2)**2 + (y1-y2)**2


# 프림 알고리즘
# def prim(N, C, positions):
#     pq = []
#     visited = [0]*N
#     total_cost = 0
#     cnt = 0

#     heapq.heappush(pq, (0,0)) # pq에 추가할 (현재까지 비용 cost, graph의 index), 현재까지 비용 중 가장 낮은 것을 선택하여 나오게 하기 위해 이렇게 입력

#     while pq:
#         current_cost, node = heapq.heappop(pq)

#         # ✅ 이미 방문한 노드는 건너뛰기
#         # 힙에는 중복된 노드가 들어가는 것은 자연스러운 현상 => 꺼낼 때 이미 방문한 노드를 무시해야 함
#         if visited[node]:continue

#         # ✅ 방문 처리 및 비용 추가
#         visited[node] = 1
#         total_cost += current_cost
#         cnt += 1

#         if cnt == N :
#             return total_cost
        
#         for next_node in range(N):
#             if not visited[next_node]:
#                 cost = cost_cal(positions[node], positions[next_node])
#                 # ✅ 첫 연결이거나 비용이 C 이상이면 추가
#                 if cost >= C:
#                     heapq.heappush(pq, (cost, next_node))

#     # ✅ 연결된 노드가 N개가 아니면 -1 반환
#     return -1


def prim(N, C, positions):
    pq = []
    visited = [0]*N
    total_cost = 0
    cnt = 0

    heapq.heappush(pq, (0,0)) # pq에 추가할 (현재까지 비용 cost, graph의 index), 현재까지 비용 중 가장 낮은 것을 선택하여 나오게 하기 위해 이렇게 입력

    while pq:
        current_cost, node = heapq.heappop(pq)

        # ✅ 이미 방문한 노드는 건너뛰기
        # 힙에는 중복된 노드가 들어가는 것은 자연스러운 현상 => 꺼낼 때 이미 방문한 노드를 무시해야 함
        if not visited[node]:
        # ✅ 방문 처리 및 비용 추가
            visited[node] = 1
            total_cost += current_cost
            cnt += 1

            for next_node in range(N):
                if not visited[next_node]:
                    cost = cost_cal(positions[node], positions[next_node])
                    # ✅ 첫 연결이거나 비용이 C 이상이면 추가
                    if cost >= C:
                        heapq.heappush(pq, (cost, next_node))

        if cnt == N :
                return total_cost

    # ✅ 연결된 노드가 N개가 아니면 -1 반환
    return -1


N, C = map(int, input().split())
# N개 좌표 입력 (좌표 자체가 노드)
positions = [tuple(map(int, input().split())) for _ in range(N)]
# graph = [[] for _ in range(N)]

# 모든 노드 간 비용 계산
# for i in range(N):
#     for j in range(i+1, N): # (i,i)는 같은 노드기 때문에 제외, 그 다음 노드부터 모든 노드 탐색
#         cost = cost_cal(positions[i], positions[j])
#         graph[i].append((cost, j)) # 비용과 노드 좌표를 함께 추가
#         graph[j].append((cost, i))


# 프림 알고리즘 실행
print(prim(N, C, positions))

