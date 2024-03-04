N = 100
arr = [[0] * 101 for _ in range(101)]
# print(arr)

for tc in range(4):
    x_1, y_1, x_2, y_2 = map(int, input().split())

    for i in range(x_1, x_2):
        for j in range(y_1, y_2):
            arr[i][j] = 1

cnt = 0
for row in range(N):
    for col in range(N):
        if arr[row][col] >= 1:
            cnt += 1

print(cnt)
