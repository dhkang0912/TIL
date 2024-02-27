import sys
sys.stdin = open("5189_input.txt", "r")
'''
# 문제 이해
전기카트로 사무실에서 출발, 관리구역을 돌고 다시 사무실로 돌아옴
-> 각 구역을 한번씩만 방문하고 사무실로 돌아오는 최소 배터리 용량
    => 순열
1번은 사무실, 2번부터 N번까지 관리구역
    -> 관리구역까지 열 중복 없이 다 돌고
1로 시작, 무조건 1에 도착, 가운데 2개 들어갈 수 있음
 => 2군데 순열, 최소합 구하기

# 재귀함수
열의 idx를 중복없이 돌면서 path에 조합을 넣어줌
만약 3번째 행에 도착했으면 여태까지 조합인 path의 값들을 행렬로 조합하여 더해줌
만약 minv보다 조합하여 더해준 값이 더 작다면 minv를 바꿔줌


# 인풋
1. T = 3
2. N = 3 # N*N 행렬
3. N*N arr 만들어주기

# 아웃풋

min_sum(1) # k = 행의 인덱스, 행의 인덱스 시작을 넣어줌

print(f'#{tc} {minv})


'''
# def per(k):
#     global minv
#     if k == N:
#         path_sum = 0
#         for num in range(N-1):
#             path_sum += arr[path[num]][path[num+1]]
#         path_sum += arr[path[-1]][0]
#         print(path, path_sum)
#         if minv > path_sum:
#             minv = path_sum
#         return
#
#     for i in range(N):
#         if not used[i]:
#             path[k] = i # k는 행의 인덱스, i가 열의 인덱스로 생각하면 됨
#             used[i] = 1
#             per(k+1)
#             used[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr= [list(map(int, input().split())) for _ in range(N)]
#     minv = 123e3435
#
#     path = [-1] * N
#     used = [0] * N
#     used[0] = 1
#     path[0] = 0
#     per(1)
#     print(minv)



# def per(k, midsum):
#     global minv
#     if k == N:
#         midsum += arr[path[-1]][0]
#         # print(path, midsum)
#         if minv > midsum:
#             minv = midsum
#         return
# 
#     for i in range(N):
#         if not used[i]:
#             path[k] = i
#             used[i] = 1
#             s = path[k-1]
#             e = path[k] # 이게 i
#             per(k+1, midsum + arr[path[k-1]][i]) # k는 행의 인덱스, i가 열의 인덱스로 생각하면 됨
#             used[i] = 0
# 
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr= [list(map(int, input().split())) for _ in range(N)]
#     minv = 123e3435
# 
#     path = [-1] * N
#     used = [0] * N
#     used[0] = 1
#     path[0] = 0
#     per(1, 0)
#     print(minv)


# 재귀함수, 순열
def min_sum(k):
    global minv
    if k == N:
        arr_sum = 0
        for num in range(N-1):
            s = path[num]
            e = path[num+1]
            arr_sum += arr[s][e]
        arr_sum += arr[path[-1]][0]

        if minv > arr_sum:
            minv = arr_sum
        return

    for i in range(N):
        if used[i] == 0:
            path[k] = i
            used[i] = 1
            min_sum(k+1)
            used[i] = 0




# 인풋
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    minv = 123e4564
    path = [0] * N
    used = [0] * N
    used[0] = 1

    min_sum(1) # k = 행의 인덱스, 행의 인덱스 시작을 넣어줌
    print(f'#{tc} {minv}')