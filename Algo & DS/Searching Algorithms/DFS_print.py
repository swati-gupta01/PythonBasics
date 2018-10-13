class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def DFS(node):
    if node:
        DFS(node.left)
        print(node.value)
        DFS(node.right)


n=Node(5)
n.left=Node(3)
n.right=Node(8)
n.left.left=Node(2)
n.left.right=Node(4)
n.right.left=Node(6)
n.right.right=Node(9)

DFS(n)