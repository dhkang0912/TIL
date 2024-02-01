# Sequential search
# 리스트에서 key를 찾아서 인덱스를 return
# 못 찾으면 -1을 return함
# def search(lst, N, key) :
#     idx = 0
#     for idx in range(N) :
#         if lst[idx] == key :
#             return idx
#     return -1


# def search(lst, N, key) :
#     idx = 0
#     while idx < N and lst[idx] != key :
#         idx += 1
#     if idx == N :
#         return -1
#     else :
#         return idx
# #
# def search(lst, N, key) :
#     idx = 0
#     while lst[idx] != key and idx < N :
#         idx += 1
#     if idx < N :
#         return idx
#     else :
#         return -1

#
# numbers = [4, 9, 11, 23, 2, 19, 7]
# N = len(numbers)
#
# print(search(numbers, N, 4))
# print(search(numbers, N, 7))
# print(search(numbers, N, 9))
# print(search(numbers, N, 100))


# 이진 검색
def binsearch(lst, N, key) :
    start = 0
    end = N - 1
    while start <= end :
        m = (start + end) // 2
        if lst[m] == key :
            return  m
        if lst[m] > key :
            end = m - 1
        else :
            start = m + 1


numbers = [4, 9, 11, 23, 2, 19, 7]
numbers.sort()
N = len(numbers)
print(binsearch(numbers, N, 2))
print(binsearch(numbers, N, 23))
print(binsearch(numbers, N, 9))
print(binsearch(numbers, N, 7))


# numbers의 데이터를 정렬한 후 정렬 결과를 리스트로 return
# def selectionS(numbers) :
#     n = len(numbers)
#     # 5개 중 제일 작은 값을 찾아서 0번째와 교환
#     # phase = 0 : 0에서 n-1까지 중 제일 작은 위치를 찾아서 0번째와 교환
#     # pahse = 1 : 1에서 n-1까지 중 제일 작은 위치를 찾아서 1번째와 교환
#     # pahse = 2 : 2에서 n-1까지 중 제일 작은 위치를 찾아서 2번째와 교환
#     # n이 5라면 phase 3까지 돌기
#     for phase in range(n-1) :
#         minV = numbers[phase]
#         minP = phase
#         for idx in range(phase+1, n) :
#             if minV > numbers[idx] :
#                 minV = numbers[idx]
#                 minP = idx
#         numbers[minP], numbers[phase] = numbers[phase], numbers[minP]
#
#
#     for phase in range(n-1) :
#         # minV = numbers[phase]
#         minP = phase
#         for idx in range(phase+1, n) :
#             if minV > numbers[idx] : #minV > numbers[idx]
#                 # minV = numbers[idx]
#                 minP = idx
#         numbers[minP], numbers[phase] = numbers[phase], numbers[minP]
        # 버블 정렬과 가장 다른 점은 위치를 변경하는 순서가 다름, 버블 정렬은 매번 교환, 이건 찾고나서 변경 -> 복잡도나 시간은 비슷
#
#
#     return numbers
#
# numbers = [64, 25, 10, 22, 11]
# print(selectionS(numbers))
# print(selectionS([64, 25, 10, 22, -1]))


# 달팽이 문제
'''
9 20 2 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14
'''
# value보다 큰 것 중 제일 작은 값을 찾아서 return
# def getMin(value) :
#     minV = 1e10
#     for row in range(N) :
#         for col in range(N) :
#             if arr[row][col] <minV  and arr[row][col] > value:
#                 minV = arr[row][col]
#     return minV
#
# N = 5
# arr = [list(map(int, input().split())) for _ in range(N)]
# # print(arr)
#
# new_arr = [[0] * N for _ in range(N)]
# # print(new_arr)
#
# value = 0
# row = 0
# col = 0
# # 우하좌상
# dr = [0, 1, 0, -1 ]
# dc = [1, 0, -1, 0]
# d = 0
# for _ in range(N*N):
#     value = getMin(value)
#     new_arr[row][col] = value
#     newR = row + dr[d] # 다음에 가는 위치
#     newC = col + dc[d]
#     if newR <0 or newR > N-1 or newC < 0 or newC > N-1 or new_arr[newR][newC] != 0 :
#         d = (d+1) % 4
#     row = row + dr[d]
#     col = col + dc[d]
#
#
# for row in range(N) :
#     for col in range(N) :
#         print(new_arr[row][col], end = ' ')
#     print()



