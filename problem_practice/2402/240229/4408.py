'''
특징 1
1) 시작과 끝을 어디로 하던지 겹치는 것만 하려면 동일함
=> 시작을 모두 더 왼쪽으로 옮겨줌
=> 목적지 > 출발지

특징 2
1) 아랫 방 사람들이 윗방으로 모두 이주하더라도 정답 결과는 같음
=> 짝수 일 때는 시작 방과 끝 방을 모두 -1씩 해줌
'''
# def room_change(current_room, target_room):


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # N = 돌아가야 할 학생들의 수
#     room_info = []
#     pre_room = 0
#     for i in range(N):
#         current_room, target_room = map(int, input().split())
#         room_info.append((current_room, target_room))
#
#     # print(room_info)
#     room_info.sort()
#     print(room_info)


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N = 돌아가야 할 학생들의 수
    corridor = [0] * 400
    max_v = 0

    for _ in range(N):
        # 현재 방 s, 돌아갈 방 e
        s, e = map(int, input().split())

        # 특징 2번 아랫방을 윗방으로 변경
        if s % 2 == 0: s -=1
        if e % 2 == 0: e -=1

        # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swap
        if s > e: s, e = e, s #swap

        for i in range(s, e+1):
            corridor[i] += 1
            max_v = max(corridor[i], max_v)

        print(f'#{tc} {max_v}')




