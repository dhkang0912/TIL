import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_heard = {}
not_seen = {}
all_lst = [-1] * (N+M)

for i in range(N):
    S = input().strip()
    not_heard[S] = i
    all_lst[i] = S

for i in range(M):
    S = input().strip()
    not_seen[S] = i
    all_lst[i] = S

both_lst = []
for i in range(N+M):
    S = all_lst[i]
    if not_heard.get(S) != None and not_seen.get(S) != None:
        both_lst.append(S)


print(len(both_lst))
both_lst.sort()
for S in both_lst:
    print(S)


