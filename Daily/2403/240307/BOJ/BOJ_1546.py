'''
세준 점수 조작 사건?ㅋㅋㅋ
자기 점수 중 최댓값을 고름 = M
점수/최댓값*100이 새로운 점수
인풋 잘 확인하자
'''

N = int(input())
lst = list(map(int, input().split()))
New_lst = []
# print(lst)
for num in lst:
    cal_num = num/max(lst)*100
    New_lst.append(cal_num)

print(sum(New_lst)/len(New_lst))