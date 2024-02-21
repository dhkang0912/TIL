import sys
sys.stdin = open("1225_input.txt", "r")

T = 10
for tc in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))

    while numbers[-1] > 0:.
        for i in range(1, 6):
            num = numbers.pop(0) - i
            if num < 0:
                num = 0
            numbers.append(num)
            if numbers[-1] == 0:
                break

    print(f'#{tc}', *numbers)