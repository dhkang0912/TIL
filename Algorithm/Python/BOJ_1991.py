'''
트리 순회
전위 순회, 중위 순회, 후위 순회한 결과를 출력

# 입력
1. N, 이진 트리 노드 개수 
2. 각 노드의 왼쪽 자식, 오른쪽 자식
- 노드 이름은 A~알파벳, 자식 없으면 .

# 출력
1. 전위 순회
    - 순서 : 루트 -> 왼쪽 -> 오른쪽
    - 루트(가장 상단)를 먼저 방문
2. 중위 순회
    - 순서 : 왼쪽 -> 루트 -> 오른쪽
    - 왼쪽을 모두 탐색한 후 루트 방문, 이후 오른쪽 서브트리 방문
    - 왼쪽을 모두 먼저 탐색하기 위해 가장 왼쪽 하단부터 시작
    - 이진 탐색 트리에서 정렬된 순서를 얻을 때 사용
3. 후위 순회
    - 순서 : 왼쪽 -> 오른쪽 -> 루트
    - 모든 하위 노드를 방문한 후 루트 방문
    - 자식을 모두 방문하기 위해 가장 왼쪽 하단부터 시작
    - 부모를 가장 나중에 방문하여 구조적 삭제 작업에 적합 (파일 시스템, 디렉토리 삭제)
'''

N = int(input())
tree = {}

for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left,right)

# print(tree)

# 전위 순회 => 루트 -> 왼쪽, 오른쪽
def preorder(node):
    if node == '.' : # 자식이 없는 경우면 빠져나오기
        return
    print(node, end="")
    preorder(tree[node][0]) # 왼쪽 자식
    preorder(tree[node][1]) # 오른쪽 자식

# 중위 순회
def inorder(node):
    if node == '.' : # 자식이 없는 경우면 빠져나오기
        return
    inorder(tree[node][0]) # 왼쪽 자식
    print(node, end="")
    inorder(tree[node][1]) # 오른쪽 자식

# 후위 순회
def postorder(node):
    if node == '.' : # 자식이 없는 경우면 빠져나오기
        return
    postorder(tree[node][0]) # 왼쪽 자식
    postorder(tree[node][1]) # 오른쪽 자식
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()