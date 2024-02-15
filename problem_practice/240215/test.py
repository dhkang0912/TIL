def isFull():
    return front == (rear + 1) % size


def isEmpty():
    return front == rear


def deQueue():
    global front
    if isEmpty():
        print('empty')
        return
    front = (front + 1) % size
    return Q[front]


def enQueue(item):
    global rear

    if isFull():
        print('full')
        return
    rear += 1
    Q[rear] = item


size = 4
Q = [-1] * size
# 무조건 더하고 처리
front = 0
rear = 0
enQueue(10)
enQueue(20)
enQueue(30)
t = deQueue()
print(t)
print(deQueue())
print(deQueue())
