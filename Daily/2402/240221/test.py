def dequeue():
    global last
    result = Tree[1]
    # 힙을 재구성
    Tree[1] = Tree[last]
    last -= 1
    p = 1
    c = p * 2

    while c <= last:
        if c + 1 <= last and Tree[c] < Tree[c + 1]:
            c += 1
        if Tree[p] < Tree[c]:
            Tree[p], Tree[c] = Tree[c], Tree[p]
            p = c
            c = p * 2
        else:
            break
    print(last, Tree)
    return result


def enqueue(data):
    global last
    last += 1
    Tree[last] = data
    c = last
    p = last // 2
    while p:
        if Tree[p] < Tree[c]:
            Tree[p], Tree[c] = Tree[c], Tree[p]
            c = p
            p = c // 2
        else:
            break

    # print(Tree)


Tree = [0] * 100  # 비어있는 완전 이진 트리를  넉넉히 만들어줌
last = 0
for data in [20, 15, 19, 24, 22]:
    enqueue(data)

print(dequeue())
# print(dequeue())
# print(dequeue())
# print(dequeue())
