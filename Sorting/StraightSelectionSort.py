def maxIndex(list_):
    temp = len(list_)-1
    if list_[temp] != max(list_) and temp-1 >= 0:
        return maxIndex(list_[:temp])
    else:
        return temp

def selection(list_, right=None):
    if right is None:
        right = len(list_)-1
    if right < 0:
        return list_
    max_ = maxIndex(list_[:right+1])
    if max_ != right:
        list_[right], list_[max_] = list_[max_], list_[right]
        print('swap',list_[max_],'<->',list_[right],':',list_)
    return selection(list_, right-1)

inp = list(map(int, input("Enter Input : ").split()))
ans = selection(inp)
print(ans)