import sys
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
class StackCalc():
    def __init__(self):
        self.s = Stack()
    def run(self,str_):
        self.str_ = str(str_)
        self.list_ = list(str_.split())
        for i in self.list_:
            if machine.RepresentsInt(i):
                self.s.push(int(i))
            elif i == 'DUP' or i == 'POP' or i == 'PSH':
                if i == 'DUP':
                    self.s.push(self.s.peek())
                elif i == 'POP':
                    self.s.pop()
                elif i == 'PSH':
                    pass
            elif i == '+' or i == '-'or i == '*' or i == '/':
                if i == '+':
                    self.s.push(self.s.pop() + self.s.pop())
                elif i == '-':
                    self.s.push(self.s.pop() - self.s.pop())
                elif i == '*':
                    self.s.push(self.s.pop() * self.s.pop())
                elif i == '/':
                    self.s.push(int(self.s.pop() / self.s.pop()))
            else:
                print('Invalid instruction: '+str(i))
                sys.exit()
                break
    def getValue(self):
        if self.s.size() == 0:
            return 0
        else :
            return self.s.pop()
    def RepresentsInt(self,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
        
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())