T =10
for tc in range(1, T+1):
    tc = int(input())
    arr = [input() for _ in range(100)]

    ans = -1
    for m in range(99, 0, -1) :

        for row in range(100) :
            for s in range(101-m):
                if arr[row][s:s+m] == arr[row][s:s+m][::-1]:
                    ans = m
                    break
            if ans != -1 :
                break


        for col in range(100):
            maxV2 = 0
            newlst = []
            for row in range(100):
                newlst.append(arr[row][col])
            for s in range(101-m):
                if newlst[s:s+m] == newlst[s:s+m][::-1] :
                    ans = m
                    break
            if ans != -1:
                break



    print(f'#{tc}', ans)