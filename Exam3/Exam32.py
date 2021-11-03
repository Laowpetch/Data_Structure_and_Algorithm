def Min(_list,min=None):
    _list = list(_list)
    if len(_list) == 0:
        return min
    elif min == None:
        min = _list.pop()
        return Min(_list,min)
    else:
        temp = _list.pop()
        if temp < min:
            min = temp
        return Min(_list,min)

inp = list(map(int, input('Enter Input : ').split()))
print('Min :',Min(inp))