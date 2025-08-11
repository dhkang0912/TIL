'''
MooTube

# 입력
1. 동영상 1~5000, N개 / Q, 농부 존의 질문
2. N-1 줄 간 USADO
    - p, q, r 
    - 동영상 p <-> 동영상 q, usado r로 연결
3. Q줄 동안 농부 존의 질문
    - usado k, v 동영상 보고 있는 경우 => 몇개의 영상 추천?

# 출력
- Q개의 답변

'''

def dfs(usado, node):
    stack = []
    stack.append(node)
    visited[node] = 1

    while stack:
        v = stack.pop()
        # w = node, usado
        for new_node, new_usado in graph[v]:
            if not visited[new_node] and new_usado >= k:
                stack.append(new_node)
                visited[new_node] = 1

# 재귀로 하는 경우 시간 초과
# import sys 
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(usado, node):
#     visited[node] = 1
#     for new_node, new_usado in graph[node]:
#         if not visited[new_node] and new_usado >= usado:
#             visited[new_node] = 1
#             dfs(usado, new_node)



N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int, input().split())
    # 양방향 그래프, 서로 연결됨
    graph[p].append((q, r)) # p <-> q , USADO R
    graph[q].append((p, r)) # q <-> p , USADO R

for _ in range(Q):
    k, v = map(int,input().split())
    visited = [0]* (N+1)
    #  0번 인덱스 사용 안함
    # USADO k값의 v 비디오의 추천 동영상 개수 
    # (v 비디오와 연결된 USADO k값의 영상 개수)
    dfs(k, v) 
    # 시작 노드의 수를 제외해줘야 함
    print(sum(visited)-1)
    

