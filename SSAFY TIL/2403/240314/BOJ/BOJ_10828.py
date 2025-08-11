'''
스택 구현하기

함수 만들어서 특정 명령어에 반응하는 프로그램을 만들기

1. push X :
정수 X를 스택에 넣음

2. pop :
스택에서 가장 마지막 들어간 정수를 빼고 그 정수를 출력, 스택이 비어있는 경우 -1

3. size :
스택에 들어있는 정수의 개수를 출력

4. empty :
스택이 비어있으면 1, 아니면 0을 출력

5. top :
스택에 가장 최근 들어있는 걸 출력 stack[-1] 없는 경우 -1 출력

'''
import sys
input = sys.stdin.readline


N = int(input())

num = 1
stack = []
while num <= N:
    order = input().strip()
    # print(order)
    if 'push' in order:
        order, n = order.split()
        n = int(n)
        # print(order)
        # print(n)
    if order == 'push':
        stack.append(n)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    num += 1

# print(stack)