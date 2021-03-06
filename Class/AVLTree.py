class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL: 
    def __init__(self):
        self.root = None

    def insert(self, node, data):
	    if not node:
		    return Node(data)
	    elif data < node.data:
		    node.left = self.insert(node.left, data)
	    else:
		    node.right = self.insert(node.right, data)
	    node.height = 1 + max(self.getHeight(node.left),
						self.getHeight(node.right))
	    b = self.getBalance(node)
	    if b > 1 and data < node.left.data:
	    	return self.rightRotate(node)
	    if b < -1 and data > node.right.data:
	    	return self.leftRotate(node)
	    if b > 1 and data > node.left.data:
	    	node.left = self.leftRotate(node.left)
	    	return self.rightRotate(node)
	    if b < -1 and data < node.right.data:
	    	node.right = self.rightRotate(node.right)
	    	return self.leftRotate(node)
	    return node

    def leftRotate(self, z):
	    y = z.right
	    T2 = y.left
	    y.left = z
	    z.right = T2
	    z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
	    y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
	    return y

    def rightRotate(self, z):
	    y = z.left
	    T3 = y.right
	    y.right = z
	    z.left = T3
	    z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
	    y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))
	    return y

    def getHeight(self, root):
	    if not root:
	    	return 0
	    return root.height

    def getBalance(self, root):
	    if not root:
		    return 0
	    return self.getHeight(root.left) - self.getHeight(root.right)