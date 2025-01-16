'''
2*n 타일링
- 그림 그려서 해보는게 좋음
'''

n = int(input())
dp = [0] * 10007
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 10007

print(dp[n])
