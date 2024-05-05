'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
'''
def perm(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        if not visited[i]:
            path[level] = i
            visited[i] = 1
            perm(level+1, i+1)
            visited[i]=0




N, M = map(int, input().split())
path = [-1]*M
visited = [0]*(N+1)
visited[0] = 1
perm(0, 0)
