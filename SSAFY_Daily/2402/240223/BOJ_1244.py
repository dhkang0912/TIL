switch_num = int(input()) # 스위치의 총 갯수
switch_lst = [-1] + list(map(int, input().split())) # 스위치 온 오프 정보
student_num = int(input()) # 학생 수

def change(switch_info):
    global switch_lst
    if switch_lst[switch_info] == 1:
        switch_lst[switch_info] = 0
    # elif switch_lst[switch_info] == 0:
    else:
        switch_lst[switch_info] = 1


for tc in range(student_num):
    sex, switch_info = map(int, input().split()) # 성별, 스위치 정보

    if sex == 1 :
        for i in range(1, switch_num+1): #스위치 번호를 순회함
            if i % switch_info == 0:
                change(i)
    elif sex == 2:
        start = switch_info
        end = switch_info
        max_start = 0
        max_end = 0

        while start >= 1 and end <= switch_num:
            if switch_lst[start] == switch_lst[end]:
                max_start = start
                max_end = end
                start -= 1
                end += 1
            else:
                break

        for num in range(max_start,max_end+1):
            change(num)

# switch_lst = switch_lst[1:]
# print_num = 20
# start_idx = 0
# end_idx = start_idx+print_num
# while len(switch_lst) > 0:
#     if len(switch_lst) <= 20:
#         print(*switch_lst)
#     else:
#         print(*switch_lst[start:end_idx])
#         start_idx += 20
#         switch_lst = switch_lst[start_idx:end_idx]


for print_num in range(1, switch_num+1, 20):
    print(*switch_lst[print_num:print_num+20])
    if print_num % 20 == 0:
        print()