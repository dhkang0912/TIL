'''
순열, 최소합
'''

# def perm(L):
#     global minv
#     if L == N:
#         sumv = 0
#         for j in range(L):
#             sumv += arr[j][result[j]]
#         if minv > sumv:
#             minv = sumv
#
#     for i in range(N):
#         if not visited[i]:
#             result[L] = i
#             visited[i] = 1
#             perm(L+1)
#             visited[i] = 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 제품과 공장의 개수
#     arr = [list(map(int, input().split())) for _ in range(N)] # 각 경우의 수의 값
#     # print(arr)
#
#     minv = float('inf')
#     visited = [0] * N
#     result = [-1] * N # 뽑을 수의 인덱스의 집합
#
#     perm(0)
#     print(minv)

def perm(L, sumv):
    global minv
    if minv < sumv:
        return

    if L == N:
        if minv > sumv:
            minv = sumv
        return

    for i in range(N):
        if not visited[i]:
            result[L] = i
            visited[i] = 1
            perm(L+1, sumv+arr[L][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 제품과 공장의 개수
    arr = [list(map(int, input().split())) for _ in range(N)] # 각 경우의 수의 값
    # print(arr)

    minv = float('inf')
    visited = [0] * N
    result = [-1] * N # 뽑을 수의 인덱스의 집합

    perm(0, 0) # level 0부터 시작, sum 0부터 시작
    print(f'#{tc} {minv}')
