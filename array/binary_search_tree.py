from tree import Node

class BinaryTree:
    def __init__(self,data= None):
        self.root = Node(data)

    def insert(self,data=None):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,start,data):
        if data > start.data:
            if start.right == None:
                start.right = Node(data)
            else:
                _insert(start.right,data)
        elif data < start.data:
            if start.left == None:
                start.left = Node(data)
            else:
                _insert(start.left,data)
        else :
            print("data already exists")