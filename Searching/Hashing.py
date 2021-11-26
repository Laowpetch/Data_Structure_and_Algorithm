class Data:
    def __init__(self, key, data):
        self.key = key
        self.value = data
    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
class hash:
    def __init__(self,data,table):
        data = data.split()
        self.data = Data(data[0],data[1])
        temp = 0
        for i in data[0]:
            temp+=ord(i)
        self.id = temp%table
    def __str__(self):
        return str(self.data)
    
print(' ***** Fun with hashing *****')
s = input('Enter Input : ').split('/')
table ,maxCol ,empt = int(s[0].split()[0]),int(s[0].split()[1]),int(s[0].split()[0])
list_ = [None]*table
for i in s[1].split(','):
    hash_ = hash(i,table)
    id = hash_.id
    colNum = 1
    while list_[id] is not None and colNum <= maxCol:
        print('collision number',colNum,'at',id)
        id = (hash_.id+pow(colNum,2))%table
        colNum+=1
    if colNum-1 == maxCol:
        print('Max of collisionChain')
        for j in range(len(list_)):
            print('#'+str(j+1)+'\t'+str(list_[j]))
        print('---------------------------')
    if list_[id] is None and colNum <= maxCol :
        list_[id] = hash_
        empt-=1
        for j in range(len(list_)):
            print('#'+str(j+1)+'\t'+str(list_[j]))
        print('---------------------------')
    if empt == 0:
        print('This table is full !!!!!!')
        break