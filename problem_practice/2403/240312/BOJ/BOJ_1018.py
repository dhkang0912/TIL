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


