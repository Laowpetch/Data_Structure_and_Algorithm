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
F = Queue()
S = Queue()
x = input('Enter people : ')
for i in x:
    Q.enqueue(i)
Start = False
i = 1
j = 1
while not Q.is_empty():
    if F.size() < 5:
        F.enqueue(Q.dequeue())
    elif S.size() < 5:
        S.enqueue(Q.dequeue())
        Start = True
    else:
        pass
    print(str(i)+" "+str(Q)+" "+str(F)+" "+str(S))
    if j%2 == 0 and not S.is_empty():
        S.dequeue()
    if i%3 == 0 and not F.is_empty():
        F.dequeue()
    i+=1
    if Start == True:
        j+=1