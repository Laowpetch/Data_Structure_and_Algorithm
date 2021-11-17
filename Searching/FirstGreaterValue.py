def firstGreaterValue(list_, value_):
    list_ = sorted(list_)
    for i in list_:
        if i > value_:
            return i
    return 'No First Greater Value'

inp = input("Enter Input : ").split('/')
list_, value_ = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in value_:
    print(firstGreaterValue(list_, i))