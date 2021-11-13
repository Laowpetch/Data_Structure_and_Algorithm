class Node:
    def __init__(self, data, freq, left = None, right = None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def addSortedList(li,node):
    ans = []
    if len(li) == 0:
        ans.append(node)
    for i in range(len(li)):
        if li[i].freq < node.freq:
            ans += li[0:i] + [node] + li[i::]
            break
        if li[i].freq == node.freq:
            if li[i].data != '*' and node.data != '*':
                if ord(li[i].data) < ord(node.data):
                    ans += li[0:i] + [node] + li[i::]
                    break
            elif li[i].data == '*' and node.data == '*':
                ans += li[0:i] + [node] + li[i::]
                break
        if i == len(li)-1:
            ans = li + [node]
            break
    return ans

def huffman(node, binString=''):
    if node.data != '*':
        return {node.data: binString}
    d = dict()
    d.update(huffman(node.right, binString + '1'))
    d.update(huffman(node.left, binString + '0'))  
    return d

inp = input("Enter Input : ")
T = BST()
freq = {}
char = []
li = []
for i in inp:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    if i not in char:
        char.append(i)
while len(char) > 0:
    buffer = char.pop()
    li = addSortedList(li,Node(str(buffer),int(freq[buffer])))
while len(li) > 1:
    temp1 = li.pop()
    temp2 = li.pop()
    li = addSortedList(li,Node('*',temp1.freq+temp2.freq,temp1,temp2))
T.root = li.pop()
ans = huffman(T.root)
print(ans)
T.printTree(T.root)
print("Encoded! :",''.join(ans[e] for e in inp))