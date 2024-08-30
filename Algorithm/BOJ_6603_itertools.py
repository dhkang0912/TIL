# itertools 최고야!
from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    k = lst.pop(0)
    if k == 0:
        break
    else:
       for i in combinations(lst,6):
           print(*i)
    
       print()