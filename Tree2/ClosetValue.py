class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            buffer = self.root
            while buffer is not None:
                if value < buffer.value:
                    if buffer.left is None:
                        buffer.left = Node(value)
                        break
                    else:
                        buffer = buffer.left
                else:
                    if buffer.right is None:
                        buffer.right = Node(value)
                        break
                    else:
                        buffer = buffer.right

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def closestValue(self, value):
        if self.root is not None:
            diff = 999999999999
            return_ = -1
            q = Queue()
            q.enqueue(self.root)
            while not q.is_empty():
                buffer = q.dequeue()
                if value == buffer.value:
                    return_ = buffer.value
                    break
                else:
                    if abs(value-buffer.value) < diff:
                        diff = abs(value-buffer.value)
                        return_ = buffer.value
                if buffer.left is not None:
                    q.enqueue(buffer.left)
                if buffer.right is not None:
                    q.enqueue(buffer.right)
            return return_




inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
tree = BST()
comp = int(inp[1])
for item in lst:
    tree.insert(item)
    tree.print_tree(tree.root)
    print('--------------------------------------------------')
print('Closest value of',comp,":",str(tree.closestValue(comp)))