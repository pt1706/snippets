# ------------------with constructor-----------------------------------

import random


class Node:
    counter = 1
    max_level = 0

    def __init__(self, data, left=None, right=None, level=0):
        self.id = Node.counter
        self.level = level
        self.data = data
        self.left = left
        self.right = right
        Node.counter += 1
        if self.level > Node.max_level:
            Node.max_level = self.level

    @classmethod
    def return_max_level(cls):
        return Node.max_level

    def __repr__(self):
        return (f'Node num: {self.id}; '
                f'value: {self.data}; '
                f'level: {self.level}')


class CreateTree:
    nodes = {}

    def __init__(self, value):
        self.root = Node(value)

    def add_node(self, item):
        new_node = self.root
        level = 1
        while new_node.data != item:
            if new_node.data > item:
                if not new_node.left:
                    new_node.left = Node(item, level=level)
                    break
                else:
                    new_node = new_node.left
                    level += 1
                    continue
            if new_node.data < item:
                if not new_node.right:
                    new_node.right = Node(item, level=level)
                    break
                else:
                    new_node = new_node.right
                    level += 1
                    continue

    def print_all(self):
        node = self.root
        queue = [node]
        visited = []
        while queue:
            print(node)
            visited += [node]
            if node.left:
                if node.left not in visited:
                    queue += [node.left]
            if node.right:
                if node.right not in visited:
                    queue += [node.right]
            queue = queue[1:]
            if queue:
                node = queue[0]

    def add_list(self, lst):
        for item in lst:
            self.add_node(item)


if __name__ == '__main__':
    def test(scale=500):
        lst = [random.randrange(0, scale) for i in range(100)]
        c = CreateTree(scale // 2)
        c.add_list(lst)
        return Node.max_level

    min_scale = 100
    max_scale = 0
    avg_scale = 0
    for i in range(100):
        res = test()
        if res < min_scale:
            min_scale = res
        if res > max_scale:
            max_scale = res
        avg_scale += res
    avg_scale = avg_scale / 100
    print(f'min_scale: {min_scale}; '
          f'max_scale: {max_scale}; '
          f'avg_scale: {avg_scale}.')

# ------------------adding manually-----------------------------------


class ManNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, child):
        self.__left = child

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, child):
        self.__right = child

    # def __repr__(self):
    #     return f"value: {self.value};"


n_root = ManNode(10)
n_1 = ManNode(1)
n_root.left = n_1
n_11 = ManNode(11)
n_root.right = n_11
n_4 = ManNode(4)
n_1.right = n_4
n_15 = ManNode(15)
n_11.right = n_15
n_2 = ManNode(2)
n_4.left = n_2


def find_all(root):
    print(root.value)
    if root.left:
        find_all(root.left)
    if root.right:
        find_all(root.right)
    return 'end of search'


print(find_all(n_root))
