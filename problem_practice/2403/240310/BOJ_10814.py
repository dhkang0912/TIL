import sys
input = sys.stdin.readline
N = int(input())
lst = []
# lst = [list(input().split()) for _ in range(N)]
for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst.append([age, name])

# 첫번째 열을 기준으로 정렬
lst.sort(key= lambda x:x[0])
print(lst)렬

# 기본 오름차순을 기준으로 정렬하기 때문에 첫번째 기준이 오름차순으로 동일하다면 다음 열이 오름차순으로 비교되어 정렬됨
lst.sort()
print(lst)

for j in lst:
    print(*j)

