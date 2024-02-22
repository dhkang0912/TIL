# 5185_이진수
import sys
sys.stdin = open("5185_input.txt", "r")
'''
16진수 1자리 => 2진수 4자리로 표시
N자리 16진수 =>각 자리수를 4자리 2진수로 표시
2진수의 앞자리 0도 반드시 출력
'''
# 십진수를 이진수로 변환하는 함수
def decTobin(intV):
    s = ''
    for _ in range(4):
        s = str(intV%2) + s
        intV //= 2
    return s



T = int(input())
for tc in range(1,T+1):
    N, S = list(input().split())
    N = int(N)
    # print(N, S)
    '''
    4 47FE
    5 79E12
    8 41DA16CD
    '''
    result = ''
    for c in S:
        if c.isdecimal():
            result += decTobin(int(c))
        else:
            result += decTobin(ord(c) - ord('A') + 10)

    # print(decTobin(20))
    print(f'#{tc} {result}')


