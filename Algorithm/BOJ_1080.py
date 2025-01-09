import sys
sys.stdin = open("BOJ_1080_input.txt","r",encoding="utf-8")

'''
행렬
이차원 행렬
모든 원소를 뒤집는데 필요한 최소 연산의 값

# 인풋
1. 이차원 행렬 N*M
2. N, M은 50이하
3. N개의 행에는 행렬 A
4. 그 다음 N개의 행에는 행렬 B가 주어짐
=> 행렬 2개가 주어지는 것

A 행렬에서 0을 1로 뒤집거나 1을 0으로 뒤집어서 같게 만들 수 있는 최소 횟수를 구하기
만약 바꿀 수 없다면 -1

# 로직
이거 bfs 아냐? 근데 연결되어있다는 건 없다
그냥 생각나는 대로 한다면 사실 상 A,B 행렬을 input 받고
하나씩 비교하면서 이미 동일한 부분은 안 뒤집고... 나머지를 뒤집으면 되는 거 아닌가?
행렬을 뒤집는다는게 어떤 의미지?
=> 진짜 3*3 배열로 그대로 뒤집는 것...

그럼 사실 상 3*3이 넘지 않으면 안될거고
3*3을 기준으로 대칭이 아닌 이상 안될 것 같은데 어케 한담...
'''
def toggle(r, c):
    # 3*3 행렬을 뒤집어주기
    for i in range(r, r+3):
        for j in range(c, c+3):
            A[i][j] = not A[i][j]

N, M = map(int,input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
# print(N,M)
# print(A)
# print(B)

cnt = 0
# 시작부터 칸 수를 확인하기 위해 시작+3까지 차지 => N-3까지 가능
# range는 미만이니까 하나 더 큰 기준으로 적기 => N-2
for i in range(N-2):
    for j in range(M-2):
        # 하나씩 지나가며 확인하면서 같지 않다면 3*3으로 뒤집어 주기
        if A[i][j] != B[i][j]:
            toggle(i,j)
            cnt+=1

if A == B:
    print(cnt)
else:
    print(-1)