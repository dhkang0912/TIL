N = int(input())
lst = [input() for _ in range(N)]
lst = list(set(lst))
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
# print(lst)
