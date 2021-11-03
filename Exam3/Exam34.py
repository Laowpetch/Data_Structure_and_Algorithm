class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self,node):
        if self.root is None:
            self.root= Node(node)
        else:
            Rootnode=self.root
            node = Node(node)
            while True:
                if node.data >= Rootnode.data:
                    if Rootnode.right is None :
                        Rootnode.right = node
                        break
                    Rootnode = Rootnode.right
                else:
                    if Rootnode.left is None:
                        Rootnode.left = node
                        break
                    Rootnode = Rootnode.left

def height(node, level=-1):
    if node:
        level += 1
        return max(height(node.left, level), height(node.right, level))
    return level

print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))

for e in arr:
    tree.create(e)

print("Height = ",height(tree.root),end="\n\n")