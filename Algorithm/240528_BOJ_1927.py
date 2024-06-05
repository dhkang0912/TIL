'''
최소힙
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
3. 비어있는 배열에서 시작한다.

#입력
첫째 줄에 연산의 개수가 주어짐
N줄에는 연산에 대한 정보가 주어짐
x가 자연수라면 배열에 x라는 값을 추가하고 (삽입),
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에 제거(루트 출력 후 삭제)
'''

# 힙큐를 구현하는 방법을 고민했는데 대부분 모듈을 사용해서 하네
import sys
import heapq
input = sys.stdin.readline

# 우선순위 큐, 최소힙
min_heap = []
# 첫줄에 주어진 연산의 개수만큼 for문 돌리기
for _ in range(int(input())):
    # 주어진 연산을 할당받고 판단함
    n = int(input())
    if n != 0:
        # min_heap(우선순위 큐)에 n을 삽입한다.
        heapq.heappush(min_heap, n)
    else : # n=0인 경우
        if len(min_heap) == 0:
            print(0)
        else:
            # heapq에서 heappop의 경우 반환 값이 존재한다. 가장 작은 값을 삭제하고 이를 반환한다.
            print(heapq.heappop(min_heap))


