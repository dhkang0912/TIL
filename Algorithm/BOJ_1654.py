# import sys
# sys.stdin = open("BOJ_1654_input.txt", "r", encoding="utf-8")

'''
랜선 자르기

K개의 랜선
랜선의 길이는 제각각
N개의 같은 길이의 랜선으로 만들고 싶음
N개보다 많아도 되지만 자르면 남는 길이는 버려짐
최대한 랜선의 길이를 길게 해야함
=> 그리디일 것 같은데...
아닌가? 분할정복인가?
이분탐색 같은데 절반 나눠서 조건 안 되면 바꾸는

# 인풋
1. K, N을 인풋받음 => 존재하는 랜선의 개수, 필요한 랜선의 개수
2. K번만큼 랜선의 길이가 입력됨

'''
# 이분 탐색
def check(start, end):
    while start <= end:
        mid = (start+end)//2
        cnt = 0

        # 자르려는 길이만큼 자른 후 몇개가 나오는지 확인함
        for lan in lans:
            cnt += (lan//mid)
        
        # 목표 개수보다 랜선의 개수가 더 많다면 더 짧게 조각남 => 시작을 더 키워도 됨
        if cnt >= N : 
            start = mid + 1
        # 목표 개수보다 랜선의 개수가 더 적음 => 랜선이 너무 길게 조각남 => 최대 길이를 줄이기
        else:
            end = mid - 1
    # 가장 큰 길이를 출력하기
    print(end)

K, N = map(int, input().split())
lans = [0]*K
# for i in range(K):
#     lans[i] = int(input())

lans = [int(input()) for _ in range(K)]

# lans = sorted(lans)
lans.sort()
check(1,lans[-1])