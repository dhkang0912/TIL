def calc_fuc(v, calc):
    if calc == '+1':
        w = v+1
        return w
    elif calc == '-1':
        w = v-1
        return w
    elif calc == '*2':
        w = v * 2
        return w
    else:
        w = v - 10
        return w

def bfs(s, e):
    global minv

    Q = [s]
    visited[s] = 1

    while Q:
        v = Q.pop(0)
        if v == e and visited[v] < minv:
            minv = visited[v]

        for calc in ['+1', '-1', '*2', '-10']:
            w = calc_fuc(v, calc)
            Q.append(w)
            visited[w] = visited[v]+1


T = int(input())
for tc in range(1, T+1):
    s, e = map(int, input().split())
    visited = [0] * 1000001
    minv = float('inf')
    bfs(s, e)

    print(minv)