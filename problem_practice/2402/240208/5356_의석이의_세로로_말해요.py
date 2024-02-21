# 5356_의석이의 세로로 말해요
# 내가 의석이와의 기싸움에서 이길 수 있을까?
# 코딩은 기세니까 시비 걸며 가보겠어

# A~Z까지, a~z, 0~9까지 받아다가 세로로 읽는데
# 왼쪽에어 오른쪽으로 읽음 중간에 없으면 다음 글자를 읽음
# 각 줄은 row는 5줄로 이뤄짐
# col은 15줄까지 가

'''
2
ABCDE (0,0) (0,1) (0,2) -> col 고정 row 변경
abcde (1,0) (1,1) (1,2)
01234 (2,0) (2,1) (2,2)
FGHIJ (3,0) (3,1) (3,2)
fghij (4,0) (4,1) (4,2)
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

import sys
sys.stdin = open("5356_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    result = ""

    for col in range(16):
        for row in range(5):
            if col < len(arr[row]):
                result += arr[row][col]

    print(f'#{tc}',result)






