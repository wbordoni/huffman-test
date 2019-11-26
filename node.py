
class Node:
    """
    Simple binary tree structure
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_node(self):
        print("{}: data={}, left={}, right={}".format(self, self.data, self.left, self.right))

    