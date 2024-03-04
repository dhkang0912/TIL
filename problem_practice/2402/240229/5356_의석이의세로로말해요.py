import sys
sys.stdin = open("5356_input.txt", "r")
'''
2
ABCDE
abcde
01234
FGHIJ
fghij

AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

T = int(input())
for tc in range(1, T+1):
    N = 5
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    result = ''
    len_info = []

    for idx in range(N):
        len_info.append(len(arr[idx]))
    max_len_info = max(len_info)


    for col in range(max_len_info):
        for row in range(N):
            if col < len(arr[row]):
                result += arr[row][col]

    print(f'#{tc} {result}')
