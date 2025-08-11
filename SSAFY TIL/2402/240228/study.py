# def KFC(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         if not used[i]:
#             path.append(i)
#             used[i] = 1
#             KFC(x+1)
#             path.pop()
#             used[i] = 0
#
# path = []
# used = [-1]+[0] * 6
# KFC(0)


'''
arr의 배열에서 꺼짐, 켜짐을 확인하고 싶어
-> 꺼짐 켜짐의 조합을 구하고 싶어 (중복 가능)
n 자리의 꺼짐, 켜짐 조합을 구함
n을 가지고 해

0~2^n:
0 = 000
1 = 001
2 = 010
3 = 011
4 = 100
5 = 101
6 = 110
7 = 111

0~n: why n on, off



1. n자리를 보면서 꺼짐 켜짐 조합을 만들거야
-> 어떻게 해?
비트연산자 가지고 n자리까지 확인
=> 2^n까지
마지막 자리가 켜졌는지 꺼졌는지 확인하고
확인 여부를 더해줌 
확인 후 자리를 밀어줌
'''

arr = ['A', 'B', 'C', 'D']
n = len(arr)

def binary_counting(s):
    # print(bin(s))
    for i in range(n):
        if s & 0b1:
            # print(i)
            print(arr[i], end = ' ')
        s >>= 1

for c in range(0, 1<<n):
    binary_counting(c)
    print()



