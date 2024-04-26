def perm(level, start):
    if level == M:
        print(*path)

    for i in range(start, N):
        path.append(lst[i])
        perm(level+1, i+1)
        path.pop()

N ,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []

perm(0, 0)