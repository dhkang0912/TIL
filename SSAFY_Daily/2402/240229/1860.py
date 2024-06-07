import sys
sys.stdin = open('1860_input.txt', "r")
'''
진기의 최고급 붕어빵
T 인풋 받기
N, M, K 인풋 받기
-> N명의 사람에게 판매, M초 단위로 K개의 붕어빵 생성
=> (각 사람이 오는 시간/만들 수 있는 초단위)*만들 수 있는 붕어빵의 수

한명 당 한개씩 판매
재고관리가 중요
'''

# def start():
#     sold_bread = 0
#     for person in customers:
#         # 공식, 특정시간에 만들 수 있는 빵의 개수
#         made_bread = (person // M) * K
#
#         # 빵을 1개 팔았다
#         sold_bread += 1
#
#         # 재고 계산
#         remain = made_bread - sold_bread
#
#         # 재고가 0보다 작으면 실패
#         if remain < 0:
#             return 'Impossible'
#
#         # 실패가 없었으면 성공
#         return 'Possible'
#
# T = int(input())
# for tc in range(1, T+1):
#     #손님 수 N, M초에 K개의 빵을 만든다. 손님들이 도착하는 시간 customer
#     N, M, K = map(int, input().split())
#     customers = list(map(int, input().split()))
#
#     customers.sort()
#     result = start()
#     print(f'#{tc} {result}')

'''
# 인풋
1. T를 인풋 받음
2. N, M, K를 인풋 받음 => N = 붕어빵을 사는 사람 수, M = 붕어빵 만드는 단위, K = 단위마다 생성하는 붕어빵 갯수
=> 1초마다 생성할 수 있는 붕어빵 갯수 = (K/M) = 시간마다 생성하는 붕어빵 갯수 / 붕어빵 만드는데 걸린 시간
    => 이렇게 하면 아직 만들 수 있는 시간 단위가 되지 못했는데 붕어빵을 만든 게 되어버림, 특정 시간 초가 지나야 생성되는 게 가능하여 틀림

=> 기다린 시간동안 만들 수 있는 시간 단위가 얼마나 들어있는가? 그 단위에 만들 수 있는 빵의 단위를 곱하면 됨
    (waiting_time//M)*K

# 로직
1. 팔 수 있는 지 판단할 기준인 재고관리가 필요 = 재고관리
2. 다음 손님이 올 때까지 만들 수 있는 붕어빵 갯수가 필요 = 만든 갯수
    => 만들어서 재고관리에 더해줌
3. 만약 재고가 0보다 크다면 팔 수 있는 상태
    => 다음으로 넘어감
    => 재고를 1 줄임
4. 만약 재고가 0보다 작거나 같으면 팔 수 없는 상태
    => impossible을 return
5. 모든 손님을 마주했지만 불가능한 적이 없다면 possible을 return함                              
'''
# def boong_sold():
#     remain = 0
#     for i in range(N):
#         boong_num = (waiting[i]//M)*K
#         remain += boong_num
#         if remain > 0:
#             remain -=1
#         else:
#             return 'Impossible'
#     return 'Possible'



T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N = 붕어빵을 사는 사람 수, M = 붕어빵 만드는 단위, K = 단위마다 생성하는 붕어빵 갯수
    waiting = list(map(int, input().split()))
    waiting.sort()
    # print(sec1_boong, waiting)

    result = 'Possible'
    for i in range(N):
        boog_num = (waiting[i] // M)*K # 나까지 오는 동안 생성되는 붕어빵 갯수
        if i+1 > boog_num:
            result = 'Impossible' #내 앞에 사간 사람이 더 많으면 불가능

    print(f'#{tc} {result}')