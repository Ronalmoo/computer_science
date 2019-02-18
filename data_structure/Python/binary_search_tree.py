from binary_tree import TreeNode


class BST:
    def __init__(self):
        self.root = Node

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func, *args, **kwargs):
        if not cur:
            return

        func(cur, *args, **kwargs)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def insert(self, data):
        new_node = TreeNode()
        new_node.data = data

        cur = self.root
        if not cur:
            self.root = new_node
            return

        while True:
            parent = cur
            if data < cur.data:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return

            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    def search(self, target):
        cur = self.root
        while cur:
            if cur.data == target:
                return cur
            elif cur.data > target:
                cur = cur.left
            elif cur.data < target:
                cur = cur.right

        return cur

    def __remove_recursion(self, cur, target):
        if not cur:
            return None, None
        elif target < cur.data:
            cur.left, rem_node = self.__remove_recursion(cur.left, target)
        elif target > cur.data:
            cur.right, rem_node = self.__remove_recursion(cur.right, target)
        else:
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
            elif not cur.right:
                rem_node = cur
                cur = cur.left
            elif not cur.left:
                rem_node = cur
                cur = cur.right
            else:
                replace = cur.left
                while replace.right:
                    replace = replace.right
                cur.data, replace.data = replace.data, cur.data
                cur.left, rem_node = self.__remove_recursion(
                    cur.left, replace.data)
        return cur, rem_node

    def remove(self, target):
        self.root, removed_node = self.__remove_recursion(self.root, target)
        if removed_node:
            removed_node.left = removed_node.right = None
        return removed_node


if __name__ == "__main__":
    print('*' * 100)
    bst = BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    def f(x):
        return print(x.data, end="  ")

    bst.preorder_traverse(bst.get_root(), f)
    print()

    print('searched data : {}'.format(bst.search(8).data))

    # bst.remove(9)
    # bst.remove(8)
    # bst.remove(6)

    print(bst.remove(15))

    bst.preorder_traverse(bst.get_root(), f)
    print()
    print('*' * 100)
