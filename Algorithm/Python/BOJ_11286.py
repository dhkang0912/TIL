'''
절댓값 힙
배열에 정수를 넣으면 절댓값이 가장 작은 것을 출력하고 배열에서 제거
여러 개인 경우 가장 작은 수를 출력하고 그 값을 배열에서 제거

# 입력
1. N = 연산의 개수
2. N개의 연산에 대한 정보 => 정수 x

# 연산
3. x!=0 => 배열에 x 추가
4. x=0 배열에서 절댓값이 가장 작은 값을 출력 후 제거

# 출력
입력에서 0이 주어진 회수만큼 답을 출력
배열이 비어있는데 출력하라고 한 경우 0 출력
'''

# sys.stdin = open("BOJ_11286_input.txt", "r", encoding="utf-8")

# 연산
# arr = []

# def check(arr):
#     arr.sort(key = lambda x: (x[1],x[0]))
#     return arr.popleft()[0]

# for i in range(N):
#     x = int(input())
#     if x != 0 :
#         arr.append((x, abs(x)))
#     else:
#         if len(arr) == 0:
#             print(0)
#         else:
#             # 최댓값이 가장 작은 수가 출력
#             print(check(arr))

# 시간초과로 인한 heapq의 등장 (우선순위 큐, 자동으로 오름차순 정렬되어 들어감, 최소힙 형태로 내부적으로 정렬됨)
# 튜플을 사용하면 원소별 기준으로 오름차순 정렬을 할 수 있음
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())

heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        print(heappop(heap)[1] if heap else 0)
    else:
        heappush(heap, (abs(x), x))
