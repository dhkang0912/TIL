def perm(L, Battery, cnt):
    global minv
    if minv < cnt:
        return

    if L == N: # 만약 버스가 마지막 정류장에 도착했을 때
        # print(result)
        if minv > cnt:
            minv = cnt
        return

    if Battery == 0: # 배터리가 0이고 도착했을 때는 성공할 수 있게 해야함
        return

    result[L] = 0 # 충전 안 했을 때
    perm(L+1, Battery-1, cnt)

    result[L] = 1 # 충전을 했을 때
    perm(L+1, batter_lst[L], cnt+1)




T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0] # 정류장 개수
    batter_lst = lst[1:] + [0]
    result = [-1] * N # 각 버스정류장에서 충전 여부
    minv = float('inf')
    perm(1, batter_lst[0], 0) #1번에서 충전하고 가고 cnt를 치지 않음, 1번 배터리를 가지고 감

    print(f'#{tc} {minv}')