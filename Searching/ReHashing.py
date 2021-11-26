def checkPrime(data):
    for i in range(2,data//2):
        if data % i == 0 :
            return False
    return True

def createTable(list_):
    size_ = len(list_) * 2
    while checkPrime(size_) == False:
        size_ += 1
    for i in range(size_-len(list_)):
        list_.append(None)
    return list_

def rehashing(list_):
    for i in range(len(list_)-1,-1,-1) :
        temp1 = list_[i]
        temp2 = temp1
        colNum = 0
        if list_[i] is not None and list_[temp1 % len(list_)] is None:
            temp1 = (temp2 % len(list_)+pow(colNum,2)) % len(list_)
        elif list_[i] is not None and list_[temp1 % len(list_)] is not None :
            if list_[(temp1+1) % len(list_)] is None and i != temp1 % len(list_):
                print('collision number', colNum + 1 ,'at',temp1 % len(list_))
                temp1 = (temp2 % len(list_)+pow(colNum + 1,2))%len(list_)          
        if list_[i] is not None and list_[temp1 % len(list_)] is None :
            list_[i],list_[temp1 % len(list_)] = list_[temp1 % len(list_)],list_[i]
    return list_

def insert_(list_,colNum,maxCol,num):
    k = num%len(list_)
    if list_[k] is None:
        list_[k] = num
        return list_
    else:
        while colNum < maxCol and list_[k] is not None:
            print('collision number', colNum + 1 ,'at',k)
            colNum+=1
            k = (num+pow(colNum,2))%len(list_)
            if colNum == maxCol :
                print('****** Max collision - Rehash !!! ******')
                list_ = createTable(list_)
                list_ = rehashing(list_)
                k = num % len(list_)
                colNum = 0
        list_[k] = num
        return list_

def printlist_(list_):
    for i in range(len(list_)):
        print('#'+str(i+1)+'	'+str(list_[i]))
    print('----------------------------------------')

print(' ***** Rehashing *****')
s = input('Enter Input : ').split('/')
sTable, maxCol, threshold = int(s[0].split()[0]),int(s[0].split()[1]),int(s[0].split()[2])
empt = 0
l = [None]*(sTable)
print('Initial Table :')
printlist_(l)
for i in [int(e) for e in s[1].split()]:
    colNum = 0
    k = i % len(l)
    print('Add :',i)
    empt += 1
    if empt/len(l)*100 >= threshold:
        print('****** Data over threshold - Rehash !!! ******')
        l = createTable(l)
        l = rehashing(l)
        insert_(l,colNum,maxCol,i)
    else:
        insert_(l,colNum,maxCol,i)
    printlist_(l)