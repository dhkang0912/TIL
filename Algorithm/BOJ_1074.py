import sys
sys.stdin = open("BOJ_1074_input.txt", "r", encoding="utf-8")

def cnt_z(N, r, c):
    # N이 0이라면 재귀가 끝나고 모두 탐방한 것
    if N == 0:
        return 0
    
    # 사분면의 사이즈
    # 애초에 문제에 2^(N-1)로 사분할한다고 나와있음
    # 한변의 길이
    line = 2**(N-1)
    # 사분면의 크기
    size = line * line
    
    # 각 영역의 사분면의 첫번째 좌표를 찾기
    if r < line and c < line:
        # 왼쪽 위
        # 바로 카운트를 세면 동일
        return cnt_z(N-1, r, c)
    elif r < line and c >= line:
        # 오른쪽 위
        # size만큼 세지고 오른쪽 위로 이동
        return size + cnt_z(N-1, r, c-line)
    elif r >= line and c < line:
        # 왼쪽 아래
        # 2*size만큼 세지고 왼쪽 아래로 이동
        return 2*size + cnt_z(N-1, r - line, c)
    else:
        # 오른쪽 아래
        # 3*size만큼 세지고 오른쪽 아래로 이동
        return 3*size + cnt_z(N-1, r-line, c-line)



N, r, c = map(int, input().split())
# 2의 N제곱, cnt 확인할 좌표
print(cnt_z(N, r, c))


