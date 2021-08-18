def is_odd(n):
    return n%2 != 0
def has_odds(x):
    for i in x :
        if i % 2 != 0:
            return True
    return False
def all_odds(x):
    for i in x :
        if i % 2 == 0:
            return False
    return True
def no_odds(x):
    for i in x :
        if i % 2 == 1:
            return False
    return True
def get_odds(x):
    result = filter(lambda x: x % 2 == 1, x)
    return list(result)
def zip_odds(a,b):
    x = filter(lambda a: a % 2 == 1, a)
    x = list(x)
    lenx = len(x)
    y = filter(lambda b: b % 2 == 1, b)
    y = list(y)
    leny=len(y)
    i=0
    z=[]
    while i < leny or i < lenx:
        if i<lenx:
            z.append(x[i])
        if i<leny:
            z.append(y[i])
        i+=1
    return z
print(is_odd(31))
print(has_odds([0,2,3,4,8]))
print(all_odds([1,3,11,17]))
print(no_odds([2,4,8]))
print(get_odds([1,3,11,2,17]))
print(zip_odds([1,3,11,2,17],[2,4,97,99]))
print(zip_odds([2,4,97,99],[1,3,11,2,17]))