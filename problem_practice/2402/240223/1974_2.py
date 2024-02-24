T = int(input())
for tc in range(1, T + 1):
    N = 9
    sudoku = [list(map(int, input().split())) for _ in range(N)]
    # print(sudoku)

    row_confirm = 1
    for row in range(N):
        row_confirm_list = [0] * 9
        for col in range(N):
            i = sudoku[row][col] - 1
            row_confirm_list[i] += 1
        if 0 not in row_confirm_list:
            row_confirm *= 1
        else:
            row_confirm *= 0

    col_confirm = 1
    for col in range(N):
        col_confirm_list = [0] * 9
        for row in range(N):
            i = sudoku[row][col] - 1
            col_confirm_list[i] += 1
        if 0 not in col_confirm_list:
            col_confirm *= 1
        else:
            col_confirm *= 0

    arr_confirm = 1
    for row in range(0, N, 3):
        arr_confirm_list = [0] * 9
        for col in range(0, N, 3):
            new_row = 0
            new_col = 0
            for new_row in range(3):
                for new_col in range(3):
                    i = sudoku[new_row][new_col] - 1
                    arr_confirm_list[i] += 1
            if 0 not in arr_confirm_list:
                arr_confirm *= 1
            else:
                arr_confirm *= 0

    if row_confirm == 1 and col_confirm == 1 and arr_confirm == 1:
        all_confirm = 1
    else:
        all_confirm = 0

    print(f'#{tc} {all_confirm}')