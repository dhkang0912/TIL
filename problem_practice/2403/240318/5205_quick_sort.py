
def partition_h(s, e):
    p = s #피봇을 처음으로 지정
    i = s #또는 s+1, i는 처음부터 피봇보다 작은 것들의 집합을 만들어감
    j = e # j는 끝에서부터 피봇보다 큰 애들의 집합을 만들어감

    while i <= j: # 서로 교차되지 않을때까지 반복
        # 서로 교차되지 않고 피봇보다 작거나 클 때까지 인덱스를 증가한다 -> 큰 걸 발견하면 멈춤
        while i <= j and numbers[i] <= numbers[p]:
            i += 1
        while i <= j and numbers[j] > numbers[p]:
            # 서로 교차되지 않고 피봇보다 클 때까지 인덱스를 줄여가면서 이동
            j -= 1
        if i < j: # i는 피봇보다 크고, j가 피봇보다 작을 때, i가 j보다 작다면 서로 위치 이동
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[p], numbers[j] = numbers[j], numbers[p] # 최종적으로 피봇 위치를 찾아줌 (첫번째와 자신보다 작은 집합 중 마지막 인덱스와 자리 변경)
    return j # 피봇의 위치를 반환


def quick_sort(s, e):
    if s < e : # 인덱스가 교차되기 전까지 파티셔닝하여 분할
        # 파티셔닝 후 피봇의 위치를 반환
        p = partition_h(s, e)
        # 파티셔닝을 통해 피봇의 위치는 정해졌음, 피봇 왼쪽과 오른쪽 정렬이 필요하여 재귀 반복
        quick_sort(s, p-1)
        quick_sort(p+1, e)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 시작 인덱스와 끝 인덱스를 넣어 정렬해주기
    quick_sort(0, N-1)
    print(f'#{tc} {numbers[N//2]}')


