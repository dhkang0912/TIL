# 16811. 당근 포장하기
# 문제 이해
# N개의 당근을 주문
# 대 -> 중 -> 소 로 구분해 포장
#     -> 같은 크기의 당근은 같은 상자에 들어있어야 함
#     -> 대중소를 구분하는 기준이 뭐지?
#     -> 합계를 3으로 나눠서 대략적 구간을 나눠야 하나? (x)
#     -> 아니면 오름차순 후 각 갯수만큼 카운팅 정렬을 해서 빼와야 하나?
#     -> 이 방식 괜찮은 것 같은데?
#     -> 같은 것들은 같은 곳에 넣고 나머지는 어떤식으로 넣어야지...?
#     -> 각 한개씩 있는 경우는 각자 그냥 3으로 나눠서 몫만큼 넣고 한군데에 더 많이 넣으면 됨 -> 나머지가 차이일 것
#     -> 각 여러개 있는 경우 앞 순서부터 같은 숫자는 소 안에 넣기
#         -> 이때 만약 갯수가 N//2를 넘기어간다면 0
#         -> 그렇지 않다면 몇개를 넣어줘야 하는거지? N//3만큼 넣어주기?
#     -> 이후 중에도 여기도 같은 것만큼 갯수 넣어주는데
#         -> 이때 만약 갯수가 N//2를 넘어간다면 0
#         -> N-소//2만큼 넣어주기
#     -> 이후 여기도 같은 것만큼 갯수 넣어주
# 한 상자에 N//2 개를 초과하는 당근이 있으면 안됨
#     -> 한 상자에 몰리면 안됨
#     -> 비어있는 상자가 있으면 안됨
#
# 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 함
# 개수 차이를 기록
#
# 당근의 크기를 입력하면 조건을 확인
# => 포장할 수 없으면 -1
# => 포장할 수 있으면 당근 개수 차이가 최소일 때 차이값
#
# 아니 뭘 어떻게 하라는건지 자체를 모르겠는데...?
#
#
# 인풋
# 수확횟수 T가 주어짐 -> tc
# 당근의 갯수 N이 주어짐
# 수확한 N개의 당근 크기가 주어짐

import sys
sys.stdin = open("16811_input.txt", "r")

def carrot_counting(carrots, N):
    large = []
    middle = []
    small = []

    maxv = 0
    # 선택 정렬을 사용하여 당근을 오름차순으로 정렬
    for i in range(N):
        minv = carrots[i]
        minp = i
        maxv = carrots[i]
        for j in range(i, N):
            if minv > carrots[j]:
                minv = carrots[j]
                minp = j
                carrots[j], carrots[minp] = carrots[minp], carrots[j]
            if maxv < carrots[j]:
                maxv = carrots[j]

    print(carrots)

    # 당근의 개수를 세는 counting 정렬 수
    carrots_num = [0]*(maxv+1)
    for carrot in carrots:
        carrots_num[carrot] += 1

    # 각 크기별로 나누어 리스트에 추가
    for i in range(1, len(carrots_num)):
        count = carrots_num[i]
        if 0 < count < N//3:
            small.extend([i]*count)
        elif 0 < count < N//2:
            middle.extend([i]*count)
        else:
            large.extend([i]*count)

    len(small), len(middle), len(large)
    max_len_of_boxes = len(small)
    min_len_of_boxes = len(small)
    for _ in range(3):
        if max_len_of_boxes < len(middle):
            max_len_of_boxes = len(middle)
        if max_len_of_boxes < len(large):
            max_len_of_boxes = len(large)
        if min_len_of_boxes > len(middle):
            min_len_of_boxes = len(middle)
        if min_len_of_boxes > len(large):
            min_len_of_boxes = len(large)

    # 어느 한 상자라도 비어있는 경우
    if (len(small) <= 0) or (len(middle) <= 0) or (len(large) <= 0):
        return -1
    elif (len(small) > N//2) or (len(middle) > N//2) or (len(large) > N//2):
        return -1
    else:
        max_len_of_boxes - min_len_of_boxes




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    print(carrot_counting(carrots, N))




