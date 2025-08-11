import sys
sys.stdin = open("4615_input(1).txt", "r")

# 색을 바꿀 좌표들의 리스트가 있음
def change_color(will_change_list):
    for row, col in will_change_list:
        if arr[row][col] == 1:
            arr[row][col] = 2
        elif arr[row][col] == 2:
            arr[row][col] = 1


def check(row, col, color, dr, dc):
    will_change_list = []
    New_row = row + dr
    New_col = col + dc
    # 범위 안에 있고 현재 위치의 돌과 색이 다르고 빈칸이 아닌 동안 반복
    while 0 <= New_row <= N-1 and 0 <= New_col <= N-1 and arr[New_row][New_col] != 0:
        # 쭉 가다가 나랑 같은 색 돌을 만났다 -> 그 전까지 쌓인 흰색 돌의 좌표를 가져감
        if arr[New_row][New_col] == color:
            return will_change_list
        # 다른 색깔 돌인 경우에는 좌표를 추가하고 다음 좌표 확인하러 감
        else:
            will_change_list.append((New_row, New_col))
            New_row += dr
            New_col += dc

    # 범위 안에서 검은 돌인 걸 만나지 못한 경우 빈 리스트를 리턴
    will_change_list = []
    return will_change_list
    # 어떻게 정상적으로 빠져나온 것과 아닌 것을 구분하지?




T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # N = N*N, M = 돌 놓는 횟수
    arr = [[0]*N for _ in range(N)]
    # 정가운데 흑, 백돌 배치하기
    start_row = N//2 - 1
    start_col = N//2 - 1
    for dr, dc in [(0, 0), (1, 1)]:
        arr[start_row+dr][start_col+dc] = 2

    for dr, dc in [(1, 0), (0, 1)]:
        arr[start_row+dr][start_col+dc] = 1
    print(arr)

    for i in range(M):
        row, col, color = map(int, input().split())
        row -= 1
        col -= 1
        arr[row][col] = color
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # 색을 바꿀 좌표들의 리스트를 가져옴
            change_color(check(row, col, color, dr, dc))

    # 돌면서 각각 개수 확인해주기
    cnt_B = 0
    cnt_W = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 1:
                cnt_B += 1
            elif arr[row][col] == 2:
                cnt_W += 1

    print(f'#{tc} {cnt_B} {cnt_W}')


