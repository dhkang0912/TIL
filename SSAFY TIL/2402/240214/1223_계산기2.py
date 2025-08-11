# 1223. 계산기 2
# 후위계산식으로 변경하기
# 숫자는 우선 뽑기, 연산자를 스택에 저장
# 만약 다음 뽑힌 것도 연산자라면 연산자 우선순위를 비교
    # -> 만약 연산자 우선순위가 낮다면 result에 넣어주면 됨
    # -> 만약 연산자 우선순위가 높다면 나보다 우선순위 낮은 애를 만날 때까지 연산자를 result에 넣어줌
# 남아있는 연산자가 있으면 그걸 뽑아서 result에 넣어줌

import sys
sys.stdin = open("1223_input.txt", "r")

def post_fx(s):
    result = []
    stack = []
    for c in s:
        if c.isdecimal():
            result.append(c)
        else:
            if stack and prio[c] > prio[stack[-1]]:
                stack.append(c)
            else:
                while stack and prio[c] <= prio[stack[-1]]:
                    result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    return result

def calc(s, v1, v2):
    if s == '+':
        return v1 + v2
    elif s == '-':
        return v1 - v2
    elif s == '*':
        return v1 * v2
    else:
        return v1 // v2


def calc_post(fx):
    stack = []
    for c in fx:
        if c.isdigit():
            stack.append(c)
        else:
            if stack:
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(calc(c, int(v1), int(v2)))
    return stack



T = 10
for tc in range(1, T+1):
    N = int(input())
    s = input()
    prio = {'+':1, '-':1, '*':2, '//':2}
    # print(post_fx(s))
    print(f'#{tc}', *calc_post(post_fx(s)))


