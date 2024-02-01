# 1954. 달팽이 숫자
# import sys
# sys.stdin = open("1954_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     print(f'#{tc}')
#     N = int(input()) # N*N 배열이라는 의미
#     arr = [[0] * N for _ in range(N)]
#
#     value = 0
#     d = 0
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     row = 0
#     col = 0
#
#     for _ in range(N*N) :
#         value += 1
#         arr[row][col] = value
#         row = row + dr[d]
#         col = col + dc[d]
#         if row < 0 or col < 0 or row > N-1 or col > N-1 or arr[row][col] != 0 :
#             row = row - dr[d]
#             col = col - dc[d]
#             d = (d+1)% 4
#             row = row + dr[d]
#             col = col + dc[d]
#
#
#     for new_row in range(N) :
#         for new_col in range(N) :
#             print(arr[new_row][new_col], end = ' ')
#         print()


# 1966. 숫자를 정렬하자
# import sys
# sys.stdin = open("4843_input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1) :
#     N = int(input()) # numbers의 갯수
#     numbers = list(map(int,input().split()))
#
#     for i in range(N-1) :
#         minV = numbers[i]
#         minP = i
#         for idx in range(i+1, N) :
#             if minV > numbers[idx] :
#                 minV = numbers[idx]
#                 minP = idx
#         numbers[i], numbers[minP] = numbers[minP], numbers[i]
#
#     print(f'#{tc}', *numbers)



#
