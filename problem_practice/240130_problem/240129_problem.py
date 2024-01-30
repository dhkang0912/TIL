# 4828 min, max
# T = int(input())
# # 1. T만큼 테스트 케이스를 돌린다.
# # 2. number를 순회한다
#     # 3. 만약 number 요소가 number보다 크다면 number에 할당한다
# for idx in range(1, T+1) :
#     N = int(input())
#     number = list(map(int, input().split()))
#     max_v = 0
#     min_v = 1241e5
#     for num in number :
#         if max_v < num :
#             max_v = num
#
#     for num in number :
#         if min_v > num :
#             min_v = num
#
#     result = max_v - min_v
#     print(f'#{idx} {result}')

# import sys
# sys.stdin = open("4835_sample_input.txt", 'r')
#import sys
#sys.stdin = open("input.txt", "r")
# 4835 구간합
# sum 사용
# T = int(input())
# for t in range(1, T+1):
#     #t번 테스트 케이스를 돌린다.
#     N, M = list(map(int, input().split()))
#     number = list(map(int, input().split()))
#     # N개의 숫자가 주어짐
#     # 구간의 갯수 M이 주어짐
#     Max_N = 0
#     Min_N = 12345e19828
#     for i in range((N-M)+1) :
#         if Max_N < sum(number[i:M+i]) :
#             Max_N = sum(number[i:M+i])
# 
#         if Min_N > sum(number[i:M+i]) :
#             Min_N = sum(number[i:M+i])
# 
# 
#     result = Max_N - Min_N
#     print(f'#{t} {result}')


# T = int(input())
# for t in range(1, T+1):
#     #t번 테스트 케이스를 돌린다.
#     N, M = map(int, input().split())
#     number = list(map(int, input().split()))
#     # N개의 숫자가 주어짐
#     # 구간의 갯수 M이 주어짐
#     Max_N = 0
#     Min_N = 12345e19828
#     for i in range((N-M)+1):
#         sum_num = 0
#         for num in range(i, M+i):
#             sum_num += number[num]
#         if Max_N < sum_num:
#             Max_N = sum_num
#         if Min_N > sum_num:
#             Min_N = sum_num
#
#     result = Max_N - Min_N
#     print(f'#{t} {result}')




# 1일차_view
# 가로 길이 확인
# 건물의 갯수
# 건물의 높이
import sys
sys.stdin = open("240129_input.txt", "r")

T = 10

for tc in range(1, T+1) :
    N = int(input()) # 건물 개수
    Height = list(map(int, input().split())) # 건물 높이
    accumulate_height = 0
    for i in range(2, N-2) :
        Height_over = [Height[i-2], Height[i-1], Height[i+1], Height[i+2]]
        result = 0
        if (Height[i] > Height[i-1]) and (Height[i] > Height[i-2]) and (Height[i] > Height[i+1]) and (Height[i] > Height[i+2]):
            max_a_h = 0
            for H_v in Height_over:
                if max_a_h < H_v:
                    max_a_h = H_v
            result = Height[i] - max_a_h
        accumulate_height += result
    print(f'#{tc} {accumulate_height}')



