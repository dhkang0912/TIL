'''
N, M
수의 개수 N, 합을 구해야하는 횟 M

numbers = N개의 수

합을 구해야하는 구간의 인덱스

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
pre_sum = [0]

temp_sum = 0
for num in numbers:
    temp_sum += num
    # 누적합이 될 때마다 관련된 합을 pre_sum에 저장
    pre_sum.append(temp_sum)


result_sum = 0
for _ in range(M):
    i, j = map(int, input().split())
    # j+1까지 더한 거에서 a까지 더한 걸 빼면 사이 값
    # 1 2 3 4 5
    # result_sum = sum(numbers[i:j+1])
    # print(result_sum)
    result = pre_sum[j+1]-pre_sum[i]
    print(result)
