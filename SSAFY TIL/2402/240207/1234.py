# [S/W 문제해결 기본] 10일차 - 비밀번호
# 0~9번호 문자열
# 같은 번호로 붙어있는 쌍들을 소거하고
# 남은 번호로 비밀번호를 만듦

# 소거된 후 쌍들이 같은 번호이면 다시 소거할 수 잇음

# 인풋
# 10개의 tc를 줌
# N, number가 같이 주어짐, number->list로 받기

# 로직
# stack 활용
# stack[0] = numbers[0]
# numbers 요소를 순회하면서
    # c가 stack[-1]과 같으면 pop
    # 만약 다르다면 append


# 아웃풋
# #{tc} {number}

import sys
sys.stdin = open("1234_input.txt", "r")

T = 10
for tc in range(1, T+1):
    N, numbers = input().split()
    N = int(N)
    password = []
    for num in numbers :
        if len(password) > 0 and num == password[-1]:
            password.pop()
        else:
            password.append(num)

    print(f'#{tc}', ''.join(password))