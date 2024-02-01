# 1954. 달팽이 숫자
# import sys
# sys.stdin = open("1954_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     print(f'#{tc}')
#     N = int(input()) # N*N 배열이라는 의미
#     arr = [[0] * N for _ in range(N)]
#
#     value = 0
#     d = 0
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     row = 0
#     col = 0
#
#     for _ in range(N*N) :
#         value += 1
#         arr[row][col] = value
#         row = row + dr[d]
#         col = col + dc[d]
#         if row < 0 or col < 0 or row > N-1 or col > N-1 or arr[row][col] != 0 :
#             row = row - dr[d]
#             col = col - dc[d]
#             d = (d+1)% 4
#             row = row + dr[d]
#             col = col + dc[d]
#
#
#     for new_row in range(N) :
#         for new_col in range(N) :
#             print(arr[new_row][new_col], end = ' ')
#         print()


# 1966. 숫자를 정렬하자
# import sys
# sys.stdin = open("4843_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input()) # numbers의 갯수
#     numbers = list(map(int,input().split()))
#
#     for i in range(N-1) :
#         minV = numbers[i]
#         minP = i
#         for idx in range(i+1, N) :
#             if minV > numbers[idx] :
#                 minV = numbers[idx]
#                 minP = idx
#         numbers[i], numbers[minP] = numbers[minP], numbers[i]
#
#     print(f'#{tc}', *numbers)


# 4843 특별한 정렬
# 테스트 케이스 T를 인풋 받음
# 정수의 갯수 N을 인풋 받음
# num = N개의 정수가 주어짐
# 가장 큰 수, 가장 작은 수, 2번째 큰수, 2번째 작은수를 번갈아 정렬
# 가장 큰 수 찾기
# 10개가 있을
# num[0]일 때 -> num[1]~num[9]까지 확인
# num[1]~num[9] 중에서 가장 큰 수를 찾기 -> maxV
# maxV와 num[0] 값의 위치를 할당을 통해 바꾸기
# -> maxV와 maxV의 idx를 알아야 함함
# 0번째 수와 maxV의 idx번째 를 변경해줘야
# 가장 작은 수 찾기
# 10개가 있을 때 -> 큰 수를 찾고 다음 값에 작은 수를 찾아야
# num[1]일 때 -> num[2]~num[9]까지 확인
# num[1]~num[9] 중에서 가장 작 수를 찾기 -> minV
# minV와 num[0] 값의 위치를 할당을 통해 바꾸기
# -> minV와 minV의 idx를 알아야 함
# 1번째 수와 maxV의 idx번째 를 변경해줘야 함

# import sys
# sys.stdin = open("4843_input.txt", "r")
#
#
# T = int(input())
# for tc in range(1, T+1) :
#     n = int(input())
#     number = list(map(int, input().split()))
#     # print(number)
#
#     for i in range(0, n-1, 2) :
#         maxV = number[i]
#         maxP = i
#         minV = number[i+1]
#         minP = i+1
#         for max_idx in range(i+1, n) :
#             if maxV < number[max_idx] :
#                 maxV = number[max_idx]
#                 maxP = max_idx
#         number[i], number[maxP] = number[maxP], number[i]
#
#         for min_idx in range(i+2, n) :
#             if minV > number[min_idx] :
#                 minV = number[min_idx]
#                 minP = min_idx
#         number[i+1], number[minP] = number[minP], number[i+1]
#
#     print(f'#{tc}', *number[0:10])

# 4839 이진탐색력
# T개의 테스트 개수를 인풋 받음
# 찾을 범위인 P가 주어짐, 찾을 번호인 A, B가 주어
# A, B 두 명이 각자 찾을 쪽 번호가 주어짐
# -> 찾을 번호가 2개 주어짐
# A 번호를 이진탐색으로 찾기 위해 반복을 돌린 횟수를 셈
# 총 숫자의 길이의 // 2 로 나는 위치의 수를 A와 비교
# 만약 A보다 숫자가 작으면 시작의 위치를 숫자의 위치+1로 바꿔줌
# 만약 A보다 숫자가 크면 끝의 위치를 숫자의 위치-1로 바꿔줌
# 만약 A랑 숫자가 같으면 숫자의 위치를 반
# 총 길이를 알 수 없으니 while 끝나는 조건은 ? -> 시작보다 끝이 작거나 같을
# B 번호를 이진탐색으로 찾기 위해 반복을 돌린 횟수를 셈
# -> 동일하면 0, A가 먼저 나오면 A, B가 먼저 나오면 B를 출


import sys
sys.stdin = open("4839_input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    # P = 찾을 범위, N개 / A = 찾을 숫자 1, B = 찾을 숫자 2때
    startA = 1
    endA = P
    middleA = 0
    cntA = 0
    while startA <= endA:
        middleA = (startA + endA) // 2
        cntA += 1
        if middleA == A:
            break
        if A < middleA:
            endA = middleA
        if A > middleA:
            startA = middleA

    startB = 1
    endB = P
    middleB = 0
    cntB = 0

    while startB <= endB:
        cntB += 1
        middleB = (startB + endB) // 2
        if middleB == B:
            break
        if B < middleB:
            endB = middleB
        if B > middleB:
            startB = middleB

    if cntA == cntB:
        print(f'#{tc} 0')
    elif cntA < cntB:
        print(f'#{tc} A')
    elif cntA > cntB:
        print(f'#{tc} B')
