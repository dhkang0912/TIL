# import sys
# sys.stdin = open("4880_input.txt", "r")

def WinGame(player1_idx, player2_idx):
    P1 = game_info[player1_idx]
    P2 = game_info[player2_idx]

    if P1 == 1:
        if P2 == 1:
            return player1_idx
        elif P2 == 2:
            return player2_idx
        elif P2 == 3:
            return player1_idx
    if P1 == 2:
        if P2 == 2:
            return player1_idx
        elif P2 == 1:
            return player1_idx
        elif P2 == 3:
            return player2_idx
    if P1 == 3:
        if P2 == 3:
            return player1_idx
        elif P2 == 1:
            return player2_idx
        elif P2 == 2:
            return player1_idx


def game(start_idx, end_idx):
    if start_idx == end_idx:
        return start_idx
    half = (start_idx+end_idx)//2
    player1_idx = game(start_idx, half)
    player2_idx = game(half+1, end_idx)
    return WinGame(player1_idx, player2_idx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game_info = list(map(int, input().split()))
    # print(game_info)
    winner_idx = game(0, N-1)
    print(f'#{tc}', winner_idx+1)