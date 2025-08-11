# import sys
# sys.stdin = open("1240_input.txt", "r")
'''
각 숫자의 이진수를 딕셔너리에 저장하고 7개씩 순회하면서 값을 읽어옴
ARR[row].index('1')
ARR[row][::-1].index('1')
'''
def my_sum(numbers):
    last = 0
    for num in numbers:
        last += num
    return last

T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 행, M은 열
    # 우선 arr을 문자열로 한 행으 받기
    arr = ''
    for num in range(N):
        arr += input()

    # 뒤집어서 저장
    # print(arr)
    arr = arr[::-1]
    # print(arr)

    # 처음으로 1이 발견된 곳을 찾아 그곳부터 7개를 추출하기
    idx = 0
    while idx < len(arr):
        if arr[idx] == '1':
            tem = arr[idx : idx+56][::-1]
            break
        else:
            idx += 1

    # print(tem)

    # 7개 단위로 딕셔너리에서 같은 것을 확인하여 저장
    code = {'0001101':'0', '0011001':'1',
            '0010011':'2', '0111101':'3',
            '0100011':'4', '0110001':'5',
            '0101111':'6', '0111011':'7',
            '0110111':'8', '0001011':'9'
            }
    result = []
    for i in range(0,len(tem),7):
        result.append(code[tem[i:i+7]])


    # print(result)
    result = list(map(int, result))
    answer = 0
    for i in range(0, len(result), 2):
        answer += ((result[i]*3) + result[i+1])

    if answer % 10 == 0:
        print(f'#{tc} {my_sum(result)}')
    else:
        print(f'#{tc}', 0)






