'''
최대 공약수와 최소공배수를 출력
-> 이게 뭔말이더라?
유클리드 호제법이 중요하다...
'''
'''
N, M = map(int, input().split())
N_lst = []
M_lst = []

i = 2
while N>1 :
    if i >= 10:
        i = 2
    if N % i == 0:
        N_lst.append(i)
        N //= i
        i = 2
    else:
        i += 1

while M>1:
    if i >= 10:
        i = 2
    if M % i == 0:
        M_lst.append(i)
        M //= i
        i = 2
    else:
        i += 1


# print(N_lst, M_lst)




print(small)
print(large)
'''
N, M = map(int, input().split())
if N == M:
    print(N)
    print(M)
else:
    min_value = 1
    i = 2

    while i < max(N, M):
        if N % i == 0 and M % i == 0:
            N //= i
            M //= i
            min_value *= i
            i = 2
        else:
            i+=1

    max_value = min_value * N * M

    print(min_value)
    print(max_value)
