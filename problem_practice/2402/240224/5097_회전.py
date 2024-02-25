T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N=숫자의 갯수, M=회전의 수
    lst = list(map(int, input().split()))
    for i in range(M):
        lst.append(lst.pop(0))
    print(f'#{tc} {lst[0]}')