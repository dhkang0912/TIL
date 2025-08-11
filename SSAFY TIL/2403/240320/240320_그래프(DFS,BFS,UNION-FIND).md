## 그래프
### 1. 그래프 기본
- 노드 + 간선으로 이루어진 자료 구조 (데이터 간 관계를 표시하기 위해)
### 2. DFS
### 3. BFS
### 4. Union-Find (Disjoint set)

## 그래프
### 그래프
- 그래프는 아이템들과 이들 사이의 연결 관계를 표현
- 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료 구조
- 선형 자료 구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이
    - 실생활의 얽힌 데이터를 표현하기 좋음
    
### 그래프 유형
- 무향 그래프 (Undirected Graph) = 양방향
- 유향 그래프 (Directed Graph)
- ***<u>가중치 그래프 (Weighted Graph)</u>***
    - 다익스트라
    - 여행 경로
    - 톨비
- 사이클이 없는 방향 그래프 (DAG, Directed Acyclic Graph)

### 인접 정점
- 인접 (Adjacency)
    - 두 개의 정점에 ***간선이 존재(연결됨)하면 서로 인접해 있다고 함***
    - 완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있음
    
### 그래프 경로
- 경로 : 간선들을 순서대로 나열한 것
- 단순 경로 : 경로 중 한 정점을 최대한 한번만 지나는 경로
- 사이클 : 시작한 정점에서 끝나는 경로

### 그래프 표현
- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정
- 인접 행렬 (Adjacent matrix)
    - |V| * |V| 크기의 2차원 배열을 이용해서 간선 정보를 저장
    - 배열의 배열 (포인터 배열)
    
- 인접 리스트 (Adjacent list)
    - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
    
- 간선의 배열 
    - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

### 그래프를 코드로 표현
1. 인접 행렬
    - V*V 크기의 2차원 배열을 이용해서 간선 정보를 저장
    - 갈 수 없다면 0, 있다면 1(가중치)를 저장
    - 장점 
        - 노드 간의 연결 정보를 한 방에 확인 가능
        - 행렬 곱을 이용해서 탐색이 쉽게 가능
        - 간선이 많을수록 유리
    - 단점
        - 노드 수가 커지면 메모리가 낭비됨 (연결이 안 된 것도 저장)
        -> 노드 수 + 메모리 제한 반드시 확인할 것!

- DFS        
```python
# 양방향 그래프는 중앙 우하단 대각선 기준 대칭
graph = [
    # 0번은 1과 3으로 갈 수 있음
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1], 
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!
    
    # 다음 재귀 호출 전
    # visited[now] = 1
    # print(now, end=' ')
    
    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인
    # 다른 노드들 == 반복문
    for to in range(5):
        # 갈 수 없다면 pass
        if graph[now][to] == 0:
            continue
        
        # 이미 방문 했다면 pass
        if visited[to]:
            continue
            
        # 다음에 갈 때 visited를 하면 출발점 작업을 해야함
        visited[to] = 1
        path.append(to)
        dfs(to)
    
    # 돌아왔을 때 작업

visited[0] = 1
path. append(0)
dfs(0)
print(path)

```
- BFS (Queue 사용)       
```python
# 양방향 그래프는 중앙 우하단 대각선 기준 대칭
graph = [
    # 0번은 1과 3으로 갈 수 있음
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1], 
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

visited = [0] * 5
path = []

def bfs(start):    
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1
    
    while queue:
        now = queue.pop(0)
        print(now, end = ' ')
    
    # 갈 수 있는 곳 체크
    for to in range(5):
        if graph[now][to] == 0:
            continue
        if visited[to]:
            continue
        
        visited[to] = 1
        print(visited)
        queue.append(to)

bfs(0)

```
2. 인접 리스트 (조금 더 권장)
    - V개의 노드가 갈 수 있는 정보만 저장
    - 장점
        - 메모리 사용량이 적다
        - 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율
    - 단점
        - 특정 노드 간 연결 여부를 확인하는데 시간이 걸림
    
```python
graph = [
    # 0번은 1과 3으로 갈 수 있음
    [1, 3],
    [0, 2, 4], 
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!
    
    # 다음 재귀 호출 전
    # visited[now] = 1
    # print(now, end=' ')
    
    # 다음 재귀 호출
    # 인접 리스트
    # 차이점 1. 갈 수 없는 곳 조건 필요없음
    # 차이점 2. for 문 작성 수정
    for to in graph[now]:     
        # 이미 방문 했다면 pass
        if visited[to]:
            continue
            
        # 다음에 갈 때 visited를 하면 출발점 작업을 해야함
        visited[to] = 1
        path.append(to)
        dfs(to)
    
    # 돌아왔을 때 작업

visited[0] = 1
path. append(0)
dfs(0)
print(path)
```
- BFS (Queue 사용)       
```python
# 양방향 그래프는 중앙 우하단 대각선 기준 대칭
graph = [
    # 0번은 1과 3으로 갈 수 있음
    [1, 3],
    [0, 2, 4], 
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * 5
path = []

def bfs(start):    
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1
    
    while queue:
        now = queue.pop(0)
        print(now, end = ' ')
    
    # 갈 수 있는 곳 체크
    for to in graph[now]:
        if visited[to]:
            continue
        
        visited[to] = 1
        print(visited)
        queue.append(to)

bfs(0)

```

## 서로소 집합 (Disjoint-sets)
- 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들임, 교집합이 없음
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분함, 이를 대표자라고 함
- 대표자를 통해 어디에 속해있는지 소속을 확인하는 것

### 상호 배타 집합을 표현하는 방법
(데이터가 같은 집합에 속해있는 것 -> 관계가 있음, 그래프의 일종)
1. 연결 리스트
2. 트리 (cycle이 없는 무향 연결 그래프)

- 상호배타 집합 연산
    - Make-set(x) : 집합 만들기 (처음엔 자기자신이 대표)
    - Find-set(x) : 너네 대표 누구야?
    - Union(x, y) : 같은 집합으로 묶자 
      => 대표자를 뽑는 건 조건에 따라서 함, 다만 y가 속해져있는 것의 대표는 x야라고 해주는 것
      
### 상호 배타 집합 표현 - 연결리스트
- 같은 집합의 원소들은 하나의 연결리스트로 관리함
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼음
- 각 원소는 집합의 대표원소를 가르키는 링크를 갖음

### 상호 배타 집합 표현 - 트리
- 하나의 집합(a disjoint set)을 하나의 트리로 표현
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 됨

```python
# 1~6까지 노드 존재
# 1. make_set
def make_set(n):
    # 자기 자신이 대표인 데이터 6개가 리스트로 생성
    # [0, 1, 2, 3, 4, 5, 6] => 숫자는 무슨의미?? 
        # -> 대표자 인덱스, 아직 합치지 않아서 자기 자신을 대표자로 가진 여러가지 노드가 나옴
    return [i for i in range(n)]
    
# 2. find_set : 대표자를 찾아보자
# - 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# - 언제까지 ? 자기 자신이 대표인 데이터를 찾을 때까지 (연결이 없을 때까지)

# 1~6번까지를 사용하기 위해 7개 생성, 0번은 버림
parents = make_set(7)

def find_set(x): # cycle을 체크하는데 사용됨
    # 자기 자신이 대표네? 끝
    if parents[x] == x:
        return x
    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다
    # 부모의 노드를 통해서 연결된 대표자를 찾아가는 것
    return find_set(parents[x])
    
    
# 3. union 
def union(x, y): # 두개를 합쳐라
    x = find_set(x)
    y = find_set(y)
    
    #이미 같은 집합에 속해있다면 continue
    if x== y:
        return
    
    # 다른 집합이라면 합침
    # 예) 더 작은 루트 노드에 합쳐라~
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

union(1, 3)
union(2, 3)
    
```

### 상호 배타 집합에 대한 연산
- 연산의 효율을 높이는 방법
    - Rank를 이용한 Union
        - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크라는 이름으로 저장
        - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다
    - Path compression
        - Find-set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어줌
    

## 오프라인 강사님 설명
- 상호 배타 집합 표현 (자료 구조의 일종)
```python
def make_set(data):
    idx = datas.index(data)
    p[idx] = idx
    # print(p)
    
# data가 포함된 set의 대표의 index를 return
def find_set(data):
    idx = datas.index(data)
    while idx != p[idx]:
        idx = p[idx]
    return idx

def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    if idx1 < idx2:
        p[idx2] = p[idx1]
    else:
        p[idx1] = idx2
    

datas = ['a', 'b', 'c', 'd', 'e', 'f']
p = [-1] * len(datas) # 각 인덱스 별로 나랑 연결된 대표를 확인하는 리스트

for d in datas:
    make_set(d)

union('c', 'd')
print(p)
union('e', 'f')
print(p)
union('d', 'f')
print(p)
print(find_set('d'))
print(find_set('e'))
print(find_set('f'))
```

```python
def make_set(data):
    idx = datas.index(data)
    p[idx] = idx
    # print(p)
    
# data가 포함된 set의 대표의 index를 return
def find_set(data):
    idx = datas.index(data)
    while idx != p[idx]:
        idx = p[idx]
    return idx

def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        p[idx2] = p[idx1]
    else:
        p[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1

def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    link(idx1, idx2)
    
    

datas = ['a', 'b', 'c', 'd', 'e', 'f']
p = [-1] * len(datas)
rank = [-1] * len(datas)

for d in datas:
    make_set(d)

union('c', 'd')
print(p)
union('e', 'f')
print(p)
union('d', 'f')
print(p)
print(find_set('d'))
print(find_set('e'))
print(find_set('f'))
```
- 쌤이 올려주신 것
```python
def make_set(data):
    idx = datas.index(data)
    p[idx] = idx
    rank[idx] = 0

# data가 포함된 셋의 대표의 index를 return
def find_set(data):
    idx = datas.index(data)
    while idx != p[idx]:
        idx = p[idx]
    return idx

def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        p[idx1] = idx2
    else:
        p[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1

def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    link(idx1, idx2)

def union_old(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    if idx1 < idx2:
        p[idx2] = idx1
    else:
        p[idx1] = idx2

datas = ['a', 'b', 'c', 'd', 'e', 'f']
p = [-1] * len(datas)
rank = [0] * len(datas)

for d in datas:
    make_set(d)

union('c', 'd')
print(p)
union('e', 'f')
print(p)
union('d', 'f')
print(p)
print(find_set('d'))
print(find_set('e'))
print(find_set('f'))
```