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
    
    def Preorder(self):
        def _Preorder(node):
            if node != None:
                print(node.data,end=' ')
                _Preorder(node.left)
                _Preorder(node.right)
        _Preorder(self.root)

    def Inorder(self):
        def _Inorder(node):
            if node != None:
                _Inorder(node.left)
                print(node.data,end=' ')
                _Inorder(node.right)        
        _Inorder(self.root)
    
    def Postorder(self):
        def _Postorder(node):
            if node != None:
                _Postorder(node.left)
                _Postorder(node.right)  
                print(node.data,end=' ')      
        _Postorder(self.root)

    def Breadth(self):
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            print(curr.data,end=' ')
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(Node(i))
print('Preorder : ',end='')
T.Preorder()
print()
print('Inorder : ',end='')
T.Inorder()
print()
print('Postorder : ',end='')
T.Postorder()
print()
print('Breadth : ',end='')
T.Breadth()