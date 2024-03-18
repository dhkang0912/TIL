import sys
sys.stdin = open("5204_input.txt","r")

def Merge(left, right):
    global cnt
    New_lst = []
    lp = 0
    rp = 0

    if left[-1] > right[-1]:
        cnt += 1

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            New_lst.append(left[lp])
            lp += 1
        else:
            New_lst.append(right[rp])
            rp += 1


    New_lst.extend(left[lp:])
    New_lst.extend(right[rp:])

    return New_lst



def Merge_Sort(lst):
    if len(lst) <= 1:
        return lst # 가장 깊이 들어간 요소가 1개만 남은 lst를 반환하는 경우

    mid = len(lst)//2
    left = Merge_Sort(lst[:mid]) # 왼쪽 => 미만이라 오른쪽은 mid부터 시작
    right = Merge_Sort(lst[mid:])
    New_lst = Merge(left, right)

    return New_lst # 정렬된 리스트를 반환해야 함

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))

    cnt = 0
    sorted_N_lst = Merge_Sort(N_lst)
    # print(sorted_N_lst)
    print(f'#{tc} {sorted_N_lst[N//2]} {cnt}')
