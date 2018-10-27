class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def BFS(node):
    q=[]
    q.append(node)

    while q :
        a = q.pop(0)
        if a.left:
            q.append(a.left)
        if a.right:
            q.append(a.right)
        print(a.value)


n=Node(5)
n.left=Node(3)
n.right=Node(8)
n.left.left=Node(2)
n.left.right=Node(4)
n.right.left=Node(6)
n.right.right=Node(9)

print(BFS(n))