#5178_노드의 합
# 리프노드 : 자식을 갖지 않는 노드
# 재귀 postorder
# import sys
# sys.stdin = open("5178_input.txt", "r")

# def postorder(root):
#     if root*2 <= N:
#         Tree[root] += postorder(root*2)
#     if root*2+1 <= N
#         Tree[root] += postorder(root*2+1)
#     return Tree[root]


def postorder(root):
    if root <= N and Tree[root]:
        return Tree[root]

    v = 0
    if root*2 <= N:
        v = postorder(root*2)
    if root*2+1 <= N:
        v += postorder(root*2+1)
    Tree[root] = v
    return Tree[root]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    Tree = [0] * (N+1)
    for _ in range(M):
        no, value = map(int, input().split())
        Tree[no] = value

    postorder(1)
    print(f'#{tc} {Tree[L]}')