'''
N, M
중복 순열

카드는 중복된 걸 뽑을 수 있음 -> visited는 없음
동일한 수열을 여러번 뽑을 수는 없음 -> 오름차순으로 증가
순서대로 증가하게 출력

'''

def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path.append(lst[i])
        perm(level+1)
        path.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
perm(0)