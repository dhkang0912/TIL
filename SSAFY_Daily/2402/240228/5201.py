# import sys
# sys.stdin = open("5202_input.txt", "r")

'''

'''

T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 컨테이너의 수, M = 트럭의 수
    containers = list(map(int, input().split())) # 개당 컨테이너의 무게
    trucks = list(map(int, input().split())) # 한 트럭 싣을 수 있는 무게
    # print(containers)
    # print(trucks)

    # 컨테이너, 트럭 모두 무거운 순으로 정렬 => 내림차순
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    # print(containers)
    # print(trucks)
    '''
    [5, 3, 1]
    [8, 3]
    컨테이너의 무게와 트럭의 무게를 비교
    1) 만약 트럭의 무게가 컨테이너의 무게보다 크다면 싣을 수 있음
        총 화물 수에 누적해줌
        그렇다면 비교할 컨테이너 무게를 다음 걸로 바꿔주고 
        트럭도 다음 트럭으로 바꿔줌  
    2) 그렇지 않다면
        비교해야할 컨테이너의 무게는 그대로지만 트럭의 무게는 다음걸로 바꿔줌  
        => 이게 반대임 오히려 트럭이 고정되어야 함
    '''

    result = 0
    truck_weight = trucks[0]
    truck_idx = 0
    container_idx = 0
    # print(N, M)
    while container_idx <= N-1 and truck_idx <= M-1:
        if trucks[truck_idx] >= containers[container_idx]:
            result += containers[container_idx]
            truck_idx += 1
        container_idx += 1


    print(f'#{tc} {result}')

