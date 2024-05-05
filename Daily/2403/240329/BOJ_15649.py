# N = 내가 뽑을 수 있는 카드 수(목록), M = 카드를 뽑을 갯수 = level
def perm (level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        if not visited[i]:
            path[level] = i
            visited[i] = 1
            perm(level+1)
            visited[i] = 0



N, M = map(int, input().split())
path = [-1] * (M)
visited = [0] * (N+1)
visited[0] = 1
perm(0) # 0레벨 부터 시작
