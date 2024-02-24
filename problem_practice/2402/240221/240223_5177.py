# 이진 최소힙 만들기
import sys
sys.stdin = open("5177_input.txt", "r")

# enqueue 함수 만들기
def enqueue(num):
    global last_index
    last_index += 1
    Tree[last_index] = num
    # 1. 부모노드의 값을 가져옴
    p = last_index//2
    c = last_index
    while Tree[p] > Tree[c] and c > 1:
    # 2. 부모노드와 자식노드의 값을 비교
        Tree[p], Tree[c] = Tree[c], Tree[p]
        c = p
        p = c//2
    # 3. 만약 자식노드가 크면 값을 바꿈
    # 4. 자식노드가 부모노드보다 크지 않을 때까지 바꿈
    # 5. 노드 인덱스가 1일때까지만 비교



# 인풋 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Tree = [0] * (N+1)
    last_index = 0
    result = 0

    for num in lst:
        enqueue(num)

    while last_index > 1:
        result += Tree[last_index//2]
        last_index //= 2


    print(f'#{tc}', result)