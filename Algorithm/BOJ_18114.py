
'''
블랙 프라이데이

백화점에서 제시하는 양의 정수 무게 C에 맞게 물건을 가져오면 => 만원
최대 3개, 중복 선택 불가
무게는 다 다름
=> 조합이네

# 인풋
1. N개의 물건 제시, C 목표 무게 제시
2. w 리스트 => 각 물건 무게

# 출력
문제의 조건을 만족하는 조합이 있으면 1
그렇지 않으면 0

재귀함수로 조합을 구하는 방식이 있었는데..
중복되면 안됨

=> 이렇게 하면 시간 초과가 남
=> 이분 탐색으로 경우를 나눠서 풀어야 함


'''
import sys
sys.stdin = open("BOJ_18114_input.txt","r", encoding="utf-8")

# input = sys.stdin.readline

# def combi(cnt, weight ):
#     if weight == C:
#         global success
#         success = 1
#         return
#     if cnt >= 3 or weight > C:
#         return 
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             combi(cnt+1, weight+w[i])
#             visited[i] = 0
    
# visited = [0]*N
# success = 0

# combi(0, 0)

# print(success)

def binary_search(s, e, target):
    while s <= e:
        mid = (s+e)//2
        if w[mid] == target:
            return True
        elif w[mid] > target:
            e = mid -1
        else:
            s = mid +1
    return False


def check(N, C):
    global success
    # 한번에 찾을 수 있는 경우
    if C in w :
        success = 1
        return
    # 가능한 인덱스 범위
    i, j = 0, N-1

    while i < j:
        # 두개를 가지고 더해서 찾을 수 있는 경우
        # 양 끝단을 더하고, 뒤에서부터 작아지는 수를 더 해가면서 조건을 확인
        sum = w[i] + w[j]
        if sum > C:
            j-=1
        elif sum == C:
            success = 1
            return
        # 세개를 더해야만 찾을 수 있는 경우
        else:
            diff = C - sum
            if w[i] != diff and w[j] != diff and binary_search(i, j, diff):
                success = 1
                return
            i+=1

N, C = map(int, input().strip().split())
w = list(map(int, input().strip().split()))
w.sort()
success = 0

check(N,C)
print(success)

    
        
