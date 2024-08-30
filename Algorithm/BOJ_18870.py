'''
좌표 압축
N개의 좌표들이 주어지고
각 좌표들보다 더 작은 수가 몇개 있는지 확인함

# 인풋
1. N을 받음
2. N개의 숫자들을 리스트로 받음

# 로직
1. 각 숫자들을 set으로 넘겨 중복을 제거하고 sort로 변경
2. N개의 숫자들을 순회하며 해당되는 숫자의 위치를 확인함
=> 현재 본인의 인덱스가 자신보다 작은 숫자 개수

'''

def check(num, start, end):
    #이진 탐색
    # 중앙값 찾기
    while start <= end:
        mid = (start + end) // 2
        # 만약 mid 인덱스가 찾으려는 num이랑 같다면 발견!
        if lstset[mid] == num:
            # 해당 인덱스가 0부터 sorted 되어 표현되니 더 작은 숫자들은 해당 인덱스 번째의까지 있음
            return mid
        elif lstset[mid] < num:
            start = mid + 1
        elif lstset[mid] > num:
            end = mid - 1


N = int(input())
lst = list(map(int, input().split()))

lstset = list(set(lst))
lstset.sort()

for i in lst:
    print(check(i, 0, len(lstset)), end=" ")
