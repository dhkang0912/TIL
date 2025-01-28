'''
절댓값 힙
배열에 정수를 넣으면 절댓값이 가장 작은 것을 출력하고 배열에서 제거
여러 개인 경우 가장 작은 수를 출력하고 그 값을 배열에서 제거

# 입력
1. N = 연산의 개수
2. N개의 연산에 대한 정보 => 정수 x

# 연산
3. x!=0 => 배열에 x 추가
4. x=0 배열에서 절댓값이 가장 작은 값을 출력 후 제거

# 출력
입력에서 0이 주어진 회수만큼 답을 출력
배열이 비어있는데 출력하라고 한 경우 0 출력
'''
import sys
input = sys.stdin.readline

N = int(input())
# 연산
make = list(map(int, input().split()))
arr = []

def check(arr):
    arr.sort(key = lambda x: (x[1],x[0]))
    return arr.pop(0)[0]

for x in make:
    if x != 0 :
        arr.append((x, abs(x)))
    else:
        if len(arr) == 0:
            print(0)
        else:
            # 최댓값이 가장 작은 수가 출력
            print(check(arr))
