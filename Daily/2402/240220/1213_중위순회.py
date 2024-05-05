import sys
sys.stdin = open("1213_input.txt", "r")

T = 10
for tc in range(1, T+1):
    global result
    def inOrder(root):
        root = int(root)
        if Data[root]:
            inOrder(left_child[root])
            result.append(Data[root])
            inOrder(right_child[root])


    N = int(input())
    # Tree = [[0] for _ in range(N)]
    left_child = [0] * (N+1)
    right_child = [0] * (N+1)
    Data = [0] * (N+1)
    result = []
    for i in range(N):
        element = input().split()
        Data[i+1] = element[1]
        if len(element) >= 3:
            left_child[i+1] = element[2]
        if len(element) >= 4:
            right_child[i+1] = element[3]

    # print(Data)
    # print(left_child)
    # print(right_child)
    '''
    [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']
    [0, '2', '4', '6', '8', 0, 0, 0, 0]
    [0, '3', '5', '7', 0, 0, 0, 0, 0]
    '''

    inOrder(1)
    print(f'#{tc}', ''.join(result))

    # print(Data)
    # print(left_child)
    # print(right_child)


