import sys
sys.stdin = open("5202_input.txt", "r")
'''
1. 문제를 이해해보자
회의실 문제와 같이 시작, 종료 시간을 통해서 배치하는 그리디 문제
종료 시간(time_list[0][1]]이 가장 이른 기준으로 선택하고 (IDX=0)
다음 시작 시간(time_list[1][0]]이 종료시간과 같거나 크면 CNT +=1하고
종료 시간을 해당 종료 시작으로 변경 = time_list[1][1]
그 다음 IDX의 시작 시간과 비교
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 화물차의 수
    time_list = []
    for _ in range(N):
        s, e = map(int, input().split())
        time_list.append([s, e]) #시작시간과, 종료 시간을 묶어서 append
    # print(time_list) # 묶어서 넣기는 함

    time_list.sort(key = lambda x:x[1])
    # print(time_list) # lambda를 통해서 종료 시간을 기준으로 오름차순으로 변경 (작은 수 -> 큰 수)
    end_time = 0
    idx = 0
    cnt = 0

    while idx <= N-1:
        if end_time <= time_list[idx][0]:
            end_time = time_list[idx][1]
            cnt += 1
        idx += 1

    print(f'#{tc} {cnt}')