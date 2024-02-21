# i~j 중 위너의 위치를 return
import sys
sys.stdin = open("4880_input.txt", "r")

def getWinner(w1, w2):
    # 가위 바위 보 게임 위너 결정
    if s[w1] == 1 :
        if s[w2] == 1:
            return w1
        elif s[w2] == 2:
            return  w2
        elif s[w2] == 3:
            return w1
    elif s[w1] == 2:
        if s[w2] == 2:
            return w1
        elif s[w2] == 1:
            return w1
        elif s[w2] == 3:
            return w2
    elif s[w1] == 3:
        if s[w2] == 3:
            return w1
        elif s[w2] == 2:
            return w1
        elif s[w2] == 1:
            return w2



def game(i, j):
    if i == j:
        return i
    winner1 = game(i, (i+j)//2)
    winner2 = game((i+j)//2+1, j)
    return getWinner(winner1, winner2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = [0] + list(map(int, input().split()))
    print(f'#{tc}', game(1, N))
