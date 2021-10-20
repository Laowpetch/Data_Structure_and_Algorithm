class LinkedList :
    class Node :
        def __init__(self,data) :
            self.data = data
            self.next = None

    def __init__(self):                
        self.head = None 
        self.size = 0
        
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
    def push(self,data):
        current = self.head
        new_node = self.Node(data)
        if current is None:
            self.head = new_node
            self.size += 1  
            return 
        if current.data > data:
            new_node.next = current
            self.head = new_node
            self.size += 1  
            return
        while(current.next != None):
            if current.data <= data and current.next.data >= data:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1  
       
    def __str__(self):
        str_ = ''
        current = self.head
        while current != None:
            str_ +=str(current.data)+' '
            current = current.next
        return 'Linked data : ' + str_
    def __len__(self):
        return self.size
    def __iter__(self):
        ref = self.head
        while ref is not None:
            yield ref.data
            ref = ref.next
def findMode(lst):
    set_ = {}    
    for i in lst:
        if i not in set_.keys():
            set_[i] = 1
        else:
            set_[i] += 1 
    Max = 0
    for i, j in set_.items():
        if j > Max:
            Max = j
    if Max <= 1:
        print('Mode is not available.')
    else:
        listMax = LinkedList()
        for i, j in set_.items():
            if j == Max:
                listMax.push(i)
        print( 'Mode =  ' + ' '.join([str(i) for i in listMax]))

inp_ = [int(i) for i in input('Enter numbers : ').split()]
ll = LinkedList()
for i in inp_:
    ll.push(i)
print('Output :')
print(ll)
print('Amount of data = '+ str(len(ll)) )
findMode(ll)