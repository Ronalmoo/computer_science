class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def __del__(self):
        print('data of {} is deleted'.format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class SingleLinkedList:
    def __init__(self):
        self.head = Node()
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.d_size += 1

    def search(self, target):
        cur = self.head.next
        while cur:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def delete(self):
        self.head.next = self.head.next.next
        self.d_size -= 1

    def traverse(self):
        cur = self.head.next
        while cur:
            yield cur
            cur = cur.next

def show_list(slist):
    print('data size : {}'.format(slist.size()))
    g = slist.traverse()
    for node in g:
        print(node.data, end= ' ')
    print()

if __name__ == '__main__':
    print('*' * 100)
    slist = SingleLinkedList()

    slist.add(3)
    slist.add(1)
    slist.add(5)
    slist.add(2)
    slist.add(7)
    slist.add(8)
    slist.add(3)
    show_list(slist)

    print('데이터 탐색')
    target = 5
    res = slist.search(target)
    if res:
        print('데이터 {} 검색 성공'.format(res.data))
    else:
        print('데이터 {} 탐색 실패'.format(target))
    res = None
    print()

    print('데이터 삭제')
    slist.delete()
    slist.delete()
    slist.delete()
    show_list(slist)

    print('*' * 100)