class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def __str__(self):
        check = False
        s = ''
        p = self.head
        while p != None:
            if check == False and p.value != None:
                s += str(p.value)
                check = True
            elif p.value != None:
                s += ' ' + str(p.value)
            p = p.next
        return s

    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def delete(self, value):
        if self.search(value) is not True:
            return "Not in list"
        else:
            current = self.head
            while current is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next
    def reverse(self):
        current = self.head
        previous,next = None,None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous  

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def display(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value, end = ' ')
            current = current.next
        print()

L1 = LinkedList()
L2 = LinkedList()
x,y = input('Enter Input (L1,L2) : ').split()
x = x.split('->')
y = y.split('->')
for i in x :
    L1.insert(i)
for i in y:
    L2.insert(i)
L2.reverse()
print('L1    : ',end='')
for i in range(0,len(x)):
    print(x[i],end=' ')
print()
print('L2    : ',end='')
for i in range(0,len(y)):
    print(y[i],end=' ')
print()
print('Merge : ',end='')
print(L1,end='')
print(' ',end='')
print(L2,end='')