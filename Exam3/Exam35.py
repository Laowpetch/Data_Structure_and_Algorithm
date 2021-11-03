class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,node):
        if self.root is None:
            self.root= node
        else:
            Rootnode=self.root
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
    
    def PrintTree(self):
        def _PrintTree(node, level):
            if node != None:
                _PrintTree(node.right, level + 1)
                print('     ' * level, node)
                _PrintTree(node.left, level + 1)
        _PrintTree(self.root, 0)

    def max(self):
        buffer = self.root
        while(True):
            if buffer.right is None:
                return buffer.data
            buffer = buffer.right
            
    def min(self):
        buffer = self.root
        while(True):
            if buffer.left is None:
                return buffer.data
            buffer = buffer.left

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(Node(i))
T.PrintTree()
print('--------------------------------------------------')
print('Min : '+str(T.min()))
print('Max : '+str(T.max()))