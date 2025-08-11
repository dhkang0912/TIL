# 9490 풍선팡
# 테스트 케이스 T를 인풋 받음 -> 이걸 순회함
# N, M을 주어짐
    # -> 이걸로 N*N 배열을 만듦
    # -> 풍선이 M개 있음
# 그 안에 개수만큼 꽃가루가 상하좌우로 터짐 (가운데 있는 나를 포함하여, 상하좌우로 터짐)
    # 1개가 터지면
    #      010
    # # -> 111
    #      010
    # 만약 2개가 터지면 2배로 움직여야 함

# import sys
# sys.stdin = open("9490_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = 0
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     # newR = 0
#     # newC = 0
#     for row in range(N) :
#         for col in range(M) :
#             sumV = arr[row][col]
#             for jump in range(4) :
#                 for jump_arrow in range(1, arr[row][col]+1) :
#                     newR = row + dr[jump]*jump_arrow
#                     newC = col + dc[jump]*jump_arrow
#                     if 0 <= newR < N and 0 <= newC < M :
#                         sumV += arr[newR][newC]
#             if maxV < sumV :
#                 maxV = sumV
#
#     print(f'#{tc} {maxV}')
                       



# 240202 _ ladder 문제
# T = 10
# for _ in range(1, T+1) :
#     N = 100
#     tc = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(N)]
#     # 1. 99 row에서 2의 위치를 찾아라
#     for col in range(N) :
#         if ladder[99][col] == 2 :
#             break
#     # print(col)
#
#     # 3. 위로 한칸씩 이동하면서
#     for row in range(98, -1, -1):
#         #2-1 col의 왼쪽에 1이 있는지 확인
#         if col > 0 and ladder[row][col-1] == 1 :
#             while col > 0 and ladder[row][col-1] == 1 :
#                 col -= 1
#         # 2-1 col의 오른쪽에 1이 있는지 확인
#         elif col < N-1 and ladder[row][col+1] == 1:
#             while col < N-1 and ladder[row][col+1] == 1 :
#                 col += 1
#     print(col)
#

# 240202 _ ladder 문제 -> 직접 짜보기

# import sys
# sys.stdin = open("240201_ladder_input.txt", "r")
#
# T = 10
# for _ in range(1, T+1) :
#     tc = int(input())
#     n = 100
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     # print(arr)
#
#     for col in range(n) :
#         if arr[99][col] == 2 :
#             break # 시작 col 을 찾음
#
#     # print(col)
#
#     for row in range(98, -1, -1) :
#         if col > 0 and arr[row][col-1] == 1 :
#             while col > 0 and arr[row][col-1] == 1 :
#                 col -= 1
#         elif col < n-1 and arr[row][col+1] == 1 :
#             while col < n-1 and arr[row][col+1] == 1 :
#                 col += 1
#
#     print(f'#{tc} {col}')


# 9386 연속한 1의 개수
# 내 코드
# 0과 1로 이루어진 수열 중 연속한 1의 개수 중 최대값을 출력
# -> 1<=T<=10, 10<=N<=1000
# 1. 첫줄에 테스트 케이스 T를 인풋받음
# 2. 수열의 길이인 N을 입력 받음 -> 수열의 갯수
# 3. 01로 이뤄진 수열 numbers가 입력됨

# numbers에서 찾아야 할 것
# 0011001110일 경우
# 앞에서부터 순회하면서 각 인덱스의 값을 확인해야 함
    # 만약 현재 인덱스 값이 0이면 그냥 지나가면 됨 -> 1의 갯수를 카운트 해줄 필요가 없음
    # 만약 현재 인덱스 값이 1이면 1의 갯수를 카운트 해줌 ,
        # 만약 순회하다가 다음 인덱스 값이 0이 되면 카운트를 누적하면 안됨
        # 맥스를 확인함

# import sys
# sys.stdin = open("9386_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     numbers = list(map(int,input()))
#     cnt = 0
#     maxV = 0
#     for i in range(N) :
#         if numbers[i] == 0 :
#             cnt = 0
#         if numbers[i] == 1 :
#            cnt += 1
#            if maxV < cnt :
#                maxV = cnt
#
#     print(f'#{tc} {maxV}')

# 쌤 코드
# S = input()
# cnt = 0
# maxV = 0
# for c in S :
    #if c == '1' :
    #   cnt+= 1
    #else :
    #   if maxV < cnt :
    #      maxV = cnt
    #      cnt = 0
    #   if maxV < cnt :
    #      maxV = cnt



# 9367 점점 커지는 당근의 개수
# 당근 선별기 기능 : 연속으로 당근이 커진 경우 그 개수를 알려줌
# 연속으로 당근이 커진 경우의 최대값
# 당근의 크기는 1부터 10까지 정수로 이뤄짐

# 테스트 케이스 T개를 인풋 받는다
# T개를 순회한다
    # 당근 개수인 N을 인풋 받는다
    # 당근 크기를 의미하는 C를 리스트로 인풋받는다 (N개의 정수 ex: 12345)
    # cnt = 0
    # maxV = 0
    # 당근 크기인 C의 값들을 N번만큼 순회한다
        # 만약 C[i] < C[i+1]
            # cnt += 1
            # maxV가 cnt보다 작으면 maxV를 변경
        # 그렇지 않으면
            # cnt = 0

# import sys
# sys.stdin = open("9367_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     C = list(map(int, input().split()))
#
#     cnt = 1
#     maxV = 1
#     for i in range(N) :
#         if i < N-1 and C[i] < C[i+1] :
#             cnt += 1
#             if maxV < cnt :
#                 maxV = cnt
#         elif i < N-1 and C[i] > C[i+1] :
#             cnt = 1
#
#     print(f'#{tc} {maxV}')


# 9490 풍선팡
# M*N 배열
# 풍선에 든 꽃가루가 1개일 때  ->  총 5개가 터
    #   010
    # ->111
    #   010
# 만약 풍선에 든 꽃가루가 2개일 때 -> 9
    #00200
    #00200
    #22222
    #00200
    #00200

# 이런 식으로 구해질 때 꽃가루의 합이 가장 큰 수를 구하라
# -> 뭘 주의해야할까? -> 내가 생각했을 때는 상하좌우로 꽃가루의 배수만큼 커지는 건 유념이 될 것 같음
# -> 자기 자신의 꽃가루를 더해주는 걸 놓칠 수 있으니 유의하는 게 필요
    # 상하좌우 꽃가루를 어떻게 구현하면 좋을까?
    # 최대 값을 구할거니까 max_v를 초기화 필요
    # 한번 움직일 때마다 더한 값을 저장할 곳이 필요하니까 sum_v를 지정해줘야
    # 현재 위치 지정하고 -> dr, dc 이용해서 4방향으로 움직이는 게 필요 줌
        # -> 처음에 잊지 말고 꽃가루 자신을 더해줘야
       # -> 이때 꽃가루의 배수만큼 움직여줌
       # -> 왜 그렇냐? 4방향으로 꽃가루의 배수만큼 움직이며 꽃가루가 지정됨
       # -> 이때 모든 위치가 다 찍히면서 꽃가루를 더해주려면?
       # -> 위치만 갈 수 있는지 확인하고, 만약 가능하다면 더할 때 4*꽃가루의 갯수로 하면 됨
            # -> 어차피 이게 상하좌우의 꽃가루 갯수

# import sys
# sys.stdin = open("9490_input.txt","r")

# T = int(input())
# for tc in range(1, T+1) :
#     # N*M 행렬
#     N, M = map(int, input().split()) #행*열
#     # 테스트 배열 받기
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr)
#     sum_v = 0
#     max_v = 0
#     dr = [-1, 0, 0, 1]
#     dc = [0, 1, -1, 0]
#     for row in range(N) :
#         for col in range(M) :
#             sum_v = arr[row][col]
#             newR = 0
#             newC = 0
#             for i in range(4):
#                 for jump_num in range(1, arr[row][col]+1): # 상하좌우 꽃잎의 개수만큼 이동하도록 반복
#                     newR = row + dr[i]*jump_num
#                     newC = col + dc[i]*jump_num
#                     if 0 <= newR <= N-1 and 0 <= newC <= M-1 :
#                         sum_v += arr[newR][newC]
#             if max_v < sum_v:
#                 max_v = sum_v
#
#
#     print(f'#{tc} {max_v}')


# 16268 풍선팡 2
# N*M의 배열이 있음
# 꽃가루가 터지면 상하좌우 풍선이 하나씩 더 터짐
# 첫줄에 테스트 케이스 T를 인풋 받음
# N*M 배열이 주어짐
# maxV를 찾아야 하니 maxV를 처음에 초기
# for문을 돌며 현재 위치에 들어있는 꽃가루를 확인, 그걸 sumV에 넣어줌
    # for 문을 돌며 현재 위치에서 한칸씩 옮겨줌
        # 만약 옮긴 위치가 0보다 크거나 같고 M-1이랑 크거나 같으면
        # sumV에 1을 누적해줌
    # sumV가 maxV보다 크면 maxV 변경

# import sys
# sys.stdin = open("16268_input.txt","r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N, M = map(int, input().split()) # N*M -> 가로가(row) N줄, 세로(col)가 M
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     maxV = 0
#     # 상하좌우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     for row in range(N) :
#         for col in range(M) :
#             sumV = arr[row][col]
#             newR = 0
#             newC = 0
#             for i in range (4) :
#                 newR = row + dr[i]
#                 newC = col + dc[i]
#                 if 0 <= newR <= N-1 and 0 <= newC <= M-1 :
#                     sumV += arr[newR][newC]
#             if maxV < sumV :
#                 maxV = sumV
#
#     print(f'#{tc} {maxV}')

# 16910 원 안의 점
# 반지름 N이 주어짐
# 그 원 안에 포함되는 격자점(x,y가 모두 정수)의 개수를 구하는 프로그램
# x**2 + y**2 <= N**2인 격자점의 개수를 구하라
# 이걸 어떻게 구하지?
# (0,0)을 원의 중심으로 삼음 원
    # -> 좌표는 반지름만큼 상하좌우로 뻗은 직사각형 안에 들어가는
    # 상하좌우 좌표 = (n, 0), (-n, 0), (0, -n), (0, n)
    # 이 안의 사각형을 탐색하는데 -> 원 안에 들어가는지 확인하기 위해서는 x**2 + y**2 <= N**2인 걸 확인
    # 근데 이게 다 정수여야 함
    # 내가 배운 배열, 정렬
    # 버블정렬, 카운팅정렬, 이진검색, 선택정렬
    # 꼭 정렬을 써야 하나?
    # 그냥 2n*2n 배열 만들고 각 배열 좌표를 확인하면 되는 거 아닌가?
    # -> 대신 좌측 시작이 (n,-n), 우측 시작이 (n,n),
    # -> 좌측 끝이 (-n,-n), 우측 끝이 (-n,n)
    # 그럼 row의 시작과 끝은 n~-n
    # col의 시작은 -n~n
    # 이 좌표들을 검증해 가면 되는 거 아닌가?
    # 위 좌표가 row**2 + col**2 = n**2이고 타입이 int이면 cnt+1해주면 되는 거 아닌가?

# 첫 줄은 테스트 케이스의 수 T가 인풋됨
    # 1<=N<=200인 반지름, N이 주어짐

# import sys
# sys.stdin = open("16910_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     cnt = 0
#     for row in range(N, (-N-1), -1) :
#         for col in range((-N), N+1) :
#             if (row**2) + (col**2) <= (N**2) and type(row) == int and type(col) == int :
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')

# 6485 삼성 시의 버스 노선
# 버스 정류장의 번호는 1부터 5000까지 있음
# 버스 노선은 N개가 있음
# 특정 버스 노선은 A 이상이고 B 이하인 모든 정류장만을 다니는 버스 노선이다
# P개 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지 구하라


# T의 테스트 케이스를 인풋 받음
# 버스 노선 테스트 케이스의 갯수를 인풋받음 = N
# 구간 자체를 N번 그럼 인풋 받아야 하네? 여기서 for 문을 돌려야겠구만, 아니면 while문
#-> 종료 조건을 N이랑 같아지면 끝나게 하거나
    # 첫번째 노선이 가는 구간
    # 두번째 노선이 가는 구간
    # N번째 노선이 가는 구간
    # P개의 정류장이 주어짐
    # j도 여러개 주어짐
    # 1번째 정류장을 들리는 버스의 갯수
    # 2번째 정류장을 들리는 버스의 갯수
    # ... j번째 정류장을 들리는 버스의 갯수

# import sys
# sys.stdin = open("6485_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input()) # 테스트 케이스 안 예시 갯수
#     section = [list(map(int,input().split())) for _ in range(N)] # 지나가는 노선 범위 배열 N*2
#     P = int(input()) # 확인할 정류장의 수
#     Cj_list = []
#     for i in range(P) :
#         cnt = 0
#         J = int(input())
#         for row in range(N) :
#             if section[row][0] <= J <= section[row][1] :
#                 cnt += 1
#         Cj_list.append(cnt)
#
#     # ' '.join(map(str, Cj_list))
#     print(f'#{tc}', *Cj_list)


# 6019 기차 사이의 파리
# 기차 사이의 간격은 250마일
# A 기차의 시속은 10마일
# B 기차의 시속은 15마일
# 파리가 A기차 전면부에서 B 기차로 시속 20마일로 날아감
# B 기차의 전면부에 닿으면 A 기차를 향해 20마일로 날아감
# A와 B가 닿으면 파리는 죽음
# 파리가 죽기 전까지 이동한 마일을 찾음
# 어느 지점에서 기차가 서로 충돌할지 확인 필요 -> 어느 시간에 서로 부딪힘?
# 지속적으로 어느 정도 간격이 줄어듦?
# 그 거리를 파리가 얼마나 갈 수 있음?
# -> 사실 상 거리보다는 시간을 구해서 그 시간동안 이동한 거리를 구하는 문제가 아닐까?

# 10x+15x = 250 마일 -> 10시간 후면 서로 충돌 -> 이 시간만큼 파리가 이동할 수 있는 거리를 구하면됨

# 첫째줄에는 테스트 케이스의 수 T를 인풋받음
# D,A,B,F가 주어짐
# D는 기차 사이 거리, A는 A기차의 속력, B는 B 기차의 속력, F는 파리의 속력
# -> 각 케이스별로 파리가 이동한 거리를 구하라
# import sys
# sys.stdin = open("6019_input.txt","r")
#
# T = int(input())
# for tc in range(1, T+1):
#     D, A, B, F = map(int, input().split())
#     # D = 기차 사이 거리, A는 기차 속력, B는 기차 속력, F는 파리 속력
#     time = D/(A+B)
#     F_mile = F*time
#
#     print(f'#{tc} {F_mile}')


# 5789 현주의 상자 바꾸기
# 1~N번까지 N개의 상자가 주어짐
# 상자의 처음 숫자는 다 0
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# 1<=i<=Q 작업에 대해 L번~R번 값을 i로 변경 -> Q만큼 반복문
# Q회 동안 작업하고 N개의 상자에 들어있는 값을 출력

# T 케이스를 인풋 받고 T번 반복
    # N, Q를 인풋 받음 (상자 갯수, 상자를 변경할 갯수)지
    # Q만큼 반복하면서 값을 변경함
        # 변경할 범위가 주어짐 L~R 사이를 i로 채움
    # 케이스 번호와 들어있는 리스트를 언팩하여 프린트

# import sys
# sys.stdin = open("5789_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N, Q = map(int, input().split())
#     lst = [0] * N
#     for i in range(1, Q+1) :
#         L, R = map(int, input().split())
#         for idx in range(L-1, R) :
#             lst[idx] = i
#
#     print(f'#{tc}', *lst)


# 2001 파리 퇴치
# N*N 배열 안에 파리의 개수가 적혀있음
# M*M 크기의 파리채를 한번 내리쳐 최대한 많은 파리를 죽이기
# -> N*N 배열을 돌면서 그 주변 M*M 안의 수를 누적
# -> 이걸 어떻게 하면 좋을까?어
# -> maxV도 필요 여기서 초기
# -> 우선 N*N 배열을 이차원 리스트로 받아야 함함
    # -> 이 안에서 cnt 초기화
# -> 복잡하게 생각할 필요없이 M*M의 이차원 리스트가 또 있는거임, 그 좌표에 해당하는 값을 매번 누적
# -> 그냥 이중 for문을 또 돌리면 되는 거 아냐? 그럼 한개씩 나오잖아 그 값을 누적!
    # -> cnt를 그 안에서화
# -> 여기서 maxV를 비
# -> 자신에서 하의 파리 갯수를 구함
        # -> 이 때 주의할 점은 우로 가거나 하로 갈 때
        # -> 암튼 어디로 가든, 새로 간 곳의 row, col이 0과 N을 넘으면 안


# tc를 T개 인풋받음
# N, M을 인풋 받음 (N은 N*N 파리가 있는 배열의 갯수, M은 그 안에서 확인할 배열 갯수)
# N*N 이차원 배열을 인풋 받음
# 행렬은 row, col임
#
# import sys
# sys.stdin = open("2001_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N, M = map(int, input().split())
#     arr_fly = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr_fly)
#
#     maxV = 0
#     for row in range(N) :
#         for col in range(N) :
#             new_row = 0
#             new_col = 0
#             sumV = 0
#             for new_row_idx in range(M) :
#                 for new_col_idx in range(M) :
#                     new_row = row + new_row_idx
#                     new_col = col + new_col_idx
#                     if 0 <= new_row <= N-1 and 0 <= new_col <= N-1 :
#                         sumV += arr_fly[new_row][new_col]
#             if maxV < sumV :
#                 maxV = sumV
#
#     print(f'#{tc} {maxV}')


# 1979 어디에 단어가 들어갈 수 있을까
# N*N 단어 퍼즐
# 단어 퍼즐의 모양이 주어짐 -> 특정길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력
# -> 가로 세로를 다 확인해야 함, 한꺼번에 확인하는 건 어려울 것 같고 행을 먼저 확인하는 걸 만들고다
    # -> 첫번째 행일 때 확인, 두번째 행일 때 확인 이러면 좋을 것 같은데?
# -> 이어서 따로 열을 확인하는 걸 만들면 좋을 것 같아
    # -> 첫번째 열을 우선 확인, 두번째 열을 확인 이렇게
# 더 커서도 안되고 딱 K만큼 커야 함 -> 뒷부분이 막혀야 함
# 1일 때 갈 수 있고 0일 때 못감 끝부분을 확인하기 어려우니 끝에 0을 다 추가해서 막아버리자
# -> 이걸 어떻게 하지? 이거 알려주셨던 것 같은데
# -> 일단 인풋 받는거에 [0]추가하고 돌리고 [0] 추가하면 되는 것 같던데?

# tc를 T개 인풋 받아 순회하기
# N, K를 한꺼번에 인풋 받음, N개의 행렬을 가진 배열, K 길이의 단어를 넣어야 함
# 2차원 리스트를 통해 낱말퍼즐이 주어짐
# 단어를 입력할 수 있는 부분은 1, 입력 못하는 부분은 0

# import sys
# sys.stdin = open("1979_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]
#     N += 1
#
#     num_of_words_row = 0
#     for row in range(N):
#         for col in range(N):
#             new_row = 0
#             new_col = 0
#             section_cnt = 0
#             for i in range(K):
#                 new_col = col + i
#                 if 0 <= new_col <= N-1 and arr[row][new_col] == 1 :
#                     section_cnt += 1
#                 if section_cnt == K and arr[row][new_col+1] == 0 and arr[row][col-1] == 0:
#                     num_of_words_row += 1
#
#     num_of_words_col = 0
#     for col in range(N):
#         for row in range(N):
#             new_row = 0
#             new_col = 0
#             section_cnt = 0
#             for i in range(K):
#                 new_row = row + i
#                 if 0 <= new_row <= N-1 and arr[new_row][col] == 1 :
#                     section_cnt += 1
#                 if section_cnt == K and arr[new_row+1][col] == 0 and arr[row-1][col] == 0 :
#                     num_of_words_col += 1
                    # 애매하게 조건 하나씩 빼먹었다 -> 구현하는 부분에서 이 과정을 놓쳐버림, 구현을 어떻게 쉽게 할 수 있을지 잘 고민하기 그냥 넘어가지 말자
#
#     num_of_words = num_of_words_row + num_of_words_col
#     print(f'#{tc} {num_of_words}')

#
    # num_of_words = 0
    # for row in range(N) :
    #     cnt = 0
        # 이런 식으로 한 행을 다 보려면 초기화를 이 부분에서 하면 되는구나, 이 생각을 못함
    #     for col in range(N):
    #         if arr[row][col] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K :
    #                 num_of_words += 1
    #             cnt = 0
    #
    # for col in range(N):
    #     cnt = 0
    #     for row in range(N):
    #         if arr[row][col] == 1 :
    #             cnt += 1
    #         else:
    #             if cnt == K :
    #                 num_of_words += 1
    #             cnt = 0
    #
    # print(f'#{tc} {num_of_words}')



# 1974 스도쿠 검증
# 9*9 배열의 이차원리스트
# 행도 1~9까지 겹치는 것 없이 있어야 함
# 열도 1~9까지 겹치는 것 없이 있어야 함
# 3*3도 겹치는 것 없이 있어야 함
# -> 겹치는 숫자가 없는 경우 1 아니면 0

# 행을 어떻게 검증할 것인가?
# 어디에 단어가 들어갈 수 있을까와 비슷하게 구현하면 될 듯
# 각 숫자에 대해 누적으로 확인할 수 있는 리스트를 사용
# -> 빈 리스트를 넣고 i와 같은지 확인하고 같으면 i를 누적
# 한 행을 검증하면서 i+1 과 같은지 확인하고 같으면 i번째를 누적

# 빈 열을 만들기
# 열을 검증하면서 i+1 과 같은지 확인하고 같으면 i번째를 누적

# -> 만약 각 행과 열에 대해 누적한 리스트에 0이 있으면 0, 0이 없으면 1

# 그렇다면 3*3만큼씩은 어떻게 확인할 것인가?
# 행렬 3단위씩 반복하면서
    # -> 이걸 어떻게 할 것인가?
    # dr, dc를 활용하여 3칸씩 이동 -> *i만큼 가게 하기
    # 이 값을 빈 리스트에 넣어줌
# 자신과 그 주변 3*3을 확인 -> 한 3*3을 하고 나서 set으로 중복을 제거했을 때 set의 길이가 9명 1, 아니면 0

# import sys
# sys.stdin = open("1974_input.txt","r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = 9
#     sudoku = [list(map(int, input().split())) for _ in range(N)]
#     # print(sudoku)
#
#     row_confirm = 1
#     for row in range(N):
#         row_confirm_list = [0]*9
#         for col in range(N):
#             i = sudoku[row][col] - 1
#             row_confirm_list[i] += 1
#         if 0 not in row_confirm_list :
#             row_confirm *= 1
#         else:
#             row_confirm *= 0
#
#     col_confirm = 1
#     for col in range(N):
#         col_confirm_list = [0]*9
#         for row in range(N):
#             i = sudoku[row][col] - 1
#             col_confirm_list[i] += 1
#         if 0 not in col_confirm_list :
#             col_confirm *= 1
#         else:
#             col_confirm *= 0
#
#     arr_confirm = 1
#     for row in range(0, N, 3) :
#         arr_confirm_list = [0]*9
#         for col in range(0, N , 3) :
#             new_row = 0
#             new_col = 0
#             for new_row in range(3):
#                 for new_col in range(3):
#                     i = sudoku[new_row][new_col]-1
#                     arr_confirm_list[i] += 1
#             if 0 not in arr_confirm_list :
#                 arr_confirm *= 1
#             else:
#                 arr_confirm *= 0
#
#     if row_confirm == 1 and col_confirm == 1 and arr_confirm == 1 :
#         all_confirm = 1
#     else :
#         all_confirm = 0
#
#     print(f'#{tc} {all_confirm}')


# 1966 숫자를 정렬하자
# 주어진 N 길이의 숫자열을 오름차순으로 정렬
# T개의 tc가 주어짐
# N을 인풋받음
# N개의 숫자 길이를 가진 number가 주어짐
# 이 숫자를 오름차순으로 정렬

# 아 그 이름 뭐였는지 까먹었는데 전체 비교해서 가장 작은 수를 젤 앞으로 배치하고, 그 다음 부터 확인해서 젤 작은 수 배치하고 그 정렬 쓰고 싶어
# -> 이거 어떻게 하더라?
# 위치를 바꾸려면 number를 리스트로 입력 받아야 함
# n = 0
# number를 N번 순회함
    # for idx in range(N)
    # -> min값의 idx를 찾아
    # number[i], number[idx]를 서로 바꿔
    # n += 1

# import sys
# sys.stdin = open("1966_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     number = list(map(int, input().split()))
#     n = 0
#     for i in range(N) :
#         minV = 123e12
#         min_i = 0
#         for idx in range(n, N) :
#             if minV > number[idx] :
#                 minV = number[idx]
#                 min_i = idx
#         n += 1
#         number[i], number[min_i] = number[min_i], number[i]
#
#     print(f'#{tc}', *number)

# -> 짜는 법 다시 보기 이런 방식이 아니었던 것 같음
# -> 조금 다른데 대략 맞긴 함
# -> 마지막은 고정이라 N-1만큼 순회
# -> 가장 작은 값의 인덱스를 i로 설정??
# -> 아 그것보다 다음 인덱스가 더 작으면 위치 바꾸려고 인덱스 불러와서 값을 비교했구나
# -> 나는 그냥 가장 작은 값과 해당 인덱스 값을 비교한 거고
# 기준이 나였네, 난 minV를 계속 바꿔나간 거였는데 이건 계속 자리를 바꾸면서 갔네


# 1945 간단한 소인수분해
# N은 숫자
# 그 숫자를 소인수분해함
# 2, 3, 5, 7, 11을 몇번씩 곱해서 해당 숫자가 나오는지를 확인해야 함
# -> 각 숫자로 나눴을 때 나머지가 0이면 해당 숫자들이 들어갔다는 것은 알겠음
# 몇 제곱인지는 어떻게 알지?
# 매번 각 숫자로 나누기 해서 나머지가 0인걸 채택해서 +1 해줘야겠네
# 더 안 나눠질 때까지 -> 이걸 어떻게 확인해? 일단 2가 있으니까 안 나눠지는 가장 작은 정수는 1
# 몫이 1이 될 때까지 찾아야겠네
#
# import sys
# sys.stdin = open("1945_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     numbers = int(input())
#     divide_num = [2, 3, 5, 7, 11]
#     divide_num_check = [0]*5
#     while numbers > 1 :
#         for i in range(len(divide_num)) :
#             if numbers % divide_num[i] == 0 :
#                 divide_num_check[i] += 1
#                 numbers = numbers // divide_num[i]
#
#     print(f'#{tc}', *divide_num_check)











