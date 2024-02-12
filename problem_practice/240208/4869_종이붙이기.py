# 4869_종이 붙이
# https://hyunse0.tistory.com/279기
# 와우 이런 식으로 표현할 수 있고 생각할 수 있다는게 신기할 따름...
# DP를 사용

# 논리
# import sys
# sys.stdin = open("4869_input.txt", "r")

# def paper_num(N):
#     memo = [0,1,3]
#
#     for i in range(3, N+1):
#         memo.append(memo[i-1] + (memo[i-2]*2))
#
#     return memo[N]

def paper_num(N):
    memo = [0]*(N+1)
    for i in range(N+1):
        if i ==0:
            memo[0] = 0
        elif i == 1:
            memo[1] = 1
        elif i == 2:
            memo[2] = 3
        else:
            memo[i] = memo[i-1] + (memo[i-2]*2)

    return memo[N]

# def paper(n):
#     lst = [1, 3]
#
#     for i in range(2, n):
#         lst.append(lst[i-1] + lst[i-2]*2)
#
#     return lst[n-1]


# 인풋
T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10

    print(f'#{tc}', paper_num(N))