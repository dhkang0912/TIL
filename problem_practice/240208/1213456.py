s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))

def dfs(s):
    st = []
    visited = [False] * (N+1) #0은 안 들어가서 뺌

    st.append(s)
    while st :
        v = st.pop()
        if not visited[v] :    # 두 번 들어갈 수 있기 때문에 방문 표시 안 되었을 때
            visited[v] = True
            print(v)

        for w in G[v] :
            if not visited[w] : # 방문 안 한 것만 추가
                st.append(w)

def dfs_b(s):
    st = []
    visited = [False] * (N+1) #0은 안 들어가서 뺌/방문표시할 거 준비

    st.append(s)      #스택 비어있으니까 무조건 start 넣어놓고 시작하기
    visited[s] = True #넣을 때 방문표시해서 무조건 하나만 들어감
    while st :
        v = st.pop()
        print(v)

        for w in G[v] :
            if not visited[w] : # 방문 안 한 것만 추가
                st.append(w)
                visited[w] = True



def dfs_r(v) :
    print(v)
    visited[v] = True

    for w in G[v] :
        if not visited[w] :
            dfs_r(w)


N = 7 #1~7
E = len(l)

G = [[] for _ in range(N+1)]
# s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
for i in range(0, E, 2) : #i가 시작만 표시해줌
    v1 = l[i]
    v2 = l[i+1]
    G[v1].append(v2) #무방향 = 양방향
    G[v2].append(v1)
#print(G)

dfs_b(1)
#defs_r 쓸 때 넣어주기 visited = [False] * (N+1)