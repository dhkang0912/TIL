# 1989 초심자의 회문 검사
# 거꾸로 읽어도 동일한 게 회문
# 회문이면 1을 출력, 아니면 0을 출력
# 단어의 길이는 3이상, 10이하
# -> 홀수일수도 있고, 짝수일수도 있고
    # 홀수일 때는
        # -> 나누기 2해서 몫만큼의 길이를 역순하여 저장
        # [단어길이+2:M]까지가 역순으로 저장한 것과 같다면 1
            # 아니면 0
    # 짝수일 때는
        # -> 나누기 2해서 몫만큼의 길이를 역순하여 저장
        # [단어길이:M]까지가 역순으로 저장한 것과 같다면 1
            # 아니면 0

T = int(input())
for tc in range(1, T+1):

    txt = input()

    txt_num = len(txt)
    txt_cut_num = txt_num//2
    txt_reverse = txt[0:txt_cut_num][::-1]

    if txt_num % 2 == 0 and txt_reverse == txt[txt_cut_num:txt_num] :
        print(f'#{tc} 1')
    elif txt_num % 2 == 1 and txt_reverse == txt[txt_cut_num+1:txt_num] :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')