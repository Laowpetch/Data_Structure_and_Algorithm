class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None

    def __len__(self):
        now = self.head
        len = 0
        while now != None:
            len += 1
            now = now.next
        return len

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        now = self.head
        s = ''
        while now != None:
            s += str(now.data)
            if now.next != None:
                s += ' '
            now = now.next
        return s
    
    def isIn(self,data):
        now = self.head
        while now != None:
            if now == data:
                return True
            now = now.next
        return False

    def pushTail(self,data):
        curr = self.head
        n = self.Node(data)
        if curr is None:
            self.head = n
            return

        if curr.data > data:
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.data < data and curr.next.data > data:
                break
            curr = curr.next
        n.next = curr.next
        curr.next = n

    def contentEquivalence(self,other):
        check = 1
        buffer1 = self.head
        buffer2 = other.head
        while buffer1.next != None:
            if buffer1.data != buffer2.data or len(self) != len(other):
                check = 0
                break
            buffer1 = buffer1.next
            buffer2 = buffer2.next
        if buffer1.data != buffer2.data:
                check = 0
        if check == 1:
            return "True"
        return "False"
    

x,y = input('List1,List2 : ').split(',')
List1 = x.split()
List2 = y.split()
LL1 = LinkedList()
LL2 = LinkedList()
for i in List1:
    LL1.pushTail(i)
for i in List2:
    LL2.pushTail(i)
print('List1 content Equivalence List2 : ',end='')
print(LL1.contentEquivalence(LL2))