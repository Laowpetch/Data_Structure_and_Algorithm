def Search(_list,max=None):
    _list = list(_list)
    if len(_list) == 0:
        return max
    elif max == None:
        max = _list.pop()
        return Search(_list,max)
    else:
        temp = _list.pop()
        if temp > max:
            max = temp
        return Search(_list,max)

inp = list(map(int, input('Enter Input : ').split()))
print('Max :',Search(inp))