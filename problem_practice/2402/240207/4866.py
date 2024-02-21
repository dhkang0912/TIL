# 4866 괄호 검사
# stack 개념 사용해서 풀어보기
# 괄호의 짝을 검사하기
# -> 어떻게 짝이 맞는지 확인할까?
    # -> stack = []
    # -> 각 요소들을 for문으로 하나씩 순회하기
    # -> 제일 처음 순회 시 { or (라면 stack에 append를 한다
    # -> 지금이 }일 때 직전이 {라면 pop 지금을 한다
    # -> 지금이 )일 때 직전이 (라면 pop 지금을 한다

    # 만약 둘 다 아니라면 다음으로 넘어간다

# 모두 짝이 맞는 괄호이면 1
    # 만약 stack이 빈 괄호라면(False) 1을 프린트
# 짝이 맞지 않는 괄호이면 0
    # 만약 stack에 뭐라도 남아있으면 0을 프린트
#
import sys
sys.stdin = open("4866_input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     str = input()
#     stack = []
#     for c in str:
#         if c == '{' or c == '(' or c ==')' or c == '}':
#             if len(stack) > 0 and (stack[-1] == '{') and (c == '}'):
#                 stack.pop()
#             elif len(stack) > 0 and (stack[-1] == '(') and (c == ')'):
#                 stack.pop()
#             else:
#                 stack.append(c)
#
#     if len(stack) == 0:
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')


T = int(input())
for tc in range(1, T+1):
    str = input()
    stack = []
    check = 1
    # 스택이 비어있는 경우
        # {( <- 이건 들어가야 하고
        # )} <- check를 False
    # 스택이 들어있는 경우
        # 짝이 맞는 경우
            # { (가 들어있음
            # -> 앞의 것과 현재 c가 짝이 되면 stack 앞 값을 삭제

        # 짝이 맞지 않는 경우
            # {()}))
            # 그렇지 않으면 chek를 False


    # for c in str:
    #     if c in ['{', '(', ')', '}']:
    #         if (c == '{') or (c == '('):
    #             stack.append(c)
    #         elif len(stack) > 0 and stack[-1] == '{' and c == '}':
    #             stack.pop()
    #         elif len(stack) > 0 and stack[-1] == '(' and c == ')':
    #             stack.pop()
    #         else:
    #             check = 0
    #             break
    #
    # if check == 1 and len(stack) > 0:
    #     check = 0
    #
    #
    # print(f'#{tc} {check}')





    for c in str:
        if (c == '(') or (c == '{') or (c == '}') or (c == ')'):
            if (len(stack) > 0) and (stack[-1] == '{') and (c == '}'):
                stack.pop()
            elif (len(stack) > 0) and (stack[-1] == '(') and (c == ')'):
                stack.pop()
            else:
                stack.append(c)

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')



