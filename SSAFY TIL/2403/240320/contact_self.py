import sys
sys.stdin = open("contact_input.txt", "r")

'''
출력은 마지막 전달 받은 사람 중 가장 노드 번호가 끝 사람
'''

def bfs(s):
    global maxC
    global resV
    Q = [(s, 0)]
    visited[s] = 1

    while Q:
        v, cnt = Q.pop(0)
        if maxC < cnt:
            maxC = cnt
            resV = v
        elif maxC == cnt:
            resV = max(resV, v)
        for w in G[v]:
            if not visited[w]:
                Q.append((w, cnt+1))
                visited[w] = visited[v] + 1
                # if maxC < visited[w]:
                #     maxC = visited[w]
                # elif maxC == visited[w]:
                #     resV = max(resV, w)





T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 데이터의 길이, M = 시작
    contact = list(map(int, input().split()))
    visited = [0] * 101

    G = [set() for _ in range(101)] # 0번 노드 사용 안함
    for i in range(0, N, 2):
        v1 = contact[i]
        v2 = contact[i+1]
        G[v1].add(v2)

    maxC = 0
    resV = 0
    bfs(M) # 시작값 입력
    print(f'#{tc} {resV}')