import sys
sys.stdin = open("5202_input.txt", "r")


T = int(input())
T = 1
for tc in range(1, T+1):
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    N = len(trucks)
    # print(containers)
    # print(trucks)
    container_weight = containers[0]
    idx = 0
    while idx <= N-1:
        if trucks[idx] >= container_weight:
            idx += 1
            containers_weight = containers[idx]
        else:
            idx += 1

