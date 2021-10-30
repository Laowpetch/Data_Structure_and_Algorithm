class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
            
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

    def x3(self):
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            print(curr.data,end='')
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

T = BST()
inp = input('Enter Input : ').split('/')
k = int(inp[-1])
data = [int(i) for i in inp[0].split()]
for i in data:
    T.insert(Node(i))
T.PrintTree()
print('--------------------------------------------------')
T.x3(k)
T.PrintTree()