# import sys
# sys.stdin = open("4874_sample.txt", "r")

def calc(v1, v2, c):
    v1 = int(v1)
    v2 = int(v2)
    if c == '+':
        return v1 + v2
    elif c == '-':
        return v1 - v2
    elif c == '*':
        return v1 * v2
    else:
        return v1 // v2

T = int(input())
for tc in range(1, T+1):
    sentence = list(input().split())
    stack = []
    error_check = 0
    for c in sentence:
        if c == '.':
            break
        elif c not in '+-*/':
            stack.append(c)
        elif c in '+-*/' and len(stack) >= 2:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(calc(v1, v2, c))
        else:
            error_check = 1
            break

    if len(stack) == 1 and error_check == 0:
        print(f'#{tc}', stack[0])
    else:
        print(f'#{tc} error')

