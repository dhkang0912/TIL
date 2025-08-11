#뒤집을 돌의 좌표들을 구해주는 함수
get_reverse_stone (y, x, bang):
    result = []
    dy, dx = dir[bang]
    ny, nx = y, x
    while True:
        ny, nx = ny + dy, nx + dx
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return []
        if board[ny][nx] == 0: return []
        if board[ny][nx] == color: break
        result.append((ny, nx))
    return result


# 1. 빈 좌표를 만든다
arr = [][]

# 2. 중앙에 배치

# 명령 갯수만큼 반복
    row, col, color =
    if color == 1:
        color_r = 2
    else:
        color_r = 1

    for dr, dc in [8방향]:
        while 범위비교, 값 비교 (나하고 같은 색이 나올 때까지, 나하고 다른 색인 동안 => 뒤집을 수 있는지 확인):
            newR newC =
        if 값을 찾아서 빠져 나온 경우:
            while 원래 좌표가 아닌 동안
                역 방향으로 뒤집는다
    누가 이겼는지 센다