# 1240_이진수2
import sys
sys.stdin = open("5186_input.txt", "r")
'''
0보다 크고 1미만인 십진수 N을 이진수로 바꿈
'''

T = int(input())
for tc in range(1,T+1):
    num = float(input())
    divide = 0.5
    s = ''
    while num > 0:
        if len(s) <= 12:
            if num >= divide:
                num = num - divide
                s += '1'
                divide *= 0.5
            else:
                s += '0'
                divide *= 0.5
        else:
            s = 'overflow'
            break
    print(f'#{tc} {s}')