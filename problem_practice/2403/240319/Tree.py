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
    while TREE[pos] != -1:
        if TREE[pos] > value:
            pos *= 2
        else:pos = pos*2+1
    TREE[pos] = value
            

def inOrder(rootP):
    if len(TREE[rootP*2]) != -1:
        inOrder(rootP*2)
    print(TREE[rootP])
    if len(TREE[rootP*2+1]) != -1:
        inOrder(rootP*2+1)

# 이런 방식으로도 가능
def inOrder(rootP):
    if TREE[rootP] != -1:
        inOrder(rootP*2)
        print(TREE[rootP])
        inOrder(rootP*2+1)

# key가 트리에 있으면 저장
def find(key):
    pos = 1
    while TREE[pos] != -1:
        if TREE[pos] == key:
            return pos
        if TREE[pos] < key:
            pos = pos*2+1
        else:
            pos *= 2



TREE = [-1] * 100
insert(9)
insert(12)
insert(15)
insert(4)
print(TREE)
inOrder(1)

# 최대 힙, 넣을 때는 아래부터 정비
def insert(value):
    global last

    last += 1
    TREE[last] = value

    c = last
    p = c//2

    while p >= 1 and  TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c//2

# 뺄 때는 위에부터 정비
def pop():
    global last
    t = TREE[1]
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p * 2
    while TREE[c] <= last:
        if c+1 <=last and TREE[c] < TREE[c+1]:
            c += 1
        if TREE[p] < TREE[c]:
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p * 2
        else:
            break

    return t

    

TREE = [0, 20, 15, 19, 4, 13, 11] + [-1]*100
last = 6 # 마지막으로 들어있는 인덱스 위치
insert(17)
insert(23)
print(pop())
