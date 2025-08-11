'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
-> 중복 수열
-> 중복은 가능하지만 오름차순으로 선택
'''

def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        path[level] = i
        perm(level+1)


N, M = map(int, input().split()) # N까지 숫자, M개를 고름
path = [-1] * M
perm(0)