# while True:
#     v1, v2, v3 = map(int, input().split())
#     if v1 == 0 and v2 == 0 and v3 == 0:
#         break
#     lst = [v1, v2, v3]
#     max_line_idx = lst.index(max(lst))
#     max_line = lst[max_line_idx]
#     lst.pop(max_line_idx)
#     if (lst[0]**2) + (lst[1]**2) == max_line**2:
#         print('right')
#     else:
#         print('wrong')

# sort를 쓰면
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    lst.sort()
    if (lst[0]**2) + (lst[1]**2) == lst[2]**2:
        print('right')
    else:
        print('wrong')