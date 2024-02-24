#
# def incode_decode(num):
#     return num ^ code
#
# code = 1004
#
# print(incode_decode(1000))
# print(incode_decode(4))

# num = 1
# for i in range(5):
#     print(bin(num),num)
#     num = num << 1
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int,input().split())
#     t = bin(M)
#     t = list(t)
#     # print(t)
#     t = t[::-1][0:len(t)-2][0:N]
#     # print(t)
#     if '0' not in t:
#         print(f'#{tc} ON')
#     else:
#         print(f'#{tc} OFF')
#
# M = 31
# N = 5
# def Test():
#     tar = M
#     for i in range(N):
#         if tar & 0X1 == 0:
#             return False
#         tar = tar >>1
#     return True
# print(Test())

# print(0.1)
# print(f'{0.1:.25f}')

# def bitPrint(num):
#     for j in range(3, -1, -1):
#         if num & 1<<j:
#             print(1)
#         else:
#             print(0)
#
# bitPrint(5)
# print(bin(5))
#
# def decTobin(num):
#     s = ''
#     for j in range(3, -1, -1):
#         if num & 1<<j:
#             s += '1'
#         else:
#             s += '0'
#     return s
#
# print(decTobin(7))

def decTobin(num):
    s =''
    for j in range(3, -1, -1) :
        s += '1' if num&1 << j else '0'
    return s


print(decTobin(7))