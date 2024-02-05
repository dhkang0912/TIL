# 4865 글자수
# import sys
# sys.stdin = open("4865_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     str1 = list(input())
#     str2 = list(input())
#     count_num = [0] * len(str1)
#     maxV = 0
#
#     for str in str2 :
#         for idx in range(len(str1)) :
#             if str == str1[idx]:
#                 count_num[idx] += 1
#
#     for num in count_num:
#         if maxV < num:
#             maxV = num
#
#
#     print(f'#{tc} {maxV}')

# 4864 문자열 비교
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input() #확인할 문자
#     str2 = input() #주어진 문자
#     if str1 in str2 :
#         result = 1
#     else:
#         result = 0
#     print(f'#{tc} {result}')


# [S/W 문제해결 기본] 5일차 - GNS
# 0~9까지 숫자 체계가 문자로 지정
# 작은 수부터 차례로 정렬하는 프로그램 필요
# 문자열과 값을 매칭하여 정렬 필요

T = int(input())
for tc in range(1, T+1):
    tc_num, N = input().split()
    N = int(N)
    num_list = list(input().split())
    order = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5 , "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    for i in range(N):
        num_list[i] = order[num_list[i]]


    for idx in range(N) :
        minV = 12e23
        minP = 0
        for i in range(idx, N) :
            if minV > num_list[i]:
                minV = num_list[i]
                minP = i
        num_list[idx], num_list[minP] = num_list[minP], num_list[idx]

    result = []
    for key in order.keys():
        for i in range(len(num_list)):
            if num_list[i] == order[key]:
                result.append(key)

    print(f'{tc_num}', *result)



    # T = int(input())
    #
    # for tc in range(1, T + 1):
    #     tc_num, N = input().split()
    #     N = int(N)
    #     num_list = list(input().split())
    #     order = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    #     for i in range(N):
    #         num_list[i] = order[num_list[i]]
    #
    #     for i in range(N):
    #         minV = num_list[i]
    #         minP = i
    #         for j in range(i + 1, N):
    #             if minV > num_list[j]:
    #                 minV = num_list[j]
    #                 minP = j
    #         num_list[i], num_list[minP] = num_list[minP], num_list[i]
    #
    #     result = []
    #
    #     print(f'{tc_num}', *num_list)