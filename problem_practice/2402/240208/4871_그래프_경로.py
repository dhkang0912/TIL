# 4871_그래프_경로

# 논리
# 예를 들어 S가 1이고 G가 6인 경우
# 1에서부터 연결된 간선들을 확인하면서 visited를 변경해
# 시작 노드부터 끝까지 쭉 돌아갈 때까지 6인 노드를 방문하는지 체크
# 해당 노드가 방문했다고 변경되면 return 1줌
# 만약 해당 반목문을 다 돌 동안 G가 visited가 되지 못한다면 return 0을 해줌

# 리턴이 필요하니 함수로 만들기
# 아직 모두 방문을 안 했으니 visited = [F]*(V+1)
# 비어있는 stack을 만들고 확인해야하는 것들을 넣기
# 한개씩 연결된 것들을 확인하기
    #

import sys
sys.stdin = open("4871_input.txt", "r")

def check(S, G): # s는 출발할 노드, G는 도착 노
    stack = []
    stack.append(S)
    visited = [False]*(V+1)
    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True
            if current_node == G:
                return 1
        for next_node in arr[current_node]:
            if visited[next_node] == False:
                stack.append(next_node)

    return 0


# 인풋
# T를 인풋 받음
# V, E를 인풋 받음 => V는 노드의 갯수, E는 간선 정보의 갯수
# E줄 동안 간선 정보를 인풋 받음
# 어떻게 간선정보들을 받아줄 것인가?
# [1,4]
# [1,3]
# [2,3]
# 이런 식으로 들어올 때
# 빈 리스트를 V번 반복한 G 리스트를 만듦
# 반복문을 돌면서 E번 인풋을 받음
    # 노드와 갈 수 있는 간선 정보를 인풋 받을 때
    # vertax, road
    # G[vertax].append(road)
    # => 해당 vertax에 갈 수 있는 road를 넣어줌
# E개의 줄 이후 S, G를 인풋 받음 => S는 출발할 노드, G는 도착 노드

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        node1, node2 = map(int, input().split())
        arr[node1].append(node2)

    S, G = map(int, input().split())
    # print(V,E)
    # print(arr)
    # print(S, G)

    print(f'#{tc}', check(S, G))






# 아웃풋
# 만약 S부터 G까지 도착하는 간선 정보가 있다면 1,
# 그렇지 않다면 0