# import sys
# sys.stdin = open("16268_input1.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1 , 0, 0]
    dc = [0, 0, -1 ,1]
    max_sum = 0
    for row in range(N):
        for col in range(M):
            arr_sum = arr[row][col]
            new_row = 0
            new_col = 0
            for d in range(4):
                new_row = row + dr[d]
                new_col = col + dc[d]
                if 0 <= new_row <= N-1 and 0 <= new_col <= M-1:
                    arr_sum += arr[new_row][new_col]
            if max_sum < arr_sum:
                max_sum = arr_sum
    print(f'#{tc} {max_sum}')


