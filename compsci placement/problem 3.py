class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None

    def add(self, loc, value):
        if self.root is None:
            self.root = Node(value)
