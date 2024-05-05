'''
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
10 70 180 400
6 9 7 7 7 5 5 0 0 0 0 0
10 70 200 550
0 0 0 0 8 9 6 9 6 9 8 6
10 80 200 550
0 8 9 15 1 13 2 4 9 0 0 0
10 130 360 1200
0 0 0 15 14 11 15 13 12 15 10 15
10 180 520 1900
0 18 16 16 19 19 18 18 15 16 17 16
10 100 200 1060
12 9 11 13 11 8 6 12 8 7 15 6
10 170 500 1980
19 18 18 17 15 19 19 16 19 15 17 18
10 200 580 2320
12 28 24 24 29 25 23 26 26 28 27 22
'''
def dfs(month, sum_price):
    global min_sum
    # 사용할 수 있는 개월 수가 12개월이 넘으면 종료
    # 이때 가장 작은 값을 확인함
    if sum_price >= min_sum:
        return

    if month > 12:
        min_sum = min(min_sum, sum_price)
        return

    # 1일권 구매, 변수명 좀 확실히 하자!!!! 제발... 그냥 자동완성 쓰지마...
    dfs(month+1, sum_price+(plans[month]*price[0]))

    # 1달권 구매
    dfs(month+1, sum_price+price[1])

    # 3달권 구매
    dfs(month+3, sum_price+price[2])

    # 1년권 구매
    dfs(month+12, sum_price+price[3])



T = int(input())
for tc in range(1, T+1):
    # 인덱스 순서대로 : 1일권-0, 1달권-1, 3달권-2, 1년권 가격-3
    price = list(map(int, input().split()))
    # 인덱스는 달, 값은 이용할 일수
    plans = [0] + list(map(int, input().split()))

    # 가장 적은 비용 변수 할당
    min_sum = float('inf')
    # 시작 월, 가격의 합
    dfs(1, 0)
    print(f'#{tc} {min_sum}')

