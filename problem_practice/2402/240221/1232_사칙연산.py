import sys
sys.stdin = open("1232_input.txt", "r")

def calc(v1, v2, operator):
    v1 = float(v1)
    v2 = float(v2)
    if operator == '+':
        return v1 + v2
    elif operator == '-':
        return v1 - v2
    elif operator == '*':
        return v1 * v2
    else:
        return v1 // v2


def postorder(root):
<<<<<<< HEAD
    if Tree[root][0] in ['+', '-', '*', '/']:
        v1 = postorder(int(Tree[root][1]))
        v2 = postorder(int(Tree[root][2]))
        return calc(v1, v2, Tree[root][0])

    else:
        return Tree[root][0]
=======
    if Tree[root] in ['+', '-', '*', '/']:
        v1 = postorder(Tree[root][1])
        v2 = postorder(Tree[root][2])
        return calc(v1, v2, Tree[root][0])
>>>>>>> e0ce9d7716a9ccf424064ddd9caa94727d8e78b3




T = 10
for tc in range(1, T+1):
    N = int(input())
    Tree = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = input().split()
        no = int(lst[0])
        Tree[no] = lst[1:] # Tree[no] -> Tree[no][0] = no 부모의 값, Tree[no][1] = 왼자 인덱스, Tree[no][2] = 우자 인덱스
    print(Tree)

<<<<<<< HEAD
    print(f'#{tc} {int(postorder(1))}')
=======
    print(postorder(1))
>>>>>>> e0ce9d7716a9ccf424064ddd9caa94727d8e78b3
