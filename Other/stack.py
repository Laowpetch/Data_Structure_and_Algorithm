class Stack:
    """class Stack
    default : empty stack / Stack([...})
    """
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
    def __str__(self):
        s = 'stack of'+str(self.size())+'items : '
        for ele in self.items:
            s += str(ele)+''
        return s

def match(open,close):
    return (open == '(' and close == ')') or (open == '[' and close == ']') or (open == '{' and close == '}')

def mathch2(ops,cl):
    opens = '([{'
    closes = ')]}'
    return opens.index(ops)==closes.index(cl)

def parenMacthing(str):
    s = Stack()
    i = 0
    error = 0
    while i < len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(),c):
                        error = 1
                else:
                    error = 2
        i+=1
    if s.size()>0:
        error = 3
    return error,c,i,s

str = '[{a+b+c}'
err,c,i,s = parenMacthing(str)
if err == 1:
    print(str,'unmatch open - close')
elif err == 2:
    print(str,'close paren excess')
elif err == 3:
    print(str,'open paren(s) excess ',s.size(),':',end="")
    for ele in s.items:
        print(ele,sep='',end="")
    print()
else:
    print(str,'MATCH')