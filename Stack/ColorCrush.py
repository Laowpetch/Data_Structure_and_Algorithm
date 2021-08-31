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

inp = input('Enter Input : ').split()
S = Stack()

def checkCrush (inp):
    if len(inp) > 2:
        try: 
            for j in range(2,len(inp)):
                if inp[j-2] == inp[j-1] == inp[j]:
                    inp.pop(j-2)
                    inp.pop(j-2)
                    inp.pop(j-2)
                    global num
                    num += 1
                    checkCrush(inp)
            return inp
        except IndexError:
            return inp
    else:
        return inp
num = 0
inp = checkCrush(inp)

for i in range(0,len(inp)):
    S.push(inp[i])
print(S.size())
inp = ""
for i in range(0,S.size()):
    inp += str(S.pop())

if inp != "":
    print(inp)
else:
    print('Empty')

if num > 1 :
    print('Combo :',num,"! ! !")
