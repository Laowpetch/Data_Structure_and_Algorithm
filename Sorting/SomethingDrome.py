def lesstomore(inp):
    check = True
    for i in range(1,len(inp)):
        if not inp[i] >= inp[i-1]:
            check = False
    return check

def moretoless(inp):
    check = True
    for i in range(1,len(inp)):
        if not inp[i] <= inp[i-1]:
            check = False
    return check

def duplicate(inp):
    if len(set(inp)) == len(inp):
        return False
    else:
        return True
        
def samenumber(inp):
    check = True
    for i in range(1,len(inp)):
        if not inp[i] == inp[i-1]:
            check = False
    return check

inp = input('Enter Input : ')
inp = [int(i) for i in str(inp)]
ltm = lesstomore(inp)
mtl = moretoless(inp)
dup = duplicate(inp)
if samenumber(inp):
    print('Repdrome')
elif lesstomore(inp) and not duplicate(inp):
    print('Metadrome')
elif lesstomore(inp) and duplicate(inp):
    print('Plaindrome')
elif moretoless(inp) and not duplicate(inp):
    print('Katadrome')
elif moretoless(inp) and duplicate(inp):
    print('Nialpdrome')
else:
    print('Nondrome')