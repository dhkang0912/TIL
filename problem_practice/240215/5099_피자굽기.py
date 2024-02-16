import sys
sys.stdin = open("5099_input.txt", "r")


# SSAFY code
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 화덕의 크기, M = 피자의 갯수
    Ci = [0] + list(map(int, input().split())) # 피자의 치즈양
    pan = [0] * N
    nextPizzNo = 1
    while pan:
        pizzNo = pan.pop(0)
        # 치즈의 양을 1/2로 감소
        Ci[pizzNo]//=2
        if Ci[pizzNo] == 0:
            if nextPizzNo <= M: #남은 피자가 있다면:
                pan.append(nextPizzNo)
                nextPizzNo += 1
        else:
            pan.append(pizzNo)

    print(f'#{tc} {pizzNo}')




'''
    pizza = [0]+[5,3,1,2]
    oven = [0]*N
    nextPizzaNo = 1
    while oven :
        pizzaNo = oven.pop(0)
        oven.pop(0)//2
        if 치즈량이 0이라면 :
            -새 피자가 있으면 새 피자를 oven에, nextPizzaNo += 1
            -새 피자가 없으면 그대로 유지(oven의 크기가 줄어듦)
        else :
            -pizzaNo를 다시 oven에(oven.append(pizzaNo))
    print(pizzaNo)
'''

# Home study

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N = 화덕의 크기, M = 피자의 갯수
#     pizzas = list(map(int, input().split()))
#     pizza_idx = [i for i in range(N, M)]
#     ovens = [j for j in range(N)]
#
#     while len(ovens) > 1:
#         for i in range(len(ovens)):
#             if pizza_idx and pizzas[ovens[i]] == 0 :
#                 ovens[i] = pizza_idx.pop(0)
#             elif not pizza_idx and pizzas[ovens[i]] == 0:
#                 ovens.pop(i)
#             else:
#                 pizzas[ovens[i]] = pizzas[ovens[i]] // 2
#     print(ovens)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 화덕의 크기, M = 피자의 갯수
    cheese_amount = list(map(int, input().split()))
    pizza_idx = [i for i in range(N, M)]
    ovens = [j for j in range(N)]
    next_pizza_idx = N

    # print(cheese_amount)
    # print(pizza_idx)
    # print(ovens)

    while len(ovens)>1:
        current_pizza_idx = ovens.pop(0)
        cheese_amount[current_pizza_idx] //= 2
        if cheese_amount[current_pizza_idx] == 0:
            if pizza_idx:
                ovens.append(pizza_idx.pop(0))
            elif not pizza_idx:
                continue
        else:
            ovens.append(current_pizza_idx)

    print(f'#{tc}', ovens[-1]+1)

# 쌤 코드
    # T = int(input())
    # for tc in range(1, T + 1):
    #     N, M = map(int, input().split())
    #     pizza = [0] + list(map(int, input().split()))
    #
    #     oven = [0] * N  # 0번 피자 다 넣기(미리 안 넣어놓고 다 녹은 치즈 상태의 피자 넣어놓기)
    #     nextPizzaNo = 1
    #     while oven:
    #         pizzaNo = oven.pop(0)
    #         # cheese = pizza[pizzaNo]//2
    #         pizza[pizzaNo] //= 2
    #         if pizza[pizzaNo] == 0:
    #             if nextPizzaNo <= M:  # 남은 피자가 있으면
    #                 oven.append(nextPizzaNo)
    #                 nextPizzaNo += 1
    #
    #             # 새 피자가 없으면 그대로 유지(oven의 크기가 줄어듦)
    #         else:
    #             # pizzaNo를 다시 oven에
    #             oven.append(pizzaNo)
    #     print(f'{tc} {pizzaNo}')








