from collections import deque

N = int(input())
for tc in range(1, N+1):
    lst = deque(list(input()))
    stack = []
    N = len(lst)
    check = 1
    for ele in lst:
        if ele == '(':
            stack.append(ele)
        elif len(stack) > 0 and ele == ')':
            stack.pop()
        elif len(stack) <= 0 and ele == ')':
            check = 0


    # if len(stack) == 0 and check == 1:
    #     print('YES')
    # else:
    #     print('NO')

    if check == 0:
        print('NO')
    elif len(stack) > 0 and check == 1:
        print('NO')
    elif len(stack) == 0 and check == 1:
        print('YES')


