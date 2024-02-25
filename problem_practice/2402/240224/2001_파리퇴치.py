# import sys
# sys.stdin = open("2001_파리퇴치_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for row in range(N):
        for col in range(N):
            M_sum = 0
            for i in range(M):
                for j in range(M):
                    new_row = row + i
                    new_col = col + j
                    if 0 <= new_row <= N-1 and 0 <= new_col <= N-1:
                        M_sum += arr[new_row][new_col]
            if max_sum < M_sum:
                max_sum = M_sum

    print(f'#{tc} {max_sum}')

