'''
N과 M (9)
- 재귀, 백트래킹을 통한 수열 구하기

N개의 자연수 중 M개를 고른 수열 출력
수열 한개씩 출력
중복되는 수열은 한번만 출력함 (순열이 아님)
공백으로 구분하여 출력함
사전 순으로 증가하는 순서로 출력해야함

# 인풋
1. N, M = N개 중 M개의 수열 고르기
2. N개의 숫자

# 로직
- 숫자를 받아서
- M의 level만큼 반복하여 N개 안에서 뽑음
    - level에 도달하면 return하고 출력해야함
    - 오름차순이니 정렬을 해놓아야 함
    - 중복되면 안되니 visited를 통해 방문 여부 확인
    - ans에 하나씩 뽑아서 넣고 이를 출력, 출력 후 초기화
'''

def perms(level):
    global ans
    if level == M:
        print(*ans)
        return
    
    prev = -1
    for i in range(len(nums)):
        # i번째를 방문하지 않았다면 뽑기
        # 같은 레벨에서 동일한 값을 뽑는 것을 방지 => 중복 수열 방지
        if visited[i] == 0 and nums[i] != prev:
            visited[i] = 1
            ans.append(nums[i])
            perms(level+1)
            ans.pop()
            visited[i] = 0
            prev = nums[i]


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0]*len(nums)
ans = []
# print(nums, visited)

perms(0)