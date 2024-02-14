# stack = (LIFO)
st = list()
st.append(3)
st.append(5)
st.append(6)
st.append(7)
st.append(8)
print(st)
st.pop() # 8이 빠지고
a = st.pop() # 7이 빠지고 a에 7이 할당
print(st) # 8,7을 뺀 나머지

while st: # st가 비어지면 멈춘다.
    a = st.pop()
    print(a)
print(st)


#######################################################################
'''  앞에서부터 뺀다면?  '''
queue = list()
queue.append(3)
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)
queue.append(9)
print(queue)
# 0번 인덱스를 빼겠다!
queue.pop(0) # 시간 복잡도가 O(1) / O(n) : 앞이나 중간을 뺄 때는 시간복잡도 증가
queue.pop(0)
print(queue)
#######################################################################
'''  collections 사용하기  '''
from collections import deque
q = deque()
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
print(q)  # 출력값 : deque([5, 6, 7, 8, 9])
print(*q) # 출력값 : 5 6 7 8 9
print([*q]) # 출력값 : [5, 6, 7, 8, 9] 이런식으로 list 형태로도 출력 가능

q.popleft() # 왼쪽의 값이 빠진다 (5)
q.popleft() # 왼쪽의 값이 빠진다 (6)
print(*q) # 출력값 : 7 8 9
#######################################################################
'''   DFS 와 BFS   '''
# BFS : 너비우선탐색 / 지금 현재 위치에서 갈 수 있는 곳을 queue에 적기!
from collections import deque

name = list(input().split()) # A B C D E F
arr = [
    [0,1,1,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]

answer = []
def bfs(st):
    global answer
    q = deque()
    q.append(st) # 시작점을 q에 넣어주고 시작!

    while q:
        now = q.popleft()
        answer.append(name[now])
        # print(name[now], end = ' ') 만약에 순서를 그때그때마다 출력하고싶다면 이렇게!!!
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

bfs(0)  # bfs 시작인덱스 넣어주기
print(*answer)

''' 내가 다시 풀어보기!! '''
# from collections import deque
#
# # name과 arr가 정의됨, 크기는 n이라 할 때
#
# answer = []
#
# def dfs(now): # 이 함수를 계속 돌리는게 아니다!
#     global answer
#     q = deque()
#     q.append(now) # 루트노드에서 시작!
#
#     while q: # q가 다 비워지면 끝낸다.
#         now = q.leftpop()
#         for i in range(6):
#             if arr[now][i] == 1:
#                 q.append(i)

##############################################################################################################################################
'''   한번씩만 탐색하기      '''
from collections import deque
''' 내가 작성해본 코드 
arr = [
    [0,1,1,0],
    [0,0,0,1],
    [0,1,0,1],
    [0,0,0,0]]

used = [0]*4

q = deque()
now = 0
q.append(now)
used[0] = 1 #넣고 시작했으니까 A 사용했다는 표시 남기기!!

while q: # q가 다 비워질때까지(empty deque) 반복하기
    now = q.popleft()
    answer.append(name[now]) # name에 이름을 넣고 싶다면!
    for i in range(4):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            q.append(i)
'''
# 강사님이 작성하신 코드
arr = [
    [0,1,1,0],
    [0,0,0,1],
    [0,1,0,1],
    [0,0,0,0]]

used = [0]*4
answer = []
'''
리스트 할당 안에마다 새로운 주소값을 가지는 느낌??
append는 괜찮은데 형태를 바꾸는 건 안된다!
'''

name = ['A','B','C','D']
def bfs(start):
    q = deque() # 기록할 q 만들기
    q.append(start) # 시작 인덱스를 queue에 넣고 시작

    while q: # q가 다 비워질 때 까지
        now = q.popleft()
        answer.append(name[now]) # 방문 순서를 answer에 저장한다.

        for i in range(4): # 갈 수 있는곳 탐색
            if arr[now][i] == 1 and used[i] == 0: # 갈 수 있고 탐색한 적이 없다면
                used[i] = 1 # 방문 체크하고
                q.append(i) # 넣어놓기
#  => 다음에는 넣어놓은 것들 하나하나 들어가기

used[0] = 1 #안에 넣는 순간 들어가기 때문에!
bfs(0) # 0에서부터 시작!
print(*answer)

##############################################################################################################################################
'''  경로의 개수 및 최소비용 등의 활용 문제   '''
''' used를 bfs 안에 넣어야한다 / 매개변수로 받아서 들어가기 / 그래야 A - B - C와 A - C - B가 구분된다.'''
from collections import deque
arr = [
    [0,1,1,0],
    [0,0,1,1],
    [0,1,0,1],
    [0,0,0,0]]

# 단방향인지 양방향인지 알 수 없다면, 양방향으로 가정하고 used 나 visited를 사용하기!!
# 경로를 탐색하기
# 깊은 복사를 위해서 copy 모듈 설치
import copy

cnt = 0
def bfs(st): # st : start
    global cnt
    q = deque()
    used = [0]*4
    used[st] = 1
    q.append((st,used)) # 묶인 형태는 중요X
    while q: # q가 빌때까지 진행
        now = q.popleft() # 지점과 지나간 점들을 다 담고 있다.
        if now[0] == 3: # D(=3)에 도착한다면
            cnt += 1 # 경로의 수 1씩 증가!
        for i in range(4):
            if arr[now[0]][i] == 1 and now[1][i] == 0:
                used = copy.deepcopy(now[1])
                used[i] = 1 # 가는 방향마다 used 리스트가 바뀌기 때문에 다시 돌려줄 필요 X
                q.append((i,used))
bfs(0)
print(cnt)
####################################################################################################
'''

dfs : 그래프탐색, 완전탐색 - brute force, backtracking

bfs = 그래프탐색, 완전탐색, flood fill

'''
from collections import deque
n = int(input()) # 배열 사이즈 입력
arr = [[0]*n for _ in range(n)]
y, x = map(int,input().split()) # 시작좌표 입력
arr[y][x] = 1 # 시작점에 1표시
q = deque()
q.append([y,x]) # 시작점을 넣고 들어간다.

while q:
    now = q.popleft() # while에서 하나를 빼고 시작하기 때문에 미리 하나를 넣어두어야한다. = 시작점
    y, x = now
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for i in range(4): # 상하좌우로 꽃 체크!
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
        if arr[dy][dx] != 0: continue # 0인곳에만 새로운 값이 처리가 된다. 안그러면 순서에 맞지않게 값이 바뀐다.
        arr[dy][dx] = arr[y][x] + 1 # 여기에서 값이 처리가 된다! 중심을 잡은 곳에서 퍼지기 때문에!
        answer = arr[ny][nx]
        q.append([dy][dx])

for lst in arr:
    print(*arr)
# 지금 내 현재 시작지점 적어두고, 지나간다는거 체크해주기



##################################################################################
# N 입력받은 후 N x N 사이즈의 맵에 바이러스를 투입해 보자고 합니다.
# 바이러스를 최초로 투입 할 좌표를 입력 받습니다.
# 0,1 좌표에는 몇일날 바이러스가 도착 할까요?
''' 내가 작성한 코드 '''
from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
q = deque()
y, x = map(int, input().split())
q.append((y, x))
arr[y][x] = 1  # 시작지점에 1 표시하기

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while q:
    now = q.popleft()
    y, x = now
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= n or nx >= n or ny < 0 or nx < 0: continue
        if arr[ny][nx] != 0: continue
        arr[ny][nx] = arr[y][x] + 1
    if arr[0][1] != 0:
        print(arr[0][1])
        break
    q.append((ny, nx))  # 넣어주는거 까먹지 말기!!

''' 강사님이 작성한 코드'''
n = int(input())
arr = [[0] * n for _ in range(n)]
y, x = map(int, input().split())

q = deque()
q.append((y, x, 1))  # level을 추가하기
arr[y][x] = 1
ans = 0
while q:
    nowy, nowx, level = q.popleft()
    directy = [-1, 1, 0, 0]
    directx = [0, 0, 1, -1]

    for i in range(4):
        dy = nowy + directy[i]
        dx = nowx + directx[i]
        # 이쪽에 조건을 넣었을 때는 [level]
        if nowx == 0 and nowy == 1:  # 찾고자했던 좌표
            ans = level
        if dy < 0 or dx < 0 or dy >= n or dx >= n: continue
        if arr[dy][dx] != 0: continue
        arr[dy][dx] = arr[nowy][nowx] + 1
        q.append((dy, dx, level + 1))
        # 이쪽에 조건을 넣었을 때는 [level + 1]
        if nowx == 0 and nowy == 1:  # 찾고자했던 좌표
            ans = level + 1

#############################################################################
'''   바이러슨를 두 곳에서 받을 때    '''
from collections import deque
n = int(input())
arr = [[0]*n for _ in range(n)]
# 시작점 두 곳을 받는다.
a,b,c,d = map(int,input().split())
q = deque()
q.append((a,b))
q.append((c,d))
arr[a][b] = 1
arr[c][d] = 1

dy = [1,-1,0,0]
dx = [0,0,-1,1]

while q: # level을 넣어서 풀어도 된다! => 이 풀이는 밑에 작성하기
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >=n or nx >=n or ny < 0 or nx < 0: continue
        if arr[ny][nx] != 0: continue
        arr[ny][nx] = arr[y][x] + 1
        q.append((ny,nx))
    if arr[0][0] != 0:
        print(arr[0][0])
        break


''' 강사님이 추천하신 코드 '''
## 3일차일 때
from collections import deque
n = int(input())
arr = [[0]*n for _ in range(n)]
# 시작점 두 곳을 받는다.
a,b,c,d = map(int,input().split())
q = deque()
start = [(a,b,1),(c,d,1)]
arr[a][b] = 1
arr[c][d] = 1

dy = [1,-1,0,0]
dx = [0,0,-1,1]
def bfs(virus):
    q = deque(virus)
    while q: # level을 넣어서 풀어도 된다! => 이 풀이는 밑에 작성하기
        y, x, level = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >=n or nx >=n or ny < 0 or nx < 0: continue
            if arr[ny][nx] != 0: continue
            arr[ny][nx] = arr[y][x] + 1
            q.append((ny,nx,level+1))
            if ny == 0 and nx == 0:
                print(level+1) # level이 1일 때 2가 채워지고, level이 2일 때 3이 채워지고 ~~
                break
bfs(start)





