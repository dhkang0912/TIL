# 4861 회문
# ABBA 처럼 어느 방향에서 읽어도 같은 문자열을 회문
# -> 문자 갯수 나누기 2만큼의 문자가 역순으로 다시 반복
# 회문은 1개 존재, 가로~세로로 찾아볼 수 있음

# 오 대박 좋다
# N*M일 때 회문을 찾아야 함

# 테스트 케이스의 T가 주어짐
# 첫 줄에 N*M이 주어짐
# 다음 줄 부터 N개의 글자를 가진 N의 줄이 주어짐
    # 한 행씩 확인하기
    # 거꾸로 해도 같은 건지만 보면 됨
    # 한 행에서 가능한 start를 지정해서 확인하면 됨
    # -> 이걸 어떻게 확인할 것인가?
    # -> col을 계속 조정해주는 것
    # col이 10개, 회문 갯수가 8 일 때 가능한 시작지점 = 10-8+1 -> col-M+1
    # 확인해야할 회문 길이 = arr[row][start+M]까지를 확인하기
    # 한행마다 이렇게 확인하면 됨, 행은 한개씩 늘어날 때에 col을 이런 식으로 돌려서 확인하면 됨

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(str,input())) for _ in range(N)]

    # 행마다 비교
    # 가능한 시작지점 잡아줘서 그걸 돌렸을 때 동일하다면 회문

    for row in range(N) :
        for start in range(N-M+1):
            if arr[row][start:start+M] == arr[row][start:start+M][::-1]:
                print(f'#{tc}', "".join(arr[row][start:start+M]))


    for col in range(N):
        new_arr = []
        for row in range(N):
            new_arr.append(arr[row][col])
        for start in range(N-M+1):
            if new_arr[start:start+M] == new_arr[start:start+M][::-1]:
                print(f'#{tc}', ''.join(new_arr[start:start+M]))

    # for col in range(N):
    #     new_arr = ''
    #     for row in range(N):
    #         new_arr+=arr[row][col]
    #    for start in range(N-M+1):
    #         if new_arr == new_arr[::-1]:
    #             print(f'#{tc}', new_arr)






