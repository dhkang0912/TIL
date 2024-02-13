import sys
sys.stdin = open("1222_input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    s = input()
    result = []
    stack = []
    for c in s:
        if c.isdigit():
            result.append(c)
        else:
            stack.append(c)
            if len(result) >= 2:
                result.append(stack.pop())
    result.append(stack.pop())
    print(result)

    stack2 = []
    for char in result:
        if c.isdigit():
            stack2.append(char)
        else:
            










