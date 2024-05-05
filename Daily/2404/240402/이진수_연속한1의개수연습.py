N = 1200
N = format(N, 'X')
print(N)

result = ''
for c in N:
    # print(format(int(c, 16), '04b'))
    result += format(int(c, 16), '04b')

print(result)

# max_cnt = 0
# lst = []
# count = []
# for i in range(len(result)):
#     if result[i] == '1':
#         lst.append(result[i])
#     elif (result[i] == '0' or i == N-1) and lst:
#         if len(lst) > 1:
#             count.append(len(lst))
#         lst.clear()
#
# print(*count)



