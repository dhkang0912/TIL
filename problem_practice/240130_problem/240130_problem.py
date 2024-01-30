# Counting 정렬
# DATA = [0, 4, 1(1), 3, 1(2), 2, 4, 1(3)]
# TEMP = [0, 1(1), 1(2), 1(3), 2, 3, 4, 4]

# DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# # TEMP = [0, 1, 1, 1, 2, 3, 4, 4]
# K = 4 # DATA에 있는 것 중 가장 큰 값 + 1
# N = len(DATA) # DATA의 길이
# COUNTS = [0] * (K+1)
# for d in DATA :
#     COUNTS[d] += 1
#
# # print(COUNTS)
# for i in range(1, K+1) :
#     COUNTS[i] =  COUNTS[i] + COUNTS[i-1]
#
# TEMP = [-1] * N
# # for d in DATA[::-1] :
# for i in range(N-1, -1, -1) :
#     d = DATA[i]
#     idx = COUNTS[d] - 1
#     TEMP[idx] = d
#     COUNTS[d] -= 1
#
# print(TEMP)
#
#
# numbers = [0, 1 ,2]
# for i in range(3):
#     for j in range(3) :
#         if j == i :
#             continue
#         for k in range(3) :
#             if k == i or k == j :
#                 continue
#             print(i, j, k, '=>', numbers[i], numbers[j], numbers[k])



# i = 0
# tri = run = 0
# while i < 10 :
#     if c[i] >= 3: # triplete 조사 후 데이터 삭제
#         c[i] -= 3
#         tri += 1
#         continue;
#     if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1 : #run 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i + 1] -=1
#         c[i + 2] -=1
#         run += 1
#         continue
#         i += 1
#     if run + tri == 2:
#         print("Baby Gin")
#     else: print("Lose")


#<baby-gin>

# N=6
# def babygin(n_numbers):
#     counts =[0]*12
#
#     for _ in range(6) :
#         #d = n_numbers%10
#         counts[n_numbers%10] += 1
#         n_numbers //= 10
#
#     print(counts)
#
# # def babygin(s_numbers):
# #     counts =[0]*12
# #     numbers = list(map(int, s_numbers))
# #     for n in numbers :
# #         counts[n] += 1
# #     print(s_numbers, counts)
#
#     n_tri = 0
#     n_run = 0
#     i = 0
#     while i < 10 :
#     #tri
#         if counts[i] >= 3 :
#             n_tri += 1
#             counts[i] -= 3
#             continue
#
#     #run
#         if i <=7 and (counts[i]>0 and counts[i+1]>0 and counts[i+2]>0) :
#             n_run += 1
#             counts[i] -=1
#             counts[i+1] -= 1
#             counts[i+2] -= 1
#
#         i += 1
#     print(n_tri, n_run)
#     return
#
# # babygin('445678')
# # babygin('475432')
# babygin(475432)



#  4834 숫자카드
# N장의 카드를 인풋 받음 (0~9까지)
# 가장 많은 카드에 적힌 숫자, 카드가 몇장인지 출력하는 프로그램 만들기 (장수가 같다면 큰 숫자 출력)

# 1. T번 tc를 반복하여 출력함 #테스트 케이스 반복
    # 1) 카드 장수인 N을 인풋 받음
    # 2) Num에 숫자를 공백 없이 인풋 받음 -> 이걸 어떻게 쪼갤 것인가? (나머지를 통해서 할 수 있음)
        # 2-1) Num_list = []
        # 2-1) for i in N 통해서, 리스트에 집어넣기
            # 2-1-1) add_num = Num % 10
                    # Num_list.append[add_num] # 마지막 자리부터 들어
                    # Num = Num// 10
                #Num_list.reversed() # 순서를 뒤집어서 맞춰줌

    # 3) accumulate_Num = [0] * N
    # 3) for i in Num_list :
        # 3-1) accumulate_Num[i] += 1

    # 4) Max_num = 0
    # 4) idx = 0
    # 4) for i in range(len(accumulate_Num)) :
        #4-1) if Max_num < accumulate_Num[i] :
        # 4-2) Max_Num = accumulate_Num[i]
        # 4-3) idx = i

    # 5. print(f'#{tc} {idx} {Max_Num}

# import sys
# sys.stdin = open("4834_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input())
#     Num = int(input())
#     Num_list = []
#     for i in range(N) :
#         add_num = Num % 10
#         Num_list.append(add_num)
#         Num = Num // 10
#     # Num_list.reverse()
#     Num_list = Num_list[::-1]
#
#     accumulate_Num = [0] * 10
#     for i in Num_list :
#         accumulate_Num[i] += 1
#
#     Max_Num = 0
#     idx = 0
#     for i in range(len(accumulate_Num)) :
#         if Max_Num <= accumulate_Num[i] :
#             Max_Num = accumulate_Num[i]
#             idx = i
#
#     # Num = 0 8 2 7 1
#     #                0 1 2 3 4 5 6 7 8 9
#     # accumulate_Num 1 1 1 0 0 0 0 1 1 0
#
#     print(f'#{tc} {idx} {Max_Num}')


# [S/W 문제해결 기본] 1일차 - Flatten D3
# 높은 곳 상자를 -1, 낮은 곳에 +1 -> 반복하여 평탄화
# 가장 높은 곳 - 가장 낮은 곳  <= 1
# 옮기는 횟수가 정해져있음 -> n개만큼 옮긴 후 점(최고점 - 최저점)
# 가장 높은 곳에서 -1, 가장 낮은 곳으로 +1을 N번 반복해야 함
# 숫자의 최대 갯수 (가로의 길이)가 100으로 제한됨
# 높이는 1이상 100 이하로 제한됨
# 옮기는 dump라는 작업의 제한은 1이상 1000 이하 -> dump 횟수 제한이 끝나면 -> 최고점 - 최저점

# 1. T = 10
# 2. 10개의 테스트 케이스를 순회함
    # 1) dump의 횟수를 인풋 받음
    # 2) box_height에 각 상자의 높이를 인풋 받음 -> 리스트에 넣음

    # 3) for i in range(dump) :
        # 3) min_box_height와 max_box_height를 찾음 -> min, max를 box_height의 첫번째 v로 지
            # for num in box_height :
                # if min_box_height < num :
                #   min_box_height = num
                # if max_box_height > num :
                # max_box_height = num
            # box_height[box_height.index(min_box_height)] += 1
            # box_height[box_height.index(min_box_height)] -= 1


# import sys
# sys.stdin = open("240130_input.txt", "r")
#
#
#
# T = 10
# for tc in range(1, T+1) :
#     dump = int(input())
#     box_height = list(map(int, input().split()))
#
#     for i in range(dump) :
#         min_box_height = 124325e1334
#         max_box_height = 0
#         for num in box_height :
#             if min_box_height > num :
#                 min_box_height = num
#             if max_box_height < num :
#                 max_box_height = num
#         box_height[box_height.index(min_box_height)] += 1
#         box_height[box_height.index(max_box_height)] -= 1
#
#
#     min_v = 124325e1334
#     max_v = 0
#     for box_height_element in box_height :
#         if min_v > box_height_element :
#             min_v = box_height_element
#         if max_v < box_height_element :
#             max_v = box_height_element
#
#     result = max_v - min_v
#
#     print(f'#{tc} {result}')


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
#           # 5-2-2) 충천 횟수 +1을 한다
        # 5-3) 이동 횟수를 -1한다


