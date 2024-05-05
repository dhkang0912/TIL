import sys
sys.stdin = open("1926_input.txt", "r")
N = int(input())  # 범위의 끝을 입력 받음
num_list = range(1, N+1)  # 1부터 N까지의 숫자 리스트를 생성
for num in num_list:  # 각 숫자에 대해
    str_num = str(num)  # 숫자를 문자열로 변환
    # 첫번째 방법
    game = [str_num.count('3'), str_num.count('6'), str_num.count('9')]  # 숫자에 3, 6, 9가 각각 몇 번 등장하는지 세어 리스트에 저장
    # 두번째 방법
    # repeat = 0
    # for s in s_num: #문자열을 앞에서부터 탐색
    #     if s in '369':
    #         repeat += 1
    # print('-' * repeat, end = ' ')

    if sum(game):  # 만약 3, 6, 9 중 하나라도 등장한다면
        print('-' * sum(game), end=' ')  # 등장한 횟수만큼 '-'를 출력
    else:  # 그렇지 않다면 (즉, 숫자에 3, 6, 9가 없다면)
        print(num, end=' ')  # 숫자를 출력

'''
1. 사용자로부터 정수 N을 입력 받습니다. 이 N은 숫자 리스트의 범위의 끝을 나타냅니다.
2. 1부터 N까지의 숫자 리스트를 생성합니다.
3. 각 숫자에 대해 다음 작업을 수행합니다:
   - 숫자를 문자열로 변환합니다.
   - 변환된 문자열에서 '3', '6', '9'의 등장 횟수를 세어 리스트에 저장합니다.
   - 만약 '3', '6', '9' 중 하나라도 등장한다면, 등장한 횟수만큼 '-'를 출력합니다.
   - 그렇지 않다면 (즉, 숫자에 '3', '6', '9'가 없다면), 숫자를 그대로 출력합니다.

이 코드는 3, 6, 9 게임을 구현한 것으로, 숫자에 3, 6, 9가 등장하는 횟수만큼 '-'를 출력하고, 그렇지 않다면 숫자를 그대로 출력.
이 작업은 문자열의 `count` 메서드를 사용하여 수행
'''

N = int(input())
print(N)
#1 1부터 N까지의 숫자 범위를...
# numbers = range(1, N)  # 끝점은 제외
numbers = list(range(1, N+1))  # 수정 가능하게...
# range(a) : 0부터 a 직전까지
# range(a, b) : a부터 b 직전까지
# range(a, b, c) : a부터 b 직전까지 c만큼 뛰어서
# print(numbers[0])  # range의 경우 인덱스를 통한 조회는 되는데
# numbers[0] += 1  # range는 수정불가
# print(numbers)
#2. 3, 6, 9 를 포함한 숫자들(원소들)을 변환 -, --...
# 3-2
answer = []  # result, answer 리스트
for number in numbers:
    # print(number)
    # if 3 in number:
    # 숫자를 자릿수단위로 연결된 문자열로 취급
    # if 3 in str(number):  # 문자열 내부에는 문자열 '3'인데
    s_num = str(number)
    if '3' in s_num or '6' in s_num or '9' in s_num:
        # 3이나 6이나 9를 포함하고 있는 숫자들...
        # print(number)  # 3, 6, 9 -> -
        # 1) 여러개의 369 판별
        repeat = 0
        # print('-', end=' ')  # '\n' -> ' '
        # repeat += s_num.count('3')
        # repeat += s_num.count('6')
        # repeat += s_num.count('9')
        # 2)
        for s in s_num:  # 문자열을 앞에서부터 한글자씩 탐색
            # 앞에 s가 뒤에 in 다음에 있는 문자열 또는 리스트에 포함?
            if s in '369':  # ['3', '6', '9']
                repeat += 1
        # if repeat > 0: <- 이걸로 위의 or을 대체 가능
        # print('-' * repeat, end=' ')
        answer.append('-' * repeat)
        # sep=' ', end='\n'
        # sep 여러개 넣었을 때 그 인자들 간의 사이에 들어갈 것
        # end print하고 끝에 뭘 뒤에 붙여줄지 (줄바꿈 문자)
    else: # 일반 숫자들
        # print(number, end=' ')
        answer.append(number)
        # answer.append(str(number))  # join을 쓰려면...

    # 3 출력하는 방법.
    # 3-1 print(v, end=' ')
# 3-2
# print(answer)
# 3-2-1
# print(' '.join(answer))  # '?' 합칠 때 기준이 되는 글자.join(문자열)
# print(' '.join(map(str, answer)))
# join할 때 숫자 섞이면 숫자 자체를 문자열로 추가하거나 append(str(num))
# 혹은 map하면 됨. -> str도 int처럼 쓸 수 있음.
# join을 하는 건 문자열들끼리만 가능. answer -> 그냥 들어가는 숫자들을 str하거나 map(str, ...)
# 3-2-2
print(*answer)  # 리스트 언패킹
# print는 변수로 가변인자를 받아요 -> 언패킹을 하면 각각 원소를 sep로 연결해서 출력
# print(f'{*answer}')  # f-string에서는 리스트 언패킹 안됨
print(f'{"".join(map(str,answer))}')
# f-string 안에서 스페이스 등으로 연결된 문구를 쓰고 싶다면 join을 써야함.
# 언패킹 2가지 상황 1: 변수 할당 2: 함수를 쓸 때
# f-string을 통한 텍스트 표현식 -> 함수도 아니고 할당도 아니에요...