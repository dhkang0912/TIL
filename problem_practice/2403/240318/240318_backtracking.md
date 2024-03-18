## 알고리즘 설계 기법의 종류
### 1. 전체를 그냥 다 보자 (Brute Force- 완전 탐색)
- 배열 : for문, while 문
- 그래프 (관계가 있는 데이터)
    - BFS, DFS

그러나 완전 탐색을 구현하면, 시간 or 메모리 초과가 되더라!

### 2. 상황마다 좋은 걸 고르자 (Greedy - 그리디)
- 규칙  + 증명 -> 구현

### 3. 큰 문제를 작은 문제로 나누어 부분적으로 해결하자 (Dynamic Programming)
- 분할 정복과 다르게 작은 문제가 중복
- 중복된 문제의 해답을 저장해놓고 재활용하자! (Memoization)

### 4. 큰 문제를 작은 문제로 나누어 부분적으로 해결하자 (분할 정복)

### 5. 전체 중 가능성 없는 것을 빼자 (Backtracking - 백트래킹)

-> 이 기본들을 기반으로 더 고급 알고리즘들이 개발됨


## 목차
### 1. 분할정복
### 2. 대표적인 분할 정복 알고리즘
#### 2-1. 병합 정렬 (손으로 그릴 줄 알아야 함)
#### 2-2. 퀵 정렬 (손으로 그릴 줄 알아야 함)
#### 2-3. 이진 검색


## 분할 정복 기법
### 유래
- 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
- 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔
- 둘로 나뉜 연합군을 한 부분씩 격파함

### 설계 전략
- 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복(Conquer) : 나눈 작은 문제를 각각 해결함
- 통합(Combine) : (필요하다면) 해결된 해답을 모음

=> 재귀를 통해 구현
=> 대신 하나라도 틀리면 전체 결과가 잘못나옴


### Top-down approach 예시
- 분할 크기는 원하는 대로 정할 수 있지만 대부분 절반
- 언제까지 분할해야할까? -> 작은 문제로 나눌 수 없을 때까지
- 제일 작은 부분 문제의 해를 구해서 다시 합쳐서 전체 문제의 해를 구함

## 병합 정렬(Merge Sort)
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

### 분할 정복 알고리즘 활용
- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
- Top-down 방식
- 시간 복잡도 : O(n log n)

### 병합 정렬 과정
- 더 이상 쪼갤 수 없을 때까지 쪼개고 정렬함
- 이것들을 합치면서 다시 크기를 비교해서 정렬

- 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
- 시간 복잡도 : O(n log n)

```python
def merge(left, right):
    new_lst = []
    lp = 0
    rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else :
            new_lst.append(right[rp])
            rp += 1
    

    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    # if lp < len(left):
    #     new_lst.extend(left[lp:])
    # if rp < len(right):
    #     new_lst.extend(right[rp:])

    return new_lst

# 리스트의 값들을 정렬한 후 new_list를 return
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    m = len(lst)//2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])
    new_lst = merge(left, right)
    
    
    return new_lst


numbers = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_lst = merge_sort(numbers)
print(sorted_lst)
```

## 퀵 정렬
- 주어진 배열을 두개로 분할하고, 각각 정렬한다
- 인덱스를 많이 활용함

### 병합 정렬과 퀵 정렬이 다른 점
1. 병합 정렬은 그냥 두 부분을 나누는 반면, 퀵 정렬은 분할할 때 기준 아이템 중심으로 분할함
-> Hoare-Partition 알고리즘
-> Lomuto partition 알고리즘 (Hoare보다 안 좋음)

2. 각 부분 정렬이 끝난 후, 병합정렬은 '병합'이라는 후처리 작업이 필요하나 퀵 정렬은 필요 없음

=> 병합 정렬보다 효율적임

### 퀵 정렬 아이디어
- 피봇 값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다
- 피봇을 두 집합의 가운데에 위치시킨다

### 피봇 선택
- 왼쪽 끝, 오른쪽 끝, 임의의 세 값 중 중간 값을 선택함

``` python
# s, e 사이에서 s 위치의 값을 pivot으로 
# 좌측에는 작은 값들이 우측에는 큰 값들을 모으고
# pivot의 위치를 return
def partition_h(s, e):
    p = s
    i = s+1 # 또는 s
    j = e

    while i <= j:
        # i의 위치 이동
        while  i <= j and numbers[i] <= numbers[p]:
            i += 1
        # j의 위치 이동
        while i <= j and numbers[j] > numbers[p]:
            j -= 1
        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[p], numbers[j] = numbers[j], numbers[p]
    return j


# #j는 처음부터 끝까지 보기위한 용
# #i는 나보다 작은 거의 마지막 위치(큰 애가 나타나면 i 변하지 않음, 작은 애 나타나면 교환)
def partition_l(s, e):
    p = e
    i = s-1
    for j in range(s, e):
        if number[j] < numbers[p]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[p] = numbers[p], numbers[p+i]
    return i + 1

def quick_sort(s, e):
    if s < e:
      p = partition(s, e)
      quick_sort(s, p-1)
      quick_sort(p+1, e)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
N = len(numbers)
quick_sort(0, N-1)
print(numbers)

```



## 분할 정복 알고리즘 정리
### 병합 정렬
- 외부 정렬의 기본이 되는 정렬 알고리즘
- 멀티 코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용됨
### 퀵 정렬
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보이는 알고리즘
- 거꾸로 정렬되어 있는 경우 최악의 경우
- 시간 복잡도가 평균은 nlogn, 최악의 경우 n2

<br>
<br>
<br>

## 이진 검색
- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함

### 검색 과정
1. 자료의 중앙에 있는 원소를 고름
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복

### 이진 검색 예시
```python
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 정렬된 상태의 데이터
arr.sort()

# 이진 검색 - 반복문 버전
def binarySearch(target):
    low = 0 
    high = len(arr)-1
    # 탐색 횟수
    cnt = 0

    # 해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low+high) // 2
        # 확인하기 위한 출력
        print(f'mid = {mid} / arr[mid] = {arr[mid]}')
        cnt += 1

        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1

    # 못 찾으면 -1 반환
    return -1, cnt


# 이진 검색 - 재귀 함수 버전
def binarySearch_recur(low, high, target):
    # 기저 조건 (언제까지 재귀가 반복되어야 할까?)
    if low > high:
        return -1

    # 다음 재귀 들어가기 전엔 무엇을 해야할까?
    # 정답 판별
    mid = (low + high) //2
    if target == arr[mid] :
        return mid

    # 다음 재귀 함수 호출 (파라미터)
    if target < arr[mid] :
        return binarySearch_recur(low, mid-1, target)
    else :
        return binarySearch_recur(mid+1, high, target)

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?
    # 이진 검색에서는 없음

```

### 이진 검색
- 정렬된 데이터를 기준으로 특정 값이나 범위를 검색하는데 사용
- 이진 검색을 활용한 심화 학습 키워드 = Lower Bound, Upper Bound
    - 정렬된 배열에서 특정 값 이상 또는 이하가 처음으로 나타나는 위치를 찾는 알고리즘
    - 특정 데이터의 범위 검색 등에서 활용




