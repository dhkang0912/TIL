'''
{}
add -> 이미 x가 있는 경우 무시, x를 넣는다
remove -> S에서 x를 제거한다, 없는 경우 무시
check -> x가 있으면 1을 없으면 0
toggle -> x가 있으면 x를 제거하고 없으면 x추가
all -> ???
empty -> clear S

26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

'''
import sys
input = sys.stdin.readline

def make_set(order):
    global my_set
    if len(order) >= 2:
        order, n = order
        n = int(n)
        if order == 'add':
            my_set.add(n)

        elif order == 'remove':
            if n in my_set:
                my_set.remove(n)

        elif order == 'check':
            if n in my_set:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if n in my_set:
                my_set.remove(n)
            else:
                my_set.add(n)
    else:
        order = order[0]
        if order == 'all':
            # for i in range(1,21):
            #     my_set.add(i)
            my_set = set(range(1, 21))
        elif order == 'empty':
            my_set.clear()


my_set = set()
M = int(input())
for tc in range(M):
    order = input().strip().split()
    make_set(order)
