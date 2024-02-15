# 5097_회전
# N개의 숫자로 이루어진 수열
# 맨 앞의 숫자를 맨뒤로 보내는 작업을 M번 했을 때 수열의 맨 앞에 있는 숫자 출력
import sys
sys.stdin = open("5097_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 숫자의 갯수, M = 이동 횟수
    numbers = list(map(int, input().split()))
    for i in range(M):
        num = numbers.pop(0)
        numbers.append(num)
    result = numbers[0]

    print(f'#{tc}', result)

