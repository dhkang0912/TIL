# 연휴라 공부가 너무 하기 싫다.... 따흐흑 ㅠㅠ
# 1219 길찾기
# A도시에서 B도시로 가는 길
# 최대 2개의 갈림길 존재
# 모든 길은 ***일방통행***
# 가는 길이 있는지 찾아내기
# A, B = 0, 99 (출발점은 0, 도착점은 99)
# 모든 길은 순서쌍으로 나타냄
# 한가지 길이라도 존재하면 길이 존재하는 것
# node의 갯수는 98개 (출발점 도착점 제외), 포함하면 100개
# 순서쌍이 주어짐
# 로직
def check(start, destination):
    visited = [False] * 100
    stack = []
    stack.append(start)
    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True
            # if current_node == destination:
            #     return 1
            if visited[destination] == True:
                return 1
        for next_node in G[current_node]:
            if visited[next_node] == False:
                stack.append(next_node)


    return 0


# 인풋
import sys
sys.stdin = open("1219_input.txt", "r")
# T의 갯수가 주어짐
# 순서쌍이 주어짐
T = 10
for tc in range(1, T+1):
    TC, N = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    for i in range(0,N*2,2):
        G[arr[i]].append(arr[i+1]) # 단방향, 일방통행이기에 하나만 더해줌
        # 진짜 어이가 없다
        # N개의 선이 이어져있는데 출발, 도착으로 나눠져있으니 순회해야하는 갯수가 *2가 되어줘야 함...ㅎ
    # print(G)

    # 아웃풋
    # 연결되어있으면 1, 아니면 0
    print(f'#{tc}', check(0, 99))
