'''
N명의 사람들, 1~N번까지 번호
i번 사람이 돈을 인출할 때 걸리는 시간 Pi

사람마다 돈을 인출하는데 필요한 시간이 다름
기다리는 시간들이 있어서 나의 앞의 사람들 인출시간과 내가 돈을 뽑는 시간을 더해야지 필요한 시간이 나옴

대기 시간이 적은 순으로 인출하는게 가장 좋음
이거 그리디 문제 아닌가?

아 각각 대기 시간이 다 다르기 때문에 각 사람의 대기시간+내 인출시간이 내가 걸린 시간이네
각자 걸린 시간의 합이구나
'''

N = int(input())
wait_list = list(map(int, input().split()))
wait_list.sort()
wait_time = 0
for i in range(N):
    if i == 0:
        wait_time += wait_list[i]
    else:
        # print(sum(wait_list[0:i]))
        wait_time += sum(wait_list[0:i+1])
        # print(wait_time)

print(wait_time)