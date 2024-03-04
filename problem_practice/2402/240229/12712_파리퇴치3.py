import sys
sys.stdin = open("12712_input.txt", "r")

def plus_flies(row, col):
    dr = [-1 , 1, 0, 0]
    dc = [0, 0, -1, 1]

    arr_sum = 0
    for jump in range(1, M):
        for i in range(4):
            new_row = row + dr[i] * jump
            new_col = col + dc[i] * jump
            if 0 <= new_row <= N-1 and 0 <= new_col <= N-1:
                arr_sum += arr[new_row][new_col]

    return arr_sum


def cross_flies(row, col):
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    arr_sum = 0
    for jump in range(1, M):
        for i in range(4):
            new_row = row + dr[i] * jump
            new_col = col + dc[i] * jump
            if 0 <= new_row <= N - 1 and 0 <= new_col <= N - 1:
                arr_sum += arr[new_row][new_col]

    return arr_sum


# 인풋
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 배열 크기, M은 파리 약의 세기
    arr = [list(map(int, input().split())) for _ in range(N)] # 파리의 개수가 정해진 arr
    # print(arr)
    died_flies = [] # 잡을 수 있는 파리 갯수 저장


    # 처음부터 쭉 돌면서 시작점 지정
    for row in range(N):
        for col in range(N):
            # +형태로 잡을 수 있는 파리 개수 저장 변수에 시작점 넣고 시작
            plus_sum = arr[row][col]
            # +형태로 잡을 수 있는 파리의 위치에서 잡을 수 있는 값을 모두 더하여 리턴
            plus_sum += plus_flies(row, col)
            # 최대 비교를 위한 리스트에 추가
            died_flies.append(plus_sum)

            # X 형태로 잡을 수 있는 파리 개수 저장 변수에 시작점 넣고 시작
            cross_sum = arr[row][col]
            # X 형태로 잡을 수 있는 파리의 위치에서 잡을 수 있는 값을 모두 더하여 리턴
            cross_sum += cross_flies(row, col)
            # 최대 비교를 위한 리스트에 추가
            died_flies.append(cross_sum)

    print(f'#{tc} {max(died_flies)}')

