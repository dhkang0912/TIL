import sys
sys.stdin = open("2817_input (1).txt", "r")

# def dfs(level, sum):
#     path = []
#     global cnt
#     # base 조건 (N개를 뽑고 안 뽑고 할 수 있음, N개를 다 뽑아버리면 더 뽑을게 없어서 끝내야 함)
#     if level >= N:
#         if sum == K:
#             cnt += 1
#         return
#
#     dfs(level+1, sum+lst[level])
#     dfs(level+1, sum)
#
#
# T =int(input())
# for tc in range(1, T+1):
#     # N은 주어진 수의 개수, K는 보고자 하는 경우 -> 특정 합
#     N, K = map(int, input().split())
#     lst = list(map(int, input().split()))
#     cnt = 0
#
#     # 시작 레벨 -> 아무것도 없음, sum = 아무것도 안 더해짐
#     dfs(0, 0)
#     print(f'#{tc} {cnt}')


def dfs(level, start, sum):
    global cnt
    # base 조건 (N개를 뽑고 안 뽑고 할 수 있음, N개를 다 뽑아버리면 더 뽑을게 없어서 끝내야 함)
    if level >= N:
        if sum == K:
            cnt += 1
        return

    for i in range(start, N):
        dfs(level+1, i + 1, sum+lst[i])
        dfs(level + 1, i + 1, sum)



T =int(input())
for tc in range(1, T+1):
    # N은 주어진 수의 개수, K는 보고자 하는 경우 -> 특정 합
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    visited = [0] * N

    # 시작 레벨 -> 아무것도 없음, sum = 아무것도 안 더해짐
    dfs(0, 0, 0)
    print(f'#{tc} {cnt}')