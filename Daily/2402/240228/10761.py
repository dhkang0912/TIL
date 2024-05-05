# T = int(input())
# for tc in range(1, T+1):
#     lst = input().split()
#
#     N = int(lst[0])
#     robot, x = lst[1], int(lst[2])
#     pre_robot = robot
#     pos = {'B':1, '0':1}
#     pre_time = x
#     pos[robot] = x
#     total = x
#
#     for i in range(1, len(lst), 2):
#         robot, x = lst[i], int(lst[i+1])
#         if pre_robot == robot:
#             time = abs(x-pos[robot]) + 1
#             total += time
#
#             pre_time += time
#             pre_robot = robot
#             pos[robot] = x
#         else:
#             time = abs(x- [pos[robot]])
#             if time < pre_time:
#                 time = 1
#             else:
#                 time = time - pre_time + 1
#             pre_time =time


T = int(input())
for tc in range(1, T+1):
    lst = input().split()

    N = int(lst[0])
    robot, x = lst[1], int(lst[2])
    pre_robot = robot
    pos = {'B':1, 'O':1}
    pre_time = x
    pos[robot] = x
    total = x

    for i in range(3, len(lst), 2):
        robot, x = lst[i], int(lst[i+1])
        if pre_robot == robot:
            time = abs(x-pos[robot]) + 1
            pre_time += time
        else:
            time = abs(x- pos[robot])
            if time < pre_time:
                time = 1
            else:
                time = time - pre_time + 1
            pre_time = time
        pre_robot = robot
        pos[robot] = x
        total += time
    print(f'#{tc} {total}')

# 3
# 4 B 2 O 1 O 2 B 4
# 3 B 5 B 8 O 100
# 2 O 2 O 1