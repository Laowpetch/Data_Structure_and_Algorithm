class Queue :
    def __init__(self) -> None:
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def enQueue(self, new_data):
        return self.data.append(new_data)

    def deQueue(self):
        if self.isEmpty():
            return 'Empty'
        return self.data.pop(0)

    def size(self):
        return len(self.data)
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty Queue'
        else:
            return 'Queue data : '+' '.join(str(i) for i in self.data)

ch = input('Enter choice : ')
ch = int(ch)
if ch == 1:
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print(q1)
elif ch == 2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.isEmpty())
elif ch == 3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())