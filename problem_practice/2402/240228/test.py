# arr= ['A', 'B', 'C', 'D', 'E'] # 2명 이상 픽
# n = len(arr)
#
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end = ' ')
#         tar >>= 1
#
# for tar in range(1<<n): # range(0,2**5)
#     print('{', end = '')
#     get_sub(tar)
#     print('}')
#
# get_sub(n)

'''
가장 적은 사람들부터 들어감
'''
# waiting = [15, 30, 50, 10]
# waiting.sort()
# n = len(waiting)
# # waiting = sorted(waiting)
# left_person = n-1
# result = 0
# for i in range(n):
#     result += waiting.pop(0)*left_person
#     left_person -= 1
#
#
#
# print(result)

# person = [15, 30, 50, 10]
# n = len(person)
# person.sort()
# sum = 0
# left_person = n - 1 # 화장실을 이용 아직 못한 대기자의 수
#
# for turn in range(n):
#     time = person[turn]
#     sum += left_person * time
#     left_person -= 1
# print(sum)

'''
음...오...아...예...
가장 적은 회의 시간 걸 먼저 배치, 그리고 남은 걸 배치

'''


# def print_data(path):
#     for idx in path:
#         print(arr[idx], end=' ')
#
#
# def perm(k, N, K):
#     if k == K:
#         # print(path)
#         print_data(path)
#         return
#     for i in range(N):
#         path[k] = i
#         visited[i] = True
#         perm(k + 1, N, K)
#         visited[i] = False
#
#
# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# K = 3
# path = [-1] * K
# visited = [False] * N
# perm(0, N, K)

# def subsum_print(path):
#     sumv = 0
#     for idx in range(N):
#         if path[idx]:
#             print(arr[idx], end=' ')
#     print()
#
#
# # N개의 데이터로 K개의 순열을 재귀로 만든다
# def subset(k):
#     if k == N:
#         # print(path)
#         subsum_print(path)
#         return
#
#     for i in range(2):
#         path[k] = i
#         subset(k + 1)


# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# path = [-1] * N
# subset(0)
#
# cnt = 0
# def combi(k, start):
#     global cnt
#     cnt += 1
#     if k == K:
#         print(path)
#         return
#
#     for i in range(start, N - K + 1 + k):  # 마지막 [5,5] => 반복 안함
#         path[k] = i
#         combi(k + 1, i + 1)
#
#
# arr = ['a', 'b', 'c', 'd', 'e']
# N = 5
# K = 3
# path = [-1] * N
# combi(0, 0)
# path = [-1] * K
# print(cnt)

lst = [(1,4), (3,5), (1,6), (5,7), (3,8), (5,9), (6,10), (8,11), (2,13), (12,14)]
lst2 = []
N = len(lst)
for d in lst:
    d = list(d)
    lst2.append(d)
    d[0], d[1] = d[1], d[0]

lst.sort(key = lambda x : x[1])
print(lst)
print(lst2)
# print(2. sorted(lst))

idx = 0

while idx < N:
    s = lst[idx][0]
    e = lst[idx][1]
    print(s, e)
    while idx < N and e > lst[idx][0]: # 안 되는 경우의 조건, 종료시간보다 시간시간이 빠른 경우
        idx += 1


