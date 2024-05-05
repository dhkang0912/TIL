def partical(k, subSum, rSum):
    if subSum > 10 :
        return

    # 필요에 따라 이렇게 할 수도 있음
    if subSum==10:
        print(result.count(1))
        print(result)
        return

    # 남은 것들과 subSum 합을 통해서 확인할 수 있음 -> 시간이 많이 걸림
    if subSum + sum(numbers[k:]) < 10:
        return

    # 내려보낼 때 남은 것의 합을 내려보낼 수 있음
    if subSum + rSum < 10:
        return



    if k == N:
        # print(subSum)
        # print(result)
        if subSum == 10:
            print(result.count(1))
            print(result)

        # print(result)
        # for i in range(N):
        #     if result[i]:
        #         sumV += numbers[i]
        # if sumV == 10:
        #     print(result.count(1))
            # print(sumV)
            # print(result)
        return

    result[k]=0
    # 내가 포함 안 됐을 경우
    partical(k+1, subSum, rSum-numbers[k])
    result[k] = 1
    # 내가 포함됐을 경우에는 내 데이터를 더해서 넘겨줌
    partical(k+1, subSum+numbers[k], rSum-numbers[k])

    return




# numbers = [i for i in range(1, 11)]
numbers = [8, 1, 9, 7, 2, 5]
N = len(numbers)
result = [-1]*N
partical(0, 0, sum(numbers))




def perm(k):
    if k == N:
        print(result)
        for i in range(N):
            pos = result[i]
            print(numbers[pos], end = ' ')
        print()
        return
    for i in range(N):
        if not visited[i]:
            result[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False



# 조합
def perm(k, s):
    if k == K:
        # print(result)
        sumV = 0
        for i in range(K):
            pos = result[i]
            sumV += numbers[pos]
        print(sumV)
        return

    for i in range(s, N-K+1+k):
        result[k] = i
        perm(k+1, i+1)
        visited[i] = False



numbers = [i for i in range(1, 11)]
# numbers = [8, 1, 9, 7, 2, 5]
N = len(numbers)
K = 3
result = [-1]*K
visited = [False] * N
perm(0, 0)

# def patial(k):
#     if k == N :
#         print(result)
#         sumV = 0
#         for i in range(N) :
#             if result[i]:
#                 sumV += numbers[i]
#         print(sumV)
#         return
#
#     result[k] = 0
#     patial(k+1)
#     result[k] = 1
#     patial(k+1)
#     return
#
#
#
# numbers = [i for i in range(1,6)]
# N = len(numbers)
# result = [-1]*N
# patial(0)


# #합이 10이 되는 경우, 원소 개수 구하기
# def patial(k):
#     if k == N :
#         # print(result)
#         sumV = 0
#         for i in range(N) :
#             if result[i]:
#                 sumV += numbers[i]
#         if sumV == 10 :
#             # print(sumV)
#             print(result.count(1))
#         return
#
#     result[k] = 0
#     patial(k+1)
#     result[k] = 1
#     patial(k+1)
#     return
#
#
#
# # numbers = [i for i in range(1,6)]
# numbers = [8,1,9,7,2,5]
# N = len(numbers)
# result = [-1]*N
# patial(0)


# #합이 10이 되는 경우, 원소 개수 구하기
# #백트래킹 : 중간 합 구하기
# def patial(k, subSum, rSum):
#     if subSum > 10 :
#         return
#
#     # #필요에 따라 가능
#     # if subSum == 10:
#     #     print(result.count(1))
#     # return
#
#     if subSum + rSum < 10:
#         return
#
#
#     if k == N :
#         # print(subSum) #이미 더해져서 내려오니까 바로 값 출력할 수 있음
#         # print(result)
#         if subSum == 10 :
#             print(result.count(1))
#         return
#
#     result[k] = 0 #k번째 원소가 0이면 포함 안 된 거 > 포함 안 된 상태로 다음 원소를 결정해!
#     patial(k+1, subSum) #위에 넘겨받은 값 그대로 내려보내주기
#     result[k] = 1 #k번째 원소가 1이면 포함 된 거 > 포함된 상태로 다음 원소를 결정해!
#     patial(k+1, subSum+numbers[k]) #포함되었으니까 내 데이터 추가해서 내려보내주기
#
#     return
#
#
#
# # numbers = [i for i in range(1,6)]
# # numbers = [i for i in range(6,0,-1)] 남은 것의 합이 10이 안 되면 더 안 봐도 됨
# numbers = [8,1,9,7,2,5]
# N = len(numbers)
# result = [-1]*N
# patial(0,0)
#
#
#
#
# #백트래킹 :남은 거의 합이 10이 안 될 떄
# def patial(k, subSum, rSum):
#     if subSum > 10 :
#         return
#
#     # #남은 거의 합이 10이 안 될 떄
#     # if subSum + sum(numbers[k:]) < 0: #시간 많이 걸림
#     #     return
#
#     if subSum + rSum < 10:
#         return
#
#     if k == N :
#         if subSum == 10 :
#             print(result.count(1))
#         return
#
#     result[k] = 0
#     patial(k + 1, subSum, rSum-numbers[k])
#     result[k] = 1
#     patial(k + 1, subSum + numbers[k])
#     return
#
#
#
# # numbers = [i for i in range(1,6)]
# # numbers = [i for i in range(6,0,-1)] 남은 것의 합이 10이 안 되면 더 안 봐도 됨
# numbers = [8,1,9,7,2,5]
# N = len(numbers)
# result = [-1]*N
# patial(0,0, sum(numbers)) #남은 거의 총 합
#



#순열
# def perm(k) :
#     if k == N :
#         print(result)
#         for i in range(N) :
#             pos = result[i]
#             print(numbers[pos], end=' ')
#         print()
#         return
#     for i in range(N) :
#         if not visited[i] :
#             result[k] = i
#             visited[i] = True
#             perm(k+1)
#             visited[i] = False
#
#
# # numbers = [i for i in range(1,4)]
# numbers = [8,1,9,7,2,5]
# N = len(numbers)
# result = [-1]*N  #위치 인덱스
# visited = [False]*N
# perm(0)


#순열은 순서 있게, 중복 없이!
#조합은 순서 없이, 중복 없이!
#위에서 밑으로 값을 내려보내주는 방식


#조합
def combi(k, s):
    if k == K :
        print(result)
        sumV = 0
        for i in range(K):
            pos = result[i]
            sumV += numbers[pos]
        print(sumV)
        return

    for i in range(s, N-K+1+k):
        result[k] = i
        combi(k+1, i+1)

numbers = [8,1,9,7,2,5]
N = len(numbers)
K = 3
result = [-1]*K  #위치 인덱스
visited = [False]*N
combi(0, 0)

