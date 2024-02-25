import sys
sys.stdin = open("5099_input (1).txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    # print(cheese)

    pizza_idx = [i for i in range(N, M)]
    # print(pizza_idx)
    ovens = [j for j in range(N)]
    # print(ovens)

    while len(ovens) > 1:
        current_pizza_idx = ovens.pop(0)
        cheese[current_pizza_idx] //= 2
        if cheese[current_pizza_idx] == 0:
            if pizza_idx:
                ovens.append(pizza_idx.pop(0))
        else:
            ovens.append(current_pizza_idx)

    print(f'#{tc} {ovens[0]+1}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N = 화덕의 크기, M = 피자의 갯수
#     cheese_amount = list(map(int, input().split()))
#     pizza_idx = [i for i in range(N, M)]
#     ovens = [j for j in range(N)]
#     next_pizza_idx = N
#
#     # print(cheese_amount)
#     # print(pizza_idx)
#     # print(ovens)
#
#     while len(ovens)>1:
#         current_pizza_idx = ovens.pop(0)
#         cheese_amount[current_pizza_idx] //= 2
#         if cheese_amount[current_pizza_idx] == 0:
#             if pizza_idx:
#                 ovens.append(pizza_idx.pop(0))
#             elif not pizza_idx:
#                 continue
#         else:
#             ovens.append(current_pizza_idx)
#
#     print(f'#{tc}', ovens[-1]+1)
#
