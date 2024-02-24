import sys
sys.stdin = open("1974_input.txt", "r")

def row_check(arr):
    result = 1
    for row in range(N):
        count_row = [0]*(N+1)
        for col in range(N):
            count_row[arr[row][col]]+=1
        if 0 not in count_row[1:N+2]:
            result *= 1
        else:
            result *= 0
    return result

def col_check(arr):
    result = 1
    for col in range(N):
        count_col = [0]*(N+1)
        for row in range(N):
            count_col[arr[row][col]] += 1
        if 0 not in count_col[1:N+2]:
            result *= 1
        else:
            result *= 0
    return result

def row_col_check(arr):
    result = 1
    for row in range(0, N, 3):
        for col in range(0, N, 3):
            count_ARR = [0] * (N + 1)
            for i in range(3):
                for j in range(3):
                    new_row = row+i
                    new_col = col+j
                    count_ARR[arr[new_row][new_col]]+=1
            if 0 not in count_ARR[1:N+2]:
                result *= 1
            else:
                result *= 0
    return result


T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]


    result = row_check(arr) * col_check(arr) * row_col_check(arr)
    print(f'#{tc}', result)