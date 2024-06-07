'''
도감에 있는 포켓몬의 개수 N
내가 맞춰야 하는 문제의 개수 M

포켓몬 영어 이름들이 있음
첫글자는 대문자 나머지는 소문자
마지막 문자가 대문자일수도 있고 아닐 수도 있음

맞춰야 하는 M개의 포켓몬

다 받아서 N개까지 돌면서 pop해서 다른 리스트에 하나씩 넣기 인덱스는 1번부터로
그리고 나머지 남은 애들은 숫자면 해당 인덱스번째 값을 뽑고 문자면 find 써서 인덱스 찾아오면 되지 않을까...?

-> 어차피 N, M으로 도감의 개수를 받기 때문에 그냥 N번 M번 돌리면 됨 인덱스로 가능
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 도감의 수 = N, 맞춰야 하는 문제 수 = M
# print(N, M)

# 시간 초과 -> append가 아니라 index 할당 방식으로 변경
# 도감을 넣을 빈리스트 생성, 인덱스를 1번부터 사용하기 위해 0번째 임의의 값을 넣고 시작
int_dic_lst = {}
str_dic_lst = {}

for i in range(1, N+1):
    # 도감 내용 수인 N번 반복하면서 도감 완성
    S = input().strip()
    int_dic_lst[i] = S
    str_dic_lst[S] = i
    # dic_lst[i] = [input().strip(), i]

# print(int_dic_lst)
# print(str_dic_lst)


# def S_index(S):
#     for key, value in dic_lst.items():
#         if value == S:
#             print(key)


# 내가 맞춰야 하는 문제를 출력
for _ in range(M):
    # input이 문자열인지 숫자인지 확인이 되지 않으니 우선 문자열로 받기
    S = input().strip()

    # 받은 S가 숫자열이면 해당 인덱스의 값을 인쇄 -> 이미 문자열로 받았는데 이게 되나? 일단 해보지 뭐
    if S.isdigit():
        S = int(S)
        print(int_dic_lst.get(S))
    else: # 문자열이면 해당 인덱스를 인쇄
        print(str_dic_lst.get(S))

