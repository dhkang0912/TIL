# 이진 트리
# root로 시작하는 tree를 left-right-root 순으로 출력
def postOrder(root):
    if len(TREE[root]):
        postOrder(TREE[root][0])
    if len(TREE[root])>1:
        postOrder(TREE[root][1])
    print(root)

# root로 시작하는 tree를 root-left-right순으로 출력
def preOrder(root):
    print(root)
    if len(TREE[root]):
        preOrder(TREE[root][0])
    if len(TREE[root])>1:
        preOrder(TREE[root][1])

s = '1 2 1 3 12 4 3 5 3 6 4 7 5 8 5  6 10 6 11 7 12 11 13'
l = list(map(int, s.split()))
N = 13
TREE = [[] for _ in range(N+1)]
for i in range(0, len(l), 2):
    p = l[i]
    c = l[i+1]
    TREE[p].append(c) # 단방향 트리
print(TREE)

preOrder(1)

# 이진 탐색 트리
def insert(value):
    pos = 1
    while True:
        if TREE[pos] == -1:
            TREE[pos] = value
            break
        if TREE[pos] > value:
            pos *= 2
        else:pos = pos*2+1

def inOrder(rootP):
    if len(TREE[rootP*2]) != -1:
        inOrder(rootP*2)
    print(TREE[rootP])
    if len(TREE[rootP*2+1]) != -1:
        inOrder(rootP*2+1)

TREE = [-1] * 100
insert(9)
insert(12)
insert(15)
insert(4)
print(TREE)