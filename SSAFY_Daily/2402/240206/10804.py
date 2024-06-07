# 문자열 bdpq
# 거울에 비친 것처럼 나타내기 -> 역순 + bdpq -> dbqp로 바뀜

# 첫줄에 테스트 케이스 수가 주어짐
# 역순으로 바꾸고 해당 글자를 바꿔주기
# 딕셔너리로 지정해서 값만 바꾸면 되는 거 아닐까...?

# T = int(input())
# for tc in range(1, T+1):
#     origin_list = list(map(str,input()))
#     change_dict = {'b' : 'd', 'd' : 'b', 'q' : 'p', 'p' : 'q'}
#     origin_list = origin_list[::-1]
#     print(origin_list)
#
#     for i in range(len(origin_list)):
#         for key in change_dict.keys():
#             if origin_list[i] == key:
#                 origin_list[i] = change_dict[key]
#                 break
#     print(f'#{tc}', *''.join(origin_list))
#
# T = int(input())
# for tc in range(1, T + 1):
#     origin_list = list(map(str, input()))
#     change_dict = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'}
#     origin_list = origin_list[::-1]
#     result = ''
#     for i in range(len(origin_list)):
#         result += change_dict[origin_list[i]]
#     print(f'#{tc}', result)
