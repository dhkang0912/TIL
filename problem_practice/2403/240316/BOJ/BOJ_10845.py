'''
큐 구현하기
'''

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
num = 1
Q = deque()
while num <= N:
    order = input().strip()
    if 'push' in order:
        order, n = order.split()
        n = int(n)
        Q.append(n)
    elif order == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(Q))
    elif order == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)
    num += 1

