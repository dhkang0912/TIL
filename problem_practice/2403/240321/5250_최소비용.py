'''
BFS는 인접한 영역끼리 가중치가 같아서 풀 수 없음
'''
def solve():
    INF = int(1e6)
    D = [[INF]*N for _ in range(N)]
    D[0][0] = 0 # 시작은 0
    Q = [(0, 0)]
    while Q:
        row, col = Q.pop(0)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newR = row + dr
            newC = col + dc
            if 0 <= newR < N and 0 <= newC < N:
                h = max(1, ARR[newR][newC]-ARR[row][col]+1)
                if D[newR][newC] > D[row][col] + h:
                    D[newR][newC] = D[row][col] + h
                    Q.append((newR, newC))
    return D[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {solve()}')