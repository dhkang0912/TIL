'''
4*4 격자판
이 격자판에서 동서남북 이동하는 경우를 다 봐야 함
동서남북으로 움직이면서 뽑게 되는 숫자의 조합
총 6번 이동 가능 -> 이동 횟수를 세서 이걸 종료 조건으로 써먹음
이렇게 해서 뽑을 수 있었던 수의 개수를 셈, 중복은 제외
'''
def dfs(cnt, row, col, path):

    if cnt == 6:
        num_set.add(path)
        return

    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        New_row = row + i
        New_col = col + j
        # 범위 안에 있다면
        if 0 <= New_row < 4 and 0 <= New_col < 4:
            # 숫자들이 서로 합쳐져야 하는데
            dfs(cnt + 1, New_row, New_col, path + arr[New_row][New_col])




T = int(input())
for tc in range(1, T+1):
    # 격자판 정보, split 안 해서 답이 이상하게 나왔었음 ㅠㅠ , 진짜 바보바보...
    arr = list(input().split() for _ in range(4))
    # print(arr)

    # 최종 리스트
    num_set = set()

    for row in range(4):
        for col in range(4):
            dfs(0, row, col, arr[row][col])

    print(f'#{tc} {len(num_set)}')
