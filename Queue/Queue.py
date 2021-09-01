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
    
Q = Queue()
En = Queue()
str_ = input("Enter Input : ").split(',')
for i in range(0,len(str_)):
    list_ = []
    list_ = str_[i].split()
    if list_[0] == 'E':
        Q.enqueue(list_[1])
        for j in range(0,Q.size()):
            if j == Q.size()-1:
                print(Q.data[j],end='')
            else :
                print(str(Q.data[j]),end =', ')
    elif list_[0] == 'D':
            if Q.is_empty():
                print(Q.dequeue(),end ='')
            else:
                x = ''
                x = Q.dequeue()
                En.enqueue(x)
                print(str(x)+' <- ',end='')
                if Q.is_empty():
                    print(Q.dequeue(),end='')
                else:
                    for j in range(0,Q.size()):
                        if j == Q.size()-1:
                            print(Q.data[j],end='')
                        else :
                            print(str(Q.data[j]),end =', ')
    else:
        break
    print()
    
if En.is_empty():
    print(En.dequeue(),end='')
else:
    for i in range(0,En.size()):
        if i == 0:
            print(str(En.dequeue()),end='')
        else:
            print(', '+str(En.dequeue()),end='')
print(' : ',end='')
if Q.is_empty():
    print(str(Q.dequeue()))
else:
    for i in range(0,Q.size()):
        if i == 0:
            print(str(Q.dequeue()),end='')
        else:
            print(', '+str(Q.dequeue()),end ='')