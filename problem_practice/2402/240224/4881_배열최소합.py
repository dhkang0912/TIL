import sys
sys.stdin = open("4881_input.txt", "r")

def pick_col(first_row_col):
    global picked_col
    col_lst = [i for i in range(N)]
    visited = [0]*N
    picked_col.append(first_row_col)
    visited[first_row_col] = 1

    for col in col_lst:
        if visited[col] == 0:
            picked_col.append(col)
            visited[col] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    picked_col = []
    min_sum = 123e2
    for first_row_col in range(N):
        pick_col(first_row_col)
        sum = 0
        for i in range(N):
            sum += arr[i][picked_col[i]]
        if min_sum > sum:
            min_sum = sum
        picked_col = []

    print(f'#{tc} {min_sum}')
