class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    # 마지막 값을 반환하되 삭제하지 않는다.
    def peek(self):
        return self.container[-1]


if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.peek())

    i = 0
    while not s.empty():
        print("index: {}".format(i), s.pop())
        i += 1
