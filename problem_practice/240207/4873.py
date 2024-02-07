# 4873 반복문자 지우기
# 반복된 문자를 지움 -> 지우고 앞뒤 연결
# 연결에 의해 또 반복 문자가 생기면 다시 지움
# -> 반복된 문자 확인 pop으로 해당 문자 삭제를 반복 -> 재귀함수인가? 아니네 그냥 포문
# 남은 문자를 리턴
# 리턴 값이 있으므로 되도록 함수로 짜기

# 테스트 케이스 T를 인풋 받음
# 길이가 1000 이내인 문자열이 주어짐
# 연결되어 반복된 문자가 있으면 삭제하는 함수를 만듦
    # 문자의 길이만큼 i를 순회하며 반복하기
        # 현재꺼와 다음꺼를 확인했을 때 같다면 해당 문자를 삭제
        # 반복된 문자가 없을 때까지 동일한 것을 반복
        # -> 만약 반복된 문자가 없을 경우 해당 값을 리턴
# 이 함수를 호출하기
import sys
sys.stdin = open("4873_input.txt", "r")

# def pop(str_, N):
#     i = 1
#     while i <= N-1:
#         if str_[i-1] == str_[i]:
#             str_.pop(i)
#             str_.pop(i-1)
#             N -= 2
#             i = 1
#         else:
#             i += 1
#
#     return len(str_)
#
#
T = int(input())
for tc in range(1, T+1):
    str_ = list(input())
    N = len(str_)
#     result = pop(str_, N)
#     print(f'#{tc} {result}')

    stack = []
    for c in str_:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    print(f'#{tc}', len(stack))
