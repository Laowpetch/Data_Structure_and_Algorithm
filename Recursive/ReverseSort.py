def SearchMax(_list,max=None):
    _list = list(_list)
    if len(_list) == 0:
        return max
    elif max == None:
        max = _list.pop()
        return SearchMax(_list,max)
    else:
        temp = _list.pop()
        if temp > max:
            max = temp
        return SearchMax(_list,max)

def Sort(inp,ans,leng):
    inp = list(inp)
    ans = list(ans)
    leng = int(leng)
    if len(ans) < leng:
        temp = SearchMax(inp)
        ans.append(temp)
        inp.remove(temp)
        if len(ans) == leng:
            return ans
        else:
            return Sort(inp,ans,leng)
    else:
        return ans

_list = list(map(int, input('Enter your List : ').split(',')))
print('List after Sorted :',Sort(_list,[],len(_list)))