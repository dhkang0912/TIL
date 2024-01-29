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



# 4835 구간합
t = int(input())
for t in range(1, t+1):
    #t번 테스트 케이스를 돌린다.
    N, M = list(map(int, input().split()))
    number = list(map(int, input().split()))
    # N개의 숫자가 주어짐
    # 구간의 갯수 M이 주어짐
    Max_N = 0
    Min_N = 12345e19828
    for i in range(len(number)) :
        if Max_N < sum(number[i:M+i]) :
            Max_N = sum(number[i:M+i])

        if Min_N > sum(number[i:M+i]) :
            Min_N = sum(number[i:M+i])

    result = Max_N - Min_N
    print(f'#{t} {result}')







# 1일차_view
# 가로 길이 확인
# 건물의 갯수
# 건물의 높이