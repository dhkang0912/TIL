def combi(level, s):
    # 6개의 수를 뽑는다
    if level == 6:
        print(*path)
        return

    # 사용할 수 있는 숫자들을 확인하면서 조합을 만든다.
    for i in range(s, len(lst)):
        # 기존에 사용하지 않은 숫자면
        if not visited[i]:
            # 조합의 수에 넣어주기
            path[level] = lst[i]
            # 사용했다고 작성해주기
            visited[i] = 1
            # 다음 숫자 고르러 가기
            combi(level+1, i+1)
            # 마지막 숫자까지 가능성 보고 그 앞 숫자 다른 가능성 보기 위해 사용여부 빼주기
            visited[i]=0
    



while True:
    lst = list(map(int, input().split()))
    k = lst.pop(0)
    if k == 0:
        break
    else:
        visited = [0]*k
        path = [0]*6
        # 첫번째 인덱스부터 조합을 만들기 위해 0을 
        combi(0,0)
        print()