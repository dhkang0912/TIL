
# 4831 전기버스
# 1. T를 입력 받음
# 2. T만큼 반복함
    # 1) K를 입력 받음 # 한번에 이동할 수 있는 정류장 갯수
    # 2) N를 입력 받음 # 종점까지 갯수 -> 총 정류장 갯수
    # 3) M를 입력 받음 # 충전기가 설치된 정류장 갯수
    # 4) charger_pos를 리스트로 입력 받음 # 충전기 설치된 위치

    # 5) 0부터 N까지 반복하며 종점까지 이동
        # 5-1) 만약 현재 위치에 충전기가 없고, 현재 이동할 수 있는 수가 다음 충전기 위치에 도착할 수 없으면
            # 5-1-1) 0을 출력하고 종료한다
        # 5-2) 만약 현재 위치가 충전기이고 다음 충전기까지 거리가 이동할 수 있는 거리가 충분하지 않다면
            # 5-2-1) 충전을 한다 -> k만큼 이동할 수 있게 됨
            # 5-2-2) 충천 횟수 +1을 한다
        # 5-3) 이동 횟수를 -1한다

# import sys
# sys.stdin = open("4831_input.txt", "r")
#
# def check() :
#     now = 0
#     cnt = 0
#     for i in range(1, M) :
#         if Stops[i] - Stops[i-1] > K :
#             return 0
#         if now+K < Stops[i] :
#             cnt += 1
#             now = Stops[i-1]
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1) :
#     K, N, M = map(int, input().split())
#     Stops = [0] + list(map(int, input().split())) + [N]
#     M += 2 # 출발 시 0번째에서 충전, 끝나고 N에서 충전
#
#     print(f'#{tc} {check()}')





# 4837 부분 집합의 합
# 1부터 12까지 숫자를 원소로 가진 집합 A
    # 1 2 3 4 5 6 7 8 9 10 11 12
    # -> 12개의 원소를 가짐 -> num = 12
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있음
    # -> 부분 집합의 원소 갯수 = N,
    # -> 원소의 합이 K인 것을 카운팅

# -> 예시 : K = 3 -> 부분 집합의 원소 갯수, 원소가 3개
    # -> {x, y, z} -> x+y+z가 3인 것을 카운팅

# import sys
# sys.stdin = open("4837_input.txt", "r")
#
# arr = [ i for i in range(1, 13)]
#
# T = int(input()) # 테스트 케이스 갯수
# for tc in range(1, T+1) : # tc번째 돌림
#     N, K = map(int, input().split()) # N = 부분 집합의 갯수, K = 부분집합의 합
#     result = 0
#     num = 12 # 총 원소의 갯수
#     for i in range(2**num) : #2<<N
#         sum_v = 0
#         cnt = 0
#         for j in range(num) :
#             if i & (1 << j) :
#                 cnt +=1
#                 sum_v += arr[j]
#         if cnt == N and sum_v == K :
#             result += 1
#
#     print(f'#{tc} {result}')

# [S/W 문제해결 기본] 2일차 - Sum
# 보충 쌤 코드
# for _ in range(10):
#     tc = int(input())
#     galo = 0 #가로의 합 초기화
#     selo = [0 for i in range(100)] #세로의 합을 저장할 리스트 초기화
#     diag1 = 0 # 아래 오른쪽 대각선 합 초기화
#     diag2 = 0 # 아래 왼쪽 대각선 합 초기화
#     for i in range(100):
#         line = list(map(int, input().split()))
#         # 가로의 합
#         galo = max(galo, sum(line))
#         diag1 += line[i]
#         diag2 += line [99 i]
#         for j in range(100):
#             selo[j] += line[j]



# 1. 테스트 케이스는 10개가 주어진다.
# 2. 테스트 케이스를 순회한다.
# 3. 100*100의 2차원 배열이 주어진다. -> 나열된 숫자들을 2차원 배열로 만든다.
    # 3-1) 어떻게 2차원 배열을 만들었지?
        # n = 100 -> 100*100의 배열이기 때문에 한 행의 갯수가 n, 한 열의 갯수도 n
        # arr = [list(map(int, input())) for _ in range(n)]


    # 3-2) 각 행의 합을 구한다
        # for row in range(n) :
            # 1번 순회할 때마다 100열까지 더함
            # -> arr[0,0] + arr[0,1] +arr[0,2] ....+ arr[0,99]
            # -> arr[row]
            # 이걸 100번 순회함
            # 첫번째 순회했으면 두번째 번도 순회해야함 -> 이중 for 문
            # 그리고 각 열을 더해야함

    # 3-3) 각 열의 합을 구한다
        # for col in range(n) :
            # 1번 순회할 때마다 100행까지 더함
            # -> arr[0,0] + arr[1,0] +arr[2,0] ....+ arr[99,0]
            # -> arr[col]
            # 이걸 100번 순회함
            # 첫번째 순회했으면 두번째 번도 순회해야함 -> 이중 for 문
            # 그리고 각 행을 더해야함

    # 3-4) 오른쪽 아래 대각선의 합을 구한다.
        # 각 대각선 arr[0,0] arr[1,1] arr[2,2] ....arr[99,99]
        #  -> arr[i,i]

    # 3-5) 왼쪽 아래 대각선의 합을 구한다.
        # arr[0, -1] arr[1, -2]arr[2, -3] ... arr[99, -100]
        # -> arr[i, (-i) -1]

# 위 각 합들을 비교하여 가장 큰 수를 구한다.

import sys
sys.stdin = open("240131_input.txt", "r")

T = 10

for tc in range(1, T+1) :
    t_num = int(input())
    n = 100 # 100*100의 배열
    arr = [list(map(int,input().split())) for _ in range(n)]
    # n개의 데이터를 받은 후 이걸 n번 반복하여 쌓아서 저장 (n*n 이차원 배열)
    # print(arr)

    max_row = 0
    for row in range(n):  # 0~99번 row를 순회
        sum_row = 0
        for col in range(n):  # 0~99번 col을 순회
            sum_row += arr[row][col]
        if max_row < sum_row:
            max_row = sum_row

    max_col = 0
    for col in range(n):
        sum_col = 0
        for row in range(n):
            sum_col += arr[row][col]
        if max_col < sum_col:
            max_col = sum_col

    sum_right_bottom = 0
    for i in range(n):
        sum_right_bottom += arr[i][i]

    sum_left_bottom = 0
    for i in range(n):
        sum_left_bottom += arr[i][99-i]

    compared_value = [max_row, max_col, sum_right_bottom, sum_left_bottom]

    real_max_value = 0
    for value_ in compared_value:
        if real_max_value < value_:
            real_max_value = value_

    print(f'#{tc} {real_max_value}')
















# 4836 색칠하기
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     # CMD = [list(map(int,input().split())) for _ in range(N)]
#
#     brd = [[0]*10 for _ in range(10)]
#     for _ in range(N) :
#         r1, c1, r2, c2, color = map(int, input().split())
#         cnt = 0
#         for r in range(r1, r2+1) :
#             for c in range(c1, c2+1) :
#                 brd[r][c] += color
#
#     for r in range(10) :
#         for c in range(10) :
#             if brd[r][c] == 3 :
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')


