'''
팰린드롬은 회문
'''

while True:
    num_str = input()
    if num_str == '0':
        break
    if num_str == num_str[::-1]:
        print('yes')
    else:
        print('no')

