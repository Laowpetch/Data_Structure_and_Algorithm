def NewRange(list_):
    ans = []
    if len(list_) == 1:
        for i in range(0,int(list_[0]),1):
            ans.append(float(i))
    elif len(list_) == 2:
        while list_[0] <= list_[1]:
            ans.append(list_[0])
            list_[0] += 1
    elif len(list_) == 3:
        while list_[0] <= list_[1]:
            ans.append(round(list_[0],3))
            list_[0] += list_[2]
    else:
        pass
    return tuple(ans)

print('*** New Range ***')
list_ = list(map(float,input("Enter Input : ").split()))
print(NewRange(list_))