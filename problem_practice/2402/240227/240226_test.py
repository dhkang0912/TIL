'''

3
5 1
0 0 0 0 0
2 2 1
5 1
0 1 0 0 0
2 3 2
10 4
0 1 1 0 0 1 0 1 0 1
3 2 1
5 3 2
4 4 3
8 4 1

'''

def do_1(st, j):
    for idx in range(st, st+j):
        if idx < N:
            rocks[idx] = (rocks[idx]+1) % 2


def do_2(st, j):
    color = rocks[st]
    for idx in range(st, st+j):
        if idx < N:
            rocks[idx] = color

def do_3(st, j):
    s = st-1
    e = st+1
    for cnt in range(1, j):
        if s >= 0 and e<N and rocks[s] == rocks[e]:
            rocks[s] = (rocks[s] + 1) % 2
            rocks[e] = (rocks[e] + 1) % 2
        s -= 1
        e += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))

    for _ in range(M):
        i, j, w = map(int, input().split())

        i -= 1
        if w == 1:
            do_1(i, j)
        elif w == 2:
            do_2(i, j)
        else:
            do_3(i, j)

    print(f'#{tc}', *rocks)
