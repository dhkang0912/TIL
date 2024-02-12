# 3143. 가장 빠른 문자열 타이핑
# 문자열 A를 타이핑
# 이미 저장된 문자열이 존재
#
# 전체 타이핑을 위해 키를 눌러야 하는 횟수의 최솟값을 출력
import sys
sys.stdin = open("3143_input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    A = list(A)
    B_num = len(B)
    A_num = len(A)
    temp = []
    result = ""
    for char in range(0, A_num, B_num):
        if 
        else:
            result.append(A[char:char+B_num])

    print(f'#{tc}', len(result)+1)