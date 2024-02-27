import sys
sys.stdin = open("5188_input.txt", "r")
'''
# 함수 def minsum(x, y, sum)
종료 조건
- 어쨌든 최종적으로 도착할 수 있는 곳은 (N-1, N-1)
    -> (N-1, N-1)까지 갈 수 있으니, 최종 종료될 때는 (N,N)일 때 빠져나와야 함
    -> 최소값을 sum과 비교하기
        -> sum이 더 작다면 최소값 변경
    -> return

재귀 함수
- 경우의 수
1) x가 범위를 넘을 때
    - 오른쪽으로 갈 수 있음 => minsum(x, y+1, sum += arr[x][y])
2) y가 범위를 넘을 때
    - 아래로 갈 수 있음
3) 둘 다 범위를 넘지 않을 때
    - 아래로 갈 수 있음
    - 오른쪽으로 갈 수 있음



# 인풋
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

1. T를 입력
2. N을 입력
3. N*N 배열 입력
4. global minv를 사용 

# 출력
함수에 좌표를 넣어서 호출 (0,0, sum)
minv를 출력
'''

# 내가 짠 코드
def minsum(x, y, arr_sum):
    global minv
    if (x >= N-1)  and (y >= N-1): # 종료 조건
        # 최소값 비교
        if minv > arr_sum:
            minv = arr_sum
        return

    if x >= N-1:
        minsum(x, y+1, arr_sum + arr[x][y+1])
    elif y >= N-1:
        minsum(x+1, y, arr_sum + arr[x+1][y])
    # elif (0 <= x <= N-1) and (0 <= y <= N-1):
    else:
        minsum(x, y + 1, arr_sum + arr[x][y+1])
        minsum(x+1, y, arr_sum + arr[x+1][y])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minv =1243e23123

    minsum(0,0,arr[0][0])
    print(f'#{tc} {minv}')
#

'''
# 오프라인 강사님 설명
def recur(row, col, midsum):
    global minv
    # path.append((row, col))

    # if k == 2*N-1:
    if row == N-1 and col == N-1:
        # sumv = sum(path)
        # print(path)
        # print(midsum)
        if minv > midsum:
            minv = midsum


    if col + 1 < N:
        path.append((row, col+1, arr[row][col+1]))
        recur(row, col+1, midsum+arr[row][col+1])
        path.pop()
    if row + 1 < N:
        path.append((row+1, col, arr[row+1][col]))
        recur(row+1, col, midsum+arr[row+1][col])
        path.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minv = 10*N
    path = []
    recur(0, 0, arr[0][0])
    print(minv)
'''