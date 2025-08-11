import sys
sys.stdin = open("1220_input.txt", "r")

'''
교착 상태일 때 count를 증가시킴
여러개 붙어도 하나의 교착상태 => count += 1

위에서 아래로 검사 => 열검사
첫번째 A부터 검사를 시작함
A -> B를 발견할 때마다 교착 상태가 point가 됨

첫번째 row에 빨간색인 게 유의미함 => A
서로 다른 거면 교착 상태
이미 교착상태인데 다른 게 나와서 교착해도 의미없음 1개로 카운트 함

비어있는 게 있고 없고가 차이가 큼

마지막 row에 파란색인게 유의미함 => B

어떻게 아래와 같이 하면 중복되는게 걸러지지?
의문
'''

# # 열검사 함수
# def get_sero_cnt():
#     cnt = 0
#     # red 자성체를 체크
#     is_red = False
#
#     for row in range(N):
#         # 1. red 자성체 발견
#         if arr[row][col] ==1:
#             is_red = True
#         # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt +=1
#         elif is_red and arr[row][col] == 2:
#             cnt += 1
#             is_red = False # 갱신
#
#     return cnt
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     total_cnt = 0
#     # 열 순회하면서 total_cnt 누적
#     for col in range(N):
#         total_cnt += get_sero_cnt(col)
#     print(f'#{tc} {total_cnt}')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for col in range(N):
        is_red = False
        for row in range(N):
            if arr[row][col] == 1:
                is_red = True
            elif arr[row][col] == 2:
                if is_red == True:
                    cnt += 1
                    is_red = False

    print(f'#{tc} {cnt}')