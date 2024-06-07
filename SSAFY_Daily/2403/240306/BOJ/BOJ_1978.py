N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for num in lst:
    if num == 1:
        continue
    for i in range(2,num): #2부터 자신 전까지 나눠떨어지면 소수가 아님
        if num % i == 0:
            break
    else:
        cnt +=1


print(cnt)
