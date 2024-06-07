import sys
sys.stdin = open("10760_input.txt", "r")

def count_cnt(row, col, start):
    cnt = 0
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        New_row = row + dr
        New_col = col + dc
        if 0 <= New_row <= N-1 and 0 <= New_col <= M-1:
            if arr[New_row][New_col] < start:
                cnt += 1
    return cnt

# 인풋받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N = row, M = col
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    result = 0

    # 시작 지점 지정
    for row in range(N):
        for col in range(M):
            # 8구역에 시작점보다 낮은 지대 개수 확인
            start = arr[row][col]
            pre_num = count_cnt(row, col, start)
            if pre_num >= 4:
                result += 1

    print(f'#{tc} {result}')
