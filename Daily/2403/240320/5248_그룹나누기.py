# def union(x, y):
#     idx1 = find_set(x)
#     idx2 = find_set(y)
#
#     if idx1 == idx2 :
#         return
#     if idx1 < idx2 :
#         rep[idx2] = idx1
#     else :
#         rep[idx1] = idx2


def union(x,y) :
    x = find_set(x)
    y = find_set(y)

    if x == y :
        return

    if x < y :
        rep[y] = x
    else :
        rep[x] = y

def find_set(idx):
    if rep[idx] == idx :
        return idx
    return find_set(rep[idx])

# def make_set(idx) :
#     rep[idx] = idx
#     return rep


T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    rep = [i for i in range(N)]



    for idx in range(0, len(numbers), 2) :
        union(numbers[idx]-1, numbers[idx+1]-1)
    # print(rep)

    result = []
    for x in rep :
        result.append(find_set(x))
    print(f'#{tc} {len(set(result))}')
