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
                        # for jump in range(1, arr[row][col]+1):
                        #     newR = row + dr*jump



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






