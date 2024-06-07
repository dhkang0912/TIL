# import sys
# sys.stdin = open("4866_input (1).txt", "r")

def check(c):
    # global result
    global stack
    match = [['(','{'], [')','}']] # 여는 괄호 쌍, 닫는 괄호 쌍 (, { 순서로 매칭인
    # 문자, 여는 괄호, 닫는 괄호가 들어올 수 있음
    # -> 문자인 경우 조건이 (없어{ 그)냥} 종료

    if c not in match[0] and c not in match[1]:
        return 1
    if c in match[0]: # 여는 괄호인 경우 stack에 여는 괄호 추가
        stack.append(c)
    elif c in match[1]:
         # 닫는 괄호인 경우 닫는 괄호인(match[1][i]) 중 어떤 괄호인지 확인
        if len(stack) > 0:
            for idx in range(2):# 매칭된 닫는 괄호를 찾았으면
                if match[1][idx] == c:
                    if stack.pop() == match[0][idx]:# 닫는 괄호랑 매칭되는 여는 괄호가 맞아?
                        return 1 # 그럼 제대로 된 괄호야
                    else:  # 그렇지 않아?
                        return 0  # 이미 잘못됐으니 끝내줘
        else:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    sentence = input() # 여는 괄호, 닫는 괄호, 문자가 섞여서 들어옴
    stack = []
    # result = 1 # 결과를 저장할 global 변수
    for c in sentence: # 받은 문장을 하나씩 순회
        result = check(c) # 하나씩 문자 확인
        if result == 0:
            break

    if len(stack) <= 0:
        print(f'#{tc}', result)
    else:
        print(f'#{tc}', 0)

