import sys
sys.stdin = open("5174_input.txt", "r")

def preorder(root):
    global cnt
    cnt += 1
    if len(Tree[root]) >= 1:
        preorder(Tree[root][0])
    if len(Tree[root]) >= 2:
        preorder(Tree[root][1])
    # return cnt



T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E = 간선의 개수, N은 시작 노드
    lst = list(map(int, input().split()))
    Tree = [[] for _ in range(E+2)]
    cnt = 0
    for i in range(0, len(lst), 2):
        Tree[lst[i]].append(lst[i+1])

    # print(Tree)
    preorder(N)
    print(f'#{tc}', cnt)