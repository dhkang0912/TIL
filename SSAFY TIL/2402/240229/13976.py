import sys
sys.stdin = open("13976_input.txt", "r")
'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
'''

def remove_visited(row, col, power):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for d in range(4):
        for jump in range(1, power+1):
            new_r = row + dr[d] * jump
            new_c = col + dc[d] * jump
            if 0 <= new_r <= N-1 and 0 <= new_c <= N-1:
                arr[new_r][new_c] = 'X'

def find_empty_cell_count():
    cnt = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'H':
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]
    # print(arr)
    # visited = [[0]*N for _ in range(N)]

    # 시작점이 되는 기지국 위치 찾기
    for row in range(N+1):
        for col in range(N):
            if arr[row][col] == 'A':
                arr[row][col] = 'X'
                remove_visited(row, col, 1) #row, col, power
            elif arr[row][col] == 'B':
                arr[row][col] = 'X'
                remove_visited(row, col, 2) #row, col, power
            elif arr[row][col] == 'C':
                arr[row][col] = 'X'
                remove_visited(row, col, 3) #row, col, power

    print(f'#{tc} {find_empty_cell_count()}')