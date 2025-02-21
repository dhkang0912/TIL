import sys
sys.stdin = open("BOJ_1697_input.txt", "r", encoding="utf-8")
from collections import deque
'''
숨바꼭질

# 인풋
1. N, K => 수빈이가 있는 곳, 동생이 있는곳
X 좌표만 있음, 좌우로만 이동을 하는 셈

# 로직
결국 수빈이가 한번에 갈 수 있는 위치는 -1, +1, *2
이렇게 움직여서 가장 가까운 곳으로 가야하는 건데 그리고 한번 갈 때 time +1을 해주는 것
bfs와 가장 비슷할 것 같음
이차원 행렬이 아닌 bfs
'''
def bfs(now, target):
    q = deque([now])

    while q:
        x = q.popleft()
        # 목표 좌표에 도달했다면 도달한 시간을 확인하기 위해 visited를 출력
        if x == target :
            return visited[x]
        # 만약 목표 좌표가 아니라면 다음 좌표를 확인할 q에 넣기
        # 갈 수 있는 방향에 맞춰 다음 좌표를 확인할 q에 넣는다.
        for x_moved in (x-1, x+1, x*2):
            # 갈 수 있는 좌표가 맞고 방문을 안 했다면
            if 0 <= x_moved < 100001 and visited[x_moved] == 0:
                # 방문할 수 있는 좌표는 이전 좌표보다 시간이 +1 됐다는 것을 표시
                visited[x_moved] = visited[x] + 1
                q.append(x_moved)

            


# n은 현재 위치, k는 목표지점
n, k = map(int, input().split())
# 인덱스 1부터 사용하여 max는 100001
# 1부터 인덱스를 사용한다고 했을 때 결국 사용할 인덱스는 1~100000
# 개수로 입력했기 때문에 0을 포함해서 100001개인 것임!!
visited = [0] * 100001
print(bfs(n, k))

