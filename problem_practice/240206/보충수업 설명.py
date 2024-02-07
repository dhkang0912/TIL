def is_palindrome(word):
    # 회문인지 아닌지를 확인
    # 회문이라면 1을 출력 (아니라면, 0을 출력)
    # N = len(word)  # 문자열의 길이 N
    # # 순회는 N // 2 까지 순회를 반복한다...!
    # for i in range(N // 2):
    #     # 앞의 문자와 뒤의 문자가 서로 동일한지를 체크...!
    #     if word[i] != word[-i - 1]:
    #         return 0
    # return 1
    # 정방향으로 읽은 단어와 역향뱡으로
    if word == word[::-1]:
        # 읽은 단어가 같다면 회문!
        return 1
    return 0


# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    word = input()
    # 로직
    result = is_palindrome(word)

    # 출력
    print(f"#{tc} {result}")



# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 문자열1 str1 / 문자열2 str2
    str1, str2 = input(), input()

    # # 로직
    # result = 0  # 결과값을 저장할 임시변수
    # # 문자열 길이 N, M
    # N = len(str1)
    # M = len(str2)
    # # 문자열2 안에 문자열1이 존재하는가...!
    # # 1. 반복문을 사용해서 M 길이만큼 문자열2를 잘라가면서 같은지 비교...!
    # for i in range(N - M + 1):
    #     if str2[i: i + M] == str1:
    #         result = 1
    #         break

    # # 2. in 키워드를 사용하는 방안...
    # # 문자열2 안에 문자열1이 존재하는가...!
    # if str1 in str2:
    #     result = 1
    # else:
    #     result = 0

    # 3. find 메서드를 사용하는 방안
    # find 메서드가 해당 문자열이 존재하는 첫번째 인덱스를 반환...
    # (단, 찾지 못하면 -1을 반환한다....)
    #  삼항연산자...
    # result = 참일때값 if 조건식 else 거짓일때값
    result = 1 if str2.find(str1) != -1 else 0

    # 존재한다면 1 (아니라면 0) 출력...!
    # 출력
    print(f"#{tc} {result}")



def is_palindrome(word):
    if word == word[::-1]:
        return 1
    return 0


# 테스트케이스 수 T
T = 10
N = 8  # 글자판의 한변의 길이
for tc in range(1, T + 1):
    # 입력
    # 회문의 길이 K
    K = int(input())
    # 8x8 글자판 boards
    boards = [list(input()) for _ in range(N)]

    # 로직
    # 카운트 값을 담아둘 변수 cnt
    # 변수명을 지을 때 어떻게 지으면 좋을까...
    # 해당 단어를 찾고 -> 거기에 모음 'a','e','i','o','u', 'y'
    # count -> cnt
    # sum -> sm -> total
    # C/C++ 언어 한정...
    # left / right -> lft / rght (row / high)
    # max / min -> mx / mn

    # 카운트 변수 cnt
    cnt = 0

    # K 길이 만큼의 회문을 가로 탐색 카운트 값 증가...
    for i in range(N):
        for j in range(N - K + 1):  # [0 ~ N - K]
            # 글자판 i행에 [j:j+K] 까지의 문자열을 가져와서 회문인지를 체크...!
            if is_palindrome(boards[i][j:j + K]):
                cnt += 1  # 카운트가 1씩 증가...!

    # # //    세로 탐색 카운트 값 증가...
    # # K 길이 만큼의 회문을 가로 탐색 카운트 값 증가...
    # for j in range(N - K + 1):  # [0 ~ N - K]
    #     for i in range(N):
    #         # 글자를 만들기 위한 임시 문자열
    #         word = ''
    #         for k in range(K):
    #             word += boards[j + k][i]
    #         if is_palindrome(word):
    #             cnt += 1

    # 글자판의 데이터를 변경...
    # 열 <-> 행을 뒤집겠다...! (전치행렬)
    # boards  # [[1,2,3],
    #          # [4,5,6],
    #          # [7,8,9]]
    #        -> [[1, 4, 7],
    #         #  [2, 5, 8],
    #         #  [3, 6, 9]] 이렇게 만들겠다!
    # zip(boards[0], boards[1], boards[2],...) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    # zip(*boards) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    boards = list(map(list, zip(*boards)))
    for i in range(N):
        for j in range(N - K + 1):  # [0 ~ N - K]
            # 글자판 i행에 [j:j+K] 까지의 문자열을 가져와서 회문인지를 체크...!
            if is_palindrome(boards[i][j:j + K]):
                cnt += 1  # 카운트가 1씩 증가...!

    # 출력
    print(f"#{tc} {cnt}")


