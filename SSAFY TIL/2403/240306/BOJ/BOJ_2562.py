lst = []
N = 9
for _ in range(N):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)