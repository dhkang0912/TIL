# 5432. 쇠막대기 자르기
# 빨리 하고 오랜만에 애니 봐야지 룰루
# 쇠막대기로 세로로 절단
# 쇠막대기를 쌓을 수 있는 규칙
    # 자신보다 긴 쇠막대기 위에만 놓일 수 있음
    # 위에 놓는 경우 완전히 포함하지만 끝점은 겹치면 안됨
    # 긴 쇠막대기를 자르는 레이저는 적어0도 하나 존재함
    # 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음
# 레이저는 괄호 ()쌍으로 나타냄
# 쇠막대기는 몇개의 조작으로 잘려지는데
    # 자른 곳 +1씩 조각남
# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때,
# 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램 작성

import sys
sys.stdin = open("5432_input.txt","r")

# T = int(input())
# for tc in range(1, T+1):
#     sticks = list(map(str, input()))
#     stack = []
#     cnt = 0
#     for i in range(len(sticks)):
#         if sticks[i] == "(":
#             stack.append("(")
#         elif sticks[i] == ")":
#             if sticks[i-1] == "(":
#                 stack.pop()
#                 cnt += len(stack)
#             else:
#                 stack.pop()
#                 cnt += 1
#     print(cnt)


T = int(input())
for tc in range(1, T+1):
    sticks = list(input())
    stack = []
    cnt = 0
    for i in range(len(sticks)):
        if sticks[i] == '(':
            stack.append('(')
        elif sticks[i] == ')' and sticks[i - 1] == '(':
                stack.pop()
                cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

    print(f'#{tc}', cnt)
