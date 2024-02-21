import sys
sys.stdin = open("5176_input.txt", "r")

'''
1~N까지 자연수를 이진 탐색 트리에 저장
왼쪽 서브 트리의 루트 -> 현재 노드 -> 오른쪽 서브 트리의 루트
=> inorder

첫번째 노드 번호는 1번
왼쪽에서 오른쪽으로 증가

N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값 (1번 값)
N//2번 노드에 저장된 값을 출력

'''

# 쌤 코드
# def inOrder(root):
#     global value
#     if root <= N:
#         inOrder(root*2)
#         TREE[root] = value
#         value += 1
#         # print(root)
#         inOrder(root*2+1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     TREE = [0] * (N+1)
#     value = 1
#     inOrder(1)
#     print(TREE[1], TREE[N//2])

# 내 코드
def inorder(root):
    global value
    if root <= N:
        inorder(root*2)
        Tree[root] = value
        value += 1
        inorder(root*2+1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Tree = [0] * (N+1)
    value = 1
    inorder(1)
    print(f'#{tc}', Tree[1], Tree[N//2])



