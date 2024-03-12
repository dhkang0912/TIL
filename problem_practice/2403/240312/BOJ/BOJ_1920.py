'''
수 찾기
정수가 주어졌을 때 특정 X라는 정수가 존재하는지 알아보기 위한 프로그램

N개의 정수가 주어지고, M개의 수들이 주어짐
M의 수가 N 사이에 들어가는지 확인해보면

간단하지만 타입별 시간을 확인하는 문제
set이 list보다 훨씬 빠름

이중 for 문이 in으로 확인하는 것보다 더 빠름

이진탐색으로도 확인 가능
-> 재귀로 사용할 때는 mid+1, mid-1로 인덱스 위치가 조정될 수 있음
-> while로도 가능하고 이게 시간이 덜 걸릴 수 있음
'''
import sys
input = sys.stdin.readline

N = int(input())
N_numbers = list(map(int, input().split()))
N_numbers.sort()
# min_N_numbers = min(N_numbers)
# max_N_numbers = max(N_numbers)

M = int(input())
M_numbers = list(map(int, input().split()))

# for i in range(M):
#     if M_numbers[i] not in N_numbers:
#         print(0)
#     else:
#         print(1)

def binary(num, start, end):
    if start > end:
        return 0
    mid = (start+end)//2

    if num == N_numbers[mid]:
        return 1
    elif num < N_numbers[mid]:
        # 끝 인덱스가 바뀜
        return binary(num, start-1, mid)
    else:
        # 시작 인덱스가 바뀜
        return binary(num, mid+1, end)

for i in range(M):
    start = 0
    end = N - 1
    print(binary(M_numbers[i], start, end))

