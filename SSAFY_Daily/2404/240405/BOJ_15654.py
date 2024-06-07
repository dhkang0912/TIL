'''
4 2
9 8 7 1

오름차순으로 정렬 후 중복 없이 순열 구하기
'''
def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if not visited[i]:
            path.append(lst[i])
            visited[i] = 1
            perm(level+1)
            path.pop()
            visited[i] = 0



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
visited = [0]*N

perm(0)