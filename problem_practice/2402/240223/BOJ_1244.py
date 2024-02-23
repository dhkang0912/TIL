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
        start = switch_info - 1
        end = switch_info + 1

        max_cnt = 0
        max_start = 0
        max_end = 0

        while start >= 1 and end <= switch_num:
            cnt = 0
            if switch_lst[start] == switch_lst[end]:
                for i in range(len(switch_lst[start:end+1])):
                    if switch_lst[start + i] == 1:
                        cnt += 1
                    if max_cnt < cnt:
                        max_cnt = cnt
                        max_start = start+i
            else:
                break
            start -= 1
            end += 1

        if max_start == 0:
            change(switch_info)
        else:
            for i in range(max_start, max_end+1):
                change(i)


print(*switch_lst[1:])