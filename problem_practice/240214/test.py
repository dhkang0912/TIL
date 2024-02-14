def perm(k):
    if k == N:
        print(check)
        for i in range(N):
            index = check[i]
            print(numbers[index], end='')
        print()
        return

    for i in range(N):
        if not visited[i]:
            check[k] = i
            visited[i] = True
            perm(k + 1)
            visited[i] = False


N = 3
numbers = [10, 30, 20]
check = [-1] * N
visited = [False] * N
perm(0)