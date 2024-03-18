# import sys
# sys.stdin = open("5207_input.txt", "r")

def BinarySearch(target, start, end, check):
    # 찾지 못하고 문제가 되는 경우는 cnt를 안 하기 위해 0을 리턴함
    if start > end: # 시작과 끝이 교차가 되는 지점이 찾지 못하는 경우
        return 0

    mid = (start+end)//2 # 중간 인덱스를 찾아서 확인함
    if target == N_lst[mid]:
        return 1 # cnt를 나타내주기 위해 1을 리턴해줌, for 문 안에서 찾은 횟수 증가해줌
    
    # target과 동일하기 않아서 재귀함수를 타고 맞는 값을 찾을 때까지 N_lst를 돈다
    elif target > N_lst[mid]: # target이 중간값보다 오른쪽에 있다면, 오른쪽을 확인해줘야 함
        if check == 'left' or check == '':
            check = 'right'
            return BinarySearch(target, mid+1, end, check)

    elif target < N_lst[mid]: # target이 중간값보다 왼쪽에 있다면, 왼쪽을 확인해줘야 함
        if check == 'right' or check == '':
            check = 'left'
            return BinarySearch(target, start, mid-1, check)
    return 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_lst = list(map(int, input().split()))
    N_lst.sort()
    M_lst = list(map(int, input().split()))

    cnt = 0
    for target in M_lst:
        # 처음엔 N_lst의 모든 인덱스를 가져다가 함수에 넣어서 확인
        start = 0
        end = N - 1
        cnt += BinarySearch(target, start, end, '')

    print(f'#{tc} {cnt}')