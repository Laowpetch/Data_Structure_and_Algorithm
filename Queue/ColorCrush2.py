class Queue :
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def enqueue(self, new_data):
        return self.data.append(new_data)

    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.data.pop(0)

    def size(self):
        return len(self.data)

class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

N = Stack()
M = Queue()
mPoint = 0
nPoint = 0
mItem = ''
mRun = False
nRun = False
Setback1 = False
Setback2 = False
First = True
insert = 2

n,m = input('Enter Input (Normal, Mirror) : ').split()
n = list(n)
m = list(m)
sizem = len(m)
sizen = len(n)

while mRun == True or First == True:
    for i in range(sizem-1,-1,-1): #Mirror Explosion
            try:
                if m[i] == m[i-1] == m[i-2]:
                    mItem += m[i]
                    m.pop(i-2)
                    m.pop(i-2)
                    m.pop(i-2)
                    mPoint += 1
                    sizem -= 3
                    Setback1 = True
                    mRun = True
                else:
                    pass
            except IndexError:
                pass
    if First == True:
        First = False
    if Setback1 == True:
        mRun = True
        Setback1 = False
    else:
        mRun = False

mItem = list(mItem)
while mItem != []:
    n.insert(insert,mItem[0])
    mItem.pop(0)
    insert += 4

First = True
while nRun == True or First == True:
    for i in range(2,sizen): #Normal Explosion
            try :
                if n[i] == n[i-1] == n[i-2]: 
                    n.pop(i-2)
                    n.pop(i-2)
                    n.pop(i-2)
                    nPoint += 1
                    sizen -= 3
                    nRun = True
                    Setback2 = True
                    break
                else:
                    pass
            except IndexError:
                pass
    if First == True:
        First = False
    if Setback2 == True:
        Setback2 = False
        nRun = True
    else:
        nRun = False

for i in range(0,len(m)):
    M.enqueue(m[i])
for i in range(0,len(n)):
    N.push(n[i])
print('NORMAL :')
print(len(n))
for i in range(0,N.size()):
    print(N.pop(),end='')
print()
print(str(nPoint)+' Explosive(s) ! ! ! (NORMAL)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(m))
if len(m) == 0:
    print('ytpmE')
else:
    for i in range(0,M.size()):
        print(M.dequeue(),end='')
    print()
print('(RORRIM) ! ! ! (s)evisolpxE '+str(mPoint))