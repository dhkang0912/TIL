'''
N, M이 주어짐
중복 가능 visited 없음
고른 수열이 비내림차순, 오름차순이거나 동일하거나
사전 순으로 증가 -> 오름 차순
'''
def perm(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(lst[i])
        perm(level+1, i)
        path.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

path =[]

perm(0, 0)