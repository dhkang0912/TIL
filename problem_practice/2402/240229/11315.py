import sys
sys.stdin = open("11315_input.txt", "r")
'''
continue보다 break를 쓰는게 더 좋은 성능을 냄
=> 덜 순회하니까

이유
5목을 다 세야하는데 2목만 범위에 벗어나는 경우
더 순회할 수 필요가 없음

N*N 크기의 배열이 있음
돌이 가로, 세로,대각선 중 하나 방향으로 다섯 개 이상 연속한 부분이 있는지 확인하기

1) 가로로 5개 연속한 방향이 있는지 확인
2) 세로로 5개 연속한 방향이 있는지 확인
3) 대각선으로 5개 연속한 방향이 있는지 확인
=> delta 사용
'''

def omok():
    dr = [1, 0, 1, 1]
    dc = [0, 1, 1, -1]
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                for d in range(len(dr)):
                    cnt = 1
                    for step in range(1, 5):
                        new_row = row + dr[d] * step
                        new_col = col + dc[d] * step
                        if 0 <= new_row <= N - 1 and 0 <= new_col <= N - 1:
                            if arr[new_row][new_col] == 'o':
                                cnt += 1
                            if cnt == 5:
                                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    print(f'#{tc} {omok()}')

# 라이브 쌤 코드
# def omok(y, x):
#     dy = [1, 0, 1, -1]
#     dx = [0, 1, 1, 1]
#
#     # 네 방향 탐색
#     for bang in range(4):
#         cnt = 1 # 기준 좌표에 돌이 있다, cnt = 1부터 시작
#         # 돌 4개를 탐색
#         for power in range(1, 5):
#             ny = y + (dy[bang] * power)
#             nx = x + (dx[bang] * power)
#             if not ( 0 <= ny < n and 0 <= nx < n):
#                 break
#             if arr[ny][nx] == 'o':
#                 cnt += 1
#
#             if cnt == 5:
#                 return True
#     return False
#
# def game_start():
#     for r in range(n):
#         for c in range(n):
#             if arr[r][c] == 'o':
#                 if omok(r,c):
#                     return 'YES'
#     return 'No'
#
# T= int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [input() for _ in range(n)]
#     result = game_start()
#     print(f'{tc} {result}')

