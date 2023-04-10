class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data = None) -> None:
        self.root = Node(data)

    def print_tree(self,style):
        if style == "inorder":
            order = self.inorder(self.root,"")
        elif style == "preorder":
            order = self.preorder(self.root,"")
        else:
            order = self.postorder(self.root,"")
        print(order)

    def preorder(self,start, traversal):
        if start:
            traversal += (str(start.data)+ "-")
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right,traversal)
        
        return traversal
    
    def postorder(self,start, traversal):
        if start:
            
            traversal = self.postorder(start.left,traversal)
            traversal = self.postorder(start.right,traversal)
            traversal += (str(start.data)+ "-")
        return traversal
    
    def inorder(self,start, traversal):
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal += (str(start.data)+ "-")
            traversal = self.inorder(start.right,traversal)
        
        return traversal

tree = Tree(7)
tree.root.left = Node(8)
tree.root.right = Node(9)
tree.root.left.left = Node(10)
tree.root.left.right = Node(11)
tree.root.right.left = Node(12)

tree.print_tree("inorder")