import sys
input = sys.stdin.readline

# sort 사용하
# N = int(input())
# lst = [0]*N
# for i in range(N):
#     j = int(input())
#     lst[i]=j
# lst.sort()
# # print(lst)
#
# for z in lst:
#     print(z)기

# 버블정렬 사용하기
# N = int(input())
# lst = []
# for _ in range(N):
#     lst.append(int(input()))
#
# # 버블 정렬은 젤 앞에꺼를 다음꺼랑 비교해서 앞에꺼가 더 크면 자리 바꿔주기 다음 자리랑 계속 반복, 마지막 자리는 안 해줘도 됨
# # 바보 이렇게 하면 딱 한번만 돼서 맨 뒷자리만 정해짐
# # 이중 for문이 필요
# for j in range(len(lst), 0, -1):
#     for i in range(N-1):
#         if lst[i] > lst[i+1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]


# print(lst)

# 선택정렬 사용하기
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

# 가장 작은 걸 맨 앞으로 가져옴
for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

for z in lst:
    print(z)