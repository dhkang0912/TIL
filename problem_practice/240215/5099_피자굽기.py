import sys
sys.stdin = open("5099_input.txt", "r")

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

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 화덕의 크기, M = 피자의 갯수
    pizzas = list(map(int, input().split()))
    pizza_idx = [i for i in range(N, M)]
    ovens = [j for j in range(N)]

    while len(ovens) > 1:
        for i in range(len(ovens)):
            if pizza_idx and pizzas[ovens[i]] == 0 :
                ovens[i] = pizza_idx.pop(0)
            elif not pizza_idx and pizzas[ovens[i]] == 0:
                ovens.pop(i)
            else:
                pizzas[ovens[i]] = pizzas[ovens[i]] // 2
    print(ovens)



