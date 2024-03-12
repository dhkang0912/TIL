'''
M*N 크기의 보드를 찾음
W, B으로 칠해져있음
보드를 잘라서 8*8로 만들어야 함

검, 흰 번갈아 칠해져있어야 함
칸은 검, 흰으로 칠해져있고 변을 공유하는 사각형은 다른 색으로 칠해져있어야 함
-> 이게 무슨 말일까?
->흰검흰검이면 밑에는 검흰검흰

8*8을 골라서 다시 칠해야하는 갯수를 세기

minv 지정하고 시작 큰 수로
이중 for 문
1. 시작점을 고른다 -> 첫번째 for문 M*N 보드
    2. 시작점부터 8*8을 돌면서 확인한다 -> 두번째 for문
        2-0. cnt 초기화가 필요함
        2-1. 돌 때 위치가 범위 안에 있어야 함 M*N 범위를 넘으면 안됨
        2-2. 고쳐야 하는 경우를 cnt함
            2-2-1. 만약 아래 또는 우측이 나랑 같다면 cnt +=1

    3. min(minv, cnt)한 걸 minv에 지정
'''

'''
N, M = map(int, input().split()) # M*N
arr = [list(input()) for _ in range(N)]
# print(arr)

minv = 1234e231
for row in range(M):
    for col in range(N): # 시작점을 고른다
        cnt = 0
        for i in range(8): #8*8을 돈다
            for j in range(8):
                move_row = row + i
                move_col = col + j
                if 0 <= move_row+1 <= M-1 and 0 <= move_col+1 <= N-1: #우측, 아래측이 있다면
                    if (arr[move_row+1][move_col] == arr[move_row][move_col]) or (arr[move_row][move_col+1] == arr[move_row][move_col]): # 우측 또는 아래측이 나랑 같다면 잘못됐다고 cnt
                        cnt += 1
        minv = min(minv, cnt)

print(minv)
'''
'''
처음에는 이차원 리스트를 돌면서 체크하려고 했지만 그렇게는 되지 않는 문제로, 정말 모든 경우의 수를 체크해야했다.
white, black board 경우 모두를 체크해서 더 바꿀 게 적은 경우를 확인해야했다.
시작점을 기준으로 white, black일 때를 체크하니 오히려 개수가 맞지 않았다.
white, black board를 이런 식으로 구현할 생각을 해본 건 좋은 시도였다.

인덱스의 패턴으로 확인한 사람들이 대부분이다.
-> 행과 열의 합이 짝수, 홀수이면 각각 일정한 색을 가지게 됨
https://fre2-dom.tistory.com/388
'''
import sys
input = sys.stdin.readline

WB = ['W', 'B']*4
BW = ['B', 'W']*4
white = [WB, BW] * 4
black = [BW, WB] * 4
# print(white)
# print(black)

M, N = map(int, input().split())
arr = [list(input()) for _ in range(M)]
minv = 12434e1332
for row in range(M-8+1):
    for col in range(N-8+1):
        black_minv = 0
        white_minv = 0
        for i in range(8):
            for j in range(8):
                New_row = row + i
                New_col = col + j
                if arr[New_row][New_col] != white[i][j]:
                    black_minv += 1
                if arr[New_row][New_col] != black[i][j]:
                    white_minv += 1

        minv = min(minv, black_minv, white_minv)

print(minv)





