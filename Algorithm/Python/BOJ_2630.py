'''
정사각형 => N*N
하얀색 또는 파란색 규칙에 따라 자름

규칙
1. 전체가 모두 한 색깔로 칠해져있지 않다면 가로, 세로로 중간을 자름
=> N/2*4개의 종이로 만든다

2. 나누어져있는 종이도 모두 그렇게 만든다.

3. 모든 종이가 한가지 색으로 칠해져있거나 더는 나눌 수 없는 종이일 때까지 나눈다.

위와 같이 잘랐을 때 파란 종이 수와, 하얀 종이 수를 세라

하얀 색은 0, 파란색은 1

2*2는 되어야 함

=> 이걸 어떻게 쪼개지?
일단 함수를 만들어야 해
함수를 만들어서 전부 0이거나 1인지 확인을 해야해
확인하는 함수
확인은 완탐하면 될 것 같음

그리고 아니라면 쪼개야해
쪼개는 함수를 만들어야 함
=> 이걸 어떻게 할까?
N을 2로 나눠서 그걸 새로운 변수에 만들어...?
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
result = [0,0]

def cut(y, x, n):
    color = arr[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != arr[i][j]:
                m = n//2
                cut(y,x,m)
                cut(y,x+m, m)
                cut(y+m,x,m)
                cut(y+m,x+m,m)
                return
    if color == 0: # 하얀색
        result[0]+=1
    else: # 1, 파란색
        result[1]+=1


cut(0,0,N)
print(result[0])
print(result[1])
