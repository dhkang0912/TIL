# 1231. [S/W 문제해결 기본] 9일차 - 중위순회
# 가로 프린트 방식, 완전이진트리이기 때문에 자식노드를 받지 않더라도 인덱스로 계산 가능

def in_order(T, N):
    if T<=N:        # 완전이진트리에서 실존하는 노드면
        in_order(T*2, N)      # 왼쪽 자식먼저
        print(tree[T], end='')  # 부모(T)처리
        in_order(T*2+1, N)      # 오른쪽 자식 방문

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)        # N번 노드까지 저장할 완전이진트리

    for _ in range(N):
        node = list(input().split())    # int(node[0]) 노드번호, node[1] 저장할 글자, 자식번호
        tree[int(node[0])] = node[1]    # 완전이진트리라 자식번호는 필요없음(계산으로 알 수 있음)

    print(f'#{tc}', end = ' ')
    in_order(1, N)
    print()


# 문자열에 삽입하여 프린트 방식, 완전이진트리이기 때문에 자식노드를 받지 않더라도 인덱스로 계산 가능
def in_order(T, N):
    global ans
    if T<=N:        # 완전이진트리에서 실존하는 노드면
        in_order(T*2, N)      # 왼쪽 자식먼저
        #print(tree[T], end='')  # 부모(T)처리
        ans += tree[T]
        in_order(T*2+1, N)      # 오른쪽 자식 방문

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)        # N번 노드까지 저장할 완전이진트리

    for _ in range(N):
        node = list(input().split())    # int(node[0]) 노드번호, node[1] 저장할 글자, 자식번호
        tree[int(node[0])] = node[1]    # 완전이진트리라 자식번호는 필요없음(계산으로 알 수 있음)

    #print(f'#{tc}', end = ' ')
    ans = ''
    in_order(1, N)
    #print()
    print(f'#{tc} {ans}')


# 완전이진트리가 아닌경우

def in_order(T):
    if T:
        in_order(left[T])
        print(tree[T], end='')
        in_order(right[T])

T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0]*(N+1)
    right = [0]*(N+1)

    tree = [0]*(N+1)        # N번 노드까지 글자 저장

    for _ in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]    # 글자 저장
        if len(node)==4:        # 자식이 두개인 경우
            right[int(node[0])] = int(node[3])
        if len(node)>=3:
            left[int(node[0])] = int(node[2])
    print(f'#{tc}', end = ' ')
    in_order(1)
    print()