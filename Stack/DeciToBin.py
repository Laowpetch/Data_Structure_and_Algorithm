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
        
def dec2bin(decnum):
    ans = ""
    s = Stack()
    decnum = int(decnum)
    while decnum > 0:
        mod = 0
        s.push(decnum % 2)
        mod = decnum % 2
        decnum -= mod
        decnum //= 2
    for i in range(0,s.size()):
        ans += str(s.pop())
    return ans

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))