# import sys
# sys.stdin = open("4873_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    sentence = list(input())
    i = 0
    while len(sentence) >=2 and i+1 < len(sentence):
        if sentence[i] == sentence[i+1]:
            sentence.pop(i)
            sentence.pop(i)
            i = 0
        else:
            i += 1

    print(f'#{tc}', len(sentence))