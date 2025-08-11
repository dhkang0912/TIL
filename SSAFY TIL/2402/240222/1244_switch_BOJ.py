'''
기준을 두고 범위를 지정하기보단, 시작점과 끝점을 설정하는 것이 더 쉬움
two point 문제
'''
def toggle(no):
    switch[no] = (switch[no] + 1) % 2
    # if switch[no] ==1:
    #     switch[no] == 0
    # else:
    #     switch[no] = 1

def m_do(no):
    for idx in range(no, N+1, no):
        toggle(idx)

def f_do(no):
    s = no - 1
    e = no + 1
    while s >= 1 and e <= N and switch[s] == switch[e]:
        toggle(s)
        toggle(e)
        s -= 1
        e += 1



N = int(input())
switch = [-10000] + list(map(int, input().split()))

num = int(input())
for _ in range(num):
    sex, no = map(int, input().split())
    if sex == 1:
        m_do(no)
    else:
        f_do(no)

for idx in range(1, len(switch), 20): # 또는 N+1
    print(*switch[idx:idx + 20])
