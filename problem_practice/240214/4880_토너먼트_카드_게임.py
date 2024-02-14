# i~j 중 위너의 위치를 return
def getWinner(w1, w2):
    # 가위 바위 보 게임 위너 결정
    return


def game(i, j):
    if i == j:
        return i
    winner1 = game(i, (i+j)//2)
    winner2 = game((i+j)//2+1, j)
    return getWinner(winner1, winner2)

N = 4
s = [0] + [1, 3, 2, 1]
game(1, N)