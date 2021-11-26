def packing(list_, num):
    temp = 1
    pack = num
    for i in range(len(list_)):
        if pack >= list_[i]:
            pack -= list_[i]
        else:
            temp += 1
            pack = num - list_[i]
    return temp

inp = input('Enter Input : ').split('/')
list_,k = list(map(int,inp[0].split())),int(inp[1])
min_ = max(list_)
while packing(list_,min_) != k:
    min_+=1
print('Minimum weigth for',k,'box(es) =',min_)