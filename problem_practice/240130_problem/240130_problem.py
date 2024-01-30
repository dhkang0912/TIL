# DATA = [0, 4, 1(1), 3, 1(2), 2, 4, 1(3)]
# TEMP = [0, 1(1), 1(2), 1(3), 2, 3, 4, 4]

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# TEMP = [0, 1, 1, 1, 2, 3, 4, 4]
K = 4 # DATA에 있는 것 중 가장 큰 값 + 1
N = len(DATA) # DATA의 길이
COUNTS = [0] * (K+1)
for d in DATA :
    COUNTS[d] += 1

# print(COUNTS)
for i in range(1, K+1) :
    COUNTS[i] =  COUNTS[i] + COUNTS[i-1]

TEMP = [-1] * N
# for d in DATA[::-1] :
for i in range(N-1, -1, -1) :
    d = DATA[i]
    idx = COUNTS[d] - 1
    TEMP[idx] = d
    COUNTS[d] -= 1

print(TEMP)


numbers = [0, 1 ,2]
for i in range(3):
    for j in range(3) :
        if j == i :
            continue
        for k in range(3) :
            if k == i or k == j :
                continue
            print(i, j, k, '=>', numbers[i], numbers[j], numbers[k])



# i = 0
# tri = run = 0
# while i < 10 :
#     if c[i] >= 3: # triplete 조사 후 데이터 삭제
#         c[i] -= 3
#         tri += 1
#         continue;
#     if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1 : #run 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i + 1] -=1
#         c[i + 2] -=1
#         run += 1
#         continue
#         i += 1
#     if run + tri == 2:
#         print("Baby Gin")
#     else: print("Lose")


#<baby-gin>

N=6
def babygin(n_numbers):
    counts =[0]*12

    for _ in range(6) :
        #d = n_numbers%10
        counts[n_numbers%10] += 1
        n_numbers //= 10

    print(counts)

# def babygin(s_numbers):
#     counts =[0]*12
#     numbers = list(map(int, s_numbers))
#     for n in numbers :
#         counts[n] += 1
#     print(s_numbers, counts)

    n_tri = 0
    n_run = 0
    i = 0
    while i < 10 :
    #tri
        if counts[i] >= 3 :
            n_tri += 1
            counts[i] -= 3
            continue

    #run
        if i <=7 and (counts[i]>0 and counts[i+1]>0 and counts[i+2]>0) :
            n_run += 1
            counts[i] -=1
            counts[i+1] -= 1
            counts[i+2] -= 1

        i += 1
    print(n_tri, n_run)
    return

# babygin('445678')
# babygin('475432')
babygin(475432)
