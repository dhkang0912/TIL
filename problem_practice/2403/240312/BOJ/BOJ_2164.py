import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
lst = deque([i for i in range(1, N+1)])
# print(lst)
while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())

print(*lst)