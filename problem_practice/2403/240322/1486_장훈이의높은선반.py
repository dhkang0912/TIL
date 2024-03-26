def bfs(person_height_idx, top_height):
    global min_height

    # 특정 탑의 높이 이상 쌓았다면 가장 작은 탑 높이를 구하고 리턴
    if top_height >= B:
        min_height = min(min_height, top_height)
        return

    if person_height_idx == N:
        return

    # 현재 뽑힌 점의 키를 더해서 넘겨줌
    bfs(person_height_idx+1, top_height+(people_lst[person_height_idx]))

    # 특정 인덱스의 키를 더해주지 않는 경우
    bfs(person_height_idx+1, top_height)






T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N = 정수의 개수(점원의 수), B = 쌓을 탑의 높이
    # 점원의 키가 담긴 리스트
    people_lst = list(map(int, input().split()))

    # 누적 키중 가장 작은 걸 담을 변수
    min_height = float('inf')

    # 점원 키의 인덱스, 탑의 높이
    bfs(0, 0)
    print(f'#{tc} {abs(B - min_height)}')
