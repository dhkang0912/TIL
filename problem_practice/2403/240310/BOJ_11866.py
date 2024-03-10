# 내가 푼 풀이
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K -= 1
lst = [i for i in range(1, N+1)]
# print(lst)

stack = []
stack.append(lst.pop(K))
idx = K

while len(stack) < N:
    idx += K
    if idx > len(lst) - 1:
        while True:
            idx -= len(lst)
            if idx <= len(lst)-1:
                break
    stack.append(lst.pop(idx))
print('<', end='')
for i in range(len(stack)):
    if i < len(stack)-1:
        print(stack[i], end =', ')
    else:
        print(stack[i], end='')
print('>')


from collections import deque

n, k = map(int, input().split())

# 찾아본 풀이  (진짜 나랑 개념은 비슷하지만 어떻게 이렇게 생각할 수 있지 싶었다 충격, 좋은 방법이다)
# https://yoondii.tistory.com/127
ysps = []  # 뽑은 수 넣을 요세푸스리스트
queue = deque()

for i in range(1, n + 1):
    queue.append(i)
# print(queue)[1, 2, 3, 4, 5, 6, 7]

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())#큐에서 k번째 수를 빼고
    ysps.append(queue.popleft()) #뺀 수를 새로운 리스트에 넣어준다.

print("<", end="")
print(", ".join(map(str, ysps)), end="")
print(">")
