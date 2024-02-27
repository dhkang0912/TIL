# def KFC(x):
#     KFC(x+1)
#
# KFC(0)
# print('끝')

# def print_x(x):
#     if x == 3:
#         return
#     print_x(x+1)
#     print(x, end = ' ')
#     print_x(x + 1)
#     print(x, end = ' ')
#
# print_x(0)

# def print_x(x):
#     if x == 3:
#         return
#     for i in range(2):
#         print_x(x+1)
#         print(x, end = ' ')
#
# print_x(0)

# def print_X(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         if not used[i]:
#             path.append(i)
#             print_X(x+1)
#             path.pop()
#             used[i] = 0
#
# used = [0] * 6 # branch의 갯수만큼 used 배열을 초기화
# path = []
# print_X(0)
#
#
# def print_X(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         if used[i] == True: continue
#         path.append(i)
#         print_X(x+1)
#         path.pop()
#         used[i] = 0

# used = [0] * 6 # branch의 갯수만큼 used 배열을 초기화
# path = []
# print_X(0)



def type1(x): # 중복 순열
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        type1(x+1)
        path.pop()

# used = [0] * 7 # branch의 갯수만큼 used 배열을 초기화
# path = []
# perm(1)

def type2(x): # 순열
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        if used[i] == 0:
            path.append(i)
            used[i] = 1
            type2(x+1)
            path.pop()
            used[i] = 0


N, Type = map(int, input().split())

used = [0] * 7 # branch의 갯수만큼 used 배열을 초기화
path = []

if Type == 1:
    type1(0)
else:
    type2(0)
