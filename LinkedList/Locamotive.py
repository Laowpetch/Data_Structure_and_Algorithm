class LinkedList:
    class Node :
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):
        check = False
        s = ''
        p = self.head
        while p != None :
            if check == False:
                s += str(p.data)
                check = True
            else:
                s += ' <- ' + str(p.data)
            p = p.next
        return s
          
    def __len__(self) :
        return self.size
            
    def isEmpty(self) :
        return self.size == 0
        
    def indexOf(self,data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
            
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(-1,i) :
            p = p.next
        return p
    
    def append(self,data):
        if self.head == None :
          self.head = self.Node(data,None)
        else :
          self.insertAfter(len(self),data)
    
    def insertAfter(self,i,data) :
        p = self.nodeAt(i-1)
        p.next = self.Node(data,p.next)
        self.size += 1
    
    def deleteAfter(self,i) :
        p = self.nodeAt(i)
        p.next = p.next.next
        self.size -= 1
    
    def removeData(self,data) :
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)

S = LinkedList()
N = LinkedList()
print(' *** Locomotive ***')
x = list(input('Enter Input : ').split())

for i in x :
    S.append(i)

print('Before :',S)

zero = False

for i in x:
    if i == '0' or zero == True:
        N.append(i)
        zero = True

for i in x:
    if i == '0':
        break
    N.append(i)

print('After :',N)