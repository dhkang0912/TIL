T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = input()
    count = []
    stack = []
    for i in range(N):
        if S[i] == '1':
            stack.append(S[i])
        if stack and (S[i] == '0' or i == N-1) :
            count.append(len(stack))
            stack.clear()

    print(f'#{tc} {max(count)}')

# s= '2B'
# # s = int(s,16)
# # print(s)
# result = ''
# for c in s:
#     result += format(int(c, 16), '04b')
# print(result)