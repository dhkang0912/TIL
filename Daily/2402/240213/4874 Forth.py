# 4874 Forth

import sys
sys.stdin = open("4874_input.txt", "r")

def calc(v1, v2, i):
    if i == '+':
        return v1 + v2
    elif i == '-':
        return v1 - v2
    elif i == '*':
        return v1 * v2
    else:
        return v1 // v2


T = int(input())
for tc in range(1, T+1):
    numbers = input().split()
    ST = []
    try:
        for i in numbers:
            if i.isdecimal():
                ST.append(i)
            elif i == '.' :
                result = ST.pop()
                if not ST:
                    print(f'#{tc}', result)
                else:
                    print(f'#{tc} error')
            elif not i.isdecimal():
                v2 = ST.pop()
                v1 = ST.pop()
                ST.append(calc(int(v1), int(v2), i))
    # print(f'#{tc}', ST.pop())
    except:
        print(f'#{tc} error')