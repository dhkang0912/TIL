import sys
sys.stdin = open("4408_input.txt", "r")
'''
특징 1
1) 시작과 끝을 어디로 하던지 겹치는 것만 하려면 동일함
=> 시작을 모두 더 왼쪽으로 옮겨줌
=> 목적지 > 출발지

특징 2
1) 아랫 방 사람들이 윗방으로 모두 이주하더라도 정답 결과는 같음
=> 짝수 일 때는 시작 방과 끝 방을 모두 -1씩 해줌
'''

# 라이브 강의 쌤 코드
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # N = 돌아가야 할 학생들의 수
#     corridor = [0] * 400
#     max_v = 0
#
#     for _ in range(N):
#         # 현재 방 s, 돌아갈 방 e
#         s, e = map(int, input().split())
#
#         # 특징 2번 아랫방을 윗방으로 변경
#         if s % 2 == 0: s -=1
#         if e % 2 == 0: e -=1
#
#         # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swap
#         if s > e: s, e = e, s #swap
#
#         for i in range(s, e+1):
#             corridor[i] += 1
#             max_v = max(corridor[i], max_v)
#
#         print(f'#{tc} {max_v}')

# 내가 짠 코드
def change_idx(x):
    if x % 2 == 1: # 홀수이면
        return x // 2
    else:
        return x // 2 - 1

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N = 돌아가야 할 학생들의 수
    # 더 빠른 방 번호를 출발, 더 느린 방 번호를 도착으로 지정하여 방 정보를 저장
    room_info = [0] * N
    count_idx = [0] * 400
    for i in range(N):
        s, e = map(int, input().split())
        # 각 방의 홀수, 짝수 중 복도의 같은 영역을 쓰는 것끼리 같은 인덱스를 부여하는 함수
        s = change_idx(s)
        e = change_idx(e)
        if s <= e:
            room_info[i] = (s, e)
        else:
            s, e = e, s
            room_info[i] = (s, e)
    # print(room_info)

    for room in room_info:
        s, e = room
        for idx in range(s, e+1):
            count_idx[idx] += 1
    print(f'#{tc} {max(count_idx)}')







