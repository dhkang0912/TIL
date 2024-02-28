import sys
sys.stdin = open("5202_input.txt", "r")


T = int(input())
T = 1
for tc in range(1, T+1):
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    # print(containers)
    # print(trucks)