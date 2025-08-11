def perm(level,start):
    if level == M:
        print(*path)
        return
    
    # 중복은 가능함 (visited 없음), 나왔던 수열이 다시 나올 수 없음, 이전 i와 동일한 start부터 시작
    for i in range(start, N+1):
        path.append(i)
        perm(level+1, i)
        path.pop()


N, M = map(int, input().split()) # N까지의 숫자, M개를 뽑음, 수는 중복 가능하지만, 중복된 수열을 여러번 출력하면 안됨
path = []
perm(0, 1)