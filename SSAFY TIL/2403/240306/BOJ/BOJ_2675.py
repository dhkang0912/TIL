T = int(input())
for tc in range(T):
    num, str = input().split()
    num = int(num)
    for num_ele in str:
        print(num_ele*num, end='')
    print()
