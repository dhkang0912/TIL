# import sys
# sys.stdin = open("5185_input (1).txt", "r")

def hexTodec(S): # 16진수를 10진수로
    result = 0 # 10진수로 바꿀거니까 정수로 저장
    for c in S: # 글자 하나씩 보기
        if c.isdecimal(): # 만약 c가 숫자이면
            result = result*16 + int(c) # 자리 올림하고 나머지 숫자 더해주기
        else: #숫자가 아니면, 문자이고 10이상의 수
            result = result*16 + (ord(c) - ord('A')+10) #자리 올림하고,c에서 'A'까지 얼마나 차이나? = 1의 자리 + 10해줘서 1n으로 바꿔줌
    return result

def decTobin(intV): # 10진수를 2진수로 바꾸기
    result = '' # 2진수는 문자열로 해야 담을 수 있음
    while intV > 0: # 몫이 0보다 클 때까지 해야 돌아갈 때 나눠져서 가능
        result = str(intV%2) + result # 2로 나눈 나머지를 뒤에서부터 저장해옴
        intV //= 2 # 2로 나눈 몫을 저장해서 숫자를 바꿔줌

    if len(result) < 4 : #4자리가 아니라면 0으로 채워줌
        for _ in range((4-len(result))): # 부족한 자리수만큼 0으로 채워줌
            result = '0'+result
    return result




T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    result = ''
    for C in S:
        result = result + decTobin(hexTodec(C))

    print(f'#{tc} {result}')
