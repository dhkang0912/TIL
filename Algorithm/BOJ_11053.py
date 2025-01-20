'''
가장 긴 증가하는 부분 수열
중복 없이 sort하면 되는건가? => 아님
부분 수열 중에 증가하게 되는 경우를 의미함
'''

N = int(input())
lst = list(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        # i번째 숫자 이전을 모두 확인하기 위해
        # 현재 숫자가 이전 숫자보다 크다면
        if lst[i] > lst[j]:
            # dp[j]+1 = lst[j]를 포함하는 수열에 lst[i]를 추가했을 때의 길이
            # 더 긴 길이를 가지고 있는 녀석의 길이를 넣어주기
            # i번째 수를 마지막으로 하는 수열
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

