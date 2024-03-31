'''
3 1
4 2

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
-> 순열

각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

순열을 나타내기
1. level = M개 (총 M개가 매번 보여짐)
2개 묶음 (한 레벨에서 2개씩 뽑음)
2. branch = N개 (내가 뽑을 수 있는 카드)
1,2,3,4
'''
def perm(level):
    if level == N :
        return

    for i in range()



N = int(input())
M = int(input())

# 시작 레벨
perm(0)
path = [0]*N

