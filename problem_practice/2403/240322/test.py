# '''
# 입력 확인하기
# T = 10으로 고정
# '''
# def bfs(start):
#     q = [start]
#     visited = [0] * (101)
#     visited[start] = 1
#
#
#     # 마지막의 방문한 곳의 가장 큰 수를 뽑아야 함
#     # 가장 깊은 depth의 가장 큰 수
#     max_number = start
#     # 가장 깊은 depth
#     max_depth = 1
#
#     while q:
#         now = q.pop(0)
#
#         # 갈 수 있는 곳들
#         for to in graph[now]:
#             # 이미 방문했다면 pass
#             if visited[to]:
#                 continue
#             q.append(to)
#             # 현재 방문 = 이전 방문 +1번만에 왔음
#             visited[to] = visited[now]+1
#
#             # depth가 더 깊어졌네? => max_number 초기화
#             # depth는 같은데 숫자가 더 크네? => 초기화
#             if max_depth < visited[to] or \
#                 (max_depth == visited[to] and max_number < to) :
#                 max_depth = visited[to]
#                 max_number = to
#     return max_number
#
#
# for tc in range(1, 11):
#     N, start = map(int, input().split())
#     input_graph = list(map(int, input().split()))
#
#     # 인접 리스트
#     # N번까지 있다고 해도 범위가 N번까지만 주어지는 게 아님, 최대 노드 번호가 100이라서 1~100까지 주어질 수 있음
#     graph = [[] for _ in range(101)]
#     for i in range(0, N, 2):
#         s = input_graph[i]
#         e = input_graph[i+1]
#         graph[s].append(e)
#
#     r = bfs(start)
#     print(f'#{tc} {r}')

# def dfs(cnt, sum_height):
#     global ans
#     # 1. 키의 합이 B 이상이면 종료
#     # -> 현재까지 쌓은 탑의 높이
#     # 다 쌓았을 때 최대
#     if sum_height >= B:
#         # 제일 높이가 낮은 탑이 정답
#         # 최소 탑의 높이는 재귀 호출 함수들이 '동시에' 사용함 -> 전역변수
#         ans = min(ans, sum_height)
#         return
#
#         # 기저 조건
#     # 2. 모든 점원이 탑을 쌓았다면 종료
#     # -> 현재까지 쌓은 점원의 수
#     if cnt == N:
#         return
#
#         # 재귀 호출 파트
#     # 쌓는다를 선택
#     dfs(cnt + 1, sum_height + arr[cnt])
#     # 안 쌓는다를 선택
#     dfs(cnt + 1, sum_height)
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#     ans = float('inf')
#     dfs(0, 0)
#     print(f'#{tc} {abs((ans - B))}')

# '''
# 1
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 1 1 1
# '''
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def dfs(y, x, path):
#     # 기저조건 : 7자리면 끝
#     if len(path) == 7:
#         # 현재까지의 경로를 저장
#         result.add(path)
#         return
#
#     for i in range(4):
#         new_y = y + dy[i]
#         new_x = x + dx[i]
#
#         # 범위 밖으로 넘어가면 pass
#         if 0 <= new_x < 4 and 0 <= new_y < 4:
#             dfs(new_y, new_x, path + map([new_y][new_x]))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 격자판 저장
#     # maps = [list(map(int, input().split())) for _ in range(4)]
#     # 갈 때마다 경로를 더하기 위해서 문자열로 저장
#     maps = [input().split() for _ in range(4)]
#
#     result = set()  # 중복 제거
#
#     # 시작 지점
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, maps[i][j])
#     print(f'#{tc} {len(result)}')

# '''
# 10
# 10 40 100 300
# 0 0 2 9 1 5 0 0 0 0 0 0
# 10 100 50 300
# 0 0 0 0 0 0 0 0 6 2 7 8
# 10 70 180 400
# 6 9 7 7 7 5 5 0 0 0 0 0
# 10 70 200 550
# 0 0 0 0 8 9 6 9 6 9 8 6
# 10 80 200 550
# 0 8 9 15 1 13 2 4 9 0 0 0
# 10 130 360 1200
# 0 0 0 15 14 11 15 13 12 15 10 15
# 10 180 520 1900
# 0 18 16 16 19 19 18 18 15 16 17 16
# 10 100 200 1060
# 12 9 11 13 11 8 6 12 8 7 15 6
# 10 170 500 1980
# 19 18 18 17 15 19 19 16 19 15 17 18
# 10 200 580 2320
# 12 28 24 24 29 25 23 26 26 28 27 22
# '''
#
#
# def dfs(month, sum_cost):
#     global ans
#     # 기저조건
#     # 1. 12월까지 다 봤네? 종료
#     if month > 12:
#         # 최소비용
#         ans = min(ans, sum_cost)
#         return
#         # 2. 이미 최소값을 넘어갔네? 종료
#     if sum_cost > ans:
#         return
#
#         # 모두 1일권으로 구매
#     dfs(month + 1, sum_cost + (days[month] * cost[0]))
#
#     # 1달권 구매
#     dfs(month + 1, sum_cost + cost[1])
#
#     # 3달권 구매
#     dfs(month + 3, sum_cost + cost[2])
#
#     # 1년권 구매
#     dfs(month + 12, sum_cost + cost[3])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     # 1부터 쓸래 (맨 앞에 안 쓰는 0 넣기)
#     days = [0] + list(map(int, input().split()))
#     ans = float('inf')
#     dfs(1, 0)
#     print(f'#{tc} {ans}')

# '''
# 1
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 1 1 1
# '''
#
# dy = [1, 0, -1, 0]
# dx = [0, 1, 0, -1]
# def dfs(y, x, path):
#     # 기저조건: 7자리면 끝
#     if len(path) == 7:
#         # 현재까지의 경로를 저장
#         result.add(path)
#         return
#
#     for i in range(4):
#         new_y = y + dy[i]
#         new_x = x + dx[i]
#
#         # 범위 밖으로 넘어가면 pass
#         if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
#             continue
#
#         dfs(new_y, new_x, path + maps[new_y][new_x])
#
# T = int(input())
#
# for tc in range(T):
#     # 격자판 저장
#     # maps = [list(map(int, input().split())) for _ in range(4)]
#     # 갈 때마다 경로를 더하기 위해서 문자열로 저장
#     maps = [input().split() for _ in range(4)]
#     # 중복을 제거하기 위해 set 사용
#     result = set()
#
#     # 시작 지점
#     for i in range(4):
#         for j in range(4):
#             dfs(i, j, maps[i][j])
#
#     print(len(result))

# '''
# 10
# 10 40 100 300
# 0 0 2 9 1 5 0 0 0 0 0 0
# 10 100 50 300
# 0 0 0 0 0 0 0 0 6 2 7 8
# 10 70 180 400
# 6 9 7 7 7 5 5 0 0 0 0 0
# 10 70 200 550
# 0 0 0 0 8 9 6 9 6 9 8 6
# 10 80 200 550
# 0 8 9 15 1 13 2 4 9 0 0 0
# 10 130 360 1200
# 0 0 0 15 14 11 15 13 12 15 10 15
# 10 180 520 1900
# 0 18 16 16 19 19 18 18 15 16 17 16
# 10 100 200 1060
# 12 9 11 13 11 8 6 12 8 7 15 6
# 10 170 500 1980
# 19 18 18 17 15 19 19 16 19 15 17 18
# 10 200 580 2320
# 12 28 24 24 29 25 23 26 26 28 27 22
# '''
# T = int(input())
# for tc in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     # 1부터 쓸래 (맨 앞에 안 쓰는 0 넣기)
#     days = [0] + list(map(int, input().split()))
#
#     # DP 배열
#     plans = [0] * 13
#
#     # 1~12월까지 반복
#     for i in range(1, 13):
#         # 현재 달의 최소 비용 계산
#         # 이전달 +1일권 구입 / 이전 달 + 1달권 구입 / 3달 전 + 3달권 구입
#         plans[i] = min(plans[i - 1] + (days[i] * cost[0]), plans[i - 1] + cost[1])
#
#         if i >= 3:
#             plans[i] = min(plans[i], plans[i - 3] + cost[2])
#
#     # 12월까지의 계산 결과 or 1년권
#     min_cost = min(plans[12], cost[3])
#     print(f'#{tc} {min_cost}')


'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(y, x, path):
    # 기저조건 : 7자리면 끝
    if len(path) == 7:
        # 현재까지의 경로를 저장
        result.add(path)
        return

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        # 범위 밖으로 넘어가면 pass
        if new_y < 0 or new_y >= 4 or new_x < 0 or new_x >= 4:
            continue

        dfs(new_y, new_x, path + maps[new_y][new_x])


T = int(input())
for tc in range(1, T + 1):
    # 격자판 저장
    # maps = [list(map(int, input().split())) for _ in range(4)]
    # 갈 때마다 경로를 더하기 위해서 문자열로 저장
    maps = [input().split() for _ in range(4)]

    result = set()  # 중복 제거

    # 시작 지점
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])
    print(f'#{tc} {len(result)}')