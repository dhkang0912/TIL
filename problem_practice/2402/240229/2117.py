'''
홈 방범 서비스
'''

def solve(row, col):
    # row, col에서 집까지의 거리의 갯수가 K에 저장되도록
    K = [0] * N


Home = []
for row in range(N):
    for col in range(N):
        solve(row, col)