'''
RGB 거리
N개의 집 (1번~N번)
빨, 초, 파로 칠하는 최소 비용
N번 집의 색 != N-1번 집의 색 or N+1번 집의 색

# 입력
- N개의 집수
- 각 번째의 집을 빨강, 초록, 파랑 색으로 칠하는 비용

# 출력
- 모든 집을 칠하는 비용의 최솟값
'''

N = int(input())Z
RGB = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
# print(RGB)
# print(dp)

# 첫 번째 집은 직접 할당 (초기화)
dp[0][0] = RGB[0][0]
dp[0][1] = RGB[0][1]
dp[0][2] = RGB[0][2]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))
