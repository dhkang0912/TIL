import sys
sys.stdin = open("5188_input (1).txt", "r")

def perm(row, col, sum):
    global minV

    if row >= N-1 and col >= N-1:
        minV = min(minV, sum)
        return

    # 오른쪽, 아래쪽
    if row >= N-1:
        perm(row, col+1, sum+arr[row][col+1])
    elif col >= N-1:
        perm(row + 1, col, sum+arr[row+1][col])
    elif 0 <= row < N-1 and 0 <= col <= N-1:
        perm(row, col + 1, sum + arr[row][col+1])
        perm(row+1, col, sum + arr[row+1][col])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    minV = float('inf')
    #x, y, sum
    perm(0, 0, arr[0][0])
    print(minV)
