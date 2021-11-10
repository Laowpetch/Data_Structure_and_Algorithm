class Queue :
    def __init__(self) -> None:
        self.data = []

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
    
    def __str__(self):
        res = ''
        for i in self.data:
            res += i
        return res