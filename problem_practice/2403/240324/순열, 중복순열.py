# '''
# 주사위 2개 던져서 나올 수 있는 순열, 중복 순열
# branch = 1~6
# level = 2
# '''
# def type1(level, path):
#     if level==N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         if not visited[i]:
#             visited[i] = 1
#             type1(level+1, path+f' {i}')
#             visited[i] = 0
#
# def type2(level, path):
#     if level==N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         type2(level+1, path+f' {i}')
#
# visited = [0] * 7
# N=4
# type1(0, '')
# print()
# type2(0, '')
n = 3
arr= ['A', 'B', 'C']
def binary_counting(s):
    cnt = 0
    for i in range(n):
        if s & 1:
            cnt+=1
            # print(arr[i], end='')
        s>>=1
    return cnt

result = 0
# for s in range(1 << n):
#     print('{', end='')
#     binary_counting(s)
#     print('}', end='')

for s in range(1 << n):
    if binary_counting(s) >= 2:
        result += 1
print(result)


