
# 240131 수업 내용
# 1) 2차원 배열 인풋 받기
# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# print(arr)


# 2) 2차원 배열에서 상하좌우로 움직이기
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# i = 3
# j = 4
#
# for k in range(0,4) :
# 	ni = i + di[k]
# 	nj = j + dj[k]
# 	print(ni, nj)
#
# -1 인덱스가 존재하여 유효성 검증을 해줘야 함
# N = 5
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# for i in range(N) :
#     for j in range(N) :
#         for k in range(4) :
#             ni = i + di[k]
#             nj = j + dj[k]
#             print((ni, nj), end = ' ')
#         print()
#
# 유효성 검증
# N = 5
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# arr = [[0]*N for _ in range(N)]
# for i in range(N) :
#     for j in range(N) :
#         for k in range(4) :
#             ni = j + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj], end = ' ')
#         print()
#
#
# N = 5
# arr = [[0]*N for _ in range(N)]
# for i in range(N) :
#     for j in range(N) :
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj], end=' ')
#         print()


# bit = [0, 0, 0, 0]
# for i in range(2) :
#     bit[0] = i
#     for j in range(2) :
#         bit[1] = j
#         for k in range(2) :
#             bit[2] = k
#             for I in range(2) :
#                 bit[3] = I
#                 print_subset(bit)



# arr = [3,6,7,1,5,4]
# n = len(arr)
# #n: 원소의 개수
# for i in range(1 <<n) :
#     for j in range(n):
#         if i & (1<<j);
#         print(arr[j], end=", ")
#         #1<<n: 부분 집합의 개수
#         # 원소의 수만큼 비트를 비교함
#         # i j번 비트가 1인경우
#         #j번 원소 출력
#     print()
# print()


# 이차원 배열
# N = 3
# M = 4
# arr = [[1, 1, 1, 10],
#        [2, 2, 2, 20],
#        [3, 3, 3, 30]]

# 이차원 배열 코드로 표현
# for row in range(N):
#     for col in range(M):
#         print(arr[row][col])
#
# print()

# 각 행별로 누적합 후 가장 큰 데이터 뽑기
# max_v = 0
# for row in range(N):
#     sum_v = 0
#     for col in range(M):
#         # print(arr[row][col])
#         sum_v += arr[row][col]
# 
#     if max_v < sum_v :
#         max_v = sum_v
# 
# print(sum_v)


# 전체 데이터의 누적합
# sum_v = 0
# for row in range(N):
#     for col in range(M):
#         # print(arr[row][col])
#         sum_v += arr[row][col]
#
# print(sum_v)
#
# print()

# 열별로 데이터 누적합
# sum_v = 0
# for col in range(M):
#     for row in range(N):
#         # print(arr[row][col])
#         sum_v += arr[row][col]
#     print(sum_v)


# 연습 문제 1-1
# 대각선 원소의 합 구하기
# sumV = 0
# for i in range(N) :
#     sumV += arr[i][N-1-i]
# # for i in range(N) :
#     sumV += arr[i][N-1-i]
#
# sumV = sumV-arr[N//2][N//2]


# 연습 문제 1-2
# def myAbs(n):
#     # if n> 0 :
#     #     return n
#     # return -n
#     return n if n>=0 else -n
#
# sumV = 0
# for row in range(N) :
#     for col in range(M) :
#         print(row, col, arr[row][col])
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#         for d in range(4):
#             newR = row + dr[d]
#             newC = col + dr[d]
#             if 0 <= newR < N and 0 <= newC < N
#             t =myAbs(arr[row][col] - arr[newR][newC])
#             sumV += t
#
# print(sumV)

# # 위치 상하좌우로 이동하기
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# for d in range(4) :
#     newR = row + dr[d]
#     newC = col + dr[d]
#
# # 방향을 틀 필요 없고 순서도 정해져있다면 이렇게 적을 수도 있음
# for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
#     newR = row + dr
#     newC = col + dr


# 부분 집합의 합
# number = [10, 11, 12]
# N = 3
# for i in [0,1] :
#     for j in [0,1] :
#         for k in [0, 1] :
#             # print(i, j, k)
#             print('{', end=' ')
#             if i == 1 :
#                 print(number[0], end=' ')
#             if j == 1 :
#                 print(number[1], end=' ')
#             if k == 1 :
#                 print(number[2], end=' ')
#
#             print('}')

# 이진수 활용해서 부분집합 구하기
# for i in range(2**N) : #1<<N : 8 == 2**3 == 1000(1<<3)
#     print(i, bin(i))


# numbers = [10, 11, 12]
# n=3 #011
#
# print(7&5)
# 111
# & 001
# 2진수로 비교할 때 위아래 모두 1이어야지 1로 뽑힘 -> 밑에가 1일 경우 원본을 뽑아줘
# 2진수로 비교할 때 하나라도 0이면 0로 뽑힘 -> 밑에가 0일 경우 원본을 무시
# 011  011  011
#&001 &010 &100
#or 000 /000 /000
# 0bit : &1<<0
# 1bit : &1<<1
#
# for i in range(2**N) : #1<<N : 8 == 2**3 == 1000(1<<3)
#     # print(i, bin(i))
#     print(i, end = '=>')
#     sumV = 0
#     for j in range(N) :
#         bitmasking = i & (1 << j)
#         if bitmasking :
#             sumV += numbers[j]
#             print(numbers[j], end = ' ')
#             # j번째 bit가 1인 경우 : 0001/0010/0100/1000
#         # else :
#         #     pass
#             # 0인 경우
#
#     print('=', sumV)

# 특정 합일 때 갯수 구하기
# numbers = [10, 11, 12, 15, 10, 2, 5, 15, 87, 95, 100, 125, 1235, 45, 68]
# N = 15
#
#
# cnt = 0
# for i in range(2**N) : #1<<N : 8 == 2**3 == 1000(1<<3)
#     # print(i, bin(i))
#     print(i, end = '=>')
#     sumV = 0
#     for j in range(N) :
#         bitmasking = i & (1 << j)
#         if bitmasking :
#             sumV += numbers[j]
#             print(numbers[j], end = ' ')
#             # j번째 bit가 1인 경우 : 0001/0010/0100/1000
#         # else :
#         #     pass
#             # 0인 경우
#     print('=', sumV)
#     if sumV == 1800 :
#         cnt += 1
# print(cnt)

# 이차원 배열 공간 만들기
# arr = [[-1] * 3 for _ in range(3)]
# print(arr)
# arr[1][1] = 0
# print(arr)