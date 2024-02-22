T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr =
    count = [[0, 0, 0] for _ in range(N)]
    for row in range(N):
        arr[row][0] = arr[row].count('W')
        arr[row][1] = arr[row].count('B')
        arr[row][2] = arr[row].count('R')

    for li in range():
        for l2 in range():
            # 0~l1까지 흰색
            # l1~l2까지 파란색
            # l2~N-1까지 빨간색
