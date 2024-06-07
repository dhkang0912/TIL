# 2005 파스칼의 삼각형
# 크기가 N인 파스칼 삼각형을 만듦
# 첫번째 줄은 항상 숫자 1
# 두번째 줄부터 자신의 왼쪽과 오른족 위의 숫자의 합으로 구성
# 1 -> 0,0
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# N은 항상 1이상 10이하의 정수 -> 1~10

# 인풋
# T를 인풋 받음
# N을 인풋 받음

import sys
sys.stdin = open("2005_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for i in range(0,N):
        arr[i][0] = 1
        arr[i][i] = 1

    for row in range(2, N):
        for col in range(1, N):
            arr[row][col] = arr[row-1][col] + arr[row-1][col-1]


    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end = ' ')
        print()
