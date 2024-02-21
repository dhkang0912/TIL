# 5177_이진힙
'''
이진 최소힙
- 마지막 노드 뒤에 새 노드 추가
- 부모 노드의 값 < 자식 노드의 값
- 루트가 1번, 왼쪽, 오른쪽
- N개의 자연수가 주어짐
=> 이진 최소힙에 저장, 조상노드에 저장된 정수의 합
'''

# def postorder(root):
#     global value
#
#     if root <= N and TREE[root] :
#         postorder(root//2)
#         value += TREE[root]

def add(n) :
    global last
    last += 1

    TREE[last] = n
    c = last
    p = last//2

    while p :
        if TREE[p] > TREE[c] :
            TREE[p], TREE[c] = TREE[c], TREE[p]
            c = p
            p = c//2
        else :
            break




T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    numlst = list(map(int, input().split()))
    TREE = [0]*(N+1)
    last = 0
    value = 0
    for num in numlst :
        add(num)
    # print(TREE)
    # postorder(N//2)
    i = N
    while i > 1 :
        value += TREE[i//2]
        i = i//2
    print(f'#{tc} {value}')
