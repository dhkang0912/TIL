# 6485. 삼성시의 버스 노선
# 1<= Ai, Bi <= 5000이라면 -> Ai, Bi 모두 1이상 5000이하이지만 둘의 순서는 모르는 것
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     counts = [0]*5001 # 5000번 정류장까지 N개의 노선을 정류장에 표시
#     for i in range(N) :
#         A,B = map(int, input().split())
#         for j in range(A, B+1): # 1<=A<=B<=5000
#             counts[j] += 1
#     P = int(input())
#     busstop = [int(input()) for _ in range(N)]
#     print(f'#{tc+1}', end =' ')
#     for i in busstop : # 출력할 정류장 번호
#         print(counts[i], end=' ')
#     print()

# 1979. 어디에 단어가 들어갈 수 있을까
# 어디에 1
# K = 3
# N = 6+1
# arr = [0, 1, 0, 1, 1, 0]
# arr[-1] = 0
# ans = 0
# cnt = 0
# for i in range(N) :
#     if arr[i] == 0 :
#         if cnt == K:
#             ans += 1
#         cnt = 0
#     else :
#         cnt += 1
        # if i == N - 1 and cnt == K :
        #     ans += 1



# 어디에 2
'''
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''

# T =int(input())
# for tc in range(1, T+1) :
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) +[0] for _ in range(N)+[[0] *(N+1)]] # ???
#     # 가로 세로로 연속한 1의 개수가 K인 수
#     N += 1 # 0인 열과 행 추가
#     ans = 0
#     for j in range(N):
#         cnt = 0 # j열에서 연속한 1의 개수
#         for i in range(N):
#             if arr[i][j] :
#                 cnt += 1
#             else:
#                 if cnt == K :
#                     ans += 1
#                 cnt = 0
#
#     print(f'#{tc} {ans}')


# 16268 풍선팡2
# 풍선팡1
# T = int(input())
# for tc in range(1, T+1) :
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # dr = [1, -1, 0, 0]
#     # dc = [0, 0, 1, -1]
#     maxV = 0
#
#     for row in range(N) :
#         for col in range(N) :
#             # print(arr[row][col])
#             sumV = arr[row][col]
#             for dr, dc in [(1,0), (-1,0), (0, 1), (0, -1)] :
#                 for dd in range(1, arr[row][col]+1) :
#                     newR = row + dr * dd
#                     newC = col + dc * dd
#                     if 0 <= newR < N and 0 <= newC < M:
#                         sumV += arr[newR][newC]
#             if maxV < sumV :
#                 maxV = sumV
#     print(maxV)

# ---
# 민영 필기
#6485

# T = int(input())
# for tc in range(T):
#     N = int(input())
#     counts = [0]*5001 # 5000번 정류장까지
#     # N개의 노선을 정류장에 표시
#     for i in range(N) :
#         A,B = map(int, input().split())
#         for j in range(A, B+1): # 1<=A<=B<=5000
#             counts[j] += 1
#     P = int(input())
#     busstop = [int(input()) for _ in range(N)]
#     print(f'#{tc+1}', end =' ')
#     for i in busstop : # 출력할 정류장 번호
#         print(counts[i], end=' ')
#     print()
#
#
# #1979 문제 들어가기전 워밍업
# K = 3
# N = 7
# arr = [0,1,0,1,1,1,0]
# ans = 0
# cnt = 0
# for i in range(N) :
#     if arr[i] == 0 :
#         if cnt == K :
#             ans += 1
#         cnt = 0
#     else :
#         cnt += 1
#         if i == N - 1 and cnt == K :
#             ans += 1
#
# #1979
# T = int(input())
# for tc in range(T) :
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) + [0] for _ in range(N)] +[[0]*(N+1)]  # 행과 열에 0 추가
#     N += 1 #0인 열과 행 추가
#     #가로, 세로로 연속한 1개의 개수가 K인 경우의 수
#
#     ans = 0
#     for i in range(N) :
#         cnt = 0 # i행에서 연속한 1의 개수
#         for j in range(N) :
#             if arr[i][j] :  # 1이면
#                 cnt += 1
#             else : # 0이면
#                 if cnt == K :
#                     ans += 1
#                 cnt = 0
#     for j in range(N):
#         cnt = 0  # j열에서 연속한 1의 개수
#         for j in range(N):
#             if arr[i][j]:  # 1이면
#                 cnt += 1
#             else:  # 0이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
# #16268. 풍선팡2
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
#
#
# T = int(input())
# for tc in range(T) :
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     maxv= 0 # 최대 꽃가루 합계
#     for i in range(N) : # N*M 크기의 게임판
#         for j in range(M) :
#             cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
#
#             # 주변 풍선의 꽃가루
#             for k in range(4) : # 주변 풍선의 인덱스 ni, nj
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M :
#                     cnt += arr[ni][nj]
#             # 꽃가루를 최대값과 비교
#             if maxv < cnt :
#                 maxv = cnt
#     print(f'# {tc+1} {maxv}')
#
# #풍선팡
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
#
#
# T = int(input())
# for tc in range(T) :
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     maxv= 0 # 최대 꽃가루 합계
#     for i in range(N) : # N*M 크기의 게임판
#         for j in range(M) :
#             cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
#
#             # 주변 풍선의 꽃가루
#             for k in range(4) : # 주변 풍선의 인덱스 ni, nj
#                 for l in range(1, arr[i][j]+1)
    #                 ni = i + di[k] *l
    #                 nj = j + dj[k] *l
    #                 if 0 <= ni < N and 0 <= nj < M :
    #                     cnt += arr[ni][nj]
#             # 꽃가루를 최대값과 비교
#             if maxv < cnt :
#                 maxv = cnt
#     print(f'# {tc+1} {maxv}')


